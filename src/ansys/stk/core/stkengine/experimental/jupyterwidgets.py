################################################################################
#          Copyright 2022-2022, Ansys Government Initiatives
################################################################################

"""Map and globe widgets for Jupyter Notebooks using Remote Frame Buffer."""

# Dependencies: jupyter_rfb, pillow, imageio, simplejpeg, ipycanvas

__all__ = ['GlobeWidget', 'MapWidget', 'GfxAnalysisWidget']

import asyncio
import numpy as np
import os
import time

from jupyter_rfb import RemoteFrameBuffer
from ctypes import byref, CFUNCTYPE, cdll, c_size_t, c_int, c_void_p, \
    addressof, Structure, cast, pointer

from ...stkx import UiAxGraphics3DCntrl, UiAx2DCntrl, \
    UiAxGraphics2DAnalysisCntrl, BUTTON_VALUES, SHIFT_VALUES
from ...internal.stkxrfb import IRemoteFrameBuffer, IRemoteFrameBufferHost
from ...internal.comutil import OLE32Lib, \
    IUnknown, Succeeded, LPVOID, CLSCTX_INPROC_SERVER, \
    GUID, PVOID, REFIID, POINTER, HRESULT, ULONG, S_OK, E_NOINTERFACE
from ...stkobjects import StkObjectRoot
from ...utilities.exceptions import STKAttributeError

TIMERPROC = CFUNCTYPE(None, c_size_t)
INSTALLTIMER = CFUNCTYPE(c_size_t, c_int, TIMERPROC, c_void_p)
DELETETIMER = CFUNCTYPE(c_int, c_size_t, c_void_p)


class AsyncioTimerManager(object):

    class TimerInfo(object):
        def __init__(self, id, milliseconds, TIMERPROC, callbackData):
            """Construct an object of type TimerInfo."""
            self.id = id
            self.interval = milliseconds/1000
            self.callback = TIMERPROC
            self.callback_data = callbackData
            self._reset()

        def _reset(self):
            self.next_proc = time.perf_counter() + self.interval

        def fire(self):
            if time.perf_counter() >= self.next_proc:
                self.callback(self.id)
                self._reset()

    def __init__(self):
        """Construct an object of type AsyncioTimerManager."""
        if os.name != 'nt':
            agutillib = cdll.LoadLibrary("libagutil.so")
        else:
            agutillib = cdll.LoadLibrary("AgUtil.dll")

        functype = CFUNCTYPE(None, INSTALLTIMER, DELETETIMER, c_void_p)
        AgUtSetTimerCallbacks = functype(
                ("AgUtSetTimerCallbacks", agutillib),
                (
                    (1, "pInstallTimer"),
                    (1, "pDeleteTimer"),
                    (1, "pCallbackData")
                )
        )

        self._next_id = 1
        self._timers = dict()
        self._install_timer_cfunc = INSTALLTIMER(self.__install_timer)
        self._delete_timer_cfunc = DELETETIMER(self.__delete_timer)
        AgUtSetTimerCallbacks(
            self._install_timer_cfunc,
            self._delete_timer_cfunc, c_void_p())

    def terminate(self):
        self._timers.clear()

    def __install_timer(self, milliseconds, TIMERPROC, callbackData):
        id = self._next_id
        self._next_id = id + 1
        self._timers[id] = AsyncioTimerManager.TimerInfo(
            id, milliseconds, TIMERPROC, callbackData)
        self._set_alarm_for_next_timer_proc()
        return id

    def __delete_timer(self, timerID, callbackData):
        if timerID in self._timers:
            del(self._timers[timerID])
        return 0

    def _fire_timers(self):
        timers = self._timers.copy()
        for timerid in timers:
            timers[timerid].fire()
        self._set_alarm_for_next_timer_proc()

    async def _wait(self, delay):
        await asyncio.sleep(delay)
        self._fire_timers()

    def _next_timer_proc(self):
        """Return time in sec until next timer proc."""
        tempTimers = self._timers.copy()
        if len(tempTimers) == 0:
            return 0.050
        else:
            proc_times = list()
            for timerid in tempTimers:
                proc_times.append(tempTimers[timerid].next_proc)
            delta_s = min(proc_times) - time.perf_counter()
            if delta_s > 0:
                return delta_s
            else:
                return 0

    def _set_alarm_for_next_timer_proc(self):
        next_proc = self._next_timer_proc()
        if next_proc > 0:
            self.task = asyncio.ensure_future(self._wait(next_proc))
        else:
            self._fire_timers()


asyncioTimerManager = None


class RemoteFrameBufferHostVTable(Structure):
    """Structure of the vtable for IRemoteFrameBufferHost."""
    
    _fields_ = [("IUnknown1",        c_void_p),
                ("IUnknown2",        c_void_p),
                ("IUnknown3",        c_void_p),
                ("refresh",          c_void_p)]


