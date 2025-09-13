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


import os
import typing

from ctypes import byref, cast, pointer, POINTER, Structure

from .comutil import BSTR, DWORD, GUID, HRESULT, INT, LONG, LPOLESTR, PVOID, ULONG, S_OK
from .comutil import OLE32Lib, OLEAut32Lib, IFuncType, IUnknown, Succeeded
from ..utilities.comobject  import COMObject
from .apiutil import error_msg_from_hresult

###############################################################################
#   Backwards Compatibility Mapping
###############################################################################

class _CreateBackwardsCompatibilityMapping(object):
    """Singleton class for recording GUID pairs needed for backwards compatability"""
    def __init__(self):
        self.mapping = dict()

    def add_mapping(self, new_guid, old_guid):
        self.mapping[new_guid] = old_guid

    def check_guid_available(self, guid):
        return guid in self.mapping

    def get_old_guid(self, new_guid):
        return self.mapping[new_guid]

AgBackwardsCompatabilityMapping = _CreateBackwardsCompatibilityMapping()

###############################################################################
#   Class Catalog
###############################################################################

class _CreateAgClassCatalog(object):
    """Singleton class for registering Object Model classes"""
    def __init__(self):
        self.catalog = dict()

    def add_catalog_entry(self, class_id, pyclass):
        self.catalog[class_id] = pyclass

    def check_clsid_available(self, class_id):
        return class_id in self.catalog

    def get_class(self, class_id):
        return self.catalog[class_id]

AgClassCatalog = _CreateAgClassCatalog()

AgTypeNameMap = {}

###############################################################################
#   Querying error information
###############################################################################

class _IErrorInfo(object):
    guid = "{1CF2B120-547D-101B-8E65-08002B2BD119}"
    def __init__(self, pUnk):
        IID__IErrorInfo = GUID.from_registry_format(_IErrorInfo.guid)
        vtable_offset = IUnknown._num_methods - 1
        #GetGUIDIndex        = 1 (skipping GetGUID as it is not needed)
        #GetSourceIndex      = 2 (skipping GetSource as it is not needed)
        GetDescriptionIndex  = 3
        #GetHelpFileIndex    = 4 (skipping GetHelpFile as it is not needed)
        #GetHelpContextIndex = 5 (skipping GetHelpContext as it is not needed)
        if os.name!="nt":
            GetDescriptionIndex = 1
        self._GetDescription = IFuncType(pUnk, IID__IErrorInfo, vtable_offset + GetDescriptionIndex, POINTER(BSTR))
    def get_description(self):
        p = BSTR()
        hr = self._GetDescription(byref(p))
        if Succeeded(hr):
            desc = p.value
            OLEAut32Lib.SysFreeString(p)
            return desc

def evaluate_hresult(hr:HRESULT) -> None:
    """Get error info and raise an exception if an HRESULT value is failing."""
    if not Succeeded(hr):
        punk = IUnknown()
        msg = None
        if OLEAut32Lib.GetErrorInfo(DWORD(), byref(punk.p)) == S_OK:
            punk.take_ownership()
            ierrorinfo = _IErrorInfo(punk)
            msg = ierrorinfo.get_description()
            del(ierrorinfo)
            del(punk)
        else:
            msg = error_msg_from_hresult(hr)
        raise RuntimeError(msg)


###############################################################################
#   Querying class information
###############################################################################

class _IProvideClassId(object):
    guid = "{C86B17CD-D670-46D8-AC90-CEFAEAE867DC}"
    def __init__(self, pUnk):
        IID__IAgProvideClassId = GUID.from_registry_format(_IProvideClassId.guid)
        pIntf = pUnk.query_interface(IID__IAgProvideClassId)
        self.valid = False
        if pIntf is not None:
            self.valid = True
            del(pIntf)
        vtable_offset = IUnknown._num_methods - 1
        GetClsidIndex = 1
        self._GetClsid = IFuncType(pUnk, IID__IAgProvideClassId, vtable_offset + GetClsidIndex, POINTER(GUID))
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        del(self._GetClsid)
        return False
    def get_clsid(self):
        coclass_clsid = GUID()
        if self.valid:
            if Succeeded(self._GetClsid(byref(coclass_clsid))):
                return coclass_clsid
        return None

