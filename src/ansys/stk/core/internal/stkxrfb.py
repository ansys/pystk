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
    _refresh_method_offset = 1
    _metadata = {
        "iid_data" : (4933363163864868357, 6362292819724085430),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, sourceObject=None):
        """Construct an object of type IRemoteFrameBufferHost."""
        initialize_from_source_object(self, sourceObject, IRemoteFrameBufferHost)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IRemoteFrameBufferHost)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IRemoteFrameBufferHost, None)
    
    _refresh_metadata = { "offset" : _refresh_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def refresh(self) -> None:
        """Request a new frame to be displayed."""
        return self._intf.invoke(IRemoteFrameBufferHost._metadata, IRemoteFrameBufferHost._refresh_metadata, )


agcls.AgClassCatalog.add_catalog_entry((4933363163864868357, 6362292819724085430), IRemoteFrameBufferHost)
agcls.AgTypeNameMap["IRemoteFrameBufferHost"] = IRemoteFrameBufferHost

class IRemoteFrameBuffer(object):
    """Expose the control as a remote frame buffer."""

    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _snap_to_rbg_raster_method_offset = 1
    _set_to_off_screen_rendering_method_offset = 2
    _notify_resize_method_offset = 3
    _notify_l_button_up_method_offset = 4
    _notify_r_button_up_method_offset = 5
    _notify_m_button_up_method_offset = 6
    _notify_l_button_down_method_offset = 7
    _notify_r_button_down_method_offset = 8
    _notify_m_button_down_method_offset = 9
    _notify_mouse_move_method_offset = 10
    _notify_mouse_wheel_method_offset = 11
    _set_host_method_offset = 12
    _render_to_direct_x_texture_method_offset = 13
    _set_to_direct_x_rendering_method_offset = 14
    _update_direct_x_rendering_texture_method_offset = 15
    _metadata = {
        "iid_data" : (4781006033999273496, 11877164716837129142),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, sourceObject=None):
        """Construct an object of type IRemoteFrameBuffer."""
        initialize_from_source_object(self, sourceObject, IRemoteFrameBuffer)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IRemoteFrameBuffer)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IRemoteFrameBuffer, None)
    
    _snap_to_rbg_raster_metadata = { "offset" : _snap_to_rbg_raster_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.PVoidArg,) }
    def snap_to_rbg_raster(self, rbgRasterPtr:agcom.PVOID) -> None:
        """Capture the current scene to a raster."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._snap_to_rbg_raster_metadata, rbgRasterPtr)

    _set_to_off_screen_rendering_metadata = { "offset" : _set_to_off_screen_rendering_method_offset,
            "arg_types" : (agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg,) }
    def set_to_off_screen_rendering(self, initialWidth:int, initialHeight:int) -> None:
        """Switch to offscreen rendering."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_to_off_screen_rendering_metadata, initialWidth, initialHeight)

    _notify_resize_metadata = { "offset" : _notify_resize_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_resize(self, left:int, top:int, width:int, height:int) -> None:
        """Notifies that a resize event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_resize_metadata, left, top, width, height)

    _notify_l_button_up_metadata = { "offset" : _notify_l_button_up_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_l_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse left button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_l_button_up_metadata, x, y, keyState)

    _notify_r_button_up_metadata = { "offset" : _notify_r_button_up_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_r_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse right button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_r_button_up_metadata, x, y, keyState)

    _notify_m_button_up_metadata = { "offset" : _notify_m_button_up_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_m_button_up(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse middle button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_m_button_up_metadata, x, y, keyState)

    _notify_l_button_down_metadata = { "offset" : _notify_l_button_down_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_l_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse left button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_l_button_down_metadata, x, y, keyState)

    _notify_r_button_down_metadata = { "offset" : _notify_r_button_down_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_r_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse right button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_r_button_down_metadata, x, y, keyState)

    _notify_m_button_down_metadata = { "offset" : _notify_m_button_down_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_m_button_down(self, x:int, y:int, keyState:int) -> None:
        """Notifies that a mouse middle button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_m_button_down_metadata, x, y, keyState)

    _notify_mouse_move_metadata = { "offset" : _notify_mouse_move_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_mouse_move(self, x:int, y:int, buttons:int, keyState:int) -> None:
        """Notifies that a mouse move event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_mouse_move_metadata, x, y, buttons, keyState)

    _notify_mouse_wheel_metadata = { "offset" : _notify_mouse_wheel_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_mouse_wheel(self, x:int, y:int, steps:int, keyState:int) -> None:
        """Notifies that a mouse wheel event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_mouse_wheel_metadata, x, y, steps, keyState)

    _set_host_metadata = { "offset" : _set_host_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("IRemoteFrameBufferHost"),) }
    def set_host(self, pHost:"IRemoteFrameBufferHost") -> None:
        """Set the host using this remote frame buffer."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_host_metadata, pHost)

    _render_to_direct_x_texture_metadata = { "offset" : _render_to_direct_x_texture_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def render_to_direct_x_texture(self) -> None:
        """Render to the DirectX texture configured by SetToDirectXRendering()."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._render_to_direct_x_texture_metadata, )

    _set_to_direct_x_rendering_metadata = { "offset" : _set_to_direct_x_rendering_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.PVOID, agcom.PVOID, agcom.PVOID, agcom.PVOID,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.PVoidArg, agmarshall.PVoidArg, agmarshall.PVoidArg, agmarshall.PVoidArg,) }
    def set_to_direct_x_rendering(self, initialWidth:int, initialHeight:int, hwnd:agcom.PVOID, directXDevice:agcom.PVOID, directXTexture:agcom.PVOID, directXSharedHandle:agcom.PVOID) -> None:
        """Switch to rendering to the specified Dirext X texture."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_to_direct_x_rendering_metadata, initialWidth, initialHeight, hwnd, directXDevice, directXTexture, directXSharedHandle)

    _update_direct_x_rendering_texture_metadata = { "offset" : _update_direct_x_rendering_texture_method_offset,
            "arg_types" : (agcom.PVOID, agcom.PVOID,),
            "marshallers" : (agmarshall.PVoidArg, agmarshall.PVoidArg,) }
    def update_direct_x_rendering_texture(self, directXTexture:agcom.PVOID, directXSharedHandle:agcom.PVOID) -> None:
        """Update Dirext X texture (for instance after a resize)."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._update_direct_x_rendering_texture_metadata, directXTexture, directXSharedHandle)


agcls.AgClassCatalog.add_catalog_entry((4781006033999273496, 11877164716837129142), IRemoteFrameBuffer)
agcls.AgTypeNameMap["IRemoteFrameBuffer"] = IRemoteFrameBuffer



################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
