################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

"""The STK UI Core library is a COM library containing classes, interfaces and enumerations for the Application Object Model."""

__all__ = ["ARRANGE_STYLE", "DOCK_STYLE", "FLOAT_STATE", "UiToolbar", "UiToolbarCollection", "UiWindow", "UiWindowGlobeObject", 
"UiWindowMapObject", "UiWindowsCollection", "WINDOW_SERVICE", "WINDOW_STATE"]

import typing

from ctypes   import POINTER
from enum     import IntEnum

from .internal  import comutil          as agcom
from .internal  import coclassutil      as agcls
from .internal  import marshall         as agmarshall
from .internal.comutil     import IUnknown, IDispatch
from .internal.apiutil     import (InterfaceProxy, EnumeratorProxy, OutArg, 
    initialize_from_source_object, get_interface_property, set_class_attribute, 
    SupportsDeleteCallback)
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



class UiWindowsCollection(SupportsDeleteCallback):
    """Provide methods and properties to manage the application's windows."""

    _num_methods = 7
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get_count_method_offset = 2
    _arrange_method_offset = 3
    _add_method_offset = 4
    _get__NewEnum_method_offset = 5
    _get_item_by_index_method_offset = 6
    _get_item_by_name_method_offset = 7
    _metadata = {
        "iid_data" : (4730401565789584263, 3861368304027982243),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UiWindowsCollection)
    def __iter__(self):
        """Create an iterator for the UiWindowsCollection object."""
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "UiWindow":
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
    def item(self, indexOrCaption:typing.Any) -> "UiWindow":
        """Retrieve a window object."""
        return self._intf.invoke(UiWindowsCollection._metadata, UiWindowsCollection._item_metadata, indexOrCaption, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return a total number of window objects in the collection."""
        return self._intf.get_property(UiWindowsCollection._metadata, UiWindowsCollection._get_count_metadata)

    _arrange_metadata = { "offset" : _arrange_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ARRANGE_STYLE),) }
    def arrange(self, arrangeStyle:"ARRANGE_STYLE") -> None:
        """Arranges the application windows using the specified style."""
        return self._intf.invoke(UiWindowsCollection._metadata, UiWindowsCollection._arrange_metadata, arrangeStyle)

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.BSTR, agcom.Variant, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantArg, agmarshall.InterfaceOutArg,) }
    def add(self, pluginID:str, initData:typing.Any) -> "UiWindow":
        """Create a new window. The bstrPluginID is a COM ProgID associated with an STK plugin."""
        return self._intf.invoke(UiWindowsCollection._metadata, UiWindowsCollection._add_metadata, pluginID, initData, OutArg())

    _get__NewEnum_metadata = { "offset" : _get__NewEnum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _NewEnum(self) -> EnumeratorProxy:
        """Enumerates the windows in the collection."""
        return self._intf.get_property(UiWindowsCollection._metadata, UiWindowsCollection._get__NewEnum_metadata)

    _get_item_by_index_metadata = { "offset" : _get_item_by_index_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "UiWindow":
        """Retrieve a window object by index in collection."""
        return self._intf.invoke(UiWindowsCollection._metadata, UiWindowsCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "offset" : _get_item_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "UiWindow":
        """Retrieve a window object by name of window object."""
        return self._intf.invoke(UiWindowsCollection._metadata, UiWindowsCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_NewEnum] = "_NewEnum"

    def __init__(self, sourceObject=None):
        """Construct an object of type UiWindowsCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, sourceObject, UiWindowsCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiWindowsCollection, [UiWindowsCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5494012632689531786, 14643514705293336469), UiWindowsCollection)
agcls.AgTypeNameMap["UiWindowsCollection"] = UiWindowsCollection

