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

"""The STK UI Core library is a COM library containing classes, interfaces and enumerations for the Application Object Model."""

__all__ = ["ApplicationWindowState", "Toolbar", "ToolbarCollection", "Window", "WindowArrangeState", "WindowArrangeStyle",
"WindowDockStyle", "WindowGlobeObject", "WindowMapObject", "WindowServiceType", "WindowsCollection"]

from ctypes import POINTER
from enum import IntEnum
import typing

from .internal import coclassutil as agcls, comutil as agcom, marshall as agmarshall
from .internal.apiutil import (
    EnumeratorProxy,
    InterfaceProxy,
    OutArg,
    SupportsDeleteCallback,
    get_interface_property,
    initialize_from_source_object,
    set_class_attribute,
)
from .internal.comutil import IDispatch, IUnknown


class WindowServiceType(IntEnum):
    """Well-known types of services."""

    WINDOW_2D = 1
    """A 2D window."""
    WINDOW_3D = 2
    """A 3D window."""

WindowServiceType.WINDOW_2D.__doc__ = "A 2D window."
WindowServiceType.WINDOW_3D.__doc__ = "A 3D window."

agcls.AgTypeNameMap["WindowServiceType"] = WindowServiceType

class ApplicationWindowState(IntEnum):
    """Window states."""

    MAXIMIZED = 1
    """Window is maximized."""
    MINIMIZED = 2
    """Window is minimized."""
    NORMAL = 3
    """Normal window state."""

ApplicationWindowState.MAXIMIZED.__doc__ = "Window is maximized."
ApplicationWindowState.MINIMIZED.__doc__ = "Window is minimized."
ApplicationWindowState.NORMAL.__doc__ = "Normal window state."

agcls.AgTypeNameMap["ApplicationWindowState"] = ApplicationWindowState

class WindowArrangeStyle(IntEnum):
    """Window layout styles."""

    CASCADE = 1
    """Child windows are cascaded within the main window."""
    TILED_HORIZONTAL = 2
    """Child windows are tiled horizontally within the main window."""
    TILED_VERTICAL = 3
    """Child windows are tiled vertically within the main window."""

WindowArrangeStyle.CASCADE.__doc__ = "Child windows are cascaded within the main window."
WindowArrangeStyle.TILED_HORIZONTAL.__doc__ = "Child windows are tiled horizontally within the main window."
WindowArrangeStyle.TILED_VERTICAL.__doc__ = "Child windows are tiled vertically within the main window."

agcls.AgTypeNameMap["WindowArrangeStyle"] = WindowArrangeStyle

class WindowDockStyle(IntEnum):
    """Window docking styles."""

    INTEGRATED = 1
    """Child window is integrated into the main window."""
    DOCKED_LEFT = 2
    """Child window is docked to the left side of the within the main window."""
    DOCKED_RIGHT = 3
    """Child window is docked to the right side of the main window."""
    DOCKED_TOP = 4
    """Child window is docked to the top of the main window."""
    DOCKED_BOTTOM = 5
    """Child window is docked to the bottom of the main window."""
    FLOATING = 6
    """Child window is not docked or integrated."""

WindowDockStyle.INTEGRATED.__doc__ = "Child window is integrated into the main window."
WindowDockStyle.DOCKED_LEFT.__doc__ = "Child window is docked to the left side of the within the main window."
WindowDockStyle.DOCKED_RIGHT.__doc__ = "Child window is docked to the right side of the main window."
WindowDockStyle.DOCKED_TOP.__doc__ = "Child window is docked to the top of the main window."
WindowDockStyle.DOCKED_BOTTOM.__doc__ = "Child window is docked to the bottom of the main window."
WindowDockStyle.FLOATING.__doc__ = "Child window is not docked or integrated."

agcls.AgTypeNameMap["WindowDockStyle"] = WindowDockStyle

class WindowArrangeState(IntEnum):
    """Floating state."""

    FLOATED = 1
    """The UI element is floated."""
    DOCKED = 2
    """The UI element is docked."""

