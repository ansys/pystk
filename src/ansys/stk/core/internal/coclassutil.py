# Copyright 2020-2020, Analytical Graphics, Inc. 

import os
import typing

from ctypes import byref, cast, pointer, POINTER, Structure

from .comutil import BSTR, DWORD, GUID, HRESULT, INT, LONG, LPOLESTR, LPVOID, PVOID, ULONG, S_OK
from .comutil import CLSIDFromString, CoTaskMemFree, IAGFUNCTYPE, IUnknown, GetErrorInfo, ole32lib, Succeeded, StringFromCLSID, SysFreeString, WINFUNCTYPE
from ..utilities.comobject  import COMObject
from ..utilities.exceptions import *

###############################################################################
#   Class Catalog
###############################################################################

class _CreateAgClassCatalog(object):
    """Singleton class for registering STK Object Model classes by clsid"""
    def __init__(self):
        self.catalog = dict()
        self.clsid_from_pyclass = dict()

    def set_catalog(self, catalog):
        self.catalog = catalog

    def add_catalog_entry(self, clsid, pyclass):
        self.catalog[clsid.upper()] = pyclass
        self.clsid_from_pyclass[pyclass] = clsid.upper()

    def check_clsid_available(self, clsid):
        return clsid.upper() in self.catalog

    def get_class(self, clsid):
        return self.catalog[clsid.upper()]
        
    def get_clsid_from_pyclass(self, pyclass):
        return self.clsid_from_pyclass[pyclass]

AgClassCatalog = _CreateAgClassCatalog()

AgTypeNameMap = {}
        
###############################################################################
#   Querying error information
###############################################################################
        
class _IErrorInfo(object):
    guid = "{1CF2B120-547D-101B-8E65-08002B2BD119}"
    def __init__(self, pUnk):
        IID__IErrorInfo = GUID(_IErrorInfo.guid)
        vtable_offset = IUnknown._num_methods - 1
        #GetGUIDIndex        = 1 (skipping GetGUID as it is not needed)
        #GetSourceIndex      = 2 (skipping GetSource as it is not needed)
        GetDescriptionIndex  = 3
        #GetHelpFileIndex    = 4 (skipping GetHelpFile as it is not needed)
        #GetHelpContextIndex = 5 (skipping GetHelpContext as it is not needed)
        if os.name!="nt":
            GetDescriptionIndex = 1
        self._GetDescription = IAGFUNCTYPE(pUnk, IID__IErrorInfo, vtable_offset + GetDescriptionIndex, POINTER(BSTR))
    def GetDescription(self):
        p = BSTR()
        hr = self._GetDescription(byref(p))
        if Succeeded(hr):
            desc = p.value
            SysFreeString(p)
            return desc
            
def evaluate_hresult(hr:HRESULT) -> None:
    """Get error info and raise an exception if an HRESULT value is failing."""
    if not Succeeded(hr):
        punk = IUnknown()
        msg = None
        if GetErrorInfo(DWORD(), byref(punk.p)) == S_OK:
            punk.TakeOwnership()
            ierrorinfo = _IErrorInfo(punk)
            msg = ierrorinfo.GetDescription()
            del(ierrorinfo)
            del(punk)
        elif (hr & 0xFFFFFFFF) == 0x80070057: # E_INVALIDARG
            msg = "One or more arguments are invalid."
        hresult_val = "(HRESULT = 0x%x)" % (hr & 0xFFFFFFFF)
        raise STKRuntimeError(msg if msg is not None else hresult_val)
            
            
###############################################################################
#   Querying class information
###############################################################################
            
class _IAgProvideClassId(object):
    guid = "{C86B17CD-D670-46D8-AC90-CEFAEAE867DC}"
    def __init__(self, pUnk):
        IID__IAgProvideClassId = GUID(_IAgProvideClassId.guid)
        pIntf = pUnk.QueryInterface(iid=IID__IAgProvideClassId)
        self.valid = False
        if pIntf is not None:
            self.valid = True
            del(pIntf)
        vtable_offset = IUnknown._num_methods - 1
        GetClsidIndex = 1
        self._GetClsid = IAGFUNCTYPE(pUnk, IID__IAgProvideClassId, vtable_offset + GetClsidIndex, POINTER(GUID))
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        del(self._GetClsid)
        return False
    def GetClsid(self):
        coclass_clsid = GUID()
        if self.valid:
            if Succeeded(self._GetClsid(byref(coclass_clsid))):
                return coclass_clsid
        return None
            
