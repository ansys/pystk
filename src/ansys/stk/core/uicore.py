################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################ 

__all__ = ["AgEArrangeStyle", "AgEDockStyle", "AgEFloatState", "AgEWindowService", "AgEWindowState", "IUiToolbar", "IUiToolbarCollection", 
"IUiWindow", "IUiWindowGlobeObject", "IUiWindowMapObject", "IUiWindowsCollection", "UiToolbar", "UiToolbarCollection", "UiWindow", 
"UiWindowGlobeObject", "UiWindowMapObject", "UiWindowsCollection"]

import typing

from ctypes   import byref, POINTER
from enum     import IntEnum

try:
    from numpy import ndarray # noqa
except ModuleNotFoundError:
    pass
    
try:
    from pandas import DataFrame # noqa
except ModuleNotFoundError:
    pass

from .internal  import comutil          as agcom
from .internal  import coclassutil      as agcls
from .internal  import marshall         as agmarshall
from .internal.comutil     import IUnknown, IDispatch, IAGFUNCTYPE, IEnumVARIANT
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

AgEWindowService.eWindowService2DWindow.__doc__ = "A 2D window."
AgEWindowService.eWindowService3DWindow.__doc__ = "A 3D window."

agcls.AgTypeNameMap["AgEWindowService"] = AgEWindowService

class AgEWindowState(IntEnum):
    """Window states."""
    # Window is maximized.
    eWindowStateMaximized = 1
    # Window is minimized.
    eWindowStateMinimized = 2
    # Normal window state.
    eWindowStateNormal = 3

AgEWindowState.eWindowStateMaximized.__doc__ = "Window is maximized."
AgEWindowState.eWindowStateMinimized.__doc__ = "Window is minimized."
AgEWindowState.eWindowStateNormal.__doc__ = "Normal window state."

agcls.AgTypeNameMap["AgEWindowState"] = AgEWindowState

class AgEArrangeStyle(IntEnum):
    """Window layout styles."""
    # Child windows are cascaded within the main window.
    eArrangeStyleCascade = 1
    # Child windows are tiled horizontally within the main window.
    eArrangeStyleTiledHorizontal = 2
    # Child windows are tiled vertically within the main window.
    eArrangeStyleTiledVertical = 3

AgEArrangeStyle.eArrangeStyleCascade.__doc__ = "Child windows are cascaded within the main window."
AgEArrangeStyle.eArrangeStyleTiledHorizontal.__doc__ = "Child windows are tiled horizontally within the main window."
AgEArrangeStyle.eArrangeStyleTiledVertical.__doc__ = "Child windows are tiled vertically within the main window."

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

AgEDockStyle.eDockStyleIntegrated.__doc__ = "Child window is integrated into the main window."
AgEDockStyle.eDockStyleDockedLeft.__doc__ = "Child window is docked to the left side of the within the main window."
AgEDockStyle.eDockStyleDockedRight.__doc__ = "Child window is docked to the right side of the main window."
AgEDockStyle.eDockStyleDockedTop.__doc__ = "Child window is docked to the top of the main window."
AgEDockStyle.eDockStyleDockedBottom.__doc__ = "Child window is docked to the bottom of the main window."
AgEDockStyle.eDockStyleFloating.__doc__ = "Child window is not docked or integrated."

agcls.AgTypeNameMap["AgEDockStyle"] = AgEDockStyle

class AgEFloatState(IntEnum):
    """Floating state."""
    # The UI element is floated.
    eFloatStateFloated = 1
    # The UI element is docked.
    eFloatStateDocked = 2

AgEFloatState.eFloatStateFloated.__doc__ = "The UI element is floated."
AgEFloatState.eFloatStateDocked.__doc__ = "The UI element is docked."

agcls.AgTypeNameMap["AgEFloatState"] = AgEFloatState


