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


import typing

from enum     import IntEnum
from ctypes   import byref, cast, pointer, POINTER
from datetime import datetime, timedelta
from math     import floor, ceil

from .           import comutil     as agcom
from .           import coclassutil as agcoclass
from ..utilities import colors      as agcolor
from ..utilities import comobject   as agcomobj

###############################################################################
#   Marshalling DATE
###############################################################################
def datetime_to_DATE(d:datetime) -> agcom.DATE:
    delta = d-datetime(1899, 12, 30, 0, 0, 0)
    if delta.total_seconds() >= 0:
        return agcom.DATE(delta.total_seconds()/60/60/24)
    elif delta.total_seconds() > -1.0:
        return agcom.DATE(abs(delta.total_seconds())/60/60/24)
    else:
        days_before = ceil(abs(delta.total_seconds()/60/60/24))
        fraction_into_day = days_before - abs(delta.total_seconds()/60/60/24)
        value = -1*days_before - fraction_into_day
        return agcom.DATE(value)

def DATE_to_datetime(d:agcom.DATE) -> datetime:
    if d.value >= 0:
        delta = timedelta(days = d.value)
        return datetime(1899, 12, 30, 0, 0, 0) + delta
    else:
        days = floor(abs(d.value))
        seconds_into_day = (abs(d.value) - floor(abs(d.value)))*60*60*24
        delta_days = timedelta(days = days)
        delta_secs = timedelta(seconds = seconds_into_day)
        return (datetime(1899, 12, 30, 0, 0, 0) - delta_days) + delta_secs


###############################################################################
#   Marshalling Variant
###############################################################################
def pytype_to_vartype(item: typing.Any) -> int:
    python_type = type(item)
    if python_type==bool:
        return agcom.VT_BOOL
    elif python_type==str:
        return agcom.VT_BSTR
    elif python_type==float:
        return agcom.VT_R8
    elif python_type==int:
        if item > agcom.ULLONG_MAX:
            return agcom.VT_R8
        elif item > agcom.LLONG_MAX:
            return agcom.VT_UI8
        elif item > agcom.LONG_MAX:
            return agcom.VT_I8
        elif item > agcom.LONG_MIN:
            return agcom.VT_I4
        elif item > agcom.LLONG_MIN:
            return agcom.VT_I8
        else:
            return agcom.VT_R8
    elif python_type==list:
        if len(item)>0:
            vt = pytype_to_vartype(item[0])
            return agcom.VT_ARRAY|vt
        else:
            return agcom.VT_ARRAY|agcom.VT_NULL
    elif hasattr(item, "_intf") and type(item._intf)==agcom.IUnknown:
        return agcom.VT_UNKNOWN

def VARIANT_from_python_data(data:typing.Any) -> agcom.Variant:
    var = agcom.Variant()
    var.vt = agcom.VT_EMPTY
    if data is not None:
        if hasattr(data, "_to_argb"):
            data = data._to_argb()
        var.vt = pytype_to_vartype(data)
        union_val = agcom.varUnion()
        if var.vt == agcom.VT_BOOL:
            union_val.boolVal = agcom.VARIANT_TRUE if data else agcom.VARIANT_FALSE
        elif var.vt == agcom.VT_BSTR:
            union_val.bstrVal = agcom.BSTR(agcom.OLEAut32Lib.SysAllocString(data))
        elif var.vt == agcom.VT_I4:
            union_val.lVal = agcom.LONG(data)
        elif var.vt == agcom.VT_I8:
            union_val.llVal = agcom.LONGLONG(data)
        elif var.vt == agcom.VT_UI8:
            union_val.ullVal = agcom.ULONGLONG(data)
        elif var.vt == agcom.VT_R8:
            union_val.dblVal = agcom.DOUBLE(data)
        elif var.vt == agcom.VT_UNKNOWN:
            union_val.punkVal = data._intf.p
            agcom._CreateAgObjectLifetimeManager._add_ref_impl(data._intf)
        elif var.vt & agcom.VT_ARRAY:
            union_val.parray = SAFEARRAY_from_list(data, True)
        var.buffer = union_val.buffer
    return var