class UiWindow(SupportsDeleteCallback):
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
    _get_no_wb_close_method_offset = 17
    _set_no_wb_close_method_offset = 18
    _get_un_pinned_method_offset = 19
    _set_un_pinned_method_offset = 20
    _get_supports_pinning_method_offset = 21
    _get_toolbars_method_offset = 22
    _get_service_by_name_method_offset = 23
    _get_service_by_type_method_offset = 24
    _metadata = {
        "iid_data" : (5238521222474863957, 13235753129659511978),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UiWindow)
    
    _get_caption_metadata = { "offset" : _get_caption_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def caption(self) -> str:
        """Get or set the window caption. Can only be set within UI plugins for the non unique windows they own."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_caption_metadata)

    _set_caption_metadata = { "offset" : _set_caption_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @caption.setter
    def caption(self, caption:str) -> None:
        """Get or set  the window caption. Can only be set within UI plugins for the non unique windows they own."""
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_caption_metadata, caption)

    _activate_metadata = { "offset" : _activate_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def activate(self) -> None:
        """Activates the window."""
        return self._intf.invoke(UiWindow._metadata, UiWindow._activate_metadata, )

    _get_window_state_metadata = { "offset" : _get_window_state_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(WINDOW_STATE),) }
    @property
    def window_state(self) -> "WINDOW_STATE":
        """The window state."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_window_state_metadata)

    _set_window_state_metadata = { "offset" : _set_window_state_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(WINDOW_STATE),) }
    @window_state.setter
    def window_state(self, newVal:"WINDOW_STATE") -> None:
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_window_state_metadata, newVal)

    _close_metadata = { "offset" : _close_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def close(self) -> None:
        """Close the window."""
        return self._intf.invoke(UiWindow._metadata, UiWindow._close_metadata, )

    _get_height_metadata = { "offset" : _get_height_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def height(self) -> int:
        """The window height."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_height_metadata)

    _set_height_metadata = { "offset" : _set_height_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @height.setter
    def height(self, newVal:int) -> None:
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_height_metadata, newVal)

    _get_width_metadata = { "offset" : _get_width_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def width(self) -> int:
        """The window width."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_width_metadata)

    _set_width_metadata = { "offset" : _set_width_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @width.setter
    def width(self, newVal:int) -> None:
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_width_metadata, newVal)

    _get_left_metadata = { "offset" : _get_left_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def left(self) -> int:
        """The window horizontal position."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_left_metadata)

    _set_left_metadata = { "offset" : _set_left_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @left.setter
    def left(self, newVal:int) -> None:
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_left_metadata, newVal)

    _get_top_metadata = { "offset" : _get_top_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def top(self) -> int:
        """The window vertical position."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_top_metadata)

    _set_top_metadata = { "offset" : _set_top_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @top.setter
    def top(self, newVal:int) -> None:
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_top_metadata, newVal)

    _get_dock_style_metadata = { "offset" : _get_dock_style_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(DOCK_STYLE),) }
    @property
    def dock_style(self) -> "DOCK_STYLE":
        """The window docking style."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_dock_style_metadata)

    _set_dock_style_metadata = { "offset" : _set_dock_style_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(DOCK_STYLE),) }
    @dock_style.setter
    def dock_style(self, newVal:"DOCK_STYLE") -> None:
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_dock_style_metadata, newVal)

    _get_no_wb_close_metadata = { "offset" : _get_no_wb_close_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def no_wb_close(self) -> bool:
        """Whether to close the window when the application workbook is loaded/closed."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_no_wb_close_metadata)

    _set_no_wb_close_metadata = { "offset" : _set_no_wb_close_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @no_wb_close.setter
    def no_wb_close(self, newVal:bool) -> None:
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_no_wb_close_metadata, newVal)

    _get_un_pinned_metadata = { "offset" : _get_un_pinned_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def un_pinned(self) -> bool:
        """The window's pinned state."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_un_pinned_metadata)

    _set_un_pinned_metadata = { "offset" : _set_un_pinned_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @un_pinned.setter
    def un_pinned(self, newVal:bool) -> None:
        return self._intf.set_property(UiWindow._metadata, UiWindow._set_un_pinned_metadata, newVal)

    _get_supports_pinning_metadata = { "offset" : _get_supports_pinning_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def supports_pinning(self) -> bool:
        """Return whether the window supports pinning."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_supports_pinning_metadata)

    _get_toolbars_metadata = { "offset" : _get_toolbars_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def toolbars(self) -> "UiToolbarCollection":
        """Return the window's toolbar collection."""
        return self._intf.get_property(UiWindow._metadata, UiWindow._get_toolbars_metadata)

    _get_service_by_name_metadata = { "offset" : _get_service_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_service_by_name(self, name:str) -> typing.Any:
        """Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name."""
        return self._intf.invoke(UiWindow._metadata, UiWindow._get_service_by_name_metadata, name, OutArg())

    _get_service_by_type_metadata = { "offset" : _get_service_by_type_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(WINDOW_SERVICE), agmarshall.InterfaceOutArg,) }
    def get_service_by_type(self, serviceType:"WINDOW_SERVICE") -> typing.Any:
        """Return a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type."""
        return self._intf.invoke(UiWindow._metadata, UiWindow._get_service_by_type_metadata, serviceType, OutArg())

    _property_names[caption] = "caption"
    _property_names[window_state] = "window_state"
    _property_names[height] = "height"
    _property_names[width] = "width"
    _property_names[left] = "left"
    _property_names[top] = "top"
    _property_names[dock_style] = "dock_style"
    _property_names[no_wb_close] = "no_wb_close"
    _property_names[un_pinned] = "un_pinned"
    _property_names[supports_pinning] = "supports_pinning"
    _property_names[toolbars] = "toolbars"

    def __init__(self, sourceObject=None):
        """Construct an object of type UiWindow."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, sourceObject, UiWindow)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiWindow, [UiWindow, ])

agcls.AgClassCatalog.add_catalog_entry((4826632444527701187, 17778306301041749141), UiWindow)
agcls.AgTypeNameMap["UiWindow"] = UiWindow

class UiToolbar(SupportsDeleteCallback):
    """Provide methods and properties to control a toolbar."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_id_method_offset = 1
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
        return get_interface_property(attrname, UiToolbar)
    
    _get_id_metadata = { "offset" : _get_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def id(self) -> int:
        """The identity."""
        return self._intf.get_property(UiToolbar._metadata, UiToolbar._get_id_metadata)

    _get_caption_metadata = { "offset" : _get_caption_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def caption(self) -> str:
        """The caption."""
        return self._intf.get_property(UiToolbar._metadata, UiToolbar._get_caption_metadata)

    _get_visible_metadata = { "offset" : _get_visible_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def visible(self) -> bool:
        """The visibility."""
        return self._intf.get_property(UiToolbar._metadata, UiToolbar._get_visible_metadata)

    _set_visible_metadata = { "offset" : _set_visible_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @visible.setter
    def visible(self, newVal:bool) -> None:
        return self._intf.set_property(UiToolbar._metadata, UiToolbar._set_visible_metadata, newVal)

    _get_float_state_metadata = { "offset" : _get_float_state_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(FLOAT_STATE),) }
    @property
    def float_state(self) -> "FLOAT_STATE":
        """The float state."""
        return self._intf.get_property(UiToolbar._metadata, UiToolbar._get_float_state_metadata)

    _set_float_state_metadata = { "offset" : _set_float_state_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(FLOAT_STATE),) }
    @float_state.setter
    def float_state(self, newVal:"FLOAT_STATE") -> None:
        return self._intf.set_property(UiToolbar._metadata, UiToolbar._set_float_state_metadata, newVal)

    _property_names[id] = "id"
    _property_names[caption] = "caption"
    _property_names[visible] = "visible"
    _property_names[float_state] = "float_state"

    def __init__(self, sourceObject=None):
        """Construct an object of type UiToolbar."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, sourceObject, UiToolbar)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiToolbar, [UiToolbar, ])

agcls.AgClassCatalog.add_catalog_entry((5472906868102444420, 13479142476234282134), UiToolbar)
agcls.AgTypeNameMap["UiToolbar"] = UiToolbar

class UiToolbarCollection(SupportsDeleteCallback):
    """Provide methods and properties to obtain a window's toolbars."""

    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get_count_method_offset = 2
    _get__NewEnum_method_offset = 3
    _get_toolbar_by_id_method_offset = 4
    _get_item_by_index_method_offset = 5
    _get_item_by_name_method_offset = 6
    _metadata = {
        "iid_data" : (5034548498384163675, 2931144109818226324),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UiToolbarCollection)
    def __iter__(self):
        """Create an iterator for the UiToolbarCollection object."""
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "UiToolbar":
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
    def item(self, indexOrCaption:typing.Any) -> "UiToolbar":
        """Retrieve a toolbar object."""
        return self._intf.invoke(UiToolbarCollection._metadata, UiToolbarCollection._item_metadata, indexOrCaption, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return a total number of toolbars in the collection."""
        return self._intf.get_property(UiToolbarCollection._metadata, UiToolbarCollection._get_count_metadata)

    _get__NewEnum_metadata = { "offset" : _get__NewEnum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _NewEnum(self) -> EnumeratorProxy:
        """Enumerates the toolbars in the collection."""
        return self._intf.get_property(UiToolbarCollection._metadata, UiToolbarCollection._get__NewEnum_metadata)

    _get_toolbar_by_id_metadata = { "offset" : _get_toolbar_by_id_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LongArg, agmarshall.InterfaceOutArg,) }
    def get_toolbar_by_id(self, id:int) -> "UiToolbar":
        """Return a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object."""
        return self._intf.invoke(UiToolbarCollection._metadata, UiToolbarCollection._get_toolbar_by_id_metadata, id, OutArg())

    _get_item_by_index_metadata = { "offset" : _get_item_by_index_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_index(self, index:int) -> "UiToolbar":
        """Retrieve a toolbar object based on the index in the collection."""
        return self._intf.invoke(UiToolbarCollection._metadata, UiToolbarCollection._get_item_by_index_metadata, index, OutArg())

    _get_item_by_name_metadata = { "offset" : _get_item_by_name_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def get_item_by_name(self, name:str) -> "UiToolbar":
        """Retrieve a toolbar object based on the name of the Toolbar in the collection."""
        return self._intf.invoke(UiToolbarCollection._metadata, UiToolbarCollection._get_item_by_name_metadata, name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_NewEnum] = "_NewEnum"

    def __init__(self, sourceObject=None):
        """Construct an object of type UiToolbarCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, sourceObject, UiToolbarCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiToolbarCollection, [UiToolbarCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5214835483446608103, 6177983444187579524), UiToolbarCollection)
agcls.AgTypeNameMap["UiToolbarCollection"] = UiToolbarCollection

class UiWindowMapObject(SupportsDeleteCallback):
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
        return get_interface_property(attrname, UiWindowMapObject)
    
    _get_map_id_metadata = { "offset" : _get_map_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def map_id(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 2D map."""
        return self._intf.get_property(UiWindowMapObject._metadata, UiWindowMapObject._get_map_id_metadata)

    _property_names[map_id] = "map_id"

    def __init__(self, sourceObject=None):
        """Construct an object of type UiWindowMapObject."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, sourceObject, UiWindowMapObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiWindowMapObject, [UiWindowMapObject, ])

agcls.AgClassCatalog.add_catalog_entry((5532961742508552268, 7732337666827650452), UiWindowMapObject)
agcls.AgTypeNameMap["UiWindowMapObject"] = UiWindowMapObject

class UiWindowGlobeObject(SupportsDeleteCallback):
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
        return get_interface_property(attrname, UiWindowGlobeObject)
    
    _get_scene_id_metadata = { "offset" : _get_scene_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def scene_id(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 3D globe."""
        return self._intf.get_property(UiWindowGlobeObject._metadata, UiWindowGlobeObject._get_scene_id_metadata)

    _property_names[scene_id] = "scene_id"

    def __init__(self, sourceObject=None):
        """Construct an object of type UiWindowGlobeObject."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, sourceObject, UiWindowGlobeObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiWindowGlobeObject, [UiWindowGlobeObject, ])

agcls.AgClassCatalog.add_catalog_entry((5334286057966533215, 999415816428096669), UiWindowGlobeObject)
agcls.AgTypeNameMap["UiWindowGlobeObject"] = UiWindowGlobeObject


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
