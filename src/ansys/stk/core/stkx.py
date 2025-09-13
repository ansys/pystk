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

"""
STK X allows developers to add advanced STK 2D, 3D visualization and analytical capabilities to applications.

The top of the STK X object model presents the following creatable components:

  * The Application component interfaces to the STK analytical engine. It can be used by itself (in a GUI-less mode), or through the Application property on the Globe and Map controls.
The main way to communicate with the engine is to send Connect commands.
Connect is a language for accessing and manipulating STK (see the
ExecuteCommand method).
The Application object also exposes connection points that you can sink to
receive notification about the state of the STK engine (for instance a
scenario has been loaded; an animation step is performed, etc.).
Notice that you can instantiate many application objects, but they all refer
to the same unique STK engine.

  * The Globe control enables you to insert a 3D view into your application.
You can use several Globe controls if you wish to have different views of the
same scenario. By default the STK keyboard and mouse interaction mechanism are
used, but various events are available, allowing your application to implement
specific keyboard and mouse interactions and modes.

  * The Map control can be used to insert a 2D view into your application.
The Map control gives your application a 2D view of the scenario. You can use
several Map controls if you wish to have different views of the same scenario.
By default the STK keyboard and mouse interaction mechanism are used, but
various events are available, allowing your application to implement specific
keyboard and mouse interactions and modes.

  * The Graphics Analysis control allows you to insert graphics analysis capability into your application. The Graphics Analysis Control can perform various analyses when set in any of the following four analysis modes.
    * Area Tool
    * AzElMask Tool
    * Obscuration Tool
    * Solar Panel Tool

.
"""

__all__ = ["ButtonValues", "DataObject", "DataObjectFiles", "Draw2DElemCollection", "Draw2DElemRect", "DrawElementCollection",
"DrawElementLine", "DrawElementRect", "FeatureCodes", "Graphics2DAnalysisMode", "Graphics2DControlBase",
"Graphics2DDrawCoordinates", "Graphics3DControlBase", "GraphicsAnalysisControlBase", "IDrawElement",
"IDrawElementCollection", "IDrawElementRect", "LoggingMode", "MouseMode", "OLEDropMode", "ObjectPathCollection",
"PickInfoData", "ProgressImageXOrigin", "ProgressImageYOrigin", "RubberBandPickInfoData", "STKXApplication",
"STKXApplicationPartnerAccess", "STKXConControlQuitReceivedEventArgs", "STKXSSLCertificateErrorEventArgs",
"ShiftValues", "ShowProgressImage", "WindowProjectionPosition"]

from ctypes import POINTER
from datetime import datetime
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
    set_interface_attribute,
)
from .internal.comutil import IDispatch, IPictureDisp
from .internal.eventutil import (
    ISTKXApplicationEventHandler,
    IUiAxGraphics2DCntrlEventHandler,
    IUiAxGraphics3DCntrlEventHandler,
)
from .stkutil import ExecuteCommandResult, ExecuteMultipleCommandsMode, ExecuteMultipleCommandsResult, LineStyle
from .utilities import colors as agcolor


class ShiftValues(IntEnum):
    """State of the Shift/Ctrl/Alt keys."""

    PRESSED = 1
    """The Shift key was pressed."""
    CTRL_PRESSED = 2
    """The Ctrl key was pressed."""
    ALT_PRESSED = 4
    """The ALT key was pressed."""

ShiftValues.PRESSED.__doc__ = "The Shift key was pressed."
ShiftValues.CTRL_PRESSED.__doc__ = "The Ctrl key was pressed."
ShiftValues.ALT_PRESSED.__doc__ = "The ALT key was pressed."

agcls.AgTypeNameMap["ShiftValues"] = ShiftValues

class ButtonValues(IntEnum):
    """Numeric value of the mouse button pressed."""

    LEFT_PRESSED = 1
    """The left button is pressed."""
    RIGHT_PRESSED = 2
    """The right button is pressed."""
    MIDDLE_PRESSED = 4
    """The middle button is pressed."""

ButtonValues.LEFT_PRESSED.__doc__ = "The left button is pressed."
ButtonValues.RIGHT_PRESSED.__doc__ = "The right button is pressed."
ButtonValues.MIDDLE_PRESSED.__doc__ = "The middle button is pressed."

agcls.AgTypeNameMap["ButtonValues"] = ButtonValues

class OLEDropMode(IntEnum):
    """Specify how to handle OLE drop operations."""

    NONE = 0
    """None. The control does not accept OLE drops and displays the No Drop cursor."""
    MANUAL = 1
    """Manual. The control triggers the OLE drop events, allowing the programmer to handle the OLE drop operation in code."""
    AUTOMATIC = 2
    """Automatic. The control automatically accepts OLE drops if the DataObject object contains data in a format it recognizes. No OLE drag/drop events on the target will occur when OLEDropMode is set to eAutomatic."""

OLEDropMode.NONE.__doc__ = "None. The control does not accept OLE drops and displays the No Drop cursor."
OLEDropMode.MANUAL.__doc__ = "Manual. The control triggers the OLE drop events, allowing the programmer to handle the OLE drop operation in code."
OLEDropMode.AUTOMATIC.__doc__ = "Automatic. The control automatically accepts OLE drops if the DataObject object contains data in a format it recognizes. No OLE drag/drop events on the target will occur when OLEDropMode is set to eAutomatic."

agcls.AgTypeNameMap["OLEDropMode"] = OLEDropMode

class MouseMode(IntEnum):
    """Mouse modes."""

    AUTOMATIC = 0
    """Automatic. The control handles the mouse events and then fires the events to the container for additional processing."""
    MANUAL = 1
    """None. No default action happens on mouse events. Events are fired to the container."""

MouseMode.AUTOMATIC.__doc__ = "Automatic. The control handles the mouse events and then fires the events to the container for additional processing."
MouseMode.MANUAL.__doc__ = "None. No default action happens on mouse events. Events are fired to the container."

agcls.AgTypeNameMap["MouseMode"] = MouseMode

class LoggingMode(IntEnum):
    """Specify the state of the log file."""

    INACTIVE = 0
    """The log file is not created."""
    ACTIVE = 1
    """The log file is created but deleted upon application termination."""
    ACTIVE_KEEP_FILE = 2
    """The log file is created and kept even after application is terminated."""

LoggingMode.INACTIVE.__doc__ = "The log file is not created."
LoggingMode.ACTIVE.__doc__ = "The log file is created but deleted upon application termination."
LoggingMode.ACTIVE_KEEP_FILE.__doc__ = "The log file is created and kept even after application is terminated."

agcls.AgTypeNameMap["LoggingMode"] = LoggingMode

class Graphics2DAnalysisMode(IntEnum):
    """Specify the mode of Gfx Analysis Control."""

    SOLAR_PANEL_TOOL = 1
    """The Solar Panel Tool mode."""
    AREA_TOOL = 2
    """The Area Tool mode."""
    OBSCURATION_TOOL = 3
    """The Obscuration Tool mode."""
    AZ_EL_MASK_TOOL = 4
    """The AzElMask Tool mode."""

Graphics2DAnalysisMode.SOLAR_PANEL_TOOL.__doc__ = "The Solar Panel Tool mode."
Graphics2DAnalysisMode.AREA_TOOL.__doc__ = "The Area Tool mode."
Graphics2DAnalysisMode.OBSCURATION_TOOL.__doc__ = "The Obscuration Tool mode."
Graphics2DAnalysisMode.AZ_EL_MASK_TOOL.__doc__ = "The AzElMask Tool mode."

agcls.AgTypeNameMap["Graphics2DAnalysisMode"] = Graphics2DAnalysisMode

class Graphics2DDrawCoordinates(IntEnum):
    """Specify the draw coordinates for Map Control."""

    PIXEL_DRAW_COORDINATES = 1
    """The draw coordinates values in pixels."""
    SCREEN_DRAW_COORDINATES = 2
    """The draw coordinates values in screen coordinates."""

Graphics2DDrawCoordinates.PIXEL_DRAW_COORDINATES.__doc__ = "The draw coordinates values in pixels."
Graphics2DDrawCoordinates.SCREEN_DRAW_COORDINATES.__doc__ = "The draw coordinates values in screen coordinates."

agcls.AgTypeNameMap["Graphics2DDrawCoordinates"] = Graphics2DDrawCoordinates

class ShowProgressImage(IntEnum):
    """Specify to show progress image."""

    NONE = 1
    """Do not show any progress Image."""
    DEFAULT = 2
    """Show the default progress image."""
    USER = 3
    """Show the user specified progress image."""

ShowProgressImage.NONE.__doc__ = "Do not show any progress Image."
ShowProgressImage.DEFAULT.__doc__ = "Show the default progress image."
ShowProgressImage.USER.__doc__ = "Show the user specified progress image."

agcls.AgTypeNameMap["ShowProgressImage"] = ShowProgressImage

class FeatureCodes(IntEnum):
    """The enumeration values are used to check availability of a given feature."""

    ENGINE_RUNTIME = 1
    """The enumeration is used to check whether the engine runtime is available."""
    GLOBE_CONTROL = 2
    """The enumeration is used to check whether the globe is available."""

FeatureCodes.ENGINE_RUNTIME.__doc__ = "The enumeration is used to check whether the engine runtime is available."
FeatureCodes.GLOBE_CONTROL.__doc__ = "The enumeration is used to check whether the globe is available."

agcls.AgTypeNameMap["FeatureCodes"] = FeatureCodes

class ProgressImageXOrigin(IntEnum):
    """Specify to align progress image X origin."""

    LEFT = 1
    """Align progress Image from X left."""
    RIGHT = 2
    """Align progress Image from X right."""
    CENTER = 3
    """Align progress Image from X center."""

ProgressImageXOrigin.LEFT.__doc__ = "Align progress Image from X left."
ProgressImageXOrigin.RIGHT.__doc__ = "Align progress Image from X right."
ProgressImageXOrigin.CENTER.__doc__ = "Align progress Image from X center."

agcls.AgTypeNameMap["ProgressImageXOrigin"] = ProgressImageXOrigin

class ProgressImageYOrigin(IntEnum):
    """Specify to align progress image Y origin."""

    TOP = 1
    """Align progress Image from Y top."""
    BOTTOM = 2
    """Align progress Image from Y bottom."""
    CENTER = 3
    """Align progress Image from Y center."""

ProgressImageYOrigin.TOP.__doc__ = "Align progress Image from Y top."
ProgressImageYOrigin.BOTTOM.__doc__ = "Align progress Image from Y bottom."
ProgressImageYOrigin.CENTER.__doc__ = "Align progress Image from Y center."

agcls.AgTypeNameMap["ProgressImageYOrigin"] = ProgressImageYOrigin