def ctype_val_from_VARIANT(var:agcom.Variant) -> typing.Any:
    union_val = agcom.varUnion()
    union_val.buffer = var.buffer
    if var.vt == agcom.VT_I8:
        return agcom.LONGLONG(union_val.llVal)
    elif var.vt == agcom.VT_I4:
        return agcom.LONG(union_val.lVal)
    elif var.vt == agcom.VT_UI1:
        return agcom.BYTE(union_val.bVal)
    elif var.vt == agcom.VT_I2:
        return agcom.SHORT(union_val.iVal)
    elif var.vt == agcom.VT_R4:
        return agcom.FLOAT(union_val.fltVal)
    elif var.vt == agcom.VT_R8:
        return agcom.DOUBLE(union_val.dblVal)
    elif var.vt == agcom.VT_BOOL:
        return agcom.VARIANT_BOOL(union_val.boolVal)
    elif var.vt == agcom.VT_BSTR:
        return agcom.BSTR(union_val.bstrVal)
    elif var.vt == agcom.VT_UNKNOWN:
        return agcom.PVOID(union_val.punkVal)
    elif var.vt & agcom.VT_ARRAY:
        if var.vt & agcom.VT_BYREF:
            return union_val.pparray
        else:
            return union_val.parray
    elif var.vt == agcom.VT_UI1|agcom.VT_BYREF:
        return union_val.pbVal
    elif var.vt == agcom.VT_I2|agcom.VT_BYREF:
        return union_val.piVal
    elif var.vt == agcom.VT_I4|agcom.VT_BYREF:
        return union_val.plVal
    elif var.vt == agcom.VT_I8|agcom.VT_BYREF:
        return union_val.pllVal
    elif var.vt == agcom.VT_R4|agcom.VT_BYREF:
        return union_val.pfltVal
    elif var.vt == agcom.VT_R8|agcom.VT_BYREF:
        return union_val.pdblVal
    elif var.vt == agcom.VT_BOOL|agcom.VT_BYREF:
        return union_val.pboolVal
    elif var.vt == agcom.VT_BSTR|agcom.VT_BYREF:
        return union_val.pbstrVal
    elif var.vt == agcom.VT_UNKNOWN|agcom.VT_BYREF:
        return union_val.ppunkVal
    elif var.vt == agcom.VT_I1:
        return agcom.CHAR(union_val.cVal)
    elif var.vt == agcom.VT_UI2:
        return agcom.USHORT(union_val.uiVal)
    elif var.vt == agcom.VT_UI4:
        return agcom.ULONG(union_val.ulVal)
    elif var.vt == agcom.VT_UI8:
        return agcom.ULONGLONG(union_val.ullVal)
    elif var.vt == agcom.VT_INT:
        return agcom.INT(union_val.intVal)
    elif var.vt == agcom.VT_UINT:
        return agcom.UINT(union_val.uintVal)
    elif var.vt == agcom.VT_I1|agcom.VT_BYREF:
        return union_val.pcVal
    elif var.vt == agcom.VT_UI2|agcom.VT_BYREF:
        return union_val.piVal
    elif var.vt == agcom.VT_UI4|agcom.VT_BYREF:
        return union_val.plVal
    elif var.vt == agcom.VT_UI8|agcom.VT_BYREF:
        return union_val.pllVal
    elif var.vt == agcom.VT_INT|agcom.VT_BYREF:
        return union_val.pintVal
    elif var.vt == agcom.VT_UINT|agcom.VT_BYREF:
        return union_val.puintVal
    elif var.vt == agcom.VT_VARIANT|agcom.VT_BYREF:
        return cast(union_val.pvarVal, POINTER(agcom.Variant))
    elif var.vt == agcom.VT_ERROR:
        return agcom.HRESULT(union_val.scode)
    elif var.vt == agcom.VT_ERROR|agcom.VT_BYREF:
        return union_val.pscode
    elif var.vt == agcom.VT_DISPATCH:
        return agcom.PVOID(union_val.pdispVal)
    elif var.vt == agcom.VT_DISPATCH|agcom.VT_BYREF:
        return union_val.ppdispVal

def vartype_is_integral_type(vt:int) -> bool:
    return vt in [agcom.VT_I1,
                  agcom.VT_I2,
                  agcom.VT_I4,
                  agcom.VT_I8,
                  agcom.VT_UI1,
                  agcom.VT_UI2,
                  agcom.VT_UI4,
                  agcom.VT_UI8,
                  agcom.VT_INT,
                  agcom.VT_UINT,
                  agcom.VT_ERROR]

