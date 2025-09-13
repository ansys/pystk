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

"""Enables Tkinter integration."""

__all__ = ["GlobeControl", "MapControl", "GfxAnalysisControl"]

import os
import pathlib
from tkinter import Frame

if os.name == "nt":
    from ctypes import CDLL, POINTER, WinDLL, WinError, c_char_p, cdll, create_unicode_buffer, get_last_error
else:
    from ctypes import CDLL, POINTER, cdll

from ..internal.comutil import BOOL, CHAR, DWORD, INT, LONG, LPCWSTR, LPVOID, WINFUNCTYPE, IUnknown
from ..stkengine import STKEngine
from ..stkx import Graphics2DControlBase, Graphics3DControlBase, GraphicsAnalysisControlBase

if os.name != "nt":
    from ctypes.util import find_library

class NativeContainerMethods:
    """Provide support for STK Engine controls (map, globe, graphics analysis)."""
    def __init__(self):
        self.jniCore = CDLL(self._get_jni_core_path())
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
    def _get_jni_core_path(self):
        if not STKEngine._is_engine_running:
            raise RuntimeError("STKEngine.StartApplication() must be called before using the STK Engine controls")

        if os.name != "nt":
            return "libagjnicore.so"
        else:
            kernel32 = WinDLL("kernel32", use_last_error=True)

            kernel32.GetModuleHandleW.restype = LPVOID
            kernel32.GetModuleHandleW.argtypes = [LPCWSTR]

            stkx_module_handle = kernel32.GetModuleHandleW("stkx.dll")
            if stkx_module_handle is None:
                raise RuntimeError(f"Error getting stkx.dll module handle ({WinError(get_last_error())})")

            kernel32.GetModuleFileNameA.restype = DWORD
            kernel32.GetModuleFileNameA.argtypes = [LPVOID, c_char_p, DWORD]

            c_path = create_unicode_buffer(1024)
            res = kernel32.GetModuleFileNameW(LPVOID(stkx_module_handle), c_path, DWORD(1024))
            if res == 0:
                err = get_last_error()
                errormsg = "Failed to get STKX module file name"
                if err != 0:
                    errormsg += f" ({WinError(err)})"
                raise RuntimeError(errormsg)
            stkx_dll_path = pathlib.Path(c_path.value).resolve()

            jni_core_dll_path = stkx_dll_path.parent / "AgJNICore.dll"
            return str(jni_core_dll_path)
    def create_container(self, progid):
        return self.AgPythonCreateContainer(LPVOID(None), LPVOID(None), LPCWSTR(progid))
    def attach_container(self, container, winid, display):
        self.Java_agi_core_awt_AgAwtNativeContainer_AttachContainer(LPVOID(None), LPVOID(None), winid, display, LPVOID(container))
    def resize_container(self, container, x, y, width, height):
        self.Java_agi_core_awt_AgAwtNativeContainer_ResizeContainer(LPVOID(None), LPVOID(None), LPVOID(container), INT(x), INT(y), INT(width), INT(height))
    def get_unknown(self, container):
        return self.AgPythonGetIAgUnknown(LPVOID(None), LPVOID(None), LPVOID(container))
    def detach_container(self, container):
        self.Java_agi_core_awt_AgAwtNativeContainer_DetachContainer(LPVOID(None), LPVOID(None), LPVOID(container))
    def release_container(self, container):
        self.Java_agi_core_awt_AgAwtNativeContainer_ReleaseContainer(LPVOID(None), LPVOID(None), LPVOID(container))
    if os.name!="nt":
        def paint(self, container):
            self.Java_agi_core_awt_AgAwtNativeContainer_Paint(LPVOID(None), LPVOID(None), LPVOID(container))
        def mouse_pressed(self, container, x, y, left_button_down, middle_button_down, right_button_down, ctrl_key_down, alt_key_down, shift_key_down):
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseAdapter_MousePressed(LPVOID(None), LPVOID(None), LPVOID(container), INT(x), INT(y), BOOL(left_button_down), BOOL(middle_button_down), BOOL(right_button_down), BOOL(ctrl_key_down), BOOL(alt_key_down), BOOL(shift_key_down))
        def mouse_released(self, container, x, y, left_button_down, middle_button_down, right_button_down, ctrl_key_down, alt_key_down, shift_key_down):
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseAdapter_MouseReleased(LPVOID(None), LPVOID(None), LPVOID(container), INT(x), INT(y), BOOL(left_button_down), BOOL(middle_button_down), BOOL(right_button_down), BOOL(ctrl_key_down), BOOL(alt_key_down), BOOL(shift_key_down))
        def mouse_moved(self, container, x, y, left_button_down, middle_button_down, right_button_down, ctrl_key_down, alt_key_down, shift_key_down):
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseMotionAdapter_MouseMoved(LPVOID(None), LPVOID(None), LPVOID(container), INT(x), INT(y), BOOL(left_button_down), BOOL(middle_button_down), BOOL(right_button_down), BOOL(ctrl_key_down), BOOL(alt_key_down), BOOL(shift_key_down))
        def mouse_wheel_moved(self, container, x, y, ticks, left_button_down, middle_button_down, right_button_down, ctrl_key_down, alt_key_down, shift_key_down):
            self.Java_agi_core_awt_AgAwtNativeContainer_00024AgAwtCanvasMouseWheelAdapter_MouseWheelMoved(LPVOID(None), LPVOID(None), LPVOID(container), INT(x), INT(y), INT(ticks), BOOL(left_button_down), BOOL(middle_button_down), BOOL(right_button_down), BOOL(ctrl_key_down), BOOL(alt_key_down), BOOL(shift_key_down))
        def key_pressed(self, container, key_code, ctrl_key_down, alt_key_down, shift_key_down):
            self.AgPythonKeyPressed(LPVOID(None), LPVOID(None), LPVOID(container), INT(key_code), BOOL(ctrl_key_down), BOOL(alt_key_down), BOOL(shift_key_down))
        def key_released(self, container, key_code, ctrl_key_down, alt_key_down, shift_key_down):
            self.AgPythonKeyReleased(LPVOID(None), LPVOID(None), LPVOID(container), INT(key_code), BOOL(ctrl_key_down), BOOL(alt_key_down), BOOL(shift_key_down))

