################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
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

from ctypes   import POINTER
from datetime import datetime
from enum     import IntEnum, IntFlag

from .internal  import comutil          as agcom
from .internal  import coclassutil      as agcls
from .internal  import marshall         as agmarshall
from .utilities import colors           as agcolor
from .internal.comutil     import IDispatch, IPictureDisp
from .internal.apiutil     import interface_proxy, enumerator_proxy, out_arg
from .internal.eventutil   import *
from .utilities.exceptions import *

from .stkutil import *


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class LOG_MSG_TYPE(IntEnum):
    """Log message types."""
    DEBUG = 0
    """Debugging message."""
    INFO = 1
    """Informational message."""
    FORCE_INFO = 2
    """Informational message."""
    WARNING = 3
    """Warning message."""
    ALARM = 4
    """Alarm message."""

LOG_MSG_TYPE.DEBUG.__doc__ = "Debugging message."
LOG_MSG_TYPE.INFO.__doc__ = "Informational message."
LOG_MSG_TYPE.FORCE_INFO.__doc__ = "Informational message."
LOG_MSG_TYPE.WARNING.__doc__ = "Warning message."
LOG_MSG_TYPE.ALARM.__doc__ = "Alarm message."

agcls.AgTypeNameMap["LOG_MSG_TYPE"] = LOG_MSG_TYPE

class LOG_MSG_DISP_ID(IntEnum):
    """Log message destination options."""
    ALL = -1
    """STK displays the message in all the log destination."""
    DEFAULT = 0
    """STK displays the message in the default log destination."""
    MSG_WIN = 1
    """STK displays the message in the message window."""
    STATUS_BAR = 2
    """STK displays the message in the status bar."""

LOG_MSG_DISP_ID.ALL.__doc__ = "STK displays the message in all the log destination."
LOG_MSG_DISP_ID.DEFAULT.__doc__ = "STK displays the message in the default log destination."
LOG_MSG_DISP_ID.MSG_WIN.__doc__ = "STK displays the message in the message window."
LOG_MSG_DISP_ID.STATUS_BAR.__doc__ = "STK displays the message in the status bar."

agcls.AgTypeNameMap["LOG_MSG_DISP_ID"] = LOG_MSG_DISP_ID

class LINE_STYLE(IntEnum):
    """Line Style"""
    SOLID = 0
    """Specify a solid line."""
    DASHED = 1
    """Specify a dashed line."""
    DOTTED = 2
    """Specify a dotted line."""
    DOT_DASHED = 3
    """Dot-dashed line."""
    LONG_DASHED = 4
    """Specify a long dashed line."""
    DASH_DOT_DOTTED = 5
    """Specify an alternating dash-dot-dot line."""
    M_DASH = 6
    """Specify a user configurable medium dashed line."""
    L_DASH = 7
    """Specify a user configurable long dashed line."""
    S_DASH_DOT = 8
    """Specify a user configurable small dash-dotted line."""
    M_DASH_DOT = 9
    """Specify a user configurable medium dash-dotted line."""
    DASH_DOT = 10
    """Specify a user configurable long dash-dotted line."""
    MS_DASH = 11
    """Specify a user configurable medium followed by small dashed line."""
    LS_DASH = 12
    """Specify a user configurable long followed by small dashed line."""
    LM_DASH = 13
    """Specify a user configurable long followed by medium dashed line."""
    LMS_DASH = 14
    """Specify a user configurable medium followed by small dashed line."""
    DOT = 15
    """Specify a dotted line."""
    LONG_DASH = 16
    """Specify a long dashed line."""
    S_DASH = 17
    """Specify an alternating dash-dot line."""

LINE_STYLE.SOLID.__doc__ = "Specify a solid line."
LINE_STYLE.DASHED.__doc__ = "Specify a dashed line."
LINE_STYLE.DOTTED.__doc__ = "Specify a dotted line."
LINE_STYLE.DOT_DASHED.__doc__ = "Dot-dashed line."
LINE_STYLE.LONG_DASHED.__doc__ = "Specify a long dashed line."
LINE_STYLE.DASH_DOT_DOTTED.__doc__ = "Specify an alternating dash-dot-dot line."
LINE_STYLE.M_DASH.__doc__ = "Specify a user configurable medium dashed line."
LINE_STYLE.L_DASH.__doc__ = "Specify a user configurable long dashed line."
LINE_STYLE.S_DASH_DOT.__doc__ = "Specify a user configurable small dash-dotted line."
LINE_STYLE.M_DASH_DOT.__doc__ = "Specify a user configurable medium dash-dotted line."
LINE_STYLE.DASH_DOT.__doc__ = "Specify a user configurable long dash-dotted line."
LINE_STYLE.MS_DASH.__doc__ = "Specify a user configurable medium followed by small dashed line."
LINE_STYLE.LS_DASH.__doc__ = "Specify a user configurable long followed by small dashed line."
LINE_STYLE.LM_DASH.__doc__ = "Specify a user configurable long followed by medium dashed line."
LINE_STYLE.LMS_DASH.__doc__ = "Specify a user configurable medium followed by small dashed line."
LINE_STYLE.DOT.__doc__ = "Specify a dotted line."
LINE_STYLE.LONG_DASH.__doc__ = "Specify a long dashed line."
LINE_STYLE.S_DASH.__doc__ = "Specify an alternating dash-dot line."

agcls.AgTypeNameMap["LINE_STYLE"] = LINE_STYLE

class EXEC_MULTI_CMD_RESULT_ACTION(IntFlag):
    """Enumeration defines a set of actions when an error occurs while executing a command batch."""
    CONTINUE_ON_ERROR = 0
    """Continue executing the remaining commands in the command batch."""
    STOP_ON_ERROR = 1
    """Terminate the execution of the command batch but do not throw an exception."""
    EXCEPTION_ON_ERROR = 2
    """Terminate the execution of the command batch and throw an exception."""
    IGNORE_EXEC_CMD_RESULT = 0x8000
    """Ignore results returned by individual commands. The option must be used in combination with other flags."""

EXEC_MULTI_CMD_RESULT_ACTION.CONTINUE_ON_ERROR.__doc__ = "Continue executing the remaining commands in the command batch."
EXEC_MULTI_CMD_RESULT_ACTION.STOP_ON_ERROR.__doc__ = "Terminate the execution of the command batch but do not throw an exception."
EXEC_MULTI_CMD_RESULT_ACTION.EXCEPTION_ON_ERROR.__doc__ = "Terminate the execution of the command batch and throw an exception."
EXEC_MULTI_CMD_RESULT_ACTION.IGNORE_EXEC_CMD_RESULT.__doc__ = "Ignore results returned by individual commands. The option must be used in combination with other flags."

agcls.AgTypeNameMap["EXEC_MULTI_CMD_RESULT_ACTION"] = EXEC_MULTI_CMD_RESULT_ACTION

class SHIFT_VALUES(IntEnum):
    """State of the Shift/Ctrl/Alt keys."""
    PRESSED = 1
    """The Shift key was pressed."""
    CTRL_PRESSED = 2
    """The Ctrl key was pressed."""
    ALTITUDE_PRESSED = 4
    """The ALT key was pressed."""

SHIFT_VALUES.PRESSED.__doc__ = "The Shift key was pressed."
SHIFT_VALUES.CTRL_PRESSED.__doc__ = "The Ctrl key was pressed."
SHIFT_VALUES.ALTITUDE_PRESSED.__doc__ = "The ALT key was pressed."

agcls.AgTypeNameMap["SHIFT_VALUES"] = SHIFT_VALUES

class BUTTON_VALUES(IntEnum):
    """Numeric value of the mouse button pressed."""
    LEFT_PRESSED = 1
    """The left button is pressed."""
    RIGHT_PRESSED = 2
    """The right button is pressed."""
    MIDDLE_PRESSED = 4
    """The middle button is pressed."""

BUTTON_VALUES.LEFT_PRESSED.__doc__ = "The left button is pressed."
BUTTON_VALUES.RIGHT_PRESSED.__doc__ = "The right button is pressed."
BUTTON_VALUES.MIDDLE_PRESSED.__doc__ = "The middle button is pressed."

agcls.AgTypeNameMap["BUTTON_VALUES"] = BUTTON_VALUES

class OLE_DROP_MODE(IntEnum):
    """Specifies how to handle OLE drop operations."""
    NONE = 0
    """None. The control does not accept OLE drops and displays the No Drop cursor."""
    MANUAL = 1
    """Manual. The control triggers the OLE drop events, allowing the programmer to handle the OLE drop operation in code."""
    AUTOMATIC = 2
    """Automatic. The control automatically accepts OLE drops if the DataObject object contains data in a format it recognizes. No OLE drag/drop events on the target will occur when OLEDropMode is set to eAutomatic."""

OLE_DROP_MODE.NONE.__doc__ = "None. The control does not accept OLE drops and displays the No Drop cursor."
OLE_DROP_MODE.MANUAL.__doc__ = "Manual. The control triggers the OLE drop events, allowing the programmer to handle the OLE drop operation in code."
OLE_DROP_MODE.AUTOMATIC.__doc__ = "Automatic. The control automatically accepts OLE drops if the DataObject object contains data in a format it recognizes. No OLE drag/drop events on the target will occur when OLEDropMode is set to eAutomatic."

agcls.AgTypeNameMap["OLE_DROP_MODE"] = OLE_DROP_MODE

class MOUSE_MODE(IntEnum):
    """Mouse modes."""
    AUTOMATIC = 0
    """Automatic. The control handles the mouse events and then fires the events to the container for additional processing."""
    MANUAL = 1
    """None. No default action happens on mouse events. Events are fired to the container."""

MOUSE_MODE.AUTOMATIC.__doc__ = "Automatic. The control handles the mouse events and then fires the events to the container for additional processing."
MOUSE_MODE.MANUAL.__doc__ = "None. No default action happens on mouse events. Events are fired to the container."

agcls.AgTypeNameMap["MOUSE_MODE"] = MOUSE_MODE

class LOGGING_MODE(IntEnum):
    """Specifies the state of the log file."""
    INACTIVE = 0
    """The log file is not created."""
    ACTIVE = 1
    """The log file is created but deleted upon application termination."""
    ACTIVE_KEEP_FILE = 2
    """The log file is created and kept even after application is terminated."""

LOGGING_MODE.INACTIVE.__doc__ = "The log file is not created."
LOGGING_MODE.ACTIVE.__doc__ = "The log file is created but deleted upon application termination."
LOGGING_MODE.ACTIVE_KEEP_FILE.__doc__ = "The log file is created and kept even after application is terminated."

agcls.AgTypeNameMap["LOGGING_MODE"] = LOGGING_MODE

class GRAPHICS_2D_ANALYSIS_MODE(IntEnum):
    """Specifies the mode of Gfx Analysis Control."""
    SOLAR_PANEL_TOOL = 1
    """The Solar Panel Tool mode."""
    AREA_TOOL = 2
    """The Area Tool mode."""
    OBSCURATION_TOOL = 3
    """The Obscuration Tool mode."""
    AZ_EL_MASK_TOOL = 4
    """The AzElMask Tool mode."""

GRAPHICS_2D_ANALYSIS_MODE.SOLAR_PANEL_TOOL.__doc__ = "The Solar Panel Tool mode."
GRAPHICS_2D_ANALYSIS_MODE.AREA_TOOL.__doc__ = "The Area Tool mode."
GRAPHICS_2D_ANALYSIS_MODE.OBSCURATION_TOOL.__doc__ = "The Obscuration Tool mode."
GRAPHICS_2D_ANALYSIS_MODE.AZ_EL_MASK_TOOL.__doc__ = "The AzElMask Tool mode."

agcls.AgTypeNameMap["GRAPHICS_2D_ANALYSIS_MODE"] = GRAPHICS_2D_ANALYSIS_MODE