def python_val_from_ctypes_val(ctypes_val:typing.Any, vt:int):
    if vt == agcom.VT_BOOL or vt == agcom.VT_BOOL|agcom.VT_BYREF:
        if vt & agcom.VT_BYREF:
            val = ctypes_val.contents.value
        else:
            val = ctypes_val.value
        return False if val == 0 else True
    elif vartype_is_integral_type(vt):
        return ctypes_val.value
    elif vartype_is_integral_type(vt ^ agcom.VT_BYREF):
        return ctypes_val.contents.value
    elif vt in [agcom.VT_R4, agcom.VT_R8]:
        return ctypes_val.value
    elif vt ^ agcom.VT_BYREF in [agcom.VT_R4, agcom.VT_R8]:
        return ctypes_val.contents.value
    elif vt == agcom.VT_BSTR or vt == agcom.VT_BSTR|agcom.VT_BYREF:
        if vt & agcom.VT_BYREF:
            val = ctypes_val.contents.value
        else:
            val = ctypes_val.value
        return val
    elif vt == agcom.VT_UNKNOWN or vt == agcom.VT_UNKNOWN|agcom.VT_BYREF \
        or vt == agcom.VT_DISPATCH or vt == agcom.VT_DISPATCH|agcom.VT_BYREF:
        if vt & agcom.VT_BYREF:
            pUnk = agcom.PVOID(ctypes_val.contents.value)
        else:
            pUnk = ctypes_val
        ret = agcom.IUnknown()
        ret.p = pUnk
        ret.create_ownership()
        return agcoclass.get_concrete_class(ret)
    elif vt & agcom.VT_ARRAY:
        if vt & agcom.VT_BYREF:
            sa = ctypes_val.contents
        else:
            sa = ctypes_val
        return list_from_SAFEARRAY(sa)
    elif vt == agcom.VT_VARIANT or vt == agcom.VT_VARIANT|agcom.VT_BYREF:
        if vt & agcom.VT_BYREF:
            return python_val_from_VARIANT(ctypes_val.contents)
        else:
            return python_val_from_VARIANT(ctypes_val)
    elif vt in [agcom.VT_EMPTY, agcom.VT_NULL]:
        return None
    raise RuntimeError("Unrecognized variant type: " + str(vt))

def python_val_from_VARIANT(var:agcom.Variant, clear_variant:bool=False) -> typing.Any:
    retval = python_val_from_ctypes_val(ctype_val_from_VARIANT(var), var.vt)
    if clear_variant:
        agcom.OLEAut32Lib.VariantClear(var)
    return retval

###############################################################################
#   Marshalling SAFEARRAY
###############################################################################
def SAFEARRAY_elem_from_python_elem(python_elem:typing.Any, as_VARIANT:bool = True) -> typing.Any:
    if as_VARIANT:
        return VARIANT_from_python_data(python_elem)
    else:
        t = type(python_elem)
        if t == str:
            # IAgCatAny expects SAFEARRAY(BSTR)
            return agcom.BSTR(agcom.SysAllocString(python_elem))
        else:
            raise RuntimeError("Unexpected Safearray element type.")

def _create_SAFEARRAY(vt:int, dim:int, num_elems_dim1:int, num_elems_dim2:int = 0) -> agcom.LPSAFEARRAY:
    rgsabound = (agcom.SafearrayBound*dim)()
    num_elems = [num_elems_dim1]
    if dim == 2:
        num_elems.append(num_elems_dim2)
    for i in range(dim):
        rgsabound[i].lLbound = agcom.LONG(0)
        rgsabound[i].cElements = agcom.ULONG(num_elems[i])
    sa = agcom.LPSAFEARRAY(agcom.OLEAut32Lib.SafeArrayCreate(vt, agcom.UINT(dim), cast(pointer(rgsabound), POINTER(agcom.SafearrayBound))))
    return sa

