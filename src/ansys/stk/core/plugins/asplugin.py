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


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgEAsPluginErrorCodes(IntEnum):
    """Enumeration of AgAsPlugin General Error Codes"""
    # Plugin: An internal failure occurred.
    eAstroPluginInternalFailure = (((1 << 31) | (4 << 16)) | 0x0001),
    # The specified format is invalid (either containing spaces or matching an existing format).
    eEphemerisReaderBadFormat = (((1 << 31) | (4 << 16)) | 0x0002),
    # The central body name is invalid.
    eAstroPluginBadCentralBody = (((1 << 31) | (4 << 16)) | 0x0003),
    # The coordinate system is unrecognized.
    eEphemerisReaderBadCoordinateSystem = (((1 << 31) | (4 << 16)) | 0x0004),
    # The interpolation method is invalid.
    eEphemerisReaderBadInterpolationMethod = (((1 << 31) | (4 << 16)) | 0x0005),
    # The interpolation order is invalid.
    eEphemerisReaderBadInterpolationOrder = (((1 << 31) | (4 << 16)) | 0x0006),
    # The covariance representation is invalid.
    eEphemerisReaderBadCovarianceRepresentation = (((1 << 31) | (4 << 16)) | 0x0008),
    # The VopMu value is invalid. Must be positive.
    eEphemerisReaderBadVopMu = (((1 << 31) | (4 << 16)) | 0x0007),
    # The distance unit is invalid.
    eEphemerisReaderBadDistanceUnit = (((1 << 31) | (4 << 16)) | 0x0008),
    # The time unit is invalid.
    eEphemerisReaderBadTimeUnit = (((1 << 31) | (4 << 16)) | 0x0009),
    # The double is not a finite value (i.e., infinite or indeterminant).
    eAstroPluginBadDouble = (((1 << 31) | (4 << 16)) | 0x0010),
    # The covariance array does not contain the required number of entries (6 or 21).
    eEphemerisReaderBadCovarianceArray = (((1 << 31) | (4 << 16)) | 0x0011)

agcls.AgTypeNameMap["AgEAsPluginErrorCodes"] = AgEAsPluginErrorCodes
__all__.append("AgEAsPluginErrorCodes")

class AgEAsEphemInterpolationMethod(IntEnum):
    """Enumeration of interpolation methods valid for IAgAsEphemFileReaderPlugin"""
    # Invalid AgEAsEphemInterpolationMethod indicator.
    eAsEphemInterpolationMethodUnknown = -1,
    # Lagrange interpolation. Position and velocity are interpolated independently.
    eAsEphemInterpolationMethodLagrange = 0,
    # Hermitian interpolation. Position and velocity are interpolated together.
    eAsEphemInterpolationMethodHermite = 1,
    # Lagrange VOP interpolation. Position and velocity are interpolated independently, using a VOP formulation.
    eAsEphemInterpolationMethodLagrangeVOP = 2

agcls.AgTypeNameMap["AgEAsEphemInterpolationMethod"] = AgEAsEphemInterpolationMethod
__all__.append("AgEAsEphemInterpolationMethod")

class AgEAsCovRep(IntEnum):
    """Enumeration of covariance representations for IAgAsEphemFileReaderPlugin"""
    # Invalid AgEAsCovRep indicator.
    eAsCovRepUnknown = -1,
    # The covariance components are expressed using the same coordinate system as the ephemeris (i.e., X, Y, Z, etc.)
    eAsCovRepStandard = 0,
    # The covariance components are expressed using radial, inTrack, and crossTrack components, computed using the same coordinate system as the ephemeris.
    eAsCovRepRIC = 1

agcls.AgTypeNameMap["AgEAsCovRep"] = AgEAsCovRep
__all__.append("AgEAsCovRep")

class AgEAsCovType(IntEnum):
    """Enumeration of the desired covariance level."""
    # Invalid AgEAsCovType indicator.
    eAsCovTypeUnknown = -1,
    # No covariance is desired.
    eAsCovTypeNone = 0,
    # Position covariance is desired. The 6 values of the lower triangular position covariance matrix will be kept if provided.
    eAsCovTypePosition = 1,
    # Position and velocity covariance is desired.  The 21 values of the lower triangular position-velocity covariance matrix will be kept if provided.
    eAsCovTypePositionVelocity = 2

agcls.AgTypeNameMap["AgEAsCovType"] = AgEAsCovType
__all__.append("AgEAsCovType")

class AgEAsEphemFileDistanceUnit(IntEnum):
    """Sets the distance units."""
    # Invalid AgEAsEphemFileDistanceUnit indicator.
    eAsEphemFileDistanceUnitUnknown = -1,
    # Meter
    eAsEphemFileDistanceUnitMeter = 0,
    # Kilometer
    eAsEphemFileDistanceUnitKilometer = 1,
    # KiloFeet
    eAsEphemFileDistanceUnitKiloFeet = 2,
    # Feet
    eAsEphemFileDistanceUnitFeet = 3,
    # Nautical Mile
    eAsEphemFileDistanceUnitNautMile = 4

agcls.AgTypeNameMap["AgEAsEphemFileDistanceUnit"] = AgEAsEphemFileDistanceUnit
__all__.append("AgEAsEphemFileDistanceUnit")

