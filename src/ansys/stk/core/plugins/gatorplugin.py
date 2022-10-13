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



def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class IAgGatorConfiguredCalcObject(object):
    """Astrogator Calc Object interface which computes its value. Inputs to the Calc Object are provided by the DispInterface which must support IAgGatorState."""
    _uuid = "{6AE7EF38-51E3-4a5a-88DC-7AE3A200AD31}"
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Evaluate"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgGatorConfiguredCalcObject._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgGatorConfiguredCalcObject from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgGatorConfiguredCalcObject = agcom.GUID(IAgGatorConfiguredCalcObject._uuid)
        vtable_offset_local = IAgGatorConfiguredCalcObject._vtable_offset - 1
        self.__dict__["_Evaluate"] = IAGFUNCTYPE(pUnk, IID_IAgGatorConfiguredCalcObject, vtable_offset_local+1, agcom.PVOID, POINTER(agcom.DOUBLE))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGatorConfiguredCalcObject.__dict__ and type(IAgGatorConfiguredCalcObject.__dict__[attrname]) == property:
            return IAgGatorConfiguredCalcObject.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgGatorConfiguredCalcObject.")
    
    def Evaluate(self, dispInterface:"IDispatch") -> float:
        """Computes the Value (in internal units) at the time indicated by the interface. The interface must support IAgGatorState."""
        with agmarshall.AgInterface_in_arg(dispInterface, IDispatch) as arg_dispInterface, \
             agmarshall.DOUBLE_arg() as arg_pValue:
            agcls.evaluate_hresult(self.__dict__["_Evaluate"](arg_dispInterface.COM_val, byref(arg_pValue.COM_val)))
            return arg_pValue.python_val


agcls.AgClassCatalog.add_catalog_entry("{6AE7EF38-51E3-4a5a-88DC-7AE3A200AD31}", IAgGatorConfiguredCalcObject)
agcls.AgTypeNameMap["IAgGatorConfiguredCalcObject"] = IAgGatorConfiguredCalcObject
__all__.append("IAgGatorConfiguredCalcObject")

class IAgGatorPluginProvider(object):
    """Astrogator plugin provider interface."""
    _uuid = "{4E0C33A8-25A9-4ae2-BD33-FC086EF3979D}"
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_ConfigureCalcObject"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgGatorPluginProvider._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgGatorPluginProvider from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgGatorPluginProvider = agcom.GUID(IAgGatorPluginProvider._uuid)
        vtable_offset_local = IAgGatorPluginProvider._vtable_offset - 1
        self.__dict__["_ConfigureCalcObject"] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginProvider, vtable_offset_local+1, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGatorPluginProvider.__dict__ and type(IAgGatorPluginProvider.__dict__[attrname]) == property:
            return IAgGatorPluginProvider.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgGatorPluginProvider.")
    
    def ConfigureCalcObject(self, name:str) -> "IAgGatorConfiguredCalcObject":
        """Creates an IAgGatorCalcObject object from Astrogator component browser."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_calcObject:
            agcls.evaluate_hresult(self.__dict__["_ConfigureCalcObject"](arg_name.COM_val, byref(arg_calcObject.COM_val)))
            return arg_calcObject.python_val


agcls.AgClassCatalog.add_catalog_entry("{4E0C33A8-25A9-4ae2-BD33-FC086EF3979D}", IAgGatorPluginProvider)
agcls.AgTypeNameMap["IAgGatorPluginProvider"] = IAgGatorPluginProvider
__all__.append("IAgGatorPluginProvider")



class AgGatorConfiguredCalcObject(IAgGatorConfiguredCalcObject):
    """Astrogator Calc object from the component browser"""
    def __init__(self, sourceObject=None):
        IAgGatorConfiguredCalcObject.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgGatorConfiguredCalcObject._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgGatorConfiguredCalcObject._get_property(self, attrname) is not None: found_prop = IAgGatorConfiguredCalcObject._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgGatorConfiguredCalcObject.")
        
agcls.AgClassCatalog.add_catalog_entry("{7498D5D7-BA11-439E-8D61-18143D22D858}", AgGatorConfiguredCalcObject)
__all__.append("AgGatorConfiguredCalcObject")


class AgGatorPluginProvider(IAgGatorPluginProvider):
    """Astrogator plugin provider."""
    def __init__(self, sourceObject=None):
        IAgGatorPluginProvider.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgGatorPluginProvider._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgGatorPluginProvider._get_property(self, attrname) is not None: found_prop = IAgGatorPluginProvider._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgGatorPluginProvider.")
        
agcls.AgClassCatalog.add_catalog_entry("{43B6DEE2-9DE1-41BE-AC26-4FEEA9BA932A}", AgGatorPluginProvider)
__all__.append("AgGatorPluginProvider")



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
