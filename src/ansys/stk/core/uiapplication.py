################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

__all__ = ["APP_CONSTANTS", "APP_ERROR_CODES", "IMRUCollection", "IUiApplication", "IUiApplicationPartnerAccess", "IUiFileOpenExt", 
"IUiFileOpenExtCollection", "MRUCollection", "OPEN_LOG_FILE_MODE", "UI_LOG_MSG_TYPE", "UiApplication", "UiFileOpenExt", 
"UiFileOpenExtCollection"]

from ctypes import POINTER
from enum import IntEnum
import typing

try:
    from numpy import ndarray
except ModuleNotFoundError:
    pass
    
try:
    from pandas import DataFrame
except ModuleNotFoundError:
    pass

from .internal import coclassutil as agcls, comutil as agcom, marshall as agmarshall
from .internal.apiutil import enumerator_proxy, interface_proxy, out_arg
from .internal.comutil import IDispatch, IUnknown
from .internal.eventutil import *
from .uicore import *
from .utilities.exceptions import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class OPEN_LOG_FILE_MODE(IntEnum):
    """Log file open modes."""
    FOR_WRITING = 2
    """Open log file in write file mode."""
    FOR_APPENDING = 8
    """Open log file in append file mode."""

OPEN_LOG_FILE_MODE.FOR_WRITING.__doc__ = "Open log file in write file mode."
OPEN_LOG_FILE_MODE.FOR_APPENDING.__doc__ = "Open log file in append file mode."

agcls.AgTypeNameMap["OPEN_LOG_FILE_MODE"] = OPEN_LOG_FILE_MODE

class UI_LOG_MSG_TYPE(IntEnum):
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

UI_LOG_MSG_TYPE.DEBUG.__doc__ = "Log messages that provide Debug text."
UI_LOG_MSG_TYPE.INFO.__doc__ = "Log messages that provide information text."
UI_LOG_MSG_TYPE.FORCE_INFO.__doc__ = "Log messages that provide forceful information text."
UI_LOG_MSG_TYPE.WARNING.__doc__ = "Log messages that provide warning text."
UI_LOG_MSG_TYPE.ALARM.__doc__ = "Log messages that provide alarm text."

agcls.AgTypeNameMap["UI_LOG_MSG_TYPE"] = UI_LOG_MSG_TYPE

class APP_CONSTANTS(IntEnum):
    """APP_CONSTANTS contains base IDs for various structures."""
    APP_ERROR_BASE = 0x200
    """Error base."""

APP_CONSTANTS.APP_ERROR_BASE.__doc__ = "Error base."

agcls.AgTypeNameMap["APP_CONSTANTS"] = APP_CONSTANTS

class APP_ERROR_CODES(IntEnum):
    """App error codes."""
    PERS_LOAD_FAIL = (((1 << 31) | (4 << 16)) | (APP_CONSTANTS.APP_ERROR_BASE + 1))
    """Failed to load personality."""
    ALREADY_LOAD_FAIL = (((1 << 31) | (4 << 16)) | (APP_CONSTANTS.APP_ERROR_BASE + 2))
    """Personality already loaded."""
    PERS_LOAD_FIRST = (((1 << 31) | (4 << 16)) | (APP_CONSTANTS.APP_ERROR_BASE + 3))
    """No personality is loaded."""
    PERS_LICENSE_ERROR = (((1 << 31) | (4 << 16)) | (APP_CONSTANTS.APP_ERROR_BASE + 4))
    """You do not have the required license to connect externally to the application."""
    NO_LICENSE_ERROR = (((1 << 31) | (4 << 16)) | (APP_CONSTANTS.APP_ERROR_BASE + 5))
    """No license could be found."""

