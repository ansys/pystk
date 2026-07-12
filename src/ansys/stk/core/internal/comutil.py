# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

import os
import typing

from ctypes import c_void_p, c_longlong, c_ulonglong, c_int, c_uint, c_ulong, c_ushort, c_short, c_ubyte, c_wchar_p, c_double, c_float, c_bool
from ctypes import POINTER, Structure, Union, byref, cast, pointer, addressof

from .apiutil import OutArg

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
PGRPCBYTES = PVOID


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

# Variant Types
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
            if OLE32Lib.CLSIDFromString is None:
                OLE32Lib._initialize()
            OLE32Lib.CLSIDFromString(str(name), byref(self))

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

    _data_pair_cache = {}

    @staticmethod
    def from_data_pair(data:tuple) -> "GUID":
        if data not in GUID._data_pair_cache:
            guid_union = _guid_union(data)
            GUID._data_pair_cache[data] = guid_union.guid
        return GUID._data_pair_cache[data]

    def as_data_pair(self) -> tuple:
        guid_union = _guid_union(self)
        return (guid_union.data[0], guid_union.data[1])

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

class _guid_union(Union):
    _fields_ = [("guid", GUID), ("data", ULONGLONG*2)]
    def __init__(self, iid:typing.Union[GUID, tuple]):
        if type(iid) == tuple:
            self.data[0] = iid[0]
            self.data[1] = iid[1]
        else:
            self.guid = iid

IID = GUID
REFIID = POINTER(IID)

class Variant(Structure):
    # Copy a varUnion into the buffer to get the correct data.
    _fields_ = [("vt", WORD), ("wReserved1", WORD), ("wReserved2", WORD), ("wReserved3", WORD), ("buffer", BYTE*16)]
    def __init__(self):
        # To initialize Variant from python data, use marshall.VARIANT_from_python_data
        pass

class varUnion(Union):
    # GCC throws an error when trying to marshall ctypes.Union to C++ methods. Therefore the Variant class
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
                ("pvarVal", POINTER(Variant)), #VT_VARIANT|VT_BYREF
                ("scode", HRESULT), #VT_ERROR
                ("pscode", POINTER(HRESULT)), #VT_ERROR|VT_BYREF
                ("pdispVal", PVOID), #VT_DISPATCH
                ("ppdispVal", POINTER(PVOID)) #VT_DISPATCH|VT_BYREF
               ]

class SafearrayBound(Structure):
    _fields_ = [("cElements", ULONG), ("lLbound", LONG)]

class DispParams(Structure):
    _fields_ = [("rgvarg", POINTER(Variant)), ("rgdispidNamedArgs", POINTER(DISPID)), ("cArgs", UINT), ("cNamedArgs", UINT)]

class ExcepInfo(Structure):
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

