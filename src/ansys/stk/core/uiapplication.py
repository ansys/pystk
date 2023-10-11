################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["APP_CONSTANTS", "APP_ERROR_CODES", "IMRUCollection", "IUiApplication", "IUiApplicationPartnerAccess", "IUiFileOpenExt", 
"IUiFileOpenExtCollection", "MRUCollection", "OPEN_LOG_FILE_MODE", "UI_LOG_MSG_TYPE", "UiApplication", "UiFileOpenExt", 
"UiFileOpenExtCollection"]

import typing

from ctypes   import byref, POINTER
from enum     import IntEnum

try:
    from numpy import ndarray 
except ModuleNotFoundError:
    pass
    
try:
    from pandas import DataFrame 
except ModuleNotFoundError:
    pass

from .internal  import comutil          as agcom
from .internal  import coclassutil      as agcls
from .internal  import marshall         as agmarshall
from .internal.comutil     import IUnknown, IDispatch, IAGFUNCTYPE, IEnumVARIANT
from .internal.eventutil   import *
from .utilities.exceptions import *

from .uicore import *


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
    _uuid = "{68FAF906-BAD0-4C7C-80D5-26E6765800F7}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IMRUCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IMRUCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IMRUCollection = agcom.GUID(IMRUCollection._uuid)
        vtable_offset_local = IMRUCollection._vtable_offset - 1
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IMRUCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.BSTR))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IMRUCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IMRUCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
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
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> str:
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    def item(self, index:typing.Any) -> str:
        """Gets the MRU at the specified index."""
        with agmarshall.VARIANT_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def count(self) -> int:
        """Gets the total count of MRUs in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates through the MRU collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{68FAF906-BAD0-4C7C-80D5-26E6765800F7}", IMRUCollection)
agcls.AgTypeNameMap["IMRUCollection"] = IMRUCollection

class IUiFileOpenExt(object):
    """Access to file open dialog that allows multiple file specifications."""
    _uuid = "{42DFA066-8474-4FAA-9F66-E4477DBD44E2}"
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_file_name"] = _raise_uninitialized_error
        self.__dict__["_set_file_name"] = _raise_uninitialized_error
        self.__dict__["_get_filter_description"] = _raise_uninitialized_error
        self.__dict__["_set_filter_description"] = _raise_uninitialized_error
        self.__dict__["_get_filter_pattern"] = _raise_uninitialized_error
        self.__dict__["_set_filter_pattern"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiFileOpenExt._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiFileOpenExt from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiFileOpenExt = agcom.GUID(IUiFileOpenExt._uuid)
        vtable_offset_local = IUiFileOpenExt._vtable_offset - 1
        self.__dict__["_get_file_name"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExt, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_set_file_name"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExt, vtable_offset_local+2, agcom.PVOID)
        self.__dict__["_get_filter_description"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExt, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_set_filter_description"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExt, vtable_offset_local+4, agcom.BSTR)
        self.__dict__["_get_filter_pattern"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExt, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_set_filter_pattern"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExt, vtable_offset_local+6, agcom.BSTR)
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
    
    @property
    def file_name(self) -> "IUiFileOpenExtCollection":
        """Gets/sets the multiple file open collection."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_file_name"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @file_name.setter
    def file_name(self, newVal:"IUiFileOpenExtCollection") -> None:
        """Gets/sets the multiple file open collection."""
        with agmarshall.AgInterface_in_arg(newVal, IUiFileOpenExtCollection) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_file_name"](arg_newVal.COM_val))

    @property
    def filter_description(self) -> str:
        """Gets/sets the file open dialog filter description."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_filter_description"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @filter_description.setter
    def filter_description(self, newVal:str) -> None:
        """Gets/sets the file open dialog filter description."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_filter_description"](arg_newVal.COM_val))

    @property
    def filter_pattern(self) -> str:
        """Gets/sets the file open dialog filter pattern."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_filter_pattern"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @filter_pattern.setter
    def filter_pattern(self, newVal:str) -> None:
        """Gets/sets the file open dialog filter pattern."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_filter_pattern"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{42DFA066-8474-4FAA-9F66-E4477DBD44E2}", IUiFileOpenExt)
agcls.AgTypeNameMap["IUiFileOpenExt"] = IUiFileOpenExt

