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

class AgEAttrAddFlags(IntFlag):
    """Enumeration of Attribute Flags"""
    # No special flag
    eAddFlagNone = 0x0000,
    # When applied to a container, makes the container transparent (i.e. its attributes are directly visible without having to navigate into the container)
    eAddFlagTransparent = 0x0002,
    # The attribute is not visible in the user interface property page.
    eAddFlagHidden = 0x0004,
    # The attribute is ignored during save/load.
    eAddFlagTransient = 0x0008,
    # The attribute is read-only and cannot be modified by the user.
    eAddFlagReadOnly = 0x0010,
    # The attribute container has a fixed size. Additions/removals of sub-elements are prohibited.
    eAddFlagFixed = 0x0020

agcls.AgTypeNameMap["AgEAttrAddFlags"] = AgEAttrAddFlags
__all__.append("AgEAttrAddFlags")


class IAgAttrBuilder(object):
    """Attribute Automation Builder Interface helps construct an Attribute Scope"""
    _uuid = "{BD47DED6-51B4-425f-AD80-6BB07C7E8B41}"
    _num_methods = 29
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_NewScope"] = _raise_uninitialized_error
        self.__dict__["_AddIntDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddLongDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddStringDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddBoolDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddFileDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddDirectoryDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddRelFileDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddDoubleDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddDateDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_ToString"] = _raise_uninitialized_error
        self.__dict__["_MergeFromString"] = _raise_uninitialized_error
        self.__dict__["_AddDependencyDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddFlagsDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddChoicesDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddListDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddVARIANTDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddMultiLineStringDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_ToFormattedString"] = _raise_uninitialized_error
        self.__dict__["_AddQuantityDispatchProperty2"] = _raise_uninitialized_error
        self.__dict__["_AddQuantityMinMaxDispatchProperty2"] = _raise_uninitialized_error
        self.__dict__["_AddScopeDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddChoicesFuncDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddDoubleMinDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddDoubleMinMaxDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddQuantityMinDispatchProperty2"] = _raise_uninitialized_error
        self.__dict__["_AddIntMinDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddIntMinMaxDispatchProperty"] = _raise_uninitialized_error
        self.__dict__["_AddScopeDispatchProperty2"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgAttrBuilder._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgAttrBuilder from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgAttrBuilder = agcom.GUID(IAgAttrBuilder._uuid)
        vtable_offset_local = IAgAttrBuilder._vtable_offset - 1
        self.__dict__["_NewScope"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_AddIntDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+2, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddLongDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+3, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddStringDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+4, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddBoolDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+5, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddFileDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+6, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddDirectoryDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+7, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddRelFileDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+8, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddDoubleDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+9, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddDateDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+10, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_ToString"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+11, agcom.PVOID, agcom.PVOID, POINTER(agcom.BSTR))
        self.__dict__["_MergeFromString"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+12, agcom.PVOID, agcom.PVOID, agcom.BSTR)
        self.__dict__["_AddDependencyDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+13, agcom.PVOID, agcom.BSTR, agcom.BSTR)
        self.__dict__["_AddFlagsDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+14, agcom.PVOID, agcom.BSTR, agcom.BSTR)
        self.__dict__["_AddChoicesDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+15, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.SAFEARRAY)
        self.__dict__["_AddListDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+16, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddVARIANTDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+17, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddMultiLineStringDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+18, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_ToFormattedString"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+19, agcom.PVOID, agcom.PVOID, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_AddQuantityDispatchProperty2"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+20, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.LONG)
        self.__dict__["_AddQuantityMinMaxDispatchProperty2"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+21, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG)
        self.__dict__["_AddScopeDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+22, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.PVOID)
        self.__dict__["_AddChoicesFuncDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+23, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR)
        self.__dict__["_AddDoubleMinDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+24, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, agcom.LONG)
        self.__dict__["_AddDoubleMinMaxDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+25, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG)
        self.__dict__["_AddQuantityMinDispatchProperty2"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+26, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, agcom.LONG)
        self.__dict__["_AddIntMinDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+27, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.INT, agcom.LONG)
        self.__dict__["_AddIntMinMaxDispatchProperty"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+28, agcom.PVOID, agcom.BSTR, agcom.BSTR, agcom.BSTR, agcom.INT, agcom.INT, agcom.LONG)
        self.__dict__["_AddScopeDispatchProperty2"] = IAGFUNCTYPE(pUnk, IID_IAgAttrBuilder, vtable_offset_local+29, agcom.PVOID, agcom.BSTR, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAttrBuilder.__dict__ and type(IAgAttrBuilder.__dict__[attrname]) == property:
            return IAgAttrBuilder.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgAttrBuilder.")
    
    def NewScope(self) -> typing.Any:
        """Create a new Attribute Scope for use in Attribute Builder method calls"""
        with agmarshall.AgInterface_out_arg() as arg_dispScope:
            agcls.evaluate_hresult(self.__dict__["_NewScope"](byref(arg_dispScope.COM_val)))
            return arg_dispScope.python_val

    def AddIntDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type int to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddIntDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def AddLongDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type long to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddLongDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def AddStringDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type string to the Attribute Scope. Only allows single line strings. For multi-line strings use AddMultiLineStringDispatchProperty. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddStringDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def AddBoolDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type bool to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddBoolDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def AddFileDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, fileType:str, fileFilter:str, flags:int) -> None:
        """Add an Attribute of type file (string) to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.BSTR_arg(fileType) as arg_fileType, \
             agmarshall.BSTR_arg(fileFilter) as arg_fileFilter, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddFileDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_fileType.COM_val, arg_fileFilter.COM_val, arg_flags.COM_val))

    def AddDirectoryDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type directory (string) to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddDirectoryDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def AddRelFileDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, fileType:str, fileFilter:str, flags:int) -> None:
        """Add an Attribute of type relative file path (string) to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.BSTR_arg(fileType) as arg_fileType, \
             agmarshall.BSTR_arg(fileFilter) as arg_fileFilter, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddRelFileDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_fileType.COM_val, arg_fileFilter.COM_val, arg_flags.COM_val))

    def AddDoubleDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type double to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddDoubleDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def AddDateDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type date (represented as a double in EpSec) to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddDateDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def ToString(self, dispPlugin:"IDispatch", dispScope:"IDispatch") -> str:
        """Serialize an Attribute scope for a plugin to a formatted XML String representation. (internal use)"""
        with agmarshall.AgInterface_in_arg(dispPlugin, IDispatch) as arg_dispPlugin, \
             agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg() as arg_xmlString:
            agcls.evaluate_hresult(self.__dict__["_ToString"](arg_dispPlugin.COM_val, arg_dispScope.COM_val, byref(arg_xmlString.COM_val)))
            return arg_xmlString.python_val

    def MergeFromString(self, dispPlugin:"IDispatch", dispScope:"IDispatch", xmlString:str) -> None:
        """Deserialize an Attribute scope into a plugin from a formatted XML String representation. (internal use)"""
        with agmarshall.AgInterface_in_arg(dispPlugin, IDispatch) as arg_dispPlugin, \
             agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(xmlString) as arg_xmlString:
            agcls.evaluate_hresult(self.__dict__["_MergeFromString"](arg_dispPlugin.COM_val, arg_dispScope.COM_val, arg_xmlString.COM_val))

    def AddDependencyDispatchProperty(self, dispScope:"IDispatch", parentAttributeName:str, childAttributeName:str) -> None:
        """Add a Dependency between two Attributes within the Attribute Scope provided. Dependencies are used to force the update of the child attribute when the parent attribute is modified by the user."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(parentAttributeName) as arg_parentAttributeName, \
             agmarshall.BSTR_arg(childAttributeName) as arg_childAttributeName:
            agcls.evaluate_hresult(self.__dict__["_AddDependencyDispatchProperty"](arg_dispScope.COM_val, arg_parentAttributeName.COM_val, arg_childAttributeName.COM_val))

    def AddFlagsDispatchProperty(self, dispScope:"IDispatch", name:str, flagPropName:str) -> None:
        """Add a callback to retrieve the flags for the provided Attribute name from the provided property name. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(flagPropName) as arg_flagPropName:
            agcls.evaluate_hresult(self.__dict__["_AddFlagsDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_flagPropName.COM_val))

    def AddChoicesDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, choices:list) -> None:
        """Add an Attribute that provides a combobox of values from which the user can choose. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.SAFEARRAY_arg(choices) as arg_choices:
            agcls.evaluate_hresult(self.__dict__["_AddChoicesDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_choices.COM_val))

    def AddListDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, newElemMethodName:str, flags:int) -> None:
        """Add an Attribute that represents a list of values. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.BSTR_arg(newElemMethodName) as arg_newElemMethodName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddListDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_newElemMethodName.COM_val, arg_flags.COM_val))

    def AddVARIANTDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type variant to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddVARIANTDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def AddMultiLineStringDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, flags:int) -> None:
        """Add an Attribute of type multi-line string to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddMultiLineStringDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_flags.COM_val))

    def ToFormattedString(self, dispPlugin:"IDispatch", dispScope:"IDispatch", formatId:str) -> str:
        """Get a String representation of the Attribute Scope, formatted using the specified FormatId. (internal use)"""
        with agmarshall.AgInterface_in_arg(dispPlugin, IDispatch) as arg_dispPlugin, \
             agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(formatId) as arg_formatId, \
             agmarshall.BSTR_arg() as arg_xmlString:
            agcls.evaluate_hresult(self.__dict__["_ToFormattedString"](arg_dispPlugin.COM_val, arg_dispScope.COM_val, arg_formatId.COM_val, byref(arg_xmlString.COM_val)))
            return arg_xmlString.python_val

    def AddQuantityDispatchProperty2(self, dispScope:"IDispatch", name:str, description:str, propName:str, dimension:str, displayUnit:str, internalUnit:str, flags:int) -> None:
        """Add an Attribute of type quantity to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.BSTR_arg(displayUnit) as arg_displayUnit, \
             agmarshall.BSTR_arg(internalUnit) as arg_internalUnit, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddQuantityDispatchProperty2"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_dimension.COM_val, arg_displayUnit.COM_val, arg_internalUnit.COM_val, arg_flags.COM_val))

    def AddQuantityMinMaxDispatchProperty2(self, dispScope:"IDispatch", name:str, description:str, propName:str, dimension:str, displayUnit:str, internalUnit:str, minVal:float, maxVal:float, flags:int) -> None:
        """Add an Attribute of type quantity to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.BSTR_arg(displayUnit) as arg_displayUnit, \
             agmarshall.BSTR_arg(internalUnit) as arg_internalUnit, \
             agmarshall.DOUBLE_arg(minVal) as arg_minVal, \
             agmarshall.DOUBLE_arg(maxVal) as arg_maxVal, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddQuantityMinMaxDispatchProperty2"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_dimension.COM_val, arg_displayUnit.COM_val, arg_internalUnit.COM_val, arg_minVal.COM_val, arg_maxVal.COM_val, arg_flags.COM_val))

    def AddScopeDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, newDispScope:"IDispatch") -> None:
        """Add an Attribute to the 'NewDispScope' Scope (to construct a hierarchy). It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.AgInterface_in_arg(newDispScope, IDispatch) as arg_newDispScope:
            agcls.evaluate_hresult(self.__dict__["_AddScopeDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_newDispScope.COM_val))

    def AddChoicesFuncDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, funcPropName:str) -> None:
        """Add an Attribute that provides a combobox of values from which the user can choose. Similar to AddChoicesDispatchProperty but uses a callback to get the list of available values instead of a static array of strings. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.BSTR_arg(funcPropName) as arg_funcPropName:
            agcls.evaluate_hresult(self.__dict__["_AddChoicesFuncDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_funcPropName.COM_val))

    def AddDoubleMinDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, minVal:float, flags:int) -> None:
        """Add an Attribute of type double with a min to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.DOUBLE_arg(minVal) as arg_minVal, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddDoubleMinDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_minVal.COM_val, arg_flags.COM_val))

    def AddDoubleMinMaxDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, minVal:float, maxVal:float, flags:int) -> None:
        """Add an Attribute of type double with a min and max to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.DOUBLE_arg(minVal) as arg_minVal, \
             agmarshall.DOUBLE_arg(maxVal) as arg_maxVal, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddDoubleMinMaxDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_minVal.COM_val, arg_maxVal.COM_val, arg_flags.COM_val))

    def AddQuantityMinDispatchProperty2(self, dispScope:"IDispatch", name:str, description:str, propName:str, dimension:str, displayUnit:str, internalUnit:str, minVal:float, flags:int) -> None:
        """Add an Attribute of type quantity with a min to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.BSTR_arg(displayUnit) as arg_displayUnit, \
             agmarshall.BSTR_arg(internalUnit) as arg_internalUnit, \
             agmarshall.DOUBLE_arg(minVal) as arg_minVal, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddQuantityMinDispatchProperty2"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_dimension.COM_val, arg_displayUnit.COM_val, arg_internalUnit.COM_val, arg_minVal.COM_val, arg_flags.COM_val))

    def AddIntMinDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, minVal:int, flags:int) -> None:
        """Add an Attribute of type int with a minimum to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.INT_arg(minVal) as arg_minVal, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddIntMinDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_minVal.COM_val, arg_flags.COM_val))

    def AddIntMinMaxDispatchProperty(self, dispScope:"IDispatch", name:str, description:str, propName:str, minVal:int, maxVal:int, flags:int) -> None:
        """Add an Attribute of type int with a min and max to the Attribute Scope. It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description, \
             agmarshall.BSTR_arg(propName) as arg_propName, \
             agmarshall.INT_arg(minVal) as arg_minVal, \
             agmarshall.INT_arg(maxVal) as arg_maxVal, \
             agmarshall.LONG_arg(flags) as arg_flags:
            agcls.evaluate_hresult(self.__dict__["_AddIntMinMaxDispatchProperty"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val, arg_propName.COM_val, arg_minVal.COM_val, arg_maxVal.COM_val, arg_flags.COM_val))

    def AddScopeDispatchProperty2(self, dispScope:"IDispatch", name:str, description:str) -> None:
        """Add an Attribute to the current Attribute Scope (to construct a hierarchy). It is recommended that any name used for these configuration properties not include spaces because certain interfaces to the properties may not work correctly."""
        with agmarshall.AgInterface_in_arg(dispScope, IDispatch) as arg_dispScope, \
             agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.BSTR_arg(description) as arg_description:
            agcls.evaluate_hresult(self.__dict__["_AddScopeDispatchProperty2"](arg_dispScope.COM_val, arg_name.COM_val, arg_description.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{BD47DED6-51B4-425f-AD80-6BB07C7E8B41}", IAgAttrBuilder)
agcls.AgTypeNameMap["IAgAttrBuilder"] = IAgAttrBuilder
__all__.append("IAgAttrBuilder")

class IAgAttrConfig(object):
    """Attributes Configuration Interface"""
    _uuid = "{EB74434B-4493-413b-A098-DB610508745D}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetConfig"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgAttrConfig._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgAttrConfig from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgAttrConfig = agcom.GUID(IAgAttrConfig._uuid)
        vtable_offset_local = IAgAttrConfig._vtable_offset - 1
        self.__dict__["_GetConfig"] = IAGFUNCTYPE(pUnk, IID_IAgAttrConfig, vtable_offset_local+1, agcom.PVOID, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAttrConfig.__dict__ and type(IAgAttrConfig.__dict__[attrname]) == property:
            return IAgAttrConfig.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgAttrConfig.")
    
    def GetConfig(self, pAttrBuilder:"IAgAttrBuilder") -> typing.Any:
        """Get the configuration represented by an attribute container (also called attribute scope)."""
        with agmarshall.AgInterface_in_arg(pAttrBuilder, IAgAttrBuilder) as arg_pAttrBuilder, \
             agmarshall.AgInterface_out_arg() as arg_ppDispScope:
            agcls.evaluate_hresult(self.__dict__["_GetConfig"](arg_pAttrBuilder.COM_val, byref(arg_ppDispScope.COM_val)))
            return arg_ppDispScope.python_val


agcls.AgClassCatalog.add_catalog_entry("{EB74434B-4493-413b-A098-DB610508745D}", IAgAttrConfig)
agcls.AgTypeNameMap["IAgAttrConfig"] = IAgAttrConfig
__all__.append("IAgAttrConfig")

class IAgAttrAutomationConnector(object):
    """Attributes Automation Connector Interface"""
    _uuid = "{2A376EFB-4A22-4767-A9F5-36B95D863EC4}"
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_ConnectObject"] = _raise_uninitialized_error
        self.__dict__["_DisconnectObject"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgAttrAutomationConnector._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgAttrAutomationConnector from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgAttrAutomationConnector = agcom.GUID(IAgAttrAutomationConnector._uuid)
        vtable_offset_local = IAgAttrAutomationConnector._vtable_offset - 1
        self.__dict__["_ConnectObject"] = IAGFUNCTYPE(pUnk, IID_IAgAttrAutomationConnector, vtable_offset_local+1, agcom.PVOID)
        self.__dict__["_DisconnectObject"] = IAGFUNCTYPE(pUnk, IID_IAgAttrAutomationConnector, vtable_offset_local+2, )
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAttrAutomationConnector.__dict__ and type(IAgAttrAutomationConnector.__dict__[attrname]) == property:
            return IAgAttrAutomationConnector.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgAttrAutomationConnector.")
    
    def ConnectObject(self, objectDispatch:"IDispatch") -> None:
        """Connect to Attributes Automation Adapter Object (AgAttrAutomationAdapter)"""
        with agmarshall.AgInterface_in_arg(objectDispatch, IDispatch) as arg_objectDispatch:
            agcls.evaluate_hresult(self.__dict__["_ConnectObject"](arg_objectDispatch.COM_val))

    def DisconnectObject(self) -> None:
        """Disconnect from Attributes Automation Adapter Object (AgAttrAutomationAdapter)"""
        agcls.evaluate_hresult(self.__dict__["_DisconnectObject"]())


agcls.AgClassCatalog.add_catalog_entry("{2A376EFB-4A22-4767-A9F5-36B95D863EC4}", IAgAttrAutomationConnector)
agcls.AgTypeNameMap["IAgAttrAutomationConnector"] = IAgAttrAutomationConnector
__all__.append("IAgAttrAutomationConnector")



class AgAttrBuilder(IAgAttrBuilder):
    """Attribute Automation Builder Class helps construct an Attribute Scope"""
    def __init__(self, sourceObject=None):
        IAgAttrBuilder.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgAttrBuilder._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAttrBuilder._get_property(self, attrname) is not None: found_prop = IAgAttrBuilder._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgAttrBuilder.")
        
agcls.AgClassCatalog.add_catalog_entry("{2F0A09A2-B9DC-4740-9A60-735CA72F81A0}", AgAttrBuilder)
__all__.append("AgAttrBuilder")



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