def SAFEARRAY_from_list(data:list, as_VARIANT:bool=True) -> agcom.LPSAFEARRAY:
    if len(data) == 0:
        return _create_SAFEARRAY(agcom.VT_VARIANT, 1, 0)
    elif type(data[0]) == list:
        #have a 2-D array; always as_VARIANT
        indices = (agcom.LONG*2)()
        indices[0] = 0
        indices[1] = 0
        pIndx = cast(pointer(indices), POINTER(agcom.LONG))
        sa = _create_SAFEARRAY(agcom.VT_VARIANT, 2, len(data), len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[0])):
                indices[0] = agcom.LONG(i)
                indices[1] = agcom.LONG(j)
                elem = SAFEARRAY_elem_from_python_elem(data[i][j])
                agcoclass.evaluate_hresult(agcom.OLEAut32Lib.SafeArrayPutElement(sa, pIndx, byref(elem)))
        return sa
    else:
        # 1-D Vector
        vt = agcom.VT_VARIANT
        if not as_VARIANT and type(data[0]) == str:
            vt = agcom.VT_BSTR
        sa = _create_SAFEARRAY(vt, 1, len(data))
        for i in range(len(data)):
            index = agcom.LONG(i)
            elem = SAFEARRAY_elem_from_python_elem(data[i], as_VARIANT)
            if vt == agcom.VT_BSTR:
                agcom.OLEAut32Lib.SafeArrayPutElement(sa, byref(index), elem)
            else:
                agcom.OLEAut32Lib.SafeArrayPutElement(sa, byref(index), byref(elem))
        return sa

def _vartype_to_ctypes_type(vt:agcom.INT) -> typing.Any:
    if vt == agcom.VT_I8:
        return agcom.LONGLONG
    elif vt == agcom.VT_I4:
        return agcom.LONG
    elif vt == agcom.VT_UI1:
        return agcom.BYTE
    elif vt == agcom.VT_I2:
        return agcom.SHORT
    elif vt == agcom.VT_R4:
        return agcom.FLOAT
    elif vt == agcom.VT_R8:
        return agcom.DOUBLE
    elif vt == agcom.VT_BOOL:
        return agcom.VARIANT_BOOL
    elif vt == agcom.VT_BSTR:
        return agcom.BSTR
    elif vt == agcom.VT_UNKNOWN:
        return agcom.PVOID
    elif vt & agcom.VT_ARRAY:
        return agcom.PVOID
    elif vt == agcom.VT_UI1|agcom.VT_BYREF:
        return POINTER(agcom.BYTE)
    elif vt == agcom.VT_I2|agcom.VT_BYREF:
        return POINTER(agcom.SHORT)
    elif vt == agcom.VT_I4|agcom.VT_BYREF:
        return POINTER(agcom.LONG)
    elif vt == agcom.VT_I8|agcom.VT_BYREF:
        return POINTER(agcom.LONGLONG)
    elif vt == agcom.VT_R4|agcom.VT_BYREF:
        return POINTER(agcom.FLOAT)
    elif vt == agcom.VT_R8|agcom.VT_BYREF:
        return POINTER(agcom.DOUBLE)
    elif vt == agcom.VT_BOOL|agcom.VT_BYREF:
        return POINTER(agcom.VARIANT_BOOL)
    elif vt == agcom.VT_BSTR|agcom.VT_BYREF:
        return POINTER(agcom.BSTR)
    elif vt == agcom.VT_UNKNOWN|agcom.VT_BYREF:
        return POINTER(agcom.PVOID)
    elif vt == agcom.VT_I1:
        return agcom.CHAR
    elif vt == agcom.VT_UI2:
        return agcom.USHORT
    elif vt == agcom.VT_UI4:
        return agcom.ULONG
    elif vt == agcom.VT_UI8:
        return agcom.ULONGLONG
    elif vt == agcom.VT_INT:
        return agcom.INT
    elif vt == agcom.VT_UINT:
        return agcom.UINT
    elif vt == agcom.VT_I1|agcom.VT_BYREF:
        return POINTER(agcom.CHAR)
    elif vt == agcom.VT_UI2|agcom.VT_BYREF:
        return POINTER(agcom.USHORT)
    elif vt == agcom.VT_UI4|agcom.VT_BYREF:
        return POINTER(agcom.ULONG)
    elif vt == agcom.VT_UI8|agcom.VT_BYREF:
        return POINTER(agcom.ULONGLONG)
    elif vt == agcom.VT_INT|agcom.VT_BYREF:
        return POINTER(agcom.INT)
    elif vt == agcom.VT_UINT|agcom.VT_BYREF:
        return POINTER(agcom.UINT)
    elif vt == agcom.VT_VARIANT:
        return agcom.Variant
    elif vt == agcom.VT_VARIANT|agcom.VT_BYREF:
        return POINTER(agcom.Variant)
    elif vt == agcom.VT_ERROR:
        return agcom.HRESULT
    elif vt == agcom.VT_ERROR|agcom.VT_BYREF:
        return POINTER(agcom.HRESULT)
    elif vt == agcom.VT_DISPATCH:
        return agcom.PVOID
    elif vt == agcom.VT_DISPATCH|agcom.VT_BYREF:
        return POINTER(agcom.PVOID)
    else:
        raise RuntimeError("Unrecognized variant type: " + str(vt))

