# Copyright 2020-2023, Ansys Government Initiatives 

from __future__ import annotations

import os
import gc

from ctypes import c_void_p, c_longlong, c_ulonglong, c_int, c_uint, c_ulong, c_ushort, c_short, c_ubyte, c_wchar_p, c_double, c_float, c_bool
from ctypes import POINTER, Structure, Union, byref, cast, pointer 

from .apiutil import out_arg

###############################################################################
#   COM Types
###############################################################################
BSTR = c_wchar_p
BYTE = c_ubyte
CHAR = c_ubyte
DOUBLE = c_double
DWORD = c_ulong
INT = c_int
LONG = c_int #don't use c_long because of cross-platform size differences
FLOAT = c_float
HRESULT = c_int
LONGLONG = c_longlong
LPCOLESTR = c_wchar_p
LPCVOID = c_void_p
LPOLESTR = c_wchar_p
LPVOID = c_void_p
LPCWSTR = c_wchar_p
LPWSTR = c_wchar_p
OLESTR = c_wchar_p
PVOID = c_void_p
SHORT = c_short
UINT = c_uint
ULONG = c_uint #don't use c_long because of cross-platform size differences
ULONGLONG = c_ulonglong
USHORT = c_ushort
VARIANT_BOOL = c_short
VARTYPE = c_int
WORD = c_ushort
BOOL = c_bool

DATE = DOUBLE
DISPID = LONG
LCID = DWORD
OLE_COLOR = ULONG
OLE_HANDLE = UINT
OLE_XPOS_PIXELS = LONG
OLE_YPOS_PIXELS = LONG
LPSAFEARRAY = PVOID
LPSTREAM = PVOID


###############################################################################
#   Constants
###############################################################################
# CLSCTX Enumeration
CLSCTX_INPROC_SERVER = 1
CLSCTX_LOCAL_SERVER = 0x4

# COINIT enumeration
COINIT_APARTMENTTHREADED = 0x2

# HRESULT values
S_OK                = 0
E_NOTIMPL           = 0x80004001
E_NOINTERFACE       = 0x80004002
CO_E_NOTINITIALIZED = 0x800401F0

# Numeric Limits
ULLONG_MAX =  0xffffffffffffffff
LLONG_MAX  =  9223372036854775807
LLONG_MIN  = -9223372036854775808
LONG_MAX   =  2147483647
LONG_MIN   = -2147483648

# VARIANT_BOOL
VARIANT_FALSE = VARIANT_BOOL(0)
VARIANT_TRUE = VARIANT_BOOL(-1)

# VARIANT Types
VT_EMPTY           = 0x0000
VT_NULL            = 0x0001
VT_I2              = 0x0002
VT_I4              = 0x0003
VT_R4              = 0x0004
VT_R8              = 0x0005
VT_CY              = 0x0006
VT_DATE            = 0x0007
VT_BSTR            = 0x0008
VT_DISPATCH        = 0x0009
VT_ERROR           = 0x000A
VT_BOOL            = 0x000B
VT_VARIANT         = 0x000C
VT_UNKNOWN         = 0x000D
VT_DECIMAL         = 0x000E
VT_I1              = 0x0010
VT_UI1             = 0x0011
VT_UI2             = 0x0012
VT_UI4             = 0x0013
VT_I8              = 0x0014
VT_UI8             = 0x0015
VT_INT             = 0x0016
VT_UINT            = 0x0017
VT_VOID            = 0x0018
VT_HRESULT         = 0x0019
VT_PTR             = 0x001A
VT_SAFEARRAY       = 0x001B
VT_CARRAY          = 0x001C
VT_USERDEFINED     = 0x001D
VT_LPSTR           = 0x001E
VT_LPWSTR          = 0x001F
VT_INT_PTR         = 0x0025
VT_UINT_PTR        = 0x0026
VT_ARRAY           = 0x2000
VT_BYREF           = 0x4000