class OLE32Lib:

    _handle = None

    CLSIDFromString     = None
    CLSIDFromProgID     = None
    CoCreateInstance    = None
    CoInitializeEx      = None
    CoTaskMemFree       = None
    CoUninitialize      = None
    StringFromCLSID     = None

    use_xcom_registry = False
    xcom_bin_dir = None
    if os.name != "nt":
        use_xcom_registry = True
    elif os.getenv("STK_USE_XCOM_REGISTRY") is not None:
        use_xcom_registry = True
        if os.getenv("STK_BIN_DIR") is not None:
            xcom_bin_dir = os.path.normpath(os.getenv("STK_BIN_DIR"))

    if not use_xcom_registry:
        CoMarshalInterThreadInterfaceInStream = None
        CoGetInterfaceAndReleaseStream        = None
        CoReleaseMarshalData                  = None
        CreateClassMoniker    = None
        GetRunningObjectTable = None
        CreateBindCtx         = None
        CoGetMalloc           = None

    def _initialize():

        if OLE32Lib._handle is not None:
            return

        if os.name == "nt" and not OLE32Lib.use_xcom_registry:
            from ctypes import windll
            OLE32Lib._handle = windll.ole32
        else:
            from ctypes import cdll
            if os.name == "nt":
                try:
                    if OLE32Lib.xcom_bin_dir is not None:
                        OLE32Lib._handle = cdll.LoadLibrary(os.path.join(OLE32Lib.xcom_bin_dir, "AgXCom.dll"))
                    else:
                        raise RuntimeError("Error loading STK libraries. Ensure STK libraries can be found from the STK_BIN_DIR environment variable.")
                except FileNotFoundError as e:
                    raise RuntimeError(f"Error loading STK libraries. Ensure STK libraries can be found from the STK_BIN_DIR environment variable.") from e
            else:
                OLE32Lib._handle = cdll.LoadLibrary("libagxcom.so")

        xcom_prefix = "AgXCom" if OLE32Lib.use_xcom_registry else ""

        OLE32Lib.CLSIDFromString     = WINFUNCTYPE(HRESULT, LPCWSTR, POINTER(GUID))((f"{xcom_prefix}CLSIDFromString", OLE32Lib._handle), ((1, "lpsz"), (1, "pclsid")))
        OLE32Lib.CLSIDFromProgID     = WINFUNCTYPE(HRESULT, LPCWSTR, POINTER(GUID))((f"{xcom_prefix}CLSIDFromProgID", OLE32Lib._handle), ((1, "lpszProgID"), (1, "lpclsid")))
        OLE32Lib.CoCreateInstance    = WINFUNCTYPE(HRESULT, POINTER(GUID), LPVOID, DWORD, POINTER(GUID), POINTER(LPVOID))((f"{xcom_prefix}CoCreateInstance", OLE32Lib._handle),
                                       ((1, "rclsid"), (1, "pUnkOuter"), (1, "dwClsContext"), (1, "riid"), (1, "ppv")))
        OLE32Lib.CoInitializeEx      = WINFUNCTYPE(HRESULT, c_void_p, DWORD)((f"{xcom_prefix}CoInitializeEx", OLE32Lib._handle), ((1, "pvReserved"), (1, "dwCoInit")))
        OLE32Lib.CoUninitialize      = WINFUNCTYPE(None)((f"{xcom_prefix}CoUninitialize", OLE32Lib._handle))
        OLE32Lib.StringFromCLSID     = WINFUNCTYPE(HRESULT, POINTER(GUID), POINTER(LPOLESTR))((f"{xcom_prefix}StringFromCLSID", OLE32Lib._handle), ((1, "rclsid"), (1, "lplpsz")))

        if os.name == "nt":
            from ctypes import windll
            OLE32Lib.CoTaskMemFree = WINFUNCTYPE(None, LPVOID)(("CoTaskMemFree", windll.ole32), ((1, "pv"),))
        else:
            OLE32Lib.CoTaskMemFree = WINFUNCTYPE(None, LPVOID)(("CoTaskMemFree", OLE32Lib._handle), ((1, "pv"),))

        if os.name == "nt" and not OLE32Lib.use_xcom_registry:

            OLE32Lib.CoMarshalInterThreadInterfaceInStream = WINFUNCTYPE(HRESULT, REFIID, PVOID, POINTER(LPSTREAM))(("CoMarshalInterThreadInterfaceInStream", OLE32Lib._handle), ((1, "riid"), (1, "pUnk"), (1, "ppStm")))
            OLE32Lib.CoGetInterfaceAndReleaseStream        = WINFUNCTYPE(HRESULT, LPSTREAM, REFIID, POINTER(PVOID))(("CoGetInterfaceAndReleaseStream", OLE32Lib._handle), ((1, "pStm"), (1, "iid"), (1, "ppv")))
            OLE32Lib.CoReleaseMarshalData                  = WINFUNCTYPE(HRESULT, LPSTREAM)(("CoReleaseMarshalData", OLE32Lib._handle), ((1, "pStm"),))

            OLE32Lib.CreateClassMoniker    = WINFUNCTYPE(HRESULT, GUID, POINTER(LPVOID))(("CreateClassMoniker", OLE32Lib._handle), ((1, "rclsid"), (1, "ppmk")))
            OLE32Lib.GetRunningObjectTable = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("GetRunningObjectTable", OLE32Lib._handle), ((1, "dwReserved"), (1, "pprot")))
            OLE32Lib.CreateBindCtx         = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("CreateBindCtx", OLE32Lib._handle), ((1, "dwReserved"), (1, "ppbc")))
            OLE32Lib.CoGetMalloc           = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("CoGetMalloc", OLE32Lib._handle), ((1, "dwMemContext"), (1, "ppMalloc")))