APP_ERROR_CODES.PERS_LOAD_FAIL.__doc__ = "Failed to load personality."
APP_ERROR_CODES.ALREADY_LOAD_FAIL.__doc__ = "Personality already loaded."
APP_ERROR_CODES.PERS_LOAD_FIRST.__doc__ = "No personality is loaded."
APP_ERROR_CODES.PERS_LICENSE_ERROR.__doc__ = "You do not have the required license to connect externally to the application."
APP_ERROR_CODES.NO_LICENSE_ERROR.__doc__ = "No license could be found."

agcls.AgTypeNameMap["APP_ERROR_CODES"] = APP_ERROR_CODES


class IMRUCollection(object):
    """Provides information about most recently used (MRU) list."""
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{68FAF906-BAD0-4C7C-80D5-26E6765800F7}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "item" : 1,
                             "get_count" : 2,
                             "get__NewEnum" : 3, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IMRUCollection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IMRUCollection from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IMRUCollection.__dict__ and type(IMRUCollection.__dict__[attrname]) == property:
            return IMRUCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IMRUCollection.")
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.VARIANT, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.VARIANT_arg, agmarshall.BSTR_arg,) }
    def item(self, index:typing.Any) -> str:
        """Gets the MRU at the specified index."""
        return self._intf.invoke(IMRUCollection._metadata, IMRUCollection._item_metadata, index, out_arg())

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Gets the total count of MRUs in the collection."""
        return self._intf.get_property(IMRUCollection._metadata, IMRUCollection._get_count_metadata)

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Enumerates through the MRU collection."""
        return self._intf.get_property(IMRUCollection._metadata, IMRUCollection._get__NewEnum_metadata)

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{68FAF906-BAD0-4C7C-80D5-26E6765800F7}", IMRUCollection)
agcls.AgTypeNameMap["IMRUCollection"] = IMRUCollection

