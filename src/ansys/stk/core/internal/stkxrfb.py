################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["IRemoteFrameBuffer", "IRemoteFrameBufferHost"]



try:
    from numpy import ndarray 
except ModuleNotFoundError:
    pass
    
try:
    from pandas import DataFrame 
except ModuleNotFoundError:
    pass

from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal.comutil     import IUnknown, IAGFUNCTYPE
from ..internal.eventutil   import *
from ..utilities.exceptions import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class IRemoteFrameBufferHost(object):
    """Called by engine to request operations from the host using the remote frame buffer."""
    _uuid = "{D229A605-D3A8-4476-B628-AC549C674B58}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_refresh"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IRemoteFrameBufferHost._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IRemoteFrameBufferHost from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IRemoteFrameBufferHost = agcom.GUID(IRemoteFrameBufferHost._uuid)
        vtable_offset_local = IRemoteFrameBufferHost._vtable_offset - 1
        self.__dict__["_refresh"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBufferHost, vtable_offset_local+1, )
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IRemoteFrameBufferHost.__dict__ and type(IRemoteFrameBufferHost.__dict__[attrname]) == property:
            return IRemoteFrameBufferHost.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IRemoteFrameBufferHost.")
    
    def refresh(self) -> None:
        """A new frame is ready to be displayed."""
        agcls.evaluate_hresult(self.__dict__["_refresh"]())


agcls.AgClassCatalog.add_catalog_entry("{D229A605-D3A8-4476-B628-AC549C674B58}", IRemoteFrameBufferHost)
agcls.AgTypeNameMap["IRemoteFrameBufferHost"] = IRemoteFrameBufferHost

