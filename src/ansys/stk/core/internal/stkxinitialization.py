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

from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal  import dataanalysisutil as agdata
from ..utilities import colors           as agcolor
from ..internal.comutil     import IUnknown, IDispatch, IPictureDisp, IAGFUNCTYPE, IEnumVARIANT
from ..internal.eventutil   import *
from ..utilities.exceptions import *



def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class IAgSTKXInitialize(object):
    """STK X Advanced Initialization Options."""
    _uuid = "{EDC9E451-09B3-4D8B-9EC5-B75C6D95A52D}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_InitializeActivationContext"] = _raise_uninitialized_error
        self.__dict__["_InitializeData"] = _raise_uninitialized_error
        self.__dict__["_InitializeDataEx"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSTKXInitialize._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSTKXInitialize from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSTKXInitialize = agcom.GUID(IAgSTKXInitialize._uuid)
        vtable_offset_local = IAgSTKXInitialize._vtable_offset - 1
        self.__dict__["_InitializeActivationContext"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXInitialize, vtable_offset_local+1, )
        self.__dict__["_InitializeData"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXInitialize, vtable_offset_local+2, agcom.BSTR, agcom.BSTR)
        self.__dict__["_InitializeDataEx"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXInitialize, vtable_offset_local+3, agcom.BSTR, agcom.BSTR, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSTKXInitialize.__dict__ and type(IAgSTKXInitialize.__dict__[attrname]) == property:
            return IAgSTKXInitialize.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSTKXInitialize.")
    
    def InitializeActivationContext(self) -> None:
        """Initialize the activation context to be used by STK Engine based on the current activation context."""
        agcls.evaluate_hresult(self.__dict__["_InitializeActivationContext"]())

    def InitializeData(self, installHome:str, configDirectory:str) -> None:
        """Copy the virtual registry to the Config directory and initialize it with the install home specified."""
        with agmarshall.BSTR_arg(installHome) as arg_installHome, \
             agmarshall.BSTR_arg(configDirectory) as arg_configDirectory:
            agcls.evaluate_hresult(self.__dict__["_InitializeData"](arg_installHome.COM_val, arg_configDirectory.COM_val))

    def InitializeDataEx(self, installHome:str, configDirectory:str, bDefaults:bool, bStyles:bool, bVGT:bool, bAMM:bool, bGator:bool, bOnlineData:bool, bOnlineSGP4:bool) -> None:
        """Copy the virtual registry to the Config directory and initialize it with the install home specified, and config options."""
        with agmarshall.BSTR_arg(installHome) as arg_installHome, \
             agmarshall.BSTR_arg(configDirectory) as arg_configDirectory, \
             agmarshall.VARIANT_BOOL_arg(bDefaults) as arg_bDefaults, \
             agmarshall.VARIANT_BOOL_arg(bStyles) as arg_bStyles, \
             agmarshall.VARIANT_BOOL_arg(bVGT) as arg_bVGT, \
             agmarshall.VARIANT_BOOL_arg(bAMM) as arg_bAMM, \
             agmarshall.VARIANT_BOOL_arg(bGator) as arg_bGator, \
             agmarshall.VARIANT_BOOL_arg(bOnlineData) as arg_bOnlineData, \
             agmarshall.VARIANT_BOOL_arg(bOnlineSGP4) as arg_bOnlineSGP4:
            agcls.evaluate_hresult(self.__dict__["_InitializeDataEx"](arg_installHome.COM_val, arg_configDirectory.COM_val, arg_bDefaults.COM_val, arg_bStyles.COM_val, arg_bVGT.COM_val, arg_bAMM.COM_val, arg_bGator.COM_val, arg_bOnlineData.COM_val, arg_bOnlineSGP4.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{EDC9E451-09B3-4D8B-9EC5-B75C6D95A52D}", IAgSTKXInitialize)
agcls.AgTypeNameMap["IAgSTKXInitialize"] = IAgSTKXInitialize
__all__.append("IAgSTKXInitialize")



class AgSTKXInitialize(IAgSTKXInitialize):
    """STK X Initialize object."""
    def __init__(self, sourceObject=None):
        IAgSTKXInitialize.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSTKXInitialize._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSTKXInitialize._get_property(self, attrname) is not None: found_prop = IAgSTKXInitialize._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgSTKXInitialize.")
        
agcls.AgClassCatalog.add_catalog_entry("{3B85901D-FC82-4733-97E6-5BB25CE69379}", AgSTKXInitialize)
__all__.append("AgSTKXInitialize")



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
