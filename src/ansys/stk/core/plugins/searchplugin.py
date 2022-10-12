################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = []

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

import agi.stk12.internal.comutil          as agcom
import agi.stk12.internal.coclassutil      as agcls
import agi.stk12.internal.marshall         as agmarshall
import agi.stk12.internal.dataanalysisutil as agdata
import agi.stk12.utilities.colors          as agcolor
from   agi.stk12.internal.comutil     import IUnknown, IDispatch, IPictureDisp, IAGFUNCTYPE, IEnumVARIANT
from   agi.stk12.internal.eventutil   import *
from   agi.stk12.utilities.exceptions import *


from agi.stk12.plugins.utplugin import *
from agi.stk12.plugins.hpopplugin import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgEGatorPluginErrorCodes(IntEnum):
    """Enumeration of AgGatorPlugin General Error Codes"""
    # Gator Plugin: An internal failure occurred.
    eGatorPluginInternalFailure = (((1 << 31) | (4 << 16)) | 0x101),
    # Gator Plugin: Not configured properly.
    eGatorPluginNotConfigured = (((1 << 31) | (4 << 16)) | 0x102),
    # Gator Plugin: Central Body is undefined.
    eGatorPluginCentralBodyUndefined = (((1 << 31) | (4 << 16)) | 0x103),
    # Gator Plugin: Sun Position Type SRP not supported.
    eGatorPluginSunPositionTypeSRPNotSupported = (((1 << 31) | (4 << 16)) | 0x104),
    # Gator Plugin: The Square Root of an invalid value occurred.
    eGatorPluginInvalidSqr = (((1 << 31) | (4 << 16)) | 0x105),
    # Gator Plugin: Reference Axes Unavailable.
    eGatorPluginReferenceAxesUnavailable = (((1 << 31) | (4 << 16)) | 0x106),
    # Gator Plugin: Color not valid.
    eGatorPluginInvalidColor = (((1 << 31) | (4 << 16)) | 0x107)

agcls.AgTypeNameMap["AgEGatorPluginErrorCodes"] = AgEGatorPluginErrorCodes
__all__.append("AgEGatorPluginErrorCodes")

class AgESearchPluginErrorCodes(IntEnum):
    """Enumeration of AgSearchPlugin General Error Codes."""
    # Seach Plugin: Operand Error.
    eSearchPluginErrorCodesOperandError = (((1 << 31) | (4 << 16)) | 0x108),
    # Seach Plugin: Profile Failure.
    eSearchPluginErrorCodesOperandProfileFailure = (((1 << 31) | (4 << 16)) | 0x109),
    # Search Plugin: GUI Data Failure.
    eSearchPluginErrorCodesGUIDataFailure = (((1 << 31) | (4 << 16)) | 0x110),
    # Seach Plugin: Operand Stopped.
    eSearchPluginErrorCodesOperandStopped = (((1 << 31) | (4 << 16)) | 0x111),
    # Seach Plugin: Operand Canceled.
    eSearchPluginErrorCodesOperandCanceled = (((1 << 31) | (4 << 16)) | 0x112)

agcls.AgTypeNameMap["AgESearchPluginErrorCodes"] = AgESearchPluginErrorCodes
__all__.append("AgESearchPluginErrorCodes")

class AgESearchControlTypes(IntEnum):
    """Enumeration of control types for search plugins."""
    # Real numbers (doubles)
    eSearchControlTypesReal = 0

agcls.AgTypeNameMap["AgESearchControlTypes"] = AgESearchControlTypes
__all__.append("AgESearchControlTypes")