class ControlBase(Frame):
    """Base class for Tkinter controls."""

    _shift = 0x0001
    _control = 0x0004
    _lalt = 0x0008
    _ralt = 0x0080
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

        self._container = self._nativeContainerMethods.create_container(self._progid)
        self._unk = self._nativeContainerMethods.get_unknown(self._container)

        _cntrlinit_unk = IUnknown()
        _cntrlinit_unk.p = LPVOID(self._unk)

        self._interface._private_init(self, _cntrlinit_unk)

        self.bind("<Configure>", self._configure)
        if os.name!="nt":
            self.bind("<Expose>", self._expose)
            self.bind("<ButtonPress>", self._button_press)
            self.bind("<ButtonRelease>", self._button_release)
            self.bind("<Motion>", self._motion)
            self.bind_all("<Any-KeyPress>", self._key_press)
            self.bind_all("<Any-KeyRelease>", self._key_release)

    def __setattr__(self, attrname, value):
        try:
            self._interface.__setattr__(self, attrname, value)
        except AttributeError:
            Frame.__setattr__(self, attrname, value)

    def _configure(self, event):
        """Occurs when the frame is resized."""
        if not self._is_container_attached:
            self._xDisplay = None if os.name=="nt" else self._XOpenDisplay(self.winfo_screen().encode("utf-8"))
            self._nativeContainerMethods.attach_container(self._container, self.winfo_id(), self._xDisplay)
            self._is_container_attached = True
        self._nativeContainerMethods.resize_container(self._container, 0, 0, event.width, event.height)

    def destroy(self):
        """Occurs before the frame is destroyed."""
        self._nativeContainerMethods.detach_container(self._container)
        self._nativeContainerMethods.release_container(self._container)
        super().destroy()

    if os.name!="nt":
        def _expose(self, event):
            """Occurs when at least some part of the frame becomes visible after having been covered up by another window."""
            if self._is_container_attached:
                self._nativeContainerMethods.paint(self._container)

        def _button_press(self, event):
            """Occurs when a mouse button is pressed."""
            if event.num == 4:
                if not(event.state & self._mouse1 or event.state & self._mouse2 or event.state & self._mouse3):
                    self._nativeContainerMethods.mouse_wheel_moved(self._container, event.x, event.y, 1, event.num == 1, event.num == 2, event.num == 3, event.state & self._control, event.state & self._lalt or event.state & self._ralt , event.state & self._shift)
            elif event.num == 5:
                if not(event.state & self._mouse1 or event.state & self._mouse2 or event.state & self._mouse3):
                    self._nativeContainerMethods.mouse_wheel_moved(self._container, event.x, event.y, -1, event.num == 1, event.num == 2, event.num == 3, event.state & self._control, event.state & self._lalt or event.state & self._ralt , event.state & self._shift)
            else:
                if not(event.state & self._mouse1 or event.state & self._mouse2 or event.state & self._mouse3):
                    self._nativeContainerMethods.mouse_pressed(self._container, event.x, event.y, event.num == 1, event.num == 2, event.num == 3, event.state & self._control, event.state & self._lalt or event.state & self._ralt , event.state & self._shift)

        def _button_release(self, event):
            """Occurs when a mouse button is released."""
            self._nativeContainerMethods.mouse_released(self._container, event.x, event.y, event.num == 1, event.num == 2, event.num == 3, event.state & self._control, event.state & self._lalt or event.state & self._ralt , event.state & self._shift)

        def _motion(self, event):
            """Occurs when mouse motion occurs."""
            self._nativeContainerMethods.mouse_moved(self._container, event.x, event.y, event.state & self._mouse1, event.state & self._mouse2, event.state & self._mouse3, event.state & self._control, event.state & self._lalt or event.state & self._ralt , event.state & self._shift)

        def _key_press(self, event):
            """Occurs when a key is pressed."""
            self._nativeContainerMethods.key_pressed(self._container, event.keysym_num, event.state & self._control, event.state & self._lalt or event.state & self._ralt , event.state & self._shift)

        def _key_release(self, event):
            """Occurs when key is released."""
            self._nativeContainerMethods.key_released(self._container, event.keysym_num, event.state & self._control, event.state & self._lalt or event.state & self._ralt , event.state & self._shift)

