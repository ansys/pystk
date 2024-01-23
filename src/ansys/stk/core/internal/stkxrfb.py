################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

__all__ = ["IRemoteFrameBuffer", "IRemoteFrameBufferHost"]



from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal.comutil     import IUnknown
from ..internal.apiutil     import (InterfaceProxy, initialize_from_source_object, get_interface_property, 
    set_interface_attribute)
from ..internal.eventutil   import *
from ..utilities.exceptions import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class IRemoteFrameBufferHost(object):
    """Called by engine to request operations from the host using the remote frame buffer."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{D229A605-D3A8-4476-B628-AC549C674B58}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "refresh" : 1, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, IRemoteFrameBufferHost)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IRemoteFrameBufferHost)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, IRemoteFrameBufferHost, None)
    
    _refresh_metadata = { "name" : "refresh",
            "arg_types" : (),
            "marshallers" : () }
    def refresh(self) -> None:
        """A new frame is ready to be displayed."""
        return self._intf.invoke(IRemoteFrameBufferHost._metadata, IRemoteFrameBufferHost._refresh_metadata, )


agcls.AgClassCatalog.add_catalog_entry("{D229A605-D3A8-4476-B628-AC549C674B58}", IRemoteFrameBufferHost)
agcls.AgTypeNameMap["IRemoteFrameBufferHost"] = IRemoteFrameBufferHost

class IRemoteFrameBuffer(object):
    """Expose the control as a remote frame buffer."""

    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{35869E18-8BA8-4259-B64B-E1CD612AD4A4}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "snap_to_rbg_raster" : 1,
                             "set_to_off_screen_rendering" : 2,
                             "notify_resize" : 3,
                             "notify_l_button_up" : 4,
                             "notify_r_button_up" : 5,
                             "notify_m_button_up" : 6,
                             "notify_l_button_down" : 7,
                             "notify_r_button_down" : 8,
                             "notify_m_button_down" : 9,
                             "notify_mouse_move" : 10,
                             "notify_mouse_wheel" : 11,
                             "set_host" : 12,
                             "render_to_direct_x_texture" : 13,
                             "set_to_direct_x_rendering" : 14,
                             "update_direct_x_rendering_texture" : 15, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, IRemoteFrameBuffer)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IRemoteFrameBuffer)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, IRemoteFrameBuffer, None)
    
    _snap_to_rbg_raster_metadata = { "name" : "snap_to_rbg_raster",
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.PVoidArg,) }
    def snap_to_rbg_raster(self, rbgRasterPtr:agcom.PVOID) -> None:
        """Captures the current scene to a raster."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._snap_to_rbg_raster_metadata, rbgRasterPtr)

    _set_to_off_screen_rendering_metadata = { "name" : "set_to_off_screen_rendering",
            "arg_types" : (agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg,) }
    def set_to_off_screen_rendering(self, initialWidth:int, initialHeight:int) -> None:
        """Switch to offscreen rendering."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_to_off_screen_rendering_metadata, initialWidth, initialHeight)

    _notify_resize_metadata = { "name" : "notify_resize",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_resize(self, left:int, top:int, width:int, height:int) -> None:
        """Notifies that a resize event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_resize_metadata, left, top, width, height)

    _notify_l_button_up_metadata = { "name" : "notify_l_button_up",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_l_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse left button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_l_button_up_metadata, x, y, keyState)

    _notify_r_button_up_metadata = { "name" : "notify_r_button_up",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_r_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse right button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_r_button_up_metadata, x, y, keyState)

    _notify_m_button_up_metadata = { "name" : "notify_m_button_up",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_m_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse middle button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_m_button_up_metadata, x, y, keyState)

    _notify_l_button_down_metadata = { "name" : "notify_l_button_down",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_l_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse left button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_l_button_down_metadata, x, y, keyState)

    _notify_r_button_down_metadata = { "name" : "notify_r_button_down",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_r_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse right button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_r_button_down_metadata, x, y, keyState)

    _notify_m_button_down_metadata = { "name" : "notify_m_button_down",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_m_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse middle button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_m_button_down_metadata, x, y, keyState)

    _notify_mouse_move_metadata = { "name" : "notify_mouse_move",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_mouse_move(self, x:int, y:int, buttons:int, keyState:int) -> None:
        """Called by the client on a mouse move event."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_mouse_move_metadata, x, y, buttons, keyState)

    _notify_mouse_wheel_metadata = { "name" : "notify_mouse_wheel",
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_mouse_wheel(self, x:int, y:int, steps:int, keyState:int) -> None:
        """Called by the client on a mouse wheel event."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_mouse_wheel_metadata, x, y, steps, keyState)

    _set_host_metadata = { "name" : "set_host",
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("IRemoteFrameBufferHost"),) }
    def set_host(self, pHost:"IRemoteFrameBufferHost") -> None:
        """Set the host using this remote frame buffer."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_host_metadata, pHost)

    _render_to_direct_x_texture_metadata = { "name" : "render_to_direct_x_texture",
            "arg_types" : (),
            "marshallers" : () }
    def render_to_direct_x_texture(self) -> None:
        """Render to the DirectX texture configured by SetToDirectXRendering()."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._render_to_direct_x_texture_metadata, )

    _set_to_direct_x_rendering_metadata = { "name" : "set_to_direct_x_rendering",
            "arg_types" : (agcom.INT, agcom.INT, agcom.PVOID, agcom.PVOID, agcom.PVOID, agcom.PVOID,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.PVoidArg, agmarshall.PVoidArg, agmarshall.PVoidArg, agmarshall.PVoidArg,) }
    def set_to_direct_x_rendering(self, initialWidth:int, initialHeight:int, hwnd:agcom.PVOID, directXDevice:agcom.PVOID, directXTexture:agcom.PVOID, directXSharedHandle:agcom.PVOID) -> None:
        """Switch to rendering to the specified Dirext X texture."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_to_direct_x_rendering_metadata, initialWidth, initialHeight, hwnd, directXDevice, directXTexture, directXSharedHandle)

    _update_direct_x_rendering_texture_metadata = { "name" : "update_direct_x_rendering_texture",
            "arg_types" : (agcom.PVOID, agcom.PVOID,),
            "marshallers" : (agmarshall.PVoidArg, agmarshall.PVoidArg,) }
    def update_direct_x_rendering_texture(self, directXTexture:agcom.PVOID, directXSharedHandle:agcom.PVOID) -> None:
        """Update Dirext X texture (for instance after a resize)."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._update_direct_x_rendering_texture_metadata, directXTexture, directXSharedHandle)


agcls.AgClassCatalog.add_catalog_entry("{35869E18-8BA8-4259-B64B-E1CD612AD4A4}", IRemoteFrameBuffer)
agcls.AgTypeNameMap["IRemoteFrameBuffer"] = IRemoteFrameBuffer



################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