class _TYPEATTR(Structure):
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
        IID__ITypeInfo = GUID(_ITypeInfo.guid)
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
        #ReleaseTypeAttrIndex       = 17  (skipping ReleaseTypeAttr as it is not needed)
        #ReleaseFuncDescIndex       = 18  (skipping ReleaseFuncDesc as it is not needed)
        #ReleaseVarDescIndex        = 19  (skipping ReleaseVarDesc as it is not needed)
        self._GetTypeAttr = IAGFUNCTYPE(pUnk, IID__ITypeInfo, vtable_offset + GetTypeAttrIndex, POINTER(PVOID))
    def GetTypeAttr(self):
        p = PVOID()
        hr = self._GetTypeAttr(byref(p))
        if Succeeded(hr):
            ta = cast(p, POINTER(_TYPEATTR)).contents
            return ta
            
class _IProvideClassInfo(object):
    guid = "{B196B283-BAB4-101A-B69C-00AA00341D07}"
    def __init__(self, pUnk):
        IID__IProvideClassInfo = GUID(_IProvideClassInfo.guid)
        pIntf = pUnk.QueryInterface(iid=IID__IProvideClassInfo)
        self.valid = False
        if pIntf is not None:
            self.valid = True
            del(pIntf)
        vtable_offset = IUnknown._num_methods - 1
        GetClassInfoIndex = 1
        self._GetClassInfo = IAGFUNCTYPE(pUnk, IID__IProvideClassInfo, vtable_offset + GetClassInfoIndex, POINTER(PVOID))
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        del(self._GetClassInfo)
        return False
    def GetClassInfo(self):
        if self.valid:
            pUnk = IUnknown()
            hr = self._GetClassInfo(byref(pUnk.p))
            if Succeeded(hr):
                pUnk.TakeOwnership()
                type_info = _ITypeInfo(pUnk)
                type_attr = type_info.GetTypeAttr()
                del(type_info)
                del(pUnk)
                if type_attr is not None:
                    return type_attr.guid
        return None
        
def get_concrete_class(punk:IUnknown) -> typing.Any:
    """Convert an interface pointer to the concrete class it belongs to."""
    coclass = COMObject()
    if punk:
        coclass._pUnk = punk
        my_clsid = None
        with _IAgProvideClassId(punk) as provideClassInfo:
            my_clsid = provideClassInfo.GetClsid()
        if my_clsid is None and os.name=="nt":
            with _IProvideClassInfo(punk) as provideClassInfo:
                my_clsid = provideClassInfo.GetClassInfo()
        if my_clsid is not None:
            p = BSTR()
            if Succeeded(StringFromCLSID(byref(my_clsid), byref(p))):
                if AgClassCatalog.check_clsid_available(p.value):
                    coclass = AgClassCatalog.get_class(p.value)()
                    coclass._private_init(punk)
                CoTaskMemFree(p)
    return coclass
    
def compare_com_objects(first, second) -> bool:
    """Used to compare whether the given interfaces point to the same COM object."""
    if first is None and second is None:
        return True
    elif first is None or second is None:
        return False
    if hasattr(first, "_pUnk") and hasattr(second, "_pUnk"):
        iid_IUnknown = GUID(IUnknown._guid)
        first_pUnk = first.__dict__["_pUnk"].QueryInterface(iid_IUnknown)
        second_pUnk = second.__dict__["_pUnk"].QueryInterface(iid_IUnknown)
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
        IID_IConnectionPoint = GUID(IConnectionPoint.guid)
        vtable_offset = IUnknown._num_methods - 1
        GetConnectionInterfaceIndex         = 1 
        #GetConnectionPointContainerIndex   = 2 (skipping GetConnectionPointContainer as it is not needed)
        AdviseIndex                         = 3 
        UnadviseIndex                       = 4 
        #EnumConnectionsIndex               = 5 (skipping EnumConnections as it is not needed)
        self._GetConnectionInterface = IAGFUNCTYPE(pUnk, IID_IConnectionPoint, vtable_offset + GetConnectionInterfaceIndex, POINTER(GUID))
        self._Advise                 = IAGFUNCTYPE(pUnk, IID_IConnectionPoint, vtable_offset + AdviseIndex, PVOID, POINTER(DWORD))
        self._Unadvise               = IAGFUNCTYPE(pUnk, IID_IConnectionPoint, vtable_offset + UnadviseIndex, DWORD)
    def GetConnectionInterface(self) -> GUID:
        guid = GUID()
        hr = self._GetConnectionInterface(byref(guid))
        if Succeeded(hr):
            return guid
    def Advise(self, event_sink:PVOID) -> DWORD:
        cookie = DWORD()
        hr = self._Advise(event_sink, byref(cookie))
        if Succeeded(hr):
            return cookie
    def Unadvise(self, cookie:DWORD):
        self._Unadvise(cookie)
            