class IDrawElement(object):
    """Draw element."""

    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_visible_method_offset = 1
    _set_visible_method_offset = 2
    _metadata = {
        "iid_data" : (5628420527828914297, 11851369920546476691),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IDrawElement."""
        initialize_from_source_object(self, source_object, IDrawElement)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IDrawElement)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IDrawElement, None)

    _get_visible_metadata = { "offset" : _get_visible_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def visible(self) -> bool:
        """Show or hide the element."""
        return self._intf.get_property(IDrawElement._metadata, IDrawElement._get_visible_metadata)

    _set_visible_metadata = { "offset" : _set_visible_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @visible.setter
    def visible(self, value:bool) -> None:
        return self._intf.set_property(IDrawElement._metadata, IDrawElement._set_visible_metadata, value)

    _property_names[visible] = "visible"


agcls.AgClassCatalog.add_catalog_entry((5628420527828914297, 11851369920546476691), IDrawElement)
agcls.AgTypeNameMap["IDrawElement"] = IDrawElement

class IDrawElementRect(IDrawElement):
    """Define a rectangle in control coordinates."""

    _num_methods = 11
    _vtable_offset = IDrawElement._vtable_offset + IDrawElement._num_methods
    _get_left_method_offset = 1
    _get_right_method_offset = 2
    _get_top_method_offset = 3
    _get_bottom_method_offset = 4
    _set_method_offset = 5
    _get_color_method_offset = 6
    _set_color_method_offset = 7
    _get_line_width_method_offset = 8
    _set_line_width_method_offset = 9
    _get_line_style_method_offset = 10
    _set_line_style_method_offset = 11
    _metadata = {
        "iid_data" : (5760057209317875442, 11089162376366659215),
        "vtable_reference" : IDrawElement._vtable_offset + IDrawElement._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IDrawElementRect."""
        initialize_from_source_object(self, source_object, IDrawElementRect)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDrawElement._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IDrawElementRect)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IDrawElementRect, IDrawElement)

    _get_left_metadata = { "offset" : _get_left_method_offset,
            "arg_types" : (POINTER(agcom.OLE_XPOS_PIXELS),),
            "marshallers" : (agmarshall.OLEXPosPixelsArg,) }
    @property
    def left(self) -> int:
        """The x-coordinate of the left edge of this rectangle."""
        return self._intf.get_property(IDrawElementRect._metadata, IDrawElementRect._get_left_metadata)

    _get_right_metadata = { "offset" : _get_right_method_offset,
            "arg_types" : (POINTER(agcom.OLE_XPOS_PIXELS),),
            "marshallers" : (agmarshall.OLEXPosPixelsArg,) }
    @property
    def right(self) -> int:
        """The x-coordinate of the right edge of this rectangle."""
        return self._intf.get_property(IDrawElementRect._metadata, IDrawElementRect._get_right_metadata)

    _get_top_metadata = { "offset" : _get_top_method_offset,
            "arg_types" : (POINTER(agcom.OLE_YPOS_PIXELS),),
            "marshallers" : (agmarshall.OLEYPosPixelsArg,) }
    @property
    def top(self) -> int:
        """The y-coordinate of the top edge of this rectangle."""
        return self._intf.get_property(IDrawElementRect._metadata, IDrawElementRect._get_top_metadata)

    _get_bottom_metadata = { "offset" : _get_bottom_method_offset,
            "arg_types" : (POINTER(agcom.OLE_YPOS_PIXELS),),
            "marshallers" : (agmarshall.OLEYPosPixelsArg,) }
    @property
    def bottom(self) -> int:
        """The y-coordinate of the bottom edge of this rectangle."""
        return self._intf.get_property(IDrawElementRect._metadata, IDrawElementRect._get_bottom_metadata)

    _set_metadata = { "offset" : _set_method_offset,
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS,),
            "marshallers" : (agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg, agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg,) }
    def set(self, left:int, top:int, right:int, bottom:int) -> None:
        """Set the rectangle coordinates."""
        return self._intf.invoke(IDrawElementRect._metadata, IDrawElementRect._set_metadata, left, top, right, bottom)

    _get_color_metadata = { "offset" : _get_color_method_offset,
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @property
    def color(self) -> agcolor.Color:
        """Color of the rectangle."""
        return self._intf.get_property(IDrawElementRect._metadata, IDrawElementRect._get_color_metadata)

    _set_color_metadata = { "offset" : _set_color_method_offset,
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @color.setter
    def color(self, value:agcolor.Color) -> None:
        return self._intf.set_property(IDrawElementRect._metadata, IDrawElementRect._set_color_metadata, value)

    _get_line_width_metadata = { "offset" : _get_line_width_method_offset,
            "arg_types" : (POINTER(agcom.FLOAT),),
            "marshallers" : (agmarshall.FloatArg,) }
    @property
    def line_width(self) -> float:
        """Specify the width of the line."""
        return self._intf.get_property(IDrawElementRect._metadata, IDrawElementRect._get_line_width_metadata)

    _set_line_width_metadata = { "offset" : _set_line_width_method_offset,
            "arg_types" : (agcom.FLOAT,),
            "marshallers" : (agmarshall.FloatArg,) }
    @line_width.setter
    def line_width(self, value:float) -> None:
        return self._intf.set_property(IDrawElementRect._metadata, IDrawElementRect._set_line_width_metadata, value)

    _get_line_style_metadata = { "offset" : _get_line_style_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(LineStyle),) }
    @property
    def line_style(self) -> "LineStyle":
        """Specify the style of the line."""
        return self._intf.get_property(IDrawElementRect._metadata, IDrawElementRect._get_line_style_metadata)

    _set_line_style_metadata = { "offset" : _set_line_style_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(LineStyle),) }
    @line_style.setter
    def line_style(self, value:"LineStyle") -> None:
        return self._intf.set_property(IDrawElementRect._metadata, IDrawElementRect._set_line_style_metadata, value)

    _property_names[left] = "left"
    _property_names[right] = "right"
    _property_names[top] = "top"
    _property_names[bottom] = "bottom"
    _property_names[color] = "color"
    _property_names[line_width] = "line_width"
    _property_names[line_style] = "line_style"


agcls.AgClassCatalog.add_catalog_entry((5760057209317875442, 11089162376366659215), IDrawElementRect)
agcls.AgTypeNameMap["IDrawElementRect"] = IDrawElementRect

