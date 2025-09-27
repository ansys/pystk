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

from __future__ import annotations

__all__ = [ "ISTKObjectRootEventHandler",
            "ISTKXApplicationEventHandler",
            "IUiAxGraphics2DCntrlEventHandler",
            "IUiAxGraphics3DCntrlEventHandler",
            "ISceneEventHandler",
            "IKmlGraphicsEventHandler",
            "IImageCollectionEventHandler",
            "ITerrainOverlayCollectionEventHandler"]

import typing

from .comutil                import IUnknown
from .comevents import (COMEventHandlerImpl, ISTKXApplicationEventCOMHandler,
                        IImageCollectionEventCOMHandler,
                        IKmlGraphicsEventCOMHandler,
                        ISceneEventCOMHandler,
                        ITerrainOverlayCollectionEventCOMHandler,
                        ISTKObjectRootEventCOMHandler, IGraphics2DControlEventCOMHandler,
                        IGraphics3DControlEventCOMHandler)

try:
    from .grpcutil   import GrpcInterface
    from .grpcevents import (GrpcEventHandlerImpl, ISTKXApplicationEventGrpcHandler,
                         IImageCollectionEventGrpcHandler,
                         IKmlGraphicsEventGrpcHandler, ISceneEventGrpcHandler,
                         ITerrainOverlayCollectionEventGrpcHandler,
                         ISTKObjectRootEventGrpcHandler)
except:
    class GrpcInterface(object):
        def __init__(self):
            pass

invalid_use_exception = SyntaxError("Use operator += to register an event callback or operator -= to unregister the callback.")

class _EventSubscriptionManagerImpl(object):
    def __init__(self):
        self._next_id = 0
        self._handlers: typing.Dict[int, STKEventSubscriber] = {}

    def subscribe(self, handler: STKEventSubscriber) -> int:
        self._next_id = self._next_id + 1
        self._handlers[self._next_id] = handler
        handler._subscribe_impl()
        return self._next_id

    def unsubscribe(self, id:int):
        if id in self._handlers:
            self._handlers[id]._unsubscribe_impl()
            del(self._handlers[id])

    def unsubscribe_all(self):
        ids = [id for id in self._handlers]
        for id in ids:
            self.unsubscribe(id)

EventSubscriptionManager = _EventSubscriptionManagerImpl()

class STKEventSubscriber(object):
    def __init__(self, impl: COMEventHandlerImpl | GrpcEventHandlerImpl):
        self.__dict__["_event_manager_id"] = None
        self.__dict__["_impl"]: COMEventHandlerImpl | GrpcEventHandlerImpl = impl
        self.subscribe()

    def __del__(self):
        self.unsubscribe()
        del(self._impl)

    def subscribe(self):
        """Use to re-subscribe to events after calling Unsubscribe.  This class is initialized as subscribed when returned from STKObjectRoot.Subscribe()."""
        if self._event_manager_id is None:
            self.__dict__["_event_manager_id"] = EventSubscriptionManager.subscribe(self)

    def _subscribe_impl(self):
        """Private method, called by EventSubscriptionManager"""
        impl : COMEventHandlerImpl | GrpcEventHandlerImpl = self._impl
        impl.subscribe()

    def unsubscribe(self):
        """Unsubscribe from events."""
        if self._event_manager_id is not None:
            EventSubscriptionManager.unsubscribe(self._event_manager_id)
            self.__dict__["_event_manager_id"] = None

    def _unsubscribe_impl(self):
        """Private method, called by EventSubscriptionManager"""
        impl : COMEventHandlerImpl | GrpcEventHandlerImpl = self._impl
        impl.unsubscribe()

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