class IUiApplication(object):
    """IUiApplication represents a root of the Application Model."""
    _uuid = "{769EDAA1-8767-4781-BC43-D968B0D67C02}"
    _num_methods = 37
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_load_personality"] = _raise_uninitialized_error
        self.__dict__["_get_personality"] = _raise_uninitialized_error
        self.__dict__["_get_visible"] = _raise_uninitialized_error
        self.__dict__["_set_visible"] = _raise_uninitialized_error
        self.__dict__["_get_user_control"] = _raise_uninitialized_error
        self.__dict__["_set_user_control"] = _raise_uninitialized_error
        self.__dict__["_get_windows"] = _raise_uninitialized_error
        self.__dict__["_get_height"] = _raise_uninitialized_error
        self.__dict__["_set_height"] = _raise_uninitialized_error
        self.__dict__["_get_width"] = _raise_uninitialized_error
        self.__dict__["_set_width"] = _raise_uninitialized_error
        self.__dict__["_get_left"] = _raise_uninitialized_error
        self.__dict__["_set_left"] = _raise_uninitialized_error
        self.__dict__["_get_top"] = _raise_uninitialized_error
        self.__dict__["_set_top"] = _raise_uninitialized_error
        self.__dict__["_get_window_state"] = _raise_uninitialized_error
        self.__dict__["_set_window_state"] = _raise_uninitialized_error
        self.__dict__["_activate"] = _raise_uninitialized_error
        self.__dict__["_get_mru_list"] = _raise_uninitialized_error
        self.__dict__["_file_open_dialog"] = _raise_uninitialized_error
        self.__dict__["_get_path"] = _raise_uninitialized_error
        self.__dict__["_create_object"] = _raise_uninitialized_error
        self.__dict__["_file_save_as_dialog"] = _raise_uninitialized_error
        self.__dict__["_quit"] = _raise_uninitialized_error
        self.__dict__["_file_open_dialog_ext"] = _raise_uninitialized_error
        self.__dict__["_get_hwnd"] = _raise_uninitialized_error
        self.__dict__["_directory_picker_dialog"] = _raise_uninitialized_error
        self.__dict__["_get_message_pending_delay"] = _raise_uninitialized_error
        self.__dict__["_set_message_pending_delay"] = _raise_uninitialized_error
        self.__dict__["_get_personality2"] = _raise_uninitialized_error
        self.__dict__["_open_log_file"] = _raise_uninitialized_error
        self.__dict__["_log_msg"] = _raise_uninitialized_error
        self.__dict__["_get_log_file"] = _raise_uninitialized_error
        self.__dict__["_get_display_alerts"] = _raise_uninitialized_error
        self.__dict__["_set_display_alerts"] = _raise_uninitialized_error
        self.__dict__["_create_application"] = _raise_uninitialized_error
        self.__dict__["_get_process_id"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiApplication._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiApplication from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiApplication = agcom.GUID(IUiApplication._uuid)
        vtable_offset_local = IUiApplication._vtable_offset - 1
        self.__dict__["_load_personality"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+1, agcom.BSTR)
        self.__dict__["_get_personality"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_get_visible"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_visible"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+4, agcom.VARIANT_BOOL)
        self.__dict__["_get_user_control"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_user_control"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+6, agcom.VARIANT_BOOL)
        self.__dict__["_get_windows"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+7, POINTER(agcom.PVOID))
        self.__dict__["_get_height"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+8, POINTER(agcom.LONG))
        self.__dict__["_set_height"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+9, agcom.LONG)
        self.__dict__["_get_width"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_set_width"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+11, agcom.LONG)
        self.__dict__["_get_left"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+12, POINTER(agcom.LONG))
        self.__dict__["_set_left"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+13, agcom.LONG)
        self.__dict__["_get_top"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+14, POINTER(agcom.LONG))
        self.__dict__["_set_top"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+15, agcom.LONG)
        self.__dict__["_get_window_state"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+16, POINTER(agcom.LONG))
        self.__dict__["_set_window_state"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+17, agcom.LONG)
        self.__dict__["_activate"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+18, )
        self.__dict__["_get_mru_list"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+19, POINTER(agcom.PVOID))
        self.__dict__["_file_open_dialog"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+20, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_get_path"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+21, POINTER(agcom.BSTR))
        self.__dict__["_create_object"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+22, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_file_save_as_dialog"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+23, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_quit"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+24, )
        self.__dict__["_file_open_dialog_ext"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+25, agcom.VARIANT_BOOL, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_get_hwnd"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+26, POINTER(agcom.LONG))
        self.__dict__["_directory_picker_dialog"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+27, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_get_message_pending_delay"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+28, POINTER(agcom.LONG))
        self.__dict__["_set_message_pending_delay"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+29, agcom.LONG)
        self.__dict__["_get_personality2"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+30, POINTER(agcom.PVOID))
        self.__dict__["_open_log_file"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+31, agcom.BSTR, agcom.LONG, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_log_msg"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+32, agcom.LONG, agcom.BSTR)
        self.__dict__["_get_log_file"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+33, POINTER(agcom.BSTR))
        self.__dict__["_get_display_alerts"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+34, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_display_alerts"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+35, agcom.VARIANT_BOOL)
        self.__dict__["_create_application"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+36, POINTER(agcom.PVOID))
        self.__dict__["_get_process_id"] = IAGFUNCTYPE(pUnk, IID_IUiApplication, vtable_offset_local+37, POINTER(agcom.LONG))
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
    
    def load_personality(self, persName:str) -> None:
        """Loads a personality by its name."""
        with agmarshall.BSTR_arg(persName) as arg_persName:
            agcls.evaluate_hresult(self.__dict__["_load_personality"](arg_persName.COM_val))

    @property
    def personality(self) -> typing.Any:
        """Returns a reference to the currently loaded personality."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_personality"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def visible(self) -> bool:
        """Gets/sets whether the main window is visible."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_visible"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @visible.setter
    def visible(self, newVal:bool) -> None:
        """Gets/sets whether the main window is visible."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_visible"](arg_newVal.COM_val))

    @property
    def user_control(self) -> bool:
        """Gets/sets whether the application is user controlled."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_user_control"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @user_control.setter
    def user_control(self, newVal:bool) -> None:
        """Gets/sets whether the application is user controlled."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_user_control"](arg_newVal.COM_val))

    @property
    def windows(self) -> "IUiWindowsCollection":
        """Returns a collection of windows."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_windows"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def height(self) -> int:
        """Gets/sets a height of the main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_height"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @height.setter
    def height(self, newVal:int) -> None:
        """Gets/sets a height of the main window."""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_height"](arg_newVal.COM_val))

    @property
    def width(self) -> int:
        """Gets/sets a width of the main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_width"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @width.setter
    def width(self, newVal:int) -> None:
        """Gets/sets a width of the main window."""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_width"](arg_newVal.COM_val))

    @property
    def left(self) -> int:
        """Gets/sets a vertical coordinate of the main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_left"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @left.setter
    def left(self, newVal:int) -> None:
        """Gets/sets a vertical coordinate of the main window."""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_left"](arg_newVal.COM_val))

    @property
    def top(self) -> int:
        """Gets/sets a horizontal coordinate of the main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_top"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @top.setter
    def top(self, newVal:int) -> None:
        """Gets/sets a horizontal coordinate of the main window."""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_top"](arg_newVal.COM_val))

    @property
    def window_state(self) -> "WINDOW_STATE":
        """Gets/sets the state of the main window."""
        with agmarshall.AgEnum_arg(WINDOW_STATE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_window_state"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @window_state.setter
    def window_state(self, newVal:"WINDOW_STATE") -> None:
        """Gets/sets the state of the main window."""
        with agmarshall.AgEnum_arg(WINDOW_STATE, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_window_state"](arg_newVal.COM_val))

    def activate(self) -> None:
        """Activates the application's main window."""
        agcls.evaluate_hresult(self.__dict__["_activate"]())

    @property
    def mru_list(self) -> "IMRUCollection":
        """Returns a collection most recently used files."""
        with agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_mru_list"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def file_open_dialog(self, defaultExt:str, filter:str, initialDir:str) -> str:
        """Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name."""
        with agmarshall.BSTR_arg(defaultExt) as arg_defaultExt, \
             agmarshall.BSTR_arg(filter) as arg_filter, \
             agmarshall.BSTR_arg(initialDir) as arg_initialDir, \
             agmarshall.BSTR_arg() as arg_pFileName:
            agcls.evaluate_hresult(self.__dict__["_file_open_dialog"](arg_defaultExt.COM_val, arg_filter.COM_val, arg_initialDir.COM_val, byref(arg_pFileName.COM_val)))
            return arg_pFileName.python_val

    @property
    def path(self) -> str:
        """Returns the complete path to the application, excluding the final separator and name of the application. Read-only String."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_path"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def create_object(self, progID:str, remoteServer:str) -> typing.Any:
        """Only works from local HTML pages and scripts"""
        with agmarshall.BSTR_arg(progID) as arg_progID, \
             agmarshall.BSTR_arg(remoteServer) as arg_remoteServer, \
             agmarshall.AgInterface_out_arg() as arg_ppObject:
            agcls.evaluate_hresult(self.__dict__["_create_object"](arg_progID.COM_val, arg_remoteServer.COM_val, byref(arg_ppObject.COM_val)))
            return arg_ppObject.python_val

    def file_save_as_dialog(self, defaultExt:str, filter:str, initialDir:str) -> str:
        """Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name."""
        with agmarshall.BSTR_arg(defaultExt) as arg_defaultExt, \
             agmarshall.BSTR_arg(filter) as arg_filter, \
             agmarshall.BSTR_arg(initialDir) as arg_initialDir, \
             agmarshall.BSTR_arg() as arg_pFileName:
            agcls.evaluate_hresult(self.__dict__["_file_save_as_dialog"](arg_defaultExt.COM_val, arg_filter.COM_val, arg_initialDir.COM_val, byref(arg_pFileName.COM_val)))
            return arg_pFileName.python_val

    def quit(self) -> None:
        """Shuts down the application."""
        agcls.evaluate_hresult(self.__dict__["_quit"]())

    def file_open_dialog_ext(self, allowMultiSelect:bool, defaultExt:str, filter:str, initialDir:str) -> "IUiFileOpenExt":
        """Brings up a standard File Open Dialog and returns an object representing the selected file."""
        with agmarshall.VARIANT_BOOL_arg(allowMultiSelect) as arg_allowMultiSelect, \
             agmarshall.BSTR_arg(defaultExt) as arg_defaultExt, \
             agmarshall.BSTR_arg(filter) as arg_filter, \
             agmarshall.BSTR_arg(initialDir) as arg_initialDir, \
             agmarshall.AgInterface_out_arg() as arg_ppObject:
            agcls.evaluate_hresult(self.__dict__["_file_open_dialog_ext"](arg_allowMultiSelect.COM_val, arg_defaultExt.COM_val, arg_filter.COM_val, arg_initialDir.COM_val, byref(arg_ppObject.COM_val)))
            return arg_ppObject.python_val

    @property
    def hwnd(self) -> int:
        """Returns an HWND handle associated with the application main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_hwnd"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def directory_picker_dialog(self, title:str, initialDir:str) -> str:
        """Brings up the Directory Picker Dialog and returns a selected directory name."""
        with agmarshall.BSTR_arg(title) as arg_title, \
             agmarshall.BSTR_arg(initialDir) as arg_initialDir, \
             agmarshall.BSTR_arg() as arg_pDirName:
            agcls.evaluate_hresult(self.__dict__["_directory_picker_dialog"](arg_title.COM_val, arg_initialDir.COM_val, byref(arg_pDirName.COM_val)))
            return arg_pDirName.python_val

    @property
    def message_pending_delay(self) -> int:
        """Gets/Sets message-pending delay for server busy dialog (in milliseconds )"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_message_pending_delay"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @message_pending_delay.setter
    def message_pending_delay(self, newVal:int) -> None:
        """Gets/Sets message-pending delay for server busy dialog (in milliseconds)"""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_message_pending_delay"](arg_newVal.COM_val))

    @property
    def personality2(self) -> typing.Any:
        """Returns an new instance of the root object of the STK Object Model"""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_personality2"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def open_log_file(self, logFileName:str, logFileMode:"OPEN_LOG_FILE_MODE") -> bool:
        """Specifies the current log file to be written to."""
        with agmarshall.BSTR_arg(logFileName) as arg_logFileName, \
             agmarshall.AgEnum_arg(OPEN_LOG_FILE_MODE, logFileMode) as arg_logFileMode, \
             agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_open_log_file"](arg_logFileName.COM_val, arg_logFileMode.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def log_msg(self, msgType:"UI_LOG_MSG_TYPE", msg:str) -> None:
        """Logs the Message specified."""
        with agmarshall.AgEnum_arg(UI_LOG_MSG_TYPE, msgType) as arg_msgType, \
             agmarshall.BSTR_arg(msg) as arg_msg:
            agcls.evaluate_hresult(self.__dict__["_log_msg"](arg_msgType.COM_val, arg_msg.COM_val))

    @property
    def log_file(self) -> str:
        """Gets the current log files full path."""
        with agmarshall.BSTR_arg() as arg_pLogFilePath:
            agcls.evaluate_hresult(self.__dict__["_get_log_file"](byref(arg_pLogFilePath.COM_val)))
            return arg_pLogFilePath.python_val

    @property
    def display_alerts(self) -> bool:
        """Set to true to display certain alerts and messages. Otherwise false. The default value is True."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_display_alerts"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @display_alerts.setter
    def display_alerts(self, displayAlerts:bool) -> None:
        """Set to true to display certain alerts and messages. Otherwise false. The default value is True."""
        with agmarshall.VARIANT_BOOL_arg(displayAlerts) as arg_displayAlerts:
            agcls.evaluate_hresult(self.__dict__["_set_display_alerts"](arg_displayAlerts.COM_val))

    def create_application(self) -> "IUiApplication":
        """Create a new instance of the application model root object."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_create_application"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    @property
    def process_id(self) -> int:
        """Gets process id for the current instance."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_process_id"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{769EDAA1-8767-4781-BC43-D968B0D67C02}", IUiApplication)
agcls.AgTypeNameMap["IUiApplication"] = IUiApplication

class IUiApplicationPartnerAccess(object):
    """Access to the application object model for business partners."""
    _uuid = "{DFC7DB2A-FA00-47B7-95D8-0E1171705A0F}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_grant_partner_access"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiApplicationPartnerAccess._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiApplicationPartnerAccess from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiApplicationPartnerAccess = agcom.GUID(IUiApplicationPartnerAccess._uuid)
        vtable_offset_local = IUiApplicationPartnerAccess._vtable_offset - 1
        self.__dict__["_grant_partner_access"] = IAGFUNCTYPE(pUnk, IID_IUiApplicationPartnerAccess, vtable_offset_local+1, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
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
    
    def grant_partner_access(self, vendor:str, product:str, key:str) -> typing.Any:
        """Provide object model root for authorized business partners."""
        with agmarshall.BSTR_arg(vendor) as arg_vendor, \
             agmarshall.BSTR_arg(product) as arg_product, \
             agmarshall.BSTR_arg(key) as arg_key, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_grant_partner_access"](arg_vendor.COM_val, arg_product.COM_val, arg_key.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{DFC7DB2A-FA00-47B7-95D8-0E1171705A0F}", IUiApplicationPartnerAccess)
agcls.AgTypeNameMap["IUiApplicationPartnerAccess"] = IUiApplicationPartnerAccess

class IUiFileOpenExtCollection(object):
    """Multiple file open collection."""
    _uuid = "{564BF89D-F0F8-4E98-A5A4-033DB16FC659}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_item"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiFileOpenExtCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiFileOpenExtCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiFileOpenExtCollection = agcom.GUID(IUiFileOpenExtCollection._uuid)
        vtable_offset_local = IUiFileOpenExtCollection._vtable_offset - 1
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExtCollection, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExtCollection, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IUiFileOpenExtCollection, vtable_offset_local+3, agcom.LONG, POINTER(agcom.BSTR))
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
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> str:
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    @property
    def count(self) -> int:
        """Gets the total count of files in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates through the file collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def item(self, nIndex:int) -> str:
        """Gets the file at the specified index."""
        with agmarshall.LONG_arg(nIndex) as arg_nIndex, \
             agmarshall.BSTR_arg() as arg_pBSTR:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_nIndex.COM_val, byref(arg_pBSTR.COM_val)))
            return arg_pBSTR.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{564BF89D-F0F8-4E98-A5A4-033DB16FC659}", IUiFileOpenExtCollection)
agcls.AgTypeNameMap["IUiFileOpenExtCollection"] = IUiFileOpenExtCollection



class UiApplication(IUiApplication, IUiApplicationPartnerAccess):
    """A root object of the Application Model."""
    def __init__(self, sourceObject=None):
        IUiApplication.__init__(self, sourceObject)
        IUiApplicationPartnerAccess.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiApplication._private_init(self, pUnk)
        IUiApplicationPartnerAccess._private_init(self, pUnk)
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


class MRUCollection(IMRUCollection):
    """Provides information about most recently used (MRU) list."""
    def __init__(self, sourceObject=None):
        IMRUCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IMRUCollection._private_init(self, pUnk)
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


class UiFileOpenExtCollection(IUiFileOpenExtCollection):
    """Multiple file open collection."""
    def __init__(self, sourceObject=None):
        IUiFileOpenExtCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiFileOpenExtCollection._private_init(self, pUnk)
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


class UiFileOpenExt(IUiFileOpenExt):
    """Access to file open dialog that allows multiple file specifications."""
    def __init__(self, sourceObject=None):
        IUiFileOpenExt.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiFileOpenExt._private_init(self, pUnk)
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



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
