################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["AgEAppConstants", "AgEAppErrorCodes", "AgEOpenLogFileMode", "AgEUiLogMsgType", "AgMRUCollection", "AgUiApplication", 
"AgUiFileOpenExt", "AgUiFileOpenExtCollection", "IAgMRUCollection", "IAgUiApplication", "IAgUiApplicationPartnerAccess", 
"IAgUiFileOpenExt", "IAgUiFileOpenExtCollection"]

import typing

from ctypes   import byref, POINTER
from datetime import datetime
from enum     import IntEnum, IntFlag

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
from .internal  import dataanalysisutil as agdata
from .utilities import colors           as agcolor
from .internal.comutil     import IUnknown, IDispatch, IPictureDisp, IAGFUNCTYPE, IEnumVARIANT
from .internal.eventutil   import *
from .utilities.exceptions import *


from .uicore import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgEOpenLogFileMode(IntEnum):
    """Log file open modes."""
    # Open log file in write file mode.
    eOpenLogFileForWriting = 2
    # Open log file in append file mode.
    eOpenLogFileForAppending = 8

agcls.AgTypeNameMap["AgEOpenLogFileMode"] = AgEOpenLogFileMode

class AgEUiLogMsgType(IntEnum):
    """Log message types."""
    # Log messages that provide Debug text.
    eUiLogMsgDebug = 0
    # Log messages that provide information text.
    eUiLogMsgInfo = 1
    # Log messages that provide forceful information text.
    eUiLogMsgForceInfo = 2
    # Log messages that provide warning text.
    eUiLogMsgWarning = 3
    # Log messages that provide alarm text.
    eUiLogMsgAlarm = 4

agcls.AgTypeNameMap["AgEUiLogMsgType"] = AgEUiLogMsgType

class AgEAppConstants(IntEnum):
    """AgEAppConstants contains base IDs for various structures."""
    # Error base.
    eAppErrorBase = 0x200

agcls.AgTypeNameMap["AgEAppConstants"] = AgEAppConstants

class AgEAppErrorCodes(IntEnum):
    """App error codes."""
    # Failed to load personality.
    eAppErrorPersLoadFail = (((1 << 31) | (4 << 16)) | (AgEAppConstants.eAppErrorBase + 1))
    # Personality already loaded.
    eAppErrorAlreadyLoadFail = (((1 << 31) | (4 << 16)) | (AgEAppConstants.eAppErrorBase + 2))
    # No personality is loaded.
    eAppErrorPersLoadFirst = (((1 << 31) | (4 << 16)) | (AgEAppConstants.eAppErrorBase + 3))
    # You do not have the required license to connect externally to the application.
    eAppErrorPersLicenseError = (((1 << 31) | (4 << 16)) | (AgEAppConstants.eAppErrorBase + 4))
    # No license could be found.
    eAppErrorNoLicenseError = (((1 << 31) | (4 << 16)) | (AgEAppConstants.eAppErrorBase + 5))

agcls.AgTypeNameMap["AgEAppErrorCodes"] = AgEAppErrorCodes


