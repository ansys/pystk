################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################

__all__ = [ "StkObjectRootEventGrpcHandler", 
            "STKXApplicationEventGrpcHandler", 
            "SceneEventGrpcHandler",
            "KmlGraphicsEventGrpcHandler",
            "ImageCollectionEventGrpcHandler",
            "TerrainOverlayCollectionEventGrpcHandler"]

from .grpcutil import *
from .coclassutil import AgTypeNameMap
from . import AgGrpcServices_pb2
from ..utilities.exceptions import *

class _iadd_callback(object):
    def __init__(self, intf, event_name, handler, callback_func):
        self._intf = intf
        self._event_name = event_name
        self._handler = handler
        self._func = callback_func

    def __call__(self, count):
        if count == 1:
            self._intf.subscribe(self._handler, self._event_name, self._func)

class _isub_callback(object):
    def __init__(self, intf, event_name, handler, callback_func):
        self._intf = intf
        self._event_name = event_name
        self._handler = handler
        self._func = callback_func

    def __call__(self, count):
        if count == 0:
            self._intf.unsubscribe(self._handler, self._event_name, self._func)

class _GrpcEventHandlerImpl(object):
    def __init__(self, interface:grpc_interface, event_handler:AgGrpcServices_pb2.EventHandler, events:dict):
        self._intf = interface
        self._handler = event_handler
        self._events = events

    def __del__(self):
        pass
        
    def _register_iadd_isub_callbacks(self, event:str, callback):
        self._events[event]._set_iadd_callback(_iadd_callback(self._intf, event, self._handler, callback))
        self._events[event]._set_isub_callback(_isub_callback(self._intf, event, self._handler, callback))

    def Subscribe(self):
        # No action needed since events are subscribed individually rather than all at once
        pass
    
    def Unsubscribe(self):
        self._intf.unsubscribe_all(self._handler)
        
################################################################################
#          IAgStkObjectRootEvents
################################################################################