WindowArrangeState.FLOATED.__doc__ = "The UI element is floated."
WindowArrangeState.DOCKED.__doc__ = "The UI element is docked."

agcls.AgTypeNameMap["WindowArrangeState"] = WindowArrangeState



class WindowsCollection(SupportsDeleteCallback):
    """Provide methods and properties to manage the application's windows."""

    _num_methods = 7
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get_count_method_offset = 2
    _arrange_method_offset = 3
    _add_method_offset = 4
    _get__new_enum_method_offset = 5
    _get_item_by_index_method_offset = 6
    _get_item_by_name_method_offset = 7
    _metadata = {
        "iid_data" : (4730401565789584263, 3861368304027982243),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, WindowsCollection)
    def __iter__(self):
        """Create an iterator for the WindowsCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "Window":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def item(self, index_or_caption:typing.Any) -> "Window":
        """Retrieve a window object."""
        return self._intf.invoke(WindowsCollection._metadata, WindowsCollection._item_metadata, index_or_caption, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return a total number of window objects in the collection."""
        return self._intf.get_property(WindowsCollection._metadata, WindowsCollection._get_count_metadata)

    _arrange_metadata = { "offset" : _arrange_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(WindowArrangeStyle),) }
    def arrange(self, arrange_style:"WindowArrangeStyle") -> None:
        """Arranges the application windows using the specified style."""
        return self._intf.invoke(WindowsCollection._metadata, WindowsCollection._arrange_metadata, arrange_style)

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.BSTR, agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def add(self, plugin_id:str, init_data:typing.Any) -> "Window":
        """Create a new window. The bstrPluginID is a COM ProgID associated with an STK plugin."""
        return self._intf.invoke(WindowsCollection._metadata, WindowsCollection._add_metadata, plugin_id, init_data, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Enumerates the windows in the collection."""
        return self._intf.get_property(WindowsCollection._metadata, WindowsCollection._get__new_enum_metadata)

    _get_item_by_index_metadata = { "offset" : _get_item_by_index_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "Window":
        """Retrieve a window object by index in collection."""
        return self._intf.invoke(WindowsCollection._metadata, WindowsCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "offset" : _get_item_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "Window":
        """Retrieve a window object by name of window object."""
        return self._intf.invoke(WindowsCollection._metadata, WindowsCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type WindowsCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, WindowsCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, WindowsCollection, [WindowsCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5214364363717914366, 13578877492221407144), WindowsCollection)
agcls.AgTypeNameMap["WindowsCollection"] = WindowsCollection

class Window(SupportsDeleteCallback):
    """Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window."""

    _num_methods = 24
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_caption_method_offset = 1
    _set_caption_method_offset = 2
    _activate_method_offset = 3
    _get_window_state_method_offset = 4
    _set_window_state_method_offset = 5
    _close_method_offset = 6
    _get_height_method_offset = 7
    _set_height_method_offset = 8
    _get_width_method_offset = 9
    _set_width_method_offset = 10
    _get_left_method_offset = 11
    _set_left_method_offset = 12
    _get_top_method_offset = 13
    _set_top_method_offset = 14
    _get_dock_style_method_offset = 15
    _set_dock_style_method_offset = 16
    _get_no_workbook_close_method_offset = 17
    _set_no_workbook_close_method_offset = 18
    _get_unpinned_method_offset = 19
    _set_unpinned_method_offset = 20
    _get_can_pin_method_offset = 21
    _get_toolbars_method_offset = 22
    _get_service_by_name_method_offset = 23
    _get_service_by_type_method_offset = 24
    _metadata = {
        "iid_data" : (5238521222474863957, 13235753129659511978),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Window)

    _get_caption_metadata = { "offset" : _get_caption_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def caption(self) -> str:
        """Get or set the window caption. Can only be set within UI plugins for the non unique windows they own."""
        return self._intf.get_property(Window._metadata, Window._get_caption_metadata)

    _set_caption_metadata = { "offset" : _set_caption_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @caption.setter
    def caption(self, caption:str) -> None:
        """Get or set  the window caption. Can only be set within UI plugins for the non unique windows they own."""
        return self._intf.set_property(Window._metadata, Window._set_caption_metadata, caption)

    _activate_metadata = { "offset" : _activate_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def activate(self) -> None:
        """Activates the window."""
        return self._intf.invoke(Window._metadata, Window._activate_metadata, )

    _get_window_state_metadata = { "offset" : _get_window_state_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ApplicationWindowState),) }
    @property
    def window_state(self) -> "ApplicationWindowState":
        """The window state."""
        return self._intf.get_property(Window._metadata, Window._get_window_state_metadata)

    _set_window_state_metadata = { "offset" : _set_window_state_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ApplicationWindowState),) }
    @window_state.setter
    def window_state(self, new_value:"ApplicationWindowState") -> None:
        return self._intf.set_property(Window._metadata, Window._set_window_state_metadata, new_value)

    _close_metadata = { "offset" : _close_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def close(self) -> None:
        """Close the window."""
        return self._intf.invoke(Window._metadata, Window._close_metadata, )

    _get_height_metadata = { "offset" : _get_height_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def height(self) -> int:
        """The window height."""
        return self._intf.get_property(Window._metadata, Window._get_height_metadata)

    _set_height_metadata = { "offset" : _set_height_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @height.setter
    def height(self, new_value:int) -> None:
        return self._intf.set_property(Window._metadata, Window._set_height_metadata, new_value)

    _get_width_metadata = { "offset" : _get_width_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def width(self) -> int:
        """The window width."""
        return self._intf.get_property(Window._metadata, Window._get_width_metadata)

    _set_width_metadata = { "offset" : _set_width_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @width.setter
    def width(self, new_value:int) -> None:
        return self._intf.set_property(Window._metadata, Window._set_width_metadata, new_value)

    _get_left_metadata = { "offset" : _get_left_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def left(self) -> int:
        """The window horizontal position."""
        return self._intf.get_property(Window._metadata, Window._get_left_metadata)

    _set_left_metadata = { "offset" : _set_left_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @left.setter
    def left(self, new_value:int) -> None:
        return self._intf.set_property(Window._metadata, Window._set_left_metadata, new_value)

    _get_top_metadata = { "offset" : _get_top_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def top(self) -> int:
        """The window vertical position."""
        return self._intf.get_property(Window._metadata, Window._get_top_metadata)

    _set_top_metadata = { "offset" : _set_top_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @top.setter
    def top(self, new_value:int) -> None:
        return self._intf.set_property(Window._metadata, Window._set_top_metadata, new_value)

    _get_dock_style_metadata = { "offset" : _get_dock_style_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(WindowDockStyle),) }
    @property
    def dock_style(self) -> "WindowDockStyle":
        """The window docking style."""
        return self._intf.get_property(Window._metadata, Window._get_dock_style_metadata)

    _set_dock_style_metadata = { "offset" : _set_dock_style_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(WindowDockStyle),) }
    @dock_style.setter
    def dock_style(self, new_value:"WindowDockStyle") -> None:
        return self._intf.set_property(Window._metadata, Window._set_dock_style_metadata, new_value)

    _get_no_workbook_close_metadata = { "offset" : _get_no_workbook_close_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def no_workbook_close(self) -> bool:
        """Whether to close the window when the application workbook is loaded/closed."""
        return self._intf.get_property(Window._metadata, Window._get_no_workbook_close_metadata)

    _set_no_workbook_close_metadata = { "offset" : _set_no_workbook_close_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @no_workbook_close.setter
    def no_workbook_close(self, new_value:bool) -> None:
        return self._intf.set_property(Window._metadata, Window._set_no_workbook_close_metadata, new_value)

    _get_unpinned_metadata = { "offset" : _get_unpinned_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def unpinned(self) -> bool:
        """The window's pinned state."""
        return self._intf.get_property(Window._metadata, Window._get_unpinned_metadata)

    _set_unpinned_metadata = { "offset" : _set_unpinned_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @unpinned.setter
    def unpinned(self, new_value:bool) -> None:
        return self._intf.set_property(Window._metadata, Window._set_unpinned_metadata, new_value)

    _get_can_pin_metadata = { "offset" : _get_can_pin_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def can_pin(self) -> bool:
        """Return whether the window supports pinning."""
        return self._intf.get_property(Window._metadata, Window._get_can_pin_metadata)

    _get_toolbars_metadata = { "offset" : _get_toolbars_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def toolbars(self) -> "ToolbarCollection":
        """Return the window's toolbar collection."""
        return self._intf.get_property(Window._metadata, Window._get_toolbars_metadata)

    _get_service_by_name_metadata = { "offset" : _get_service_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_service_by_name(self, name:str) -> typing.Any:
        """Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name."""
        return self._intf.invoke(Window._metadata, Window._get_service_by_name_metadata, name, OutArg())

    _get_service_by_type_metadata = { "offset" : _get_service_by_type_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(WindowServiceType), agmarshall.InterfaceOutArg,) }
    def get_service_by_type(self, service_type:"WindowServiceType") -> typing.Any:
        """Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type."""
        return self._intf.invoke(Window._metadata, Window._get_service_by_type_metadata, service_type, OutArg())

    _property_names[caption] = "caption"
    _property_names[window_state] = "window_state"
    _property_names[height] = "height"
    _property_names[width] = "width"
    _property_names[left] = "left"
    _property_names[top] = "top"
    _property_names[dock_style] = "dock_style"
    _property_names[no_workbook_close] = "no_workbook_close"
    _property_names[unpinned] = "unpinned"
    _property_names[can_pin] = "can_pin"
    _property_names[toolbars] = "toolbars"

    def __init__(self, source_object=None):
        """Construct an object of type Window."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Window)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Window, [Window, ])

agcls.AgClassCatalog.add_catalog_entry((5499256377237207604, 1833479666897313423), Window)
agcls.AgTypeNameMap["Window"] = Window

class Toolbar(SupportsDeleteCallback):
    """Provide methods and properties to control a toolbar."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_identifier_method_offset = 1
    _get_caption_method_offset = 2
    _get_visible_method_offset = 3
    _set_visible_method_offset = 4
    _get_float_state_method_offset = 5
    _set_float_state_method_offset = 6
    _metadata = {
        "iid_data" : (4815534316350549014, 8106580190020797345),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Toolbar)

    _get_identifier_metadata = { "offset" : _get_identifier_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def identifier(self) -> int:
        """The identity."""
        return self._intf.get_property(Toolbar._metadata, Toolbar._get_identifier_metadata)

    _get_caption_metadata = { "offset" : _get_caption_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def caption(self) -> str:
        """The caption."""
        return self._intf.get_property(Toolbar._metadata, Toolbar._get_caption_metadata)

    _get_visible_metadata = { "offset" : _get_visible_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def visible(self) -> bool:
        """The visibility."""
        return self._intf.get_property(Toolbar._metadata, Toolbar._get_visible_metadata)

    _set_visible_metadata = { "offset" : _set_visible_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @visible.setter
    def visible(self, new_value:bool) -> None:
        return self._intf.set_property(Toolbar._metadata, Toolbar._set_visible_metadata, new_value)

    _get_float_state_metadata = { "offset" : _get_float_state_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(WindowArrangeState),) }
    @property
    def float_state(self) -> "WindowArrangeState":
        """The float state."""
        return self._intf.get_property(Toolbar._metadata, Toolbar._get_float_state_metadata)

    _set_float_state_metadata = { "offset" : _set_float_state_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(WindowArrangeState),) }
    @float_state.setter
    def float_state(self, new_value:"WindowArrangeState") -> None:
        return self._intf.set_property(Toolbar._metadata, Toolbar._set_float_state_metadata, new_value)

    _property_names[identifier] = "identifier"
    _property_names[caption] = "caption"
    _property_names[visible] = "visible"
    _property_names[float_state] = "float_state"

    def __init__(self, source_object=None):
        """Construct an object of type Toolbar."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Toolbar)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Toolbar, [Toolbar, ])

agcls.AgClassCatalog.add_catalog_entry((4933179785366539802, 14000769212146133947), Toolbar)
agcls.AgTypeNameMap["Toolbar"] = Toolbar

class ToolbarCollection(SupportsDeleteCallback):
    """Provide methods and properties to obtain a window's toolbars."""

    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get_count_method_offset = 2
    _get__new_enum_method_offset = 3
    _get_toolbar_by_id_method_offset = 4
    _get_item_by_index_method_offset = 5
    _get_item_by_name_method_offset = 6
    _metadata = {
        "iid_data" : (5034548498384163675, 2931144109818226324),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ToolbarCollection)
    def __iter__(self):
        """Create an iterator for the ToolbarCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "Toolbar":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def item(self, index_or_caption:typing.Any) -> "Toolbar":
        """Retrieve a toolbar object."""
        return self._intf.invoke(ToolbarCollection._metadata, ToolbarCollection._item_metadata, index_or_caption, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return a total number of toolbars in the collection."""
        return self._intf.get_property(ToolbarCollection._metadata, ToolbarCollection._get_count_metadata)

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Enumerates the toolbars in the collection."""
        return self._intf.get_property(ToolbarCollection._metadata, ToolbarCollection._get__new_enum_metadata)

    _get_toolbar_by_id_metadata = { "offset" : _get_toolbar_by_id_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LongArg, agmarshall.InterfaceOutArg,) }
    def get_toolbar_by_id(self, id:int) -> "Toolbar":
        """Return a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object."""
        return self._intf.invoke(ToolbarCollection._metadata, ToolbarCollection._get_toolbar_by_id_metadata, id, OutArg())

    _get_item_by_index_metadata = { "offset" : _get_item_by_index_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "Toolbar":
        """Retrieve a toolbar object based on the index in the collection."""
        return self._intf.invoke(ToolbarCollection._metadata, ToolbarCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "offset" : _get_item_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "Toolbar":
        """Retrieve a toolbar object based on the name of the Toolbar in the collection."""
        return self._intf.invoke(ToolbarCollection._metadata, ToolbarCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type ToolbarCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ToolbarCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ToolbarCollection, [ToolbarCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5456824333564167713, 9127285738383814044), ToolbarCollection)
agcls.AgTypeNameMap["ToolbarCollection"] = ToolbarCollection

class WindowMapObject(SupportsDeleteCallback):
    """Represents a 2D (Map) window. Provides methods and properties to access the 2D window properties."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_map_id_method_offset = 1
    _metadata = {
        "iid_data" : (5665093236705462569, 949456394611833022),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, WindowMapObject)

    _get_map_id_metadata = { "offset" : _get_map_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def map_id(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 2D map."""
        return self._intf.get_property(WindowMapObject._metadata, WindowMapObject._get_map_id_metadata)

    _property_names[map_id] = "map_id"

    def __init__(self, source_object=None):
        """Construct an object of type WindowMapObject."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, WindowMapObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, WindowMapObject, [WindowMapObject, ])

agcls.AgClassCatalog.add_catalog_entry((4810650615632165871, 5900599590476949660), WindowMapObject)
agcls.AgTypeNameMap["WindowMapObject"] = WindowMapObject

class WindowGlobeObject(SupportsDeleteCallback):
    """Represents a 3D (Globe) window. Provides methods and properties to access the 3D window properties."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_scene_id_method_offset = 1
    _metadata = {
        "iid_data" : (5014201186762943933, 15007269609063404450),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, WindowGlobeObject)

    _get_scene_id_metadata = { "offset" : _get_scene_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def scene_id(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 3D globe."""
        return self._intf.get_property(WindowGlobeObject._metadata, WindowGlobeObject._get_scene_id_metadata)

    _property_names[scene_id] = "scene_id"

    def __init__(self, source_object=None):
        """Construct an object of type WindowGlobeObject."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, WindowGlobeObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, WindowGlobeObject, [WindowGlobeObject, ])

agcls.AgClassCatalog.add_catalog_entry((4681936252797348470, 12626443510729352364), WindowGlobeObject)
agcls.AgTypeNameMap["WindowGlobeObject"] = WindowGlobeObject