###############################################################################
#   COM Structures
###############################################################################
class GUID(Structure):
    _fields_ = [("Data1", BYTE*4), ("Data2", BYTE*2), ("Data3", BYTE*2), ("Data4", BYTE*8)]
    def __init__(self, name=None):
        if name is not None:
            if ole32lib.CLSIDFromString is None:
                ole32lib._initialize()
            ole32lib.CLSIDFromString(str(name), byref(self))

    @staticmethod
    def from_registry_format(data: str) -> "GUID":
        if len(data) != 38 or data[0] != "{" or data[-1] != "}":
            raise ValueError(f"{data} not a GUID in registry format")

        guid = GUID()

        data_bytes = bytes.fromhex(data[1:-1].replace('-', ''))

        guid.Data1 = (BYTE * 4).from_buffer_copy(data_bytes[3::-1])

        guid.Data2[0] = data_bytes[5]
        guid.Data2[1] = data_bytes[4]

        guid.Data3[0] = data_bytes[7]
        guid.Data3[1] = data_bytes[6]

        guid.Data4 = (BYTE * 8).from_buffer_copy(data_bytes[8:16])

        return guid

    def __eq__(self, other):
        are_equal = True
        if self.Data1[0] != other.Data1[0]: are_equal = False
        if self.Data1[1] != other.Data1[1]: are_equal = False
        if self.Data1[2] != other.Data1[2]: are_equal = False
        if self.Data1[3] != other.Data1[3]: are_equal = False
        if self.Data2[0] != other.Data2[0]: are_equal = False
        if self.Data2[1] != other.Data2[1]: are_equal = False
        if self.Data3[0] != other.Data3[0]: are_equal = False
        if self.Data3[1] != other.Data3[1]: are_equal = False
        if self.Data4[0] != other.Data4[0]: are_equal = False
        if self.Data4[1] != other.Data4[1]: are_equal = False
        if self.Data4[2] != other.Data4[2]: are_equal = False
        if self.Data4[3] != other.Data4[3]: are_equal = False
        if self.Data4[4] != other.Data4[4]: are_equal = False
        if self.Data4[5] != other.Data4[5]: are_equal = False
        if self.Data4[6] != other.Data4[6]: are_equal = False
        if self.Data4[7] != other.Data4[7]: are_equal = False
        return are_equal

    def __str__(self):
        return "{{{:02X}{:02X}{:02X}{:02X}-{:02X}{:02X}-{:02X}{:02X}-{:02X}{:02X}-{:02X}{:02X}{:02X}{:02X}{:02X}{:02X}}}".format(
            self.Data1[3],
            self.Data1[2],
            self.Data1[1],
            self.Data1[0],
            self.Data2[1],
            self.Data2[0],
            self.Data3[1],
            self.Data3[0],
            self.Data4[0],
            self.Data4[1],
            self.Data4[2],
            self.Data4[3],
            self.Data4[4],
            self.Data4[5],
            self.Data4[6],
            self.Data4[7])

IID = GUID
REFIID = POINTER(IID)
            
