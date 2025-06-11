# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__all__ = [ "GrpcEventHandlerImpl",
            "ISTKObjectRootEventGrpcHandler",
            "ISTKXApplicationEventGrpcHandler",
            "ISceneEventGrpcHandler",
            "IKmlGraphicsEventGrpcHandler",
            "IImageCollectionEventGrpcHandler",
            "ITerrainOverlayCollectionEventGrpcHandler"]

import typing

from .grpcutil import GrpcInterface
from .coclassutil import AgTypeNameMap
from . import AgGrpcServices_pb2

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

class GrpcEventHandlerImpl(object):
    def __init__(self, interface:GrpcInterface, event_handler:AgGrpcServices_pb2.EventHandler, events:dict):
        self._intf = interface
        self._handler = event_handler
        self._events = events

    def __del__(self):
        pass

    def _register_iadd_isub_callbacks(self, event:str, callback):
        self._events[event]._set_iadd_callback(_iadd_callback(self._intf, event, self._handler, callback))
        self._events[event]._set_isub_callback(_isub_callback(self._intf, event, self._handler, callback))

    def subscribe(self):
        # No action needed since events are subscribed individually rather than all at once
        pass

    def unsubscribe(self):
        self._intf.unsubscribe_all(self._handler)

################################################################################
#          IStkObjectRootEvents
################################################################################

