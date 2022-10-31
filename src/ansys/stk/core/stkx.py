################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["AgDataObject", "AgDataObjectFiles", "AgDraw2DElemCollection", "AgDraw2DElemRect", "AgDrawElemCollection", "AgDrawElemLine", 
"AgDrawElemRect", "AgEButtonValues", "AgEExecMultiCmdResultAction", "AgEFeatureCodes", "AgEGfxAnalysisMode", "AgEGfxDrawCoords", 
"AgELineStyle", "AgELogMsgDispID", "AgELogMsgType", "AgELoggingMode", "AgEMouseMode", "AgEOLEDropMode", "AgEProgressImageXOrigin", 
"AgEProgressImageYOrigin", "AgEShiftValues", "AgEShowProgressImage", "AgExecCmdResult", "AgExecMultiCmdResult", "AgObjPathCollection", 
"AgPickInfoData", "AgRubberBandPickInfoData", "AgSTKXApplication", "AgSTKXApplicationPartnerAccess", "AgSTKXConControlQuitReceivedEventArgs", 
"AgSTKXSSLCertificateErrorEventArgs", "AgUiAx2DCntrl", "AgUiAxGfxAnalysisCntrl", "AgUiAxVOCntrl", "AgWinProjPos", "IAgDataObject", 
"IAgDataObjectFiles", "IAgDrawElem", "IAgDrawElemCollection", "IAgDrawElemLine", "IAgDrawElemRect", "IAgExecCmdResult", 
"IAgExecMultiCmdResult", "IAgObjPathCollection", "IAgPickInfoData", "IAgRubberBandPickInfoData", "IAgSTKXApplication", "IAgSTKXApplicationPartnerAccess", 
"IAgSTKXConControlQuitReceivedEventArgs", "IAgSTKXSSLCertificateErrorEventArgs", "IAgUiAx2DCntrl", "IAgUiAxGfxAnalysisCntrl", 
"IAgUiAxVOCntrl", "IAgWinProjPos"]

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


from .stkutil import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgELogMsgType(IntEnum):
    """Log message types."""
    # Debugging message.
    eLogMsgDebug = 0,
    # Informational message.
    eLogMsgInfo = 1,
    # Informational message.
    eLogMsgForceInfo = 2,
    # Warning message.
    eLogMsgWarning = 3,
    # Alarm message.
    eLogMsgAlarm = 4

agcls.AgTypeNameMap["AgELogMsgType"] = AgELogMsgType

class AgELogMsgDispID(IntEnum):
    """Log message destination options."""
    # STK displays the message in all the log destination.
    eLogMsgDispAll = -1,
    # STK displays the message in the default log destination.
    eLogMsgDispDefault = 0,
    # STK displays the message in the message window.
    eLogMsgDispMsgWin = 1,
    # STK displays the message in the status bar.
    eLogMsgDispStatusBar = 2

agcls.AgTypeNameMap["AgELogMsgDispID"] = AgELogMsgDispID

class AgELineStyle(IntEnum):
    """Line Style"""
    # Specifies a solid line.
    eSolid = 0,
    # Specifies a dashed line.
    eDashed = 1,
    # Specifies a dotted line.
    eDotted = 2,
    # Dot-dashed line.
    eDotDashed = 3,
    # Specifies a long dashed line.
    eLongDashed = 4,
    # Specifies an alternating dash-dot-dot line.
    eDashDotDotted = 5,
    # Specifies a user configurable medium dashed line.
    eMDash = 6,
    # Specifies a user configurable long dashed line.
    eLDash = 7,
    # Specifies a user configurable small dash-dotted line.
    eSDashDot = 8,
    # Specifies a user configurable medium dash-dotted line.
    eMDashDot = 9,
    # Specifies a user configurable long dash-dotted line.
    eLDashDot = 10,
    # Specifies a user configurable medium followed by small dashed line.
    eMSDash = 11,
    # Specifies a user configurable long followed by small dashed line.
    eLSDash = 12,
    # Specifies a user configurable long followed by medium dashed line.
    eLMDash = 13,
    # Specifies a user configurable medium followed by small dashed line.
    eLMSDash = 14,
    # Specifies a dotted line.
    eDot = 15,
    # Specifies a long dashed line.
    eLongDash = 16,
    # Specifies an alternating dash-dot line.
    eSDash = 17

agcls.AgTypeNameMap["AgELineStyle"] = AgELineStyle

class AgEExecMultiCmdResultAction(IntFlag):
    """Enumeration defines a set of actions when an error occurs while executing a command batch."""
    # Continue executing the remaining commands in the command batch.
    eContinueOnError = 0,
    # Terminate the execution of the command batch but do not throw an exception.
    eStopOnError = 1,
    # Terminate the execution of the command batch and throw an exception.
    eExceptionOnError = 2,
    # Ignore results returned by individual commands. The option must be used in combination with other flags.
    eIgnoreExecCmdResult = 0x8000

agcls.AgTypeNameMap["AgEExecMultiCmdResultAction"] = AgEExecMultiCmdResultAction

class AgEShiftValues(IntEnum):
    """State of the Shift/Ctrl/Alt keys."""
    # The Shift key was pressed.
    eShiftPressed = 1,
    # The Ctrl key was pressed.
    eCtrlPressed = 2,
    # The ALT key was pressed.
    eAltPressed = 4

agcls.AgTypeNameMap["AgEShiftValues"] = AgEShiftValues

class AgEButtonValues(IntEnum):
    """Numeric value of the mouse button pressed."""
    # The left button is pressed.
    eLeftPressed = 1,
    # The right button is pressed.
    eRightPressed = 2,
    # The middle button is pressed.
    eMiddlePressed = 4

agcls.AgTypeNameMap["AgEButtonValues"] = AgEButtonValues

class AgEOLEDropMode(IntEnum):
    """Specifies how to handle OLE drop operations."""
    # None. The control does not accept OLE drops and displays the No Drop cursor.
    eNone = 0,
    # Manual. The control triggers the OLE drop events, allowing the programmer to handle the OLE drop operation in code.
    eManual = 1,
    # Automatic. The control automatically accepts OLE drops if the DataObject object contains data in a format it recognizes. No OLE drag/drop events on the target will occur when OLEDropMode is set to eAutomatic.
    eAutomatic = 2

agcls.AgTypeNameMap["AgEOLEDropMode"] = AgEOLEDropMode

class AgEMouseMode(IntEnum):
    """Mouse modes."""
    # Automatic. The control handles the mouse events and then fires the events to the container for additional processing.
    eMouseModeAutomatic = 0,
    # None. No default action happens on mouse events. Events are fired to the container.
    eMouseModeManual = 1

agcls.AgTypeNameMap["AgEMouseMode"] = AgEMouseMode

class AgELoggingMode(IntEnum):
    """Specifies the state of the log file."""
    # The log file is not created.
    eLogInactive = 0,
    # The log file is created but deleted upon application termination.
    eLogActive = 1,
    # The log file is created and kept even after application is terminated.
    eLogActiveKeepFile = 2

agcls.AgTypeNameMap["AgELoggingMode"] = AgELoggingMode

class AgEGfxAnalysisMode(IntEnum):
    """Specifies the mode of Gfx Analysis Control."""
    # The Solar Panel Tool mode.
    eSolarPanelTool = 1,
    # The Area Tool mode.
    eAreaTool = 2,
    # The Obscuration Tool mode.
    eObscurationTool = 3,
    # The AzElMask Tool mode.
    eAzElMaskTool = 4

agcls.AgTypeNameMap["AgEGfxAnalysisMode"] = AgEGfxAnalysisMode

class AgEGfxDrawCoords(IntEnum):
    """Specifies the draw coordinates for Map Control."""
    # The draw coordinates values in pixels.
    ePixelDrawCoords = 1,
    # The draw coordinates values in screen coordinates.
    eScreenDrawCoords = 2

agcls.AgTypeNameMap["AgEGfxDrawCoords"] = AgEGfxDrawCoords

class AgEShowProgressImage(IntEnum):
    """Specifies to show progress image."""
    # Do not show any progress Image.
    eShowProgressImageNone = 1,
    # Show the default progress image.
    eShowProgressImageDefault = 2,
    # Show the user specified progress image.
    eShowProgressImageUser = 3

agcls.AgTypeNameMap["AgEShowProgressImage"] = AgEShowProgressImage

class AgEFeatureCodes(IntEnum):
    """The enumeration values are used to check availability of a given feature."""
    # The enumeration is used to check whether the engine runtime is available.
    eFeatureCodeEngineRuntime = 1,
    # The enumeration is used to check whether the globe is available.
    eFeatureCodeGlobeControl = 2

agcls.AgTypeNameMap["AgEFeatureCodes"] = AgEFeatureCodes

class AgEProgressImageXOrigin(IntEnum):
    """Specifies to align progress image X origin."""
    # Align progress Image from X left.
    eProgressImageXLeft = 1,
    # Align progress Image from X right.
    eProgressImageXRight = 2,
    # Align progress Image from X center.
    eProgressImageXCenter = 3

agcls.AgTypeNameMap["AgEProgressImageXOrigin"] = AgEProgressImageXOrigin

class AgEProgressImageYOrigin(IntEnum):
    """Specifies to align progress image Y origin."""
    # Align progress Image from Y top.
    eProgressImageYTop = 1,
    # Align progress Image from Y bottom.
    eProgressImageYBottom = 2,
    # Align progress Image from Y center.
    eProgressImageYCenter = 3

agcls.AgTypeNameMap["AgEProgressImageYOrigin"] = AgEProgressImageYOrigin