class _TypeAttr(Structure):
    LCID = DWORD
    MEMBERID = LONG
    TYPEKIND = INT
    #there are more entries to this struct we just don't need them
    _fields_ = [("guid", GUID), \
                ("lcid", LCID), \
                ("dwReserved", DWORD), \
                ("memidConstructor", MEMBERID), \
                ("memidDestructor", MEMBERID), \
                ("lpstrSchema", LPOLESTR), \
                ("cbSizeInstance", ULONG), \
                ("typekind", TYPEKIND), \
               ]

class _ITypeInfo(object):
    guid = "{00020401-0000-0000-C000-000000000046}"
    def __init__(self, pUnk):
        IID__ITypeInfo = GUID.from_registry_format(_ITypeInfo.guid)
        vtable_offset = IUnknown._num_methods - 1
        GetTypeAttrIndex            = 1
        #GetTypeCompIndex           = 2   (skipping GetTypeComp as it is not needed)
        #GetFuncDescIndex           = 3   (skipping GetFuncDesc as it is not needed)
        #GetVarDescIndex            = 4   (skipping GetVarDesc as it is not needed)
        #GetNamesIndex              = 5   (skipping GetNames as it is not needed)
        #GetRefTypeOfImplTypeIndex  = 6   (skipping GetRefTypeOfImplType as it is not needed)
        #GetImplTypeFlagsIndex      = 7   (skipping GetImplTypeFlags as it is not needed)
        #GetIDsOfNamesIndex         = 8   (skipping GetIDsOfNames as it is not needed)
        #InvokeIndex                = 9   (skipping Invoke as it is not needed)
        #GetDocumentationIndex      = 10  (skipping GetDocumentation as it is not needed)
        #GetDllEntryIndex           = 11  (skipping GetDllEntry as it is not needed)
        #GetRefTypeInfoIndex        = 12  (skipping GetRefTypeInfo as it is not needed)
        #AddressOfMemberIndex       = 13  (skipping AddressOfMember as it is not needed)
        #CreateInstanceIndex        = 14  (skipping CreateInstance as it is not needed)
        #GetMopsIndex               = 15  (skipping GetMops as it is not needed)
        #GetContainingTypeLibIndex  = 16  (skipping GetContainingTypeLib as it is not needed)
        ReleaseTypeAttrIndex        = 17
        #ReleaseFuncDescIndex       = 18  (skipping ReleaseFuncDesc as it is not needed)
        #ReleaseVarDescIndex        = 19  (skipping ReleaseVarDesc as it is not needed)
        self._GetTypeAttr = IFuncType(pUnk, IID__ITypeInfo, vtable_offset + GetTypeAttrIndex, POINTER(PVOID))
        self._ReleaseTypeAttr = IFuncType(pUnk, IID__ITypeInfo, vtable_offset + ReleaseTypeAttrIndex, POINTER(_TypeAttr))
    def get_type_attr(self):
        p = PVOID()
        hr = self._GetTypeAttr(byref(p))
        if Succeeded(hr):
            ta = cast(p, POINTER(_TypeAttr)).contents
            return ta
    def release_type_attr(self, ta):
        self._ReleaseTypeAttr(byref(ta))

class _IProvideClassInfo(object):
    guid = "{B196B283-BAB4-101A-B69C-00AA00341D07}"
    def __init__(self, pUnk):
        IID__IProvideClassInfo = GUID.from_registry_format(_IProvideClassInfo.guid)
        pIntf = pUnk.query_interface(IID__IProvideClassInfo)
        self.valid = False
        if pIntf is not None:
            self.valid = True
            del(pIntf)
        vtable_offset = IUnknown._num_methods - 1
        GetClassInfoIndex = 1
        self._GetClassInfo = IFuncType(pUnk, IID__IProvideClassInfo, vtable_offset + GetClassInfoIndex, POINTER(PVOID))
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        del(self._GetClassInfo)
        return False
    def get_class_info(self):
        if self.valid:
            pUnk = IUnknown()
            hr = self._GetClassInfo(byref(pUnk.p))
            if Succeeded(hr):
                pUnk.take_ownership()
                type_info = _ITypeInfo(pUnk)
                type_attr = type_info.get_type_attr()
                if type_attr is not None:
                    guid = GUID.from_guid(type_attr.guid)
                    type_info.release_type_attr(type_attr)
                else:
                    guid = None
                del(type_info)
                del(pUnk)
                return guid
        return None