class ISTKObjectRootEventGrpcHandler(GrpcEventHandlerImpl):

    def __init__(self, interface:GrpcInterface, events:dict):
        GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkObjectRootEvents, events)
        self._register_iadd_isub_callbacks("OnScenarioNew", self._on_scenario_new)
        self._register_iadd_isub_callbacks("OnScenarioLoad", self._on_scenario_load)
        self._register_iadd_isub_callbacks("OnScenarioClose", self._on_scenario_close)
        self._register_iadd_isub_callbacks("OnScenarioSave", self._on_scenario_save)
        self._register_iadd_isub_callbacks("OnLogMessage", self._on_log_message)
        self._register_iadd_isub_callbacks("OnAnimUpdate", self._on_anim_update)
        self._register_iadd_isub_callbacks("OnStkObjectAdded", self._on_stk_object_added)
        self._register_iadd_isub_callbacks("OnStkObjectDeleted", self._on_stk_object_deleted)
        self._register_iadd_isub_callbacks("OnStkObjectRenamed", self._on_stk_object_renamed)
        self._register_iadd_isub_callbacks("OnAnimationPlayback", self._on_animation_playback)
        self._register_iadd_isub_callbacks("OnAnimationRewind", self._on_animation_rewind)
        self._register_iadd_isub_callbacks("OnAnimationPause", self._on_animation_pause)
        self._register_iadd_isub_callbacks("OnScenarioBeforeSave", self._on_scenario_before_save)
        self._register_iadd_isub_callbacks("OnAnimationStep", self._on_animation_step)
        self._register_iadd_isub_callbacks("OnAnimationStepBack", self._on_animation_step_back)
        self._register_iadd_isub_callbacks("OnAnimationSlower", self._on_animation_slower)
        self._register_iadd_isub_callbacks("OnAnimationFaster", self._on_animation_faster)
        self._register_iadd_isub_callbacks("OnPercentCompleteUpdate", self._on_percent_complete_update)
        self._register_iadd_isub_callbacks("OnPercentCompleteEnd", self._on_percent_complete_end)
        self._register_iadd_isub_callbacks("OnPercentCompleteBegin", self._on_percent_complete_begin)
        self._register_iadd_isub_callbacks("OnStkObjectChanged", self._on_stk_object_changed)
        self._register_iadd_isub_callbacks("OnScenarioBeforeClose", self._on_scenario_before_close)
        self._register_iadd_isub_callbacks("OnStkObjectPreDelete", self._on_stk_object_pre_delete)
        self._register_iadd_isub_callbacks("OnStkObjectStart3dEditing", self._on_stk_object_start_3d_editing)
        self._register_iadd_isub_callbacks("OnStkObjectStop3dEditing", self._on_stk_object_stop_3d_editing)
        self._register_iadd_isub_callbacks("OnStkObjectApply3dEditing", self._on_stk_object_apply_3d_editing)
        self._register_iadd_isub_callbacks("OnStkObjectCancel3dEditing", self._on_stk_object_cancel_3d_editing)
        self._register_iadd_isub_callbacks("OnStkObjectPreCut", self._on_stk_object_pre_cut)
        self._register_iadd_isub_callbacks("OnStkObjectCopy", self._on_stk_object_copy)
        self._register_iadd_isub_callbacks("OnStkObjectPaste", self._on_stk_object_paste)

    def _on_scenario_new(self, path:str) -> None:
        for callback in self._events["OnScenarioNew"]._callbacks:
            callback(path)

    def _on_scenario_load(self, path:str) -> None:
        for callback in self._events["OnScenarioLoad"]._callbacks:
            callback(path)

    def _on_scenario_close(self) -> None:
        for callback in self._events["OnScenarioClose"]._callbacks:
            callback()

    def _on_scenario_save(self, path:str) -> None:
        for callback in self._events["OnScenarioSave"]._callbacks:
            callback(path)

    def _on_log_message(self, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._events["OnLogMessage"]._callbacks:
            callback(message, AgTypeNameMap["LogMessageType"](msgType), errorCode, fileName, lineNo, AgTypeNameMap["LogMessageDisplayID"](dispID))

    def _on_anim_update(self, timeEpSec:float) -> None:
        for callback in self._events["OnAnimUpdate"]._callbacks:
            callback(timeEpSec)

    def _on_stk_object_added(self, Sender:typing.Any) -> None:
        for callback in self._events["OnStkObjectAdded"]._callbacks:
            callback(Sender)

    def _on_stk_object_deleted(self, Sender:typing.Any) -> None:
        for callback in self._events["OnStkObjectDeleted"]._callbacks:
            callback(Sender)

    def _on_stk_object_renamed(self, Sender:typing.Any, OldPath:str, NewPath:str) -> None:
        for callback in self._events["OnStkObjectRenamed"]._callbacks:
            callback(Sender, OldPath, NewPath)

    def _on_animation_playback(self, CurrentTime:float, eAction:int, eDirection:int) -> None:
        for callback in self._events["OnAnimationPlayback"]._callbacks:
            callback(CurrentTime, AgTypeNameMap["AnimationActionType"](eAction), AgTypeNameMap["AnimationDirectionType"](eDirection))

    def _on_animation_rewind(self) -> None:
        for callback in self._events["OnAnimationRewind"]._callbacks:
            callback()

    def _on_animation_pause(self, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationPause"]._callbacks:
            callback(CurrentTime)

    def _on_scenario_before_save(self, pArgs:"ScenarioBeforeSaveEventArguments") -> None:
        for callback in self._events["OnScenarioBeforeSave"]._callbacks:
            callback(pArgs)

    def _on_animation_step(self, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationStep"]._callbacks:
            callback(CurrentTime)

    def _on_animation_step_back(self, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationStepBack"]._callbacks:
            callback(CurrentTime)

    def _on_animation_slower(self) -> None:
        for callback in self._events["OnAnimationSlower"]._callbacks:
            callback()

    def _on_animation_faster(self) -> None:
        for callback in self._events["OnAnimationFaster"]._callbacks:
            callback()

    def _on_percent_complete_update(self, pArgs:"ProgressBarEventArguments") -> None:
        for callback in self._events["OnPercentCompleteUpdate"]._callbacks:
            callback(pArgs)

    def _on_percent_complete_end(self) -> None:
        for callback in self._events["OnPercentCompleteEnd"]._callbacks:
            callback()

    def _on_percent_complete_begin(self) -> None:
        for callback in self._events["OnPercentCompleteBegin"]._callbacks:
            callback()

    def _on_stk_object_changed(self, pArgs:"STKObjectChangedEventArguments") -> None:
        for callback in self._events["OnStkObjectChanged"]._callbacks:
            callback(pArgs)

    def _on_scenario_before_close(self) -> None:
        for callback in self._events["OnScenarioBeforeClose"]._callbacks:
            callback()

    def _on_stk_object_pre_delete(self, pArgs:"STKObjectPreDeleteEventArguments") -> None:
        for callback in self._events["OnStkObjectPreDelete"]._callbacks:
            callback(pArgs)

    def _on_stk_object_start_3d_editing(self, path:str) -> None:
        for callback in self._events["OnStkObjectStart3dEditing"]._callbacks:
            callback(path)

    def _on_stk_object_stop_3d_editing(self, path:str) -> None:
        for callback in self._events["OnStkObjectStop3dEditing"]._callbacks:
            callback(path)

    def _on_stk_object_apply_3d_editing(self, path:str) -> None:
        for callback in self._events["OnStkObjectApply3dEditing"]._callbacks:
            callback(path)

    def _on_stk_object_cancel_3d_editing(self, path:str) -> None:
        for callback in self._events["OnStkObjectCancel3dEditing"]._callbacks:
            callback(path)

    def _on_stk_object_pre_cut(self, pArgs:"STKObjectCutCopyPasteEventArguments") -> None:
        for callback in self._events["OnStkObjectPreCut"]._callbacks:
            callback(pArgs)

    def _on_stk_object_copy(self, pArgs:"STKObjectCutCopyPasteEventArguments") -> None:
        for callback in self._events["OnStkObjectCopy"]._callbacks:
            callback(pArgs)

    def _on_stk_object_paste(self, pArgs:"STKObjectCutCopyPasteEventArguments") -> None:
        for callback in self._events["OnStkObjectPaste"]._callbacks:
            callback(pArgs)


################################################################################
#          ISTKXApplicationEvents
################################################################################

class ISTKXApplicationEventGrpcHandler(GrpcEventHandlerImpl):

    def __init__(self, interface:GrpcInterface, events:dict):
        GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgSTKXApplicationEvents, events)
        self._register_iadd_isub_callbacks("OnScenarioNew", self._on_scenario_new)
        self._register_iadd_isub_callbacks("OnScenarioLoad", self._on_scenario_load)
        self._register_iadd_isub_callbacks("OnScenarioClose", self._on_scenario_close)
        self._register_iadd_isub_callbacks("OnScenarioSave", self._on_scenario_save)
        self._register_iadd_isub_callbacks("OnLogMessage", self._on_log_message)
        self._register_iadd_isub_callbacks("OnAnimUpdate", self._on_anim_update)
        self._register_iadd_isub_callbacks("OnNewGlobeCtrlRequest", self._on_new_globe_ctrl_request)
        self._register_iadd_isub_callbacks("OnNewMapCtrlRequest", self._on_new_map_ctrl_request)
        self._register_iadd_isub_callbacks("OnBeforeNewScenario", self._on_before_new_scenario)
        self._register_iadd_isub_callbacks("OnBeforeLoadScenario", self._on_before_load_scenario)
        self._register_iadd_isub_callbacks("OnBeginScenarioClose", self._on_begin_scenario_close)
        self._register_iadd_isub_callbacks("OnNewGfxAnalysisCtrlRequest", self._on_new_gfx_analysis_ctrl_request)
        self._register_iadd_isub_callbacks("OnSSLCertificateServerError", self._on_ssl_certificate_server_error)
        self._register_iadd_isub_callbacks("OnConControlQuitReceived", self._on_con_control_quit_received)

    def _on_scenario_new(self, path:str) -> None:
        for callback in self._events["OnScenarioNew"]._callbacks:
            callback(path)

    def _on_scenario_load(self, path:str) -> None:
        for callback in self._events["OnScenarioLoad"]._callbacks:
            callback(path)

    def _on_scenario_close(self) -> None:
        for callback in self._events["OnScenarioClose"]._callbacks:
            callback()

    def _on_scenario_save(self, path:str) -> None:
        for callback in self._events["OnScenarioSave"]._callbacks:
            callback(path)

    def _on_log_message(self, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._events["OnLogMessage"]._callbacks:
            callback(message, AgTypeNameMap["LogMessageType"](msgType), errorCode, fileName, lineNo, AgTypeNameMap["LogMessageDisplayID"](dispID))

    def _on_anim_update(self, timeEpSec:float) -> None:
        for callback in self._events["OnAnimUpdate"]._callbacks:
            callback(timeEpSec)

    def _on_new_globe_ctrl_request(self, SceneID:int) -> None:
        for callback in self._events["OnNewGlobeCtrlRequest"]._callbacks:
            callback(SceneID)

    def _on_new_map_ctrl_request(self, WinID:int) -> None:
        for callback in self._events["OnNewMapCtrlRequest"]._callbacks:
            callback(WinID)

    def _on_before_new_scenario(self, Scenario:str) -> None:
        for callback in self._events["OnBeforeNewScenario"]._callbacks:
            callback(Scenario)

    def _on_before_load_scenario(self, Scenario:str) -> None:
        for callback in self._events["OnBeforeLoadScenario"]._callbacks:
            callback(Scenario)

    def _on_begin_scenario_close(self) -> None:
        for callback in self._events["OnBeginScenarioClose"]._callbacks:
            callback()

    def _on_new_gfx_analysis_ctrl_request(self, SceneID:int, GfxAnalysisMode:int) -> None:
        for callback in self._events["OnNewGfxAnalysisCtrlRequest"]._callbacks:
            callback(SceneID, AgTypeNameMap["Graphics2DAnalysisMode"](GfxAnalysisMode))

    def _on_ssl_certificate_server_error(self, pArgs:"STKXSSLCertificateErrorEventArgs") -> None:
        for callback in self._events["OnSSLCertificateServerError"]._callbacks:
            callback(pArgs)

    def _on_con_control_quit_received(self, pArgs:"STKXConControlQuitReceivedEventArgs") -> None:
        for callback in self._events["OnConControlQuitReceived"]._callbacks:
            callback(pArgs)


################################################################################
#          IStkGraphicsSceneEvents
################################################################################

class ISceneEventGrpcHandler(GrpcEventHandlerImpl):

    def __init__(self, interface:GrpcInterface, events:dict):
        GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsSceneEvents, events)
        self._register_iadd_isub_callbacks("Rendering", self._rendering)

    def _rendering(self, Sender:typing.Any, Args:"RenderingEventArgs") -> None:
        for callback in self._events["Rendering"]._callbacks:
            callback(Sender, Args)


################################################################################
#          IStkGraphicsKmlGraphicsEvents
################################################################################

class IKmlGraphicsEventGrpcHandler(GrpcEventHandlerImpl):

    def __init__(self, interface:GrpcInterface, events:dict):
        GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsKmlGraphicsEvents, events)
        self._register_iadd_isub_callbacks("DocumentLoaded", self._document_loaded)

    def _document_loaded(self, Sender:typing.Any, Args:"KmlDocumentLoadedEventArgs") -> None:
        for callback in self._events["DocumentLoaded"]._callbacks:
            callback(Sender, Args)


################################################################################
#          IStkGraphicsImageCollectionEvents
################################################################################

class IImageCollectionEventGrpcHandler(GrpcEventHandlerImpl):

    def __init__(self, interface:GrpcInterface, events:dict):
        GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsImageCollectionEvents, events)
        self._register_iadd_isub_callbacks("AddComplete", self._add_complete)

    def _add_complete(self, Sender:typing.Any, Args:"GlobeImageOverlayAddCompleteEventArgs") -> None:
        for callback in self._events["AddComplete"]._callbacks:
            callback(Sender, Args)


################################################################################
#          IStkGraphicsTerrainCollectionEvents
################################################################################

class ITerrainOverlayCollectionEventGrpcHandler(GrpcEventHandlerImpl):

    def __init__(self, interface:GrpcInterface, events:dict):
        GrpcEventHandlerImpl.__init__(self, interface, AgGrpcServices_pb2.EventHandler.eIAgStkGraphicsTerrainCollectionEvents, events)
        self._register_iadd_isub_callbacks("AddComplete", self._add_complete)

    def _add_complete(self, Sender:typing.Any, Args:"TerrainOverlayAddCompleteEventArgs") -> None:
        for callback in self._events["AddComplete"]._callbacks:
            callback(Sender, Args)