class OLEAut32Lib:

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

        if OLEAut32Lib._handle is not None:
            return

        if os.name == "nt":
            from ctypes import windll
            OLEAut32Lib._handle = windll.OleAut32
        else:
            from ctypes import cdll
            OLEAut32Lib._handle = cdll.LoadLibrary("libagxcom.so")

        OLEAut32Lib.GetActiveObject     = WINFUNCTYPE(HRESULT, POINTER(GUID), LPVOID, POINTER(LPVOID))(("GetActiveObject", OLEAut32Lib._handle),
                                       ((1, "rclsid"), (1, "pvReserved"), (1, "ppunk"))) if os.name=="nt" else None
        OLEAut32Lib.GetErrorInfo        = WINFUNCTYPE(HRESULT, DWORD, POINTER(LPVOID))(("GetErrorInfo", OLEAut32Lib._handle), ((1, "dwReserved"), (1, "ppErrorInfo")))
        OLEAut32Lib.SafeArrayAccessData = WINFUNCTYPE(HRESULT, LPSAFEARRAY, POINTER(LPVOID))(("SafeArrayAccessData", OLEAut32Lib._handle), ((1, "pSafeArray"), (1, "ppvData")))
        OLEAut32Lib.SafeArrayCreate     = WINFUNCTYPE(LPSAFEARRAY, VARTYPE, UINT, POINTER(SafearrayBound))(("SafeArrayCreate", OLEAut32Lib._handle), ((1, "vt"), (1, "cDims"), (1, "rgsabound")))
        OLEAut32Lib.SafeArrayDestroy    = WINFUNCTYPE(HRESULT, LPSAFEARRAY)(("SafeArrayDestroy", OLEAut32Lib._handle), ((1, "pSafeArray"),))
        OLEAut32Lib.SafeArrayGetDim     = WINFUNCTYPE(UINT,    LPSAFEARRAY)(("SafeArrayGetDim", OLEAut32Lib._handle), ((1, "pSafeArray"),))
        OLEAut32Lib.SafeArrayGetLBound  = WINFUNCTYPE(HRESULT, LPSAFEARRAY, UINT, POINTER(LONG))(("SafeArrayGetLBound", OLEAut32Lib._handle), ((1, "pSafeArray"), (1, "nDim"), (1, "pLBound")))
        OLEAut32Lib.SafeArrayGetUBound  = WINFUNCTYPE(HRESULT, LPSAFEARRAY, UINT, POINTER(LONG))(("SafeArrayGetUBound", OLEAut32Lib._handle), ((1, "pSafeArray"), (1, "nDim"), (1, "pUBound")))
        OLEAut32Lib.SafeArrayGetVartype = WINFUNCTYPE(HRESULT, LPSAFEARRAY, POINTER(VARTYPE))(("SafeArrayGetVartype", OLEAut32Lib._handle), ((1, "pSafeArray"), (1, "vt")))
        OLEAut32Lib.SafeArrayGetElement = WINFUNCTYPE(HRESULT, LPSAFEARRAY, POINTER(LONG), PVOID)(("SafeArrayGetElement", OLEAut32Lib._handle), ((1, "pSafeArray"), (1, "rgIndices"), (1, "pElement")))
        OLEAut32Lib.SafeArrayPutElement = WINFUNCTYPE(HRESULT, LPSAFEARRAY, POINTER(LONG), PVOID)(("SafeArrayPutElement", OLEAut32Lib._handle), ((1, "pSafeArray"), (1, "rgIndices"), (1, "pElement")))
        OLEAut32Lib.SafeArrayUnaccessData = WINFUNCTYPE(HRESULT, LPSAFEARRAY)(("SafeArrayUnaccessData", OLEAut32Lib._handle), ((1, "pSafeArray"),))
        OLEAut32Lib.SysAllocString      = WINFUNCTYPE(LPVOID, LPOLESTR)(("SysAllocString", OLEAut32Lib._handle), ((1, "psz"),))
        OLEAut32Lib.SysFreeString       = WINFUNCTYPE(None, LPOLESTR)(("SysFreeString", OLEAut32Lib._handle), ((1, "bstrString"),))
        OLEAut32Lib.VariantClear        = WINFUNCTYPE(HRESULT, POINTER(Variant))(("VariantClear", OLEAut32Lib._handle), ((1, "pVariant"),))
        OLEAut32Lib.VariantCopy         = WINFUNCTYPE(HRESULT, POINTER(Variant), POINTER(Variant))(("VariantCopy", OLEAut32Lib._handle), ((1, "pvargDest"),(1, "pvargSrc")))
        OLEAut32Lib.VariantInit         = WINFUNCTYPE(None, POINTER(Variant))(("VariantInit", OLEAut32Lib._handle), ((1, "pVariant"),))

