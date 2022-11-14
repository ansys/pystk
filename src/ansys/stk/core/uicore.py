################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["AgEArrangeStyle", "AgEDockStyle", "AgEFloatState", "AgEWindowService", "AgEWindowState", "AgUiToolbar", "AgUiToolbarCollection", 
"AgUiWindow", "AgUiWindowGlobeObject", "AgUiWindowMapObject", "AgUiWindowsCollection", "IAgUiToolbar", "IAgUiToolbarCollection", 
"IAgUiWindow", "IAgUiWindowGlobeObject", "IAgUiWindowMapObject", "IAgUiWindowsCollection"]

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



def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class AgEWindowService(IntEnum):
    """Well-known types of services."""
    # A 2D window.
    eWindowService2DWindow = 1
    # A 3D window.
    eWindowService3DWindow = 2

agcls.AgTypeNameMap["AgEWindowService"] = AgEWindowService

class AgEWindowState(IntEnum):
    """Window states."""
    # Window is maximized.
    eWindowStateMaximized = 1
    # Window is minimized.
    eWindowStateMinimized = 2
    # Normal window state.
    eWindowStateNormal = 3

agcls.AgTypeNameMap["AgEWindowState"] = AgEWindowState

class AgEArrangeStyle(IntEnum):
    """Window layout styles."""
    # Child windows are cascaded within the main window.
    eArrangeStyleCascade = 1
    # Child windows are tiled horizontally within the main window.
    eArrangeStyleTiledHorizontal = 2
    # Child windows are tiled vertically within the main window.
    eArrangeStyleTiledVertical = 3

agcls.AgTypeNameMap["AgEArrangeStyle"] = AgEArrangeStyle

class AgEDockStyle(IntEnum):
    """Window docking styles."""
    # Child window is integrated into the main window.
    eDockStyleIntegrated = 1
    # Child window is docked to the left side of the within the main window.
    eDockStyleDockedLeft = 2
    # Child window is docked to the right side of the main window.
    eDockStyleDockedRight = 3
    # Child window is docked to the top of the main window.
    eDockStyleDockedTop = 4
    # Child window is docked to the bottom of the main window.
    eDockStyleDockedBottom = 5
    # Child window is not docked or integrated.
    eDockStyleFloating = 6

agcls.AgTypeNameMap["AgEDockStyle"] = AgEDockStyle

class AgEFloatState(IntEnum):
    """Floating state."""
    # The UI element is floated.
    eFloatStateFloated = 1
    # The UI element is docked.
    eFloatStateDocked = 2

agcls.AgTypeNameMap["AgEFloatState"] = AgEFloatState


