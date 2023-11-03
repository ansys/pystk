################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################

__all__ = [ "IStkObjectRootEventHandler", 
            "ISTKXApplicationEventHandler", 
            "IUiAxGraphics2DCntrlEventHandler", 
            "IUiAxGraphics3DCntrlEventHandler",
            "ISceneEventHandler",
            "IKmlGraphicsEventHandler",
            "IImageCollectionEventHandler",
            "ITerrainOverlayCollectionEventHandler"]


from .comutil                import IUnknown
from .comevents              import *
from ..utilities.exceptions  import *

try:
    from .grpcutil   import grpc_interface
    from .grpcevents import *
except:
    class grpc_interface(object):
        def __init__(self):
            pass

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
    def __init__(self, impl):
        self.__dict__["_event_manager_id"] = None
        self.__dict__["_impl"] = impl
        self.Subscribe()
        
    def __del__(self):
        self.Unsubscribe()
        del(self._impl)
    
    def Subscribe(self):
        """Use to re-subscribe to events after calling Unsubscribe.  This class is initialized as subscribed when returned from StkObjectRoot.Subscribe()."""
        if self._event_manager_id is None:
            self.__dict__["_event_manager_id"] = EventSubscriptionManager.Subscribe(self)
            
    def _SubscribeImpl(self):
        """Private method, called by EventSubscriptionManager"""
        self._impl.Subscribe()
        
    def Unsubscribe(self):
        """Unsubscribe from events."""
        if self._event_manager_id is not None:
            EventSubscriptionManager.Unsubscribe(self._event_manager_id)
            self.__dict__["_event_manager_id"] = None
            
    def _UnsubscribeImpl(self):
        """Private method, called by EventSubscriptionManager"""
        self._impl.Unsubscribe()
        
class _STKEvent(object):
    def __init__(self):
        self.__dict__["_callbacks"] = list()
        self.__dict__["_iadd_callback"] = None
        self.__dict__["_isub_callback"] = None
        
    def __eq__(self, other):
        raise invalid_use_exception
        
    def __setattr__(self, attrname, value):
        raise invalid_use_exception
    
    def __iadd__(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)
            if self._iadd_callback is not None:
                self._iadd_callback(len(self._callbacks))
        return self
            
    def __isub__(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)
            if self._isub_callback is not None:
                self._isub_callback(len(self._callbacks))
        return self

    def _set_iadd_callback(self, iadd_callback):
        self.__dict__["_iadd_callback"] = iadd_callback

    def _set_isub_callback(self, isub_callback):
        self.__dict__["_isub_callback"] = isub_callback
    
    def _safe_assign(self, rhs):
        if type(rhs)==_STKEvent:
            self.__dict__["_callbacks"] = rhs._callbacks.copy()
        else:
            raise invalid_use_exception
        
################################################################################
#          IAgStkObjectRootEvents
################################################################################
        