###############################################################################
#   Helper functions
###############################################################################
def Succeeded(hr):
    return hr >= S_OK

class _CreateAgObjectLifetimeManager(object):
    """Singleton class for managing the lifetime of COM interfaces."""

    def __init__(self):
        self._objects = set()
        self._applications = set()
        self._shutting_down = False

    def add_application(self, pUnk:"IUnknown"):
        """Add pUnk to the list of applications."""
        self._applications.add(pUnk)

    def add_object(self, pUnk:"IUnknown"):
        """Add pUnk to the reference manager."""
        self._objects.add(pUnk)

    def remove_object(self, pUnk:"IUnknown"):
        """Remove pUnk from the reference manager."""
        if not self._shutting_down:
            if pUnk in self._objects:
                self._objects.remove(pUnk)
            elif pUnk in self._applications:
                self._applications.remove(pUnk)

    def release_all(self, release_applications=True):
        self._shutting_down = True
        for obj in self._objects:
            obj.final_release()
        self._objects = set()
        if release_applications:
            for app in self._applications:
                app.final_release()
            self._applications = set()
        self._shutting_down = False

ObjectLifetimeManager = _CreateAgObjectLifetimeManager()


class _CreateCoInitializeManager(object):
    def __init__(self, ole32lib, oleaut32lib):
        self.init_count = 0
        self.ole32lib = ole32lib
        self.oleaut32lib = oleaut32lib

    def initialize(self):
        if self.init_count == 0:
            self.ole32lib._initialize()
            self.oleaut32lib._initialize()
            self.ole32lib.CoInitializeEx(None, COINIT_APARTMENTTHREADED)
        self.init_count = self.init_count + 1

    def uninitialize(self):
        self.init_count = self.init_count - 1
        if self.init_count == 0:
            self.ole32lib.CoUninitialize()

CoInitializeManager = _CreateCoInitializeManager(OLE32Lib, OLEAut32Lib)

def _initialize_embedded():
    """Initialize OLE libraries for plugin initialization."""
    OLE32Lib._initialize()
    OLEAut32Lib._initialize()

