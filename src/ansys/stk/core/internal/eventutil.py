################################################################################
#          Copyright 2020-2021, Analytical Graphics, Inc.
################################################################################

__all__ = [ "IAgStkObjectRootEventHandler", 
            "IAgSTKXApplicationEventHandler", 
            "IAgUiAx2DCntrlEventHandler", 
            "IAgUiAxVOCntrlEventHandler",
            "IAgStkGraphicsSceneEventHandler",
            "IAgStkGraphicsKmlGraphicsEventHandler",
            "IAgStkGraphicsImageCollectionEventHandler",
            "IAgStkGraphicsTerrainCollectionEventHandler"]

import os
import typing
from ctypes import CFUNCTYPE, POINTER, c_void_p, cast, addressof, sizeof, Structure

import agi.stk12.internal.marshall     as agmarshall
import agi.stk12.internal.coclassutil  as agcls
from   agi.stk12.internal.comutil      import *
from   agi.stk12.utilities.exceptions  import *

invalid_use_exception = STKEventsAPIError("Use operator += to register an event callback or operator -= to unregister the callback.")

class _EventSubscriptionManagerImpl(object):
    def __init__(self):
        self._next_id = 0
        self._handlers = dict()
        
    def Subscribe(self, handler) -> int:
        self._next_id = self._next_id + 1
        self._handlers[self._next_id] = handler
        handler._SubscribeImpl()
        return self._next_id
        
    def Unsubscribe(self, id:int):
        if id in self._handlers:
            self._handlers[id]._UnsubscribeImpl()
            del(self._handlers[id])
        
    def UnsubscribeAll(self):
        ids = [id for id in self._handlers]
        for id in ids:
            self.Unsubscribe(id)
            
EventSubscriptionManager = _EventSubscriptionManagerImpl()

class STKEventSubscriber(object):
    def __init__(self, pUnk, pUnkSink, iid):
        self.__dict__["_connection_id"] = None
        self.__dict__["_event_manager_id"] = None
        self.__dict__["_base_pUnkSink"] = pUnkSink
        self.__dict__["_cpc"] = agcls.IConnectionPointContainer(IUnknown(pUnk))
        self.__dict__["_cp"] = self._cpc.FindConnectionPoint(iid)
        self.Subscribe()
        
    def __del__(self):
        self.Unsubscribe()
        del(self._cp)
        del(self._cpc)
    
    def Subscribe(self):
        """Use to re-subscribe to events after calling Unsubscribe.  This class is initialized as subscribed when returned from IAgStkObjectRoot.Subscribe()."""
        if self._event_manager_id is None:
            self.__dict__["_event_manager_id"] = EventSubscriptionManager.Subscribe(self)
            
    def _SubscribeImpl(self):
        """Private method, called by EventSubscriptionManager"""
        if self._connection_id is None:
            self.__dict__["_connection_id"] = self._cp.Advise(addressof(self._base_pUnkSink))
        
    def Unsubscribe(self):
        """Unsubscribe from events."""
        if self._event_manager_id is not None:
            EventSubscriptionManager.Unsubscribe(self._event_manager_id)
            self.__dict__["_event_manager_id"] = None
            
    def _UnsubscribeImpl(self):
        """Private method, called by EventSubscriptionManager"""
        if self._connection_id is not None:
            self._cp.Unadvise(self._connection_id)
            self.__dict__["_connection_id"] = None
    
class STKEventHandlerBase(object):
    _IID_IUnknown  = GUID(IUnknown._guid)
    _IID_IDispatch = GUID("{00020400-0000-0000-C000-000000000046}")
    
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
        
class _STKEvent(object):
    def __init__(self):
        self.__dict__["_callbacks"] = list()
        
    def __eq__(self, other):
        raise invalid_use_exception
        
    def __setattr__(self, attrname, value):
        raise invalid_use_exception
    
    def __iadd__(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)
        return self
            
    def __isub__(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)
        return self
    
    def _safe_assign(self, rhs):
        if type(rhs)==_STKEvent:
            self.__dict__["_callbacks"] = rhs._callbacks.copy()
        else:
            raise invalid_use_exception
        
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
        
