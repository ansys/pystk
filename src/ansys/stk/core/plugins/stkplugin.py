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


from agi.stk12.plugins.attrautomation import *
from agi.stk12.plugins.utplugin import *
from agi.stk12.plugins.crdnplugin import *
from agi.stk12.plugins.gatorplugin import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError('Valid STK object model classes are returned from STK methods and should not be created independently.')

class IAgStkPluginSite(IAgUtPluginSite):
    '''
    STK application plugin site
    '''
    _uuid = '{F1D25E90-2512-4f8f-8B4E-1FEDE57606BD}'
    _num_methods = 6
    _vtable_offset = IAgUtPluginSite._vtable_offset + IAgUtPluginSite._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetVectorToolProvider'] = _raise_uninitialized_error
        self.__dict__['_GetScenarioDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetInstallDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetConfigDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetStkRootObject'] = _raise_uninitialized_error
        self.__dict__['_GetCalcToolProvider'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgStkPluginSite._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgStkPluginSite from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgUtPluginSite._private_init(self, pUnk)
        IID_IAgStkPluginSite = agcom.GUID(IAgStkPluginSite._uuid)
        vtable_offset_local = IAgStkPluginSite._vtable_offset - 1
        self.__dict__['_GetVectorToolProvider'] = IAGFUNCTYPE(pUnk, IID_IAgStkPluginSite, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__['_GetScenarioDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgStkPluginSite, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__['_GetInstallDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgStkPluginSite, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_GetConfigDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgStkPluginSite, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__['_GetStkRootObject'] = IAGFUNCTYPE(pUnk, IID_IAgStkPluginSite, vtable_offset_local+5, POINTER(agcom.PVOID))
        self.__dict__['_GetCalcToolProvider'] = IAGFUNCTYPE(pUnk, IID_IAgStkPluginSite, vtable_offset_local+6, POINTER(agcom.PVOID))
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgStkPluginSite.__dict__ and type(IAgStkPluginSite.__dict__[attrname]) == property:
            return IAgStkPluginSite.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgUtPluginSite.__setattr__(self, attrname, value)
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        '''
        Creates an IAgCrdnPluginProvider object.
        '''
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__['_GetVectorToolProvider'](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def ScenarioDirectory(self) -> str:
        '''
        The directory path of the current scenario.
        '''
        with agmarshall.BSTR_arg() as arg_pDirPath:
            agcls.evaluate_hresult(self.__dict__['_GetScenarioDirectory'](byref(arg_pDirPath.COM_val)))
            return arg_pDirPath.python_val

    @property
    def InstallDirectory(self) -> str:
        '''
        The directory path of the installation of the application.
        '''
        with agmarshall.BSTR_arg() as arg_pDirPath:
            agcls.evaluate_hresult(self.__dict__['_GetInstallDirectory'](byref(arg_pDirPath.COM_val)))
            return arg_pDirPath.python_val

    @property
    def ConfigDirectory(self) -> str:
        '''
        The directory path of the user configuration area.
        '''
        with agmarshall.BSTR_arg() as arg_pDirPath:
            agcls.evaluate_hresult(self.__dict__['_GetConfigDirectory'](byref(arg_pDirPath.COM_val)))
            return arg_pDirPath.python_val

    @property
    def StkRootObject(self) -> typing.Any:
        '''
        Returns an instance of the STK Object Model Root Object
        '''
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__['_GetStkRootObject'](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        '''
        Creates an IAgCrdnPluginCalcProvider object.
        '''
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__['_GetCalcToolProvider'](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val


agcls.AgClassCatalog.add_catalog_entry('{F1D25E90-2512-4f8f-8B4E-1FEDE57606BD}', IAgStkPluginSite)
agcls.AgTypeNameMap['IAgStkPluginSite'] = IAgStkPluginSite
__all__.append('IAgStkPluginSite')

class IAgGatorPluginSite(IAgUtPluginSite):
    '''
    Astrogator plugin site interface.
    '''
    _uuid = '{62BD3410-1F8F-4d19-AE3B-FD3AA8669FBD}'
    _num_methods = 8
    _vtable_offset = IAgUtPluginSite._vtable_offset + IAgUtPluginSite._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__['_pUnk'] = None
        self.__dict__['_GetVectorToolProvider'] = _raise_uninitialized_error
        self.__dict__['_GetGatorProvider'] = _raise_uninitialized_error
        self.__dict__['_GetScenarioDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetInstallDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetConfigDirectory'] = _raise_uninitialized_error
        self.__dict__['_GetStkRootObject'] = _raise_uninitialized_error
        self.__dict__['_GetDisplayUnit'] = _raise_uninitialized_error
        self.__dict__['_GetCalcToolProvider'] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__['_pUnk'] is not None:
            pUnk = sourceObject.__dict__['_pUnk'].QueryInterface(agcom.GUID(IAgGatorPluginSite._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError('Failed to create IAgGatorPluginSite from source object.')
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgUtPluginSite._private_init(self, pUnk)
        IID_IAgGatorPluginSite = agcom.GUID(IAgGatorPluginSite._uuid)
        vtable_offset_local = IAgGatorPluginSite._vtable_offset - 1
        self.__dict__['_GetVectorToolProvider'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginSite, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__['_GetGatorProvider'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginSite, vtable_offset_local+2, POINTER(agcom.PVOID))
        self.__dict__['_GetScenarioDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginSite, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__['_GetInstallDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginSite, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__['_GetConfigDirectory'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginSite, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__['_GetStkRootObject'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginSite, vtable_offset_local+6, POINTER(agcom.PVOID))
        self.__dict__['_GetDisplayUnit'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginSite, vtable_offset_local+7, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__['_GetCalcToolProvider'] = IAGFUNCTYPE(pUnk, IID_IAgGatorPluginSite, vtable_offset_local+8, POINTER(agcom.PVOID))
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgGatorPluginSite.__dict__ and type(IAgGatorPluginSite.__dict__[attrname]) == property:
            return IAgGatorPluginSite.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgUtPluginSite.__setattr__(self, attrname, value)
    
    @property
    def VectorToolProvider(self) -> "IAgCrdnPluginProvider":
        '''
        Creates an IAgCrdnPluginProvider object.
        '''
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__['_GetVectorToolProvider'](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val

    @property
    def GatorProvider(self) -> "IAgGatorPluginProvider":
        '''
        Creates an IAgGatorPluginProvider object.
        '''
        with agmarshall.AgInterface_out_arg() as arg_ppGatorPrv:
            agcls.evaluate_hresult(self.__dict__['_GetGatorProvider'](byref(arg_ppGatorPrv.COM_val)))
            return arg_ppGatorPrv.python_val

    @property
    def ScenarioDirectory(self) -> str:
        '''
        The directory path of the current scenario.
        '''
        with agmarshall.BSTR_arg() as arg_pDirPath:
            agcls.evaluate_hresult(self.__dict__['_GetScenarioDirectory'](byref(arg_pDirPath.COM_val)))
            return arg_pDirPath.python_val

    @property
    def InstallDirectory(self) -> str:
        '''
        The directory path of the installation of the application.
        '''
        with agmarshall.BSTR_arg() as arg_pDirPath:
            agcls.evaluate_hresult(self.__dict__['_GetInstallDirectory'](byref(arg_pDirPath.COM_val)))
            return arg_pDirPath.python_val

    @property
    def ConfigDirectory(self) -> str:
        '''
        The directory path of the user configuration area.
        '''
        with agmarshall.BSTR_arg() as arg_pDirPath:
            agcls.evaluate_hresult(self.__dict__['_GetConfigDirectory'](byref(arg_pDirPath.COM_val)))
            return arg_pDirPath.python_val

    @property
    def StkRootObject(self) -> typing.Any:
        '''
        Returns an instance of the STK Object Model Root Object
        '''
        with agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__['_GetStkRootObject'](byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def GetDisplayUnit(self, dimension:str) -> str:
        '''
        Gets the display unit (scenario unit) for the given dimension.
        '''
        with agmarshall.BSTR_arg(dimension) as arg_dimension, \
             agmarshall.BSTR_arg() as arg_pDisplayUnit:
            agcls.evaluate_hresult(self.__dict__['_GetDisplayUnit'](arg_dimension.COM_val, byref(arg_pDisplayUnit.COM_val)))
            return arg_pDisplayUnit.python_val

    @property
    def CalcToolProvider(self) -> "IAgCrdnPluginCalcProvider":
        '''
        Creates an IAgCrdnPluginCalcProvider object.
        '''
        with agmarshall.AgInterface_out_arg() as arg_ppCrdnPrv:
            agcls.evaluate_hresult(self.__dict__['_GetCalcToolProvider'](byref(arg_ppCrdnPrv.COM_val)))
            return arg_ppCrdnPrv.python_val


agcls.AgClassCatalog.add_catalog_entry('{62BD3410-1F8F-4d19-AE3B-FD3AA8669FBD}', IAgGatorPluginSite)
agcls.AgTypeNameMap['IAgGatorPluginSite'] = IAgGatorPluginSite
__all__.append('IAgGatorPluginSite')



class AgStkPluginSite(IAgStkPluginSite):
    '''
    STK plugin site.
    '''
    def __init__(self, sourceObject=None):
        IAgStkPluginSite.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgStkPluginSite._private_init(self, pUnk)
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkPluginSite._get_property(self, attrname) is not None: found_prop = IAgStkPluginSite._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgStkPluginSite.')
        
agcls.AgClassCatalog.add_catalog_entry('{2B85A5E2-6B88-40BB-A326-1DC721BE7E43}', AgStkPluginSite)
__all__.append('AgStkPluginSite')


class AgGatorPluginSite(IAgStkPluginSite, IAgGatorPluginSite):
    '''
    Astrogator plugin site.
    '''
    def __init__(self, sourceObject=None):
        IAgStkPluginSite.__init__(self, sourceObject)
        IAgGatorPluginSite.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__['_pUnk'] = pUnk
        IAgStkPluginSite._private_init(self, pUnk)
        IAgGatorPluginSite._private_init(self, pUnk)
    def __eq__(self, other):
        '''
        Checks equality of the underlying STK references.
        '''
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgStkPluginSite._get_property(self, attrname) is not None: found_prop = IAgStkPluginSite._get_property(self, attrname)
        if IAgGatorPluginSite._get_property(self, attrname) is not None: found_prop = IAgGatorPluginSite._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + ' is not a recognized attribute in AgGatorPluginSite.')
        
agcls.AgClassCatalog.add_catalog_entry('{B4813887-1533-4724-AF06-C8282B2C46DB}', AgGatorPluginSite)
__all__.append('AgGatorPluginSite')



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