###############################################################################
#   Interfaces
###############################################################################
class IUnknown(object):
    _guid = "{00000000-0000-0000-C000-000000000046}"
    _vtable_offset = 0
    _num_methods = 3
    _AddRef = WINFUNCTYPE(ULONG, LPVOID)
    _Release = WINFUNCTYPE(ULONG, LPVOID)
    _QueryInterface = WINFUNCTYPE(HRESULT, LPVOID, POINTER(GUID), POINTER(LPVOID))
    _ptr_to_vtable = POINTER(POINTER(c_void_p))
    _metadata = {
        "iid_data" : (0, 5044031582654955712),
    }
    if os.name == "nt":
        _QIIndex = 0
        _AddRefIndex = 1
        _ReleaseIndex = 2
    else:
        _AddRefIndex = 0
        _ReleaseIndex = 1
        _QIIndex = 2
    def __init__(self):
        self._vtbl = None
        self._vtbl_p_value = -1
        self._interfaces = {}
        self.p = c_void_p()
        self._skip_release = False
        self._application = False
        # Local references needed during shutdown
        self._ObjectLifetimeManager = ObjectLifetimeManager
        self._Release = IUnknown._Release
        self._ReleaseIndex = IUnknown._ReleaseIndex
    @staticmethod
    def create_weak_interface(addr:int, prefetch_interface_iids:tuple[tuple[int, int]]=()) -> "IUnknown":
        """
        Create a weak Python wrapper around IUnknown without owning the reference.

        addr is the integer value of the IUnknown pointer address.
        prefetch_interface_iids are a set of interface iids that the wrapped interface implements.
            Providing these improves performance by bypassing calls to QueryInterface. IUnknown
            is always prefetched.
        """
        pUnk = IUnknown()
        pUnk.p.value = addr
        pUnk._interfaces[IUnknown._metadata["iid_data"]] = pUnk
        for prefetch_iid in prefetch_interface_iids:
            pUnk._interfaces[prefetch_iid] = pUnk
        pUnk._skip_release = True
        return pUnk
    def __del__(self):
        self._ObjectLifetimeManager.remove_object(self)
        self.final_release()
    def __eq__(self, other):
        return self.p.value == other.p.value
    def __hash__(self):
        return id(self)
    def __bool__(self):
        return self.p.value is not None and self.p.value > 0
    def _ensure_vtbl(self):
        if self.p.value != self._vtbl_p_value:
            self._vtbl_p_value = self.p.value
            self._vtbl = IUnknown._ptr_to_vtable.from_address(addressof(self.p))[0]
    def _get_vtbl_entry(self, index):
        self._ensure_vtbl()
        return self._vtbl[index]
    def _query_backwards_compatability_interface(self, iid):
        from .coclassutil import AgBackwardsCompatabilityMapping
        iid_tuple = iid.as_data_pair()
        if AgBackwardsCompatabilityMapping.check_guid_available(iid_tuple):
            old_iid = GUID.from_data_pair(AgBackwardsCompatabilityMapping.get_old_guid(iid_tuple))
            return self.query_interface(intf_metadata=None, iid=old_iid)
        return None
    def query_interface(self, intf_metadata:dict=None, iid:GUID=None) -> "IUnknown":
        if intf_metadata is not None:
            iid_tuple = intf_metadata["iid_data"]
        else:
            iid_tuple = iid.as_data_pair()
        if iid_tuple in self._interfaces:
            return self._interfaces[iid_tuple]
        if iid is None:
            iid = GUID.from_data_pair(intf_metadata["iid_data"])
        intf = IUnknown()
        hr = IUnknown._QueryInterface(self._get_vtbl_entry(IUnknown._QIIndex))(self.p, byref(iid), byref(intf.p))
        if not Succeeded(hr):
            return self._query_backwards_compatability_interface(iid)
        intf.take_ownership(is_application=self._application)
        self._interfaces[iid_tuple] = intf
        return intf
    def take_ownership(self, is_application:bool=False):
        """Register the pointer to be Released at exit."""
        if is_application:
            self._application = True
            self._ObjectLifetimeManager.add_application(self)
        else:
            self._ObjectLifetimeManager.add_object(self)
    def add_ref(self):
        """Call AddRef on the COM interface."""
        IUnknown._AddRef(self._get_vtbl_entry(IUnknown._AddRefIndex))(self.p)
    def release(self):
        """Call Release on the COM interface."""
        self._Release(self._get_vtbl_entry(self._ReleaseIndex))(self.p)
    def final_release(self):
        """Clean up resources and nullify object."""
        if self:
            self._interfaces = {}
            if not self._skip_release:
                self.release()
            self._vtbl = None
            self._vtbl_p_value = -1
            self.p.value = 0

    def invoke(self, intf_metadata:dict, method_metadata:dict, *args):
        return self._invoke_impl(intf_metadata, method_metadata, *args)

    def get_property(self, intf_metadata:dict, method_metadata:dict):
        return self._invoke_impl(intf_metadata, method_metadata, OutArg())

    def set_property(self, intf_metadata:dict, method_metadata:dict, value):
        return self._invoke_impl(intf_metadata, method_metadata, value)

    def _invoke_impl(self, intf_metadata:dict, method_metadata:dict, *args):
        from .coclassutil import evaluate_hresult
        method_offset = method_metadata["offset"]
        vtable_index = intf_metadata["vtable_reference"] + method_offset
        arg_types = method_metadata["arg_types"]
        marshaller_classes = method_metadata["marshallers"]
        method = IFuncType(self, intf_metadata, vtable_index, *arg_types)
        marshallers = []
        for arg, marshaller_class in zip(args, marshaller_classes):
            if type(arg) is OutArg:
                marshaller = marshaller_class()
                marshallers.append(marshaller)
            else:
                marshaller = marshaller_class(arg)
                marshallers.append(marshaller)
        call_args = []
        for marshaller, arg_type in zip(marshallers, arg_types):
            if type(arg_type) == type(POINTER(PVOID)): # type(POINTER(X)) == type(POINTER(Y)) for all X,Y. the choice of PVOID was arbitrary
                call_args.append(byref(marshaller.com_val))
            else:
                call_args.append(marshaller.com_val)
        evaluate_hresult(method(*call_args))
        return_vals = []
        for arg, marshaller in zip(args, marshallers):
            if type(arg) is OutArg:
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
    _metadata = {
        "iid_data" : (132096, 5044031582654955712),
    }
    def __init__(self, pUnk: IUnknown):
        IUnknown.__init__(self, pUnk)