class varUnion(Union):
    # GCC throws an error when trying to marshall ctypes.Union to C++ methods. Therefore the VARIANT class
    # only has a raw buffer that is equivalent in size to the varUnion.
    _fields_ = [
                ("buffer", BYTE*16),
                ("llVal", LONGLONG), #VT_I8
                ("lVal", LONG), #VT_I4
                ("bVal", BYTE), #VT_UI1
                ("iVal", SHORT), #VT_I2
                ("fltVal", FLOAT), #VT_R4
                ("dblVal", DOUBLE), #VT_R8
                ("boolVal", VARIANT_BOOL), #VT_BOOL
                ("bstrVal", BSTR), #VT_BSTR
                ("punkVal", PVOID), #VT_UNKNOWN
                ("parray", LPSAFEARRAY), #VT_ARRAY
                ("pbVal", POINTER(BYTE)), #VT_UI1|VT_BYREF
                ("piVal", POINTER(SHORT)), #VT_I2|VT_BYREF
                ("plVal", POINTER(LONG)), #VT_I4|VT_BYREF
                ("pllVal", POINTER(LONGLONG)), #VT_I8|VT_BYREF
                ("pfltVal", POINTER(FLOAT)), #VT_R4|VT_BYREF
                ("pdblVal", POINTER(DOUBLE)), #VT_R8|VT_BYREF
                ("pboolVal", POINTER(VARIANT_BOOL)), #VT_BOOL|VT_BYREF
                ("pbstrVal", POINTER(BSTR)), #VT_BSTR|VT_BYREF
                ("ppunkVal", POINTER(PVOID)), #VT_UNKNOWN|VT_BYREF
                ("pparray", POINTER(LPSAFEARRAY)), #VT_ARRAY|VT_BYREF
                ("cVal", CHAR), #VT_I1
                ("uiVal", USHORT), #VT_UI2
                ("ulVal", ULONG), #VT_UI4
                ("ullVal", ULONGLONG), #VT_UI8
                ("intVal", INT), #VT_INT
                ("uintVal", UINT), #VT_UINT
                ("pcVal", POINTER(CHAR)), #VT_I1|VT_BYREF
                ("puiVal", POINTER(USHORT)), #VT_UI2|VT_BYREF
                ("pulVal", POINTER(ULONG)), #VT_UI4|VT_BYREF
                ("pullVal", POINTER(ULONGLONG)), #VT_UI8|VT_BYREF
                ("pintVal", POINTER(INT)), #VT_INT|VT_BYREF
                ("puintVal", POINTER(UINT)), #VT_UINT|VT_BYREF
                ("pvarVal", POINTER(PVOID)), #VT_VARIANT|VT_BYREF
                ("scode", HRESULT), #VT_ERROR
                ("pscode", POINTER(HRESULT)), #VT_ERROR|VT_BYREF
                ("pdispVal", PVOID), #VT_DISPATCH
                ("ppdispVal", POINTER(PVOID)) #VT_DISPATCH|VT_BYREF
               ]
                
class VARIANT(Structure):
    # Copy a varUnion into the buffer to get the correct data.
    _fields_ = [("vt", WORD), ("wReserved1", WORD), ("wReserved2", WORD), ("wReserved3", WORD), ("buffer", BYTE*16)]
    def __init__(self):
        # To initialize VARIANT from python data, use marshall.VARIANT_from_python_data
        pass
    
class SAFEARRAYBOUND(Structure):
    _fields_ = [("cElements", ULONG), ("lLbound", LONG)]
    
class DISPPARAMS(Structure):
    _fields_ = [("rgvarg", POINTER(VARIANT)), ("rgdispidNamedArgs", POINTER(DISPID)), ("cArgs", UINT), ("cNamedArgs", UINT)]
    
class EXCEPINFO(Structure):
    _fields_ = [
                ("wCode", WORD), 
                ("wReserved", WORD), 
                ("bstrSource", BSTR), 
                ("bstrDescription", BSTR), 
                ("bstrHelpFile", BSTR), 
                ("dwHelpContext", DWORD), 
                ("pvReserved", POINTER(ULONG)), 
                ("pfnDeferredFillIn", POINTER(ULONG)), 
                ("scode", HRESULT)
            ]

###############################################################################
#   COM Methods
###############################################################################

if os.name == "nt":
    from ctypes import WINFUNCTYPE
else:
    from ctypes import CFUNCTYPE
    WINFUNCTYPE = CFUNCTYPE

