################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################

__all__ = [ "IStkObjectRootEventCOMHandler", 
            "ISTKXApplicationEventCOMHandler", 
            "IUiAxGraphics2DCntrlEventCOMHandler", 
            "IUiAxGraphics3DCntrlEventCOMHandler",
            "ISceneEventCOMHandler",
            "IKmlGraphicsEventCOMHandler",
            "IImageCollectionEventCOMHandler",
            "ITerrainOverlayCollectionEventCOMHandler"]

import os
from ctypes import CFUNCTYPE, POINTER, c_void_p, cast, addressof, Structure

from .                       import marshall     as agmarshall
from .                       import coclassutil  as agcls
from .comutil                import *
from ..utilities.exceptions  import *

class _COMEventHandlerImpl(object):
    _IID_IUnknown  = GUID.from_registry_format(IUnknown._guid)
    _IID_IDispatch = GUID.from_registry_format(IDispatch._guid)

    def __init__(self, pUnk, pUnkSink, iid):
        self._connection_id = None
        self._base_pUnkSink = pUnkSink
        self._cpc = agcls.IConnectionPointContainer(IUnknown(pUnk))
        self._cp = self._cpc.find_connection_point(iid)

    def __del__(self):
        del(self._cp)
        del(self._cpc)

    def _AddRef(self, pThis:PVOID) -> int:
        return 1
        
    def _Release(self, pThis:PVOID) -> int:
        return 0
        
    def _GetTypeInfoCount(self, pThis:PVOID, pctinfo:POINTER(UINT)) -> int:
        return E_NOTIMPL
        
    def _GetTypeInfo(self, pThis:PVOID, iTInfo:UINT, lcid:LCID, ppTInfo:POINTER(PVOID)) -> int:
        return E_NOTIMPL
        
    def _GetIDsOfNames(self, pThis:PVOID, riid:REFIID, rgszNames:POINTER(LPOLESTR), cNames:UINT, lcid:LCID, rgDispId:POINTER(DISPID)) -> int:
        return E_NOTIMPL

    def Subscribe(self):
        if self._connection_id is None:
            self._connection_id = self._cp.advise(addressof(self._base_pUnkSink))
    
    def Unsubscribe(self):
        if self._connection_id is not None:
            self._cp.unadvise(self._connection_id)
            self._connection_id = None
        
################################################################################
#          IAgStkObjectRootEvents
################################################################################
                 
class _AgStkObjectRootRawEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",               c_void_p),
                 ("IUnknown2",               c_void_p),
                 ("IUnknown3",               c_void_p),
                 ("OnScenarioNew",           c_void_p),
                 ("OnScenarioLoad",          c_void_p),
                 ("OnScenarioClose",         c_void_p),
                 ("OnScenarioSave",          c_void_p),
                 ("OnLogMessage",            c_void_p),
                 ("OnAnimUpdate",            c_void_p),
                 ("OnStkObjectAdded",        c_void_p),
                 ("OnStkObjectDeleted",      c_void_p),
                 ("OnStkObjectRenamed",      c_void_p),
                 ("OnAnimationPlayback",     c_void_p),
                 ("OnAnimationRewind",       c_void_p),
                 ("OnAnimationPause",        c_void_p),
                 ("OnScenarioBeforeSave",    c_void_p),
                 ("OnAnimationStep",         c_void_p),
                 ("OnAnimationStepBack",     c_void_p),
                 ("OnAnimationSlower",       c_void_p),
                 ("OnAnimationFaster",       c_void_p),
                 ("OnPercentCompleteUpdate", c_void_p),
                 ("OnPercentCompleteEnd",    c_void_p),
                 ("OnPercentCompleteBegin",  c_void_p),
                 ("OnStkObjectChanged",      c_void_p),
                 ("OnScenarioBeforeClose",   c_void_p),
                 ("OnStkObjectPreDelete",    c_void_p)]
                 
class _AgStkObjectRootRawEvents2UnkSink(Structure):
    _fields_ = [ ("IUnknown1",                  c_void_p),
                 ("IUnknown2",                  c_void_p),
                 ("IUnknown3",                  c_void_p),
                 ("OnStkObjectStart3dEditing",  c_void_p),
                 ("OnStkObjectStop3dEditing",   c_void_p),
                 ("OnStkObjectApply3dEditing",  c_void_p),
                 ("OnStkObjectCancel3dEditing", c_void_p),
                 ("OnStkObjectPreCut",          c_void_p),
                 ("OnStkObjectCopy",            c_void_p),
                 ("OnStkObjectPaste",           c_void_p) ]