class IConnectionPointContainer(object):
    guid = "{B196B284-BAB4-101A-B69C-00AA00341D07}"
    def __init__(self, pUnk):
        IID_IConnectionPointContainer = GUID(IConnectionPointContainer.guid)
        vtable_offset = IUnknown._num_methods - 1
        #EnumConnectionPointsIndex = 1 (skipping EnumConnectionPoints as it is not needed)
        FindConnectionPointIndex   = 2
        self._FindConnectionPoint = IAGFUNCTYPE(pUnk, IID_IConnectionPointContainer, vtable_offset + FindConnectionPointIndex, POINTER(GUID), POINTER(PVOID))
    def FindConnectionPoint(self, iid:GUID) -> IConnectionPoint:
        pUnk = IUnknown()
        hr = self._FindConnectionPoint(iid, byref(pUnk.p))
        if Succeeded(hr):
            pUnk.TakeOwnership()
            conn_point = IConnectionPoint(pUnk)
            del(pUnk)
            return conn_point
        
        
###############################################################################
#   Helper Methods for IDispatch marshalling
###############################################################################
def IUnknown_from_IDispatch(pdisp:PVOID) -> IUnknown: 
    pDispAsUnk = IUnknown()
    if pdisp.value > 0:
        pDispAsUnk.p = pdisp
        IID_IUnknown = GUID(IUnknown._guid)
        pUnk = pDispAsUnk.QueryInterface(iid=IID_IUnknown)
        del(pDispAsUnk)
        return pUnk

      
