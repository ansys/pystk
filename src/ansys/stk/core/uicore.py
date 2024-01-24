################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

__all__ = ["ARRANGE_STYLE", "DOCK_STYLE", "FLOAT_STATE", "IUiToolbar", "IUiToolbarCollection", "IUiWindow", "IUiWindowGlobeObject", 
"IUiWindowMapObject", "IUiWindowsCollection", "UiToolbar", "UiToolbarCollection", "UiWindow", "UiWindowGlobeObject", "UiWindowMapObject", 
"UiWindowsCollection", "WINDOW_SERVICE", "WINDOW_STATE"]

import typing

from ctypes   import POINTER
from enum     import IntEnum

from .internal  import comutil          as agcom
from .internal  import coclassutil      as agcls
from .internal  import marshall         as agmarshall
from .internal.comutil     import IUnknown, IDispatch
from .internal.apiutil     import (InterfaceProxy, EnumeratorProxy, OutArg, 
    initialize_from_source_object, get_interface_property, set_interface_attribute, 
    set_class_attribute)
from .internal.eventutil   import *
from .utilities.exceptions import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class WINDOW_SERVICE(IntEnum):
    """Well-known types of services."""
   
    WINDOW_2D = 1
    """A 2D window."""
    WINDOW_3D = 2
    """A 3D window."""

WINDOW_SERVICE.WINDOW_2D.__doc__ = "A 2D window."
WINDOW_SERVICE.WINDOW_3D.__doc__ = "A 3D window."

agcls.AgTypeNameMap["WINDOW_SERVICE"] = WINDOW_SERVICE

class WINDOW_STATE(IntEnum):
    """Window states."""
   
    MAXIMIZED = 1
    """Window is maximized."""
    MINIMIZED = 2
    """Window is minimized."""
    NORMAL = 3
    """Normal window state."""

WINDOW_STATE.MAXIMIZED.__doc__ = "Window is maximized."
WINDOW_STATE.MINIMIZED.__doc__ = "Window is minimized."
WINDOW_STATE.NORMAL.__doc__ = "Normal window state."

agcls.AgTypeNameMap["WINDOW_STATE"] = WINDOW_STATE

class ARRANGE_STYLE(IntEnum):
    """Window layout styles."""
   
    CASCADE = 1
    """Child windows are cascaded within the main window."""
    TILED_HORIZONTAL = 2
    """Child windows are tiled horizontally within the main window."""
    TILED_VERTICAL = 3
    """Child windows are tiled vertically within the main window."""

ARRANGE_STYLE.CASCADE.__doc__ = "Child windows are cascaded within the main window."
ARRANGE_STYLE.TILED_HORIZONTAL.__doc__ = "Child windows are tiled horizontally within the main window."
ARRANGE_STYLE.TILED_VERTICAL.__doc__ = "Child windows are tiled vertically within the main window."

agcls.AgTypeNameMap["ARRANGE_STYLE"] = ARRANGE_STYLE

class DOCK_STYLE(IntEnum):
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

DOCK_STYLE.INTEGRATED.__doc__ = "Child window is integrated into the main window."
DOCK_STYLE.DOCKED_LEFT.__doc__ = "Child window is docked to the left side of the within the main window."
DOCK_STYLE.DOCKED_RIGHT.__doc__ = "Child window is docked to the right side of the main window."
DOCK_STYLE.DOCKED_TOP.__doc__ = "Child window is docked to the top of the main window."
DOCK_STYLE.DOCKED_BOTTOM.__doc__ = "Child window is docked to the bottom of the main window."
DOCK_STYLE.FLOATING.__doc__ = "Child window is not docked or integrated."

agcls.AgTypeNameMap["DOCK_STYLE"] = DOCK_STYLE

class FLOAT_STATE(IntEnum):
    """Floating state."""
   
    FLOATED = 1
    """The UI element is floated."""
    DOCKED = 2
    """The UI element is docked."""

FLOAT_STATE.FLOATED.__doc__ = "The UI element is floated."
FLOAT_STATE.DOCKED.__doc__ = "The UI element is docked."

agcls.AgTypeNameMap["FLOAT_STATE"] = FLOAT_STATE