class RemoteFrameBufferHost(object):
    """
    Implements IRemoteFrameBufferHost.
    
    Assemble a vtable following the layout of that interface
    """
    
    _IID_IUnknown = GUID(IUnknown._guid)
    _IID_IAgRemoteFrameBufferHost = GUID('{D229A605-D3A8-4476-B628-AC549C674B58}')

    def __init__(self, owner):
        """Construct an object of type RemoteFrameBufferHost."""
        self.owner = owner
        self._init_vtable()

    def _init_vtable(self):

        qi = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
        addref = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
        release = CFUNCTYPE(ULONG, PVOID)(self._release)

        if os.name == "nt":
            self.__dict__['_cfunc_IUnknown1'] = qi
            self.__dict__['_cfunc_IUnknown2'] = addref
            self.__dict__['_cfunc_IUnknown3'] = release
        else:
            self.__dict__['_cfunc_IUnknown3'] = qi
            self.__dict__['_cfunc_IUnknown1'] = addref
            self.__dict__['_cfunc_IUnknown2'] = release

        self.__dict__['_cfunc_Refresh'] = CFUNCTYPE(None, PVOID)(self._refresh)

        self.__dict__['_vtable'] = RemoteFrameBufferHostVTable(
            *[cast(self._cfunc_IUnknown1, c_void_p),
              cast(self._cfunc_IUnknown2, c_void_p),
              cast(self._cfunc_IUnknown3, c_void_p),
              cast(self._cfunc_Refresh, c_void_p)]
        )
        self.__dict__['_pUnk'] = pointer(self._vtable)

    def _add_ref(self, pThis: PVOID) -> int:
        return 1

    def _release(self, pThis: PVOID) -> int:
        return 0

    def _query_interface(self,
                        pThis: PVOID,
                        riid: REFIID,
                        ppvObject: POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == RemoteFrameBufferHost._IID_IUnknown:
            ppvObject[0] = addressof(self._pUnk)
            return S_OK
        elif iid == RemoteFrameBufferHost._IID_IAgRemoteFrameBufferHost:
            ppvObject[0] = addressof(self._pUnk)
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _refresh(self, pThis: PVOID) -> None:
        self.owner.request_draw()


class WidgetBase(RemoteFrameBuffer):
    """Base class for Jupyter controls."""
    
    _shift = 0x0001
    _control = 0x0004
    _lAlt = 0x0008
    _rAlt = 0x0080
    _mouse1 = 0x0100
    _mouse2 = 0x0200
    _mouse3 = 0x0400

    def __init__(self,
                 root: StkObjectRoot,
                 w: int = 800,
                 h: int = 600,
                 title: str = None,
                 resizable: bool = True):
        """Construct an object of type WidgetBase."""
        super().__init__()

        self.frame = None

        self.css_width = f"{w}px"
        self.css_height = f"{h}px"

        self.resizable = resizable
        self.pixel_ratio = 1.0

        self._unk = self.__create_instance(self._progid)

        self._interface._private_init(self, self._unk)

        self.__create_frame_buffer(w, h)

        self._rfb = IRemoteFrameBuffer(self)
        self._rfb.set_to_off_screen_rendering(w, h)

        self._rfbHostImpl = RemoteFrameBufferHost(self)

        self._rfbHostImplUnk = IUnknown()
        self._rfbHostImplUnk.p = addressof(self._rfbHostImpl._pUnk)

        self._rfbHost = IRemoteFrameBufferHost()
        self._rfbHost._private_init(self._rfbHostImplUnk)

        self._rfb.set_host(self._rfbHost)

        self.mouse_callbacks = [
            [
                self._rfb.notify_l_button_down,
                self._rfb.notify_r_button_down,
                self._rfb.notify_m_button_down
            ],
            [
                self._rfb.notify_l_button_up,
                self._rfb.notify_r_button_up,
                self._rfb.notify_m_button_up
            ]
        ]

        global asyncioTimerManager
        if asyncioTimerManager is None:
            asyncioTimerManager = AsyncioTimerManager()

        self.root = root
        self.title = title or self.root.current_scenario.instance_name
        self.camera = self.root.current_scenario.scene_manager.scenes.item(0).camera

    def __del__(self):
        del self._rfb
        del self._rfbHostImpl
        del self._rfbHost
        del self._unk
        self.root = None

    def __create_frame_buffer(self, w: int, h: int):
        if self.frame is not None:
            del self.frame
        self.frame = np.ones((int(h), int(w), 3), np.uint8)
        self.pointer, read_only_flag = self.frame.__array_interface__['data']

    def __create_instance(self, clsid: str) -> LPVOID:
        guid = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString(clsid, guid)):
            IID_IUnknown = GUID(IUnknown._guid)
            unk = IUnknown()
            if Succeeded(OLE32Lib.CoCreateInstance(byref(guid), None,
                                          CLSCTX_INPROC_SERVER,
                                          byref(IID_IUnknown), byref(unk.p))):
                unk.take_ownership()
                return unk
        return None

    def __setattr__(self, attrname, value):
        try:
            self._interface.__setattr__(self, attrname, value)
        except STKAttributeError:
            RemoteFrameBuffer.__setattr__(self, attrname, value)

    def __get_modifiers(self, event):
        modifiers = event['modifiers']
        result = 0
        if "Shift" in modifiers:
            result = result | SHIFT_VALUES.PRESSED
        if "Ctrl" in modifiers:
            result = result | SHIFT_VALUES.CTRL_PRESSED
        if "Alt" in modifiers:
            result = result | SHIFT_VALUES.ALTITUDE_PRESSED
        return result

    def __get_position(self, event):
        x = int(event["x"] * self.pixel_ratio)
        y = int(event["y"] * self.pixel_ratio)
        return (x, y)

    def handle_event(self, event):

        event_type = event.get("event_type", None)
        if event_type == "resize":
            pixel_ratio = event["pixel_ratio"]
            w = int(event["width"]*pixel_ratio)
            h = int(event["height"]*pixel_ratio)
            self.pixel_ratio = pixel_ratio
            self.__create_frame_buffer(w, h)
            self._rfb.notify_resize(0, 0, w, h)
        elif event_type == "pointer_down":
            (x, y) = self.__get_position(event)
            self.mouse_callbacks[0][event["button"]-1](
                x, y, self.__get_modifiers(event))
        elif event_type == "pointer_up" and event["button"] == 1:
            (x, y) = self.__get_position(event)
            self.mouse_callbacks[1][event["button"]-1](
                x, y, self.__get_modifiers(event))
        elif event_type == "pointer_move":
            (x, y) = self.__get_position(event)
            buttons = event["buttons"]
            if len(buttons) > 0 and buttons[0] == 1:
                self._rfb.notify_mouse_move(x, y, BUTTON_VALUES.LEFT_PRESSED,
                                          self.__get_modifiers(event))
            elif len(buttons) > 0 and buttons[0] == 2:
                self._rfb.notify_mouse_move(x, y, BUTTON_VALUES.RIGHT_PRESSED,
                                          self.__get_modifiers(event))
            elif len(buttons) > 0 and buttons[0] == 3:
                self._rfb.notify_mouse_move(x, y, BUTTON_VALUES.MIDDLE_PRESSED,
                                          self.__get_modifiers(event))
            else:
                self._rfb.notify_mouse_move(x, y, 0, 0)
        elif event_type == "wheel":
            (x, y) = self.__get_position(event)
            dy = int(event["dy"] * self.pixel_ratio/100)
            self._rfb.notify_mouse_wheel(x, y, -dy, self.__get_modifiers(event))

    def set_title(self, title):
        self.title = title

    def get_frame(self):
        self._rfb.snap_to_rbg_raster(self.pointer)
        return self.frame
    
    def animate(self, time_step):        
        self.root.current_scenario.animation.anim_step_value = time_step
        self.root.execute_command("Animate * Start Loop")
        self.show()

    def show(self, in_sidecar=False, **snapshot_kwargs):
        needs_snapshot = os.environ.get("BUILD_EXAMPLES", "false") == "true"
        canvas = self.snapshot(**snapshot_kwargs) if needs_snapshot else self
        if in_sidecar:
            from sidecar import Sidecar
            with Sidecar(title=self.title):
                display(canvas)
        else:
            return canvas