class ole32lib:

    _handle = None

    CLSIDFromString     = None
    CLSIDFromProgID     = None
    CoCreateInstance    = None
    CoInitializeEx      = None
    CoTaskMemFree       = None
    CoUninitialize      = None
    StringFromCLSID     = None

    if os.name=="nt":

        CoMarshalInterThreadInterfaceInStream = None
        CoGetInterfaceAndReleaseStream        = None
        CoReleaseMarshalData                  = None

        CreateClassMoniker    = None
        GetRunningObjectTable = None
        CreateBindCtx         = None
        CoGetMalloc           = None

    def _initialize():

        if ole32lib._handle is not None:
            return

        if os.name == "nt":
            from ctypes import windll
            ole32lib._handle = windll.ole32
        else:
            from ctypes import cdll
            ole32lib._handle = cdll.LoadLibrary("libagxcom.so")

        ole32lib.CLSIDFromString     = WINFUNCTYPE(HRESULT, LPCWSTR, POINTER(GUID))(("CLSIDFromString", ole32lib._handle), ((1, "lpsz"), (1, "pclsid")))
        ole32lib.CLSIDFromProgID     = WINFUNCTYPE(HRESULT, LPCWSTR, POINTER(GUID))(("CLSIDFromProgID", ole32lib._handle), ((1, "lpszProgID"), (1, "lpclsid")))
        ole32lib.CoCreateInstance    = WINFUNCTYPE(HRESULT, POINTER(GUID), LPVOID, DWORD, POINTER(GUID), POINTER(LPVOID))(("CoCreateInstance", ole32lib._handle),
                                       ((1, "rclsid"), (1, "pUnkOuter"), (1, "dwClsContext"), (1, "riid"), (1, "ppv")))
        ole32lib.CoInitializeEx      = WINFUNCTYPE(HRESULT, c_void_p, DWORD)(("CoInitializeEx", ole32lib._handle), ((1, "pvReserved"), (1, "dwCoInit")))
        ole32lib.CoTaskMemFree       = WINFUNCTYPE(None, LPVOID)(("CoTaskMemFree", ole32lib._handle), ((1, "pv"),))
        ole32lib.CoUninitialize      = WINFUNCTYPE(None)(("CoUninitialize", ole32lib._handle))
        ole32lib.StringFromCLSID     = WINFUNCTYPE(HRESULT, POINTER(GUID), POINTER(LPOLESTR))(("StringFromCLSID", ole32lib._handle), ((1, "rclsid"), (1, "lplpsz")))

        if os.name=="nt":

            ole32lib.CoMarshalInterThreadInterfaceInStream = WINFUNCTYPE(HRESULT, REFIID, PVOID, POINTER(LPSTREAM))(("CoMarshalInterThreadInterfaceInStream", ole32lib._handle), ((1, "riid"), (1, "pUnk"), (1, "ppStm")))
            ole32lib.CoGetInterfaceAndReleaseStream        = WINFUNCTYPE(HRESULT, LPSTREAM, REFIID, POINTER(PVOID))(("CoGetInterfaceAndReleaseStream", ole32lib._handle), ((1, "pStm"), (1, "iid"), (1, "ppv")))
            ole32lib.CoReleaseMarshalData                  = WINFUNCTYPE(HRESULT, LPSTREAM)(("CoReleaseMarshalData", ole32lib._handle), ((1, "pStm"),))

            ole32lib.CreateClassMoniker    = WINFUNCTYPE(HRESULT, GUID, POINTER(LPVOID))(("CreateClassMoniker", ole32lib._handle), ((1, "rclsid"), (1, "ppmk")))
            ole32lib.GetRunningObjectTable = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("GetRunningObjectTable", ole32lib._handle), ((1, "dwReserved"), (1, "pprot")))
            ole32lib.CreateBindCtx         = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("CreateBindCtx", ole32lib._handle), ((1, "dwReserved"), (1, "ppbc")))
            ole32lib.CoGetMalloc           = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("CoGetMalloc", ole32lib._handle), ((1, "dwMemContext"), (1, "ppMalloc")))