class IUiToolbar(object):
    """Provide methods and properties to control a toolbar."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{69C72C16-36F2-42d4-A183-6879BB5B8070}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_id" : 1,
                             "get_caption" : 2,
                             "get_visible" : 3,
                             "set_visible" : 4,
                             "get_float_state" : 5,
                             "set_float_state" : 6, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, IUiToolbar)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IUiToolbar)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, IUiToolbar, None)
    
    _get_id_metadata = { "name" : "id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def id(self) -> int:
        """The identity."""
        return self._intf.get_property(IUiToolbar._metadata, IUiToolbar._get_id_metadata)

    _get_caption_metadata = { "name" : "caption",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def caption(self) -> str:
        """The caption."""
        return self._intf.get_property(IUiToolbar._metadata, IUiToolbar._get_caption_metadata)

    _get_visible_metadata = { "name" : "visible",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def visible(self) -> bool:
        """The visibility."""
        return self._intf.get_property(IUiToolbar._metadata, IUiToolbar._get_visible_metadata)

    _set_visible_metadata = { "name" : "visible",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @visible.setter
    def visible(self, newVal:bool) -> None:
        return self._intf.set_property(IUiToolbar._metadata, IUiToolbar._set_visible_metadata, newVal)

    _get_float_state_metadata = { "name" : "float_state",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(FLOAT_STATE),) }
    @property
    def float_state(self) -> "FLOAT_STATE":
        """The float state."""
        return self._intf.get_property(IUiToolbar._metadata, IUiToolbar._get_float_state_metadata)

    _set_float_state_metadata = { "name" : "float_state",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(FLOAT_STATE),) }
    @float_state.setter
    def float_state(self, newVal:"FLOAT_STATE") -> None:
        return self._intf.set_property(IUiToolbar._metadata, IUiToolbar._set_float_state_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{69C72C16-36F2-42d4-A183-6879BB5B8070}", IUiToolbar)
agcls.AgTypeNameMap["IUiToolbar"] = IUiToolbar

class IUiToolbarCollection(object):
    """Provide methods and properties to obtain a window's toolbars."""

    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{62AA135B-4F2F-45de-94A6-31BB0984AD28}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "item" : 1,
                             "get_count" : 2,
                             "get__NewEnum" : 3,
                             "get_toolbar_by_id" : 4,
                             "get_item_by_index" : 5,
                             "get_item_by_name" : 6, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, IUiToolbarCollection)
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IUiToolbarCollection)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, IUiToolbarCollection, None)
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IUiToolbar":
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def item(self, indexOrCaption:typing.Any) -> "UiToolbar":
        """Retrieve a toolbar object."""
        return self._intf.invoke(IUiToolbarCollection._metadata, IUiToolbarCollection._item_metadata, indexOrCaption, OutArg())

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return a total number of toolbars in the collection."""
        return self._intf.get_property(IUiToolbarCollection._metadata, IUiToolbarCollection._get_count_metadata)

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _NewEnum(self) -> EnumeratorProxy:
        """Enumerates the toolbars in the collection."""
        return self._intf.get_property(IUiToolbarCollection._metadata, IUiToolbarCollection._get__NewEnum_metadata)

    _get_toolbar_by_id_metadata = { "name" : "get_toolbar_by_id",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LongArg, agmarshall.InterfaceOutArg,) }
    def get_toolbar_by_id(self, id:int) -> "UiToolbar":
        """Return a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object."""
        return self._intf.invoke(IUiToolbarCollection._metadata, IUiToolbarCollection._get_toolbar_by_id_metadata, id, OutArg())

    _get_item_by_index_metadata = { "name" : "get_item_by_index",
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "UiToolbar":
        """Retrieve a toolbar object based on the index in the collection."""
        return self._intf.invoke(IUiToolbarCollection._metadata, IUiToolbarCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "name" : "get_item_by_name",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "UiToolbar":
        """Retrieve a toolbar object based on the name of the Toolbar in the collection."""
        return self._intf.invoke(IUiToolbarCollection._metadata, IUiToolbarCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{62AA135B-4F2F-45de-94A6-31BB0984AD28}", IUiToolbarCollection)
agcls.AgTypeNameMap["IUiToolbarCollection"] = IUiToolbarCollection

class IUiWindow(object):
    """Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window."""

    _num_methods = 24
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{05F59555-F74C-48b2-AAB4-1E6C58D7AEB7}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_caption" : 1,
                             "set_caption" : 2,
                             "activate" : 3,
                             "get_window_state" : 4,
                             "set_window_state" : 5,
                             "close" : 6,
                             "get_height" : 7,
                             "set_height" : 8,
                             "get_width" : 9,
                             "set_width" : 10,
                             "get_left" : 11,
                             "set_left" : 12,
                             "get_top" : 13,
                             "set_top" : 14,
                             "get_dock_style" : 15,
                             "set_dock_style" : 16,
                             "get_no_wb_close" : 17,
                             "set_no_wb_close" : 18,
                             "get_un_pinned" : 19,
                             "set_un_pinned" : 20,
                             "get_supports_pinning" : 21,
                             "get_toolbars" : 22,
                             "get_service_by_name" : 23,
                             "get_service_by_type" : 24, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, IUiWindow)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IUiWindow)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, IUiWindow, None)
    
    _get_caption_metadata = { "name" : "caption",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def caption(self) -> str:
        """The window caption. Can only be set within UI plugins for the non unique windows they own."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_caption_metadata)

    _set_caption_metadata = { "name" : "caption",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @caption.setter
    def caption(self, caption:str) -> None:
        """The window caption. Can only be set within UI plugins for the non unique windows they own."""
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_caption_metadata, caption)

    _activate_metadata = { "name" : "activate",
            "arg_types" : (),
            "marshallers" : () }
    def activate(self) -> None:
        """Activates the window."""
        return self._intf.invoke(IUiWindow._metadata, IUiWindow._activate_metadata, )

    _get_window_state_metadata = { "name" : "window_state",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(WINDOW_STATE),) }
    @property
    def window_state(self) -> "WINDOW_STATE":
        """The window state."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_window_state_metadata)

    _set_window_state_metadata = { "name" : "window_state",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(WINDOW_STATE),) }
    @window_state.setter
    def window_state(self, newVal:"WINDOW_STATE") -> None:
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_window_state_metadata, newVal)

    _close_metadata = { "name" : "close",
            "arg_types" : (),
            "marshallers" : () }
    def close(self) -> None:
        """Close the window."""
        return self._intf.invoke(IUiWindow._metadata, IUiWindow._close_metadata, )

    _get_height_metadata = { "name" : "height",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def height(self) -> int:
        """The window height."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_height_metadata)

    _set_height_metadata = { "name" : "height",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @height.setter
    def height(self, newVal:int) -> None:
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_height_metadata, newVal)

    _get_width_metadata = { "name" : "width",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def width(self) -> int:
        """The window width."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_width_metadata)

    _set_width_metadata = { "name" : "width",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @width.setter
    def width(self, newVal:int) -> None:
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_width_metadata, newVal)

    _get_left_metadata = { "name" : "left",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def left(self) -> int:
        """The window horizontal position."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_left_metadata)

    _set_left_metadata = { "name" : "left",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @left.setter
    def left(self, newVal:int) -> None:
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_left_metadata, newVal)

    _get_top_metadata = { "name" : "top",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def top(self) -> int:
        """The window vertical position."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_top_metadata)

    _set_top_metadata = { "name" : "top",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @top.setter
    def top(self, newVal:int) -> None:
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_top_metadata, newVal)

    _get_dock_style_metadata = { "name" : "dock_style",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(DOCK_STYLE),) }
    @property
    def dock_style(self) -> "DOCK_STYLE":
        """The window docking style."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_dock_style_metadata)

    _set_dock_style_metadata = { "name" : "dock_style",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(DOCK_STYLE),) }
    @dock_style.setter
    def dock_style(self, newVal:"DOCK_STYLE") -> None:
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_dock_style_metadata, newVal)

    _get_no_wb_close_metadata = { "name" : "no_wb_close",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def no_wb_close(self) -> bool:
        """Whether to close the window when the application workbook is loaded/closed."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_no_wb_close_metadata)

    _set_no_wb_close_metadata = { "name" : "no_wb_close",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @no_wb_close.setter
    def no_wb_close(self, newVal:bool) -> None:
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_no_wb_close_metadata, newVal)

    _get_un_pinned_metadata = { "name" : "un_pinned",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def un_pinned(self) -> bool:
        """The window's pinned state."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_un_pinned_metadata)

    _set_un_pinned_metadata = { "name" : "un_pinned",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @un_pinned.setter
    def un_pinned(self, newVal:bool) -> None:
        return self._intf.set_property(IUiWindow._metadata, IUiWindow._set_un_pinned_metadata, newVal)

    _get_supports_pinning_metadata = { "name" : "supports_pinning",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def supports_pinning(self) -> bool:
        """Return whether the window supports pinning."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_supports_pinning_metadata)

    _get_toolbars_metadata = { "name" : "toolbars",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def toolbars(self) -> "UiToolbarCollection":
        """Return the window's toolbar collection."""
        return self._intf.get_property(IUiWindow._metadata, IUiWindow._get_toolbars_metadata)

    _get_service_by_name_metadata = { "name" : "get_service_by_name",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_service_by_name(self, name:str) -> typing.Any:
        """Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name."""
        return self._intf.invoke(IUiWindow._metadata, IUiWindow._get_service_by_name_metadata, name, OutArg())

    _get_service_by_type_metadata = { "name" : "get_service_by_type",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(WINDOW_SERVICE), agmarshall.InterfaceOutArg,) }
    def get_service_by_type(self, serviceType:"WINDOW_SERVICE") -> typing.Any:
        """Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type."""
        return self._intf.invoke(IUiWindow._metadata, IUiWindow._get_service_by_type_metadata, serviceType, OutArg())


agcls.AgClassCatalog.add_catalog_entry("{05F59555-F74C-48b2-AAB4-1E6C58D7AEB7}", IUiWindow)
agcls.AgTypeNameMap["IUiWindow"] = IUiWindow

class IUiWindowsCollection(object):
    """Provide methods and properties to manage the application's windows."""

    _num_methods = 7
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{4DD6FB87-C329-41a5-A359-8A9C03569635}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "item" : 1,
                             "get_count" : 2,
                             "arrange" : 3,
                             "add" : 4,
                             "get__NewEnum" : 5,
                             "get_item_by_index" : 6,
                             "get_item_by_name" : 7, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, IUiWindowsCollection)
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IUiWindowsCollection)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, IUiWindowsCollection, None)
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IUiWindow":
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def item(self, indexOrCaption:typing.Any) -> "UiWindow":
        """Retrieve a window object."""
        return self._intf.invoke(IUiWindowsCollection._metadata, IUiWindowsCollection._item_metadata, indexOrCaption, OutArg())

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return a total number of window objects in the collection."""
        return self._intf.get_property(IUiWindowsCollection._metadata, IUiWindowsCollection._get_count_metadata)

    _arrange_metadata = { "name" : "arrange",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ARRANGE_STYLE),) }
    def arrange(self, arrangeStyle:"ARRANGE_STYLE") -> None:
        """Arranges the application windows using the specified style."""
        return self._intf.invoke(IUiWindowsCollection._metadata, IUiWindowsCollection._arrange_metadata, arrangeStyle)

    _add_metadata = { "name" : "add",
            "arg_types" : (agcom.BSTR, agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def add(self, pluginID:str, initData:typing.Any) -> "UiWindow":
        """Create a new window. The bstrPluginID is a COM ProgID associated with an STK plugin."""
        return self._intf.invoke(IUiWindowsCollection._metadata, IUiWindowsCollection._add_metadata, pluginID, initData, OutArg())

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _NewEnum(self) -> EnumeratorProxy:
        """Enumerates the windows in the collection."""
        return self._intf.get_property(IUiWindowsCollection._metadata, IUiWindowsCollection._get__NewEnum_metadata)

    _get_item_by_index_metadata = { "name" : "get_item_by_index",
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "UiWindow":
        """Retrieve a window object by index in collection."""
        return self._intf.invoke(IUiWindowsCollection._metadata, IUiWindowsCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "name" : "get_item_by_name",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "UiWindow":
        """Retrieve a window object by name of window object."""
        return self._intf.invoke(IUiWindowsCollection._metadata, IUiWindowsCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{4DD6FB87-C329-41a5-A359-8A9C03569635}", IUiWindowsCollection)
agcls.AgTypeNameMap["IUiWindowsCollection"] = IUiWindowsCollection

class IUiWindowMapObject(object):
    """Represents a 2D (Map) window. Provides methods and properties to access the 2D window properties."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{A94C0929-7448-4e9e-BEB8-8F7A8F252D0D}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_map_id" : 1, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, IUiWindowMapObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IUiWindowMapObject)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, IUiWindowMapObject, None)
    
    _get_map_id_metadata = { "name" : "map_id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def map_id(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 2D map."""
        return self._intf.get_property(IUiWindowMapObject._metadata, IUiWindowMapObject._get_map_id_metadata)


agcls.AgClassCatalog.add_catalog_entry("{A94C0929-7448-4e9e-BEB8-8F7A8F252D0D}", IUiWindowMapObject)
agcls.AgTypeNameMap["IUiWindowMapObject"] = IUiWindowMapObject

class IUiWindowGlobeObject(object):
    """Represents a 3D (Globe) window. Provides methods and properties to access the 3D window properties."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{B958EDBD-0569-4596-A253-BD90328844D0}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_scene_id" : 1, }
    }
    def __init__(self, sourceObject=None):
        initialize_from_source_object(self, sourceObject, IUiWindowGlobeObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IUiWindowGlobeObject)
    def __setattr__(self, attrname, value):
        set_interface_attribute(self, attrname, value, IUiWindowGlobeObject, None)
    
    _get_scene_id_metadata = { "name" : "scene_id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def scene_id(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 3D globe."""
        return self._intf.get_property(IUiWindowGlobeObject._metadata, IUiWindowGlobeObject._get_scene_id_metadata)


agcls.AgClassCatalog.add_catalog_entry("{B958EDBD-0569-4596-A253-BD90328844D0}", IUiWindowGlobeObject)
agcls.AgTypeNameMap["IUiWindowGlobeObject"] = IUiWindowGlobeObject



class UiWindowsCollection(IUiWindowsCollection):
    """Provide methods and properties to manage the windows."""

    def __init__(self, sourceObject=None):
        IUiWindowsCollection.__init__(self, sourceObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IUiWindowsCollection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        set_class_attribute(self, attrname, value, UiWindowsCollection, [IUiWindowsCollection])

agcls.AgClassCatalog.add_catalog_entry("{82F7DB8A-A761-4C3E-95DF-37300A3738CB}", UiWindowsCollection)
agcls.AgTypeNameMap["UiWindowsCollection"] = UiWindowsCollection

class UiWindow(IUiWindow):
    """Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window."""

    def __init__(self, sourceObject=None):
        IUiWindow.__init__(self, sourceObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IUiWindow._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        set_class_attribute(self, attrname, value, UiWindow, [IUiWindow])

agcls.AgClassCatalog.add_catalog_entry("{BD72ECC3-A4A2-42FB-95AC-AE25633BB9F6}", UiWindow)
agcls.AgTypeNameMap["UiWindow"] = UiWindow

class UiToolbar(IUiToolbar):
    """Represents a toolbar abstraction. Provides methods and properties to manipulate the position and the state of the toolbar."""

    def __init__(self, sourceObject=None):
        IUiToolbar.__init__(self, sourceObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IUiToolbar._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        set_class_attribute(self, attrname, value, UiToolbar, [IUiToolbar])

agcls.AgClassCatalog.add_catalog_entry("{C20AB584-ABCC-4BF3-96D4-D2A4AA880FBB}", UiToolbar)
agcls.AgTypeNameMap["UiToolbar"] = UiToolbar

class UiToolbarCollection(IUiToolbarCollection):
    """Provide methods and properties to manage the toolbars."""

    def __init__(self, sourceObject=None):
        IUiToolbarCollection.__init__(self, sourceObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IUiToolbarCollection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        set_class_attribute(self, attrname, value, UiToolbarCollection, [IUiToolbarCollection])

agcls.AgClassCatalog.add_catalog_entry("{28F000E7-D13E-485E-8484-0BCB359BBC55}", UiToolbarCollection)
agcls.AgTypeNameMap["UiToolbarCollection"] = UiToolbarCollection

class UiWindowMapObject(IUiWindowMapObject):
    """Provide methods and properties to manipulate the 2D map."""

    def __init__(self, sourceObject=None):
        IUiWindowMapObject.__init__(self, sourceObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IUiWindowMapObject._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        set_class_attribute(self, attrname, value, UiWindowMapObject, [IUiWindowMapObject])

agcls.AgClassCatalog.add_catalog_entry("{D20C704C-0763-4CC9-9485-A2EA23C84E6B}", UiWindowMapObject)
agcls.AgTypeNameMap["UiWindowMapObject"] = UiWindowMapObject

class UiWindowGlobeObject(IUiWindowGlobeObject):
    """Provide methods and properties to manipulate the 3D globe."""

    def __init__(self, sourceObject=None):
        IUiWindowGlobeObject.__init__(self, sourceObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IUiWindowGlobeObject._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        set_class_attribute(self, attrname, value, UiWindowGlobeObject, [IUiWindowGlobeObject])

agcls.AgClassCatalog.add_catalog_entry("{4F69FA5F-30E8-4A07-9D8C-1AD163A3DE0D}", UiWindowGlobeObject)
agcls.AgTypeNameMap["UiWindowGlobeObject"] = UiWindowGlobeObject


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
