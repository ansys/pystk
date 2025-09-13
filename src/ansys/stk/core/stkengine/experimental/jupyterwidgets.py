# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Map and globe widgets for Jupyter Notebooks using Remote Frame Buffer."""

# Dependencies: jupyter_rfb, pillow, imageio, simplejpeg, ipycanvas

__all__ = ['GlobeWidget', 'MapWidget', 'GfxAnalysisWidget']

import asyncio
from ctypes import CFUNCTYPE, Structure, addressof, byref, c_int, c_size_t, c_void_p, cast, cdll, pointer
import os
import time

from IPython.display import display
from jupyter_rfb import RemoteFrameBuffer
from jupyter_rfb._png import array2png
import numpy as np

from ...internal.comutil import (
    CLSCTX_INPROC_SERVER,
    E_NOINTERFACE,
    GUID,
    HRESULT,
    LPVOID,
    POINTER,
    PVOID,
    REFIID,
    S_OK,
    ULONG,
    IUnknown,
    OLE32Lib,
    Succeeded,
)
from ...internal.stkxrfb import IRemoteFrameBuffer, IRemoteFrameBufferHost
from ...stkobjects import IAnimation, Scenario, STKObjectRoot
from ...stkx import ButtonValues, Graphics2DControlBase, Graphics3DControlBase, GraphicsAnalysisControlBase, ShiftValues

TIMERPROC = CFUNCTYPE(None, c_size_t)
INSTALLTIMER = CFUNCTYPE(c_size_t, c_int, TIMERPROC, c_void_p)
DELETETIMER = CFUNCTYPE(c_int, c_size_t, c_void_p)