class IDrawElementCollection(object):
    """Collection of elements to draw on the control."""

    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _clear_method_offset = 4
    _add_method_offset = 5
    _remove_method_offset = 6
    _get_visible_method_offset = 7
    _set_visible_method_offset = 8
    _metadata = {
        "iid_data" : (5260087635497314219, 16347332931743479485),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IDrawElementCollection."""
        initialize_from_source_object(self, source_object, IDrawElementCollection)
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IDrawElementCollection)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IDrawElementCollection, None)
    def __iter__(self):
        """Create an iterator for the IDrawElementCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IDrawElement":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(IDrawElementCollection._metadata, IDrawElementCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LongArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "IDrawElement":
        """Get the element at the specified index (0-based)."""
        return self._intf.invoke(IDrawElementCollection._metadata, IDrawElementCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an object that can be used to iterate through all the strings in the collection."""
        return self._intf.get_property(IDrawElementCollection._metadata, IDrawElementCollection._get__new_enum_metadata)

    _clear_metadata = { "offset" : _clear_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def clear(self) -> None:
        """Clear the contents of the collection and updates the display."""
        return self._intf.invoke(IDrawElementCollection._metadata, IDrawElementCollection._clear_metadata, )

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def add(self, elem_type:str) -> "IDrawElement":
        """Create and add a new element to the end of the sequence."""
        return self._intf.invoke(IDrawElementCollection._metadata, IDrawElementCollection._add_metadata, elem_type, OutArg())

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("IDrawElement"),) }
    def remove(self, draw_elem:"IDrawElement") -> None:
        """Remove the specified element."""
        return self._intf.invoke(IDrawElementCollection._metadata, IDrawElementCollection._remove_metadata, draw_elem)

    _get_visible_metadata = { "offset" : _get_visible_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def visible(self) -> bool:
        """Show or hide all the elements."""
        return self._intf.get_property(IDrawElementCollection._metadata, IDrawElementCollection._get_visible_metadata)

    _set_visible_metadata = { "offset" : _set_visible_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @visible.setter
    def visible(self, value:bool) -> None:
        return self._intf.set_property(IDrawElementCollection._metadata, IDrawElementCollection._set_visible_metadata, value)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"
    _property_names[visible] = "visible"


agcls.AgClassCatalog.add_catalog_entry((5260087635497314219, 16347332931743479485), IDrawElementCollection)
agcls.AgTypeNameMap["IDrawElementCollection"] = IDrawElementCollection



class Graphics3DControlBase(SupportsDeleteCallback):
    """AGI Globe control."""

    _num_methods = 46
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_back_color_method_offset = 1
    _set_back_color_method_offset = 2
    _get_picture_method_offset = 3
    _picture_put_reference_method_offset = 4
    _set_picture_method_offset = 5
    _pick_info_method_offset = 6
    _get_window_id_method_offset = 7
    _set_window_id_method_offset = 8
    _get_application_method_offset = 9
    _zoom_in_method_offset = 10
    _get_no_logo_method_offset = 11
    _set_no_logo_method_offset = 12
    _get_ole_drop_mode_method_offset = 13
    _set_ole_drop_mode_method_offset = 14
    _rubber_band_pick_info_method_offset = 15
    _get_mouse_mode_method_offset = 16
    _set_mouse_mode_method_offset = 17
    _get_draw_elements_method_offset = 18
    _get_ready_state_method_offset = 19
    _get_ppt_preload_mode_method_offset = 20
    _set_ppt_preload_mode_method_offset = 21
    _get_advanced_pick_mode_method_offset = 22
    _set_advanced_pick_mode_method_offset = 23
    _copy_from_window_id_method_offset = 24
    _start_object_editing_method_offset = 25
    _apply_object_editing_method_offset = 26
    _stop_object_editing_method_offset = 27
    _get_is_object_editing_method_offset = 28
    _get_in_zoom_mode_method_offset = 29
    _set_mouse_cursor_from_file_method_offset = 30
    _restore_mouse_cursor_method_offset = 31
    _set_mouse_cursor_from_handle_method_offset = 32
    _get_show_progress_image_method_offset = 33
    _set_show_progress_image_method_offset = 34
    _get_progress_image_x_offset_method_offset = 35
    _set_progress_image_x_offset_method_offset = 36
    _get_progress_image_y_offset_method_offset = 37
    _set_progress_image_y_offset_method_offset = 38
    _get_progress_image_file_method_offset = 39
    _set_progress_image_file_method_offset = 40
    _get_progress_image_x_origin_method_offset = 41
    _set_progress_image_x_origin_method_offset = 42
    _get_progress_image_y_origin_method_offset = 43
    _set_progress_image_y_origin_method_offset = 44
    _get_picture_from_file_method_offset = 45
    _set_picture_from_file_method_offset = 46
    _metadata = {
        "iid_data" : (5755316323156254440, 16340472556888379575),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Graphics3DControlBase)
    def subscribe(self) -> IUiAxGraphics3DCntrlEventHandler:
        """Return an IUiAxGraphics3DCntrlEventHandler that is subscribed to handle events associated with this instance of Graphics3DControlBase."""
        return IUiAxGraphics3DCntrlEventHandler(self._intf)

    _get_back_color_metadata = { "offset" : _get_back_color_method_offset,
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_back_color_metadata)

    _set_back_color_metadata = { "offset" : _set_back_color_method_offset,
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_back_color_metadata, clr)

    _get_picture_metadata = { "offset" : _get_picture_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    @property
    def picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_picture_metadata)

    _picture_put_reference_metadata = { "offset" : _picture_put_reference_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    def picture_put_reference(self, picture:IPictureDisp) -> None:
        """Set a reference to the splash logo graphic to be displayed in the control."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._picture_put_reference_metadata, picture)

    _set_picture_metadata = { "offset" : _set_picture_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    @picture.setter
    def picture(self, picture:IPictureDisp) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_picture_metadata, picture)

    _pick_info_metadata = { "offset" : _pick_info_method_offset,
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg, agmarshall.InterfaceOutArg,) }
    def pick_info(self, x:int, y:int) -> "PickInfoData":
        """Get detailed information about a mouse pick."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._pick_info_metadata, x, y, OutArg())

    _get_window_id_metadata = { "offset" : _get_window_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def window_id(self) -> int:
        """Window identifier (for Connect commands)."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_window_id_metadata)

    _set_window_id_metadata = { "offset" : _set_window_id_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @window_id.setter
    def window_id(self, value:int) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_window_id_metadata, value)

    _get_application_metadata = { "offset" : _get_application_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def application(self) -> "STKXApplication":
        """Reference to the STK X application object."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_application_metadata)

    _zoom_in_metadata = { "offset" : _zoom_in_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def zoom_in(self) -> None:
        """Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._zoom_in_metadata, )

    _get_no_logo_metadata = { "offset" : _get_no_logo_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_no_logo_metadata)

    _set_no_logo_metadata = { "offset" : _set_no_logo_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @no_logo.setter
    def no_logo(self, no_logo:bool) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_no_logo_metadata, no_logo)

    _get_ole_drop_mode_metadata = { "offset" : _get_ole_drop_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(OLEDropMode),) }
    @property
    def ole_drop_mode(self) -> "OLEDropMode":
        """How the control handles drop operations."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_ole_drop_mode_metadata)

    _set_ole_drop_mode_metadata = { "offset" : _set_ole_drop_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(OLEDropMode),) }
    @ole_drop_mode.setter
    def ole_drop_mode(self, ole_drop_mode:"OLEDropMode") -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_ole_drop_mode_metadata, ole_drop_mode)

    _rubber_band_pick_info_metadata = { "offset" : _rubber_band_pick_info_method_offset,
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg, agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg, agmarshall.InterfaceOutArg,) }
    def rubber_band_pick_info(self, left:int, top:int, right:int, bottom:int) -> "RubberBandPickInfoData":
        """Get detailed information about a rubber-band mouse pick. The values must be within the VO window (0 to width-1 for left and right, 0 to height-1 for top and bottom)."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._rubber_band_pick_info_metadata, left, top, right, bottom, OutArg())

    _get_mouse_mode_metadata = { "offset" : _get_mouse_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(MouseMode),) }
    @property
    def mouse_mode(self) -> "MouseMode":
        """Whether this control responds to mouse events."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_mouse_mode_metadata)

    _set_mouse_mode_metadata = { "offset" : _set_mouse_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(MouseMode),) }
    @mouse_mode.setter
    def mouse_mode(self, mouse_mode:"MouseMode") -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_mouse_mode_metadata, mouse_mode)

    _get_draw_elements_metadata = { "offset" : _get_draw_elements_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def draw_elements(self) -> "IDrawElementCollection":
        """Elements to draw on the control."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_draw_elements_metadata)

    _get_ready_state_metadata = { "offset" : _get_ready_state_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def ready_state(self) -> int:
        """Return/sets the background color of the control."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_ready_state_metadata)

    _get_ppt_preload_mode_metadata = { "offset" : _get_ppt_preload_mode_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def ppt_preload_mode(self) -> bool:
        """Special mode for PowerPoint : if true the VO control window is kept around when switching between slides."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_ppt_preload_mode_metadata)

    _set_ppt_preload_mode_metadata = { "offset" : _set_ppt_preload_mode_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @ppt_preload_mode.setter
    def ppt_preload_mode(self, ppt_preload_mode:bool) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_ppt_preload_mode_metadata, ppt_preload_mode)

    _get_advanced_pick_mode_metadata = { "offset" : _get_advanced_pick_mode_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def advanced_pick_mode(self) -> bool:
        """If true, sets the advance pick mode."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_advanced_pick_mode_metadata)

    _set_advanced_pick_mode_metadata = { "offset" : _set_advanced_pick_mode_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @advanced_pick_mode.setter
    def advanced_pick_mode(self, advanced_pick_mode:bool) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_advanced_pick_mode_metadata, advanced_pick_mode)

    _copy_from_window_id_metadata = { "offset" : _copy_from_window_id_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    def copy_from_window_id(self, win_id:int) -> None:
        """Copy an existing Window's scene into this control."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._copy_from_window_id_metadata, win_id)

    _start_object_editing_metadata = { "offset" : _start_object_editing_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def start_object_editing(self, obj_edit_path:str) -> None:
        """Enters into 3D object editing mode."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._start_object_editing_metadata, obj_edit_path)

    _apply_object_editing_metadata = { "offset" : _apply_object_editing_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def apply_object_editing(self) -> None:
        """Commit changes when in 3D object editing mode."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._apply_object_editing_metadata, )

    _stop_object_editing_metadata = { "offset" : _stop_object_editing_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    def stop_object_editing(self, canceled:bool) -> None:
        """End 3D object editing mode."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._stop_object_editing_metadata, canceled)

    _get_is_object_editing_metadata = { "offset" : _get_is_object_editing_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def is_object_editing(self) -> bool:
        """Return true if in 3D object editing mode."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_is_object_editing_metadata)

    _get_in_zoom_mode_metadata = { "offset" : _get_in_zoom_mode_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def in_zoom_mode(self) -> bool:
        """Return true if in zoom in mode."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_in_zoom_mode_metadata)

    _set_mouse_cursor_from_file_metadata = { "offset" : _set_mouse_cursor_from_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def set_mouse_cursor_from_file(self, cursor_file_name:str) -> None:
        """Set mouse cursor to the selected cursor file."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._set_mouse_cursor_from_file_metadata, cursor_file_name)

    _restore_mouse_cursor_metadata = { "offset" : _restore_mouse_cursor_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def restore_mouse_cursor(self) -> None:
        """Restores mouse cursor back to normal."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._restore_mouse_cursor_metadata, )

    _set_mouse_cursor_from_handle_metadata = { "offset" : _set_mouse_cursor_from_handle_method_offset,
            "arg_types" : (agcom.OLE_HANDLE,),
            "marshallers" : (agmarshall.OLEHandleArg,) }
    def set_mouse_cursor_from_handle(self, cursor_handle:int) -> None:
        """Set mouse cursor to the passed cursor handle."""
        return self._intf.invoke(Graphics3DControlBase._metadata, Graphics3DControlBase._set_mouse_cursor_from_handle_metadata, cursor_handle)

    _get_show_progress_image_metadata = { "offset" : _get_show_progress_image_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ShowProgressImage),) }
    @property
    def show_progress_image(self) -> "ShowProgressImage":
        """The animated progress image type."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_show_progress_image_metadata)

    _set_show_progress_image_metadata = { "offset" : _set_show_progress_image_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ShowProgressImage),) }
    @show_progress_image.setter
    def show_progress_image(self, progress_image:"ShowProgressImage") -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_show_progress_image_metadata, progress_image)

    _get_progress_image_x_offset_metadata = { "offset" : _get_progress_image_x_offset_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def progress_image_x_offset(self) -> int:
        """The horizontal X offset for animated progress image."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_progress_image_x_offset_metadata)

    _set_progress_image_x_offset_metadata = { "offset" : _set_progress_image_x_offset_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @progress_image_x_offset.setter
    def progress_image_x_offset(self, x_offset:int) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_progress_image_x_offset_metadata, x_offset)

    _get_progress_image_y_offset_metadata = { "offset" : _get_progress_image_y_offset_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def progress_image_y_offset(self) -> int:
        """The vertical Y offset for animated progress image."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_progress_image_y_offset_metadata)

    _set_progress_image_y_offset_metadata = { "offset" : _set_progress_image_y_offset_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @progress_image_y_offset.setter
    def progress_image_y_offset(self, y_offset:int) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_progress_image_y_offset_metadata, y_offset)

    _get_progress_image_file_metadata = { "offset" : _get_progress_image_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def progress_image_file(self) -> str:
        """The complete image file name/path for animated progress image."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_progress_image_file_metadata)

    _set_progress_image_file_metadata = { "offset" : _set_progress_image_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @progress_image_file.setter
    def progress_image_file(self, image_file:str) -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_progress_image_file_metadata, image_file)

    _get_progress_image_x_origin_metadata = { "offset" : _get_progress_image_x_origin_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ProgressImageXOrigin),) }
    @property
    def progress_image_x_origin(self) -> "ProgressImageXOrigin":
        """The X origin alignment for animated progress image."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_progress_image_x_origin_metadata)

    _set_progress_image_x_origin_metadata = { "offset" : _set_progress_image_x_origin_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ProgressImageXOrigin),) }
    @progress_image_x_origin.setter
    def progress_image_x_origin(self, progress_image_x_origin:"ProgressImageXOrigin") -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_progress_image_x_origin_metadata, progress_image_x_origin)

    _get_progress_image_y_origin_metadata = { "offset" : _get_progress_image_y_origin_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ProgressImageYOrigin),) }
    @property
    def progress_image_y_origin(self) -> "ProgressImageYOrigin":
        """The Y origin alignment for animated progress image."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_progress_image_y_origin_metadata)

    _set_progress_image_y_origin_metadata = { "offset" : _set_progress_image_y_origin_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ProgressImageYOrigin),) }
    @progress_image_y_origin.setter
    def progress_image_y_origin(self, progress_image_y_origin:"ProgressImageYOrigin") -> None:
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_progress_image_y_origin_metadata, progress_image_y_origin)

    _get_picture_from_file_metadata = { "offset" : _get_picture_from_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def picture_from_file(self) -> str:
        """Get or set the splash logo graphic file to be displayed in the control."""
        return self._intf.get_property(Graphics3DControlBase._metadata, Graphics3DControlBase._get_picture_from_file_metadata)

    _set_picture_from_file_metadata = { "offset" : _set_picture_from_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @picture_from_file.setter
    def picture_from_file(self, picture_file:str) -> None:
        """Get or set the splash logo graphic file to be displayed in the control."""
        return self._intf.set_property(Graphics3DControlBase._metadata, Graphics3DControlBase._set_picture_from_file_metadata, picture_file)

    _property_names[back_color] = "back_color"
    _property_names[picture] = "picture"
    _property_names[window_id] = "window_id"
    _property_names[application] = "application"
    _property_names[no_logo] = "no_logo"
    _property_names[ole_drop_mode] = "ole_drop_mode"
    _property_names[mouse_mode] = "mouse_mode"
    _property_names[draw_elements] = "draw_elements"
    _property_names[ready_state] = "ready_state"
    _property_names[ppt_preload_mode] = "ppt_preload_mode"
    _property_names[advanced_pick_mode] = "advanced_pick_mode"
    _property_names[is_object_editing] = "is_object_editing"
    _property_names[in_zoom_mode] = "in_zoom_mode"
    _property_names[show_progress_image] = "show_progress_image"
    _property_names[progress_image_x_offset] = "progress_image_x_offset"
    _property_names[progress_image_y_offset] = "progress_image_y_offset"
    _property_names[progress_image_file] = "progress_image_file"
    _property_names[progress_image_x_origin] = "progress_image_x_origin"
    _property_names[progress_image_y_origin] = "progress_image_y_origin"
    _property_names[picture_from_file] = "picture_from_file"

    def __init__(self, source_object=None):
        """Construct an object of type Graphics3DControlBase."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Graphics3DControlBase)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Graphics3DControlBase, [Graphics3DControlBase, ])