class GlobeWidget(UiAxGraphics3DCntrl, WidgetBase):
    """The 3D Globe widget for jupyter."""

    # Example:
    #   from ansys.stk.core.stkengine import *
    #   from ansys.stk.core.stkengine.jupyterwidgets import GlobeWidget

    #   stk = STKEngine.StartApplication(noGraphics=False)
    #   root = stk.NewObjectRoot()
    #   g = GlobeWidget(root, 600, 400)
    #   root.NewScenario("RemoteFrameBuffer")
    #   root.ExecuteCommand('Animate * Start Loop')
    #   g

    _progid = "STKX12.VOControl.1"
    _interface = UiAxGraphics3DCntrl

    def __init__(self, root: StkObjectRoot, w: int, h: int, title: str = None):
        """Construct an object of type GlobeWidget."""
        WidgetBase.__init__(self, root, w, h, title)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        WidgetBase.__setattr__(self, attrname, value)


class MapWidget(UiAx2DCntrl, WidgetBase):
    """The 2D Map widget for jupyter."""
    
    _progid = "STKX12.2DControl.1"
    _interface = UiAx2DCntrl

    def __init__(self, root: StkObjectRoot, w: int, h: int, title: str = None):
        """Construct an object of type MapWidget."""
        WidgetBase.__init__(self, root, w, h, title)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        WidgetBase.__setattr__(self, attrname, value)


class GfxAnalysisWidget(UiAxGraphics2DAnalysisCntrl, WidgetBase):
    """The Graphics Analysis widget for jupyter."""
    
    _progid = "STKX12.GfxAnalysisControl.1"
    _interface = UiAxGraphics2DAnalysisCntrl

    def __init__(self, root: StkObjectRoot, w: int, h: int, title: str = None):
        """Construct an object of type GfxAnalysisWidget."""
        WidgetBase.__init__(self, root, w, h, title)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        WidgetBase.__setattr__(self, attrname, value)