class IUiFileOpenExt(object):
    """Access to file open dialog that allows multiple file specifications."""
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{42DFA066-8474-4FAA-9F66-E4477DBD44E2}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "get_file_name" : 1,
                             "set_file_name" : 2,
                             "get_filter_description" : 3,
                             "set_filter_description" : 4,
                             "get_filter_pattern" : 5,
                             "set_filter_pattern" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUiFileOpenExt._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUiFileOpenExt from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiFileOpenExt.__dict__ and type(IUiFileOpenExt.__dict__[attrname]) == property:
            return IUiFileOpenExt.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiFileOpenExt.")
    
    _get_file_name_metadata = { "name" : "file_name",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def file_name(self) -> "UiFileOpenExtCollection":
        """Gets/sets the multiple file open collection."""
        return self._intf.get_property(IUiFileOpenExt._metadata, IUiFileOpenExt._get_file_name_metadata)

    _set_file_name_metadata = { "name" : "file_name",
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.AgInterface_in_arg("IUiFileOpenExtCollection"),) }
    @file_name.setter
    def file_name(self, newVal:"IUiFileOpenExtCollection") -> None:
        """Gets/sets the multiple file open collection."""
        return self._intf.set_property(IUiFileOpenExt._metadata, IUiFileOpenExt._set_file_name_metadata, newVal)

    _get_filter_description_metadata = { "name" : "filter_description",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def filter_description(self) -> str:
        """Gets/sets the file open dialog filter description."""
        return self._intf.get_property(IUiFileOpenExt._metadata, IUiFileOpenExt._get_filter_description_metadata)

    _set_filter_description_metadata = { "name" : "filter_description",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @filter_description.setter
    def filter_description(self, newVal:str) -> None:
        """Gets/sets the file open dialog filter description."""
        return self._intf.set_property(IUiFileOpenExt._metadata, IUiFileOpenExt._set_filter_description_metadata, newVal)

    _get_filter_pattern_metadata = { "name" : "filter_pattern",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def filter_pattern(self) -> str:
        """Gets/sets the file open dialog filter pattern."""
        return self._intf.get_property(IUiFileOpenExt._metadata, IUiFileOpenExt._get_filter_pattern_metadata)

    _set_filter_pattern_metadata = { "name" : "filter_pattern",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @filter_pattern.setter
    def filter_pattern(self, newVal:str) -> None:
        """Gets/sets the file open dialog filter pattern."""
        return self._intf.set_property(IUiFileOpenExt._metadata, IUiFileOpenExt._set_filter_pattern_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{42DFA066-8474-4FAA-9F66-E4477DBD44E2}", IUiFileOpenExt)
agcls.AgTypeNameMap["IUiFileOpenExt"] = IUiFileOpenExt

class IUiApplication(object):
    """UiApplication represents a root of the Application Model."""
    _num_methods = 37
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{769EDAA1-8767-4781-BC43-D968B0D67C02}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "load_personality" : 1,
                             "get_personality" : 2,
                             "get_visible" : 3,
                             "set_visible" : 4,
                             "get_user_control" : 5,
                             "set_user_control" : 6,
                             "get_windows" : 7,
                             "get_height" : 8,
                             "set_height" : 9,
                             "get_width" : 10,
                             "set_width" : 11,
                             "get_left" : 12,
                             "set_left" : 13,
                             "get_top" : 14,
                             "set_top" : 15,
                             "get_window_state" : 16,
                             "set_window_state" : 17,
                             "activate" : 18,
                             "get_mru_list" : 19,
                             "file_open_dialog" : 20,
                             "get_path" : 21,
                             "create_object" : 22,
                             "file_save_as_dialog" : 23,
                             "quit" : 24,
                             "file_open_dialog_ext" : 25,
                             "get_hwnd" : 26,
                             "directory_picker_dialog" : 27,
                             "get_message_pending_delay" : 28,
                             "set_message_pending_delay" : 29,
                             "get_personality2" : 30,
                             "open_log_file" : 31,
                             "log_msg" : 32,
                             "get_log_file" : 33,
                             "get_display_alerts" : 34,
                             "set_display_alerts" : 35,
                             "create_application" : 36,
                             "get_process_id" : 37, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUiApplication._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUiApplication from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiApplication.__dict__ and type(IUiApplication.__dict__[attrname]) == property:
            return IUiApplication.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiApplication.")
    
    _load_personality_metadata = { "name" : "load_personality",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    def load_personality(self, persName:str) -> None:
        """Loads a personality by its name."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._load_personality_metadata, persName)

    _get_personality_metadata = { "name" : "personality",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def personality(self) -> typing.Any:
        """Returns a reference to the currently loaded personality."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_personality_metadata)

    _get_visible_metadata = { "name" : "visible",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def visible(self) -> bool:
        """Gets/sets whether the main window is visible."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_visible_metadata)

    _set_visible_metadata = { "name" : "visible",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @visible.setter
    def visible(self, newVal:bool) -> None:
        """Gets/sets whether the main window is visible."""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_visible_metadata, newVal)

    _get_user_control_metadata = { "name" : "user_control",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def user_control(self) -> bool:
        """Gets/sets whether the application is user controlled."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_user_control_metadata)

    _set_user_control_metadata = { "name" : "user_control",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @user_control.setter
    def user_control(self, newVal:bool) -> None:
        """Gets/sets whether the application is user controlled."""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_user_control_metadata, newVal)

    _get_windows_metadata = { "name" : "windows",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def windows(self) -> "IUiWindowsCollection":
        """Returns a collection of windows."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_windows_metadata)

    _get_height_metadata = { "name" : "height",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def height(self) -> int:
        """Gets/sets a height of the main window."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_height_metadata)

    _set_height_metadata = { "name" : "height",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @height.setter
    def height(self, newVal:int) -> None:
        """Gets/sets a height of the main window."""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_height_metadata, newVal)

    _get_width_metadata = { "name" : "width",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def width(self) -> int:
        """Gets/sets a width of the main window."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_width_metadata)

    _set_width_metadata = { "name" : "width",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @width.setter
    def width(self, newVal:int) -> None:
        """Gets/sets a width of the main window."""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_width_metadata, newVal)

    _get_left_metadata = { "name" : "left",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def left(self) -> int:
        """Gets/sets a vertical coordinate of the main window."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_left_metadata)

    _set_left_metadata = { "name" : "left",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @left.setter
    def left(self, newVal:int) -> None:
        """Gets/sets a vertical coordinate of the main window."""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_left_metadata, newVal)

    _get_top_metadata = { "name" : "top",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def top(self) -> int:
        """Gets/sets a horizontal coordinate of the main window."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_top_metadata)

    _set_top_metadata = { "name" : "top",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @top.setter
    def top(self, newVal:int) -> None:
        """Gets/sets a horizontal coordinate of the main window."""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_top_metadata, newVal)

    _get_window_state_metadata = { "name" : "window_state",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(WINDOW_STATE),) }
    @property
    def window_state(self) -> "WINDOW_STATE":
        """Gets/sets the state of the main window."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_window_state_metadata)

    _set_window_state_metadata = { "name" : "window_state",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(WINDOW_STATE),) }
    @window_state.setter
    def window_state(self, newVal:"WINDOW_STATE") -> None:
        """Gets/sets the state of the main window."""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_window_state_metadata, newVal)

    _activate_metadata = { "name" : "activate",
            "arg_types" : (),
            "marshallers" : () }
    def activate(self) -> None:
        """Activates the application's main window."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._activate_metadata, )

    _get_mru_list_metadata = { "name" : "mru_list",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def mru_list(self) -> "MRUCollection":
        """Returns a collection most recently used files."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_mru_list_metadata)

    _file_open_dialog_metadata = { "name" : "file_open_dialog",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def file_open_dialog(self, defaultExt:str, filter:str, initialDir:str) -> str:
        """Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._file_open_dialog_metadata, defaultExt, filter, initialDir, out_arg())

    _get_path_metadata = { "name" : "path",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def path(self) -> str:
        """Returns the complete path to the application, excluding the final separator and name of the application. Read-only String."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_path_metadata)

    _create_object_metadata = { "name" : "create_object",
            "arg_types" : (agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def create_object(self, progID:str, remoteServer:str) -> typing.Any:
        """Only works from local HTML pages and scripts"""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._create_object_metadata, progID, remoteServer, out_arg())

    _file_save_as_dialog_metadata = { "name" : "file_save_as_dialog",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def file_save_as_dialog(self, defaultExt:str, filter:str, initialDir:str) -> str:
        """Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._file_save_as_dialog_metadata, defaultExt, filter, initialDir, out_arg())

    _quit_metadata = { "name" : "quit",
            "arg_types" : (),
            "marshallers" : () }
    def quit(self) -> None:
        """Shuts down the application."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._quit_metadata, )

    _file_open_dialog_ext_metadata = { "name" : "file_open_dialog_ext",
            "arg_types" : (agcom.VARIANT_BOOL, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def file_open_dialog_ext(self, allowMultiSelect:bool, defaultExt:str, filter:str, initialDir:str) -> "UiFileOpenExt":
        """Brings up a standard File Open Dialog and returns an object representing the selected file."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._file_open_dialog_ext_metadata, allowMultiSelect, defaultExt, filter, initialDir, out_arg())

    _get_hwnd_metadata = { "name" : "hwnd",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def hwnd(self) -> int:
        """Returns an HWND handle associated with the application main window."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_hwnd_metadata)

    _directory_picker_dialog_metadata = { "name" : "directory_picker_dialog",
            "arg_types" : (agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def directory_picker_dialog(self, title:str, initialDir:str) -> str:
        """Brings up the Directory Picker Dialog and returns a selected directory name."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._directory_picker_dialog_metadata, title, initialDir, out_arg())

    _get_message_pending_delay_metadata = { "name" : "message_pending_delay",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def message_pending_delay(self) -> int:
        """Gets/Sets message-pending delay for server busy dialog (in milliseconds )"""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_message_pending_delay_metadata)

    _set_message_pending_delay_metadata = { "name" : "message_pending_delay",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @message_pending_delay.setter
    def message_pending_delay(self, newVal:int) -> None:
        """Gets/Sets message-pending delay for server busy dialog (in milliseconds)"""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_message_pending_delay_metadata, newVal)

    _get_personality2_metadata = { "name" : "personality2",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def personality2(self) -> typing.Any:
        """Returns an new instance of the root object of the STK Object Model"""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_personality2_metadata)

    _open_log_file_metadata = { "name" : "open_log_file",
            "arg_types" : (agcom.BSTR, agcom.LONG, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.AgEnum_arg(OPEN_LOG_FILE_MODE), agmarshall.VARIANT_BOOL_arg,) }
    def open_log_file(self, logFileName:str, logFileMode:"OPEN_LOG_FILE_MODE") -> bool:
        """Specifies the current log file to be written to."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._open_log_file_metadata, logFileName, logFileMode, out_arg())

    _log_msg_metadata = { "name" : "log_msg",
            "arg_types" : (agcom.LONG, agcom.BSTR,),
            "marshallers" : (agmarshall.AgEnum_arg(UI_LOG_MSG_TYPE), agmarshall.BSTR_arg,) }
    def log_msg(self, msgType:"UI_LOG_MSG_TYPE", msg:str) -> None:
        """Logs the Message specified."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._log_msg_metadata, msgType, msg)

    _get_log_file_metadata = { "name" : "log_file",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def log_file(self) -> str:
        """Gets the current log files full path."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_log_file_metadata)

    _get_display_alerts_metadata = { "name" : "display_alerts",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def display_alerts(self) -> bool:
        """Set to true to display certain alerts and messages. Otherwise false. The default value is True."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_display_alerts_metadata)

    _set_display_alerts_metadata = { "name" : "display_alerts",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @display_alerts.setter
    def display_alerts(self, displayAlerts:bool) -> None:
        """Set to true to display certain alerts and messages. Otherwise false. The default value is True."""
        return self._intf.set_property(IUiApplication._metadata, IUiApplication._set_display_alerts_metadata, displayAlerts)

    _create_application_metadata = { "name" : "create_application",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    def create_application(self) -> "UiApplication":
        """Create a new instance of the application model root object."""
        return self._intf.invoke(IUiApplication._metadata, IUiApplication._create_application_metadata, out_arg())

    _get_process_id_metadata = { "name" : "process_id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def process_id(self) -> int:
        """Gets process id for the current instance."""
        return self._intf.get_property(IUiApplication._metadata, IUiApplication._get_process_id_metadata)


agcls.AgClassCatalog.add_catalog_entry("{769EDAA1-8767-4781-BC43-D968B0D67C02}", IUiApplication)
agcls.AgTypeNameMap["IUiApplication"] = IUiApplication

class IUiApplicationPartnerAccess(object):
    """Access to the application object model for business partners."""
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "uuid" : "{DFC7DB2A-FA00-47B7-95D8-0E1171705A0F}",
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
        "method_offsets" : { "grant_partner_access" : 1, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUiApplicationPartnerAccess._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUiApplicationPartnerAccess from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiApplicationPartnerAccess.__dict__ and type(IUiApplicationPartnerAccess.__dict__[attrname]) == property:
            return IUiApplicationPartnerAccess.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiApplicationPartnerAccess.")
    
    _grant_partner_access_metadata = { "name" : "grant_partner_access",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def grant_partner_access(self, vendor:str, product:str, key:str) -> typing.Any:
        """Provide object model root for authorized business partners."""
        return self._intf.invoke(IUiApplicationPartnerAccess._metadata, IUiApplicationPartnerAccess._grant_partner_access_metadata, vendor, product, key, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{DFC7DB2A-FA00-47B7-95D8-0E1171705A0F}", IUiApplicationPartnerAccess)
agcls.AgTypeNameMap["IUiApplicationPartnerAccess"] = IUiApplicationPartnerAccess

class IUiFileOpenExtCollection(object):
    """Multiple file open collection."""
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{564BF89D-F0F8-4E98-A5A4-033DB16FC659}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_count" : 1,
                             "get__NewEnum" : 2,
                             "item" : 3, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUiFileOpenExtCollection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUiFileOpenExtCollection from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiFileOpenExtCollection.__dict__ and type(IUiFileOpenExtCollection.__dict__[attrname]) == property:
            return IUiFileOpenExtCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiFileOpenExtCollection.")
    def __iter__(self):
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Gets the total count of files in the collection."""
        return self._intf.get_property(IUiFileOpenExtCollection._metadata, IUiFileOpenExtCollection._get_count_metadata)

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Enumerates through the file collection."""
        return self._intf.get_property(IUiFileOpenExtCollection._metadata, IUiFileOpenExtCollection._get__NewEnum_metadata)

    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.BSTR_arg,) }
    def item(self, nIndex:int) -> str:
        """Gets the file at the specified index."""
        return self._intf.invoke(IUiFileOpenExtCollection._metadata, IUiFileOpenExtCollection._item_metadata, nIndex, out_arg())

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{564BF89D-F0F8-4E98-A5A4-033DB16FC659}", IUiFileOpenExtCollection)
agcls.AgTypeNameMap["IUiFileOpenExtCollection"] = IUiFileOpenExtCollection



class UiApplication(IUiApplication, IUiApplicationPartnerAccess):
    """A root object of the Application Model."""
    def __init__(self, sourceObject=None):
        IUiApplication.__init__(self, sourceObject)
        IUiApplicationPartnerAccess.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUiApplication._private_init(self, intf)
        IUiApplicationPartnerAccess._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiApplication._get_property(self, attrname) is not None: found_prop = IUiApplication._get_property(self, attrname)
        if IUiApplicationPartnerAccess._get_property(self, attrname) is not None: found_prop = IUiApplicationPartnerAccess._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiApplication.")

agcls.AgClassCatalog.add_catalog_entry("{7ADA6C22-FA34-4578-8BE8-65405A55EE15}", UiApplication)
agcls.AgTypeNameMap["UiApplication"] = UiApplication

class MRUCollection(IMRUCollection):
    """Provides information about most recently used (MRU) list."""
    def __init__(self, sourceObject=None):
        IMRUCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IMRUCollection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IMRUCollection._get_property(self, attrname) is not None: found_prop = IMRUCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in MRUCollection.")

agcls.AgClassCatalog.add_catalog_entry("{8033C4FF-4A7D-4416-9B07-6807EA9C794E}", MRUCollection)
agcls.AgTypeNameMap["MRUCollection"] = MRUCollection

class UiFileOpenExtCollection(IUiFileOpenExtCollection):
    """Multiple file open collection."""
    def __init__(self, sourceObject=None):
        IUiFileOpenExtCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUiFileOpenExtCollection._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiFileOpenExtCollection._get_property(self, attrname) is not None: found_prop = IUiFileOpenExtCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiFileOpenExtCollection.")

agcls.AgClassCatalog.add_catalog_entry("{A733AF99-E82E-42D8-AD9A-29BB005B3703}", UiFileOpenExtCollection)
agcls.AgTypeNameMap["UiFileOpenExtCollection"] = UiFileOpenExtCollection

class UiFileOpenExt(IUiFileOpenExt):
    """Access to file open dialog that allows multiple file specifications."""
    def __init__(self, sourceObject=None):
        IUiFileOpenExt.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUiFileOpenExt._private_init(self, intf)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiFileOpenExt._get_property(self, attrname) is not None: found_prop = IUiFileOpenExt._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiFileOpenExt.")

agcls.AgClassCatalog.add_catalog_entry("{26A2C933-DB59-434E-85FD-2D92A97AA8AD}", UiFileOpenExt)
agcls.AgTypeNameMap["UiFileOpenExt"] = UiFileOpenExt


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