class oleaut32lib:

    _handle = None

    GetActiveObject     = None
    GetErrorInfo        = None
    SafeArrayCreate     = None
    SafeArrayDestroy    = None
    SafeArrayGetDim     = None
    SafeArrayGetLBound  = None
    SafeArrayGetUBound  = None
    SafeArrayGetVartype = None
    SafeArrayGetElement = None
    SafeArrayPutElement = None
    SysAllocString      = None
    SysFreeString       = None
    VariantClear        = None
    VariantCopy         = None
    VariantInit         = None

    def _initialize():

        if oleaut32lib._handle is not None:
            return

        if os.name == "nt":
            from ctypes import windll
            oleaut32lib._handle = windll.OleAut32
        else:
            from ctypes import cdll
            oleaut32lib._handle = cdll.LoadLibrary("libagxcom.so")

        oleaut32lib.GetActiveObject     = WINFUNCTYPE(HRESULT, POINTER(GUID), LPVOID, POINTER(LPVOID))(("GetActiveObject", oleaut32lib._handle),
                                       ((1, "rclsid"), (1, "pvReserved"), (1, "ppunk"))) if os.name=="nt" else None
        oleaut32lib.GetErrorInfo        = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("GetErrorInfo", oleaut32lib._handle), ((1, "dwReserved"), (1, "ppErrorInfo")))
        oleaut32lib.SafeArrayAccessData = WINFUNCTYPE(HRESULT, LPSAFEARRAY, POINTER(LPVOID))(("SafeArrayAccessData", oleaut32lib._handle), ((1, "pSafeArray"), (1, "ppvData")))
        oleaut32lib.SafeArrayCreate     = WINFUNCTYPE(LPSAFEARRAY, VARTYPE, UINT, POINTER(SAFEARRAYBOUND))(("SafeArrayCreate", oleaut32lib._handle), ((1, "vt"), (1, "cDims"), (1, "rgsabound")))
        oleaut32lib.SafeArrayDestroy    = WINFUNCTYPE(HRESULT, LPSAFEARRAY)(("SafeArrayDestroy", oleaut32lib._handle), ((1, "pSafeArray"),))
        oleaut32lib.SafeArrayGetDim     = WINFUNCTYPE(UINT,    LPSAFEARRAY)(("SafeArrayGetDim", oleaut32lib._handle), ((1, "pSafeArray"),))
        oleaut32lib.SafeArrayGetLBound  = WINFUNCTYPE(HRESULT, LPSAFEARRAY, UINT, POINTER(LONG))(("SafeArrayGetLBound", oleaut32lib._handle), ((1, "pSafeArray"), (1, "nDim"), (1, "pLBound")))
        oleaut32lib.SafeArrayGetUBound  = WINFUNCTYPE(HRESULT, LPSAFEARRAY, UINT, POINTER(LONG))(("SafeArrayGetUBound", oleaut32lib._handle), ((1, "pSafeArray"), (1, "nDim"), (1, "pUBound")))
        oleaut32lib.SafeArrayGetVartype = WINFUNCTYPE(HRESULT, LPSAFEARRAY, POINTER(VARTYPE))(("SafeArrayGetVartype", oleaut32lib._handle), ((1, "pSafeArray"), (1, "vt")))
        oleaut32lib.SafeArrayGetElement = WINFUNCTYPE(HRESULT, LPSAFEARRAY, POINTER(LONG), PVOID)(("SafeArrayGetElement", oleaut32lib._handle), ((1, "pSafeArray"), (1, "rgIndices"), (1, "pElement")))
        oleaut32lib.SafeArrayPutElement = WINFUNCTYPE(HRESULT, LPSAFEARRAY, POINTER(LONG), PVOID)(("SafeArrayPutElement", oleaut32lib._handle), ((1, "pSafeArray"), (1, "rgIndices"), (1, "pElement")))
        oleaut32lib.SafeArrayUnaccessData = WINFUNCTYPE(HRESULT, LPSAFEARRAY)(("SafeArrayUnaccessData", oleaut32lib._handle), ((1, "pSafeArray"),))
        oleaut32lib.SysAllocString      = WINFUNCTYPE(LPVOID, LPOLESTR)(("SysAllocString", oleaut32lib._handle), ((1, "psz"),))
        oleaut32lib.SysFreeString       = WINFUNCTYPE(None, LPOLESTR)(("SysFreeString", oleaut32lib._handle), ((1, "bstrString"),))
        oleaut32lib.VariantClear        = WINFUNCTYPE(HRESULT, POINTER(VARIANT))(("VariantClear", oleaut32lib._handle), ((1, "pVariant"),))
        oleaut32lib.VariantCopy         = WINFUNCTYPE(HRESULT, POINTER(VARIANT), POINTER(VARIANT))(("VariantCopy", oleaut32lib._handle), ((1, "pvargDest"),(1, "pvargSrc")))
        oleaut32lib.VariantInit         = WINFUNCTYPE(None, POINTER(VARIANT))(("VariantInit", oleaut32lib._handle), ((1, "pVariant"),))

