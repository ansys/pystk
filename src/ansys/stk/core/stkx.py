################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["BUTTON_VALUES", "DataObject", "DataObjectFiles", "Draw2DElemCollection", "Draw2DElemRect", "DrawElemCollection", 
"DrawElemLine", "DrawElemRect", "EXEC_MULTI_CMD_RESULT_ACTION", "ExecCmdResult", "ExecMultiCmdResult", "FEATURE_CODES", 
"GRAPHICS_2D_ANALYSIS_MODE", "GRAPHICS_2D_DRAW_COORDS", "IDataObject", "IDataObjectFiles", "IDrawElem", "IDrawElemCollection", 
"IDrawElemLine", "IDrawElemRect", "IExecCmdResult", "IExecMultiCmdResult", "IObjPathCollection", "IPickInfoData", "IRubberBandPickInfoData", 
"ISTKXApplication", "ISTKXApplicationPartnerAccess", "ISTKXConControlQuitReceivedEventArgs", "ISTKXSSLCertificateErrorEventArgs", 
"IUiAx2DCntrl", "IUiAxGraphics2DAnalysisCntrl", "IUiAxGraphics3DCntrl", "IWinProjectionPosition", "LINE_STYLE", "LOGGING_MODE", 
"LOG_MSG_DISP_ID", "LOG_MSG_TYPE", "MOUSE_MODE", "OLE_DROP_MODE", "ObjPathCollection", "PROGRESS_IMAGE_X_ORIGIN", "PROGRESS_IMAGE_Y_ORIGIN", 
"PickInfoData", "RubberBandPickInfoData", "SHIFT_VALUES", "SHOW_PROGRESS_IMAGE", "STKXApplication", "STKXApplicationPartnerAccess", 
"STKXConControlQuitReceivedEventArgs", "STKXSSLCertificateErrorEventArgs", "UiAx2DCntrl", "UiAxGraphics2DAnalysisCntrl", 
"UiAxGraphics3DCntrl", "WinProjectionPosition"]

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
from .utilities import colors           as agcolor
from .internal.comutil     import IUnknown, IDispatch, IPictureDisp, IAGFUNCTYPE, IEnumVARIANT
from .internal.eventutil   import *
from .utilities.exceptions import *

from .stkutil import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class LOG_MSG_TYPE(IntEnum):
    """Log message types."""
    # Debugging message.
    DEBUG = 0
    # Informational message.
    INFO = 1
    # Informational message.
    FORCE_INFO = 2
    # Warning message.
    WARNING = 3
    # Alarm message.
    ALARM = 4

LOG_MSG_TYPE.DEBUG.__doc__ = "Debugging message."
LOG_MSG_TYPE.INFO.__doc__ = "Informational message."
LOG_MSG_TYPE.FORCE_INFO.__doc__ = "Informational message."
LOG_MSG_TYPE.WARNING.__doc__ = "Warning message."
LOG_MSG_TYPE.ALARM.__doc__ = "Alarm message."

agcls.AgTypeNameMap["LOG_MSG_TYPE"] = LOG_MSG_TYPE

class LOG_MSG_DISP_ID(IntEnum):
    """Log message destination options."""
    # STK displays the message in all the log destination.
    ALL = -1
    # STK displays the message in the default log destination.
    DEFAULT = 0
    # STK displays the message in the message window.
    MSG_WIN = 1
    # STK displays the message in the status bar.
    STATUS_BAR = 2

LOG_MSG_DISP_ID.ALL.__doc__ = "STK displays the message in all the log destination."
LOG_MSG_DISP_ID.DEFAULT.__doc__ = "STK displays the message in the default log destination."
LOG_MSG_DISP_ID.MSG_WIN.__doc__ = "STK displays the message in the message window."
LOG_MSG_DISP_ID.STATUS_BAR.__doc__ = "STK displays the message in the status bar."

agcls.AgTypeNameMap["LOG_MSG_DISP_ID"] = LOG_MSG_DISP_ID

class LINE_STYLE(IntEnum):
    """Line Style"""
    # Specifies a solid line.
    SOLID = 0
    # Specifies a dashed line.
    DASHED = 1
    # Specifies a dotted line.
    DOTTED = 2
    # Dot-dashed line.
    DOT_DASHED = 3
    # Specifies a long dashed line.
    LONG_DASHED = 4
    # Specifies an alternating dash-dot-dot line.
    DASH_DOT_DOTTED = 5
    # Specifies a user configurable medium dashed line.
    M_DASH = 6
    # Specifies a user configurable long dashed line.
    L_DASH = 7
    # Specifies a user configurable small dash-dotted line.
    S_DASH_DOT = 8
    # Specifies a user configurable medium dash-dotted line.
    M_DASH_DOT = 9
    # Specifies a user configurable long dash-dotted line.
    DASH_DOT = 10
    # Specifies a user configurable medium followed by small dashed line.
    MS_DASH = 11
    # Specifies a user configurable long followed by small dashed line.
    LS_DASH = 12
    # Specifies a user configurable long followed by medium dashed line.
    LM_DASH = 13
    # Specifies a user configurable medium followed by small dashed line.
    LMS_DASH = 14
    # Specifies a dotted line.
    DOT = 15
    # Specifies a long dashed line.
    LONG_DASH = 16
    # Specifies an alternating dash-dot line.
    S_DASH = 17

LINE_STYLE.SOLID.__doc__ = "Specifies a solid line."
LINE_STYLE.DASHED.__doc__ = "Specifies a dashed line."
LINE_STYLE.DOTTED.__doc__ = "Specifies a dotted line."
LINE_STYLE.DOT_DASHED.__doc__ = "Dot-dashed line."
LINE_STYLE.LONG_DASHED.__doc__ = "Specifies a long dashed line."
LINE_STYLE.DASH_DOT_DOTTED.__doc__ = "Specifies an alternating dash-dot-dot line."
LINE_STYLE.M_DASH.__doc__ = "Specifies a user configurable medium dashed line."
LINE_STYLE.L_DASH.__doc__ = "Specifies a user configurable long dashed line."
LINE_STYLE.S_DASH_DOT.__doc__ = "Specifies a user configurable small dash-dotted line."
LINE_STYLE.M_DASH_DOT.__doc__ = "Specifies a user configurable medium dash-dotted line."
LINE_STYLE.DASH_DOT.__doc__ = "Specifies a user configurable long dash-dotted line."
LINE_STYLE.MS_DASH.__doc__ = "Specifies a user configurable medium followed by small dashed line."
LINE_STYLE.LS_DASH.__doc__ = "Specifies a user configurable long followed by small dashed line."
LINE_STYLE.LM_DASH.__doc__ = "Specifies a user configurable long followed by medium dashed line."
LINE_STYLE.LMS_DASH.__doc__ = "Specifies a user configurable medium followed by small dashed line."
LINE_STYLE.DOT.__doc__ = "Specifies a dotted line."
LINE_STYLE.LONG_DASH.__doc__ = "Specifies a long dashed line."
LINE_STYLE.S_DASH.__doc__ = "Specifies an alternating dash-dot line."

agcls.AgTypeNameMap["LINE_STYLE"] = LINE_STYLE

class EXEC_MULTI_CMD_RESULT_ACTION(IntFlag):
    """Enumeration defines a set of actions when an error occurs while executing a command batch."""
    # Continue executing the remaining commands in the command batch.
    CONTINUE_ON_ERROR = 0
    # Terminate the execution of the command batch but do not throw an exception.
    STOP_ON_ERROR = 1
    # Terminate the execution of the command batch and throw an exception.
    EXCEPTION_ON_ERROR = 2
    # Ignore results returned by individual commands. The option must be used in combination with other flags.
    IGNORE_EXEC_CMD_RESULT = 0x8000

EXEC_MULTI_CMD_RESULT_ACTION.CONTINUE_ON_ERROR.__doc__ = "Continue executing the remaining commands in the command batch."
EXEC_MULTI_CMD_RESULT_ACTION.STOP_ON_ERROR.__doc__ = "Terminate the execution of the command batch but do not throw an exception."
EXEC_MULTI_CMD_RESULT_ACTION.EXCEPTION_ON_ERROR.__doc__ = "Terminate the execution of the command batch and throw an exception."
EXEC_MULTI_CMD_RESULT_ACTION.IGNORE_EXEC_CMD_RESULT.__doc__ = "Ignore results returned by individual commands. The option must be used in combination with other flags."

agcls.AgTypeNameMap["EXEC_MULTI_CMD_RESULT_ACTION"] = EXEC_MULTI_CMD_RESULT_ACTION

class SHIFT_VALUES(IntEnum):
    """State of the Shift/Ctrl/Alt keys."""
    # The Shift key was pressed.
    PRESSED = 1
    # The Ctrl key was pressed.
    CTRL_PRESSED = 2
    # The ALT key was pressed.
    ALTITUDE_PRESSED = 4

SHIFT_VALUES.PRESSED.__doc__ = "The Shift key was pressed."
SHIFT_VALUES.CTRL_PRESSED.__doc__ = "The Ctrl key was pressed."
SHIFT_VALUES.ALTITUDE_PRESSED.__doc__ = "The ALT key was pressed."

agcls.AgTypeNameMap["SHIFT_VALUES"] = SHIFT_VALUES

class BUTTON_VALUES(IntEnum):
    """Numeric value of the mouse button pressed."""
    # The left button is pressed.
    LEFT_PRESSED = 1
    # The right button is pressed.
    RIGHT_PRESSED = 2
    # The middle button is pressed.
    MIDDLE_PRESSED = 4

BUTTON_VALUES.LEFT_PRESSED.__doc__ = "The left button is pressed."
BUTTON_VALUES.RIGHT_PRESSED.__doc__ = "The right button is pressed."
BUTTON_VALUES.MIDDLE_PRESSED.__doc__ = "The middle button is pressed."

agcls.AgTypeNameMap["BUTTON_VALUES"] = BUTTON_VALUES

class OLE_DROP_MODE(IntEnum):
    """Specifies how to handle OLE drop operations."""
    # None. The control does not accept OLE drops and displays the No Drop cursor.
    NONE = 0
    # Manual. The control triggers the OLE drop events, allowing the programmer to handle the OLE drop operation in code.
    MANUAL = 1
    # Automatic. The control automatically accepts OLE drops if the DataObject object contains data in a format it recognizes. No OLE drag/drop events on the target will occur when OLEDropMode is set to eAutomatic.
    AUTOMATIC = 2

OLE_DROP_MODE.NONE.__doc__ = "None. The control does not accept OLE drops and displays the No Drop cursor."
OLE_DROP_MODE.MANUAL.__doc__ = "Manual. The control triggers the OLE drop events, allowing the programmer to handle the OLE drop operation in code."
OLE_DROP_MODE.AUTOMATIC.__doc__ = "Automatic. The control automatically accepts OLE drops if the DataObject object contains data in a format it recognizes. No OLE drag/drop events on the target will occur when OLEDropMode is set to eAutomatic."

agcls.AgTypeNameMap["OLE_DROP_MODE"] = OLE_DROP_MODE

class MOUSE_MODE(IntEnum):
    """Mouse modes."""
    # Automatic. The control handles the mouse events and then fires the events to the container for additional processing.
    AUTOMATIC = 0
    # None. No default action happens on mouse events. Events are fired to the container.
    MANUAL = 1

MOUSE_MODE.AUTOMATIC.__doc__ = "Automatic. The control handles the mouse events and then fires the events to the container for additional processing."
MOUSE_MODE.MANUAL.__doc__ = "None. No default action happens on mouse events. Events are fired to the container."

agcls.AgTypeNameMap["MOUSE_MODE"] = MOUSE_MODE

class LOGGING_MODE(IntEnum):
    """Specifies the state of the log file."""
    # The log file is not created.
    INACTIVE = 0
    # The log file is created but deleted upon application termination.
    ACTIVE = 1
    # The log file is created and kept even after application is terminated.
    ACTIVE_KEEP_FILE = 2

LOGGING_MODE.INACTIVE.__doc__ = "The log file is not created."
LOGGING_MODE.ACTIVE.__doc__ = "The log file is created but deleted upon application termination."
LOGGING_MODE.ACTIVE_KEEP_FILE.__doc__ = "The log file is created and kept even after application is terminated."

agcls.AgTypeNameMap["LOGGING_MODE"] = LOGGING_MODE

class GRAPHICS_2D_ANALYSIS_MODE(IntEnum):
    """Specifies the mode of Gfx Analysis Control."""
    # The Solar Panel Tool mode.
    SOLAR_PANEL_TOOL = 1
    # The Area Tool mode.
    AREA_TOOL = 2
    # The Obscuration Tool mode.
    OBSCURATION_TOOL = 3
    # The AzElMask Tool mode.
    AZ_EL_MASK_TOOL = 4

GRAPHICS_2D_ANALYSIS_MODE.SOLAR_PANEL_TOOL.__doc__ = "The Solar Panel Tool mode."
GRAPHICS_2D_ANALYSIS_MODE.AREA_TOOL.__doc__ = "The Area Tool mode."
GRAPHICS_2D_ANALYSIS_MODE.OBSCURATION_TOOL.__doc__ = "The Obscuration Tool mode."
GRAPHICS_2D_ANALYSIS_MODE.AZ_EL_MASK_TOOL.__doc__ = "The AzElMask Tool mode."

agcls.AgTypeNameMap["GRAPHICS_2D_ANALYSIS_MODE"] = GRAPHICS_2D_ANALYSIS_MODE

class GRAPHICS_2D_DRAW_COORDS(IntEnum):
    """Specifies the draw coordinates for Map Control."""
    # The draw coordinates values in pixels.
    PIXEL_DRAW_COORDS = 1
    # The draw coordinates values in screen coordinates.
    SCREEN_DRAW_COORDS = 2

GRAPHICS_2D_DRAW_COORDS.PIXEL_DRAW_COORDS.__doc__ = "The draw coordinates values in pixels."
GRAPHICS_2D_DRAW_COORDS.SCREEN_DRAW_COORDS.__doc__ = "The draw coordinates values in screen coordinates."

agcls.AgTypeNameMap["GRAPHICS_2D_DRAW_COORDS"] = GRAPHICS_2D_DRAW_COORDS

class SHOW_PROGRESS_IMAGE(IntEnum):
    """Specifies to show progress image."""
    # Do not show any progress Image.
    NONE = 1
    # Show the default progress image.
    DEFAULT = 2
    # Show the user specified progress image.
    USER = 3

SHOW_PROGRESS_IMAGE.NONE.__doc__ = "Do not show any progress Image."
SHOW_PROGRESS_IMAGE.DEFAULT.__doc__ = "Show the default progress image."
SHOW_PROGRESS_IMAGE.USER.__doc__ = "Show the user specified progress image."

agcls.AgTypeNameMap["SHOW_PROGRESS_IMAGE"] = SHOW_PROGRESS_IMAGE

class FEATURE_CODES(IntEnum):
    """The enumeration values are used to check availability of a given feature."""
    # The enumeration is used to check whether the engine runtime is available.
    ENGINE_RUNTIME = 1
    # The enumeration is used to check whether the globe is available.
    GLOBE_CONTROL = 2

FEATURE_CODES.ENGINE_RUNTIME.__doc__ = "The enumeration is used to check whether the engine runtime is available."
FEATURE_CODES.GLOBE_CONTROL.__doc__ = "The enumeration is used to check whether the globe is available."

agcls.AgTypeNameMap["FEATURE_CODES"] = FEATURE_CODES