class IPictureDisp(IUnknown):
    def __init__(self):
        raise RuntimeError("IPictureDisp not supported.")

class IEnumVariant(object):
    guid = "{00020404-0000-0000-C000-000000000046}"
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _num_methods = 4
    _metadata = {
        "iid_data" : (132100, 5044031582654955712),
    }
    def __init__(self, pIntf):
        self._intf: IUnknown = pIntf.query_interface(IEnumVariant._metadata)
        vtable_offset_local = IEnumVariant._vtable_offset - 1
        self._Next = WINFUNCTYPE(HRESULT, LPVOID, ULONG, POINTER(Variant), POINTER(ULONG))(self._intf._get_vtbl_entry(vtable_offset_local + 1))
        self._Reset = WINFUNCTYPE(HRESULT, LPVOID)(self._intf._get_vtbl_entry(vtable_offset_local + 3))
    def next(self) -> Variant:
        from .marshall import python_val_from_VARIANT
        one_obj = ULONG(1)
        num_fetched = ULONG()
        obj = Variant()
        OLEAut32Lib.VariantInit(obj)
        if self._Next(self._intf.p, one_obj, byref(obj), byref(num_fetched)) == S_OK:
            return python_val_from_VARIANT(obj, clear_variant=True)
        else:
            return None
    def reset(self) -> None:
        self._Reset(self._intf.p)

class IFuncType(object):
    """Wrapper for calling methods into COM interface vtables."""
    def __init__(self, pUnk, iid:typing.Union[GUID, dict], method_index, *argtypes):
        self.pUnk = pUnk
        self.iid = iid
        self.index = method_index
        self.method = WINFUNCTYPE(HRESULT, LPVOID, *argtypes)
    def __call__(self, *args):
        if type(self.iid) == GUID:
            pIntf: IUnknown = self.pUnk.query_interface(iid=self.iid)
        else:
            pIntf: IUnknown = self.pUnk.query_interface(self.iid)
        ret = self.method(pIntf._get_vtbl_entry(self.index))(pIntf.p, *args)
        del(pIntf)
        return ret

def create_instance(guid:str) -> IUnknown:
    """Uses CoCreateInstance to instantiate the coclass associated with the provided guid."""
    clsid = GUID()
    pUnk = IUnknown()
    if Succeeded(OLE32Lib.CLSIDFromString(guid, clsid)):
        IID_IUnknown = GUID(IUnknown._guid)
        if Succeeded(OLE32Lib.CoCreateInstance(byref(clsid), None, CLSCTX_INPROC_SERVER, byref(IID_IUnknown), byref(pUnk.p))):
            pUnk.take_ownership()
    return pUnk