class GRAPHICS_2D_DRAW_COORDS(IntEnum):
    """Specifies the draw coordinates for Map Control."""
    PIXEL_DRAW_COORDS = 1
    """The draw coordinates values in pixels."""
    SCREEN_DRAW_COORDS = 2
    """The draw coordinates values in screen coordinates."""

GRAPHICS_2D_DRAW_COORDS.PIXEL_DRAW_COORDS.__doc__ = "The draw coordinates values in pixels."
GRAPHICS_2D_DRAW_COORDS.SCREEN_DRAW_COORDS.__doc__ = "The draw coordinates values in screen coordinates."

agcls.AgTypeNameMap["GRAPHICS_2D_DRAW_COORDS"] = GRAPHICS_2D_DRAW_COORDS

class SHOW_PROGRESS_IMAGE(IntEnum):
    """Specifies to show progress image."""
    NONE = 1
    """Do not show any progress Image."""
    DEFAULT = 2
    """Show the default progress image."""
    USER = 3
    """Show the user specified progress image."""

SHOW_PROGRESS_IMAGE.NONE.__doc__ = "Do not show any progress Image."
SHOW_PROGRESS_IMAGE.DEFAULT.__doc__ = "Show the default progress image."
SHOW_PROGRESS_IMAGE.USER.__doc__ = "Show the user specified progress image."

agcls.AgTypeNameMap["SHOW_PROGRESS_IMAGE"] = SHOW_PROGRESS_IMAGE

class FEATURE_CODES(IntEnum):
    """The enumeration values are used to check availability of a given feature."""
    ENGINE_RUNTIME = 1
    """The enumeration is used to check whether the engine runtime is available."""
    GLOBE_CONTROL = 2
    """The enumeration is used to check whether the globe is available."""

FEATURE_CODES.ENGINE_RUNTIME.__doc__ = "The enumeration is used to check whether the engine runtime is available."
FEATURE_CODES.GLOBE_CONTROL.__doc__ = "The enumeration is used to check whether the globe is available."

agcls.AgTypeNameMap["FEATURE_CODES"] = FEATURE_CODES

class PROGRESS_IMAGE_X_ORIGIN(IntEnum):
    """Specifies to align progress image X origin."""
    LEFT = 1
    """Align progress Image from X left."""
    RIGHT = 2
    """Align progress Image from X right."""
    CENTER = 3
    """Align progress Image from X center."""

PROGRESS_IMAGE_X_ORIGIN.LEFT.__doc__ = "Align progress Image from X left."
PROGRESS_IMAGE_X_ORIGIN.RIGHT.__doc__ = "Align progress Image from X right."
PROGRESS_IMAGE_X_ORIGIN.CENTER.__doc__ = "Align progress Image from X center."

agcls.AgTypeNameMap["PROGRESS_IMAGE_X_ORIGIN"] = PROGRESS_IMAGE_X_ORIGIN

class PROGRESS_IMAGE_Y_ORIGIN(IntEnum):
    """Specifies to align progress image Y origin."""
    TOP = 1
    """Align progress Image from Y top."""
    BOTTOM = 2
    """Align progress Image from Y bottom."""
    CENTER = 3
    """Align progress Image from Y center."""

PROGRESS_IMAGE_Y_ORIGIN.TOP.__doc__ = "Align progress Image from Y top."
PROGRESS_IMAGE_Y_ORIGIN.BOTTOM.__doc__ = "Align progress Image from Y bottom."
PROGRESS_IMAGE_Y_ORIGIN.CENTER.__doc__ = "Align progress Image from Y center."

agcls.AgTypeNameMap["PROGRESS_IMAGE_Y_ORIGIN"] = PROGRESS_IMAGE_Y_ORIGIN