###############################################################################
#   attach_to_stk_by_pid (Windows-only)
###############################################################################
if os.name=="nt":
    CreateClassMoniker    = WINFUNCTYPE(HRESULT, GUID, POINTER(LPVOID))(("CreateClassMoniker", ole32lib), ((1, "rclsid"), (1, "ppmk")))
    GetRunningObjectTable = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("GetRunningObjectTable", ole32lib), ((1, "dwReserved"), (1, "pprot")))
    CreateBindCtx         = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("CreateBindCtx", ole32lib), ((1, "dwReserved"), (1, "ppbc")))
    CoGetMalloc           = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("CoGetMalloc", ole32lib), ((1, "dwMemContext"), (1, "ppMalloc")))
            
    class _IRunningObjectTable(object):
        guid = "{00000010-0000-0000-C000-000000000046}"
        def __init__(self, pUnk):
            self.gettingAnApplication = True
            IID__IRunningObjectTable = GUID(_IRunningObjectTable.guid)
            vtable_offset = IUnknown._num_methods - 1
            #RegisterIndex              = 1 (skipping Register as it is not needed)
            #RevokeIndex                = 2 (skipping Revoke as it is not needed)
            #IsRunningIndex             = 3 (skipping IsRunning as it is not needed)
            GetObjectIndex              = 4 
            #NoteChangeTimeIndex        = 5 (skipping NoteChangeTime as it is not needed)
            #GetTimeOfLastChangeIndex   = 6 (skipping GetTimeOfLastChange as it is not needed)
            EnumRunningIndex            = 7 
            self._GetObject   = IAGFUNCTYPE(pUnk, IID__IRunningObjectTable, vtable_offset + GetObjectIndex, PVOID, POINTER(PVOID))
            self._EnumRunning = IAGFUNCTYPE(pUnk, IID__IRunningObjectTable, vtable_offset + EnumRunningIndex, POINTER(PVOID))
        def GetObject(self, pmkObjectName:"IMoniker") -> "IUnknown":
            ppunkObject = IUnknown()
            self._GetObject(pmkObjectName.pUnk.p, byref(ppunkObject.p))
            ppunkObject.TakeOwnership(isApplication=self.gettingAnApplication) 
            return ppunkObject
        def EnumRunning(self) -> "_IEnumMoniker":
            ppenumMoniker = IUnknown()
            self._EnumRunning(byref(ppenumMoniker.p))
            ppenumMoniker.TakeOwnership()
            iEnumMon = _IEnumMoniker(ppenumMoniker)
            del(ppenumMoniker)
            return iEnumMon
        
    class _IEnumMoniker(object):
        guid = "{00000102-0000-0000-C000-000000000046}"
        def __init__(self, pUnk):
            IID__IEnumMoniker = GUID(_IEnumMoniker.guid)
            vtable_offset = IUnknown._num_methods - 1
            NextIndex   = 1 
            #SkipIndex  = 2 (skipping Skip as it is not needed)
            ResetIndex  = 3
            #CloneIndex = 4 (skipping Clone as it is not needed)
            self._Next   = IAGFUNCTYPE(pUnk, IID__IEnumMoniker, vtable_offset + NextIndex, ULONG, POINTER(PVOID), POINTER(ULONG))
            self._Reset  = IAGFUNCTYPE(pUnk, IID__IEnumMoniker, vtable_offset + ResetIndex)
        def Next(self) -> "_IMoniker":
            one_obj = ULONG(1)
            num_fetched = ULONG(0)
            pUnk = IUnknown()
            CLSID_AgUiApplication = GUID()
            CLSIDFromString("STK12.Application", CLSID_AgUiApplication)
            CreateClassMoniker(CLSID_AgUiApplication, byref(pUnk.p))
            pUnk.TakeOwnership()
            self._Next(one_obj, byref(pUnk.p), byref(num_fetched))
            if num_fetched.value == 1:
                iMon = _IMoniker(pUnk)
                del(pUnk)
                return iMon
        def Reset(self):
            self._Reset()
        
    class _IMalloc(object):
        guid = "{00000002-0000-0000-C000-000000000046}"
        def __init__(self, pUnk):
            IID__IMalloc = GUID(_IMalloc.guid)
            vtable_offset = IUnknown._num_methods - 1
            #AllocIndex          = 1 (skipping Alloc as it is not needed)
            #ReallocIndex        = 2 (skipping Realloc as it is not needed)
            FreeIndex            = 3 
            #GetSizeIndex        = 4 (skipping GetSize as it is not needed)
            #DidAllocIndex       = 5 (skipping DidAlloc as it is not needed)
            #HeapMinimizeIndex   = 6 (skipping HeapMinimize as it is not needed)
            self._Free = IAGFUNCTYPE(pUnk, IID__IMalloc, vtable_offset + FreeIndex, PVOID)
        def Free(self, pv):
            self._Free(pv)
       
    class _IMoniker(object):
        guid = "{0000000f-0000-0000-C000-000000000046}"
        def __init__(self, pUnk):
            self.pUnk = pUnk
            IID__IMoniker = GUID(_IMoniker.guid)
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
            self._GetDisplayName = IAGFUNCTYPE(pUnk, IID__IMoniker, vtable_offset + GetDisplayNameIndex, PVOID, PVOID, POINTER(BSTR))
        def _FreeDisplayName(self, ppszDisplayName):
            pMalloc = IUnknown()
            CoGetMalloc(DWORD(1), byref(pMalloc.p))
            pMalloc.TakeOwnership()
            iMalloc = _IMalloc(pMalloc)
            iMalloc.Free(ppszDisplayName)
            del(iMalloc)
            del(pMalloc)
        def GetDisplayName(self) -> str:
            pbc = IUnknown()
            pmkToLeft = IUnknown()
            CreateBindCtx(DWORD(0), byref(pbc.p))
            pbc.TakeOwnership()
            ppszDisplayName = BSTR()
            self._GetDisplayName(pbc.p, pmkToLeft.p, byref(ppszDisplayName))
            display_name = ppszDisplayName.value
            self._FreeDisplayName(ppszDisplayName)
            del(pmkToLeft)
            del(pbc)
            return display_name
        
    def attach_to_stk_by_pid(pid:int) -> IUnknown:
        runningObjectTable = IUnknown()
        str_prog_id = "!STK.Application:" + str(pid)
        if Succeeded(GetRunningObjectTable(DWORD(0), byref(runningObjectTable.p))):
            runningObjectTable.TakeOwnership()
            runningObjectTable = _IRunningObjectTable(runningObjectTable)
            enumMoniker = runningObjectTable.EnumRunning()
            enumMoniker.Reset()
            moniker = enumMoniker.Next()
            while moniker is not None:
                instanceName = moniker.GetDisplayName()
                if instanceName == str_prog_id:
                    ret = runningObjectTable.GetObject(moniker)
                    del(moniker)
                    del(enumMoniker)
                    del(runningObjectTable)
                    return ret
                else:
                    moniker = enumMoniker.Next()
            del(moniker)
            del(enumMoniker)
            del(runningObjectTable)
        else:
            raise RuntimeError("Failed to retrieve the Running Object Table.")
else:
    def attach_to_stk_by_pid(pid:int) -> IUnknown:
        if os.name != "nt":
            raise RuntimeError("STKDesktop is only available on Windows. Use STKEngine.")

