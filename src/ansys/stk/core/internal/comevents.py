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

__all__ = [ "COMEventHandlerImpl",
            "ISTKObjectRootEventCOMHandler",
            "ISTKXApplicationEventCOMHandler",
            "IGraphics2DControlEventCOMHandler",
            "IGraphics3DControlEventCOMHandler",
            "ISceneEventCOMHandler",
            "IKmlGraphicsEventCOMHandler",
            "IImageCollectionEventCOMHandler",
            "ITerrainOverlayCollectionEventCOMHandler"]

import os
from ctypes import CFUNCTYPE, POINTER, c_void_p, cast, addressof, Structure

from .                       import marshall     as agmarshall
from .                       import coclassutil  as agcls
from .comutil import (BSTR, DISPID, DispParams, DOUBLE, ExcepInfo, E_NOINTERFACE, E_NOTIMPL, GUID,
                      HRESULT, IDispatch, IUnknown, LCID, LONG, LPOLESTR, OLE_XPOS_PIXELS,
                      OLE_YPOS_PIXELS, PVOID, REFIID, SHORT, S_OK, UINT, ULONG, Variant, WORD,
                      pointer)

class COMEventHandlerImpl(object):
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

    def _add_ref(self, pThis:PVOID) -> int:
        return 1

    def _release(self, pThis:PVOID) -> int:
        return 0

    def _get_type_info_count(self, pThis:PVOID, pctinfo:POINTER(UINT)) -> int:
        return E_NOTIMPL

    def _get_type_info(self, pThis:PVOID, iTInfo:UINT, lcid:LCID, ppTInfo:POINTER(PVOID)) -> int:
        return E_NOTIMPL

    def _get_ids_of_names(self, pThis:PVOID, riid:REFIID, rgszNames:POINTER(LPOLESTR), cNames:UINT, lcid:LCID, rgDispId:POINTER(DISPID)) -> int:
        return E_NOTIMPL

    def subscribe(self):
        if self._connection_id is None:
            self._connection_id = self._cp.advise(addressof(self._base_pUnkSink))

    def unsubscribe(self):
        if self._connection_id is not None:
            self._cp.unadvise(self._connection_id)
            self._connection_id = None

################################################################################
#          IAgStkObjectRootEvents
################################################################################

class _STKObjectRootRawEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",               c_void_p),
                 ("IUnknown2",               c_void_p),
                 ("IUnknown3",               c_void_p),
                 ("on_scenario_new",           c_void_p),
                 ("on_scenario_load",          c_void_p),
                 ("on_scenario_close",         c_void_p),
                 ("on_scenario_save",          c_void_p),
                 ("on_log_message",            c_void_p),
                 ("on_anim_update",            c_void_p),
                 ("on_stk_object_added",        c_void_p),
                 ("on_stk_object_deleted",      c_void_p),
                 ("on_stk_object_renamed",      c_void_p),
                 ("on_animation_playback",     c_void_p),
                 ("on_animation_rewind",       c_void_p),
                 ("on_animation_pause",        c_void_p),
                 ("on_scenario_before_save",    c_void_p),
                 ("on_animation_step",         c_void_p),
                 ("on_animation_step_back",     c_void_p),
                 ("on_animation_slower",       c_void_p),
                 ("on_animation_faster",       c_void_p),
                 ("on_percent_complete_update", c_void_p),
                 ("on_percent_complete_end",    c_void_p),
                 ("on_percent_complete_begin",  c_void_p),
                 ("on_stk_object_changed",      c_void_p),
                 ("on_scenario_before_close",   c_void_p),
                 ("on_stk_object_pre_delete",    c_void_p)]

class _STKObjectRootRawEvents2UnkSink(Structure):
    _fields_ = [ ("IUnknown1",                  c_void_p),
                 ("IUnknown2",                  c_void_p),
                 ("IUnknown3",                  c_void_p),
                 ("on_stk_object_start_3d_editing",  c_void_p),
                 ("on_stk_object_stop_3d_editing",   c_void_p),
                 ("on_stk_object_apply_3d_editing",  c_void_p),
                 ("on_stk_object_cancel_3d_editing", c_void_p),
                 ("on_stk_object_pre_cut",          c_void_p),
                 ("on_stk_object_copy",            c_void_p),
                 ("on_stk_object_paste",           c_void_p) ]