def get_concrete_class(punk:IUnknown) -> typing.Any:
    """Convert an interface pointer to the concrete class it belongs to."""
    coclass = COMObject()
    if punk:
        coclass._pUnk = punk
        my_clsid = None
        with _IProvideClassId(punk) as provideClassInfo:
            my_clsid = provideClassInfo.get_clsid()
        if my_clsid is None and os.name=="nt":
            with _IProvideClassInfo(punk) as provideClassInfo:
                my_clsid = provideClassInfo.get_class_info()
        if my_clsid is not None:
            guid_data = my_clsid.as_data_pair()
            if AgClassCatalog.check_clsid_available(guid_data):
                coclass = AgClassCatalog.get_class(guid_data)()
                coclass._private_init(punk)
    return coclass

def compare_com_objects(first, second) -> bool:
    """Compare whether the given interfaces point to the same COM object."""
    if first is None and second is None:
        return True
    elif first is None or second is None:
        return False
    if hasattr(first, "_intf") and hasattr(second, "_intf"):
        first_pUnk = first._intf.query_interface(IUnknown._metadata)
        second_pUnk = second._intf.query_interface(IUnknown._metadata)
        result = (first_pUnk == second_pUnk)
        del(first_pUnk)
        del(second_pUnk)
        return result
    else:
        return False

###############################################################################
#   Events related classes
###############################################################################
class IConnectionPoint(object):
    guid = "{B196B286-BAB4-101A-B69C-00AA00341D07}"
    def __init__(self, pUnk):
        IID_IConnectionPoint = GUID.from_registry_format(IConnectionPoint.guid)
        vtable_offset = IUnknown._num_methods - 1
        GetConnectionInterfaceIndex         = 1
        #GetConnectionPointContainerIndex   = 2 (skipping GetConnectionPointContainer as it is not needed)
        AdviseIndex                         = 3
        UnadviseIndex                       = 4
        #EnumConnectionsIndex               = 5 (skipping EnumConnections as it is not needed)
        self._GetConnectionInterface = IFuncType(pUnk, IID_IConnectionPoint, vtable_offset + GetConnectionInterfaceIndex, POINTER(GUID))
        self._Advise                 = IFuncType(pUnk, IID_IConnectionPoint, vtable_offset + AdviseIndex, PVOID, POINTER(DWORD))
        self._Unadvise               = IFuncType(pUnk, IID_IConnectionPoint, vtable_offset + UnadviseIndex, DWORD)
    def get_connection_interface(self) -> GUID:
        guid = GUID()
        hr = self._GetConnectionInterface(byref(guid))
        if Succeeded(hr):
            return guid
    def advise(self, event_sink:PVOID) -> DWORD:
        cookie = DWORD()
        hr = self._Advise(event_sink, byref(cookie))
        if Succeeded(hr):
            return cookie
    def unadvise(self, cookie:DWORD):
        self._Unadvise(cookie)

class IConnectionPointContainer(object):
    guid = "{B196B284-BAB4-101A-B69C-00AA00341D07}"
    def __init__(self, pUnk):
        IID_IConnectionPointContainer = GUID.from_registry_format(IConnectionPointContainer.guid)
        vtable_offset = IUnknown._num_methods - 1
        #EnumConnectionPointsIndex = 1 (skipping EnumConnectionPoints as it is not needed)
        FindConnectionPointIndex   = 2
        self._FindConnectionPoint = IFuncType(pUnk, IID_IConnectionPointContainer, vtable_offset + FindConnectionPointIndex, POINTER(GUID), POINTER(PVOID))
    def find_connection_point(self, iid:GUID) -> IConnectionPoint:
        pUnk = IUnknown()
        hr = self._FindConnectionPoint(iid, byref(pUnk.p))
        if Succeeded(hr):
            pUnk.take_ownership()
            conn_point = IConnectionPoint(pUnk)
            del(pUnk)
            return conn_point