class IAgGatorPropagatorScriptDriver(object):
    """HPOP plugin engine interface utilizing a script driver interface (Perl, VBScript, Matlab)"""
    _uuid = "{62574EAE-D805-48f1-9579-A3885B05A5F6}"
    _num_methods = 30
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetUseInitFile"] = _raise_uninitialized_error
        self.__dict__["_SetUseInitFile"] = _raise_uninitialized_error
        self.__dict__["_GetInitFile"] = _raise_uninitialized_error
        self.__dict__["_SetInitFile"] = _raise_uninitialized_error
        self.__dict__["_GetInitFileRWFlag"] = _raise_uninitialized_error
        self.__dict__["_GetUsePrePropagateFile"] = _raise_uninitialized_error
        self.__dict__["_SetUsePrePropagateFile"] = _raise_uninitialized_error
        self.__dict__["_GetPrePropagateFile"] = _raise_uninitialized_error
        self.__dict__["_SetPrePropagateFile"] = _raise_uninitialized_error
        self.__dict__["_GetPrePropagateFileRWFlag"] = _raise_uninitialized_error
        self.__dict__["_GetUsePreNextStepFile"] = _raise_uninitialized_error
        self.__dict__["_SetUsePreNextStepFile"] = _raise_uninitialized_error
        self.__dict__["_GetPreNextStepFile"] = _raise_uninitialized_error
        self.__dict__["_SetPreNextStepFile"] = _raise_uninitialized_error
        self.__dict__["_GetPreNextStepFileRWFlag"] = _raise_uninitialized_error
        self.__dict__["_GetUseEvaluateFile"] = _raise_uninitialized_error
        self.__dict__["_SetUseEvaluateFile"] = _raise_uninitialized_error
        self.__dict__["_GetEvaluateFile"] = _raise_uninitialized_error
        self.__dict__["_SetEvaluateFile"] = _raise_uninitialized_error
        self.__dict__["_GetEvaluateFileRWFlag"] = _raise_uninitialized_error
        self.__dict__["_GetUsePostPropagateFile"] = _raise_uninitialized_error
        self.__dict__["_SetUsePostPropagateFile"] = _raise_uninitialized_error
        self.__dict__["_GetPostPropagateFile"] = _raise_uninitialized_error
        self.__dict__["_SetPostPropagateFile"] = _raise_uninitialized_error
        self.__dict__["_GetPostPropagateFileRWFlag"] = _raise_uninitialized_error
        self.__dict__["_GetUseFreeFile"] = _raise_uninitialized_error
        self.__dict__["_SetUseFreeFile"] = _raise_uninitialized_error
        self.__dict__["_GetFreeFile"] = _raise_uninitialized_error
        self.__dict__["_SetFreeFile"] = _raise_uninitialized_error
        self.__dict__["_GetFreeFileRWFlag"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgGatorPropagatorScriptDriver._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgGatorPropagatorScriptDriver from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgGatorPropagatorScriptDriver = agcom.GUID(IAgGatorPropagatorScriptDriver._uuid)
        vtable_offset_local = IAgGatorPropagatorScriptDriver._vtable_offset - 1
        self.__dict__["_GetUseInitFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetUseInitFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+2, agcom.VARIANT_BOOL)
        self.__dict__["_GetInitFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_SetInitFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+4, agcom.BSTR)
        self.__dict__["_GetInitFileRWFlag"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_GetUsePrePropagateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetUsePrePropagateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+7, agcom.VARIANT_BOOL)
        self.__dict__["_GetPrePropagateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetPrePropagateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_GetPrePropagateFileRWFlag"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_GetUsePreNextStepFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+11, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetUsePreNextStepFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+12, agcom.VARIANT_BOOL)
        self.__dict__["_GetPreNextStepFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+13, POINTER(agcom.BSTR))
        self.__dict__["_SetPreNextStepFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+14, agcom.BSTR)
        self.__dict__["_GetPreNextStepFileRWFlag"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+15, POINTER(agcom.LONG))
        self.__dict__["_GetUseEvaluateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+16, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetUseEvaluateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+17, agcom.VARIANT_BOOL)
        self.__dict__["_GetEvaluateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+18, POINTER(agcom.BSTR))
        self.__dict__["_SetEvaluateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+19, agcom.BSTR)
        self.__dict__["_GetEvaluateFileRWFlag"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+20, POINTER(agcom.LONG))
        self.__dict__["_GetUsePostPropagateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+21, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetUsePostPropagateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+22, agcom.VARIANT_BOOL)
        self.__dict__["_GetPostPropagateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+23, POINTER(agcom.BSTR))
        self.__dict__["_SetPostPropagateFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+24, agcom.BSTR)
        self.__dict__["_GetPostPropagateFileRWFlag"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+25, POINTER(agcom.LONG))
        self.__dict__["_GetUseFreeFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+26, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetUseFreeFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+27, agcom.VARIANT_BOOL)
        self.__dict__["_GetFreeFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+28, POINTER(agcom.BSTR))
        self.__dict__["_SetFreeFile"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+29, agcom.BSTR)
        self.__dict__["_GetFreeFileRWFlag"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPropagatorScriptDriver, vtable_offset_local+30, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGatorPropagatorScriptDriver.__dict__ and type(IAgGatorPropagatorScriptDriver.__dict__[attrname]) == property:
            return IAgGatorPropagatorScriptDriver.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgGatorPropagatorScriptDriver.")
    
    @property
    def UseInitFile(self) -> bool:
        """Use Init File"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUseInitFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @UseInitFile.setter
    def UseInitFile(self, newVal:bool) -> None:
        """Use Init File"""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUseInitFile"](arg_newVal.COM_val))

    @property
    def InitFile(self) -> str:
        """Init File"""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetInitFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @InitFile.setter
    def InitFile(self, newVal:str) -> None:
        """Init File"""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetInitFile"](arg_newVal.COM_val))

    @property
    def InitFileRWFlag(self) -> int:
        """Init File RW Flag"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetInitFileRWFlag"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def UsePrePropagateFile(self) -> bool:
        """Use PrePropagate File"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUsePrePropagateFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @UsePrePropagateFile.setter
    def UsePrePropagateFile(self, newVal:bool) -> None:
        """Use PrePropagate File"""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUsePrePropagateFile"](arg_newVal.COM_val))

    @property
    def PrePropagateFile(self) -> str:
        """PrePropagate File"""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPrePropagateFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @PrePropagateFile.setter
    def PrePropagateFile(self, newVal:str) -> None:
        """PrePropagate File"""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetPrePropagateFile"](arg_newVal.COM_val))

    @property
    def PrePropagateFileRWFlag(self) -> int:
        """PrePropagate File RW Flag"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPrePropagateFileRWFlag"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def UsePreNextStepFile(self) -> bool:
        """Use PreNextStep File"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUsePreNextStepFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @UsePreNextStepFile.setter
    def UsePreNextStepFile(self, newVal:bool) -> None:
        """Use PreNextStep File"""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUsePreNextStepFile"](arg_newVal.COM_val))

    @property
    def PreNextStepFile(self) -> str:
        """PreNextStep File"""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPreNextStepFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @PreNextStepFile.setter
    def PreNextStepFile(self, newVal:str) -> None:
        """PreNextStep File"""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetPreNextStepFile"](arg_newVal.COM_val))

    @property
    def PreNextStepFileRWFlag(self) -> int:
        """PreNextStep File RW Flag"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPreNextStepFileRWFlag"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def UseEvaluateFile(self) -> bool:
        """Use Evaluate File"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUseEvaluateFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @UseEvaluateFile.setter
    def UseEvaluateFile(self, newVal:bool) -> None:
        """Use Evaluate File"""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUseEvaluateFile"](arg_newVal.COM_val))

    @property
    def EvaluateFile(self) -> str:
        """Evaluate File"""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetEvaluateFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @EvaluateFile.setter
    def EvaluateFile(self, newVal:str) -> None:
        """Evaluate File"""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetEvaluateFile"](arg_newVal.COM_val))

    @property
    def EvaluateFileRWFlag(self) -> int:
        """Evaluate File RW Flag"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetEvaluateFileRWFlag"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def UsePostPropagateFile(self) -> bool:
        """Use PostPropagate File"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUsePostPropagateFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @UsePostPropagateFile.setter
    def UsePostPropagateFile(self, newVal:bool) -> None:
        """Use PostPropagate File"""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUsePostPropagateFile"](arg_newVal.COM_val))

    @property
    def PostPropagateFile(self) -> str:
        """PostPropagate File"""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPostPropagateFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @PostPropagateFile.setter
    def PostPropagateFile(self, newVal:str) -> None:
        """PostPropagate File"""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetPostPropagateFile"](arg_newVal.COM_val))

    @property
    def PostPropagateFileRWFlag(self) -> int:
        """PostPropagate File RW Flag"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetPostPropagateFileRWFlag"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def UseFreeFile(self) -> bool:
        """Use Free File"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUseFreeFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @UseFreeFile.setter
    def UseFreeFile(self, newVal:bool) -> None:
        """Use Free File"""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUseFreeFile"](arg_newVal.COM_val))

    @property
    def FreeFile(self) -> str:
        """Free File"""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFreeFile"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FreeFile.setter
    def FreeFile(self, newVal:str) -> None:
        """Free File"""
        with agmarshall.BSTR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFreeFile"](arg_newVal.COM_val))

    @property
    def FreeFileRWFlag(self) -> int:
        """Free File RW Flag"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFreeFileRWFlag"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{62574EAE-D805-48f1-9579-A3885B05A5F6}", IAgGatorPropagatorScriptDriver)
agcls.AgTypeNameMap["IAgGatorPropagatorScriptDriver"] = IAgGatorPropagatorScriptDriver
__all__.append("IAgGatorPropagatorScriptDriver")

class IAgSearchControl(object):
    """Plugin search algorithm control"""
    _uuid = "{A05CFD20-F2E0-48d7-BD4C-D3DF88FF852A}"
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetObjectName"] = _raise_uninitialized_error
        self.__dict__["_SetObjectName"] = _raise_uninitialized_error
        self.__dict__["_GetControlName"] = _raise_uninitialized_error
        self.__dict__["_SetControlName"] = _raise_uninitialized_error
        self.__dict__["_GetControlType"] = _raise_uninitialized_error
        self.__dict__["_SetControlType"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSearchControl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSearchControl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSearchControl = agcom.GUID(IAgSearchControl._uuid)
        vtable_offset_local = IAgSearchControl._vtable_offset - 1
        self.__dict__["_GetObjectName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControl, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_SetObjectName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControl, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_GetControlName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControl, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_SetControlName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControl, vtable_offset_local+4, agcom.BSTR)
        self.__dict__["_GetControlType"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControl, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_SetControlType"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControl, vtable_offset_local+6, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSearchControl.__dict__ and type(IAgSearchControl.__dict__[attrname]) == property:
            return IAgSearchControl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSearchControl.")
    
    @property
    def ObjectName(self) -> str:
        """Name of the object associated with the control.  Set by STK."""
        with agmarshall.BSTR_arg() as arg_pObjectName:
            agcls.evaluate_hresult(self.__dict__["_GetObjectName"](byref(arg_pObjectName.COM_val)))
            return arg_pObjectName.python_val

    @ObjectName.setter
    def ObjectName(self, objectName:str) -> None:
        """Name of the object associated with the control.  Set by STK."""
        with agmarshall.BSTR_arg(objectName) as arg_objectName:
            agcls.evaluate_hresult(self.__dict__["_SetObjectName"](arg_objectName.COM_val))

    @property
    def ControlName(self) -> str:
        """Name of the control.  Set by STK."""
        with agmarshall.BSTR_arg() as arg_pControlName:
            agcls.evaluate_hresult(self.__dict__["_GetControlName"](byref(arg_pControlName.COM_val)))
            return arg_pControlName.python_val

    @ControlName.setter
    def ControlName(self, controlName:str) -> None:
        """Name of the control.  Set by STK."""
        with agmarshall.BSTR_arg(controlName) as arg_controlName:
            agcls.evaluate_hresult(self.__dict__["_SetControlName"](arg_controlName.COM_val))

    @property
    def ControlType(self) -> "AgESearchControlTypes":
        """Type of the control.  Set by STK."""
        with agmarshall.AgEnum_arg(AgESearchControlTypes) as arg_pType:
            agcls.evaluate_hresult(self.__dict__["_GetControlType"](byref(arg_pType.COM_val)))
            return arg_pType.python_val

    @ControlType.setter
    def ControlType(self, type:"AgESearchControlTypes") -> None:
        """Type of the control.  Set by STK."""
        with agmarshall.AgEnum_arg(AgESearchControlTypes, type) as arg_type:
            agcls.evaluate_hresult(self.__dict__["_SetControlType"](arg_type.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{A05CFD20-F2E0-48d7-BD4C-D3DF88FF852A}", IAgSearchControl)
agcls.AgTypeNameMap["IAgSearchControl"] = IAgSearchControl
__all__.append("IAgSearchControl")

class IAgSearchControlReal(IAgSearchControl):
    """Plugin search algorithm control, real number"""
    _uuid = "{56C81403-0567-48d9-A8CA-76D722AEE95F}"
    _num_methods = 8
    _vtable_offset = IAgSearchControl._vtable_offset + IAgSearchControl._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCurrentValue"] = _raise_uninitialized_error
        self.__dict__["_SetCurrentValue"] = _raise_uninitialized_error
        self.__dict__["_GetInitialValue"] = _raise_uninitialized_error
        self.__dict__["_SetInitialValue"] = _raise_uninitialized_error
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        self.__dict__["_SetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetInternalUnit"] = _raise_uninitialized_error
        self.__dict__["_SetInternalUnit"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSearchControlReal._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSearchControlReal from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSearchControl._private_init(self, pUnk)
        IID_IAgSearchControlReal = agcom.GUID(IAgSearchControlReal._uuid)
        vtable_offset_local = IAgSearchControlReal._vtable_offset - 1
        self.__dict__["_GetCurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlReal, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_SetCurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlReal, vtable_offset_local+2, agcom.DOUBLE)
        self.__dict__["_GetInitialValue"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlReal, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_SetInitialValue"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlReal, vtable_offset_local+4, agcom.DOUBLE)
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlReal, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_SetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlReal, vtable_offset_local+6, agcom.BSTR)
        self.__dict__["_GetInternalUnit"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlReal, vtable_offset_local+7, POINTER(agcom.BSTR))
        self.__dict__["_SetInternalUnit"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlReal, vtable_offset_local+8, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSearchControlReal.__dict__ and type(IAgSearchControlReal.__dict__[attrname]) == property:
            return IAgSearchControlReal.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgSearchControl.__setattr__(self, attrname, value)
    
    @property
    def CurrentValue(self) -> float:
        """The current value of the control.  Set by the plugin search algorithm."""
        with agmarshall.DOUBLE_arg() as arg_pCurrentValue:
            agcls.evaluate_hresult(self.__dict__["_GetCurrentValue"](byref(arg_pCurrentValue.COM_val)))
            return arg_pCurrentValue.python_val

    @CurrentValue.setter
    def CurrentValue(self, currentValue:float) -> None:
        """The current value of the control.  Set by the plugin search algorithm."""
        with agmarshall.DOUBLE_arg(currentValue) as arg_currentValue:
            agcls.evaluate_hresult(self.__dict__["_SetCurrentValue"](arg_currentValue.COM_val))

    @property
    def InitialValue(self) -> float:
        """The value of the control at the start of the plugin search run.  Set by STK."""
        with agmarshall.DOUBLE_arg() as arg_pInitialValue:
            agcls.evaluate_hresult(self.__dict__["_GetInitialValue"](byref(arg_pInitialValue.COM_val)))
            return arg_pInitialValue.python_val

    @InitialValue.setter
    def InitialValue(self, initialValue:float) -> None:
        """The value of the control at the start of the plugin search run.  Set by STK."""
        with agmarshall.DOUBLE_arg(initialValue) as arg_initialValue:
            agcls.evaluate_hresult(self.__dict__["_SetInitialValue"](arg_initialValue.COM_val))

    @property
    def Dimension(self) -> str:
        """The dimension of the control.  Set by STK."""
        with agmarshall.BSTR_arg() as arg_pDimension:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_pDimension.COM_val)))
            return arg_pDimension.python_val

    @Dimension.setter
    def Dimension(self, dimension:str) -> None:
        """The dimension of the control.  Set by STK."""
        with agmarshall.BSTR_arg(dimension) as arg_dimension:
            agcls.evaluate_hresult(self.__dict__["_SetDimension"](arg_dimension.COM_val))

    @property
    def InternalUnit(self) -> str:
        """The internal unit of the control.  Set by STK."""
        with agmarshall.BSTR_arg() as arg_pInternalUnit:
            agcls.evaluate_hresult(self.__dict__["_GetInternalUnit"](byref(arg_pInternalUnit.COM_val)))
            return arg_pInternalUnit.python_val

    @InternalUnit.setter
    def InternalUnit(self, internalUnit:str) -> None:
        """The internal unit of the control.  Set by STK."""
        with agmarshall.BSTR_arg(internalUnit) as arg_internalUnit:
            agcls.evaluate_hresult(self.__dict__["_SetInternalUnit"](arg_internalUnit.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{56C81403-0567-48d9-A8CA-76D722AEE95F}", IAgSearchControlReal)
agcls.AgTypeNameMap["IAgSearchControlReal"] = IAgSearchControlReal
__all__.append("IAgSearchControlReal")

class IAgSearchControlCollection(object):
    """Collection for plugin search algorithm controls"""
    _uuid = "{67A00871-9B5A-42da-B63D-49674C35ED39}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSearchControlCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSearchControlCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSearchControlCollection = agcom.GUID(IAgSearchControlCollection._uuid)
        vtable_offset_local = IAgSearchControlCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlCollection, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlCollection, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgSearchControlCollection, vtable_offset_local+3, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSearchControlCollection.__dict__ and type(IAgSearchControlCollection.__dict__[attrname]) == property:
            return IAgSearchControlCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSearchControlCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgSearchControl":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, index:int) -> "IAgSearchControl":
        """Given an index, returns the element in the collection."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_pSearchControl:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pSearchControl.COM_val)))
            return arg_pSearchControl.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an enumerator for the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnumerator:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppEnumerator.COM_val)))
            return arg_ppEnumerator.python_val

    @property
    def Count(self) -> int:
        """Number of items in the collection"""
        with agmarshall.LONG_arg() as arg_plCount:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_plCount.COM_val)))
            return arg_plCount.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{67A00871-9B5A-42da-B63D-49674C35ED39}", IAgSearchControlCollection)
agcls.AgTypeNameMap["IAgSearchControlCollection"] = IAgSearchControlCollection
__all__.append("IAgSearchControlCollection")

class IAgSearchResult(object):
    """Plugin search algorithm result"""
    _uuid = "{1794AA9C-1762-4e2d-9DDE-C5E0C95F825D}"
    _num_methods = 12
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetObjectName"] = _raise_uninitialized_error
        self.__dict__["_SetObjectName"] = _raise_uninitialized_error
        self.__dict__["_GetResultName"] = _raise_uninitialized_error
        self.__dict__["_SetResultName"] = _raise_uninitialized_error
        self.__dict__["_GetCurrentValue"] = _raise_uninitialized_error
        self.__dict__["_SetCurrentValue"] = _raise_uninitialized_error
        self.__dict__["_GetIsValid"] = _raise_uninitialized_error
        self.__dict__["_SetIsValid"] = _raise_uninitialized_error
        self.__dict__["_GetDimension"] = _raise_uninitialized_error
        self.__dict__["_SetDimension"] = _raise_uninitialized_error
        self.__dict__["_GetInternalUnit"] = _raise_uninitialized_error
        self.__dict__["_SetInternalUnit"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSearchResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSearchResult from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSearchResult = agcom.GUID(IAgSearchResult._uuid)
        vtable_offset_local = IAgSearchResult._vtable_offset - 1
        self.__dict__["_GetObjectName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_SetObjectName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_GetResultName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_SetResultName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+4, agcom.BSTR)
        self.__dict__["_GetCurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+5, POINTER(agcom.DOUBLE))
        self.__dict__["_SetCurrentValue"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+6, agcom.DOUBLE)
        self.__dict__["_GetIsValid"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+7, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetIsValid"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+8, agcom.VARIANT_BOOL)
        self.__dict__["_GetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+9, POINTER(agcom.BSTR))
        self.__dict__["_SetDimension"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+10, agcom.BSTR)
        self.__dict__["_GetInternalUnit"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+11, POINTER(agcom.BSTR))
        self.__dict__["_SetInternalUnit"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResult, vtable_offset_local+12, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSearchResult.__dict__ and type(IAgSearchResult.__dict__[attrname]) == property:
            return IAgSearchResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSearchResult.")
    
    @property
    def ObjectName(self) -> str:
        """Name of the object associated with the result.  Set by STK."""
        with agmarshall.BSTR_arg() as arg_pObjectName:
            agcls.evaluate_hresult(self.__dict__["_GetObjectName"](byref(arg_pObjectName.COM_val)))
            return arg_pObjectName.python_val

    @ObjectName.setter
    def ObjectName(self, objectName:str) -> None:
        """Name of the object associated with the result.  Set by STK."""
        with agmarshall.BSTR_arg(objectName) as arg_objectName:
            agcls.evaluate_hresult(self.__dict__["_SetObjectName"](arg_objectName.COM_val))

    @property
    def ResultName(self) -> str:
        """Name of the result.  Set by STK."""
        with agmarshall.BSTR_arg() as arg_pResultName:
            agcls.evaluate_hresult(self.__dict__["_GetResultName"](byref(arg_pResultName.COM_val)))
            return arg_pResultName.python_val

    @ResultName.setter
    def ResultName(self, resultName:str) -> None:
        """Name of the result.  Set by STK."""
        with agmarshall.BSTR_arg(resultName) as arg_resultName:
            agcls.evaluate_hresult(self.__dict__["_SetResultName"](arg_resultName.COM_val))

    @property
    def CurrentValue(self) -> float:
        """The current value of the result.  Set by STK."""
        with agmarshall.DOUBLE_arg() as arg_pCurrentValue:
            agcls.evaluate_hresult(self.__dict__["_GetCurrentValue"](byref(arg_pCurrentValue.COM_val)))
            return arg_pCurrentValue.python_val

    @CurrentValue.setter
    def CurrentValue(self, currentValue:float) -> None:
        """The current value of the result.  Set by STK."""
        with agmarshall.DOUBLE_arg(currentValue) as arg_currentValue:
            agcls.evaluate_hresult(self.__dict__["_SetCurrentValue"](arg_currentValue.COM_val))

    @property
    def IsValid(self) -> bool:
        """Whether the current value of the result is valid.  Set by STK."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__["_GetIsValid"](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val

    @IsValid.setter
    def IsValid(self, isValid:bool) -> None:
        """Whether the current value of the result is valid.  Set by STK."""
        with agmarshall.VARIANT_BOOL_arg(isValid) as arg_isValid:
            agcls.evaluate_hresult(self.__dict__["_SetIsValid"](arg_isValid.COM_val))

    @property
    def Dimension(self) -> str:
        """The dimension of the result.  Set by STK."""
        with agmarshall.BSTR_arg() as arg_pDimension:
            agcls.evaluate_hresult(self.__dict__["_GetDimension"](byref(arg_pDimension.COM_val)))
            return arg_pDimension.python_val

    @Dimension.setter
    def Dimension(self, dimension:str) -> None:
        """The dimension of the result.  Set by STK."""
        with agmarshall.BSTR_arg(dimension) as arg_dimension:
            agcls.evaluate_hresult(self.__dict__["_SetDimension"](arg_dimension.COM_val))

    @property
    def InternalUnit(self) -> str:
        """The internal unit of the result.  Set by STK."""
        with agmarshall.BSTR_arg() as arg_pInternalUnit:
            agcls.evaluate_hresult(self.__dict__["_GetInternalUnit"](byref(arg_pInternalUnit.COM_val)))
            return arg_pInternalUnit.python_val

    @InternalUnit.setter
    def InternalUnit(self, internalUnit:str) -> None:
        """The internal unit of the result.  Set by STK."""
        with agmarshall.BSTR_arg(internalUnit) as arg_internalUnit:
            agcls.evaluate_hresult(self.__dict__["_SetInternalUnit"](arg_internalUnit.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{1794AA9C-1762-4e2d-9DDE-C5E0C95F825D}", IAgSearchResult)
agcls.AgTypeNameMap["IAgSearchResult"] = IAgSearchResult
__all__.append("IAgSearchResult")

class IAgSearchResultCollection(object):
    """Collection for plugin search algorithm results"""
    _uuid = "{EFF32FA4-F98E-4e7f-891B-523B8133AAA3}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSearchResultCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSearchResultCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSearchResultCollection = agcom.GUID(IAgSearchResultCollection._uuid)
        vtable_offset_local = IAgSearchResultCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResultCollection, vtable_offset_local+1, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResultCollection, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgSearchResultCollection, vtable_offset_local+3, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSearchResultCollection.__dict__ and type(IAgSearchResultCollection.__dict__[attrname]) == property:
            return IAgSearchResultCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSearchResultCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgSearchResult":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, index:int) -> "IAgSearchResult":
        """Given an index, returns the element in the collection."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_pSearchResult:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pSearchResult.COM_val)))
            return arg_pSearchResult.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an enumerator for the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnumerator:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppEnumerator.COM_val)))
            return arg_ppEnumerator.python_val

    @property
    def Count(self) -> int:
        """Number of items in the collection"""
        with agmarshall.LONG_arg() as arg_plCount:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_plCount.COM_val)))
            return arg_plCount.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{EFF32FA4-F98E-4e7f-891B-523B8133AAA3}", IAgSearchResultCollection)
agcls.AgTypeNameMap["IAgSearchResultCollection"] = IAgSearchResultCollection
__all__.append("IAgSearchResultCollection")

class IAgPluginSearchStatusGrid(object):
    """Astrogator plugin class for plugin search algorithm's status grid."""
    _uuid = "{36B1DC5D-0BA4-42ac-8225-DE9F6E6C6AEB}"
    _num_methods = 11
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_CreateGrid"] = _raise_uninitialized_error
        self.__dict__["_SetCellString"] = _raise_uninitialized_error
        self.__dict__["_SetCellValue"] = _raise_uninitialized_error
        self.__dict__["_SetStatus"] = _raise_uninitialized_error
        self.__dict__["_Refresh"] = _raise_uninitialized_error
        self.__dict__["_SetColumnToTruncateLeft"] = _raise_uninitialized_error
        self.__dict__["_SetHeaderCellString"] = _raise_uninitialized_error
        self.__dict__["_SetCellControlValue"] = _raise_uninitialized_error
        self.__dict__["_SetCellResultValue"] = _raise_uninitialized_error
        self.__dict__["_SetCellControlDeltaValue"] = _raise_uninitialized_error
        self.__dict__["_SetCellResultDeltaValue"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgPluginSearchStatusGrid._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgPluginSearchStatusGrid from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgPluginSearchStatusGrid = agcom.GUID(IAgPluginSearchStatusGrid._uuid)
        vtable_offset_local = IAgPluginSearchStatusGrid._vtable_offset - 1
        self.__dict__["_CreateGrid"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+1, agcom.INT, agcom.INT)
        self.__dict__["_SetCellString"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+2, agcom.INT, agcom.INT, agcom.BSTR)
        self.__dict__["_SetCellValue"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+3, agcom.INT, agcom.INT, agcom.DOUBLE, agcom.BSTR, agcom.INT)
        self.__dict__["_SetStatus"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+4, agcom.BSTR)
        self.__dict__["_Refresh"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+5, )
        self.__dict__["_SetColumnToTruncateLeft"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+6, agcom.INT)
        self.__dict__["_SetHeaderCellString"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+7, agcom.INT, agcom.INT, agcom.BSTR)
        self.__dict__["_SetCellControlValue"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+8, agcom.INT, agcom.INT, agcom.INT, agcom.DOUBLE, agcom.INT)
        self.__dict__["_SetCellResultValue"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+9, agcom.INT, agcom.INT, agcom.INT, agcom.DOUBLE, agcom.INT)
        self.__dict__["_SetCellControlDeltaValue"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+10, agcom.INT, agcom.INT, agcom.INT, agcom.DOUBLE, agcom.INT)
        self.__dict__["_SetCellResultDeltaValue"] = IAGFUNCTYPE(pUnk, IID_IAgPluginSearchStatusGrid, vtable_offset_local+11, agcom.INT, agcom.INT, agcom.INT, agcom.DOUBLE, agcom.INT)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgPluginSearchStatusGrid.__dict__ and type(IAgPluginSearchStatusGrid.__dict__[attrname]) == property:
            return IAgPluginSearchStatusGrid.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgPluginSearchStatusGrid.")
    
    def CreateGrid(self, numRows:int, numCols:int) -> None:
        """Creates the grid."""
        with agmarshall.INT_arg(numRows) as arg_numRows, \
             agmarshall.INT_arg(numCols) as arg_numCols:
            agcls.evaluate_hresult(self.__dict__["_CreateGrid"](arg_numRows.COM_val, arg_numCols.COM_val))

    def SetCellString(self, row:int, col:int, text:str) -> None:
        """Sets a string in a cell."""
        with agmarshall.INT_arg(row) as arg_row, \
             agmarshall.INT_arg(col) as arg_col, \
             agmarshall.BSTR_arg(text) as arg_text:
            agcls.evaluate_hresult(self.__dict__["_SetCellString"](arg_row.COM_val, arg_col.COM_val, arg_text.COM_val))

    def SetCellValue(self, row:int, col:int, value:float, dimension:str, numDigits:int) -> None:
        """Sets a number in a cell. Uses scenario units."""
        with agmarshall.INT_arg(row) as arg_row, \
             agmarshall.INT_arg(col) as arg_col, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.INT_arg(numDigits) as arg_numDigits:
            agcls.evaluate_hresult(self.__dict__["_SetCellValue"](arg_row.COM_val, arg_col.COM_val, arg_value.COM_val, arg_dimension.COM_val, arg_numDigits.COM_val))

    def SetStatus(self, value:str) -> None:
        """Sets the status in the title bar."""
        with agmarshall.BSTR_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_SetStatus"](arg_value.COM_val))

    def Refresh(self) -> None:
        """Refreshes the grid."""
        agcls.evaluate_hresult(self.__dict__["_Refresh"]())

    def SetColumnToTruncateLeft(self, col:int) -> None:
        """Sets a column to truncate left."""
        with agmarshall.INT_arg(col) as arg_col:
            agcls.evaluate_hresult(self.__dict__["_SetColumnToTruncateLeft"](arg_col.COM_val))

    def SetHeaderCellString(self, row:int, col:int, text:str) -> None:
        """Sets a bold string in a cell."""
        with agmarshall.INT_arg(row) as arg_row, \
             agmarshall.INT_arg(col) as arg_col, \
             agmarshall.BSTR_arg(text) as arg_text:
            agcls.evaluate_hresult(self.__dict__["_SetHeaderCellString"](arg_row.COM_val, arg_col.COM_val, arg_text.COM_val))

    def SetCellControlValue(self, row:int, col:int, controlIndex:int, value:float, numDigits:int) -> None:
        """Sets a number in a cell in the units of a control value."""
        with agmarshall.INT_arg(row) as arg_row, \
             agmarshall.INT_arg(col) as arg_col, \
             agmarshall.INT_arg(controlIndex) as arg_controlIndex, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.INT_arg(numDigits) as arg_numDigits:
            agcls.evaluate_hresult(self.__dict__["_SetCellControlValue"](arg_row.COM_val, arg_col.COM_val, arg_controlIndex.COM_val, arg_value.COM_val, arg_numDigits.COM_val))

    def SetCellResultValue(self, row:int, col:int, resultIndex:int, value:float, numDigits:int) -> None:
        """Sets a number in a cell in the units of a result value."""
        with agmarshall.INT_arg(row) as arg_row, \
             agmarshall.INT_arg(col) as arg_col, \
             agmarshall.INT_arg(resultIndex) as arg_resultIndex, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.INT_arg(numDigits) as arg_numDigits:
            agcls.evaluate_hresult(self.__dict__["_SetCellResultValue"](arg_row.COM_val, arg_col.COM_val, arg_resultIndex.COM_val, arg_value.COM_val, arg_numDigits.COM_val))

    def SetCellControlDeltaValue(self, row:int, col:int, controlIndex:int, value:float, numDigits:int) -> None:
        """Sets a number in a cell in the delta units of a control value."""
        with agmarshall.INT_arg(row) as arg_row, \
             agmarshall.INT_arg(col) as arg_col, \
             agmarshall.INT_arg(controlIndex) as arg_controlIndex, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.INT_arg(numDigits) as arg_numDigits:
            agcls.evaluate_hresult(self.__dict__["_SetCellControlDeltaValue"](arg_row.COM_val, arg_col.COM_val, arg_controlIndex.COM_val, arg_value.COM_val, arg_numDigits.COM_val))

    def SetCellResultDeltaValue(self, row:int, col:int, resultIndex:int, value:float, numDigits:int) -> None:
        """Sets a number in a cell in the delta units of a result value."""
        with agmarshall.INT_arg(row) as arg_row, \
             agmarshall.INT_arg(col) as arg_col, \
             agmarshall.INT_arg(resultIndex) as arg_resultIndex, \
             agmarshall.DOUBLE_arg(value) as arg_value, \
             agmarshall.INT_arg(numDigits) as arg_numDigits:
            agcls.evaluate_hresult(self.__dict__["_SetCellResultDeltaValue"](arg_row.COM_val, arg_col.COM_val, arg_resultIndex.COM_val, arg_value.COM_val, arg_numDigits.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{36B1DC5D-0BA4-42ac-8225-DE9F6E6C6AEB}", IAgPluginSearchStatusGrid)
agcls.AgTypeNameMap["IAgPluginSearchStatusGrid"] = IAgPluginSearchStatusGrid
__all__.append("IAgPluginSearchStatusGrid")

class IAgSearchPluginOperand(object):
    """Astrogator plugin class for plugin search algorithm's operand."""
    _uuid = "{45D6651F-FF93-48cc-ABE9-78FD08C4CEBB}"
    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Trace"] = _raise_uninitialized_error
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        self.__dict__["_GetControls"] = _raise_uninitialized_error
        self.__dict__["_GetResults"] = _raise_uninitialized_error
        self.__dict__["_GetStatusGrid"] = _raise_uninitialized_error
        self.__dict__["_Evaluate2"] = _raise_uninitialized_error
        self.__dict__["_GetLogFile"] = _raise_uninitialized_error
        self.__dict__["_GetProfileName"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSearchPluginOperand._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSearchPluginOperand from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSearchPluginOperand = agcom.GUID(IAgSearchPluginOperand._uuid)
        vtable_offset_local = IAgSearchPluginOperand._vtable_offset - 1
        self.__dict__["_Trace"] = IAGFUNCTYPE(pUnk, IID_IAgSearchPluginOperand, vtable_offset_local+1, agcom.LONG)
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgSearchPluginOperand, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetControls"] = IAGFUNCTYPE(pUnk, IID_IAgSearchPluginOperand, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_GetResults"] = IAGFUNCTYPE(pUnk, IID_IAgSearchPluginOperand, vtable_offset_local+4, POINTER(agcom.PVOID))
        self.__dict__["_GetStatusGrid"] = IAGFUNCTYPE(pUnk, IID_IAgSearchPluginOperand, vtable_offset_local+5, POINTER(agcom.PVOID))
        self.__dict__["_Evaluate2"] = IAGFUNCTYPE(pUnk, IID_IAgSearchPluginOperand, vtable_offset_local+6, agcom.VARIANT_BOOL, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetLogFile"] = IAGFUNCTYPE(pUnk, IID_IAgSearchPluginOperand, vtable_offset_local+7, POINTER(agcom.BSTR))
        self.__dict__["_GetProfileName"] = IAGFUNCTYPE(pUnk, IID_IAgSearchPluginOperand, vtable_offset_local+8, POINTER(agcom.BSTR))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSearchPluginOperand.__dict__ and type(IAgSearchPluginOperand.__dict__[attrname]) == property:
            return IAgSearchPluginOperand.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSearchPluginOperand.")
    
    def Trace(self, numCalls:int) -> None:
        """Set this interface to trace the next numCalls by outputting a message to the message viewer."""
        with agmarshall.LONG_arg(numCalls) as arg_numCalls:
            agcls.evaluate_hresult(self.__dict__["_Trace"](arg_numCalls.COM_val))

    def Evaluate(self) -> bool:
        """Evaluates the operand of the search.  Treated as a perturbation so graphs are not updated."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pReturn:
            agcls.evaluate_hresult(self.__dict__["_Evaluate"](byref(arg_pReturn.COM_val)))
            return arg_pReturn.python_val

    @property
    def Controls(self) -> "IAgSearchControlCollection":
        """Collection of controls."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetControls"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Results(self) -> "IAgSearchResultCollection":
        """Collection of results."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetResults"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def StatusGrid(self) -> "IAgPluginSearchStatusGrid":
        """Status Grid."""
        with agmarshall.AgInterface_out_arg() as arg_pGrid:
            agcls.evaluate_hresult(self.__dict__["_GetStatusGrid"](byref(arg_pGrid.COM_val)))
            return arg_pGrid.python_val

    def Evaluate2(self, isIteration:bool) -> bool:
        """Evaluates the operand of the search.  Graphs are updated if IsIteration is true."""
        with agmarshall.VARIANT_BOOL_arg(isIteration) as arg_isIteration, \
             agmarshall.VARIANT_BOOL_arg() as arg_pReturn:
            agcls.evaluate_hresult(self.__dict__["_Evaluate2"](arg_isIteration.COM_val, byref(arg_pReturn.COM_val)))
            return arg_pReturn.python_val

    @property
    def LogFile(self) -> str:
        """Log file plugin can use."""
        with agmarshall.BSTR_arg() as arg_pbstrFileName:
            agcls.evaluate_hresult(self.__dict__["_GetLogFile"](byref(arg_pbstrFileName.COM_val)))
            return arg_pbstrFileName.python_val

    @property
    def ProfileName(self) -> str:
        """Name of this search profile."""
        with agmarshall.BSTR_arg() as arg_pbstrProfileName:
            agcls.evaluate_hresult(self.__dict__["_GetProfileName"](byref(arg_pbstrProfileName.COM_val)))
            return arg_pbstrProfileName.python_val


agcls.AgClassCatalog.add_catalog_entry("{45D6651F-FF93-48cc-ABE9-78FD08C4CEBB}", IAgSearchPluginOperand)
agcls.AgTypeNameMap["IAgSearchPluginOperand"] = IAgSearchPluginOperand
__all__.append("IAgSearchPluginOperand")


class IAgPluginSearch(object):
    """
    Plugin search algorithm interface. A method returning false indicates an error.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Name(self) -> str:
        """Triggered to set the name of the plugin used in messages."""
        raise STKPluginMethodNotImplementedError("Name was not implemented.")

    def GetControlsProgID(self, type:"AgESearchControlTypes") -> str:
        """Gets the progid of the controls of the specified type for this algorithm.  If a certain control type isn't supported, return an empty string."""
        raise STKPluginMethodNotImplementedError("GetControlsProgID was not implemented.")

    def GetResultsProgID(self) -> str:
        """Gets the progid of the results for this algorithm."""
        raise STKPluginMethodNotImplementedError("GetResultsProgID was not implemented.")

    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered when the plugin is initialized to allow for any additional needed initialization. Must return true to turn on use of plugin."""
        raise STKPluginMethodNotImplementedError("Init was not implemented.")

    def Run(self, searchOperand:"IAgSearchPluginOperand", testing:bool) -> bool:
        """Triggered when the plugin is run."""
        raise STKPluginMethodNotImplementedError("Run was not implemented.")

    def Free(self) -> None:
        """Triggered just before the plugin is freed from use to allow for any additional cleanup."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

__all__.append("IAgPluginSearch")



class AgGatorPropagatorScriptDriver(IAgGatorPropagatorScriptDriver, IAgAsHpopPlugin, IAgUtPluginConfig):
    """Astrogator plugin class to use old script plug-ins as HPOP COM plugins"""
    def __init__(self, sourceObject=None):
        IAgGatorPropagatorScriptDriver.__init__(self, sourceObject)
        IAgAsHpopPlugin.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgGatorPropagatorScriptDriver._private_init(self, pUnk)
        IAgAsHpopPlugin._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgGatorPropagatorScriptDriver._get_property(self, attrname) is not None: found_prop = IAgGatorPropagatorScriptDriver._get_property(self, attrname)
        if IAgAsHpopPlugin._get_property(self, attrname) is not None: found_prop = IAgAsHpopPlugin._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgGatorPropagatorScriptDriver.")
        
agcls.AgClassCatalog.add_catalog_entry("{D843A31B-CDB0-4437-9DE6-59E6AB21D0CC}", AgGatorPropagatorScriptDriver)
__all__.append("AgGatorPropagatorScriptDriver")


class AgPluginSearchPython(IAgPluginSearch, IAgUtPluginConfig):
    """The implementation of IAgPluginSearch for Python."""
    def __init__(self, sourceObject=None):
        IAgPluginSearch.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPluginSearch._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgPluginSearch._get_property(self, attrname) is not None: found_prop = IAgPluginSearch._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgPluginSearchPython.")
        
agcls.AgClassCatalog.add_catalog_entry("{2061AEB3-68DD-4FA0-A4AE-E96E30E3CDEC}", AgPluginSearchPython)
__all__.append("AgPluginSearchPython")


class AgSearchControlRealPython(IAgSearchControlReal, IAgUtPluginConfig):
    """The implementation of IAgSearchControlReal for Python."""
    def __init__(self, sourceObject=None):
        IAgSearchControlReal.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSearchControlReal._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSearchControlReal._get_property(self, attrname) is not None: found_prop = IAgSearchControlReal._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgSearchControlRealPython.")
        
agcls.AgClassCatalog.add_catalog_entry("{25965585-6EC6-4DE4-8E90-54CA7EC45F7D}", AgSearchControlRealPython)
__all__.append("AgSearchControlRealPython")


class AgSearchResultPython(IAgSearchResult, IAgUtPluginConfig):
    """The implementation of IAgSearchResult for Python."""
    def __init__(self, sourceObject=None):
        IAgSearchResult.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSearchResult._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSearchResult._get_property(self, attrname) is not None: found_prop = IAgSearchResult._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgSearchResultPython.")
        
agcls.AgClassCatalog.add_catalog_entry("{47E1488F-EF1B-4DF5-89D2-435169D8176A}", AgSearchResultPython)
__all__.append("AgSearchResultPython")



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
