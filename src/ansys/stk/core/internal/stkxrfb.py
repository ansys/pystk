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

__all__ = ["IRemoteFrameBuffer", "IRemoteFrameBufferHost"]



from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal.comutil     import IUnknown
from ..internal.apiutil     import (InterfaceProxy, initialize_from_source_object, get_interface_property,
    set_interface_attribute)


class IRemoteFrameBufferHost(object):
    """Called by engine to request operations from the host using the remote frame buffer."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _refresh_method_offset = 1
    _metadata = {
        "iid_data" : (4887649441960683467, 6262802818133504392),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IRemoteFrameBufferHost."""
        initialize_from_source_object(self, source_object, IRemoteFrameBufferHost)
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



agcls.AgClassCatalog.add_catalog_entry((4887649441960683467, 6262802818133504392), IRemoteFrameBufferHost)
agcls.AgTypeNameMap["IRemoteFrameBufferHost"] = IRemoteFrameBufferHost

class IRemoteFrameBuffer(object):
    """Expose the control as a remote frame buffer."""

    _num_methods = 15
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _snap_to_rbg_raster_method_offset = 1
    _set_to_offscreen_rendering_method_offset = 2
    _notify_resize_method_offset = 3
    _notify_left_button_up_method_offset = 4
    _notify_right_button_up_method_offset = 5
    _notify_middle_button_up_method_offset = 6
    _notify_left_button_down_method_offset = 7
    _notify_right_button_down_method_offset = 8
    _notify_middle_button_down_method_offset = 9
    _notify_mouse_move_method_offset = 10
    _notify_mouse_wheel_method_offset = 11
    _set_host_method_offset = 12
    _render_to_directx_texture_method_offset = 13
    _set_to_directx_rendering_method_offset = 14
    _update_directx_rendering_texture_method_offset = 15
    _metadata = {
        "iid_data" : (5092725537887735708, 17412474012788944557),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IRemoteFrameBuffer."""
        initialize_from_source_object(self, source_object, IRemoteFrameBuffer)
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
    def snap_to_rbg_raster(self, rbg_raster_ptr:agcom.PVOID) -> None:
        """Capture the current scene to a raster."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._snap_to_rbg_raster_metadata, rbg_raster_ptr)

    _set_to_offscreen_rendering_metadata = { "offset" : _set_to_offscreen_rendering_method_offset,
            "arg_types" : (agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg,) }
    def set_to_offscreen_rendering(self, initial_width:int, initial_height:int) -> None:
        """Switch to offscreen rendering."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_to_offscreen_rendering_metadata, initial_width, initial_height)

    _notify_resize_metadata = { "offset" : _notify_resize_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_resize(self, left:int, top:int, width:int, height:int) -> None:
        """Notifies that a resize event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_resize_metadata, left, top, width, height)

    _notify_left_button_up_metadata = { "offset" : _notify_left_button_up_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_left_button_up(self, x:int, y:int, key_state:int) -> None:
        """Notifies that a mouse left button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_left_button_up_metadata, x, y, key_state)

    _notify_right_button_up_metadata = { "offset" : _notify_right_button_up_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_right_button_up(self, x:int, y:int, key_state:int) -> None:
        """Notifies that a mouse right button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_right_button_up_metadata, x, y, key_state)

    _notify_middle_button_up_metadata = { "offset" : _notify_middle_button_up_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_middle_button_up(self, x:int, y:int, key_state:int) -> None:
        """Notifies that a mouse middle button up event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_middle_button_up_metadata, x, y, key_state)

    _notify_left_button_down_metadata = { "offset" : _notify_left_button_down_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_left_button_down(self, x:int, y:int, key_state:int) -> None:
        """Notifies that a mouse left button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_left_button_down_metadata, x, y, key_state)

    _notify_right_button_down_metadata = { "offset" : _notify_right_button_down_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_right_button_down(self, x:int, y:int, key_state:int) -> None:
        """Notifies that a mouse right button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_right_button_down_metadata, x, y, key_state)

    _notify_middle_button_down_metadata = { "offset" : _notify_middle_button_down_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_middle_button_down(self, x:int, y:int, key_state:int) -> None:
        """Notifies that a mouse middle button down event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_middle_button_down_metadata, x, y, key_state)

    _notify_mouse_move_metadata = { "offset" : _notify_mouse_move_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_mouse_move(self, x:int, y:int, buttons:int, key_state:int) -> None:
        """Notifies that a mouse move event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_mouse_move_metadata, x, y, buttons, key_state)

    _notify_mouse_wheel_metadata = { "offset" : _notify_mouse_wheel_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.INT, agcom.INT,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg, agmarshall.IntArg,) }
    def notify_mouse_wheel(self, x:int, y:int, steps:int, key_state:int) -> None:
        """Notifies that a mouse wheel event occurred."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._notify_mouse_wheel_metadata, x, y, steps, key_state)

    _set_host_metadata = { "offset" : _set_host_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("IRemoteFrameBufferHost"),) }
    def set_host(self, host:"IRemoteFrameBufferHost") -> None:
        """Set the host using this remote frame buffer."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_host_metadata, host)

    _render_to_directx_texture_metadata = { "offset" : _render_to_directx_texture_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def render_to_directx_texture(self) -> None:
        """Render to the DirectX texture configured by SetToDirectXRendering()."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._render_to_directx_texture_metadata, )

    _set_to_directx_rendering_metadata = { "offset" : _set_to_directx_rendering_method_offset,
            "arg_types" : (agcom.INT, agcom.INT, agcom.PVOID, agcom.PVOID, agcom.PVOID, agcom.PVOID,),
            "marshallers" : (agmarshall.IntArg, agmarshall.IntArg, agmarshall.PVoidArg, agmarshall.PVoidArg, agmarshall.PVoidArg, agmarshall.PVoidArg,) }
    def set_to_directx_rendering(self, initial_width:int, initial_height:int, hwnd:agcom.PVOID, direct_x_device:agcom.PVOID, direct_x_texture:agcom.PVOID, direct_x_shared_handle:agcom.PVOID) -> None:
        """Switch to rendering to the specified Dirext X texture."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._set_to_directx_rendering_metadata, initial_width, initial_height, hwnd, direct_x_device, direct_x_texture, direct_x_shared_handle)

    _update_directx_rendering_texture_metadata = { "offset" : _update_directx_rendering_texture_method_offset,
            "arg_types" : (agcom.PVOID, agcom.PVOID,),
            "marshallers" : (agmarshall.PVoidArg, agmarshall.PVoidArg,) }
    def update_directx_rendering_texture(self, direct_x_texture:agcom.PVOID, direct_x_shared_handle:agcom.PVOID) -> None:
        """Update Dirext X texture (for instance after a resize)."""
        return self._intf.invoke(IRemoteFrameBuffer._metadata, IRemoteFrameBuffer._update_directx_rendering_texture_metadata, direct_x_texture, direct_x_shared_handle)



agcls.AgClassCatalog.add_catalog_entry((5092725537887735708, 17412474012788944557), IRemoteFrameBuffer)
agcls.AgTypeNameMap["IRemoteFrameBuffer"] = IRemoteFrameBuffer