class GlobeControl(Graphics3DControlBase, ControlBase):
    """The 3D Globe control for Tkinter."""

    _progid = "STKX13.VOControl.1"
    _interface = Graphics3DControlBase

    def __init__(self, parent, *args, **kwargs):
        """Construct an object of type GlobeControl."""
        Graphics3DControlBase.__init__(self)
        ControlBase.__init__(self, parent, *args, **kwargs)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        ControlBase.__setattr__(self, attrname, value)

class MapControl(Graphics2DControlBase, ControlBase):
    """The 2D Map control for Tkinter."""

    _progid = "STKX13.2DControl.1"
    _interface = Graphics2DControlBase

    def __init__(self, parent, *args, **kwargs):
        """Construct an object of type MapControl."""
        Graphics2DControlBase.__init__(self)
        ControlBase.__init__(self, parent, *args, **kwargs)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        ControlBase.__setattr__(self, attrname, value)

class GfxAnalysisControl(GraphicsAnalysisControlBase, ControlBase):
    """The Graphics Analysis control for Tkinter."""

    _progid = "STKX13.GfxAnalysisControl.1"
    _interface = GraphicsAnalysisControlBase

    def __init__(self, parent, *args, **kwargs):
        """Construct an object of type GfxAnalysisControl."""
        GraphicsAnalysisControlBase.__init__(self)
        ControlBase.__init__(self, parent, *args, **kwargs)

    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        ControlBase.__setattr__(self, attrname, value)