class IAgStkObjectRootEventGrpcHandler(_GrpcEventHandlerImpl):

    def __init__(self, interface:grpc_interface, events:dict):
        _GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkObjectRootEvents, events)
        self._register_iadd_isub_callbacks("OnScenarioNew", self._OnScenarioNew)
        self._register_iadd_isub_callbacks("OnScenarioLoad", self._OnScenarioLoad)
        self._register_iadd_isub_callbacks("OnScenarioClose", self._OnScenarioClose)
        self._register_iadd_isub_callbacks("OnScenarioSave", self._OnScenarioSave)
        self._register_iadd_isub_callbacks("OnLogMessage", self._OnLogMessage)
        self._register_iadd_isub_callbacks("OnAnimUpdate", self._OnAnimUpdate)
        self._register_iadd_isub_callbacks("OnStkObjectAdded", self._OnStkObjectAdded)
        self._register_iadd_isub_callbacks("OnStkObjectDeleted", self._OnStkObjectDeleted)
        self._register_iadd_isub_callbacks("OnStkObjectRenamed", self._OnStkObjectRenamed)
        self._register_iadd_isub_callbacks("OnAnimationPlayback", self._OnAnimationPlayback)
        self._register_iadd_isub_callbacks("OnAnimationRewind", self._OnAnimationRewind)
        self._register_iadd_isub_callbacks("OnAnimationPause", self._OnAnimationPause)
        self._register_iadd_isub_callbacks("OnScenarioBeforeSave", self._OnScenarioBeforeSave)
        self._register_iadd_isub_callbacks("OnAnimationStep", self._OnAnimationStep)
        self._register_iadd_isub_callbacks("OnAnimationStepBack", self._OnAnimationStepBack)
        self._register_iadd_isub_callbacks("OnAnimationSlower", self._OnAnimationSlower)
        self._register_iadd_isub_callbacks("OnAnimationFaster", self._OnAnimationFaster)
        self._register_iadd_isub_callbacks("OnPercentCompleteUpdate", self._OnPercentCompleteUpdate)
        self._register_iadd_isub_callbacks("OnPercentCompleteEnd", self._OnPercentCompleteEnd)
        self._register_iadd_isub_callbacks("OnPercentCompleteBegin", self._OnPercentCompleteBegin)
        self._register_iadd_isub_callbacks("OnStkObjectChanged", self._OnStkObjectChanged)
        self._register_iadd_isub_callbacks("OnScenarioBeforeClose", self._OnScenarioBeforeClose)
        self._register_iadd_isub_callbacks("OnStkObjectPreDelete", self._OnStkObjectPreDelete)
        self._register_iadd_isub_callbacks("OnStkObjectStart3dEditing", self._OnStkObjectStart3dEditing)
        self._register_iadd_isub_callbacks("OnStkObjectStop3dEditing", self._OnStkObjectStop3dEditing)
        self._register_iadd_isub_callbacks("OnStkObjectApply3dEditing", self._OnStkObjectApply3dEditing)
        self._register_iadd_isub_callbacks("OnStkObjectCancel3dEditing", self._OnStkObjectCancel3dEditing)
        self._register_iadd_isub_callbacks("OnStkObjectPreCut", self._OnStkObjectPreCut)
        self._register_iadd_isub_callbacks("OnStkObjectCopy", self._OnStkObjectCopy)
        self._register_iadd_isub_callbacks("OnStkObjectPaste", self._OnStkObjectPaste)

    def _OnScenarioNew(self, path:str) -> None:
        for callback in self._events["OnScenarioNew"]._callbacks:
            try:
                callback(path)
            except:
                pass
                
    def _OnScenarioLoad(self, path:str) -> None:
        for callback in self._events["OnScenarioLoad"]._callbacks:
            try:
                callback(path)
            except:
                pass
    
    def _OnScenarioClose(self) -> None:
        for callback in self._events["OnScenarioClose"]._callbacks:
            try:
                callback()
            except:
                pass
    
    def _OnScenarioSave(self, path:str) -> None:
        for callback in self._events["OnScenarioSave"]._callbacks:
            try:
                callback(path)
            except:
                pass
    
    def _OnLogMessage(self, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._events["OnLogMessage"]._callbacks:
            try:
                callback(message, AgTypeNameMap["LOG_MSG_TYPE"](msgType), errorCode, fileName, lineNo, AgTypeNameMap["LOG_MSG_DISP_ID"](dispID))
            except:
                pass
    
    def _OnAnimUpdate(self, timeEpSec:float) -> None:
        for callback in self._events["OnAnimUpdate"]._callbacks:
            try:
                callback(timeEpSec)
            except:
                pass
    
    def _OnStkObjectAdded(self, Sender:typing.Any) -> None:
        for callback in self._events["OnStkObjectAdded"]._callbacks:
            try:
                callback(Sender)
            except:
                pass
                
    def _OnStkObjectDeleted(self, Sender:typing.Any) -> None:
        for callback in self._events["OnStkObjectDeleted"]._callbacks:
            try:
                callback(Sender)
            except:
                pass
                
    def _OnStkObjectRenamed(self, Sender:typing.Any, OldPath:str, NewPath:str) -> None:
        for callback in self._events["OnStkObjectRenamed"]._callbacks:
            try:
                callback(Sender, OldPath, NewPath)
            except:
                pass
                
    def _OnAnimationPlayback(self, CurrentTime:float, eAction:int, eDirection:int) -> None:
        for callback in self._events["OnAnimationPlayback"]._callbacks:
            try:
                callback(CurrentTime, AgTypeNameMap["ANIMATION_ACTIONS"](eAction), AgTypeNameMap["ANIMATION_DIRECTIONS"](eDirection))
            except:
                pass
                
    def _OnAnimationRewind(self) -> None:
        for callback in self._events["OnAnimationRewind"]._callbacks:
            try:
                callback()
            except:
                pass
            
    def _OnAnimationPause(self, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationPause"]._callbacks:
            try:
                callback(CurrentTime)
            except:
                pass
                
    def _OnScenarioBeforeSave(self, pArgs:"ScenarioBeforeSaveEventArgs") -> None:
        for callback in self._events["OnScenarioBeforeSave"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass
                
    def _OnAnimationStep(self, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationStep"]._callbacks:
            try:
                callback(CurrentTime)
            except:
                pass
                
    def _OnAnimationStepBack(self, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationStepBack"]._callbacks:
            try:
                callback(CurrentTime)
            except:
                pass
                
    def _OnAnimationSlower(self) -> None:
        for callback in self._events["OnAnimationSlower"]._callbacks:
            try:
                callback()
            except:
                pass
            
    def _OnAnimationFaster(self) -> None:
        for callback in self._events["OnAnimationFaster"]._callbacks:
            try:
                callback()
            except:
                pass
            
    def _OnPercentCompleteUpdate(self, pArgs:"PctCmpltEventArgs") -> None:
        for callback in self._events["OnPercentCompleteUpdate"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass
                
    def _OnPercentCompleteEnd(self) -> None:
        for callback in self._events["OnPercentCompleteEnd"]._callbacks:
            try:
                callback()
            except:
                pass
            
    def _OnPercentCompleteBegin(self) -> None:
        for callback in self._events["OnPercentCompleteBegin"]._callbacks:
            try:
                callback()
            except:
                pass
            
    def _OnStkObjectChanged(self, pArgs:"StkObjectChangedEventArgs") -> None:
        for callback in self._events["OnStkObjectChanged"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass
                
    def _OnScenarioBeforeClose(self) -> None:
        for callback in self._events["OnScenarioBeforeClose"]._callbacks:
            try:
                callback()
            except:
                pass
            
    def _OnStkObjectPreDelete(self, pArgs:"StkObjectPreDeleteEventArgs") -> None:
        for callback in self._events["OnStkObjectPreDelete"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass
                
    def _OnStkObjectStart3dEditing(self, path:str) -> None:
        for callback in self._events["OnStkObjectStart3dEditing"]._callbacks:
            try:
                callback(path)
            except:
                pass
            
    def _OnStkObjectStop3dEditing(self, path:str) -> None:
        for callback in self._events["OnStkObjectStop3dEditing"]._callbacks:
            try:
                callback(path)
            except:
                pass
            
    def _OnStkObjectApply3dEditing(self, path:str) -> None:
        for callback in self._events["OnStkObjectApply3dEditing"]._callbacks:
            try:
                callback(path)
            except:
                pass
            
    def _OnStkObjectCancel3dEditing(self, path:str) -> None:
        for callback in self._events["OnStkObjectCancel3dEditing"]._callbacks:
            try:
                callback(path)
            except:
                pass
            
    def _OnStkObjectPreCut(self, pArgs:"StkObjectCutCopyPasteEventArgs") -> None:
        for callback in self._events["OnStkObjectPreCut"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass
            
    def _OnStkObjectCopy(self, pArgs:"StkObjectCutCopyPasteEventArgs") -> None:
        for callback in self._events["OnStkObjectCopy"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass
            
    def _OnStkObjectPaste(self, pArgs:"StkObjectCutCopyPasteEventArgs") -> None:
        for callback in self._events["OnStkObjectPaste"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass
      
    
################################################################################
#          IAgSTKXApplicationEvents
################################################################################

class IAgSTKXApplicationEventGrpcHandler(_GrpcEventHandlerImpl):

    def __init__(self, interface:grpc_interface, events:dict):
        _GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgSTKXApplicationEvents, events)
        self._register_iadd_isub_callbacks("OnScenarioNew", self._OnScenarioNew)
        self._register_iadd_isub_callbacks("OnScenarioLoad", self._OnScenarioLoad)
        self._register_iadd_isub_callbacks("OnScenarioClose", self._OnScenarioClose)
        self._register_iadd_isub_callbacks("OnScenarioSave", self._OnScenarioSave)
        self._register_iadd_isub_callbacks("OnLogMessage", self._OnLogMessage)
        self._register_iadd_isub_callbacks("OnAnimUpdate", self._OnAnimUpdate)
        self._register_iadd_isub_callbacks("OnNewGlobeCtrlRequest", self._OnNewGlobeCtrlRequest)
        self._register_iadd_isub_callbacks("OnNewMapCtrlRequest", self._OnNewMapCtrlRequest)
        self._register_iadd_isub_callbacks("OnBeforeNewScenario", self._OnBeforeNewScenario)
        self._register_iadd_isub_callbacks("OnBeforeLoadScenario", self._OnBeforeLoadScenario)
        self._register_iadd_isub_callbacks("OnBeginScenarioClose", self._OnBeginScenarioClose)
        self._register_iadd_isub_callbacks("OnNewGfxAnalysisCtrlRequest", self._OnNewGfxAnalysisCtrlRequest)
        self._register_iadd_isub_callbacks("OnSSLCertificateServerError", self._OnSSLCertificateServerError)
        self._register_iadd_isub_callbacks("OnConControlQuitReceived", self._OnConControlQuitReceived)

    def _OnScenarioNew(self, path:str) -> None:
        for callback in self._events["OnScenarioNew"]._callbacks:
            try:
                callback(path)
            except:
                pass
                
    def _OnScenarioLoad(self, path:str) -> None:
        for callback in self._events["OnScenarioLoad"]._callbacks:
            try:
                callback(path)
            except:
                pass
    
    def _OnScenarioClose(self) -> None:
        for callback in self._events["OnScenarioClose"]._callbacks:
            try:
                callback()
            except:
                pass
    
    def _OnScenarioSave(self, path:str) -> None:
        for callback in self._events["OnScenarioSave"]._callbacks:
            try:
                callback(path)
            except:
                pass
    
    def _OnLogMessage(self, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._events["OnLogMessage"]._callbacks:
            try:
                callback(message, AgTypeNameMap["LOG_MSG_TYPE"](msgType), errorCode, fileName, lineNo, AgTypeNameMap["LOG_MSG_DISP_ID"](dispID))
            except:
                pass
    
    def _OnAnimUpdate(self, timeEpSec:float) -> None:
        for callback in self._events["OnAnimUpdate"]._callbacks:
            try:
                callback(timeEpSec)
            except:
                pass
    
    def _OnNewGlobeCtrlRequest(self, SceneID:int) -> None:
        for callback in self._events["OnNewGlobeCtrlRequest"]._callbacks:
            try:
                callback(SceneID)
            except:
                pass
    
    def _OnNewMapCtrlRequest(self, WinID:int) -> None:
        for callback in self._events["OnNewMapCtrlRequest"]._callbacks:
            try:
                callback(WinID)
            except:
                pass
        
    def _OnBeforeNewScenario(self, Scenario:str) -> None:
        for callback in self._events["OnBeforeNewScenario"]._callbacks:
            try:
                callback(Scenario)
            except:
                pass
        
    def _OnBeforeLoadScenario(self, Scenario:str) -> None:
        for callback in self._events["OnBeforeLoadScenario"]._callbacks:
            try:
                callback(Scenario)
            except:
                pass
        
    def _OnBeginScenarioClose(self) -> None:
        for callback in self._events["OnBeginScenarioClose"]._callbacks:
            try:
                callback()
            except:
                pass
    
    def _OnNewGfxAnalysisCtrlRequest(self, SceneID:int, GfxAnalysisMode:int) -> None:
        for callback in self._events["OnNewGfxAnalysisCtrlRequest"]._callbacks:
            try:
                callback(SceneID, AgTypeNameMap["GRAPHICS_2D_ANALYSIS_MODE"](GfxAnalysisMode))
            except:
                pass
    
    def _OnSSLCertificateServerError(self, pArgs:"STKXSSLCertificateErrorEventArgs") -> None:
        for callback in self._events["OnSSLCertificateServerError"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass
        
    def _OnConControlQuitReceived(self, pArgs:"STKXConControlQuitReceivedEventArgs") -> None:
        for callback in self._events["OnConControlQuitReceived"]._callbacks:
            try:
                callback(pArgs)
            except:
                pass


################################################################################
#          IAgStkGraphicsSceneEvents
################################################################################

class IAgStkGraphicsSceneEventGrpcHandler(_GrpcEventHandlerImpl):

    def __init__(self, interface:grpc_interface, events:dict):
        _GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsSceneEvents, events)
        self._register_iadd_isub_callbacks("Rendering", self._Rendering)

    def _Rendering(self, Sender:typing.Any, Args:"RenderingEventArgs") -> None:
        for callback in self._events["Rendering"]._callbacks:
            try:
                callback(Sender, Args)
            except:
                pass

                
################################################################################
#          IAgStkGraphicsKmlGraphicsEvents
################################################################################

class IAgStkGraphicsKmlGraphicsEventGrpcHandler(_GrpcEventHandlerImpl):

    def __init__(self, interface:grpc_interface, events:dict):
        _GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsKmlGraphicsEvents, events)
        self._register_iadd_isub_callbacks("DocumentLoaded", self._DocumentLoaded)

    def _DocumentLoaded(self, Sender:typing.Any, Args:"KmlDocumentLoadedEventArgs") -> None:
        for callback in self._events["DocumentLoaded"]._callbacks:
            try:
                callback(Sender, Args)
            except:
                pass


################################################################################
#          IAgStkGraphicsImageCollectionEvents
################################################################################

class IAgStkGraphicsImageCollectionEventGrpcHandler(_GrpcEventHandlerImpl):

    def __init__(self, interface:grpc_interface, events:dict):
        _GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsImageCollectionEvents, events)
        self._register_iadd_isub_callbacks("AddComplete", self._AddComplete)

    def _AddComplete(self, Sender:typing.Any, Args:"GlobeImageOverlayAddCompleteEventArgs") -> None:
        for callback in self._events["AddComplete"]._callbacks:
            try:
                callback(Sender, Args)
            except:
                pass

                
################################################################################
#          IAgStkGraphicsTerrainCollectionEvents
################################################################################

class IAgStkGraphicsTerrainCollectionEventGrpcHandler(_GrpcEventHandlerImpl):

    def __init__(self, interface:grpc_interface, events:dict):
        _GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsTerrainCollectionEvents, events)
        self._register_iadd_isub_callbacks("AddComplete", self._AddComplete)

    def _AddComplete(self, Sender:typing.Any, Args:"TerrainOverlayAddCompleteEventArgs") -> None:
        for callback in self._events["AddComplete"]._callbacks:
            try:
                callback(Sender, Args)
            except:
                pass


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################