class AsyncioTimerManager(object):
    """Provide timer support for animation in jupyter notebooks."""
    class TimerInfo(object):
        def __init__(self, id, milliseconds, timer_proc, callback_data):
            """Construct an object of type TimerInfo."""
            self.id = id
            self.interval = milliseconds/1000
            self.callback = timer_proc
            self.callback_data = callback_data
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
        set_timer_callbacks = functype(
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
        set_timer_callbacks(
            self._install_timer_cfunc,
            self._delete_timer_cfunc, c_void_p())

    def terminate(self):
        self._timers.clear()

    def __install_timer(self, milliseconds, timer_proc, callback_data):
        id = self._next_id
        self._next_id = id + 1
        self._timers[id] = AsyncioTimerManager.TimerInfo(
            id, milliseconds, timer_proc, callback_data)
        self._set_alarm_for_next_timer_proc()
        return id

    def __delete_timer(self, timer_id, callback_data):
        if timer_id in self._timers:
            del(self._timers[timer_id])
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
        temp_timers = self._timers.copy()
        if len(temp_timers) == 0:
            return 0.050
        else:
            proc_times = list()
            for timerid in temp_timers:
                proc_times.append(temp_timers[timerid].next_proc)
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


asyncio_timer_manager = None


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
    _iid_unknown = GUID(IUnknown._guid)
    _iid_iagremoteframebufferhost = GUID('{86B3E7CB-6B45-43D4-88B1-2939FBF1E956}')

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
        self.__dict__['_unknown'] = pointer(self._vtable)

    def _add_ref(self, this: PVOID) -> int:
        return 1

    def _release(self, this: PVOID) -> int:
        return 0

    def _query_interface(self,
                        this: PVOID,
                        riid: REFIID,
                        object: POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == RemoteFrameBufferHost._iid_unknown:
            object[0] = addressof(self._unknown)
            return S_OK
        elif iid == RemoteFrameBufferHost._iid_iagremoteframebufferhost:
            object[0] = addressof(self._unknown)
            return S_OK
        else:
            object[0] = 0
            return E_NOINTERFACE

    def _refresh(self, this: PVOID) -> None:
        self.owner.request_draw()


class WidgetBase(RemoteFrameBuffer):
    """Base class for Jupyter controls."""
    _shift = 0x0001
    _control = 0x0004
    _lalt = 0x0008
    _ralt = 0x0080
    _mouse1 = 0x0100
    _mouse2 = 0x0200
    _mouse3 = 0x0400

    def __init__(self,
                 root: STKObjectRoot,
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
        self._rfb.set_to_offscreen_rendering(w, h)

        self._rfbHostImpl = RemoteFrameBufferHost(self)

        self._rfbHostImplUnk = IUnknown()
        self._rfbHostImplUnk.p.value = addressof(self._rfbHostImpl._unknown)

        self._rfbHost = IRemoteFrameBufferHost()
        self._rfbHost._private_init(self._rfbHostImplUnk)

        self._rfb.set_host(self._rfbHost)

        self._building_examples = os.getenv("BUILD_EXAMPLES", "false") == "true"

        self.mouse_callbacks = [
            [
                self._rfb.notify_left_button_down,
                self._rfb.notify_right_button_down,
                self._rfb.notify_middle_button_down
            ],
            [
                self._rfb.notify_left_button_up,
                self._rfb.notify_right_button_up,
                self._rfb.notify_middle_button_up
            ]
        ]

        global asyncio_timer_manager
        if asyncio_timer_manager is None:
            asyncio_timer_manager = AsyncioTimerManager()

        self.root = root
        if self.root.current_scenario is not None:
            self.title = title or self.root.current_scenario.instance_name
            scenario: Scenario = Scenario(self.root.current_scenario)
            if scenario.scene_manager.scenes.count > 0:
                self.camera = scenario.scene_manager.scenes.item(0).camera

    def __del__(self):
        del self._rfb
        del self._rfbHostImpl
        del self._rfbHost
        del self._unk
        self.root = None
        self.camera = None

    def __create_frame_buffer(self, w: int, h: int):
        if self.frame is not None:
            del self.frame
        self.frame = np.ones((int(h), int(w), 3), np.uint8)
        self.pointer, read_only_flag = self.frame.__array_interface__['data']

    def __create_instance(self, clsid: str) -> LPVOID:
        guid = GUID()
        if Succeeded(OLE32Lib.CLSIDFromString(clsid, guid)):
            iid_iunknown = GUID(IUnknown._guid)
            unk = IUnknown()
            if Succeeded(OLE32Lib.CoCreateInstance(byref(guid), None,
                                          CLSCTX_INPROC_SERVER,
                                          byref(iid_iunknown), byref(unk.p))):
                unk.take_ownership()
                return unk
        return None

    def __setattr__(self, attrname, value):
        try:
            self._interface.__setattr__(self, attrname, value)
        except AttributeError:
            RemoteFrameBuffer.__setattr__(self, attrname, value)

    def __get_modifiers(self, event):
        modifiers = event['modifiers']
        result = 0
        if "Shift" in modifiers:
            result = result | ShiftValues.PRESSED
        if "Ctrl" in modifiers:
            result = result | ShiftValues.CTRL_PRESSED
        if "Alt" in modifiers:
            result = result | ShiftValues.ALT_PRESSED
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
                self._rfb.notify_mouse_move(x, y, ButtonValues.LEFT_PRESSED,
                                          self.__get_modifiers(event))
            elif len(buttons) > 0 and buttons[0] == 2:
                self._rfb.notify_mouse_move(x, y, ButtonValues.RIGHT_PRESSED,
                                          self.__get_modifiers(event))
            elif len(buttons) > 0 and buttons[0] == 3:
                self._rfb.notify_mouse_move(x, y, ButtonValues.MIDDLE_PRESSED,
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
        scenario: Scenario = Scenario(self.root.current_scenario)
        scenario.animation_settings.animation_step_value = time_step
        animation_control: IAnimation = IAnimation(self.root)
        animation_control.play_forward()
        self.show()

    def _repr_mimebundle_(self, **kwargs):
        """Return the desired MIME type representation.

        The MIME type representation is a dictionary relating MIME types to
        the data that should be rendered in that format.

        The main goal of this function is to provide the right type of data when
        renedring different types of documents, including HTML, Notebooks, and
        PDF files.

        """
        if not self._building_examples:
            data = super()._repr_mimebundle_(**kwargs)
        else:
            data = {
                "image/png": array2png(self.snapshot().data)
            }
        return data

    def show(self, in_sidecar=False, **snapshot_kwargs):
        if in_sidecar:
            from sidecar import Sidecar
            with Sidecar(title=self.title):
                display(self)
        else:
            return self

    def snapshot(self, pixel_ratio=None, _initial=False):
        if self._building_examples:
            # There is currently no good way to detect when terrain and
            # imagery fetched in background threads are finished loading,
            # so when building the documentation to capture snapshots,
            # just use an arbitrary delay for now and fetch a few frames
            # before taking the snapshot
            for _ in range(0, 4):
                _ = self.get_frame()
                time.sleep(0.5)
        return super().snapshot(pixel_ratio, _initial)

class GlobeWidget(Graphics3DControlBase, WidgetBase):
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

    _progid = "STKX13.VOControl.1"
    _interface = Graphics3DControlBase

    def __init__(self, root: STKObjectRoot, w: int, h: int, title: str = None):
        """Construct an object of type GlobeWidget."""
        WidgetBase.__init__(self, root, w, h, title)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        WidgetBase.__setattr__(self, attrname, value)


class MapWidget(Graphics2DControlBase, WidgetBase):
    """The 2D Map widget for jupyter."""
    _progid = "STKX13.2DControl.1"
    _interface = Graphics2DControlBase

    def __init__(self, root: STKObjectRoot, w: int, h: int, title: str = None):
        """Construct an object of type MapWidget."""
        WidgetBase.__init__(self, root, w, h, title)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        WidgetBase.__setattr__(self, attrname, value)


class GfxAnalysisWidget(GraphicsAnalysisControlBase, WidgetBase):
    """The Graphics Analysis widget for jupyter."""
    _progid = "STKX13.GfxAnalysisControl.1"
    _interface = GraphicsAnalysisControlBase

    def __init__(self, root: STKObjectRoot, w: int, h: int, title: str = None):
        """Construct an object of type GfxAnalysisWidget."""
        WidgetBase.__init__(self, root, w, h, title)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        WidgetBase.__setattr__(self, attrname, value)