###############################################################################
#   Helper functions
###############################################################################
def Succeeded(hr):
    return hr >= S_OK
    
class _gc_disabler(object):
    def __init__(self):
        self._is_gc_enabled = False
    def __enter__(self):
        if gc.isenabled():
            self._is_gc_enabled = True
            gc.disable()
        return self
    def __exit__(self, type, value, tb):
        if self._is_gc_enabled:
            gc.enable()
        return False

class _CreateAgObjectLifetimeManager(object):
    """Singleton class for managing reference counts on COM interfaces."""
    _AddRef = WINFUNCTYPE(ULONG, LPVOID)
    _Release = WINFUNCTYPE(ULONG, LPVOID)
    if os.name == "nt":
        _AddRefIndex = 1
        _ReleaseIndex = 2
    else:
        _AddRefIndex = 0
        _ReleaseIndex = 1

    def __init__(self):
        self._ref_counts = dict()
        self._applications = list()
        
    @staticmethod
    def _ReleaseImpl(pUnk:"IUnknown"):
        """Call Release in STK."""
        _CreateAgObjectLifetimeManager._Release(pUnk._getVtblEntry(_CreateAgObjectLifetimeManager._ReleaseIndex))(pUnk.p)
        
    @staticmethod
    def _AddRefImpl(pUnk:"IUnknown"):
        """Call AddRef in STK."""
        _CreateAgObjectLifetimeManager._AddRef(pUnk._getVtblEntry(_CreateAgObjectLifetimeManager._AddRefIndex))(pUnk.p)
                
    def create_ownership(self, pUnk:"IUnknown"):
        """
        Adds pUnk to the reference manager and calls AddRef in STK.

        Use if pUnk has a ref-count of 0.
        """
        ptraddress = pUnk.p.value
        if ptraddress is not None:
            _CreateAgObjectLifetimeManager._AddRefImpl(pUnk)
            self.take_ownership(pUnk, False)
                
    def take_ownership(self, pUnk:"IUnknown", isApplication=False):
        """
        Adds pUnk to the reference manager; does not call AddRef in STK.

        Use if pUnk has a ref-count of 1.
        """
        ptraddress = pUnk.p.value
        if ptraddress is not None:
            with _gc_disabler() as gc_lock:
                if isApplication:
                    self._applications.append(ptraddress)
                if ptraddress in self._ref_counts:
                    _CreateAgObjectLifetimeManager._ReleaseImpl(pUnk)
                    self.InternalAddRef(pUnk)
                else:
                    self._ref_counts[ptraddress] = 1
                
    def InternalAddRef(self, pUnk:"IUnknown"):
        """Increment the internal reference count of pUnk."""
        ptraddress = pUnk.p.value
        with _gc_disabler() as gc_lock:
            if ptraddress in self._ref_counts:
                self._ref_counts[ptraddress] = self._ref_counts[ptraddress] + 1

    def Release(self, pUnk:"IUnknown"):
        """
        Decrements the internal reference count of pUnk.
        
        If the internal reference count reaches zero, calls Release in STK.
        """
        ptraddress = pUnk.p.value
        if ptraddress is not None:
            with _gc_disabler() as gc_lock:
                if ptraddress in self._ref_counts:
                    if self._ref_counts[ptraddress] == 1:
                        _CreateAgObjectLifetimeManager._ReleaseImpl(pUnk)
                        del(self._ref_counts[ptraddress])
                    else:
                        self._ref_counts[ptraddress] = self._ref_counts[ptraddress] - 1
                
    def ReleaseAll(self, releaseApplication=True):
        with _gc_disabler() as gc_lock:
            preserved_app_ref_counts = dict()
            while len(self._ref_counts) > 0:
                ref_count = self._ref_counts.popitem()
                ptraddress = ref_count[0]
                if not releaseApplication and ptraddress in self._applications:
                    preserved_app_ref_counts[ptraddress] = ref_count[1]
                    continue
                pUnk = IUnknown()
                pUnk.p = c_void_p(ptraddress)
                _CreateAgObjectLifetimeManager._ReleaseImpl(pUnk)
                pUnk.p = c_void_p(0)
            self._ref_counts = preserved_app_ref_counts