###############################################################################
#   attach_to_stk_by_pid (Windows-only)
###############################################################################

class _IRunningObjectTable(object):
    guid = "{00000010-0000-0000-C000-000000000046}"
    def __init__(self, pUnk: "IUnknown"):
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows. Use STKEngine.")
        self.gettingAnApplication = True
        IID__IRunningObjectTable = GUID.from_registry_format(_IRunningObjectTable.guid)
        vtable_offset = IUnknown._num_methods - 1
        #RegisterIndex              = 1 (skipping Register as it is not needed)
        #RevokeIndex                = 2 (skipping Revoke as it is not needed)
        #IsRunningIndex             = 3 (skipping IsRunning as it is not needed)
        GetObjectIndex              = 4
        #NoteChangeTimeIndex        = 5 (skipping NoteChangeTime as it is not needed)
        #GetTimeOfLastChangeIndex   = 6 (skipping GetTimeOfLastChange as it is not needed)
        EnumRunningIndex            = 7
        self._GetObject   = IFuncType(pUnk, IID__IRunningObjectTable, vtable_offset + GetObjectIndex, PVOID, POINTER(PVOID))
        self._EnumRunning = IFuncType(pUnk, IID__IRunningObjectTable, vtable_offset + EnumRunningIndex, POINTER(PVOID))
    def get_object(self, pmkObjectName: "_IMoniker") -> "IUnknown":
        ppunkObject = IUnknown()
        self._GetObject(pmkObjectName.pUnk.p, byref(ppunkObject.p))
        ppunkObject.take_ownership(isApplication=self.gettingAnApplication)
        return ppunkObject
    def enum_running(self) -> "_IEnumMoniker":
        ppenumMoniker = IUnknown()
        self._EnumRunning(byref(ppenumMoniker.p))
        ppenumMoniker.take_ownership()
        iEnumMon = _IEnumMoniker(ppenumMoniker)
        del(ppenumMoniker)
        return iEnumMon

class _IEnumMoniker(object):
    guid = "{00000102-0000-0000-C000-000000000046}"
    def __init__(self, pUnk: "IUnknown"):
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows. Use STKEngine.")
        IID__IEnumMoniker = GUID.from_registry_format(_IEnumMoniker.guid)
        vtable_offset = IUnknown._num_methods - 1
        NextIndex   = 1
        #SkipIndex  = 2 (skipping Skip as it is not needed)
        ResetIndex  = 3
        #CloneIndex = 4 (skipping Clone as it is not needed)
        self._Next   = IFuncType(pUnk, IID__IEnumMoniker, vtable_offset + NextIndex, ULONG, POINTER(PVOID), POINTER(ULONG))
        self._Reset  = IFuncType(pUnk, IID__IEnumMoniker, vtable_offset + ResetIndex)
    def next(self) -> "_IMoniker":
        one_obj = ULONG(1)
        num_fetched = ULONG(0)
        pUnk = IUnknown()
        CLSID_AgUiApplication = GUID()
        OLE32Lib.CLSIDFromString("STK13.Application", CLSID_AgUiApplication)
        OLE32Lib.CreateClassMoniker(CLSID_AgUiApplication, byref(pUnk.p))
        pUnk.take_ownership()
        self._Next(one_obj, byref(pUnk.p), byref(num_fetched))
        if num_fetched.value == 1:
            iMon = _IMoniker(pUnk)
            del(pUnk)
            return iMon
    def reset(self):
        self._Reset()

class _IMalloc(object):
    guid = "{00000002-0000-0000-C000-000000000046}"
    def __init__(self, pUnk: "IUnknown"):
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows. Use STKEngine.")
        IID__IMalloc = GUID.from_registry_format(_IMalloc.guid)
        vtable_offset = IUnknown._num_methods - 1
        #AllocIndex          = 1 (skipping Alloc as it is not needed)
        #ReallocIndex        = 2 (skipping Realloc as it is not needed)
        FreeIndex            = 3
        #GetSizeIndex        = 4 (skipping GetSize as it is not needed)
        #DidAllocIndex       = 5 (skipping DidAlloc as it is not needed)
        #HeapMinimizeIndex   = 6 (skipping HeapMinimize as it is not needed)
        self._Free = IFuncType(pUnk, IID__IMalloc, vtable_offset + FreeIndex, PVOID)
    def free(self, pv):
        self._Free(pv)