class IAgSTKXSSLCertificateErrorEventArgs(object):
    """Provides information about an SSL certificate that is expired or invalid."""
    _uuid = "{D0C7ACBC-D1DD-45AE-9582-C7AE5C2E5BEF}"
    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_SetIgnoreError"] = _raise_uninitialized_error
        self.__dict__["_GetIsErrorIgnored"] = _raise_uninitialized_error
        self.__dict__["_SetIgnoreErrorPermanently"] = _raise_uninitialized_error
        self.__dict__["_GetSerialNumber"] = _raise_uninitialized_error
        self.__dict__["_GetIssuer"] = _raise_uninitialized_error
        self.__dict__["_GetSubject"] = _raise_uninitialized_error
        self.__dict__["_GetValidDate"] = _raise_uninitialized_error
        self.__dict__["_GetExpirationDate"] = _raise_uninitialized_error
        self.__dict__["_GetIsExpired"] = _raise_uninitialized_error
        self.__dict__["_GetPEMData"] = _raise_uninitialized_error
        self.__dict__["_GetHandled"] = _raise_uninitialized_error
        self.__dict__["_SetHandled"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSTKXSSLCertificateErrorEventArgs._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSTKXSSLCertificateErrorEventArgs from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSTKXSSLCertificateErrorEventArgs = agcom.GUID(IAgSTKXSSLCertificateErrorEventArgs._uuid)
        vtable_offset_local = IAgSTKXSSLCertificateErrorEventArgs._vtable_offset - 1
        self.__dict__["_SetIgnoreError"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+1, agcom.VARIANT_BOOL)
        self.__dict__["_GetIsErrorIgnored"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetIgnoreErrorPermanently"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+3, agcom.VARIANT_BOOL)
        self.__dict__["_GetSerialNumber"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_GetIssuer"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_GetSubject"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_GetValidDate"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+7, POINTER(agcom.DATE))
        self.__dict__["_GetExpirationDate"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+8, POINTER(agcom.DATE))
        self.__dict__["_GetIsExpired"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+9, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetPEMData"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+10, POINTER(agcom.BSTR))
        self.__dict__["_GetHandled"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+11, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetHandled"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXSSLCertificateErrorEventArgs, vtable_offset_local+12, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSTKXSSLCertificateErrorEventArgs.__dict__ and type(IAgSTKXSSLCertificateErrorEventArgs.__dict__[attrname]) == property:
            return IAgSTKXSSLCertificateErrorEventArgs.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSTKXSSLCertificateErrorEventArgs.")
    
    def SetIgnoreError(self, ignoreError:bool) -> None:
        """Specify True to ignore the certificate error and continue with establishing secure HTTP connection to the remote server."""
        with agmarshall.VARIANT_BOOL_arg(ignoreError) as arg_ignoreError:
            agcls.evaluate_hresult(self.__dict__["_SetIgnoreError"](arg_ignoreError.COM_val))

    @property
    def IsErrorIgnored(self) -> bool:
        """Returns whether the invalid certificate error is ignored."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetIsErrorIgnored"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    def SetIgnoreErrorPermanently(self, ignoreErrorPermanently:bool) -> None:
        """Specify True to ignore the certificate error and add the certificate to the list of trusted certificates."""
        with agmarshall.VARIANT_BOOL_arg(ignoreErrorPermanently) as arg_ignoreErrorPermanently:
            agcls.evaluate_hresult(self.__dict__["_SetIgnoreErrorPermanently"](arg_ignoreErrorPermanently.COM_val))

    @property
    def SerialNumber(self) -> str:
        """Certificate's serial number."""
        with agmarshall.BSTR_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetSerialNumber"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def Issuer(self) -> str:
        """The provider who issued the certificate."""
        with agmarshall.BSTR_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetIssuer"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def Subject(self) -> str:
        """Certificate's subject field."""
        with agmarshall.BSTR_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetSubject"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def ValidDate(self) -> datetime:
        """Certificate's valid date."""
        with agmarshall.DATE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetValidDate"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def ExpirationDate(self) -> datetime:
        """Certificate's expiration date."""
        with agmarshall.DATE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetExpirationDate"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def IsExpired(self) -> bool:
        """Whether the certificate is expired."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetIsExpired"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def PEMData(self) -> str:
        """Certificate's PEM data encoded as base-64."""
        with agmarshall.BSTR_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetPEMData"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def Handled(self) -> bool:
        """Indicates whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetHandled"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @Handled.setter
    def Handled(self, bHandled:bool) -> None:
        """Indicates whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners."""
        with agmarshall.VARIANT_BOOL_arg(bHandled) as arg_bHandled:
            agcls.evaluate_hresult(self.__dict__["_SetHandled"](arg_bHandled.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{D0C7ACBC-D1DD-45AE-9582-C7AE5C2E5BEF}", IAgSTKXSSLCertificateErrorEventArgs)
agcls.AgTypeNameMap["IAgSTKXSSLCertificateErrorEventArgs"] = IAgSTKXSSLCertificateErrorEventArgs

class IAgSTKXConControlQuitReceivedEventArgs(object):
    """Arguments for the OnConControlQuitReceived event."""
    _uuid = "{F8925F99-8841-4DF3-A6E4-CE63E298868C}"
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetAcknowledge"] = _raise_uninitialized_error
        self.__dict__["_SetAcknowledge"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSTKXConControlQuitReceivedEventArgs._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSTKXConControlQuitReceivedEventArgs from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSTKXConControlQuitReceivedEventArgs = agcom.GUID(IAgSTKXConControlQuitReceivedEventArgs._uuid)
        vtable_offset_local = IAgSTKXConControlQuitReceivedEventArgs._vtable_offset - 1
        self.__dict__["_GetAcknowledge"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXConControlQuitReceivedEventArgs, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetAcknowledge"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXConControlQuitReceivedEventArgs, vtable_offset_local+2, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSTKXConControlQuitReceivedEventArgs.__dict__ and type(IAgSTKXConControlQuitReceivedEventArgs.__dict__[attrname]) == property:
            return IAgSTKXConControlQuitReceivedEventArgs.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSTKXConControlQuitReceivedEventArgs.")
    
    @property
    def Acknowledge(self) -> bool:
        """Indicates whether or not to acknowledge the connect command."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetAcknowledge"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @Acknowledge.setter
    def Acknowledge(self, acknowledge:bool) -> None:
        """Indicates whether or not to acknowledge the connect command."""
        with agmarshall.VARIANT_BOOL_arg(acknowledge) as arg_acknowledge:
            agcls.evaluate_hresult(self.__dict__["_SetAcknowledge"](arg_acknowledge.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{F8925F99-8841-4DF3-A6E4-CE63E298868C}", IAgSTKXConControlQuitReceivedEventArgs)
agcls.AgTypeNameMap["IAgSTKXConControlQuitReceivedEventArgs"] = IAgSTKXConControlQuitReceivedEventArgs

class IAgPickInfoData(object):
    """Mouse pick details."""
    _uuid = "{C87F43DA-DD89-4F13-BCB6-D78D0FE8D7E4}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetObjPath"] = _raise_uninitialized_error
        self.__dict__["_GetLat"] = _raise_uninitialized_error
        self.__dict__["_GetLon"] = _raise_uninitialized_error
        self.__dict__["_GetAlt"] = _raise_uninitialized_error
        self.__dict__["_GetIsObjPathValid"] = _raise_uninitialized_error
        self.__dict__["_GetIsLatLonAltValid"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgPickInfoData._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgPickInfoData from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgPickInfoData = agcom.GUID(IAgPickInfoData._uuid)
        vtable_offset_local = IAgPickInfoData._vtable_offset - 1
        self.__dict__["_GetObjPath"] = IAGFUNCTYPE(pUnk, IID_IAgPickInfoData, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_GetLat"] = IAGFUNCTYPE(pUnk, IID_IAgPickInfoData, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__["_GetLon"] = IAGFUNCTYPE(pUnk, IID_IAgPickInfoData, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_GetAlt"] = IAGFUNCTYPE(pUnk, IID_IAgPickInfoData, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_GetIsObjPathValid"] = IAGFUNCTYPE(pUnk, IID_IAgPickInfoData, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetIsLatLonAltValid"] = IAGFUNCTYPE(pUnk, IID_IAgPickInfoData, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgPickInfoData.__dict__ and type(IAgPickInfoData.__dict__[attrname]) == property:
            return IAgPickInfoData.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgPickInfoData.")
    
    @property
    def ObjPath(self) -> str:
        """Path of the STK object picked if any (or empty string)."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetObjPath"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Lat(self) -> float:
        """Latitude of point clicked (if available)."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLat"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Lon(self) -> float:
        """Longitude of point clicked (if available)."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Alt(self) -> float:
        """Altitude of point clicked (if available)."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetAlt"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def IsObjPathValid(self) -> bool:
        """Indicate if the ObjPath property is valid."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__["_GetIsObjPathValid"](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val

    @property
    def IsLatLonAltValid(self) -> bool:
        """Indicate if the Lat/Lon/Alt properties are valid."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__["_GetIsLatLonAltValid"](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val


agcls.AgClassCatalog.add_catalog_entry("{C87F43DA-DD89-4F13-BCB6-D78D0FE8D7E4}", IAgPickInfoData)
agcls.AgTypeNameMap["IAgPickInfoData"] = IAgPickInfoData

class IAgRubberBandPickInfoData(object):
    """Rubber-band mouse pick result."""
    _uuid = "{54417F99-E500-4BD8-A762-DC3367C7624C}"
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetObjPaths"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgRubberBandPickInfoData._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgRubberBandPickInfoData from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgRubberBandPickInfoData = agcom.GUID(IAgRubberBandPickInfoData._uuid)
        vtable_offset_local = IAgRubberBandPickInfoData._vtable_offset - 1
        self.__dict__["_GetObjPaths"] = IAGFUNCTYPE(pUnk, IID_IAgRubberBandPickInfoData, vtable_offset_local+1, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgRubberBandPickInfoData.__dict__ and type(IAgRubberBandPickInfoData.__dict__[attrname]) == property:
            return IAgRubberBandPickInfoData.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgRubberBandPickInfoData.")
    
    @property
    def ObjPaths(self) -> "IAgObjPathCollection":
        """List of object paths selected."""
        with agmarshall.AgInterface_out_arg() as arg_ppColl:
            agcls.evaluate_hresult(self.__dict__["_GetObjPaths"](byref(arg_ppColl.COM_val)))
            return arg_ppColl.python_val


agcls.AgClassCatalog.add_catalog_entry("{54417F99-E500-4BD8-A762-DC3367C7624C}", IAgRubberBandPickInfoData)
agcls.AgTypeNameMap["IAgRubberBandPickInfoData"] = IAgRubberBandPickInfoData

class IAgSTKXApplication(object):
    """STK X Application object."""
    _uuid = "{A2BB8372-EA5F-4D9D-84C3-4D9E5B9A8840}"
    _num_methods = 27
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_ExecuteCommand"] = _raise_uninitialized_error
        self.__dict__["_GetEnableConnect"] = _raise_uninitialized_error
        self.__dict__["_SetEnableConnect"] = _raise_uninitialized_error
        self.__dict__["_GetConnectPort"] = _raise_uninitialized_error
        self.__dict__["_SetConnectPort"] = _raise_uninitialized_error
        self.__dict__["_GetHostID"] = _raise_uninitialized_error
        self.__dict__["_GetRegistrationID"] = _raise_uninitialized_error
        self.__dict__["_GetVersion"] = _raise_uninitialized_error
        self.__dict__["_GetLicensingReport"] = _raise_uninitialized_error
        self.__dict__["_GetVendorID"] = _raise_uninitialized_error
        self.__dict__["_SetVendorID"] = _raise_uninitialized_error
        self.__dict__["_SetOnlineOptions"] = _raise_uninitialized_error
        self.__dict__["_GetOnlineOptions"] = _raise_uninitialized_error
        self.__dict__["_SetConnectHandler"] = _raise_uninitialized_error
        self.__dict__["_GetLogFileFullName"] = _raise_uninitialized_error
        self.__dict__["_GetLoggingMode"] = _raise_uninitialized_error
        self.__dict__["_SetLoggingMode"] = _raise_uninitialized_error
        self.__dict__["_GetConnectMaxConnections"] = _raise_uninitialized_error
        self.__dict__["_SetConnectMaxConnections"] = _raise_uninitialized_error
        self.__dict__["_ExecuteMultipleCommands"] = _raise_uninitialized_error
        self.__dict__["_IsFeatureAvailable"] = _raise_uninitialized_error
        self.__dict__["_GetNoGraphics"] = _raise_uninitialized_error
        self.__dict__["_SetNoGraphics"] = _raise_uninitialized_error
        self.__dict__["_Terminate"] = _raise_uninitialized_error
        self.__dict__["_GetShowSLAIfNotAccepted"] = _raise_uninitialized_error
        self.__dict__["_SetShowSLAIfNotAccepted"] = _raise_uninitialized_error
        self.__dict__["_SetUseHook"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSTKXApplication._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSTKXApplication from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSTKXApplication = agcom.GUID(IAgSTKXApplication._uuid)
        vtable_offset_local = IAgSTKXApplication._vtable_offset - 1
        self.__dict__["_ExecuteCommand"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+1, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_GetEnableConnect"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetEnableConnect"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+3, agcom.VARIANT_BOOL)
        self.__dict__["_GetConnectPort"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+4, POINTER(agcom.SHORT))
        self.__dict__["_SetConnectPort"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+5, agcom.SHORT)
        self.__dict__["_GetHostID"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_GetRegistrationID"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+7, POINTER(agcom.BSTR))
        self.__dict__["_GetVersion"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_GetLicensingReport"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+9, POINTER(agcom.BSTR))
        self.__dict__["_GetVendorID"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+10, POINTER(agcom.BSTR))
        self.__dict__["_SetVendorID"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+11, agcom.BSTR)
        self.__dict__["_SetOnlineOptions"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+12, agcom.VARIANT_BOOL, agcom.BSTR, agcom.LONG, agcom.BSTR, agcom.BSTR, agcom.VARIANT_BOOL, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetOnlineOptions"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+13, POINTER(agcom.VARIANT_BOOL), POINTER(agcom.BSTR), POINTER(agcom.LONG), POINTER(agcom.BSTR), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetConnectHandler"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+14, agcom.BSTR, agcom.BSTR)
        self.__dict__["_GetLogFileFullName"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+15, POINTER(agcom.BSTR))
        self.__dict__["_GetLoggingMode"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+16, POINTER(agcom.LONG))
        self.__dict__["_SetLoggingMode"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+17, agcom.LONG)
        self.__dict__["_GetConnectMaxConnections"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+18, POINTER(agcom.LONG))
        self.__dict__["_SetConnectMaxConnections"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+19, agcom.LONG)
        self.__dict__["_ExecuteMultipleCommands"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+20, POINTER(agcom.SAFEARRAY), agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_IsFeatureAvailable"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+21, agcom.LONG, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetNoGraphics"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+22, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetNoGraphics"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+23, agcom.VARIANT_BOOL)
        self.__dict__["_Terminate"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+24, )
        self.__dict__["_GetShowSLAIfNotAccepted"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+25, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetShowSLAIfNotAccepted"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+26, agcom.VARIANT_BOOL)
        self.__dict__["_SetUseHook"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplication, vtable_offset_local+27, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSTKXApplication.__dict__ and type(IAgSTKXApplication.__dict__[attrname]) == property:
            return IAgSTKXApplication.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSTKXApplication.")
    def Subscribe(self) -> IAgSTKXApplicationEventHandler:
        """Returns an IAgSTKXApplicationEventHandler that is subscribed to handle events associated with this instance of IAgSTKXApplication."""
        return IAgSTKXApplicationEventHandler(self._pUnk)    
    def ExecuteCommand(self, command:str) -> "IAgExecCmdResult":
        """Send a connect command to STK X."""
        with agmarshall.BSTR_arg(command) as arg_command, \
             agmarshall.AgInterface_out_arg() as arg_ppExecCmdRes:
            agcls.evaluate_hresult(self.__dict__["_ExecuteCommand"](arg_command.COM_val, byref(arg_ppExecCmdRes.COM_val)))
            return arg_ppExecCmdRes.python_val

    @property
    def EnableConnect(self) -> bool:
        """Enable or disable TCP/IP connect command processing (default: disabled)."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetEnableConnect"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @EnableConnect.setter
    def EnableConnect(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetEnableConnect"](arg_newVal.COM_val))

    @property
    def ConnectPort(self) -> int:
        """Specify TCP/IP port to be used by Connect (default: 5001)."""
        with agmarshall.SHORT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetConnectPort"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @ConnectPort.setter
    def ConnectPort(self, newVal:int) -> None:
        with agmarshall.SHORT_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetConnectPort"](arg_newVal.COM_val))

    @property
    def HostID(self) -> str:
        """Returns the Host ID."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetHostID"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @property
    def RegistrationID(self) -> str:
        """Returns the Registration ID."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetRegistrationID"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @property
    def Version(self) -> str:
        """Returns the version number"""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetVersion"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    def GetLicensingReport(self) -> str:
        """This method is deprecated. Returns a formatted string that contains the license names and their states. The string is formatted as an XML document."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetLicensingReport"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @property
    def VendorID(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetVendorID"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @VendorID.setter
    def VendorID(self, vendorID:str) -> None:
        with agmarshall.BSTR_arg(vendorID) as arg_vendorID:
            agcls.evaluate_hresult(self.__dict__["_SetVendorID"](arg_vendorID.COM_val))

    def SetOnlineOptions(self, useProxy:bool, serverName:str, portNum:int, userName:str, password:str, savePassword:bool) -> bool:
        """Set http proxy online options"""
        with agmarshall.VARIANT_BOOL_arg(useProxy) as arg_useProxy, \
             agmarshall.BSTR_arg(serverName) as arg_serverName, \
             agmarshall.LONG_arg(portNum) as arg_portNum, \
             agmarshall.BSTR_arg(userName) as arg_userName, \
             agmarshall.BSTR_arg(password) as arg_password, \
             agmarshall.VARIANT_BOOL_arg(savePassword) as arg_savePassword, \
             agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_SetOnlineOptions"](arg_useProxy.COM_val, arg_serverName.COM_val, arg_portNum.COM_val, arg_userName.COM_val, arg_password.COM_val, arg_savePassword.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def GetOnlineOptions(self) -> typing.Tuple[bool, str, int, str, bool]:
        """Get http proxy online options"""
        with agmarshall.VARIANT_BOOL_arg() as arg_useProxy, \
             agmarshall.BSTR_arg() as arg_serverName, \
             agmarshall.LONG_arg() as arg_portNum, \
             agmarshall.BSTR_arg() as arg_userName, \
             agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetOnlineOptions"](byref(arg_useProxy.COM_val), byref(arg_serverName.COM_val), byref(arg_portNum.COM_val), byref(arg_userName.COM_val), byref(arg_pVal.COM_val)))
            return arg_useProxy.python_val, arg_serverName.python_val, arg_portNum.python_val, arg_userName.python_val, arg_pVal.python_val

    def SetConnectHandler(self, commandID:str, progID:str) -> None:
        """Set callback to handle a certain connect command"""
        with agmarshall.BSTR_arg(commandID) as arg_commandID, \
             agmarshall.BSTR_arg(progID) as arg_progID:
            agcls.evaluate_hresult(self.__dict__["_SetConnectHandler"](arg_commandID.COM_val, arg_progID.COM_val))

    @property
    def LogFileFullName(self) -> str:
        """Returns full path and log file name."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetLogFileFullName"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @property
    def LoggingMode(self) -> "AgELoggingMode":
        """Controls the log file generation, and if the log file is deleted or not on application exit."""
        with agmarshall.AgEnum_arg(AgELoggingMode) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLoggingMode"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @LoggingMode.setter
    def LoggingMode(self, newVal:"AgELoggingMode") -> None:
        with agmarshall.AgEnum_arg(AgELoggingMode, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetLoggingMode"](arg_newVal.COM_val))

    @property
    def ConnectMaxConnections(self) -> int:
        """Specify the maximum number of Connect connections to allow."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetConnectMaxConnections"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @ConnectMaxConnections.setter
    def ConnectMaxConnections(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetConnectMaxConnections"](arg_newVal.COM_val))

    def ExecuteMultipleCommands(self, connectCommands:list, eAction:"AgEExecMultiCmdResultAction") -> "IAgExecMultiCmdResult":
        """Executes multiple CONNECT actions. The method throws an exception if any of the specified commands have failed."""
        with agmarshall.SAFEARRAY_arg(connectCommands) as arg_connectCommands, \
             agmarshall.AgEnum_arg(AgEExecMultiCmdResultAction, eAction) as arg_eAction, \
             agmarshall.AgInterface_out_arg() as arg_ppResult:
            agcls.evaluate_hresult(self.__dict__["_ExecuteMultipleCommands"](byref(arg_connectCommands.COM_val), arg_eAction.COM_val, byref(arg_ppResult.COM_val)))
            return arg_ppResult.python_val

    def IsFeatureAvailable(self, featureCode:"AgEFeatureCodes") -> bool:
        """Returns true if the specified feature is available."""
        with agmarshall.AgEnum_arg(AgEFeatureCodes, featureCode) as arg_featureCode, \
             agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_IsFeatureAvailable"](arg_featureCode.COM_val, byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def NoGraphics(self) -> bool:
        """Start engine with or without graphics (default: engine starts with graphics.)."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetNoGraphics"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @NoGraphics.setter
    def NoGraphics(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetNoGraphics"](arg_newVal.COM_val))

    def Terminate(self) -> None:
        """Terminates the use of STK Engine. This must be the last call to STK Engine."""
        agcls.evaluate_hresult(self.__dict__["_Terminate"]())

    @property
    def ShowSLAIfNotAccepted(self) -> bool:
        """Shows the Software License Agreement dialog if not already accepted."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetShowSLAIfNotAccepted"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @ShowSLAIfNotAccepted.setter
    def ShowSLAIfNotAccepted(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetShowSLAIfNotAccepted"](arg_newVal.COM_val))

    @property
    def UseHook(self) -> None:
        """UseHook is a write-only property."""
        raise RuntimeError("UseHook is a write-only property.")


    @UseHook.setter
    def UseHook(self, newVal:bool) -> None:
        """Start engine with or without message hook setup (default: engine starts with message hook setup.)."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUseHook"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{A2BB8372-EA5F-4D9D-84C3-4D9E5B9A8840}", IAgSTKXApplication)
agcls.AgTypeNameMap["IAgSTKXApplication"] = IAgSTKXApplication

class IAgDataObject(object):
    """IAgDataObject is used for OLE drag and drop operations"""
    _uuid = "{557F091D-247F-4040-B1E9-10E5BCEDFFD5}"
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetFiles"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDataObject._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDataObject from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgDataObject = agcom.GUID(IAgDataObject._uuid)
        vtable_offset_local = IAgDataObject._vtable_offset - 1
        self.__dict__["_GetFiles"] = IAGFUNCTYPE(pUnk, IID_IAgDataObject, vtable_offset_local+1, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDataObject.__dict__ and type(IAgDataObject.__dict__[attrname]) == property:
            return IAgDataObject.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgDataObject.")
    
    @property
    def Files(self) -> "IAgDataObjectFiles":
        """Returns a collection of filenames."""
        with agmarshall.AgInterface_out_arg() as arg_pFile:
            agcls.evaluate_hresult(self.__dict__["_GetFiles"](byref(arg_pFile.COM_val)))
            return arg_pFile.python_val


agcls.AgClassCatalog.add_catalog_entry("{557F091D-247F-4040-B1E9-10E5BCEDFFD5}", IAgDataObject)
agcls.AgTypeNameMap["IAgDataObject"] = IAgDataObject

class IAgObjPathCollection(object):
    """Collection of object paths."""
    _uuid = "{831E53E8-4E79-4E2E-B289-A6AD76A76F3A}"
    _num_methods = 4
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_Range"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgObjPathCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgObjPathCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgObjPathCollection = agcom.GUID(IAgObjPathCollection._uuid)
        vtable_offset_local = IAgObjPathCollection._vtable_offset - 1
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgObjPathCollection, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgObjPathCollection, vtable_offset_local+2, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgObjPathCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_Range"] = IAGFUNCTYPE(pUnk, IID_IAgObjPathCollection, vtable_offset_local+4, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgObjPathCollection.__dict__ and type(IAgObjPathCollection.__dict__[attrname]) == property:
            return IAgObjPathCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgObjPathCollection.")
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
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def Item(self, index:int) -> str:
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pItem:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pItem.COM_val)))
            return arg_pItem.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the object paths in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    def Range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        with agmarshall.LONG_arg(startIndex) as arg_startIndex, \
             agmarshall.LONG_arg(stopIndex) as arg_stopIndex, \
             agmarshall.SAFEARRAY_arg() as arg_pVar:
            agcls.evaluate_hresult(self.__dict__["_Range"](arg_startIndex.COM_val, arg_stopIndex.COM_val, byref(arg_pVar.COM_val)))
            return arg_pVar.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{831E53E8-4E79-4E2E-B289-A6AD76A76F3A}", IAgObjPathCollection)
agcls.AgTypeNameMap["IAgObjPathCollection"] = IAgObjPathCollection

class IAgDrawElem(object):
    """Draw element."""
    _uuid = "{C661025D-FFB3-429A-A0B1-D8421DE76AC6}"
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetVisible"] = _raise_uninitialized_error
        self.__dict__["_SetVisible"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDrawElem._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDrawElem from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgDrawElem = agcom.GUID(IAgDrawElem._uuid)
        vtable_offset_local = IAgDrawElem._vtable_offset - 1
        self.__dict__["_GetVisible"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElem, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetVisible"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElem, vtable_offset_local+2, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDrawElem.__dict__ and type(IAgDrawElem.__dict__[attrname]) == property:
            return IAgDrawElem.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgDrawElem.")
    
    @property
    def Visible(self) -> bool:
        """Show or hide the element."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetVisible"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Visible.setter
    def Visible(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetVisible"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{C661025D-FFB3-429A-A0B1-D8421DE76AC6}", IAgDrawElem)
agcls.AgTypeNameMap["IAgDrawElem"] = IAgDrawElem

class IAgDrawElemRect(IAgDrawElem):
    """Defines a rectangle in control coordinates."""
    _uuid = "{B017EED9-DC32-4865-BDB9-6C586DC1818C}"
    _num_methods = 11
    _vtable_offset = IAgDrawElem._vtable_offset + IAgDrawElem._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetLeft"] = _raise_uninitialized_error
        self.__dict__["_GetRight"] = _raise_uninitialized_error
        self.__dict__["_GetTop"] = _raise_uninitialized_error
        self.__dict__["_GetBottom"] = _raise_uninitialized_error
        self.__dict__["_Set"] = _raise_uninitialized_error
        self.__dict__["_GetColor"] = _raise_uninitialized_error
        self.__dict__["_SetColor"] = _raise_uninitialized_error
        self.__dict__["_GetLineWidth"] = _raise_uninitialized_error
        self.__dict__["_SetLineWidth"] = _raise_uninitialized_error
        self.__dict__["_GetLineStyle"] = _raise_uninitialized_error
        self.__dict__["_SetLineStyle"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDrawElemRect._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDrawElemRect from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDrawElem._private_init(self, pUnk)
        IID_IAgDrawElemRect = agcom.GUID(IAgDrawElemRect._uuid)
        vtable_offset_local = IAgDrawElemRect._vtable_offset - 1
        self.__dict__["_GetLeft"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+1, POINTER(agcom.OLE_XPOS_PIXELS))
        self.__dict__["_GetRight"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+2, POINTER(agcom.OLE_XPOS_PIXELS))
        self.__dict__["_GetTop"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+3, POINTER(agcom.OLE_YPOS_PIXELS))
        self.__dict__["_GetBottom"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+4, POINTER(agcom.OLE_YPOS_PIXELS))
        self.__dict__["_Set"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+5, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS)
        self.__dict__["_GetColor"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+6, POINTER(agcom.OLE_COLOR))
        self.__dict__["_SetColor"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+7, agcom.OLE_COLOR)
        self.__dict__["_GetLineWidth"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+8, POINTER(agcom.FLOAT))
        self.__dict__["_SetLineWidth"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+9, agcom.FLOAT)
        self.__dict__["_GetLineStyle"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_SetLineStyle"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemRect, vtable_offset_local+11, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDrawElemRect.__dict__ and type(IAgDrawElemRect.__dict__[attrname]) == property:
            return IAgDrawElemRect.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgDrawElem.__setattr__(self, attrname, value)
    
    @property
    def Left(self) -> int:
        """The x-coordinate of the left edge of this rectangle."""
        with agmarshall.OLE_XPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLeft"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Right(self) -> int:
        """The x-coordinate of the right edge of this rectangle."""
        with agmarshall.OLE_XPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetRight"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Top(self) -> int:
        """The y-coordinate of the top edge of this rectangle."""
        with agmarshall.OLE_YPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetTop"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Bottom(self) -> int:
        """The y-coordinate of the bottom edge of this rectangle."""
        with agmarshall.OLE_YPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetBottom"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def Set(self, left:int, top:int, right:int, bottom:int) -> None:
        """Set the rectangle coordinates."""
        with agmarshall.OLE_XPOS_PIXELS_arg(left) as arg_left, \
             agmarshall.OLE_YPOS_PIXELS_arg(top) as arg_top, \
             agmarshall.OLE_XPOS_PIXELS_arg(right) as arg_right, \
             agmarshall.OLE_YPOS_PIXELS_arg(bottom) as arg_bottom:
            agcls.evaluate_hresult(self.__dict__["_Set"](arg_left.COM_val, arg_top.COM_val, arg_right.COM_val, arg_bottom.COM_val))

    @property
    def Color(self) -> agcolor.Color:
        """Color of the rectangle."""
        with agmarshall.OLE_COLOR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetColor"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Color.setter
    def Color(self, newVal:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetColor"](arg_newVal.COM_val))

    @property
    def LineWidth(self) -> float:
        """Specifies the width of the line."""
        with agmarshall.FLOAT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLineWidth"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @LineWidth.setter
    def LineWidth(self, newVal:float) -> None:
        with agmarshall.FLOAT_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetLineWidth"](arg_newVal.COM_val))

    @property
    def LineStyle(self) -> "AgELineStyle":
        """Specifies the style of the line."""
        with agmarshall.AgEnum_arg(AgELineStyle) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLineStyle"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @LineStyle.setter
    def LineStyle(self, newVal:"AgELineStyle") -> None:
        with agmarshall.AgEnum_arg(AgELineStyle, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetLineStyle"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{B017EED9-DC32-4865-BDB9-6C586DC1818C}", IAgDrawElemRect)
agcls.AgTypeNameMap["IAgDrawElemRect"] = IAgDrawElemRect

class IAgDrawElemCollection(object):
    """Collection of elements to draw on the control."""
    _uuid = "{3D6D784D-7C84-4A30-95D8-7D57AF7C560E}"
    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_Clear"] = _raise_uninitialized_error
        self.__dict__["_Add"] = _raise_uninitialized_error
        self.__dict__["_Remove"] = _raise_uninitialized_error
        self.__dict__["_GetVisible"] = _raise_uninitialized_error
        self.__dict__["_SetVisible"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDrawElemCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDrawElemCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgDrawElemCollection = agcom.GUID(IAgDrawElemCollection._uuid)
        vtable_offset_local = IAgDrawElemCollection._vtable_offset - 1
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemCollection, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemCollection, vtable_offset_local+2, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_Clear"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemCollection, vtable_offset_local+4, )
        self.__dict__["_Add"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemCollection, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_Remove"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemCollection, vtable_offset_local+6, agcom.PVOID)
        self.__dict__["_GetVisible"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemCollection, vtable_offset_local+7, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetVisible"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemCollection, vtable_offset_local+8, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDrawElemCollection.__dict__ and type(IAgDrawElemCollection.__dict__[attrname]) == property:
            return IAgDrawElemCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgDrawElemCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgDrawElem":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    @property
    def Count(self) -> int:
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def Item(self, index:int) -> "IAgDrawElem":
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the strings in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppUnk:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppUnk.COM_val)))
            return arg_ppUnk.python_val

    def Clear(self) -> None:
        """Clears the contents of the collection and updates the display."""
        agcls.evaluate_hresult(self.__dict__["_Clear"]())

    def Add(self, elemType:str) -> "IAgDrawElem":
        """Factory to create and add a new element to the end of the sequence."""
        with agmarshall.BSTR_arg(elemType) as arg_elemType, \
             agmarshall.AgInterface_out_arg() as arg_ppDrawElem:
            agcls.evaluate_hresult(self.__dict__["_Add"](arg_elemType.COM_val, byref(arg_ppDrawElem.COM_val)))
            return arg_ppDrawElem.python_val

    def Remove(self, drawElem:"IAgDrawElem") -> None:
        """Remove the specified element."""
        with agmarshall.AgInterface_in_arg(drawElem, IAgDrawElem) as arg_drawElem:
            agcls.evaluate_hresult(self.__dict__["_Remove"](arg_drawElem.COM_val))

    @property
    def Visible(self) -> bool:
        """Show or hide all the elements."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetVisible"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Visible.setter
    def Visible(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetVisible"](arg_newVal.COM_val))

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{3D6D784D-7C84-4A30-95D8-7D57AF7C560E}", IAgDrawElemCollection)
agcls.AgTypeNameMap["IAgDrawElemCollection"] = IAgDrawElemCollection

class IAgWinProjPos(object):
    """Projected window position detail."""
    _uuid = "{56FF29E4-6311-4E94-B91D-53C02288C55A}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetXPos"] = _raise_uninitialized_error
        self.__dict__["_GetYPos"] = _raise_uninitialized_error
        self.__dict__["_GetIsWinProjPosValid"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgWinProjPos._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgWinProjPos from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgWinProjPos = agcom.GUID(IAgWinProjPos._uuid)
        vtable_offset_local = IAgWinProjPos._vtable_offset - 1
        self.__dict__["_GetXPos"] = IAGFUNCTYPE(pUnk, IID_IAgWinProjPos, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_GetYPos"] = IAGFUNCTYPE(pUnk, IID_IAgWinProjPos, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__["_GetIsWinProjPosValid"] = IAGFUNCTYPE(pUnk, IID_IAgWinProjPos, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgWinProjPos.__dict__ and type(IAgWinProjPos.__dict__[attrname]) == property:
            return IAgWinProjPos.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgWinProjPos.")
    
    @property
    def XPos(self) -> float:
        """Projected window X position."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetXPos"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def YPos(self) -> float:
        """Projected window Y position."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetYPos"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def IsWinProjPosValid(self) -> bool:
        """Indicates if the returned projected position is valid or not."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__["_GetIsWinProjPosValid"](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val


agcls.AgClassCatalog.add_catalog_entry("{56FF29E4-6311-4E94-B91D-53C02288C55A}", IAgWinProjPos)
agcls.AgTypeNameMap["IAgWinProjPos"] = IAgWinProjPos

class IAgDrawElemLine(IAgDrawElem):
    """Defines a line in control coordinates."""
    _uuid = "{1A550DDC-7769-4A6C-9D0C-8E9D8C1757E2}"
    _num_methods = 11
    _vtable_offset = IAgDrawElem._vtable_offset + IAgDrawElem._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetLeft"] = _raise_uninitialized_error
        self.__dict__["_GetRight"] = _raise_uninitialized_error
        self.__dict__["_GetTop"] = _raise_uninitialized_error
        self.__dict__["_GetBottom"] = _raise_uninitialized_error
        self.__dict__["_Set"] = _raise_uninitialized_error
        self.__dict__["_GetColor"] = _raise_uninitialized_error
        self.__dict__["_SetColor"] = _raise_uninitialized_error
        self.__dict__["_GetLineWidth"] = _raise_uninitialized_error
        self.__dict__["_SetLineWidth"] = _raise_uninitialized_error
        self.__dict__["_GetLineStyle"] = _raise_uninitialized_error
        self.__dict__["_SetLineStyle"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDrawElemLine._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDrawElemLine from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDrawElem._private_init(self, pUnk)
        IID_IAgDrawElemLine = agcom.GUID(IAgDrawElemLine._uuid)
        vtable_offset_local = IAgDrawElemLine._vtable_offset - 1
        self.__dict__["_GetLeft"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+1, POINTER(agcom.OLE_XPOS_PIXELS))
        self.__dict__["_GetRight"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+2, POINTER(agcom.OLE_XPOS_PIXELS))
        self.__dict__["_GetTop"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+3, POINTER(agcom.OLE_YPOS_PIXELS))
        self.__dict__["_GetBottom"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+4, POINTER(agcom.OLE_YPOS_PIXELS))
        self.__dict__["_Set"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+5, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS)
        self.__dict__["_GetColor"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+6, POINTER(agcom.OLE_COLOR))
        self.__dict__["_SetColor"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+7, agcom.OLE_COLOR)
        self.__dict__["_GetLineWidth"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+8, POINTER(agcom.FLOAT))
        self.__dict__["_SetLineWidth"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+9, agcom.FLOAT)
        self.__dict__["_GetLineStyle"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_SetLineStyle"] = IAGFUNCTYPE(pUnk, IID_IAgDrawElemLine, vtable_offset_local+11, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDrawElemLine.__dict__ and type(IAgDrawElemLine.__dict__[attrname]) == property:
            return IAgDrawElemLine.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IAgDrawElem.__setattr__(self, attrname, value)
    
    @property
    def Left(self) -> int:
        """The x-coordinate of the left edge of this line."""
        with agmarshall.OLE_XPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLeft"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Right(self) -> int:
        """The x-coordinate of the right edge of this line."""
        with agmarshall.OLE_XPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetRight"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Top(self) -> int:
        """The y-coordinate of the top edge of this line."""
        with agmarshall.OLE_YPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetTop"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Bottom(self) -> int:
        """The y-coordinate of the bottom edge of this line."""
        with agmarshall.OLE_YPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetBottom"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def Set(self, left:int, top:int, right:int, bottom:int) -> None:
        """Set the rectangle coordinates."""
        with agmarshall.OLE_XPOS_PIXELS_arg(left) as arg_left, \
             agmarshall.OLE_YPOS_PIXELS_arg(top) as arg_top, \
             agmarshall.OLE_XPOS_PIXELS_arg(right) as arg_right, \
             agmarshall.OLE_YPOS_PIXELS_arg(bottom) as arg_bottom:
            agcls.evaluate_hresult(self.__dict__["_Set"](arg_left.COM_val, arg_top.COM_val, arg_right.COM_val, arg_bottom.COM_val))

    @property
    def Color(self) -> agcolor.Color:
        """Color of the rectangle."""
        with agmarshall.OLE_COLOR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetColor"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Color.setter
    def Color(self, newVal:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetColor"](arg_newVal.COM_val))

    @property
    def LineWidth(self) -> float:
        """Specifies the width of the line."""
        with agmarshall.FLOAT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLineWidth"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @LineWidth.setter
    def LineWidth(self, newVal:float) -> None:
        with agmarshall.FLOAT_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetLineWidth"](arg_newVal.COM_val))

    @property
    def LineStyle(self) -> "AgELineStyle":
        """Specifies the style of the line."""
        with agmarshall.AgEnum_arg(AgELineStyle) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLineStyle"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @LineStyle.setter
    def LineStyle(self, newVal:"AgELineStyle") -> None:
        with agmarshall.AgEnum_arg(AgELineStyle, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetLineStyle"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{1A550DDC-7769-4A6C-9D0C-8E9D8C1757E2}", IAgDrawElemLine)
agcls.AgTypeNameMap["IAgDrawElemLine"] = IAgDrawElemLine

class IAgExecCmdResult(object):
    """Collection of strings returned by the ExecuteCommand."""
    _uuid = "{90EF2D03-F064-4F54-9E02-6E34E3CF5D55}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_Range"] = _raise_uninitialized_error
        self.__dict__["_GetIsSucceeded"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgExecCmdResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgExecCmdResult from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgExecCmdResult = agcom.GUID(IAgExecCmdResult._uuid)
        vtable_offset_local = IAgExecCmdResult._vtable_offset - 1
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_Range"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+4, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_GetIsSucceeded"] = IAGFUNCTYPE(pUnk, IID_IAgExecCmdResult, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgExecCmdResult.__dict__ and type(IAgExecCmdResult.__dict__[attrname]) == property:
            return IAgExecCmdResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgExecCmdResult.")
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
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def Item(self, index:int) -> str:
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pItem:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pItem.COM_val)))
            return arg_pItem.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the strings in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    def Range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        with agmarshall.LONG_arg(startIndex) as arg_startIndex, \
             agmarshall.LONG_arg(stopIndex) as arg_stopIndex, \
             agmarshall.SAFEARRAY_arg() as arg_ppVar:
            agcls.evaluate_hresult(self.__dict__["_Range"](arg_startIndex.COM_val, arg_stopIndex.COM_val, byref(arg_ppVar.COM_val)))
            return arg_ppVar.python_val

    @property
    def IsSucceeded(self) -> bool:
        """Indicates whether the object contains valid results."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetIsSucceeded"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{90EF2D03-F064-4F54-9E02-6E34E3CF5D55}", IAgExecCmdResult)
agcls.AgTypeNameMap["IAgExecCmdResult"] = IAgExecCmdResult

class IAgExecMultiCmdResult(object):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    _uuid = "{0558BE8E-AF66-4F52-9C6D-76962FC52577}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgExecMultiCmdResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgExecMultiCmdResult from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgExecMultiCmdResult = agcom.GUID(IAgExecMultiCmdResult._uuid)
        vtable_offset_local = IAgExecMultiCmdResult._vtable_offset - 1
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgExecMultiCmdResult, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgExecMultiCmdResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgExecMultiCmdResult, vtable_offset_local+3, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgExecMultiCmdResult.__dict__ and type(IAgExecMultiCmdResult.__dict__[attrname]) == property:
            return IAgExecMultiCmdResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgExecMultiCmdResult.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgExecCmdResult":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    @property
    def Count(self) -> int:
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def Item(self, index:int) -> "IAgExecCmdResult":
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the objects in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{0558BE8E-AF66-4F52-9C6D-76962FC52577}", IAgExecMultiCmdResult)
agcls.AgTypeNameMap["IAgExecMultiCmdResult"] = IAgExecMultiCmdResult

class IAgUiAxVOCntrl(object):
    """AGI Globe control."""
    _uuid = "{0975BA23-E273-4B8F-BA8D-32ECB328C092}"
    _num_methods = 48
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetBackColor"] = _raise_uninitialized_error
        self.__dict__["_SetBackColor"] = _raise_uninitialized_error
        self.__dict__["_GetPicture"] = _raise_uninitialized_error
        self.__dict__["_PicturePutRef"] = _raise_uninitialized_error
        self.__dict__["_SetPicture"] = _raise_uninitialized_error
        self.__dict__["_PickInfo"] = _raise_uninitialized_error
        self.__dict__["_GetWinID"] = _raise_uninitialized_error
        self.__dict__["_SetWinID"] = _raise_uninitialized_error
        self.__dict__["_GetApplication"] = _raise_uninitialized_error
        self.__dict__["_ZoomIn"] = _raise_uninitialized_error
        self.__dict__["_GetNoLogo"] = _raise_uninitialized_error
        self.__dict__["_SetNoLogo"] = _raise_uninitialized_error
        self.__dict__["_GetOLEDropMode"] = _raise_uninitialized_error
        self.__dict__["_SetOLEDropMode"] = _raise_uninitialized_error
        self.__dict__["_GetVendorID"] = _raise_uninitialized_error
        self.__dict__["_SetVendorID"] = _raise_uninitialized_error
        self.__dict__["_RubberBandPickInfo"] = _raise_uninitialized_error
        self.__dict__["_GetMouseMode"] = _raise_uninitialized_error
        self.__dict__["_SetMouseMode"] = _raise_uninitialized_error
        self.__dict__["_GetDrawElements"] = _raise_uninitialized_error
        self.__dict__["_GetReadyState"] = _raise_uninitialized_error
        self.__dict__["_GetPptPreloadMode"] = _raise_uninitialized_error
        self.__dict__["_SetPptPreloadMode"] = _raise_uninitialized_error
        self.__dict__["_GetAdvancedPickMode"] = _raise_uninitialized_error
        self.__dict__["_SetAdvancedPickMode"] = _raise_uninitialized_error
        self.__dict__["_CopyFromWinID"] = _raise_uninitialized_error
        self.__dict__["_StartObjectEditing"] = _raise_uninitialized_error
        self.__dict__["_ApplyObjectEditing"] = _raise_uninitialized_error
        self.__dict__["_StopObjectEditing"] = _raise_uninitialized_error
        self.__dict__["_GetIsObjectEditing"] = _raise_uninitialized_error
        self.__dict__["_GetInZoomMode"] = _raise_uninitialized_error
        self.__dict__["_SetMouseCursorFromFile"] = _raise_uninitialized_error
        self.__dict__["_RestoreMouseCursor"] = _raise_uninitialized_error
        self.__dict__["_SetMouseCursorFromHandle"] = _raise_uninitialized_error
        self.__dict__["_GetShowProgressImage"] = _raise_uninitialized_error
        self.__dict__["_SetShowProgressImage"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageXOffset"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageXOffset"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageYOffset"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageYOffset"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageFile"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageFile"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageXOrigin"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageXOrigin"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageYOrigin"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageYOrigin"] = _raise_uninitialized_error
        self.__dict__["_GetPictureFromFile"] = _raise_uninitialized_error
        self.__dict__["_SetPictureFromFile"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiAxVOCntrl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiAxVOCntrl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiAxVOCntrl = agcom.GUID(IAgUiAxVOCntrl._uuid)
        vtable_offset_local = IAgUiAxVOCntrl._vtable_offset - 1
        self.__dict__["_GetBackColor"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+1, POINTER(agcom.OLE_COLOR))
        self.__dict__["_SetBackColor"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+2, agcom.OLE_COLOR)
        self.__dict__["_GetPicture"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_PicturePutRef"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+4, POINTER(agcom.PVOID))
        self.__dict__["_SetPicture"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+5, POINTER(agcom.PVOID))
        self.__dict__["_PickInfo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+6, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID))
        self.__dict__["_GetWinID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+7, POINTER(agcom.LONG))
        self.__dict__["_SetWinID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+8, agcom.LONG)
        self.__dict__["_GetApplication"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+9, POINTER(agcom.PVOID))
        self.__dict__["_ZoomIn"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+10, )
        self.__dict__["_GetNoLogo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+11, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetNoLogo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+12, agcom.VARIANT_BOOL)
        self.__dict__["_GetOLEDropMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+13, POINTER(agcom.LONG))
        self.__dict__["_SetOLEDropMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+14, agcom.LONG)
        self.__dict__["_GetVendorID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+15, POINTER(agcom.BSTR))
        self.__dict__["_SetVendorID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+16, agcom.BSTR)
        self.__dict__["_RubberBandPickInfo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+17, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID))
        self.__dict__["_GetMouseMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+18, POINTER(agcom.LONG))
        self.__dict__["_SetMouseMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+19, agcom.LONG)
        self.__dict__["_GetDrawElements"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+20, POINTER(agcom.PVOID))
        self.__dict__["_GetReadyState"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+21, POINTER(agcom.LONG))
        self.__dict__["_GetPptPreloadMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+22, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetPptPreloadMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+23, agcom.VARIANT_BOOL)
        self.__dict__["_GetAdvancedPickMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+24, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetAdvancedPickMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+25, agcom.VARIANT_BOOL)
        self.__dict__["_CopyFromWinID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+26, agcom.LONG)
        self.__dict__["_StartObjectEditing"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+27, agcom.BSTR)
        self.__dict__["_ApplyObjectEditing"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+28, )
        self.__dict__["_StopObjectEditing"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+29, agcom.VARIANT_BOOL)
        self.__dict__["_GetIsObjectEditing"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+30, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetInZoomMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+31, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetMouseCursorFromFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+32, agcom.BSTR)
        self.__dict__["_RestoreMouseCursor"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+33, )
        self.__dict__["_SetMouseCursorFromHandle"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+34, agcom.OLE_HANDLE)
        self.__dict__["_GetShowProgressImage"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+35, POINTER(agcom.LONG))
        self.__dict__["_SetShowProgressImage"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+36, agcom.LONG)
        self.__dict__["_GetProgressImageXOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+37, POINTER(agcom.LONG))
        self.__dict__["_SetProgressImageXOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+38, agcom.LONG)
        self.__dict__["_GetProgressImageYOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+39, POINTER(agcom.LONG))
        self.__dict__["_SetProgressImageYOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+40, agcom.LONG)
        self.__dict__["_GetProgressImageFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+41, POINTER(agcom.BSTR))
        self.__dict__["_SetProgressImageFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+42, agcom.BSTR)
        self.__dict__["_GetProgressImageXOrigin"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+43, POINTER(agcom.LONG))
        self.__dict__["_SetProgressImageXOrigin"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+44, agcom.LONG)
        self.__dict__["_GetProgressImageYOrigin"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+45, POINTER(agcom.LONG))
        self.__dict__["_SetProgressImageYOrigin"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+46, agcom.LONG)
        self.__dict__["_GetPictureFromFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+47, POINTER(agcom.BSTR))
        self.__dict__["_SetPictureFromFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxVOCntrl, vtable_offset_local+48, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiAxVOCntrl.__dict__ and type(IAgUiAxVOCntrl.__dict__[attrname]) == property:
            return IAgUiAxVOCntrl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiAxVOCntrl.")
    def Subscribe(self) -> IAgUiAxVOCntrlEventHandler:
        """Returns an IAgUiAxVOCntrlEventHandler that is subscribed to handle events associated with this instance of IAgUiAxVOCntrl."""
        return IAgUiAxVOCntrlEventHandler(self._pUnk)    
    @property
    def BackColor(self) -> agcolor.Color:
        """The background color of the control."""
        with agmarshall.OLE_COLOR_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_GetBackColor"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @BackColor.setter
    def BackColor(self, clr:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(clr) as arg_clr:
            agcls.evaluate_hresult(self.__dict__["_SetBackColor"](arg_clr.COM_val))

    @property
    def Picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        with agmarshall.PVOID_arg() as arg_ppPicture:
            agcls.evaluate_hresult(self.__dict__["_GetPicture"](byref(arg_ppPicture.COM_val)))
            return arg_ppPicture.python_val

    def PicturePutRef(self, pPicture:IPictureDisp) -> None:
        with agmarshall.PVOID_arg(pPicture) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_PicturePutRef"](byref(arg_pPicture.COM_val)))

    @Picture.setter
    def Picture(self, pPicture:IPictureDisp) -> None:
        with agmarshall.PVOID_arg(pPicture) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_SetPicture"](byref(arg_pPicture.COM_val)))

    def PickInfo(self, x:int, y:int) -> "IAgPickInfoData":
        """Get detailed information about a mouse pick."""
        with agmarshall.OLE_XPOS_PIXELS_arg(x) as arg_x, \
             agmarshall.OLE_YPOS_PIXELS_arg(y) as arg_y, \
             agmarshall.AgInterface_out_arg() as arg_ppPickData:
            agcls.evaluate_hresult(self.__dict__["_PickInfo"](arg_x.COM_val, arg_y.COM_val, byref(arg_ppPickData.COM_val)))
            return arg_ppPickData.python_val

    @property
    def WinID(self) -> int:
        """Window identifier (for Connect commands)."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWinID"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @WinID.setter
    def WinID(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetWinID"](arg_newVal.COM_val))

    @property
    def Application(self) -> "IAgSTKXApplication":
        """Reference to the STK X application object."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetApplication"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def ZoomIn(self) -> None:
        """Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom."""
        agcls.evaluate_hresult(self.__dict__["_ZoomIn"]())

    @property
    def NoLogo(self) -> bool:
        """If true, the splash logo is not shown."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pNoLogo:
            agcls.evaluate_hresult(self.__dict__["_GetNoLogo"](byref(arg_pNoLogo.COM_val)))
            return arg_pNoLogo.python_val

    @NoLogo.setter
    def NoLogo(self, bNoLogo:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bNoLogo) as arg_bNoLogo:
            agcls.evaluate_hresult(self.__dict__["_SetNoLogo"](arg_bNoLogo.COM_val))

    @property
    def OLEDropMode(self) -> "AgEOLEDropMode":
        """How the control handles drop operations."""
        with agmarshall.AgEnum_arg(AgEOLEDropMode) as arg_psOLEDropMode:
            agcls.evaluate_hresult(self.__dict__["_GetOLEDropMode"](byref(arg_psOLEDropMode.COM_val)))
            return arg_psOLEDropMode.python_val

    @OLEDropMode.setter
    def OLEDropMode(self, psOLEDropMode:"AgEOLEDropMode") -> None:
        with agmarshall.AgEnum_arg(AgEOLEDropMode, psOLEDropMode) as arg_psOLEDropMode:
            agcls.evaluate_hresult(self.__dict__["_SetOLEDropMode"](arg_psOLEDropMode.COM_val))

    @property
    def VendorID(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetVendorID"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @VendorID.setter
    def VendorID(self, vendorID:str) -> None:
        with agmarshall.BSTR_arg(vendorID) as arg_vendorID:
            agcls.evaluate_hresult(self.__dict__["_SetVendorID"](arg_vendorID.COM_val))

    def RubberBandPickInfo(self, left:int, top:int, right:int, bottom:int) -> "IAgRubberBandPickInfoData":
        """Get detailed information about a rubber-band mouse pick. The values must be within the VO window (0 to width-1 for left and right, 0 to height-1 for top and bottom)."""
        with agmarshall.OLE_XPOS_PIXELS_arg(left) as arg_left, \
             agmarshall.OLE_YPOS_PIXELS_arg(top) as arg_top, \
             agmarshall.OLE_XPOS_PIXELS_arg(right) as arg_right, \
             agmarshall.OLE_YPOS_PIXELS_arg(bottom) as arg_bottom, \
             agmarshall.AgInterface_out_arg() as arg_ppPickInfoData:
            agcls.evaluate_hresult(self.__dict__["_RubberBandPickInfo"](arg_left.COM_val, arg_top.COM_val, arg_right.COM_val, arg_bottom.COM_val, byref(arg_ppPickInfoData.COM_val)))
            return arg_ppPickInfoData.python_val

    @property
    def MouseMode(self) -> "AgEMouseMode":
        """Whether this control responds to mouse events."""
        with agmarshall.AgEnum_arg(AgEMouseMode) as arg_psMouseMode:
            agcls.evaluate_hresult(self.__dict__["_GetMouseMode"](byref(arg_psMouseMode.COM_val)))
            return arg_psMouseMode.python_val

    @MouseMode.setter
    def MouseMode(self, psMouseMode:"AgEMouseMode") -> None:
        with agmarshall.AgEnum_arg(AgEMouseMode, psMouseMode) as arg_psMouseMode:
            agcls.evaluate_hresult(self.__dict__["_SetMouseMode"](arg_psMouseMode.COM_val))

    @property
    def DrawElements(self) -> "IAgDrawElemCollection":
        """Elements to draw on the control."""
        with agmarshall.AgInterface_out_arg() as arg_ppDrawElemColl:
            agcls.evaluate_hresult(self.__dict__["_GetDrawElements"](byref(arg_ppDrawElemColl.COM_val)))
            return arg_ppDrawElemColl.python_val

    @property
    def ReadyState(self) -> int:
        """Returns/sets the background color of the control."""
        with agmarshall.LONG_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_GetReadyState"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @property
    def PptPreloadMode(self) -> bool:
        """Special mode for PowerPoint : if true the VO control window is kept around when switching between slides."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pPptPreloadMode:
            agcls.evaluate_hresult(self.__dict__["_GetPptPreloadMode"](byref(arg_pPptPreloadMode.COM_val)))
            return arg_pPptPreloadMode.python_val

    @PptPreloadMode.setter
    def PptPreloadMode(self, bPptPreloadMode:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bPptPreloadMode) as arg_bPptPreloadMode:
            agcls.evaluate_hresult(self.__dict__["_SetPptPreloadMode"](arg_bPptPreloadMode.COM_val))

    @property
    def AdvancedPickMode(self) -> bool:
        """If true, sets the advance pick mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pAdvancePickMode:
            agcls.evaluate_hresult(self.__dict__["_GetAdvancedPickMode"](byref(arg_pAdvancePickMode.COM_val)))
            return arg_pAdvancePickMode.python_val

    @AdvancedPickMode.setter
    def AdvancedPickMode(self, bAdvancePickMode:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bAdvancePickMode) as arg_bAdvancePickMode:
            agcls.evaluate_hresult(self.__dict__["_SetAdvancedPickMode"](arg_bAdvancePickMode.COM_val))

    def CopyFromWinID(self, winID:int) -> None:
        """Copies an existing Window's scene into this control"""
        with agmarshall.LONG_arg(winID) as arg_winID:
            agcls.evaluate_hresult(self.__dict__["_CopyFromWinID"](arg_winID.COM_val))

    def StartObjectEditing(self, objEditPath:str) -> None:
        """Enters into 3D object editing mode."""
        with agmarshall.BSTR_arg(objEditPath) as arg_objEditPath:
            agcls.evaluate_hresult(self.__dict__["_StartObjectEditing"](arg_objEditPath.COM_val))

    def ApplyObjectEditing(self) -> None:
        """Commits changes when in 3D object editing mode."""
        agcls.evaluate_hresult(self.__dict__["_ApplyObjectEditing"]())

    def StopObjectEditing(self, canceled:bool) -> None:
        """Ends 3D object editing mode."""
        with agmarshall.VARIANT_BOOL_arg(canceled) as arg_canceled:
            agcls.evaluate_hresult(self.__dict__["_StopObjectEditing"](arg_canceled.COM_val))

    @property
    def IsObjectEditing(self) -> bool:
        """Returns true if in 3D object editing mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_p3DObjectEditing:
            agcls.evaluate_hresult(self.__dict__["_GetIsObjectEditing"](byref(arg_p3DObjectEditing.COM_val)))
            return arg_p3DObjectEditing.python_val

    @property
    def InZoomMode(self) -> bool:
        """Returns true if in zoom in mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pZoomIn:
            agcls.evaluate_hresult(self.__dict__["_GetInZoomMode"](byref(arg_pZoomIn.COM_val)))
            return arg_pZoomIn.python_val

    def SetMouseCursorFromFile(self, cursorFileName:str) -> None:
        """Sets mouse cursor to the selected cursor file."""
        with agmarshall.BSTR_arg(cursorFileName) as arg_cursorFileName:
            agcls.evaluate_hresult(self.__dict__["_SetMouseCursorFromFile"](arg_cursorFileName.COM_val))

    def RestoreMouseCursor(self) -> None:
        """Restores mouse cursor back to normal."""
        agcls.evaluate_hresult(self.__dict__["_RestoreMouseCursor"]())

    def SetMouseCursorFromHandle(self, cursorHandle:int) -> None:
        """Sets mouse cursor to the passed cursor handle."""
        with agmarshall.OLE_HANDLE_arg(cursorHandle) as arg_cursorHandle:
            agcls.evaluate_hresult(self.__dict__["_SetMouseCursorFromHandle"](arg_cursorHandle.COM_val))

    @property
    def ShowProgressImage(self) -> "AgEShowProgressImage":
        """The animated progress image type."""
        with agmarshall.AgEnum_arg(AgEShowProgressImage) as arg_psProgressImage:
            agcls.evaluate_hresult(self.__dict__["_GetShowProgressImage"](byref(arg_psProgressImage.COM_val)))
            return arg_psProgressImage.python_val

    @ShowProgressImage.setter
    def ShowProgressImage(self, psProgressImage:"AgEShowProgressImage") -> None:
        with agmarshall.AgEnum_arg(AgEShowProgressImage, psProgressImage) as arg_psProgressImage:
            agcls.evaluate_hresult(self.__dict__["_SetShowProgressImage"](arg_psProgressImage.COM_val))

    @property
    def ProgressImageXOffset(self) -> int:
        """The horizontal X offset for animated progress image."""
        with agmarshall.LONG_arg() as arg_pXOffset:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageXOffset"](byref(arg_pXOffset.COM_val)))
            return arg_pXOffset.python_val

    @ProgressImageXOffset.setter
    def ProgressImageXOffset(self, xOffset:int) -> None:
        with agmarshall.LONG_arg(xOffset) as arg_xOffset:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageXOffset"](arg_xOffset.COM_val))

    @property
    def ProgressImageYOffset(self) -> int:
        """The vertical Y offset for animated progress image."""
        with agmarshall.LONG_arg() as arg_pYOffset:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageYOffset"](byref(arg_pYOffset.COM_val)))
            return arg_pYOffset.python_val

    @ProgressImageYOffset.setter
    def ProgressImageYOffset(self, yOffset:int) -> None:
        with agmarshall.LONG_arg(yOffset) as arg_yOffset:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageYOffset"](arg_yOffset.COM_val))

    @property
    def ProgressImageFile(self) -> str:
        """The complete image file name/path for animated progress image."""
        with agmarshall.BSTR_arg() as arg_pImageFile:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageFile"](byref(arg_pImageFile.COM_val)))
            return arg_pImageFile.python_val

    @ProgressImageFile.setter
    def ProgressImageFile(self, imageFile:str) -> None:
        with agmarshall.BSTR_arg(imageFile) as arg_imageFile:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageFile"](arg_imageFile.COM_val))

    @property
    def ProgressImageXOrigin(self) -> "AgEProgressImageXOrigin":
        """The X origin alignment for animated progress image."""
        with agmarshall.AgEnum_arg(AgEProgressImageXOrigin) as arg_psProgressImageXOrigin:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageXOrigin"](byref(arg_psProgressImageXOrigin.COM_val)))
            return arg_psProgressImageXOrigin.python_val

    @ProgressImageXOrigin.setter
    def ProgressImageXOrigin(self, progressImageXOrigin:"AgEProgressImageXOrigin") -> None:
        with agmarshall.AgEnum_arg(AgEProgressImageXOrigin, progressImageXOrigin) as arg_progressImageXOrigin:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageXOrigin"](arg_progressImageXOrigin.COM_val))

    @property
    def ProgressImageYOrigin(self) -> "AgEProgressImageYOrigin":
        """The Y origin alignment for animated progress image."""
        with agmarshall.AgEnum_arg(AgEProgressImageYOrigin) as arg_psProgressImageYOrigin:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageYOrigin"](byref(arg_psProgressImageYOrigin.COM_val)))
            return arg_psProgressImageYOrigin.python_val

    @ProgressImageYOrigin.setter
    def ProgressImageYOrigin(self, progressImageYOrigin:"AgEProgressImageYOrigin") -> None:
        with agmarshall.AgEnum_arg(AgEProgressImageYOrigin, progressImageYOrigin) as arg_progressImageYOrigin:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageYOrigin"](arg_progressImageYOrigin.COM_val))

    @property
    def PictureFromFile(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg() as arg_pPictureFile:
            agcls.evaluate_hresult(self.__dict__["_GetPictureFromFile"](byref(arg_pPictureFile.COM_val)))
            return arg_pPictureFile.python_val

    @PictureFromFile.setter
    def PictureFromFile(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg(pictureFile) as arg_pictureFile:
            agcls.evaluate_hresult(self.__dict__["_SetPictureFromFile"](arg_pictureFile.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{0975BA23-E273-4B8F-BA8D-32ECB328C092}", IAgUiAxVOCntrl)
agcls.AgTypeNameMap["IAgUiAxVOCntrl"] = IAgUiAxVOCntrl

class IAgUiAx2DCntrl(object):
    """AGI Map control."""
    _uuid = "{A5C18751-1656-4FB9-BA4E-D5746D509CFC}"
    _num_methods = 45
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetBackColor"] = _raise_uninitialized_error
        self.__dict__["_SetBackColor"] = _raise_uninitialized_error
        self.__dict__["_GetPicture"] = _raise_uninitialized_error
        self.__dict__["_PicturePutRef"] = _raise_uninitialized_error
        self.__dict__["_SetPicture"] = _raise_uninitialized_error
        self.__dict__["_GetWinID"] = _raise_uninitialized_error
        self.__dict__["_SetWinID"] = _raise_uninitialized_error
        self.__dict__["_ZoomIn"] = _raise_uninitialized_error
        self.__dict__["_ZoomOut"] = _raise_uninitialized_error
        self.__dict__["_PickInfo"] = _raise_uninitialized_error
        self.__dict__["_GetApplication"] = _raise_uninitialized_error
        self.__dict__["_GetNoLogo"] = _raise_uninitialized_error
        self.__dict__["_SetNoLogo"] = _raise_uninitialized_error
        self.__dict__["_GetOLEDropMode"] = _raise_uninitialized_error
        self.__dict__["_SetOLEDropMode"] = _raise_uninitialized_error
        self.__dict__["_GetVendorID"] = _raise_uninitialized_error
        self.__dict__["_SetVendorID"] = _raise_uninitialized_error
        self.__dict__["_GetMouseMode"] = _raise_uninitialized_error
        self.__dict__["_SetMouseMode"] = _raise_uninitialized_error
        self.__dict__["_GetReadyState"] = _raise_uninitialized_error
        self.__dict__["_CopyFromWinID"] = _raise_uninitialized_error
        self.__dict__["_RubberBandPickInfo"] = _raise_uninitialized_error
        self.__dict__["_GetAdvancedPickMode"] = _raise_uninitialized_error
        self.__dict__["_SetAdvancedPickMode"] = _raise_uninitialized_error
        self.__dict__["_GetWindowProjectedPosition"] = _raise_uninitialized_error
        self.__dict__["_GetInZoomMode"] = _raise_uninitialized_error
        self.__dict__["_SetMouseCursorFromFile"] = _raise_uninitialized_error
        self.__dict__["_RestoreMouseCursor"] = _raise_uninitialized_error
        self.__dict__["_SetMouseCursorFromHandle"] = _raise_uninitialized_error
        self.__dict__["_GetShowProgressImage"] = _raise_uninitialized_error
        self.__dict__["_SetShowProgressImage"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageXOffset"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageXOffset"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageYOffset"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageYOffset"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageFile"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageFile"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageXOrigin"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageXOrigin"] = _raise_uninitialized_error
        self.__dict__["_GetProgressImageYOrigin"] = _raise_uninitialized_error
        self.__dict__["_SetProgressImageYOrigin"] = _raise_uninitialized_error
        self.__dict__["_GetPictureFromFile"] = _raise_uninitialized_error
        self.__dict__["_SetPictureFromFile"] = _raise_uninitialized_error
        self.__dict__["_GetPanModeEnabled"] = _raise_uninitialized_error
        self.__dict__["_SetPanModeEnabled"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiAx2DCntrl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiAx2DCntrl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiAx2DCntrl = agcom.GUID(IAgUiAx2DCntrl._uuid)
        vtable_offset_local = IAgUiAx2DCntrl._vtable_offset - 1
        self.__dict__["_GetBackColor"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+1, POINTER(agcom.OLE_COLOR))
        self.__dict__["_SetBackColor"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+2, agcom.OLE_COLOR)
        self.__dict__["_GetPicture"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_PicturePutRef"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+4, POINTER(agcom.PVOID))
        self.__dict__["_SetPicture"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+5, POINTER(agcom.PVOID))
        self.__dict__["_GetWinID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+6, POINTER(agcom.LONG))
        self.__dict__["_SetWinID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+7, agcom.LONG)
        self.__dict__["_ZoomIn"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+8, )
        self.__dict__["_ZoomOut"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+9, )
        self.__dict__["_PickInfo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+10, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID))
        self.__dict__["_GetApplication"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+11, POINTER(agcom.PVOID))
        self.__dict__["_GetNoLogo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+12, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetNoLogo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+13, agcom.VARIANT_BOOL)
        self.__dict__["_GetOLEDropMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+14, POINTER(agcom.LONG))
        self.__dict__["_SetOLEDropMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+15, agcom.LONG)
        self.__dict__["_GetVendorID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+16, POINTER(agcom.BSTR))
        self.__dict__["_SetVendorID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+17, agcom.BSTR)
        self.__dict__["_GetMouseMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+18, POINTER(agcom.LONG))
        self.__dict__["_SetMouseMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+19, agcom.LONG)
        self.__dict__["_GetReadyState"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+20, POINTER(agcom.LONG))
        self.__dict__["_CopyFromWinID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+21, agcom.LONG)
        self.__dict__["_RubberBandPickInfo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+22, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID))
        self.__dict__["_GetAdvancedPickMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+23, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetAdvancedPickMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+24, agcom.VARIANT_BOOL)
        self.__dict__["_GetWindowProjectedPosition"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+25, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_GetInZoomMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+26, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetMouseCursorFromFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+27, agcom.BSTR)
        self.__dict__["_RestoreMouseCursor"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+28, )
        self.__dict__["_SetMouseCursorFromHandle"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+29, agcom.OLE_HANDLE)
        self.__dict__["_GetShowProgressImage"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+30, POINTER(agcom.LONG))
        self.__dict__["_SetShowProgressImage"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+31, agcom.LONG)
        self.__dict__["_GetProgressImageXOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+32, POINTER(agcom.LONG))
        self.__dict__["_SetProgressImageXOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+33, agcom.LONG)
        self.__dict__["_GetProgressImageYOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+34, POINTER(agcom.LONG))
        self.__dict__["_SetProgressImageYOffset"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+35, agcom.LONG)
        self.__dict__["_GetProgressImageFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+36, POINTER(agcom.BSTR))
        self.__dict__["_SetProgressImageFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+37, agcom.BSTR)
        self.__dict__["_GetProgressImageXOrigin"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+38, POINTER(agcom.LONG))
        self.__dict__["_SetProgressImageXOrigin"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+39, agcom.LONG)
        self.__dict__["_GetProgressImageYOrigin"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+40, POINTER(agcom.LONG))
        self.__dict__["_SetProgressImageYOrigin"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+41, agcom.LONG)
        self.__dict__["_GetPictureFromFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+42, POINTER(agcom.BSTR))
        self.__dict__["_SetPictureFromFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+43, agcom.BSTR)
        self.__dict__["_GetPanModeEnabled"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+44, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetPanModeEnabled"] = IAGFUNCTYPE(pUnk, IID_IAgUiAx2DCntrl, vtable_offset_local+45, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiAx2DCntrl.__dict__ and type(IAgUiAx2DCntrl.__dict__[attrname]) == property:
            return IAgUiAx2DCntrl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiAx2DCntrl.")
    def Subscribe(self) -> IAgUiAx2DCntrlEventHandler:
        """Returns an IAgUiAx2DCntrlEventHandler that is subscribed to handle events associated with this instance of IAgUiAx2DCntrl."""
        return IAgUiAx2DCntrlEventHandler(self._pUnk)    
    @property
    def BackColor(self) -> agcolor.Color:
        """The background color of the control."""
        with agmarshall.OLE_COLOR_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_GetBackColor"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @BackColor.setter
    def BackColor(self, clr:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(clr) as arg_clr:
            agcls.evaluate_hresult(self.__dict__["_SetBackColor"](arg_clr.COM_val))

    @property
    def Picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        with agmarshall.PVOID_arg() as arg_ppPicture:
            agcls.evaluate_hresult(self.__dict__["_GetPicture"](byref(arg_ppPicture.COM_val)))
            return arg_ppPicture.python_val

    def PicturePutRef(self, pPicture:IPictureDisp) -> None:
        with agmarshall.PVOID_arg(pPicture) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_PicturePutRef"](byref(arg_pPicture.COM_val)))

    @Picture.setter
    def Picture(self, pPicture:IPictureDisp) -> None:
        with agmarshall.PVOID_arg(pPicture) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_SetPicture"](byref(arg_pPicture.COM_val)))

    @property
    def WinID(self) -> int:
        """Window identifier (for Connect commands)."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWinID"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @WinID.setter
    def WinID(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetWinID"](arg_newVal.COM_val))

    def ZoomIn(self) -> None:
        """Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom."""
        agcls.evaluate_hresult(self.__dict__["_ZoomIn"]())

    def ZoomOut(self) -> None:
        """Zoom out to view a larger portion of a previously magnified map."""
        agcls.evaluate_hresult(self.__dict__["_ZoomOut"]())

    def PickInfo(self, x:int, y:int) -> "IAgPickInfoData":
        """Get detailed information about a mouse pick."""
        with agmarshall.OLE_XPOS_PIXELS_arg(x) as arg_x, \
             agmarshall.OLE_YPOS_PIXELS_arg(y) as arg_y, \
             agmarshall.AgInterface_out_arg() as arg_ppPickData:
            agcls.evaluate_hresult(self.__dict__["_PickInfo"](arg_x.COM_val, arg_y.COM_val, byref(arg_ppPickData.COM_val)))
            return arg_ppPickData.python_val

    @property
    def Application(self) -> "IAgSTKXApplication":
        """Reference to the STK X application object."""
        with agmarshall.AgInterface_out_arg() as arg_ppApp:
            agcls.evaluate_hresult(self.__dict__["_GetApplication"](byref(arg_ppApp.COM_val)))
            return arg_ppApp.python_val

    @property
    def NoLogo(self) -> bool:
        """If true, the splash logo is not shown."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pNoLogo:
            agcls.evaluate_hresult(self.__dict__["_GetNoLogo"](byref(arg_pNoLogo.COM_val)))
            return arg_pNoLogo.python_val

    @NoLogo.setter
    def NoLogo(self, bNoLogo:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bNoLogo) as arg_bNoLogo:
            agcls.evaluate_hresult(self.__dict__["_SetNoLogo"](arg_bNoLogo.COM_val))

    @property
    def OLEDropMode(self) -> "AgEOLEDropMode":
        """How the control handles drop operations."""
        with agmarshall.AgEnum_arg(AgEOLEDropMode) as arg_psOLEDropMode:
            agcls.evaluate_hresult(self.__dict__["_GetOLEDropMode"](byref(arg_psOLEDropMode.COM_val)))
            return arg_psOLEDropMode.python_val

    @OLEDropMode.setter
    def OLEDropMode(self, psOLEDropMode:"AgEOLEDropMode") -> None:
        with agmarshall.AgEnum_arg(AgEOLEDropMode, psOLEDropMode) as arg_psOLEDropMode:
            agcls.evaluate_hresult(self.__dict__["_SetOLEDropMode"](arg_psOLEDropMode.COM_val))

    @property
    def VendorID(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetVendorID"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @VendorID.setter
    def VendorID(self, vendorID:str) -> None:
        with agmarshall.BSTR_arg(vendorID) as arg_vendorID:
            agcls.evaluate_hresult(self.__dict__["_SetVendorID"](arg_vendorID.COM_val))

    @property
    def MouseMode(self) -> "AgEMouseMode":
        """Whether this control responds to mouse events."""
        with agmarshall.AgEnum_arg(AgEMouseMode) as arg_psMouseMode:
            agcls.evaluate_hresult(self.__dict__["_GetMouseMode"](byref(arg_psMouseMode.COM_val)))
            return arg_psMouseMode.python_val

    @MouseMode.setter
    def MouseMode(self, psMouseMode:"AgEMouseMode") -> None:
        with agmarshall.AgEnum_arg(AgEMouseMode, psMouseMode) as arg_psMouseMode:
            agcls.evaluate_hresult(self.__dict__["_SetMouseMode"](arg_psMouseMode.COM_val))

    @property
    def ReadyState(self) -> int:
        """Returns/sets the background color of the control."""
        with agmarshall.LONG_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_GetReadyState"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    def CopyFromWinID(self, winID:int) -> None:
        """Copies an existing Window's scene into this control"""
        with agmarshall.LONG_arg(winID) as arg_winID:
            agcls.evaluate_hresult(self.__dict__["_CopyFromWinID"](arg_winID.COM_val))

    def RubberBandPickInfo(self, left:int, top:int, right:int, bottom:int) -> "IAgRubberBandPickInfoData":
        """Get detailed information about a rubber-band mouse pick. The values must be within the 2D window (0 to width-1 for left and right, 0 to height-1 for top and bottom)."""
        with agmarshall.OLE_XPOS_PIXELS_arg(left) as arg_left, \
             agmarshall.OLE_YPOS_PIXELS_arg(top) as arg_top, \
             agmarshall.OLE_XPOS_PIXELS_arg(right) as arg_right, \
             agmarshall.OLE_YPOS_PIXELS_arg(bottom) as arg_bottom, \
             agmarshall.AgInterface_out_arg() as arg_ppPickInfoData:
            agcls.evaluate_hresult(self.__dict__["_RubberBandPickInfo"](arg_left.COM_val, arg_top.COM_val, arg_right.COM_val, arg_bottom.COM_val, byref(arg_ppPickInfoData.COM_val)))
            return arg_ppPickInfoData.python_val

    @property
    def AdvancedPickMode(self) -> bool:
        """If true, sets the advance pick mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pAdvancePickMode:
            agcls.evaluate_hresult(self.__dict__["_GetAdvancedPickMode"](byref(arg_pAdvancePickMode.COM_val)))
            return arg_pAdvancePickMode.python_val

    @AdvancedPickMode.setter
    def AdvancedPickMode(self, bAdvancePickMode:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bAdvancePickMode) as arg_bAdvancePickMode:
            agcls.evaluate_hresult(self.__dict__["_SetAdvancedPickMode"](arg_bAdvancePickMode.COM_val))

    def GetWindowProjectedPosition(self, lat:float, lon:float, alt:float, drawCoords:"AgEGfxDrawCoords") -> "IAgWinProjPos":
        """Get the window projected position for given values."""
        with agmarshall.DOUBLE_arg(lat) as arg_lat, \
             agmarshall.DOUBLE_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt, \
             agmarshall.AgEnum_arg(AgEGfxDrawCoords, drawCoords) as arg_drawCoords, \
             agmarshall.AgInterface_out_arg() as arg_ppWinProjPos:
            agcls.evaluate_hresult(self.__dict__["_GetWindowProjectedPosition"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val, arg_drawCoords.COM_val, byref(arg_ppWinProjPos.COM_val)))
            return arg_ppWinProjPos.python_val

    @property
    def InZoomMode(self) -> bool:
        """Returns true if in zoom in mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pZoomIn:
            agcls.evaluate_hresult(self.__dict__["_GetInZoomMode"](byref(arg_pZoomIn.COM_val)))
            return arg_pZoomIn.python_val

    def SetMouseCursorFromFile(self, cursorFileName:str) -> None:
        """Sets mouse cursor to the selected cursor file."""
        with agmarshall.BSTR_arg(cursorFileName) as arg_cursorFileName:
            agcls.evaluate_hresult(self.__dict__["_SetMouseCursorFromFile"](arg_cursorFileName.COM_val))

    def RestoreMouseCursor(self) -> None:
        """Restores mouse cursor back to normal."""
        agcls.evaluate_hresult(self.__dict__["_RestoreMouseCursor"]())

    def SetMouseCursorFromHandle(self, cursorHandle:int) -> None:
        """Sets mouse cursor to the passed cursor handle."""
        with agmarshall.OLE_HANDLE_arg(cursorHandle) as arg_cursorHandle:
            agcls.evaluate_hresult(self.__dict__["_SetMouseCursorFromHandle"](arg_cursorHandle.COM_val))

    @property
    def ShowProgressImage(self) -> "AgEShowProgressImage":
        """The animated progress image type."""
        with agmarshall.AgEnum_arg(AgEShowProgressImage) as arg_psProgressImage:
            agcls.evaluate_hresult(self.__dict__["_GetShowProgressImage"](byref(arg_psProgressImage.COM_val)))
            return arg_psProgressImage.python_val

    @ShowProgressImage.setter
    def ShowProgressImage(self, psProgressImage:"AgEShowProgressImage") -> None:
        with agmarshall.AgEnum_arg(AgEShowProgressImage, psProgressImage) as arg_psProgressImage:
            agcls.evaluate_hresult(self.__dict__["_SetShowProgressImage"](arg_psProgressImage.COM_val))

    @property
    def ProgressImageXOffset(self) -> int:
        """The horizontal X offset for animated progress image."""
        with agmarshall.LONG_arg() as arg_pXOffset:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageXOffset"](byref(arg_pXOffset.COM_val)))
            return arg_pXOffset.python_val

    @ProgressImageXOffset.setter
    def ProgressImageXOffset(self, xOffset:int) -> None:
        with agmarshall.LONG_arg(xOffset) as arg_xOffset:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageXOffset"](arg_xOffset.COM_val))

    @property
    def ProgressImageYOffset(self) -> int:
        """The vertical Y offset for animated progress image."""
        with agmarshall.LONG_arg() as arg_pYOffset:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageYOffset"](byref(arg_pYOffset.COM_val)))
            return arg_pYOffset.python_val

    @ProgressImageYOffset.setter
    def ProgressImageYOffset(self, yOffset:int) -> None:
        with agmarshall.LONG_arg(yOffset) as arg_yOffset:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageYOffset"](arg_yOffset.COM_val))

    @property
    def ProgressImageFile(self) -> str:
        """The complete image file name/path for animated progress image."""
        with agmarshall.BSTR_arg() as arg_pImageFile:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageFile"](byref(arg_pImageFile.COM_val)))
            return arg_pImageFile.python_val

    @ProgressImageFile.setter
    def ProgressImageFile(self, imageFile:str) -> None:
        with agmarshall.BSTR_arg(imageFile) as arg_imageFile:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageFile"](arg_imageFile.COM_val))

    @property
    def ProgressImageXOrigin(self) -> "AgEProgressImageXOrigin":
        """The X origin alignment for animated progress image."""
        with agmarshall.AgEnum_arg(AgEProgressImageXOrigin) as arg_psProgressImageXOrigin:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageXOrigin"](byref(arg_psProgressImageXOrigin.COM_val)))
            return arg_psProgressImageXOrigin.python_val

    @ProgressImageXOrigin.setter
    def ProgressImageXOrigin(self, progressImageXOrigin:"AgEProgressImageXOrigin") -> None:
        with agmarshall.AgEnum_arg(AgEProgressImageXOrigin, progressImageXOrigin) as arg_progressImageXOrigin:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageXOrigin"](arg_progressImageXOrigin.COM_val))

    @property
    def ProgressImageYOrigin(self) -> "AgEProgressImageYOrigin":
        """The Y origin alignment for animated progress image."""
        with agmarshall.AgEnum_arg(AgEProgressImageYOrigin) as arg_psProgressImageYOrigin:
            agcls.evaluate_hresult(self.__dict__["_GetProgressImageYOrigin"](byref(arg_psProgressImageYOrigin.COM_val)))
            return arg_psProgressImageYOrigin.python_val

    @ProgressImageYOrigin.setter
    def ProgressImageYOrigin(self, progressImageYOrigin:"AgEProgressImageYOrigin") -> None:
        with agmarshall.AgEnum_arg(AgEProgressImageYOrigin, progressImageYOrigin) as arg_progressImageYOrigin:
            agcls.evaluate_hresult(self.__dict__["_SetProgressImageYOrigin"](arg_progressImageYOrigin.COM_val))

    @property
    def PictureFromFile(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg() as arg_pPictureFile:
            agcls.evaluate_hresult(self.__dict__["_GetPictureFromFile"](byref(arg_pPictureFile.COM_val)))
            return arg_pPictureFile.python_val

    @PictureFromFile.setter
    def PictureFromFile(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg(pictureFile) as arg_pictureFile:
            agcls.evaluate_hresult(self.__dict__["_SetPictureFromFile"](arg_pictureFile.COM_val))

    @property
    def PanModeEnabled(self) -> bool:
        """Enables/disables pan mode for map control."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pPanMode:
            agcls.evaluate_hresult(self.__dict__["_GetPanModeEnabled"](byref(arg_pPanMode.COM_val)))
            return arg_pPanMode.python_val

    @PanModeEnabled.setter
    def PanModeEnabled(self, bPanMode:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bPanMode) as arg_bPanMode:
            agcls.evaluate_hresult(self.__dict__["_SetPanModeEnabled"](arg_bPanMode.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{A5C18751-1656-4FB9-BA4E-D5746D509CFC}", IAgUiAx2DCntrl)
agcls.AgTypeNameMap["IAgUiAx2DCntrl"] = IAgUiAx2DCntrl

class IAgSTKXApplicationPartnerAccess(object):
    """Access to the application object model for business partners."""
    _uuid = "{ABF4E08E-211F-40B6-A2F0-6938DAA560CE}"
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GrantPartnerAccess"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgSTKXApplicationPartnerAccess._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgSTKXApplicationPartnerAccess from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgSTKXApplicationPartnerAccess = agcom.GUID(IAgSTKXApplicationPartnerAccess._uuid)
        vtable_offset_local = IAgSTKXApplicationPartnerAccess._vtable_offset - 1
        self.__dict__["_GrantPartnerAccess"] = IAGFUNCTYPE(pUnk, IID_IAgSTKXApplicationPartnerAccess, vtable_offset_local+1, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgSTKXApplicationPartnerAccess.__dict__ and type(IAgSTKXApplicationPartnerAccess.__dict__[attrname]) == property:
            return IAgSTKXApplicationPartnerAccess.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgSTKXApplicationPartnerAccess.")
    
    def GrantPartnerAccess(self, vendor:str, product:str, key:str) -> "IAgSTKXApplication":
        """Provide object model root for authorized business partners."""
        with agmarshall.BSTR_arg(vendor) as arg_vendor, \
             agmarshall.BSTR_arg(product) as arg_product, \
             agmarshall.BSTR_arg(key) as arg_key, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GrantPartnerAccess"](arg_vendor.COM_val, arg_product.COM_val, arg_key.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{ABF4E08E-211F-40B6-A2F0-6938DAA560CE}", IAgSTKXApplicationPartnerAccess)
agcls.AgTypeNameMap["IAgSTKXApplicationPartnerAccess"] = IAgSTKXApplicationPartnerAccess

class IAgDataObjectFiles(object):
    """Collection of file names."""
    _uuid = "{C4428821-C59F-45B1-9747-0AD1F988317E}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgDataObjectFiles._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgDataObjectFiles from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgDataObjectFiles = agcom.GUID(IAgDataObjectFiles._uuid)
        vtable_offset_local = IAgDataObjectFiles._vtable_offset - 1
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgDataObjectFiles, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgDataObjectFiles, vtable_offset_local+2, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgDataObjectFiles, vtable_offset_local+3, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgDataObjectFiles.__dict__ and type(IAgDataObjectFiles.__dict__[attrname]) == property:
            return IAgDataObjectFiles.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgDataObjectFiles.")
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
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the file names in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppUnk:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppUnk.COM_val)))
            return arg_ppUnk.python_val

    def Item(self, index:int) -> str:
        """Gets the file name at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Count(self) -> int:
        """Number of file names contained in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{C4428821-C59F-45B1-9747-0AD1F988317E}", IAgDataObjectFiles)
agcls.AgTypeNameMap["IAgDataObjectFiles"] = IAgDataObjectFiles

class IAgUiAxGfxAnalysisCntrl(object):
    """AGI Gfx Analysis control."""
    _uuid = "{5933D068-12E5-4B73-96A3-E06CC3ACC05A}"
    _num_methods = 17
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetBackColor"] = _raise_uninitialized_error
        self.__dict__["_SetBackColor"] = _raise_uninitialized_error
        self.__dict__["_GetPicture"] = _raise_uninitialized_error
        self.__dict__["_PicturePutRef"] = _raise_uninitialized_error
        self.__dict__["_SetPicture"] = _raise_uninitialized_error
        self.__dict__["_GetNoLogo"] = _raise_uninitialized_error
        self.__dict__["_SetNoLogo"] = _raise_uninitialized_error
        self.__dict__["_GetVendorID"] = _raise_uninitialized_error
        self.__dict__["_SetVendorID"] = _raise_uninitialized_error
        self.__dict__["_GetReadyState"] = _raise_uninitialized_error
        self.__dict__["_GetApplication"] = _raise_uninitialized_error
        self.__dict__["_GetControlMode"] = _raise_uninitialized_error
        self.__dict__["_SetControlMode"] = _raise_uninitialized_error
        self.__dict__["_GetPictureFromFile"] = _raise_uninitialized_error
        self.__dict__["_SetPictureFromFile"] = _raise_uninitialized_error
        self.__dict__["_GetWinID"] = _raise_uninitialized_error
        self.__dict__["_SetWinID"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiAxGfxAnalysisCntrl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiAxGfxAnalysisCntrl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiAxGfxAnalysisCntrl = agcom.GUID(IAgUiAxGfxAnalysisCntrl._uuid)
        vtable_offset_local = IAgUiAxGfxAnalysisCntrl._vtable_offset - 1
        self.__dict__["_GetBackColor"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+1, POINTER(agcom.OLE_COLOR))
        self.__dict__["_SetBackColor"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+2, agcom.OLE_COLOR)
        self.__dict__["_GetPicture"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_PicturePutRef"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+4, POINTER(agcom.PVOID))
        self.__dict__["_SetPicture"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+5, POINTER(agcom.PVOID))
        self.__dict__["_GetNoLogo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetNoLogo"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+7, agcom.VARIANT_BOOL)
        self.__dict__["_GetVendorID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_SetVendorID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_GetReadyState"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_GetApplication"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+11, POINTER(agcom.PVOID))
        self.__dict__["_GetControlMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+12, POINTER(agcom.LONG))
        self.__dict__["_SetControlMode"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+13, agcom.LONG)
        self.__dict__["_GetPictureFromFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+14, POINTER(agcom.BSTR))
        self.__dict__["_SetPictureFromFile"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+15, agcom.BSTR)
        self.__dict__["_GetWinID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+16, POINTER(agcom.LONG))
        self.__dict__["_SetWinID"] = IAGFUNCTYPE(pUnk, IID_IAgUiAxGfxAnalysisCntrl, vtable_offset_local+17, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiAxGfxAnalysisCntrl.__dict__ and type(IAgUiAxGfxAnalysisCntrl.__dict__[attrname]) == property:
            return IAgUiAxGfxAnalysisCntrl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiAxGfxAnalysisCntrl.")
    
    @property
    def BackColor(self) -> agcolor.Color:
        """The background color of the control."""
        with agmarshall.OLE_COLOR_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_GetBackColor"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @BackColor.setter
    def BackColor(self, clr:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(clr) as arg_clr:
            agcls.evaluate_hresult(self.__dict__["_SetBackColor"](arg_clr.COM_val))

    @property
    def Picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        with agmarshall.PVOID_arg() as arg_ppPicture:
            agcls.evaluate_hresult(self.__dict__["_GetPicture"](byref(arg_ppPicture.COM_val)))
            return arg_ppPicture.python_val

    def PicturePutRef(self, pPicture:IPictureDisp) -> None:
        with agmarshall.PVOID_arg(pPicture) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_PicturePutRef"](byref(arg_pPicture.COM_val)))

    @Picture.setter
    def Picture(self, pPicture:IPictureDisp) -> None:
        with agmarshall.PVOID_arg(pPicture) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_SetPicture"](byref(arg_pPicture.COM_val)))

    @property
    def NoLogo(self) -> bool:
        """If true, the splash logo is not shown."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pNoLogo:
            agcls.evaluate_hresult(self.__dict__["_GetNoLogo"](byref(arg_pNoLogo.COM_val)))
            return arg_pNoLogo.python_val

    @NoLogo.setter
    def NoLogo(self, bNoLogo:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bNoLogo) as arg_bNoLogo:
            agcls.evaluate_hresult(self.__dict__["_SetNoLogo"](arg_bNoLogo.COM_val))

    @property
    def VendorID(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_GetVendorID"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @VendorID.setter
    def VendorID(self, vendorID:str) -> None:
        with agmarshall.BSTR_arg(vendorID) as arg_vendorID:
            agcls.evaluate_hresult(self.__dict__["_SetVendorID"](arg_vendorID.COM_val))

    @property
    def ReadyState(self) -> int:
        """Returns the ready state of the control."""
        with agmarshall.LONG_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_GetReadyState"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @property
    def Application(self) -> "IAgSTKXApplication":
        """Reference to the STK X application object."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetApplication"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def ControlMode(self) -> "AgEGfxAnalysisMode":
        """The Graphics control mode."""
        with agmarshall.AgEnum_arg(AgEGfxAnalysisMode) as arg_peGfxAnalysisMode:
            agcls.evaluate_hresult(self.__dict__["_GetControlMode"](byref(arg_peGfxAnalysisMode.COM_val)))
            return arg_peGfxAnalysisMode.python_val

    @ControlMode.setter
    def ControlMode(self, eGfxAnalysisMode:"AgEGfxAnalysisMode") -> None:
        with agmarshall.AgEnum_arg(AgEGfxAnalysisMode, eGfxAnalysisMode) as arg_eGfxAnalysisMode:
            agcls.evaluate_hresult(self.__dict__["_SetControlMode"](arg_eGfxAnalysisMode.COM_val))

    @property
    def PictureFromFile(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg() as arg_pPictureFile:
            agcls.evaluate_hresult(self.__dict__["_GetPictureFromFile"](byref(arg_pPictureFile.COM_val)))
            return arg_pPictureFile.python_val

    @PictureFromFile.setter
    def PictureFromFile(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg(pictureFile) as arg_pictureFile:
            agcls.evaluate_hresult(self.__dict__["_SetPictureFromFile"](arg_pictureFile.COM_val))

    @property
    def WinID(self) -> int:
        """Window identifier (for Connect commands)."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWinID"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @WinID.setter
    def WinID(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetWinID"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{5933D068-12E5-4B73-96A3-E06CC3ACC05A}", IAgUiAxGfxAnalysisCntrl)
agcls.AgTypeNameMap["IAgUiAxGfxAnalysisCntrl"] = IAgUiAxGfxAnalysisCntrl



class AgExecCmdResult(IAgExecCmdResult):
    """Collection of strings returned by the ExecuteCommand."""
    def __init__(self, sourceObject=None):
        IAgExecCmdResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgExecCmdResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgExecCmdResult._get_property(self, attrname) is not None: found_prop = IAgExecCmdResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgExecCmdResult.")
        
agcls.AgClassCatalog.add_catalog_entry("{97E6F619-31E5-4AF7-B3AF-0E927F2134D4}", AgExecCmdResult)


class AgExecMultiCmdResult(IAgExecMultiCmdResult):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    def __init__(self, sourceObject=None):
        IAgExecMultiCmdResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgExecMultiCmdResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgExecMultiCmdResult._get_property(self, attrname) is not None: found_prop = IAgExecMultiCmdResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgExecMultiCmdResult.")
        
agcls.AgClassCatalog.add_catalog_entry("{3849A604-DEB9-428C-8A72-D879719277E5}", AgExecMultiCmdResult)


class AgUiAxVOCntrl(IAgUiAxVOCntrl):
    """AGI Globe control."""
    def __init__(self, sourceObject=None):
        IAgUiAxVOCntrl.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiAxVOCntrl._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiAxVOCntrl._get_property(self, attrname) is not None: found_prop = IAgUiAxVOCntrl._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiAxVOCntrl.")
        
agcls.AgClassCatalog.add_catalog_entry("{0E939AC2-43D9-456E-9FE7-4C3C687BCDF2}", AgUiAxVOCntrl)


class AgUiAx2DCntrl(IAgUiAx2DCntrl):
    """AGI Map control."""
    def __init__(self, sourceObject=None):
        IAgUiAx2DCntrl.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiAx2DCntrl._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiAx2DCntrl._get_property(self, attrname) is not None: found_prop = IAgUiAx2DCntrl._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiAx2DCntrl.")
        
agcls.AgClassCatalog.add_catalog_entry("{33FBA419-2BD0-422D-81A7-C5B68A49FB01}", AgUiAx2DCntrl)


class AgPickInfoData(IAgPickInfoData):
    """Single mouse pick result."""
    def __init__(self, sourceObject=None):
        IAgPickInfoData.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgPickInfoData._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgPickInfoData._get_property(self, attrname) is not None: found_prop = IAgPickInfoData._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgPickInfoData.")
        
agcls.AgClassCatalog.add_catalog_entry("{9B6FCD4D-91A0-4855-A113-F7CC8D774608}", AgPickInfoData)


class AgSTKXApplication(IAgSTKXApplication):
    """STK X Application object."""
    def __init__(self, sourceObject=None):
        IAgSTKXApplication.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSTKXApplication._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSTKXApplication._get_property(self, attrname) is not None: found_prop = IAgSTKXApplication._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgSTKXApplication.")
        
agcls.AgClassCatalog.add_catalog_entry("{062AB565-B121-45B5-A9A9-B412CEFAB6A9}", AgSTKXApplication)


class AgSTKXApplicationPartnerAccess(IAgSTKXApplicationPartnerAccess):
    """STK X Application Partner Access object."""
    def __init__(self, sourceObject=None):
        IAgSTKXApplicationPartnerAccess.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSTKXApplicationPartnerAccess._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSTKXApplicationPartnerAccess._get_property(self, attrname) is not None: found_prop = IAgSTKXApplicationPartnerAccess._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgSTKXApplicationPartnerAccess.")
        
agcls.AgClassCatalog.add_catalog_entry("{3E8358E8-6042-4E4C-B89D-1F42164CDE3D}", AgSTKXApplicationPartnerAccess)


class AgDataObject(IAgDataObject):
    """Data Object for OLE drag & drop operations."""
    def __init__(self, sourceObject=None):
        IAgDataObject.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDataObject._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDataObject._get_property(self, attrname) is not None: found_prop = IAgDataObject._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDataObject.")
        
agcls.AgClassCatalog.add_catalog_entry("{C58BE31A-8063-46F9-9751-AF13C1101D75}", AgDataObject)


class AgDataObjectFiles(IAgDataObjectFiles):
    """Collection of files for OLE drag & drop operations."""
    def __init__(self, sourceObject=None):
        IAgDataObjectFiles.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDataObjectFiles._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDataObjectFiles._get_property(self, attrname) is not None: found_prop = IAgDataObjectFiles._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDataObjectFiles.")
        
agcls.AgClassCatalog.add_catalog_entry("{83A2F2F3-3122-4317-8D59-2F43906E4168}", AgDataObjectFiles)


class AgRubberBandPickInfoData(IAgRubberBandPickInfoData):
    """Rubber-band mouse pick result."""
    def __init__(self, sourceObject=None):
        IAgRubberBandPickInfoData.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgRubberBandPickInfoData._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgRubberBandPickInfoData._get_property(self, attrname) is not None: found_prop = IAgRubberBandPickInfoData._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgRubberBandPickInfoData.")
        
agcls.AgClassCatalog.add_catalog_entry("{A7EB5C99-B818-4531-B598-368AA2DD3CF6}", AgRubberBandPickInfoData)


class AgObjPathCollection(IAgObjPathCollection):
    """Collection of object paths."""
    def __init__(self, sourceObject=None):
        IAgObjPathCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgObjPathCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgObjPathCollection._get_property(self, attrname) is not None: found_prop = IAgObjPathCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgObjPathCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{0B3FFC58-8105-4BE4-9D60-254A142448D5}", AgObjPathCollection)


class AgDrawElemRect(IAgDrawElemRect):
    """Defines a rectangle in window coordinates."""
    def __init__(self, sourceObject=None):
        IAgDrawElemRect.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDrawElemRect._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDrawElemRect._get_property(self, attrname) is not None: found_prop = IAgDrawElemRect._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDrawElemRect.")
        
agcls.AgClassCatalog.add_catalog_entry("{55B0A7B5-2508-48BB-90D0-4B8B51DC9178}", AgDrawElemRect)


class AgDrawElemCollection(IAgDrawElemCollection):
    """Collection of elements to draw on the control."""
    def __init__(self, sourceObject=None):
        IAgDrawElemCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDrawElemCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDrawElemCollection._get_property(self, attrname) is not None: found_prop = IAgDrawElemCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDrawElemCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{97A759F9-49E4-42DE-A8E3-7B670EB3BDAC}", AgDrawElemCollection)


class AgDraw2DElemRect(IAgDrawElemRect):
    """Defines a rectangle in window coordinates for map control."""
    def __init__(self, sourceObject=None):
        IAgDrawElemRect.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDrawElemRect._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDrawElemRect._get_property(self, attrname) is not None: found_prop = IAgDrawElemRect._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDraw2DElemRect.")
        
agcls.AgClassCatalog.add_catalog_entry("{C26CEE82-EB4B-4D63-86B0-C5E2BB261E3F}", AgDraw2DElemRect)


class AgDraw2DElemCollection(IAgDrawElemCollection):
    """Collection of elements to draw on map control."""
    def __init__(self, sourceObject=None):
        IAgDrawElemCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDrawElemCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDrawElemCollection._get_property(self, attrname) is not None: found_prop = IAgDrawElemCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDraw2DElemCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{D6B1A826-3ABB-49FD-8C9F-F49ADBE6D2B8}", AgDraw2DElemCollection)


class AgUiAxGfxAnalysisCntrl(IAgUiAxGfxAnalysisCntrl):
    """AGI Graphics Analysis Control"""
    def __init__(self, sourceObject=None):
        IAgUiAxGfxAnalysisCntrl.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiAxGfxAnalysisCntrl._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiAxGfxAnalysisCntrl._get_property(self, attrname) is not None: found_prop = IAgUiAxGfxAnalysisCntrl._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiAxGfxAnalysisCntrl.")
        
agcls.AgClassCatalog.add_catalog_entry("{600541C4-8B16-47AD-ABA4-EE8BC5E9FD5F}", AgUiAxGfxAnalysisCntrl)


class AgWinProjPos(IAgWinProjPos):
    """Projected window position result."""
    def __init__(self, sourceObject=None):
        IAgWinProjPos.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgWinProjPos._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgWinProjPos._get_property(self, attrname) is not None: found_prop = IAgWinProjPos._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgWinProjPos.")
        
agcls.AgClassCatalog.add_catalog_entry("{21D08121-9F86-485E-B143-337DACCD5022}", AgWinProjPos)


class AgDrawElemLine(IAgDrawElemLine):
    """Defines a line in window coordinates."""
    def __init__(self, sourceObject=None):
        IAgDrawElemLine.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgDrawElemLine._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgDrawElemLine._get_property(self, attrname) is not None: found_prop = IAgDrawElemLine._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgDrawElemLine.")
        
agcls.AgClassCatalog.add_catalog_entry("{A4C86FD0-95FA-4F15-BE04-1FDF0DD6B0B5}", AgDrawElemLine)


class AgSTKXSSLCertificateErrorEventArgs(IAgSTKXSSLCertificateErrorEventArgs):
    """Provides information about an SSL certificate that is expired or invalid."""
    def __init__(self, sourceObject=None):
        IAgSTKXSSLCertificateErrorEventArgs.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSTKXSSLCertificateErrorEventArgs._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSTKXSSLCertificateErrorEventArgs._get_property(self, attrname) is not None: found_prop = IAgSTKXSSLCertificateErrorEventArgs._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgSTKXSSLCertificateErrorEventArgs.")
        
agcls.AgClassCatalog.add_catalog_entry("{2BCBD8EC-2EA5-4D14-855D-BB85A201BCB4}", AgSTKXSSLCertificateErrorEventArgs)


class AgSTKXConControlQuitReceivedEventArgs(IAgSTKXConControlQuitReceivedEventArgs):
    """Arguments for the OnConControlQuitReceived event."""
    def __init__(self, sourceObject=None):
        IAgSTKXConControlQuitReceivedEventArgs.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgSTKXConControlQuitReceivedEventArgs._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgSTKXConControlQuitReceivedEventArgs._get_property(self, attrname) is not None: found_prop = IAgSTKXConControlQuitReceivedEventArgs._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgSTKXConControlQuitReceivedEventArgs.")
        
agcls.AgClassCatalog.add_catalog_entry("{CA9E9226-74BE-4733-B50A-D64703165F4E}", AgSTKXConControlQuitReceivedEventArgs)



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