ObjectLifetimeManager = _CreateAgObjectLifetimeManager()


class _CreateCoInitializeManager(object):
    def __init__(self):
        self.init_count = 0
        
    def initialize(self):
        if self.init_count == 0:
            ole32lib._initialize()
            oleaut32lib._initialize()
            ole32lib.CoInitializeEx(None, COINIT_APARTMENTTHREADED)
        self.init_count = self.init_count + 1
        
    def uninitialize(self):
        self.init_count = self.init_count - 1
        if self.init_count == 0:
            ole32lib.CoUninitialize()
            
CoInitializeManager = _CreateCoInitializeManager()

def _initialize_embedded():
    """Called by STK during plugin initialization."""
    ole32lib._initialize()
    oleaut32lib._initialize()

###############################################################################
#   Interfaces
###############################################################################
class IUnknown(object):
    _guid = "{00000000-0000-0000-C000-000000000046}"
    _vtable_offset = 0
    _num_methods = 3
    _QueryInterface = WINFUNCTYPE(HRESULT, LPVOID, POINTER(GUID), POINTER(LPVOID))
    if os.name == "nt":
        _QIIndex = 0
    else:
        _QIIndex = 2
    def __init__(self, pUnk=None):
        if pUnk is not None:
            self.p = pUnk.p
            self.AddRef()
        else:
            self.p = c_void_p()
    def __del__(self):
        if self:
            self.Release()
    def __eq__(self, other):
        return self.p.value == other.p.value
    def __hash__(self):
        return self.p.value
    def __bool__(self):
        return self.p.value is not None and self.p.value > 0
    def _getVtblEntry(self, index):
        vptr = cast(self.p, POINTER(c_void_p))
        vtbl = cast(vptr.contents, POINTER(c_void_p))
        return vtbl[index]
    def query_interface(self, iid:GUID|str) -> "IUnknown":
        pIntf = IUnknown()
        if isinstance(iid, str): iid=GUID(iid)
        hr = IUnknown._QueryInterface(self._getVtblEntry(IUnknown._QIIndex))(self.p, byref(iid), byref(pIntf.p))
        if not Succeeded(hr):
            return None
        pIntf.take_ownership()
        return pIntf
    def create_ownership(self):
        """Call AddRef on the pointer, and register the pointer to be Released when the ref count goes to zero."""
        ObjectLifetimeManager.create_ownership(self) 
    def take_ownership(self, isApplication=False):
        """Register the pointer to be Released when the ref count goes to zero but does not call AddRef."""
        ObjectLifetimeManager.take_ownership(self, isApplication) 
    def AddRef(self):
        """Increment the ref count if the pointer was registered.
        
        Pointer registration must be done by create_ownership or take_ownership.
        """
        ObjectLifetimeManager.InternalAddRef(self)  
    def Release(self):
        """Decrement the ref count if the pointer was registered. Calls Release if the ref count goes to zero.
        
        Pointer registration must be done by create_ownership or take_ownership.
        """
        ObjectLifetimeManager.Release(self)   

    def invoke(self, intf_metatdata:dict, method_metadata:dict, *args):
        method_offset = intf_metatdata["method_offsets"][method_metadata["name"]]
        return self._invoke_impl(intf_metatdata, method_metadata, method_offset, *args)

    def get_property(self, intf_metatdata:dict, method_metadata:dict):
        method_offset = intf_metatdata["method_offsets"]["get_" + method_metadata["name"]]
        return self._invoke_impl(intf_metatdata, method_metadata, method_offset, out_arg())

    def set_property(self, intf_metatdata:dict, method_metadata:dict, value):
        method_offset = intf_metatdata["method_offsets"]["set_" + method_metadata["name"]]
        return self._invoke_impl(intf_metatdata, method_metadata, method_offset, value)

    def _invoke_impl(self, intf_metatdata:dict, method_metadata:dict, method_offset:int, *args):
        from .coclassutil import evaluate_hresult
        guid = GUID(intf_metatdata["uuid"])
        vtable_index = intf_metatdata["vtable_reference"] + method_offset
        arg_types = method_metadata["arg_types"]
        marshaller_classes = method_metadata["marshallers"]
        method = IAGFUNCTYPE(self, guid, vtable_index, *arg_types)
        marshallers = []
        for arg, marshaller_class in zip(args, marshaller_classes):
            if type(arg) is out_arg:
                marshaller = marshaller_class()
                marshallers.append(marshaller)
            else:
                marshaller = marshaller_class(arg)
                marshallers.append(marshaller)
        call_args = []
        for marshaller, arg_type in zip(marshallers, arg_types):
            if type(arg_type) == type(POINTER(PVOID)): # type(POINTER(X)) == type(POINTER(Y)) for all X,Y. the choice of PVOID was arbitrary
                call_args.append(byref(marshaller.COM_val))
            else:
                call_args.append(marshaller.COM_val)
        evaluate_hresult(method(*call_args))
        return_vals = []
        for arg, marshaller in zip(args, marshallers):
            if type(arg) is out_arg:
                return_vals.append(marshaller.python_val)  
        del(marshallers)
        if len(return_vals) == 0:
            return
        elif len(return_vals) == 1:
            return return_vals[0]
        else:
            return tuple(return_vals)      