def _is_uniform_type(p_array:POINTER(agcom.Variant), num_elems:int) -> bool:
    first_elem_type = p_array[0].vt
    for i in range(num_elems):
        if p_array[i].vt != first_elem_type:
            return False
    return True

def _fast_1d_numeric_array(p_variant_array:agcom.LPVOID, num_elems:int, data_type) -> list:
    if data_type == agcom.FLOAT:
        # Index is 2 - the third FLOAT value in Union(FLOAT*6, Variant)
        data_union_type = data_type * 6
        data_union_index = 2
    elif data_type == agcom.DOUBLE:
        # Index is 1 - the second DOUBLE value in Union(DOUBLE*3, Variant)
        data_union_type = data_type * 3
        data_union_index = 1
    src_array_type = data_union_type * num_elems
    p_source_array = cast(p_variant_array, POINTER(src_array_type))
    source_array = p_source_array[0]
    dest_array_type = data_type * num_elems
    dest_array = dest_array_type()
    for i in range(num_elems):
        dest_array[i] = source_array[i][data_union_index]
    return list(dest_array)

def _single_dimension_list_from_SAFEARRAY(sa:agcom.LPSAFEARRAY, index:int, from_2d_array=False) -> list:
    python_array = list()
    vt = agcom.VARTYPE()
    agcom.OLEAut32Lib.SafeArrayGetVartype(sa, byref(vt))
    lb1 = agcom.LONG()
    ub1 = agcom.LONG()
    agcom.OLEAut32Lib.SafeArrayGetLBound(sa, agcom.UINT(1), byref(lb1))
    agcom.OLEAut32Lib.SafeArrayGetUBound(sa, agcom.UINT(1), byref(ub1))
    num_elems_dim1 = int(ub1.value) + 1 - int(lb1.value)
    if num_elems_dim1 == 0:
        return []
    pVoid = agcom.LPVOID()
    hr = agcom.OLEAut32Lib.SafeArrayAccessData(sa, byref(pVoid))
    pElem = cast(pVoid, POINTER(_vartype_to_ctypes_type(vt.value)))
    if not from_2d_array:
        if vt.value == agcom.VT_VARIANT and _vartype_to_ctypes_type(pElem[0].vt) in [agcom.FLOAT, agcom.DOUBLE] and _is_uniform_type(pElem, num_elems_dim1) and lb1.value == 0:
                python_array = _fast_1d_numeric_array(pVoid, num_elems_dim1, _vartype_to_ctypes_type(pElem[0].vt))
        else:
            for i in range(int(lb1.value), int(lb1.value) + num_elems_dim1):
                python_array.append(python_val_from_ctypes_val(pElem[i], vt.value))
    else:
        lb2 = agcom.LONG()
        ub2 = agcom.LONG()
        agcom.OLEAut32Lib.SafeArrayGetLBound(sa, agcom.UINT(2), byref(lb2))
        agcom.OLEAut32Lib.SafeArrayGetUBound(sa, agcom.UINT(2), byref(ub2))
        num_elems_dim2 = int(ub2.value) + 1 - int(lb2.value)
        for i in range(int(lb2.value), int(lb2.value) + num_elems_dim2):
            python_array.append(python_val_from_ctypes_val(pElem[(i * (num_elems_dim1)) + index], vt.value))
    hr = agcom.OLEAut32Lib.SafeArrayUnaccessData(sa)
    return python_array

def list_from_SAFEARRAY(sa:agcom.LPSAFEARRAY) -> list:
    dim = agcom.OLEAut32Lib.SafeArrayGetDim(sa)
    if dim == 0:
        return list()
    elif dim == 1:
        return _single_dimension_list_from_SAFEARRAY(sa, 0)
    elif dim == 2:
        lb = agcom.LONG()
        ub = agcom.LONG()
        agcom.OLEAut32Lib.SafeArrayGetLBound(sa, agcom.UINT(1), byref(lb))
        agcom.OLEAut32Lib.SafeArrayGetUBound(sa, agcom.UINT(1), byref(ub))
        ret = []
        for i in range(int(lb.value), int(ub.value)+1):
            ret.append(_single_dimension_list_from_SAFEARRAY(sa, i, True))
        return ret
    else:
        raise RuntimeError("Unexpected dimension of SafeArray.  Expected 1 or 2, got " + str(dim) + ".")