class IAgMRUCollection(object):
    """Provides information about most recently used (MRU) list."""
    _uuid = "{68FAF906-BAD0-4C7C-80D5-26E6765800F7}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgMRUCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgMRUCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgMRUCollection = agcom.GUID(IAgMRUCollection._uuid)
        vtable_offset_local = IAgMRUCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgMRUCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.BSTR))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgMRUCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgMRUCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgMRUCollection.__dict__ and type(IAgMRUCollection.__dict__[attrname]) == property:
            return IAgMRUCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgMRUCollection.")
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
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, index:typing.Any) -> str:
        """Gets the MRU at the specified index."""
        with agmarshall.VARIANT_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Count(self) -> int:
        """Gets the total count of MRUs in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates through the MRU collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{68FAF906-BAD0-4C7C-80D5-26E6765800F7}", IAgMRUCollection)
agcls.AgTypeNameMap["IAgMRUCollection"] = IAgMRUCollection

class IAgUiFileOpenExt(object):
    """Access to file open dialog that allows multiple file specifications."""
    _uuid = "{42DFA066-8474-4FAA-9F66-E4477DBD44E2}"
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFileName"] = _raise_uninitialized_error
        self.__dict__["_SetFileName"] = _raise_uninitialized_error
        self.__dict__["_GetFilterDescription"] = _raise_uninitialized_error
        self.__dict__["_SetFilterDescription"] = _raise_uninitialized_error
        self.__dict__["_GetFilterPattern"] = _raise_uninitialized_error
        self.__dict__["_SetFilterPattern"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiFileOpenExt._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiFileOpenExt from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiFileOpenExt = agcom.GUID(IAgUiFileOpenExt._uuid)
        vtable_offset_local = IAgUiFileOpenExt._vtable_offset - 1
        self.__dict__["_GetFileName"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExt, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_SetFileName"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExt, vtable_offset_local+2, agcom.PVOID)
        self.__dict__["_GetFilterDescription"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExt, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_SetFilterDescription"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExt, vtable_offset_local+4, agcom.BSTR)
        self.__dict__["_GetFilterPattern"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExt, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_SetFilterPattern"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExt, vtable_offset_local+6, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiFileOpenExt.__dict__ and type(IAgUiFileOpenExt.__dict__[attrname]) == property:
            return IAgUiFileOpenExt.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiFileOpenExt.")
    
    @property
    def FileName(self) -> "IAgUiFileOpenExtCollection":
        """Gets/sets the multiple file open collection."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFileName"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FileName.setter
    def FileName(self, newVal:"IAgUiFileOpenExtCollection") -> None:
        """Gets/sets the multiple file open collection."""
        with agmarshall.AgInterface_in_arg(newVal, IAgUiFileOpenExtCollection) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFileName"](arg_newVal.COM_val))

    @property
    def FilterDescription(self) -> str:
        """Gets/sets the file open dialog filter description."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFilterDescription"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FilterDescription.setter
    def FilterDescription(self, newVal:str) -> None:
        """Gets/sets the file open dialog filter description."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFilterDescription"](arg_newVal.COM_val))

    @property
    def FilterPattern(self) -> str:
        """Gets/sets the file open dialog filter pattern."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFilterPattern"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FilterPattern.setter
    def FilterPattern(self, newVal:str) -> None:
        """Gets/sets the file open dialog filter pattern."""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFilterPattern"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{42DFA066-8474-4FAA-9F66-E4477DBD44E2}", IAgUiFileOpenExt)
agcls.AgTypeNameMap["IAgUiFileOpenExt"] = IAgUiFileOpenExt

class IAgUiApplication(object):
    """IAgUiApplication represents a root of the Application Model."""
    _uuid = "{769EDAA1-8767-4781-BC43-D968B0D67C02}"
    _num_methods = 37
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_LoadPersonality"] = _raise_uninitialized_error
        self.__dict__["_GetPersonality"] = _raise_uninitialized_error
        self.__dict__["_GetVisible"] = _raise_uninitialized_error
        self.__dict__["_SetVisible"] = _raise_uninitialized_error
        self.__dict__["_GetUserControl"] = _raise_uninitialized_error
        self.__dict__["_SetUserControl"] = _raise_uninitialized_error
        self.__dict__["_GetWindows"] = _raise_uninitialized_error
        self.__dict__["_GetHeight"] = _raise_uninitialized_error
        self.__dict__["_SetHeight"] = _raise_uninitialized_error
        self.__dict__["_GetWidth"] = _raise_uninitialized_error
        self.__dict__["_SetWidth"] = _raise_uninitialized_error
        self.__dict__["_GetLeft"] = _raise_uninitialized_error
        self.__dict__["_SetLeft"] = _raise_uninitialized_error
        self.__dict__["_GetTop"] = _raise_uninitialized_error
        self.__dict__["_SetTop"] = _raise_uninitialized_error
        self.__dict__["_GetWindowState"] = _raise_uninitialized_error
        self.__dict__["_SetWindowState"] = _raise_uninitialized_error
        self.__dict__["_Activate"] = _raise_uninitialized_error
        self.__dict__["_GetMRUList"] = _raise_uninitialized_error
        self.__dict__["_FileOpenDialog"] = _raise_uninitialized_error
        self.__dict__["_GetPath"] = _raise_uninitialized_error
        self.__dict__["_CreateObject"] = _raise_uninitialized_error
        self.__dict__["_FileSaveAsDialog"] = _raise_uninitialized_error
        self.__dict__["_Quit"] = _raise_uninitialized_error
        self.__dict__["_FileOpenDialogExt"] = _raise_uninitialized_error
        self.__dict__["_GetHWND"] = _raise_uninitialized_error
        self.__dict__["_DirectoryPickerDialog"] = _raise_uninitialized_error
        self.__dict__["_GetMessagePendingDelay"] = _raise_uninitialized_error
        self.__dict__["_SetMessagePendingDelay"] = _raise_uninitialized_error
        self.__dict__["_GetPersonality2"] = _raise_uninitialized_error
        self.__dict__["_OpenLogFile"] = _raise_uninitialized_error
        self.__dict__["_LogMsg"] = _raise_uninitialized_error
        self.__dict__["_GetLogFile"] = _raise_uninitialized_error
        self.__dict__["_GetDisplayAlerts"] = _raise_uninitialized_error
        self.__dict__["_SetDisplayAlerts"] = _raise_uninitialized_error
        self.__dict__["_CreateApplication"] = _raise_uninitialized_error
        self.__dict__["_GetProcessID"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiApplication._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiApplication from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiApplication = agcom.GUID(IAgUiApplication._uuid)
        vtable_offset_local = IAgUiApplication._vtable_offset - 1
        self.__dict__["_LoadPersonality"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+1, agcom.BSTR)
        self.__dict__["_GetPersonality"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetVisible"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetVisible"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+4, agcom.VARIANT_BOOL)
        self.__dict__["_GetUserControl"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetUserControl"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+6, agcom.VARIANT_BOOL)
        self.__dict__["_GetWindows"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+7, POINTER(agcom.PVOID))
        self.__dict__["_GetHeight"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+8, POINTER(agcom.LONG))
        self.__dict__["_SetHeight"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+9, agcom.LONG)
        self.__dict__["_GetWidth"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_SetWidth"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+11, agcom.LONG)
        self.__dict__["_GetLeft"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+12, POINTER(agcom.LONG))
        self.__dict__["_SetLeft"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+13, agcom.LONG)
        self.__dict__["_GetTop"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+14, POINTER(agcom.LONG))
        self.__dict__["_SetTop"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+15, agcom.LONG)
        self.__dict__["_GetWindowState"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+16, POINTER(agcom.LONG))
        self.__dict__["_SetWindowState"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+17, agcom.LONG)
        self.__dict__["_Activate"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+18, )
        self.__dict__["_GetMRUList"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+19, POINTER(agcom.PVOID))
        self.__dict__["_FileOpenDialog"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+20, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_GetPath"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+21, POINTER(agcom.BSTR))
        self.__dict__["_CreateObject"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+22, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_FileSaveAsDialog"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+23, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_Quit"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+24, )
        self.__dict__["_FileOpenDialogExt"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+25, agcom.VARIANT_BOOL, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_GetHWND"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+26, POINTER(agcom.LONG))
        self.__dict__["_DirectoryPickerDialog"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+27, agcom.BSTR, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_GetMessagePendingDelay"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+28, POINTER(agcom.LONG))
        self.__dict__["_SetMessagePendingDelay"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+29, agcom.LONG)
        self.__dict__["_GetPersonality2"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+30, POINTER(agcom.PVOID))
        self.__dict__["_OpenLogFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+31, agcom.BSTR, agcom.LONG, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_LogMsg"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+32, agcom.LONG, agcom.BSTR)
        self.__dict__["_GetLogFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+33, POINTER(agcom.BSTR))
        self.__dict__["_GetDisplayAlerts"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+34, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetDisplayAlerts"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+35, agcom.VARIANT_BOOL)
        self.__dict__["_CreateApplication"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+36, POINTER(agcom.PVOID))
        self.__dict__["_GetProcessID"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplication, vtable_offset_local+37, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiApplication.__dict__ and type(IAgUiApplication.__dict__[attrname]) == property:
            return IAgUiApplication.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiApplication.")
    
    def LoadPersonality(self, persName:str) -> None:
        """Loads a personality by its name."""
        with agmarshall.BSTR_arg(persName) as arg_persName:
            agcls.evaluate_hresult(self.__dict__["_LoadPersonality"](arg_persName.COM_val))

    @property
    def Personality(self) -> typing.Any:
        """Returns a reference to the currently loaded personality."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPersonality"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Visible(self) -> bool:
        """Gets/sets whether the main window is visible."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetVisible"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Visible.setter
    def Visible(self, newVal:bool) -> None:
        """Gets/sets whether the main window is visible."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetVisible"](arg_newVal.COM_val))

    @property
    def UserControl(self) -> bool:
        """Gets/sets whether the application is user controlled."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUserControl"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @UserControl.setter
    def UserControl(self, newVal:bool) -> None:
        """Gets/sets whether the application is user controlled."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUserControl"](arg_newVal.COM_val))

    @property
    def Windows(self) -> "IAgUiWindowsCollection":
        """Returns a collection of windows."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWindows"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Height(self) -> int:
        """Gets/sets a height of the main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetHeight"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Height.setter
    def Height(self, newVal:int) -> None:
        """Gets/sets a height of the main window."""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetHeight"](arg_newVal.COM_val))

    @property
    def Width(self) -> int:
        """Gets/sets a width of the main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWidth"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Width.setter
    def Width(self, newVal:int) -> None:
        """Gets/sets a width of the main window."""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetWidth"](arg_newVal.COM_val))

    @property
    def Left(self) -> int:
        """Gets/sets a vertical coordinate of the main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLeft"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Left.setter
    def Left(self, newVal:int) -> None:
        """Gets/sets a vertical coordinate of the main window."""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetLeft"](arg_newVal.COM_val))

    @property
    def Top(self) -> int:
        """Gets/sets a horizontal coordinate of the main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetTop"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Top.setter
    def Top(self, newVal:int) -> None:
        """Gets/sets a horizontal coordinate of the main window."""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetTop"](arg_newVal.COM_val))

    @property
    def WindowState(self) -> "AgEWindowState":
        """Gets/sets the state of the main window."""
        with agmarshall.AgEnum_arg(AgEWindowState) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWindowState"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @WindowState.setter
    def WindowState(self, newVal:"AgEWindowState") -> None:
        """Gets/sets the state of the main window."""
        with agmarshall.AgEnum_arg(AgEWindowState, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetWindowState"](arg_newVal.COM_val))

    def Activate(self) -> None:
        """Activates the application's main window."""
        agcls.evaluate_hresult(self.__dict__["_Activate"]())

    @property
    def MRUList(self) -> "IAgMRUCollection":
        """Returns a collection most recently used files."""
        with agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetMRUList"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def FileOpenDialog(self, defaultExt:str, filter:str, initialDir:str) -> str:
        """Brings up a common File Open dialog and returns the file name selected by the user. If the user canceled, returns an empty file name."""
        with agmarshall.BSTR_arg(defaultExt) as arg_defaultExt, \
             agmarshall.BSTR_arg(filter) as arg_filter, \
             agmarshall.BSTR_arg(initialDir) as arg_initialDir, \
             agmarshall.BSTR_arg() as arg_pFileName:
            agcls.evaluate_hresult(self.__dict__["_FileOpenDialog"](arg_defaultExt.COM_val, arg_filter.COM_val, arg_initialDir.COM_val, byref(arg_pFileName.COM_val)))
            return arg_pFileName.python_val

    @property
    def Path(self) -> str:
        """Returns the complete path to the application, excluding the final separator and name of the application. Read-only String."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPath"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def CreateObject(self, progID:str, remoteServer:str) -> typing.Any:
        """Only works from local HTML pages and scripts"""
        with agmarshall.BSTR_arg(progID) as arg_progID, \
             agmarshall.BSTR_arg(remoteServer) as arg_remoteServer, \
             agmarshall.AgInterface_out_arg() as arg_ppObject:
            agcls.evaluate_hresult(self.__dict__["_CreateObject"](arg_progID.COM_val, arg_remoteServer.COM_val, byref(arg_ppObject.COM_val)))
            return arg_ppObject.python_val

    def FileSaveAsDialog(self, defaultExt:str, filter:str, initialDir:str) -> str:
        """Brings up a common File SaveAs dialog and returns the file name selected by the user. If the user canceled, returns an empty file name."""
        with agmarshall.BSTR_arg(defaultExt) as arg_defaultExt, \
             agmarshall.BSTR_arg(filter) as arg_filter, \
             agmarshall.BSTR_arg(initialDir) as arg_initialDir, \
             agmarshall.BSTR_arg() as arg_pFileName:
            agcls.evaluate_hresult(self.__dict__["_FileSaveAsDialog"](arg_defaultExt.COM_val, arg_filter.COM_val, arg_initialDir.COM_val, byref(arg_pFileName.COM_val)))
            return arg_pFileName.python_val

    def Quit(self) -> None:
        """Shuts down the application."""
        agcls.evaluate_hresult(self.__dict__["_Quit"]())

    def FileOpenDialogExt(self, allowMultiSelect:bool, defaultExt:str, filter:str, initialDir:str) -> "IAgUiFileOpenExt":
        """Brings up a standard File Open Dialog and returns an object representing the selected file."""
        with agmarshall.VARIANT_BOOL_arg(allowMultiSelect) as arg_allowMultiSelect, \
             agmarshall.BSTR_arg(defaultExt) as arg_defaultExt, \
             agmarshall.BSTR_arg(filter) as arg_filter, \
             agmarshall.BSTR_arg(initialDir) as arg_initialDir, \
             agmarshall.AgInterface_out_arg() as arg_ppObject:
            agcls.evaluate_hresult(self.__dict__["_FileOpenDialogExt"](arg_allowMultiSelect.COM_val, arg_defaultExt.COM_val, arg_filter.COM_val, arg_initialDir.COM_val, byref(arg_ppObject.COM_val)))
            return arg_ppObject.python_val

    @property
    def HWND(self) -> int:
        """Returns an HWND handle associated with the application main window."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetHWND"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def DirectoryPickerDialog(self, title:str, initialDir:str) -> str:
        """Brings up the Directory Picker Dialog and returns a selected directory name."""
        with agmarshall.BSTR_arg(title) as arg_title, \
             agmarshall.BSTR_arg(initialDir) as arg_initialDir, \
             agmarshall.BSTR_arg() as arg_pDirName:
            agcls.evaluate_hresult(self.__dict__["_DirectoryPickerDialog"](arg_title.COM_val, arg_initialDir.COM_val, byref(arg_pDirName.COM_val)))
            return arg_pDirName.python_val

    @property
    def MessagePendingDelay(self) -> int:
        """Gets/Sets message-pending delay for server busy dialog (in milliseconds )"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetMessagePendingDelay"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @MessagePendingDelay.setter
    def MessagePendingDelay(self, newVal:int) -> None:
        """Gets/Sets message-pending delay for server busy dialog (in milliseconds)"""
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetMessagePendingDelay"](arg_newVal.COM_val))

    @property
    def Personality2(self) -> typing.Any:
        """Returns an new instance of the root object of the STK Object Model"""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetPersonality2"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def OpenLogFile(self, logFileName:str, logFileMode:"AgEOpenLogFileMode") -> bool:
        """Specifies the current log file to be written to."""
        with agmarshall.BSTR_arg(logFileName) as arg_logFileName, \
             agmarshall.AgEnum_arg(AgEOpenLogFileMode, logFileMode) as arg_logFileMode, \
             agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_OpenLogFile"](arg_logFileName.COM_val, arg_logFileMode.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def LogMsg(self, msgType:"AgEUiLogMsgType", msg:str) -> None:
        """Logs the Message specified."""
        with agmarshall.AgEnum_arg(AgEUiLogMsgType, msgType) as arg_msgType, \
             agmarshall.BSTR_arg(msg) as arg_msg:
            agcls.evaluate_hresult(self.__dict__["_LogMsg"](arg_msgType.COM_val, arg_msg.COM_val))

    @property
    def LogFile(self) -> str:
        """Gets the current log files full path."""
        with agmarshall.BSTR_arg() as arg_pLogFilePath:
            agcls.evaluate_hresult(self.__dict__["_GetLogFile"](byref(arg_pLogFilePath.COM_val)))
            return arg_pLogFilePath.python_val

    @property
    def DisplayAlerts(self) -> bool:
        """Set to true to display certain alerts and messages. Otherwise false. The default value is True."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetDisplayAlerts"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @DisplayAlerts.setter
    def DisplayAlerts(self, displayAlerts:bool) -> None:
        """Set to true to display certain alerts and messages. Otherwise false. The default value is True."""
        with agmarshall.VARIANT_BOOL_arg(displayAlerts) as arg_displayAlerts:
            agcls.evaluate_hresult(self.__dict__["_SetDisplayAlerts"](arg_displayAlerts.COM_val))

    def CreateApplication(self) -> "IAgUiApplication":
        """Create a new instance of the application model root object."""
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_CreateApplication"](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    @property
    def ProcessID(self) -> int:
        """Gets process id for the current instance."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetProcessID"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{769EDAA1-8767-4781-BC43-D968B0D67C02}", IAgUiApplication)
agcls.AgTypeNameMap["IAgUiApplication"] = IAgUiApplication

class IAgUiApplicationPartnerAccess(object):
    """Access to the application object model for business partners."""
    _uuid = "{DFC7DB2A-FA00-47B7-95D8-0E1171705A0F}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GrantPartnerAccess"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiApplicationPartnerAccess._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiApplicationPartnerAccess from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiApplicationPartnerAccess = agcom.GUID(IAgUiApplicationPartnerAccess._uuid)
        vtable_offset_local = IAgUiApplicationPartnerAccess._vtable_offset - 1
        self.__dict__["_GrantPartnerAccess"] = IAGFUNCTYPE(pUnk, IID_IAgUiApplicationPartnerAccess, vtable_offset_local+1, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiApplicationPartnerAccess.__dict__ and type(IAgUiApplicationPartnerAccess.__dict__[attrname]) == property:
            return IAgUiApplicationPartnerAccess.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiApplicationPartnerAccess.")
    
    def GrantPartnerAccess(self, vendor:str, product:str, key:str) -> typing.Any:
        """Provide object model root for authorized business partners."""
        with agmarshall.BSTR_arg(vendor) as arg_vendor, \
             agmarshall.BSTR_arg(product) as arg_product, \
             agmarshall.BSTR_arg(key) as arg_key, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GrantPartnerAccess"](arg_vendor.COM_val, arg_product.COM_val, arg_key.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{DFC7DB2A-FA00-47B7-95D8-0E1171705A0F}", IAgUiApplicationPartnerAccess)
agcls.AgTypeNameMap["IAgUiApplicationPartnerAccess"] = IAgUiApplicationPartnerAccess

class IAgUiFileOpenExtCollection(object):
    """Multiple file open collection."""
    _uuid = "{564BF89D-F0F8-4E98-A5A4-033DB16FC659}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiFileOpenExtCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiFileOpenExtCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiFileOpenExtCollection = agcom.GUID(IAgUiFileOpenExtCollection._uuid)
        vtable_offset_local = IAgUiFileOpenExtCollection._vtable_offset - 1
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExtCollection, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExtCollection, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgUiFileOpenExtCollection, vtable_offset_local+3, agcom.LONG, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiFileOpenExtCollection.__dict__ and type(IAgUiFileOpenExtCollection.__dict__[attrname]) == property:
            return IAgUiFileOpenExtCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiFileOpenExtCollection.")
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
        return agmarshall.python_val_from_VARIANT(nextval)
    
    @property
    def Count(self) -> int:
        """Gets the total count of files in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates through the file collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def Item(self, nIndex:int) -> str:
        """Gets the file at the specified index."""
        with agmarshall.LONG_arg(nIndex) as arg_nIndex, \
             agmarshall.BSTR_arg() as arg_pBSTR:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_nIndex.COM_val, byref(arg_pBSTR.COM_val)))
            return arg_pBSTR.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{564BF89D-F0F8-4E98-A5A4-033DB16FC659}", IAgUiFileOpenExtCollection)
