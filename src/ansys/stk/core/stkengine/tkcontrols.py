################################################################################
#          Copyright 2021-2021, Ansys Government Initiatives
################################################################################

__all__ = ["GlobeControl", "MapControl", "GfxAnalysisControl"]

import os
from tkinter                    import Frame
from ctypes                     import *

from ..stkx             import UiAxGraphics3DCntrl, UiAx2DCntrl, UiAxGraphics2DAnalysisCntrl
from ..internal.comutil import IUnknown, INT, LONG, CHAR, LPVOID, LPCWSTR, DWORD, BOOL, WINFUNCTYPE
from ..stkengine        import *

if os.name != "nt":
    from ctypes.util import find_library

class NativeContainerMethods:
    def __init__(self):
        self.jniCore = CDLL(self._getJNICorePath())
        self.AgPythonCreateContainer                                         = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPCWSTR)(("AgPythonCreateContainer", self.jniCore), ((1, "env"), (1, "_this"), (1, "progId")))
        self.Java_agi_core_awt_AgAwtNativeContainer_AttachContainer          = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID, LPVOID, LPVOID)(("Java_agi_core_awt_AgAwtNativeContainer_AttachContainer", self.jniCore), ((1, "env"), (1, "_this"), (1, "pNativeCanvas"), (1, "pNativeDisplay"), (1, "pContainer")))
        self.Java_agi_core_awt_AgAwtNativeContainer_ResizeContainer          = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID, LONG, LONG, LONG, LONG)(("Java_agi_core_awt_AgAwtNativeContainer_ResizeContainer", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer"), (1, "x"), (1, "y"), (1, "width"), (1, "height")))
        self.AgPythonGetIAgUnknown                                           = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID)(("AgPythonGetIAgUnknown", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer")))
        self.Java_agi_core_awt_AgAwtNativeContainer_DetachContainer          = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID)(("Java_agi_core_awt_AgAwtNativeContainer_DetachContainer", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer")))
        self.Java_agi_core_awt_AgAwtNativeContainer_ReleaseContainer         = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID)(("Java_agi_core_awt_AgAwtNativeContainer_ReleaseContainer", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer")))
        if os.name!="nt":
            self.Java_agi_core_awt_AgAwtNativeContainer_Paint                                               = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID)(("Java_agi_core_awt_AgAwtNativeContainer_Paint", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer")))
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseAdapter_MousePressed           = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID, LONG, LONG, BOOL, BOOL, BOOL, BOOL, BOOL, BOOL)(("Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseAdapter_MousePressed", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer"), (1, "x"), (1, "y"), (1, "leftButtonDown"), (1, "middleButtonDown"), (1, "rightButtonDown"), (1, "ctrlKeyDown"), (1, "altKeyDown"), (1, "shiftKeyDown")))
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseAdapter_MouseReleased          = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID, LONG, LONG, BOOL, BOOL, BOOL, BOOL, BOOL, BOOL)(("Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseAdapter_MouseReleased", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer"), (1, "x"), (1, "y"), (1, "leftButtonDown"), (1, "middleButtonDown"), (1, "rightButtonDown"), (1, "ctrlKeyDown"), (1, "altKeyDown"), (1, "shiftKeyDown")))
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseMotionAdapter_MouseMoved       = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID, LONG, LONG, BOOL, BOOL, BOOL, BOOL, BOOL, BOOL)(("Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseMotionAdapter_MouseMoved", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer"), (1, "x"), (1, "y"), (1, "leftButtonDown"), (1, "middleButtonDown"), (1, "rightButtonDown"), (1, "ctrlKeyDown"), (1, "altKeyDown"), (1, "shiftKeyDown")))
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseWheelAdapter_MouseWheelMoved   = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID, LONG, LONG, LONG, BOOL, BOOL, BOOL, BOOL, BOOL, BOOL)(("Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseWheelAdapter_MouseWheelMoved", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer"), (1, "x"), (1, "y"), (1, "ticks"), (1, "leftButtonDown"), (1, "middleButtonDown"), (1, "rightButtonDown"), (1, "ctrlKeyDown"), (1, "altKeyDown"), (1, "shiftKeyDown")))
            self.AgPythonKeyPressed                                                                         = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID, LONG, BOOL, BOOL, BOOL)(("AgPythonKeyPressed", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer"), (1, "keyCode"), (1, "ctrlKeyDown"), (1, "altKeyDown"), (1, "shiftKeyDown")))
            self.AgPythonKeyReleased                                                                        = WINFUNCTYPE(LPVOID, LPVOID, LPVOID, LPVOID, LONG, BOOL, BOOL, BOOL)(("AgPythonKeyReleased", self.jniCore), ((1, "env"), (1, "_this"), (1, "pContainer"), (1, "keyCode"), (1, "ctrlKeyDown"), (1, "altKeyDown"), (1, "shiftKeyDown")))
    def _getJNICorePath(self):
        if not STKEngine._is_engine_running:
            raise STKRuntimeError(f"STKEngine.StartApplication() must be called before using the STK Engine controls")
            
        if os.name != "nt":
            return "libagjnicore.so"
        else:
            kernel32 = WinDLL("kernel32", use_last_error=True)

            kernel32.GetModuleHandleW.restype = LPVOID
            kernel32.GetModuleHandleW.argtypes = [LPCWSTR]

            stkxModuleHandle = kernel32.GetModuleHandleW("stkx.dll")
            if stkxModuleHandle is None:
                raise STKRuntimeError(f"Error getting stkx.dll module handle ({WinError(get_last_error())})")

            kernel32.GetModuleFileNameA.restype = DWORD
            kernel32.GetModuleFileNameA.argtypes = [LPVOID, c_char_p, DWORD]

            cPath = create_unicode_buffer(1024)
            res = kernel32.GetModuleFileNameW(LPVOID(stkxModuleHandle), cPath, DWORD(1024))
            if res == 0:
                err = get_last_error()
                errormsg = "Failed to get STKX module file name"
                if err != 0:
                    errormsg += f" ({WinError(err)})"
                raise STKRuntimeError(errormsg)
            stkxdllpath = cPath.value

            jniCoreDllPath = os.path.join(os.path.dirname(stkxdllpath), "AgJNICore.dll")
            return jniCoreDllPath
    def CreateContainer(self, progid):
        return self.AgPythonCreateContainer(LPVOID(None), LPVOID(None), LPCWSTR(progid))
    def AttachContainer(self, pContainer, winid, display):
        self.Java_agi_core_awt_AgAwtNativeContainer_AttachContainer(LPVOID(None), LPVOID(None), winid, display, LPVOID(pContainer))
    def ResizeContainer(self, pContainer, x, y, width, height):
        self.Java_agi_core_awt_AgAwtNativeContainer_ResizeContainer(LPVOID(None), LPVOID(None), LPVOID(pContainer), INT(x), INT(y), INT(width), INT(height))
    def GetIAgUnknown(self, pContainer):
        return self.AgPythonGetIAgUnknown(LPVOID(None), LPVOID(None), LPVOID(pContainer))
    def DetachContainer(self, pContainer):
        self.Java_agi_core_awt_AgAwtNativeContainer_DetachContainer(LPVOID(None), LPVOID(None), LPVOID(pContainer))
    def ReleaseContainer(self, pContainer):
        self.Java_agi_core_awt_AgAwtNativeContainer_ReleaseContainer(LPVOID(None), LPVOID(None), LPVOID(pContainer))
    if os.name!="nt":
        def Paint(self, pContainer):
            self.Java_agi_core_awt_AgAwtNativeContainer_Paint(LPVOID(None), LPVOID(None), LPVOID(pContainer))
        def MousePressed(self, pContainer, x, y, leftButtonDown, middleButtonDown, rightButtonDown, ctrlKeyDown, altKeyDown, shiftKeyDown):
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseAdapter_MousePressed(LPVOID(None), LPVOID(None), LPVOID(pContainer), INT(x), INT(y), BOOL(leftButtonDown), BOOL(middleButtonDown), BOOL(rightButtonDown), BOOL(ctrlKeyDown), BOOL(altKeyDown), BOOL(shiftKeyDown))
        def MouseReleased(self, pContainer, x, y, leftButtonDown, middleButtonDown, rightButtonDown, ctrlKeyDown, altKeyDown, shiftKeyDown):
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseAdapter_MouseReleased(LPVOID(None), LPVOID(None), LPVOID(pContainer), INT(x), INT(y), BOOL(leftButtonDown), BOOL(middleButtonDown), BOOL(rightButtonDown), BOOL(ctrlKeyDown), BOOL(altKeyDown), BOOL(shiftKeyDown))
        def MouseMoved(self, pContainer, x, y, leftButtonDown, middleButtonDown, rightButtonDown, ctrlKeyDown, altKeyDown, shiftKeyDown):
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseMotionAdapter_MouseMoved(LPVOID(None), LPVOID(None), LPVOID(pContainer), INT(x), INT(y), BOOL(leftButtonDown), BOOL(middleButtonDown), BOOL(rightButtonDown), BOOL(ctrlKeyDown), BOOL(altKeyDown), BOOL(shiftKeyDown))
        def MouseWheelMoved(self, pContainer, x, y, ticks, leftButtonDown, middleButtonDown, rightButtonDown, ctrlKeyDown, altKeyDown, shiftKeyDown):
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseWheelAdapter_MouseWheelMoved(LPVOID(None), LPVOID(None), LPVOID(pContainer), INT(x), INT(y), INT(ticks), BOOL(leftButtonDown), BOOL(middleButtonDown), BOOL(rightButtonDown), BOOL(ctrlKeyDown), BOOL(altKeyDown), BOOL(shiftKeyDown))
        def KeyPressed(self, pContainer, keyCode, ctrlKeyDown, altKeyDown, shiftKeyDown):
            self.AgPythonKeyPressed(LPVOID(None), LPVOID(None), LPVOID(pContainer), INT(keyCode), BOOL(ctrlKeyDown), BOOL(altKeyDown), BOOL(shiftKeyDown))
        def KeyReleased(self, pContainer, keyCode, ctrlKeyDown, altKeyDown, shiftKeyDown):
            self.AgPythonKeyReleased(LPVOID(None), LPVOID(None), LPVOID(pContainer), INT(keyCode), BOOL(ctrlKeyDown), BOOL(altKeyDown), BOOL(shiftKeyDown))
        
class ControlBase(Frame):
    """Base class for Tkinter controls."""
    
    _shift = 0x0001
    _control = 0x0004
    _lAlt = 0x0008
    _rAlt = 0x0080
    _mouse1 = 0x0100
    _mouse2 = 0x0200
    _mouse3 = 0x0400

    def __init__(self, parent, *args, **kwargs):
        # Set background to empty string to prevent tk from drawing background over opengl draws
        kwargs["bg"] = ""
        Frame.__init__(self, parent, *args, **kwargs)
        self._is_container_attached = False
        self._nativeContainerMethods = NativeContainerMethods()
        if os.name!="nt":
            self._x11lib = cdll.LoadLibrary(find_library("X11"))
            self._XOpenDisplay = WINFUNCTYPE(POINTER(CHAR))(("XOpenDisplay", self._x11lib))
        
        self._container = self._nativeContainerMethods.CreateContainer(self._progid)
        self._unk = self._nativeContainerMethods.GetIAgUnknown(self._container)
        
        _cntrlinit_unk = IUnknown()
        _cntrlinit_unk.p = LPVOID(self._unk)
        
        self._interface._private_init(self, _cntrlinit_unk)
        
        self.bind("<Configure>", self._Configure)
        if os.name!="nt":
            self.bind("<Expose>", self._Expose)
            self.bind("<ButtonPress>", self._ButtonPress)
            self.bind("<ButtonRelease>", self._ButtonRelease)
            self.bind("<Motion>", self._Motion)
            self.bind_all("<Any-KeyPress>", self._KeyPress)
            self.bind_all("<Any-KeyRelease>", self._KeyRelease)
        
    def __setattr__(self, attrname, value):
        try:
            self._interface.__setattr__(self, attrname, value)
        except:
            Frame.__setattr__(self, attrname, value)
        
    def _Configure(self, event):
        """Occurs when the frame is resized."""
        if not self._is_container_attached:
            self._xDisplay = None if os.name=="nt" else self._XOpenDisplay(self.winfo_screen().encode("utf-8"))
            self._nativeContainerMethods.AttachContainer(self._container, self.winfo_id(), self._xDisplay)
            self._is_container_attached = True
        self._nativeContainerMethods.ResizeContainer(self._container, 0, 0, event.width, event.height)
            
    def destroy(self):
        """Occurs before the frame is destroyed."""
        self._nativeContainerMethods.DetachContainer(self._container)
        self._nativeContainerMethods.ReleaseContainer(self._container)
        super().destroy()

    if os.name!="nt":
        def _Expose(self, event):
            """Occurs when at least some part of the frame becomes visible after having been covered up by another window."""
            if self._is_container_attached:
                self._nativeContainerMethods.Paint(self._container)
            
        def _ButtonPress(self, event):
            """Occurs when a mouse button is pressed."""
            if event.num == 4:
                if not(event.state & self._mouse1 or event.state & self._mouse2 or event.state & self._mouse3):
                    self._nativeContainerMethods.MouseWheelMoved(self._container, event.x, event.y, 1, event.num == 1, event.num == 2, event.num == 3, event.state & self._control, event.state & self._lAlt or event.state & self._rAlt , event.state & self._shift)
            elif event.num == 5:
                if not(event.state & self._mouse1 or event.state & self._mouse2 or event.state & self._mouse3):
                    self._nativeContainerMethods.MouseWheelMoved(self._container, event.x, event.y, -1, event.num == 1, event.num == 2, event.num == 3, event.state & self._control, event.state & self._lAlt or event.state & self._rAlt , event.state & self._shift)
            else:
                if not(event.state & self._mouse1 or event.state & self._mouse2 or event.state & self._mouse3):
                    self._nativeContainerMethods.MousePressed(self._container, event.x, event.y, event.num == 1, event.num == 2, event.num == 3, event.state & self._control, event.state & self._lAlt or event.state & self._rAlt , event.state & self._shift)

        def _ButtonRelease(self, event):
            """Occurs when a mouse button is released."""
            self._nativeContainerMethods.MouseReleased(self._container, event.x, event.y, event.num == 1, event.num == 2, event.num == 3, event.state & self._control, event.state & self._lAlt or event.state & self._rAlt , event.state & self._shift)

        def _Motion(self, event):
            """Occurs when mouse motion occurs."""
            self._nativeContainerMethods.MouseMoved(self._container, event.x, event.y, event.state & self._mouse1, event.state & self._mouse2, event.state & self._mouse3, event.state & self._control, event.state & self._lAlt or event.state & self._rAlt , event.state & self._shift)

        def _KeyPress(self, event):
            """Occurs when a key is pressed."""
            self._nativeContainerMethods.KeyPressed(self._container, event.keysym_num, event.state & self._control, event.state & self._lAlt or event.state & self._rAlt , event.state & self._shift)

        def _KeyRelease(self, event):
            """Occurs when key is released."""
            self._nativeContainerMethods.KeyReleased(self._container, event.keysym_num, event.state & self._control, event.state & self._lAlt or event.state & self._rAlt , event.state & self._shift)

class GlobeControl(UiAxGraphics3DCntrl, ControlBase):
    """The 3D Globe control for Tkinter."""

    _progid = "STKX12.VOControl.1"
    _interface = UiAxGraphics3DCntrl

    def __init__(self, parent, *args, **kwargs):
        ControlBase.__init__(self, parent, *args, **kwargs)
        
    def __setattr__(self, attrname, value):
        ControlBase.__setattr__(self, attrname, value)

class MapControl(UiAx2DCntrl, ControlBase):
    """The 2D Map control for Tkinter."""

    _progid = "STKX12.2DControl.1"
    _interface = UiAx2DCntrl

    def __init__(self, parent, *args, **kwargs):
        ControlBase.__init__(self, parent, *args, **kwargs)
        
    def __setattr__(self, attrname, value):
        ControlBase.__setattr__(self, attrname, value)

class GfxAnalysisControl(UiAxGraphics2DAnalysisCntrl, ControlBase):
    """The Graphics Analysis control for Tkinter."""

    _progid = "STKX12.GfxAnalysisControl.1"
    _interface = UiAxGraphics2DAnalysisCntrl

    def __init__(self, parent, *args, **kwargs):
        ControlBase.__init__(self, parent, *args, **kwargs)
        
    def __setattr__(self, attrname, value):
        ControlBase.__setattr__(self, attrname, value)