agcls.AgClassCatalog.add_catalog_entry((4702692981507542637, 14841496120833509769), Graphics3DControlBase)
agcls.AgTypeNameMap["Graphics3DControlBase"] = Graphics3DControlBase

class Graphics2DControlBase(SupportsDeleteCallback):
    """AGI Map control."""

    _num_methods = 43
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_back_color_method_offset = 1
    _set_back_color_method_offset = 2
    _get_picture_method_offset = 3
    _picture_put_reference_method_offset = 4
    _set_picture_method_offset = 5
    _get_window_id_method_offset = 6
    _set_window_id_method_offset = 7
    _zoom_in_method_offset = 8
    _zoom_out_method_offset = 9
    _pick_info_method_offset = 10
    _get_application_method_offset = 11
    _get_no_logo_method_offset = 12
    _set_no_logo_method_offset = 13
    _get_ole_drop_mode_method_offset = 14
    _set_ole_drop_mode_method_offset = 15
    _get_mouse_mode_method_offset = 16
    _set_mouse_mode_method_offset = 17
    _get_ready_state_method_offset = 18
    _copy_from_window_id_method_offset = 19
    _rubber_band_pick_info_method_offset = 20
    _get_advanced_pick_mode_method_offset = 21
    _set_advanced_pick_mode_method_offset = 22
    _get_window_projected_position_method_offset = 23
    _get_in_zoom_mode_method_offset = 24
    _set_mouse_cursor_from_file_method_offset = 25
    _restore_mouse_cursor_method_offset = 26
    _set_mouse_cursor_from_handle_method_offset = 27
    _get_show_progress_image_method_offset = 28
    _set_show_progress_image_method_offset = 29
    _get_progress_image_x_offset_method_offset = 30
    _set_progress_image_x_offset_method_offset = 31
    _get_progress_image_y_offset_method_offset = 32
    _set_progress_image_y_offset_method_offset = 33
    _get_progress_image_file_method_offset = 34
    _set_progress_image_file_method_offset = 35
    _get_progress_image_x_origin_method_offset = 36
    _set_progress_image_x_origin_method_offset = 37
    _get_progress_image_y_origin_method_offset = 38
    _set_progress_image_y_origin_method_offset = 39
    _get_picture_from_file_method_offset = 40
    _set_picture_from_file_method_offset = 41
    _get_pan_mode_enabled_method_offset = 42
    _set_pan_mode_enabled_method_offset = 43
    _metadata = {
        "iid_data" : (5050754371719525381, 2220746668469695642),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Graphics2DControlBase)
    def subscribe(self) -> IUiAxGraphics2DCntrlEventHandler:
        """Return an IUiAxGraphics2DCntrlEventHandler that is subscribed to handle events associated with this instance of Graphics2DControlBase."""
        return IUiAxGraphics2DCntrlEventHandler(self._intf)

    _get_back_color_metadata = { "offset" : _get_back_color_method_offset,
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_back_color_metadata)

    _set_back_color_metadata = { "offset" : _set_back_color_method_offset,
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_back_color_metadata, clr)

    _get_picture_metadata = { "offset" : _get_picture_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    @property
    def picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_picture_metadata)

    _picture_put_reference_metadata = { "offset" : _picture_put_reference_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    def picture_put_reference(self, picture:IPictureDisp) -> None:
        """Set a reference to the splash logo graphic to be displayed in the control."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._picture_put_reference_metadata, picture)

    _set_picture_metadata = { "offset" : _set_picture_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    @picture.setter
    def picture(self, picture:IPictureDisp) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_picture_metadata, picture)

    _get_window_id_metadata = { "offset" : _get_window_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def window_id(self) -> int:
        """Window identifier (for Connect commands)."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_window_id_metadata)

    _set_window_id_metadata = { "offset" : _set_window_id_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @window_id.setter
    def window_id(self, value:int) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_window_id_metadata, value)

    _zoom_in_metadata = { "offset" : _zoom_in_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def zoom_in(self) -> None:
        """Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._zoom_in_metadata, )

    _zoom_out_metadata = { "offset" : _zoom_out_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def zoom_out(self) -> None:
        """Zoom out to view a larger portion of a previously magnified map."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._zoom_out_metadata, )

    _pick_info_metadata = { "offset" : _pick_info_method_offset,
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg, agmarshall.InterfaceOutArg,) }
    def pick_info(self, x:int, y:int) -> "PickInfoData":
        """Get detailed information about a mouse pick."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._pick_info_metadata, x, y, OutArg())

    _get_application_metadata = { "offset" : _get_application_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def application(self) -> "STKXApplication":
        """Reference to the STK X application object."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_application_metadata)

    _get_no_logo_metadata = { "offset" : _get_no_logo_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_no_logo_metadata)

    _set_no_logo_metadata = { "offset" : _set_no_logo_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @no_logo.setter
    def no_logo(self, no_logo:bool) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_no_logo_metadata, no_logo)

    _get_ole_drop_mode_metadata = { "offset" : _get_ole_drop_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(OLEDropMode),) }
    @property
    def ole_drop_mode(self) -> "OLEDropMode":
        """How the control handles drop operations."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_ole_drop_mode_metadata)

    _set_ole_drop_mode_metadata = { "offset" : _set_ole_drop_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(OLEDropMode),) }
    @ole_drop_mode.setter
    def ole_drop_mode(self, ole_drop_mode:"OLEDropMode") -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_ole_drop_mode_metadata, ole_drop_mode)

    _get_mouse_mode_metadata = { "offset" : _get_mouse_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(MouseMode),) }
    @property
    def mouse_mode(self) -> "MouseMode":
        """Whether this control responds to mouse events."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_mouse_mode_metadata)

    _set_mouse_mode_metadata = { "offset" : _set_mouse_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(MouseMode),) }
    @mouse_mode.setter
    def mouse_mode(self, mouse_mode:"MouseMode") -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_mouse_mode_metadata, mouse_mode)

    _get_ready_state_metadata = { "offset" : _get_ready_state_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def ready_state(self) -> int:
        """Return/sets the background color of the control."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_ready_state_metadata)

    _copy_from_window_id_metadata = { "offset" : _copy_from_window_id_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    def copy_from_window_id(self, win_id:int) -> None:
        """Copy an existing Window's scene into this control."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._copy_from_window_id_metadata, win_id)

    _rubber_band_pick_info_metadata = { "offset" : _rubber_band_pick_info_method_offset,
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg, agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg, agmarshall.InterfaceOutArg,) }
    def rubber_band_pick_info(self, left:int, top:int, right:int, bottom:int) -> "RubberBandPickInfoData":
        """Get detailed information about a rubber-band mouse pick. The values must be within the 2D window (0 to width-1 for left and right, 0 to height-1 for top and bottom)."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._rubber_band_pick_info_metadata, left, top, right, bottom, OutArg())

    _get_advanced_pick_mode_metadata = { "offset" : _get_advanced_pick_mode_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def advanced_pick_mode(self) -> bool:
        """If true, sets the advance pick mode."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_advanced_pick_mode_metadata)

    _set_advanced_pick_mode_metadata = { "offset" : _set_advanced_pick_mode_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @advanced_pick_mode.setter
    def advanced_pick_mode(self, advanced_pick_mode:bool) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_advanced_pick_mode_metadata, advanced_pick_mode)

    _get_window_projected_position_metadata = { "offset" : _get_window_projected_position_method_offset,
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.EnumArg(Graphics2DDrawCoordinates), agmarshall.InterfaceOutArg,) }
    def get_window_projected_position(self, lat:float, lon:float, alt:float, draw_coords:"Graphics2DDrawCoordinates") -> "WindowProjectionPosition":
        """Get the window projected position for given values."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._get_window_projected_position_metadata, lat, lon, alt, draw_coords, OutArg())

    _get_in_zoom_mode_metadata = { "offset" : _get_in_zoom_mode_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def in_zoom_mode(self) -> bool:
        """Return true if in zoom in mode."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_in_zoom_mode_metadata)

    _set_mouse_cursor_from_file_metadata = { "offset" : _set_mouse_cursor_from_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def set_mouse_cursor_from_file(self, cursor_file_name:str) -> None:
        """Set mouse cursor to the selected cursor file."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._set_mouse_cursor_from_file_metadata, cursor_file_name)

    _restore_mouse_cursor_metadata = { "offset" : _restore_mouse_cursor_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def restore_mouse_cursor(self) -> None:
        """Restores mouse cursor back to normal."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._restore_mouse_cursor_metadata, )

    _set_mouse_cursor_from_handle_metadata = { "offset" : _set_mouse_cursor_from_handle_method_offset,
            "arg_types" : (agcom.OLE_HANDLE,),
            "marshallers" : (agmarshall.OLEHandleArg,) }
    def set_mouse_cursor_from_handle(self, cursor_handle:int) -> None:
        """Set mouse cursor to the passed cursor handle."""
        return self._intf.invoke(Graphics2DControlBase._metadata, Graphics2DControlBase._set_mouse_cursor_from_handle_metadata, cursor_handle)

    _get_show_progress_image_metadata = { "offset" : _get_show_progress_image_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ShowProgressImage),) }
    @property
    def show_progress_image(self) -> "ShowProgressImage":
        """The animated progress image type."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_show_progress_image_metadata)

    _set_show_progress_image_metadata = { "offset" : _set_show_progress_image_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ShowProgressImage),) }
    @show_progress_image.setter
    def show_progress_image(self, progress_image:"ShowProgressImage") -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_show_progress_image_metadata, progress_image)

    _get_progress_image_x_offset_metadata = { "offset" : _get_progress_image_x_offset_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def progress_image_x_offset(self) -> int:
        """The horizontal X offset for animated progress image."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_progress_image_x_offset_metadata)

    _set_progress_image_x_offset_metadata = { "offset" : _set_progress_image_x_offset_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @progress_image_x_offset.setter
    def progress_image_x_offset(self, x_offset:int) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_progress_image_x_offset_metadata, x_offset)

    _get_progress_image_y_offset_metadata = { "offset" : _get_progress_image_y_offset_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def progress_image_y_offset(self) -> int:
        """The vertical Y offset for animated progress image."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_progress_image_y_offset_metadata)

    _set_progress_image_y_offset_metadata = { "offset" : _set_progress_image_y_offset_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @progress_image_y_offset.setter
    def progress_image_y_offset(self, y_offset:int) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_progress_image_y_offset_metadata, y_offset)

    _get_progress_image_file_metadata = { "offset" : _get_progress_image_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def progress_image_file(self) -> str:
        """The complete image file name/path for animated progress image."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_progress_image_file_metadata)

    _set_progress_image_file_metadata = { "offset" : _set_progress_image_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @progress_image_file.setter
    def progress_image_file(self, image_file:str) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_progress_image_file_metadata, image_file)

    _get_progress_image_x_origin_metadata = { "offset" : _get_progress_image_x_origin_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ProgressImageXOrigin),) }
    @property
    def progress_image_x_origin(self) -> "ProgressImageXOrigin":
        """The X origin alignment for animated progress image."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_progress_image_x_origin_metadata)

    _set_progress_image_x_origin_metadata = { "offset" : _set_progress_image_x_origin_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ProgressImageXOrigin),) }
    @progress_image_x_origin.setter
    def progress_image_x_origin(self, progress_image_x_origin:"ProgressImageXOrigin") -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_progress_image_x_origin_metadata, progress_image_x_origin)

    _get_progress_image_y_origin_metadata = { "offset" : _get_progress_image_y_origin_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ProgressImageYOrigin),) }
    @property
    def progress_image_y_origin(self) -> "ProgressImageYOrigin":
        """The Y origin alignment for animated progress image."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_progress_image_y_origin_metadata)

    _set_progress_image_y_origin_metadata = { "offset" : _set_progress_image_y_origin_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ProgressImageYOrigin),) }
    @progress_image_y_origin.setter
    def progress_image_y_origin(self, progress_image_y_origin:"ProgressImageYOrigin") -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_progress_image_y_origin_metadata, progress_image_y_origin)

    _get_picture_from_file_metadata = { "offset" : _get_picture_from_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def picture_from_file(self) -> str:
        """Get or set the splash logo graphic file to be displayed in the control."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_picture_from_file_metadata)

    _set_picture_from_file_metadata = { "offset" : _set_picture_from_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @picture_from_file.setter
    def picture_from_file(self, picture_file:str) -> None:
        """Get or set the splash logo graphic file to be displayed in the control."""
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_picture_from_file_metadata, picture_file)

    _get_pan_mode_enabled_metadata = { "offset" : _get_pan_mode_enabled_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def pan_mode_enabled(self) -> bool:
        """Enable/disable pan mode for map control."""
        return self._intf.get_property(Graphics2DControlBase._metadata, Graphics2DControlBase._get_pan_mode_enabled_metadata)

    _set_pan_mode_enabled_metadata = { "offset" : _set_pan_mode_enabled_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @pan_mode_enabled.setter
    def pan_mode_enabled(self, pan_mode:bool) -> None:
        return self._intf.set_property(Graphics2DControlBase._metadata, Graphics2DControlBase._set_pan_mode_enabled_metadata, pan_mode)

    _property_names[back_color] = "back_color"
    _property_names[picture] = "picture"
    _property_names[window_id] = "window_id"
    _property_names[application] = "application"
    _property_names[no_logo] = "no_logo"
    _property_names[ole_drop_mode] = "ole_drop_mode"
    _property_names[mouse_mode] = "mouse_mode"
    _property_names[ready_state] = "ready_state"
    _property_names[advanced_pick_mode] = "advanced_pick_mode"
    _property_names[in_zoom_mode] = "in_zoom_mode"
    _property_names[show_progress_image] = "show_progress_image"
    _property_names[progress_image_x_offset] = "progress_image_x_offset"
    _property_names[progress_image_y_offset] = "progress_image_y_offset"
    _property_names[progress_image_file] = "progress_image_file"
    _property_names[progress_image_x_origin] = "progress_image_x_origin"
    _property_names[progress_image_y_origin] = "progress_image_y_origin"
    _property_names[picture_from_file] = "picture_from_file"
    _property_names[pan_mode_enabled] = "pan_mode_enabled"

    def __init__(self, source_object=None):
        """Construct an object of type Graphics2DControlBase."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Graphics2DControlBase)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Graphics2DControlBase, [Graphics2DControlBase, ])

agcls.AgClassCatalog.add_catalog_entry((5282650413006135393, 1308832256522158520), Graphics2DControlBase)
agcls.AgTypeNameMap["Graphics2DControlBase"] = Graphics2DControlBase

class PickInfoData(SupportsDeleteCallback):
    """Mouse pick details."""

    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_object_path_method_offset = 1
    _get_latitude_method_offset = 2
    _get_longitude_method_offset = 3
    _get_altitude_method_offset = 4
    _get_is_object_path_valid_method_offset = 5
    _get_is_lat_lon_altitude_valid_method_offset = 6
    _metadata = {
        "iid_data" : (5095284727995613085, 1272110162266713781),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, PickInfoData)

    _get_object_path_metadata = { "offset" : _get_object_path_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def object_path(self) -> str:
        """Path of the STK object picked if any (or empty string)."""
        return self._intf.get_property(PickInfoData._metadata, PickInfoData._get_object_path_metadata)

    _get_latitude_metadata = { "offset" : _get_latitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def latitude(self) -> float:
        """Latitude of point clicked (if available)."""
        return self._intf.get_property(PickInfoData._metadata, PickInfoData._get_latitude_metadata)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def longitude(self) -> float:
        """Longitude of point clicked (if available)."""
        return self._intf.get_property(PickInfoData._metadata, PickInfoData._get_longitude_metadata)

    _get_altitude_metadata = { "offset" : _get_altitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def altitude(self) -> float:
        """Altitude of point clicked (if available)."""
        return self._intf.get_property(PickInfoData._metadata, PickInfoData._get_altitude_metadata)

    _get_is_object_path_valid_metadata = { "offset" : _get_is_object_path_valid_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def is_object_path_valid(self) -> bool:
        """Indicate if the ObjPath property is valid."""
        return self._intf.get_property(PickInfoData._metadata, PickInfoData._get_is_object_path_valid_metadata)

    _get_is_lat_lon_altitude_valid_metadata = { "offset" : _get_is_lat_lon_altitude_valid_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def is_lat_lon_altitude_valid(self) -> bool:
        """Indicate if the Lat/Lon/Alt properties are valid."""
        return self._intf.get_property(PickInfoData._metadata, PickInfoData._get_is_lat_lon_altitude_valid_metadata)

    _property_names[object_path] = "object_path"
    _property_names[latitude] = "latitude"
    _property_names[longitude] = "longitude"
    _property_names[altitude] = "altitude"
    _property_names[is_object_path_valid] = "is_object_path_valid"
    _property_names[is_lat_lon_altitude_valid] = "is_lat_lon_altitude_valid"

    def __init__(self, source_object=None):
        """Construct an object of type PickInfoData."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, PickInfoData)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, PickInfoData, [PickInfoData, ])

agcls.AgClassCatalog.add_catalog_entry((5237657917144607746, 17746628831672826803), PickInfoData)
agcls.AgTypeNameMap["PickInfoData"] = PickInfoData

class STKXApplication(SupportsDeleteCallback):
    """STK X Application object."""

    _num_methods = 26
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _execute_command_method_offset = 1
    _get_enable_connect_method_offset = 2
    _set_enable_connect_method_offset = 3
    _get_connect_port_method_offset = 4
    _set_connect_port_method_offset = 5
    _get_host_id_method_offset = 6
    _get_registration_id_method_offset = 7
    _get_version_method_offset = 8
    _set_online_options_method_offset = 9
    _get_online_options_method_offset = 10
    _set_connect_handler_method_offset = 11
    _get_log_file_full_name_method_offset = 12
    _get_logging_mode_method_offset = 13
    _set_logging_mode_method_offset = 14
    _get_connect_max_connections_method_offset = 15
    _set_connect_max_connections_method_offset = 16
    _execute_multiple_commands_method_offset = 17
    _is_feature_available_method_offset = 18
    _get_no_graphics_method_offset = 19
    _set_no_graphics_method_offset = 20
    _terminate_method_offset = 21
    _get_show_sla_if_not_accepted_method_offset = 22
    _set_show_sla_if_not_accepted_method_offset = 23
    _get_use_hook_method_offset = 24
    _set_use_hook_method_offset = 25
    _use_software_renderer_method_offset = 26
    _metadata = {
        "iid_data" : (5451411510624686901, 5826643244584847294),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, STKXApplication)
    def subscribe(self) -> ISTKXApplicationEventHandler:
        """Return an ISTKXApplicationEventHandler that is subscribed to handle events associated with this instance of STKXApplication."""
        return ISTKXApplicationEventHandler(self._intf)

    _execute_command_metadata = { "offset" : _execute_command_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def execute_command(self, command:str) -> "ExecuteCommandResult":
        """Send a connect command to STK X."""
        return self._intf.invoke(STKXApplication._metadata, STKXApplication._execute_command_metadata, command, OutArg())

    _get_enable_connect_metadata = { "offset" : _get_enable_connect_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def enable_connect(self) -> bool:
        """Enable or disable TCP/IP connect command processing (default: disabled)."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_enable_connect_metadata)

    _set_enable_connect_metadata = { "offset" : _set_enable_connect_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @enable_connect.setter
    def enable_connect(self, value:bool) -> None:
        return self._intf.set_property(STKXApplication._metadata, STKXApplication._set_enable_connect_metadata, value)

    _get_connect_port_metadata = { "offset" : _get_connect_port_method_offset,
            "arg_types" : (POINTER(agcom.SHORT),),
            "marshallers" : (agmarshall.ShortArg,) }
    @property
    def connect_port(self) -> int:
        """Specify TCP/IP port to be used by Connect (default: 5001)."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_connect_port_metadata)

    _set_connect_port_metadata = { "offset" : _set_connect_port_method_offset,
            "arg_types" : (agcom.SHORT,),
            "marshallers" : (agmarshall.ShortArg,) }
    @connect_port.setter
    def connect_port(self, value:int) -> None:
        return self._intf.set_property(STKXApplication._metadata, STKXApplication._set_connect_port_metadata, value)

    _get_host_id_metadata = { "offset" : _get_host_id_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def host_id(self) -> str:
        """Return the Host ID."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_host_id_metadata)

    _get_registration_id_metadata = { "offset" : _get_registration_id_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def registration_id(self) -> str:
        """Return the Registration ID."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_registration_id_metadata)

    _get_version_metadata = { "offset" : _get_version_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def version(self) -> str:
        """Return the version number."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_version_metadata)

    _set_online_options_metadata = { "offset" : _set_online_options_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL, agcom.BSTR, agcom.LONG, agcom.BSTR, agcom.BSTR, agcom.VARIANT_BOOL, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg, agmarshall.BStrArg, agmarshall.LongArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.VariantBoolArg, agmarshall.VariantBoolArg,) }
    def set_online_options(self, use_proxy:bool, server_name:str, port_num:int, user_name:str, password:str, save_password:bool) -> bool:
        """Set http proxy online options."""
        return self._intf.invoke(STKXApplication._metadata, STKXApplication._set_online_options_metadata, use_proxy, server_name, port_num, user_name, password, save_password, OutArg())

    _get_online_options_metadata = { "offset" : _get_online_options_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL), POINTER(agcom.BSTR), POINTER(agcom.LONG), POINTER(agcom.BSTR), POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg, agmarshall.BStrArg, agmarshall.LongArg, agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def get_online_options(self) -> typing.Tuple[bool, str, int, str, bool]:
        """Get http proxy online options."""
        return self._intf.invoke(STKXApplication._metadata, STKXApplication._get_online_options_metadata, OutArg(), OutArg(), OutArg(), OutArg(), OutArg())

    _set_connect_handler_metadata = { "offset" : _set_connect_handler_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg,) }
    def set_connect_handler(self, command_id:str, prog_id:str) -> None:
        """Set callback to handle a certain connect command."""
        return self._intf.invoke(STKXApplication._metadata, STKXApplication._set_connect_handler_metadata, command_id, prog_id)

    _get_log_file_full_name_metadata = { "offset" : _get_log_file_full_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def log_file_full_name(self) -> str:
        """Return full path and log file name."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_log_file_full_name_metadata)

    _get_logging_mode_metadata = { "offset" : _get_logging_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(LoggingMode),) }
    @property
    def logging_mode(self) -> "LoggingMode":
        """Control the log file generation, and if the log file is deleted or not on application exit."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_logging_mode_metadata)

    _set_logging_mode_metadata = { "offset" : _set_logging_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(LoggingMode),) }
    @logging_mode.setter
    def logging_mode(self, value:"LoggingMode") -> None:
        return self._intf.set_property(STKXApplication._metadata, STKXApplication._set_logging_mode_metadata, value)

    _get_connect_max_connections_metadata = { "offset" : _get_connect_max_connections_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def connect_max_connections(self) -> int:
        """Specify the maximum number of Connect connections to allow."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_connect_max_connections_metadata)

    _set_connect_max_connections_metadata = { "offset" : _set_connect_max_connections_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @connect_max_connections.setter
    def connect_max_connections(self, value:int) -> None:
        return self._intf.set_property(STKXApplication._metadata, STKXApplication._set_connect_max_connections_metadata, value)

    _execute_multiple_commands_metadata = { "offset" : _execute_multiple_commands_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY), agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LPSafearrayArg, agmarshall.EnumArg(ExecuteMultipleCommandsMode), agmarshall.InterfaceOutArg,) }
    def execute_multiple_commands(self, connect_commands:list, action:"ExecuteMultipleCommandsMode") -> "ExecuteMultipleCommandsResult":
        """Execute multiple CONNECT actions. The method throws an exception if any of the specified commands have failed."""
        return self._intf.invoke(STKXApplication._metadata, STKXApplication._execute_multiple_commands_metadata, connect_commands, action, OutArg())

    _is_feature_available_metadata = { "offset" : _is_feature_available_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.EnumArg(FeatureCodes), agmarshall.VariantBoolArg,) }
    def is_feature_available(self, feature_code:"FeatureCodes") -> bool:
        """Return true if the specified feature is available."""
        return self._intf.invoke(STKXApplication._metadata, STKXApplication._is_feature_available_metadata, feature_code, OutArg())

    _get_no_graphics_metadata = { "offset" : _get_no_graphics_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def no_graphics(self) -> bool:
        """Start engine with or without graphics (default: engine starts with graphics.)."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_no_graphics_metadata)

    _set_no_graphics_metadata = { "offset" : _set_no_graphics_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @no_graphics.setter
    def no_graphics(self, value:bool) -> None:
        return self._intf.set_property(STKXApplication._metadata, STKXApplication._set_no_graphics_metadata, value)

    _terminate_metadata = { "offset" : _terminate_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def terminate(self) -> None:
        """Terminates the use of STK Engine. This must be the last call to STK Engine."""
        return self._intf.invoke(STKXApplication._metadata, STKXApplication._terminate_metadata, )

    _get_show_sla_if_not_accepted_metadata = { "offset" : _get_show_sla_if_not_accepted_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def show_sla_if_not_accepted(self) -> bool:
        """Show the Software License Agreement dialog if not already accepted."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_show_sla_if_not_accepted_metadata)

    _set_show_sla_if_not_accepted_metadata = { "offset" : _set_show_sla_if_not_accepted_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @show_sla_if_not_accepted.setter
    def show_sla_if_not_accepted(self, value:bool) -> None:
        return self._intf.set_property(STKXApplication._metadata, STKXApplication._set_show_sla_if_not_accepted_metadata, value)

    _get_use_hook_metadata = { "offset" : _get_use_hook_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def use_hook(self) -> bool:
        """Start engine with or without message hook setup (default: engine starts with message hook setup.)."""
        return self._intf.get_property(STKXApplication._metadata, STKXApplication._get_use_hook_metadata)

    _set_use_hook_metadata = { "offset" : _set_use_hook_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @use_hook.setter
    def use_hook(self, value:bool) -> None:
        """Start engine with or without message hook setup (default: engine starts with message hook setup.)."""
        return self._intf.set_property(STKXApplication._metadata, STKXApplication._set_use_hook_metadata, value)

    _use_software_renderer_metadata = { "offset" : _use_software_renderer_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def use_software_renderer(self) -> None:
        """Configure engine graphics to use a software renderer in order to meet minimum graphics requirements. Enabling this option will result in significant performance impacts."""
        return self._intf.invoke(STKXApplication._metadata, STKXApplication._use_software_renderer_metadata, )

    _property_names[enable_connect] = "enable_connect"
    _property_names[connect_port] = "connect_port"
    _property_names[host_id] = "host_id"
    _property_names[registration_id] = "registration_id"
    _property_names[version] = "version"
    _property_names[log_file_full_name] = "log_file_full_name"
    _property_names[logging_mode] = "logging_mode"
    _property_names[connect_max_connections] = "connect_max_connections"
    _property_names[no_graphics] = "no_graphics"
    _property_names[show_sla_if_not_accepted] = "show_sla_if_not_accepted"
    _property_names[use_hook] = "use_hook"

    def __init__(self, source_object=None):
        """Construct an object of type STKXApplication."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, STKXApplication)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, STKXApplication, [STKXApplication, ])

agcls.AgClassCatalog.add_catalog_entry((4965612477927357047, 8047925612354185625), STKXApplication)
agcls.AgTypeNameMap["STKXApplication"] = STKXApplication

class STKXApplicationPartnerAccess(SupportsDeleteCallback):
    """Access to the application object model for business partners."""

    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _grant_partner_access_method_offset = 1
    _metadata = {
        "iid_data" : (4656947247342630568, 6384161945059936654),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, STKXApplicationPartnerAccess)

    _grant_partner_access_metadata = { "offset" : _grant_partner_access_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def grant_partner_access(self, vendor:str, product:str, key:str) -> "STKXApplication":
        """Provide object model root for authorized business partners."""
        return self._intf.invoke(STKXApplicationPartnerAccess._metadata, STKXApplicationPartnerAccess._grant_partner_access_metadata, vendor, product, key, OutArg())


    def __init__(self, source_object=None):
        """Construct an object of type STKXApplicationPartnerAccess."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, STKXApplicationPartnerAccess)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, STKXApplicationPartnerAccess, [STKXApplicationPartnerAccess, ])

agcls.AgClassCatalog.add_catalog_entry((4703777975430642151, 17291114889972261525), STKXApplicationPartnerAccess)
agcls.AgTypeNameMap["STKXApplicationPartnerAccess"] = STKXApplicationPartnerAccess

class DataObject(SupportsDeleteCallback):
    """DataObject is used for OLE drag and drop operations."""

    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_files_method_offset = 1
    _metadata = {
        "iid_data" : (4642770678746827267, 8490102002319634849),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, DataObject)

    _get_files_metadata = { "offset" : _get_files_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def files(self) -> "DataObjectFiles":
        """Return a collection of filenames."""
        return self._intf.get_property(DataObject._metadata, DataObject._get_files_metadata)

    _property_names[files] = "files"

    def __init__(self, source_object=None):
        """Construct an object of type DataObject."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, DataObject)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DataObject, [DataObject, ])

agcls.AgClassCatalog.add_catalog_entry((4669950847213151624, 11716425685151442827), DataObject)
agcls.AgTypeNameMap["DataObject"] = DataObject

class DataObjectFiles(SupportsDeleteCallback):
    """Collection of file names."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get__new_enum_method_offset = 1
    _item_method_offset = 2
    _get_count_method_offset = 3
    _metadata = {
        "iid_data" : (5241656308538360439, 1178344093334617245),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, DataObjectFiles)
    def __iter__(self):
        """Create an iterator for the DataObjectFiles object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an object that can be used to iterate through all the file names in the collection."""
        return self._intf.get_property(DataObjectFiles._metadata, DataObjectFiles._get__new_enum_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LongArg, agmarshall.BStrArg,) }
    def item(self, index:int) -> str:
        """Get the file name at the specified index (0-based)."""
        return self._intf.invoke(DataObjectFiles._metadata, DataObjectFiles._item_metadata, index, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Number of file names contained in the collection."""
        return self._intf.get_property(DataObjectFiles._metadata, DataObjectFiles._get_count_metadata)

    __getitem__ = item


    _property_names[_new_enum] = "_new_enum"
    _property_names[count] = "count"

    def __init__(self, source_object=None):
        """Construct an object of type DataObjectFiles."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, DataObjectFiles)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DataObjectFiles, [DataObjectFiles, ])

agcls.AgClassCatalog.add_catalog_entry((5720513526779713943, 6221409099379914630), DataObjectFiles)
agcls.AgTypeNameMap["DataObjectFiles"] = DataObjectFiles

class RubberBandPickInfoData(SupportsDeleteCallback):
    """Rubber-band mouse pick result."""

    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_object_paths_method_offset = 1
    _metadata = {
        "iid_data" : (5560493386036245755, 13880678457623717547),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RubberBandPickInfoData)

    _get_object_paths_metadata = { "offset" : _get_object_paths_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def object_paths(self) -> "ObjectPathCollection":
        """List of object paths selected."""
        return self._intf.get_property(RubberBandPickInfoData._metadata, RubberBandPickInfoData._get_object_paths_metadata)

    _property_names[object_paths] = "object_paths"

    def __init__(self, source_object=None):
        """Construct an object of type RubberBandPickInfoData."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RubberBandPickInfoData)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RubberBandPickInfoData, [RubberBandPickInfoData, ])

agcls.AgClassCatalog.add_catalog_entry((5458801463718913441, 17686737888889441455), RubberBandPickInfoData)
agcls.AgTypeNameMap["RubberBandPickInfoData"] = RubberBandPickInfoData

class ObjectPathCollection(SupportsDeleteCallback):
    """Collection of object paths."""

    _num_methods = 4
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _range_method_offset = 4
    _metadata = {
        "iid_data" : (4873072426225207527, 3451812691016086192),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ObjectPathCollection)
    def __iter__(self):
        """Create an iterator for the ObjectPathCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(ObjectPathCollection._metadata, ObjectPathCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LongArg, agmarshall.BStrArg,) }
    def item(self, index:int) -> str:
        """Get the element at the specified index (0-based)."""
        return self._intf.invoke(ObjectPathCollection._metadata, ObjectPathCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an object that can be used to iterate through all the object paths in the collection."""
        return self._intf.get_property(ObjectPathCollection._metadata, ObjectPathCollection._get__new_enum_metadata)

    _range_metadata = { "offset" : _range_method_offset,
            "arg_types" : (agcom.LONG, agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LongArg, agmarshall.LongArg, agmarshall.LPSafearrayArg,) }
    def range(self, start_index:int, stop_index:int) -> list:
        """Return the elements within the specified range."""
        return self._intf.invoke(ObjectPathCollection._metadata, ObjectPathCollection._range_metadata, start_index, stop_index, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type ObjectPathCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ObjectPathCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ObjectPathCollection, [ObjectPathCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5431479243483082589, 6842341544396155807), ObjectPathCollection)
agcls.AgTypeNameMap["ObjectPathCollection"] = ObjectPathCollection

class DrawElementRect(IDrawElementRect, SupportsDeleteCallback):
    """Define a rectangle in window coordinates."""
    def __init__(self, source_object=None):
        """Construct an object of type DrawElementRect."""
        SupportsDeleteCallback.__init__(self)
        IDrawElementRect.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDrawElementRect._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DrawElementRect, [IDrawElementRect])

agcls.AgClassCatalog.add_catalog_entry((5647133156743739852, 8979899515705915799), DrawElementRect)
agcls.AgTypeNameMap["DrawElementRect"] = DrawElementRect

class DrawElementCollection(IDrawElementCollection, SupportsDeleteCallback):
    """Collection of elements to draw on the control."""
    def __init__(self, source_object=None):
        """Construct an object of type DrawElementCollection."""
        SupportsDeleteCallback.__init__(self)
        IDrawElementCollection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDrawElementCollection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DrawElementCollection, [IDrawElementCollection])

agcls.AgClassCatalog.add_catalog_entry((4846626779169586992, 12981751770474951553), DrawElementCollection)
agcls.AgTypeNameMap["DrawElementCollection"] = DrawElementCollection

class Draw2DElemRect(IDrawElementRect, SupportsDeleteCallback):
    """Define a rectangle in window coordinates for map control."""
    def __init__(self, source_object=None):
        """Construct an object of type Draw2DElemRect."""
        SupportsDeleteCallback.__init__(self)
        IDrawElementRect.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDrawElementRect._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Draw2DElemRect, [IDrawElementRect])

agcls.AgClassCatalog.add_catalog_entry((4925473448220414623, 7614461974460404874), Draw2DElemRect)
agcls.AgTypeNameMap["Draw2DElemRect"] = Draw2DElemRect

class Draw2DElemCollection(IDrawElementCollection, SupportsDeleteCallback):
    """Collection of elements to draw on map control."""
    def __init__(self, source_object=None):
        """Construct an object of type Draw2DElemCollection."""
        SupportsDeleteCallback.__init__(self)
        IDrawElementCollection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IDrawElementCollection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Draw2DElemCollection, [IDrawElementCollection])

agcls.AgClassCatalog.add_catalog_entry((4825844800505981150, 12877675232260377739), Draw2DElemCollection)
agcls.AgTypeNameMap["Draw2DElemCollection"] = Draw2DElemCollection

class GraphicsAnalysisControlBase(SupportsDeleteCallback):
    """AGI Gfx Analysis control."""

    _num_methods = 15
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_back_color_method_offset = 1
    _set_back_color_method_offset = 2
    _get_picture_method_offset = 3
    _picture_put_reference_method_offset = 4
    _set_picture_method_offset = 5
    _get_no_logo_method_offset = 6
    _set_no_logo_method_offset = 7
    _get_ready_state_method_offset = 8
    _get_application_method_offset = 9
    _get_control_mode_method_offset = 10
    _set_control_mode_method_offset = 11
    _get_picture_from_file_method_offset = 12
    _set_picture_from_file_method_offset = 13
    _get_window_id_method_offset = 14
    _set_window_id_method_offset = 15
    _metadata = {
        "iid_data" : (5043927542341553470, 3435865452458513818),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, GraphicsAnalysisControlBase)

    _get_back_color_metadata = { "offset" : _get_back_color_method_offset,
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        return self._intf.get_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._get_back_color_metadata)

    _set_back_color_metadata = { "offset" : _set_back_color_method_offset,
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        return self._intf.set_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._set_back_color_metadata, clr)

    _get_picture_metadata = { "offset" : _get_picture_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    @property
    def picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        return self._intf.get_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._get_picture_metadata)

    _picture_put_reference_metadata = { "offset" : _picture_put_reference_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    def picture_put_reference(self, picture:IPictureDisp) -> None:
        """Set a reference to the splash logo graphic to be displayed in the control."""
        return self._intf.invoke(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._picture_put_reference_metadata, picture)

    _set_picture_metadata = { "offset" : _set_picture_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDispArg,) }
    @picture.setter
    def picture(self, picture:IPictureDisp) -> None:
        return self._intf.set_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._set_picture_metadata, picture)

    _get_no_logo_metadata = { "offset" : _get_no_logo_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        return self._intf.get_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._get_no_logo_metadata)

    _set_no_logo_metadata = { "offset" : _set_no_logo_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @no_logo.setter
    def no_logo(self, no_logo:bool) -> None:
        return self._intf.set_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._set_no_logo_metadata, no_logo)

    _get_ready_state_metadata = { "offset" : _get_ready_state_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def ready_state(self) -> int:
        """Return the ready state of the control."""
        return self._intf.get_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._get_ready_state_metadata)

    _get_application_metadata = { "offset" : _get_application_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def application(self) -> "STKXApplication":
        """Reference to the STK X application object."""
        return self._intf.get_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._get_application_metadata)

    _get_control_mode_metadata = { "offset" : _get_control_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(Graphics2DAnalysisMode),) }
    @property
    def control_mode(self) -> "Graphics2DAnalysisMode":
        """The Graphics control mode."""
        return self._intf.get_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._get_control_mode_metadata)

    _set_control_mode_metadata = { "offset" : _set_control_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(Graphics2DAnalysisMode),) }
    @control_mode.setter
    def control_mode(self, gfx_analysis_mode:"Graphics2DAnalysisMode") -> None:
        return self._intf.set_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._set_control_mode_metadata, gfx_analysis_mode)

    _get_picture_from_file_metadata = { "offset" : _get_picture_from_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def picture_from_file(self) -> str:
        """Get or set the splash logo graphic file to be displayed in the control."""
        return self._intf.get_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._get_picture_from_file_metadata)

    _set_picture_from_file_metadata = { "offset" : _set_picture_from_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @picture_from_file.setter
    def picture_from_file(self, picture_file:str) -> None:
        """Get or set the splash logo graphic file to be displayed in the control."""
        return self._intf.set_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._set_picture_from_file_metadata, picture_file)

    _get_window_id_metadata = { "offset" : _get_window_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def window_id(self) -> int:
        """Window identifier (for Connect commands)."""
        return self._intf.get_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._get_window_id_metadata)

    _set_window_id_metadata = { "offset" : _set_window_id_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @window_id.setter
    def window_id(self, value:int) -> None:
        return self._intf.set_property(GraphicsAnalysisControlBase._metadata, GraphicsAnalysisControlBase._set_window_id_metadata, value)

    _property_names[back_color] = "back_color"
    _property_names[picture] = "picture"
    _property_names[no_logo] = "no_logo"
    _property_names[ready_state] = "ready_state"
    _property_names[application] = "application"
    _property_names[control_mode] = "control_mode"
    _property_names[picture_from_file] = "picture_from_file"
    _property_names[window_id] = "window_id"

    def __init__(self, source_object=None):
        """Construct an object of type GraphicsAnalysisControlBase."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, GraphicsAnalysisControlBase)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, GraphicsAnalysisControlBase, [GraphicsAnalysisControlBase, ])

agcls.AgClassCatalog.add_catalog_entry((5014026146283335070, 224619130580477084), GraphicsAnalysisControlBase)
agcls.AgTypeNameMap["GraphicsAnalysisControlBase"] = GraphicsAnalysisControlBase

class WindowProjectionPosition(SupportsDeleteCallback):
    """Projected window position detail."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_x_position_method_offset = 1
    _get_y_position_method_offset = 2
    _get_is_window_projection_position_valid_method_offset = 3
    _metadata = {
        "iid_data" : (4973576687073445418, 9233127695963312296),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, WindowProjectionPosition)

    _get_x_position_metadata = { "offset" : _get_x_position_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def x_position(self) -> float:
        """Projected window X position."""
        return self._intf.get_property(WindowProjectionPosition._metadata, WindowProjectionPosition._get_x_position_metadata)

    _get_y_position_metadata = { "offset" : _get_y_position_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def y_position(self) -> float:
        """Projected window Y position."""
        return self._intf.get_property(WindowProjectionPosition._metadata, WindowProjectionPosition._get_y_position_metadata)

    _get_is_window_projection_position_valid_metadata = { "offset" : _get_is_window_projection_position_valid_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def is_window_projection_position_valid(self) -> bool:
        """Indicate if the returned projected position is valid or not."""
        return self._intf.get_property(WindowProjectionPosition._metadata, WindowProjectionPosition._get_is_window_projection_position_valid_metadata)

    _property_names[x_position] = "x_position"
    _property_names[y_position] = "y_position"
    _property_names[is_window_projection_position_valid] = "is_window_projection_position_valid"

    def __init__(self, source_object=None):
        """Construct an object of type WindowProjectionPosition."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, WindowProjectionPosition)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, WindowProjectionPosition, [WindowProjectionPosition, ])

agcls.AgClassCatalog.add_catalog_entry((4893863575783400406, 8243445408594598314), WindowProjectionPosition)
agcls.AgTypeNameMap["WindowProjectionPosition"] = WindowProjectionPosition

class DrawElementLine(SupportsDeleteCallback):
    """Define a line in control coordinates."""

    _num_methods = 11
    _vtable_offset = IDrawElement._vtable_offset + IDrawElement._num_methods
    _get_left_method_offset = 1
    _get_right_method_offset = 2
    _get_top_method_offset = 3
    _get_bottom_method_offset = 4
    _set_method_offset = 5
    _get_color_method_offset = 6
    _set_color_method_offset = 7
    _get_line_width_method_offset = 8
    _set_line_width_method_offset = 9
    _get_line_style_method_offset = 10
    _set_line_style_method_offset = 11
    _metadata = {
        "iid_data" : (4941722960863766416, 11670089675664877230),
        "vtable_reference" : IDrawElement._vtable_offset + IDrawElement._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, DrawElementLine)

    _get_left_metadata = { "offset" : _get_left_method_offset,
            "arg_types" : (POINTER(agcom.OLE_XPOS_PIXELS),),
            "marshallers" : (agmarshall.OLEXPosPixelsArg,) }
    @property
    def left(self) -> int:
        """The x-coordinate of the left edge of this line."""
        return self._intf.get_property(DrawElementLine._metadata, DrawElementLine._get_left_metadata)

    _get_right_metadata = { "offset" : _get_right_method_offset,
            "arg_types" : (POINTER(agcom.OLE_XPOS_PIXELS),),
            "marshallers" : (agmarshall.OLEXPosPixelsArg,) }
    @property
    def right(self) -> int:
        """The x-coordinate of the right edge of this line."""
        return self._intf.get_property(DrawElementLine._metadata, DrawElementLine._get_right_metadata)

    _get_top_metadata = { "offset" : _get_top_method_offset,
            "arg_types" : (POINTER(agcom.OLE_YPOS_PIXELS),),
            "marshallers" : (agmarshall.OLEYPosPixelsArg,) }
    @property
    def top(self) -> int:
        """The y-coordinate of the top edge of this line."""
        return self._intf.get_property(DrawElementLine._metadata, DrawElementLine._get_top_metadata)

    _get_bottom_metadata = { "offset" : _get_bottom_method_offset,
            "arg_types" : (POINTER(agcom.OLE_YPOS_PIXELS),),
            "marshallers" : (agmarshall.OLEYPosPixelsArg,) }
    @property
    def bottom(self) -> int:
        """The y-coordinate of the bottom edge of this line."""
        return self._intf.get_property(DrawElementLine._metadata, DrawElementLine._get_bottom_metadata)

    _set_metadata = { "offset" : _set_method_offset,
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS,),
            "marshallers" : (agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg, agmarshall.OLEXPosPixelsArg, agmarshall.OLEYPosPixelsArg,) }
    def set(self, left:int, top:int, right:int, bottom:int) -> None:
        """Set the rectangle coordinates."""
        return self._intf.invoke(DrawElementLine._metadata, DrawElementLine._set_metadata, left, top, right, bottom)

    _get_color_metadata = { "offset" : _get_color_method_offset,
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @property
    def color(self) -> agcolor.Color:
        """Color of the rectangle."""
        return self._intf.get_property(DrawElementLine._metadata, DrawElementLine._get_color_metadata)

    _set_color_metadata = { "offset" : _set_color_method_offset,
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLEColorArg,) }
    @color.setter
    def color(self, value:agcolor.Color) -> None:
        return self._intf.set_property(DrawElementLine._metadata, DrawElementLine._set_color_metadata, value)

    _get_line_width_metadata = { "offset" : _get_line_width_method_offset,
            "arg_types" : (POINTER(agcom.FLOAT),),
            "marshallers" : (agmarshall.FloatArg,) }
    @property
    def line_width(self) -> float:
        """Specify the width of the line."""
        return self._intf.get_property(DrawElementLine._metadata, DrawElementLine._get_line_width_metadata)

    _set_line_width_metadata = { "offset" : _set_line_width_method_offset,
            "arg_types" : (agcom.FLOAT,),
            "marshallers" : (agmarshall.FloatArg,) }
    @line_width.setter
    def line_width(self, value:float) -> None:
        return self._intf.set_property(DrawElementLine._metadata, DrawElementLine._set_line_width_metadata, value)

    _get_line_style_metadata = { "offset" : _get_line_style_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(LineStyle),) }
    @property
    def line_style(self) -> "LineStyle":
        """Specify the style of the line."""
        return self._intf.get_property(DrawElementLine._metadata, DrawElementLine._get_line_style_metadata)

    _set_line_style_metadata = { "offset" : _set_line_style_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(LineStyle),) }
    @line_style.setter
    def line_style(self, value:"LineStyle") -> None:
        return self._intf.set_property(DrawElementLine._metadata, DrawElementLine._set_line_style_metadata, value)

    _property_names[left] = "left"
    _property_names[right] = "right"
    _property_names[top] = "top"
    _property_names[bottom] = "bottom"
    _property_names[color] = "color"
    _property_names[line_width] = "line_width"
    _property_names[line_style] = "line_style"

    def __init__(self, source_object=None):
        """Construct an object of type DrawElementLine."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, DrawElementLine)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, DrawElementLine, [DrawElementLine, ])

agcls.AgClassCatalog.add_catalog_entry((4857795362755123937, 15595470460410295944), DrawElementLine)
agcls.AgTypeNameMap["DrawElementLine"] = DrawElementLine

class STKXSSLCertificateErrorEventArgs(SupportsDeleteCallback):
    """Provide information about an SSL certificate that is expired or invalid."""

    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _set_ignore_error_method_offset = 1
    _get_is_error_ignored_method_offset = 2
    _set_ignore_error_permanently_method_offset = 3
    _get_serial_number_method_offset = 4
    _get_issuer_method_offset = 5
    _get_subject_method_offset = 6
    _get_valid_date_method_offset = 7
    _get_expiration_date_method_offset = 8
    _get_is_expired_method_offset = 9
    _get_pem_data_method_offset = 10
    _get_handled_method_offset = 11
    _set_handled_method_offset = 12
    _metadata = {
        "iid_data" : (5720974690728289973, 10366462130882712979),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, STKXSSLCertificateErrorEventArgs)

    _set_ignore_error_metadata = { "offset" : _set_ignore_error_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    def set_ignore_error(self, ignore_error:bool) -> None:
        """Specify True to ignore the certificate error and continue with establishing secure HTTP connection to the remote server."""
        return self._intf.invoke(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._set_ignore_error_metadata, ignore_error)

    _get_is_error_ignored_metadata = { "offset" : _get_is_error_ignored_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def is_error_ignored(self) -> bool:
        """Return whether the invalid certificate error is ignored."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_is_error_ignored_metadata)

    _set_ignore_error_permanently_metadata = { "offset" : _set_ignore_error_permanently_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    def set_ignore_error_permanently(self, ignore_error_permanently:bool) -> None:
        """Specify True to ignore the certificate error and add the certificate to the list of trusted certificates."""
        return self._intf.invoke(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._set_ignore_error_permanently_metadata, ignore_error_permanently)

    _get_serial_number_metadata = { "offset" : _get_serial_number_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def serial_number(self) -> str:
        """Certificate's serial number."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_serial_number_metadata)

    _get_issuer_metadata = { "offset" : _get_issuer_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def issuer(self) -> str:
        """The provider who issued the certificate."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_issuer_metadata)

    _get_subject_metadata = { "offset" : _get_subject_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def subject(self) -> str:
        """Certificate's subject field."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_subject_metadata)

    _get_valid_date_metadata = { "offset" : _get_valid_date_method_offset,
            "arg_types" : (POINTER(agcom.DATE),),
            "marshallers" : (agmarshall.DateArg,) }
    @property
    def valid_date(self) -> datetime:
        """Certificate's valid date."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_valid_date_metadata)

    _get_expiration_date_metadata = { "offset" : _get_expiration_date_method_offset,
            "arg_types" : (POINTER(agcom.DATE),),
            "marshallers" : (agmarshall.DateArg,) }
    @property
    def expiration_date(self) -> datetime:
        """Certificate's expiration date."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_expiration_date_metadata)

    _get_is_expired_metadata = { "offset" : _get_is_expired_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def is_expired(self) -> bool:
        """Whether the certificate is expired."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_is_expired_metadata)

    _get_pem_data_metadata = { "offset" : _get_pem_data_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def pem_data(self) -> str:
        """Certificate's PEM data encoded as base-64."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_pem_data_metadata)

    _get_handled_metadata = { "offset" : _get_handled_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def handled(self) -> bool:
        """Indicate whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners."""
        return self._intf.get_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._get_handled_metadata)

    _set_handled_metadata = { "offset" : _set_handled_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @handled.setter
    def handled(self, handled:bool) -> None:
        """Indicate whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners."""
        return self._intf.set_property(STKXSSLCertificateErrorEventArgs._metadata, STKXSSLCertificateErrorEventArgs._set_handled_metadata, handled)

    _property_names[is_error_ignored] = "is_error_ignored"
    _property_names[serial_number] = "serial_number"
    _property_names[issuer] = "issuer"
    _property_names[subject] = "subject"
    _property_names[valid_date] = "valid_date"
    _property_names[expiration_date] = "expiration_date"
    _property_names[is_expired] = "is_expired"
    _property_names[pem_data] = "pem_data"
    _property_names[handled] = "handled"

    def __init__(self, source_object=None):
        """Construct an object of type STKXSSLCertificateErrorEventArgs."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, STKXSSLCertificateErrorEventArgs)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, STKXSSLCertificateErrorEventArgs, [STKXSSLCertificateErrorEventArgs, ])

agcls.AgClassCatalog.add_catalog_entry((5441759658174404467, 7058418447957075853), STKXSSLCertificateErrorEventArgs)
agcls.AgTypeNameMap["STKXSSLCertificateErrorEventArgs"] = STKXSSLCertificateErrorEventArgs

class STKXConControlQuitReceivedEventArgs(SupportsDeleteCallback):
    """Arguments for the OnConControlQuitReceived event."""

    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_acknowledge_method_offset = 1
    _set_acknowledge_method_offset = 2
    _metadata = {
        "iid_data" : (4866391703832323418, 17032249666119597455),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, STKXConControlQuitReceivedEventArgs)

    _get_acknowledge_metadata = { "offset" : _get_acknowledge_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def acknowledge(self) -> bool:
        """Indicate whether or not to acknowledge the connect command."""
        return self._intf.get_property(STKXConControlQuitReceivedEventArgs._metadata, STKXConControlQuitReceivedEventArgs._get_acknowledge_metadata)

    _set_acknowledge_metadata = { "offset" : _set_acknowledge_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @acknowledge.setter
    def acknowledge(self, acknowledge:bool) -> None:
        """Indicate whether or not to acknowledge the connect command."""
        return self._intf.set_property(STKXConControlQuitReceivedEventArgs._metadata, STKXConControlQuitReceivedEventArgs._set_acknowledge_metadata, acknowledge)

    _property_names[acknowledge] = "acknowledge"

    def __init__(self, source_object=None):
        """Construct an object of type STKXConControlQuitReceivedEventArgs."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, STKXConControlQuitReceivedEventArgs)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, STKXConControlQuitReceivedEventArgs, [STKXConControlQuitReceivedEventArgs, ])

agcls.AgClassCatalog.add_catalog_entry((4908290544374795249, 3464197164321935535), STKXConControlQuitReceivedEventArgs)
agcls.AgTypeNameMap["STKXConControlQuitReceivedEventArgs"] = STKXConControlQuitReceivedEventArgs