class ISTKObjectRootEventHandler(STKEventSubscriber):
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
            impl = ISTKObjectRootEventCOMHandler(interface, self._events)
        elif type(interface)==GrpcInterface:
            impl = ISTKObjectRootEventGrpcHandler(interface, self._events)
        else:
            raise RuntimeError(f"Unexpected type {type(interface)}, cannot create ISTKObjectRootEventHandler.")
        STKEventSubscriber.__init__(self, impl)

    def __del__(self):
        STKEventSubscriber.__del__(self)

    def __setattr__(self, attrname, value):
        if attrname in ISTKObjectRootEventHandler.__dict__ and type(ISTKObjectRootEventHandler.__dict__[attrname]) == property:
            ISTKObjectRootEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise AttributeError(attrname + " is not a recognized event in STKObjectRootEvents.")

    @property
    def on_scenario_new(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioNew(Path:str) -> None]"""
        return self._events["OnScenarioNew"]

    @on_scenario_new.setter
    def on_scenario_new(self, callback):
        self._events["OnScenarioNew"]._safe_assign(callback)

    @property
    def on_scenario_load(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioLoad(Path:str) -> None]"""
        return self._events["OnScenarioLoad"]

    @on_scenario_load.setter
    def on_scenario_load(self, callback):
        self._events["OnScenarioLoad"]._safe_assign(callback)

    @property
    def on_scenario_close(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioClose() -> None]"""
        return self._events["OnScenarioClose"]

    @on_scenario_close.setter
    def on_scenario_close(self, callback):
        self._events["OnScenarioClose"]._safe_assign(callback)

    @property
    def on_scenario_save(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioSave(Path:str) -> None]"""
        return self._events["OnScenarioSave"]

    @on_scenario_save.setter
    def on_scenario_save(self, callback):
        self._events["OnScenarioSave"]._safe_assign(callback)

    @property
    def on_log_message(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnLogMessage(message:str, msgType:"LogMessageType", errorCode:int, fileName:str, lineNo:int, dispID:"LogMessageDisplayID") -> None]"""
        return self._events["OnLogMessage"]

    @on_log_message.setter
    def on_log_message(self, callback):
        self._events["OnLogMessage"]._safe_assign(callback)

    @property
    def on_anim_update(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimUpdate(timeEpSec:float) -> None]"""
        return self._events["OnAnimUpdate"]

    @on_anim_update.setter
    def on_anim_update(self, callback):
        self._events["OnAnimUpdate"]._safe_assign(callback)

    @property
    def on_stk_object_added(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectAdded(Sender:typing.Any) -> None]"""
        return self._events["OnStkObjectAdded"]

    @on_stk_object_added.setter
    def on_stk_object_added(self, callback):
        self._events["OnStkObjectAdded"]._safe_assign(callback)

    @property
    def on_stk_object_deleted(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectDeleted(Sender:typing.Any) -> None]"""
        return self._events["OnStkObjectDeleted"]

    @on_stk_object_deleted.setter
    def on_stk_object_deleted(self, callback):
        self._events["OnStkObjectDeleted"]._safe_assign(callback)

    @property
    def on_stk_object_renamed(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectRenamed(Sender:typing.Any, OldPath:str, NewPath:str) -> None]"""
        return self._events["OnStkObjectRenamed"]

    @on_stk_object_renamed.setter
    def on_stk_object_renamed(self, callback):
        self._events["OnStkObjectRenamed"]._safe_assign(callback)

    @property
    def on_animation_playback(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationPlayback(CurrentTime:float, eAction:"AnimationActionType", eDirection:"AnimationDirectionType") -> None]"""
        return self._events["OnAnimationPlayback"]

    @on_animation_playback.setter
    def on_animation_playback(self, callback):
        self._events["OnAnimationPlayback"]._safe_assign(callback)

    @property
    def on_animation_rewind(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationRewind() -> None]"""
        return self._events["OnAnimationRewind"]

    @on_animation_rewind.setter
    def on_animation_rewind(self, callback):
        self._events["OnAnimationRewind"]._safe_assign(callback)

    @property
    def on_animation_pause(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationPause(CurrentTime:float) -> None]"""
        return self._events["OnAnimationPause"]

    @on_animation_pause.setter
    def on_animation_pause(self, callback):
        self._events["OnAnimationPause"]._safe_assign(callback)

    @property
    def on_scenario_before_save(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioBeforeSave(pArgs:"ScenarioBeforeSaveEventArguments") -> None]"""
        return self._events["OnScenarioBeforeSave"]

    @on_scenario_before_save.setter
    def on_scenario_before_save(self, callback):
        self._events["OnScenarioBeforeSave"]._safe_assign(callback)

    @property
    def on_animation_step(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationStep(CurrentTime:float) -> None]"""
        return self._events["OnAnimationStep"]

    @on_animation_step.setter
    def on_animation_step(self, callback):
        self._events["OnAnimationStep"]._safe_assign(callback)

    @property
    def on_animation_step_back(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationStepBack(CurrentTime:float) -> None]"""
        return self._events["OnAnimationStepBack"]

    @on_animation_step_back.setter
    def on_animation_step_back(self, callback):
        self._events["OnAnimationStepBack"]._safe_assign(callback)

    @property
    def on_animation_slower(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationSlower() -> None]"""
        return self._events["OnAnimationSlower"]

    @on_animation_slower.setter
    def on_animation_slower(self, callback):
        self._events["OnAnimationSlower"]._safe_assign(callback)

    @property
    def on_animation_faster(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimationFaster() -> None]"""
        return self._events["OnAnimationFaster"]

    @on_animation_faster.setter
    def on_animation_faster(self, callback):
        self._events["OnAnimationFaster"]._safe_assign(callback)

    @property
    def on_percent_complete_update(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteUpdate(pArgs:"ProgressBarEventArguments") -> None]"""
        return self._events["OnPercentCompleteUpdate"]

    @on_percent_complete_update.setter
    def on_percent_complete_update(self, callback):
        self._events["OnPercentCompleteUpdate"]._safe_assign(callback)

    @property
    def on_percent_complete_end(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteEnd() -> None]"""
        return self._events["OnPercentCompleteEnd"]

    @on_percent_complete_end.setter
    def on_percent_complete_end(self, callback):
        self._events["OnPercentCompleteEnd"]._safe_assign(callback)

    @property
    def on_percent_complete_begin(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnPercentCompleteBegin() -> None]"""
        return self._events["OnPercentCompleteBegin"]

    @on_percent_complete_begin.setter
    def on_percent_complete_begin(self, callback):
        self._events["OnPercentCompleteBegin"]._safe_assign(callback)

    @property
    def on_stk_object_changed(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectChanged(pArgs:"STKObjectChangedEventArguments") -> None]"""
        return self._events["OnStkObjectChanged"]

    @on_stk_object_changed.setter
    def on_stk_object_changed(self, callback):
        self._events["OnStkObjectChanged"]._safe_assign(callback)

    @property
    def on_scenario_before_close(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioBeforeClose() -> None]"""
        return self._events["OnScenarioBeforeClose"]

    @on_scenario_before_close.setter
    def on_scenario_before_close(self, callback):
        self._events["OnScenarioBeforeClose"]._safe_assign(callback)

    @property
    def on_stk_object_pre_delete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPreDelete(pArgs:"STKObjectPreDeleteEventArguments") -> None]"""
        return self._events["OnStkObjectPreDelete"]

    @on_stk_object_pre_delete.setter
    def on_stk_object_pre_delete(self, callback):
        self._events["OnStkObjectPreDelete"]._safe_assign(callback)

    @property
    def on_stk_object_start_3d_editing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectStart3dEditing(Path:str) -> None]"""
        return self._events["OnStkObjectStart3dEditing"]

    @on_stk_object_start_3d_editing.setter
    def on_stk_object_start_3d_editing(self, callback):
        self._events["OnStkObjectStart3dEditing"]._safe_assign(callback)

    @property
    def on_stk_object_stop_3d_editing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectStop3dEditing(Path:str) -> None]"""
        return self._events["OnStkObjectStop3dEditing"]

    @on_stk_object_stop_3d_editing.setter
    def on_stk_object_stop_3d_editing(self, callback):
        self._events["OnStkObjectStop3dEditing"]._safe_assign(callback)

    @property
    def on_stk_object_apply_3d_editing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectApply3dEditing(Path:str) -> None]"""
        return self._events["OnStkObjectApply3dEditing"]

    @on_stk_object_apply_3d_editing.setter
    def on_stk_object_apply_3d_editing(self, callback):
        self._events["OnStkObjectApply3dEditing"]._safe_assign(callback)

    @property
    def on_stk_object_cancel_3d_editing(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectCancel3dEditing(Path:str) -> None]"""
        return self._events["OnStkObjectCancel3dEditing"]

    @on_stk_object_cancel_3d_editing.setter
    def on_stk_object_cancel_3d_editing(self, callback):
        self._events["OnStkObjectCancel3dEditing"]._safe_assign(callback)

    @property
    def on_stk_object_pre_cut(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPreCut(pArgs:"STKObjectCutCopyPasteEventArguments") -> None]"""
        return self._events["OnStkObjectPreCut"]

    @on_stk_object_pre_cut.setter
    def on_stk_object_pre_cut(self, callback):
        self._events["OnStkObjectPreCut"]._safe_assign(callback)

    @property
    def on_stk_object_copy(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectCopy(pArgs:"STKObjectCutCopyPasteEventArguments") -> None]"""
        return self._events["OnStkObjectCopy"]

    @on_stk_object_copy.setter
    def on_stk_object_copy(self, callback):
        self._events["OnStkObjectCopy"]._safe_assign(callback)

    @property
    def on_stk_object_paste(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnStkObjectPaste(pArgs:"STKObjectCutCopyPasteEventArguments") -> None]"""
        return self._events["OnStkObjectPaste"]

    @on_stk_object_paste.setter
    def on_stk_object_paste(self, callback):
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
        elif type(interface)==GrpcInterface:
            impl = ISTKXApplicationEventGrpcHandler(interface, self._events)
        else:
            raise RuntimeError(f"Unexpected type {type(interface)}, cannot create ISTKXApplicationEventHandler.")
        STKEventSubscriber.__init__(self, impl)

    def __del__(self):
        STKEventSubscriber.__del__(self)

    def __setattr__(self, attrname, value):
        if attrname in ISTKXApplicationEventHandler.__dict__ and type(ISTKXApplicationEventHandler.__dict__[attrname]) == property:
            ISTKXApplicationEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise AttributeError(attrname + " is not a recognized event in STKXApplicationEvents.")

    @property
    def on_scenario_new(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioNew(Path:str) -> None]"""
        return self._events["OnScenarioNew"]

    @on_scenario_new.setter
    def on_scenario_new(self, callback):
        self._events["OnScenarioNew"]._safe_assign(callback)

    @property
    def on_scenario_load(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioLoad(Path:str) -> None]"""
        return self._events["OnScenarioLoad"]

    @on_scenario_load.setter
    def on_scenario_load(self, callback):
        self._events["OnScenarioLoad"]._safe_assign(callback)

    @property
    def on_scenario_close(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioClose() -> None]"""
        return self._events["OnScenarioClose"]

    @on_scenario_close.setter
    def on_scenario_close(self, callback):
        self._events["OnScenarioClose"]._safe_assign(callback)

    @property
    def OnScenarioSave(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnScenarioSave(Path:str) -> None]"""
        return self._events["OnScenarioSave"]

    @OnScenarioSave.setter
    def OnScenarioSave(self, callback):
        self._events["OnScenarioSave"]._safe_assign(callback)

    @property
    def on_log_message(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnLogMessage(message:str, msgType:"LogMessageType", errorCode:int, fileName:str, lineNo:int, dispID:"LogMessageDisplayID") -> None]"""
        return self._events["OnLogMessage"]

    @on_log_message.setter
    def on_log_message(self, callback):
        self._events["OnLogMessage"]._safe_assign(callback)

    @property
    def on_anim_update(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnAnimUpdate(timeEpSec:float) -> None]"""
        return self._events["OnAnimUpdate"]

    @on_anim_update.setter
    def on_anim_update(self, callback):
        self._events["OnAnimUpdate"]._safe_assign(callback)

    @property
    def on_new_globe_ctrl_request(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewGlobeCtrlRequest(SceneID:int) -> None]"""
        return self._events["OnNewGlobeCtrlRequest"]

    @on_new_globe_ctrl_request.setter
    def on_new_globe_ctrl_request(self, callback):
        self._events["OnNewGlobeCtrlRequest"]._safe_assign(callback)

    @property
    def on_new_map_ctrl_request(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewMapCtrlRequest(WinID:int) -> None]"""
        return self._events["OnNewMapCtrlRequest"]

    @on_new_map_ctrl_request.setter
    def on_new_map_ctrl_request(self, callback):
        self._events["OnNewMapCtrlRequest"]._safe_assign(callback)

    @property
    def on_before_new_scenario(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeforeNewScenario(Scenario:str) -> None]"""
        return self._events["OnBeforeNewScenario"]

    @on_before_new_scenario.setter
    def on_before_new_scenario(self, callback):
        self._events["OnBeforeNewScenario"]._safe_assign(callback)

    @property
    def on_before_load_scenario(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeforeLoadScenario(Scenario:str) -> None]"""
        return self._events["OnBeforeLoadScenario"]

    @on_before_load_scenario.setter
    def on_before_load_scenario(self, callback):
        self._events["OnBeforeLoadScenario"]._safe_assign(callback)

    @property
    def on_begin_scenario_close(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnBeginScenarioClose() -> None]"""
        return self._events["OnBeginScenarioClose"]

    @on_begin_scenario_close.setter
    def on_begin_scenario_close(self, callback):
        self._events["OnBeginScenarioClose"]._safe_assign(callback)

    @property
    def on_new_gfx_analysis_ctrl_request(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnNewGfxAnalysisCtrlRequest(SceneID:int, GfxAnalysisMode:"Graphics2DAnalysisMode") -> None]"""
        return self._events["OnNewGfxAnalysisCtrlRequest"]

    @on_new_gfx_analysis_ctrl_request.setter
    def on_new_gfx_analysis_ctrl_request(self, callback):
        self._events["OnNewGfxAnalysisCtrlRequest"]._safe_assign(callback)

    @property
    def on_ssl_certificate_server_error(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnSSLCertificateServerError(pArgs:"STKXSSLCertificateErrorEventArgs") -> None]"""
        return self._events["OnSSLCertificateServerError"]

    @on_ssl_certificate_server_error.setter
    def on_ssl_certificate_server_error(self, callback):
        self._events["OnSSLCertificateServerError"]._safe_assign(callback)

    @property
    def on_con_control_quit_received(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnConControlQuitReceived(pArgs:"STKXConControlQuitReceivedEventArgs") -> None]"""
        return self._events["OnConControlQuitReceived"]

    @on_con_control_quit_received.setter
    def on_con_control_quit_received(self, callback):
        self._events["OnConControlQuitReceived"]._safe_assign(callback)