class IUiToolbar(object):
    """Provides methods and properties to control a toolbar."""
    _uuid = "{69C72C16-36F2-42d4-A183-6879BB5B8070}"
    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_id"] = _raise_uninitialized_error
        self.__dict__["_get_caption"] = _raise_uninitialized_error
        self.__dict__["_get_visible"] = _raise_uninitialized_error
        self.__dict__["_set_visible"] = _raise_uninitialized_error
        self.__dict__["_get_float_state"] = _raise_uninitialized_error
        self.__dict__["_set_float_state"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiToolbar._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiToolbar from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiToolbar = agcom.GUID(IUiToolbar._uuid)
        vtable_offset_local = IUiToolbar._vtable_offset - 1
        self.__dict__["_get_id"] = IAGFUNCTYPE(pUnk, IID_IUiToolbar, vtable_offset_local+1, POINTER(agcom.LONG))
        self.__dict__["_get_caption"] = IAGFUNCTYPE(pUnk, IID_IUiToolbar, vtable_offset_local+2, POINTER(agcom.BSTR))
        self.__dict__["_get_visible"] = IAGFUNCTYPE(pUnk, IID_IUiToolbar, vtable_offset_local+3, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_visible"] = IAGFUNCTYPE(pUnk, IID_IUiToolbar, vtable_offset_local+4, agcom.VARIANT_BOOL)
        self.__dict__["_get_float_state"] = IAGFUNCTYPE(pUnk, IID_IUiToolbar, vtable_offset_local+5, POINTER(agcom.LONG))
        self.__dict__["_set_float_state"] = IAGFUNCTYPE(pUnk, IID_IUiToolbar, vtable_offset_local+6, agcom.LONG)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiToolbar.__dict__ and type(IUiToolbar.__dict__[attrname]) == property:
            return IUiToolbar.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiToolbar.")
    
    @property
    def id(self) -> int:
        """The identity."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_id"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def caption(self) -> str:
        """The caption."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_caption"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def visible(self) -> bool:
        """The visibility."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_visible"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @visible.setter
    def visible(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_visible"](arg_newVal.COM_val))

    @property
    def float_state(self) -> "AgEFloatState":
        """The float state."""
        with agmarshall.AgEnum_arg(AgEFloatState) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_float_state"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @float_state.setter
    def float_state(self, newVal:"AgEFloatState") -> None:
        with agmarshall.AgEnum_arg(AgEFloatState, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_float_state"](arg_newVal.COM_val))


agcls.AgClassCatalog.add_catalog_entry("{69C72C16-36F2-42d4-A183-6879BB5B8070}", IUiToolbar)
agcls.AgTypeNameMap["IUiToolbar"] = IUiToolbar

class IUiToolbarCollection(object):
    """Provides methods and properties to obtain a window's toolbars."""
    _uuid = "{62AA135B-4F2F-45de-94A6-31BB0984AD28}"
    _num_methods = 6
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_get_toolbar_by_id"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_index"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_name"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiToolbarCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiToolbarCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiToolbarCollection = agcom.GUID(IUiToolbarCollection._uuid)
        vtable_offset_local = IUiToolbarCollection._vtable_offset - 1
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IUiToolbarCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IUiToolbarCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IUiToolbarCollection, vtable_offset_local+3, POINTER(agcom.PVOID))
        self.__dict__["_get_toolbar_by_id"] = IAGFUNCTYPE(pUnk, IID_IUiToolbarCollection, vtable_offset_local+4, agcom.LONG, POINTER(agcom.PVOID))
        self.__dict__["_get_item_by_index"] = IAGFUNCTYPE(pUnk, IID_IUiToolbarCollection, vtable_offset_local+5, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_get_item_by_name"] = IAGFUNCTYPE(pUnk, IID_IUiToolbarCollection, vtable_offset_local+6, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiToolbarCollection.__dict__ and type(IUiToolbarCollection.__dict__[attrname]) == property:
            return IUiToolbarCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiToolbarCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IUiToolbar":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def item(self, indexOrCaption:typing.Any) -> "IUiToolbar":
        """Retrieves a toolbar object."""
        with agmarshall.VARIANT_arg(indexOrCaption) as arg_indexOrCaption, \
             agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_indexOrCaption.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def count(self) -> int:
        """Returns a total number of toolbars in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates the toolbars in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def get_toolbar_by_id(self, id:int) -> "IUiToolbar":
        """Returns a toolbar object with the specified toolbar identifier. The identifier is a unique number assigned to a toolbar object."""
        with agmarshall.LONG_arg(id) as arg_id, \
             agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_toolbar_by_id"](arg_id.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def get_item_by_index(self, index:int) -> "IUiToolbar":
        """Retrieves a toolbar object based on the index in the collection."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_index"](arg_index.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def get_item_by_name(self, name:str) -> "IUiToolbar":
        """Retrieves a toolbar object based on the name of the Toolbar in the collection."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_name"](arg_name.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{62AA135B-4F2F-45de-94A6-31BB0984AD28}", IUiToolbarCollection)
agcls.AgTypeNameMap["IUiToolbarCollection"] = IUiToolbarCollection

class IUiWindow(object):
    """Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window."""
    _uuid = "{05F59555-F74C-48b2-AAB4-1E6C58D7AEB7}"
    _num_methods = 24
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_caption"] = _raise_uninitialized_error
        self.__dict__["_set_caption"] = _raise_uninitialized_error
        self.__dict__["_activate"] = _raise_uninitialized_error
        self.__dict__["_get_window_state"] = _raise_uninitialized_error
        self.__dict__["_set_window_state"] = _raise_uninitialized_error
        self.__dict__["_close"] = _raise_uninitialized_error
        self.__dict__["_get_height"] = _raise_uninitialized_error
        self.__dict__["_set_height"] = _raise_uninitialized_error
        self.__dict__["_get_width"] = _raise_uninitialized_error
        self.__dict__["_set_width"] = _raise_uninitialized_error
        self.__dict__["_get_left"] = _raise_uninitialized_error
        self.__dict__["_set_left"] = _raise_uninitialized_error
        self.__dict__["_get_top"] = _raise_uninitialized_error
        self.__dict__["_set_top"] = _raise_uninitialized_error
        self.__dict__["_get_dock_style"] = _raise_uninitialized_error
        self.__dict__["_set_dock_style"] = _raise_uninitialized_error
        self.__dict__["_get_no_wb_close"] = _raise_uninitialized_error
        self.__dict__["_set_no_wb_close"] = _raise_uninitialized_error
        self.__dict__["_get_un_pinned"] = _raise_uninitialized_error
        self.__dict__["_set_un_pinned"] = _raise_uninitialized_error
        self.__dict__["_get_supports_pinning"] = _raise_uninitialized_error
        self.__dict__["_get_toolbars"] = _raise_uninitialized_error
        self.__dict__["_get_service_by_name"] = _raise_uninitialized_error
        self.__dict__["_get_service_by_type"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiWindow._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiWindow from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiWindow = agcom.GUID(IUiWindow._uuid)
        vtable_offset_local = IUiWindow._vtable_offset - 1
        self.__dict__["_get_caption"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+1, POINTER(agcom.BSTR))
        self.__dict__["_set_caption"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+2, agcom.BSTR)
        self.__dict__["_activate"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+3, )
        self.__dict__["_get_window_state"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+4, POINTER(agcom.LONG))
        self.__dict__["_set_window_state"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+5, agcom.LONG)
        self.__dict__["_close"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+6, )
        self.__dict__["_get_height"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+7, POINTER(agcom.LONG))
        self.__dict__["_set_height"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+8, agcom.LONG)
        self.__dict__["_get_width"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+9, POINTER(agcom.LONG))
        self.__dict__["_set_width"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+10, agcom.LONG)
        self.__dict__["_get_left"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+11, POINTER(agcom.LONG))
        self.__dict__["_set_left"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+12, agcom.LONG)
        self.__dict__["_get_top"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+13, POINTER(agcom.LONG))
        self.__dict__["_set_top"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+14, agcom.LONG)
        self.__dict__["_get_dock_style"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+15, POINTER(agcom.LONG))
        self.__dict__["_set_dock_style"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+16, agcom.LONG)
        self.__dict__["_get_no_wb_close"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+17, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_no_wb_close"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+18, agcom.VARIANT_BOOL)
        self.__dict__["_get_un_pinned"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+19, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_set_un_pinned"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+20, agcom.VARIANT_BOOL)
        self.__dict__["_get_supports_pinning"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+21, POINTER(agcom.VARIANT_BOOL))
        self.__dict__["_get_toolbars"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+22, POINTER(agcom.PVOID))
        self.__dict__["_get_service_by_name"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+23, agcom.BSTR, POINTER(agcom.PVOID))
        self.__dict__["_get_service_by_type"] = IAGFUNCTYPE(pUnk, IID_IUiWindow, vtable_offset_local+24, agcom.LONG, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiWindow.__dict__ and type(IUiWindow.__dict__[attrname]) == property:
            return IUiWindow.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiWindow.")
    
    @property
    def caption(self) -> str:
        """The window caption. Can only be set within UI plugins for the non unique windows they own."""
        with agmarshall.BSTR_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_caption"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @caption.setter
    def caption(self, caption:str) -> None:
        """The window caption. Can only be set within UI plugins for the non unique windows they own."""
        with agmarshall.BSTR_arg(caption) as arg_caption:
            agcls.evaluate_hresult(self.__dict__["_set_caption"](arg_caption.COM_val))

    def activate(self) -> None:
        """Activates the window."""
        agcls.evaluate_hresult(self.__dict__["_activate"]())

    @property
    def window_state(self) -> "AgEWindowState":
        """The window state."""
        with agmarshall.AgEnum_arg(AgEWindowState) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_window_state"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @window_state.setter
    def window_state(self, newVal:"AgEWindowState") -> None:
        with agmarshall.AgEnum_arg(AgEWindowState, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_window_state"](arg_newVal.COM_val))

    def close(self) -> None:
        """Closes the window."""
        agcls.evaluate_hresult(self.__dict__["_close"]())

    @property
    def height(self) -> int:
        """The window height."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_height"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @height.setter
    def height(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_height"](arg_newVal.COM_val))

    @property
    def width(self) -> int:
        """The window width."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_width"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @width.setter
    def width(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_width"](arg_newVal.COM_val))

    @property
    def left(self) -> int:
        """The window horizontal position."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_left"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @left.setter
    def left(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_left"](arg_newVal.COM_val))

    @property
    def top(self) -> int:
        """The window vertical position"""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_top"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @top.setter
    def top(self, newVal:int) -> None:
        with agmarshall.LONG_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_top"](arg_newVal.COM_val))

    @property
    def dock_style(self) -> "AgEDockStyle":
        """The window docking style."""
        with agmarshall.AgEnum_arg(AgEDockStyle) as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_dock_style"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @dock_style.setter
    def dock_style(self, newVal:"AgEDockStyle") -> None:
        with agmarshall.AgEnum_arg(AgEDockStyle, newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_dock_style"](arg_newVal.COM_val))

    @property
    def no_wb_close(self) -> bool:
        """Whether to close the window when the application workbook is loaded/closed."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_no_wb_close"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @no_wb_close.setter
    def no_wb_close(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_no_wb_close"](arg_newVal.COM_val))

    @property
    def un_pinned(self) -> bool:
        """The window's pinned state."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_un_pinned"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @un_pinned.setter
    def un_pinned(self, newVal:bool) -> None:
        with agmarshall.VARIANT_BOOL_arg(newVal) as arg_newVal:
            agcls.evaluate_hresult(self.__dict__["_set_un_pinned"](arg_newVal.COM_val))

    @property
    def supports_pinning(self) -> bool:
        """Returns whether the window supports pinning."""
        with agmarshall.VARIANT_BOOL_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_supports_pinning"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def toolbars(self) -> "IUiToolbarCollection":
        """Returns the window's toolbar collection."""
        with agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_toolbars"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def get_service_by_name(self, name:str) -> typing.Any:
        """Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified symbolic name."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_service_by_name"](arg_name.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val

    def get_service_by_type(self, serviceType:"AgEWindowService") -> typing.Any:
        """Returns a service object that can be accessed at runtime. The method returns null if no service object is associated with the specified service type."""
        with agmarshall.AgEnum_arg(AgEWindowService, serviceType) as arg_serviceType, \
             agmarshall.AgInterface_out_arg() as arg_ppRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_service_by_type"](arg_serviceType.COM_val, byref(arg_ppRetVal.COM_val)))
            return arg_ppRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{05F59555-F74C-48b2-AAB4-1E6C58D7AEB7}", IUiWindow)
agcls.AgTypeNameMap["IUiWindow"] = IUiWindow

class IUiWindowsCollection(object):
    """Provides methods and properties to manage the application's windows."""
    _uuid = "{4DD6FB87-C329-41a5-A359-8A9C03569635}"
    _num_methods = 7
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_item"] = _raise_uninitialized_error
        self.__dict__["_get_count"] = _raise_uninitialized_error
        self.__dict__["_arrange"] = _raise_uninitialized_error
        self.__dict__["_add"] = _raise_uninitialized_error
        self.__dict__["_get__NewEnum"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_index"] = _raise_uninitialized_error
        self.__dict__["_get_item_by_name"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiWindowsCollection._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiWindowsCollection from source object.")
        self.__dict__["enumerator"] = None
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiWindowsCollection = agcom.GUID(IUiWindowsCollection._uuid)
        vtable_offset_local = IUiWindowsCollection._vtable_offset - 1
        self.__dict__["_item"] = IAGFUNCTYPE(pUnk, IID_IUiWindowsCollection, vtable_offset_local+1, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_get_count"] = IAGFUNCTYPE(pUnk, IID_IUiWindowsCollection, vtable_offset_local+2, POINTER(agcom.LONG))
        self.__dict__["_arrange"] = IAGFUNCTYPE(pUnk, IID_IUiWindowsCollection, vtable_offset_local+3, agcom.LONG)
        self.__dict__["_add"] = IAGFUNCTYPE(pUnk, IID_IUiWindowsCollection, vtable_offset_local+4, agcom.BSTR, agcom.VARIANT, POINTER(agcom.PVOID))
        self.__dict__["_get__NewEnum"] = IAGFUNCTYPE(pUnk, IID_IUiWindowsCollection, vtable_offset_local+5, POINTER(agcom.PVOID))
        self.__dict__["_get_item_by_index"] = IAGFUNCTYPE(pUnk, IID_IUiWindowsCollection, vtable_offset_local+6, agcom.INT, POINTER(agcom.PVOID))
        self.__dict__["_get_item_by_name"] = IAGFUNCTYPE(pUnk, IID_IUiWindowsCollection, vtable_offset_local+7, agcom.BSTR, POINTER(agcom.PVOID))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiWindowsCollection.__dict__ and type(IUiWindowsCollection.__dict__[attrname]) == property:
            return IUiWindowsCollection.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiWindowsCollection.")
    def __iter__(self):
        self.__dict__["enumerator"] = self._NewEnum
        self.__dict__["enumerator"].Reset()
        return self
    def __next__(self) -> "IUiWindow":
        if self.__dict__["enumerator"] is None:
            raise StopIteration
        nextval = self.__dict__["enumerator"].Next()
        if nextval is None:
            raise StopIteration
        return agmarshall.python_val_from_VARIANT(nextval)
    
    def item(self, indexOrCaption:typing.Any) -> "IUiWindow":
        """Retrieves a window object."""
        with agmarshall.VARIANT_arg(indexOrCaption) as arg_indexOrCaption, \
             agmarshall.AgInterface_out_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_item"](arg_indexOrCaption.COM_val, byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    @property
    def count(self) -> int:
        """Returns a total number of window objects in the collection."""
        with agmarshall.LONG_arg() as arg_pVal:
            agcls.evaluate_hresult(self.__dict__["_get_count"](byref(arg_pVal.COM_val)))
            return arg_pVal.python_val

    def arrange(self, arrangeStyle:"AgEArrangeStyle") -> None:
        """Arranges the application windows using the specified style."""
        with agmarshall.AgEnum_arg(AgEArrangeStyle, arrangeStyle) as arg_arrangeStyle:
            agcls.evaluate_hresult(self.__dict__["_arrange"](arg_arrangeStyle.COM_val))

    def add(self, pluginID:str, initData:typing.Any) -> "IUiWindow":
        """Creates a new window. The bstrPluginID is a COM ProgID associated with an STK plugin."""
        with agmarshall.BSTR_arg(pluginID) as arg_pluginID, \
             agmarshall.VARIANT_arg(initData) as arg_initData, \
             agmarshall.AgInterface_out_arg() as arg_pNewWin:
            agcls.evaluate_hresult(self.__dict__["_add"](arg_pluginID.COM_val, arg_initData.COM_val, byref(arg_pNewWin.COM_val)))
            return arg_pNewWin.python_val

    @property
    def _NewEnum(self) -> IEnumVARIANT:
        """Enumerates the windows in the collection."""
        with agmarshall.IEnumVARIANT_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get__NewEnum"](byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def get_item_by_index(self, index:int) -> "IUiWindow":
        """Retrieves a window object by index in collection."""
        with agmarshall.INT_arg(index) as arg_index, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_index"](arg_index.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    def get_item_by_name(self, name:str) -> "IUiWindow":
        """Retrieves a window object by name of window object."""
        with agmarshall.BSTR_arg(name) as arg_name, \
             agmarshall.AgInterface_out_arg() as arg_ppVal:
            agcls.evaluate_hresult(self.__dict__["_get_item_by_name"](arg_name.COM_val, byref(arg_ppVal.COM_val)))
            return arg_ppVal.python_val

    __getitem__ = item



agcls.AgClassCatalog.add_catalog_entry("{4DD6FB87-C329-41a5-A359-8A9C03569635}", IUiWindowsCollection)
agcls.AgTypeNameMap["IUiWindowsCollection"] = IUiWindowsCollection

class IUiWindowMapObject(object):
    """Represents a 2D (Map) window. Provides methods and properties to access the 2D window properties."""
    _uuid = "{A94C0929-7448-4e9e-BEB8-8F7A8F252D0D}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_map_id"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiWindowMapObject._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiWindowMapObject from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiWindowMapObject = agcom.GUID(IUiWindowMapObject._uuid)
        vtable_offset_local = IUiWindowMapObject._vtable_offset - 1
        self.__dict__["_get_map_id"] = IAGFUNCTYPE(pUnk, IID_IUiWindowMapObject, vtable_offset_local+1, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiWindowMapObject.__dict__ and type(IUiWindowMapObject.__dict__[attrname]) == property:
            return IUiWindowMapObject.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiWindowMapObject.")
    
    @property
    def map_id(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 2D map."""
        with agmarshall.LONG_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_map_id"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{A94C0929-7448-4e9e-BEB8-8F7A8F252D0D}", IUiWindowMapObject)
agcls.AgTypeNameMap["IUiWindowMapObject"] = IUiWindowMapObject

class IUiWindowGlobeObject(object):
    """Represents a 3D (Globe) window. Provides methods and properties to access the 3D window properties."""
    _uuid = "{B958EDBD-0569-4596-A253-BD90328844D0}"
    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    def __init__(self, sourceObject=None):
        self.__dict__["_pUnk"] = None
        self.__dict__["_get_scene_id"] = _raise_uninitialized_error
        if sourceObject is not None and sourceObject.__dict__["_pUnk"] is not None:
            pUnk = sourceObject.__dict__["_pUnk"].QueryInterface(agcom.GUID(IUiWindowGlobeObject._uuid))
            if pUnk is not None:
                self._private_init(pUnk)
                del(pUnk)
            else:
                raise STKInvalidCastError("Failed to create IUiWindowGlobeObject from source object.")
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IID_IUiWindowGlobeObject = agcom.GUID(IUiWindowGlobeObject._uuid)
        vtable_offset_local = IUiWindowGlobeObject._vtable_offset - 1
        self.__dict__["_get_scene_id"] = IAGFUNCTYPE(pUnk, IID_IUiWindowGlobeObject, vtable_offset_local+1, POINTER(agcom.LONG))
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        if attrname in IUiWindowGlobeObject.__dict__ and type(IUiWindowGlobeObject.__dict__[attrname]) == property:
            return IUiWindowGlobeObject.__dict__[attrname]
        return None
    def __setattr__(self, attrname, value):
        if self._get_property(attrname) is not None:
            self._get_property(attrname).__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in IUiWindowGlobeObject.")
    
    @property
    def scene_id(self) -> int:
        """A unique identifier associated with the window that can be used with Connect to control the 3D globe."""
        with agmarshall.LONG_arg() as arg_pRetVal:
            agcls.evaluate_hresult(self.__dict__["_get_scene_id"](byref(arg_pRetVal.COM_val)))
            return arg_pRetVal.python_val


agcls.AgClassCatalog.add_catalog_entry("{B958EDBD-0569-4596-A253-BD90328844D0}", IUiWindowGlobeObject)
agcls.AgTypeNameMap["IUiWindowGlobeObject"] = IUiWindowGlobeObject



class UiWindowsCollection(IUiWindowsCollection):
    """Provides methods and properties to manage the windows."""
    def __init__(self, sourceObject=None):
        IUiWindowsCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiWindowsCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiWindowsCollection._get_property(self, attrname) is not None: found_prop = IUiWindowsCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiWindowsCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{82F7DB8A-A761-4C3E-95DF-37300A3738CB}", UiWindowsCollection)


class UiWindow(IUiWindow):
    """Represents a window abstraction. Provides methods and properties to manipulate the position and the state of the window."""
    def __init__(self, sourceObject=None):
        IUiWindow.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiWindow._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiWindow._get_property(self, attrname) is not None: found_prop = IUiWindow._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiWindow.")
        
agcls.AgClassCatalog.add_catalog_entry("{BD72ECC3-A4A2-42FB-95AC-AE25633BB9F6}", UiWindow)


class UiToolbar(IUiToolbar):
    """Represents a toolbar abstraction. Provides methods and properties to manipulate the position and the state of the toolbar."""
    def __init__(self, sourceObject=None):
        IUiToolbar.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiToolbar._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiToolbar._get_property(self, attrname) is not None: found_prop = IUiToolbar._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiToolbar.")
        
agcls.AgClassCatalog.add_catalog_entry("{C20AB584-ABCC-4BF3-96D4-D2A4AA880FBB}", UiToolbar)


class UiToolbarCollection(IUiToolbarCollection):
    """Provides methods and properties to manage the toolbars."""
    def __init__(self, sourceObject=None):
        IUiToolbarCollection.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiToolbarCollection._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiToolbarCollection._get_property(self, attrname) is not None: found_prop = IUiToolbarCollection._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiToolbarCollection.")
        
agcls.AgClassCatalog.add_catalog_entry("{28F000E7-D13E-485E-8484-0BCB359BBC55}", UiToolbarCollection)


class UiWindowMapObject(IUiWindowMapObject):
    """Provides methods and properties to manipulate the 2D map."""
    def __init__(self, sourceObject=None):
        IUiWindowMapObject.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiWindowMapObject._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiWindowMapObject._get_property(self, attrname) is not None: found_prop = IUiWindowMapObject._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiWindowMapObject.")
        
agcls.AgClassCatalog.add_catalog_entry("{D20C704C-0763-4CC9-9485-A2EA23C84E6B}", UiWindowMapObject)


class UiWindowGlobeObject(IUiWindowGlobeObject):
    """Provides methods and properties to manipulate the 3D globe."""
    def __init__(self, sourceObject=None):
        IUiWindowGlobeObject.__init__(self, sourceObject)
    def _private_init(self, pUnk:IUnknown):
        self.__dict__["_pUnk"] = pUnk
        IUiWindowGlobeObject._private_init(self, pUnk)
    def __eq__(self, other):
        """Checks equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        found_prop = None
        if IUiWindowGlobeObject._get_property(self, attrname) is not None: found_prop = IUiWindowGlobeObject._get_property(self, attrname)
        if found_prop is not None:
            found_prop.__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized attribute in UiWindowGlobeObject.")
        
agcls.AgClassCatalog.add_catalog_entry("{4F69FA5F-30E8-4A07-9D8C-1AD163A3DE0D}", UiWindowGlobeObject)



################################################################################
#          Copyright 2020-2020, Analytical Graphics, Inc.
################################################################################