class IAgUiToolbar(object):
    """Provides methods and properties to control a toolbar."""
    _uuid = "{69C72C16-36F2-42d4-A183-6879BB5B8070}"
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetID"] = _raise_uninitialized_error
        self.__dict__["_GetCaption"] = _raise_uninitialized_error
        self.__dict__["_GetVisible"] = _raise_uninitialized_error
        self.__dict__["_SetVisible"] = _raise_uninitialized_error
        self.__dict__["_GetFloatState"] = _raise_uninitialized_error
        self.__dict__["_SetFloatState"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiToolbar._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiToolbar from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiToolbar = agcom.GUID(IAgUiToolbar._uuid)
        vtable_offset_local = IAgUiToolbar._vtable_offset - 1
        self.__dict__["_GetID"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbar, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_GetCaption"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbar, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_GetVisible"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbar, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetVisible"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbar, vtable_offset_local+4, agcom.VARIANT_BOOL)
        self.__dict__["_GetFloatState"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbar, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_SetFloatState"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbar, vtable_offset_local+6, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiToolbar.__dict__ and type(IAgUiToolbar.__dict__[attrname]) == property:
            return IAgUiToolbar.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiToolbar.")
    
    @property
    def ID(self) -> int:
        """The identity."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetID"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Caption(self) -> str:
        """The caption."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCaption"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Visible(self) -> bool:
        """The visibility."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetVisible"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Visible.setter
    def Visible(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetVisible"](arg_newVal.COM_val))

    @property
    def FloatState(self) -> "AgEFloatState":
        """The float state."""
        with agmarshall.AgEnum_arg(AgEFloatState) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetFloatState"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @FloatState.setter
    def FloatState(self, newVal:"AgEFloatState") -> None:
        with agmarshall.AgEnum_arg(AgEFloatState, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetFloatState"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{69C72C16-36F2-42d4-A183-6879BB5B8070}", IAgUiToolbar)
agcls.AgTypeNameMap["IAgUiToolbar"] = IAgUiToolbar

class IAgUiToolbarCollection(object):
    """Provides methods and properties to obtain a window's toolbars."""
    _uuid = "{62AA135B-4F2F-45de-94A6-31BB0984AD28}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_GetToolbarByID"] = _raise_uninitialized_error
        self.__dict__["_GetItemByIndex"] = _raise_uninitialized_error
        self.__dict__["_GetItemByName"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiToolbarCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiToolbarCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiToolbarCollection = agcom.GUID(IAgUiToolbarCollection._uuid)
        vtable_offset_local = IAgUiToolbarCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbarCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbarCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbarCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_GetToolbarByID"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbarCollection, vtable_offset_local+4, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_GetItemByIndex"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbarCollection, vtable_offset_local+5, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_GetItemByName"] = IAGFUNCTYPE(pUnk, IID_IAgUiToolbarCollection, vtable_offset_local+6, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiToolbarCollection.__dict__ and type(IAgUiToolbarCollection.__dict__[attrname]) == property:
            return IAgUiToolbarCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiToolbarCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgUiToolbar":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, indexOrCaption:typing.Any) -> "IAgUiToolbar":
        """Retrieves a toolbar object."""
        with agmarshall.VARIANT_arg(indexOrCaption) as arg_indexOrCaption, \
             agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_indexOrCaption.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Count(self) -> int:
        """Returns a total number of toolbars in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates the toolbars in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def GetToolbarByID(self, id:int) -> "IAgUiToolbar":
        """Returns a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object."""
        with agmarshall.LONG_arg(id) as arg_id, \
             agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetToolbarByID"](arg_id.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def GetItemByIndex(self, index:int) -> "IAgUiToolbar":
        """Retrieves a toolbar object based on the index in the collection."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetItemByIndex"](arg_index.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def GetItemByName(self, name:str) -> "IAgUiToolbar":
        """Retrieves a toolbar object based on the name of the Toolbar in the collection."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetItemByName"](arg_name.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{62AA135B-4F2F-45de-94A6-31BB0984AD28}", IAgUiToolbarCollection)
agcls.AgTypeNameMap["IAgUiToolbarCollection"] = IAgUiToolbarCollection

class IAgUiWindow(object):
    """Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window."""
    _uuid = "{05F59555-F74C-48b2-AAB4-1E6C58D7AEB7}"
    _num_methods = 24
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetCaption"] = _raise_uninitialized_error
        self.__dict__["_SetCaption"] = _raise_uninitialized_error
        self.__dict__["_Activate"] = _raise_uninitialized_error
        self.__dict__["_GetWindowState"] = _raise_uninitialized_error
        self.__dict__["_SetWindowState"] = _raise_uninitialized_error
        self.__dict__["_Close"] = _raise_uninitialized_error
        self.__dict__["_GetHeight"] = _raise_uninitialized_error
        self.__dict__["_SetHeight"] = _raise_uninitialized_error
        self.__dict__["_GetWidth"] = _raise_uninitialized_error
        self.__dict__["_SetWidth"] = _raise_uninitialized_error
        self.__dict__["_GetLeft"] = _raise_uninitialized_error
        self.__dict__["_SetLeft"] = _raise_uninitialized_error
        self.__dict__["_GetTop"] = _raise_uninitialized_error
        self.__dict__["_SetTop"] = _raise_uninitialized_error
        self.__dict__["_GetDockStyle"] = _raise_uninitialized_error
        self.__dict__["_SetDockStyle"] = _raise_uninitialized_error
        self.__dict__["_GetNoWBClose"] = _raise_uninitialized_error
        self.__dict__["_SetNoWBClose"] = _raise_uninitialized_error
        self.__dict__["_GetUnPinned"] = _raise_uninitialized_error
        self.__dict__["_SetUnPinned"] = _raise_uninitialized_error
        self.__dict__["_GetSupportsPinning"] = _raise_uninitialized_error
        self.__dict__["_GetToolbars"] = _raise_uninitialized_error
        self.__dict__["_GetServiceByName"] = _raise_uninitialized_error
        self.__dict__["_GetServiceByType"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiWindow._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiWindow from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiWindow = agcom.GUID(IAgUiWindow._uuid)
        vtable_offset_local = IAgUiWindow._vtable_offset - 1
        self.__dict__["_GetCaption"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_SetCaption"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_Activate"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+3, )
        self.__dict__["_GetWindowState"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+4, POINTER(agcom.LONG))
        self.__dict__["_SetWindowState"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+5, agcom.LONG)
        self.__dict__["_Close"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+6, )
        self.__dict__["_GetHeight"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+7, POINTER(agcom.LONG))
        self.__dict__["_SetHeight"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+8, agcom.LONG)
        self.__dict__["_GetWidth"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+9, POINTER(agcom.LONG))
        self.__dict__["_SetWidth"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+10, agcom.LONG)
        self.__dict__["_GetLeft"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+11, POINTER(agcom.LONG))
        self.__dict__["_SetLeft"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+12, agcom.LONG)
        self.__dict__["_GetTop"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+13, POINTER(agcom.LONG))
        self.__dict__["_SetTop"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+14, agcom.LONG)
        self.__dict__["_GetDockStyle"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+15, POINTER(agcom.LONG))
        self.__dict__["_SetDockStyle"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+16, agcom.LONG)
        self.__dict__["_GetNoWBClose"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+17, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetNoWBClose"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+18, agcom.VARIANT_BOOL)
        self.__dict__["_GetUnPinned"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+19, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_SetUnPinned"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+20, agcom.VARIANT_BOOL)
        self.__dict__["_GetSupportsPinning"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+21, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_GetToolbars"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+22, POINTER(agcom.PVOID))
        self.__dict__["_GetServiceByName"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+23, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_GetServiceByType"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindow, vtable_offset_local+24, agcom.LONG, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiWindow.__dict__ and type(IAgUiWindow.__dict__[attrname]) == property:
            return IAgUiWindow.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiWindow.")
    
    @property
    def Caption(self) -> str:
        """The window caption. Can only be set within UI plugins for the non unique windows they own."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCaption"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Caption.setter
    def Caption(self, caption:str) -> None:
        """The window caption. Can only be set within UI plugins for the non unique windows they own."""
        with agmarshall.BSTR_arg(caption) as arg_caption:
            agcls.evaluate_hresult(self.__dict__["_SetCaption"](arg_caption.COM_val))

    def Activate(self) -> None:
        """Activates the window."""
        agcls.evaluate_hresult(self.__dict__["_Activate"]())

    @property
    def WindowState(self) -> "AgEWindowState":
        """The window state."""
        with agmarshall.AgEnum_arg(AgEWindowState) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWindowState"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @WindowState.setter
    def WindowState(self, newVal:"AgEWindowState") -> None:
        with agmarshall.AgEnum_arg(AgEWindowState, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetWindowState"](arg_newVal.COM_val))

    def Close(self) -> None:
        """Closes the window."""
        agcls.evaluate_hresult(self.__dict__["_Close"]())

    @property
    def Height(self) -> int:
        """The window height."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetHeight"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Height.setter
    def Height(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetHeight"](arg_newVal.COM_val))

    @property
    def Width(self) -> int:
        """The window width."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetWidth"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Width.setter
    def Width(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetWidth"](arg_newVal.COM_val))

    @property
    def Left(self) -> int:
        """The window horizontal position."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetLeft"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Left.setter
    def Left(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetLeft"](arg_newVal.COM_val))

    @property
    def Top(self) -> int:
        """The window vertical position"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetTop"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @Top.setter
    def Top(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetTop"](arg_newVal.COM_val))

    @property
    def DockStyle(self) -> "AgEDockStyle":
        """The window docking style."""
        with agmarshall.AgEnum_arg(AgEDockStyle) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetDockStyle"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @DockStyle.setter
    def DockStyle(self, newVal:"AgEDockStyle") -> None:
        with agmarshall.AgEnum_arg(AgEDockStyle, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetDockStyle"](arg_newVal.COM_val))

    @property
    def NoWBClose(self) -> bool:
        """Whether to close the window when the application workbook is loaded/closed."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetNoWBClose"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @NoWBClose.setter
    def NoWBClose(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetNoWBClose"](arg_newVal.COM_val))

    @property
    def UnPinned(self) -> bool:
        """The window's pinned state."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetUnPinned"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @UnPinned.setter
    def UnPinned(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_SetUnPinned"](arg_newVal.COM_val))

    @property
    def SupportsPinning(self) -> bool:
        """Returns whether the window supports pinning."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetSupportsPinning"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Toolbars(self) -> "IAgUiToolbarCollection":
        """Returns the window's toolbar collection."""
        with agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetToolbars"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def GetServiceByName(self, name:str) -> typing.Any:
        """Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetServiceByName"](arg_name.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def GetServiceByType(self, serviceType:"AgEWindowService") -> typing.Any:
        """Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type."""
        with agmarshall.AgEnum_arg(AgEWindowService, serviceType) as arg_serviceType, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetServiceByType"](arg_serviceType.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{05F59555-F74C-48b2-AAB4-1E6C58D7AEB7}", IAgUiWindow)
agcls.AgTypeNameMap["IAgUiWindow"] = IAgUiWindow

class IAgUiWindowsCollection(object):
    """Provides methods and properties to manage the application's windows."""
    _uuid = "{4DD6FB87-C329-41a5-A359-8A9C03569635}"
    _num_methods = 7
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_Item"] = _raise_uninitialized_error
        self.__dict__["_GetCount"] = _raise_uninitialized_error
        self.__dict__["_Arrange"] = _raise_uninitialized_error
        self.__dict__["_Add"] = _raise_uninitialized_error
        self.__dict__["_Get_NewEnum"] = _raise_uninitialized_error
        self.__dict__["_GetItemByIndex"] = _raise_uninitialized_error
        self.__dict__["_GetItemByName"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiWindowsCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiWindowsCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiWindowsCollection = agcom.GUID(IAgUiWindowsCollection._uuid)
        vtable_offset_local = IAgUiWindowsCollection._vtable_offset - 1
        self.__dict__["_Item"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowsCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_GetCount"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowsCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_Arrange"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowsCollection, vtable_offset_local+3, agcom.LONG)
        self.__dict__["_Add"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowsCollection, vtable_offset_local+4, agcom.BSTR, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_Get_NewEnum"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowsCollection, vtable_offset_local+5, POINTER(agcom.PVOID))
        self.__dict__["_GetItemByIndex"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowsCollection, vtable_offset_local+6, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_GetItemByName"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowsCollection, vtable_offset_local+7, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiWindowsCollection.__dict__ and type(IAgUiWindowsCollection.__dict__[attrname]) == property:
            return IAgUiWindowsCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiWindowsCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IAgUiWindow":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def Item(self, indexOrCaption:typing.Any) -> "IAgUiWindow":
        """Retrieves a window object."""
        with agmarshall.VARIANT_arg(indexOrCaption) as arg_indexOrCaption, \
             agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_Item"](arg_indexOrCaption.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def Count(self) -> int:
        """Returns a total number of window objects in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_GetCount"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def Arrange(self, arrangeStyle:"AgEArrangeStyle") -> None:
        """Arranges the application windows using the specified style."""
        with agmarshall.AgEnum_arg(AgEArrangeStyle, arrangeStyle) as arg_arrangeStyle:
            agcls.evaluate_hresult(self.__dict__["_Arrange"](arg_arrangeStyle.COM_val))

    def Add(self, pluginID:str, initData:typing.Any) -> "IAgUiWindow":
        """Creates a new window. The bstrPluginID is a COM ProgID associated with an STK plugin."""
        with agmarshall.BSTR_arg(pluginID) as arg_pluginID, \
             agmarshall.VARIANT_arg(initData) as arg_initData, \
             agmarshall.AgInterface_out_arg() as arg_pNewWin:
            agcls.evaluate_hresult(self.__dict__["_Add"](arg_pluginID.COM_val, arg_initData.COM_val, byref(arg_pNewWin.COM_val)))
            return arg_pNewWin.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates the windows in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_Get_NewEnum"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def GetItemByIndex(self, index:int) -> "IAgUiWindow":
        """Retrieves a window object by index in collection."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetItemByIndex"](arg_index.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def GetItemByName(self, name:str) -> "IAgUiWindow":
        """Retrieves a window object by name of window object."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_GetItemByName"](arg_name.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    __getitem__ = Item



agcls.AgClassCatalog.add_catalog_entry("{4DD6FB87-C329-41a5-A359-8A9C03569635}", IAgUiWindowsCollection)
agcls.AgTypeNameMap["IAgUiWindowsCollection"] = IAgUiWindowsCollection

class IAgUiWindowMapObject(object):
    """Represents a 2D (Map) window. Provides methods and properties to access the 2D window properties."""
    _uuid = "{A94C0929-7448-4e9e-BEB8-8F7A8F252D0D}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetMapID"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiWindowMapObject._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiWindowMapObject from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiWindowMapObject = agcom.GUID(IAgUiWindowMapObject._uuid)
        vtable_offset_local = IAgUiWindowMapObject._vtable_offset - 1
        self.__dict__["_GetMapID"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowMapObject, vtable_offset_local+1, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiWindowMapObject.__dict__ and type(IAgUiWindowMapObject.__dict__[attrname]) == property:
            return IAgUiWindowMapObject.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiWindowMapObject.")
    
    @property
    def MapID(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 2D map."""
        with agmarshall.LONG_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetMapID"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{A94C0929-7448-4e9e-BEB8-8F7A8F252D0D}", IAgUiWindowMapObject)
agcls.AgTypeNameMap["IAgUiWindowMapObject"] = IAgUiWindowMapObject

class IAgUiWindowGlobeObject(object):
    """Represents a 3D (Globe) window. Provides methods and properties to access the 3D window properties."""
    _uuid = "{B958EDBD-0569-4596-A253-BD90328844D0}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_GetSceneID"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IAgUiWindowGlobeObject._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IAgUiWindowGlobeObject from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IAgUiWindowGlobeObject = agcom.GUID(IAgUiWindowGlobeObject._uuid)
        vtable_offset_local = IAgUiWindowGlobeObject._vtable_offset - 1
        self.__dict__["_GetSceneID"] = IAGFUNCTYPE(pUnk, IID_IAgUiWindowGlobeObject, vtable_offset_local+1, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IAgUiWindowGlobeObject.__dict__ and type(IAgUiWindowGlobeObject.__dict__[attrname]) == property:
            return IAgUiWindowGlobeObject.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IAgUiWindowGlobeObject.")
    
    @property
    def SceneID(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 3D globe."""
        with agmarshall.LONG_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_GetSceneID"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{B958EDBD-0569-4596-A253-BD90328844D0}", IAgUiWindowGlobeObject)
agcls.AgTypeNameMap["IAgUiWindowGlobeObject"] = IAgUiWindowGlobeObject



class AgUiWindowsCollection(IAgUiWindowsCollection):
    """Provides methods and properties to manage the windows."""
    def __init__(self, sourceObject=None):
        IAgUiWindowsCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiWindowsCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiWindowsCollection._get_property(self, attrname) is not None: found_prop = IAgUiWindowsCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiWindowsCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{82F7DB8A-A761-4C3E-95DF-37300A3738CB}", AgUiWindowsCollection)


class AgUiWindow(IAgUiWindow):
    """Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window."""
    def __init__(self, sourceObject=None):
        IAgUiWindow.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiWindow._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiWindow._get_property(self, attrname) is not None: found_prop = IAgUiWindow._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiWindow.")
        
agcls.AgClassCatalog.add_catalog_entry("{BD72ECC3-A4A2-42FB-95AC-AE25633BB9F6}", AgUiWindow)


class AgUiToolbar(IAgUiToolbar):
    """Represents a toolbar abstraction. Provides methods and properties to manipulate the position and the state of the toolbar."""
    def __init__(self, sourceObject=None):
        IAgUiToolbar.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiToolbar._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiToolbar._get_property(self, attrname) is not None: found_prop = IAgUiToolbar._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiToolbar.")
        
agcls.AgClassCatalog.add_catalog_entry("{C20AB584-ABCC-4BF3-96D4-D2A4AA880FBB}", AgUiToolbar)


class AgUiToolbarCollection(IAgUiToolbarCollection):
    """Provides methods and properties to manage the toolbars."""
    def __init__(self, sourceObject=None):
        IAgUiToolbarCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiToolbarCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiToolbarCollection._get_property(self, attrname) is not None: found_prop = IAgUiToolbarCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiToolbarCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{28F000E7-D13E-485E-8484-0BCB359BBC55}", AgUiToolbarCollection)


class AgUiWindowMapObject(IAgUiWindowMapObject):
    """Provides methods and properties to manipulate the 2D map."""
    def __init__(self, sourceObject=None):
        IAgUiWindowMapObject.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiWindowMapObject._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiWindowMapObject._get_property(self, attrname) is not None: found_prop = IAgUiWindowMapObject._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiWindowMapObject.")
        
agcls.AgClassCatalog.add_catalog_entry("{D20C704C-0763-4CC9-9485-A2EA23C84E6B}", AgUiWindowMapObject)


class AgUiWindowGlobeObject(IAgUiWindowGlobeObject):
    """Provides methods and properties to manipulate the 3D globe."""
    def __init__(self, sourceObject=None):
        IAgUiWindowGlobeObject.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IAgUiWindowGlobeObject._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IAgUiWindowGlobeObject._get_property(self, attrname) is not None: found_prop = IAgUiWindowGlobeObject._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in AgUiWindowGlobeObject.")
        
agcls.AgClassCatalog.add_catalog_entry("{4F69FA5F-30E8-4A07-9D8C-1AD163A3DE0D}", AgUiWindowGlobeObject)



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