class IStkObjectRootEventCOMHandler(_COMEventHandlerImpl):
    _IID_IAgStkObjectRootEvents     = GUID.from_registry_format("{4A25888C-BF0A-4B79-816B-2623D16042B0}")
    _IID_IAgStkObjectRootRawEvents  = GUID.from_registry_format("{A381FC71-ACBF-4034-B732-2A36B0CFA2E4}")
    _IID_IAgStkObjectRootRawEvents2 = GUID.from_registry_format("{F607E46E-A49F-4B9B-BE24-F29F63709FB0}")

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable1()
        self._init_vtable2()
        _COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink1, IStkObjectRootEventCOMHandler._IID_IAgStkObjectRootEvents)

    def _init_vtable1(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]           = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown2"]           = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown3"]           = CFUNCTYPE(ULONG, PVOID)(self._Release)
        else:           
            self.__dict__["_cfunc_IUnknown3"]           = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown1"]           = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown2"]           = CFUNCTYPE(ULONG, PVOID)(self._Release)
        self.__dict__["_cfunc_OnScenarioNew"]           = CFUNCTYPE(None, PVOID, BSTR)(self._OnScenarioNew)
        self.__dict__["_cfunc_OnScenarioLoad"]          = CFUNCTYPE(None, PVOID, BSTR)(self._OnScenarioLoad)
        self.__dict__["_cfunc_OnScenarioClose"]         = CFUNCTYPE(None, PVOID)(self._OnScenarioClose)
        self.__dict__["_cfunc_OnScenarioSave"]          = CFUNCTYPE(None, PVOID, BSTR)(self._OnScenarioSave)
        self.__dict__["_cfunc_OnLogMessage"]            = CFUNCTYPE(None, PVOID, BSTR, LONG, LONG, BSTR, LONG, LONG)(self._OnLogMessage)
        self.__dict__["_cfunc_OnAnimUpdate"]            = CFUNCTYPE(None, PVOID, DOUBLE)(self._OnAnimUpdate)
        self.__dict__["_cfunc_OnStkObjectAdded"]        = CFUNCTYPE(None, PVOID, VARIANT)(self._OnStkObjectAdded)
        self.__dict__["_cfunc_OnStkObjectDeleted"]      = CFUNCTYPE(None, PVOID, VARIANT)(self._OnStkObjectDeleted)
        self.__dict__["_cfunc_OnStkObjectRenamed"]      = CFUNCTYPE(None, PVOID, VARIANT, BSTR, BSTR)(self._OnStkObjectRenamed)
        self.__dict__["_cfunc_OnAnimationPlayback"]     = CFUNCTYPE(None, PVOID, DOUBLE, LONG, LONG)(self._OnAnimationPlayback)
        self.__dict__["_cfunc_OnAnimationRewind"]       = CFUNCTYPE(None, PVOID)(self._OnAnimationRewind)
        self.__dict__["_cfunc_OnAnimationPause"]        = CFUNCTYPE(None, PVOID, DOUBLE)(self._OnAnimationPause)
        self.__dict__["_cfunc_OnScenarioBeforeSave"]    = CFUNCTYPE(None, PVOID, PVOID)(self._OnScenarioBeforeSave)
        self.__dict__["_cfunc_OnAnimationStep"]         = CFUNCTYPE(None, PVOID, DOUBLE)(self._OnAnimationStep)
        self.__dict__["_cfunc_OnAnimationStepBack"]     = CFUNCTYPE(None, PVOID, DOUBLE)(self._OnAnimationStepBack)
        self.__dict__["_cfunc_OnAnimationSlower"]       = CFUNCTYPE(None, PVOID)(self._OnAnimationSlower)
        self.__dict__["_cfunc_OnAnimationFaster"]       = CFUNCTYPE(None, PVOID)(self._OnAnimationFaster)
        self.__dict__["_cfunc_OnPercentCompleteUpdate"] = CFUNCTYPE(None, PVOID, PVOID)(self._OnPercentCompleteUpdate)
        self.__dict__["_cfunc_OnPercentCompleteEnd"]    = CFUNCTYPE(None, PVOID)(self._OnPercentCompleteEnd)
        self.__dict__["_cfunc_OnPercentCompleteBegin"]  = CFUNCTYPE(None, PVOID)(self._OnPercentCompleteBegin)
        self.__dict__["_cfunc_OnStkObjectChanged"]      = CFUNCTYPE(None, PVOID, PVOID)(self._OnStkObjectChanged)
        self.__dict__["_cfunc_OnScenarioBeforeClose"]   = CFUNCTYPE(None, PVOID)(self._OnScenarioBeforeClose)
        self.__dict__["_cfunc_OnStkObjectPreDelete"]    = CFUNCTYPE(None, PVOID, PVOID)(self._OnStkObjectPreDelete)

        self.__dict__["_vtable1"] = _AgStkObjectRootRawEventsUnkSink( *[cast(self._cfunc_IUnknown1,               c_void_p),
                                                                        cast(self._cfunc_IUnknown2,               c_void_p),
                                                                        cast(self._cfunc_IUnknown3,               c_void_p),
                                                                        cast(self._cfunc_OnScenarioNew,           c_void_p),
                                                                        cast(self._cfunc_OnScenarioLoad,          c_void_p),
                                                                        cast(self._cfunc_OnScenarioClose,         c_void_p),
                                                                        cast(self._cfunc_OnScenarioSave,          c_void_p),
                                                                        cast(self._cfunc_OnLogMessage,            c_void_p),
                                                                        cast(self._cfunc_OnAnimUpdate,            c_void_p),
                                                                        cast(self._cfunc_OnStkObjectAdded,        c_void_p),
                                                                        cast(self._cfunc_OnStkObjectDeleted,      c_void_p),
                                                                        cast(self._cfunc_OnStkObjectRenamed,      c_void_p),
                                                                        cast(self._cfunc_OnAnimationPlayback,     c_void_p),
                                                                        cast(self._cfunc_OnAnimationRewind,       c_void_p),
                                                                        cast(self._cfunc_OnAnimationPause,        c_void_p),
                                                                        cast(self._cfunc_OnScenarioBeforeSave,    c_void_p),
                                                                        cast(self._cfunc_OnAnimationStep,         c_void_p),
                                                                        cast(self._cfunc_OnAnimationStepBack,     c_void_p),
                                                                        cast(self._cfunc_OnAnimationSlower,       c_void_p),
                                                                        cast(self._cfunc_OnAnimationFaster,       c_void_p),
                                                                        cast(self._cfunc_OnPercentCompleteUpdate, c_void_p),
                                                                        cast(self._cfunc_OnPercentCompleteEnd,    c_void_p),
                                                                        cast(self._cfunc_OnPercentCompleteBegin,  c_void_p),
                                                                        cast(self._cfunc_OnStkObjectChanged,      c_void_p),
                                                                        cast(self._cfunc_OnScenarioBeforeClose,   c_void_p),
                                                                        cast(self._cfunc_OnStkObjectPreDelete,    c_void_p)] )
        self.__dict__["_pUnkSink1"] = pointer(self._vtable1)
        
    def _init_vtable2(self):
        self.__dict__["_cfunc_OnStkObjectStart3dEditing"]  = CFUNCTYPE(None, PVOID, BSTR)(self._OnStkObjectStart3dEditing)
        self.__dict__["_cfunc_OnStkObjectStop3dEditing"]   = CFUNCTYPE(None, PVOID, BSTR)(self._OnStkObjectStop3dEditing)
        self.__dict__["_cfunc_OnStkObjectApply3dEditing"]  = CFUNCTYPE(None, PVOID, BSTR)(self._OnStkObjectApply3dEditing)
        self.__dict__["_cfunc_OnStkObjectCancel3dEditing"] = CFUNCTYPE(None, PVOID, BSTR)(self._OnStkObjectCancel3dEditing)
        self.__dict__["_cfunc_OnStkObjectPreCut"]          = CFUNCTYPE(None, PVOID, PVOID)(self._OnStkObjectPreCut)
        self.__dict__["_cfunc_OnStkObjectCopy"]            = CFUNCTYPE(None, PVOID, PVOID)(self._OnStkObjectCopy)
        self.__dict__["_cfunc_OnStkObjectPaste"]           = CFUNCTYPE(None, PVOID, PVOID)(self._OnStkObjectPaste)

        self.__dict__["_vtable2"] = _AgStkObjectRootRawEvents2UnkSink( *[cast(self._cfunc_IUnknown1,                  c_void_p),
                                                                         cast(self._cfunc_IUnknown2,                  c_void_p),
                                                                         cast(self._cfunc_IUnknown3,                  c_void_p),
                                                                         cast(self._cfunc_OnStkObjectStart3dEditing,  c_void_p),
                                                                         cast(self._cfunc_OnStkObjectStop3dEditing,   c_void_p),
                                                                         cast(self._cfunc_OnStkObjectApply3dEditing,  c_void_p),
                                                                         cast(self._cfunc_OnStkObjectCancel3dEditing, c_void_p),
                                                                         cast(self._cfunc_OnStkObjectPreCut,          c_void_p),
                                                                         cast(self._cfunc_OnStkObjectCopy,            c_void_p),
                                                                         cast(self._cfunc_OnStkObjectPaste,           c_void_p)] )
        self.__dict__["_pUnkSink2"] = pointer(self._vtable2)

    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == _COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == IStkObjectRootEventCOMHandler._IID_IAgStkObjectRootEvents:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == IStkObjectRootEventCOMHandler._IID_IAgStkObjectRootRawEvents:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == IStkObjectRootEventCOMHandler._IID_IAgStkObjectRootRawEvents2:
            ppvObject[0] = addressof(self._pUnkSink2)
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE 

    def _OnScenarioNew(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioNew"]._callbacks:
            callback(path)
                
    def _OnScenarioLoad(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioLoad"]._callbacks:
            callback(path)

    def _OnScenarioClose(self, pThis:PVOID) -> None:
        for callback in self._events["OnScenarioClose"]._callbacks:
            callback()

    def _OnScenarioSave(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioSave"]._callbacks:
            callback(path)

    def _OnLogMessage(self, pThis:PVOID, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._events["OnLogMessage"]._callbacks:
            callback(message, agcls.AgTypeNameMap["LOG_MSG_TYPE"](msgType), errorCode, fileName, lineNo, agcls.AgTypeNameMap["LOG_MSG_DISP_ID"](dispID))

    def _OnAnimUpdate(self, pThis:PVOID, timeEpSec:float) -> None:
        for callback in self._events["OnAnimUpdate"]._callbacks:
            callback(timeEpSec)

    def _OnStkObjectAdded(self, pThis:PVOID, Sender:VARIANT) -> None:
        for callback in self._events["OnStkObjectAdded"]._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender:
                callback(arg_Sender.python_val)
                
    def _OnStkObjectDeleted(self, pThis:PVOID, Sender:VARIANT) -> None:
        for callback in self._events["OnStkObjectDeleted"]._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender:
                callback(arg_Sender.python_val)
                
    def _OnStkObjectRenamed(self, pThis:PVOID, Sender:VARIANT, OldPath:str, NewPath:str) -> None:
        for callback in self._events["OnStkObjectRenamed"]._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender:
                callback(arg_Sender.python_val, OldPath, NewPath)
                
    def _OnAnimationPlayback(self, pThis:PVOID, CurrentTime:float, eAction:int, eDirection:int) -> None:
        for callback in self._events["OnAnimationPlayback"]._callbacks:
            callback(CurrentTime, agcls.AgTypeNameMap["ANIMATION_ACTIONS"](eAction), agcls.AgTypeNameMap["ANIMATION_DIRECTIONS"](eDirection.python_val))
                
    def _OnAnimationRewind(self, pThis:PVOID) -> None:
        for callback in self._events["OnAnimationRewind"]._callbacks:
            callback()
            
    def _OnAnimationPause(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationPause"]._callbacks:
            callback(CurrentTime)
                
    def _OnScenarioBeforeSave(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnScenarioBeforeSave"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["ScenarioBeforeSaveEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
                
    def _OnAnimationStep(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationStep"]._callbacks:
            callback(CurrentTime)
                
    def _OnAnimationStepBack(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationStepBack"]._callbacks:
            callback(CurrentTime)
                
    def _OnAnimationSlower(self, pThis:PVOID) -> None:
        for callback in self._events["OnAnimationSlower"]._callbacks:
            callback()
            
    def _OnAnimationFaster(self, pThis:PVOID) -> None:
        for callback in self._events["OnAnimationFaster"]._callbacks:
            callback()
            
    def _OnPercentCompleteUpdate(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnPercentCompleteUpdate"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["PctCmpltEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
                
    def _OnPercentCompleteEnd(self, pThis:PVOID) -> None:
        for callback in self._events["OnPercentCompleteEnd"]._callbacks:
            callback()
            
    def _OnPercentCompleteBegin(self, pThis:PVOID) -> None:
        for callback in self._events["OnPercentCompleteBegin"]._callbacks:
            callback()
            
    def _OnStkObjectChanged(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectChanged"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["StkObjectChangedEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
                
    def _OnScenarioBeforeClose(self, pThis:PVOID) -> None:
        for callback in self._events["OnScenarioBeforeClose"]._callbacks:
            callback()
            
    def _OnStkObjectPreDelete(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectPreDelete"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["StkObjectPreDeleteEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
                
    def _OnStkObjectStart3dEditing(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnStkObjectStart3dEditing"]._callbacks:
            callback(path)
            
    def _OnStkObjectStop3dEditing(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnStkObjectStop3dEditing"]._callbacks:
            callback(path)
            
    def _OnStkObjectApply3dEditing(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnStkObjectApply3dEditing"]._callbacks:
            callback(path)
            
    def _OnStkObjectCancel3dEditing(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnStkObjectCancel3dEditing"]._callbacks:
            callback(path)
            
    def _OnStkObjectPreCut(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectPreCut"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["StkObjectCutCopyPasteEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
            
    def _OnStkObjectCopy(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectCopy"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["StkObjectCutCopyPasteEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
            
    def _OnStkObjectPaste(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectPaste"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["StkObjectCutCopyPasteEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
      
    
################################################################################
#          IAgSTKXApplicationEvents
################################################################################
                 
class _AgSTKXApplicationEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",                   c_void_p),
                 ("IUnknown2",                   c_void_p),
                 ("IUnknown3",                   c_void_p),
                 ("OnScenarioNew",               c_void_p),
                 ("OnScenarioLoad",              c_void_p),
                 ("OnScenarioClose",             c_void_p),
                 ("OnScenarioSave",              c_void_p),
                 ("OnLogMessage",                c_void_p),
                 ("OnAnimUpdate",                c_void_p),
                 ("OnNewGlobeCtrlRequest",       c_void_p),
                 ("OnNewMapCtrlRequest",         c_void_p),
                 ("OnBeforeNewScenario",         c_void_p),
                 ("OnBeforeLoadScenario",        c_void_p),
                 ("OnBeginScenarioClose",        c_void_p),
                 ("OnNewGfxAnalysisCtrlRequest", c_void_p),
                 ("OnSSLCertificateServerError", c_void_p),
                 ("OnConControlQuitReceived",    c_void_p) ]

class ISTKXApplicationEventCOMHandler(_COMEventHandlerImpl):
    _IID_IAgSTKXApplicationRawEvents = GUID.from_registry_format("{78C74BAF-7845-40BA-9EBE-C10FD081BC60}")
    _IID_IAgSTKXApplicationEvents    = GUID.from_registry_format("{3787DAB9-9A91-414B-B4EF-2339E0FBA96C}")

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        _COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, ISTKXApplicationEventCOMHandler._IID_IAgSTKXApplicationEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]               = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown2"]               = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown3"]               = CFUNCTYPE(ULONG, PVOID)(self._Release)
        else:               
            self.__dict__["_cfunc_IUnknown3"]               = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown1"]               = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown2"]               = CFUNCTYPE(ULONG, PVOID)(self._Release)
        self.__dict__["_cfunc_OnScenarioNew"]               = CFUNCTYPE(None, PVOID, BSTR)(self._OnScenarioNew)
        self.__dict__["_cfunc_OnScenarioLoad"]              = CFUNCTYPE(None, PVOID, BSTR)(self._OnScenarioLoad)
        self.__dict__["_cfunc_OnScenarioClose"]             = CFUNCTYPE(None, PVOID)(self._OnScenarioClose)
        self.__dict__["_cfunc_OnScenarioSave"]              = CFUNCTYPE(None, PVOID, BSTR)(self._OnScenarioSave)
        self.__dict__["_cfunc_OnLogMessage"]                = CFUNCTYPE(None, PVOID, BSTR, LONG, LONG, BSTR, LONG, LONG)(self._OnLogMessage)
        self.__dict__["_cfunc_OnAnimUpdate"]                = CFUNCTYPE(HRESULT, PVOID, DOUBLE)(self._OnAnimUpdate)
        self.__dict__["_cfunc_OnNewGlobeCtrlRequest"]       = CFUNCTYPE(None, PVOID, LONG)(self._OnNewGlobeCtrlRequest)
        self.__dict__["_cfunc_OnNewMapCtrlRequest"]         = CFUNCTYPE(None, PVOID, LONG)(self._OnNewMapCtrlRequest)
        self.__dict__["_cfunc_OnBeforeNewScenario"]         = CFUNCTYPE(None, PVOID, BSTR)(self._OnBeforeNewScenario)
        self.__dict__["_cfunc_OnBeforeLoadScenario"]        = CFUNCTYPE(None, PVOID, BSTR)(self._OnBeforeLoadScenario)
        self.__dict__["_cfunc_OnBeginScenarioClose"]        = CFUNCTYPE(None, PVOID)(self._OnBeginScenarioClose)
        self.__dict__["_cfunc_OnNewGfxAnalysisCtrlRequest"] = CFUNCTYPE(None, PVOID, LONG, LONG)(self._OnNewGfxAnalysisCtrlRequest)
        self.__dict__["_cfunc_OnSSLCertificateServerError"] = CFUNCTYPE(None, PVOID, PVOID)(self._OnSSLCertificateServerError)
        self.__dict__["_cfunc_OnConControlQuitReceived"]    = CFUNCTYPE(None, PVOID, PVOID)(self._OnConControlQuitReceived)
        
        self.__dict__["_vtable"] = _AgSTKXApplicationEventsUnkSink( *[cast(self._cfunc_IUnknown1,                   c_void_p),
                                                                      cast(self._cfunc_IUnknown2,                   c_void_p),
                                                                      cast(self._cfunc_IUnknown3,                   c_void_p),
                                                                      cast(self._cfunc_OnScenarioNew,               c_void_p),
                                                                      cast(self._cfunc_OnScenarioLoad,              c_void_p),
                                                                      cast(self._cfunc_OnScenarioClose,             c_void_p),
                                                                      cast(self._cfunc_OnScenarioSave,              c_void_p),
                                                                      cast(self._cfunc_OnLogMessage,                c_void_p),
                                                                      cast(self._cfunc_OnAnimUpdate,                c_void_p),
                                                                      cast(self._cfunc_OnNewGlobeCtrlRequest,       c_void_p),
                                                                      cast(self._cfunc_OnNewMapCtrlRequest,         c_void_p),
                                                                      cast(self._cfunc_OnBeforeNewScenario,         c_void_p),
                                                                      cast(self._cfunc_OnBeforeLoadScenario,        c_void_p),
                                                                      cast(self._cfunc_OnBeginScenarioClose,        c_void_p),
                                                                      cast(self._cfunc_OnNewGfxAnalysisCtrlRequest, c_void_p),
                                                                      cast(self._cfunc_OnSSLCertificateServerError, c_void_p),
                                                                      cast(self._cfunc_OnConControlQuitReceived,    c_void_p)] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)

    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == _COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        elif iid == ISTKXApplicationEventCOMHandler._IID_IAgSTKXApplicationRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == ISTKXApplicationEventCOMHandler._IID_IAgSTKXApplicationEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _OnScenarioNew(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioNew"]._callbacks:
            callback(path)
                
    def _OnScenarioLoad(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioLoad"]._callbacks:
            callback(path)

    def _OnScenarioClose(self, pThis:PVOID) -> None:
        for callback in self._events["OnScenarioClose"]._callbacks:
            callback()

    def _OnScenarioSave(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioSave"]._callbacks:
            callback(path)

    def _OnLogMessage(self, pThis:PVOID, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._events["OnLogMessage"]._callbacks:
            callback(message, agcls.AgTypeNameMap["LOG_MSG_TYPE"](msgType), errorCode, fileName, lineNo, agcls.AgTypeNameMap["LOG_MSG_DISP_ID"](dispID))

    def _OnAnimUpdate(self, pThis:PVOID, timeEpSec:float) -> int:
        for callback in self._events["OnAnimUpdate"]._callbacks:
            callback(timeEpSec)
        return S_OK

    def _OnNewGlobeCtrlRequest(self, pThis:PVOID, SceneID:int) -> None:
        for callback in self._events["OnNewGlobeCtrlRequest"]._callbacks:
            callback(SceneID)
    
    def _OnNewMapCtrlRequest(self, pThis:PVOID, WinID:int) -> None:
        for callback in self._events["OnNewMapCtrlRequest"]._callbacks:
            callback(WinID)
        
    def _OnBeforeNewScenario(self, pThis:PVOID, Scenario:str) -> None:
        for callback in self._events["OnBeforeNewScenario"]._callbacks:
            callback(Scenario)
        
    def _OnBeforeLoadScenario(self, pThis:PVOID, Scenario:str) -> None:
        for callback in self._events["OnBeforeLoadScenario"]._callbacks:
            callback(Scenario)
        
    def _OnBeginScenarioClose(self, pThis:PVOID) -> None:
        for callback in self._events["OnBeginScenarioClose"]._callbacks:
            callback()
    
    def _OnNewGfxAnalysisCtrlRequest(self, pThis:PVOID, SceneID:int, GfxAnalysisMode:int) -> None:
        for callback in self._events["OnNewGfxAnalysisCtrlRequest"]._callbacks:
            callback(SceneID, agcls.AgTypeNameMap["GRAPHICS_2D_ANALYSIS_MODE"](GfxAnalysisMode))
    
    def _OnSSLCertificateServerError(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnSSLCertificateServerError"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["STKXSSLCertificateErrorEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
        
    def _OnConControlQuitReceived(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnConControlQuitReceived"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["STKXConControlQuitReceivedEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)

                
################################################################################
#          ActiveX controls
################################################################################
                 
class _AgUiAxStockEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",   c_void_p),
                 ("IUnknown2",   c_void_p),
                 ("IUnknown3",   c_void_p),
                 ("KeyDown",     c_void_p),
                 ("KeyPress",    c_void_p),
                 ("KeyUp",       c_void_p),
                 ("Click",       c_void_p),
                 ("DblClick",    c_void_p),
                 ("MouseDown",   c_void_p),
                 ("MouseMove",   c_void_p),
                 ("MouseUp",     c_void_p),
                 ("OLEDragDrop", c_void_p),
                 ("MouseWheel",  c_void_p)]
                 
class _AgUiAxVOCntrlEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",             c_void_p),
                 ("IUnknown2",             c_void_p),
                 ("IUnknown3",             c_void_p),
                 ("KeyDown",               c_void_p),
                 ("KeyPress",              c_void_p),
                 ("KeyUp",                 c_void_p),
                 ("Click",                 c_void_p),
                 ("DblClick",              c_void_p),
                 ("MouseDown",             c_void_p),
                 ("MouseMove",             c_void_p),
                 ("MouseUp",               c_void_p),
                 ("OLEDragDrop",           c_void_p),
                 ("MouseWheel",            c_void_p),
                 ("OnObjectEditingStart",  c_void_p),
                 ("OnObjectEditingApply",  c_void_p),
                 ("OnObjectEditingCancel", c_void_p),
                 ("OnObjectEditingStop",   c_void_p)]

class IAgUiAxStockEventCOMHandler(object):
    _IID_IAgUiAxStockRawEvents   = GUID.from_registry_format("{32A1F220-C90C-4FC6-B2BF-DF06DB89B72E}")

    def __init__(self, events:dict):
        self._events = events
        self.__dict__["_cfunc_KeyDown"]     = CFUNCTYPE(HRESULT, PVOID, POINTER(SHORT), SHORT)(self._KeyDown)
        self.__dict__["_cfunc_KeyPress"]    = CFUNCTYPE(HRESULT, PVOID, POINTER(SHORT))(self._KeyPress)
        self.__dict__["_cfunc_KeyUp"]       = CFUNCTYPE(HRESULT, PVOID, POINTER(SHORT), SHORT)(self._KeyUp)
        self.__dict__["_cfunc_Click"]       = CFUNCTYPE(HRESULT, PVOID)(self._Click)
        self.__dict__["_cfunc_DblClick"]    = CFUNCTYPE(HRESULT, PVOID)(self._DblClick)
        self.__dict__["_cfunc_MouseDown"]   = CFUNCTYPE(HRESULT, PVOID, SHORT, SHORT, OLE_XPOS_PIXELS, OLE_YPOS_PIXELS)(self._MouseDown)
        self.__dict__["_cfunc_MouseMove"]   = CFUNCTYPE(HRESULT, PVOID, SHORT, SHORT, OLE_XPOS_PIXELS, OLE_YPOS_PIXELS)(self._MouseMove)
        self.__dict__["_cfunc_MouseUp"]     = CFUNCTYPE(HRESULT, PVOID, SHORT, SHORT, OLE_XPOS_PIXELS, OLE_YPOS_PIXELS)(self._MouseUp)
        self.__dict__["_cfunc_OLEDragDrop"] = CFUNCTYPE(HRESULT, PVOID, PVOID, LONG, SHORT, SHORT, LONG, LONG)(self._OLEDragDrop)
        self.__dict__["_cfunc_MouseWheel"]  = CFUNCTYPE(HRESULT, PVOID, SHORT, SHORT, SHORT, OLE_XPOS_PIXELS, OLE_YPOS_PIXELS)(self._MouseWheel)

    def _MouseWheel(self, pThis:PVOID, Button:int, Shift:int, Delta:int, X:int, Y:int) -> int:
        for callback in self._events["MouseWheel"]._callbacks:
            callback(KeyCode, Shift, Delta, X, Y)
        return S_OK

    def _KeyDown(self, pThis:PVOID, KeyCode:POINTER(SHORT), Shift:int) -> int:
        for callback in self._events["KeyDown"]._callbacks:
            callback(KeyCode[0], Shift)
        return S_OK

    def _KeyPress(self, pThis:PVOID, KeyAscii:POINTER(SHORT)) -> int:
        for callback in self._events["KeyPress"]._callbacks:
            callback(KeyAscii[0])
        return S_OK

    def _KeyUp(self, pThis:PVOID, KeyCode:POINTER(SHORT), Shift:int) -> int:
        for callback in self._events["KeyUp"]._callbacks:
            callback(KeyCode[0], Shift)
        return S_OK

    def _Click(self, pThis:PVOID) -> int:
        for callback in self._events["Click"]._callbacks:
            callback()
        return S_OK

    def _DblClick(self, pThis:PVOID) -> int:
        for callback in self._events["DblClick"]._callbacks:
            callback()
        return S_OK

    def _MouseDown(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._events["MouseDown"]._callbacks:
            callback(KeyCode, Shift, X, Y)
        return S_OK

    def _MouseMove(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._events["MouseMove"]._callbacks:
            callback(KeyCode, Shift, X, Y)
        return S_OK

    def _MouseUp(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._events["MouseUp"]._callbacks:
            callback(KeyCode, Shift, X, Y)
        return S_OK

    def _OLEDragDrop(self, pThis:PVOID, Data:PVOID, Effect:int, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._events["OLEDragDrop"]._callbacks:
            with agmarshall.AgInterface_event_callback_arg(Data, agcls.AgTypeNameMap["DataObject"]) as arg_Data:
                callback(arg_Data.python_val, Effect, KeyCode, Shift, X, Y)
        return S_OK
            
class IUiAxGraphics2DCntrlEventCOMHandler(_COMEventHandlerImpl, IAgUiAxStockEventCOMHandler):
    _IID_IAgUiAx2DCntrlEvents    = GUID.from_registry_format("{DA0E1628-101E-4A18-B922-B4189E31AD7E}")

    def __init__(self, pUnk:IUnknown, events:dict):
        IAgUiAxStockEventCOMHandler.__init__(self, events)
        self._init_vtable()
        _COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, IUiAxGraphics2DCntrlEventHandler._IID_IAgUiAx2DCntrlEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"] = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown2"] = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown3"] = CFUNCTYPE(ULONG, PVOID)(self._Release)
        else:               
            self.__dict__["_cfunc_IUnknown3"] = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown1"] = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown2"] = CFUNCTYPE(ULONG, PVOID)(self._Release)
        
        self.__dict__["_vtable"] = _AgUiAxStockEventsUnkSink( *[cast(self._cfunc_IUnknown1,   c_void_p),
                                                                cast(self._cfunc_IUnknown2,   c_void_p),
                                                                cast(self._cfunc_IUnknown3,   c_void_p),
                                                                cast(self._cfunc_KeyDown,     c_void_p),
                                                                cast(self._cfunc_KeyPress,    c_void_p),
                                                                cast(self._cfunc_KeyUp,       c_void_p),
                                                                cast(self._cfunc_Click,       c_void_p),
                                                                cast(self._cfunc_DblClick,    c_void_p),
                                                                cast(self._cfunc_MouseDown,   c_void_p),
                                                                cast(self._cfunc_MouseMove,   c_void_p),
                                                                cast(self._cfunc_MouseUp,     c_void_p),
                                                                cast(self._cfunc_OLEDragDrop, c_void_p),
                                                                cast(self._cfunc_MouseWheel,  c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)
        
    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == _COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgUiAxStockEventCOMHandler._IID_IAgUiAxStockRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IUiAxGraphics2DCntrlEventCOMHandler._IID_IAgUiAx2DCntrlEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

class IUiAxGraphics3DCntrlEventCOMHandler(_COMEventHandlerImpl, IAgUiAxStockEventCOMHandler):
    _IID_IAgUiAxVOCntrlRawEvents = GUID.from_registry_format("{1ADE7AE0-B431-4ED4-8494-335EBB14007C}")
    _IID_IAgUiAxVOCntrlEvents    = GUID.from_registry_format("{C46F1BA0-22E4-432B-9259-C6DEF33FE2B2}")

    def __init__(self, pUnk:IUnknown, events:dict):
        IAgUiAxStockEventCOMHandler.__init__(self, events)
        self._init_vtable()
        _COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, IUiAxGraphics3DCntrlEventCOMHandler._IID_IAgUiAxVOCntrlEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"] = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown2"] = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown3"] = CFUNCTYPE(ULONG, PVOID)(self._Release)
        else:               
            self.__dict__["_cfunc_IUnknown3"] = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown1"] = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown2"] = CFUNCTYPE(ULONG, PVOID)(self._Release)
        self.__dict__["_cfunc_OnObjectEditingStart"]  = CFUNCTYPE(HRESULT, PVOID, BSTR)(self._OnObjectEditingStart)
        self.__dict__["_cfunc_OnObjectEditingApply"]  = CFUNCTYPE(HRESULT, PVOID, BSTR)(self._OnObjectEditingApply)
        self.__dict__["_cfunc_OnObjectEditingCancel"] = CFUNCTYPE(HRESULT, PVOID, BSTR)(self._OnObjectEditingCancel)
        self.__dict__["_cfunc_OnObjectEditingStop"]   = CFUNCTYPE(HRESULT, PVOID, BSTR)(self._OnObjectEditingStop)
        
        self.__dict__["_vtable"] = _AgUiAxVOCntrlEventsUnkSink( *[cast(self._cfunc_IUnknown1,             c_void_p),
                                                                  cast(self._cfunc_IUnknown2,             c_void_p),
                                                                  cast(self._cfunc_IUnknown3,             c_void_p),
                                                                  cast(self._cfunc_KeyDown,               c_void_p),
                                                                  cast(self._cfunc_KeyPress,              c_void_p),
                                                                  cast(self._cfunc_KeyUp,                 c_void_p),
                                                                  cast(self._cfunc_Click,                 c_void_p),
                                                                  cast(self._cfunc_DblClick,              c_void_p),
                                                                  cast(self._cfunc_MouseDown,             c_void_p),
                                                                  cast(self._cfunc_MouseMove,             c_void_p),
                                                                  cast(self._cfunc_MouseUp,               c_void_p),
                                                                  cast(self._cfunc_OLEDragDrop,           c_void_p),
                                                                  cast(self._cfunc_MouseWheel,            c_void_p),
                                                                  cast(self._cfunc_OnObjectEditingStart,  c_void_p),
                                                                  cast(self._cfunc_OnObjectEditingApply,  c_void_p),
                                                                  cast(self._cfunc_OnObjectEditingCancel, c_void_p),
                                                                  cast(self._cfunc_OnObjectEditingStop,   c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)
        
    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == _COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgUiAxStockEventCOMHandler._IID_IAgUiAxStockRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IUiAxGraphics3DCntrlEventCOMHandler._IID_IAgUiAxVOCntrlRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IUiAxGraphics3DCntrlEventCOMHandler._IID_IAgUiAxVOCntrlEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _OnObjectEditingStart(self, pThis:PVOID, Path:str) -> int:
        for callback in self._events["OnObjectEditingStart"]._callbacks:
            callback(Path)
        return S_OK

    def _OnObjectEditingApply(self, pThis:PVOID, Path:str) -> int:
        for callback in self._events["OnObjectEditingApply"]._callbacks:
            callback(Path)
        return S_OK

    def _OnObjectEditingCancel(self, pThis:PVOID, Path:str) -> int:
        for callback in self._events["OnObjectEditingCancel"]._callbacks:
            callback(Path)
        return S_OK

    def _OnObjectEditingStop(self, pThis:PVOID, Path:str) -> int:
        for callback in self._events["OnObjectEditingStop"]._callbacks:
            callback(Path)
        return S_OK
            
        
################################################################################
#          IAgStkGraphicsSceneEvents
################################################################################
                 
class _AgStkGraphicsSceneEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",        c_void_p),
                 ("IUnknown2",        c_void_p),
                 ("IUnknown3",        c_void_p),
                 ("GetTypeInfoCount", c_void_p),
                 ("GetTypeInfo",      c_void_p),
                 ("GetIDsOfNames",    c_void_p),
                 ("Invoke",           c_void_p),
                 ("Rendering",        c_void_p)]

class ISceneEventCOMHandler(_COMEventHandlerImpl):
    _IID_IAgStkGraphicsSceneEvents = GUID.from_registry_format("{FACA0112-848C-415D-B38C-0ED3F121D906}")
    _DISPID_Rendering = 13901

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        _COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, ISceneEventCOMHandler._IID_IAgStkGraphicsSceneEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(ULONG, PVOID)(self._Release)
        else:                                    
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._Release)
        self.__dict__["_cfunc_GetTypeInfoCount"] = CFUNCTYPE(HRESULT, PVOID, POINTER(UINT))(self._GetTypeInfoCount)
        self.__dict__["_cfunc_GetTypeInfo"]      = CFUNCTYPE(HRESULT, PVOID, UINT, LCID, POINTER(PVOID))(self._GetTypeInfo)
        self.__dict__["_cfunc_GetIDsOfNames"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID))(self._GetIDsOfNames)
        self.__dict__["_cfunc_Invoke"]           = CFUNCTYPE(HRESULT, PVOID, DISPID, REFIID, LCID, WORD, POINTER(DISPPARAMS), POINTER(VARIANT), POINTER(EXCEPINFO), POINTER(UINT))(self._Invoke)
        self.__dict__["_cfunc_Rendering"]        = CFUNCTYPE(HRESULT, PVOID, VARIANT, PVOID)(self._Rendering)
        
        self.__dict__["_vtable"] = _AgStkGraphicsSceneEventsUnkSink( *[cast(self._cfunc_IUnknown1,        c_void_p),
                                                                       cast(self._cfunc_IUnknown2,        c_void_p),
                                                                       cast(self._cfunc_IUnknown3,        c_void_p),
                                                                       cast(self._cfunc_GetTypeInfoCount, c_void_p),
                                                                       cast(self._cfunc_GetTypeInfo,      c_void_p),
                                                                       cast(self._cfunc_GetIDsOfNames,    c_void_p),
                                                                       cast(self._cfunc_Invoke,           c_void_p),
                                                                       cast(self._cfunc_Rendering,        c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)
        
    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == _COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == _COMEventHandlerImpl._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == ISceneEventCOMHandler._IID_IAgStkGraphicsSceneEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    def _Invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DISPPARAMS), pVarResult:POINTER(VARIANT), pExcepInfo:POINTER(EXCEPINFO), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == ISceneEventCOMHandler._DISPID_Rendering:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._Rendering(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    def _Rendering(self, pThis:PVOID, Sender:VARIANT, Args:PVOID) -> None:
        for callback in self._events["Rendering"]._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender, \
                 agmarshall.AgInterface_event_callback_arg(Args, agcls.AgTypeNameMap["RenderingEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)

                
################################################################################
#          IAgStkGraphicsKmlGraphicsEvents
################################################################################

class _AgStkGraphicsKmlGraphicsEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",        c_void_p),
                 ("IUnknown2",        c_void_p),
                 ("IUnknown3",        c_void_p),
                 ("GetTypeInfoCount", c_void_p),
                 ("GetTypeInfo",      c_void_p),
                 ("GetIDsOfNames",    c_void_p),
                 ("Invoke",           c_void_p),
                 ("DocumentLoaded",   c_void_p)]

class IKmlGraphicsEventCOMHandler(_COMEventHandlerImpl):
    _IID_IAgStkGraphicsKmlGraphicsEvents = GUID.from_registry_format("{0B64622D-307A-4549-9692-7F15F4D9AC94}")
    _DISPID_DocumentLoaded = 27101

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        _COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, IKmlGraphicsEventHandler._IID_IAgStkGraphicsKmlGraphicsEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(ULONG, PVOID)(self._Release)
        else:                                    
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._Release)
        self.__dict__["_cfunc_GetTypeInfoCount"] = CFUNCTYPE(HRESULT, PVOID, POINTER(UINT))(self._GetTypeInfoCount)
        self.__dict__["_cfunc_GetTypeInfo"]      = CFUNCTYPE(HRESULT, PVOID, UINT, LCID, POINTER(PVOID))(self._GetTypeInfo)
        self.__dict__["_cfunc_GetIDsOfNames"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID))(self._GetIDsOfNames)
        self.__dict__["_cfunc_Invoke"]           = CFUNCTYPE(HRESULT, PVOID, DISPID, REFIID, LCID, WORD, POINTER(DISPPARAMS), POINTER(VARIANT), POINTER(EXCEPINFO), POINTER(UINT))(self._Invoke)
        self.__dict__["_cfunc_DocumentLoaded"]   = CFUNCTYPE(HRESULT, PVOID, VARIANT, PVOID)(self._DocumentLoaded)
        
        self.__dict__["_vtable"] = _AgStkGraphicsKmlGraphicsEventsUnkSink( *[cast(self._cfunc_IUnknown1,        c_void_p),
                                                                             cast(self._cfunc_IUnknown2,        c_void_p),
                                                                             cast(self._cfunc_IUnknown3,        c_void_p),
                                                                             cast(self._cfunc_GetTypeInfoCount, c_void_p),
                                                                             cast(self._cfunc_GetTypeInfo,      c_void_p),
                                                                             cast(self._cfunc_GetIDsOfNames,    c_void_p),
                                                                             cast(self._cfunc_Invoke,           c_void_p),
                                                                             cast(self._cfunc_DocumentLoaded,   c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)
        
    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == _COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == _COMEventHandlerImpl._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IKmlGraphicsEventCOMHandler._IID_IAgStkGraphicsKmlGraphicsEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    def _Invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DISPPARAMS), pVarResult:POINTER(VARIANT), pExcepInfo:POINTER(EXCEPINFO), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == IKmlGraphicsEventCOMHandler._DISPID_DocumentLoaded:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._DocumentLoaded(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    def _DocumentLoaded(self, pThis:PVOID, Sender:VARIANT, Args:PVOID) -> None:
        for callback in self._events["DocumentLoaded"]._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender, \
                 agmarshall.AgInterface_event_callback_arg(Args, agcls.AgTypeNameMap["KmlDocumentLoadedEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)


################################################################################
#          IAgStkGraphicsImageCollectionEvents
################################################################################

class _AgStkGraphicsImageCollectionEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",        c_void_p),
                 ("IUnknown2",        c_void_p),
                 ("IUnknown3",        c_void_p),
                 ("GetTypeInfoCount", c_void_p),
                 ("GetTypeInfo",      c_void_p),
                 ("GetIDsOfNames",    c_void_p),
                 ("Invoke",           c_void_p),
                 ("AddComplete",      c_void_p)]

class IImageCollectionEventCOMHandler(_COMEventHandlerImpl):
    _IID_IAgStkGraphicsImageCollectionEvents = GUID.from_registry_format("{150DFFDA-DD8C-4227-9B7D-F813277BCB8E}")
    _DISPID_AddComplete = 13301

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        _COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, IImageCollectionEventHandler._IID_IAgStkGraphicsImageCollectionEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(ULONG, PVOID)(self._Release)
        else:                                    
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._Release)
        self.__dict__["_cfunc_GetTypeInfoCount"] = CFUNCTYPE(HRESULT, PVOID, POINTER(UINT))(self._GetTypeInfoCount)
        self.__dict__["_cfunc_GetTypeInfo"]      = CFUNCTYPE(HRESULT, PVOID, UINT, LCID, POINTER(PVOID))(self._GetTypeInfo)
        self.__dict__["_cfunc_GetIDsOfNames"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID))(self._GetIDsOfNames)
        self.__dict__["_cfunc_Invoke"]           = CFUNCTYPE(HRESULT, PVOID, DISPID, REFIID, LCID, WORD, POINTER(DISPPARAMS), POINTER(VARIANT), POINTER(EXCEPINFO), POINTER(UINT))(self._Invoke)
        self.__dict__["_cfunc_AddComplete"]      = CFUNCTYPE(HRESULT, PVOID, VARIANT, PVOID)(self._AddComplete)
        
        self.__dict__["_vtable"] = _AgStkGraphicsImageCollectionEventsUnkSink( *[cast(self._cfunc_IUnknown1,        c_void_p),
                                                                                 cast(self._cfunc_IUnknown2,        c_void_p),
                                                                                 cast(self._cfunc_IUnknown3,        c_void_p),
                                                                                 cast(self._cfunc_GetTypeInfoCount, c_void_p),
                                                                                 cast(self._cfunc_GetTypeInfo,      c_void_p),
                                                                                 cast(self._cfunc_GetIDsOfNames,    c_void_p),
                                                                                 cast(self._cfunc_Invoke,           c_void_p),
                                                                                 cast(self._cfunc_AddComplete,      c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)
        
    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == _COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == _COMEventHandlerImpl._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IImageCollectionEventCOMHandler._IID_IAgStkGraphicsImageCollectionEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    def _Invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DISPPARAMS), pVarResult:POINTER(VARIANT), pExcepInfo:POINTER(EXCEPINFO), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == IImageCollectionEventCOMHandler._DISPID_AddComplete:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._AddComplete(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    def _AddComplete(self, pThis:PVOID, Sender:VARIANT, Args:PVOID) -> None:
        for callback in self._events["AddComplete"]._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender, \
                 agmarshall.AgInterface_event_callback_arg(Args, agcls.AgTypeNameMap["GlobeImageOverlayAddCompleteEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)

                
################################################################################
#          IAgStkGraphicsTerrainCollectionEvents
################################################################################

class _AgStkGraphicsTerrainCollectionEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",        c_void_p),
                 ("IUnknown2",        c_void_p),
                 ("IUnknown3",        c_void_p),
                 ("GetTypeInfoCount", c_void_p),
                 ("GetTypeInfo",      c_void_p),
                 ("GetIDsOfNames",    c_void_p),
                 ("Invoke",           c_void_p),
                 ("AddComplete",      c_void_p)]

class ITerrainOverlayCollectionEventCOMHandler(_COMEventHandlerImpl):
    _IID_IAgStkGraphicsTerrainCollectionEvents = GUID.from_registry_format("{0744D80B-C88B-4F1D-BF3F-78A5C3AB69BA}")
    _DISPID_AddComplete = 13401

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        _COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, ITerrainOverlayCollectionEventHandler._IID_IAgStkGraphicsTerrainCollectionEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(ULONG, PVOID)(self._Release)
        else:                                    
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._QueryInterface)
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(ULONG, PVOID)(self._AddRef)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._Release)
        self.__dict__["_cfunc_GetTypeInfoCount"] = CFUNCTYPE(HRESULT, PVOID, POINTER(UINT))(self._GetTypeInfoCount)
        self.__dict__["_cfunc_GetTypeInfo"]      = CFUNCTYPE(HRESULT, PVOID, UINT, LCID, POINTER(PVOID))(self._GetTypeInfo)
        self.__dict__["_cfunc_GetIDsOfNames"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID))(self._GetIDsOfNames)
        self.__dict__["_cfunc_Invoke"]           = CFUNCTYPE(HRESULT, PVOID, DISPID, REFIID, LCID, WORD, POINTER(DISPPARAMS), POINTER(VARIANT), POINTER(EXCEPINFO), POINTER(UINT))(self._Invoke)
        self.__dict__["_cfunc_AddComplete"]      = CFUNCTYPE(HRESULT, PVOID, VARIANT, PVOID)(self._AddComplete)
        
        self.__dict__["_vtable"] = _AgStkGraphicsTerrainCollectionEventsUnkSink( *[cast(self._cfunc_IUnknown1,        c_void_p),
                                                                                   cast(self._cfunc_IUnknown2,        c_void_p),
                                                                                   cast(self._cfunc_IUnknown3,        c_void_p),
                                                                                   cast(self._cfunc_GetTypeInfoCount, c_void_p),
                                                                                   cast(self._cfunc_GetTypeInfo,      c_void_p),
                                                                                   cast(self._cfunc_GetIDsOfNames,    c_void_p),
                                                                                   cast(self._cfunc_Invoke,           c_void_p),
                                                                                   cast(self._cfunc_AddComplete,      c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)
        
    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == _COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == _COMEventHandlerImpl._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == ITerrainOverlayCollectionEventCOMHandler._IID_IAgStkGraphicsTerrainCollectionEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    def _Invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DISPPARAMS), pVarResult:POINTER(VARIANT), pExcepInfo:POINTER(EXCEPINFO), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == ITerrainOverlayCollectionEventCOMHandler._DISPID_AddComplete:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._AddComplete(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    def _AddComplete(self, pThis:PVOID, Sender:VARIANT, Args:PVOID) -> None:
        for callback in self._events["AddComplete"]._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender, \
                 agmarshall.AgInterface_event_callback_arg(Args, agcls.AgTypeNameMap["TerrainOverlayAddCompleteEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################