class IAgStkObjectRootEventHandler(STKEventSubscriber, STKEventHandlerBase):
    _IID_IAgStkObjectRootEvents     = GUID("{4A25888C-BF0A-4B79-816B-2623D16042B0}")
    _IID_IAgStkObjectRootRawEvents  = GUID("{A381FC71-ACBF-4034-B732-2A36B0CFA2E4}")
    _IID_IAgStkObjectRootRawEvents2 = GUID("{F607E46E-A49F-4B9B-BE24-F29F63709FB0}")

    def __init__(self, pUnk):
        STKEventHandlerBase.__init__(self)
        self._init_vtable1()
        self._init_vtable2()
        self.__dict__["_OnScenarioNewEvent"]              = _STKEvent()
        self.__dict__["_OnScenarioLoadEvent"]             = _STKEvent()
        self.__dict__["_OnScenarioCloseEvent"]            = _STKEvent()
        self.__dict__["_OnScenarioSaveEvent"]             = _STKEvent()
        self.__dict__["_OnLogMessageEvent"]               = _STKEvent()
        self.__dict__["_OnAnimUpdateEvent"]               = _STKEvent()
        self.__dict__["_OnStkObjectAddedEvent"]           = _STKEvent()
        self.__dict__["_OnStkObjectDeletedEvent"]         = _STKEvent()
        self.__dict__["_OnStkObjectRenamedEvent"]         = _STKEvent()
        self.__dict__["_OnAnimationPlaybackEvent"]        = _STKEvent()
        self.__dict__["_OnAnimationRewindEvent"]          = _STKEvent()
        self.__dict__["_OnAnimationPauseEvent"]           = _STKEvent()
        self.__dict__["_OnScenarioBeforeSaveEvent"]       = _STKEvent()
        self.__dict__["_OnAnimationStepEvent"]            = _STKEvent()
        self.__dict__["_OnAnimationStepBackEvent"]        = _STKEvent()
        self.__dict__["_OnAnimationSlowerEvent"]          = _STKEvent()
        self.__dict__["_OnAnimationFasterEvent"]          = _STKEvent()
        self.__dict__["_OnPercentCompleteUpdateEvent"]    = _STKEvent()
        self.__dict__["_OnPercentCompleteEndEvent"]       = _STKEvent()
        self.__dict__["_OnPercentCompleteBeginEvent"]     = _STKEvent()
        self.__dict__["_OnStkObjectChangedEvent"]         = _STKEvent()
        self.__dict__["_OnScenarioBeforeCloseEvent"]      = _STKEvent()
        self.__dict__["_OnStkObjectPreDeleteEvent"]       = _STKEvent()
        self.__dict__["_OnStkObjectStart3dEditingEvent"]  = _STKEvent()
        self.__dict__["_OnStkObjectStop3dEditingEvent"]   = _STKEvent()
        self.__dict__["_OnStkObjectApply3dEditingEvent"]  = _STKEvent()
        self.__dict__["_OnStkObjectCancel3dEditingEvent"] = _STKEvent()
        self.__dict__["_OnStkObjectPreCutEvent"]          = _STKEvent()
        self.__dict__["_OnStkObjectCopyEvent"]            = _STKEvent()
        self.__dict__["_OnStkObjectPasteEvent"]           = _STKEvent()
        STKEventSubscriber.__init__(self, pUnk, self._pUnkSink1, IAgStkObjectRootEventHandler._IID_IAgStkObjectRootEvents)
        
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
                
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IAgStkObjectRootEventHandler.__dict__ and type(IAgStkObjectRootEventHandler.__dict__[attrname]) == property:
            IAgStkObjectRootEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in IAgStkObjectRootEvents.")
        
    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == STKEventHandlerBase._IID_IUnknown:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == IAgStkObjectRootEventHandler._IID_IAgStkObjectRootEvents:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == IAgStkObjectRootEventHandler._IID_IAgStkObjectRootRawEvents:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == IAgStkObjectRootEventHandler._IID_IAgStkObjectRootRawEvents2:
            ppvObject[0] = addressof(self._pUnkSink2)
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    @property
    def OnScenarioNew(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioNew(Path:str) -> None]"""
        return self._OnScenarioNewEvent
        
    @OnScenarioNew.setter
    def OnScenarioNew(self, stk_event):
        self._OnScenarioNewEvent._safe_assign(stk_event)
        
    @property
    def OnScenarioLoad(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioLoad(Path:str) -> None]"""
        return self._OnScenarioLoadEvent
        
    @OnScenarioLoad.setter
    def OnScenarioLoad(self, stk_event):
        self._OnScenarioLoadEvent._safe_assign(stk_event)
        
    @property
    def OnScenarioClose(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioClose() -> None]"""
        return self._OnScenarioCloseEvent
        
    @OnScenarioClose.setter
    def OnScenarioClose(self, stk_event):
        self._OnScenarioCloseEvent._safe_assign(stk_event)
        
    @property
    def OnScenarioSave(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioSave(Path:str) -> None]"""
        return self._OnScenarioSaveEvent
        
    @OnScenarioSave.setter
    def OnScenarioSave(self, stk_event):
        self._OnScenarioSaveEvent._safe_assign(stk_event)
        
    @property
    def OnLogMessage(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnLogMessage(message:str, msgType:"AgELogMsgType", errorCode:int, fileName:str, lineNo:int, dispID:"AgELogMsgDispID") -> None]"""
        return self._OnLogMessageEvent
        
    @OnLogMessage.setter
    def OnLogMessage(self, stk_event):
        self._OnLogMessageEvent._safe_assign(stk_event)

    @property
    def OnAnimUpdate(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimUpdate(timeEpSec:float) -> None]"""
        return self._OnAnimUpdateEvent
        
    @OnAnimUpdate.setter
    def OnAnimUpdate(self, stk_event):
        self._OnAnimUpdateEvent._safe_assign(stk_event)
    
    @property
    def OnStkObjectAdded(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectAdded(Sender:typing.Any) -> None]"""
        return self._OnStkObjectAddedEvent
        
    @OnStkObjectAdded.setter
    def OnStkObjectAdded(self, stk_event):
        self._OnStkObjectAddedEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectDeleted(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectDeleted(Sender:typing.Any) -> None]"""
        return self._OnStkObjectDeletedEvent
        
    @OnStkObjectDeleted.setter
    def OnStkObjectDeleted(self, stk_event):
        self._OnStkObjectDeletedEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectRenamed(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectRenamed(Sender:typing.Any, OldPath:str, NewPath:str) -> None]"""
        return self._OnStkObjectRenamedEvent
        
    @OnStkObjectRenamed.setter
    def OnStkObjectRenamed(self, stk_event):
        self._OnStkObjectRenamedEvent._safe_assign(stk_event)
        
    @property
    def OnAnimationPlayback(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationPlayback(CurrentTime:float, eAction:"AgEAnimationActions", eDirection:"AgEAnimationDirections") -> None]"""
        return self._OnAnimationPlaybackEvent
        
    @OnAnimationPlayback.setter
    def OnAnimationPlayback(self, stk_event):
        self._OnAnimationPlaybackEvent._safe_assign(stk_event)
        
    @property
    def OnAnimationRewind(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationRewind() -> None]"""
        return self._OnAnimationRewindEvent
        
    @OnAnimationRewind.setter
    def OnAnimationRewind(self, stk_event):
        self._OnAnimationRewindEvent._safe_assign(stk_event)
        
    @property
    def OnAnimationPause(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationPause(CurrentTime:float) -> None]"""
        return self._OnAnimationPauseEvent
        
    @OnAnimationPause.setter
    def OnAnimationPause(self, stk_event):
        self._OnAnimationPauseEvent._safe_assign(stk_event)
        
    @property
    def OnScenarioBeforeSave(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioBeforeSave(pArgs:"IAgScenarioBeforeSaveEventArgs") -> None]"""
        return self._OnScenarioBeforeSaveEvent
        
    @OnScenarioBeforeSave.setter
    def OnScenarioBeforeSave(self, stk_event):
        self._OnScenarioBeforeSaveEvent._safe_assign(stk_event)
        
    @property
    def OnAnimationStep(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationStep(CurrentTime:float) -> None]"""
        return self._OnAnimationStepEvent
        
    @OnAnimationStep.setter
    def OnAnimationStep(self, stk_event):
        self._OnAnimationStepEvent._safe_assign(stk_event)
        
    @property
    def OnAnimationStepBack(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationStepBack(CurrentTime:float) -> None]"""
        return self._OnAnimationStepBackEvent
        
    @OnAnimationStepBack.setter
    def OnAnimationStepBack(self, stk_event):
        self._OnAnimationStepBackEvent._safe_assign(stk_event)
        
    @property
    def OnAnimationSlower(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationSlower() -> None]"""
        return self._OnAnimationSlowerEvent
        
    @OnAnimationSlower.setter
    def OnAnimationSlower(self, stk_event):
        self._OnAnimationSlowerEvent._safe_assign(stk_event)
        
    @property
    def OnAnimationFaster(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationFaster() -> None]"""
        return self._OnAnimationFasterEvent
        
    @OnAnimationFaster.setter
    def OnAnimationFaster(self, stk_event):
        self._OnAnimationFasterEvent._safe_assign(stk_event)
        
    @property
    def OnPercentCompleteUpdate(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteUpdate(pArgs:"IAgPctCmpltEventArgs") -> None]"""
        return self._OnPercentCompleteUpdateEvent
        
    @OnPercentCompleteUpdate.setter
    def OnPercentCompleteUpdate(self, stk_event):
        self._OnPercentCompleteUpdateEvent._safe_assign(stk_event)
        
    @property
    def OnPercentCompleteEnd(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteEnd() -> None]"""
        return self._OnPercentCompleteEndEvent
        
    @OnPercentCompleteEnd.setter
    def OnPercentCompleteEnd(self, stk_event):
        self._OnPercentCompleteEndEvent._safe_assign(stk_event)
        
    @property
    def OnPercentCompleteBegin(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteBegin() -> None]"""
        return self._OnPercentCompleteBeginEvent
        
    @OnPercentCompleteBegin.setter
    def OnPercentCompleteBegin(self, stk_event):
        self._OnPercentCompleteBeginEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectChanged(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectChanged(pArgs:"IAgStkObjectChangedEventArgs") -> None]"""
        return self._OnStkObjectChangedEvent
        
    @OnStkObjectChanged.setter
    def OnStkObjectChanged(self, stk_event):
        self._OnStkObjectChangedEvent._safe_assign(stk_event)
        
    @property
    def OnScenarioBeforeClose(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioBeforeClose() -> None]"""
        return self._OnScenarioBeforeCloseEvent
        
    @OnScenarioBeforeClose.setter
    def OnScenarioBeforeClose(self, stk_event):
        self._OnScenarioBeforeCloseEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectPreDelete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPreDelete(pArgs:"IAgStkObjectPreDeleteEventArgs") -> None]"""
        return self._OnStkObjectPreDeleteEvent
        
    @OnStkObjectPreDelete.setter
    def OnStkObjectPreDelete(self, stk_event):
        self._OnStkObjectPreDeleteEvent._safe_assign(stk_event)
    
    @property
    def OnStkObjectStart3dEditing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectStart3dEditing(Path:str) -> None]"""
        return self._OnStkObjectStart3dEditingEvent
        
    @OnStkObjectStart3dEditing.setter
    def OnStkObjectStart3dEditing(self, stk_event):
        self._OnStkObjectStart3dEditingEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectStop3dEditing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectStop3dEditing(Path:str) -> None]"""
        return self._OnStkObjectStop3dEditingEvent
        
    @OnStkObjectStop3dEditing.setter
    def OnStkObjectStop3dEditing(self, stk_event):
        self._OnStkObjectStop3dEditingEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectApply3dEditing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectApply3dEditing(Path:str) -> None]"""
        return self._OnStkObjectApply3dEditingEvent
        
    @OnStkObjectApply3dEditing.setter
    def OnStkObjectApply3dEditing(self, stk_event):
        self._OnStkObjectApply3dEditingEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectCancel3dEditing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectCancel3dEditing(Path:str) -> None]"""
        return self._OnStkObjectCancel3dEditingEvent
        
    @OnStkObjectCancel3dEditing.setter
    def OnStkObjectCancel3dEditing(self, stk_event):
        self._OnStkObjectCancel3dEditingEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectPreCut(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPreCut(pArgs:"IAgStkObjectCutCopyPasteEventArgs") -> None]"""
        return self._OnStkObjectPreCutEvent
        
    @OnStkObjectPreCut.setter
    def OnStkObjectPreCut(self, stk_event):
        self._OnStkObjectPreCutEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectCopy(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectCopy(pArgs:"IAgStkObjectCutCopyPasteEventArgs") -> None]"""
        return self._OnStkObjectCopyEvent
        
    @OnStkObjectCopy.setter
    def OnStkObjectCopy(self, stk_event):
        self._OnStkObjectCopyEvent._safe_assign(stk_event)
        
    @property
    def OnStkObjectPaste(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPaste(pArgs:"IAgStkObjectCutCopyPasteEventArgs") -> None]"""
        return self._OnStkObjectPasteEvent
        
    @OnStkObjectPaste.setter
    def OnStkObjectPaste(self, stk_event):
        self._OnStkObjectPasteEvent._safe_assign(stk_event)
    
    def _OnScenarioNew(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnScenarioNewEvent._callbacks:
            callback(path)
                
    def _OnScenarioLoad(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnScenarioLoadEvent._callbacks:
            callback(path)

    def _OnScenarioClose(self, pThis:PVOID) -> None:
        for callback in self._OnScenarioCloseEvent._callbacks:
            callback()

    def _OnScenarioSave(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnScenarioSaveEvent._callbacks:
            callback(path)

    def _OnLogMessage(self, pThis:PVOID, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._OnLogMessageEvent._callbacks:
            callback(message, agcls.AgTypeNameMap["AgELogMsgType"](msgType), errorCode, fileName, lineNo, agcls.AgTypeNameMap["AgELogMsgDispID"](dispID))

    def _OnAnimUpdate(self, pThis:PVOID, timeEpSec:float) -> None:
        for callback in self._OnAnimUpdateEvent._callbacks:
            callback(timeEpSec)

    def _OnStkObjectAdded(self, pThis:PVOID, Sender:VARIANT) -> None:
        for callback in self._OnStkObjectAddedEvent._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender:
                callback(arg_Sender.python_val)
                
    def _OnStkObjectDeleted(self, pThis:PVOID, Sender:VARIANT) -> None:
        for callback in self._OnStkObjectDeletedEvent._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender:
                callback(arg_Sender.python_val)
                
    def _OnStkObjectRenamed(self, pThis:PVOID, Sender:VARIANT, OldPath:str, NewPath:str) -> None:
        for callback in self._OnStkObjectRenamedEvent._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender:
                callback(arg_Sender.python_val, OldPath, NewPath)
                
    def _OnAnimationPlayback(self, pThis:PVOID, CurrentTime:float, eAction:int, eDirection:int) -> None:
        for callback in self._OnAnimationPlaybackEvent._callbacks:
            callback(CurrentTime, agcls.AgTypeNameMap["AgEAnimationActions"](eAction), agcls.AgTypeNameMap["AgEAnimationDirections"](eDirection.python_val))
                
    def _OnAnimationRewind(self, pThis:PVOID) -> None:
        for callback in self._OnAnimationRewindEvent._callbacks:
            callback()
            
    def _OnAnimationPause(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._OnAnimationPauseEvent._callbacks:
            callback(CurrentTime)
                
    def _OnScenarioBeforeSave(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnScenarioBeforeSaveEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgScenarioBeforeSaveEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
                
    def _OnAnimationStep(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._OnAnimationStepEvent._callbacks:
            callback(CurrentTime)
                
    def _OnAnimationStepBack(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._OnAnimationStepBackEvent._callbacks:
            callback(CurrentTime)
                
    def _OnAnimationSlower(self, pThis:PVOID) -> None:
        for callback in self._OnAnimationSlowerEvent._callbacks:
            callback()
            
    def _OnAnimationFaster(self, pThis:PVOID) -> None:
        for callback in self._OnAnimationFasterEvent._callbacks:
            callback()
            
    def _OnPercentCompleteUpdate(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnPercentCompleteUpdateEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgPctCmpltEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
                
    def _OnPercentCompleteEnd(self, pThis:PVOID) -> None:
        for callback in self._OnPercentCompleteEndEvent._callbacks:
            callback()
            
    def _OnPercentCompleteBegin(self, pThis:PVOID) -> None:
        for callback in self._OnPercentCompleteBeginEvent._callbacks:
            callback()
            
    def _OnStkObjectChanged(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnStkObjectChangedEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgStkObjectChangedEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
                
    def _OnScenarioBeforeClose(self, pThis:PVOID) -> None:
        for callback in self._OnScenarioBeforeCloseEvent._callbacks:
            callback()
            
    def _OnStkObjectPreDelete(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnStkObjectPreDeleteEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgStkObjectPreDeleteEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
                
    def _OnStkObjectStart3dEditing(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnStkObjectStart3dEditingEvent._callbacks:
            callback(path)
            
    def _OnStkObjectStop3dEditing(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnStkObjectStop3dEditingEvent._callbacks:
            callback(path)
            
    def _OnStkObjectApply3dEditing(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnStkObjectApply3dEditingEvent._callbacks:
            callback(path)
            
    def _OnStkObjectCancel3dEditing(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnStkObjectCancel3dEditingEvent._callbacks:
            callback(path)
            
    def _OnStkObjectPreCut(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnStkObjectPreCutEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgStkObjectCutCopyPasteEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
            
    def _OnStkObjectCopy(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnStkObjectCopyEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgStkObjectCutCopyPasteEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
            
    def _OnStkObjectPaste(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnStkObjectPasteEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgStkObjectCutCopyPasteEventArgs"]) as arg_pArgs:
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
        
class IAgSTKXApplicationEventHandler(STKEventSubscriber, STKEventHandlerBase):
    _IID_IAgSTKXApplicationRawEvents = GUID("{78C74BAF-7845-40BA-9EBE-C10FD081BC60}")
    _IID_IAgSTKXApplicationEvents    = GUID("{3787DAB9-9A91-414B-B4EF-2339E0FBA96C}")

    def __init__(self, pUnk):
        STKEventHandlerBase.__init__(self)
        self._init_vtable()
        self.__dict__["_OnScenarioNewEvent"]                = _STKEvent()
        self.__dict__["_OnScenarioLoadEvent"]               = _STKEvent()
        self.__dict__["_OnScenarioCloseEvent"]              = _STKEvent()
        self.__dict__["_OnScenarioSaveEvent"]               = _STKEvent()
        self.__dict__["_OnLogMessageEvent"]                 = _STKEvent()
        self.__dict__["_OnAnimUpdateEvent"]                 = _STKEvent()
        self.__dict__["_OnNewGlobeCtrlRequestEvent"]        = _STKEvent()
        self.__dict__["_OnNewMapCtrlRequestEvent"]          = _STKEvent()
        self.__dict__["_OnBeforeNewScenarioEvent"]          = _STKEvent()
        self.__dict__["_OnBeforeLoadScenarioEvent"]         = _STKEvent()
        self.__dict__["_OnBeginScenarioCloseEvent"]         = _STKEvent()
        self.__dict__["_OnNewGfxAnalysisCtrlRequestEvent"]  = _STKEvent()
        self.__dict__["_OnSSLCertificateServerErrorEvent"]  = _STKEvent()
        self.__dict__["_OnConControlQuitReceivedEvent"]     = _STKEvent()
        STKEventSubscriber.__init__(self, pUnk, self._pUnkSink, IAgSTKXApplicationEventHandler._IID_IAgSTKXApplicationEvents)
        
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
                
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IAgSTKXApplicationEventHandler.__dict__ and type(IAgSTKXApplicationEventHandler.__dict__[attrname]) == property:
            IAgSTKXApplicationEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in IAgSTKXApplicationEvents.")
        
    def _QueryInterface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == STKEventHandlerBase._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgSTKXApplicationEventHandler._IID_IAgSTKXApplicationRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgSTKXApplicationEventHandler._IID_IAgSTKXApplicationEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
        
    @property
    def OnScenarioNew(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioNew(Path:str) -> None]"""
        return self._OnScenarioNewEvent
        
    @OnScenarioNew.setter
    def OnScenarioNew(self, stk_event):
        self._OnScenarioNewEvent._safe_assign(stk_event)
        
    @property
    def OnScenarioLoad(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioLoad(Path:str) -> None]"""
        return self._OnScenarioLoadEvent
        
    @OnScenarioLoad.setter
    def OnScenarioLoad(self, stk_event):
        self._OnScenarioLoadEvent._safe_assign(stk_event)
        
    @property
    def OnScenarioClose(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioClose() -> None]"""
        return self._OnScenarioCloseEvent
        
    @OnScenarioClose.setter
    def OnScenarioClose(self, stk_event):
        self._OnScenarioCloseEvent._safe_assign(stk_event)
        
    @property
    def OnScenarioSave(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioSave(Path:str) -> None]"""
        return self._OnScenarioSaveEvent
        
    @OnScenarioSave.setter
    def OnScenarioSave(self, stk_event):
        self._OnScenarioSaveEvent._safe_assign(stk_event)
        
    @property
    def OnLogMessage(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnLogMessage(message:str, msgType:"AgELogMsgType", errorCode:int, fileName:str, lineNo:int, dispID:"AgELogMsgDispID") -> None]"""
        return self._OnLogMessageEvent
        
    @OnLogMessage.setter
    def OnLogMessage(self, stk_event):
        self._OnLogMessageEvent._safe_assign(stk_event)

    @property
    def OnAnimUpdate(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimUpdate(timeEpSec:float) -> None]"""
        return self._OnAnimUpdateEvent
        
    @OnAnimUpdate.setter
    def OnAnimUpdate(self, stk_event):
        self._OnAnimUpdateEvent._safe_assign(stk_event)
        
    @property
    def OnNewGlobeCtrlRequest(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewGlobeCtrlRequest(SceneID:int) -> None]"""
        return self._OnNewGlobeCtrlRequestEvent
        
    @OnNewGlobeCtrlRequest.setter
    def OnNewGlobeCtrlRequest(self, stk_event):
        self._OnNewGlobeCtrlRequestEvent._safe_assign(stk_event)
    
    @property
    def OnNewMapCtrlRequest(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewMapCtrlRequest(WinID:int) -> None]"""
        return self._OnNewMapCtrlRequestEvent
        
    @OnNewMapCtrlRequest.setter
    def OnNewMapCtrlRequest(self, stk_event):
        self._OnNewMapCtrlRequestEvent._safe_assign(stk_event)
        
    @property
    def OnBeforeNewScenario(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeforeNewScenario(Scenario:str) -> None]"""
        return self._OnBeforeNewScenarioEvent
        
    @OnBeforeNewScenario.setter
    def OnBeforeNewScenario(self, stk_event):
        self._OnBeforeNewScenarioEvent._safe_assign(stk_event)
        
    @property
    def OnBeforeLoadScenario(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeforeLoadScenario(Scenario:str) -> None]"""
        return self._OnBeforeLoadScenarioEvent
        
    @OnBeforeLoadScenario.setter
    def OnBeforeLoadScenario(self, stk_event):
        self._OnBeforeLoadScenarioEvent._safe_assign(stk_event)
        
    @property
    def OnBeginScenarioClose(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeginScenarioClose() -> None]"""
        return self._OnBeginScenarioCloseEvent
        
    @OnBeginScenarioClose.setter
    def OnBeginScenarioClose(self, stk_event):
        self._OnBeginScenarioCloseEvent._safe_assign(stk_event)
    
    @property
    def OnNewGfxAnalysisCtrlRequest(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewGfxAnalysisCtrlRequest(SceneID:int, GfxAnalysisMode:"AgEGfxAnalysisMode") -> None]"""
        return self._OnNewGfxAnalysisCtrlRequestEvent
        
    @OnNewGfxAnalysisCtrlRequest.setter
    def OnNewGfxAnalysisCtrlRequest(self, stk_event):
        self._OnNewGfxAnalysisCtrlRequestEvent._safe_assign(stk_event)
    
    @property
    def OnSSLCertificateServerError(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnSSLCertificateServerError(pArgs:"IAgSTKXSSLCertificateErrorEventArgs") -> None]"""
        return self._OnSSLCertificateServerErrorEvent
        
    @OnSSLCertificateServerError.setter
    def OnSSLCertificateServerError(self, stk_event):
        self._OnSSLCertificateServerErrorEvent._safe_assign(stk_event)
        
    @property
    def OnConControlQuitReceived(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnConControlQuitReceived(pArgs:"IAgSTKXConControlQuitReceivedEventArgs") -> None]"""
        return self._OnConControlQuitReceivedEvent
        
    @OnConControlQuitReceived.setter
    def OnConControlQuitReceived(self, stk_event):
        self._OnConControlQuitReceivedEvent._safe_assign(stk_event)
    
    def _OnScenarioNew(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnScenarioNewEvent._callbacks:
            callback(path)
                
    def _OnScenarioLoad(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnScenarioLoadEvent._callbacks:
            callback(path)

    def _OnScenarioClose(self, pThis:PVOID) -> None:
        for callback in self._OnScenarioCloseEvent._callbacks:
            callback()

    def _OnScenarioSave(self, pThis:PVOID, path:str) -> None:
        for callback in self._OnScenarioSaveEvent._callbacks:
            callback(path)

    def _OnLogMessage(self, pThis:PVOID, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._OnLogMessageEvent._callbacks:
            callback(message, agcls.AgTypeNameMap["AgELogMsgType"](msgType), errorCode, fileName, lineNo, agcls.AgTypeNameMap["AgELogMsgDispID"](dispID))

    def _OnAnimUpdate(self, pThis:PVOID, timeEpSec:float) -> int:
        for callback in self._OnAnimUpdateEvent._callbacks:
            callback(timeEpSec)
        return S_OK

    def _OnNewGlobeCtrlRequest(self, pThis:PVOID, SceneID:int) -> None:
        for callback in self._OnNewGlobeCtrlRequestEvent._callbacks:
            callback(SceneID)
    
    def _OnNewMapCtrlRequest(self, pThis:PVOID, WinID:int) -> None:
        for callback in self._OnNewMapCtrlRequestEvent._callbacks:
            callback(WinID)
        
    def _OnBeforeNewScenario(self, pThis:PVOID, Scenario:str) -> None:
        for callback in self._OnBeforeNewScenarioEvent._callbacks:
            callback(Scenario)
        
    def _OnBeforeLoadScenario(self, pThis:PVOID, Scenario:str) -> None:
        for callback in self._OnBeforeLoadScenarioEvent._callbacks:
            callback(Scenario)
        
    def _OnBeginScenarioClose(self, pThis:PVOID) -> None:
        for callback in self._OnBeginScenarioCloseEvent._callbacks:
            callback()
    
    def _OnNewGfxAnalysisCtrlRequest(self, pThis:PVOID, SceneID:int, GfxAnalysisMode:int) -> None:
        for callback in self._OnNewGfxAnalysisCtrlRequestEvent._callbacks:
            callback(SceneID, agcls.AgTypeNameMap["AgEGfxAnalysisMode"](GfxAnalysisMode))
    
    def _OnSSLCertificateServerError(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnSSLCertificateServerErrorEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgSTKXSSLCertificateErrorEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)
        
    def _OnConControlQuitReceived(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._OnConControlQuitReceivedEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(pArgs, agcls.AgTypeNameMap["IAgSTKXConControlQuitReceivedEventArgs"]) as arg_pArgs:
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
                 
class IAgUiAxStockEventHandler(STKEventHandlerBase):
    _IID_IAgUiAxStockRawEvents   = GUID("{32A1F220-C90C-4FC6-B2BF-DF06DB89B72E}")

    def __init__(self):
        STKEventHandlerBase.__init__(self)
        self.__dict__["_KeyDownEvent"]      = _STKEvent()
        self.__dict__["_KeyPressEvent"]     = _STKEvent()
        self.__dict__["_KeyUpEvent"]        = _STKEvent()
        self.__dict__["_ClickEvent"]        = _STKEvent()
        self.__dict__["_DblClickEvent"]     = _STKEvent()
        self.__dict__["_MouseDownEvent"]    = _STKEvent()
        self.__dict__["_MouseMoveEvent"]    = _STKEvent()
        self.__dict__["_MouseUpEvent"]      = _STKEvent()
        self.__dict__["_OLEDragDropEvent"]  = _STKEvent()
        self.__dict__["_MouseWheelEvent"]   = _STKEvent()
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
        
    def __setattr__(self, attrname, value):
        if attrname in IAgUiAxStockEventHandler.__dict__ and type(IAgUiAxStockEventHandler.__dict__[attrname]) == property:
            IAgUiAxStockEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in IAgUiAxStockEvents.")
    
    @property
    def KeyDown(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyDown(KeyCode:int, Shift:int) -> None]"""
        return self._KeyDownEvent
        
    @KeyDown.setter
    def KeyDown(self, stk_event):
        self._KeyDownEvent._safe_assign(stk_event)
        
    def _KeyDown(self, pThis:PVOID, KeyCode:POINTER(SHORT), Shift:int) -> int:
        for callback in self._KeyDownEvent._callbacks:
            callback(KeyCode[0], Shift)
        return S_OK

    @property
    def KeyPress(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyPress(KeyAscii:int) -> None]"""
        return self._KeyPressEvent
        
    @KeyPress.setter
    def KeyPress(self, stk_event):
        self._KeyPressEvent._safe_assign(stk_event)
        
    def _KeyPress(self, pThis:PVOID, KeyAscii:POINTER(SHORT)) -> int:
        for callback in self._KeyPressEvent._callbacks:
            callback(KeyAscii[0])
        return S_OK
        
    @property
    def KeyUp(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyUp(KeyCode:int, Shift:int) -> None]"""
        return self._KeyUpEvent
        
    @KeyUp.setter
    def KeyUp(self, stk_event):
        self._KeyUpEvent._safe_assign(stk_event)
        
    def _KeyUp(self, pThis:PVOID, KeyCode:POINTER(SHORT), Shift:int) -> int:
        for callback in self._KeyUpEvent._callbacks:
            callback(KeyCode[0], Shift)
        return S_OK
        
    @property
    def Click(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [Click() -> None]"""
        return self._ClickEvent
        
    @Click.setter
    def Click(self, stk_event):
        self._ClickEvent._safe_assign(stk_event)
        
    def _Click(self, pThis:PVOID) -> int:
        for callback in self._ClickEvent._callbacks:
            callback()
        return S_OK
        
    @property
    def DblClick(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [DblClick() -> None]"""
        return self._DblClickEvent
        
    @DblClick.setter
    def DblClick(self, stk_event):
        self._DblClickEvent._safe_assign(stk_event)
        
    def _DblClick(self, pThis:PVOID) -> int:
        for callback in self._DblClickEvent._callbacks:
            callback()
        return S_OK
                
    @property
    def MouseDown(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseDown(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._MouseDownEvent
        
    @MouseDown.setter
    def MouseDown(self, stk_event):
        self._MouseDownEvent._safe_assign(stk_event)
        
    def _MouseDown(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._MouseDownEvent._callbacks:
            callback(KeyCode, Shift, X, Y)
        return S_OK

    @property
    def MouseMove(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseMove(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._MouseMoveEvent
        
    @MouseMove.setter
    def MouseMove(self, stk_event):
        self._MouseMoveEvent._safe_assign(stk_event)
        
    def _MouseMove(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._MouseMoveEvent._callbacks:
            callback(KeyCode, Shift, X, Y)
        return S_OK

    @property
    def MouseUp(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseUp(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._MouseUpEvent
        
    @MouseUp.setter
    def MouseUp(self, stk_event):
        self._MouseUpEvent._safe_assign(stk_event)
        
    def _MouseUp(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._MouseUpEvent._callbacks:
            callback(KeyCode, Shift, X, Y)
        return S_OK
        
    @property
    def OLEDragDrop(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OLEDragDrop(Data:"IAgDataObject", Effect:int, Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._OLEDragDropEvent
        
    @OLEDragDrop.setter
    def OLEDragDrop(self, stk_event):
        self._OLEDragDropEvent._safe_assign(stk_event)
        
    def _OLEDragDrop(self, pThis:PVOID, Data:PVOID, Effect:int, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._OLEDragDropEvent._callbacks:
            with agmarshall.AgInterface_event_callback_arg(Data, agcls.AgTypeNameMap["IAgDataObject"]) as arg_Data:
                callback(arg_Data.python_val, Effect, KeyCode, Shift, X, Y)
        return S_OK
        
    @property
    def MouseWheel(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseWheel(Button:int, Shift:int, Delta:int, X:int, Y:int) -> None]"""
        return self._MouseWheelEvent
        
    @MouseWheel.setter
    def MouseWheel(self, stk_event):
        self._MouseWheelEvent._safe_assign(stk_event)
        
    def _MouseWheel(self, pThis:PVOID, Button:int, Shift:int, Delta:int, X:int, Y:int) -> int:
        for callback in self._MouseWheelEvent._callbacks:
            callback(KeyCode, Shift, Delta, X, Y)
        return S_OK
        
        
class IAgUiAx2DCntrlEventHandler(STKEventSubscriber, IAgUiAxStockEventHandler):
    _IID_IAgUiAx2DCntrlEvents    = GUID("{DA0E1628-101E-4A18-B922-B4189E31AD7E}")

    def __init__(self, pUnk):
        IAgUiAxStockEventHandler.__init__(self)
        self._init_vtable()
        STKEventSubscriber.__init__(self, pUnk, self._pUnkSink, IAgUiAx2DCntrlEventHandler._IID_IAgUiAx2DCntrlEvents)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        try:
            IAgUiAxStockEventHandler.__setattr__(self, attrname, value)
        except:
            if attrname in IAgUiAx2DCntrlEventHandler.__dict__ and type(IAgUiAx2DCntrlEventHandler.__dict__[attrname]) == property:
                IAgUiAx2DCntrlEventHandler.__dict__[attrname].__set__(self, value)
            else:
                raise STKAttributeError(attrname + " is not a recognized event in IAgUiAx2DCntrlEvents.")
        
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
        if iid == STKEventHandlerBase._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgUiAxStockEventHandler._IID_IAgUiAxStockRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgUiAx2DCntrlEventHandler._IID_IAgUiAx2DCntrlEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
            
            
class IAgUiAxVOCntrlEventHandler(STKEventSubscriber, IAgUiAxStockEventHandler):
    _IID_IAgUiAxVOCntrlRawEvents = GUID("{1ADE7AE0-B431-4ED4-8494-335EBB14007C}")
    _IID_IAgUiAxVOCntrlEvents    = GUID("{C46F1BA0-22E4-432B-9259-C6DEF33FE2B2}")

    def __init__(self, pUnk):
        IAgUiAxStockEventHandler.__init__(self)
        self._init_vtable()
        self.__dict__["_OnObjectEditingStartEvent"]     = _STKEvent()
        self.__dict__["_OnObjectEditingApplyEvent"]     = _STKEvent()
        self.__dict__["_OnObjectEditingCancelEvent"]    = _STKEvent()
        self.__dict__["_OnObjectEditingStopEvent"]      = _STKEvent()
        STKEventSubscriber.__init__(self, pUnk, self._pUnkSink, IAgUiAxVOCntrlEventHandler._IID_IAgUiAxVOCntrlEvents)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        try:
            IAgUiAxStockEventHandler.__setattr__(self, attrname, value)
        except:
            if attrname in IAgUiAxVOCntrlEventHandler.__dict__ and type(IAgUiAxVOCntrlEventHandler.__dict__[attrname]) == property:
                IAgUiAxVOCntrlEventHandler.__dict__[attrname].__set__(self, value)
            else:
                raise STKAttributeError(attrname + " is not a recognized event in IAgUiAxVOCntrlEvents.")
        
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
        if iid == STKEventHandlerBase._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgUiAxStockEventHandler._IID_IAgUiAxStockRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgUiAxVOCntrlEventHandler._IID_IAgUiAxVOCntrlRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgUiAxVOCntrlEventHandler._IID_IAgUiAxVOCntrlEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    @property
    def OnObjectEditingStart(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingStart(Path:str) -> None]"""
        return self._OnObjectEditingStartEvent
        
    @OnObjectEditingStart.setter
    def OnObjectEditingStart(self, stk_event):
        self._OnObjectEditingStartEvent._safe_assign(stk_event)
        
    def _OnObjectEditingStart(self, pThis:PVOID, Path:str) -> int:
        for callback in self._OnObjectEditingStartEvent._callbacks:
            callback(Path)
        return S_OK
        
    @property
    def OnObjectEditingApply(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingApply(Path:str) -> None]"""
        return self._OnObjectEditingApplyEvent
        
    @OnObjectEditingApply.setter
    def OnObjectEditingApply(self, stk_event):
        self._OnObjectEditingApplyEvent._safe_assign(stk_event)
        
    def _OnObjectEditingApply(self, pThis:PVOID, Path:str) -> int:
        for callback in self._OnObjectEditingApplyEvent._callbacks:
            callback(Path)
        return S_OK
        
    @property
    def OnObjectEditingCancel(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingCancel(Path:str) -> None]"""
        return self._OnObjectEditingCancelEvent
        
    @OnObjectEditingCancel.setter
    def OnObjectEditingCancel(self, stk_event):
        self._OnObjectEditingCancelEvent._safe_assign(stk_event)
        
    def _OnObjectEditingCancel(self, pThis:PVOID, Path:str) -> int:
        for callback in self._OnObjectEditingCancelEvent._callbacks:
            callback(Path)
        return S_OK
        
    @property
    def OnObjectEditingStop(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingStop(Path:str) -> None]"""
        return self._OnObjectEditingStopEvent
        
    @OnObjectEditingStop.setter
    def OnObjectEditingStop(self, stk_event):
        self._OnObjectEditingStopEvent._safe_assign(stk_event)
        
    def _OnObjectEditingStop(self, pThis:PVOID, Path:str) -> int:
        for callback in self._OnObjectEditingStopEvent._callbacks:
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
                 
class IAgStkGraphicsSceneEventHandler(STKEventSubscriber, STKEventHandlerBase):
    _IID_IAgStkGraphicsSceneEvents = GUID("{FACA0112-848C-415D-B38C-0ED3F121D906}")
    _DISPID_Rendering = 13901

    def __init__(self, pUnk):
        STKEventHandlerBase.__init__(self)
        self._init_vtable()
        self.__dict__["_RenderingEvent"] = _STKEvent()
        STKEventSubscriber.__init__(self, pUnk, self._pUnkSink, IAgStkGraphicsSceneEventHandler._IID_IAgStkGraphicsSceneEvents)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IAgStkGraphicsSceneEventHandler.__dict__ and type(IAgStkGraphicsSceneEventHandler.__dict__[attrname]) == property:
            IAgStkGraphicsSceneEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in IAgStkGraphicsSceneEvents.")
        
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
        if iid == STKEventHandlerBase._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == STKEventHandlerBase._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgStkGraphicsSceneEventHandler._IID_IAgStkGraphicsSceneEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    def _Invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DISPPARAMS), pVarResult:POINTER(VARIANT), pExcepInfo:POINTER(EXCEPINFO), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == IAgStkGraphicsSceneEventHandler._DISPID_Rendering:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._Rendering(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE
          
    @property
    def Rendering(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [Rendering(Sender:typing.Any, Args:"IAgStkGraphicsRenderingEventArgs") -> None]"""
        return self._RenderingEvent
        
    @Rendering.setter
    def Rendering(self, stk_event):
        self._RenderingEvent._safe_assign(stk_event)
        
    def _Rendering(self, pThis:PVOID, Sender:VARIANT, Args:PVOID) -> None:
        for callback in self._RenderingEvent._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender, \
                 agmarshall.AgInterface_event_callback_arg(Args, agcls.AgTypeNameMap["IAgStkGraphicsRenderingEventArgs"]) as arg_Args:
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
                 
class IAgStkGraphicsKmlGraphicsEventHandler(STKEventSubscriber, STKEventHandlerBase):
    _IID_IAgStkGraphicsKmlGraphicsEvents = GUID("{0B64622D-307A-4549-9692-7F15F4D9AC94}")
    _DISPID_DocumentLoaded = 27101

    def __init__(self, pUnk):
        STKEventHandlerBase.__init__(self)
        self._init_vtable()
        self.__dict__["_DocumentLoadedEvent"] = _STKEvent()
        STKEventSubscriber.__init__(self, pUnk, self._pUnkSink, IAgStkGraphicsKmlGraphicsEventHandler._IID_IAgStkGraphicsKmlGraphicsEvents)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IAgStkGraphicsKmlGraphicsEventHandler.__dict__ and type(IAgStkGraphicsKmlGraphicsEventHandler.__dict__[attrname]) == property:
            IAgStkGraphicsKmlGraphicsEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in IAgStkGraphicsKmlGraphicsEvents.")
        
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
        if iid == STKEventHandlerBase._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == STKEventHandlerBase._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgStkGraphicsKmlGraphicsEventHandler._IID_IAgStkGraphicsKmlGraphicsEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    def _Invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DISPPARAMS), pVarResult:POINTER(VARIANT), pExcepInfo:POINTER(EXCEPINFO), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == IAgStkGraphicsKmlGraphicsEventHandler._DISPID_DocumentLoaded:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._DocumentLoaded(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    @property
    def DocumentLoaded(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [DocumentLoaded(Sender:typing.Any, Args:"IAgStkGraphicsKmlDocumentLoadedEventArgs") -> None]"""
        return self._DocumentLoadedEvent
        
    @DocumentLoaded.setter
    def DocumentLoaded(self, stk_event):
        self._DocumentLoadedEvent._safe_assign(stk_event)
        
    def _DocumentLoaded(self, pThis:PVOID, Sender:VARIANT, Args:PVOID) -> None:
        for callback in self._DocumentLoadedEvent._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender, \
                 agmarshall.AgInterface_event_callback_arg(Args, agcls.AgTypeNameMap["IAgStkGraphicsKmlDocumentLoadedEventArgs"]) as arg_Args:
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
                 
class IAgStkGraphicsImageCollectionEventHandler(STKEventSubscriber, STKEventHandlerBase):
    _IID_IAgStkGraphicsImageCollectionEvents = GUID("{150DFFDA-DD8C-4227-9B7D-F813277BCB8E}")
    _DISPID_AddComplete = 13301

    def __init__(self, pUnk):
        STKEventHandlerBase.__init__(self)
        self._init_vtable()
        self.__dict__["_AddCompleteEvent"] = _STKEvent()
        STKEventSubscriber.__init__(self, pUnk, self._pUnkSink, IAgStkGraphicsImageCollectionEventHandler._IID_IAgStkGraphicsImageCollectionEvents)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IAgStkGraphicsImageCollectionEventHandler.__dict__ and type(IAgStkGraphicsImageCollectionEventHandler.__dict__[attrname]) == property:
            IAgStkGraphicsImageCollectionEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in IAgStkGraphicsImageCollectionEvents.")
        
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
        if iid == STKEventHandlerBase._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == STKEventHandlerBase._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgStkGraphicsImageCollectionEventHandler._IID_IAgStkGraphicsImageCollectionEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    def _Invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DISPPARAMS), pVarResult:POINTER(VARIANT), pExcepInfo:POINTER(EXCEPINFO), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == IAgStkGraphicsImageCollectionEventHandler._DISPID_AddComplete:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._AddComplete(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    @property
    def AddComplete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [AddComplete(Sender:typing.Any, Args:"IAgStkGraphicsGlobeImageOverlayAddCompleteEventArgs") -> None]"""
        return self._AddCompleteEvent
        
    @AddComplete.setter
    def AddComplete(self, stk_event):
        self._AddCompleteEvent._safe_assign(stk_event)
        
    def _AddComplete(self, pThis:PVOID, Sender:VARIANT, Args:PVOID) -> None:
        for callback in self._AddCompleteEvent._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender, \
                 agmarshall.AgInterface_event_callback_arg(Args, agcls.AgTypeNameMap["IAgStkGraphicsGlobeImageOverlayAddCompleteEventArgs"]) as arg_Args:
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
                 
class IAgStkGraphicsTerrainCollectionEventHandler(STKEventSubscriber, STKEventHandlerBase):
    _IID_IAgStkGraphicsTerrainCollectionEvents = GUID("{0744D80B-C88B-4F1D-BF3F-78A5C3AB69BA}")
    _DISPID_AddComplete = 13401

    def __init__(self, pUnk):
        STKEventHandlerBase.__init__(self)
        self._init_vtable()
        self.__dict__["_AddCompleteEvent"] = _STKEvent()
        STKEventSubscriber.__init__(self, pUnk, self._pUnkSink, IAgStkGraphicsTerrainCollectionEventHandler._IID_IAgStkGraphicsTerrainCollectionEvents)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IAgStkGraphicsTerrainCollectionEventHandler.__dict__ and type(IAgStkGraphicsTerrainCollectionEventHandler.__dict__[attrname]) == property:
            IAgStkGraphicsTerrainCollectionEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in IAgStkGraphicsTerrainCollectionEvents.")
        
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
        if iid == STKEventHandlerBase._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == STKEventHandlerBase._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IAgStkGraphicsTerrainCollectionEventHandler._IID_IAgStkGraphicsTerrainCollectionEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE
            
    def _Invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DISPPARAMS), pVarResult:POINTER(VARIANT), pExcepInfo:POINTER(EXCEPINFO), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == IAgStkGraphicsTerrainCollectionEventHandler._DISPID_AddComplete:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._AddComplete(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    @property
    def AddComplete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [AddComplete(Sender:typing.Any, Args:"IAgStkGraphicsTerrainOverlayAddCompleteEventArgs") -> None]"""
        return self._AddCompleteEvent
        
    @AddComplete.setter
    def AddComplete(self, stk_event):
        self._AddCompleteEvent._safe_assign(stk_event)
        
    def _AddComplete(self, pThis:PVOID, Sender:VARIANT, Args:PVOID) -> None:
        for callback in self._AddCompleteEvent._callbacks:
            with agmarshall.VARIANT_arg(Sender) as arg_Sender, \
                 agmarshall.AgInterface_event_callback_arg(Args, agcls.AgTypeNameMap["IAgStkGraphicsTerrainOverlayAddCompleteEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)

################################################################################
#          Copyright 2020-2021, Analytical Graphics, Inc.
################################################################################