agcls.AgTypeNameMap["IAgUiFileOpenExtCollection"] = IAgUiFileOpenExtCollection



class AgUiApplication(IAgUiApplication, IAgUiApplicationPartnerAccess):
    """A root object of the Application Model."""
    def __init__(self, sourceObject=None):
        IAgUiApplication.__init__(self, sourceObject)
        IAgUiApplicationPartnerAccess.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiApplication._private_init(self, pUnk)
        IAgUiApplicationPartnerAccess._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiApplication._get_property(self, attrname) is not None: found_prop = IAgUiApplication._get_property(self, attrname)
        if IAgUiApplicationPartnerAccess._get_property(self, attrname) is not None: found_prop = IAgUiApplicationPartnerAccess._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiApplication.")
        
agcls.AgClassCatalog.add_catalog_entry("{7ADA6C22-FA34-4578-8BE8-65405A55EE15}", AgUiApplication)


class AgMRUCollection(IAgMRUCollection):
    """Provides information about most recently used (MRU) list."""
    def __init__(self, sourceObject=None):
        IAgMRUCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgMRUCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgMRUCollection._get_property(self, attrname) is not None: found_prop = IAgMRUCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgMRUCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{8033C4FF-4A7D-4416-9B07-6807EA9C794E}", AgMRUCollection)


class AgUiFileOpenExtCollection(IAgUiFileOpenExtCollection):
    """Multiple file open collection."""
    def __init__(self, sourceObject=None):
        IAgUiFileOpenExtCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiFileOpenExtCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiFileOpenExtCollection._get_property(self, attrname) is not None: found_prop = IAgUiFileOpenExtCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiFileOpenExtCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{A733AF99-E82E-42D8-AD9A-29BB005B3703}", AgUiFileOpenExtCollection)


class AgUiFileOpenExt(IAgUiFileOpenExt):
    """Access to file open dialog that allows multiple file specifications."""
    def __init__(self, sourceObject=None):
        IAgUiFileOpenExt.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiFileOpenExt._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiFileOpenExt._get_property(self, attrname) is not None: found_prop = IAgUiFileOpenExt._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiFileOpenExt.")
        
agcls.AgClassCatalog.add_catalog_entry("{26A2C933-DB59-434E-85FD-2D92A97AA8AD}", AgUiFileOpenExt)



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