class AgEAsEphemFileTimeUnit(IntEnum):
    """Sets the time units."""
    # Invalid AgEAsEphemFileTimeUnit indicator.
    eAsEphemFileTimeUnitUnknown = -1,
    # Seconds
    eAsEphemFileTimeUnitSecond = 0,
    # Minutes
    eAsEphemFileTimeUnitMinute = 1,
    # Hours
    eAsEphemFileTimeUnitHour = 2,
    # Days
    eAsEphemFileTimeUnitDay = 3

agcls.AgTypeNameMap["AgEAsEphemFileTimeUnit"] = AgEAsEphemFileTimeUnit
__all__.append("AgEAsEphemFileTimeUnit")


class IAgAsEphemFileReaderPluginResultReg(object):
    """Interface for use with IAgAsEphemFileReaderPlugin"""
    _uuid = "{F6A367B8-235A-423d-BBD6-F00486DC1CCB}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFormatID"] = _raise_uninitialized_error
        self.__dict__["_SetFormatID"] = _raise_uninitialized_error
        self.__dict__["_GetName"] = _raise_uninitialized_error
        self.__dict__["_SetName"] = _raise_uninitialized_error
        self.__dict__["_AddFileExtension"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgAsEphemFileReaderPluginResultReg._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgAsEphemFileReaderPluginResultReg from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgAsEphemFileReaderPluginResultReg = agcom.GUID(IAgAsEphemFileReaderPluginResultReg._uuid)
        vtable_offset_local = IAgAsEphemFileReaderPluginResultReg._vtable_offset - 1
        self.__dict__["_GetFormatID"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultReg, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_SetFormatID"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultReg, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_GetName"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultReg, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_SetName"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultReg, vtable_offset_local+4, agcom.BSTR)
        self.__dict__["_AddFileExtension"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultReg, vtable_offset_local+5, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsEphemFileReaderPluginResultReg.__dict__ and type(IAgAsEphemFileReaderPluginResultReg.__dict__[attrname]) == property:
            return IAgAsEphemFileReaderPluginResultReg.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgAsEphemFileReaderPluginResultReg.")
    
    @property
    def FormatID(self) -> str:
        """File Format identification. Cannot contain spaces."""
        with agmarshall.BSTR_arg() as arg_pFormatID:
            agcls.evaluate_hresult(self.__dict__["_GetFormatID"](byref(arg_pFormatID.COM_val)))
            return arg_pFormatID.python_val

    @FormatID.setter
    def FormatID(self, formatID:str) -> None:
        """File Format identification. Cannot contain spaces."""
        with agmarshall.BSTR_arg(formatID) as arg_formatID:
            agcls.evaluate_hresult(self.__dict__["_SetFormatID"](arg_formatID.COM_val))

    @property
    def Name(self) -> str:
        """Name to use in the user interface."""
        with agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__["_GetName"](byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @Name.setter
    def Name(self, name:str) -> None:
        """Name to use in the user interface."""
        with agmarshall.BSTR_arg(name) as arg_name:
            agcls.evaluate_hresult(self.__dict__["_SetName"](arg_name.COM_val))

    def AddFileExtension(self, fileExt:str) -> None:
        """Adds a file extension to associate with this format. For example, .txt, .inp, ...."""
        with agmarshall.BSTR_arg(fileExt) as arg_fileExt:
            agcls.evaluate_hresult(self.__dict__["_AddFileExtension"](arg_fileExt.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{F6A367B8-235A-423d-BBD6-F00486DC1CCB}", IAgAsEphemFileReaderPluginResultReg)
agcls.AgTypeNameMap["IAgAsEphemFileReaderPluginResultReg"] = IAgAsEphemFileReaderPluginResultReg
__all__.append("IAgAsEphemFileReaderPluginResultReg")

class IAgAsEphemFileReaderPluginResultVerify(object):
    """Interface for use with IAgAsEphemFileReaderPlugin"""
    _uuid = "{51F4FB14-83AB-4ce1-9A71-D294701D8BE3}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFilename"] = _raise_uninitialized_error
        self.__dict__["_GetIsValid"] = _raise_uninitialized_error
        self.__dict__["_SetIsValid"] = _raise_uninitialized_error
        self.__dict__["_GetMessage"] = _raise_uninitialized_error
        self.__dict__["_SetMessage"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgAsEphemFileReaderPluginResultVerify._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgAsEphemFileReaderPluginResultVerify from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgAsEphemFileReaderPluginResultVerify = agcom.GUID(IAgAsEphemFileReaderPluginResultVerify._uuid)
        vtable_offset_local = IAgAsEphemFileReaderPluginResultVerify._vtable_offset - 1
        self.__dict__["_GetFilename"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultVerify, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetIsValid"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultVerify, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetIsValid"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultVerify, vtable_offset_local+3, agcom.VARIANT_BOOL)
        self.__dict__["_GetMessage"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultVerify, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_SetMessage"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultVerify, vtable_offset_local+5, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsEphemFileReaderPluginResultVerify.__dict__ and type(IAgAsEphemFileReaderPluginResultVerify.__dict__[attrname]) == property:
            return IAgAsEphemFileReaderPluginResultVerify.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgAsEphemFileReaderPluginResultVerify.")
    
    @property
    def Filename(self) -> str:
        """The filename to verify."""
        with agmarshall.BSTR_arg() as arg_pFilename:
            agcls.evaluate_hresult(self.__dict__["_GetFilename"](byref(arg_pFilename.COM_val)))
            return arg_pFilename.python_val

    @property
    def IsValid(self) -> bool:
        """The result of validating the file. Return true for a valid file, else return false."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__["_GetIsValid"](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val

    @IsValid.setter
    def IsValid(self, isValid:bool) -> None:
        """The result of validating the file. Return true for a valid file, else return false."""
        with agmarshall.VARIANT_BOOL_arg(isValid) as arg_isValid:
            agcls.evaluate_hresult(self.__dict__["_SetIsValid"](arg_isValid.COM_val))

    @property
    def Message(self) -> str:
        """The message of the validation of the file if it has failed."""
        with agmarshall.BSTR_arg() as arg_pMessage:
            agcls.evaluate_hresult(self.__dict__["_GetMessage"](byref(arg_pMessage.COM_val)))
            return arg_pMessage.python_val

    @Message.setter
    def Message(self, message:str) -> None:
        """The message of the validation of the file if it has failed."""
        with agmarshall.BSTR_arg(message) as arg_message:
            agcls.evaluate_hresult(self.__dict__["_SetMessage"](arg_message.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{51F4FB14-83AB-4ce1-9A71-D294701D8BE3}", IAgAsEphemFileReaderPluginResultVerify)
agcls.AgTypeNameMap["IAgAsEphemFileReaderPluginResultVerify"] = IAgAsEphemFileReaderPluginResultVerify
__all__.append("IAgAsEphemFileReaderPluginResultVerify")

class IAgAsEphemFileReaderPluginResultEphem(object):
    """Interface for use with IAgAsEphemFileReaderPlugin"""
    _uuid = "{239441E1-34E6-4826-9056-531B3E45D681}"
    _num_methods = 29
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFormatID"] = _raise_uninitialized_error
        self.__dict__["_GetName"] = _raise_uninitialized_error
        self.__dict__["_GetFilename"] = _raise_uninitialized_error
        self.__dict__["_SetIsValid"] = _raise_uninitialized_error
        self.__dict__["_SetMessage"] = _raise_uninitialized_error
        self.__dict__["_AddMetaData"] = _raise_uninitialized_error
        self.__dict__["_SetCentralBody"] = _raise_uninitialized_error
        self.__dict__["_SetCoordinateSystem"] = _raise_uninitialized_error
        self.__dict__["_SetCoordinateSystemEpoch"] = _raise_uninitialized_error
        self.__dict__["_GetCoordinateSystemEpoch"] = _raise_uninitialized_error
        self.__dict__["_SetInterpolationMethod"] = _raise_uninitialized_error
        self.__dict__["_GetInterpolationMethod"] = _raise_uninitialized_error
        self.__dict__["_SetInterpolationOrder"] = _raise_uninitialized_error
        self.__dict__["_GetInterpolationOrder"] = _raise_uninitialized_error
        self.__dict__["_SetCovarianceRepresentation"] = _raise_uninitialized_error
        self.__dict__["_GetCovarianceRepresentation"] = _raise_uninitialized_error
        self.__dict__["_AddInterpolationBoundary"] = _raise_uninitialized_error
        self.__dict__["_SetRefEpoch"] = _raise_uninitialized_error
        self.__dict__["_GetRefEpoch"] = _raise_uninitialized_error
        self.__dict__["_SetUnits"] = _raise_uninitialized_error
        self.__dict__["_GetDistanceUnit"] = _raise_uninitialized_error
        self.__dict__["_GetTimeUnit"] = _raise_uninitialized_error
        self.__dict__["_SetMuLagrangeVOP"] = _raise_uninitialized_error
        self.__dict__["_GetMuLagrangeVOP"] = _raise_uninitialized_error
        self.__dict__["_AddEphemeris"] = _raise_uninitialized_error
        self.__dict__["_AddEphemerisAtEpoch"] = _raise_uninitialized_error
        self.__dict__["_AddEphemerisOnDate"] = _raise_uninitialized_error
        self.__dict__["_GetCovarianceType"] = _raise_uninitialized_error
        self.__dict__["_AddTrendControlTime"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgAsEphemFileReaderPluginResultEphem._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgAsEphemFileReaderPluginResultEphem from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgAsEphemFileReaderPluginResultEphem = agcom.GUID(IAgAsEphemFileReaderPluginResultEphem._uuid)
        vtable_offset_local = IAgAsEphemFileReaderPluginResultEphem._vtable_offset - 1
        self.__dict__["_GetFormatID"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetName"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetFilename"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_SetIsValid"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+4, agcom.VARIANT_BOOL)
        self.__dict__["_SetMessage"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+5, agcom.BSTR)
        self.__dict__["_AddMetaData"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+6, agcom.BSTR, agcom.BSTR)
        self.__dict__["_SetCentralBody"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+7, agcom.BSTR)
        self.__dict__["_SetCoordinateSystem"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+8, agcom.BSTR)
        self.__dict__["_SetCoordinateSystemEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+9, agcom.BSTR, agcom.BSTR)
        self.__dict__["_GetCoordinateSystemEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+10, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_SetInterpolationMethod"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+11, agcom.LONG)
        self.__dict__["_GetInterpolationMethod"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+12, POINTER(agcom.LONG))
        self.__dict__["_SetInterpolationOrder"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+13, agcom.LONG)
        self.__dict__["_GetInterpolationOrder"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+14, POINTER(agcom.LONG))
        self.__dict__["_SetCovarianceRepresentation"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+15, agcom.LONG)
        self.__dict__["_GetCovarianceRepresentation"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+16, POINTER(agcom.LONG))
        self.__dict__["_AddInterpolationBoundary"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+17, agcom.BSTR, agcom.BSTR)
        self.__dict__["_SetRefEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+18, agcom.BSTR, agcom.BSTR)
        self.__dict__["_GetRefEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+19, agcom.BSTR, POINTER(agcom.BSTR))
        self.__dict__["_SetUnits"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+20, agcom.LONG, agcom.LONG)
        self.__dict__["_GetDistanceUnit"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+21, POINTER(agcom.LONG))
        self.__dict__["_GetTimeUnit"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+22, POINTER(agcom.LONG))
        self.__dict__["_SetMuLagrangeVOP"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+23, agcom.DOUBLE)
        self.__dict__["_GetMuLagrangeVOP"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+24, POINTER(agcom.DOUBLE))
        self.__dict__["_AddEphemeris"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+25, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.SAFEARRAY, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_AddEphemerisAtEpoch"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+26, agcom.BSTR, agcom.BSTR, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.SAFEARRAY, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_AddEphemerisOnDate"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+27, agcom.LONG, agcom.LONG, agcom.LONG, agcom.LONG, agcom.LONG, agcom.LONG, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.SAFEARRAY, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetCovarianceType"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+28, POINTER(agcom.LONG))
        self.__dict__["_AddTrendControlTime"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultEphem, vtable_offset_local+29, agcom.BSTR, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsEphemFileReaderPluginResultEphem.__dict__ and type(IAgAsEphemFileReaderPluginResultEphem.__dict__[attrname]) == property:
            return IAgAsEphemFileReaderPluginResultEphem.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgAsEphemFileReaderPluginResultEphem.")
    
    @property
    def FormatID(self) -> str:
        """File Format identification. Cannot contain spaces."""
        with agmarshall.BSTR_arg() as arg_pFormatID:
            agcls.evaluate_hresult(self.__dict__["_GetFormatID"](byref(arg_pFormatID.COM_val)))
            return arg_pFormatID.python_val

    @property
    def Name(self) -> str:
        """Name to use in the user interface."""
        with agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__["_GetName"](byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def Filename(self) -> str:
        """The filename to verify."""
        with agmarshall.BSTR_arg() as arg_pFilename:
            agcls.evaluate_hresult(self.__dict__["_GetFilename"](byref(arg_pFilename.COM_val)))
            return arg_pFilename.python_val

    @property
    def IsValid(self) -> None:
        """IsValid is a write-only property."""
        raise RuntimeError("IsValid is a write-only property.")


    @IsValid.setter
    def IsValid(self, validity:bool) -> None:
        """False indicates a failure has occurred and that the message should be displayed"""
        with agmarshall.VARIANT_BOOL_arg(validity) as arg_validity:
            agcls.evaluate_hresult(self.__dict__["_SetIsValid"](arg_validity.COM_val))

    @property
    def Message(self) -> None:
        """Message is a write-only property."""
        raise RuntimeError("Message is a write-only property.")


    @Message.setter
    def Message(self, errorMsg:str) -> None:
        """Sets an error message when not valid"""
        with agmarshall.BSTR_arg(errorMsg) as arg_errorMsg:
            agcls.evaluate_hresult(self.__dict__["_SetMessage"](arg_errorMsg.COM_val))

    def AddMetaData(self, keyword:str, value:str) -> None:
        """Associates the Value with the given Keyword"""
        with agmarshall.BSTR_arg(keyword) as arg_keyword, \
             agmarshall.BSTR_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_AddMetaData"](arg_keyword.COM_val, arg_value.COM_val))

    @property
    def CentralBody(self) -> None:
        """CentralBody is a write-only property."""
        raise RuntimeError("CentralBody is a write-only property.")


    @CentralBody.setter
    def CentralBody(self, name:str) -> None:
        """The central body for the coordinate system used for the ephemeris and covariance."""
        with agmarshall.BSTR_arg(name) as arg_name:
            agcls.evaluate_hresult(self.__dict__["_SetCentralBody"](arg_name.COM_val))

    @property
    def CoordinateSystem(self) -> None:
        """CoordinateSystem is a write-only property."""
        raise RuntimeError("CoordinateSystem is a write-only property.")


    @CoordinateSystem.setter
    def CoordinateSystem(self, name:str) -> None:
        """The name of the coordinate system used for the ephemeris and covariance."""
        with agmarshall.BSTR_arg(name) as arg_name:
            agcls.evaluate_hresult(self.__dict__["_SetCoordinateSystem"](arg_name.COM_val))

    def SetCoordinateSystemEpoch(self, dateAbbrv:str, epoch:str) -> None:
        """The coordinate system epoch for the CoordinateSystem, expressed as a string in format given by DateAbbrv. Not needed for systems with fixed epochs (like ICRF, J2000, B1950)."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(epoch) as arg_epoch:
            agcls.evaluate_hresult(self.__dict__["_SetCoordinateSystemEpoch"](arg_dateAbbrv.COM_val, arg_epoch.COM_val))

    def GetCoordinateSystemEpoch(self, dateAbbrv:str) -> str:
        """The coordinate system epoch for the CoordinateSystem, expressed as a string in format given by DateAbbrv. Not needed for systems with fixed epochs (like ICRF, J2000, B1950)."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pEpoch:
            agcls.evaluate_hresult(self.__dict__["_GetCoordinateSystemEpoch"](arg_dateAbbrv.COM_val, byref(arg_pEpoch.COM_val)))
            return arg_pEpoch.python_val

    @property
    def InterpolationMethod(self) -> "AgEAsEphemInterpolationMethod":
        """The interpolation method used with the ephemeris."""
        with agmarshall.AgEnum_arg(AgEAsEphemInterpolationMethod) as arg_pMethod:
            agcls.evaluate_hresult(self.__dict__["_GetInterpolationMethod"](byref(arg_pMethod.COM_val)))
            return arg_pMethod.python_val

    @InterpolationMethod.setter
    def InterpolationMethod(self, method:"AgEAsEphemInterpolationMethod") -> None:
        """The interpolation method used with the ephemeris."""
        with agmarshall.AgEnum_arg(AgEAsEphemInterpolationMethod, method) as arg_method:
            agcls.evaluate_hresult(self.__dict__["_SetInterpolationMethod"](arg_method.COM_val))

    @property
    def InterpolationOrder(self) -> int:
        """The interpolation order to use. For Lagrange-type interpolation, 1+Order samples are used; for Hermitian, (Order+1)/2 samples are used."""
        with agmarshall.LONG_arg() as arg_pOrder:
            agcls.evaluate_hresult(self.__dict__["_GetInterpolationOrder"](byref(arg_pOrder.COM_val)))
            return arg_pOrder.python_val

    @InterpolationOrder.setter
    def InterpolationOrder(self, order:int) -> None:
        """The interpolation order to use. For Lagrange-type interpolation, 1+Order samples are used; for Hermitian, (Order+1)/2 samples are used."""
        with agmarshall.LONG_arg(order) as arg_order:
            agcls.evaluate_hresult(self.__dict__["_SetInterpolationOrder"](arg_order.COM_val))

    @property
    def CovarianceRepresentation(self) -> "AgEAsCovRep":
        """Sets the covariance representation."""
        with agmarshall.AgEnum_arg(AgEAsCovRep) as arg_pCovRep:
            agcls.evaluate_hresult(self.__dict__["_GetCovarianceRepresentation"](byref(arg_pCovRep.COM_val)))
            return arg_pCovRep.python_val

    @CovarianceRepresentation.setter
    def CovarianceRepresentation(self, covRep:"AgEAsCovRep") -> None:
        """Sets the covariance representation."""
        with agmarshall.AgEnum_arg(AgEAsCovRep, covRep) as arg_covRep:
            agcls.evaluate_hresult(self.__dict__["_SetCovarianceRepresentation"](arg_covRep.COM_val))

    def AddInterpolationBoundary(self, dateAbbrv:str, epoch:str) -> None:
        """Adds an interpolation boundary at the Epoch specified in format given by DateAbbrv."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(epoch) as arg_epoch:
            agcls.evaluate_hresult(self.__dict__["_AddInterpolationBoundary"](arg_dateAbbrv.COM_val, arg_epoch.COM_val))

    def SetRefEpoch(self, dateAbbrv:str, epoch:str) -> None:
        """Sets the reference epoch for points added by AddEphemeris(). The Epoch is specified in the format given by DateAbbrv."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(epoch) as arg_epoch:
            agcls.evaluate_hresult(self.__dict__["_SetRefEpoch"](arg_dateAbbrv.COM_val, arg_epoch.COM_val))

    def GetRefEpoch(self, dateAbbrv:str) -> str:
        """Sets the reference epoch for points added by AddEphemeris(). The Epoch is specified in the format given by DateAbbrv."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg() as arg_pEpoch:
            agcls.evaluate_hresult(self.__dict__["_GetRefEpoch"](arg_dateAbbrv.COM_val, byref(arg_pEpoch.COM_val)))
            return arg_pEpoch.python_val

    def SetUnits(self, distUnit:"AgEAsEphemFileDistanceUnit", timeUnit:"AgEAsEphemFileTimeUnit") -> None:
        """Sets the distance and time units used for both ephemeris and covariance."""
        with agmarshall.AgEnum_arg(AgEAsEphemFileDistanceUnit, distUnit) as arg_distUnit, \
             agmarshall.AgEnum_arg(AgEAsEphemFileTimeUnit, timeUnit) as arg_timeUnit:
            agcls.evaluate_hresult(self.__dict__["_SetUnits"](arg_distUnit.COM_val, arg_timeUnit.COM_val))

    def GetDistanceUnit(self) -> "AgEAsEphemFileDistanceUnit":
        """Gets the distance unit used for both ephemeris and covariance."""
        with agmarshall.AgEnum_arg(AgEAsEphemFileDistanceUnit) as arg_pDistUnit:
            agcls.evaluate_hresult(self.__dict__["_GetDistanceUnit"](byref(arg_pDistUnit.COM_val)))
            return arg_pDistUnit.python_val

    def GetTimeUnit(self) -> "AgEAsEphemFileTimeUnit":
        """Gets the distance unit used for both ephemeris and covariance."""
        with agmarshall.AgEnum_arg(AgEAsEphemFileTimeUnit) as arg_pTimeUnit:
            agcls.evaluate_hresult(self.__dict__["_GetTimeUnit"](byref(arg_pTimeUnit.COM_val)))
            return arg_pTimeUnit.python_val

    @property
    def MuLagrangeVOP(self) -> float:
        """The gravitational parameter (expressed using the distance and time units) to use when using LagrangeVOP interpolation."""
        with agmarshall.DOUBLE_arg() as arg_pVopMu:
            agcls.evaluate_hresult(self.__dict__["_GetMuLagrangeVOP"](byref(arg_pVopMu.COM_val)))
            return arg_pVopMu.python_val

    @MuLagrangeVOP.setter
    def MuLagrangeVOP(self, vopMu:float) -> None:
        """The gravitational parameter (expressed using the distance and time units) to use when using LagrangeVOP interpolation."""
        with agmarshall.DOUBLE_arg(vopMu) as arg_vopMu:
            agcls.evaluate_hresult(self.__dict__["_SetMuLagrangeVOP"](arg_vopMu.COM_val))

    def AddEphemeris(self, timeSinceEpoch:float, x:float, y:float, z:float, vx:float, vy:float, vz:float, covArray:list) -> bool:
        """Adds an ephemeris point. Covariance array is optional. It contains the lower triangle of the covariance matrix, either 6 elements for position only, or 21 elements when using pos-vel covariance."""
        with agmarshall.DOUBLE_arg(timeSinceEpoch) as arg_timeSinceEpoch, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.DOUBLE_arg(vx) as arg_vx, \
             agmarshall.DOUBLE_arg(vy) as arg_vy, \
             agmarshall.DOUBLE_arg(vz) as arg_vz, \
             agmarshall.SAFEARRAY_arg(covArray) as arg_covArray, \
             agmarshall.VARIANT_BOOL_arg() as arg_pAdded:
            agcls.evaluate_hresult(self.__dict__["_AddEphemeris"](arg_timeSinceEpoch.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, arg_vx.COM_val, arg_vy.COM_val, arg_vz.COM_val, arg_covArray.COM_val, byref(arg_pAdded.COM_val)))
            return arg_pAdded.python_val

    def AddEphemerisAtEpoch(self, dateAbbrv:str, epoch:str, x:float, y:float, z:float, vx:float, vy:float, vz:float, covArray:list) -> bool:
        """Adds an ephemeris point at the Epoch given in the format DateAbbrv. The Covariance array is optional. It contains the lower triangle of the covariance matrix, either 6 elements for position only, or 21 elements when using pos-vel covariance."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(epoch) as arg_epoch, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.DOUBLE_arg(vx) as arg_vx, \
             agmarshall.DOUBLE_arg(vy) as arg_vy, \
             agmarshall.DOUBLE_arg(vz) as arg_vz, \
             agmarshall.SAFEARRAY_arg(covArray) as arg_covArray, \
             agmarshall.VARIANT_BOOL_arg() as arg_pAdded:
            agcls.evaluate_hresult(self.__dict__["_AddEphemerisAtEpoch"](arg_dateAbbrv.COM_val, arg_epoch.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, arg_vx.COM_val, arg_vy.COM_val, arg_vz.COM_val, arg_covArray.COM_val, byref(arg_pAdded.COM_val)))
            return arg_pAdded.python_val

    def AddEphemerisOnDate(self, scale:"AgEUtTimeScale", year:int, month:int, dayOfMonth:int, hour:int, minute:int, seconds:float, x:float, y:float, z:float, vx:float, vy:float, vz:float, covArray:list) -> bool:
        """Adds an ephemeris point on the date specified. The Covariance array is optional. It contains the lower triangle of the covariance matrix, either 6 elements for position only, or 21 elements when using pos-vel covariance. Year [yyyy], DayOfYear [1-366], Month [1-12], DayOfMonth [1-31], Hour [0-23], Minute [0-59], Seconds [0-60]."""
        with agmarshall.AgEnum_arg(AgEUtTimeScale, scale) as arg_scale, \
             agmarshall.LONG_arg(year) as arg_year, \
             agmarshall.LONG_arg(month) as arg_month, \
             agmarshall.LONG_arg(dayOfMonth) as arg_dayOfMonth, \
             agmarshall.LONG_arg(hour) as arg_hour, \
             agmarshall.LONG_arg(minute) as arg_minute, \
             agmarshall.DOUBLE_arg(seconds) as arg_seconds, \
             agmarshall.DOUBLE_arg(x) as arg_x, \
             agmarshall.DOUBLE_arg(y) as arg_y, \
             agmarshall.DOUBLE_arg(z) as arg_z, \
             agmarshall.DOUBLE_arg(vx) as arg_vx, \
             agmarshall.DOUBLE_arg(vy) as arg_vy, \
             agmarshall.DOUBLE_arg(vz) as arg_vz, \
             agmarshall.SAFEARRAY_arg(covArray) as arg_covArray, \
             agmarshall.VARIANT_BOOL_arg() as arg_pAdded:
            agcls.evaluate_hresult(self.__dict__["_AddEphemerisOnDate"](arg_scale.COM_val, arg_year.COM_val, arg_month.COM_val, arg_dayOfMonth.COM_val, arg_hour.COM_val, arg_minute.COM_val, arg_seconds.COM_val, arg_x.COM_val, arg_y.COM_val, arg_z.COM_val, arg_vx.COM_val, arg_vy.COM_val, arg_vz.COM_val, arg_covArray.COM_val, byref(arg_pAdded.COM_val)))
            return arg_pAdded.python_val

    @property
    def CovarianceType(self) -> "AgEAsCovType":
        """Specifies the type of covariance desired."""
        with agmarshall.AgEnum_arg(AgEAsCovType) as arg_pCovType:
            agcls.evaluate_hresult(self.__dict__["_GetCovarianceType"](byref(arg_pCovType.COM_val)))
            return arg_pCovType.python_val

    def AddTrendControlTime(self, dateAbbrv:str, epoch:str) -> None:
        """Adds a trending control time at the Epoch specified in format given by DateAbbrv."""
        with agmarshall.BSTR_arg(dateAbbrv) as arg_dateAbbrv, \
             agmarshall.BSTR_arg(epoch) as arg_epoch:
            agcls.evaluate_hresult(self.__dict__["_AddTrendControlTime"](arg_dateAbbrv.COM_val, arg_epoch.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{239441E1-34E6-4826-9056-531B3E45D681}", IAgAsEphemFileReaderPluginResultEphem)
agcls.AgTypeNameMap["IAgAsEphemFileReaderPluginResultEphem"] = IAgAsEphemFileReaderPluginResultEphem
__all__.append("IAgAsEphemFileReaderPluginResultEphem")

class IAgAsEphemFileReaderPluginResultData(object):
    """Interface for use with IAgAsEphemFileReaderPlugin"""
    _uuid = "{659FAA5C-5845-430d-B192-E9D096619CAC}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFormatID"] = _raise_uninitialized_error
        self.__dict__["_GetName"] = _raise_uninitialized_error
        self.__dict__["_GetFilename"] = _raise_uninitialized_error
        self.__dict__["_SetIsValid"] = _raise_uninitialized_error
        self.__dict__["_SetMessage"] = _raise_uninitialized_error
        self.__dict__["_AddMetaData"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgAsEphemFileReaderPluginResultData._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgAsEphemFileReaderPluginResultData from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgAsEphemFileReaderPluginResultData = agcom.GUID(IAgAsEphemFileReaderPluginResultData._uuid)
        vtable_offset_local = IAgAsEphemFileReaderPluginResultData._vtable_offset - 1
        self.__dict__["_GetFormatID"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultData, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetName"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultData, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetFilename"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultData, vtable_offset_local+3, POINTER(agcom.BSTR))
        self.__dict__["_SetIsValid"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultData, vtable_offset_local+4, agcom.VARIANT_BOOL)
        self.__dict__["_SetMessage"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultData, vtable_offset_local+5, agcom.BSTR)
        self.__dict__["_AddMetaData"] = IAGFUNCTYPE(pUnk, IID_IAgAsEphemFileReaderPluginResultData, vtable_offset_local+6, agcom.BSTR, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgAsEphemFileReaderPluginResultData.__dict__ and type(IAgAsEphemFileReaderPluginResultData.__dict__[attrname]) == property:
            return IAgAsEphemFileReaderPluginResultData.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgAsEphemFileReaderPluginResultData.")
    
    @property
    def FormatID(self) -> str:
        """File Format identification. Cannot contain spaces."""
        with agmarshall.BSTR_arg() as arg_pFormatID:
            agcls.evaluate_hresult(self.__dict__["_GetFormatID"](byref(arg_pFormatID.COM_val)))
            return arg_pFormatID.python_val

    @property
    def Name(self) -> str:
        """Name to use in the user interface."""
        with agmarshall.BSTR_arg() as arg_pName:
            agcls.evaluate_hresult(self.__dict__["_GetName"](byref(arg_pName.COM_val)))
            return arg_pName.python_val

    @property
    def Filename(self) -> str:
        """The filename to verify."""
        with agmarshall.BSTR_arg() as arg_pFilename:
            agcls.evaluate_hresult(self.__dict__["_GetFilename"](byref(arg_pFilename.COM_val)))
            return arg_pFilename.python_val

    @property
    def IsValid(self) -> None:
        """IsValid is a write-only property."""
        raise RuntimeError("IsValid is a write-only property.")


    @IsValid.setter
    def IsValid(self, validity:bool) -> None:
        """False indicates a failure has occurred and that the message should be displayed"""
        with agmarshall.VARIANT_BOOL_arg(validity) as arg_validity:
            agcls.evaluate_hresult(self.__dict__["_SetIsValid"](arg_validity.COM_val))

    @property
    def Message(self) -> None:
        """Message is a write-only property."""
        raise RuntimeError("Message is a write-only property.")


    @Message.setter
    def Message(self, errorMsg:str) -> None:
        """Sets an error message when not valid"""
        with agmarshall.BSTR_arg(errorMsg) as arg_errorMsg:
            agcls.evaluate_hresult(self.__dict__["_SetMessage"](arg_errorMsg.COM_val))

    def AddMetaData(self, keyword:str, value:str) -> None:
        """Associates the Value with the given Keyword"""
        with agmarshall.BSTR_arg(keyword) as arg_keyword, \
             agmarshall.BSTR_arg(value) as arg_value:
            agcls.evaluate_hresult(self.__dict__["_AddMetaData"](arg_keyword.COM_val, arg_value.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{659FAA5C-5845-430d-B192-E9D096619CAC}", IAgAsEphemFileReaderPluginResultData)
agcls.AgTypeNameMap["IAgAsEphemFileReaderPluginResultData"] = IAgAsEphemFileReaderPluginResultData
__all__.append("IAgAsEphemFileReaderPluginResultData")


class IAgAsEphemFileReaderPlugin(object):
    """
    COM Plugin interface for a External File Reader.
    This interface may be inherited from to assist in development of the plugin.  All methods should be overridden.
    """
    def Init(self, site:"IAgUtPluginSite") -> bool:
        """Triggered on instantiation of the reader."""
        raise STKPluginMethodNotImplementedError("Init was not implemented.")

    def Register(self, result:"IAgAsEphemFileReaderPluginResultReg") -> None:
        """Triggered when the plugin is asked to register its name, format, and file extension associations"""
        raise STKPluginMethodNotImplementedError("Register was not implemented.")

    def Verify(self, result:"IAgAsEphemFileReaderPluginResultVerify") -> None:
        """Triggered when the plugin is asked to verify a file."""
        raise STKPluginMethodNotImplementedError("Verify was not implemented.")

    def ReadEphemeris(self, result:"IAgAsEphemFileReaderPluginResultEphem") -> None:
        """Triggered when the plugin is asked to read a file and obtain its ephemeris"""
        raise STKPluginMethodNotImplementedError("ReadEphemeris was not implemented.")

    def ReadMetaData(self, result:"IAgAsEphemFileReaderPluginResultData") -> None:
        """Triggered when the plugin is asked to read a file and return any meta-data contained in the file"""
        raise STKPluginMethodNotImplementedError("ReadMetaData was not implemented.")

    def Free(self) -> None:
        """Triggered just before the plugin is destroyed."""
        raise STKPluginMethodNotImplementedError("Free was not implemented.")

__all__.append("IAgAsEphemFileReaderPlugin")



class AgAsEphemFileReaderPluginResultReg(IAgAsEphemFileReaderPluginResultReg):
    """Interface for use with IAgAsEphemFileReaderPlugin"""
    def __init__(self, sourceObject=None):
        IAgAsEphemFileReaderPluginResultReg.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgAsEphemFileReaderPluginResultReg._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsEphemFileReaderPluginResultReg._get_property(self, attrname) is not None: found_prop = IAgAsEphemFileReaderPluginResultReg._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgAsEphemFileReaderPluginResultReg.")
        
agcls.AgClassCatalog.add_catalog_entry("{9E573C0F-F41B-4517-AA69-F9D308C6FB46}", AgAsEphemFileReaderPluginResultReg)
__all__.append("AgAsEphemFileReaderPluginResultReg")


class AgAsEphemFileReaderPluginResultVerify(IAgAsEphemFileReaderPluginResultVerify):
    """Interface for use with IAgAsEphemFileReaderPlugin"""
    def __init__(self, sourceObject=None):
        IAgAsEphemFileReaderPluginResultVerify.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgAsEphemFileReaderPluginResultVerify._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsEphemFileReaderPluginResultVerify._get_property(self, attrname) is not None: found_prop = IAgAsEphemFileReaderPluginResultVerify._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgAsEphemFileReaderPluginResultVerify.")
        
agcls.AgClassCatalog.add_catalog_entry("{E50B059B-38F9-43D3-BD45-56DBED598301}", AgAsEphemFileReaderPluginResultVerify)
__all__.append("AgAsEphemFileReaderPluginResultVerify")


class AgAsEphemFileReaderPluginResultEphem(IAgAsEphemFileReaderPluginResultEphem):
    """Interface for use with IAgAsEphemFileReaderPlugin"""
    def __init__(self, sourceObject=None):
        IAgAsEphemFileReaderPluginResultEphem.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgAsEphemFileReaderPluginResultEphem._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsEphemFileReaderPluginResultEphem._get_property(self, attrname) is not None: found_prop = IAgAsEphemFileReaderPluginResultEphem._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgAsEphemFileReaderPluginResultEphem.")
        
agcls.AgClassCatalog.add_catalog_entry("{42A115BD-82D1-4DA1-A5B2-578D8E3132F6}", AgAsEphemFileReaderPluginResultEphem)
__all__.append("AgAsEphemFileReaderPluginResultEphem")


class AgAsEphemFileReaderPluginResultData(IAgAsEphemFileReaderPluginResultData):
    """Interface for use with IAgAsEphemFileReaderPlugin"""
    def __init__(self, sourceObject=None):
        IAgAsEphemFileReaderPluginResultData.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgAsEphemFileReaderPluginResultData._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsEphemFileReaderPluginResultData._get_property(self, attrname) is not None: found_prop = IAgAsEphemFileReaderPluginResultData._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgAsEphemFileReaderPluginResultData.")
        
agcls.AgClassCatalog.add_catalog_entry("{DC324635-1F91-456B-85AE-1249E41ED524}", AgAsEphemFileReaderPluginResultData)
__all__.append("AgAsEphemFileReaderPluginResultData")


class AgAsEphemFileReaderPythonPlugin(IAgAsEphemFileReaderPlugin, IAgUtPluginConfig):
    """The implementation of IAgAsEphemFileReaderPlugin for Python."""
    def __init__(self, sourceObject=None):
        IAgAsEphemFileReaderPlugin.__init__(self, sourceObject)
        IAgUtPluginConfig.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgAsEphemFileReaderPlugin._private_init(self, pUnk)
        IAgUtPluginConfig._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgAsEphemFileReaderPlugin._get_property(self, attrname) is not None: found_prop = IAgAsEphemFileReaderPlugin._get_property(self, attrname)
        if IAgUtPluginConfig._get_property(self, attrname) is not None: found_prop = IAgUtPluginConfig._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgAsEphemFileReaderPythonPlugin.")
        
agcls.AgClassCatalog.add_catalog_entry("{24630EE2-6C38-457A-87C5-CBB881DB1E0F}", AgAsEphemFileReaderPythonPlugin)
__all__.append("AgAsEphemFileReaderPythonPlugin")



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
