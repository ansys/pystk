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

"""The STK UI Application library is a COM library containing classes, interfaces and enumerations for the Application Object Model."""

__all__ = ["ApplicationConstants", "ApplicationErrorCodes", "ApplicationLogMessageType", "ApplicationOpenLogFileMode",
"IUiApplicationPartnerAccess", "MostRecentlyUsedCollection", "PreferencesFilesMode", "UiApplication",
"UiFileOpenDialogExtension", "UiFileOpenDialogExtensionCollection"]

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
    set_interface_attribute,
)
from .internal.comutil import IDispatch, IUnknown
from .uicore import ApplicationWindowState


class ApplicationOpenLogFileMode(IntEnum):
    """Log file open modes."""

    FOR_WRITING = 2
    """Open log file in write file mode."""
    FOR_APPENDING = 8
    """Open log file in append file mode."""

ApplicationOpenLogFileMode.FOR_WRITING.__doc__ = "Open log file in write file mode."
ApplicationOpenLogFileMode.FOR_APPENDING.__doc__ = "Open log file in append file mode."

agcls.AgTypeNameMap["ApplicationOpenLogFileMode"] = ApplicationOpenLogFileMode

class ApplicationLogMessageType(IntEnum):
    """Log message types."""

    DEBUG = 0
    """Log messages that provide Debug text."""
    INFO = 1
    """Log messages that provide information text."""
    FORCE_INFO = 2
    """Log messages that provide forceful information text."""
    WARNING = 3
    """Log messages that provide warning text."""
    ALARM = 4
    """Log messages that provide alarm text."""

ApplicationLogMessageType.DEBUG.__doc__ = "Log messages that provide Debug text."
ApplicationLogMessageType.INFO.__doc__ = "Log messages that provide information text."
ApplicationLogMessageType.FORCE_INFO.__doc__ = "Log messages that provide forceful information text."
ApplicationLogMessageType.WARNING.__doc__ = "Log messages that provide warning text."
ApplicationLogMessageType.ALARM.__doc__ = "Log messages that provide alarm text."

agcls.AgTypeNameMap["ApplicationLogMessageType"] = ApplicationLogMessageType

class PreferencesFilesMode(IntEnum):
    """Specify how application should handle user preference files"""

    _NO_LOAD_NO_SAVE = 0
    """Neither Load nor Save user preference files."""
    _LOAD_NO_SAVE = 1
    """Only Load (on startup) but do not Save user preference files."""
    _LOAD_AND_SAVE = 2
    """Both Load (on startup) and Save (on exit) user preference files."""

PreferencesFilesMode._NO_LOAD_NO_SAVE.__doc__ = "Neither Load nor Save user preference files."
PreferencesFilesMode._LOAD_NO_SAVE.__doc__ = "Only Load (on startup) but do not Save user preference files."
PreferencesFilesMode._LOAD_AND_SAVE.__doc__ = "Both Load (on startup) and Save (on exit) user preference files."

agcls.AgTypeNameMap["PreferencesFilesMode"] = PreferencesFilesMode

class ApplicationConstants(IntEnum):
    """ApplicationConstants contains base IDs for various structures."""

    APPLICATION_ERROR_BASE = 0x200
    """Error base."""

ApplicationConstants.APPLICATION_ERROR_BASE.__doc__ = "Error base."

agcls.AgTypeNameMap["ApplicationConstants"] = ApplicationConstants

class ApplicationErrorCodes(IntEnum):
    """App error codes."""

    PERSONALITY_LOAD_FAILED = (((1 << 31) | (4 << 16)) | (ApplicationConstants.APPLICATION_ERROR_BASE + 1))
    """Failed to load personality."""
    PERSONALITY_ALREADY_LOADED = (((1 << 31) | (4 << 16)) | (ApplicationConstants.APPLICATION_ERROR_BASE + 2))
    """Personality already loaded."""
    PERSONALITY_NOT_LOADED = (((1 << 31) | (4 << 16)) | (ApplicationConstants.APPLICATION_ERROR_BASE + 3))
    """No personality is loaded."""
    PERSONALITY_LICENSE_ERROR = (((1 << 31) | (4 << 16)) | (ApplicationConstants.APPLICATION_ERROR_BASE + 4))
    """You do not have the required license to connect externally to the application."""
    NO_LICENSE_ERROR = (((1 << 31) | (4 << 16)) | (ApplicationConstants.APPLICATION_ERROR_BASE + 5))
    """No license could be found."""