class IStkObjectRootEventHandler(STKEventSubscriber):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        self._events["OnScenarioNew"]              = _STKEvent()
        self._events["OnScenarioLoad"]             = _STKEvent()
        self._events["OnScenarioClose"]            = _STKEvent()
        self._events["OnScenarioSave"]             = _STKEvent()
        self._events["OnLogMessage"]               = _STKEvent()
        self._events["OnAnimUpdate"]               = _STKEvent()
        self._events["OnStkObjectAdded"]           = _STKEvent()
        self._events["OnStkObjectDeleted"]         = _STKEvent()
        self._events["OnStkObjectRenamed"]         = _STKEvent()
        self._events["OnAnimationPlayback"]        = _STKEvent()
        self._events["OnAnimationRewind"]          = _STKEvent()
        self._events["OnAnimationPause"]           = _STKEvent()
        self._events["OnScenarioBeforeSave"]       = _STKEvent()
        self._events["OnAnimationStep"]            = _STKEvent()
        self._events["OnAnimationStepBack"]        = _STKEvent()
        self._events["OnAnimationSlower"]          = _STKEvent()
        self._events["OnAnimationFaster"]          = _STKEvent()
        self._events["OnPercentCompleteUpdate"]    = _STKEvent()
        self._events["OnPercentCompleteEnd"]       = _STKEvent()
        self._events["OnPercentCompleteBegin"]     = _STKEvent()
        self._events["OnStkObjectChanged"]         = _STKEvent()
        self._events["OnScenarioBeforeClose"]      = _STKEvent()
        self._events["OnStkObjectPreDelete"]       = _STKEvent()
        self._events["OnStkObjectStart3dEditing"]  = _STKEvent()
        self._events["OnStkObjectStop3dEditing"]   = _STKEvent()
        self._events["OnStkObjectApply3dEditing"]  = _STKEvent()
        self._events["OnStkObjectCancel3dEditing"] = _STKEvent()
        self._events["OnStkObjectPreCut"]          = _STKEvent()
        self._events["OnStkObjectCopy"]            = _STKEvent()
        self._events["OnStkObjectPaste"]           = _STKEvent()
        if type(interface)==IUnknown:
            impl = IStkObjectRootEventCOMHandler(interface, self._events)
        elif type(interface)==grpc_interface:
            impl = IAgStkObjectRootEventGrpcHandler(interface, self._events)
        else:
            raise STKRuntimeError(f"Unexpected type {type(interface)}, cannot create IStkObjectRootEventHandler.")
        STKEventSubscriber.__init__(self, impl)
   
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IStkObjectRootEventHandler.__dict__ and type(IStkObjectRootEventHandler.__dict__[attrname]) == property:
            IStkObjectRootEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in StkObjectRootEvents.")
 
    @property
    def OnScenarioNew(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioNew(Path:str) -> None]"""
        return self._events["OnScenarioNew"]
        
    @OnScenarioNew.setter
    def OnScenarioNew(self, callback):
        self._events["OnScenarioNew"]._safe_assign(callback)
        
    @property
    def OnScenarioLoad(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioLoad(Path:str) -> None]"""
        return self._events["OnScenarioLoad"]
        
    @OnScenarioLoad.setter
    def OnScenarioLoad(self, callback):
        self._events["OnScenarioLoad"]._safe_assign(callback)
        
    @property
    def OnScenarioClose(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioClose() -> None]"""
        return self._events["OnScenarioClose"]
        
    @OnScenarioClose.setter
    def OnScenarioClose(self, callback):
        self._events["OnScenarioClose"]._safe_assign(callback)
        
    @property
    def OnScenarioSave(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioSave(Path:str) -> None]"""
        return self._events["OnScenarioSave"]
        
    @OnScenarioSave.setter
    def OnScenarioSave(self, callback):
        self._events["OnScenarioSave"]._safe_assign(callback)
        
    @property
    def OnLogMessage(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnLogMessage(message:str, msgType:"LOG_MSG_TYPE", errorCode:int, fileName:str, lineNo:int, dispID:"LOG_MSG_DISP_ID") -> None]"""
        return self._events["OnLogMessage"]
        
    @OnLogMessage.setter
    def OnLogMessage(self, callback):
        self._events["OnLogMessage"]._safe_assign(callback)

    @property
    def OnAnimUpdate(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimUpdate(timeEpSec:float) -> None]"""
        return self._events["OnAnimUpdate"]
        
    @OnAnimUpdate.setter
    def OnAnimUpdate(self, callback):
        self._events["OnAnimUpdate"]._safe_assign(callback)
    
    @property
    def OnStkObjectAdded(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectAdded(Sender:typing.Any) -> None]"""
        return self._events["OnStkObjectAdded"]
        
    @OnStkObjectAdded.setter
    def OnStkObjectAdded(self, callback):
        self._events["OnStkObjectAdded"]._safe_assign(callback)
        
    @property
    def OnStkObjectDeleted(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectDeleted(Sender:typing.Any) -> None]"""
        return self._events["OnStkObjectDeleted"]
        
    @OnStkObjectDeleted.setter
    def OnStkObjectDeleted(self, callback):
        self._events["OnStkObjectDeleted"]._safe_assign(callback)
        
    @property
    def OnStkObjectRenamed(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectRenamed(Sender:typing.Any, OldPath:str, NewPath:str) -> None]"""
        return self._events["OnStkObjectRenamed"]
        
    @OnStkObjectRenamed.setter
    def OnStkObjectRenamed(self, callback):
        self._events["OnStkObjectRenamed"]._safe_assign(callback)
        
    @property
    def OnAnimationPlayback(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationPlayback(CurrentTime:float, eAction:"ANIMATION_ACTIONS", eDirection:"ANIMATION_DIRECTIONS") -> None]"""
        return self._events["OnAnimationPlayback"]
        
    @OnAnimationPlayback.setter
    def OnAnimationPlayback(self, callback):
        self._events["OnAnimationPlayback"]._safe_assign(callback)
        
    @property
    def OnAnimationRewind(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationRewind() -> None]"""
        return self._events["OnAnimationRewind"]
        
    @OnAnimationRewind.setter
    def OnAnimationRewind(self, callback):
        self._events["OnAnimationRewind"]._safe_assign(callback)
        
    @property
    def OnAnimationPause(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationPause(CurrentTime:float) -> None]"""
        return self._events["OnAnimationPause"]
        
    @OnAnimationPause.setter
    def OnAnimationPause(self, callback):
        self._events["OnAnimationPause"]._safe_assign(callback)
        
    @property
    def OnScenarioBeforeSave(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioBeforeSave(pArgs:"ScenarioBeforeSaveEventArgs") -> None]"""
        return self._events["OnScenarioBeforeSave"]
        
    @OnScenarioBeforeSave.setter
    def OnScenarioBeforeSave(self, callback):
        self._events["OnScenarioBeforeSave"]._safe_assign(callback)
        
    @property
    def OnAnimationStep(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationStep(CurrentTime:float) -> None]"""
        return self._events["OnAnimationStep"]
        
    @OnAnimationStep.setter
    def OnAnimationStep(self, callback):
        self._events["OnAnimationStep"]._safe_assign(callback)
        
    @property
    def OnAnimationStepBack(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationStepBack(CurrentTime:float) -> None]"""
        return self._events["OnAnimationStepBack"]
        
    @OnAnimationStepBack.setter
    def OnAnimationStepBack(self, callback):
        self._events["OnAnimationStepBack"]._safe_assign(callback)
        
    @property
    def OnAnimationSlower(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationSlower() -> None]"""
        return self._events["OnAnimationSlower"]
        
    @OnAnimationSlower.setter
    def OnAnimationSlower(self, callback):
        self._events["OnAnimationSlower"]._safe_assign(callback)
        
    @property
    def OnAnimationFaster(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationFaster() -> None]"""
        return self._events["OnAnimationFaster"]
        
    @OnAnimationFaster.setter
    def OnAnimationFaster(self, callback):
        self._events["OnAnimationFaster"]._safe_assign(callback)
        
    @property
    def OnPercentCompleteUpdate(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteUpdate(pArgs:"PctCmpltEventArgs") -> None]"""
        return self._events["OnPercentCompleteUpdate"]
        
    @OnPercentCompleteUpdate.setter
    def OnPercentCompleteUpdate(self, callback):
        self._events["OnPercentCompleteUpdate"]._safe_assign(callback)
        
    @property
    def OnPercentCompleteEnd(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteEnd() -> None]"""
        return self._events["OnPercentCompleteEnd"]
        
    @OnPercentCompleteEnd.setter
    def OnPercentCompleteEnd(self, callback):
        self._events["OnPercentCompleteEnd"]._safe_assign(callback)
        
    @property
    def OnPercentCompleteBegin(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteBegin() -> None]"""
        return self._events["OnPercentCompleteBegin"]
        
    @OnPercentCompleteBegin.setter
    def OnPercentCompleteBegin(self, callback):
        self._events["OnPercentCompleteBegin"]._safe_assign(callback)
        
    @property
    def OnStkObjectChanged(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectChanged(pArgs:"StkObjectChangedEventArgs") -> None]"""
        return self._events["OnStkObjectChanged"]
        
    @OnStkObjectChanged.setter
    def OnStkObjectChanged(self, callback):
        self._events["OnStkObjectChanged"]._safe_assign(callback)
        
    @property
    def OnScenarioBeforeClose(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioBeforeClose() -> None]"""
        return self._events["OnScenarioBeforeClose"]
        
    @OnScenarioBeforeClose.setter
    def OnScenarioBeforeClose(self, callback):
        self._events["OnScenarioBeforeClose"]._safe_assign(callback)
        
    @property
    def OnStkObjectPreDelete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPreDelete(pArgs:"StkObjectPreDeleteEventArgs") -> None]"""
        return self._events["OnStkObjectPreDelete"]
        
    @OnStkObjectPreDelete.setter
    def OnStkObjectPreDelete(self, callback):
        self._events["OnStkObjectPreDelete"]._safe_assign(callback)
    
    @property
    def OnStkObjectStart3dEditing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectStart3dEditing(Path:str) -> None]"""
        return self._events["OnStkObjectStart3dEditing"]
        
    @OnStkObjectStart3dEditing.setter
    def OnStkObjectStart3dEditing(self, callback):
        self._events["OnStkObjectStart3dEditing"]._safe_assign(callback)
        
    @property
    def OnStkObjectStop3dEditing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectStop3dEditing(Path:str) -> None]"""
        return self._events["OnStkObjectStop3dEditing"]
        
    @OnStkObjectStop3dEditing.setter
    def OnStkObjectStop3dEditing(self, callback):
        self._events["OnStkObjectStop3dEditing"]._safe_assign(callback)
        
    @property
    def OnStkObjectApply3dEditing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectApply3dEditing(Path:str) -> None]"""
        return self._events["OnStkObjectApply3dEditing"]
        
    @OnStkObjectApply3dEditing.setter
    def OnStkObjectApply3dEditing(self, callback):
        self._events["OnStkObjectApply3dEditing"]._safe_assign(callback)
        
    @property
    def OnStkObjectCancel3dEditing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectCancel3dEditing(Path:str) -> None]"""
        return self._events["OnStkObjectCancel3dEditing"]
        
    @OnStkObjectCancel3dEditing.setter
    def OnStkObjectCancel3dEditing(self, callback):
        self._events["OnStkObjectCancel3dEditing"]._safe_assign(callback)
        
    @property
    def OnStkObjectPreCut(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPreCut(pArgs:"StkObjectCutCopyPasteEventArgs") -> None]"""
        return self._events["OnStkObjectPreCut"]
        
    @OnStkObjectPreCut.setter
    def OnStkObjectPreCut(self, callback):
        self._events["OnStkObjectPreCut"]._safe_assign(callback)
        
    @property
    def OnStkObjectCopy(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectCopy(pArgs:"StkObjectCutCopyPasteEventArgs") -> None]"""
        return self._events["OnStkObjectCopy"]
        
    @OnStkObjectCopy.setter
    def OnStkObjectCopy(self, callback):
        self._events["OnStkObjectCopy"]._safe_assign(callback)
        
    @property
    def OnStkObjectPaste(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPaste(pArgs:"StkObjectCutCopyPasteEventArgs") -> None]"""
        return self._events["OnStkObjectPaste"]
        
    @OnStkObjectPaste.setter
    def OnStkObjectPaste(self, callback):
        self._events["OnStkObjectPaste"]._safe_assign(callback)
    
    