class IDispatch(IUnknown):
    _guid = "{00020400-0000-0000-C000-000000000046}"
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _num_methods = 4
    def __init__(self, pUnk: IUnknown):
        IUnknown.__init__(self, pUnk)
          
class IPictureDisp(IUnknown):
    def __init__(self):
        raise STKRuntimeError("IPictureDisp not supported.")
        
class IEnumVARIANT(object):
    guid = "{00020404-0000-0000-C000-000000000046}"
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _num_methods = 4
    def __init__(self, pUnk):
        self.pUnk = pUnk
        IID_IEnumVARIANT = GUID(IEnumVARIANT.guid)
        vtable_offset_local = IEnumVARIANT._vtable_offset - 1
        self._Next  = IAGFUNCTYPE(pUnk, IID_IEnumVARIANT, vtable_offset_local+1, ULONG, POINTER(VARIANT), POINTER(ULONG))
        self._Reset = IAGFUNCTYPE(pUnk, IID_IEnumVARIANT, vtable_offset_local+3)
    def next(self) -> VARIANT:
        from .marshall import python_val_from_VARIANT
        one_obj = ULONG(1)
        num_fetched = ULONG()
        obj = VARIANT()
        oleaut32lib.VariantInit(obj)
        if self._Next(one_obj, byref(obj), byref(num_fetched)) == S_OK:
            return python_val_from_VARIANT(obj, clear_variant=True)
        else:
            return None
    def reset(self) -> None:
        self._Reset()
          
class IAGFUNCTYPE(object):
    """Wrapper for calling methods into COM interface vtables."""
    def __init__(self, pUnk, iid, method_index, *argtypes):
        self.pUnk = pUnk
        self.iid = iid
        self.index = method_index
        self.method = WINFUNCTYPE(HRESULT, LPVOID, *argtypes)
    def __call__(self, *args):
        pIntf = self.pUnk.query_interface(self.iid)
        ret = self.method(pIntf._getVtblEntry(self.index))(pIntf.p, *args)
        del(pIntf)
        return ret