class ISTKObjectRootEventCOMHandler(COMEventHandlerImpl):
    _IID_IAgStkObjectRootEvents     = GUID.from_registry_format("{3151628E-C9EC-43F8-B111-05705D64AB7A}")
    _IID_IAgStkObjectRootRawEvents  = GUID.from_registry_format("{250F722D-C0FF-44D4-8B4E-EC09499D5345}")
    _IID_IAgStkObjectRootRawEvents2 = GUID.from_registry_format("{02EE4178-1311-4BF7-B547-1DA906D8393F}")

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable1()
        self._init_vtable2()
        COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink1, ISTKObjectRootEventCOMHandler._IID_IAgStkObjectRootEvents)

    def _init_vtable1(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]           = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown2"]           = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown3"]           = CFUNCTYPE(ULONG, PVOID)(self._release)
        else:
            self.__dict__["_cfunc_IUnknown3"]           = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown1"]           = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown2"]           = CFUNCTYPE(ULONG, PVOID)(self._release)
        self.__dict__["_cfunc_OnScenarioNew"]           = CFUNCTYPE(None, PVOID, BSTR)(self._on_scenario_new)
        self.__dict__["_cfunc_OnScenarioLoad"]          = CFUNCTYPE(None, PVOID, BSTR)(self._on_scenario_load)
        self.__dict__["_cfunc_OnScenarioClose"]         = CFUNCTYPE(None, PVOID)(self._on_scenario_close)
        self.__dict__["_cfunc_OnScenarioSave"]          = CFUNCTYPE(None, PVOID, BSTR)(self._on_scenario_save)
        self.__dict__["_cfunc_OnLogMessage"]            = CFUNCTYPE(None, PVOID, BSTR, LONG, LONG, BSTR, LONG, LONG)(self._on_log_message)
        self.__dict__["_cfunc_OnAnimUpdate"]            = CFUNCTYPE(None, PVOID, DOUBLE)(self._on_anim_update)
        self.__dict__["_cfunc_OnStkObjectAdded"]        = CFUNCTYPE(None, PVOID, Variant)(self._on_stk_object_added)
        self.__dict__["_cfunc_OnStkObjectDeleted"]      = CFUNCTYPE(None, PVOID, Variant)(self._on_stk_object_deleted)
        self.__dict__["_cfunc_OnStkObjectRenamed"]      = CFUNCTYPE(None, PVOID, Variant, BSTR, BSTR)(self._on_stk_object_renamed)
        self.__dict__["_cfunc_OnAnimationPlayback"]     = CFUNCTYPE(None, PVOID, DOUBLE, LONG, LONG)(self._on_animation_playback)
        self.__dict__["_cfunc_OnAnimationRewind"]       = CFUNCTYPE(None, PVOID)(self._on_animation_rewind)
        self.__dict__["_cfunc_OnAnimationPause"]        = CFUNCTYPE(None, PVOID, DOUBLE)(self._on_animation_pause)
        self.__dict__["_cfunc_OnScenarioBeforeSave"]    = CFUNCTYPE(None, PVOID, PVOID)(self._on_scenario_before_save)
        self.__dict__["_cfunc_OnAnimationStep"]         = CFUNCTYPE(None, PVOID, DOUBLE)(self._on_animation_step)
        self.__dict__["_cfunc_OnAnimationStepBack"]     = CFUNCTYPE(None, PVOID, DOUBLE)(self._on_animation_step_back)
        self.__dict__["_cfunc_OnAnimationSlower"]       = CFUNCTYPE(None, PVOID)(self._on_animation_slower)
        self.__dict__["_cfunc_OnAnimationFaster"]       = CFUNCTYPE(None, PVOID)(self._on_animation_faster)
        self.__dict__["_cfunc_OnPercentCompleteUpdate"] = CFUNCTYPE(None, PVOID, PVOID)(self._on_percent_complete_update)
        self.__dict__["_cfunc_OnPercentCompleteEnd"]    = CFUNCTYPE(None, PVOID)(self._on_percent_complete_end)
        self.__dict__["_cfunc_OnPercentCompleteBegin"]  = CFUNCTYPE(None, PVOID)(self._on_percent_complete_begin)
        self.__dict__["_cfunc_OnStkObjectChanged"]      = CFUNCTYPE(None, PVOID, PVOID)(self._on_stk_object_changed)
        self.__dict__["_cfunc_OnScenarioBeforeClose"]   = CFUNCTYPE(None, PVOID)(self._on_scenario_before_close)
        self.__dict__["_cfunc_OnStkObjectPreDelete"]    = CFUNCTYPE(None, PVOID, PVOID)(self._on_stk_object_pre_delete)

        self.__dict__["_vtable1"] = _STKObjectRootRawEventsUnkSink( *[cast(self._cfunc_IUnknown1,               c_void_p),
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
        self.__dict__["_cfunc_OnStkObjectStart3dEditing"]  = CFUNCTYPE(None, PVOID, BSTR)(self._on_stk_object_start_3d_editing)
        self.__dict__["_cfunc_OnStkObjectStop3dEditing"]   = CFUNCTYPE(None, PVOID, BSTR)(self._on_stk_object_stop_3d_editing)
        self.__dict__["_cfunc_OnStkObjectApply3dEditing"]  = CFUNCTYPE(None, PVOID, BSTR)(self._on_stk_object_apply_3d_editing)
        self.__dict__["_cfunc_OnStkObjectCancel3dEditing"] = CFUNCTYPE(None, PVOID, BSTR)(self._on_stk_object_cancel_3d_editing)
        self.__dict__["_cfunc_OnStkObjectPreCut"]          = CFUNCTYPE(None, PVOID, PVOID)(self._on_stk_object_pre_cut)
        self.__dict__["_cfunc_OnStkObjectCopy"]            = CFUNCTYPE(None, PVOID, PVOID)(self._on_stk_object_copy)
        self.__dict__["_cfunc_OnStkObjectPaste"]           = CFUNCTYPE(None, PVOID, PVOID)(self._on_stk_object_paste)

        self.__dict__["_vtable2"] = _STKObjectRootRawEvents2UnkSink( *[cast(self._cfunc_IUnknown1,                  c_void_p),
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

    def _query_interface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == ISTKObjectRootEventCOMHandler._IID_IAgStkObjectRootEvents:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == ISTKObjectRootEventCOMHandler._IID_IAgStkObjectRootRawEvents:
            ppvObject[0] = addressof(self._pUnkSink1)
            return S_OK
        elif iid == ISTKObjectRootEventCOMHandler._IID_IAgStkObjectRootRawEvents2:
            ppvObject[0] = addressof(self._pUnkSink2)
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _on_scenario_new(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioNew"]._callbacks:
            callback(path)

    def _on_scenario_load(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioLoad"]._callbacks:
            callback(path)

    def _on_scenario_close(self, pThis:PVOID) -> None:
        for callback in self._events["OnScenarioClose"]._callbacks:
            callback()

    def _on_scenario_save(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioSave"]._callbacks:
            callback(path)

    def _on_log_message(self, pThis:PVOID, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._events["OnLogMessage"]._callbacks:
            callback(message, agcls.AgTypeNameMap["LogMessageType"](msgType), errorCode, fileName, lineNo, agcls.AgTypeNameMap["LogMessageDisplayID"](dispID))

    def _on_anim_update(self, pThis:PVOID, timeEpSec:float) -> None:
        for callback in self._events["OnAnimUpdate"]._callbacks:
            callback(timeEpSec)

    def _on_stk_object_added(self, pThis:PVOID, Sender:Variant) -> None:
        for callback in self._events["OnStkObjectAdded"]._callbacks:
            with agmarshall.VariantArg(Sender) as arg_Sender:
                callback(arg_Sender.python_val)

    def _on_stk_object_deleted(self, pThis:PVOID, Sender:Variant) -> None:
        for callback in self._events["OnStkObjectDeleted"]._callbacks:
            with agmarshall.VariantArg(Sender) as arg_Sender:
                callback(arg_Sender.python_val)

    def _on_stk_object_renamed(self, pThis:PVOID, Sender:Variant, OldPath:str, NewPath:str) -> None:
        for callback in self._events["OnStkObjectRenamed"]._callbacks:
            with agmarshall.VariantArg(Sender) as arg_Sender:
                callback(arg_Sender.python_val, OldPath, NewPath)

    def _on_animation_playback(self, pThis:PVOID, CurrentTime:float, eAction:int, eDirection:int) -> None:
        for callback in self._events["OnAnimationPlayback"]._callbacks:
            callback(CurrentTime, agcls.AgTypeNameMap["AnimationActionType"](eAction), agcls.AgTypeNameMap["AnimationDirectionType"](eDirection.python_val))

    def _on_animation_rewind(self, pThis:PVOID) -> None:
        for callback in self._events["OnAnimationRewind"]._callbacks:
            callback()

    def _on_animation_pause(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationPause"]._callbacks:
            callback(CurrentTime)

    def _on_scenario_before_save(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnScenarioBeforeSave"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["ScenarioBeforeSaveEventArguments"]) as arg_pArgs:
                callback(arg_pArgs.python_val)

    def _on_animation_step(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationStep"]._callbacks:
            callback(CurrentTime)

    def _on_animation_step_back(self, pThis:PVOID, CurrentTime:float) -> None:
        for callback in self._events["OnAnimationStepBack"]._callbacks:
            callback(CurrentTime)

    def _on_animation_slower(self, pThis:PVOID) -> None:
        for callback in self._events["OnAnimationSlower"]._callbacks:
            callback()

    def _on_animation_faster(self, pThis:PVOID) -> None:
        for callback in self._events["OnAnimationFaster"]._callbacks:
            callback()

    def _on_percent_complete_update(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnPercentCompleteUpdate"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["ProgressBarEventArguments"]) as arg_pArgs:
                callback(arg_pArgs.python_val)

    def _on_percent_complete_end(self, pThis:PVOID) -> None:
        for callback in self._events["OnPercentCompleteEnd"]._callbacks:
            callback()

    def _on_percent_complete_begin(self, pThis:PVOID) -> None:
        for callback in self._events["OnPercentCompleteBegin"]._callbacks:
            callback()

    def _on_stk_object_changed(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectChanged"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["STKObjectChangedEventArguments"]) as arg_pArgs:
                callback(arg_pArgs.python_val)

    def _on_scenario_before_close(self, pThis:PVOID) -> None:
        for callback in self._events["OnScenarioBeforeClose"]._callbacks:
            callback()

    def _on_stk_object_pre_delete(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectPreDelete"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["STKObjectPreDeleteEventArguments"]) as arg_pArgs:
                callback(arg_pArgs.python_val)

    def _on_stk_object_start_3d_editing(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnStkObjectStart3dEditing"]._callbacks:
            callback(path)

    def _on_stk_object_stop_3d_editing(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnStkObjectStop3dEditing"]._callbacks:
            callback(path)

    def _on_stk_object_apply_3d_editing(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnStkObjectApply3dEditing"]._callbacks:
            callback(path)

    def _on_stk_object_cancel_3d_editing(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnStkObjectCancel3dEditing"]._callbacks:
            callback(path)

    def _on_stk_object_pre_cut(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectPreCut"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["STKObjectCutCopyPasteEventArguments"]) as arg_pArgs:
                callback(arg_pArgs.python_val)

    def _on_stk_object_copy(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectCopy"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["STKObjectCutCopyPasteEventArguments"]) as arg_pArgs:
                callback(arg_pArgs.python_val)

    def _on_stk_object_paste(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnStkObjectPaste"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["STKObjectCutCopyPasteEventArguments"]) as arg_pArgs:
                callback(arg_pArgs.python_val)


################################################################################
#          IAgSTKXApplicationEvents
################################################################################

class _STKXApplicationEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",                   c_void_p),
                 ("IUnknown2",                   c_void_p),
                 ("IUnknown3",                   c_void_p),
                 ("on_scenario_new",               c_void_p),
                 ("on_scenario_load",              c_void_p),
                 ("on_scenario_close",             c_void_p),
                 ("on_scenario_save",              c_void_p),
                 ("on_log_message",                c_void_p),
                 ("on_anim_update",                c_void_p),
                 ("on_new_globe_ctrl_request",       c_void_p),
                 ("on_new_map_ctrl_request",         c_void_p),
                 ("on_before_new_scenario",         c_void_p),
                 ("on_before_load_scenario",        c_void_p),
                 ("on_begin_scenario_close",        c_void_p),
                 ("on_new_gfx_analysis_ctrl_request", c_void_p),
                 ("on_ssl_certificate_server_error", c_void_p),
                 ("on_con_control_quit_received",    c_void_p) ]

class ISTKXApplicationEventCOMHandler(COMEventHandlerImpl):
    _IID_IAgSTKXApplicationRawEvents = GUID.from_registry_format("{9CC75BA6-DA22-4C2E-B05D-C460C71C6ACD}")
    _IID_IAgSTKXApplicationEvents    = GUID.from_registry_format("{5A049BEE-0D35-45DE-AA40-9898AA7314BF}")

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, ISTKXApplicationEventCOMHandler._IID_IAgSTKXApplicationEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]               = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown2"]               = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown3"]               = CFUNCTYPE(ULONG, PVOID)(self._release)
        else:
            self.__dict__["_cfunc_IUnknown3"]               = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown1"]               = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown2"]               = CFUNCTYPE(ULONG, PVOID)(self._release)
        self.__dict__["_cfunc_OnScenarioNew"]               = CFUNCTYPE(None, PVOID, BSTR)(self._on_scenario_new)
        self.__dict__["_cfunc_OnScenarioLoad"]              = CFUNCTYPE(None, PVOID, BSTR)(self._on_scenario_load)
        self.__dict__["_cfunc_OnScenarioClose"]             = CFUNCTYPE(None, PVOID)(self._on_scenario_close)
        self.__dict__["_cfunc_OnScenarioSave"]              = CFUNCTYPE(None, PVOID, BSTR)(self._on_scenario_save)
        self.__dict__["_cfunc_OnLogMessage"]                = CFUNCTYPE(None, PVOID, BSTR, LONG, LONG, BSTR, LONG, LONG)(self._on_log_message)
        self.__dict__["_cfunc_OnAnimUpdate"]                = CFUNCTYPE(HRESULT, PVOID, DOUBLE)(self._on_anim_update)
        self.__dict__["_cfunc_OnNewGlobeCtrlRequest"]       = CFUNCTYPE(None, PVOID, LONG)(self._on_new_globe_ctrl_request)
        self.__dict__["_cfunc_OnNewMapCtrlRequest"]         = CFUNCTYPE(None, PVOID, LONG)(self._on_new_map_ctrl_request)
        self.__dict__["_cfunc_OnBeforeNewScenario"]         = CFUNCTYPE(None, PVOID, BSTR)(self._on_before_new_scenario)
        self.__dict__["_cfunc_OnBeforeLoadScenario"]        = CFUNCTYPE(None, PVOID, BSTR)(self._on_before_load_scenario)
        self.__dict__["_cfunc_OnBeginScenarioClose"]        = CFUNCTYPE(None, PVOID)(self._on_begin_scenario_close)
        self.__dict__["_cfunc_OnNewGfxAnalysisCtrlRequest"] = CFUNCTYPE(None, PVOID, LONG, LONG)(self._on_new_gfx_analysis_ctrl_request)
        self.__dict__["_cfunc_OnSSLCertificateServerError"] = CFUNCTYPE(None, PVOID, PVOID)(self._on_ssl_certificate_server_error)
        self.__dict__["_cfunc_OnConControlQuitReceived"]    = CFUNCTYPE(None, PVOID, PVOID)(self._on_con_control_quit_received)

        self.__dict__["_vtable"] = _STKXApplicationEventsUnkSink( *[cast(self._cfunc_IUnknown1,                   c_void_p),
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

    def _query_interface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == COMEventHandlerImpl._IID_IUnknown:
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

    def _on_scenario_new(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioNew"]._callbacks:
            callback(path)

    def _on_scenario_load(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioLoad"]._callbacks:
            callback(path)

    def _on_scenario_close(self, pThis:PVOID) -> None:
        for callback in self._events["OnScenarioClose"]._callbacks:
            callback()

    def _on_scenario_save(self, pThis:PVOID, path:str) -> None:
        for callback in self._events["OnScenarioSave"]._callbacks:
            callback(path)

    def _on_log_message(self, pThis:PVOID, message:str, msgType:int, errorCode:int, fileName:str, lineNo:int, dispID:int) -> None:
        for callback in self._events["OnLogMessage"]._callbacks:
            callback(message, agcls.AgTypeNameMap["LogMessageType"](msgType), errorCode, fileName, lineNo, agcls.AgTypeNameMap["LogMessageDisplayID"](dispID))

    def _on_anim_update(self, pThis:PVOID, timeEpSec:float) -> int:
        for callback in self._events["OnAnimUpdate"]._callbacks:
            callback(timeEpSec)
        return S_OK

    def _on_new_globe_ctrl_request(self, pThis:PVOID, SceneID:int) -> None:
        for callback in self._events["OnNewGlobeCtrlRequest"]._callbacks:
            callback(SceneID)

    def _on_new_map_ctrl_request(self, pThis:PVOID, WinID:int) -> None:
        for callback in self._events["OnNewMapCtrlRequest"]._callbacks:
            callback(WinID)

    def _on_before_new_scenario(self, pThis:PVOID, Scenario:str) -> None:
        for callback in self._events["OnBeforeNewScenario"]._callbacks:
            callback(Scenario)

    def _on_before_load_scenario(self, pThis:PVOID, Scenario:str) -> None:
        for callback in self._events["OnBeforeLoadScenario"]._callbacks:
            callback(Scenario)

    def _on_begin_scenario_close(self, pThis:PVOID) -> None:
        for callback in self._events["OnBeginScenarioClose"]._callbacks:
            callback()

    def _on_new_gfx_analysis_ctrl_request(self, pThis:PVOID, SceneID:int, GfxAnalysisMode:int) -> None:
        for callback in self._events["OnNewGfxAnalysisCtrlRequest"]._callbacks:
            callback(SceneID, agcls.AgTypeNameMap["Graphics2DAnalysisMode"](GfxAnalysisMode))

    def _on_ssl_certificate_server_error(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnSSLCertificateServerError"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["STKXSSLCertificateErrorEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)

    def _on_con_control_quit_received(self, pThis:PVOID, pArgs:PVOID) -> None:
        for callback in self._events["OnConControlQuitReceived"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(pArgs, agcls.AgTypeNameMap["STKXConControlQuitReceivedEventArgs"]) as arg_pArgs:
                callback(arg_pArgs.python_val)


################################################################################
#          ActiveX controls
################################################################################

class _UiAxStockEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",   c_void_p),
                 ("IUnknown2",   c_void_p),
                 ("IUnknown3",   c_void_p),
                 ("key_down",     c_void_p),
                 ("key_press",    c_void_p),
                 ("key_up",       c_void_p),
                 ("click",       c_void_p),
                 ("dbl_click",    c_void_p),
                 ("mouse_down",   c_void_p),
                 ("mouse_move",   c_void_p),
                 ("mouse_up",     c_void_p),
                 ("ole_drag_drop", c_void_p),
                 ("mouse_wheel",  c_void_p)]

class _Graphics3DControlEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",             c_void_p),
                 ("IUnknown2",             c_void_p),
                 ("IUnknown3",             c_void_p),
                 ("key_down",               c_void_p),
                 ("key_press",              c_void_p),
                 ("key_up",                 c_void_p),
                 ("click",                 c_void_p),
                 ("dbl_click",              c_void_p),
                 ("mouse_down",             c_void_p),
                 ("mouse_move",             c_void_p),
                 ("mouse_up",               c_void_p),
                 ("ole_drag_drop",           c_void_p),
                 ("mouse_wheel",            c_void_p),
                 ("on_object_editing_start",  c_void_p),
                 ("on_object_editing_apply",  c_void_p),
                 ("on_object_editing_cancel", c_void_p),
                 ("on_object_editing_stop",   c_void_p)]

class IUiAxStockEventCOMHandler(object):
    _IID_IAgUiAxStockRawEvents   = GUID.from_registry_format("{00C151C5-3214-452A-B88A-9DB558F5A746}")

    def __init__(self, events:dict):
        self._events = events
        self.__dict__["_cfunc_KeyDown"]     = CFUNCTYPE(HRESULT, PVOID, POINTER(SHORT), SHORT)(self._key_down)
        self.__dict__["_cfunc_KeyPress"]    = CFUNCTYPE(HRESULT, PVOID, POINTER(SHORT))(self._key_press)
        self.__dict__["_cfunc_KeyUp"]       = CFUNCTYPE(HRESULT, PVOID, POINTER(SHORT), SHORT)(self._key_up)
        self.__dict__["_cfunc_Click"]       = CFUNCTYPE(HRESULT, PVOID)(self._click)
        self.__dict__["_cfunc_DblClick"]    = CFUNCTYPE(HRESULT, PVOID)(self._dbl_click)
        self.__dict__["_cfunc_MouseDown"]   = CFUNCTYPE(HRESULT, PVOID, SHORT, SHORT, OLE_XPOS_PIXELS, OLE_YPOS_PIXELS)(self._mouse_down)
        self.__dict__["_cfunc_MouseMove"]   = CFUNCTYPE(HRESULT, PVOID, SHORT, SHORT, OLE_XPOS_PIXELS, OLE_YPOS_PIXELS)(self._mouse_move)
        self.__dict__["_cfunc_MouseUp"]     = CFUNCTYPE(HRESULT, PVOID, SHORT, SHORT, OLE_XPOS_PIXELS, OLE_YPOS_PIXELS)(self._mouse_up)
        self.__dict__["_cfunc_OLEDragDrop"] = CFUNCTYPE(HRESULT, PVOID, PVOID, LONG, SHORT, SHORT, LONG, LONG)(self._ole_drag_drop)
        self.__dict__["_cfunc_MouseWheel"]  = CFUNCTYPE(HRESULT, PVOID, SHORT, SHORT, SHORT, OLE_XPOS_PIXELS, OLE_YPOS_PIXELS)(self._mouse_wheel)

    def _mouse_wheel(self, pThis:PVOID, Button:int, Shift:int, Delta:int, X:int, Y:int) -> int:
        for callback in self._events["MouseWheel"]._callbacks:
            callback(Button, Shift, Delta, X, Y)
        return S_OK

    def _key_down(self, pThis:PVOID, KeyCode:POINTER(SHORT), Shift:int) -> int:
        for callback in self._events["KeyDown"]._callbacks:
            callback(KeyCode[0], Shift)
        return S_OK

    def _key_press(self, pThis:PVOID, KeyAscii:POINTER(SHORT)) -> int:
        for callback in self._events["KeyPress"]._callbacks:
            callback(KeyAscii[0])
        return S_OK

    def _key_up(self, pThis:PVOID, KeyCode:POINTER(SHORT), Shift:int) -> int:
        for callback in self._events["KeyUp"]._callbacks:
            callback(KeyCode[0], Shift)
        return S_OK

    def _click(self, pThis:PVOID) -> int:
        for callback in self._events["Click"]._callbacks:
            callback()
        return S_OK

    def _dbl_click(self, pThis:PVOID) -> int:
        for callback in self._events["DblClick"]._callbacks:
            callback()
        return S_OK

    def _mouse_down(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._events["MouseDown"]._callbacks:
            callback(Button, Shift, X, Y)
        return S_OK

    def _mouse_move(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._events["MouseMove"]._callbacks:
            callback(Button, Shift, X, Y)
        return S_OK

    def _mouse_up(self, pThis:PVOID, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._events["MouseUp"]._callbacks:
            callback(Button, Shift, X, Y)
        return S_OK

    def _ole_drag_drop(self, pThis:PVOID, Data:PVOID, Effect:int, Button:int, Shift:int, X:int, Y:int) -> int:
        for callback in self._events["OLEDragDrop"]._callbacks:
            with agmarshall.InterfaceEventCallbackArg(Data, agcls.AgTypeNameMap["DataObject"]) as arg_Data:
                callback(arg_Data.python_val, Effect, Button, Shift, X, Y)
        return S_OK

class IGraphics2DControlEventCOMHandler(COMEventHandlerImpl, IUiAxStockEventCOMHandler):
    _IID_IAgUiAx2DCntrlEvents    = GUID.from_registry_format("{A9B940DC-EA25-4488-A3E4-1F854B1DAF44}")

    def __init__(self, pUnk:IUnknown, events:dict):
        IUiAxStockEventCOMHandler.__init__(self, events)
        self._init_vtable()
        COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, IGraphics2DControlEventCOMHandler._IID_IAgUiAx2DCntrlEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"] = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown2"] = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown3"] = CFUNCTYPE(ULONG, PVOID)(self._release)
        else:
            self.__dict__["_cfunc_IUnknown3"] = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown1"] = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown2"] = CFUNCTYPE(ULONG, PVOID)(self._release)

        self.__dict__["_vtable"] = _UiAxStockEventsUnkSink( *[cast(self._cfunc_IUnknown1,   c_void_p),
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

    def _query_interface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IUiAxStockEventCOMHandler._IID_IAgUiAxStockRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IGraphics2DControlEventCOMHandler._IID_IAgUiAx2DCntrlEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

class IGraphics3DControlEventCOMHandler(COMEventHandlerImpl, IUiAxStockEventCOMHandler):
    _IID_IAgUiAxVOCntrlRawEvents = GUID.from_registry_format("{3ED83DF9-2536-47E4-A953-7BDE61DB4CC6}")
    _IID_IAgUiAxVOCntrlEvents    = GUID.from_registry_format("{6A7FD24F-8E58-43C3-A7DB-9432DFB5B4B9}")

    def __init__(self, pUnk:IUnknown, events:dict):
        IUiAxStockEventCOMHandler.__init__(self, events)
        self._init_vtable()
        COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, IGraphics3DControlEventCOMHandler._IID_IAgUiAxVOCntrlEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"] = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown2"] = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown3"] = CFUNCTYPE(ULONG, PVOID)(self._release)
        else:
            self.__dict__["_cfunc_IUnknown3"] = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown1"] = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown2"] = CFUNCTYPE(ULONG, PVOID)(self._release)
        self.__dict__["_cfunc_OnObjectEditingStart"]  = CFUNCTYPE(HRESULT, PVOID, BSTR)(self._on_object_editing_start)
        self.__dict__["_cfunc_OnObjectEditingApply"]  = CFUNCTYPE(HRESULT, PVOID, BSTR)(self._on_object_editing_apply)
        self.__dict__["_cfunc_OnObjectEditingCancel"] = CFUNCTYPE(HRESULT, PVOID, BSTR)(self._on_object_editing_cancel)
        self.__dict__["_cfunc_OnObjectEditingStop"]   = CFUNCTYPE(HRESULT, PVOID, BSTR)(self._on_object_editing_stop)

        self.__dict__["_vtable"] = _Graphics3DControlEventsUnkSink( *[cast(self._cfunc_IUnknown1,             c_void_p),
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

    def _query_interface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IUiAxStockEventCOMHandler._IID_IAgUiAxStockRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IGraphics3DControlEventCOMHandler._IID_IAgUiAxVOCntrlRawEvents:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IGraphics3DControlEventCOMHandler._IID_IAgUiAxVOCntrlEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _on_object_editing_start(self, pThis:PVOID, Path:str) -> int:
        for callback in self._events["OnObjectEditingStart"]._callbacks:
            callback(Path)
        return S_OK

    def _on_object_editing_apply(self, pThis:PVOID, Path:str) -> int:
        for callback in self._events["OnObjectEditingApply"]._callbacks:
            callback(Path)
        return S_OK

    def _on_object_editing_cancel(self, pThis:PVOID, Path:str) -> int:
        for callback in self._events["OnObjectEditingCancel"]._callbacks:
            callback(Path)
        return S_OK

    def _on_object_editing_stop(self, pThis:PVOID, Path:str) -> int:
        for callback in self._events["OnObjectEditingStop"]._callbacks:
            callback(Path)
        return S_OK


################################################################################
#          IAgStkGraphicsSceneEvents
################################################################################

class _STKGraphicsSceneEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",        c_void_p),
                 ("IUnknown2",        c_void_p),
                 ("IUnknown3",        c_void_p),
                 ("GetTypeInfoCount", c_void_p),
                 ("GetTypeInfo",      c_void_p),
                 ("GetIDsOfNames",    c_void_p),
                 ("invoke",           c_void_p),
                 ("rendering",        c_void_p)]

class ISceneEventCOMHandler(COMEventHandlerImpl):
    _IID_IAgStkGraphicsSceneEvents = GUID.from_registry_format("{87350BE6-236F-4130-8B4D-BA542EEDDA1E}")
    _DISPID_Rendering = 13901

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, ISceneEventCOMHandler._IID_IAgStkGraphicsSceneEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(ULONG, PVOID)(self._release)
        else:
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._release)
        self.__dict__["_cfunc_GetTypeInfoCount"] = CFUNCTYPE(HRESULT, PVOID, POINTER(UINT))(self._get_type_info_count)
        self.__dict__["_cfunc_GetTypeInfo"]      = CFUNCTYPE(HRESULT, PVOID, UINT, LCID, POINTER(PVOID))(self._get_type_info)
        self.__dict__["_cfunc_GetIDsOfNames"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID))(self._get_ids_of_names)
        self.__dict__["_cfunc_Invoke"]           = CFUNCTYPE(HRESULT, PVOID, DISPID, REFIID, LCID, WORD, POINTER(DispParams), POINTER(Variant), POINTER(ExcepInfo), POINTER(UINT))(self._invoke)
        self.__dict__["_cfunc_Rendering"]        = CFUNCTYPE(HRESULT, PVOID, Variant, PVOID)(self._rendering)

        self.__dict__["_vtable"] = _STKGraphicsSceneEventsUnkSink( *[cast(self._cfunc_IUnknown1,        c_void_p),
                                                                       cast(self._cfunc_IUnknown2,        c_void_p),
                                                                       cast(self._cfunc_IUnknown3,        c_void_p),
                                                                       cast(self._cfunc_GetTypeInfoCount, c_void_p),
                                                                       cast(self._cfunc_GetTypeInfo,      c_void_p),
                                                                       cast(self._cfunc_GetIDsOfNames,    c_void_p),
                                                                       cast(self._cfunc_Invoke,           c_void_p),
                                                                       cast(self._cfunc_Rendering,        c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)

    def _query_interface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == COMEventHandlerImpl._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == ISceneEventCOMHandler._IID_IAgStkGraphicsSceneEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DispParams), pVarResult:POINTER(Variant), pExcepInfo:POINTER(ExcepInfo), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == ISceneEventCOMHandler._DISPID_Rendering:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._rendering(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    def _rendering(self, pThis:PVOID, Sender:Variant, Args:PVOID) -> None:
        for callback in self._events["Rendering"]._callbacks:
            with agmarshall.VariantArg(Sender) as arg_Sender, \
                 agmarshall.InterfaceEventCallbackArg(Args, agcls.AgTypeNameMap["RenderingEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)


################################################################################
#          IAgStkGraphicsKmlGraphicsEvents
################################################################################

class _STKGraphicsKmlGraphicsEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",        c_void_p),
                 ("IUnknown2",        c_void_p),
                 ("IUnknown3",        c_void_p),
                 ("GetTypeInfoCount", c_void_p),
                 ("GetTypeInfo",      c_void_p),
                 ("GetIDsOfNames",    c_void_p),
                 ("invoke",           c_void_p),
                 ("document_loaded",   c_void_p)]

class IKmlGraphicsEventCOMHandler(COMEventHandlerImpl):
    _IID_IAgStkGraphicsKmlGraphicsEvents = GUID.from_registry_format("{5247C199-8DBC-4ABA-910E-074171EEE97E}")
    _DISPID_DocumentLoaded = 27101

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, IKmlGraphicsEventCOMHandler._IID_IAgStkGraphicsKmlGraphicsEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(ULONG, PVOID)(self._release)
        else:
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._release)
        self.__dict__["_cfunc_GetTypeInfoCount"] = CFUNCTYPE(HRESULT, PVOID, POINTER(UINT))(self._get_type_info_count)
        self.__dict__["_cfunc_GetTypeInfo"]      = CFUNCTYPE(HRESULT, PVOID, UINT, LCID, POINTER(PVOID))(self._get_type_info)
        self.__dict__["_cfunc_GetIDsOfNames"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID))(self._get_ids_of_names)
        self.__dict__["_cfunc_Invoke"]           = CFUNCTYPE(HRESULT, PVOID, DISPID, REFIID, LCID, WORD, POINTER(DispParams), POINTER(Variant), POINTER(ExcepInfo), POINTER(UINT))(self._invoke)
        self.__dict__["_cfunc_DocumentLoaded"]   = CFUNCTYPE(HRESULT, PVOID, Variant, PVOID)(self._document_loaded)

        self.__dict__["_vtable"] = _STKGraphicsKmlGraphicsEventsUnkSink( *[cast(self._cfunc_IUnknown1,        c_void_p),
                                                                             cast(self._cfunc_IUnknown2,        c_void_p),
                                                                             cast(self._cfunc_IUnknown3,        c_void_p),
                                                                             cast(self._cfunc_GetTypeInfoCount, c_void_p),
                                                                             cast(self._cfunc_GetTypeInfo,      c_void_p),
                                                                             cast(self._cfunc_GetIDsOfNames,    c_void_p),
                                                                             cast(self._cfunc_Invoke,           c_void_p),
                                                                             cast(self._cfunc_DocumentLoaded,   c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)

    def _query_interface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == COMEventHandlerImpl._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IKmlGraphicsEventCOMHandler._IID_IAgStkGraphicsKmlGraphicsEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DispParams), pVarResult:POINTER(Variant), pExcepInfo:POINTER(ExcepInfo), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == IKmlGraphicsEventCOMHandler._DISPID_DocumentLoaded:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._document_loaded(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    def _document_loaded(self, pThis:PVOID, Sender:Variant, Args:PVOID) -> None:
        for callback in self._events["DocumentLoaded"]._callbacks:
            with agmarshall.VariantArg(Sender) as arg_Sender, \
                 agmarshall.InterfaceEventCallbackArg(Args, agcls.AgTypeNameMap["KmlDocumentLoadedEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)


################################################################################
#          IAgStkGraphicsImageCollectionEvents
################################################################################

class _STKGraphicsImageCollectionEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",        c_void_p),
                 ("IUnknown2",        c_void_p),
                 ("IUnknown3",        c_void_p),
                 ("GetTypeInfoCount", c_void_p),
                 ("GetTypeInfo",      c_void_p),
                 ("GetIDsOfNames",    c_void_p),
                 ("invoke",           c_void_p),
                 ("add_complete",      c_void_p)]

class IImageCollectionEventCOMHandler(COMEventHandlerImpl):
    _IID_IAgStkGraphicsImageCollectionEvents = GUID.from_registry_format("{2F8954AA-10E1-4ACD-8FD3-439A80AAF835}")
    _DISPID_AddComplete = 13301

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, IImageCollectionEventCOMHandler._IID_IAgStkGraphicsImageCollectionEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(ULONG, PVOID)(self._release)
        else:
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._release)
        self.__dict__["_cfunc_GetTypeInfoCount"] = CFUNCTYPE(HRESULT, PVOID, POINTER(UINT))(self._get_type_info_count)
        self.__dict__["_cfunc_GetTypeInfo"]      = CFUNCTYPE(HRESULT, PVOID, UINT, LCID, POINTER(PVOID))(self._get_type_info)
        self.__dict__["_cfunc_GetIDsOfNames"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID))(self._get_ids_of_names)
        self.__dict__["_cfunc_Invoke"]           = CFUNCTYPE(HRESULT, PVOID, DISPID, REFIID, LCID, WORD, POINTER(DispParams), POINTER(Variant), POINTER(ExcepInfo), POINTER(UINT))(self._invoke)
        self.__dict__["_cfunc_AddComplete"]      = CFUNCTYPE(HRESULT, PVOID, Variant, PVOID)(self._add_complete)

        self.__dict__["_vtable"] = _STKGraphicsImageCollectionEventsUnkSink( *[cast(self._cfunc_IUnknown1,        c_void_p),
                                                                                 cast(self._cfunc_IUnknown2,        c_void_p),
                                                                                 cast(self._cfunc_IUnknown3,        c_void_p),
                                                                                 cast(self._cfunc_GetTypeInfoCount, c_void_p),
                                                                                 cast(self._cfunc_GetTypeInfo,      c_void_p),
                                                                                 cast(self._cfunc_GetIDsOfNames,    c_void_p),
                                                                                 cast(self._cfunc_Invoke,           c_void_p),
                                                                                 cast(self._cfunc_AddComplete,      c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)

    def _query_interface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == COMEventHandlerImpl._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == IImageCollectionEventCOMHandler._IID_IAgStkGraphicsImageCollectionEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DispParams), pVarResult:POINTER(Variant), pExcepInfo:POINTER(ExcepInfo), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == IImageCollectionEventCOMHandler._DISPID_AddComplete:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._add_complete(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    def _add_complete(self, pThis:PVOID, Sender:Variant, Args:PVOID) -> None:
        for callback in self._events["AddComplete"]._callbacks:
            with agmarshall.VariantArg(Sender) as arg_Sender, \
                 agmarshall.InterfaceEventCallbackArg(Args, agcls.AgTypeNameMap["GlobeImageOverlayAddCompleteEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)


################################################################################
#          IAgStkGraphicsTerrainCollectionEvents
################################################################################

class _STKGraphicsTerrainCollectionEventsUnkSink(Structure):
    _fields_ = [ ("IUnknown1",        c_void_p),
                 ("IUnknown2",        c_void_p),
                 ("IUnknown3",        c_void_p),
                 ("GetTypeInfoCount", c_void_p),
                 ("GetTypeInfo",      c_void_p),
                 ("GetIDsOfNames",    c_void_p),
                 ("invoke",           c_void_p),
                 ("add_complete",      c_void_p)]

class ITerrainOverlayCollectionEventCOMHandler(COMEventHandlerImpl):
    _IID_IAgStkGraphicsTerrainCollectionEvents = GUID.from_registry_format("{854C2737-45FF-4867-A31C-0465E0E12BA2}")
    _DISPID_AddComplete = 13401

    def __init__(self, pUnk:IUnknown, events:dict):
        self._events = events
        self._init_vtable()
        COMEventHandlerImpl.__init__(self, pUnk, self._pUnkSink, ITerrainOverlayCollectionEventCOMHandler._IID_IAgStkGraphicsTerrainCollectionEvents)

    def _init_vtable(self):
        if os.name == "nt":
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(ULONG, PVOID)(self._release)
        else:
            self.__dict__["_cfunc_IUnknown3"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(PVOID))(self._query_interface)
            self.__dict__["_cfunc_IUnknown1"]    = CFUNCTYPE(ULONG, PVOID)(self._add_ref)
            self.__dict__["_cfunc_IUnknown2"]    = CFUNCTYPE(ULONG, PVOID)(self._release)
        self.__dict__["_cfunc_GetTypeInfoCount"] = CFUNCTYPE(HRESULT, PVOID, POINTER(UINT))(self._get_type_info_count)
        self.__dict__["_cfunc_GetTypeInfo"]      = CFUNCTYPE(HRESULT, PVOID, UINT, LCID, POINTER(PVOID))(self._get_type_info)
        self.__dict__["_cfunc_GetIDsOfNames"]    = CFUNCTYPE(HRESULT, PVOID, REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID))(self._get_ids_of_names)
        self.__dict__["_cfunc_Invoke"]           = CFUNCTYPE(HRESULT, PVOID, DISPID, REFIID, LCID, WORD, POINTER(DispParams), POINTER(Variant), POINTER(ExcepInfo), POINTER(UINT))(self._invoke)
        self.__dict__["_cfunc_AddComplete"]      = CFUNCTYPE(HRESULT, PVOID, Variant, PVOID)(self._add_complete)

        self.__dict__["_vtable"] = _STKGraphicsTerrainCollectionEventsUnkSink( *[cast(self._cfunc_IUnknown1,        c_void_p),
                                                                                   cast(self._cfunc_IUnknown2,        c_void_p),
                                                                                   cast(self._cfunc_IUnknown3,        c_void_p),
                                                                                   cast(self._cfunc_GetTypeInfoCount, c_void_p),
                                                                                   cast(self._cfunc_GetTypeInfo,      c_void_p),
                                                                                   cast(self._cfunc_GetIDsOfNames,    c_void_p),
                                                                                   cast(self._cfunc_Invoke,           c_void_p),
                                                                                   cast(self._cfunc_AddComplete,      c_void_p) ] )
        self.__dict__["_pUnkSink"] = pointer(self._vtable)

    def _query_interface(self, pThis:PVOID, riid:REFIID, ppvObject:POINTER(PVOID)) -> int:
        iid = riid.contents
        if iid == COMEventHandlerImpl._IID_IUnknown:
            ppvObject[0] = pThis
            return S_OK
        if iid == COMEventHandlerImpl._IID_IDispatch:
            ppvObject[0] = pThis
            return S_OK
        elif iid == ITerrainOverlayCollectionEventCOMHandler._IID_IAgStkGraphicsTerrainCollectionEvents:
            ppvObject[0] = pThis
            return S_OK
        else:
            ppvObject[0] = 0
            return E_NOINTERFACE

    def _invoke(self, pThis:PVOID, dispIdMember:DISPID, riid:REFIID, lcid:LCID, wFlags:WORD, pDispParams:POINTER(DispParams), pVarResult:POINTER(Variant), pExcepInfo:POINTER(ExcepInfo), puArgErr:POINTER(UINT)) -> int:
        if dispIdMember == ITerrainOverlayCollectionEventCOMHandler._DISPID_AddComplete:
            variant_Sender = pDispParams.contents.rgvarg[1]
            pArgs = agmarshall.ctype_val_from_VARIANT(pDispParams.contents.rgvarg[0])
            self._add_complete(pThis, variant_Sender, pArgs)
            return S_OK
        else:
            return E_NOINTERFACE

    def _add_complete(self, pThis:PVOID, Sender:Variant, Args:PVOID) -> None:
        for callback in self._events["AddComplete"]._callbacks:
            with agmarshall.VariantArg(Sender) as arg_Sender, \
                 agmarshall.InterfaceEventCallbackArg(Args, agcls.AgTypeNameMap["TerrainOverlayAddCompleteEventArgs"]) as arg_Args:
                callback(arg_Sender.python_val, arg_Args.python_val)