class ISTKXSSLCertificateErrorEventArgs(object):
    """Provide information about an SSL certificate that is expired or invalid."""
    _num_methods = 12
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{D0C7ACBC-D1DD-45AE-9582-C7AE5C2E5BEF}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "set_ignore_error" : 1,
                             "get_is_error_ignored" : 2,
                             "set_ignore_error_permanently" : 3,
                             "get_serial_number" : 4,
                             "get_issuer" : 5,
                             "get_subject" : 6,
                             "get_valid_date" : 7,
                             "get_expiration_date" : 8,
                             "get_is_expired" : 9,
                             "get_pem_data" : 10,
                             "get_handled" : 11,
                             "set_handled" : 12, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ISTKXSSLCertificateErrorEventArgs._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ISTKXSSLCertificateErrorEventArgs from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _set_ignore_error_metadata = { "name" : "set_ignore_error",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    def set_ignore_error(self, ignoreError:bool) -> None:
        """Specify True to ignore the certificate error and continue with establishing secure HTTP connection to the remote server."""
        return self._intf.invoke(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._set_ignore_error_metadata, ignoreError)

    _get_is_error_ignored_metadata = { "name" : "is_error_ignored",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_error_ignored(self) -> bool:
        """Return whether the invalid certificate error is ignored."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_is_error_ignored_metadata)

    _set_ignore_error_permanently_metadata = { "name" : "set_ignore_error_permanently",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    def set_ignore_error_permanently(self, ignoreErrorPermanently:bool) -> None:
        """Specify True to ignore the certificate error and add the certificate to the list of trusted certificates."""
        return self._intf.invoke(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._set_ignore_error_permanently_metadata, ignoreErrorPermanently)

    _get_serial_number_metadata = { "name" : "serial_number",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def serial_number(self) -> str:
        """Certificate's serial number."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_serial_number_metadata)

    _get_issuer_metadata = { "name" : "issuer",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def issuer(self) -> str:
        """The provider who issued the certificate."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_issuer_metadata)

    _get_subject_metadata = { "name" : "subject",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def subject(self) -> str:
        """Certificate's subject field."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_subject_metadata)

    _get_valid_date_metadata = { "name" : "valid_date",
            "arg_types" : (POINTER(agcom.DATE),),
            "marshallers" : (agmarshall.DATE_arg,) }
    @property
    def valid_date(self) -> datetime:
        """Certificate's valid date."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_valid_date_metadata)

    _get_expiration_date_metadata = { "name" : "expiration_date",
            "arg_types" : (POINTER(agcom.DATE),),
            "marshallers" : (agmarshall.DATE_arg,) }
    @property
    def expiration_date(self) -> datetime:
        """Certificate's expiration date."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_expiration_date_metadata)

    _get_is_expired_metadata = { "name" : "is_expired",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_expired(self) -> bool:
        """Whether the certificate is expired."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_is_expired_metadata)

    _get_pem_data_metadata = { "name" : "pem_data",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def pem_data(self) -> str:
        """Certificate's PEM data encoded as base-64."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_pem_data_metadata)

    _get_handled_metadata = { "name" : "handled",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def handled(self) -> bool:
        """Indicate whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners."""
        return self._intf.get_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._get_handled_metadata)

    _set_handled_metadata = { "name" : "handled",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @handled.setter
    def handled(self, bHandled:bool) -> None:
        """Indicate whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners."""
        return self._intf.set_property(ISTKXSSLCertificateErrorEventArgs._metadata, ISTKXSSLCertificateErrorEventArgs._set_handled_metadata, bHandled)


agcls.AgClassCatalog.add_catalog_entry("{D0C7ACBC-D1DD-45AE-9582-C7AE5C2E5BEF}", ISTKXSSLCertificateErrorEventArgs)
agcls.AgTypeNameMap["ISTKXSSLCertificateErrorEventArgs"] = ISTKXSSLCertificateErrorEventArgs

class ISTKXConControlQuitReceivedEventArgs(object):
    """Arguments for the OnConControlQuitReceived event."""
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{F8925F99-8841-4DF3-A6E4-CE63E298868C}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_acknowledge" : 1,
                             "set_acknowledge" : 2, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ISTKXConControlQuitReceivedEventArgs._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ISTKXConControlQuitReceivedEventArgs from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _get_acknowledge_metadata = { "name" : "acknowledge",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def acknowledge(self) -> bool:
        """Indicate whether or not to acknowledge the connect command."""
        return self._intf.get_property(ISTKXConControlQuitReceivedEventArgs._metadata, ISTKXConControlQuitReceivedEventArgs._get_acknowledge_metadata)

    _set_acknowledge_metadata = { "name" : "acknowledge",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @acknowledge.setter
    def acknowledge(self, acknowledge:bool) -> None:
        """Indicate whether or not to acknowledge the connect command."""
        return self._intf.set_property(ISTKXConControlQuitReceivedEventArgs._metadata, ISTKXConControlQuitReceivedEventArgs._set_acknowledge_metadata, acknowledge)


agcls.AgClassCatalog.add_catalog_entry("{F8925F99-8841-4DF3-A6E4-CE63E298868C}", ISTKXConControlQuitReceivedEventArgs)
agcls.AgTypeNameMap["ISTKXConControlQuitReceivedEventArgs"] = ISTKXConControlQuitReceivedEventArgs

class IPickInfoData(object):
    """Mouse pick details."""
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{C87F43DA-DD89-4F13-BCB6-D78D0FE8D7E4}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_obj_path" : 1,
                             "get_lat" : 2,
                             "get_lon" : 3,
                             "get_altitude" : 4,
                             "get_is_obj_path_valid" : 5,
                             "get_is_lat_lon_altitude_valid" : 6, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IPickInfoData._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IPickInfoData from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _get_obj_path_metadata = { "name" : "obj_path",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def obj_path(self) -> str:
        """Path of the STK object picked if any (or empty string)."""
        return self._intf.get_property(IPickInfoData._metadata, IPickInfoData._get_obj_path_metadata)

    _get_lat_metadata = { "name" : "lat",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def lat(self) -> float:
        """Latitude of point clicked (if available)."""
        return self._intf.get_property(IPickInfoData._metadata, IPickInfoData._get_lat_metadata)

    _get_lon_metadata = { "name" : "lon",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def lon(self) -> float:
        """Longitude of point clicked (if available)."""
        return self._intf.get_property(IPickInfoData._metadata, IPickInfoData._get_lon_metadata)

    _get_altitude_metadata = { "name" : "altitude",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def altitude(self) -> float:
        """Altitude of point clicked (if available)."""
        return self._intf.get_property(IPickInfoData._metadata, IPickInfoData._get_altitude_metadata)

    _get_is_obj_path_valid_metadata = { "name" : "is_obj_path_valid",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_obj_path_valid(self) -> bool:
        """Indicate if the ObjPath property is valid."""
        return self._intf.get_property(IPickInfoData._metadata, IPickInfoData._get_is_obj_path_valid_metadata)

    _get_is_lat_lon_altitude_valid_metadata = { "name" : "is_lat_lon_altitude_valid",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_lat_lon_altitude_valid(self) -> bool:
        """Indicate if the Lat/Lon/Alt properties are valid."""
        return self._intf.get_property(IPickInfoData._metadata, IPickInfoData._get_is_lat_lon_altitude_valid_metadata)


agcls.AgClassCatalog.add_catalog_entry("{C87F43DA-DD89-4F13-BCB6-D78D0FE8D7E4}", IPickInfoData)
agcls.AgTypeNameMap["IPickInfoData"] = IPickInfoData

class IRubberBandPickInfoData(object):
    """Rubber-band mouse pick result."""
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{54417F99-E500-4BD8-A762-DC3367C7624C}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_obj_paths" : 1, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IRubberBandPickInfoData._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IRubberBandPickInfoData from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _get_obj_paths_metadata = { "name" : "obj_paths",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def obj_paths(self) -> "ObjPathCollection":
        """List of object paths selected."""
        return self._intf.get_property(IRubberBandPickInfoData._metadata, IRubberBandPickInfoData._get_obj_paths_metadata)


agcls.AgClassCatalog.add_catalog_entry("{54417F99-E500-4BD8-A762-DC3367C7624C}", IRubberBandPickInfoData)
agcls.AgTypeNameMap["IRubberBandPickInfoData"] = IRubberBandPickInfoData

class ISTKXApplication(object):
    """STK X Application object."""
    _num_methods = 28
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{A2BB8372-EA5F-4D9D-84C3-4D9E5B9A8840}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "execute_command" : 1,
                             "get_enable_connect" : 2,
                             "set_enable_connect" : 3,
                             "get_connect_port" : 4,
                             "set_connect_port" : 5,
                             "get_host_id" : 6,
                             "get_registration_id" : 7,
                             "get_version" : 8,
                             "get_licensing_report" : 9,
                             "get_vendor_id" : 10,
                             "set_vendor_id" : 11,
                             "set_online_options" : 12,
                             "get_online_options" : 13,
                             "set_connect_handler" : 14,
                             "get_log_file_full_name" : 15,
                             "get_logging_mode" : 16,
                             "set_logging_mode" : 17,
                             "get_connect_max_connections" : 18,
                             "set_connect_max_connections" : 19,
                             "execute_multiple_commands" : 20,
                             "is_feature_available" : 21,
                             "get_no_graphics" : 22,
                             "set_no_graphics" : 23,
                             "terminate" : 24,
                             "get_show_sla_if_not_accepted" : 25,
                             "set_show_sla_if_not_accepted" : 26,
                             "set_use_hook" : 27,
                             "use_software_renderer" : 28, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ISTKXApplication._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ISTKXApplication from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
        return ISTKXApplicationEventHandler(self._intf)
    
    _execute_command_metadata = { "name" : "execute_command",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def execute_command(self, command:str) -> "ExecCmdResult":
        """Send a connect command to STK X."""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._execute_command_metadata, command, out_arg())

    _get_enable_connect_metadata = { "name" : "enable_connect",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def enable_connect(self) -> bool:
        """Enable or disable TCP/IP connect command processing (default: disabled)."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_enable_connect_metadata)

    _set_enable_connect_metadata = { "name" : "enable_connect",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @enable_connect.setter
    def enable_connect(self, newVal:bool) -> None:
        return self._intf.set_property(ISTKXApplication._metadata, ISTKXApplication._set_enable_connect_metadata, newVal)

    _get_connect_port_metadata = { "name" : "connect_port",
            "arg_types" : (POINTER(agcom.SHORT),),
            "marshallers" : (agmarshall.SHORT_arg,) }
    @property
    def connect_port(self) -> int:
        """Specify TCP/IP port to be used by Connect (default: 5001)."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_connect_port_metadata)

    _set_connect_port_metadata = { "name" : "connect_port",
            "arg_types" : (agcom.SHORT,),
            "marshallers" : (agmarshall.SHORT_arg,) }
    @connect_port.setter
    def connect_port(self, newVal:int) -> None:
        return self._intf.set_property(ISTKXApplication._metadata, ISTKXApplication._set_connect_port_metadata, newVal)

    _get_host_id_metadata = { "name" : "host_id",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def host_id(self) -> str:
        """Return the Host ID."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_host_id_metadata)

    _get_registration_id_metadata = { "name" : "registration_id",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def registration_id(self) -> str:
        """Return the Registration ID."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_registration_id_metadata)

    _get_version_metadata = { "name" : "version",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def version(self) -> str:
        """Return the version number"""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_version_metadata)

    _get_licensing_report_metadata = { "name" : "get_licensing_report",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    def get_licensing_report(self) -> str:
        """This method is deprecated. Returns a formatted string that contains the license names and their states. The string is formatted as an XML document."""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._get_licensing_report_metadata, out_arg())

    _get_vendor_id_metadata = { "name" : "vendor_id",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def vendor_id(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_vendor_id_metadata)

    _set_vendor_id_metadata = { "name" : "vendor_id",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @vendor_id.setter
    def vendor_id(self, vendorID:str) -> None:
        return self._intf.set_property(ISTKXApplication._metadata, ISTKXApplication._set_vendor_id_metadata, vendorID)

    _set_online_options_metadata = { "name" : "set_online_options",
            "arg_types" : (agcom.VARIANT_BOOL, agcom.BSTR, agcom.LONG, agcom.BSTR, agcom.BSTR, agcom.VARIANT_BOOL, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg, agmarshall.BSTR_arg, agmarshall.LONG_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.VARIANT_BOOL_arg, agmarshall.VARIANT_BOOL_arg,) }
    def set_online_options(self, useProxy:bool, serverName:str, portNum:int, userName:str, password:str, savePassword:bool) -> bool:
        """Set http proxy online options"""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._set_online_options_metadata, useProxy, serverName, portNum, userName, password, savePassword, out_arg())

    _get_online_options_metadata = { "name" : "get_online_options",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL), POINTER(agcom.BSTR), POINTER(agcom.LONG), POINTER(agcom.BSTR), POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg, agmarshall.BSTR_arg, agmarshall.LONG_arg, agmarshall.BSTR_arg, agmarshall.VARIANT_BOOL_arg,) }
    def get_online_options(self) -> typing.Tuple[bool, str, int, str, bool]:
        """Get http proxy online options"""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._get_online_options_metadata, out_arg(), out_arg(), out_arg(), out_arg(), out_arg())

    _set_connect_handler_metadata = { "name" : "set_connect_handler",
            "arg_types" : (agcom.BSTR, agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg,) }
    def set_connect_handler(self, commandID:str, progID:str) -> None:
        """Set callback to handle a certain connect command"""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._set_connect_handler_metadata, commandID, progID)

    _get_log_file_full_name_metadata = { "name" : "log_file_full_name",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def log_file_full_name(self) -> str:
        """Return full path and log file name."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_log_file_full_name_metadata)

    _get_logging_mode_metadata = { "name" : "logging_mode",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(LOGGING_MODE),) }
    @property
    def logging_mode(self) -> "LOGGING_MODE":
        """Control the log file generation, and if the log file is deleted or not on application exit."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_logging_mode_metadata)

    _set_logging_mode_metadata = { "name" : "logging_mode",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(LOGGING_MODE),) }
    @logging_mode.setter
    def logging_mode(self, newVal:"LOGGING_MODE") -> None:
        return self._intf.set_property(ISTKXApplication._metadata, ISTKXApplication._set_logging_mode_metadata, newVal)

    _get_connect_max_connections_metadata = { "name" : "connect_max_connections",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def connect_max_connections(self) -> int:
        """Specify the maximum number of Connect connections to allow."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_connect_max_connections_metadata)

    _set_connect_max_connections_metadata = { "name" : "connect_max_connections",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @connect_max_connections.setter
    def connect_max_connections(self, newVal:int) -> None:
        return self._intf.set_property(ISTKXApplication._metadata, ISTKXApplication._set_connect_max_connections_metadata, newVal)

    _execute_multiple_commands_metadata = { "name" : "execute_multiple_commands",
            "arg_types" : (POINTER(agcom.LPSAFEARRAY), agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LPSAFEARRAY_arg, agmarshall.AgEnum_arg(EXEC_MULTI_CMD_RESULT_ACTION), agmarshall.AgInterface_out_arg,) }
    def execute_multiple_commands(self, connectCommands:list, eAction:"EXEC_MULTI_CMD_RESULT_ACTION") -> "ExecMultiCmdResult":
        """Execute multiple CONNECT actions. The method throws an exception if any of the specified commands have failed."""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._execute_multiple_commands_metadata, connectCommands, eAction, out_arg())

    _is_feature_available_metadata = { "name" : "is_feature_available",
            "arg_types" : (agcom.LONG, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.AgEnum_arg(FEATURE_CODES), agmarshall.VARIANT_BOOL_arg,) }
    def is_feature_available(self, featureCode:"FEATURE_CODES") -> bool:
        """Return true if the specified feature is available."""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._is_feature_available_metadata, featureCode, out_arg())

    _get_no_graphics_metadata = { "name" : "no_graphics",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def no_graphics(self) -> bool:
        """Start engine with or without graphics (default: engine starts with graphics.)."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_no_graphics_metadata)

    _set_no_graphics_metadata = { "name" : "no_graphics",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @no_graphics.setter
    def no_graphics(self, newVal:bool) -> None:
        return self._intf.set_property(ISTKXApplication._metadata, ISTKXApplication._set_no_graphics_metadata, newVal)

    _terminate_metadata = { "name" : "terminate",
            "arg_types" : (),
            "marshallers" : () }
    def terminate(self) -> None:
        """Terminates the use of STK Engine. This must be the last call to STK Engine."""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._terminate_metadata, )

    _get_show_sla_if_not_accepted_metadata = { "name" : "show_sla_if_not_accepted",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def show_sla_if_not_accepted(self) -> bool:
        """Show the Software License Agreement dialog if not already accepted."""
        return self._intf.get_property(ISTKXApplication._metadata, ISTKXApplication._get_show_sla_if_not_accepted_metadata)

    _set_show_sla_if_not_accepted_metadata = { "name" : "show_sla_if_not_accepted",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @show_sla_if_not_accepted.setter
    def show_sla_if_not_accepted(self, newVal:bool) -> None:
        return self._intf.set_property(ISTKXApplication._metadata, ISTKXApplication._set_show_sla_if_not_accepted_metadata, newVal)

    _get_use_hook_metadata = { "name" : "use_hook",
            "arg_types" : (),
            "marshallers" : () }
    @property
    def use_hook(self) -> None:
        """use_hook is a write-only property."""
        raise RuntimeError("use_hook is a write-only property.")


    _set_use_hook_metadata = { "name" : "use_hook",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @use_hook.setter
    def use_hook(self, newVal:bool) -> None:
        """Start engine with or without message hook setup (default: engine starts with message hook setup.)."""
        return self._intf.set_property(ISTKXApplication._metadata, ISTKXApplication._set_use_hook_metadata, newVal)

    _use_software_renderer_metadata = { "name" : "use_software_renderer",
            "arg_types" : (),
            "marshallers" : () }
    def use_software_renderer(self) -> None:
        """Configure engine graphics to use a software renderer in order to meet minimum graphics requirements. Enabling this option will result in significant performance impacts."""
        return self._intf.invoke(ISTKXApplication._metadata, ISTKXApplication._use_software_renderer_metadata, )


agcls.AgClassCatalog.add_catalog_entry("{A2BB8372-EA5F-4D9D-84C3-4D9E5B9A8840}", ISTKXApplication)
agcls.AgTypeNameMap["ISTKXApplication"] = ISTKXApplication

class IDataObject(object):
    """DataObject is used for OLE drag and drop operations"""
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{557F091D-247F-4040-B1E9-10E5BCEDFFD5}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_files" : 1, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDataObject._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDataObject from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _get_files_metadata = { "name" : "files",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def files(self) -> "DataObjectFiles":
        """Return a collection of filenames."""
        return self._intf.get_property(IDataObject._metadata, IDataObject._get_files_metadata)


agcls.AgClassCatalog.add_catalog_entry("{557F091D-247F-4040-B1E9-10E5BCEDFFD5}", IDataObject)
agcls.AgTypeNameMap["IDataObject"] = IDataObject

class IObjPathCollection(object):
    """Collection of object paths."""
    _num_methods = 4
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{831E53E8-4E79-4E2E-B289-A6AD76A76F3A}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_count" : 1,
                             "item" : 2,
                             "get__NewEnum" : 3,
                             "range" : 4, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IObjPathCollection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IObjPathCollection from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(IObjPathCollection._metadata, IObjPathCollection._get_count_metadata)

    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.BSTR_arg,) }
    def item(self, index:int) -> str:
        """Get the element at the specified index (0-based)."""
        return self._intf.invoke(IObjPathCollection._metadata, IObjPathCollection._item_metadata, index, out_arg())

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Return an object that can be used to iterate through all the object paths in the collection."""
        return self._intf.get_property(IObjPathCollection._metadata, IObjPathCollection._get__NewEnum_metadata)

    _range_metadata = { "name" : "range",
            "arg_types" : (agcom.LONG, agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.LONG_arg, agmarshall.LPSAFEARRAY_arg,) }
    def range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        return self._intf.invoke(IObjPathCollection._metadata, IObjPathCollection._range_metadata, startIndex, stopIndex, out_arg())

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{831E53E8-4E79-4E2E-B289-A6AD76A76F3A}", IObjPathCollection)
agcls.AgTypeNameMap["IObjPathCollection"] = IObjPathCollection

class IDrawElem(object):
    """Draw element."""
    _num_methods = 2
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{C661025D-FFB3-429A-A0B1-D8421DE76AC6}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_visible" : 1,
                             "set_visible" : 2, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDrawElem._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDrawElem from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _get_visible_metadata = { "name" : "visible",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def visible(self) -> bool:
        """Show or hide the element."""
        return self._intf.get_property(IDrawElem._metadata, IDrawElem._get_visible_metadata)

    _set_visible_metadata = { "name" : "visible",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @visible.setter
    def visible(self, newVal:bool) -> None:
        return self._intf.set_property(IDrawElem._metadata, IDrawElem._set_visible_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{C661025D-FFB3-429A-A0B1-D8421DE76AC6}", IDrawElem)
agcls.AgTypeNameMap["IDrawElem"] = IDrawElem

class IDrawElemRect(IDrawElem):
    """Define a rectangle in control coordinates."""
    _num_methods = 11
    _vtable_offset = IDrawElem._vtable_offset + IDrawElem._num_methods
    _metadata = {
        "uuid" : "{B017EED9-DC32-4865-BDB9-6C586DC1818C}",
        "vtable_reference" : IDrawElem._vtable_offset + IDrawElem._num_methods - 1,
        "method_offsets" : { "get_left" : 1,
                             "get_right" : 2,
                             "get_top" : 3,
                             "get_bottom" : 4,
                             "set" : 5,
                             "get_color" : 6,
                             "set_color" : 7,
                             "get_line_width" : 8,
                             "set_line_width" : 9,
                             "get_line_style" : 10,
                             "set_line_style" : 11, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDrawElemRect._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDrawElemRect from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDrawElem._private_init(self, intf)
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
    
    _get_left_metadata = { "name" : "left",
            "arg_types" : (POINTER(agcom.OLE_XPOS_PIXELS),),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg,) }
    @property
    def left(self) -> int:
        """The x-coordinate of the left edge of this rectangle."""
        return self._intf.get_property(IDrawElemRect._metadata, IDrawElemRect._get_left_metadata)

    _get_right_metadata = { "name" : "right",
            "arg_types" : (POINTER(agcom.OLE_XPOS_PIXELS),),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg,) }
    @property
    def right(self) -> int:
        """The x-coordinate of the right edge of this rectangle."""
        return self._intf.get_property(IDrawElemRect._metadata, IDrawElemRect._get_right_metadata)

    _get_top_metadata = { "name" : "top",
            "arg_types" : (POINTER(agcom.OLE_YPOS_PIXELS),),
            "marshallers" : (agmarshall.OLE_YPOS_PIXELS_arg,) }
    @property
    def top(self) -> int:
        """The y-coordinate of the top edge of this rectangle."""
        return self._intf.get_property(IDrawElemRect._metadata, IDrawElemRect._get_top_metadata)

    _get_bottom_metadata = { "name" : "bottom",
            "arg_types" : (POINTER(agcom.OLE_YPOS_PIXELS),),
            "marshallers" : (agmarshall.OLE_YPOS_PIXELS_arg,) }
    @property
    def bottom(self) -> int:
        """The y-coordinate of the bottom edge of this rectangle."""
        return self._intf.get_property(IDrawElemRect._metadata, IDrawElemRect._get_bottom_metadata)

    _set_metadata = { "name" : "set",
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS,),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg, agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg,) }
    def set(self, left:int, top:int, right:int, bottom:int) -> None:
        """Set the rectangle coordinates."""
        return self._intf.invoke(IDrawElemRect._metadata, IDrawElemRect._set_metadata, left, top, right, bottom)

    _get_color_metadata = { "name" : "color",
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @property
    def color(self) -> agcolor.Color:
        """Color of the rectangle."""
        return self._intf.get_property(IDrawElemRect._metadata, IDrawElemRect._get_color_metadata)

    _set_color_metadata = { "name" : "color",
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @color.setter
    def color(self, newVal:agcolor.Color) -> None:
        return self._intf.set_property(IDrawElemRect._metadata, IDrawElemRect._set_color_metadata, newVal)

    _get_line_width_metadata = { "name" : "line_width",
            "arg_types" : (POINTER(agcom.FLOAT),),
            "marshallers" : (agmarshall.FLOAT_arg,) }
    @property
    def line_width(self) -> float:
        """Specify the width of the line."""
        return self._intf.get_property(IDrawElemRect._metadata, IDrawElemRect._get_line_width_metadata)

    _set_line_width_metadata = { "name" : "line_width",
            "arg_types" : (agcom.FLOAT,),
            "marshallers" : (agmarshall.FLOAT_arg,) }
    @line_width.setter
    def line_width(self, newVal:float) -> None:
        return self._intf.set_property(IDrawElemRect._metadata, IDrawElemRect._set_line_width_metadata, newVal)

    _get_line_style_metadata = { "name" : "line_style",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(LINE_STYLE),) }
    @property
    def line_style(self) -> "LINE_STYLE":
        """Specify the style of the line."""
        return self._intf.get_property(IDrawElemRect._metadata, IDrawElemRect._get_line_style_metadata)

    _set_line_style_metadata = { "name" : "line_style",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(LINE_STYLE),) }
    @line_style.setter
    def line_style(self, newVal:"LINE_STYLE") -> None:
        return self._intf.set_property(IDrawElemRect._metadata, IDrawElemRect._set_line_style_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{B017EED9-DC32-4865-BDB9-6C586DC1818C}", IDrawElemRect)
agcls.AgTypeNameMap["IDrawElemRect"] = IDrawElemRect

class IDrawElemCollection(object):
    """Collection of elements to draw on the control."""
    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{3D6D784D-7C84-4A30-95D8-7D57AF7C560E}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_count" : 1,
                             "item" : 2,
                             "get__NewEnum" : 3,
                             "clear" : 4,
                             "add" : 5,
                             "remove" : 6,
                             "get_visible" : 7,
                             "set_visible" : 8, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDrawElemCollection._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDrawElemCollection from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IDrawElem":
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(IDrawElemCollection._metadata, IDrawElemCollection._get_count_metadata)

    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.AgInterface_out_arg,) }
    def item(self, index:int) -> "IDrawElem":
        """Get the element at the specified index (0-based)."""
        return self._intf.invoke(IDrawElemCollection._metadata, IDrawElemCollection._item_metadata, index, out_arg())

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Return an object that can be used to iterate through all the strings in the collection."""
        return self._intf.get_property(IDrawElemCollection._metadata, IDrawElemCollection._get__NewEnum_metadata)

    _clear_metadata = { "name" : "clear",
            "arg_types" : (),
            "marshallers" : () }
    def clear(self) -> None:
        """Clear the contents of the collection and updates the display."""
        return self._intf.invoke(IDrawElemCollection._metadata, IDrawElemCollection._clear_metadata, )

    _add_metadata = { "name" : "add",
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def add(self, elemType:str) -> "IDrawElem":
        """Factory to create and add a new element to the end of the sequence."""
        return self._intf.invoke(IDrawElemCollection._metadata, IDrawElemCollection._add_metadata, elemType, out_arg())

    _remove_metadata = { "name" : "remove",
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.AgInterface_in_arg("IDrawElem"),) }
    def remove(self, drawElem:"IDrawElem") -> None:
        """Remove the specified element."""
        return self._intf.invoke(IDrawElemCollection._metadata, IDrawElemCollection._remove_metadata, drawElem)

    _get_visible_metadata = { "name" : "visible",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def visible(self) -> bool:
        """Show or hide all the elements."""
        return self._intf.get_property(IDrawElemCollection._metadata, IDrawElemCollection._get_visible_metadata)

    _set_visible_metadata = { "name" : "visible",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @visible.setter
    def visible(self, newVal:bool) -> None:
        return self._intf.set_property(IDrawElemCollection._metadata, IDrawElemCollection._set_visible_metadata, newVal)

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{3D6D784D-7C84-4A30-95D8-7D57AF7C560E}", IDrawElemCollection)
agcls.AgTypeNameMap["IDrawElemCollection"] = IDrawElemCollection

class IWinProjectionPosition(object):
    """Projected window position detail."""
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{56FF29E4-6311-4E94-B91D-53C02288C55A}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_x_position" : 1,
                             "get_y_position" : 2,
                             "get_is_win_projection_position_valid" : 3, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IWinProjectionPosition._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IWinProjectionPosition from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _get_x_position_metadata = { "name" : "x_position",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def x_position(self) -> float:
        """Projected window X position."""
        return self._intf.get_property(IWinProjectionPosition._metadata, IWinProjectionPosition._get_x_position_metadata)

    _get_y_position_metadata = { "name" : "y_position",
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DOUBLE_arg,) }
    @property
    def y_position(self) -> float:
        """Projected window Y position."""
        return self._intf.get_property(IWinProjectionPosition._metadata, IWinProjectionPosition._get_y_position_metadata)

    _get_is_win_projection_position_valid_metadata = { "name" : "is_win_projection_position_valid",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_win_projection_position_valid(self) -> bool:
        """Indicate if the returned projected position is valid or not."""
        return self._intf.get_property(IWinProjectionPosition._metadata, IWinProjectionPosition._get_is_win_projection_position_valid_metadata)


agcls.AgClassCatalog.add_catalog_entry("{56FF29E4-6311-4E94-B91D-53C02288C55A}", IWinProjectionPosition)
agcls.AgTypeNameMap["IWinProjectionPosition"] = IWinProjectionPosition

class IDrawElemLine(IDrawElem):
    """Define a line in control coordinates."""
    _num_methods = 11
    _vtable_offset = IDrawElem._vtable_offset + IDrawElem._num_methods
    _metadata = {
        "uuid" : "{1A550DDC-7769-4A6C-9D0C-8E9D8C1757E2}",
        "vtable_reference" : IDrawElem._vtable_offset + IDrawElem._num_methods - 1,
        "method_offsets" : { "get_left" : 1,
                             "get_right" : 2,
                             "get_top" : 3,
                             "get_bottom" : 4,
                             "set" : 5,
                             "get_color" : 6,
                             "set_color" : 7,
                             "get_line_width" : 8,
                             "set_line_width" : 9,
                             "get_line_style" : 10,
                             "set_line_style" : 11, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDrawElemLine._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDrawElemLine from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDrawElem._private_init(self, intf)
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
    
    _get_left_metadata = { "name" : "left",
            "arg_types" : (POINTER(agcom.OLE_XPOS_PIXELS),),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg,) }
    @property
    def left(self) -> int:
        """The x-coordinate of the left edge of this line."""
        return self._intf.get_property(IDrawElemLine._metadata, IDrawElemLine._get_left_metadata)

    _get_right_metadata = { "name" : "right",
            "arg_types" : (POINTER(agcom.OLE_XPOS_PIXELS),),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg,) }
    @property
    def right(self) -> int:
        """The x-coordinate of the right edge of this line."""
        return self._intf.get_property(IDrawElemLine._metadata, IDrawElemLine._get_right_metadata)

    _get_top_metadata = { "name" : "top",
            "arg_types" : (POINTER(agcom.OLE_YPOS_PIXELS),),
            "marshallers" : (agmarshall.OLE_YPOS_PIXELS_arg,) }
    @property
    def top(self) -> int:
        """The y-coordinate of the top edge of this line."""
        return self._intf.get_property(IDrawElemLine._metadata, IDrawElemLine._get_top_metadata)

    _get_bottom_metadata = { "name" : "bottom",
            "arg_types" : (POINTER(agcom.OLE_YPOS_PIXELS),),
            "marshallers" : (agmarshall.OLE_YPOS_PIXELS_arg,) }
    @property
    def bottom(self) -> int:
        """The y-coordinate of the bottom edge of this line."""
        return self._intf.get_property(IDrawElemLine._metadata, IDrawElemLine._get_bottom_metadata)

    _set_metadata = { "name" : "set",
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS,),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg, agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg,) }
    def set(self, left:int, top:int, right:int, bottom:int) -> None:
        """Set the rectangle coordinates."""
        return self._intf.invoke(IDrawElemLine._metadata, IDrawElemLine._set_metadata, left, top, right, bottom)

    _get_color_metadata = { "name" : "color",
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @property
    def color(self) -> agcolor.Color:
        """Color of the rectangle."""
        return self._intf.get_property(IDrawElemLine._metadata, IDrawElemLine._get_color_metadata)

    _set_color_metadata = { "name" : "color",
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @color.setter
    def color(self, newVal:agcolor.Color) -> None:
        return self._intf.set_property(IDrawElemLine._metadata, IDrawElemLine._set_color_metadata, newVal)

    _get_line_width_metadata = { "name" : "line_width",
            "arg_types" : (POINTER(agcom.FLOAT),),
            "marshallers" : (agmarshall.FLOAT_arg,) }
    @property
    def line_width(self) -> float:
        """Specify the width of the line."""
        return self._intf.get_property(IDrawElemLine._metadata, IDrawElemLine._get_line_width_metadata)

    _set_line_width_metadata = { "name" : "line_width",
            "arg_types" : (agcom.FLOAT,),
            "marshallers" : (agmarshall.FLOAT_arg,) }
    @line_width.setter
    def line_width(self, newVal:float) -> None:
        return self._intf.set_property(IDrawElemLine._metadata, IDrawElemLine._set_line_width_metadata, newVal)

    _get_line_style_metadata = { "name" : "line_style",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(LINE_STYLE),) }
    @property
    def line_style(self) -> "LINE_STYLE":
        """Specify the style of the line."""
        return self._intf.get_property(IDrawElemLine._metadata, IDrawElemLine._get_line_style_metadata)

    _set_line_style_metadata = { "name" : "line_style",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(LINE_STYLE),) }
    @line_style.setter
    def line_style(self, newVal:"LINE_STYLE") -> None:
        return self._intf.set_property(IDrawElemLine._metadata, IDrawElemLine._set_line_style_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{1A550DDC-7769-4A6C-9D0C-8E9D8C1757E2}", IDrawElemLine)
agcls.AgTypeNameMap["IDrawElemLine"] = IDrawElemLine

class IExecCmdResult(object):
    """Collection of strings returned by the ExecuteCommand."""
    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{90EF2D03-F064-4F54-9E02-6E34E3CF5D55}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_count" : 1,
                             "item" : 2,
                             "get__NewEnum" : 3,
                             "range" : 4,
                             "get_is_succeeded" : 5, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IExecCmdResult._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IExecCmdResult from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(IExecCmdResult._metadata, IExecCmdResult._get_count_metadata)

    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.BSTR_arg,) }
    def item(self, index:int) -> str:
        """Get the element at the specified index (0-based)."""
        return self._intf.invoke(IExecCmdResult._metadata, IExecCmdResult._item_metadata, index, out_arg())

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Return an object that can be used to iterate through all the strings in the collection."""
        return self._intf.get_property(IExecCmdResult._metadata, IExecCmdResult._get__NewEnum_metadata)

    _range_metadata = { "name" : "range",
            "arg_types" : (agcom.LONG, agcom.LONG, POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.LONG_arg, agmarshall.LPSAFEARRAY_arg,) }
    def range(self, startIndex:int, stopIndex:int) -> list:
        """Return the elements within the specified range."""
        return self._intf.invoke(IExecCmdResult._metadata, IExecCmdResult._range_metadata, startIndex, stopIndex, out_arg())

    _get_is_succeeded_metadata = { "name" : "is_succeeded",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_succeeded(self) -> bool:
        """Indicate whether the object contains valid results."""
        return self._intf.get_property(IExecCmdResult._metadata, IExecCmdResult._get_is_succeeded_metadata)

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{90EF2D03-F064-4F54-9E02-6E34E3CF5D55}", IExecCmdResult)
agcls.AgTypeNameMap["IExecCmdResult"] = IExecCmdResult

class IExecMultiCmdResult(object):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{0558BE8E-AF66-4F52-9C6D-76962FC52577}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_count" : 1,
                             "item" : 2,
                             "get__NewEnum" : 3, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IExecMultiCmdResult._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IExecMultiCmdResult from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IExecCmdResult":
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Number of elements contained in the collection."""
        return self._intf.get_property(IExecMultiCmdResult._metadata, IExecMultiCmdResult._get_count_metadata)

    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.AgInterface_out_arg,) }
    def item(self, index:int) -> "ExecCmdResult":
        """Get the element at the specified index (0-based)."""
        return self._intf.invoke(IExecMultiCmdResult._metadata, IExecMultiCmdResult._item_metadata, index, out_arg())

    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Return an object that can be used to iterate through all the objects in the collection."""
        return self._intf.get_property(IExecMultiCmdResult._metadata, IExecMultiCmdResult._get__NewEnum_metadata)

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{0558BE8E-AF66-4F52-9C6D-76962FC52577}", IExecMultiCmdResult)
agcls.AgTypeNameMap["IExecMultiCmdResult"] = IExecMultiCmdResult

class IUiAxGraphics3DCntrl(object):
    """AGI Globe control."""
    _num_methods = 48
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{0975BA23-E273-4B8F-BA8D-32ECB328C092}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_back_color" : 1,
                             "set_back_color" : 2,
                             "get_picture" : 3,
                             "picture_put_reference" : 4,
                             "set_picture" : 5,
                             "pick_info" : 6,
                             "get_win_id" : 7,
                             "set_win_id" : 8,
                             "get_application" : 9,
                             "zoom_in" : 10,
                             "get_no_logo" : 11,
                             "set_no_logo" : 12,
                             "get_ole_drop_mode" : 13,
                             "set_ole_drop_mode" : 14,
                             "get_vendor_id" : 15,
                             "set_vendor_id" : 16,
                             "rubber_band_pick_info" : 17,
                             "get_mouse_mode" : 18,
                             "set_mouse_mode" : 19,
                             "get_draw_elements" : 20,
                             "get_ready_state" : 21,
                             "get_ppt_preload_mode" : 22,
                             "set_ppt_preload_mode" : 23,
                             "get_advanced_pick_mode" : 24,
                             "set_advanced_pick_mode" : 25,
                             "copy_from_win_id" : 26,
                             "start_object_editing" : 27,
                             "apply_object_editing" : 28,
                             "stop_object_editing" : 29,
                             "get_is_object_editing" : 30,
                             "get_in_zoom_mode" : 31,
                             "set_mouse_cursor_from_file" : 32,
                             "restore_mouse_cursor" : 33,
                             "set_mouse_cursor_from_handle" : 34,
                             "get_show_progress_image" : 35,
                             "set_show_progress_image" : 36,
                             "get_progress_image_x_offset" : 37,
                             "set_progress_image_x_offset" : 38,
                             "get_progress_image_y_offset" : 39,
                             "set_progress_image_y_offset" : 40,
                             "get_progress_image_file" : 41,
                             "set_progress_image_file" : 42,
                             "get_progress_image_x_origin" : 43,
                             "set_progress_image_x_origin" : 44,
                             "get_progress_image_y_origin" : 45,
                             "set_progress_image_y_origin" : 46,
                             "get_picture_from_file" : 47,
                             "set_picture_from_file" : 48, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUiAxGraphics3DCntrl._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUiAxGraphics3DCntrl from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
        return IUiAxGraphics3DCntrlEventHandler(self._intf)
    
    _get_back_color_metadata = { "name" : "back_color",
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_back_color_metadata)

    _set_back_color_metadata = { "name" : "back_color",
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_back_color_metadata, clr)

    _get_picture_metadata = { "name" : "picture",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    @property
    def picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_picture_metadata)

    _picture_put_reference_metadata = { "name" : "picture_put_reference",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    def picture_put_reference(self, pPicture:IPictureDisp) -> None:
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._picture_put_reference_metadata, pPicture)

    _set_picture_metadata = { "name" : "picture",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    @picture.setter
    def picture(self, pPicture:IPictureDisp) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_picture_metadata, pPicture)

    _pick_info_metadata = { "name" : "pick_info",
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg, agmarshall.AgInterface_out_arg,) }
    def pick_info(self, x:int, y:int) -> "PickInfoData":
        """Get detailed information about a mouse pick."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._pick_info_metadata, x, y, out_arg())

    _get_win_id_metadata = { "name" : "win_id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def win_id(self) -> int:
        """Window identifier (for Connect commands)."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_win_id_metadata)

    _set_win_id_metadata = { "name" : "win_id",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @win_id.setter
    def win_id(self, newVal:int) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_win_id_metadata, newVal)

    _get_application_metadata = { "name" : "application",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def application(self) -> "STKXApplication":
        """Reference to the STK X application object."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_application_metadata)

    _zoom_in_metadata = { "name" : "zoom_in",
            "arg_types" : (),
            "marshallers" : () }
    def zoom_in(self) -> None:
        """Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._zoom_in_metadata, )

    _get_no_logo_metadata = { "name" : "no_logo",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_no_logo_metadata)

    _set_no_logo_metadata = { "name" : "no_logo",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @no_logo.setter
    def no_logo(self, bNoLogo:bool) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_no_logo_metadata, bNoLogo)

    _get_ole_drop_mode_metadata = { "name" : "ole_drop_mode",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(OLE_DROP_MODE),) }
    @property
    def ole_drop_mode(self) -> "OLE_DROP_MODE":
        """How the control handles drop operations."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_ole_drop_mode_metadata)

    _set_ole_drop_mode_metadata = { "name" : "ole_drop_mode",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(OLE_DROP_MODE),) }
    @ole_drop_mode.setter
    def ole_drop_mode(self, psOLEDropMode:"OLE_DROP_MODE") -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_ole_drop_mode_metadata, psOLEDropMode)

    _get_vendor_id_metadata = { "name" : "vendor_id",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def vendor_id(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_vendor_id_metadata)

    _set_vendor_id_metadata = { "name" : "vendor_id",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @vendor_id.setter
    def vendor_id(self, vendorID:str) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_vendor_id_metadata, vendorID)

    _rubber_band_pick_info_metadata = { "name" : "rubber_band_pick_info",
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg, agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg, agmarshall.AgInterface_out_arg,) }
    def rubber_band_pick_info(self, left:int, top:int, right:int, bottom:int) -> "RubberBandPickInfoData":
        """Get detailed information about a rubber-band mouse pick. The values must be within the VO window (0 to width-1 for left and right, 0 to height-1 for top and bottom)."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._rubber_band_pick_info_metadata, left, top, right, bottom, out_arg())

    _get_mouse_mode_metadata = { "name" : "mouse_mode",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(MOUSE_MODE),) }
    @property
    def mouse_mode(self) -> "MOUSE_MODE":
        """Whether this control responds to mouse events."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_mouse_mode_metadata)

    _set_mouse_mode_metadata = { "name" : "mouse_mode",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(MOUSE_MODE),) }
    @mouse_mode.setter
    def mouse_mode(self, psMouseMode:"MOUSE_MODE") -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_mouse_mode_metadata, psMouseMode)

    _get_draw_elements_metadata = { "name" : "draw_elements",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def draw_elements(self) -> "IDrawElemCollection":
        """Elements to draw on the control."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_draw_elements_metadata)

    _get_ready_state_metadata = { "name" : "ready_state",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def ready_state(self) -> int:
        """Return/sets the background color of the control."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_ready_state_metadata)

    _get_ppt_preload_mode_metadata = { "name" : "ppt_preload_mode",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def ppt_preload_mode(self) -> bool:
        """Special mode for PowerPoint : if true the VO control window is kept around when switching between slides."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_ppt_preload_mode_metadata)

    _set_ppt_preload_mode_metadata = { "name" : "ppt_preload_mode",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @ppt_preload_mode.setter
    def ppt_preload_mode(self, bPptPreloadMode:bool) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_ppt_preload_mode_metadata, bPptPreloadMode)

    _get_advanced_pick_mode_metadata = { "name" : "advanced_pick_mode",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def advanced_pick_mode(self) -> bool:
        """If true, sets the advance pick mode."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_advanced_pick_mode_metadata)

    _set_advanced_pick_mode_metadata = { "name" : "advanced_pick_mode",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @advanced_pick_mode.setter
    def advanced_pick_mode(self, bAdvancePickMode:bool) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_advanced_pick_mode_metadata, bAdvancePickMode)

    _copy_from_win_id_metadata = { "name" : "copy_from_win_id",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    def copy_from_win_id(self, winID:int) -> None:
        """Copy an existing Window's scene into this control"""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._copy_from_win_id_metadata, winID)

    _start_object_editing_metadata = { "name" : "start_object_editing",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    def start_object_editing(self, objEditPath:str) -> None:
        """Enters into 3D object editing mode."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._start_object_editing_metadata, objEditPath)

    _apply_object_editing_metadata = { "name" : "apply_object_editing",
            "arg_types" : (),
            "marshallers" : () }
    def apply_object_editing(self) -> None:
        """Commit changes when in 3D object editing mode."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._apply_object_editing_metadata, )

    _stop_object_editing_metadata = { "name" : "stop_object_editing",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    def stop_object_editing(self, canceled:bool) -> None:
        """End 3D object editing mode."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._stop_object_editing_metadata, canceled)

    _get_is_object_editing_metadata = { "name" : "is_object_editing",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def is_object_editing(self) -> bool:
        """Return true if in 3D object editing mode."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_is_object_editing_metadata)

    _get_in_zoom_mode_metadata = { "name" : "in_zoom_mode",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def in_zoom_mode(self) -> bool:
        """Return true if in zoom in mode."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_in_zoom_mode_metadata)

    _set_mouse_cursor_from_file_metadata = { "name" : "set_mouse_cursor_from_file",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    def set_mouse_cursor_from_file(self, cursorFileName:str) -> None:
        """Set mouse cursor to the selected cursor file."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_mouse_cursor_from_file_metadata, cursorFileName)

    _restore_mouse_cursor_metadata = { "name" : "restore_mouse_cursor",
            "arg_types" : (),
            "marshallers" : () }
    def restore_mouse_cursor(self) -> None:
        """Restores mouse cursor back to normal."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._restore_mouse_cursor_metadata, )

    _set_mouse_cursor_from_handle_metadata = { "name" : "set_mouse_cursor_from_handle",
            "arg_types" : (agcom.OLE_HANDLE,),
            "marshallers" : (agmarshall.OLE_HANDLE_arg,) }
    def set_mouse_cursor_from_handle(self, cursorHandle:int) -> None:
        """Set mouse cursor to the passed cursor handle."""
        return self._intf.invoke(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_mouse_cursor_from_handle_metadata, cursorHandle)

    _get_show_progress_image_metadata = { "name" : "show_progress_image",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(SHOW_PROGRESS_IMAGE),) }
    @property
    def show_progress_image(self) -> "SHOW_PROGRESS_IMAGE":
        """The animated progress image type."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_show_progress_image_metadata)

    _set_show_progress_image_metadata = { "name" : "show_progress_image",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(SHOW_PROGRESS_IMAGE),) }
    @show_progress_image.setter
    def show_progress_image(self, psProgressImage:"SHOW_PROGRESS_IMAGE") -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_show_progress_image_metadata, psProgressImage)

    _get_progress_image_x_offset_metadata = { "name" : "progress_image_x_offset",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def progress_image_x_offset(self) -> int:
        """The horizontal X offset for animated progress image."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_progress_image_x_offset_metadata)

    _set_progress_image_x_offset_metadata = { "name" : "progress_image_x_offset",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @progress_image_x_offset.setter
    def progress_image_x_offset(self, xOffset:int) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_progress_image_x_offset_metadata, xOffset)

    _get_progress_image_y_offset_metadata = { "name" : "progress_image_y_offset",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def progress_image_y_offset(self) -> int:
        """The vertical Y offset for animated progress image."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_progress_image_y_offset_metadata)

    _set_progress_image_y_offset_metadata = { "name" : "progress_image_y_offset",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @progress_image_y_offset.setter
    def progress_image_y_offset(self, yOffset:int) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_progress_image_y_offset_metadata, yOffset)

    _get_progress_image_file_metadata = { "name" : "progress_image_file",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def progress_image_file(self) -> str:
        """The complete image file name/path for animated progress image."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_progress_image_file_metadata)

    _set_progress_image_file_metadata = { "name" : "progress_image_file",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @progress_image_file.setter
    def progress_image_file(self, imageFile:str) -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_progress_image_file_metadata, imageFile)

    _get_progress_image_x_origin_metadata = { "name" : "progress_image_x_origin",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(PROGRESS_IMAGE_X_ORIGIN),) }
    @property
    def progress_image_x_origin(self) -> "PROGRESS_IMAGE_X_ORIGIN":
        """The X origin alignment for animated progress image."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_progress_image_x_origin_metadata)

    _set_progress_image_x_origin_metadata = { "name" : "progress_image_x_origin",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(PROGRESS_IMAGE_X_ORIGIN),) }
    @progress_image_x_origin.setter
    def progress_image_x_origin(self, progressImageXOrigin:"PROGRESS_IMAGE_X_ORIGIN") -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_progress_image_x_origin_metadata, progressImageXOrigin)

    _get_progress_image_y_origin_metadata = { "name" : "progress_image_y_origin",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(PROGRESS_IMAGE_Y_ORIGIN),) }
    @property
    def progress_image_y_origin(self) -> "PROGRESS_IMAGE_Y_ORIGIN":
        """The Y origin alignment for animated progress image."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_progress_image_y_origin_metadata)

    _set_progress_image_y_origin_metadata = { "name" : "progress_image_y_origin",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(PROGRESS_IMAGE_Y_ORIGIN),) }
    @progress_image_y_origin.setter
    def progress_image_y_origin(self, progressImageYOrigin:"PROGRESS_IMAGE_Y_ORIGIN") -> None:
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_progress_image_y_origin_metadata, progressImageYOrigin)

    _get_picture_from_file_metadata = { "name" : "picture_from_file",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def picture_from_file(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        return self._intf.get_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._get_picture_from_file_metadata)

    _set_picture_from_file_metadata = { "name" : "picture_from_file",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @picture_from_file.setter
    def picture_from_file(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        return self._intf.set_property(IUiAxGraphics3DCntrl._metadata, IUiAxGraphics3DCntrl._set_picture_from_file_metadata, pictureFile)


agcls.AgClassCatalog.add_catalog_entry("{0975BA23-E273-4B8F-BA8D-32ECB328C092}", IUiAxGraphics3DCntrl)
agcls.AgTypeNameMap["IUiAxGraphics3DCntrl"] = IUiAxGraphics3DCntrl

class IUiAx2DCntrl(object):
    """AGI Map control."""
    _num_methods = 45
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{A5C18751-1656-4FB9-BA4E-D5746D509CFC}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_back_color" : 1,
                             "set_back_color" : 2,
                             "get_picture" : 3,
                             "picture_put_reference" : 4,
                             "set_picture" : 5,
                             "get_win_id" : 6,
                             "set_win_id" : 7,
                             "zoom_in" : 8,
                             "zoom_out" : 9,
                             "pick_info" : 10,
                             "get_application" : 11,
                             "get_no_logo" : 12,
                             "set_no_logo" : 13,
                             "get_ole_drop_mode" : 14,
                             "set_ole_drop_mode" : 15,
                             "get_vendor_id" : 16,
                             "set_vendor_id" : 17,
                             "get_mouse_mode" : 18,
                             "set_mouse_mode" : 19,
                             "get_ready_state" : 20,
                             "copy_from_win_id" : 21,
                             "rubber_band_pick_info" : 22,
                             "get_advanced_pick_mode" : 23,
                             "set_advanced_pick_mode" : 24,
                             "get_window_projected_position" : 25,
                             "get_in_zoom_mode" : 26,
                             "set_mouse_cursor_from_file" : 27,
                             "restore_mouse_cursor" : 28,
                             "set_mouse_cursor_from_handle" : 29,
                             "get_show_progress_image" : 30,
                             "set_show_progress_image" : 31,
                             "get_progress_image_x_offset" : 32,
                             "set_progress_image_x_offset" : 33,
                             "get_progress_image_y_offset" : 34,
                             "set_progress_image_y_offset" : 35,
                             "get_progress_image_file" : 36,
                             "set_progress_image_file" : 37,
                             "get_progress_image_x_origin" : 38,
                             "set_progress_image_x_origin" : 39,
                             "get_progress_image_y_origin" : 40,
                             "set_progress_image_y_origin" : 41,
                             "get_picture_from_file" : 42,
                             "set_picture_from_file" : 43,
                             "get_pan_mode_enabled" : 44,
                             "set_pan_mode_enabled" : 45, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUiAx2DCntrl._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUiAx2DCntrl from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
        return IUiAxGraphics2DCntrlEventHandler(self._intf)
    
    _get_back_color_metadata = { "name" : "back_color",
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_back_color_metadata)

    _set_back_color_metadata = { "name" : "back_color",
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_back_color_metadata, clr)

    _get_picture_metadata = { "name" : "picture",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    @property
    def picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_picture_metadata)

    _picture_put_reference_metadata = { "name" : "picture_put_reference",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    def picture_put_reference(self, pPicture:IPictureDisp) -> None:
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._picture_put_reference_metadata, pPicture)

    _set_picture_metadata = { "name" : "picture",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    @picture.setter
    def picture(self, pPicture:IPictureDisp) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_picture_metadata, pPicture)

    _get_win_id_metadata = { "name" : "win_id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def win_id(self) -> int:
        """Window identifier (for Connect commands)."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_win_id_metadata)

    _set_win_id_metadata = { "name" : "win_id",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @win_id.setter
    def win_id(self, newVal:int) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_win_id_metadata, newVal)

    _zoom_in_metadata = { "name" : "zoom_in",
            "arg_types" : (),
            "marshallers" : () }
    def zoom_in(self) -> None:
        """Enter zoom-in mode. User must left click-and-drag mouse to define area to zoom."""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._zoom_in_metadata, )

    _zoom_out_metadata = { "name" : "zoom_out",
            "arg_types" : (),
            "marshallers" : () }
    def zoom_out(self) -> None:
        """Zoom out to view a larger portion of a previously magnified map."""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._zoom_out_metadata, )

    _pick_info_metadata = { "name" : "pick_info",
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg, agmarshall.AgInterface_out_arg,) }
    def pick_info(self, x:int, y:int) -> "PickInfoData":
        """Get detailed information about a mouse pick."""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._pick_info_metadata, x, y, out_arg())

    _get_application_metadata = { "name" : "application",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def application(self) -> "STKXApplication":
        """Reference to the STK X application object."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_application_metadata)

    _get_no_logo_metadata = { "name" : "no_logo",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_no_logo_metadata)

    _set_no_logo_metadata = { "name" : "no_logo",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @no_logo.setter
    def no_logo(self, bNoLogo:bool) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_no_logo_metadata, bNoLogo)

    _get_ole_drop_mode_metadata = { "name" : "ole_drop_mode",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(OLE_DROP_MODE),) }
    @property
    def ole_drop_mode(self) -> "OLE_DROP_MODE":
        """How the control handles drop operations."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_ole_drop_mode_metadata)

    _set_ole_drop_mode_metadata = { "name" : "ole_drop_mode",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(OLE_DROP_MODE),) }
    @ole_drop_mode.setter
    def ole_drop_mode(self, psOLEDropMode:"OLE_DROP_MODE") -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_ole_drop_mode_metadata, psOLEDropMode)

    _get_vendor_id_metadata = { "name" : "vendor_id",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def vendor_id(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_vendor_id_metadata)

    _set_vendor_id_metadata = { "name" : "vendor_id",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @vendor_id.setter
    def vendor_id(self, vendorID:str) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_vendor_id_metadata, vendorID)

    _get_mouse_mode_metadata = { "name" : "mouse_mode",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(MOUSE_MODE),) }
    @property
    def mouse_mode(self) -> "MOUSE_MODE":
        """Whether this control responds to mouse events."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_mouse_mode_metadata)

    _set_mouse_mode_metadata = { "name" : "mouse_mode",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(MOUSE_MODE),) }
    @mouse_mode.setter
    def mouse_mode(self, psMouseMode:"MOUSE_MODE") -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_mouse_mode_metadata, psMouseMode)

    _get_ready_state_metadata = { "name" : "ready_state",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def ready_state(self) -> int:
        """Return/sets the background color of the control."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_ready_state_metadata)

    _copy_from_win_id_metadata = { "name" : "copy_from_win_id",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    def copy_from_win_id(self, winID:int) -> None:
        """Copy an existing Window's scene into this control"""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._copy_from_win_id_metadata, winID)

    _rubber_band_pick_info_metadata = { "name" : "rubber_band_pick_info",
            "arg_types" : (agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, agcom.OLE_XPOS_PIXELS, agcom.OLE_YPOS_PIXELS, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg, agmarshall.OLE_XPOS_PIXELS_arg, agmarshall.OLE_YPOS_PIXELS_arg, agmarshall.AgInterface_out_arg,) }
    def rubber_band_pick_info(self, left:int, top:int, right:int, bottom:int) -> "RubberBandPickInfoData":
        """Get detailed information about a rubber-band mouse pick. The values must be within the 2D window (0 to width-1 for left and right, 0 to height-1 for top and bottom)."""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._rubber_band_pick_info_metadata, left, top, right, bottom, out_arg())

    _get_advanced_pick_mode_metadata = { "name" : "advanced_pick_mode",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def advanced_pick_mode(self) -> bool:
        """If true, sets the advance pick mode."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_advanced_pick_mode_metadata)

    _set_advanced_pick_mode_metadata = { "name" : "advanced_pick_mode",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @advanced_pick_mode.setter
    def advanced_pick_mode(self, bAdvancePickMode:bool) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_advanced_pick_mode_metadata, bAdvancePickMode)

    _get_window_projected_position_metadata = { "name" : "get_window_projected_position",
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.LONG, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.DOUBLE_arg, agmarshall.AgEnum_arg(GRAPHICS_2D_DRAW_COORDS), agmarshall.AgInterface_out_arg,) }
    def get_window_projected_position(self, lat:float, lon:float, alt:float, drawCoords:"GRAPHICS_2D_DRAW_COORDS") -> "WinProjectionPosition":
        """Get the window projected position for given values."""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_window_projected_position_metadata, lat, lon, alt, drawCoords, out_arg())

    _get_in_zoom_mode_metadata = { "name" : "in_zoom_mode",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def in_zoom_mode(self) -> bool:
        """Return true if in zoom in mode."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_in_zoom_mode_metadata)

    _set_mouse_cursor_from_file_metadata = { "name" : "set_mouse_cursor_from_file",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    def set_mouse_cursor_from_file(self, cursorFileName:str) -> None:
        """Set mouse cursor to the selected cursor file."""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_mouse_cursor_from_file_metadata, cursorFileName)

    _restore_mouse_cursor_metadata = { "name" : "restore_mouse_cursor",
            "arg_types" : (),
            "marshallers" : () }
    def restore_mouse_cursor(self) -> None:
        """Restores mouse cursor back to normal."""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._restore_mouse_cursor_metadata, )

    _set_mouse_cursor_from_handle_metadata = { "name" : "set_mouse_cursor_from_handle",
            "arg_types" : (agcom.OLE_HANDLE,),
            "marshallers" : (agmarshall.OLE_HANDLE_arg,) }
    def set_mouse_cursor_from_handle(self, cursorHandle:int) -> None:
        """Set mouse cursor to the passed cursor handle."""
        return self._intf.invoke(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_mouse_cursor_from_handle_metadata, cursorHandle)

    _get_show_progress_image_metadata = { "name" : "show_progress_image",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(SHOW_PROGRESS_IMAGE),) }
    @property
    def show_progress_image(self) -> "SHOW_PROGRESS_IMAGE":
        """The animated progress image type."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_show_progress_image_metadata)

    _set_show_progress_image_metadata = { "name" : "show_progress_image",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(SHOW_PROGRESS_IMAGE),) }
    @show_progress_image.setter
    def show_progress_image(self, psProgressImage:"SHOW_PROGRESS_IMAGE") -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_show_progress_image_metadata, psProgressImage)

    _get_progress_image_x_offset_metadata = { "name" : "progress_image_x_offset",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def progress_image_x_offset(self) -> int:
        """The horizontal X offset for animated progress image."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_progress_image_x_offset_metadata)

    _set_progress_image_x_offset_metadata = { "name" : "progress_image_x_offset",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @progress_image_x_offset.setter
    def progress_image_x_offset(self, xOffset:int) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_progress_image_x_offset_metadata, xOffset)

    _get_progress_image_y_offset_metadata = { "name" : "progress_image_y_offset",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def progress_image_y_offset(self) -> int:
        """The vertical Y offset for animated progress image."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_progress_image_y_offset_metadata)

    _set_progress_image_y_offset_metadata = { "name" : "progress_image_y_offset",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @progress_image_y_offset.setter
    def progress_image_y_offset(self, yOffset:int) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_progress_image_y_offset_metadata, yOffset)

    _get_progress_image_file_metadata = { "name" : "progress_image_file",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def progress_image_file(self) -> str:
        """The complete image file name/path for animated progress image."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_progress_image_file_metadata)

    _set_progress_image_file_metadata = { "name" : "progress_image_file",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @progress_image_file.setter
    def progress_image_file(self, imageFile:str) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_progress_image_file_metadata, imageFile)

    _get_progress_image_x_origin_metadata = { "name" : "progress_image_x_origin",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(PROGRESS_IMAGE_X_ORIGIN),) }
    @property
    def progress_image_x_origin(self) -> "PROGRESS_IMAGE_X_ORIGIN":
        """The X origin alignment for animated progress image."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_progress_image_x_origin_metadata)

    _set_progress_image_x_origin_metadata = { "name" : "progress_image_x_origin",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(PROGRESS_IMAGE_X_ORIGIN),) }
    @progress_image_x_origin.setter
    def progress_image_x_origin(self, progressImageXOrigin:"PROGRESS_IMAGE_X_ORIGIN") -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_progress_image_x_origin_metadata, progressImageXOrigin)

    _get_progress_image_y_origin_metadata = { "name" : "progress_image_y_origin",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(PROGRESS_IMAGE_Y_ORIGIN),) }
    @property
    def progress_image_y_origin(self) -> "PROGRESS_IMAGE_Y_ORIGIN":
        """The Y origin alignment for animated progress image."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_progress_image_y_origin_metadata)

    _set_progress_image_y_origin_metadata = { "name" : "progress_image_y_origin",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(PROGRESS_IMAGE_Y_ORIGIN),) }
    @progress_image_y_origin.setter
    def progress_image_y_origin(self, progressImageYOrigin:"PROGRESS_IMAGE_Y_ORIGIN") -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_progress_image_y_origin_metadata, progressImageYOrigin)

    _get_picture_from_file_metadata = { "name" : "picture_from_file",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def picture_from_file(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_picture_from_file_metadata)

    _set_picture_from_file_metadata = { "name" : "picture_from_file",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @picture_from_file.setter
    def picture_from_file(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_picture_from_file_metadata, pictureFile)

    _get_pan_mode_enabled_metadata = { "name" : "pan_mode_enabled",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def pan_mode_enabled(self) -> bool:
        """Enable/disable pan mode for map control."""
        return self._intf.get_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._get_pan_mode_enabled_metadata)

    _set_pan_mode_enabled_metadata = { "name" : "pan_mode_enabled",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @pan_mode_enabled.setter
    def pan_mode_enabled(self, bPanMode:bool) -> None:
        return self._intf.set_property(IUiAx2DCntrl._metadata, IUiAx2DCntrl._set_pan_mode_enabled_metadata, bPanMode)


agcls.AgClassCatalog.add_catalog_entry("{A5C18751-1656-4FB9-BA4E-D5746D509CFC}", IUiAx2DCntrl)
agcls.AgTypeNameMap["IUiAx2DCntrl"] = IUiAx2DCntrl

class ISTKXApplicationPartnerAccess(object):
    """Access to the application object model for business partners."""
    _num_methods = 1
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{ABF4E08E-211F-40B6-A2F0-6938DAA560CE}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "grant_partner_access" : 1, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(ISTKXApplicationPartnerAccess._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create ISTKXApplicationPartnerAccess from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _grant_partner_access_metadata = { "name" : "grant_partner_access",
            "arg_types" : (agcom.BSTR, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.BSTR_arg, agmarshall.AgInterface_out_arg,) }
    def grant_partner_access(self, vendor:str, product:str, key:str) -> "STKXApplication":
        """Provide object model root for authorized business partners."""
        return self._intf.invoke(ISTKXApplicationPartnerAccess._metadata, ISTKXApplicationPartnerAccess._grant_partner_access_metadata, vendor, product, key, out_arg())


agcls.AgClassCatalog.add_catalog_entry("{ABF4E08E-211F-40B6-A2F0-6938DAA560CE}", ISTKXApplicationPartnerAccess)
agcls.AgTypeNameMap["ISTKXApplicationPartnerAccess"] = ISTKXApplicationPartnerAccess

class IDataObjectFiles(object):
    """Collection of file names."""
    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{C4428821-C59F-45B1-9747-0AD1F988317E}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get__NewEnum" : 1,
                             "item" : 2,
                             "get_count" : 3, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IDataObjectFiles._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IDataObjectFiles from source object.")
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
        self.__dict__["_enumerator"] = self._NewEnum
        self._enumerator.reset()
        return self
    def __next__(self) -> str:
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval
    
    _get__NewEnum_metadata = { "name" : "_NewEnum",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVARIANT_arg,) }
    @property
    def _NewEnum(self) -> enumerator_proxy:
        """Return an object that can be used to iterate through all the file names in the collection."""
        return self._intf.get_property(IDataObjectFiles._metadata, IDataObjectFiles._get__NewEnum_metadata)

    _item_metadata = { "name" : "item",
            "arg_types" : (agcom.LONG, POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.LONG_arg, agmarshall.BSTR_arg,) }
    def item(self, index:int) -> str:
        """Get the file name at the specified index (0-based)."""
        return self._intf.invoke(IDataObjectFiles._metadata, IDataObjectFiles._item_metadata, index, out_arg())

    _get_count_metadata = { "name" : "count",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def count(self) -> int:
        """Number of file names contained in the collection."""
        return self._intf.get_property(IDataObjectFiles._metadata, IDataObjectFiles._get_count_metadata)

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{C4428821-C59F-45B1-9747-0AD1F988317E}", IDataObjectFiles)
agcls.AgTypeNameMap["IDataObjectFiles"] = IDataObjectFiles

class IUiAxGraphics2DAnalysisCntrl(object):
    """AGI Gfx Analysis control."""
    _num_methods = 17
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _metadata = {
        "uuid" : "{5933D068-12E5-4B73-96A3-E06CC3ACC05A}",
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
        "method_offsets" : { "get_back_color" : 1,
                             "set_back_color" : 2,
                             "get_picture" : 3,
                             "picture_put_reference" : 4,
                             "set_picture" : 5,
                             "get_no_logo" : 6,
                             "set_no_logo" : 7,
                             "get_vendor_id" : 8,
                             "set_vendor_id" : 9,
                             "get_ready_state" : 10,
                             "get_application" : 11,
                             "get_control_mode" : 12,
                             "set_control_mode" : 13,
                             "get_picture_from_file" : 14,
                             "set_picture_from_file" : 15,
                             "get_win_id" : 16,
                             "set_win_id" : 17, }
    }
    def __init__(self, sourceObject=None):
        self.__dict__["_intf"] = interface_proxy()
        if sourceObject is not None and sourceObject._intf is not None:
            intf = sourceObject._intf.query_interface(agcom.GUID(IUiAxGraphics2DAnalysisCntrl._metadata["uuid"]))
            if intf is not None:
                self._private_init(intf)
                del(intf)
            else:
                raise STKInvalidCastError("Failed to create IUiAxGraphics2DAnalysisCntrl from source object.")
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
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
    
    _get_back_color_metadata = { "name" : "back_color",
            "arg_types" : (POINTER(agcom.OLE_COLOR),),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @property
    def back_color(self) -> agcolor.Color:
        """The background color of the control."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_back_color_metadata)

    _set_back_color_metadata = { "name" : "back_color",
            "arg_types" : (agcom.OLE_COLOR,),
            "marshallers" : (agmarshall.OLE_COLOR_arg,) }
    @back_color.setter
    def back_color(self, clr:agcolor.Color) -> None:
        return self._intf.set_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._set_back_color_metadata, clr)

    _get_picture_metadata = { "name" : "picture",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    @property
    def picture(self) -> IPictureDisp:
        """The splash logo graphic to be displayed in the control."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_picture_metadata)

    _picture_put_reference_metadata = { "name" : "picture_put_reference",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    def picture_put_reference(self, pPicture:IPictureDisp) -> None:
        return self._intf.invoke(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._picture_put_reference_metadata, pPicture)

    _set_picture_metadata = { "name" : "picture",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IPictureDisp_arg,) }
    @picture.setter
    def picture(self, pPicture:IPictureDisp) -> None:
        return self._intf.set_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._set_picture_metadata, pPicture)

    _get_no_logo_metadata = { "name" : "no_logo",
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @property
    def no_logo(self) -> bool:
        """If true, the splash logo is not shown."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_no_logo_metadata)

    _set_no_logo_metadata = { "name" : "no_logo",
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VARIANT_BOOL_arg,) }
    @no_logo.setter
    def no_logo(self, bNoLogo:bool) -> None:
        return self._intf.set_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._set_no_logo_metadata, bNoLogo)

    _get_vendor_id_metadata = { "name" : "vendor_id",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def vendor_id(self) -> str:
        """This property is deprecated. The identifier of the vendor."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_vendor_id_metadata)

    _set_vendor_id_metadata = { "name" : "vendor_id",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @vendor_id.setter
    def vendor_id(self, vendorID:str) -> None:
        return self._intf.set_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._set_vendor_id_metadata, vendorID)

    _get_ready_state_metadata = { "name" : "ready_state",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def ready_state(self) -> int:
        """Return the ready state of the control."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_ready_state_metadata)

    _get_application_metadata = { "name" : "application",
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.AgInterface_out_arg,) }
    @property
    def application(self) -> "STKXApplication":
        """Reference to the STK X application object."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_application_metadata)

    _get_control_mode_metadata = { "name" : "control_mode",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.AgEnum_arg(GRAPHICS_2D_ANALYSIS_MODE),) }
    @property
    def control_mode(self) -> "GRAPHICS_2D_ANALYSIS_MODE":
        """The Graphics control mode."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_control_mode_metadata)

    _set_control_mode_metadata = { "name" : "control_mode",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.AgEnum_arg(GRAPHICS_2D_ANALYSIS_MODE),) }
    @control_mode.setter
    def control_mode(self, eGfxAnalysisMode:"GRAPHICS_2D_ANALYSIS_MODE") -> None:
        return self._intf.set_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._set_control_mode_metadata, eGfxAnalysisMode)

    _get_picture_from_file_metadata = { "name" : "picture_from_file",
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @property
    def picture_from_file(self) -> str:
        """The splash logo graphic file to be displayed in the control."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_picture_from_file_metadata)

    _set_picture_from_file_metadata = { "name" : "picture_from_file",
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BSTR_arg,) }
    @picture_from_file.setter
    def picture_from_file(self, pictureFile:str) -> None:
        """The splash logo graphic file to be displayed in the control."""
        return self._intf.set_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._set_picture_from_file_metadata, pictureFile)

    _get_win_id_metadata = { "name" : "win_id",
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LONG_arg,) }
    @property
    def win_id(self) -> int:
        """Window identifier (for Connect commands)."""
        return self._intf.get_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._get_win_id_metadata)

    _set_win_id_metadata = { "name" : "win_id",
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.LONG_arg,) }
    @win_id.setter
    def win_id(self, newVal:int) -> None:
        return self._intf.set_property(IUiAxGraphics2DAnalysisCntrl._metadata, IUiAxGraphics2DAnalysisCntrl._set_win_id_metadata, newVal)


agcls.AgClassCatalog.add_catalog_entry("{5933D068-12E5-4B73-96A3-E06CC3ACC05A}", IUiAxGraphics2DAnalysisCntrl)
agcls.AgTypeNameMap["IUiAxGraphics2DAnalysisCntrl"] = IUiAxGraphics2DAnalysisCntrl



class ExecCmdResult(IExecCmdResult):
    """Collection of strings returned by the ExecuteCommand."""
    def __init__(self, sourceObject=None):
        IExecCmdResult.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IExecCmdResult._private_init(self, intf)
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
agcls.AgTypeNameMap["ExecCmdResult"] = ExecCmdResult

class ExecMultiCmdResult(IExecMultiCmdResult):
    """Collection of objects returned by the ExecuteMultipleCommands."""
    def __init__(self, sourceObject=None):
        IExecMultiCmdResult.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IExecMultiCmdResult._private_init(self, intf)
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
agcls.AgTypeNameMap["ExecMultiCmdResult"] = ExecMultiCmdResult

class UiAxGraphics3DCntrl(IUiAxGraphics3DCntrl):
    """AGI Globe control."""
    def __init__(self, sourceObject=None):
        IUiAxGraphics3DCntrl.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUiAxGraphics3DCntrl._private_init(self, intf)
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
agcls.AgTypeNameMap["UiAxGraphics3DCntrl"] = UiAxGraphics3DCntrl

class UiAx2DCntrl(IUiAx2DCntrl):
    """AGI Map control."""
    def __init__(self, sourceObject=None):
        IUiAx2DCntrl.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUiAx2DCntrl._private_init(self, intf)
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
agcls.AgTypeNameMap["UiAx2DCntrl"] = UiAx2DCntrl

class PickInfoData(IPickInfoData):
    """Single mouse pick result."""
    def __init__(self, sourceObject=None):
        IPickInfoData.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IPickInfoData._private_init(self, intf)
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
agcls.AgTypeNameMap["PickInfoData"] = PickInfoData

class STKXApplication(ISTKXApplication):
    """STK X Application object."""
    def __init__(self, sourceObject=None):
        ISTKXApplication.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ISTKXApplication._private_init(self, intf)
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
agcls.AgTypeNameMap["STKXApplication"] = STKXApplication

class STKXApplicationPartnerAccess(ISTKXApplicationPartnerAccess):
    """STK X Application Partner Access object."""
    def __init__(self, sourceObject=None):
        ISTKXApplicationPartnerAccess.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ISTKXApplicationPartnerAccess._private_init(self, intf)
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
agcls.AgTypeNameMap["STKXApplicationPartnerAccess"] = STKXApplicationPartnerAccess

class DataObject(IDataObject):
    """Data Object for OLE drag & drop operations."""
    def __init__(self, sourceObject=None):
        IDataObject.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDataObject._private_init(self, intf)
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
agcls.AgTypeNameMap["DataObject"] = DataObject

class DataObjectFiles(IDataObjectFiles):
    """Collection of files for OLE drag & drop operations."""
    def __init__(self, sourceObject=None):
        IDataObjectFiles.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDataObjectFiles._private_init(self, intf)
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
agcls.AgTypeNameMap["DataObjectFiles"] = DataObjectFiles

class RubberBandPickInfoData(IRubberBandPickInfoData):
    """Rubber-band mouse pick result."""
    def __init__(self, sourceObject=None):
        IRubberBandPickInfoData.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IRubberBandPickInfoData._private_init(self, intf)
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
agcls.AgTypeNameMap["RubberBandPickInfoData"] = RubberBandPickInfoData

class ObjPathCollection(IObjPathCollection):
    """Collection of object paths."""
    def __init__(self, sourceObject=None):
        IObjPathCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IObjPathCollection._private_init(self, intf)
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
agcls.AgTypeNameMap["ObjPathCollection"] = ObjPathCollection

class DrawElemRect(IDrawElemRect):
    """Define a rectangle in window coordinates."""
    def __init__(self, sourceObject=None):
        IDrawElemRect.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDrawElemRect._private_init(self, intf)
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
agcls.AgTypeNameMap["DrawElemRect"] = DrawElemRect

class DrawElemCollection(IDrawElemCollection):
    """Collection of elements to draw on the control."""
    def __init__(self, sourceObject=None):
        IDrawElemCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDrawElemCollection._private_init(self, intf)
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
agcls.AgTypeNameMap["DrawElemCollection"] = DrawElemCollection

class Draw2DElemRect(IDrawElemRect):
    """Define a rectangle in window coordinates for map control."""
    def __init__(self, sourceObject=None):
        IDrawElemRect.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDrawElemRect._private_init(self, intf)
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
agcls.AgTypeNameMap["Draw2DElemRect"] = Draw2DElemRect

class Draw2DElemCollection(IDrawElemCollection):
    """Collection of elements to draw on map control."""
    def __init__(self, sourceObject=None):
        IDrawElemCollection.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDrawElemCollection._private_init(self, intf)
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
agcls.AgTypeNameMap["Draw2DElemCollection"] = Draw2DElemCollection

class UiAxGraphics2DAnalysisCntrl(IUiAxGraphics2DAnalysisCntrl):
    """AGI Graphics Analysis Control"""
    def __init__(self, sourceObject=None):
        IUiAxGraphics2DAnalysisCntrl.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IUiAxGraphics2DAnalysisCntrl._private_init(self, intf)
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
agcls.AgTypeNameMap["UiAxGraphics2DAnalysisCntrl"] = UiAxGraphics2DAnalysisCntrl

class WinProjectionPosition(IWinProjectionPosition):
    """Projected window position result."""
    def __init__(self, sourceObject=None):
        IWinProjectionPosition.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IWinProjectionPosition._private_init(self, intf)
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
agcls.AgTypeNameMap["WinProjectionPosition"] = WinProjectionPosition

class DrawElemLine(IDrawElemLine):
    """Define a line in window coordinates."""
    def __init__(self, sourceObject=None):
        IDrawElemLine.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        IDrawElemLine._private_init(self, intf)
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
agcls.AgTypeNameMap["DrawElemLine"] = DrawElemLine

class STKXSSLCertificateErrorEventArgs(ISTKXSSLCertificateErrorEventArgs):
    """Provide information about an SSL certificate that is expired or invalid."""
    def __init__(self, sourceObject=None):
        ISTKXSSLCertificateErrorEventArgs.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ISTKXSSLCertificateErrorEventArgs._private_init(self, intf)
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
agcls.AgTypeNameMap["STKXSSLCertificateErrorEventArgs"] = STKXSSLCertificateErrorEventArgs

class STKXConControlQuitReceivedEventArgs(ISTKXConControlQuitReceivedEventArgs):
    """Arguments for the OnConControlQuitReceived event."""
    def __init__(self, sourceObject=None):
        ISTKXConControlQuitReceivedEventArgs.__init__(self, sourceObject)
    def _private_init(self, intf:interface_proxy):
        self.__dict__["_intf"] = intf
        ISTKXConControlQuitReceivedEventArgs._private_init(self, intf)
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
agcls.AgTypeNameMap["STKXConControlQuitReceivedEventArgs"] = STKXConControlQuitReceivedEventArgs


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