################################################################################
#          IAgSTKXApplicationEvents
################################################################################

class ISTKXApplicationEventHandler(STKEventSubscriber):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        self._events["OnScenarioNew"]                = _STKEvent()
        self._events["OnScenarioLoad"]               = _STKEvent()
        self._events["OnScenarioClose"]              = _STKEvent()
        self._events["OnScenarioSave"]               = _STKEvent()
        self._events["OnLogMessage"]                 = _STKEvent()
        self._events["OnAnimUpdate"]                 = _STKEvent()
        self._events["OnNewGlobeCtrlRequest"]        = _STKEvent()
        self._events["OnNewMapCtrlRequest"]          = _STKEvent()
        self._events["OnBeforeNewScenario"]          = _STKEvent()
        self._events["OnBeforeLoadScenario"]         = _STKEvent()
        self._events["OnBeginScenarioClose"]         = _STKEvent()
        self._events["OnNewGfxAnalysisCtrlRequest"]  = _STKEvent()
        self._events["OnSSLCertificateServerError"]  = _STKEvent()
        self._events["OnConControlQuitReceived"]     = _STKEvent()
        if type(interface)==IUnknown:
            impl = ISTKXApplicationEventCOMHandler(interface, self._events)
        elif type(interface)==grpc_interface:
            impl = IAgSTKXApplicationEventGrpcHandler(interface, self._events)
        else:
            raise STKRuntimeError(f"Unexpected type {type(interface)}, cannot create ISTKXApplicationEventHandler.")
        STKEventSubscriber.__init__(self, impl)
                
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in ISTKXApplicationEventHandler.__dict__ and type(ISTKXApplicationEventHandler.__dict__[attrname]) == property:
            ISTKXApplicationEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in STKXApplicationEvents.")
        
    @property
    def OnScenarioNew(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioNew(Path:str) -> None]"""
        return self._events["OnScenarioNew"]
        
    @OnScenarioNew.setter
    def OnScenarioNew(self, callback):
        self._events["OnScenarioNew"]._safe_assign(callback)
        
    @property
    def OnScenarioLoad(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioLoad(Path:str) -> None]"""
        return self._events["OnScenarioLoad"]
        
    @OnScenarioLoad.setter
    def OnScenarioLoad(self, callback):
        self._events["OnScenarioLoad"]._safe_assign(callback)
        
    @property
    def OnScenarioClose(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioClose() -> None]"""
        return self._events["OnScenarioClose"]
        
    @OnScenarioClose.setter
    def OnScenarioClose(self, callback):
        self._events["OnScenarioClose"]._safe_assign(callback)
        
    @property
    def OnScenarioSave(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioSave(Path:str) -> None]"""
        return self._events["OnScenarioSave"]
        
    @OnScenarioSave.setter
    def OnScenarioSave(self, callback):
        self._events["OnScenarioSave"]._safe_assign(callback)
        
    @property
    def OnLogMessage(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnLogMessage(message:str, msgType:"LOG_MSG_TYPE", errorCode:int, fileName:str, lineNo:int, dispID:"LOG_MSG_DISP_ID") -> None]"""
        return self._events["OnLogMessage"]
        
    @OnLogMessage.setter
    def OnLogMessage(self, callback):
        self._events["OnLogMessage"]._safe_assign(callback)

    @property
    def OnAnimUpdate(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimUpdate(timeEpSec:float) -> None]"""
        return self._events["OnAnimUpdate"]
        
    @OnAnimUpdate.setter
    def OnAnimUpdate(self, callback):
        self._events["OnAnimUpdate"]._safe_assign(callback)
        
    @property
    def OnNewGlobeCtrlRequest(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewGlobeCtrlRequest(SceneID:int) -> None]"""
        return self._events["OnNewGlobeCtrlRequest"]
        
    @OnNewGlobeCtrlRequest.setter
    def OnNewGlobeCtrlRequest(self, callback):
        self._events["OnNewGlobeCtrlRequest"]._safe_assign(callback)
    
    @property
    def OnNewMapCtrlRequest(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewMapCtrlRequest(WinID:int) -> None]"""
        return self._events["OnNewMapCtrlRequest"]
        
    @OnNewMapCtrlRequest.setter
    def OnNewMapCtrlRequest(self, callback):
        self._events["OnNewMapCtrlRequest"]._safe_assign(callback)
        
    @property
    def OnBeforeNewScenario(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeforeNewScenario(Scenario:str) -> None]"""
        return self._events["OnBeforeNewScenario"]
        
    @OnBeforeNewScenario.setter
    def OnBeforeNewScenario(self, callback):
        self._events["OnBeforeNewScenario"]._safe_assign(callback)
        
    @property
    def OnBeforeLoadScenario(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeforeLoadScenario(Scenario:str) -> None]"""
        return self._events["OnBeforeLoadScenario"]
        
    @OnBeforeLoadScenario.setter
    def OnBeforeLoadScenario(self, callback):
        self._events["OnBeforeLoadScenario"]._safe_assign(callback)
        
    @property
    def OnBeginScenarioClose(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeginScenarioClose() -> None]"""
        return self._events["OnBeginScenarioClose"]
        
    @OnBeginScenarioClose.setter
    def OnBeginScenarioClose(self, callback):
        self._events["OnBeginScenarioClose"]._safe_assign(callback)
    
    @property
    def OnNewGfxAnalysisCtrlRequest(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewGfxAnalysisCtrlRequest(SceneID:int, GfxAnalysisMode:"GRAPHICS_2D_ANALYSIS_MODE") -> None]"""
        return self._events["OnNewGfxAnalysisCtrlRequest"]
        
    @OnNewGfxAnalysisCtrlRequest.setter
    def OnNewGfxAnalysisCtrlRequest(self, callback):
        self._events["OnNewGfxAnalysisCtrlRequest"]._safe_assign(callback)
    
    @property
    def OnSSLCertificateServerError(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnSSLCertificateServerError(pArgs:"STKXSSLCertificateErrorEventArgs") -> None]"""
        return self._events["OnSSLCertificateServerError"]
        
    @OnSSLCertificateServerError.setter
    def OnSSLCertificateServerError(self, callback):
        self._events["OnSSLCertificateServerError"]._safe_assign(callback)
        
    @property
    def OnConControlQuitReceived(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnConControlQuitReceived(pArgs:"STKXConControlQuitReceivedEventArgs") -> None]"""
        return self._events["OnConControlQuitReceived"]
        
    @OnConControlQuitReceived.setter
    def OnConControlQuitReceived(self, callback):
        self._events["OnConControlQuitReceived"]._safe_assign(callback)

                
