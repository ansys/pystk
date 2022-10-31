################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["AgEUtFrame", "AgEUtLogMsgType", "AgEUtPluginErrorCodes", "AgEUtSunPosType", "AgEUtTimeScale", "AgUtPluginConfigVerifyResult", 
"AgUtPluginSite", "IAgPythonPluginAttrs", "IAgUtPluginConfig", "IAgUtPluginConfigVerifyResult", "IAgUtPluginLicensing", 
"IAgUtPluginSite"]

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


from ..plugins.attrautomation import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgEUtTimeScale(IntEnum):
    """Enumeration of time scales of UTC, TAI, TDT, UT1, STKEpochSec, TDB, GPS"""
    # UTC time scale (civil time, Greenwich meridian).
    eUtTimeScaleUTC = 0,
    # TAI time scale (atomic time).
    eUtTimeScaleTAI = 1,
    # TDT time scale (terrestrial dynamical time).
    eUtTimeScaleTDT = 2,
    # UT1 time scale (universal time, corrected for polar motion. Related to the mean diurnal motion of the Sun.).
    eUtTimeScaleUT1 = 3,
    # Seconds past the scenario reference epoch.
    eUtTimeScaleSTKEpochSec = 4,
    # TDB time scale (barycentric dynamical time).
    eUtTimeScaleTDB = 5,
    # GPS time scale (seconds past 06 Jan 1980 00:00:00 UTC).
    eUtTimeScaleGPS = 6

agcls.AgTypeNameMap["AgEUtTimeScale"] = AgEUtTimeScale

class AgEUtLogMsgType(IntEnum):
    """Enumeration of log message types of Debug, Informational, Force Informational, Warning, Alarm"""
    # Debugging message.
    eUtLogMsgDebug = 0,
    # Informational message.
    eUtLogMsgInfo = 1,
    # Informational message.
    eUtLogMsgForceInfo = 2,
    # Warning message.
    eUtLogMsgWarning = 3,
    # Alarm message.
    eUtLogMsgAlarm = 4

agcls.AgTypeNameMap["AgEUtLogMsgType"] = AgEUtLogMsgType

class AgEUtFrame(IntEnum):
    """Enumeration of reference frames of inertial, fixed, local vertical local horizontal (Gauss), normal tangential crosstrack (Frenet), ICRF, J2000"""
    # Inertial frame of the central body.
    eUtFrameInertial = 0,
    # Fixed frame of the central body.
    eUtFrameFixed = 1,
    # Local vertical, local horizontal frame [Gauss frame] (x along radial, y along intrack, z along crosstrack (position cross inertial velocity))
    eUtFrameLVLH = 2,
    # Normal Tangential CrossTrack frame [Frenet frame] (y along tangential (inertial velocity), z along crosstrack (position cross inertial velocity), x is normal completing the triad (radius-like))
    eUtFrameNTC = 3,
    # ICRF frame of the central body (origin at central body with axes parallel to ICRF).
    eUtFrameICRF = 4,
    # J2000 frame of the central body (origin at central body with axes parallel to J2000).
    eUtFrameJ2000 = 5

agcls.AgTypeNameMap["AgEUtFrame"] = AgEUtFrame

class AgEUtSunPosType(IntEnum):
    """Enumeration of sun position computation methods of apparent to true of central body, apparent, true position, method of current force model"""
    # Apparent Sun position from center of central body
    eUtSunPosTypeApparentToTrueCB = 0,
    # Apparent Sun position as viewed by Satellite
    eUtSunPosTypeApparent = 1,
    # True Sun position
    eUtSunPosTypeTrue = 2,
    # Use the method defined by the current force model settings
    eUtSunPosTypeSRP = 3

agcls.AgTypeNameMap["AgEUtSunPosType"] = AgEUtSunPosType

class AgEUtPluginErrorCodes(IntEnum):
    """Enumeration of AgUtPlugin General Error Codes"""
    # Plugin: An internal failure occurred.
    eUtPluginInternalFailure = (((1 << 31) | (4 << 16)) | 0x0001),
    # Plugin: The square root of an invalid value occurred.
    eUtPluginInvalidSqr = (((1 << 31) | (4 << 16)) | 0x0002),
    # Plugin: The value provided was invalid because it was negative in sign.
    eUtPluginInvalidNegativeValue = (((1 << 31) | (4 << 16)) | 0x0003),
    # Plugin: The log level value provided was not within the range of 0 to 4.
    eUtPluginLogLevelOutOfRange = (((1 << 31) | (4 << 16)) | 0x0004),
    # Plugin: The date cannot be formatted as requested.
    eUtPluginCannotFormatDate = (((1 << 31) | (4 << 16)) | 0x0005),
    # Plugin: The date abbreviation was not recognized.
    eUtPluginInvalidDateAbbrv = (((1 << 31) | (4 << 16)) | 0x0006)