class PROGRESS_IMAGE_X_ORIGIN(IntEnum):
    """Specifies to align progress image X origin."""
    # Align progress Image from X left.
    LEFT = 1
    # Align progress Image from X right.
    RIGHT = 2
    # Align progress Image from X center.
    CENTER = 3

PROGRESS_IMAGE_X_ORIGIN.LEFT.__doc__ = "Align progress Image from X left."
PROGRESS_IMAGE_X_ORIGIN.RIGHT.__doc__ = "Align progress Image from X right."
PROGRESS_IMAGE_X_ORIGIN.CENTER.__doc__ = "Align progress Image from X center."

agcls.AgTypeNameMap["PROGRESS_IMAGE_X_ORIGIN"] = PROGRESS_IMAGE_X_ORIGIN

class PROGRESS_IMAGE_Y_ORIGIN(IntEnum):
    """Specifies to align progress image Y origin."""
    # Align progress Image from Y top.
    TOP = 1
    # Align progress Image from Y bottom.
    BOTTOM = 2
    # Align progress Image from Y center.
    CENTER = 3

PROGRESS_IMAGE_Y_ORIGIN.TOP.__doc__ = "Align progress Image from Y top."
PROGRESS_IMAGE_Y_ORIGIN.BOTTOM.__doc__ = "Align progress Image from Y bottom."
PROGRESS_IMAGE_Y_ORIGIN.CENTER.__doc__ = "Align progress Image from Y center."

agcls.AgTypeNameMap["PROGRESS_IMAGE_Y_ORIGIN"] = PROGRESS_IMAGE_Y_ORIGIN