###############################################################################
#   Classes for marshalling arguments to COM interfaces
###############################################################################
class LongArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.LONG = agcom.LONG()
        else:
            self.LONG = agcom.LONG(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.LONG:
        return self.LONG
    @property
    def python_val(self) -> int:
        return self.LONG.value

class ULongArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.ULONG = agcom.ULONG()
        else:
            self.ULONG = agcom.ULONG(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.ULONG:
        return self.ULONG
    @property
    def python_val(self) -> int:
        return self.ULONG.value

class LongLongArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.LONGLONG = agcom.LONGLONG()
        else:
            self.LONGLONG = agcom.LONGLONG(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.LONGLONG:
        return self.LONGLONG
    @property
    def python_val(self) -> int:
        return self.LONGLONG.value

class ULongLongArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.ULONGLONG = agcom.ULONGLONG()
        else:
            self.ULONGLONG = agcom.ULONGLONG(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.ULONGLONG:
        return self.ULONGLONG
    @property
    def python_val(self) -> int:
        return self.ULONGLONG.value

class IntArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.INT = agcom.INT()
        else:
            self.INT = agcom.INT(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.INT:
        return self.INT
    @property
    def python_val(self) -> int:
        return self.INT.value

class UIntArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.UINT = agcom.UINT()
        else:
            self.UINT = agcom.UINT(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.UINT:
        return self.UINT
    @property
    def python_val(self) -> int:
        return self.UINT.value

class ShortArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.SHORT = agcom.SHORT()
        else:
            self.SHORT = agcom.SHORT(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.SHORT:
        return self.SHORT
    @property
    def python_val(self) -> int:
        return self.SHORT.value

class UShortArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.USHORT = agcom.USHORT()
        else:
            self.USHORT = agcom.USHORT(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.USHORT:
        return self.USHORT
    @property
    def python_val(self) -> int:
        return self.USHORT.value

class HResultArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.HRESULT = agcom.HRESULT()
        else:
            self.HRESULT = agcom.HRESULT(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.HRESULT:
        return self.HRESULT
    @property
    def python_val(self) -> int:
        return self.HRESULT.value

class OLEColorArg(object):
    def __init__(self, val: agcolor.Color = None):
        if val is None:
            self.OLE_COLOR = agcom.OLE_COLOR()
        else:
            if type(val) == agcolor.ColorRGBA:
                raise RuntimeError("Argument type is RGB only, use Color class instead of ColorRGBA.")
            self.OLE_COLOR = agcom.OLE_COLOR(val._to_ole_color())
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.OLE_COLOR:
        return self.OLE_COLOR
    @property
    def python_val(self) -> agcolor.Color:
        c = agcolor.Color()
        c._from_ole_color(self.OLE_COLOR.value)
        return c

class VariantBoolArg(object):
    def __init__(self, val: bool = None):
        if val is None:
            self.vb = agcom.VARIANT_BOOL()
        else:
            self.vb = agcom.VARIANT_TRUE if val else agcom.VARIANT_FALSE
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.VARIANT_BOOL:
        return self.vb
    @property
    def python_val(self) -> bool:
        return False if self.vb.value == agcom.VARIANT_FALSE.value else True

class DoubleArg(object):
    def __init__(self, val: float = None):
        if val is None:
            self.DOUBLE = agcom.DOUBLE()
        else:
            self.DOUBLE = agcom.DOUBLE(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.DOUBLE:
        return self.DOUBLE
    @property
    def python_val(self) -> float:
        return self.DOUBLE.value

class FloatArg(object):
    def __init__(self, val: float = None):
        if val is None:
            self.FLOAT = agcom.FLOAT()
        else:
            self.FLOAT = agcom.FLOAT(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.FLOAT:
        return self.FLOAT
    @property
    def python_val(self) -> float:
        return self.FLOAT.value

class BStrArg(object):
    def __init__(self, val: str = None):
        if val is None:
            self.bstr = agcom.BSTR()
        else:
            self.bstr = agcom.BSTR(agcom.OLEAut32Lib.SysAllocString(val))
    def _cleanup(self):
        agcom.OLEAut32Lib.SysFreeString(self.bstr)
    def __del__(self):
        self._cleanup()
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self._cleanup()
        return False
    @property
    def com_val(self) -> agcom.BSTR:
        return self.bstr
    @property
    def python_val(self) -> str:
        if self.bstr.value is not None:
            return str(self.bstr.value)

class ByteArg(object):
    def __init__(self, val: typing.Any = None):
        if val is None:
            self.BYTE = agcom.BYTE()
        else:
            if type(val) == int:
                self.BYTE = agcom.BYTE(val)
            elif type(val) == str:
                self.BYTE = agcom.BYTE(ord(val[0]))
            elif type(val) == bytes:
                self.BYTE = agcom.BYTE(ord(val[0]))
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.BYTE:
        return self.BYTE
    @property
    def python_val(self) -> bytes:
        return bytes(chr(self.BYTE.value), "ascii")

class CharArg(object):
    def __init__(self, val: typing.Any = None):
        if val is None:
            self.CHAR = agcom.CHAR()
        else:
            if type(val) == int:
                self.CHAR = agcom.CHAR(val)
            elif type(val) == str:
                self.CHAR = agcom.CHAR(ord(val[0]))
            elif type(val) == bytes:
                self.CHAR = agcom.CHAR(ord(val[0]))
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.CHAR:
        return self.CHAR
    @property
    def python_val(self) -> bytes:
        return bytes(chr(self.CHAR.value), "ascii")

class VariantArg(object):
    def __init__(self, val: typing.Any = None):
        if val is not None and type(val)==agcom.Variant:
            self.var = agcom.Variant()
            agcom.OLEAut32Lib.VariantCopy(byref(self.var), byref(val))
        else:
            self.var = VARIANT_from_python_data(val)
    def _cleanup(self):
        agcom.OLEAut32Lib.VariantClear(self.var)
    def __del__(self):
        self._cleanup()
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self._cleanup()
        return False
    @property
    def com_val(self) -> agcom.Variant:
        return self.var
    @property
    def python_val(self) -> typing.Any:
        return python_val_from_VARIANT(self.var)

class InterfaceInArg(object):
    def __init__(self, as_interface):
        self.pIntf = None
        self.as_interface = as_interface
    def __call__(self, val):
        """
        Initialize an InterfaceInArg object.

        val should be a python CoClass object (e.g. Facility)
        as_interface is the argument interface class
        """
        new_inst = InterfaceInArg(self.as_interface)
        new_inst.pIntf = None
        if type(val) == agcomobj.COMObject:
            new_inst.val = val
            new_inst.rawptr = val.get_pointer()
        elif val is not None and hasattr(val, "_intf"):
            new_inst.val = val
            if new_inst.as_interface=="IDispatch":
                new_inst.pIntf = val._intf.query_interface(agcom.GUID(agcom.IDispatch._guid))
            elif new_inst.as_interface=="IUnknown":
                new_inst.pIntf = val._intf.query_interface(agcom.GUID(agcom.IUnknown._guid))
            else:
                intf_class = agcoclass.AgTypeNameMap[new_inst.as_interface]
                new_inst.pIntf = val._intf.query_interface(intf_class._metadata)
            new_inst.rawptr = new_inst.pIntf.p
        else:
            new_inst.val = None
            new_inst.pIntf = agcom.IUnknown()
            new_inst.rawptr = new_inst.pIntf.p
        return new_inst
    def _cleanup(self):
        if self.pIntf is not None:
            del(self.pIntf)
    def __del__(self):
        self._cleanup()
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self._cleanup()
        return False
    @property
    def com_val(self) -> agcom.PVOID:
        if hasattr(self.rawptr, "value"):
            return agcom.PVOID(self.rawptr.value)
        else:
            return agcom.PVOID(int(self.rawptr))
    @property
    def python_val(self) -> typing.Any:
        return self.val

class InterfaceOutArg(object):
    def __init__(self):
        self.ptr = agcom.IUnknown()
    def _cleanup(self):
        del(self.ptr)
    def __del__(self):
        self._cleanup()
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self._cleanup()
        return False
    @property
    def com_val(self) -> agcom.PVOID:
        return self.ptr.p
    @property
    def python_val(self) -> typing.Any:
        if self.ptr:
            self.ptr.take_ownership()
            return agcoclass.get_concrete_class(self.ptr)
        else:
            return None

class PVoidArg(object):
    def __init__(self, val: agcom.PVOID = None):
        if val is None:
            self.p = agcom.PVOID()
        else:
            self.p = val
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.PVOID:
        return self.p
    @property
    def python_val(self) -> agcom.PVOID:
        return self.p

class InterfaceEventCallbackArg(object):
    def __init__(self, pUnk:agcom.PVOID, as_interface):
        """
        Initialize an InterfaceEventCallbackArg object.

        pUnk should be a IUnknown pointer as PVOID
        as_interface is the interface class to send to STK
        """
        ptr = agcom.IUnknown()
        ptr.p = agcom.PVOID(pUnk) if type(pUnk)==int else pUnk
        self.intf = as_interface()
        self.intf._private_init(ptr)
        del(ptr)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        del(self.intf)
        return False
    @property
    def com_val(self) -> agcom.PVOID:
        return self.intf.__dict__["_intf"].p
    @property
    def python_val(self) -> typing.Any:
        return self.intf

class IEnumVariantArg(object):
    def __init__(self):
        self.ptr = agcom.IUnknown()
    def _cleanup(self):
        del(self.ptr)
    def __del__(self):
        self._cleanup()
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self._cleanup()
        return False
    @property
    def com_val(self) -> agcom.PVOID:
        return self.ptr.p
    @property
    def python_val(self) -> agcom.IEnumVariant:
        if self.ptr:
            self.ptr.take_ownership()
            return agcom.IEnumVariant(self.ptr)
        else:
            return None

class EnumArg(object):
    def __init__(self, enum_type: typing.Type[IntEnum]):
        self.enum_type = enum_type
    def __call__(self, val: typing.Any = None):
        if val is None:
            self.val = agcom.LONG()
        elif type(val) == agcom.LONG:
            self.val = val
        else:
            self.val = agcom.LONG(val)
        return self
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.LONG:
        return self.val
    @property
    def python_val(self) -> IntEnum:
        return self.enum_type(self.val.value)

class LPSafearrayArg(object):
    def __init__(self, val: list = None):
        if val is None:
            self.sa = agcom.LPSAFEARRAY()
        else:
            self.sa = SAFEARRAY_from_list(val, True)
    def _cleanup(self):
        agcom.OLEAut32Lib.SafeArrayDestroy(self.sa)
    def __del__(self):
        self._cleanup()
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self._cleanup()
        return False
    @property
    def com_val(self) -> agcom.LPSAFEARRAY:
        return self.sa
    @property
    def python_val(self) -> list:
        return list_from_SAFEARRAY(self.sa)

class IPictureDispArg(object):
    def __init__(self, val: agcom.IPictureDisp = None):
        raise SyntaxError(f"Methods with the argument type \"IPictureDisp\" are not available using Python")
        if val is None:
            self.ipd = agcom.IPictureDisp()
        else:
            self.ipd = val
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.PVOID:
        return agcom.PVOID()
    @property
    def python_val(self) -> agcom.IPictureDisp:
        return self.ipd

class DateArg(object):
    def __init__(self, val: datetime = None):
        if val is None:
            self.date = agcom.DATE()
        else:
            self.date = datetime_to_DATE(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.DATE:
        return self.date
    @property
    def python_val(self) -> datetime:
        return DATE_to_datetime(self.date)

class OLEHandleArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.OLE_HANDLE = agcom.OLE_HANDLE()
        else:
            self.OLE_HANDLE = agcom.OLE_HANDLE(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.OLE_HANDLE:
        return self.OLE_HANDLE
    @property
    def python_val(self) -> int:
        return self.OLE_HANDLE.value

class OLEXPosPixelsArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.OLE_XPOS_PIXELS = agcom.OLE_XPOS_PIXELS()
        else:
            self.OLE_XPOS_PIXELS = agcom.OLE_XPOS_PIXELS(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.OLE_XPOS_PIXELS:
        return self.OLE_XPOS_PIXELS
    @property
    def python_val(self) -> int:
        return self.OLE_XPOS_PIXELS.value

class OLEYPosPixelsArg(object):
    def __init__(self, val: int = None):
        if val is None:
            self.OLE_YPOS_PIXELS = agcom.OLE_YPOS_PIXELS()
        else:
            self.OLE_YPOS_PIXELS = agcom.OLE_YPOS_PIXELS(val)
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        return False
    @property
    def com_val(self) -> agcom.OLE_YPOS_PIXELS:
        return self.OLE_YPOS_PIXELS
    @property
    def python_val(self) -> int:
        return self.OLE_YPOS_PIXELS.value