################################################################################
#          ActiveX controls
################################################################################

class IUiAxStockEventHandler(object):
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
        if attrname in IUiAxStockEventHandler.__dict__ and type(IUiAxStockEventHandler.__dict__[attrname]) == property:
            IUiAxStockEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise AttributeError(attrname + " is not a recognized event in IAgUiAxStockEvents.")

    @property
    def key_down(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyDown(KeyCode:int, Shift:int) -> None]"""
        return self._events["KeyDown"]

    @key_down.setter
    def key_down(self, callback):
        self._events["KeyDown"]._safe_assign(callback)

    @property
    def key_press(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyPress(KeyAscii:int) -> None]"""
        return self._events["KeyPress"]

    @key_press.setter
    def key_press(self, callback):
        self._events["KeyPress"]._safe_assign(callback)

    @property
    def key_up(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [KeyUp(KeyCode:int, Shift:int) -> None]"""
        return self._events["KeyUp"]

    @key_up.setter
    def key_up(self, callback):
        self._events["KeyUp"]._safe_assign(callback)

    @property
    def click(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [Click() -> None]"""
        return self._events["Click"]

    @click.setter
    def click(self, callback):
        self._events["Click"]._safe_assign(callback)

    @property
    def dbl_click(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [DblClick() -> None]"""
        return self._events["DblClick"]

    @dbl_click.setter
    def dbl_click(self, callback):
        self._events["DblClick"]._safe_assign(callback)

    @property
    def mouse_down(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseDown(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._events["MouseDown"]

    @mouse_down.setter
    def mouse_down(self, callback):
        self._events["MouseDown"]._safe_assign(callback)

    @property
    def mouse_move(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseMove(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._events["MouseMove"]

    @mouse_move.setter
    def mouse_move(self, callback):
        self._events["MouseMove"]._safe_assign(callback)

    @property
    def mouse_up(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseUp(Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._events["MouseUp"]

    @mouse_up.setter
    def mouse_up(self, callback):
        self._events["MouseUp"]._safe_assign(callback)

    @property
    def ole_drag_drop(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OLEDragDrop(Data:"DataObject", Effect:int, Button:int, Shift:int, X:int, Y:int) -> None]"""
        return self._events["OLEDragDrop"]

    @ole_drag_drop.setter
    def ole_drag_drop(self, callback):
        self._events["OLEDragDrop"]._safe_assign(callback)

    @property
    def mouse_wheel(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [MouseWheel(Button:int, Shift:int, Delta:int, X:int, Y:int) -> None]"""
        return self._events["MouseWheel"]

    @mouse_wheel.setter
    def mouse_wheel(self, callback):
        self._events["MouseWheel"]._safe_assign(callback)


class IUiAxGraphics2DCntrlEventHandler(STKEventSubscriber, IUiAxStockEventHandler):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        IUiAxStockEventHandler.__init__(self)
        if type(interface)==IUnknown:
            impl = IGraphics2DControlEventCOMHandler(interface, self._events)
        elif type(interface)==GrpcInterface:
            raise RuntimeError(f"Active X Control events are not available with gRPC.")
        else:
            raise RuntimeError(f"Unexpected type {type(interface)}, cannot create IUiAxGraphics2DCntrlEventHandler.")
        STKEventSubscriber.__init__(self, impl)

    def __del__(self):
        STKEventSubscriber.__del__(self)

    def __setattr__(self, attrname, value):
        try:
            IUiAxStockEventHandler.__setattr__(self, attrname, value)
        except:
            if attrname in IUiAxGraphics2DCntrlEventHandler.__dict__ and type(IUiAxGraphics2DCntrlEventHandler.__dict__[attrname]) == property:
                IUiAxGraphics2DCntrlEventHandler.__dict__[attrname].__set__(self, value)
            else:
                raise AttributeError(attrname + " is not a recognized event in Graphics2DControlBaseEvents.")


class IUiAxGraphics3DCntrlEventHandler(STKEventSubscriber, IUiAxStockEventHandler):
    def __init__(self, interface):
        self.__dict__["_events"] = {}
        self._events["OnObjectEditingStart"]     = _STKEvent()
        self._events["OnObjectEditingApply"]     = _STKEvent()
        self._events["OnObjectEditingCancel"]    = _STKEvent()
        self._events["OnObjectEditingStop"]      = _STKEvent()
        IUiAxStockEventHandler.__init__(self)
        if type(interface)==IUnknown:
            impl = IGraphics3DControlEventCOMHandler(interface, self._events)
        elif type(interface)==GrpcInterface:
            raise RuntimeError(f"Active X Control events are not available with gRPC.")
        else:
            raise RuntimeError(f"Unexpected type {type(interface)}, cannot create IUiAxGraphics3DCntrlEventHandler.")
        STKEventSubscriber.__init__(self, impl)

    def __del__(self):
        STKEventSubscriber.__del__(self)

    def __setattr__(self, attrname, value):
        try:
            IUiAxStockEventHandler.__setattr__(self, attrname, value)
        except:
            if attrname in IUiAxGraphics3DCntrlEventHandler.__dict__ and type(IUiAxGraphics3DCntrlEventHandler.__dict__[attrname]) == property:
                IUiAxGraphics3DCntrlEventHandler.__dict__[attrname].__set__(self, value)
            else:
                raise AttributeError(attrname + " is not a recognized event in Graphics3DControlBaseEvents.")

    @property
    def on_object_editing_start(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingStart(Path:str) -> None]"""
        return self._events["OnObjectEditingStart"]

    @on_object_editing_start.setter
    def on_object_editing_start(self, callback):
        self._events["OnObjectEditingStart"]._safe_assign(callback)

    @property
    def on_object_editing_apply(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingApply(Path:str) -> None]"""
        return self._events["OnObjectEditingApply"]

    @on_object_editing_apply.setter
    def on_object_editing_apply(self, callback):
        self._events["OnObjectEditingApply"]._safe_assign(callback)

    @property
    def on_object_editing_cancel(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingCancel(Path:str) -> None]"""
        return self._events["OnObjectEditingCancel"]

    @on_object_editing_cancel.setter
    def on_object_editing_cancel(self, callback):
        self._events["OnObjectEditingCancel"]._safe_assign(callback)

    @property
    def on_object_editing_stop(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [OnObjectEditingStop(Path:str) -> None]"""
        return self._events["OnObjectEditingStop"]

    @on_object_editing_stop.setter
    def on_object_editing_stop(self, callback):
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
        elif type(interface)==GrpcInterface:
            impl = ISceneEventGrpcHandler(interface, self._events)
        else:
            raise RuntimeError(f"Unexpected type {type(interface)}, cannot create ISceneEventHandler.")
        STKEventSubscriber.__init__(self, impl)

    def __del__(self):
        STKEventSubscriber.__del__(self)

    def __setattr__(self, attrname, value):
        if attrname in ISceneEventHandler.__dict__ and type(ISceneEventHandler.__dict__[attrname]) == property:
            ISceneEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise AttributeError(attrname + " is not a recognized event in SceneEvents.")

    @property
    def rendering(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [Rendering(Sender:typing.Any, Args:"RenderingEventArgs") -> None]"""
        return self._events["Rendering"]

    @rendering.setter
    def rendering(self, callback):
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
        elif type(interface)==GrpcInterface:
            impl = IKmlGraphicsEventGrpcHandler(interface, self._events)
        else:
            raise RuntimeError(f"Unexpected type {type(interface)}, cannot create IKmlGraphicsEventHandler.")
        STKEventSubscriber.__init__(self, impl)

    def __del__(self):
        STKEventSubscriber.__del__(self)

    def __setattr__(self, attrname, value):
        if attrname in IKmlGraphicsEventHandler.__dict__ and type(IKmlGraphicsEventHandler.__dict__[attrname]) == property:
            IKmlGraphicsEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise AttributeError(attrname + " is not a recognized event in KmlGraphicsEvents.")

    @property
    def document_loaded(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [DocumentLoaded(Sender:typing.Any, Args:"KmlDocumentLoadedEventArgs") -> None]"""
        return self._events["DocumentLoaded"]

    @document_loaded.setter
    def document_loaded(self, callback):
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
        elif type(interface)==GrpcInterface:
            impl = IImageCollectionEventGrpcHandler(interface, self._events)
        else:
            raise RuntimeError(f"Unexpected type {type(interface)}, cannot create IImageCollectionEventHandler.")
        STKEventSubscriber.__init__(self, impl)

    def __del__(self):
        STKEventSubscriber.__del__(self)

    def __setattr__(self, attrname, value):
        if attrname in IImageCollectionEventHandler.__dict__ and type(IImageCollectionEventHandler.__dict__[attrname]) == property:
            IImageCollectionEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise AttributeError(attrname + " is not a recognized event in ImageCollectionEvents.")

    @property
    def add_complete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [AddComplete(Sender:typing.Any, Args:"GlobeImageOverlayAddCompleteEventArgs") -> None]"""
        return self._events["AddComplete"]

    @add_complete.setter
    def add_complete(self, callback):
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
        elif type(interface)==GrpcInterface:
            impl = ITerrainOverlayCollectionEventGrpcHandler(interface, self._events)
        else:
            raise RuntimeError(f"Unexpected type {type(interface)}, cannot create ITerrainOverlayCollectionEventHandler.")
        STKEventSubscriber.__init__(self, impl)

    def __del__(self):
        STKEventSubscriber.__del__(self)

    def __setattr__(self, attrname, value):
        if attrname in ITerrainOverlayCollectionEventHandler.__dict__ and type(ITerrainOverlayCollectionEventHandler.__dict__[attrname]) == property:
            ITerrainOverlayCollectionEventHandler.__dict__[attrname].__set__(self, value)
        else:
            raise AttributeError(attrname + " is not a recognized event in TerrainOverlayCollectionEvents.")

    @property
    def add_complete(self):
        """Use operator += to register or operator -= to unregister callbacks with the signature [AddComplete(Sender:typing.Any, Args:"TerrainOverlayAddCompleteEventArgs") -> None]"""
        return self._events["AddComplete"]

    @add_complete.setter
    def add_complete(self, callback):
        self._events["AddComplete"]._safe_assign(callback)