class ISTKXSSLCertificateErrorEventArgs(object):
    """Provides information about an SSL certificate that is expired or invalid."""
    _uuid = "{D0C7ACBC-D1DD-45AE-9582-C7AE5C2E5BEF}"
    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_set_ignore_error"] = _raise_uninitialized_error
        self.__dict__["_get_is_error_ignored"] = _raise_uninitialized_error
        self.__dict__["_set_ignore_error_permanently"] = _raise_uninitialized_error
        self.__dict__["_get_serial_number"] = _raise_uninitialized_error
        self.__dict__["_get_issuer"] = _raise_uninitialized_error
        self.__dict__["_get_subject"] = _raise_uninitialized_error
        self.__dict__["_get_valid_date"] = _raise_uninitialized_error
        self.__dict__["_get_expiration_date"] = _raise_uninitialized_error
        self.__dict__["_get_is_expired"] = _raise_uninitialized_error
        self.__dict__["_get_pem_data"] = _raise_uninitialized_error
        self.__dict__["_get_handled"] = _raise_uninitialized_error
        self.__dict__["_set_handled"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ISTKXSSLCertificateErrorEventArgs._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ISTKXSSLCertificateErrorEventArgs from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_ISTKXSSLCertificateErrorEventArgs = agcom.GUID(ISTKXSSLCertificateErrorEventArgs._uuid)
        vtable_offset_local = ISTKXSSLCertificateErrorEventArgs._vtable_offset - 1
        self.__dict__["_set_ignore_error"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+1, agcom.VARIANT_BOOL)
        self.__dict__["_get_is_error_ignored"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_ignore_error_permanently"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+3, agcom.VARIANT_BOOL)
        self.__dict__["_get_serial_number"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+4, POINTER(agcom.BSTR))
        self.__dict__["_get_issuer"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+5, POINTER(agcom.BSTR))
        self.__dict__["_get_subject"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_get_valid_date"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+7, POINTER(agcom.DATE))
        self.__dict__["_get_expiration_date"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+8, POINTER(agcom.DATE))
        self.__dict__["_get_is_expired"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+9, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_pem_data"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+10, POINTER(agcom.BSTR))
        self.__dict__["_get_handled"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+11, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_handled"] = IAGFUNCTYPE(pUnk, IID_ISTKXSSLCertificateErrorEventArgs, vtable_offset_local+12, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ISTKXSSLCertificateErrorEventArgs.__dict__ and type(ISTKXSSLCertificateErrorEventArgs.__dict__[attrname]) == property:
            return ISTKXSSLCertificateErrorEventArgs.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ISTKXSSLCertificateErrorEventArgs.")
    
    def set_ignore_error(self, ignoreError:bool) -> None:
        """Specify True to ignore the certificate error and continue with establishing secure HTTP connection to the remote server."""
        with agmarshall.VARIANT_BOOL_arg(ignoreError) as arg_ignoreError:
            agcls.evaluate_hresult(self.__dict__["_set_ignore_error"](arg_ignoreError.COM_val))

    @property
    def is_error_ignored(self) -> bool:
        """Returns whether the invalid certificate error is ignored."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_is_error_ignored"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    def set_ignore_error_permanently(self, ignoreErrorPermanently:bool) -> None:
        """Specify True to ignore the certificate error and add the certificate to the list of trusted certificates."""
        with agmarshall.VARIANT_BOOL_arg(ignoreErrorPermanently) as arg_ignoreErrorPermanently:
            agcls.evaluate_hresult(self.__dict__["_set_ignore_error_permanently"](arg_ignoreErrorPermanently.COM_val))

    @property
    def serial_number(self) -> str:
        """Certificate's serial number."""
        with agmarshall.BSTR_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_serial_number"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def issuer(self) -> str:
        """The provider who issued the certificate."""
        with agmarshall.BSTR_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_issuer"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def subject(self) -> str:
        """Certificate's subject field."""
        with agmarshall.BSTR_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_subject"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def valid_date(self) -> datetime:
        """Certificate's valid date."""
        with agmarshall.DATE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_valid_date"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def expiration_date(self) -> datetime:
        """Certificate's expiration date."""
        with agmarshall.DATE_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_expiration_date"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def is_expired(self) -> bool:
        """Whether the certificate is expired."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_is_expired"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def pem_data(self) -> str:
        """Certificate's PEM data encoded as base-64."""
        with agmarshall.BSTR_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_pem_data"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def handled(self) -> bool:
        """Indicates whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_handled"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @handled.setter
    def handled(self, bHandled:bool) -> None:
        """Indicates whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners."""
        with agmarshall.VARIANT_BOOL_arg(bHandled) as arg_bHandled:
            agcls.evaluate_hresult(self.__dict__["_set_handled"](arg_bHandled.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{D0C7ACBC-D1DD-45AE-9582-C7AE5C2E5BEF}", ISTKXSSLCertificateErrorEventArgs)
agcls.AgTypeNameMap["ISTKXSSLCertificateErrorEventArgs"] = ISTKXSSLCertificateErrorEventArgs

class ISTKXConControlQuitReceivedEventArgs(object):
    """Arguments for the OnConControlQuitReceived event."""
    _uuid = "{F8925F99-8841-4DF3-A6E4-CE63E298868C}"
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_acknowledge"] = _raise_uninitialized_error
        self.__dict__["_set_acknowledge"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ISTKXConControlQuitReceivedEventArgs._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ISTKXConControlQuitReceivedEventArgs from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_ISTKXConControlQuitReceivedEventArgs = agcom.GUID(ISTKXConControlQuitReceivedEventArgs._uuid)
        vtable_offset_local = ISTKXConControlQuitReceivedEventArgs._vtable_offset - 1
        self.__dict__["_get_acknowledge"] = IAGFUNCTYPE(pUnk, IID_ISTKXConControlQuitReceivedEventArgs, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_acknowledge"] = IAGFUNCTYPE(pUnk, IID_ISTKXConControlQuitReceivedEventArgs, vtable_offset_local+2, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ISTKXConControlQuitReceivedEventArgs.__dict__ and type(ISTKXConControlQuitReceivedEventArgs.__dict__[attrname]) == property:
            return ISTKXConControlQuitReceivedEventArgs.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ISTKXConControlQuitReceivedEventArgs.")
    
    @property
    def acknowledge(self) -> bool:
        """Indicates whether or not to acknowledge the connect command."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_acknowledge"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @acknowledge.setter
    def acknowledge(self, acknowledge:bool) -> None:
        """Indicates whether or not to acknowledge the connect command."""
        with agmarshall.VARIANT_BOOL_arg(acknowledge) as arg_acknowledge:
            agcls.evaluate_hresult(self.__dict__["_set_acknowledge"](arg_acknowledge.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{F8925F99-8841-4DF3-A6E4-CE63E298868C}", ISTKXConControlQuitReceivedEventArgs)
agcls.AgTypeNameMap["ISTKXConControlQuitReceivedEventArgs"] = ISTKXConControlQuitReceivedEventArgs

class IPickInfoData(object):
    """Mouse pick details."""
    _uuid = "{C87F43DA-DD89-4F13-BCB6-D78D0FE8D7E4}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_obj_path"] = _raise_uninitialized_error
        self.__dict__["_get_lat"] = _raise_uninitialized_error
        self.__dict__["_get_lon"] = _raise_uninitialized_error
        self.__dict__["_get_altitude"] = _raise_uninitialized_error
        self.__dict__["_get_is_obj_path_valid"] = _raise_uninitialized_error
        self.__dict__["_get_is_lat_lon_altitude_valid"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IPickInfoData._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IPickInfoData from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IPickInfoData = agcom.GUID(IPickInfoData._uuid)
        vtable_offset_local = IPickInfoData._vtable_offset - 1
        self.__dict__["_get_obj_path"] = IAGFUNCTYPE(pUnk, IID_IPickInfoData, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_get_lat"] = IAGFUNCTYPE(pUnk, IID_IPickInfoData, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__["_get_lon"] = IAGFUNCTYPE(pUnk, IID_IPickInfoData, vtable_offset_local+3, POINTER(agcom.DOUBLE))
        self.__dict__["_get_altitude"] = IAGFUNCTYPE(pUnk, IID_IPickInfoData, vtable_offset_local+4, POINTER(agcom.DOUBLE))
        self.__dict__["_get_is_obj_path_valid"] = IAGFUNCTYPE(pUnk, IID_IPickInfoData, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_is_lat_lon_altitude_valid"] = IAGFUNCTYPE(pUnk, IID_IPickInfoData, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IPickInfoData.__dict__ and type(IPickInfoData.__dict__[attrname]) == property:
            return IPickInfoData.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IPickInfoData.")
    
    @property
    def obj_path(self) -> str:
        """Path of the STK object picked if any (or empty string)."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_obj_path"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def lat(self) -> float:
        """Latitude of point clicked (if available)."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lat"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def lon(self) -> float:
        """Longitude of point clicked (if available)."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_lon"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def altitude(self) -> float:
        """Altitude of point clicked (if available)."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_altitude"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def is_obj_path_valid(self) -> bool:
        """Indicate if the ObjPath property is valid."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__["_get_is_obj_path_valid"](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val

    @property
    def is_lat_lon_altitude_valid(self) -> bool:
        """Indicate if the Lat/Lon/Alt properties are valid."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__["_get_is_lat_lon_altitude_valid"](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val


agcls.AgClassCatalog.add_catalog_entry("{C87F43DA-DD89-4F13-BCB6-D78D0FE8D7E4}", IPickInfoData)
agcls.AgTypeNameMap["IPickInfoData"] = IPickInfoData

class IRubberBandPickInfoData(object):
    """Rubber-band mouse pick result."""
    _uuid = "{54417F99-E500-4BD8-A762-DC3367C7624C}"
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_obj_paths"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IRubberBandPickInfoData._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IRubberBandPickInfoData from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IRubberBandPickInfoData = agcom.GUID(IRubberBandPickInfoData._uuid)
        vtable_offset_local = IRubberBandPickInfoData._vtable_offset - 1
        self.__dict__["_get_obj_paths"] = IAGFUNCTYPE(pUnk, IID_IRubberBandPickInfoData, vtable_offset_local+1, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IRubberBandPickInfoData.__dict__ and type(IRubberBandPickInfoData.__dict__[attrname]) == property:
            return IRubberBandPickInfoData.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IRubberBandPickInfoData.")
    
    @property
    def obj_paths(self) -> "IObjPathCollection":
        """List of object paths selected."""
        with agmarshall.AgInterface_out_arg() as arg_ppColl:
            agcls.evaluate_hresult(self.__dict__["_get_obj_paths"](byref(arg_ppColl.COM_val)))
            return arg_ppColl.python_val


agcls.AgClassCatalog.add_catalog_entry("{54417F99-E500-4BD8-A762-DC3367C7624C}", IRubberBandPickInfoData)
agcls.AgTypeNameMap["IRubberBandPickInfoData"] = IRubberBandPickInfoData

class ISTKXApplication(object):
    """STK X Application object."""
    _uuid = "{A2BB8372-EA5F-4D9D-84C3-4D9E5B9A8840}"
    _num_methods = 27
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_execute_command"] = _raise_uninitialized_error
        self.__dict__["_get_enable_connect"] = _raise_uninitialized_error
        self.__dict__["_set_enable_connect"] = _raise_uninitialized_error
        self.__dict__["_get_connect_port"] = _raise_uninitialized_error
        self.__dict__["_set_connect_port"] = _raise_uninitialized_error
        self.__dict__["_get_host_id"] = _raise_uninitialized_error
        self.__dict__["_get_registration_id"] = _raise_uninitialized_error
        self.__dict__["_get_version"] = _raise_uninitialized_error
        self.__dict__["_get_licensing_report"] = _raise_uninitialized_error
        self.__dict__["_get_vendor_id"] = _raise_uninitialized_error
        self.__dict__["_set_vendor_id"] = _raise_uninitialized_error
        self.__dict__["_set_online_options"] = _raise_uninitialized_error
        self.__dict__["_get_online_options"] = _raise_uninitialized_error
        self.__dict__["_set_connect_handler"] = _raise_uninitialized_error
        self.__dict__["_get_log_file_full_name"] = _raise_uninitialized_error
        self.__dict__["_get_logging_mode"] = _raise_uninitialized_error
        self.__dict__["_set_logging_mode"] = _raise_uninitialized_error
        self.__dict__["_get_connect_max_connections"] = _raise_uninitialized_error
        self.__dict__["_set_connect_max_connections"] = _raise_uninitialized_error
        self.__dict__["_execute_multiple_commands"] = _raise_uninitialized_error
        self.__dict__["_is_feature_available"] = _raise_uninitialized_error
        self.__dict__["_get_no_graphics"] = _raise_uninitialized_error
        self.__dict__["_set_no_graphics"] = _raise_uninitialized_error
        self.__dict__["_terminate"] = _raise_uninitialized_error
        self.__dict__["_get_show_sla_if_not_accepted"] = _raise_uninitialized_error
        self.__dict__["_set_show_sla_if_not_accepted"] = _raise_uninitialized_error
        self.__dict__["_set_use_hook"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ISTKXApplication._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ISTKXApplication from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_ISTKXApplication = agcom.GUID(ISTKXApplication._uuid)
        vtable_offset_local = ISTKXApplication._vtable_offset - 1
        self.__dict__["_execute_command"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+1, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_get_enable_connect"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+2, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_enable_connect"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+3, agcom.VARIANT_BOOL)
        self.__dict__["_get_connect_port"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+4, POINTER(agcom.SHORT))
        self.__dict__["_set_connect_port"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+5, agcom.SHORT)
        self.__dict__["_get_host_id"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+6, POINTER(agcom.BSTR))
        self.__dict__["_get_registration_id"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+7, POINTER(agcom.BSTR))
        self.__dict__["_get_version"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_get_licensing_report"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+9, POINTER(agcom.BSTR))
        self.__dict__["_get_vendor_id"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+10, POINTER(agcom.BSTR))
        self.__dict__["_set_vendor_id"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+11, agcom.BSTR)
        self.__dict__["_set_online_options"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+12, agcom.VARIANT_BOOL, agcom.BSTR, agcom.LONG, agcom.BSTR, agcom.BSTR, agcom.VARIANT_BOOL, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_online_options"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+13, POINTER(agcom.VARIANT_BOOL), POINTER(agcom.BSTR), POINTER(agcom.LONG), POINTER(agcom.BSTR), POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_connect_handler"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+14, agcom.BSTR, agcom.BSTR)
        self.__dict__["_get_log_file_full_name"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+15, POINTER(agcom.BSTR))
        self.__dict__["_get_logging_mode"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+16, POINTER(agcom.LONG))
        self.__dict__["_set_logging_mode"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+17, agcom.LONG)
        self.__dict__["_get_connect_max_connections"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+18, POINTER(agcom.LONG))
        self.__dict__["_set_connect_max_connections"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+19, agcom.LONG)
        self.__dict__["_execute_multiple_commands"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+20, POINTER(agcom.SAFEARRAY), agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_is_feature_available"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+21, agcom.LONG, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_no_graphics"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+22, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_no_graphics"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+23, agcom.VARIANT_BOOL)
        self.__dict__["_terminate"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+24, )
        self.__dict__["_get_show_sla_if_not_accepted"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+25, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_show_sla_if_not_accepted"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+26, agcom.VARIANT_BOOL)
        self.__dict__["_set_use_hook"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplication, vtable_offset_local+27, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ISTKXApplication.__dict__ and type(ISTKXApplication.__dict__[attrname]) == property:
            return ISTKXApplication.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ISTKXApplication.")
    def Subscribe(self) -> ISTKXApplicationEventHandler:
        """Returns an ISTKXApplicationEventHandler that is subscribed to handle events associated with this instance of ISTKXApplication."""
        return ISTKXApplicationEventHandler(self._pUnk)    
    def execute_command(self, command:str) -> "IExecCmdResult":
        """Send a connect command to STK X."""
        with agmarshall.BSTR_arg(command) as arg_command, \
             agmarshall.AgInterface_out_arg() as arg_ppExecCmdRes:
            agcls.evaluate_hresult(self.__dict__["_execute_command"](arg_command.COM_val, byref(arg_ppExecCmdRes.COM_val)))
            return arg_ppExecCmdRes.python_val

    @property
    def enable_connect(self) -> bool:
        """Enable or disable TCP/IP connect command processing (default: disabled)."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_enable_connect"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @enable_connect.setter
    def enable_connect(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_enable_connect"](arg_newVal.COM_val))

    @property
    def connect_port(self) -> int:
        """Specify TCP/IP port to be used by Connect (default: 5001)."""
        with agmarshall.SHORT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_connect_port"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @connect_port.setter
    def connect_port(self, newVal:int) -> None:
        with agmarshall.SHORT_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_connect_port"](arg_newVal.COM_val))

    @property
    def host_id(self) -> str:
        """Returns the Host ID."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_host_id"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @property
    def registration_id(self) -> str:
        """Returns the Registration ID."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_registration_id"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @property
    def version(self) -> str:
        """Returns the version number"""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_version"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    def get_licensing_report(self) -> str:
        """This method is deprecated. Returns a formatted string that contains the license names and their states. The string is formatted as an XML document."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_licensing_report"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @property
    def vendor_id(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_vendor_id"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @vendor_id.setter
    def vendor_id(self, vendorID:str) -> None:
        with agmarshall.BSTR_arg(vendorID) as arg_vendorID:
            agcls.evaluate_hresult(self.__dict__["_set_vendor_id"](arg_vendorID.COM_val))

    def set_online_options(self, useProxy:bool, serverName:str, portNum:int, userName:str, password:str, savePassword:bool) -> bool:
        """Set http proxy online options"""
        with agmarshall.VARIANT_BOOL_arg(useProxy) as arg_useProxy, \
             agmarshall.BSTR_arg(serverName) as arg_serverName, \
             agmarshall.LONG_arg(portNum) as arg_portNum, \
             agmarshall.BSTR_arg(userName) as arg_userName, \
             agmarshall.BSTR_arg(password) as arg_password, \
             agmarshall.VARIANT_BOOL_arg(savePassword) as arg_savePassword, \
             agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_set_online_options"](arg_useProxy.COM_val, arg_serverName.COM_val, arg_portNum.COM_val, arg_userName.COM_val, arg_password.COM_val, arg_savePassword.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def get_online_options(self) -> typing.Tuple[bool, str, int, str, bool]:
        """Get http proxy online options"""
        with agmarshall.VARIANT_BOOL_arg() as arg_useProxy, \
             agmarshall.BSTR_arg() as arg_serverName, \
             agmarshall.LONG_arg() as arg_portNum, \
             agmarshall.BSTR_arg() as arg_userName, \
             agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_online_options"](byref(arg_useProxy.COM_val), byref(arg_serverName.COM_val), byref(arg_portNum.COM_val), byref(arg_userName.COM_val), byref(arg_pVal.COM_val)))
            return arg_useProxy.python_val, arg_serverName.python_val, arg_portNum.python_val, arg_userName.python_val, arg_pVal.python_val

    def set_connect_handler(self, commandID:str, progID:str) -> None:
        """Set callback to handle a certain connect command"""
        with agmarshall.BSTR_arg(commandID) as arg_commandID, \
             agmarshall.BSTR_arg(progID) as arg_progID:
            agcls.evaluate_hresult(self.__dict__["_set_connect_handler"](arg_commandID.COM_val, arg_progID.COM_val))

    @property
    def log_file_full_name(self) -> str:
        """Returns full path and log file name."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_log_file_full_name"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @property
    def logging_mode(self) -> "LOGGING_MODE":
        """Controls the log file generation, and if the log file is deleted or not on application exit."""
        with agmarshall.AgEnum_arg(LOGGING_MODE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_logging_mode"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @logging_mode.setter
    def logging_mode(self, newVal:"LOGGING_MODE") -> None:
        with agmarshall.AgEnum_arg(LOGGING_MODE, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_logging_mode"](arg_newVal.COM_val))

    @property
    def connect_max_connections(self) -> int:
        """Specify the maximum number of Connect connections to allow."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_connect_max_connections"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @connect_max_connections.setter
    def connect_max_connections(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_connect_max_connections"](arg_newVal.COM_val))

    def execute_multiple_commands(self, connectCommands:list, eAction:"EXEC_MULTI_CMD_RESULT_ACTION") -> "IExecMultiCmdResult":
        """Executes multiple CONNECT actions. The method throws an exception if any of the specified commands have failed."""
        with agmarshall.SAFEARRAY_arg(connectCommands) as arg_connectCommands, \
             agmarshall.AgEnum_arg(EXEC_MULTI_CMD_RESULT_ACTION, eAction) as arg_eAction, \
             agmarshall.AgInterface_out_arg() as arg_ppResult:
            agcls.evaluate_hresult(self.__dict__["_execute_multiple_commands"](byref(arg_connectCommands.COM_val), arg_eAction.COM_val, byref(arg_ppResult.COM_val)))
            return arg_ppResult.python_val

    def is_feature_available(self, featureCode:"FEATURE_CODES") -> bool:
        """Returns true if the specified feature is available."""
        with agmarshall.AgEnum_arg(FEATURE_CODES, featureCode) as arg_featureCode, \
             agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_is_feature_available"](arg_featureCode.COM_val, byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def no_graphics(self) -> bool:
        """Start engine with or without graphics (default: engine starts with graphics.)."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_no_graphics"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @no_graphics.setter
    def no_graphics(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_no_graphics"](arg_newVal.COM_val))

    def terminate(self) -> None:
        """Terminates the use of STK Engine. This must be the last call to STK Engine."""
        agcls.evaluate_hresult(self.__dict__["_terminate"]())

    @property
    def show_sla_if_not_accepted(self) -> bool:
        """Shows the Software License Agreement dialog if not already accepted."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_show_sla_if_not_accepted"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @show_sla_if_not_accepted.setter
    def show_sla_if_not_accepted(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_show_sla_if_not_accepted"](arg_newVal.COM_val))

    @property
    def use_hook(self) -> None:
        """use_hook is a write-only property."""
        raise RuntimeError("use_hook is a write-only property.")


    @use_hook.setter
    def use_hook(self, newVal:bool) -> None:
        """Start engine with or without message hook setup (default: engine starts with message hook setup.)."""
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_use_hook"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{A2BB8372-EA5F-4D9D-84C3-4D9E5B9A8840}", ISTKXApplication)
agcls.AgTypeNameMap["ISTKXApplication"] = ISTKXApplication

class IDataObject(object):
    """IDataObject is used for OLE drag and drop operations"""
    _uuid = "{557F091D-247F-4040-B1E9-10E5BCEDFFD5}"
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_files"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDataObject._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDataObject from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IDataObject = agcom.GUID(IDataObject._uuid)
        vtable_offset_local = IDataObject._vtable_offset - 1
        self.__dict__["_get_files"] = IAGFUNCTYPE(pUnk, IID_IDataObject, vtable_offset_local+1, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDataObject.__dict__ and type(IDataObject.__dict__[attrname]) == property:
            return IDataObject.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IDataObject.")
    
    @property
    def files(self) -> "IDataObjectFiles":
        """Returns a collection of filenames."""
        with agmarshall.AgInterface_out_arg() as arg_pFile:
            agcls.evaluate_hresult(self.__dict__["_get_files"](byref(arg_pFile.COM_val)))
            return arg_pFile.python_val


agcls.AgClassCatalog.add_catalog_entry("{557F091D-247F-4040-B1E9-10E5BCEDFFD5}", IDataObject)
agcls.AgTypeNameMap["IDataObject"] = IDataObject

class IObjPathCollection(object):
    """Collection of object paths."""
    _uuid = "{831E53E8-4E79-4E2E-B289-A6AD76A76F3A}"
    _num_methods = 4
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_range"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IObjPathCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IObjPathCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IObjPathCollection = agcom.GUID(IObjPathCollection._uuid)
        vtable_offset_local = IObjPathCollection._vtable_offset - 1
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IObjPathCollection, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IObjPathCollection, vtable_offset_local+2, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IObjPathCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_range"] = IAGFUNCTYPE(pUnk, IID_IObjPathCollection, vtable_offset_local+4, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IObjPathCollection.__dict__ and type(IObjPathCollection.__dict__[attrname]) == property:
            return IObjPathCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IObjPathCollection.")
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
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def item(self, index:int) -> str:
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pItem:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pItem.COM_val)))
            return arg_pItem.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the object paths in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    def range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        with agmarshall.LONG_arg(startIndex) as arg_startIndex, \
             agmarshall.LONG_arg(stopIndex) as arg_stopIndex, \
             agmarshall.SAFEARRAY_arg() as arg_pVar:
            agcls.evaluate_hresult(self.__dict__["_range"](arg_startIndex.COM_val, arg_stopIndex.COM_val, byref(arg_pVar.COM_val)))
            return arg_pVar.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{831E53E8-4E79-4E2E-B289-A6AD76A76F3A}", IObjPathCollection)
agcls.AgTypeNameMap["IObjPathCollection"] = IObjPathCollection

class IDrawElem(object):
    """Draw element."""
    _uuid = "{C661025D-FFB3-429A-A0B1-D8421DE76AC6}"
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_visible"] = _raise_uninitialized_error
        self.__dict__["_set_visible"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDrawElem._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDrawElem from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IDrawElem = agcom.GUID(IDrawElem._uuid)
        vtable_offset_local = IDrawElem._vtable_offset - 1
        self.__dict__["_get_visible"] = IAGFUNCTYPE(pUnk, IID_IDrawElem, vtable_offset_local+1, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_visible"] = IAGFUNCTYPE(pUnk, IID_IDrawElem, vtable_offset_local+2, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDrawElem.__dict__ and type(IDrawElem.__dict__[attrname]) == property:
            return IDrawElem.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IDrawElem.")
    
    @property
    def visible(self) -> bool:
        """Show or hide the element."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_visible"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @visible.setter
    def visible(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_visible"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{C661025D-FFB3-429A-A0B1-D8421DE76AC6}", IDrawElem)
agcls.AgTypeNameMap["IDrawElem"] = IDrawElem

class IDrawElemRect(IDrawElem):
    """Defines a rectangle in control coordinates."""
    _uuid = "{B017EED9-DC32-4865-BDB9-6C586DC1818C}"
    _num_methods = 11
    _vtable_offset = IDrawElem._vtable_offset + IDrawElem._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_left"] = _raise_uninitialized_error
        self.__dict__["_get_right"] = _raise_uninitialized_error
        self.__dict__["_get_top"] = _raise_uninitialized_error
        self.__dict__["_get_bottom"] = _raise_uninitialized_error
        self.__dict__["_set"] = _raise_uninitialized_error
        self.__dict__["_get_color"] = _raise_uninitialized_error
        self.__dict__["_set_color"] = _raise_uninitialized_error
        self.__dict__["_get_line_width"] = _raise_uninitialized_error
        self.__dict__["_set_line_width"] = _raise_uninitialized_error
        self.__dict__["_get_line_style"] = _raise_uninitialized_error
        self.__dict__["_set_line_style"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDrawElemRect._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDrawElemRect from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDrawElem._private_init(self, pUnk)
        IID_IDrawElemRect = agcom.GUID(IDrawElemRect._uuid)
        vtable_offset_local = IDrawElemRect._vtable_offset - 1
        self.__dict__["_get_left"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+1, POINTER(agcom.OLE_XPOS_PIXELS))
        self.__dict__["_get_right"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+2, POINTER(agcom.OLE_XPOS_PIXELS))
        self.__dict__["_get_top"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+3, POINTER(agcom.OLE_YPOS_PIXELS))
        self.__dict__["_get_bottom"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+4, POINTER(agcom.OLE_YPOS_PIXELS))
        self.__dict__["_set"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+5, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS)
        self.__dict__["_get_color"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+6, POINTER(agcom.OLE_COLOR))
        self.__dict__["_set_color"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+7, agcom.OLE_COLOR)
        self.__dict__["_get_line_width"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+8, POINTER(agcom.FLOAT))
        self.__dict__["_set_line_width"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+9, agcom.FLOAT)
        self.__dict__["_get_line_style"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_set_line_style"] = IAGFUNCTYPE(pUnk, IID_IDrawElemRect, vtable_offset_local+11, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDrawElemRect.__dict__ and type(IDrawElemRect.__dict__[attrname]) == property:
            return IDrawElemRect.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IDrawElem.__setattr__(self, attrname, value)
    
    @property
    def left(self) -> int:
        """The x-coordinate of the left edge of this rectangle."""
        with agmarshall.OLE_XPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_left"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def right(self) -> int:
        """The x-coordinate of the right edge of this rectangle."""
        with agmarshall.OLE_XPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_right"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def top(self) -> int:
        """The y-coordinate of the top edge of this rectangle."""
        with agmarshall.OLE_YPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_top"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def bottom(self) -> int:
        """The y-coordinate of the bottom edge of this rectangle."""
        with agmarshall.OLE_YPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_bottom"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def set(self, left:int, top:int, right:int, bottom:int) -> None:
        """Set the rectangle coordinates."""
        with agmarshall.OLE_XPOS_PIXELS_arg(left) as arg_left, \
             agmarshall.OLE_YPOS_PIXELS_arg(top) as arg_top, \
             agmarshall.OLE_XPOS_PIXELS_arg(right) as arg_right, \
             agmarshall.OLE_YPOS_PIXELS_arg(bottom) as arg_bottom:
            agcls.evaluate_hresult(self.__dict__["_set"](arg_left.COM_val, arg_top.COM_val, arg_right.COM_val, arg_bottom.COM_val))

    @property
    def color(self) -> agcolor.Color:
        """Color of the rectangle."""
        with agmarshall.OLE_COLOR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_color"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @color.setter
    def color(self, newVal:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_color"](arg_newVal.COM_val))

    @property
    def line_width(self) -> float:
        """Specifies the width of the line."""
        with agmarshall.FLOAT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_line_width"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @line_width.setter
    def line_width(self, newVal:float) -> None:
        with agmarshall.FLOAT_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_line_width"](arg_newVal.COM_val))

    @property
    def line_style(self) -> "LINE_STYLE":
        """Specifies the style of the line."""
        with agmarshall.AgEnum_arg(LINE_STYLE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_line_style"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @line_style.setter
    def line_style(self, newVal:"LINE_STYLE") -> None:
        with agmarshall.AgEnum_arg(LINE_STYLE, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_line_style"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{B017EED9-DC32-4865-BDB9-6C586DC1818C}", IDrawElemRect)
agcls.AgTypeNameMap["IDrawElemRect"] = IDrawElemRect

class IDrawElemCollection(object):
    """Collection of elements to draw on the control."""
    _uuid = "{3D6D784D-7C84-4A30-95D8-7D57AF7C560E}"
    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_clear"] = _raise_uninitialized_error
        self.__dict__["_add"] = _raise_uninitialized_error
        self.__dict__["_remove"] = _raise_uninitialized_error
        self.__dict__["_get_visible"] = _raise_uninitialized_error
        self.__dict__["_set_visible"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDrawElemCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDrawElemCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IDrawElemCollection = agcom.GUID(IDrawElemCollection._uuid)
        vtable_offset_local = IDrawElemCollection._vtable_offset - 1
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IDrawElemCollection, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IDrawElemCollection, vtable_offset_local+2, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IDrawElemCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_clear"] = IAGFUNCTYPE(pUnk, IID_IDrawElemCollection, vtable_offset_local+4, )
        self.__dict__["_add"] = IAGFUNCTYPE(pUnk, IID_IDrawElemCollection, vtable_offset_local+5, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_remove"] = IAGFUNCTYPE(pUnk, IID_IDrawElemCollection, vtable_offset_local+6, agcom.PVOID)
        self.__dict__["_get_visible"] = IAGFUNCTYPE(pUnk, IID_IDrawElemCollection, vtable_offset_local+7, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_visible"] = IAGFUNCTYPE(pUnk, IID_IDrawElemCollection, vtable_offset_local+8, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDrawElemCollection.__dict__ and type(IDrawElemCollection.__dict__[attrname]) == property:
            return IDrawElemCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IDrawElemCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IDrawElem":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def item(self, index:int) -> "IDrawElem":
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the strings in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppUnk:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppUnk.COM_val)))
            return arg_ppUnk.python_val

    def clear(self) -> None:
        """Clears the contents of the collection and updates the display."""
        agcls.evaluate_hresult(self.__dict__["_clear"]())

    def add(self, elemType:str) -> "IDrawElem":
        """Factory to create and add a new element to the end of the sequence."""
        with agmarshall.BSTR_arg(elemType) as arg_elemType, \
             agmarshall.AgInterface_out_arg() as arg_ppDrawElem:
            agcls.evaluate_hresult(self.__dict__["_add"](arg_elemType.COM_val, byref(arg_ppDrawElem.COM_val)))
            return arg_ppDrawElem.python_val

    def remove(self, drawElem:"IDrawElem") -> None:
        """Remove the specified element."""
        with agmarshall.AgInterface_in_arg(drawElem, IDrawElem) as arg_drawElem:
            agcls.evaluate_hresult(self.__dict__["_remove"](arg_drawElem.COM_val))

    @property
    def visible(self) -> bool:
        """Show or hide all the elements."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_visible"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @visible.setter
    def visible(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_visible"](arg_newVal.COM_val))

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{3D6D784D-7C84-4A30-95D8-7D57AF7C560E}", IDrawElemCollection)
agcls.AgTypeNameMap["IDrawElemCollection"] = IDrawElemCollection

class IWinProjectionPosition(object):
    """Projected window position detail."""
    _uuid = "{56FF29E4-6311-4E94-B91D-53C02288C55A}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_x_position"] = _raise_uninitialized_error
        self.__dict__["_get_y_position"] = _raise_uninitialized_error
        self.__dict__["_get_is_win_projection_position_valid"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IWinProjectionPosition._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IWinProjectionPosition from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IWinProjectionPosition = agcom.GUID(IWinProjectionPosition._uuid)
        vtable_offset_local = IWinProjectionPosition._vtable_offset - 1
        self.__dict__["_get_x_position"] = IAGFUNCTYPE(pUnk, IID_IWinProjectionPosition, vtable_offset_local+1, POINTER(agcom.DOUBLE))
        self.__dict__["_get_y_position"] = IAGFUNCTYPE(pUnk, IID_IWinProjectionPosition, vtable_offset_local+2, POINTER(agcom.DOUBLE))
        self.__dict__["_get_is_win_projection_position_valid"] = IAGFUNCTYPE(pUnk, IID_IWinProjectionPosition, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IWinProjectionPosition.__dict__ and type(IWinProjectionPosition.__dict__[attrname]) == property:
            return IWinProjectionPosition.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IWinProjectionPosition.")
    
    @property
    def x_position(self) -> float:
        """Projected window X position."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_x_position"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def y_position(self) -> float:
        """Projected window Y position."""
        with agmarshall.DOUBLE_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_y_position"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def is_win_projection_position_valid(self) -> bool:
        """Indicates if the returned projected position is valid or not."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pIsValid:
            agcls.evaluate_hresult(self.__dict__["_get_is_win_projection_position_valid"](byref(arg_pIsValid.COM_val)))
            return arg_pIsValid.python_val


agcls.AgClassCatalog.add_catalog_entry("{56FF29E4-6311-4E94-B91D-53C02288C55A}", IWinProjectionPosition)
agcls.AgTypeNameMap["IWinProjectionPosition"] = IWinProjectionPosition

class IDrawElemLine(IDrawElem):
    """Defines a line in control coordinates."""
    _uuid = "{1A550DDC-7769-4A6C-9D0C-8E9D8C1757E2}"
    _num_methods = 11
    _vtable_offset = IDrawElem._vtable_offset + IDrawElem._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_left"] = _raise_uninitialized_error
        self.__dict__["_get_right"] = _raise_uninitialized_error
        self.__dict__["_get_top"] = _raise_uninitialized_error
        self.__dict__["_get_bottom"] = _raise_uninitialized_error
        self.__dict__["_set"] = _raise_uninitialized_error
        self.__dict__["_get_color"] = _raise_uninitialized_error
        self.__dict__["_set_color"] = _raise_uninitialized_error
        self.__dict__["_get_line_width"] = _raise_uninitialized_error
        self.__dict__["_set_line_width"] = _raise_uninitialized_error
        self.__dict__["_get_line_style"] = _raise_uninitialized_error
        self.__dict__["_set_line_style"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDrawElemLine._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDrawElemLine from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDrawElem._private_init(self, pUnk)
        IID_IDrawElemLine = agcom.GUID(IDrawElemLine._uuid)
        vtable_offset_local = IDrawElemLine._vtable_offset - 1
        self.__dict__["_get_left"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+1, POINTER(agcom.OLE_XPOS_PIXELS))
        self.__dict__["_get_right"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+2, POINTER(agcom.OLE_XPOS_PIXELS))
        self.__dict__["_get_top"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+3, POINTER(agcom.OLE_YPOS_PIXELS))
        self.__dict__["_get_bottom"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+4, POINTER(agcom.OLE_YPOS_PIXELS))
        self.__dict__["_set"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+5, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS)
        self.__dict__["_get_color"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+6, POINTER(agcom.OLE_COLOR))
        self.__dict__["_set_color"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+7, agcom.OLE_COLOR)
        self.__dict__["_get_line_width"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+8, POINTER(agcom.FLOAT))
        self.__dict__["_set_line_width"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+9, agcom.FLOAT)
        self.__dict__["_get_line_style"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_set_line_style"] = IAGFUNCTYPE(pUnk, IID_IDrawElemLine, vtable_offset_local+11, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDrawElemLine.__dict__ and type(IDrawElemLine.__dict__[attrname]) == property:
            return IDrawElemLine.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            IDrawElem.__setattr__(self, attrname, value)
    
    @property
    def left(self) -> int:
        """The x-coordinate of the left edge of this line."""
        with agmarshall.OLE_XPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_left"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def right(self) -> int:
        """The x-coordinate of the right edge of this line."""
        with agmarshall.OLE_XPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_right"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def top(self) -> int:
        """The y-coordinate of the top edge of this line."""
        with agmarshall.OLE_YPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_top"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def bottom(self) -> int:
        """The y-coordinate of the bottom edge of this line."""
        with agmarshall.OLE_YPOS_PIXELS_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_bottom"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def set(self, left:int, top:int, right:int, bottom:int) -> None:
        """Set the rectangle coordinates."""
        with agmarshall.OLE_XPOS_PIXELS_arg(left) as arg_left, \
             agmarshall.OLE_YPOS_PIXELS_arg(top) as arg_top, \
             agmarshall.OLE_XPOS_PIXELS_arg(right) as arg_right, \
             agmarshall.OLE_YPOS_PIXELS_arg(bottom) as arg_bottom:
            agcls.evaluate_hresult(self.__dict__["_set"](arg_left.COM_val, arg_top.COM_val, arg_right.COM_val, arg_bottom.COM_val))

    @property
    def color(self) -> agcolor.Color:
        """Color of the rectangle."""
        with agmarshall.OLE_COLOR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_color"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @color.setter
    def color(self, newVal:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_color"](arg_newVal.COM_val))

    @property
    def line_width(self) -> float:
        """Specifies the width of the line."""
        with agmarshall.FLOAT_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_line_width"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @line_width.setter
    def line_width(self, newVal:float) -> None:
        with agmarshall.FLOAT_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_line_width"](arg_newVal.COM_val))

    @property
    def line_style(self) -> "LINE_STYLE":
        """Specifies the style of the line."""
        with agmarshall.AgEnum_arg(LINE_STYLE) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_line_style"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @line_style.setter
    def line_style(self, newVal:"LINE_STYLE") -> None:
        with agmarshall.AgEnum_arg(LINE_STYLE, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_line_style"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{1A550DDC-7769-4A6C-9D0C-8E9D8C1757E2}", IDrawElemLine)
agcls.AgTypeNameMap["IDrawElemLine"] = IDrawElemLine

class IExecCmdResult(object):
    """Collection of strings returned by the ExecuteCommand."""
    _uuid = "{90EF2D03-F064-4F54-9E02-6E34E3CF5D55}"
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_range"] = _raise_uninitialized_error
        self.__dict__["_get_is_succeeded"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IExecCmdResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IExecCmdResult from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IExecCmdResult = agcom.GUID(IExecCmdResult._uuid)
        vtable_offset_local = IExecCmdResult._vtable_offset - 1
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_range"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+4, agcom.LONG, agcom.LONG, POINTER(agcom.SAFEARRAY))
        self.__dict__["_get_is_succeeded"] = IAGFUNCTYPE(pUnk, IID_IExecCmdResult, vtable_offset_local+5, POINTER(agcom.VARIANT_BOOL))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IExecCmdResult.__dict__ and type(IExecCmdResult.__dict__[attrname]) == property:
            return IExecCmdResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IExecCmdResult.")
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
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def item(self, index:int) -> str:
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pItem:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pItem.COM_val)))
            return arg_pItem.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the strings in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    def range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        with agmarshall.LONG_arg(startIndex) as arg_startIndex, \
             agmarshall.LONG_arg(stopIndex) as arg_stopIndex, \
             agmarshall.SAFEARRAY_arg() as arg_ppVar:
            agcls.evaluate_hresult(self.__dict__["_range"](arg_startIndex.COM_val, arg_stopIndex.COM_val, byref(arg_ppVar.COM_val)))
            return arg_ppVar.python_val

    @property
    def is_succeeded(self) -> bool:
        """Indicates whether the object contains valid results."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_is_succeeded"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{90EF2D03-F064-4F54-9E02-6E34E3CF5D55}", IExecCmdResult)
agcls.AgTypeNameMap["IExecCmdResult"] = IExecCmdResult

class IExecMultiCmdResult(object):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    _uuid = "{0558BE8E-AF66-4F52-9C6D-76962FC52577}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IExecMultiCmdResult._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IExecMultiCmdResult from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IExecMultiCmdResult = agcom.GUID(IExecMultiCmdResult._uuid)
        vtable_offset_local = IExecMultiCmdResult._vtable_offset - 1
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IExecMultiCmdResult, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IExecMultiCmdResult, vtable_offset_local+2, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IExecMultiCmdResult, vtable_offset_local+3, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IExecMultiCmdResult.__dict__ and type(IExecMultiCmdResult.__dict__[attrname]) == property:
            return IExecMultiCmdResult.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IExecMultiCmdResult.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IExecCmdResult":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval, clear_variant=True)
    
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        with agmarshall.LONG_arg() as arg_pCount:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pCount.COM_val)))
            return arg_pCount.python_val

    def item(self, index:int) -> "IExecCmdResult":
        """Gets the element at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the objects in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppEnum:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppEnum.COM_val)))
            return arg_ppEnum.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{0558BE8E-AF66-4F52-9C6D-76962FC52577}", IExecMultiCmdResult)
agcls.AgTypeNameMap["IExecMultiCmdResult"] = IExecMultiCmdResult

class IUiAxGraphics3DCntrl(object):
    """AGI Globe control."""
    _uuid = "{0975BA23-E273-4B8F-BA8D-32ECB328C092}"
    _num_methods = 48
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_back_color"] = _raise_uninitialized_error
        self.__dict__["_set_back_color"] = _raise_uninitialized_error
        self.__dict__["_get_picture"] = _raise_uninitialized_error
        self.__dict__["_picture_put_reference"] = _raise_uninitialized_error
        self.__dict__["_set_picture"] = _raise_uninitialized_error
        self.__dict__["_pick_info"] = _raise_uninitialized_error
        self.__dict__["_get_win_id"] = _raise_uninitialized_error
        self.__dict__["_set_win_id"] = _raise_uninitialized_error
        self.__dict__["_get_application"] = _raise_uninitialized_error
        self.__dict__["_zoom_in"] = _raise_uninitialized_error
        self.__dict__["_get_no_logo"] = _raise_uninitialized_error
        self.__dict__["_set_no_logo"] = _raise_uninitialized_error
        self.__dict__["_get_ole_drop_mode"] = _raise_uninitialized_error
        self.__dict__["_set_ole_drop_mode"] = _raise_uninitialized_error
        self.__dict__["_get_vendor_id"] = _raise_uninitialized_error
        self.__dict__["_set_vendor_id"] = _raise_uninitialized_error
        self.__dict__["_rubber_band_pick_info"] = _raise_uninitialized_error
        self.__dict__["_get_mouse_mode"] = _raise_uninitialized_error
        self.__dict__["_set_mouse_mode"] = _raise_uninitialized_error
        self.__dict__["_get_draw_elements"] = _raise_uninitialized_error
        self.__dict__["_get_ready_state"] = _raise_uninitialized_error
        self.__dict__["_get_ppt_preload_mode"] = _raise_uninitialized_error
        self.__dict__["_set_ppt_preload_mode"] = _raise_uninitialized_error
        self.__dict__["_get_advanced_pick_mode"] = _raise_uninitialized_error
        self.__dict__["_set_advanced_pick_mode"] = _raise_uninitialized_error
        self.__dict__["_copy_from_win_id"] = _raise_uninitialized_error
        self.__dict__["_start_object_editing"] = _raise_uninitialized_error
        self.__dict__["_apply_object_editing"] = _raise_uninitialized_error
        self.__dict__["_stop_object_editing"] = _raise_uninitialized_error
        self.__dict__["_get_is_object_editing"] = _raise_uninitialized_error
        self.__dict__["_get_in_zoom_mode"] = _raise_uninitialized_error
        self.__dict__["_set_mouse_cursor_from_file"] = _raise_uninitialized_error
        self.__dict__["_restore_mouse_cursor"] = _raise_uninitialized_error
        self.__dict__["_set_mouse_cursor_from_handle"] = _raise_uninitialized_error
        self.__dict__["_get_show_progress_image"] = _raise_uninitialized_error
        self.__dict__["_set_show_progress_image"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_x_offset"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_x_offset"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_y_offset"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_y_offset"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_file"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_file"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_x_origin"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_x_origin"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_y_origin"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_y_origin"] = _raise_uninitialized_error
        self.__dict__["_get_picture_from_file"] = _raise_uninitialized_error
        self.__dict__["_set_picture_from_file"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiAxGraphics3DCntrl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiAxGraphics3DCntrl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiAxGraphics3DCntrl = agcom.GUID(IUiAxGraphics3DCntrl._uuid)
        vtable_offset_local = IUiAxGraphics3DCntrl._vtable_offset - 1
        self.__dict__["_get_back_color"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+1, POINTER(agcom.OLE_COLOR))
        self.__dict__["_set_back_color"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+2, agcom.OLE_COLOR)
        self.__dict__["_get_picture"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_picture_put_reference"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+4, agcom.PVOID)
        self.__dict__["_set_picture"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+5, agcom.PVOID)
        self.__dict__["_pick_info"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+6, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID))
        self.__dict__["_get_win_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+7, POINTER(agcom.LONG))
        self.__dict__["_set_win_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+8, agcom.LONG)
        self.__dict__["_get_application"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+9, POINTER(agcom.PVOID))
        self.__dict__["_zoom_in"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+10, )
        self.__dict__["_get_no_logo"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+11, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_no_logo"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+12, agcom.VARIANT_BOOL)
        self.__dict__["_get_ole_drop_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+13, POINTER(agcom.LONG))
        self.__dict__["_set_ole_drop_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+14, agcom.LONG)
        self.__dict__["_get_vendor_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+15, POINTER(agcom.BSTR))
        self.__dict__["_set_vendor_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+16, agcom.BSTR)
        self.__dict__["_rubber_band_pick_info"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+17, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID))
        self.__dict__["_get_mouse_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+18, POINTER(agcom.LONG))
        self.__dict__["_set_mouse_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+19, agcom.LONG)
        self.__dict__["_get_draw_elements"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+20, POINTER(agcom.PVOID))
        self.__dict__["_get_ready_state"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+21, POINTER(agcom.LONG))
        self.__dict__["_get_ppt_preload_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+22, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_ppt_preload_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+23, agcom.VARIANT_BOOL)
        self.__dict__["_get_advanced_pick_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+24, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_advanced_pick_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+25, agcom.VARIANT_BOOL)
        self.__dict__["_copy_from_win_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+26, agcom.LONG)
        self.__dict__["_start_object_editing"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+27, agcom.BSTR)
        self.__dict__["_apply_object_editing"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+28, )
        self.__dict__["_stop_object_editing"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+29, agcom.VARIANT_BOOL)
        self.__dict__["_get_is_object_editing"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+30, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_in_zoom_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+31, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_mouse_cursor_from_file"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+32, agcom.BSTR)
        self.__dict__["_restore_mouse_cursor"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+33, )
        self.__dict__["_set_mouse_cursor_from_handle"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+34, agcom.OLE_HANDLE)
        self.__dict__["_get_show_progress_image"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+35, POINTER(agcom.LONG))
        self.__dict__["_set_show_progress_image"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+36, agcom.LONG)
        self.__dict__["_get_progress_image_x_offset"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+37, POINTER(agcom.LONG))
        self.__dict__["_set_progress_image_x_offset"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+38, agcom.LONG)
        self.__dict__["_get_progress_image_y_offset"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+39, POINTER(agcom.LONG))
        self.__dict__["_set_progress_image_y_offset"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+40, agcom.LONG)
        self.__dict__["_get_progress_image_file"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+41, POINTER(agcom.BSTR))
        self.__dict__["_set_progress_image_file"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+42, agcom.BSTR)
        self.__dict__["_get_progress_image_x_origin"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+43, POINTER(agcom.LONG))
        self.__dict__["_set_progress_image_x_origin"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+44, agcom.LONG)
        self.__dict__["_get_progress_image_y_origin"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+45, POINTER(agcom.LONG))
        self.__dict__["_set_progress_image_y_origin"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+46, agcom.LONG)
        self.__dict__["_get_picture_from_file"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+47, POINTER(agcom.BSTR))
        self.__dict__["_set_picture_from_file"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics3DCntrl, vtable_offset_local+48, agcom.BSTR)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiAxGraphics3DCntrl.__dict__ and type(IUiAxGraphics3DCntrl.__dict__[attrname]) == property:
            return IUiAxGraphics3DCntrl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiAxGraphics3DCntrl.")
    def Subscribe(self) -> IUiAxGraphics3DCntrlEventHandler:
        """Returns an IUiAxGraphics3DCntrlEventHandler that is subscribed to handle events associated with this instance of IUiAxGraphics3DCntrl."""
        return IUiAxGraphics3DCntrlEventHandler(self._pUnk)    
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        with agmarshall.OLE_COLOR_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_get_back_color"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(clr) as arg_clr:
            agcls.evaluate_hresult(self.__dict__["_set_back_color"](arg_clr.COM_val))

    @property
    def picture(self) -> "IPictureDisp":
        """The splash logo graphic to be displayed in the control."""
        with agmarshall.PVOID_arg() as arg_ppPicture:
            agcls.evaluate_hresult(self.__dict__["_get_picture"](byref(arg_ppPicture.COM_val)))
            return arg_ppPicture.python_val

    def picture_put_reference(self, pPicture:"IPictureDisp") -> None:
        with agmarshall.PVOID_arg(pPicture, IPictureDisp) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_picture_put_reference"](arg_pPicture.COM_val))

    @picture.setter
    def picture(self, pPicture:"IPictureDisp") -> None:
        with agmarshall.PVOID_arg(pPicture, IPictureDisp) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_set_picture"](arg_pPicture.COM_val))

    def pick_info(self, x:int, y:int) -> "IPickInfoData":
        """Get detailed information about a mouse pick."""
        with agmarshall.OLE_XPOS_PIXELS_arg(x) as arg_x, \
             agmarshall.OLE_YPOS_PIXELS_arg(y) as arg_y, \
             agmarshall.AgInterface_out_arg() as arg_ppPickData:
            agcls.evaluate_hresult(self.__dict__["_pick_info"](arg_x.COM_val, arg_y.COM_val, byref(arg_ppPickData.COM_val)))
            return arg_ppPickData.python_val

    @property
    def win_id(self) -> int:
        """Window identifier (for Connect commands)."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_win_id"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @win_id.setter
    def win_id(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_win_id"](arg_newVal.COM_val))

    @property
    def application(self) -> "ISTKXApplication":
        """Reference to the STK X application object."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_application"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def zoom_in(self) -> None:
        """Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom."""
        agcls.evaluate_hresult(self.__dict__["_zoom_in"]())

    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pNoLogo:
            agcls.evaluate_hresult(self.__dict__["_get_no_logo"](byref(arg_pNoLogo.COM_val)))
            return arg_pNoLogo.python_val

    @no_logo.setter
    def no_logo(self, bNoLogo:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bNoLogo) as arg_bNoLogo:
            agcls.evaluate_hresult(self.__dict__["_set_no_logo"](arg_bNoLogo.COM_val))

    @property
    def ole_drop_mode(self) -> "OLE_DROP_MODE":
        """How the control handles drop operations."""
        with agmarshall.AgEnum_arg(OLE_DROP_MODE) as arg_psOLEDropMode:
            agcls.evaluate_hresult(self.__dict__["_get_ole_drop_mode"](byref(arg_psOLEDropMode.COM_val)))
            return arg_psOLEDropMode.python_val

    @ole_drop_mode.setter
    def ole_drop_mode(self, psOLEDropMode:"OLE_DROP_MODE") -> None:
        with agmarshall.AgEnum_arg(OLE_DROP_MODE, psOLEDropMode) as arg_psOLEDropMode:
            agcls.evaluate_hresult(self.__dict__["_set_ole_drop_mode"](arg_psOLEDropMode.COM_val))

    @property
    def vendor_id(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_vendor_id"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @vendor_id.setter
    def vendor_id(self, vendorID:str) -> None:
        with agmarshall.BSTR_arg(vendorID) as arg_vendorID:
            agcls.evaluate_hresult(self.__dict__["_set_vendor_id"](arg_vendorID.COM_val))

    def rubber_band_pick_info(self, left:int, top:int, right:int, bottom:int) -> "IRubberBandPickInfoData":
        """Get detailed information about a rubber-band mouse pick. The values must be within the VO window (0 to width-1 for left and right, 0 to height-1 for top and bottom)."""
        with agmarshall.OLE_XPOS_PIXELS_arg(left) as arg_left, \
             agmarshall.OLE_YPOS_PIXELS_arg(top) as arg_top, \
             agmarshall.OLE_XPOS_PIXELS_arg(right) as arg_right, \
             agmarshall.OLE_YPOS_PIXELS_arg(bottom) as arg_bottom, \
             agmarshall.AgInterface_out_arg() as arg_ppPickInfoData:
            agcls.evaluate_hresult(self.__dict__["_rubber_band_pick_info"](arg_left.COM_val, arg_top.COM_val, arg_right.COM_val, arg_bottom.COM_val, byref(arg_ppPickInfoData.COM_val)))
            return arg_ppPickInfoData.python_val

    @property
    def mouse_mode(self) -> "MOUSE_MODE":
        """Whether this control responds to mouse events."""
        with agmarshall.AgEnum_arg(MOUSE_MODE) as arg_psMouseMode:
            agcls.evaluate_hresult(self.__dict__["_get_mouse_mode"](byref(arg_psMouseMode.COM_val)))
            return arg_psMouseMode.python_val

    @mouse_mode.setter
    def mouse_mode(self, psMouseMode:"MOUSE_MODE") -> None:
        with agmarshall.AgEnum_arg(MOUSE_MODE, psMouseMode) as arg_psMouseMode:
            agcls.evaluate_hresult(self.__dict__["_set_mouse_mode"](arg_psMouseMode.COM_val))

    @property
    def draw_elements(self) -> "IDrawElemCollection":
        """Elements to draw on the control."""
        with agmarshall.AgInterface_out_arg() as arg_ppDrawElemColl:
            agcls.evaluate_hresult(self.__dict__["_get_draw_elements"](byref(arg_ppDrawElemColl.COM_val)))
            return arg_ppDrawElemColl.python_val

    @property
    def ready_state(self) -> int:
        """Returns/sets the background color of the control."""
        with agmarshall.LONG_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_get_ready_state"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @property
    def ppt_preload_mode(self) -> bool:
        """Special mode for PowerPoint : if true the VO control window is kept around when switching between slides."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pPptPreloadMode:
            agcls.evaluate_hresult(self.__dict__["_get_ppt_preload_mode"](byref(arg_pPptPreloadMode.COM_val)))
            return arg_pPptPreloadMode.python_val

    @ppt_preload_mode.setter
    def ppt_preload_mode(self, bPptPreloadMode:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bPptPreloadMode) as arg_bPptPreloadMode:
            agcls.evaluate_hresult(self.__dict__["_set_ppt_preload_mode"](arg_bPptPreloadMode.COM_val))

    @property
    def advanced_pick_mode(self) -> bool:
        """If true, sets the advance pick mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pAdvancePickMode:
            agcls.evaluate_hresult(self.__dict__["_get_advanced_pick_mode"](byref(arg_pAdvancePickMode.COM_val)))
            return arg_pAdvancePickMode.python_val

    @advanced_pick_mode.setter
    def advanced_pick_mode(self, bAdvancePickMode:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bAdvancePickMode) as arg_bAdvancePickMode:
            agcls.evaluate_hresult(self.__dict__["_set_advanced_pick_mode"](arg_bAdvancePickMode.COM_val))

    def copy_from_win_id(self, winID:int) -> None:
        """Copies an existing Window's scene into this control"""
        with agmarshall.LONG_arg(winID) as arg_winID:
            agcls.evaluate_hresult(self.__dict__["_copy_from_win_id"](arg_winID.COM_val))

    def start_object_editing(self, objEditPath:str) -> None:
        """Enters into 3D object editing mode."""
        with agmarshall.BSTR_arg(objEditPath) as arg_objEditPath:
            agcls.evaluate_hresult(self.__dict__["_start_object_editing"](arg_objEditPath.COM_val))

    def apply_object_editing(self) -> None:
        """Commits changes when in 3D object editing mode."""
        agcls.evaluate_hresult(self.__dict__["_apply_object_editing"]())

    def stop_object_editing(self, canceled:bool) -> None:
        """Ends 3D object editing mode."""
        with agmarshall.VARIANT_BOOL_arg(canceled) as arg_canceled:
            agcls.evaluate_hresult(self.__dict__["_stop_object_editing"](arg_canceled.COM_val))

    @property
    def is_object_editing(self) -> bool:
        """Returns true if in 3D object editing mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_p3DObjectEditing:
            agcls.evaluate_hresult(self.__dict__["_get_is_object_editing"](byref(arg_p3DObjectEditing.COM_val)))
            return arg_p3DObjectEditing.python_val

    @property
    def in_zoom_mode(self) -> bool:
        """Returns true if in zoom in mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pZoomIn:
            agcls.evaluate_hresult(self.__dict__["_get_in_zoom_mode"](byref(arg_pZoomIn.COM_val)))
            return arg_pZoomIn.python_val

    def set_mouse_cursor_from_file(self, cursorFileName:str) -> None:
        """Sets mouse cursor to the selected cursor file."""
        with agmarshall.BSTR_arg(cursorFileName) as arg_cursorFileName:
            agcls.evaluate_hresult(self.__dict__["_set_mouse_cursor_from_file"](arg_cursorFileName.COM_val))

    def restore_mouse_cursor(self) -> None:
        """Restores mouse cursor back to normal."""
        agcls.evaluate_hresult(self.__dict__["_restore_mouse_cursor"]())

    def set_mouse_cursor_from_handle(self, cursorHandle:int) -> None:
        """Sets mouse cursor to the passed cursor handle."""
        with agmarshall.OLE_HANDLE_arg(cursorHandle) as arg_cursorHandle:
            agcls.evaluate_hresult(self.__dict__["_set_mouse_cursor_from_handle"](arg_cursorHandle.COM_val))

    @property
    def show_progress_image(self) -> "SHOW_PROGRESS_IMAGE":
        """The animated progress image type."""
        with agmarshall.AgEnum_arg(SHOW_PROGRESS_IMAGE) as arg_psProgressImage:
            agcls.evaluate_hresult(self.__dict__["_get_show_progress_image"](byref(arg_psProgressImage.COM_val)))
            return arg_psProgressImage.python_val

    @show_progress_image.setter
    def show_progress_image(self, psProgressImage:"SHOW_PROGRESS_IMAGE") -> None:
        with agmarshall.AgEnum_arg(SHOW_PROGRESS_IMAGE, psProgressImage) as arg_psProgressImage:
            agcls.evaluate_hresult(self.__dict__["_set_show_progress_image"](arg_psProgressImage.COM_val))

    @property
    def progress_image_x_offset(self) -> int:
        """The horizontal X offset for animated progress image."""
        with agmarshall.LONG_arg() as arg_pXOffset:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_x_offset"](byref(arg_pXOffset.COM_val)))
            return arg_pXOffset.python_val

    @progress_image_x_offset.setter
    def progress_image_x_offset(self, xOffset:int) -> None:
        with agmarshall.LONG_arg(xOffset) as arg_xOffset:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_x_offset"](arg_xOffset.COM_val))

    @property
    def progress_image_y_offset(self) -> int:
        """The vertical Y offset for animated progress image."""
        with agmarshall.LONG_arg() as arg_pYOffset:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_y_offset"](byref(arg_pYOffset.COM_val)))
            return arg_pYOffset.python_val

    @progress_image_y_offset.setter
    def progress_image_y_offset(self, yOffset:int) -> None:
        with agmarshall.LONG_arg(yOffset) as arg_yOffset:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_y_offset"](arg_yOffset.COM_val))

    @property
    def progress_image_file(self) -> str:
        """The complete image file name/path for animated progress image."""
        with agmarshall.BSTR_arg() as arg_pImageFile:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_file"](byref(arg_pImageFile.COM_val)))
            return arg_pImageFile.python_val

    @progress_image_file.setter
    def progress_image_file(self, imageFile:str) -> None:
        with agmarshall.BSTR_arg(imageFile) as arg_imageFile:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_file"](arg_imageFile.COM_val))

    @property
    def progress_image_x_origin(self) -> "PROGRESS_IMAGE_X_ORIGIN":
        """The X origin alignment for animated progress image."""
        with agmarshall.AgEnum_arg(PROGRESS_IMAGE_X_ORIGIN) as arg_psProgressImageXOrigin:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_x_origin"](byref(arg_psProgressImageXOrigin.COM_val)))
            return arg_psProgressImageXOrigin.python_val

    @progress_image_x_origin.setter
    def progress_image_x_origin(self, progressImageXOrigin:"PROGRESS_IMAGE_X_ORIGIN") -> None:
        with agmarshall.AgEnum_arg(PROGRESS_IMAGE_X_ORIGIN, progressImageXOrigin) as arg_progressImageXOrigin:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_x_origin"](arg_progressImageXOrigin.COM_val))

    @property
    def progress_image_y_origin(self) -> "PROGRESS_IMAGE_Y_ORIGIN":
        """The Y origin alignment for animated progress image."""
        with agmarshall.AgEnum_arg(PROGRESS_IMAGE_Y_ORIGIN) as arg_psProgressImageYOrigin:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_y_origin"](byref(arg_psProgressImageYOrigin.COM_val)))
            return arg_psProgressImageYOrigin.python_val

    @progress_image_y_origin.setter
    def progress_image_y_origin(self, progressImageYOrigin:"PROGRESS_IMAGE_Y_ORIGIN") -> None:
        with agmarshall.AgEnum_arg(PROGRESS_IMAGE_Y_ORIGIN, progressImageYOrigin) as arg_progressImageYOrigin:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_y_origin"](arg_progressImageYOrigin.COM_val))

    @property
    def picture_from_file(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg() as arg_pPictureFile:
            agcls.evaluate_hresult(self.__dict__["_get_picture_from_file"](byref(arg_pPictureFile.COM_val)))
            return arg_pPictureFile.python_val

    @picture_from_file.setter
    def picture_from_file(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg(pictureFile) as arg_pictureFile:
            agcls.evaluate_hresult(self.__dict__["_set_picture_from_file"](arg_pictureFile.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{0975BA23-E273-4B8F-BA8D-32ECB328C092}", IUiAxGraphics3DCntrl)
agcls.AgTypeNameMap["IUiAxGraphics3DCntrl"] = IUiAxGraphics3DCntrl

class IUiAx2DCntrl(object):
    """AGI Map control."""
    _uuid = "{A5C18751-1656-4FB9-BA4E-D5746D509CFC}"
    _num_methods = 45
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_back_color"] = _raise_uninitialized_error
        self.__dict__["_set_back_color"] = _raise_uninitialized_error
        self.__dict__["_get_picture"] = _raise_uninitialized_error
        self.__dict__["_picture_put_reference"] = _raise_uninitialized_error
        self.__dict__["_set_picture"] = _raise_uninitialized_error
        self.__dict__["_get_win_id"] = _raise_uninitialized_error
        self.__dict__["_set_win_id"] = _raise_uninitialized_error
        self.__dict__["_zoom_in"] = _raise_uninitialized_error
        self.__dict__["_zoom_out"] = _raise_uninitialized_error
        self.__dict__["_pick_info"] = _raise_uninitialized_error
        self.__dict__["_get_application"] = _raise_uninitialized_error
        self.__dict__["_get_no_logo"] = _raise_uninitialized_error
        self.__dict__["_set_no_logo"] = _raise_uninitialized_error
        self.__dict__["_get_ole_drop_mode"] = _raise_uninitialized_error
        self.__dict__["_set_ole_drop_mode"] = _raise_uninitialized_error
        self.__dict__["_get_vendor_id"] = _raise_uninitialized_error
        self.__dict__["_set_vendor_id"] = _raise_uninitialized_error
        self.__dict__["_get_mouse_mode"] = _raise_uninitialized_error
        self.__dict__["_set_mouse_mode"] = _raise_uninitialized_error
        self.__dict__["_get_ready_state"] = _raise_uninitialized_error
        self.__dict__["_copy_from_win_id"] = _raise_uninitialized_error
        self.__dict__["_rubber_band_pick_info"] = _raise_uninitialized_error
        self.__dict__["_get_advanced_pick_mode"] = _raise_uninitialized_error
        self.__dict__["_set_advanced_pick_mode"] = _raise_uninitialized_error
        self.__dict__["_get_window_projected_position"] = _raise_uninitialized_error
        self.__dict__["_get_in_zoom_mode"] = _raise_uninitialized_error
        self.__dict__["_set_mouse_cursor_from_file"] = _raise_uninitialized_error
        self.__dict__["_restore_mouse_cursor"] = _raise_uninitialized_error
        self.__dict__["_set_mouse_cursor_from_handle"] = _raise_uninitialized_error
        self.__dict__["_get_show_progress_image"] = _raise_uninitialized_error
        self.__dict__["_set_show_progress_image"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_x_offset"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_x_offset"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_y_offset"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_y_offset"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_file"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_file"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_x_origin"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_x_origin"] = _raise_uninitialized_error
        self.__dict__["_get_progress_image_y_origin"] = _raise_uninitialized_error
        self.__dict__["_set_progress_image_y_origin"] = _raise_uninitialized_error
        self.__dict__["_get_picture_from_file"] = _raise_uninitialized_error
        self.__dict__["_set_picture_from_file"] = _raise_uninitialized_error
        self.__dict__["_get_pan_mode_enabled"] = _raise_uninitialized_error
        self.__dict__["_set_pan_mode_enabled"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiAx2DCntrl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiAx2DCntrl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiAx2DCntrl = agcom.GUID(IUiAx2DCntrl._uuid)
        vtable_offset_local = IUiAx2DCntrl._vtable_offset - 1
        self.__dict__["_get_back_color"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+1, POINTER(agcom.OLE_COLOR))
        self.__dict__["_set_back_color"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+2, agcom.OLE_COLOR)
        self.__dict__["_get_picture"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_picture_put_reference"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+4, agcom.PVOID)
        self.__dict__["_set_picture"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+5, agcom.PVOID)
        self.__dict__["_get_win_id"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+6, POINTER(agcom.LONG))
        self.__dict__["_set_win_id"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+7, agcom.LONG)
        self.__dict__["_zoom_in"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+8, )
        self.__dict__["_zoom_out"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+9, )
        self.__dict__["_pick_info"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+10, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID))
        self.__dict__["_get_application"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+11, POINTER(agcom.PVOID))
        self.__dict__["_get_no_logo"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+12, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_no_logo"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+13, agcom.VARIANT_BOOL)
        self.__dict__["_get_ole_drop_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+14, POINTER(agcom.LONG))
        self.__dict__["_set_ole_drop_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+15, agcom.LONG)
        self.__dict__["_get_vendor_id"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+16, POINTER(agcom.BSTR))
        self.__dict__["_set_vendor_id"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+17, agcom.BSTR)
        self.__dict__["_get_mouse_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+18, POINTER(agcom.LONG))
        self.__dict__["_set_mouse_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+19, agcom.LONG)
        self.__dict__["_get_ready_state"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+20, POINTER(agcom.LONG))
        self.__dict__["_copy_from_win_id"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+21, agcom.LONG)
        self.__dict__["_rubber_band_pick_info"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+22, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID))
        self.__dict__["_get_advanced_pick_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+23, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_advanced_pick_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+24, agcom.VARIANT_BOOL)
        self.__dict__["_get_window_projected_position"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+25, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get_in_zoom_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+26, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_mouse_cursor_from_file"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+27, agcom.BSTR)
        self.__dict__["_restore_mouse_cursor"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+28, )
        self.__dict__["_set_mouse_cursor_from_handle"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+29, agcom.OLE_HANDLE)
        self.__dict__["_get_show_progress_image"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+30, POINTER(agcom.LONG))
        self.__dict__["_set_show_progress_image"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+31, agcom.LONG)
        self.__dict__["_get_progress_image_x_offset"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+32, POINTER(agcom.LONG))
        self.__dict__["_set_progress_image_x_offset"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+33, agcom.LONG)
        self.__dict__["_get_progress_image_y_offset"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+34, POINTER(agcom.LONG))
        self.__dict__["_set_progress_image_y_offset"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+35, agcom.LONG)
        self.__dict__["_get_progress_image_file"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+36, POINTER(agcom.BSTR))
        self.__dict__["_set_progress_image_file"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+37, agcom.BSTR)
        self.__dict__["_get_progress_image_x_origin"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+38, POINTER(agcom.LONG))
        self.__dict__["_set_progress_image_x_origin"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+39, agcom.LONG)
        self.__dict__["_get_progress_image_y_origin"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+40, POINTER(agcom.LONG))
        self.__dict__["_set_progress_image_y_origin"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+41, agcom.LONG)
        self.__dict__["_get_picture_from_file"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+42, POINTER(agcom.BSTR))
        self.__dict__["_set_picture_from_file"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+43, agcom.BSTR)
        self.__dict__["_get_pan_mode_enabled"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+44, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_pan_mode_enabled"] = IAGFUNCTYPE(pUnk, IID_IUiAx2DCntrl, vtable_offset_local+45, agcom.VARIANT_BOOL)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiAx2DCntrl.__dict__ and type(IUiAx2DCntrl.__dict__[attrname]) == property:
            return IUiAx2DCntrl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiAx2DCntrl.")
    def Subscribe(self) -> IUiAxGraphics2DCntrlEventHandler:
        """Returns an IUiAxGraphics2DCntrlEventHandler that is subscribed to handle events associated with this instance of IUiAx2DCntrl."""
        return IUiAxGraphics2DCntrlEventHandler(self._pUnk)    
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        with agmarshall.OLE_COLOR_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_get_back_color"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(clr) as arg_clr:
            agcls.evaluate_hresult(self.__dict__["_set_back_color"](arg_clr.COM_val))

    @property
    def picture(self) -> "IPictureDisp":
        """The splash logo graphic to be displayed in the control."""
        with agmarshall.PVOID_arg() as arg_ppPicture:
            agcls.evaluate_hresult(self.__dict__["_get_picture"](byref(arg_ppPicture.COM_val)))
            return arg_ppPicture.python_val

    def picture_put_reference(self, pPicture:"IPictureDisp") -> None:
        with agmarshall.PVOID_arg(pPicture, IPictureDisp) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_picture_put_reference"](arg_pPicture.COM_val))

    @picture.setter
    def picture(self, pPicture:"IPictureDisp") -> None:
        with agmarshall.PVOID_arg(pPicture, IPictureDisp) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_set_picture"](arg_pPicture.COM_val))

    @property
    def win_id(self) -> int:
        """Window identifier (for Connect commands)."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_win_id"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @win_id.setter
    def win_id(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_win_id"](arg_newVal.COM_val))

    def zoom_in(self) -> None:
        """Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom."""
        agcls.evaluate_hresult(self.__dict__["_zoom_in"]())

    def zoom_out(self) -> None:
        """Zoom out to view a larger portion of a previously magnified map."""
        agcls.evaluate_hresult(self.__dict__["_zoom_out"]())

    def pick_info(self, x:int, y:int) -> "IPickInfoData":
        """Get detailed information about a mouse pick."""
        with agmarshall.OLE_XPOS_PIXELS_arg(x) as arg_x, \
             agmarshall.OLE_YPOS_PIXELS_arg(y) as arg_y, \
             agmarshall.AgInterface_out_arg() as arg_ppPickData:
            agcls.evaluate_hresult(self.__dict__["_pick_info"](arg_x.COM_val, arg_y.COM_val, byref(arg_ppPickData.COM_val)))
            return arg_ppPickData.python_val

    @property
    def application(self) -> "ISTKXApplication":
        """Reference to the STK X application object."""
        with agmarshall.AgInterface_out_arg() as arg_ppApp:
            agcls.evaluate_hresult(self.__dict__["_get_application"](byref(arg_ppApp.COM_val)))
            return arg_ppApp.python_val

    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pNoLogo:
            agcls.evaluate_hresult(self.__dict__["_get_no_logo"](byref(arg_pNoLogo.COM_val)))
            return arg_pNoLogo.python_val

    @no_logo.setter
    def no_logo(self, bNoLogo:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bNoLogo) as arg_bNoLogo:
            agcls.evaluate_hresult(self.__dict__["_set_no_logo"](arg_bNoLogo.COM_val))

    @property
    def ole_drop_mode(self) -> "OLE_DROP_MODE":
        """How the control handles drop operations."""
        with agmarshall.AgEnum_arg(OLE_DROP_MODE) as arg_psOLEDropMode:
            agcls.evaluate_hresult(self.__dict__["_get_ole_drop_mode"](byref(arg_psOLEDropMode.COM_val)))
            return arg_psOLEDropMode.python_val

    @ole_drop_mode.setter
    def ole_drop_mode(self, psOLEDropMode:"OLE_DROP_MODE") -> None:
        with agmarshall.AgEnum_arg(OLE_DROP_MODE, psOLEDropMode) as arg_psOLEDropMode:
            agcls.evaluate_hresult(self.__dict__["_set_ole_drop_mode"](arg_psOLEDropMode.COM_val))

    @property
    def vendor_id(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_vendor_id"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @vendor_id.setter
    def vendor_id(self, vendorID:str) -> None:
        with agmarshall.BSTR_arg(vendorID) as arg_vendorID:
            agcls.evaluate_hresult(self.__dict__["_set_vendor_id"](arg_vendorID.COM_val))

    @property
    def mouse_mode(self) -> "MOUSE_MODE":
        """Whether this control responds to mouse events."""
        with agmarshall.AgEnum_arg(MOUSE_MODE) as arg_psMouseMode:
            agcls.evaluate_hresult(self.__dict__["_get_mouse_mode"](byref(arg_psMouseMode.COM_val)))
            return arg_psMouseMode.python_val

    @mouse_mode.setter
    def mouse_mode(self, psMouseMode:"MOUSE_MODE") -> None:
        with agmarshall.AgEnum_arg(MOUSE_MODE, psMouseMode) as arg_psMouseMode:
            agcls.evaluate_hresult(self.__dict__["_set_mouse_mode"](arg_psMouseMode.COM_val))

    @property
    def ready_state(self) -> int:
        """Returns/sets the background color of the control."""
        with agmarshall.LONG_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_get_ready_state"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    def copy_from_win_id(self, winID:int) -> None:
        """Copies an existing Window's scene into this control"""
        with agmarshall.LONG_arg(winID) as arg_winID:
            agcls.evaluate_hresult(self.__dict__["_copy_from_win_id"](arg_winID.COM_val))

    def rubber_band_pick_info(self, left:int, top:int, right:int, bottom:int) -> "IRubberBandPickInfoData":
        """Get detailed information about a rubber-band mouse pick. The values must be within the 2D window (0 to width-1 for left and right, 0 to height-1 for top and bottom)."""
        with agmarshall.OLE_XPOS_PIXELS_arg(left) as arg_left, \
             agmarshall.OLE_YPOS_PIXELS_arg(top) as arg_top, \
             agmarshall.OLE_XPOS_PIXELS_arg(right) as arg_right, \
             agmarshall.OLE_YPOS_PIXELS_arg(bottom) as arg_bottom, \
             agmarshall.AgInterface_out_arg() as arg_ppPickInfoData:
            agcls.evaluate_hresult(self.__dict__["_rubber_band_pick_info"](arg_left.COM_val, arg_top.COM_val, arg_right.COM_val, arg_bottom.COM_val, byref(arg_ppPickInfoData.COM_val)))
            return arg_ppPickInfoData.python_val

    @property
    def advanced_pick_mode(self) -> bool:
        """If true, sets the advance pick mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pAdvancePickMode:
            agcls.evaluate_hresult(self.__dict__["_get_advanced_pick_mode"](byref(arg_pAdvancePickMode.COM_val)))
            return arg_pAdvancePickMode.python_val

    @advanced_pick_mode.setter
    def advanced_pick_mode(self, bAdvancePickMode:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bAdvancePickMode) as arg_bAdvancePickMode:
            agcls.evaluate_hresult(self.__dict__["_set_advanced_pick_mode"](arg_bAdvancePickMode.COM_val))

    def get_window_projected_position(self, lat:float, lon:float, alt:float, drawCoords:"GRAPHICS_2D_DRAW_COORDS") -> "IWinProjectionPosition":
        """Get the window projected position for given values."""
        with agmarshall.DOUBLE_arg(lat) as arg_lat, \
             agmarshall.DOUBLE_arg(lon) as arg_lon, \
             agmarshall.DOUBLE_arg(alt) as arg_alt, \
             agmarshall.AgEnum_arg(GRAPHICS_2D_DRAW_COORDS, drawCoords) as arg_drawCoords, \
             agmarshall.AgInterface_out_arg() as arg_ppWinProjPos:
            agcls.evaluate_hresult(self.__dict__["_get_window_projected_position"](arg_lat.COM_val, arg_lon.COM_val, arg_alt.COM_val, arg_drawCoords.COM_val, byref(arg_ppWinProjPos.COM_val)))
            return arg_ppWinProjPos.python_val

    @property
    def in_zoom_mode(self) -> bool:
        """Returns true if in zoom in mode."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pZoomIn:
            agcls.evaluate_hresult(self.__dict__["_get_in_zoom_mode"](byref(arg_pZoomIn.COM_val)))
            return arg_pZoomIn.python_val

    def set_mouse_cursor_from_file(self, cursorFileName:str) -> None:
        """Sets mouse cursor to the selected cursor file."""
        with agmarshall.BSTR_arg(cursorFileName) as arg_cursorFileName:
            agcls.evaluate_hresult(self.__dict__["_set_mouse_cursor_from_file"](arg_cursorFileName.COM_val))

    def restore_mouse_cursor(self) -> None:
        """Restores mouse cursor back to normal."""
        agcls.evaluate_hresult(self.__dict__["_restore_mouse_cursor"]())

    def set_mouse_cursor_from_handle(self, cursorHandle:int) -> None:
        """Sets mouse cursor to the passed cursor handle."""
        with agmarshall.OLE_HANDLE_arg(cursorHandle) as arg_cursorHandle:
            agcls.evaluate_hresult(self.__dict__["_set_mouse_cursor_from_handle"](arg_cursorHandle.COM_val))

    @property
    def show_progress_image(self) -> "SHOW_PROGRESS_IMAGE":
        """The animated progress image type."""
        with agmarshall.AgEnum_arg(SHOW_PROGRESS_IMAGE) as arg_psProgressImage:
            agcls.evaluate_hresult(self.__dict__["_get_show_progress_image"](byref(arg_psProgressImage.COM_val)))
            return arg_psProgressImage.python_val

    @show_progress_image.setter
    def show_progress_image(self, psProgressImage:"SHOW_PROGRESS_IMAGE") -> None:
        with agmarshall.AgEnum_arg(SHOW_PROGRESS_IMAGE, psProgressImage) as arg_psProgressImage:
            agcls.evaluate_hresult(self.__dict__["_set_show_progress_image"](arg_psProgressImage.COM_val))

    @property
    def progress_image_x_offset(self) -> int:
        """The horizontal X offset for animated progress image."""
        with agmarshall.LONG_arg() as arg_pXOffset:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_x_offset"](byref(arg_pXOffset.COM_val)))
            return arg_pXOffset.python_val

    @progress_image_x_offset.setter
    def progress_image_x_offset(self, xOffset:int) -> None:
        with agmarshall.LONG_arg(xOffset) as arg_xOffset:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_x_offset"](arg_xOffset.COM_val))

    @property
    def progress_image_y_offset(self) -> int:
        """The vertical Y offset for animated progress image."""
        with agmarshall.LONG_arg() as arg_pYOffset:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_y_offset"](byref(arg_pYOffset.COM_val)))
            return arg_pYOffset.python_val

    @progress_image_y_offset.setter
    def progress_image_y_offset(self, yOffset:int) -> None:
        with agmarshall.LONG_arg(yOffset) as arg_yOffset:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_y_offset"](arg_yOffset.COM_val))

    @property
    def progress_image_file(self) -> str:
        """The complete image file name/path for animated progress image."""
        with agmarshall.BSTR_arg() as arg_pImageFile:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_file"](byref(arg_pImageFile.COM_val)))
            return arg_pImageFile.python_val

    @progress_image_file.setter
    def progress_image_file(self, imageFile:str) -> None:
        with agmarshall.BSTR_arg(imageFile) as arg_imageFile:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_file"](arg_imageFile.COM_val))

    @property
    def progress_image_x_origin(self) -> "PROGRESS_IMAGE_X_ORIGIN":
        """The X origin alignment for animated progress image."""
        with agmarshall.AgEnum_arg(PROGRESS_IMAGE_X_ORIGIN) as arg_psProgressImageXOrigin:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_x_origin"](byref(arg_psProgressImageXOrigin.COM_val)))
            return arg_psProgressImageXOrigin.python_val

    @progress_image_x_origin.setter
    def progress_image_x_origin(self, progressImageXOrigin:"PROGRESS_IMAGE_X_ORIGIN") -> None:
        with agmarshall.AgEnum_arg(PROGRESS_IMAGE_X_ORIGIN, progressImageXOrigin) as arg_progressImageXOrigin:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_x_origin"](arg_progressImageXOrigin.COM_val))

    @property
    def progress_image_y_origin(self) -> "PROGRESS_IMAGE_Y_ORIGIN":
        """The Y origin alignment for animated progress image."""
        with agmarshall.AgEnum_arg(PROGRESS_IMAGE_Y_ORIGIN) as arg_psProgressImageYOrigin:
            agcls.evaluate_hresult(self.__dict__["_get_progress_image_y_origin"](byref(arg_psProgressImageYOrigin.COM_val)))
            return arg_psProgressImageYOrigin.python_val

    @progress_image_y_origin.setter
    def progress_image_y_origin(self, progressImageYOrigin:"PROGRESS_IMAGE_Y_ORIGIN") -> None:
        with agmarshall.AgEnum_arg(PROGRESS_IMAGE_Y_ORIGIN, progressImageYOrigin) as arg_progressImageYOrigin:
            agcls.evaluate_hresult(self.__dict__["_set_progress_image_y_origin"](arg_progressImageYOrigin.COM_val))

    @property
    def picture_from_file(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg() as arg_pPictureFile:
            agcls.evaluate_hresult(self.__dict__["_get_picture_from_file"](byref(arg_pPictureFile.COM_val)))
            return arg_pPictureFile.python_val

    @picture_from_file.setter
    def picture_from_file(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg(pictureFile) as arg_pictureFile:
            agcls.evaluate_hresult(self.__dict__["_set_picture_from_file"](arg_pictureFile.COM_val))

    @property
    def pan_mode_enabled(self) -> bool:
        """Enables/disables pan mode for map control."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pPanMode:
            agcls.evaluate_hresult(self.__dict__["_get_pan_mode_enabled"](byref(arg_pPanMode.COM_val)))
            return arg_pPanMode.python_val

    @pan_mode_enabled.setter
    def pan_mode_enabled(self, bPanMode:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bPanMode) as arg_bPanMode:
            agcls.evaluate_hresult(self.__dict__["_set_pan_mode_enabled"](arg_bPanMode.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{A5C18751-1656-4FB9-BA4E-D5746D509CFC}", IUiAx2DCntrl)
agcls.AgTypeNameMap["IUiAx2DCntrl"] = IUiAx2DCntrl

class ISTKXApplicationPartnerAccess(object):
    """Access to the application object model for business partners."""
    _uuid = "{ABF4E08E-211F-40B6-A2F0-6938DAA560CE}"
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_grant_partner_access"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(ISTKXApplicationPartnerAccess._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create ISTKXApplicationPartnerAccess from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_ISTKXApplicationPartnerAccess = agcom.GUID(ISTKXApplicationPartnerAccess._uuid)
        vtable_offset_local = ISTKXApplicationPartnerAccess._vtable_offset - 1
        self.__dict__["_grant_partner_access"] = IAGFUNCTYPE(pUnk, IID_ISTKXApplicationPartnerAccess, vtable_offset_local+1, agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in ISTKXApplicationPartnerAccess.__dict__ and type(ISTKXApplicationPartnerAccess.__dict__[attrname]) == property:
            return ISTKXApplicationPartnerAccess.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ISTKXApplicationPartnerAccess.")
    
    def grant_partner_access(self, vendor:str, product:str, key:str) -> "ISTKXApplication":
        """Provide object model root for authorized business partners."""
        with agmarshall.BSTR_arg(vendor) as arg_vendor, \
             agmarshall.BSTR_arg(product) as arg_product, \
             agmarshall.BSTR_arg(key) as arg_key, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_grant_partner_access"](arg_vendor.COM_val, arg_product.COM_val, arg_key.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{ABF4E08E-211F-40B6-A2F0-6938DAA560CE}", ISTKXApplicationPartnerAccess)
agcls.AgTypeNameMap["ISTKXApplicationPartnerAccess"] = ISTKXApplicationPartnerAccess

class IDataObjectFiles(object):
    """Collection of file names."""
    _uuid = "{C4428821-C59F-45B1-9747-0AD1F988317E}"
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IDataObjectFiles._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IDataObjectFiles from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IDataObjectFiles = agcom.GUID(IDataObjectFiles._uuid)
        vtable_offset_local = IDataObjectFiles._vtable_offset - 1
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IDataObjectFiles, vtable_offset_local+1, POINTER(agcom.PVOID))
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IDataObjectFiles, vtable_offset_local+2, agcom.LONG, POINTER(agcom.BSTR))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IDataObjectFiles, vtable_offset_local+3, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IDataObjectFiles.__dict__ and type(IDataObjectFiles.__dict__[attrname]) == property:
            return IDataObjectFiles.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IDataObjectFiles.")
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
    def _NewEnum(self) -> IEnumVARIANT:
        """Returns an object that can be used to iterate through all the file names in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppUnk:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppUnk.COM_val)))
            return arg_ppUnk.python_val

    def item(self, index:int) -> str:
        """Gets the file name at the specified index (0-based)."""
        with agmarshall.LONG_arg(index) as arg_index, \
             agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_index.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def count(self) -> int:
        """Number of file names contained in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{C4428821-C59F-45B1-9747-0AD1F988317E}", IDataObjectFiles)
agcls.AgTypeNameMap["IDataObjectFiles"] = IDataObjectFiles

class IUiAxGraphics2DAnalysisCntrl(object):
    """AGI Gfx Analysis control."""
    _uuid = "{5933D068-12E5-4B73-96A3-E06CC3ACC05A}"
    _num_methods = 17
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_back_color"] = _raise_uninitialized_error
        self.__dict__["_set_back_color"] = _raise_uninitialized_error
        self.__dict__["_get_picture"] = _raise_uninitialized_error
        self.__dict__["_picture_put_reference"] = _raise_uninitialized_error
        self.__dict__["_set_picture"] = _raise_uninitialized_error
        self.__dict__["_get_no_logo"] = _raise_uninitialized_error
        self.__dict__["_set_no_logo"] = _raise_uninitialized_error
        self.__dict__["_get_vendor_id"] = _raise_uninitialized_error
        self.__dict__["_set_vendor_id"] = _raise_uninitialized_error
        self.__dict__["_get_ready_state"] = _raise_uninitialized_error
        self.__dict__["_get_application"] = _raise_uninitialized_error
        self.__dict__["_get_control_mode"] = _raise_uninitialized_error
        self.__dict__["_set_control_mode"] = _raise_uninitialized_error
        self.__dict__["_get_picture_from_file"] = _raise_uninitialized_error
        self.__dict__["_set_picture_from_file"] = _raise_uninitialized_error
        self.__dict__["_get_win_id"] = _raise_uninitialized_error
        self.__dict__["_set_win_id"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiAxGraphics2DAnalysisCntrl._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiAxGraphics2DAnalysisCntrl from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiAxGraphics2DAnalysisCntrl = agcom.GUID(IUiAxGraphics2DAnalysisCntrl._uuid)
        vtable_offset_local = IUiAxGraphics2DAnalysisCntrl._vtable_offset - 1
        self.__dict__["_get_back_color"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+1, POINTER(agcom.OLE_COLOR))
        self.__dict__["_set_back_color"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+2, agcom.OLE_COLOR)
        self.__dict__["_get_picture"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_picture_put_reference"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+4, agcom.PVOID)
        self.__dict__["_set_picture"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+5, agcom.PVOID)
        self.__dict__["_get_no_logo"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+6, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_no_logo"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+7, agcom.VARIANT_BOOL)
        self.__dict__["_get_vendor_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+8, POINTER(agcom.BSTR))
        self.__dict__["_set_vendor_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+9, agcom.BSTR)
        self.__dict__["_get_ready_state"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+10, POINTER(agcom.LONG))
        self.__dict__["_get_application"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+11, POINTER(agcom.PVOID))
        self.__dict__["_get_control_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+12, POINTER(agcom.LONG))
        self.__dict__["_set_control_mode"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+13, agcom.LONG)
        self.__dict__["_get_picture_from_file"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+14, POINTER(agcom.BSTR))
        self.__dict__["_set_picture_from_file"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+15, agcom.BSTR)
        self.__dict__["_get_win_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+16, POINTER(agcom.LONG))
        self.__dict__["_set_win_id"] = IAGFUNCTYPE(pUnk, IID_IUiAxGraphics2DAnalysisCntrl, vtable_offset_local+17, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiAxGraphics2DAnalysisCntrl.__dict__ and type(IUiAxGraphics2DAnalysisCntrl.__dict__[attrname]) == property:
            return IUiAxGraphics2DAnalysisCntrl.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiAxGraphics2DAnalysisCntrl.")
    
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        with agmarshall.OLE_COLOR_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_get_back_color"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        with agmarshall.OLE_COLOR_arg(clr) as arg_clr:
            agcls.evaluate_hresult(self.__dict__["_set_back_color"](arg_clr.COM_val))

    @property
    def picture(self) -> "IPictureDisp":
        """The splash logo graphic to be displayed in the control."""
        with agmarshall.PVOID_arg() as arg_ppPicture:
            agcls.evaluate_hresult(self.__dict__["_get_picture"](byref(arg_ppPicture.COM_val)))
            return arg_ppPicture.python_val

    def picture_put_reference(self, pPicture:"IPictureDisp") -> None:
        with agmarshall.PVOID_arg(pPicture, IPictureDisp) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_picture_put_reference"](arg_pPicture.COM_val))

    @picture.setter
    def picture(self, pPicture:"IPictureDisp") -> None:
        with agmarshall.PVOID_arg(pPicture, IPictureDisp) as arg_pPicture:
            agcls.evaluate_hresult(self.__dict__["_set_picture"](arg_pPicture.COM_val))

    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pNoLogo:
            agcls.evaluate_hresult(self.__dict__["_get_no_logo"](byref(arg_pNoLogo.COM_val)))
            return arg_pNoLogo.python_val

    @no_logo.setter
    def no_logo(self, bNoLogo:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(bNoLogo) as arg_bNoLogo:
            agcls.evaluate_hresult(self.__dict__["_set_no_logo"](arg_bNoLogo.COM_val))

    @property
    def vendor_id(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        with agmarshall.BSTR_arg() as arg_pbstrVal:
            agcls.evaluate_hresult(self.__dict__["_get_vendor_id"](byref(arg_pbstrVal.COM_val)))
            return arg_pbstrVal.python_val

    @vendor_id.setter
    def vendor_id(self, vendorID:str) -> None:
        with agmarshall.BSTR_arg(vendorID) as arg_vendorID:
            agcls.evaluate_hresult(self.__dict__["_set_vendor_id"](arg_vendorID.COM_val))

    @property
    def ready_state(self) -> int:
        """Returns the ready state of the control."""
        with agmarshall.LONG_arg() as arg_pclr:
            agcls.evaluate_hresult(self.__dict__["_get_ready_state"](byref(arg_pclr.COM_val)))
            return arg_pclr.python_val

    @property
    def application(self) -> "ISTKXApplication":
        """Reference to the STK X application object."""
        with agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_application"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def control_mode(self) -> "GRAPHICS_2D_ANALYSIS_MODE":
        """The Graphics control mode."""
        with agmarshall.AgEnum_arg(GRAPHICS_2D_ANALYSIS_MODE) as arg_peGfxAnalysisMode:
            agcls.evaluate_hresult(self.__dict__["_get_control_mode"](byref(arg_peGfxAnalysisMode.COM_val)))
            return arg_peGfxAnalysisMode.python_val

    @control_mode.setter
    def control_mode(self, eGfxAnalysisMode:"GRAPHICS_2D_ANALYSIS_MODE") -> None:
        with agmarshall.AgEnum_arg(GRAPHICS_2D_ANALYSIS_MODE, eGfxAnalysisMode) as arg_eGfxAnalysisMode:
            agcls.evaluate_hresult(self.__dict__["_set_control_mode"](arg_eGfxAnalysisMode.COM_val))

    @property
    def picture_from_file(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg() as arg_pPictureFile:
            agcls.evaluate_hresult(self.__dict__["_get_picture_from_file"](byref(arg_pPictureFile.COM_val)))
            return arg_pPictureFile.python_val

    @picture_from_file.setter
    def picture_from_file(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        with agmarshall.BSTR_arg(pictureFile) as arg_pictureFile:
            agcls.evaluate_hresult(self.__dict__["_set_picture_from_file"](arg_pictureFile.COM_val))

    @property
    def win_id(self) -> int:
        """Window identifier (for Connect commands)."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_win_id"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @win_id.setter
    def win_id(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_win_id"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{5933D068-12E5-4B73-96A3-E06CC3ACC05A}", IUiAxGraphics2DAnalysisCntrl)
agcls.AgTypeNameMap["IUiAxGraphics2DAnalysisCntrl"] = IUiAxGraphics2DAnalysisCntrl



class ExecCmdResult(IExecCmdResult):
    """Collection of strings returned by the ExecuteCommand."""
    def __init__(self, sourceObject=None):
        IExecCmdResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IExecCmdResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IExecCmdResult._get_property(self, attrname) is not None: found_prop = IExecCmdResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ExecCmdResult.")
        
agcls.AgClassCatalog.add_catalog_entry("{97E6F619-31E5-4AF7-B3AF-0E927F2134D4}", ExecCmdResult)


class ExecMultiCmdResult(IExecMultiCmdResult):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    def __init__(self, sourceObject=None):
        IExecMultiCmdResult.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IExecMultiCmdResult._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IExecMultiCmdResult._get_property(self, attrname) is not None: found_prop = IExecMultiCmdResult._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ExecMultiCmdResult.")
        
agcls.AgClassCatalog.add_catalog_entry("{3849A604-DEB9-428C-8A72-D879719277E5}", ExecMultiCmdResult)


class UiAxGraphics3DCntrl(IUiAxGraphics3DCntrl):
    """AGI Globe control."""
    def __init__(self, sourceObject=None):
        IUiAxGraphics3DCntrl.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiAxGraphics3DCntrl._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiAxGraphics3DCntrl._get_property(self, attrname) is not None: found_prop = IUiAxGraphics3DCntrl._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiAxGraphics3DCntrl.")
        
agcls.AgClassCatalog.add_catalog_entry("{0E939AC2-43D9-456E-9FE7-4C3C687BCDF2}", UiAxGraphics3DCntrl)


class UiAx2DCntrl(IUiAx2DCntrl):
    """AGI Map control."""
    def __init__(self, sourceObject=None):
        IUiAx2DCntrl.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiAx2DCntrl._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiAx2DCntrl._get_property(self, attrname) is not None: found_prop = IUiAx2DCntrl._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiAx2DCntrl.")
        
agcls.AgClassCatalog.add_catalog_entry("{33FBA419-2BD0-422D-81A7-C5B68A49FB01}", UiAx2DCntrl)


class PickInfoData(IPickInfoData):
    """Single mouse pick result."""
    def __init__(self, sourceObject=None):
        IPickInfoData.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IPickInfoData._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IPickInfoData._get_property(self, attrname) is not None: found_prop = IPickInfoData._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in PickInfoData.")
        
agcls.AgClassCatalog.add_catalog_entry("{9B6FCD4D-91A0-4855-A113-F7CC8D774608}", PickInfoData)


class STKXApplication(ISTKXApplication):
    """STK X Application object."""
    def __init__(self, sourceObject=None):
        ISTKXApplication.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ISTKXApplication._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ISTKXApplication._get_property(self, attrname) is not None: found_prop = ISTKXApplication._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in STKXApplication.")
        
agcls.AgClassCatalog.add_catalog_entry("{062AB565-B121-45B5-A9A9-B412CEFAB6A9}", STKXApplication)


class STKXApplicationPartnerAccess(ISTKXApplicationPartnerAccess):
    """STK X Application Partner Access object."""
    def __init__(self, sourceObject=None):
        ISTKXApplicationPartnerAccess.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ISTKXApplicationPartnerAccess._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ISTKXApplicationPartnerAccess._get_property(self, attrname) is not None: found_prop = ISTKXApplicationPartnerAccess._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in STKXApplicationPartnerAccess.")
        
agcls.AgClassCatalog.add_catalog_entry("{3E8358E8-6042-4E4C-B89D-1F42164CDE3D}", STKXApplicationPartnerAccess)


class DataObject(IDataObject):
    """Data Object for OLE drag & drop operations."""
    def __init__(self, sourceObject=None):
        IDataObject.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDataObject._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDataObject._get_property(self, attrname) is not None: found_prop = IDataObject._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DataObject.")
        
agcls.AgClassCatalog.add_catalog_entry("{C58BE31A-8063-46F9-9751-AF13C1101D75}", DataObject)


class DataObjectFiles(IDataObjectFiles):
    """Collection of files for OLE drag & drop operations."""
    def __init__(self, sourceObject=None):
        IDataObjectFiles.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDataObjectFiles._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDataObjectFiles._get_property(self, attrname) is not None: found_prop = IDataObjectFiles._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DataObjectFiles.")
        
agcls.AgClassCatalog.add_catalog_entry("{83A2F2F3-3122-4317-8D59-2F43906E4168}", DataObjectFiles)


class RubberBandPickInfoData(IRubberBandPickInfoData):
    """Rubber-band mouse pick result."""
    def __init__(self, sourceObject=None):
        IRubberBandPickInfoData.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IRubberBandPickInfoData._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IRubberBandPickInfoData._get_property(self, attrname) is not None: found_prop = IRubberBandPickInfoData._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in RubberBandPickInfoData.")
        
agcls.AgClassCatalog.add_catalog_entry("{A7EB5C99-B818-4531-B598-368AA2DD3CF6}", RubberBandPickInfoData)


class ObjPathCollection(IObjPathCollection):
    """Collection of object paths."""
    def __init__(self, sourceObject=None):
        IObjPathCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IObjPathCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IObjPathCollection._get_property(self, attrname) is not None: found_prop = IObjPathCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in ObjPathCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{0B3FFC58-8105-4BE4-9D60-254A142448D5}", ObjPathCollection)


class DrawElemRect(IDrawElemRect):
    """Defines a rectangle in window coordinates."""
    def __init__(self, sourceObject=None):
        IDrawElemRect.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDrawElemRect._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDrawElemRect._get_property(self, attrname) is not None: found_prop = IDrawElemRect._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DrawElemRect.")
        
agcls.AgClassCatalog.add_catalog_entry("{55B0A7B5-2508-48BB-90D0-4B8B51DC9178}", DrawElemRect)


class DrawElemCollection(IDrawElemCollection):
    """Collection of elements to draw on the control."""
    def __init__(self, sourceObject=None):
        IDrawElemCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDrawElemCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDrawElemCollection._get_property(self, attrname) is not None: found_prop = IDrawElemCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DrawElemCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{97A759F9-49E4-42DE-A8E3-7B670EB3BDAC}", DrawElemCollection)


class Draw2DElemRect(IDrawElemRect):
    """Defines a rectangle in window coordinates for map control."""
    def __init__(self, sourceObject=None):
        IDrawElemRect.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDrawElemRect._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDrawElemRect._get_property(self, attrname) is not None: found_prop = IDrawElemRect._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Draw2DElemRect.")
        
agcls.AgClassCatalog.add_catalog_entry("{C26CEE82-EB4B-4D63-86B0-C5E2BB261E3F}", Draw2DElemRect)


class Draw2DElemCollection(IDrawElemCollection):
    """Collection of elements to draw on map control."""
    def __init__(self, sourceObject=None):
        IDrawElemCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDrawElemCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDrawElemCollection._get_property(self, attrname) is not None: found_prop = IDrawElemCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in Draw2DElemCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{D6B1A826-3ABB-49FD-8C9F-F49ADBE6D2B8}", Draw2DElemCollection)


class UiAxGraphics2DAnalysisCntrl(IUiAxGraphics2DAnalysisCntrl):
    """AGI Graphics Analysis Control"""
    def __init__(self, sourceObject=None):
        IUiAxGraphics2DAnalysisCntrl.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiAxGraphics2DAnalysisCntrl._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiAxGraphics2DAnalysisCntrl._get_property(self, attrname) is not None: found_prop = IUiAxGraphics2DAnalysisCntrl._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiAxGraphics2DAnalysisCntrl.")
        
agcls.AgClassCatalog.add_catalog_entry("{600541C4-8B16-47AD-ABA4-EE8BC5E9FD5F}", UiAxGraphics2DAnalysisCntrl)


class WinProjectionPosition(IWinProjectionPosition):
    """Projected window position result."""
    def __init__(self, sourceObject=None):
        IWinProjectionPosition.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IWinProjectionPosition._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IWinProjectionPosition._get_property(self, attrname) is not None: found_prop = IWinProjectionPosition._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in WinProjectionPosition.")
        
agcls.AgClassCatalog.add_catalog_entry("{21D08121-9F86-485E-B143-337DACCD5022}", WinProjectionPosition)


class DrawElemLine(IDrawElemLine):
    """Defines a line in window coordinates."""
    def __init__(self, sourceObject=None):
        IDrawElemLine.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IDrawElemLine._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IDrawElemLine._get_property(self, attrname) is not None: found_prop = IDrawElemLine._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in DrawElemLine.")
        
agcls.AgClassCatalog.add_catalog_entry("{A4C86FD0-95FA-4F15-BE04-1FDF0DD6B0B5}", DrawElemLine)


class STKXSSLCertificateErrorEventArgs(ISTKXSSLCertificateErrorEventArgs):
    """Provides information about an SSL certificate that is expired or invalid."""
    def __init__(self, sourceObject=None):
        ISTKXSSLCertificateErrorEventArgs.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ISTKXSSLCertificateErrorEventArgs._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ISTKXSSLCertificateErrorEventArgs._get_property(self, attrname) is not None: found_prop = ISTKXSSLCertificateErrorEventArgs._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in STKXSSLCertificateErrorEventArgs.")
        
agcls.AgClassCatalog.add_catalog_entry("{2BCBD8EC-2EA5-4D14-855D-BB85A201BCB4}", STKXSSLCertificateErrorEventArgs)


class STKXConControlQuitReceivedEventArgs(ISTKXConControlQuitReceivedEventArgs):
    """Arguments for the OnConControlQuitReceived event."""
    def __init__(self, sourceObject=None):
        ISTKXConControlQuitReceivedEventArgs.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        ISTKXConControlQuitReceivedEventArgs._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if ISTKXConControlQuitReceivedEventArgs._get_property(self, attrname) is not None: found_prop = ISTKXConControlQuitReceivedEventArgs._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in STKXConControlQuitReceivedEventArgs.")
        
agcls.AgClassCatalog.add_catalog_entry("{CA9E9226-74BE-4733-B50A-D64703165F4E}", STKXConControlQuitReceivedEventArgs)



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