ApplicationErrorCodes.PERSONALITY_LOAD_FAILED.__doc__ = "Failed to load personality."
ApplicationErrorCodes.PERSONALITY_ALREADY_LOADED.__doc__ = "Personality already loaded."
ApplicationErrorCodes.PERSONALITY_NOT_LOADED.__doc__ = "No personality is loaded."
ApplicationErrorCodes.PERSONALITY_LICENSE_ERROR.__doc__ = "You do not have the required license to connect externally to the application."
ApplicationErrorCodes.NO_LICENSE_ERROR.__doc__ = "No license could be found."

agcls.AgTypeNameMap["ApplicationErrorCodes"] = ApplicationErrorCodes


class IUiApplicationPartnerAccess(object):
    """Access to the application object model for business partners."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _grant_partner_access_method_offset = 1
    _metadata = {
        "iid_data" : (5077062202653651173, 4012358305108718229),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IUiApplicationPartnerAccess."""
        initialize_from_source_object(self, source_object, IUiApplicationPartnerAccess)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IUiApplicationPartnerAccess)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IUiApplicationPartnerAccess, None)

    _grant_partner_access_metadata = { "offset" : _grant_partner_access_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def grant_partner_access(self, vendor:str, product:str, key:str) -> typing.Any:
        """Provide object model root for authorized business partners."""
        return self._intf.invoke(IUiApplicationPartnerAccess._metadata, IUiApplicationPartnerAccess._grant_partner_access_metadata, vendor, product, key, OutArg())



agcls.AgClassCatalog.add_catalog_entry((5077062202653651173, 4012358305108718229), IUiApplicationPartnerAccess)
agcls.AgTypeNameMap["IUiApplicationPartnerAccess"] = IUiApplicationPartnerAccess



class UiApplication(IUiApplicationPartnerAccess, SupportsDeleteCallback):
    """
    UiApplication represents a root of the Application Model.

    Examples
    --------
    Close the STK desktop application:
    >>> # AgUiApplication uiApplication: STK Application
    >>> uiApplication.shutdown()
    """

    _num_methods = 39
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _load_personality_method_offset = 1
    _get_personality_method_offset = 2
    _get_visible_method_offset = 3
    _set_visible_method_offset = 4
    _get_user_control_method_offset = 5
    _set_user_control_method_offset = 6
    _get_windows_method_offset = 7
    _get_height_method_offset = 8
    _set_height_method_offset = 9
    _get_width_method_offset = 10
    _set_width_method_offset = 11
    _get_left_method_offset = 12
    _set_left_method_offset = 13
    _get_top_method_offset = 14
    _set_top_method_offset = 15
    _get_window_state_method_offset = 16
    _set_window_state_method_offset = 17
    _activate_method_offset = 18
    _get_most_recently_used_list_method_offset = 19
    _file_open_dialog_method_offset = 20
    _get_path_method_offset = 21
    _create_object_method_offset = 22
    _file_save_as_dialog_method_offset = 23
    _quit_method_offset = 24
    _file_open_dialog_extension_method_offset = 25
    _get_hwnd_method_offset = 26
    _directory_picker_dialog_method_offset = 27
    _get_message_pending_delay_method_offset = 28
    _set_message_pending_delay_method_offset = 29
    _get_personality2_method_offset = 30
    _open_log_file_method_offset = 31
    _log_message_method_offset = 32
    _get_log_file_method_offset = 33
    _get_display_alerts_method_offset = 34
    _set_display_alerts_method_offset = 35
    _create_application_method_offset = 36
    _get_process_id_method_offset = 37
    _get_preferences_files_mode_method_offset = 38
    _set_preferences_files_mode_method_offset = 39
    _metadata = {
        "iid_data" : (5664619422046306087, 8136869108016025256),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UiApplication)

    _load_personality_metadata = { "offset" : _load_personality_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def load_personality(self, pers_name:str) -> None:
        """Load a personality by its name."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._load_personality_metadata, pers_name)

    _get_personality_metadata = { "offset" : _get_personality_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def personality(self) -> typing.Any:
        """Return a reference to the currently loaded personality."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_personality_metadata)

    _get_visible_metadata = { "offset" : _get_visible_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def visible(self) -> bool:
        """Get or set whether the main window is visible."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_visible_metadata)

    _set_visible_metadata = { "offset" : _set_visible_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @visible.setter
    def visible(self, new_value:bool) -> None:
        """Get or set whether the main window is visible."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_visible_metadata, new_value)

    _get_user_control_metadata = { "offset" : _get_user_control_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def user_control(self) -> bool:
        """Get or set whether the application is user controlled."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_user_control_metadata)

    _set_user_control_metadata = { "offset" : _set_user_control_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @user_control.setter
    def user_control(self, new_value:bool) -> None:
        """Get or set whether the application is user controlled."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_user_control_metadata, new_value)

    _get_windows_metadata = { "offset" : _get_windows_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def windows(self) -> "IWindowsCollection":
        """Return a collection of windows."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_windows_metadata)

    _get_height_metadata = { "offset" : _get_height_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def height(self) -> int:
        """Get or set a height of the main window."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_height_metadata)

    _set_height_metadata = { "offset" : _set_height_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @height.setter
    def height(self, new_value:int) -> None:
        """Get or set a height of the main window."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_height_metadata, new_value)

    _get_width_metadata = { "offset" : _get_width_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def width(self) -> int:
        """Get or set a width of the main window."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_width_metadata)

    _set_width_metadata = { "offset" : _set_width_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @width.setter
    def width(self, new_value:int) -> None:
        """Get or set a width of the main window."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_width_metadata, new_value)

    _get_left_metadata = { "offset" : _get_left_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def left(self) -> int:
        """Get or set a vertical coordinate of the main window."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_left_metadata)

    _set_left_metadata = { "offset" : _set_left_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @left.setter
    def left(self, new_value:int) -> None:
        """Get or set a vertical coordinate of the main window."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_left_metadata, new_value)

    _get_top_metadata = { "offset" : _get_top_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def top(self) -> int:
        """Get or set a horizontal coordinate of the main window."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_top_metadata)

    _set_top_metadata = { "offset" : _set_top_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @top.setter
    def top(self, new_value:int) -> None:
        """Get or set a horizontal coordinate of the main window."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_top_metadata, new_value)

    _get_window_state_metadata = { "offset" : _get_window_state_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ApplicationWindowState),) }
    @property
    def window_state(self) -> "ApplicationWindowState":
        """Get or set the state of the main window."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_window_state_metadata)

    _set_window_state_metadata = { "offset" : _set_window_state_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ApplicationWindowState),) }
    @window_state.setter
    def window_state(self, new_value:"ApplicationWindowState") -> None:
        """Get or set the state of the main window."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_window_state_metadata, new_value)

    _activate_metadata = { "offset" : _activate_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def activate(self) -> None:
        """Activates the application's main window."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._activate_metadata, )

    _get_most_recently_used_list_metadata = { "offset" : _get_most_recently_used_list_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def most_recently_used_list(self) -> "MostRecentlyUsedCollection":
        """Return a collection most recently used files."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_most_recently_used_list_metadata)

    _file_open_dialog_metadata = { "offset" : _file_open_dialog_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg,) }
    def file_open_dialog(self, default_ext:str, filter:str, initial_dir:str) -> str:
        """Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._file_open_dialog_metadata, default_ext, filter, initial_dir, OutArg())

    _get_path_metadata = { "offset" : _get_path_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def path(self) -> str:
        """Return the complete path to the application, excluding the final separator and name of the application. Read-only String."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_path_metadata)

    _create_object_metadata = { "offset" : _create_object_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def create_object(self, prog_id:str, remote_server:str) -> typing.Any:
        """Only works from local HTML pages and scripts."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._create_object_metadata, prog_id, remote_server, OutArg())

    _file_save_as_dialog_metadata = { "offset" : _file_save_as_dialog_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg,) }
    def file_save_as_dialog(self, default_ext:str, filter:str, initial_dir:str) -> str:
        """Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._file_save_as_dialog_metadata, default_ext, filter, initial_dir, OutArg())

    _quit_metadata = { "offset" : _quit_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def quit(self) -> None:
        """Shuts down the application."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._quit_metadata, )

    _file_open_dialog_extension_metadata = { "offset" : _file_open_dialog_extension_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VariantBoolArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def file_open_dialog_extension(self, allow_multi_select:bool, default_ext:str, filter:str, initial_dir:str) -> "UiFileOpenDialogExtension":
        """Brings up a standard File Open Dialog and returns an object representing the selected file."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._file_open_dialog_extension_metadata, allow_multi_select, default_ext, filter, initial_dir, OutArg())

    _get_hwnd_metadata = { "offset" : _get_hwnd_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def hwnd(self) -> int:
        """Return an HWND handle associated with the application main window."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_hwnd_metadata)

    _directory_picker_dialog_metadata = { "offset" : _directory_picker_dialog_method_offset,
            "arg_types" : (agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.BStrArg,) }
    def directory_picker_dialog(self, title:str, initial_dir:str) -> str:
        """Brings up the Directory Picker Dialog and returns a selected directory name."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._directory_picker_dialog_metadata, title, initial_dir, OutArg())

    _get_message_pending_delay_metadata = { "offset" : _get_message_pending_delay_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def message_pending_delay(self) -> int:
        """Get or set message-pending delay for server busy dialog (in milliseconds)."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_message_pending_delay_metadata)

    _set_message_pending_delay_metadata = { "offset" : _set_message_pending_delay_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LongArg,) }
    @message_pending_delay.setter
    def message_pending_delay(self, new_value:int) -> None:
        """Get or set message-pending delay for server busy dialog (in milliseconds)."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_message_pending_delay_metadata, new_value)

    _get_personality2_metadata = { "offset" : _get_personality2_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def personality2(self) -> typing.Any:
        """Return an new instance of the root object of the STK Object Model."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_personality2_metadata)

    _open_log_file_metadata = { "offset" : _open_log_file_method_offset,
            "arg_types" : (agcom.BSTR, agcom.LONG, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.EnumArg(ApplicationOpenLogFileMode), agmarshall.VariantBoolArg,) }
    def open_log_file(self, log_file_name:str, log_file_mode:"ApplicationOpenLogFileMode") -> bool:
        """Specify the current log file to be written to."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._open_log_file_metadata, log_file_name, log_file_mode, OutArg())

    _log_message_metadata = { "offset" : _log_message_method_offset,
            "arg_types" : (agcom.LONG, agcom.BSTR,),
            "marshallers" : (agmarshall.EnumArg(ApplicationLogMessageType), agmarshall.BStrArg,) }
    def log_message(self, msg_type:"ApplicationLogMessageType", msg:str) -> None:
        """Log the Message specified."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._log_message_metadata, msg_type, msg)

    _get_log_file_metadata = { "offset" : _get_log_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def log_file(self) -> str:
        """Get the current log files full path."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_log_file_metadata)

    _get_display_alerts_metadata = { "offset" : _get_display_alerts_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def display_alerts(self) -> bool:
        """Set to true to display certain alerts and messages. Otherwise false. The default value is True."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_display_alerts_metadata)

    _set_display_alerts_metadata = { "offset" : _set_display_alerts_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @display_alerts.setter
    def display_alerts(self, display_alerts:bool) -> None:
        """Set to true to display certain alerts and messages. Otherwise false. The default value is True."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_display_alerts_metadata, display_alerts)

    _create_application_metadata = { "offset" : _create_application_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def create_application(self) -> "UiApplication":
        """Create a new instance of the application model root object."""
        return self._intf.invoke(UiApplication._metadata, UiApplication._create_application_metadata, OutArg())

    _get_process_id_metadata = { "offset" : _get_process_id_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def process_id(self) -> int:
        """Get process id for the current instance."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_process_id_metadata)

    _get_preferences_files_mode_metadata = { "offset" : _get_preferences_files_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(PreferencesFilesMode),) }
    @property
    def preferences_files_mode(self) -> "PreferencesFilesMode":
        """Get or set whether to use saved user preference files."""
        return self._intf.get_property(UiApplication._metadata, UiApplication._get_preferences_files_mode_metadata)

    _set_preferences_files_mode_metadata = { "offset" : _set_preferences_files_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(PreferencesFilesMode),) }
    @preferences_files_mode.setter
    def preferences_files_mode(self, pref_mode:"PreferencesFilesMode") -> None:
        """Get or set whether to use saved user preference files."""
        return self._intf.set_property(UiApplication._metadata, UiApplication._set_preferences_files_mode_metadata, pref_mode)

    _property_names[personality] = "personality"
    _property_names[visible] = "visible"
    _property_names[user_control] = "user_control"
    _property_names[windows] = "windows"
    _property_names[height] = "height"
    _property_names[width] = "width"
    _property_names[left] = "left"
    _property_names[top] = "top"
    _property_names[window_state] = "window_state"
    _property_names[most_recently_used_list] = "most_recently_used_list"
    _property_names[path] = "path"
    _property_names[hwnd] = "hwnd"
    _property_names[message_pending_delay] = "message_pending_delay"
    _property_names[personality2] = "personality2"
    _property_names[log_file] = "log_file"
    _property_names[display_alerts] = "display_alerts"
    _property_names[process_id] = "process_id"
    _property_names[preferences_files_mode] = "preferences_files_mode"

    def __init__(self, source_object=None):
        """Construct an object of type UiApplication."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, UiApplication)
        IUiApplicationPartnerAccess.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IUiApplicationPartnerAccess._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiApplication, [UiApplication, IUiApplicationPartnerAccess])

agcls.AgClassCatalog.add_catalog_entry((4897994545220499919, 9857477482842131391), UiApplication)
agcls.AgTypeNameMap["UiApplication"] = UiApplication

class MostRecentlyUsedCollection(SupportsDeleteCallback):
    """Provide information about most recently used (MRU) list."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _item_method_offset = 1
    _get_count_method_offset = 2
    _get__new_enum_method_offset = 3
    _metadata = {
        "iid_data" : (5483367896848674890, 10589458234430986426),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, MostRecentlyUsedCollection)
    def __iter__(self):
        """Create an iterator for the MostRecentlyUsedCollection object."""
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

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.Variant, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.VariantArg, agmarshall.BStrArg,) }
    def item(self, index:typing.Any) -> str:
        """Get the MRU at the specified index."""
        return self._intf.invoke(MostRecentlyUsedCollection._metadata, MostRecentlyUsedCollection._item_metadata, index, OutArg())

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Get the total count of MRUs in the collection."""
        return self._intf.get_property(MostRecentlyUsedCollection._metadata, MostRecentlyUsedCollection._get_count_metadata)

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Enumerates through the MRU collection."""
        return self._intf.get_property(MostRecentlyUsedCollection._metadata, MostRecentlyUsedCollection._get__new_enum_metadata)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type MostRecentlyUsedCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, MostRecentlyUsedCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, MostRecentlyUsedCollection, [MostRecentlyUsedCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5689642888327568715, 9796270372090483644), MostRecentlyUsedCollection)
agcls.AgTypeNameMap["MostRecentlyUsedCollection"] = MostRecentlyUsedCollection

class UiFileOpenDialogExtensionCollection(SupportsDeleteCallback):
    """Multiple file open collection."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _get__new_enum_method_offset = 2
    _item_method_offset = 3
    _metadata = {
        "iid_data" : (5324456244233588029, 5769450117707913606),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UiFileOpenDialogExtensionCollection)
    def __iter__(self):
        """Create an iterator for the UiFileOpenDialogExtensionCollection object."""
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
        """Get the total count of files in the collection."""
        return self._intf.get_property(UiFileOpenDialogExtensionCollection._metadata, UiFileOpenDialogExtensionCollection._get_count_metadata)

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Enumerates through the file collection."""
        return self._intf.get_property(UiFileOpenDialogExtensionCollection._metadata, UiFileOpenDialogExtensionCollection._get__new_enum_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LongArg, agmarshall.BStrArg,) }
    def item(self, n_index:int) -> str:
        """Get the file at the specified index."""
        return self._intf.invoke(UiFileOpenDialogExtensionCollection._metadata, UiFileOpenDialogExtensionCollection._item_metadata, n_index, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type UiFileOpenDialogExtensionCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, UiFileOpenDialogExtensionCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiFileOpenDialogExtensionCollection, [UiFileOpenDialogExtensionCollection, ])

agcls.AgClassCatalog.add_catalog_entry((4847810269717329271, 12920386918459678637), UiFileOpenDialogExtensionCollection)
agcls.AgTypeNameMap["UiFileOpenDialogExtensionCollection"] = UiFileOpenDialogExtensionCollection

class UiFileOpenDialogExtension(SupportsDeleteCallback):
    """Access to file open dialog that allows multiple file specifications."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_file_name_method_offset = 1
    _set_file_name_method_offset = 2
    _get_filter_description_method_offset = 3
    _set_filter_description_method_offset = 4
    _get_filter_pattern_method_offset = 5
    _set_filter_pattern_method_offset = 6
    _metadata = {
        "iid_data" : (5027325736684803044, 12965350138807499181),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, UiFileOpenDialogExtension)

    _get_file_name_metadata = { "offset" : _get_file_name_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def file_name(self) -> "UiFileOpenDialogExtensionCollection":
        """Get or set the multiple file open collection."""
        return self._intf.get_property(UiFileOpenDialogExtension._metadata, UiFileOpenDialogExtension._get_file_name_metadata)

    _set_file_name_metadata = { "offset" : _set_file_name_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("UiFileOpenDialogExtensionCollection"),) }
    @file_name.setter
    def file_name(self, value:"UiFileOpenDialogExtensionCollection") -> None:
        """Get or set the multiple file open collection."""
        return self._intf.set_property(UiFileOpenDialogExtension._metadata, UiFileOpenDialogExtension._set_file_name_metadata, value)

    _get_filter_description_metadata = { "offset" : _get_filter_description_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def filter_description(self) -> str:
        """Get or set the file open dialog filter description."""
        return self._intf.get_property(UiFileOpenDialogExtension._metadata, UiFileOpenDialogExtension._get_filter_description_metadata)

    _set_filter_description_metadata = { "offset" : _set_filter_description_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @filter_description.setter
    def filter_description(self, new_value:str) -> None:
        """Get or set the file open dialog filter description."""
        return self._intf.set_property(UiFileOpenDialogExtension._metadata, UiFileOpenDialogExtension._set_filter_description_metadata, new_value)

    _get_filter_pattern_metadata = { "offset" : _get_filter_pattern_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def filter_pattern(self) -> str:
        """Get or set the file open dialog filter pattern."""
        return self._intf.get_property(UiFileOpenDialogExtension._metadata, UiFileOpenDialogExtension._get_filter_pattern_metadata)

    _set_filter_pattern_metadata = { "offset" : _set_filter_pattern_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @filter_pattern.setter
    def filter_pattern(self, new_value:str) -> None:
        """Get or set the file open dialog filter pattern."""
        return self._intf.set_property(UiFileOpenDialogExtension._metadata, UiFileOpenDialogExtension._set_filter_pattern_metadata, new_value)

    _property_names[file_name] = "file_name"
    _property_names[filter_description] = "filter_description"
    _property_names[filter_pattern] = "filter_pattern"

    def __init__(self, source_object=None):
        """Construct an object of type UiFileOpenDialogExtension."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, UiFileOpenDialogExtension)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, UiFileOpenDialogExtension, [UiFileOpenDialogExtension, ])

agcls.AgClassCatalog.add_catalog_entry((5014475772752047883, 13237035948763404201), UiFileOpenDialogExtension)
agcls.AgTypeNameMap["UiFileOpenDialogExtension"] = UiFileOpenDialogExtension