class IRemoteFrameBuffer(object):
    """Expose the control as a remote frame buffer."""
    _uuid = "{35869E18-8BA8-4259-B64B-E1CD612AD4A4}"
    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_snap_to_rbg_raster"] = _raise_uninitialized_error
        self.__dict__["_set_to_off_screen_rendering"] = _raise_uninitialized_error
        self.__dict__["_render_to_direct_x_texture"] = _raise_uninitialized_error
        self.__dict__["_set_to_direct_x_rendering"] = _raise_uninitialized_error
        self.__dict__["_update_direct_x_rendering_texture"] = _raise_uninitialized_error
        self.__dict__["_notify_resize"] = _raise_uninitialized_error
        self.__dict__["_notify_l_button_up"] = _raise_uninitialized_error
        self.__dict__["_notify_r_button_up"] = _raise_uninitialized_error
        self.__dict__["_notify_m_button_up"] = _raise_uninitialized_error
        self.__dict__["_notify_l_button_down"] = _raise_uninitialized_error
        self.__dict__["_notify_r_button_down"] = _raise_uninitialized_error
        self.__dict__["_notify_m_button_down"] = _raise_uninitialized_error
        self.__dict__["_notify_mouse_move"] = _raise_uninitialized_error
        self.__dict__["_notify_mouse_wheel"] = _raise_uninitialized_error
        self.__dict__["_set_host"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IRemoteFrameBuffer._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IRemoteFrameBuffer from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IRemoteFrameBuffer = agcom.GUID(IRemoteFrameBuffer._uuid)
        vtable_offset_local = IRemoteFrameBuffer._vtable_offset - 1
        self.__dict__["_snap_to_rbg_raster"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+1, agcom.PVOID)
        self.__dict__["_set_to_off_screen_rendering"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+2, agcom.INT, agcom.INT)
        self.__dict__["_render_to_direct_x_texture"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+3, )
        self.__dict__["_set_to_direct_x_rendering"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+4, agcom.INT, agcom.INT, agcom.PVOID, agcom.PVOID, agcom.PVOID, agcom.PVOID)
        self.__dict__["_update_direct_x_rendering_texture"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+5, agcom.PVOID, agcom.PVOID)
        self.__dict__["_notify_resize"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+6, agcom.INT, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_notify_l_button_up"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+7, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_notify_r_button_up"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+8, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_notify_m_button_up"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+9, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_notify_l_button_down"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+10, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_notify_r_button_down"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+11, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_notify_m_button_down"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+12, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_notify_mouse_move"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+13, agcom.INT, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_notify_mouse_wheel"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+14, agcom.INT, agcom.INT, agcom.INT, agcom.INT)
        self.__dict__["_set_host"] = IAGFUNCTYPE(pUnk, IID_IRemoteFrameBuffer, vtable_offset_local+15, agcom.PVOID)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IRemoteFrameBuffer.__dict__ and type(IRemoteFrameBuffer.__dict__[attrname]) == property:
            return IRemoteFrameBuffer.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IRemoteFrameBuffer.")
    
    def snap_to_rbg_raster(self, rbgRasterPtr:agcom.PVOID) -> None:
        """Captures the current scene to a raster."""
        with agmarshall.PVOID_arg(rbgRasterPtr) as arg_rbgRasterPtr:
            agcls.evaluate_hresult(self.__dict__["_snap_to_rbg_raster"](arg_rbgRasterPtr.COM_val))

    def set_to_off_screen_rendering(self, initialWidth:int, initialHeight:int) -> None:
        """Switch to offscreen rendering."""
        with agmarshall.INT_arg(initialWidth) as arg_initialWidth, \
             agmarshall.INT_arg(initialHeight) as arg_initialHeight:
            agcls.evaluate_hresult(self.__dict__["_set_to_off_screen_rendering"](arg_initialWidth.COM_val, arg_initialHeight.COM_val))

    def render_to_direct_x_texture(self) -> None:
        """Render to the DirectX texture configured by SetToDirectXRendering()."""
        agcls.evaluate_hresult(self.__dict__["_render_to_direct_x_texture"]())

    def set_to_direct_x_rendering(self, initialWidth:int, initialHeight:int, hwnd:agcom.PVOID, directXDevice:agcom.PVOID, directXTexture:agcom.PVOID, directXSharedHandle:agcom.PVOID) -> None:
        """Switch to rendering to the specified Dirext X texture."""
        with agmarshall.INT_arg(initialWidth) as arg_initialWidth, \
             agmarshall.INT_arg(initialHeight) as arg_initialHeight, \
             agmarshall.PVOID_arg(hwnd) as arg_hwnd, \
             agmarshall.PVOID_arg(directXDevice) as arg_directXDevice, \
             agmarshall.PVOID_arg(directXTexture) as arg_directXTexture, \
             agmarshall.PVOID_arg(directXSharedHandle) as arg_directXSharedHandle:
            agcls.evaluate_hresult(self.__dict__["_set_to_direct_x_rendering"](arg_initialWidth.COM_val, arg_initialHeight.COM_val, arg_hwnd.COM_val, arg_directXDevice.COM_val, arg_directXTexture.COM_val, arg_directXSharedHandle.COM_val))

    def update_direct_x_rendering_texture(self, directXTexture:agcom.PVOID, directXSharedHandle:agcom.PVOID) -> None:
        """Update Dirext X texture (for instance after a resize)."""
        with agmarshall.PVOID_arg(directXTexture) as arg_directXTexture, \
             agmarshall.PVOID_arg(directXSharedHandle) as arg_directXSharedHandle:
            agcls.evaluate_hresult(self.__dict__["_update_direct_x_rendering_texture"](arg_directXTexture.COM_val, arg_directXSharedHandle.COM_val))

    def notify_resize(self, left:int, top:int, width:int, height:int) -> None:
        """Notifies that a resize event occured."""
        with agmarshall.INT_arg(left) as arg_left, \
             agmarshall.INT_arg(top) as arg_top, \
             agmarshall.INT_arg(width) as arg_width, \
             agmarshall.INT_arg(height) as arg_height:
            agcls.evaluate_hresult(self.__dict__["_notify_resize"](arg_left.COM_val, arg_top.COM_val, arg_width.COM_val, arg_height.COM_val))

    def notify_l_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse left button up event occured."""
        with agmarshall.INT_arg(x) as arg_x, \
             agmarshall.INT_arg(y) as arg_y, \
             agmarshall.INT_arg(keyState) as arg_keyState:
            agcls.evaluate_hresult(self.__dict__["_notify_l_button_up"](arg_x.COM_val, arg_y.COM_val, arg_keyState.COM_val))

    def notify_r_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse right button up event occured."""
        with agmarshall.INT_arg(x) as arg_x, \
             agmarshall.INT_arg(y) as arg_y, \
             agmarshall.INT_arg(keyState) as arg_keyState:
            agcls.evaluate_hresult(self.__dict__["_notify_r_button_up"](arg_x.COM_val, arg_y.COM_val, arg_keyState.COM_val))

    def notify_m_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse middle button up event occured."""
        with agmarshall.INT_arg(x) as arg_x, \
             agmarshall.INT_arg(y) as arg_y, \
             agmarshall.INT_arg(keyState) as arg_keyState:
            agcls.evaluate_hresult(self.__dict__["_notify_m_button_up"](arg_x.COM_val, arg_y.COM_val, arg_keyState.COM_val))

    def notify_l_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse left button down event occured."""
        with agmarshall.INT_arg(x) as arg_x, \
             agmarshall.INT_arg(y) as arg_y, \
             agmarshall.INT_arg(keyState) as arg_keyState:
            agcls.evaluate_hresult(self.__dict__["_notify_l_button_down"](arg_x.COM_val, arg_y.COM_val, arg_keyState.COM_val))

    def notify_r_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse right button down event occured."""
        with agmarshall.INT_arg(x) as arg_x, \
             agmarshall.INT_arg(y) as arg_y, \
             agmarshall.INT_arg(keyState) as arg_keyState:
            agcls.evaluate_hresult(self.__dict__["_notify_r_button_down"](arg_x.COM_val, arg_y.COM_val, arg_keyState.COM_val))

    def notify_m_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse middle button down event occured."""
        with agmarshall.INT_arg(x) as arg_x, \
             agmarshall.INT_arg(y) as arg_y, \
             agmarshall.INT_arg(keyState) as arg_keyState:
            agcls.evaluate_hresult(self.__dict__["_notify_m_button_down"](arg_x.COM_val, arg_y.COM_val, arg_keyState.COM_val))

    def notify_mouse_move(self, x:int, y:int, buttons:int, keyState:int) -> None:
        """Called by the client on a mouse move event."""
        with agmarshall.INT_arg(x) as arg_x, \
             agmarshall.INT_arg(y) as arg_y, \
             agmarshall.INT_arg(buttons) as arg_buttons, \
             agmarshall.INT_arg(keyState) as arg_keyState:
            agcls.evaluate_hresult(self.__dict__["_notify_mouse_move"](arg_x.COM_val, arg_y.COM_val, arg_buttons.COM_val, arg_keyState.COM_val))

    def notify_mouse_wheel(self, x:int, y:int, steps:int, keyState:int) -> None:
        """Called by the client on a mouse wheel event."""
        with agmarshall.INT_arg(x) as arg_x, \
             agmarshall.INT_arg(y) as arg_y, \
             agmarshall.INT_arg(steps) as arg_steps, \
             agmarshall.INT_arg(keyState) as arg_keyState:
            agcls.evaluate_hresult(self.__dict__["_notify_mouse_wheel"](arg_x.COM_val, arg_y.COM_val, arg_steps.COM_val, arg_keyState.COM_val))

    def set_host(self, pHost:"IRemoteFrameBufferHost") -> None:
        """Sets the host using this remote frame buffer."""
        with agmarshall.AgInterface_in_arg(pHost, IRemoteFrameBufferHost) as arg_pHost:
            agcls.evaluate_hresult(self.__dict__["_set_host"](arg_pHost.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{35869E18-8BA8-4259-B64B-E1CD612AD4A4}", IRemoteFrameBuffer)
agcls.AgTypeNameMap["IRemoteFrameBuffer"] = IRemoteFrameBuffer



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