################################################################################
#          ActiveX controls
################################################################################

class IAgUiAxStockEventHandler(object):
    def __init__(self):
        self._events["KeyDown"]      = _STKEvent()
        self._events["KeyPress"]     = _STKEvent()
        self._events["KeyUp"]        = _STKEvent()
        self._events["Click"]        = _STKEvent()
        self._events["DblClick"]     = _STKEvent()
        self._events["MouseDown"]    = _STKEvent()
        self._events["MouseMove"]    = _STKEvent()
        self._events["MouseUp"]      = _STKEvent()
        self._events["OLEDragDrop"]  = _STKEvent()
        self._events["MouseWheel"]   = _STKEvent()
        
    def __setattr__(self, attrname, value):
        if attrname in IAgUiAxStockEventHandler.__dict__ and type(IAgUiAxStockEventHandler.__dict__[attrname]) == property:
            IAgUiAxStockEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in IAgUiAxStockEvents.")
    
    @property
    def KeyDown(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyDown(KeyCode:int, Shift:int) -> None]"""
        return self._events["KeyDown"]
        
    @KeyDown.setter
    def KeyDown(self, callback):
        self._events["KeyDown"]._safe_assign(callback)

    @property
    def KeyPress(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyPress(KeyAscii:int) -> None]"""
        return self._events["KeyPress"]
        
    @KeyPress.setter
    def KeyPress(self, callback):
        self._events["KeyPress"]._safe_assign(callback)
        
    @property
    def KeyUp(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyUp(KeyCode:int, Shift:int) -> None]"""
        return self._events["KeyUp"]
        
    @KeyUp.setter
    def KeyUp(self, callback):
        self._events["KeyUp"]._safe_assign(callback)
        
    @property
    def Click(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [Click() -> None]"""
        return self._events["Click"]
        
    @Click.setter
    def Click(self, callback):
        self._events["Click"]._safe_assign(callback)
 
    @property
    def DblClick(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [DblClick() -> None]"""
        return self._events["DblClick"]
        
    @DblClick.setter
    def DblClick(self, callback):
        self._events["DblClick"]._safe_assign(callback)
        
    @property
    def MouseDown(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseDown(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._events["MouseDown"]
        
    @MouseDown.setter
    def MouseDown(self, callback):
        self._events["MouseDown"]._safe_assign(callback)

    @property
    def MouseMove(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseMove(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._events["MouseMove"]
        
    @MouseMove.setter
    def MouseMove(self, callback):
        self._events["MouseMove"]._safe_assign(callback)

    @property
    def MouseUp(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseUp(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._events["MouseUp"]
        
    @MouseUp.setter
    def MouseUp(self, callback):
        self._events["MouseUp"]._safe_assign(callback)

    @property
    def OLEDragDrop(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OLEDragDrop(Data:"DataObject", Effect:int, Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._events["OLEDragDrop"]
        
    @OLEDragDrop.setter
    def OLEDragDrop(self, callback):
        self._events["OLEDragDrop"]._safe_assign(callback)

    @property
    def MouseWheel(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseWheel(Button:int, Shift:int, Delta:int, X:int, Y:int) -> None]"""
        return self._events["MouseWheel"]
        
    @MouseWheel.setter
    def MouseWheel(self, callback):
        self._events["MouseWheel"]._safe_assign(callback)


class IUiAxGraphics2DCntrlEventHandler(STKEventSubscriber, IAgUiAxStockEventHandler):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        IAgUiAxStockEventHandler.__init__(self)
        if type(interface)==IUnknown:
            impl = IUiAxGraphics2DCntrlEventCOMHandler(interface, self._events)
        elif type(interface)==grpc_interface:
            raise STKRuntimeError(f"Active X Control events are not available with gRPC.")
        else:
            raise STKRuntimeError(f"Unexpected type {type(interface)}, cannot create IUiAxGraphics2DCntrlEventHandler.")
        STKEventSubscriber.__init__(self, impl)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        try:
            IAgUiAxStockEventHandler.__setattr__(self, attrname, value)
        except:
            if attrname in IUiAxGraphics2DCntrlEventHandler.__dict__ and type(IUiAxGraphics2DCntrlEventHandler.__dict__[attrname]) == property:
                IUiAxGraphics2DCntrlEventHandler.__dict__[attrname].__set__(self, value)
            else:
                raise STKAttributeError(attrname + " is not a recognized event in UiAx2DCntrlEvents.")


class IUiAxGraphics3DCntrlEventHandler(STKEventSubscriber, IAgUiAxStockEventHandler):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        self._events["_OnObjectEditingStart"]     = _STKEvent()
        self._events["_OnObjectEditingApply"]     = _STKEvent()
        self._events["_OnObjectEditingCancel"]    = _STKEvent()
        self._events["_OnObjectEditingStop"]      = _STKEvent()
        if type(interface)==IUnknown:
            impl = IUiAxGraphics3DCntrlEventCOMHandler(interface, self._events)
        elif type(interface)==grpc_interface:
            raise STKRuntimeError(f"Active X Control events are not available with gRPC.")
        else:
            raise STKRuntimeError(f"Unexpected type {type(interface)}, cannot create IUiAxGraphics3DCntrlEventHandler.")
        STKEventSubscriber.__init__(self, impl)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        try:
            IAgUiAxStockEventHandler.__setattr__(self, attrname, value)
        except:
            if attrname in IUiAxGraphics3DCntrlEventHandler.__dict__ and type(IUiAxGraphics3DCntrlEventHandler.__dict__[attrname]) == property:
                IUiAxGraphics3DCntrlEventHandler.__dict__[attrname].__set__(self, value)
            else:
                raise STKAttributeError(attrname + " is not a recognized event in UiAxGraphics3DCntrlEvents.")
            
    @property
    def OnObjectEditingStart(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingStart(Path:str) -> None]"""
        return self._events["OnObjectEditingStart"]
        
    @OnObjectEditingStart.setter
    def OnObjectEditingStart(self, callback):
        self._events["OnObjectEditingStart"]._safe_assign(callback)

    @property
    def OnObjectEditingApply(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingApply(Path:str) -> None]"""
        return self._events["OnObjectEditingApply"]
        
    @OnObjectEditingApply.setter
    def OnObjectEditingApply(self, callback):
        self._events["OnObjectEditingApply"]._safe_assign(callback)

    @property
    def OnObjectEditingCancel(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingCancel(Path:str) -> None]"""
        return self._events["OnObjectEditingCancel"]
        
    @OnObjectEditingCancel.setter
    def OnObjectEditingCancel(self, callback):
        self._events["OnObjectEditingCancel"]._safe_assign(callback)

    @property
    def OnObjectEditingStop(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingStop(Path:str) -> None]"""
        return self._events["OnObjectEditingStop"]
        
    @OnObjectEditingStop.setter
    def OnObjectEditingStop(self, callback):
        self._events["OnObjectEditingStop"]._safe_assign(callback)
        
        
################################################################################
#          IAgStkGraphicsSceneEvents
################################################################################

class ISceneEventHandler(STKEventSubscriber):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        self._events["Rendering"] = _STKEvent()
        if type(interface)==IUnknown:
            impl = ISceneEventCOMHandler(interface, self._events)
        elif type(interface)==grpc_interface:
            impl = IAgStkGraphicsSceneEventGrpcHandler(interface, self._events)
        else:
            raise STKRuntimeError(f"Unexpected type {type(interface)}, cannot create ISceneEventHandler.")
        STKEventSubscriber.__init__(self, impl)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in ISceneEventHandler.__dict__ and type(ISceneEventHandler.__dict__[attrname]) == property:
            ISceneEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in SceneEvents.")
          
    @property
    def Rendering(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [Rendering(Sender:typing.Any, Args:"RenderingEventArgs") -> None]"""
        return self._events["Rendering"]
        
    @Rendering.setter
    def Rendering(self, callback):
        self._events["Rendering"]._safe_assign(callback)
                
                
################################################################################
#          IAgStkGraphicsKmlGraphicsEvents
################################################################################

class IKmlGraphicsEventHandler(STKEventSubscriber):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        self._events["DocumentLoaded"] = _STKEvent()
        if type(interface)==IUnknown:
            impl = IKmlGraphicsEventCOMHandler(interface, self._events)
        elif type(interface)==grpc_interface:
            impl = IAgStkGraphicsKmlGraphicsEventGrpcHandler(interface, self._events)
        else:
            raise STKRuntimeError(f"Unexpected type {type(interface)}, cannot create IKmlGraphicsEventHandler.")
        STKEventSubscriber.__init__(self, impl)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IKmlGraphicsEventHandler.__dict__ and type(IKmlGraphicsEventHandler.__dict__[attrname]) == property:
            IKmlGraphicsEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in KmlGraphicsEvents.")
        
    @property
    def DocumentLoaded(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [DocumentLoaded(Sender:typing.Any, Args:"KmlDocumentLoadedEventArgs") -> None]"""
        return self._events["DocumentLoaded"]
        
    @DocumentLoaded.setter
    def DocumentLoaded(self, callback):
        self._events["DocumentLoaded"]._safe_assign(callback)
      
                
################################################################################
#          IAgStkGraphicsImageCollectionEvents
################################################################################

class IImageCollectionEventHandler(STKEventSubscriber):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        self._events["AddComplete"] = _STKEvent()
        if type(interface)==IUnknown:
            impl = IImageCollectionEventCOMHandler(interface, self._events)
        elif type(interface)==grpc_interface:
            impl = IAgStkGraphicsImageCollectionEventGrpcHandler(interface, self._events)
        else:
            raise STKRuntimeError(f"Unexpected type {type(interface)}, cannot create IImageCollectionEventHandler.")
        STKEventSubscriber.__init__(self, impl)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in IImageCollectionEventHandler.__dict__ and type(IImageCollectionEventHandler.__dict__[attrname]) == property:
            IImageCollectionEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in ImageCollectionEvents.")

    @property
    def AddComplete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [AddComplete(Sender:typing.Any, Args:"GlobeImageOverlayAddCompleteEventArgs") -> None]"""
        return self._events["AddComplete"]
        
    @AddComplete.setter
    def AddComplete(self, callback):
        self._events["AddComplete"]._safe_assign(callback)

                
################################################################################
#          IAgStkGraphicsTerrainCollectionEvents
################################################################################

class ITerrainOverlayCollectionEventHandler(STKEventSubscriber):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        self._events["AddComplete"] = _STKEvent()
        if type(interface)==IUnknown:
            impl = ITerrainOverlayCollectionEventCOMHandler(interface, self._events)
        elif type(interface)==grpc_interface:
            impl = IAgStkGraphicsTerrainCollectionEventGrpcHandler(interface, self._events)
        else:
            raise STKRuntimeError(f"Unexpected type {type(interface)}, cannot create ITerrainOverlayCollectionEventHandler.")
        STKEventSubscriber.__init__(self, impl)
        
    def __del__(self):
        STKEventSubscriber.__del__(self)
        
    def __setattr__(self, attrname, value):
        if attrname in ITerrainOverlayCollectionEventHandler.__dict__ and type(ITerrainOverlayCollectionEventHandler.__dict__[attrname]) == property:
            ITerrainOverlayCollectionEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise STKAttributeError(attrname + " is not a recognized event in TerrainOverlayCollectionEvents.")

    @property
    def AddComplete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [AddComplete(Sender:typing.Any, Args:"TerrainOverlayAddCompleteEventArgs") -> None]"""
        return self._events["AddComplete"]
        
    @AddComplete.setter
    def AddComplete(self, callback):
        self._events["AddComplete"]._safe_assign(callback)
        
    
################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################