agcls.AgTypeNameMap["AgEUtPluginErrorCodes"] = AgEUtPluginErrorCodes


class IAgUtPluginSite(object):
    """Plugin caller interface"""
    _uuid = "{65F51C50-BB26-463c-9F61-EF4D3E719B53}"
    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetSiteName"] = _raise_uninitialized_error
        self.__dict__["_Message"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUtPluginSite._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUtPluginSite from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUtPluginSite = agcom.GUID(IAgUtPluginSite._uuid)
        vtable_offset_local = IAgUtPluginSite._vtable_offset - 1
        self.__dict__["_GetSiteName"] = IAGFUNCTYPE(pUnk, IID_IAgUtPluginSite, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_Message"] = IAGFUNCTYPE(pUnk, IID_IAgUtPluginSite, vtable_offset_local+2, agcom.LONG, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUtPluginSite.__dict__ and type(IAgUtPluginSite.__dict__[attrname]) == property:
            return IAgUtPluginSite.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUtPluginSite.")
    
    @property
    def SiteName(self) -> str:
        """Returns the site name calling the plugin."""
        with agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__["_GetSiteName"](byref(arg_pName.COM_val)))
            return arg_pName.python_val

    def Message(self, msgType:"AgEUtLogMsgType", message:str) -> None:
        """Send a message to the message viewer."""
        with agmarshall.AgEnum_arg(AgEUtLogMsgType, msgType) as arg_msgType, \
             agmarshall.BSTR_arg(message) as arg_message:
            agcls.evaluate_hresult(self.__dict__["_Message"](arg_msgType.COM_val, arg_message.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{65F51C50-BB26-463c-9F61-EF4D3E719B53}", IAgUtPluginSite)
agcls.AgTypeNameMap["IAgUtPluginSite"] = IAgUtPluginSite

class IAgUtPluginConfigVerifyResult(object):
    """Plugin Configuration Verify Result Interface"""
    _uuid = "{73C70857-08E0-49a5-A1B6-C2E3D44A4075}"
    _num_methods = 4
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetResult"] = _raise_uninitialized_error
        self.__dict__["_SetResult"] = _raise_uninitialized_error
        self.__dict__["_GetMessage"] = _raise_uninitialized_error
        self.__dict__["_SetMessage"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUtPluginConfigVerifyResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUtPluginConfigVerifyResult from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUtPluginConfigVerifyResult = agcom.GUID(IAgUtPluginConfigVerifyResult._uuid)
        vtable_offset_local = IAgUtPluginConfigVerifyResult._vtable_offset - 1
        self.__dict__["_GetResult"] = IAGFUNCTYPE(pUnk, IID_IAgUtPluginConfigVerifyResult, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetResult"] = IAGFUNCTYPE(pUnk, IID_IAgUtPluginConfigVerifyResult, vtable_offset_local+2, agcom.VARIANT_BOOL)
        self.__dict__["_GetMessage"] = IAGFUNCTYPE(pUnk, IID_IAgUtPluginConfigVerifyResult, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_SetMessage"] = IAGFUNCTYPE(pUnk, IID_IAgUtPluginConfigVerifyResult, vtable_offset_local+4, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUtPluginConfigVerifyResult.__dict__ and type(IAgUtPluginConfigVerifyResult.__dict__[attrname]) == property:
            return IAgUtPluginConfigVerifyResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUtPluginConfigVerifyResult.")
    
    @property
    def Result(self) -> bool:
        """The result of the validation of the configuration whether it has succeeded or failed."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pbResult:
            agcls.evaluate_hresult(self.__dict__["_GetResult"](byref(arg_pbResult.COM_val)))
            return arg_pbResult.python_val

    @Result.setter
    def Result(self, result:bool) -> None:
        """The result of the validation of the configuration whether it has succeeded or failed."""
        with agmarshall.VARIANT_BOOL_arg(result) as arg_result:
            agcls.evaluate_hresult(self.__dict__["_SetResult"](arg_result.COM_val))

    @property
    def Message(self) -> str:
        """The message of the validation of the configuration if it has failed."""
        with agmarshall.BSTR_arg() as arg_pbstrMessage:
            agcls.evaluate_hresult(self.__dict__["_GetMessage"](byref(arg_pbstrMessage.COM_val)))
            return arg_pbstrMessage.python_val

    @Message.setter
    def Message(self, message:str) -> None:
        """The message of the validation of the configuration if it has failed."""
        with agmarshall.BSTR_arg(message) as arg_message:
            agcls.evaluate_hresult(self.__dict__["_SetMessage"](arg_message.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{73C70857-08E0-49a5-A1B6-C2E3D44A4075}", IAgUtPluginConfigVerifyResult)
agcls.AgTypeNameMap["IAgUtPluginConfigVerifyResult"] = IAgUtPluginConfigVerifyResult

class IAgUtPluginLicensing(object):
    """Plugin Licensing Interface"""
    _uuid = "{30B9CDD7-A424-4780-9562-15D358E20313}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_CheckLicense"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUtPluginLicensing._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUtPluginLicensing from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUtPluginLicensing = agcom.GUID(IAgUtPluginLicensing._uuid)
        vtable_offset_local = IAgUtPluginLicensing._vtable_offset - 1
        self.__dict__["_CheckLicense"] = IAGFUNCTYPE(pUnk, IID_IAgUtPluginLicensing, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUtPluginLicensing.__dict__ and type(IAgUtPluginLicensing.__dict__[attrname]) == property:
            return IAgUtPluginLicensing.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUtPluginLicensing.")
    
    def CheckLicense(self) -> bool:
        """Check to see if plugin is licensed"""
        with agmarshall.VARIANT_BOOL_arg() as arg_pPluginCfgResult:
            agcls.evaluate_hresult(self.__dict__["_CheckLicense"](byref(arg_pPluginCfgResult.COM_val)))
            return arg_pPluginCfgResult.python_val


agcls.AgClassCatalog.add_catalog_entry("{30B9CDD7-A424-4780-9562-15D358E20313}", IAgUtPluginLicensing)
agcls.AgTypeNameMap["IAgUtPluginLicensing"] = IAgUtPluginLicensing

class IAgPythonPluginAttrs(object):
    """COM Plugin Attribute interface for updating plugin attributes."""
    _uuid = "{FB0A773D-277E-4959-85C9-671FD5BAAE78}"
    _num_methods = 0
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgPythonPluginAttrs._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgPythonPluginAttrs from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgPythonPluginAttrs = agcom.GUID(IAgPythonPluginAttrs._uuid)
        vtable_offset_local = IAgPythonPluginAttrs._vtable_offset - 1
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgPythonPluginAttrs.__dict__ and type(IAgPythonPluginAttrs.__dict__[attrname]) == property:
            return IAgPythonPluginAttrs.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgPythonPluginAttrs.")
    

agcls.AgClassCatalog.add_catalog_entry("{FB0A773D-277E-4959-85C9-671FD5BAAE78}", IAgPythonPluginAttrs)
agcls.AgTypeNameMap["IAgPythonPluginAttrs"] = IAgPythonPluginAttrs


class IAgUtPluginConfig(object):
    """
    Plugin Configuration Interface
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def GetPluginConfig(self, pAttrBuilder:"IAgAttrBuilder") -> typing.Any:
        """Get an attribute container of the configuration settings."""
        raise STKPluginMethodNotImplementedError("GetPluginConfig was not implemented.")

    def VerifyPluginConfig(self, pPluginCfgResult:"IAgUtPluginConfigVerifyResult") -> None:
        """Verify the Plugin Config"""
        raise STKPluginMethodNotImplementedError("VerifyPluginConfig was not implemented.")




class AgUtPluginConfigVerifyResult(IAgUtPluginConfigVerifyResult):
    """Class used as parameter to the VerifyPluginConfig method of IAgUtPluginConfig interface."""
    def __init__(self, sourceObject=None):
        IAgUtPluginConfigVerifyResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUtPluginConfigVerifyResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUtPluginConfigVerifyResult._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfigVerifyResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUtPluginConfigVerifyResult.")
        
agcls.AgClassCatalog.add_catalog_entry("{B25FE56B-CD7F-4938-A895-33106BB53CBE}", AgUtPluginConfigVerifyResult)


class AgUtPluginSite(IAgUtPluginSite):
    """Plugin caller interface"""
    def __init__(self, sourceObject=None):
        IAgUtPluginSite.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUtPluginSite._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUtPluginSite._get_property(self, attrname) is not None: found_prop = IAgUtPluginSite._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUtPluginSite.")
        
agcls.AgClassCatalog.add_catalog_entry("{BA95A65F-0938-4EBF-AEC1-A77E0325DE24}", AgUtPluginSite)



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