class _IMoniker(object):
    guid = "{0000000f-0000-0000-C000-000000000046}"
    def __init__(self, pUnk: "IUnknown"):
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows. Use STKEngine.")
        self.pUnk = pUnk
        IID__IMoniker = GUID.from_registry_format(_IMoniker.guid)
        IPersist_num_methods = 1
        IPersistStream_num_methods = 4
        vtable_offset = IUnknown._num_methods + IPersist_num_methods + IPersistStream_num_methods - 1
        #BindToObjectIndex           = 1  (skipping BindToObject as it is not needed)
        #BindToStorageIndex          = 2  (skipping BindToStorage as it is not needed)
        #ReduceIndex                 = 3  (skipping Reduce as it is not needed)
        #ComposeWithIndex            = 4  (skipping ComposeWith as it is not needed)
        #EnumIndex                   = 5  (skipping Enum as it is not needed)
        #IsEqualIndex                = 6  (skipping IsEqual as it is not needed)
        #HashIndex                   = 7  (skipping Hash as it is not needed)
        #IsRunningIndex              = 8  (skipping IsRunning as it is not needed)
        #GetTimeOfLastChangeIndex    = 9  (skipping GetTimeOfLastChange as it is not needed)
        #InverseIndex                = 10 (skipping Inverse as it is not needed)
        #CommonPrefixWithIndex       = 11 (skipping CommonPrefixWith as it is not needed)
        #RelativePathToIndex         = 12 (skipping RelativePathTo as it is not needed)
        GetDisplayNameIndex          = 13
        #ParseDisplayNameIndex       = 14 (skipping ParseDisplayName as it is not needed)
        #IsSystemMonikerIndex        = 15 (skipping IsSystemMoniker as it is not needed)
        self._GetDisplayName = IFuncType(pUnk, IID__IMoniker, vtable_offset + GetDisplayNameIndex, PVOID, PVOID, POINTER(BSTR))
    def _free_display_name(self, ppszDisplayName):
        pMalloc = IUnknown()
        OLE32Lib.CoGetMalloc(DWORD(1), byref(pMalloc.p))
        pMalloc.take_ownership()
        iMalloc = _IMalloc(pMalloc)
        iMalloc.free(ppszDisplayName)
        del(iMalloc)
        del(pMalloc)
    def get_display_name(self) -> str:
        pbc = IUnknown()
        pmkToLeft = IUnknown()
        OLE32Lib.CreateBindCtx(DWORD(0), byref(pbc.p))
        pbc.take_ownership()
        ppszDisplayName = BSTR()
        self._GetDisplayName(pbc.p, pmkToLeft.p, byref(ppszDisplayName))
        display_name = ppszDisplayName.value
        self._free_display_name(ppszDisplayName)
        del(pmkToLeft)
        del(pbc)
        return display_name

def attach_to_stk_by_pid(pid:int) -> IUnknown:
    if os.name != "nt":
        raise RuntimeError("STKDesktop is only available on Windows. Use STKEngine.")
    runningObjectTable = IUnknown()
    str_prog_id = "!STK.Application:" + str(pid)
    if Succeeded(OLE32Lib.GetRunningObjectTable(DWORD(0), byref(runningObjectTable.p))):
        runningObjectTable.take_ownership()
        runningObjectTable = _IRunningObjectTable(runningObjectTable)
        enumMoniker = runningObjectTable.enum_running()
        enumMoniker.reset()
        moniker = enumMoniker.next()
        while moniker is not None:
            instanceName = moniker.get_display_name()
            if instanceName == str_prog_id:
                ret = runningObjectTable.get_object(moniker)
                del(moniker)
                del(enumMoniker)
                del(runningObjectTable)
                return ret
            else:
                moniker = enumMoniker.next()
        del(moniker)
        del(enumMoniker)
        del(runningObjectTable)
    else:
        raise RuntimeError("Failed to retrieve the Running Object Table.")
