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

"""Object Model components specifically designed to support STK RF Channel Modeler."""

__all__ = ["Analysis", "AnalysisConfiguration", "AnalysisConfigurationCollection", "AnalysisConfigurationComputeStepMode",
"AnalysisConfigurationModelType", "AnalysisLink", "AnalysisLinkCollection", "AnalysisResultsFileMode",
"AnalysisSolverBoundingBoxMode", "ChannelResponseType", "CommunicationsAnalysisConfigurationModel",
"CommunicationsTransceiverConfiguration", "CommunicationsTransceiverConfigurationCollection",
"CommunicationsTransceiverModel", "CommunicationsWaveform", "ComputeOptions", "ElementExportPatternAntenna", "Extent",
"FacetTileset", "FacetTilesetCollection", "FarFieldDataPatternAntenna", "FrequencyPulseResponse", "GpuProperties",
"IAnalysisConfigurationModel", "IAnalysisLink", "IAntenna", "IProgressTrackCancel", "IRadarAnalysisConfigurationModel",
"IResponse", "ISceneContributorCollection", "ITransceiverModel", "ImageWindowType", "Material", "ParametricBeamAntenna",
"PolarizationType", "RadarISarAnalysisConfigurationModel", "RadarISarAnalysisLink", "RadarImagingDataProduct",
"RadarImagingDataProductCollection", "RadarSarAnalysisConfigurationModel", "RadarSarAnalysisLink",
"RadarSarImageLocation", "RadarSarImageLocationCollection", "RadarTargetCollection", "RadarTransceiverConfiguration",
"RadarTransceiverConfigurationCollection", "RadarTransceiverModel", "RadarWaveform", "RangeDopplerResponse",
"STKRFChannelModeler", "SceneContributor", "SceneContributorCollection", "Transceiver", "TransceiverCollection",
"TransceiverMode", "TransceiverModelType", "ValidationResponse"]


from ctypes import POINTER
from enum import IntEnum

from ..internal import coclassutil as agcls, comutil as agcom, marshall as agmarshall
from ..internal.apiutil import (
    EnumeratorProxy,
    InterfaceProxy,
    OutArg,
    SupportsDeleteCallback,
    get_interface_property,
    initialize_from_source_object,
    set_class_attribute,
    set_interface_attribute,
)
from ..internal.comutil import IDispatch, IUnknown


class ChannelResponseType(IntEnum):
    """Channel Response Type"""

    FREQUENCY_PULSE = 0
    """Frequency-Pulse"""
    RANGE_DOPPLER = 1
    """Range-Doppler"""

ChannelResponseType.FREQUENCY_PULSE.__doc__ = "Frequency-Pulse"
ChannelResponseType.RANGE_DOPPLER.__doc__ = "Range-Doppler"

agcls.AgTypeNameMap["ChannelResponseType"] = ChannelResponseType

class AnalysisConfigurationModelType(IntEnum):
    """Analysis Configuration Model Type"""

    COMMUNICATIONS = 0
    """Communications"""
    RADAR_I_SAR = 1
    """Radar ISAR"""
    RADAR_SAR = 2
    """Radar SAR"""

AnalysisConfigurationModelType.COMMUNICATIONS.__doc__ = "Communications"
AnalysisConfigurationModelType.RADAR_I_SAR.__doc__ = "Radar ISAR"
AnalysisConfigurationModelType.RADAR_SAR.__doc__ = "Radar SAR"

agcls.AgTypeNameMap["AnalysisConfigurationModelType"] = AnalysisConfigurationModelType

class TransceiverMode(IntEnum):
    """Transceiver Mode"""

    TRANSCEIVE = 0
    """Transceive"""
    TRANSMIT_ONLY = 1
    """Transmit Only"""
    RECEIVE_ONLY = 2
    """Receive Only"""

TransceiverMode.TRANSCEIVE.__doc__ = "Transceive"
TransceiverMode.TRANSMIT_ONLY.__doc__ = "Transmit Only"
TransceiverMode.RECEIVE_ONLY.__doc__ = "Receive Only"

agcls.AgTypeNameMap["TransceiverMode"] = TransceiverMode

class AnalysisConfigurationComputeStepMode(IntEnum):
    """Analysis configuration compute step mode."""

    FIXED_STEP_SIZE = 0
    """Fixed Step size"""
    FIXED_STEP_COUNT = 1
    """Fixed Step count"""
    CONTINUOUS_CHANNEL_SOUNDINGS = 2
    """Continuous channel soundings"""

AnalysisConfigurationComputeStepMode.FIXED_STEP_SIZE.__doc__ = "Fixed Step size"
AnalysisConfigurationComputeStepMode.FIXED_STEP_COUNT.__doc__ = "Fixed Step count"
AnalysisConfigurationComputeStepMode.CONTINUOUS_CHANNEL_SOUNDINGS.__doc__ = "Continuous channel soundings"

agcls.AgTypeNameMap["AnalysisConfigurationComputeStepMode"] = AnalysisConfigurationComputeStepMode

class AnalysisResultsFileMode(IntEnum):
    """Analysis results file mode."""

    SINGLE_FILE = 0
    """Single file"""
    ONE_FILE_PER_LINK = 1
    """One file per link"""

AnalysisResultsFileMode.SINGLE_FILE.__doc__ = "Single file"
AnalysisResultsFileMode.ONE_FILE_PER_LINK.__doc__ = "One file per link"

agcls.AgTypeNameMap["AnalysisResultsFileMode"] = AnalysisResultsFileMode

class AnalysisSolverBoundingBoxMode(IntEnum):
    """Analysis solver bounding box mode."""

    DEFAULT = 0
    """Default"""
    FULL_SCENE = 1
    """Full Scene"""
    CUSTOM = 2
    """Custom"""

AnalysisSolverBoundingBoxMode.DEFAULT.__doc__ = "Default"
AnalysisSolverBoundingBoxMode.FULL_SCENE.__doc__ = "Full Scene"
AnalysisSolverBoundingBoxMode.CUSTOM.__doc__ = "Custom"

agcls.AgTypeNameMap["AnalysisSolverBoundingBoxMode"] = AnalysisSolverBoundingBoxMode

class TransceiverModelType(IntEnum):
    """Transceiver Model Type"""

    COMMUNICATIONS = 0
    """Communications"""
    RADAR = 1
    """Radar"""

TransceiverModelType.COMMUNICATIONS.__doc__ = "Communications"
TransceiverModelType.RADAR.__doc__ = "Radar"

agcls.AgTypeNameMap["TransceiverModelType"] = TransceiverModelType

class PolarizationType(IntEnum):
    """Polarization Type"""

    VERTICAL = 0
    """Vertical"""
    HORIZONTAL = 1
    """Horizontal"""
    RIGHT_HAND_CIRCULAR_POLARIZATION = 2
    """RHCP"""
    LEFT_HAND_CIRCULAR_POLARIZATION = 3
    """LHCP"""

PolarizationType.VERTICAL.__doc__ = "Vertical"
PolarizationType.HORIZONTAL.__doc__ = "Horizontal"
PolarizationType.RIGHT_HAND_CIRCULAR_POLARIZATION.__doc__ = "RHCP"
PolarizationType.LEFT_HAND_CIRCULAR_POLARIZATION.__doc__ = "LHCP"

agcls.AgTypeNameMap["PolarizationType"] = PolarizationType

class ImageWindowType(IntEnum):
    """Polarization Type"""

    FLAT = 0
    """Flat"""
    HANN = 1
    """Hann"""
    HAMMING = 2
    """Hamming"""
    TAYLOR = 3
    """Taylor"""

ImageWindowType.FLAT.__doc__ = "Flat"
ImageWindowType.HANN.__doc__ = "Hann"
ImageWindowType.HAMMING.__doc__ = "Hamming"
ImageWindowType.TAYLOR.__doc__ = "Taylor"

agcls.AgTypeNameMap["ImageWindowType"] = ImageWindowType


class IProgressTrackCancel(object):
    """Control for progress tracker."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_cancel_requested_method_offset = 1
    _update_progress_method_offset = 2
    _metadata = {
        "iid_data" : (5189323083975178084, 12155257170465652875),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IProgressTrackCancel."""
        initialize_from_source_object(self, source_object, IProgressTrackCancel)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IProgressTrackCancel)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IProgressTrackCancel, None)

    _get_cancel_requested_metadata = { "offset" : _get_cancel_requested_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def cancel_requested(self) -> bool:
        """Get whether or not cancel was requested."""
        return self._intf.get_property(IProgressTrackCancel._metadata, IProgressTrackCancel._get_cancel_requested_metadata)

    _update_progress_metadata = { "offset" : _update_progress_method_offset,
            "arg_types" : (agcom.INT, agcom.BSTR,),
            "marshallers" : (agmarshall.IntArg, agmarshall.BStrArg,) }
    def update_progress(self, progress:int, message:str) -> None:
        """Update progress."""
        return self._intf.invoke(IProgressTrackCancel._metadata, IProgressTrackCancel._update_progress_metadata, progress, message)

    _property_names[cancel_requested] = "cancel_requested"


agcls.AgClassCatalog.add_catalog_entry((5189323083975178084, 12155257170465652875), IProgressTrackCancel)
agcls.AgTypeNameMap["IProgressTrackCancel"] = IProgressTrackCancel

class IAntenna(object):
    """Base interface for a transceiver antenna model."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _metadata = {
        "iid_data" : (5148557275996632377, 8767940624566663358),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IAntenna."""
        initialize_from_source_object(self, source_object, IAntenna)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IAntenna)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IAntenna, None)

    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def type(self) -> str:
        """Get the antenna type."""
        return self._intf.get_property(IAntenna._metadata, IAntenna._get_type_metadata)

    _property_names[type] = "type"


agcls.AgClassCatalog.add_catalog_entry((5148557275996632377, 8767940624566663358), IAntenna)
agcls.AgTypeNameMap["IAntenna"] = IAntenna

class ITransceiverModel(object):
    """Base interface which defines common properties for a transceiver model."""

    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _set_antenna_type_method_offset = 2
    _get_supported_antenna_types_method_offset = 3
    _get_antenna_method_offset = 4
    _metadata = {
        "iid_data" : (5130641926513793015, 9641467165878334596),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type ITransceiverModel."""
        initialize_from_source_object(self, source_object, ITransceiverModel)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, ITransceiverModel)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, ITransceiverModel, None)

    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(TransceiverModelType),) }
    @property
    def type(self) -> "TransceiverModelType":
        """Get the transceiver unique identifier."""
        return self._intf.get_property(ITransceiverModel._metadata, ITransceiverModel._get_type_metadata)

    _set_antenna_type_metadata = { "offset" : _set_antenna_type_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def set_antenna_type(self, antenna_type:str) -> None:
        """Set the transceiver's antenna type."""
        return self._intf.invoke(ITransceiverModel._metadata, ITransceiverModel._set_antenna_type_metadata, antenna_type)

    _get_supported_antenna_types_metadata = { "offset" : _get_supported_antenna_types_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_antenna_types(self) -> list:
        """Get the supported antenna types."""
        return self._intf.get_property(ITransceiverModel._metadata, ITransceiverModel._get_supported_antenna_types_metadata)

    _get_antenna_metadata = { "offset" : _get_antenna_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def antenna(self) -> "IAntenna":
        """Get the transceiver's antenna settings."""
        return self._intf.get_property(ITransceiverModel._metadata, ITransceiverModel._get_antenna_metadata)

    _property_names[type] = "type"
    _property_names[supported_antenna_types] = "supported_antenna_types"
    _property_names[antenna] = "antenna"


agcls.AgClassCatalog.add_catalog_entry((5130641926513793015, 9641467165878334596), ITransceiverModel)
agcls.AgTypeNameMap["ITransceiverModel"] = ITransceiverModel

class ISceneContributorCollection(object):
    """Represents a collection of scene contributors."""

    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _remove_at_method_offset = 4
    _remove_method_offset = 5
    _add_new_method_offset = 6
    _remove_all_method_offset = 7
    _contains_method_offset = 8
    _metadata = {
        "iid_data" : (4655659453865151327, 5356126618700587164),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type ISceneContributorCollection."""
        initialize_from_source_object(self, source_object, ISceneContributorCollection)
        self.__dict__["_enumerator"] = None
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, ISceneContributorCollection)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, ISceneContributorCollection, None)
    def __iter__(self):
        """Create an iterator for the ISceneContributorCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "SceneContributor":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(ISceneContributorCollection._metadata, ISceneContributorCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "SceneContributor":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(ISceneContributorCollection._metadata, ISceneContributorCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(ISceneContributorCollection._metadata, ISceneContributorCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the scene contributor with the supplied index."""
        return self._intf.invoke(ISceneContributorCollection._metadata, ISceneContributorCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def remove(self, stk_object_path:str) -> None:
        """Remove the supplied scene contributor from the collection."""
        return self._intf.invoke(ISceneContributorCollection._metadata, ISceneContributorCollection._remove_metadata, stk_object_path)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def add_new(self, stk_object_path:str) -> "SceneContributor":
        """Add and returns a new scene contributor."""
        return self._intf.invoke(ISceneContributorCollection._metadata, ISceneContributorCollection._add_new_metadata, stk_object_path, OutArg())

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all scene contributors from the collection."""
        return self._intf.invoke(ISceneContributorCollection._metadata, ISceneContributorCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def contains(self, stk_object_path:str) -> bool:
        """Check to see if a given scene contributor exists in the collection."""
        return self._intf.invoke(ISceneContributorCollection._metadata, ISceneContributorCollection._contains_metadata, stk_object_path, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"


agcls.AgClassCatalog.add_catalog_entry((4655659453865151327, 5356126618700587164), ISceneContributorCollection)
agcls.AgTypeNameMap["ISceneContributorCollection"] = ISceneContributorCollection

class IResponse(object):
    """Properties and data for a channel characaterization response."""

    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _get_data_method_offset = 2
    _get_transmit_antenna_count_method_offset = 3
    _get_receive_antenna_count_method_offset = 4
    _metadata = {
        "iid_data" : (5122426286237758455, 16157611143711992501),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IResponse."""
        initialize_from_source_object(self, source_object, IResponse)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IResponse)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IResponse, None)

    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ChannelResponseType),) }
    @property
    def type(self) -> "ChannelResponseType":
        """Get the response type."""
        return self._intf.get_property(IResponse._metadata, IResponse._get_type_metadata)

    _get_data_metadata = { "offset" : _get_data_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def data(self) -> list:
        """Get the response data in a single dimension. Reshape to a multi-dimensional array using the DataDimensions property from the derived response class."""
        return self._intf.get_property(IResponse._metadata, IResponse._get_data_metadata)

    _get_transmit_antenna_count_metadata = { "offset" : _get_transmit_antenna_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def transmit_antenna_count(self) -> int:
        """Get the transmit antenna count."""
        return self._intf.get_property(IResponse._metadata, IResponse._get_transmit_antenna_count_metadata)

    _get_receive_antenna_count_metadata = { "offset" : _get_receive_antenna_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def receive_antenna_count(self) -> int:
        """Get the receive antenna count."""
        return self._intf.get_property(IResponse._metadata, IResponse._get_receive_antenna_count_metadata)

    _property_names[type] = "type"
    _property_names[data] = "data"
    _property_names[transmit_antenna_count] = "transmit_antenna_count"
    _property_names[receive_antenna_count] = "receive_antenna_count"


agcls.AgClassCatalog.add_catalog_entry((5122426286237758455, 16157611143711992501), IResponse)
agcls.AgTypeNameMap["IResponse"] = IResponse

class IAnalysisLink(object):
    """Properties for a transceiver link for an analysis."""

    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_name_method_offset = 1
    _get_transmit_transceiver_identifier_method_offset = 2
    _get_transmit_transceiver_name_method_offset = 3
    _get_receive_transceiver_identifier_method_offset = 4
    _get_receive_transceiver_name_method_offset = 5
    _get_transmit_antenna_count_method_offset = 6
    _get_receive_antenna_count_method_offset = 7
    _get_analysis_intervals_method_offset = 8
    _compute_method_offset = 9
    _metadata = {
        "iid_data" : (5004542476303939694, 2475971475159732381),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IAnalysisLink."""
        initialize_from_source_object(self, source_object, IAnalysisLink)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IAnalysisLink)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IAnalysisLink, None)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the analysis link name."""
        return self._intf.get_property(IAnalysisLink._metadata, IAnalysisLink._get_name_metadata)

    _get_transmit_transceiver_identifier_metadata = { "offset" : _get_transmit_transceiver_identifier_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def transmit_transceiver_identifier(self) -> str:
        """Get the transmit transceiver identifier."""
        return self._intf.get_property(IAnalysisLink._metadata, IAnalysisLink._get_transmit_transceiver_identifier_metadata)

    _get_transmit_transceiver_name_metadata = { "offset" : _get_transmit_transceiver_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def transmit_transceiver_name(self) -> str:
        """Get the transmit transceiver name."""
        return self._intf.get_property(IAnalysisLink._metadata, IAnalysisLink._get_transmit_transceiver_name_metadata)

    _get_receive_transceiver_identifier_metadata = { "offset" : _get_receive_transceiver_identifier_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def receive_transceiver_identifier(self) -> str:
        """Get the receive transceiver identifier."""
        return self._intf.get_property(IAnalysisLink._metadata, IAnalysisLink._get_receive_transceiver_identifier_metadata)

    _get_receive_transceiver_name_metadata = { "offset" : _get_receive_transceiver_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def receive_transceiver_name(self) -> str:
        """Get the receive transceiver name."""
        return self._intf.get_property(IAnalysisLink._metadata, IAnalysisLink._get_receive_transceiver_name_metadata)

    _get_transmit_antenna_count_metadata = { "offset" : _get_transmit_antenna_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def transmit_antenna_count(self) -> int:
        """Get the transmit antenna count."""
        return self._intf.get_property(IAnalysisLink._metadata, IAnalysisLink._get_transmit_antenna_count_metadata)

    _get_receive_antenna_count_metadata = { "offset" : _get_receive_antenna_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def receive_antenna_count(self) -> int:
        """Get the receive antenna count."""
        return self._intf.get_property(IAnalysisLink._metadata, IAnalysisLink._get_receive_antenna_count_metadata)

    _get_analysis_intervals_metadata = { "offset" : _get_analysis_intervals_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def analysis_intervals(self) -> list:
        """Get the analysis intervals array."""
        return self._intf.get_property(IAnalysisLink._metadata, IAnalysisLink._get_analysis_intervals_metadata)

    _compute_metadata = { "offset" : _compute_method_offset,
            "arg_types" : (agcom.DOUBLE, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.InterfaceOutArg,) }
    def compute(self, time:float) -> "IResponse":
        """Compute the analysis link at the given time."""
        return self._intf.invoke(IAnalysisLink._metadata, IAnalysisLink._compute_metadata, time, OutArg())

    _property_names[name] = "name"
    _property_names[transmit_transceiver_identifier] = "transmit_transceiver_identifier"
    _property_names[transmit_transceiver_name] = "transmit_transceiver_name"
    _property_names[receive_transceiver_identifier] = "receive_transceiver_identifier"
    _property_names[receive_transceiver_name] = "receive_transceiver_name"
    _property_names[transmit_antenna_count] = "transmit_antenna_count"
    _property_names[receive_antenna_count] = "receive_antenna_count"
    _property_names[analysis_intervals] = "analysis_intervals"


agcls.AgClassCatalog.add_catalog_entry((5004542476303939694, 2475971475159732381), IAnalysisLink)
agcls.AgTypeNameMap["IAnalysisLink"] = IAnalysisLink

class IAnalysisConfigurationModel(object):
    """Base interface for all analysis configuration models."""

    _num_methods = 24
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _get_scene_contributor_collection_method_offset = 2
    _get_link_count_method_offset = 3
    _get_validate_configuration_method_offset = 4
    _get_validate_platform_facets_method_offset = 5
    _get_interval_start_method_offset = 6
    _set_interval_start_method_offset = 7
    _get_interval_stop_method_offset = 8
    _set_interval_stop_method_offset = 9
    _get_compute_step_mode_method_offset = 10
    _set_compute_step_mode_method_offset = 11
    _get_fixed_step_count_method_offset = 12
    _set_fixed_step_count_method_offset = 13
    _get_fixed_step_size_method_offset = 14
    _set_fixed_step_size_method_offset = 15
    _get_results_file_mode_method_offset = 16
    _set_results_file_mode_method_offset = 17
    _get_use_scenario_analysis_interval_method_offset = 18
    _set_use_scenario_analysis_interval_method_offset = 19
    _get_hide_incompatible_tilesets_method_offset = 20
    _set_hide_incompatible_tilesets_method_offset = 21
    _get_supported_facet_tilesets_method_offset = 22
    _get_facet_tileset_collection_method_offset = 23
    _get_analysis_extent_method_offset = 24
    _metadata = {
        "iid_data" : (5047897331686887030, 8592805011568395442),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IAnalysisConfigurationModel."""
        initialize_from_source_object(self, source_object, IAnalysisConfigurationModel)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IAnalysisConfigurationModel)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IAnalysisConfigurationModel, None)

    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(AnalysisConfigurationModelType),) }
    @property
    def type(self) -> "AnalysisConfigurationModelType":
        """Get the analysis configuration model type."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_type_metadata)

    _get_scene_contributor_collection_metadata = { "offset" : _get_scene_contributor_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def scene_contributor_collection(self) -> "ISceneContributorCollection":
        """Get the collection of scene contributors."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_scene_contributor_collection_metadata)

    _get_link_count_metadata = { "offset" : _get_link_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def link_count(self) -> int:
        """Get the link count."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_link_count_metadata)

    _get_validate_configuration_metadata = { "offset" : _get_validate_configuration_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def validate_configuration(self) -> "ValidationResponse":
        """Validate whether or not the configuration is ready to run."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_validate_configuration_metadata)

    _get_validate_platform_facets_metadata = { "offset" : _get_validate_platform_facets_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def validate_platform_facets(self) -> "ValidationResponse":
        """Validate the configuration platforms which provide facets are configured properly."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_validate_platform_facets_metadata)

    _get_interval_start_metadata = { "offset" : _get_interval_start_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def interval_start(self) -> float:
        """Get or set the interval start time."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_interval_start_metadata)

    _set_interval_start_metadata = { "offset" : _set_interval_start_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @interval_start.setter
    def interval_start(self, interval_start:float) -> None:
        """Get or set the interval start time."""
        return self._intf.set_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._set_interval_start_metadata, interval_start)

    _get_interval_stop_metadata = { "offset" : _get_interval_stop_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def interval_stop(self) -> float:
        """Get or set the interval stop time."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_interval_stop_metadata)

    _set_interval_stop_metadata = { "offset" : _set_interval_stop_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @interval_stop.setter
    def interval_stop(self, interval_stop:float) -> None:
        """Get or set the interval stop time."""
        return self._intf.set_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._set_interval_stop_metadata, interval_stop)

    _get_compute_step_mode_metadata = { "offset" : _get_compute_step_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(AnalysisConfigurationComputeStepMode),) }
    @property
    def compute_step_mode(self) -> "AnalysisConfigurationComputeStepMode":
        """Get or set the compute step mode."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_compute_step_mode_metadata)

    _set_compute_step_mode_metadata = { "offset" : _set_compute_step_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(AnalysisConfigurationComputeStepMode),) }
    @compute_step_mode.setter
    def compute_step_mode(self, compute_step_mode:"AnalysisConfigurationComputeStepMode") -> None:
        """Get or set the compute step mode."""
        return self._intf.set_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._set_compute_step_mode_metadata, compute_step_mode)

    _get_fixed_step_count_metadata = { "offset" : _get_fixed_step_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def fixed_step_count(self) -> int:
        """Get or set the step count."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_fixed_step_count_metadata)

    _set_fixed_step_count_metadata = { "offset" : _set_fixed_step_count_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @fixed_step_count.setter
    def fixed_step_count(self, step_count:int) -> None:
        """Get or set the step count."""
        return self._intf.set_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._set_fixed_step_count_metadata, step_count)

    _get_fixed_step_size_metadata = { "offset" : _get_fixed_step_size_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def fixed_step_size(self) -> float:
        """Get or set the step size."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_fixed_step_size_metadata)

    _set_fixed_step_size_metadata = { "offset" : _set_fixed_step_size_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @fixed_step_size.setter
    def fixed_step_size(self, step_size:float) -> None:
        """Get or set the step size."""
        return self._intf.set_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._set_fixed_step_size_metadata, step_size)

    _get_results_file_mode_metadata = { "offset" : _get_results_file_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(AnalysisResultsFileMode),) }
    @property
    def results_file_mode(self) -> "AnalysisResultsFileMode":
        """Get or set the results file mode."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_results_file_mode_metadata)

    _set_results_file_mode_metadata = { "offset" : _set_results_file_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(AnalysisResultsFileMode),) }
    @results_file_mode.setter
    def results_file_mode(self, value:"AnalysisResultsFileMode") -> None:
        """Get or set the results file mode."""
        return self._intf.set_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._set_results_file_mode_metadata, value)

    _get_use_scenario_analysis_interval_metadata = { "offset" : _get_use_scenario_analysis_interval_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def use_scenario_analysis_interval(self) -> bool:
        """Get or set whether or not to use the scenario analysis interval."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_use_scenario_analysis_interval_metadata)

    _set_use_scenario_analysis_interval_metadata = { "offset" : _set_use_scenario_analysis_interval_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @use_scenario_analysis_interval.setter
    def use_scenario_analysis_interval(self, value:bool) -> None:
        """Get or set whether or not to use the scenario analysis interval."""
        return self._intf.set_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._set_use_scenario_analysis_interval_metadata, value)

    _get_hide_incompatible_tilesets_metadata = { "offset" : _get_hide_incompatible_tilesets_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def hide_incompatible_tilesets(self) -> bool:
        """Get or set the show all tilesets indicator."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_hide_incompatible_tilesets_metadata)

    _set_hide_incompatible_tilesets_metadata = { "offset" : _set_hide_incompatible_tilesets_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @hide_incompatible_tilesets.setter
    def hide_incompatible_tilesets(self, value:bool) -> None:
        """Get or set the show all tilesets indicator."""
        return self._intf.set_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._set_hide_incompatible_tilesets_metadata, value)

    _get_supported_facet_tilesets_metadata = { "offset" : _get_supported_facet_tilesets_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_facet_tilesets(self) -> list:
        """Get an array of available facet tilesets."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_supported_facet_tilesets_metadata)

    _get_facet_tileset_collection_metadata = { "offset" : _get_facet_tileset_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def facet_tileset_collection(self) -> "FacetTilesetCollection":
        """Get the collection of facet tilesets."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_facet_tileset_collection_metadata)

    _get_analysis_extent_metadata = { "offset" : _get_analysis_extent_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def analysis_extent(self) -> "Extent":
        """Get the facet tileset extent."""
        return self._intf.get_property(IAnalysisConfigurationModel._metadata, IAnalysisConfigurationModel._get_analysis_extent_metadata)

    _property_names[type] = "type"
    _property_names[scene_contributor_collection] = "scene_contributor_collection"
    _property_names[link_count] = "link_count"
    _property_names[validate_configuration] = "validate_configuration"
    _property_names[validate_platform_facets] = "validate_platform_facets"
    _property_names[interval_start] = "interval_start"
    _property_names[interval_stop] = "interval_stop"
    _property_names[compute_step_mode] = "compute_step_mode"
    _property_names[fixed_step_count] = "fixed_step_count"
    _property_names[fixed_step_size] = "fixed_step_size"
    _property_names[results_file_mode] = "results_file_mode"
    _property_names[use_scenario_analysis_interval] = "use_scenario_analysis_interval"
    _property_names[hide_incompatible_tilesets] = "hide_incompatible_tilesets"
    _property_names[supported_facet_tilesets] = "supported_facet_tilesets"
    _property_names[facet_tileset_collection] = "facet_tileset_collection"
    _property_names[analysis_extent] = "analysis_extent"


agcls.AgClassCatalog.add_catalog_entry((5047897331686887030, 8592805011568395442), IAnalysisConfigurationModel)
agcls.AgTypeNameMap["IAnalysisConfigurationModel"] = IAnalysisConfigurationModel

class IRadarAnalysisConfigurationModel(object):
    """Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_transceiver_configuration_collection_method_offset = 1
    _get_imaging_data_product_list_method_offset = 2
    _metadata = {
        "iid_data" : (5295919618977899412, 380209664131620768),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IRadarAnalysisConfigurationModel."""
        initialize_from_source_object(self, source_object, IRadarAnalysisConfigurationModel)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IRadarAnalysisConfigurationModel)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IRadarAnalysisConfigurationModel, None)

    _get_transceiver_configuration_collection_metadata = { "offset" : _get_transceiver_configuration_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver_configuration_collection(self) -> "RadarTransceiverConfigurationCollection":
        """Get the collection of transceiver configurations."""
        return self._intf.get_property(IRadarAnalysisConfigurationModel._metadata, IRadarAnalysisConfigurationModel._get_transceiver_configuration_collection_metadata)

    _get_imaging_data_product_list_metadata = { "offset" : _get_imaging_data_product_list_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def imaging_data_product_list(self) -> "RadarImagingDataProductCollection":
        """Get the imaging product list."""
        return self._intf.get_property(IRadarAnalysisConfigurationModel._metadata, IRadarAnalysisConfigurationModel._get_imaging_data_product_list_metadata)

    _property_names[transceiver_configuration_collection] = "transceiver_configuration_collection"
    _property_names[imaging_data_product_list] = "imaging_data_product_list"


agcls.AgClassCatalog.add_catalog_entry((5295919618977899412, 380209664131620768), IRadarAnalysisConfigurationModel)
agcls.AgTypeNameMap["IRadarAnalysisConfigurationModel"] = IRadarAnalysisConfigurationModel



class RadarImagingDataProduct(SupportsDeleteCallback):
    """Properties for the imaging data product."""

    _num_methods = 36
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_name_method_offset = 1
    _get_enable_sensor_fixed_distance_method_offset = 2
    _set_enable_sensor_fixed_distance_method_offset = 3
    _get_desired_sensor_fixed_distance_method_offset = 4
    _set_desired_sensor_fixed_distance_method_offset = 5
    _get_distance_to_range_window_start_method_offset = 6
    _get_distance_to_range_window_center_method_offset = 7
    _get_center_image_in_range_window_method_offset = 8
    _set_center_image_in_range_window_method_offset = 9
    _get_enable_range_doppler_imaging_method_offset = 10
    _set_enable_range_doppler_imaging_method_offset = 11
    _get_range_pixel_count_method_offset = 12
    _set_range_pixel_count_method_offset = 13
    _get_velocity_pixel_count_method_offset = 14
    _set_velocity_pixel_count_method_offset = 15
    _get_range_window_type_method_offset = 16
    _set_range_window_type_method_offset = 17
    _get_range_window_side_lobe_level_method_offset = 18
    _set_range_window_side_lobe_level_method_offset = 19
    _get_velocity_window_type_method_offset = 20
    _set_velocity_window_type_method_offset = 21
    _get_velocity_window_side_lobe_level_method_offset = 22
    _set_velocity_window_side_lobe_level_method_offset = 23
    _get_range_resolution_method_offset = 24
    _set_range_resolution_method_offset = 25
    _get_range_window_size_method_offset = 26
    _set_range_window_size_method_offset = 27
    _get_cross_range_resolution_method_offset = 28
    _set_cross_range_resolution_method_offset = 29
    _get_cross_range_window_size_method_offset = 30
    _set_cross_range_window_size_method_offset = 31
    _get_required_bandwidth_method_offset = 32
    _get_collection_angle_method_offset = 33
    _get_frequency_samples_per_pulse_method_offset = 34
    _get_minimum_pulse_count_method_offset = 35
    _get_identifier_method_offset = 36
    _metadata = {
        "iid_data" : (5639756055740420746, 14831647007956190867),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarImagingDataProduct)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the image product name."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_name_metadata)

    _get_enable_sensor_fixed_distance_metadata = { "offset" : _get_enable_sensor_fixed_distance_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def enable_sensor_fixed_distance(self) -> bool:
        """Enable or disables the fixed disatance mode."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_enable_sensor_fixed_distance_metadata)

    _set_enable_sensor_fixed_distance_metadata = { "offset" : _set_enable_sensor_fixed_distance_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @enable_sensor_fixed_distance.setter
    def enable_sensor_fixed_distance(self, value:bool) -> None:
        """Enable or disables the fixed disatance mode."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_enable_sensor_fixed_distance_metadata, value)

    _get_desired_sensor_fixed_distance_metadata = { "offset" : _get_desired_sensor_fixed_distance_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def desired_sensor_fixed_distance(self) -> float:
        """Get or set the fixed disatance."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_desired_sensor_fixed_distance_metadata)

    _set_desired_sensor_fixed_distance_metadata = { "offset" : _set_desired_sensor_fixed_distance_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @desired_sensor_fixed_distance.setter
    def desired_sensor_fixed_distance(self, value:float) -> None:
        """Get or set the fixed disatance."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_desired_sensor_fixed_distance_metadata, value)

    _get_distance_to_range_window_start_metadata = { "offset" : _get_distance_to_range_window_start_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def distance_to_range_window_start(self) -> float:
        """Get or set the distance to the range window start."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_distance_to_range_window_start_metadata)

    _get_distance_to_range_window_center_metadata = { "offset" : _get_distance_to_range_window_center_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def distance_to_range_window_center(self) -> float:
        """Get or set the distance to the range window center."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_distance_to_range_window_center_metadata)

    _get_center_image_in_range_window_metadata = { "offset" : _get_center_image_in_range_window_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def center_image_in_range_window(self) -> bool:
        """Enable or disables whether the image will be centered in the range window."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_center_image_in_range_window_metadata)

    _set_center_image_in_range_window_metadata = { "offset" : _set_center_image_in_range_window_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @center_image_in_range_window.setter
    def center_image_in_range_window(self, value:bool) -> None:
        """Enable or disables whether the image will be centered in the range window."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_center_image_in_range_window_metadata, value)

    _get_enable_range_doppler_imaging_metadata = { "offset" : _get_enable_range_doppler_imaging_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def enable_range_doppler_imaging(self) -> bool:
        """Enable radar range-doppler imaging."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_enable_range_doppler_imaging_metadata)

    _set_enable_range_doppler_imaging_metadata = { "offset" : _set_enable_range_doppler_imaging_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @enable_range_doppler_imaging.setter
    def enable_range_doppler_imaging(self, value:bool) -> None:
        """Enable radar range-doppler imaging."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_enable_range_doppler_imaging_metadata, value)

    _get_range_pixel_count_metadata = { "offset" : _get_range_pixel_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def range_pixel_count(self) -> int:
        """Get or set the range pixel count."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_range_pixel_count_metadata)

    _set_range_pixel_count_metadata = { "offset" : _set_range_pixel_count_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @range_pixel_count.setter
    def range_pixel_count(self, value:int) -> None:
        """Get or set the range pixel count."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_range_pixel_count_metadata, value)

    _get_velocity_pixel_count_metadata = { "offset" : _get_velocity_pixel_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def velocity_pixel_count(self) -> int:
        """Get or set the velocity pixel count."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_velocity_pixel_count_metadata)

    _set_velocity_pixel_count_metadata = { "offset" : _set_velocity_pixel_count_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @velocity_pixel_count.setter
    def velocity_pixel_count(self, value:int) -> None:
        """Get or set the velocity pixel count."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_velocity_pixel_count_metadata, value)

    _get_range_window_type_metadata = { "offset" : _get_range_window_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ImageWindowType),) }
    @property
    def range_window_type(self) -> "ImageWindowType":
        """Get or set the range window type."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_range_window_type_metadata)

    _set_range_window_type_metadata = { "offset" : _set_range_window_type_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ImageWindowType),) }
    @range_window_type.setter
    def range_window_type(self, value:"ImageWindowType") -> None:
        """Get or set the range window type."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_range_window_type_metadata, value)

    _get_range_window_side_lobe_level_metadata = { "offset" : _get_range_window_side_lobe_level_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def range_window_side_lobe_level(self) -> float:
        """Get or set the range window side lobe level."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_range_window_side_lobe_level_metadata)

    _set_range_window_side_lobe_level_metadata = { "offset" : _set_range_window_side_lobe_level_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @range_window_side_lobe_level.setter
    def range_window_side_lobe_level(self, value:float) -> None:
        """Get or set the range window side lobe level."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_range_window_side_lobe_level_metadata, value)

    _get_velocity_window_type_metadata = { "offset" : _get_velocity_window_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(ImageWindowType),) }
    @property
    def velocity_window_type(self) -> "ImageWindowType":
        """Get or set the velocity window type."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_velocity_window_type_metadata)

    _set_velocity_window_type_metadata = { "offset" : _set_velocity_window_type_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(ImageWindowType),) }
    @velocity_window_type.setter
    def velocity_window_type(self, value:"ImageWindowType") -> None:
        """Get or set the velocity window type."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_velocity_window_type_metadata, value)

    _get_velocity_window_side_lobe_level_metadata = { "offset" : _get_velocity_window_side_lobe_level_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def velocity_window_side_lobe_level(self) -> float:
        """Get or set the velocity window side lobe level."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_velocity_window_side_lobe_level_metadata)

    _set_velocity_window_side_lobe_level_metadata = { "offset" : _set_velocity_window_side_lobe_level_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @velocity_window_side_lobe_level.setter
    def velocity_window_side_lobe_level(self, value:float) -> None:
        """Get or set the velocity window side lobe level."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_velocity_window_side_lobe_level_metadata, value)

    _get_range_resolution_metadata = { "offset" : _get_range_resolution_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def range_resolution(self) -> float:
        """Get or set the range resolution."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_range_resolution_metadata)

    _set_range_resolution_metadata = { "offset" : _set_range_resolution_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @range_resolution.setter
    def range_resolution(self, value:float) -> None:
        """Get or set the range resolution."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_range_resolution_metadata, value)

    _get_range_window_size_metadata = { "offset" : _get_range_window_size_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def range_window_size(self) -> float:
        """Get or set the range window size."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_range_window_size_metadata)

    _set_range_window_size_metadata = { "offset" : _set_range_window_size_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @range_window_size.setter
    def range_window_size(self, value:float) -> None:
        """Get or set the range window size."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_range_window_size_metadata, value)

    _get_cross_range_resolution_metadata = { "offset" : _get_cross_range_resolution_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def cross_range_resolution(self) -> float:
        """Get or set the cross range resolution."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_cross_range_resolution_metadata)

    _set_cross_range_resolution_metadata = { "offset" : _set_cross_range_resolution_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @cross_range_resolution.setter
    def cross_range_resolution(self, value:float) -> None:
        """Get or set the cross range resolution."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_cross_range_resolution_metadata, value)

    _get_cross_range_window_size_metadata = { "offset" : _get_cross_range_window_size_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def cross_range_window_size(self) -> float:
        """Get or set the cross range window size."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_cross_range_window_size_metadata)

    _set_cross_range_window_size_metadata = { "offset" : _set_cross_range_window_size_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @cross_range_window_size.setter
    def cross_range_window_size(self, value:float) -> None:
        """Get or set the cross range window size."""
        return self._intf.set_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._set_cross_range_window_size_metadata, value)

    _get_required_bandwidth_metadata = { "offset" : _get_required_bandwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def required_bandwidth(self) -> float:
        """Get the waveform product's required bandwidth."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_required_bandwidth_metadata)

    _get_collection_angle_metadata = { "offset" : _get_collection_angle_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def collection_angle(self) -> float:
        """Get the waveform collection angle."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_collection_angle_metadata)

    _get_frequency_samples_per_pulse_metadata = { "offset" : _get_frequency_samples_per_pulse_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def frequency_samples_per_pulse(self) -> int:
        """Get the number of frequency samples per pulse."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_frequency_samples_per_pulse_metadata)

    _get_minimum_pulse_count_metadata = { "offset" : _get_minimum_pulse_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def minimum_pulse_count(self) -> int:
        """Get the minimum pulse count."""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_minimum_pulse_count_metadata)

    _get_identifier_metadata = { "offset" : _get_identifier_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def identifier(self) -> str:
        """Get the unique identifier for the data product"""
        return self._intf.get_property(RadarImagingDataProduct._metadata, RadarImagingDataProduct._get_identifier_metadata)

    _property_names[name] = "name"
    _property_names[enable_sensor_fixed_distance] = "enable_sensor_fixed_distance"
    _property_names[desired_sensor_fixed_distance] = "desired_sensor_fixed_distance"
    _property_names[distance_to_range_window_start] = "distance_to_range_window_start"
    _property_names[distance_to_range_window_center] = "distance_to_range_window_center"
    _property_names[center_image_in_range_window] = "center_image_in_range_window"
    _property_names[enable_range_doppler_imaging] = "enable_range_doppler_imaging"
    _property_names[range_pixel_count] = "range_pixel_count"
    _property_names[velocity_pixel_count] = "velocity_pixel_count"
    _property_names[range_window_type] = "range_window_type"
    _property_names[range_window_side_lobe_level] = "range_window_side_lobe_level"
    _property_names[velocity_window_type] = "velocity_window_type"
    _property_names[velocity_window_side_lobe_level] = "velocity_window_side_lobe_level"
    _property_names[range_resolution] = "range_resolution"
    _property_names[range_window_size] = "range_window_size"
    _property_names[cross_range_resolution] = "cross_range_resolution"
    _property_names[cross_range_window_size] = "cross_range_window_size"
    _property_names[required_bandwidth] = "required_bandwidth"
    _property_names[collection_angle] = "collection_angle"
    _property_names[frequency_samples_per_pulse] = "frequency_samples_per_pulse"
    _property_names[minimum_pulse_count] = "minimum_pulse_count"
    _property_names[identifier] = "identifier"

    def __init__(self, source_object=None):
        """Construct an object of type RadarImagingDataProduct."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarImagingDataProduct)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarImagingDataProduct, [RadarImagingDataProduct, ])

agcls.AgClassCatalog.add_catalog_entry((5226680878930314362, 6014842735258329523), RadarImagingDataProduct)
agcls.AgTypeNameMap["RadarImagingDataProduct"] = RadarImagingDataProduct

class Material(SupportsDeleteCallback):
    """Properties for a material."""

    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _set_type_method_offset = 2
    _get_properties_method_offset = 3
    _set_properties_method_offset = 4
    _get_height_standard_deviation_method_offset = 5
    _set_height_standard_deviation_method_offset = 6
    _get_roughness_method_offset = 7
    _set_roughness_method_offset = 8
    _metadata = {
        "iid_data" : (4741553615154377493, 2156103163304633273),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Material)

    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def type(self) -> str:
        """Get material type."""
        return self._intf.get_property(Material._metadata, Material._get_type_metadata)

    _set_type_metadata = { "offset" : _set_type_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @type.setter
    def type(self, value:str) -> None:
        """Set material type."""
        return self._intf.set_property(Material._metadata, Material._set_type_metadata, value)

    _get_properties_metadata = { "offset" : _get_properties_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def properties(self) -> str:
        """Get material properties."""
        return self._intf.get_property(Material._metadata, Material._get_properties_metadata)

    _set_properties_metadata = { "offset" : _set_properties_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @properties.setter
    def properties(self, value:str) -> None:
        """Set material properties."""
        return self._intf.set_property(Material._metadata, Material._set_properties_metadata, value)

    _get_height_standard_deviation_metadata = { "offset" : _get_height_standard_deviation_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def height_standard_deviation(self) -> float:
        """Get or set the material height standard deviation"""
        return self._intf.get_property(Material._metadata, Material._get_height_standard_deviation_metadata)

    _set_height_standard_deviation_metadata = { "offset" : _set_height_standard_deviation_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @height_standard_deviation.setter
    def height_standard_deviation(self, value:float) -> None:
        """Get or set the material height standard deviation"""
        return self._intf.set_property(Material._metadata, Material._set_height_standard_deviation_metadata, value)

    _get_roughness_metadata = { "offset" : _get_roughness_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def roughness(self) -> float:
        """Get or set the material roughness"""
        return self._intf.get_property(Material._metadata, Material._get_roughness_metadata)

    _set_roughness_metadata = { "offset" : _set_roughness_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @roughness.setter
    def roughness(self, value:float) -> None:
        """Get or set the material roughness"""
        return self._intf.set_property(Material._metadata, Material._set_roughness_metadata, value)

    _property_names[type] = "type"
    _property_names[properties] = "properties"
    _property_names[height_standard_deviation] = "height_standard_deviation"
    _property_names[roughness] = "roughness"

    def __init__(self, source_object=None):
        """Construct an object of type Material."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Material)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Material, [Material, ])

agcls.AgClassCatalog.add_catalog_entry((5551816211234442013, 13389948598869303701), Material)
agcls.AgTypeNameMap["Material"] = Material

class FacetTileset(SupportsDeleteCallback):
    """Properties of a facet tile set."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_name_method_offset = 1
    _get_uri_method_offset = 2
    _get_material_method_offset = 3
    _set_material_method_offset = 4
    _get_reference_frame_method_offset = 5
    _get_central_body_name_method_offset = 6
    _metadata = {
        "iid_data" : (4690660055317251169, 12365511564088604577),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, FacetTileset)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the facet tileset name."""
        return self._intf.get_property(FacetTileset._metadata, FacetTileset._get_name_metadata)

    _get_uri_metadata = { "offset" : _get_uri_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def uri(self) -> str:
        """Get the facet tileset uri."""
        return self._intf.get_property(FacetTileset._metadata, FacetTileset._get_uri_metadata)

    _get_material_metadata = { "offset" : _get_material_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def material(self) -> str:
        """Get or set the tileset material."""
        return self._intf.get_property(FacetTileset._metadata, FacetTileset._get_material_metadata)

    _set_material_metadata = { "offset" : _set_material_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @material.setter
    def material(self, value:str) -> None:
        """Get or set the tileset material."""
        return self._intf.set_property(FacetTileset._metadata, FacetTileset._set_material_metadata, value)

    _get_reference_frame_metadata = { "offset" : _get_reference_frame_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def reference_frame(self) -> str:
        """Get the tileset reference frame."""
        return self._intf.get_property(FacetTileset._metadata, FacetTileset._get_reference_frame_metadata)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the tileset central body name."""
        return self._intf.get_property(FacetTileset._metadata, FacetTileset._get_central_body_name_metadata)

    _property_names[name] = "name"
    _property_names[uri] = "uri"
    _property_names[material] = "material"
    _property_names[reference_frame] = "reference_frame"
    _property_names[central_body_name] = "central_body_name"

    def __init__(self, source_object=None):
        """Construct an object of type FacetTileset."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, FacetTileset)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, FacetTileset, [FacetTileset, ])

agcls.AgClassCatalog.add_catalog_entry((5450031916903433591, 5575085354633319297), FacetTileset)
agcls.AgTypeNameMap["FacetTileset"] = FacetTileset

class ValidationResponse(SupportsDeleteCallback):
    """Properties of the response from validating an analysis configuration."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_value_method_offset = 1
    _get_message_method_offset = 2
    _metadata = {
        "iid_data" : (5579774226002829185, 17104797398372433833),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ValidationResponse)

    _get_value_metadata = { "offset" : _get_value_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def value(self) -> bool:
        """Get the validation indicator."""
        return self._intf.get_property(ValidationResponse._metadata, ValidationResponse._get_value_metadata)

    _get_message_metadata = { "offset" : _get_message_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def message(self) -> str:
        """Get the validation message."""
        return self._intf.get_property(ValidationResponse._metadata, ValidationResponse._get_message_metadata)

    _property_names[value] = "value"
    _property_names[message] = "message"

    def __init__(self, source_object=None):
        """Construct an object of type ValidationResponse."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ValidationResponse)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ValidationResponse, [ValidationResponse, ])

agcls.AgClassCatalog.add_catalog_entry((5164176704895655660, 4265067833704363702), ValidationResponse)
agcls.AgTypeNameMap["ValidationResponse"] = ValidationResponse

class Extent(SupportsDeleteCallback):
    """Properties for a cartographic extent definition. One use of this interface is for defining the facet tile set analysis extent."""

    _num_methods = 9
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_north_latitude_method_offset = 1
    _set_north_latitude_method_offset = 2
    _get_south_latitude_method_offset = 3
    _set_south_latitude_method_offset = 4
    _get_east_longitude_method_offset = 5
    _set_east_longitude_method_offset = 6
    _get_west_longitude_method_offset = 7
    _set_west_longitude_method_offset = 8
    _set_extent_values_method_offset = 9
    _metadata = {
        "iid_data" : (4925304525695672828, 7391264363279355565),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Extent)

    _get_north_latitude_metadata = { "offset" : _get_north_latitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def north_latitude(self) -> float:
        """Get or set the north latitude."""
        return self._intf.get_property(Extent._metadata, Extent._get_north_latitude_metadata)

    _set_north_latitude_metadata = { "offset" : _set_north_latitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @north_latitude.setter
    def north_latitude(self, value:float) -> None:
        """Get or set the north latitude."""
        return self._intf.set_property(Extent._metadata, Extent._set_north_latitude_metadata, value)

    _get_south_latitude_metadata = { "offset" : _get_south_latitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def south_latitude(self) -> float:
        """Get or set the south latitude."""
        return self._intf.get_property(Extent._metadata, Extent._get_south_latitude_metadata)

    _set_south_latitude_metadata = { "offset" : _set_south_latitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @south_latitude.setter
    def south_latitude(self, value:float) -> None:
        """Get or set the south latitude."""
        return self._intf.set_property(Extent._metadata, Extent._set_south_latitude_metadata, value)

    _get_east_longitude_metadata = { "offset" : _get_east_longitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def east_longitude(self) -> float:
        """Get or set the east longitude."""
        return self._intf.get_property(Extent._metadata, Extent._get_east_longitude_metadata)

    _set_east_longitude_metadata = { "offset" : _set_east_longitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @east_longitude.setter
    def east_longitude(self, value:float) -> None:
        """Get or set the east longitude."""
        return self._intf.set_property(Extent._metadata, Extent._set_east_longitude_metadata, value)

    _get_west_longitude_metadata = { "offset" : _get_west_longitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def west_longitude(self) -> float:
        """Get or set the west longitude."""
        return self._intf.get_property(Extent._metadata, Extent._get_west_longitude_metadata)

    _set_west_longitude_metadata = { "offset" : _set_west_longitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @west_longitude.setter
    def west_longitude(self, value:float) -> None:
        """Get or set the west longitude."""
        return self._intf.set_property(Extent._metadata, Extent._set_west_longitude_metadata, value)

    _set_extent_values_metadata = { "offset" : _set_extent_values_method_offset,
            "arg_types" : (agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE, agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg, agmarshall.DoubleArg,) }
    def set_extent_values(self, north:float, south:float, east:float, west:float) -> None:
        """Set the extent values in degrees"""
        return self._intf.invoke(Extent._metadata, Extent._set_extent_values_metadata, north, south, east, west)

    _property_names[north_latitude] = "north_latitude"
    _property_names[south_latitude] = "south_latitude"
    _property_names[east_longitude] = "east_longitude"
    _property_names[west_longitude] = "west_longitude"

    def __init__(self, source_object=None):
        """Construct an object of type Extent."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Extent)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Extent, [Extent, ])

agcls.AgClassCatalog.add_catalog_entry((5151834154770850459, 13344785038746445746), Extent)
agcls.AgTypeNameMap["Extent"] = Extent

class CommunicationsWaveform(SupportsDeleteCallback):
    """Properties for a communications waveform."""

    _num_methods = 13
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_frequency_samples_per_sounding_method_offset = 1
    _set_frequency_samples_per_sounding_method_offset = 2
    _get_channel_bandwidth_method_offset = 3
    _set_channel_bandwidth_method_offset = 4
    _get_rf_channel_frequency_method_offset = 5
    _set_rf_channel_frequency_method_offset = 6
    _get_sounding_interval_method_offset = 7
    _set_sounding_interval_method_offset = 8
    _get_soundings_per_analysis_time_step_method_offset = 9
    _set_soundings_per_analysis_time_step_method_offset = 10
    _get_complete_simulation_interval_method_offset = 11
    _get_unambiguous_channel_delay_method_offset = 12
    _get_unambiguous_channel_distance_method_offset = 13
    _metadata = {
        "iid_data" : (5701009895544568603, 4060828244725623999),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, CommunicationsWaveform)

    _get_frequency_samples_per_sounding_metadata = { "offset" : _get_frequency_samples_per_sounding_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def frequency_samples_per_sounding(self) -> int:
        """Get or set the waveform number of samples."""
        return self._intf.get_property(CommunicationsWaveform._metadata, CommunicationsWaveform._get_frequency_samples_per_sounding_metadata)

    _set_frequency_samples_per_sounding_metadata = { "offset" : _set_frequency_samples_per_sounding_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @frequency_samples_per_sounding.setter
    def frequency_samples_per_sounding(self, value:int) -> None:
        """Get or set the waveform number of samples."""
        return self._intf.set_property(CommunicationsWaveform._metadata, CommunicationsWaveform._set_frequency_samples_per_sounding_metadata, value)

    _get_channel_bandwidth_metadata = { "offset" : _get_channel_bandwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def channel_bandwidth(self) -> float:
        """Get or set the waveform bandwidth."""
        return self._intf.get_property(CommunicationsWaveform._metadata, CommunicationsWaveform._get_channel_bandwidth_metadata)

    _set_channel_bandwidth_metadata = { "offset" : _set_channel_bandwidth_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @channel_bandwidth.setter
    def channel_bandwidth(self, value:float) -> None:
        """Get or set the waveform bandwidth."""
        return self._intf.set_property(CommunicationsWaveform._metadata, CommunicationsWaveform._set_channel_bandwidth_metadata, value)

    _get_rf_channel_frequency_metadata = { "offset" : _get_rf_channel_frequency_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def rf_channel_frequency(self) -> float:
        """Get or set the waveform frequency."""
        return self._intf.get_property(CommunicationsWaveform._metadata, CommunicationsWaveform._get_rf_channel_frequency_metadata)

    _set_rf_channel_frequency_metadata = { "offset" : _set_rf_channel_frequency_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @rf_channel_frequency.setter
    def rf_channel_frequency(self, value:float) -> None:
        """Get or set the waveform frequency."""
        return self._intf.set_property(CommunicationsWaveform._metadata, CommunicationsWaveform._set_rf_channel_frequency_metadata, value)

    _get_sounding_interval_metadata = { "offset" : _get_sounding_interval_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def sounding_interval(self) -> float:
        """Get or set the waveform pulse interval."""
        return self._intf.get_property(CommunicationsWaveform._metadata, CommunicationsWaveform._get_sounding_interval_metadata)

    _set_sounding_interval_metadata = { "offset" : _set_sounding_interval_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @sounding_interval.setter
    def sounding_interval(self, value:float) -> None:
        """Get or set the waveform pulse interval."""
        return self._intf.set_property(CommunicationsWaveform._metadata, CommunicationsWaveform._set_sounding_interval_metadata, value)

    _get_soundings_per_analysis_time_step_metadata = { "offset" : _get_soundings_per_analysis_time_step_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def soundings_per_analysis_time_step(self) -> int:
        """Get or set the waveform number of pulses."""
        return self._intf.get_property(CommunicationsWaveform._metadata, CommunicationsWaveform._get_soundings_per_analysis_time_step_metadata)

    _set_soundings_per_analysis_time_step_metadata = { "offset" : _set_soundings_per_analysis_time_step_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @soundings_per_analysis_time_step.setter
    def soundings_per_analysis_time_step(self, value:int) -> None:
        """Get or set the waveform number of pulses."""
        return self._intf.set_property(CommunicationsWaveform._metadata, CommunicationsWaveform._set_soundings_per_analysis_time_step_metadata, value)

    _get_complete_simulation_interval_metadata = { "offset" : _get_complete_simulation_interval_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def complete_simulation_interval(self) -> float:
        """Get the complete simulation interval."""
        return self._intf.get_property(CommunicationsWaveform._metadata, CommunicationsWaveform._get_complete_simulation_interval_metadata)

    _get_unambiguous_channel_delay_metadata = { "offset" : _get_unambiguous_channel_delay_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def unambiguous_channel_delay(self) -> float:
        """Get the unambiguous channel delay."""
        return self._intf.get_property(CommunicationsWaveform._metadata, CommunicationsWaveform._get_unambiguous_channel_delay_metadata)

    _get_unambiguous_channel_distance_metadata = { "offset" : _get_unambiguous_channel_distance_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def unambiguous_channel_distance(self) -> float:
        """Get the unambiguous channel distance."""
        return self._intf.get_property(CommunicationsWaveform._metadata, CommunicationsWaveform._get_unambiguous_channel_distance_metadata)

    _property_names[frequency_samples_per_sounding] = "frequency_samples_per_sounding"
    _property_names[channel_bandwidth] = "channel_bandwidth"
    _property_names[rf_channel_frequency] = "rf_channel_frequency"
    _property_names[sounding_interval] = "sounding_interval"
    _property_names[soundings_per_analysis_time_step] = "soundings_per_analysis_time_step"
    _property_names[complete_simulation_interval] = "complete_simulation_interval"
    _property_names[unambiguous_channel_delay] = "unambiguous_channel_delay"
    _property_names[unambiguous_channel_distance] = "unambiguous_channel_distance"

    def __init__(self, source_object=None):
        """Construct an object of type CommunicationsWaveform."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, CommunicationsWaveform)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommunicationsWaveform, [CommunicationsWaveform, ])

agcls.AgClassCatalog.add_catalog_entry((5501289608801900526, 13017124479502804625), CommunicationsWaveform)
agcls.AgTypeNameMap["CommunicationsWaveform"] = CommunicationsWaveform

class RadarWaveform(SupportsDeleteCallback):
    """Properties for a radar waveform."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_rf_channel_frequency_method_offset = 1
    _set_rf_channel_frequency_method_offset = 2
    _get_pulse_repetition_frequency_method_offset = 3
    _set_pulse_repetition_frequency_method_offset = 4
    _get_bandwidth_method_offset = 5
    _set_bandwidth_method_offset = 6
    _metadata = {
        "iid_data" : (4829791723709714335, 18003048008441454732),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarWaveform)

    _get_rf_channel_frequency_metadata = { "offset" : _get_rf_channel_frequency_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def rf_channel_frequency(self) -> float:
        """Get or set the waveform frequency."""
        return self._intf.get_property(RadarWaveform._metadata, RadarWaveform._get_rf_channel_frequency_metadata)

    _set_rf_channel_frequency_metadata = { "offset" : _set_rf_channel_frequency_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @rf_channel_frequency.setter
    def rf_channel_frequency(self, value:float) -> None:
        """Get or set the waveform frequency."""
        return self._intf.set_property(RadarWaveform._metadata, RadarWaveform._set_rf_channel_frequency_metadata, value)

    _get_pulse_repetition_frequency_metadata = { "offset" : _get_pulse_repetition_frequency_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def pulse_repetition_frequency(self) -> float:
        """Get or set the pulse repetition frequency."""
        return self._intf.get_property(RadarWaveform._metadata, RadarWaveform._get_pulse_repetition_frequency_metadata)

    _set_pulse_repetition_frequency_metadata = { "offset" : _set_pulse_repetition_frequency_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @pulse_repetition_frequency.setter
    def pulse_repetition_frequency(self, value:float) -> None:
        """Get or set the pulse repetition frequency."""
        return self._intf.set_property(RadarWaveform._metadata, RadarWaveform._set_pulse_repetition_frequency_metadata, value)

    _get_bandwidth_metadata = { "offset" : _get_bandwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def bandwidth(self) -> float:
        """Get or set the waveform bandwidth."""
        return self._intf.get_property(RadarWaveform._metadata, RadarWaveform._get_bandwidth_metadata)

    _set_bandwidth_metadata = { "offset" : _set_bandwidth_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @bandwidth.setter
    def bandwidth(self, value:float) -> None:
        """Get or set the waveform bandwidth."""
        return self._intf.set_property(RadarWaveform._metadata, RadarWaveform._set_bandwidth_metadata, value)

    _property_names[rf_channel_frequency] = "rf_channel_frequency"
    _property_names[pulse_repetition_frequency] = "pulse_repetition_frequency"
    _property_names[bandwidth] = "bandwidth"

    def __init__(self, source_object=None):
        """Construct an object of type RadarWaveform."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarWaveform)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarWaveform, [RadarWaveform, ])

agcls.AgClassCatalog.add_catalog_entry((5130441002877563298, 11472922400229006745), RadarWaveform)
agcls.AgTypeNameMap["RadarWaveform"] = RadarWaveform

class ParametricBeamAntenna(IAntenna, SupportsDeleteCallback):
    """Properties of an analytical parametric beam antenna."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_polarization_type_method_offset = 1
    _set_polarization_type_method_offset = 2
    _get_vertical_beamwidth_method_offset = 3
    _set_vertical_beamwidth_method_offset = 4
    _get_horizontal_beamwidth_method_offset = 5
    _set_horizontal_beamwidth_method_offset = 6
    _metadata = {
        "iid_data" : (5443044110083441021, 4335029080365028777),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ParametricBeamAntenna)

    _get_polarization_type_metadata = { "offset" : _get_polarization_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(PolarizationType),) }
    @property
    def polarization_type(self) -> "PolarizationType":
        """Get or set the polarization type"""
        return self._intf.get_property(ParametricBeamAntenna._metadata, ParametricBeamAntenna._get_polarization_type_metadata)

    _set_polarization_type_metadata = { "offset" : _set_polarization_type_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(PolarizationType),) }
    @polarization_type.setter
    def polarization_type(self, value:"PolarizationType") -> None:
        """Get or set the polarization type"""
        return self._intf.set_property(ParametricBeamAntenna._metadata, ParametricBeamAntenna._set_polarization_type_metadata, value)

    _get_vertical_beamwidth_metadata = { "offset" : _get_vertical_beamwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def vertical_beamwidth(self) -> float:
        """Get or set the vertical beamwidth"""
        return self._intf.get_property(ParametricBeamAntenna._metadata, ParametricBeamAntenna._get_vertical_beamwidth_metadata)

    _set_vertical_beamwidth_metadata = { "offset" : _set_vertical_beamwidth_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @vertical_beamwidth.setter
    def vertical_beamwidth(self, value:float) -> None:
        """Get or set the vertical beamwidth"""
        return self._intf.set_property(ParametricBeamAntenna._metadata, ParametricBeamAntenna._set_vertical_beamwidth_metadata, value)

    _get_horizontal_beamwidth_metadata = { "offset" : _get_horizontal_beamwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def horizontal_beamwidth(self) -> float:
        """Get or set the horizontal beamwidth"""
        return self._intf.get_property(ParametricBeamAntenna._metadata, ParametricBeamAntenna._get_horizontal_beamwidth_metadata)

    _set_horizontal_beamwidth_metadata = { "offset" : _set_horizontal_beamwidth_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @horizontal_beamwidth.setter
    def horizontal_beamwidth(self, value:float) -> None:
        """Get or set the horizontal beamwidth"""
        return self._intf.set_property(ParametricBeamAntenna._metadata, ParametricBeamAntenna._set_horizontal_beamwidth_metadata, value)

    _property_names[polarization_type] = "polarization_type"
    _property_names[vertical_beamwidth] = "vertical_beamwidth"
    _property_names[horizontal_beamwidth] = "horizontal_beamwidth"

    def __init__(self, source_object=None):
        """Construct an object of type ParametricBeamAntenna."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ParametricBeamAntenna)
        IAntenna.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAntenna._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ParametricBeamAntenna, [ParametricBeamAntenna, IAntenna])

agcls.AgClassCatalog.add_catalog_entry((5608046540505248573, 11285439221430522042), ParametricBeamAntenna)
agcls.AgTypeNameMap["ParametricBeamAntenna"] = ParametricBeamAntenna

class ElementExportPatternAntenna(IAntenna, SupportsDeleteCallback):
    """Properties for an HFSS element export pattern (EEP) antenna model. This model accepts an EEP file which is exported from the Ansys HFSS software package."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_hfss_element_export_pattern_file_method_offset = 1
    _set_hfss_element_export_pattern_file_method_offset = 2
    _metadata = {
        "iid_data" : (5702957983798155509, 612537758527468167),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ElementExportPatternAntenna)

    _get_hfss_element_export_pattern_file_metadata = { "offset" : _get_hfss_element_export_pattern_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def hfss_element_export_pattern_file(self) -> str:
        """Get or set the HFSS element export pattern file."""
        return self._intf.get_property(ElementExportPatternAntenna._metadata, ElementExportPatternAntenna._get_hfss_element_export_pattern_file_metadata)

    _set_hfss_element_export_pattern_file_metadata = { "offset" : _set_hfss_element_export_pattern_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @hfss_element_export_pattern_file.setter
    def hfss_element_export_pattern_file(self, value:str) -> None:
        """Get or set the HFSS element export pattern file."""
        return self._intf.set_property(ElementExportPatternAntenna._metadata, ElementExportPatternAntenna._set_hfss_element_export_pattern_file_metadata, value)

    _property_names[hfss_element_export_pattern_file] = "hfss_element_export_pattern_file"

    def __init__(self, source_object=None):
        """Construct an object of type ElementExportPatternAntenna."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ElementExportPatternAntenna)
        IAntenna.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAntenna._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ElementExportPatternAntenna, [ElementExportPatternAntenna, IAntenna])

agcls.AgClassCatalog.add_catalog_entry((4622115852148269206, 14645709675013215925), ElementExportPatternAntenna)
agcls.AgTypeNameMap["ElementExportPatternAntenna"] = ElementExportPatternAntenna

class FarFieldDataPatternAntenna(IAntenna, SupportsDeleteCallback):
    """Properties for an HFSS far field data (FFD) antenna model. This model accepts an FFD file which is exported from the Ansys HFSS software package."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_hfss_far_field_data_pattern_file_method_offset = 1
    _set_hfss_far_field_data_pattern_file_method_offset = 2
    _metadata = {
        "iid_data" : (4766535495631233693, 4277778482148036535),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, FarFieldDataPatternAntenna)

    _get_hfss_far_field_data_pattern_file_metadata = { "offset" : _get_hfss_far_field_data_pattern_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def hfss_far_field_data_pattern_file(self) -> str:
        """Get or set the HFSS far field data pattern file."""
        return self._intf.get_property(FarFieldDataPatternAntenna._metadata, FarFieldDataPatternAntenna._get_hfss_far_field_data_pattern_file_metadata)

    _set_hfss_far_field_data_pattern_file_metadata = { "offset" : _set_hfss_far_field_data_pattern_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @hfss_far_field_data_pattern_file.setter
    def hfss_far_field_data_pattern_file(self, value:str) -> None:
        """Get or set the HFSS far field data pattern file."""
        return self._intf.set_property(FarFieldDataPatternAntenna._metadata, FarFieldDataPatternAntenna._set_hfss_far_field_data_pattern_file_metadata, value)

    _property_names[hfss_far_field_data_pattern_file] = "hfss_far_field_data_pattern_file"

    def __init__(self, source_object=None):
        """Construct an object of type FarFieldDataPatternAntenna."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, FarFieldDataPatternAntenna)
        IAntenna.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAntenna._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, FarFieldDataPatternAntenna, [FarFieldDataPatternAntenna, IAntenna])

agcls.AgClassCatalog.add_catalog_entry((5088999985869299634, 3360945610388407703), FarFieldDataPatternAntenna)
agcls.AgTypeNameMap["FarFieldDataPatternAntenna"] = FarFieldDataPatternAntenna

class Transceiver(SupportsDeleteCallback):
    """Properties for configuring a transceiver object."""

    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_identifier_method_offset = 1
    _get_name_method_offset = 2
    _set_name_method_offset = 3
    _get_parent_object_path_method_offset = 4
    _set_parent_object_path_method_offset = 5
    _get_central_body_name_method_offset = 6
    _get_model_method_offset = 7
    _metadata = {
        "iid_data" : (5344947488130358189, 3864536301493169838),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Transceiver)

    _get_identifier_metadata = { "offset" : _get_identifier_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def identifier(self) -> str:
        """Get the transceiver unique identifier."""
        return self._intf.get_property(Transceiver._metadata, Transceiver._get_identifier_metadata)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get or set the transceiver name."""
        return self._intf.get_property(Transceiver._metadata, Transceiver._get_name_metadata)

    _set_name_metadata = { "offset" : _set_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @name.setter
    def name(self, name:str) -> None:
        """Get or set the transceiver name."""
        return self._intf.set_property(Transceiver._metadata, Transceiver._set_name_metadata, name)

    _get_parent_object_path_metadata = { "offset" : _get_parent_object_path_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def parent_object_path(self) -> str:
        """Get or set the transceiver's parent object path."""
        return self._intf.get_property(Transceiver._metadata, Transceiver._get_parent_object_path_metadata)

    _set_parent_object_path_metadata = { "offset" : _set_parent_object_path_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @parent_object_path.setter
    def parent_object_path(self, parent_object:str) -> None:
        """Get or set the transceiver's parent object path."""
        return self._intf.set_property(Transceiver._metadata, Transceiver._set_parent_object_path_metadata, parent_object)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the tileset central body name."""
        return self._intf.get_property(Transceiver._metadata, Transceiver._get_central_body_name_metadata)

    _get_model_metadata = { "offset" : _get_model_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def model(self) -> "ITransceiverModel":
        """Get the transceiver model."""
        return self._intf.get_property(Transceiver._metadata, Transceiver._get_model_metadata)

    _property_names[identifier] = "identifier"
    _property_names[name] = "name"
    _property_names[parent_object_path] = "parent_object_path"
    _property_names[central_body_name] = "central_body_name"
    _property_names[model] = "model"

    def __init__(self, source_object=None):
        """Construct an object of type Transceiver."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Transceiver)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Transceiver, [Transceiver, ])

agcls.AgClassCatalog.add_catalog_entry((5764020437003561125, 11866983976314225332), Transceiver)
agcls.AgTypeNameMap["Transceiver"] = Transceiver

class CommunicationsTransceiverConfiguration(SupportsDeleteCallback):
    """Properties for a communication transceiver configuration. A transceiver configuration allows for changing the transceiver mode to one of three options, Transmit Only, Receive Only, or Transceive."""

    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_supported_transceivers_method_offset = 1
    _get_transceiver_method_offset = 2
    _set_transceiver_method_offset = 3
    _get_mode_method_offset = 4
    _set_mode_method_offset = 5
    _get_include_parent_object_facets_method_offset = 6
    _set_include_parent_object_facets_method_offset = 7
    _metadata = {
        "iid_data" : (5339551930090768236, 7774580073833889162),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, CommunicationsTransceiverConfiguration)

    _get_supported_transceivers_metadata = { "offset" : _get_supported_transceivers_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_transceivers(self) -> list:
        """Get an array of available transceiver instances."""
        return self._intf.get_property(CommunicationsTransceiverConfiguration._metadata, CommunicationsTransceiverConfiguration._get_supported_transceivers_metadata)

    _get_transceiver_metadata = { "offset" : _get_transceiver_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver(self) -> "Transceiver":
        """Get or set the transceiver."""
        return self._intf.get_property(CommunicationsTransceiverConfiguration._metadata, CommunicationsTransceiverConfiguration._get_transceiver_metadata)

    _set_transceiver_metadata = { "offset" : _set_transceiver_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"),) }
    @transceiver.setter
    def transceiver(self, transceiver:"Transceiver") -> None:
        """Get or set the transceiver."""
        return self._intf.set_property(CommunicationsTransceiverConfiguration._metadata, CommunicationsTransceiverConfiguration._set_transceiver_metadata, transceiver)

    _get_mode_metadata = { "offset" : _get_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(TransceiverMode),) }
    @property
    def mode(self) -> "TransceiverMode":
        """Get or set the transceiver mode."""
        return self._intf.get_property(CommunicationsTransceiverConfiguration._metadata, CommunicationsTransceiverConfiguration._get_mode_metadata)

    _set_mode_metadata = { "offset" : _set_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(TransceiverMode),) }
    @mode.setter
    def mode(self, value:"TransceiverMode") -> None:
        """Get or set the transceiver mode."""
        return self._intf.set_property(CommunicationsTransceiverConfiguration._metadata, CommunicationsTransceiverConfiguration._set_mode_metadata, value)

    _get_include_parent_object_facets_metadata = { "offset" : _get_include_parent_object_facets_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def include_parent_object_facets(self) -> bool:
        """Get or set an indicator of whether or not to include the parent object facets."""
        return self._intf.get_property(CommunicationsTransceiverConfiguration._metadata, CommunicationsTransceiverConfiguration._get_include_parent_object_facets_metadata)

    _set_include_parent_object_facets_metadata = { "offset" : _set_include_parent_object_facets_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @include_parent_object_facets.setter
    def include_parent_object_facets(self, value:bool) -> None:
        """Get or set an indicator of whether or not to include the parent object facets."""
        return self._intf.set_property(CommunicationsTransceiverConfiguration._metadata, CommunicationsTransceiverConfiguration._set_include_parent_object_facets_metadata, value)

    _property_names[supported_transceivers] = "supported_transceivers"
    _property_names[transceiver] = "transceiver"
    _property_names[mode] = "mode"
    _property_names[include_parent_object_facets] = "include_parent_object_facets"

    def __init__(self, source_object=None):
        """Construct an object of type CommunicationsTransceiverConfiguration."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, CommunicationsTransceiverConfiguration)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommunicationsTransceiverConfiguration, [CommunicationsTransceiverConfiguration, ])

agcls.AgClassCatalog.add_catalog_entry((4978837709042199279, 16007307245290930305), CommunicationsTransceiverConfiguration)
agcls.AgTypeNameMap["CommunicationsTransceiverConfiguration"] = CommunicationsTransceiverConfiguration

class RadarTransceiverConfiguration(SupportsDeleteCallback):
    """Properties for a radar transceiver configuration. A transceiver configuration allows for changing the transceiver mode to one of three options, Transmit Only, Receive Only, or Transceive."""

    _num_methods = 5
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_supported_transceivers_method_offset = 1
    _get_transceiver_method_offset = 2
    _set_transceiver_method_offset = 3
    _get_mode_method_offset = 4
    _set_mode_method_offset = 5
    _metadata = {
        "iid_data" : (4970430663528823873, 18390649212433641400),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarTransceiverConfiguration)

    _get_supported_transceivers_metadata = { "offset" : _get_supported_transceivers_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_transceivers(self) -> list:
        """Get an array of available transceiver instances."""
        return self._intf.get_property(RadarTransceiverConfiguration._metadata, RadarTransceiverConfiguration._get_supported_transceivers_metadata)

    _get_transceiver_metadata = { "offset" : _get_transceiver_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver(self) -> "Transceiver":
        """Get or set the transceiver."""
        return self._intf.get_property(RadarTransceiverConfiguration._metadata, RadarTransceiverConfiguration._get_transceiver_metadata)

    _set_transceiver_metadata = { "offset" : _set_transceiver_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"),) }
    @transceiver.setter
    def transceiver(self, transceiver:"Transceiver") -> None:
        """Get or set the transceiver."""
        return self._intf.set_property(RadarTransceiverConfiguration._metadata, RadarTransceiverConfiguration._set_transceiver_metadata, transceiver)

    _get_mode_metadata = { "offset" : _get_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(TransceiverMode),) }
    @property
    def mode(self) -> "TransceiverMode":
        """Get or set the transceiver mode."""
        return self._intf.get_property(RadarTransceiverConfiguration._metadata, RadarTransceiverConfiguration._get_mode_metadata)

    _set_mode_metadata = { "offset" : _set_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(TransceiverMode),) }
    @mode.setter
    def mode(self, value:"TransceiverMode") -> None:
        """Get or set the transceiver mode."""
        return self._intf.set_property(RadarTransceiverConfiguration._metadata, RadarTransceiverConfiguration._set_mode_metadata, value)

    _property_names[supported_transceivers] = "supported_transceivers"
    _property_names[transceiver] = "transceiver"
    _property_names[mode] = "mode"

    def __init__(self, source_object=None):
        """Construct an object of type RadarTransceiverConfiguration."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarTransceiverConfiguration)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarTransceiverConfiguration, [RadarTransceiverConfiguration, ])

agcls.AgClassCatalog.add_catalog_entry((4784738055343873436, 14125734708469202355), RadarTransceiverConfiguration)
agcls.AgTypeNameMap["RadarTransceiverConfiguration"] = RadarTransceiverConfiguration

class RadarImagingDataProductCollection(SupportsDeleteCallback):
    """Represents a collection of radar imaging data products."""

    _num_methods = 5
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _contains_method_offset = 4
    _find_by_identifier_method_offset = 5
    _metadata = {
        "iid_data" : (5088766265993511249, 12626778349551849876),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarImagingDataProductCollection)
    def __iter__(self):
        """Create an iterator for the RadarImagingDataProductCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "RadarImagingDataProduct":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(RadarImagingDataProductCollection._metadata, RadarImagingDataProductCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "RadarImagingDataProduct":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(RadarImagingDataProductCollection._metadata, RadarImagingDataProductCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(RadarImagingDataProductCollection._metadata, RadarImagingDataProductCollection._get__new_enum_metadata)

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def contains(self, identifier:str) -> bool:
        """Check to see if a imaging data product with given identifier exists in the collection."""
        return self._intf.invoke(RadarImagingDataProductCollection._metadata, RadarImagingDataProductCollection._contains_metadata, identifier, OutArg())

    _find_by_identifier_metadata = { "offset" : _find_by_identifier_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def find_by_identifier(self, identifier:str) -> "RadarImagingDataProduct":
        """Return the imaging data product in the collection with the supplied identifier or Null if not found or invalid."""
        return self._intf.invoke(RadarImagingDataProductCollection._metadata, RadarImagingDataProductCollection._find_by_identifier_metadata, identifier, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type RadarImagingDataProductCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarImagingDataProductCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarImagingDataProductCollection, [RadarImagingDataProductCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5427500380070641141, 1979161084254511271), RadarImagingDataProductCollection)
agcls.AgTypeNameMap["RadarImagingDataProductCollection"] = RadarImagingDataProductCollection

class RadarTransceiverConfigurationCollection(SupportsDeleteCallback):
    """Represents a collection of radar transceiver configurations."""

    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _remove_at_method_offset = 4
    _remove_method_offset = 5
    _add_new_method_offset = 6
    _remove_all_method_offset = 7
    _contains_method_offset = 8
    _metadata = {
        "iid_data" : (5695111455108751189, 11654867469952205963),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarTransceiverConfigurationCollection)
    def __iter__(self):
        """Create an iterator for the RadarTransceiverConfigurationCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "RadarTransceiverConfiguration":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(RadarTransceiverConfigurationCollection._metadata, RadarTransceiverConfigurationCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "RadarTransceiverConfiguration":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(RadarTransceiverConfigurationCollection._metadata, RadarTransceiverConfigurationCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(RadarTransceiverConfigurationCollection._metadata, RadarTransceiverConfigurationCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the configuration with the supplied index."""
        return self._intf.invoke(RadarTransceiverConfigurationCollection._metadata, RadarTransceiverConfigurationCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"),) }
    def remove(self, transceiver:"Transceiver") -> None:
        """Remove the supplied transceiver from the collection."""
        return self._intf.invoke(RadarTransceiverConfigurationCollection._metadata, RadarTransceiverConfigurationCollection._remove_metadata, transceiver)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def add_new(self) -> "RadarTransceiverConfiguration":
        """Add and returns a new configuration."""
        return self._intf.invoke(RadarTransceiverConfigurationCollection._metadata, RadarTransceiverConfigurationCollection._add_new_metadata, OutArg())

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all configurations from the collection."""
        return self._intf.invoke(RadarTransceiverConfigurationCollection._metadata, RadarTransceiverConfigurationCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"), agmarshall.VariantBoolArg,) }
    def contains(self, transceiver:"Transceiver") -> bool:
        """Check to see if a given configuration exists in the collection."""
        return self._intf.invoke(RadarTransceiverConfigurationCollection._metadata, RadarTransceiverConfigurationCollection._contains_metadata, transceiver, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type RadarTransceiverConfigurationCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarTransceiverConfigurationCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarTransceiverConfigurationCollection, [RadarTransceiverConfigurationCollection, ])

agcls.AgClassCatalog.add_catalog_entry((4714051373887209245, 7488076708093085605), RadarTransceiverConfigurationCollection)
agcls.AgTypeNameMap["RadarTransceiverConfigurationCollection"] = RadarTransceiverConfigurationCollection

class AnalysisConfiguration(SupportsDeleteCallback):
    """Properties of a configuration for an analysis."""

    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_name_method_offset = 1
    _set_name_method_offset = 2
    _get_description_method_offset = 3
    _set_description_method_offset = 4
    _get_supported_central_bodies_method_offset = 5
    _get_central_body_name_method_offset = 6
    _set_central_body_name_method_offset = 7
    _get_model_method_offset = 8
    _metadata = {
        "iid_data" : (5248807055816840987, 5379050123730892468),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, AnalysisConfiguration)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get or set the configuration name."""
        return self._intf.get_property(AnalysisConfiguration._metadata, AnalysisConfiguration._get_name_metadata)

    _set_name_metadata = { "offset" : _set_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @name.setter
    def name(self, name:str) -> None:
        """Get or set the configuration name."""
        return self._intf.set_property(AnalysisConfiguration._metadata, AnalysisConfiguration._set_name_metadata, name)

    _get_description_metadata = { "offset" : _get_description_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def description(self) -> str:
        """Get or set the configuration description."""
        return self._intf.get_property(AnalysisConfiguration._metadata, AnalysisConfiguration._get_description_metadata)

    _set_description_metadata = { "offset" : _set_description_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @description.setter
    def description(self, description:str) -> None:
        """Get or set the configuration description."""
        return self._intf.set_property(AnalysisConfiguration._metadata, AnalysisConfiguration._set_description_metadata, description)

    _get_supported_central_bodies_metadata = { "offset" : _get_supported_central_bodies_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_central_bodies(self) -> list:
        """Get an array of available central bodies."""
        return self._intf.get_property(AnalysisConfiguration._metadata, AnalysisConfiguration._get_supported_central_bodies_metadata)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the configured central body name."""
        return self._intf.get_property(AnalysisConfiguration._metadata, AnalysisConfiguration._get_central_body_name_metadata)

    _set_central_body_name_metadata = { "offset" : _set_central_body_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @central_body_name.setter
    def central_body_name(self, value:str) -> None:
        """Set the configured central body name."""
        return self._intf.set_property(AnalysisConfiguration._metadata, AnalysisConfiguration._set_central_body_name_metadata, value)

    _get_model_metadata = { "offset" : _get_model_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def model(self) -> "IAnalysisConfigurationModel":
        """Get the analysis configuration model."""
        return self._intf.get_property(AnalysisConfiguration._metadata, AnalysisConfiguration._get_model_metadata)

    _property_names[name] = "name"
    _property_names[description] = "description"
    _property_names[supported_central_bodies] = "supported_central_bodies"
    _property_names[central_body_name] = "central_body_name"
    _property_names[model] = "model"

    def __init__(self, source_object=None):
        """Construct an object of type AnalysisConfiguration."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, AnalysisConfiguration)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, AnalysisConfiguration, [AnalysisConfiguration, ])

agcls.AgClassCatalog.add_catalog_entry((5677711054846454801, 10373044160440040109), AnalysisConfiguration)
agcls.AgTypeNameMap["AnalysisConfiguration"] = AnalysisConfiguration

class CommunicationsAnalysisConfigurationModel(IAnalysisConfigurationModel, SupportsDeleteCallback):
    """Properties for an analysis configuration model for a communications analysis. This contains a collection of the transceiver configurations belonging to the communications analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_transceiver_configuration_collection_method_offset = 1
    _metadata = {
        "iid_data" : (5377579515007843975, 8243992647081021339),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, CommunicationsAnalysisConfigurationModel)

    _get_transceiver_configuration_collection_metadata = { "offset" : _get_transceiver_configuration_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver_configuration_collection(self) -> "CommunicationsTransceiverConfigurationCollection":
        """Get the collection of transceiver configurations."""
        return self._intf.get_property(CommunicationsAnalysisConfigurationModel._metadata, CommunicationsAnalysisConfigurationModel._get_transceiver_configuration_collection_metadata)

    _property_names[transceiver_configuration_collection] = "transceiver_configuration_collection"

    def __init__(self, source_object=None):
        """Construct an object of type CommunicationsAnalysisConfigurationModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, CommunicationsAnalysisConfigurationModel)
        IAnalysisConfigurationModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAnalysisConfigurationModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommunicationsAnalysisConfigurationModel, [CommunicationsAnalysisConfigurationModel, IAnalysisConfigurationModel])

agcls.AgClassCatalog.add_catalog_entry((5011550854218530883, 5141056899419203769), CommunicationsAnalysisConfigurationModel)
agcls.AgTypeNameMap["CommunicationsAnalysisConfigurationModel"] = CommunicationsAnalysisConfigurationModel

class RadarISarAnalysisConfigurationModel(IAnalysisConfigurationModel, IRadarAnalysisConfigurationModel, SupportsDeleteCallback):
    """The analysis configuration model for an ISar analysis. This contains a collection of the transceiver configurations belonging to the ISar analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_radar_target_collection_method_offset = 1
    _metadata = {
        "iid_data" : (5560239334934040690, 13238250037870844544),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarISarAnalysisConfigurationModel)

    _get_radar_target_collection_metadata = { "offset" : _get_radar_target_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def radar_target_collection(self) -> "ISceneContributorCollection":
        """Get the collection of radar targets."""
        return self._intf.get_property(RadarISarAnalysisConfigurationModel._metadata, RadarISarAnalysisConfigurationModel._get_radar_target_collection_metadata)

    _property_names[radar_target_collection] = "radar_target_collection"

    def __init__(self, source_object=None):
        """Construct an object of type RadarISarAnalysisConfigurationModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarISarAnalysisConfigurationModel)
        IAnalysisConfigurationModel.__init__(self, source_object)
        IRadarAnalysisConfigurationModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAnalysisConfigurationModel._private_init(self, intf)
        IRadarAnalysisConfigurationModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarISarAnalysisConfigurationModel, [RadarISarAnalysisConfigurationModel, IAnalysisConfigurationModel, IRadarAnalysisConfigurationModel])

agcls.AgClassCatalog.add_catalog_entry((5595337984047056268, 14286340175974646680), RadarISarAnalysisConfigurationModel)
agcls.AgTypeNameMap["RadarISarAnalysisConfigurationModel"] = RadarISarAnalysisConfigurationModel

class RadarSarAnalysisConfigurationModel(IAnalysisConfigurationModel, IRadarAnalysisConfigurationModel, SupportsDeleteCallback):
    """The analysis configuration model for a Sar analysis. This contains a collection of the transceiver configurations belonging to the Sar analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_image_location_collection_method_offset = 1
    _metadata = {
        "iid_data" : (5664266325122672211, 16093828039737084302),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarSarAnalysisConfigurationModel)

    _get_image_location_collection_metadata = { "offset" : _get_image_location_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def image_location_collection(self) -> "RadarSarImageLocationCollection":
        """Get the collection of image locations."""
        return self._intf.get_property(RadarSarAnalysisConfigurationModel._metadata, RadarSarAnalysisConfigurationModel._get_image_location_collection_metadata)

    _property_names[image_location_collection] = "image_location_collection"

    def __init__(self, source_object=None):
        """Construct an object of type RadarSarAnalysisConfigurationModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarSarAnalysisConfigurationModel)
        IAnalysisConfigurationModel.__init__(self, source_object)
        IRadarAnalysisConfigurationModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAnalysisConfigurationModel._private_init(self, intf)
        IRadarAnalysisConfigurationModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarSarAnalysisConfigurationModel, [RadarSarAnalysisConfigurationModel, IAnalysisConfigurationModel, IRadarAnalysisConfigurationModel])

agcls.AgClassCatalog.add_catalog_entry((4618872771739007313, 785458950983957423), RadarSarAnalysisConfigurationModel)
agcls.AgTypeNameMap["RadarSarAnalysisConfigurationModel"] = RadarSarAnalysisConfigurationModel

class TransceiverCollection(SupportsDeleteCallback):
    """Collection of transceiver objects."""

    _num_methods = 9
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _remove_at_method_offset = 4
    _remove_method_offset = 5
    _add_new_method_offset = 6
    _add_method_offset = 7
    _remove_all_method_offset = 8
    _find_by_identifier_method_offset = 9
    _metadata = {
        "iid_data" : (5066882531418439896, 6025038992297931663),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, TransceiverCollection)
    def __iter__(self):
        """Create an iterator for the TransceiverCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "Transceiver":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(TransceiverCollection._metadata, TransceiverCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "Transceiver":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(TransceiverCollection._metadata, TransceiverCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(TransceiverCollection._metadata, TransceiverCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the transceiver with the supplied index."""
        return self._intf.invoke(TransceiverCollection._metadata, TransceiverCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"),) }
    def remove(self, transceiver:"Transceiver") -> None:
        """Remove the supplied transceiver from the collection."""
        return self._intf.invoke(TransceiverCollection._metadata, TransceiverCollection._remove_metadata, transceiver)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (agcom.LONG, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(TransceiverModelType), agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def add_new(self, type:"TransceiverModelType", name:str, parent_object_path:str) -> "Transceiver":
        """Add and returns a new transceiver."""
        return self._intf.invoke(TransceiverCollection._metadata, TransceiverCollection._add_new_metadata, type, name, parent_object_path, OutArg())

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"),) }
    def add(self, value:"Transceiver") -> None:
        """Add the supplied transceiver to the collection."""
        return self._intf.invoke(TransceiverCollection._metadata, TransceiverCollection._add_metadata, value)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Remove all transceivers from the collection."""
        return self._intf.invoke(TransceiverCollection._metadata, TransceiverCollection._remove_all_metadata, )

    _find_by_identifier_metadata = { "offset" : _find_by_identifier_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def find_by_identifier(self, identifier:str) -> "Transceiver":
        """Return the transceiver in the collection with the supplied identifier or Null if not found or invalid."""
        return self._intf.invoke(TransceiverCollection._metadata, TransceiverCollection._find_by_identifier_metadata, identifier, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type TransceiverCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, TransceiverCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, TransceiverCollection, [TransceiverCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5054772411595164986, 13575262620310048164), TransceiverCollection)
agcls.AgTypeNameMap["TransceiverCollection"] = TransceiverCollection

class FacetTilesetCollection(SupportsDeleteCallback):
    """Represents a collection of facet tile sets."""

    _num_methods = 7
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _remove_method_offset = 4
    _remove_at_method_offset = 5
    _remove_all_method_offset = 6
    _add_method_offset = 7
    _metadata = {
        "iid_data" : (5345107458893416639, 1879233173021731765),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, FacetTilesetCollection)
    def __iter__(self):
        """Create an iterator for the FacetTilesetCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "FacetTileset":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(FacetTilesetCollection._metadata, FacetTilesetCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "FacetTileset":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(FacetTilesetCollection._metadata, FacetTilesetCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(FacetTilesetCollection._metadata, FacetTilesetCollection._get__new_enum_metadata)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("FacetTileset"),) }
    def remove(self, value:"FacetTileset") -> None:
        """Remove the supplied facet tileset from the collection."""
        return self._intf.invoke(FacetTilesetCollection._metadata, FacetTilesetCollection._remove_metadata, value)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the facet tileset with the supplied index."""
        return self._intf.invoke(FacetTilesetCollection._metadata, FacetTilesetCollection._remove_at_metadata, index)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all facet tilesets from the collection."""
        return self._intf.invoke(FacetTilesetCollection._metadata, FacetTilesetCollection._remove_all_metadata, )

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("FacetTileset"),) }
    def add(self, value:"FacetTileset") -> None:
        """Add a facet tile set to the collection."""
        return self._intf.invoke(FacetTilesetCollection._metadata, FacetTilesetCollection._add_metadata, value)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type FacetTilesetCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, FacetTilesetCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, FacetTilesetCollection, [FacetTilesetCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5241353233790358467, 31149073901229443), FacetTilesetCollection)
agcls.AgTypeNameMap["FacetTilesetCollection"] = FacetTilesetCollection

class SceneContributor(SupportsDeleteCallback):
    """Properties for a scene contributor object."""

    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_stk_object_path_method_offset = 1
    _set_stk_object_path_method_offset = 2
    _get_material_method_offset = 3
    _set_material_method_offset = 4
    _get_central_body_name_method_offset = 5
    _get_focused_ray_density_method_offset = 6
    _set_focused_ray_density_method_offset = 7
    _metadata = {
        "iid_data" : (5575428253904179354, 871515086261766274),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, SceneContributor)

    _get_stk_object_path_metadata = { "offset" : _get_stk_object_path_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def stk_object_path(self) -> str:
        """Get or set the scene contributor path."""
        return self._intf.get_property(SceneContributor._metadata, SceneContributor._get_stk_object_path_metadata)

    _set_stk_object_path_metadata = { "offset" : _set_stk_object_path_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @stk_object_path.setter
    def stk_object_path(self, stk_object_path:str) -> None:
        """Get or set the scene contributor path."""
        return self._intf.set_property(SceneContributor._metadata, SceneContributor._set_stk_object_path_metadata, stk_object_path)

    _get_material_metadata = { "offset" : _get_material_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def material(self) -> str:
        """Get or set the scene contributor material."""
        return self._intf.get_property(SceneContributor._metadata, SceneContributor._get_material_metadata)

    _set_material_metadata = { "offset" : _set_material_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @material.setter
    def material(self, value:str) -> None:
        """Get or set the scene contributor material."""
        return self._intf.set_property(SceneContributor._metadata, SceneContributor._set_material_metadata, value)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the tileset central body name."""
        return self._intf.get_property(SceneContributor._metadata, SceneContributor._get_central_body_name_metadata)

    _get_focused_ray_density_metadata = { "offset" : _get_focused_ray_density_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def focused_ray_density(self) -> float:
        """Get or set the target focused ray density."""
        return self._intf.get_property(SceneContributor._metadata, SceneContributor._get_focused_ray_density_metadata)

    _set_focused_ray_density_metadata = { "offset" : _set_focused_ray_density_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @focused_ray_density.setter
    def focused_ray_density(self, value:float) -> None:
        """Get or set the target focused ray density."""
        return self._intf.set_property(SceneContributor._metadata, SceneContributor._set_focused_ray_density_metadata, value)

    _property_names[stk_object_path] = "stk_object_path"
    _property_names[material] = "material"
    _property_names[central_body_name] = "central_body_name"
    _property_names[focused_ray_density] = "focused_ray_density"

    def __init__(self, source_object=None):
        """Construct an object of type SceneContributor."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, SceneContributor)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, SceneContributor, [SceneContributor, ])

agcls.AgClassCatalog.add_catalog_entry((5589375568961599488, 14409153256328659874), SceneContributor)
agcls.AgTypeNameMap["SceneContributor"] = SceneContributor

class SceneContributorCollection(ISceneContributorCollection, SupportsDeleteCallback):
    """A collection of scene contributor objects."""
    def __init__(self, source_object=None):
        """Construct an object of type SceneContributorCollection."""
        SupportsDeleteCallback.__init__(self)
        ISceneContributorCollection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        ISceneContributorCollection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, SceneContributorCollection, [ISceneContributorCollection])

agcls.AgClassCatalog.add_catalog_entry((5758395187433166913, 985915763780147333), SceneContributorCollection)
agcls.AgTypeNameMap["SceneContributorCollection"] = SceneContributorCollection

class RadarTargetCollection(ISceneContributorCollection, SupportsDeleteCallback):
    """A collection of radar target objects."""
    def __init__(self, source_object=None):
        """Construct an object of type RadarTargetCollection."""
        SupportsDeleteCallback.__init__(self)
        ISceneContributorCollection.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        ISceneContributorCollection._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarTargetCollection, [ISceneContributorCollection])

agcls.AgClassCatalog.add_catalog_entry((5205732992222383405, 4091993162712122275), RadarTargetCollection)
agcls.AgTypeNameMap["RadarTargetCollection"] = RadarTargetCollection

class RadarSarImageLocation(SupportsDeleteCallback):
    """Properties for an image location used by a range doppler Sar analysis."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_name_method_offset = 1
    _set_name_method_offset = 2
    _get_latitude_method_offset = 3
    _set_latitude_method_offset = 4
    _get_longitude_method_offset = 5
    _set_longitude_method_offset = 6
    _metadata = {
        "iid_data" : (5083014330116168059, 15940326948769439153),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarSarImageLocation)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get or set the image location name."""
        return self._intf.get_property(RadarSarImageLocation._metadata, RadarSarImageLocation._get_name_metadata)

    _set_name_metadata = { "offset" : _set_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @name.setter
    def name(self, value:str) -> None:
        """Get or set the image location name."""
        return self._intf.set_property(RadarSarImageLocation._metadata, RadarSarImageLocation._set_name_metadata, value)

    _get_latitude_metadata = { "offset" : _get_latitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def latitude(self) -> float:
        """Get or set the location latitude."""
        return self._intf.get_property(RadarSarImageLocation._metadata, RadarSarImageLocation._get_latitude_metadata)

    _set_latitude_metadata = { "offset" : _set_latitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @latitude.setter
    def latitude(self, value:float) -> None:
        """Get or set the location latitude."""
        return self._intf.set_property(RadarSarImageLocation._metadata, RadarSarImageLocation._set_latitude_metadata, value)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def longitude(self) -> float:
        """Get or set the location longitude."""
        return self._intf.get_property(RadarSarImageLocation._metadata, RadarSarImageLocation._get_longitude_metadata)

    _set_longitude_metadata = { "offset" : _set_longitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @longitude.setter
    def longitude(self, value:float) -> None:
        """Get or set the location longitude."""
        return self._intf.set_property(RadarSarImageLocation._metadata, RadarSarImageLocation._set_longitude_metadata, value)

    _property_names[name] = "name"
    _property_names[latitude] = "latitude"
    _property_names[longitude] = "longitude"

    def __init__(self, source_object=None):
        """Construct an object of type RadarSarImageLocation."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarSarImageLocation)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarSarImageLocation, [RadarSarImageLocation, ])

agcls.AgClassCatalog.add_catalog_entry((5268390739219090653, 5243515772457973653), RadarSarImageLocation)
agcls.AgTypeNameMap["RadarSarImageLocation"] = RadarSarImageLocation

class RadarSarImageLocationCollection(SupportsDeleteCallback):
    """Represents a collection of Sar image locations."""

    _num_methods = 9
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _remove_at_method_offset = 4
    _remove_method_offset = 5
    _add_new_method_offset = 6
    _remove_all_method_offset = 7
    _contains_method_offset = 8
    _find_method_offset = 9
    _metadata = {
        "iid_data" : (4764964873053444677, 13541437245688784278),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarSarImageLocationCollection)
    def __iter__(self):
        """Create an iterator for the RadarSarImageLocationCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "RadarSarImageLocation":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "RadarSarImageLocation":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the SAR image location with the supplied index."""
        return self._intf.invoke(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def remove(self, name_str:str) -> None:
        """Remove the supplied SAR image location from the collection."""
        return self._intf.invoke(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._remove_metadata, name_str)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def add_new(self) -> "RadarSarImageLocation":
        """Add and returns a new SAR image location."""
        return self._intf.invoke(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._add_new_metadata, OutArg())

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all SAR image locations from the collection."""
        return self._intf.invoke(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def contains(self, name_str:str) -> bool:
        """Check to see if a given SAR image location exists in the collection."""
        return self._intf.invoke(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._contains_metadata, name_str, OutArg())

    _find_metadata = { "offset" : _find_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def find(self, name_str:str) -> "RadarSarImageLocation":
        """Find a SAR image location by name. Returns Null if the image location name does not exist in the collection."""
        return self._intf.invoke(RadarSarImageLocationCollection._metadata, RadarSarImageLocationCollection._find_metadata, name_str, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type RadarSarImageLocationCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarSarImageLocationCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarSarImageLocationCollection, [RadarSarImageLocationCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5685305254463026309, 8912470404726757004), RadarSarImageLocationCollection)
agcls.AgTypeNameMap["RadarSarImageLocationCollection"] = RadarSarImageLocationCollection

class CommunicationsTransceiverConfigurationCollection(SupportsDeleteCallback):
    """Represents a collection of communication transceiver configurations."""

    _num_methods = 8
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _remove_at_method_offset = 4
    _remove_method_offset = 5
    _add_new_method_offset = 6
    _remove_all_method_offset = 7
    _contains_method_offset = 8
    _metadata = {
        "iid_data" : (5345775547056167751, 16252874551860572851),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, CommunicationsTransceiverConfigurationCollection)
    def __iter__(self):
        """Create an iterator for the CommunicationsTransceiverConfigurationCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "CommunicationsTransceiverConfiguration":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(CommunicationsTransceiverConfigurationCollection._metadata, CommunicationsTransceiverConfigurationCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "CommunicationsTransceiverConfiguration":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(CommunicationsTransceiverConfigurationCollection._metadata, CommunicationsTransceiverConfigurationCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(CommunicationsTransceiverConfigurationCollection._metadata, CommunicationsTransceiverConfigurationCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the configuration with the supplied index."""
        return self._intf.invoke(CommunicationsTransceiverConfigurationCollection._metadata, CommunicationsTransceiverConfigurationCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"),) }
    def remove(self, transceiver:"Transceiver") -> None:
        """Remove the supplied configuration from the collection."""
        return self._intf.invoke(CommunicationsTransceiverConfigurationCollection._metadata, CommunicationsTransceiverConfigurationCollection._remove_metadata, transceiver)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def add_new(self) -> "CommunicationsTransceiverConfiguration":
        """Add and returns a new configuration."""
        return self._intf.invoke(CommunicationsTransceiverConfigurationCollection._metadata, CommunicationsTransceiverConfigurationCollection._add_new_metadata, OutArg())

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all configurations from the collection."""
        return self._intf.invoke(CommunicationsTransceiverConfigurationCollection._metadata, CommunicationsTransceiverConfigurationCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"), agmarshall.VariantBoolArg,) }
    def contains(self, transceiver:"Transceiver") -> bool:
        """Check to see if a given configuration exists in the collection."""
        return self._intf.invoke(CommunicationsTransceiverConfigurationCollection._metadata, CommunicationsTransceiverConfigurationCollection._contains_metadata, transceiver, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type CommunicationsTransceiverConfigurationCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, CommunicationsTransceiverConfigurationCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommunicationsTransceiverConfigurationCollection, [CommunicationsTransceiverConfigurationCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5303350899362741451, 15194854434690147218), CommunicationsTransceiverConfigurationCollection)
agcls.AgTypeNameMap["CommunicationsTransceiverConfigurationCollection"] = CommunicationsTransceiverConfigurationCollection

class AnalysisConfigurationCollection(SupportsDeleteCallback):
    """Represents a collection of analysis configurations."""

    _num_methods = 10
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _remove_at_method_offset = 4
    _remove_method_offset = 5
    _add_new_method_offset = 6
    _add_method_offset = 7
    _remove_all_method_offset = 8
    _contains_method_offset = 9
    _find_method_offset = 10
    _metadata = {
        "iid_data" : (5139223614838802727, 10699109125304608912),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, AnalysisConfigurationCollection)
    def __iter__(self):
        """Create an iterator for the AnalysisConfigurationCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "AnalysisConfiguration":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "AnalysisConfiguration":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the analysis configuration at the supplied index."""
        return self._intf.invoke(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("AnalysisConfiguration"),) }
    def remove(self, value:"AnalysisConfiguration") -> None:
        """Remove the supplied analysis configuration."""
        return self._intf.invoke(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._remove_metadata, value)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (agcom.LONG, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(AnalysisConfigurationModelType), agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def add_new(self, model_type:"AnalysisConfigurationModelType", configuration_name:str) -> "AnalysisConfiguration":
        """Add and returns a new analysis configuration."""
        return self._intf.invoke(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._add_new_metadata, model_type, configuration_name, OutArg())

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("AnalysisConfiguration"),) }
    def add(self, value:"AnalysisConfiguration") -> None:
        """Add the supplied analysis configuration."""
        return self._intf.invoke(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._add_metadata, value)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear the collection."""
        return self._intf.invoke(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def contains(self, configuration_name:str) -> bool:
        """Determine if the collection contains an analysis configuration with the given name."""
        return self._intf.invoke(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._contains_metadata, configuration_name, OutArg())

    _find_metadata = { "offset" : _find_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def find(self, configuration_name:str) -> "AnalysisConfiguration":
        """Find an analysis configuration by name. Returns Null if the configuration name does not exist in the collection."""
        return self._intf.invoke(AnalysisConfigurationCollection._metadata, AnalysisConfigurationCollection._find_metadata, configuration_name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type AnalysisConfigurationCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, AnalysisConfigurationCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, AnalysisConfigurationCollection, [AnalysisConfigurationCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5108384052532699175, 9239904611326260382), AnalysisConfigurationCollection)
agcls.AgTypeNameMap["AnalysisConfigurationCollection"] = AnalysisConfigurationCollection

class ComputeOptions(SupportsDeleteCallback):
    """Properties for solver advanced compute options."""

    _num_methods = 14
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_ray_density_method_offset = 1
    _set_ray_density_method_offset = 2
    _get_geometrical_optics_blockage_method_offset = 3
    _set_geometrical_optics_blockage_method_offset = 4
    _get_geometrical_optics_blockage_starting_bounce_method_offset = 5
    _set_geometrical_optics_blockage_starting_bounce_method_offset = 6
    _get_maximum_reflections_method_offset = 7
    _set_maximum_reflections_method_offset = 8
    _get_maximum_transmissions_method_offset = 9
    _set_maximum_transmissions_method_offset = 10
    _get_bounding_box_mode_method_offset = 11
    _set_bounding_box_mode_method_offset = 12
    _get_bounding_box_side_length_method_offset = 13
    _set_bounding_box_side_length_method_offset = 14
    _metadata = {
        "iid_data" : (5319721960260637185, 7309251030269011901),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, ComputeOptions)

    _get_ray_density_metadata = { "offset" : _get_ray_density_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def ray_density(self) -> float:
        """Get or set the ray density."""
        return self._intf.get_property(ComputeOptions._metadata, ComputeOptions._get_ray_density_metadata)

    _set_ray_density_metadata = { "offset" : _set_ray_density_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @ray_density.setter
    def ray_density(self, value:float) -> None:
        """Get or set the ray density"""
        return self._intf.set_property(ComputeOptions._metadata, ComputeOptions._set_ray_density_metadata, value)

    _get_geometrical_optics_blockage_metadata = { "offset" : _get_geometrical_optics_blockage_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def geometrical_optics_blockage(self) -> bool:
        """Get or set the geometrical optics blockage."""
        return self._intf.get_property(ComputeOptions._metadata, ComputeOptions._get_geometrical_optics_blockage_metadata)

    _set_geometrical_optics_blockage_metadata = { "offset" : _set_geometrical_optics_blockage_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @geometrical_optics_blockage.setter
    def geometrical_optics_blockage(self, value:bool) -> None:
        """Get or set the geometrical optics blockage."""
        return self._intf.set_property(ComputeOptions._metadata, ComputeOptions._set_geometrical_optics_blockage_metadata, value)

    _get_geometrical_optics_blockage_starting_bounce_metadata = { "offset" : _get_geometrical_optics_blockage_starting_bounce_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def geometrical_optics_blockage_starting_bounce(self) -> int:
        """Get or set the geometrical optics blockage starting bounce."""
        return self._intf.get_property(ComputeOptions._metadata, ComputeOptions._get_geometrical_optics_blockage_starting_bounce_metadata)

    _set_geometrical_optics_blockage_starting_bounce_metadata = { "offset" : _set_geometrical_optics_blockage_starting_bounce_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @geometrical_optics_blockage_starting_bounce.setter
    def geometrical_optics_blockage_starting_bounce(self, value:int) -> None:
        """Get or set the geometrical optics blockage starting bounce."""
        return self._intf.set_property(ComputeOptions._metadata, ComputeOptions._set_geometrical_optics_blockage_starting_bounce_metadata, value)

    _get_maximum_reflections_metadata = { "offset" : _get_maximum_reflections_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def maximum_reflections(self) -> int:
        """Get or set the maximum number of reflections."""
        return self._intf.get_property(ComputeOptions._metadata, ComputeOptions._get_maximum_reflections_metadata)

    _set_maximum_reflections_metadata = { "offset" : _set_maximum_reflections_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @maximum_reflections.setter
    def maximum_reflections(self, value:int) -> None:
        """Get or set the maximum number of reflections."""
        return self._intf.set_property(ComputeOptions._metadata, ComputeOptions._set_maximum_reflections_metadata, value)

    _get_maximum_transmissions_metadata = { "offset" : _get_maximum_transmissions_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def maximum_transmissions(self) -> int:
        """Get or set the maximum number of transmissions."""
        return self._intf.get_property(ComputeOptions._metadata, ComputeOptions._get_maximum_transmissions_metadata)

    _set_maximum_transmissions_metadata = { "offset" : _set_maximum_transmissions_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @maximum_transmissions.setter
    def maximum_transmissions(self, value:int) -> None:
        """Get or set the maximum number of transmissions."""
        return self._intf.set_property(ComputeOptions._metadata, ComputeOptions._set_maximum_transmissions_metadata, value)

    _get_bounding_box_mode_metadata = { "offset" : _get_bounding_box_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(AnalysisSolverBoundingBoxMode),) }
    @property
    def bounding_box_mode(self) -> "AnalysisSolverBoundingBoxMode":
        """Get or set the bounding box."""
        return self._intf.get_property(ComputeOptions._metadata, ComputeOptions._get_bounding_box_mode_metadata)

    _set_bounding_box_mode_metadata = { "offset" : _set_bounding_box_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(AnalysisSolverBoundingBoxMode),) }
    @bounding_box_mode.setter
    def bounding_box_mode(self, value:"AnalysisSolverBoundingBoxMode") -> None:
        """Get or set the bounding box."""
        return self._intf.set_property(ComputeOptions._metadata, ComputeOptions._set_bounding_box_mode_metadata, value)

    _get_bounding_box_side_length_metadata = { "offset" : _get_bounding_box_side_length_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def bounding_box_side_length(self) -> float:
        """Get or set the bounding box side length."""
        return self._intf.get_property(ComputeOptions._metadata, ComputeOptions._get_bounding_box_side_length_metadata)

    _set_bounding_box_side_length_metadata = { "offset" : _set_bounding_box_side_length_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @bounding_box_side_length.setter
    def bounding_box_side_length(self, value:float) -> None:
        """Get or set the bounding box side length"""
        return self._intf.set_property(ComputeOptions._metadata, ComputeOptions._set_bounding_box_side_length_metadata, value)

    _property_names[ray_density] = "ray_density"
    _property_names[geometrical_optics_blockage] = "geometrical_optics_blockage"
    _property_names[geometrical_optics_blockage_starting_bounce] = "geometrical_optics_blockage_starting_bounce"
    _property_names[maximum_reflections] = "maximum_reflections"
    _property_names[maximum_transmissions] = "maximum_transmissions"
    _property_names[bounding_box_mode] = "bounding_box_mode"
    _property_names[bounding_box_side_length] = "bounding_box_side_length"

    def __init__(self, source_object=None):
        """Construct an object of type ComputeOptions."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, ComputeOptions)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, ComputeOptions, [ComputeOptions, ])

agcls.AgClassCatalog.add_catalog_entry((4766697304710355048, 11020176142052091815), ComputeOptions)
agcls.AgTypeNameMap["ComputeOptions"] = ComputeOptions

class STKRFChannelModeler(SupportsDeleteCallback):
    """Properties of the main RF Channel Modeler object."""

    _num_methods = 11
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_transceiver_collection_method_offset = 1
    _get_analysis_configuration_collection_method_offset = 2
    _duplicate_transceiver_method_offset = 3
    _duplicate_analysis_configuration_method_offset = 4
    _get_supported_materials_method_offset = 5
    _get_default_materials_method_offset = 6
    _get_compute_options_method_offset = 7
    _get_supported_gpu_properties_list_method_offset = 8
    _set_gpu_devices_method_offset = 9
    _construct_analysis_method_offset = 10
    _validate_analysis_method_offset = 11
    _metadata = {
        "iid_data" : (5482733239574373466, 18166728626667036302),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, STKRFChannelModeler)

    _get_transceiver_collection_metadata = { "offset" : _get_transceiver_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver_collection(self) -> "TransceiverCollection":
        """Get the collection of transceiver objects."""
        return self._intf.get_property(STKRFChannelModeler._metadata, STKRFChannelModeler._get_transceiver_collection_metadata)

    _get_analysis_configuration_collection_metadata = { "offset" : _get_analysis_configuration_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def analysis_configuration_collection(self) -> "AnalysisConfigurationCollection":
        """Get the collection of analysis configurations."""
        return self._intf.get_property(STKRFChannelModeler._metadata, STKRFChannelModeler._get_analysis_configuration_collection_metadata)

    _duplicate_transceiver_metadata = { "offset" : _duplicate_transceiver_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("Transceiver"), agmarshall.InterfaceOutArg,) }
    def duplicate_transceiver(self, transceiver:"Transceiver") -> "Transceiver":
        """Duplicates a transceiver instance."""
        return self._intf.invoke(STKRFChannelModeler._metadata, STKRFChannelModeler._duplicate_transceiver_metadata, transceiver, OutArg())

    _duplicate_analysis_configuration_metadata = { "offset" : _duplicate_analysis_configuration_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("AnalysisConfiguration"), agmarshall.InterfaceOutArg,) }
    def duplicate_analysis_configuration(self, analysis_configuration:"AnalysisConfiguration") -> "AnalysisConfiguration":
        """Duplicates an analysis configuration instance."""
        return self._intf.invoke(STKRFChannelModeler._metadata, STKRFChannelModeler._duplicate_analysis_configuration_metadata, analysis_configuration, OutArg())

    _get_supported_materials_metadata = { "offset" : _get_supported_materials_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_materials(self) -> list:
        """Get the supported tileset materials"""
        return self._intf.get_property(STKRFChannelModeler._metadata, STKRFChannelModeler._get_supported_materials_metadata)

    _get_default_materials_metadata = { "offset" : _get_default_materials_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def default_materials(self) -> list:
        """Get the default tileset materials"""
        return self._intf.get_property(STKRFChannelModeler._metadata, STKRFChannelModeler._get_default_materials_metadata)

    _get_compute_options_metadata = { "offset" : _get_compute_options_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def compute_options(self) -> "ComputeOptions":
        """Get the compute options."""
        return self._intf.get_property(STKRFChannelModeler._metadata, STKRFChannelModeler._get_compute_options_metadata)

    _get_supported_gpu_properties_list_metadata = { "offset" : _get_supported_gpu_properties_list_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_gpu_properties_list(self) -> list:
        """Get the GPU properties list."""
        return self._intf.get_property(STKRFChannelModeler._metadata, STKRFChannelModeler._get_supported_gpu_properties_list_metadata)

    _set_gpu_devices_metadata = { "offset" : _set_gpu_devices_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def set_gpu_devices(self, gpu_device_ids:list) -> None:
        """Set the desired GPU device IDs"""
        return self._intf.invoke(STKRFChannelModeler._metadata, STKRFChannelModeler._set_gpu_devices_metadata, gpu_device_ids)

    _construct_analysis_metadata = { "offset" : _construct_analysis_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def construct_analysis(self, analysis_configuration_name:str) -> "Analysis":
        """Construct an Analysis for an analysis configuration."""
        return self._intf.invoke(STKRFChannelModeler._metadata, STKRFChannelModeler._construct_analysis_metadata, analysis_configuration_name, OutArg())

    _validate_analysis_metadata = { "offset" : _validate_analysis_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def validate_analysis(self, analysis_configuration_name:str) -> "ValidationResponse":
        """Validate an analysis configuration."""
        return self._intf.invoke(STKRFChannelModeler._metadata, STKRFChannelModeler._validate_analysis_metadata, analysis_configuration_name, OutArg())

    _property_names[transceiver_collection] = "transceiver_collection"
    _property_names[analysis_configuration_collection] = "analysis_configuration_collection"
    _property_names[supported_materials] = "supported_materials"
    _property_names[default_materials] = "default_materials"
    _property_names[compute_options] = "compute_options"
    _property_names[supported_gpu_properties_list] = "supported_gpu_properties_list"

    def __init__(self, source_object=None):
        """Construct an object of type STKRFChannelModeler."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, STKRFChannelModeler)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, STKRFChannelModeler, [STKRFChannelModeler, ])

agcls.AgClassCatalog.add_catalog_entry((5114857258521425339, 16799304675451814790), STKRFChannelModeler)
agcls.AgTypeNameMap["STKRFChannelModeler"] = STKRFChannelModeler

class CommunicationsTransceiverModel(ITransceiverModel, SupportsDeleteCallback):
    """Properties for configuring a communications transceiver model."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_waveform_method_offset = 1
    _metadata = {
        "iid_data" : (4807723900367125848, 14400719289172710809),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, CommunicationsTransceiverModel)

    _get_waveform_metadata = { "offset" : _get_waveform_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def waveform(self) -> "CommunicationsWaveform":
        """Get the transceiver's waveform settings."""
        return self._intf.get_property(CommunicationsTransceiverModel._metadata, CommunicationsTransceiverModel._get_waveform_metadata)

    _property_names[waveform] = "waveform"

    def __init__(self, source_object=None):
        """Construct an object of type CommunicationsTransceiverModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, CommunicationsTransceiverModel)
        ITransceiverModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        ITransceiverModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, CommunicationsTransceiverModel, [CommunicationsTransceiverModel, ITransceiverModel])

agcls.AgClassCatalog.add_catalog_entry((5700000732757610746, 9267747997565531836), CommunicationsTransceiverModel)
agcls.AgTypeNameMap["CommunicationsTransceiverModel"] = CommunicationsTransceiverModel

class RadarTransceiverModel(ITransceiverModel, SupportsDeleteCallback):
    """Properties for configuring a radar transceiver model."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_waveform_method_offset = 1
    _metadata = {
        "iid_data" : (5172686738002011084, 2528836882571932832),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarTransceiverModel)

    _get_waveform_metadata = { "offset" : _get_waveform_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def waveform(self) -> "RadarWaveform":
        """Get the radar transceiver's waveform settings."""
        return self._intf.get_property(RadarTransceiverModel._metadata, RadarTransceiverModel._get_waveform_metadata)

    _property_names[waveform] = "waveform"

    def __init__(self, source_object=None):
        """Construct an object of type RadarTransceiverModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarTransceiverModel)
        ITransceiverModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        ITransceiverModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarTransceiverModel, [RadarTransceiverModel, ITransceiverModel])

agcls.AgClassCatalog.add_catalog_entry((5243014444346680384, 17762784428435053729), RadarTransceiverModel)
agcls.AgTypeNameMap["RadarTransceiverModel"] = RadarTransceiverModel

class RangeDopplerResponse(IResponse, SupportsDeleteCallback):
    """The properties for a range doppler channel characterization response."""

    _num_methods = 7
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_range_values_method_offset = 1
    _get_range_count_method_offset = 2
    _get_velocity_values_method_offset = 3
    _get_velocity_count_method_offset = 4
    _get_pulse_count_method_offset = 5
    _get_angular_velocity_method_offset = 6
    _get_data_dimensions_method_offset = 7
    _metadata = {
        "iid_data" : (4775466745073477908, 4613390586284496029),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RangeDopplerResponse)

    _get_range_values_metadata = { "offset" : _get_range_values_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def range_values(self) -> list:
        """Get the range values."""
        return self._intf.get_property(RangeDopplerResponse._metadata, RangeDopplerResponse._get_range_values_metadata)

    _get_range_count_metadata = { "offset" : _get_range_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def range_count(self) -> int:
        """Get the range count."""
        return self._intf.get_property(RangeDopplerResponse._metadata, RangeDopplerResponse._get_range_count_metadata)

    _get_velocity_values_metadata = { "offset" : _get_velocity_values_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def velocity_values(self) -> list:
        """Get the velocity values."""
        return self._intf.get_property(RangeDopplerResponse._metadata, RangeDopplerResponse._get_velocity_values_metadata)

    _get_velocity_count_metadata = { "offset" : _get_velocity_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def velocity_count(self) -> int:
        """Get the velocity count."""
        return self._intf.get_property(RangeDopplerResponse._metadata, RangeDopplerResponse._get_velocity_count_metadata)

    _get_pulse_count_metadata = { "offset" : _get_pulse_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def pulse_count(self) -> int:
        """Get the pulse count."""
        return self._intf.get_property(RangeDopplerResponse._metadata, RangeDopplerResponse._get_pulse_count_metadata)

    _get_angular_velocity_metadata = { "offset" : _get_angular_velocity_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def angular_velocity(self) -> float:
        """Get the angular velocity."""
        return self._intf.get_property(RangeDopplerResponse._metadata, RangeDopplerResponse._get_angular_velocity_metadata)

    _get_data_dimensions_metadata = { "offset" : _get_data_dimensions_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def data_dimensions(self) -> list:
        """Get the dimensions of the data. The dimensions are ordered in {Transmit Antenna Count, Receive Antenna Count, Velocity Count, Range Count, Complex Number (imaginary and real)}."""
        return self._intf.get_property(RangeDopplerResponse._metadata, RangeDopplerResponse._get_data_dimensions_metadata)

    _property_names[range_values] = "range_values"
    _property_names[range_count] = "range_count"
    _property_names[velocity_values] = "velocity_values"
    _property_names[velocity_count] = "velocity_count"
    _property_names[pulse_count] = "pulse_count"
    _property_names[angular_velocity] = "angular_velocity"
    _property_names[data_dimensions] = "data_dimensions"

    def __init__(self, source_object=None):
        """Construct an object of type RangeDopplerResponse."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RangeDopplerResponse)
        IResponse.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IResponse._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RangeDopplerResponse, [RangeDopplerResponse, IResponse])

agcls.AgClassCatalog.add_catalog_entry((5632652412576303983, 13971576127268070073), RangeDopplerResponse)
agcls.AgTypeNameMap["RangeDopplerResponse"] = RangeDopplerResponse

class FrequencyPulseResponse(IResponse, SupportsDeleteCallback):
    """The properties for a frequency pulse channel characterization response."""

    _num_methods = 3
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_pulse_count_method_offset = 1
    _get_frequency_sample_count_method_offset = 2
    _get_data_dimensions_method_offset = 3
    _metadata = {
        "iid_data" : (5691094288870661932, 6275219520155905449),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, FrequencyPulseResponse)

    _get_pulse_count_metadata = { "offset" : _get_pulse_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def pulse_count(self) -> int:
        """Get the pulse count."""
        return self._intf.get_property(FrequencyPulseResponse._metadata, FrequencyPulseResponse._get_pulse_count_metadata)

    _get_frequency_sample_count_metadata = { "offset" : _get_frequency_sample_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def frequency_sample_count(self) -> int:
        """Get the frequency sample count."""
        return self._intf.get_property(FrequencyPulseResponse._metadata, FrequencyPulseResponse._get_frequency_sample_count_metadata)

    _get_data_dimensions_metadata = { "offset" : _get_data_dimensions_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def data_dimensions(self) -> list:
        """Get the dimensions of the data. The dimensions are ordered in {Transmit Antenna Count, Receive Antenna Count, Pulse Count, Frequency Sample Count, Complex Number (imaginary and real)}."""
        return self._intf.get_property(FrequencyPulseResponse._metadata, FrequencyPulseResponse._get_data_dimensions_metadata)

    _property_names[pulse_count] = "pulse_count"
    _property_names[frequency_sample_count] = "frequency_sample_count"
    _property_names[data_dimensions] = "data_dimensions"

    def __init__(self, source_object=None):
        """Construct an object of type FrequencyPulseResponse."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, FrequencyPulseResponse)
        IResponse.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IResponse._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, FrequencyPulseResponse, [FrequencyPulseResponse, IResponse])

agcls.AgClassCatalog.add_catalog_entry((4861563049527470555, 17549780910734032023), FrequencyPulseResponse)
agcls.AgTypeNameMap["FrequencyPulseResponse"] = FrequencyPulseResponse

class AnalysisLink(IAnalysisLink, SupportsDeleteCallback):
    """A transceiver link for an analysis."""
    def __init__(self, source_object=None):
        """Construct an object of type AnalysisLink."""
        SupportsDeleteCallback.__init__(self)
        IAnalysisLink.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAnalysisLink._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, AnalysisLink, [IAnalysisLink])

agcls.AgClassCatalog.add_catalog_entry((5060158165662953403, 11836744488341586055), AnalysisLink)
agcls.AgTypeNameMap["AnalysisLink"] = AnalysisLink

class RadarSarAnalysisLink(IAnalysisLink, SupportsDeleteCallback):
    """Properties for a transceiver link for a Sar analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_image_location_name_method_offset = 1
    _metadata = {
        "iid_data" : (5021421490689678073, 8232694972196791714),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarSarAnalysisLink)

    _get_image_location_name_metadata = { "offset" : _get_image_location_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def image_location_name(self) -> str:
        """Get the analysis link image location name."""
        return self._intf.get_property(RadarSarAnalysisLink._metadata, RadarSarAnalysisLink._get_image_location_name_metadata)

    _property_names[image_location_name] = "image_location_name"

    def __init__(self, source_object=None):
        """Construct an object of type RadarSarAnalysisLink."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarSarAnalysisLink)
        IAnalysisLink.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAnalysisLink._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarSarAnalysisLink, [RadarSarAnalysisLink, IAnalysisLink])

agcls.AgClassCatalog.add_catalog_entry((4866171615548271834, 17813028962091228814), RadarSarAnalysisLink)
agcls.AgTypeNameMap["RadarSarAnalysisLink"] = RadarSarAnalysisLink

class RadarISarAnalysisLink(IAnalysisLink, SupportsDeleteCallback):
    """Properties for a transceiver link for an ISar analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_target_object_path_method_offset = 1
    _metadata = {
        "iid_data" : (5204187003231234038, 12438436543135854776),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, RadarISarAnalysisLink)

    _get_target_object_path_metadata = { "offset" : _get_target_object_path_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def target_object_path(self) -> str:
        """Get the analysis link target object path."""
        return self._intf.get_property(RadarISarAnalysisLink._metadata, RadarISarAnalysisLink._get_target_object_path_metadata)

    _property_names[target_object_path] = "target_object_path"

    def __init__(self, source_object=None):
        """Construct an object of type RadarISarAnalysisLink."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, RadarISarAnalysisLink)
        IAnalysisLink.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IAnalysisLink._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, RadarISarAnalysisLink, [RadarISarAnalysisLink, IAnalysisLink])

agcls.AgClassCatalog.add_catalog_entry((5007071857080535607, 5914757046513508527), RadarISarAnalysisLink)
agcls.AgTypeNameMap["RadarISarAnalysisLink"] = RadarISarAnalysisLink

class AnalysisLinkCollection(SupportsDeleteCallback):
    """Represents a collection of analysis links between transceivers objects."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _metadata = {
        "iid_data" : (5385625875110262874, 9943192813766780073),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, AnalysisLinkCollection)
    def __iter__(self):
        """Create an iterator for the AnalysisLinkCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IAnalysisLink":
        """Return the next element in the collection."""
        if self._enumerator is None:
            raise StopIteration
        nextval = self._enumerator.next()
        if nextval is None:
            raise StopIteration
        return nextval

    _get_count_metadata = { "offset" : _get_count_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.LongArg,) }
    @property
    def count(self) -> int:
        """Return the number of elements in the collection."""
        return self._intf.get_property(AnalysisLinkCollection._metadata, AnalysisLinkCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "IAnalysisLink":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(AnalysisLinkCollection._metadata, AnalysisLinkCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(AnalysisLinkCollection._metadata, AnalysisLinkCollection._get__new_enum_metadata)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type AnalysisLinkCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, AnalysisLinkCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, AnalysisLinkCollection, [AnalysisLinkCollection, ])

agcls.AgClassCatalog.add_catalog_entry((4920812217082674708, 3127837926356734904), AnalysisLinkCollection)
agcls.AgTypeNameMap["AnalysisLinkCollection"] = AnalysisLinkCollection

class Analysis(SupportsDeleteCallback):
    """Properties of an analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_analysis_link_collection_method_offset = 1
    _metadata = {
        "iid_data" : (5680527335101181193, 5726398768767138459),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, Analysis)

    _get_analysis_link_collection_metadata = { "offset" : _get_analysis_link_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def analysis_link_collection(self) -> "AnalysisLinkCollection":
        """Get the analysis link collection."""
        return self._intf.get_property(Analysis._metadata, Analysis._get_analysis_link_collection_metadata)

    _property_names[analysis_link_collection] = "analysis_link_collection"

    def __init__(self, source_object=None):
        """Construct an object of type Analysis."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, Analysis)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, Analysis, [Analysis, ])

agcls.AgClassCatalog.add_catalog_entry((5490184404645219457, 12664048901702803107), Analysis)
agcls.AgTypeNameMap["Analysis"] = Analysis

class GpuProperties(SupportsDeleteCallback):
    """Properties of a GPU that pertain to RF Channel Modeler."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_name_method_offset = 1
    _get_compute_capability_method_offset = 2
    _get_device_id_method_offset = 3
    _get_processor_count_method_offset = 4
    _get_speed_mhz_method_offset = 5
    _get_memory_gb_method_offset = 6
    _metadata = {
        "iid_data" : (4687254183925427724, 1328639251241963677),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, GpuProperties)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the GPU name."""
        return self._intf.get_property(GpuProperties._metadata, GpuProperties._get_name_metadata)

    _get_compute_capability_metadata = { "offset" : _get_compute_capability_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def compute_capability(self) -> str:
        """Get the GPU compute capability."""
        return self._intf.get_property(GpuProperties._metadata, GpuProperties._get_compute_capability_metadata)

    _get_device_id_metadata = { "offset" : _get_device_id_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def device_id(self) -> int:
        """Get the GPU device ID."""
        return self._intf.get_property(GpuProperties._metadata, GpuProperties._get_device_id_metadata)

    _get_processor_count_metadata = { "offset" : _get_processor_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def processor_count(self) -> int:
        """Get the GPU processor count."""
        return self._intf.get_property(GpuProperties._metadata, GpuProperties._get_processor_count_metadata)

    _get_speed_mhz_metadata = { "offset" : _get_speed_mhz_method_offset,
            "arg_types" : (POINTER(agcom.FLOAT),),
            "marshallers" : (agmarshall.FloatArg,) }
    @property
    def speed_mhz(self) -> float:
        """Get the GPU speed in MHz."""
        return self._intf.get_property(GpuProperties._metadata, GpuProperties._get_speed_mhz_metadata)

    _get_memory_gb_metadata = { "offset" : _get_memory_gb_method_offset,
            "arg_types" : (POINTER(agcom.FLOAT),),
            "marshallers" : (agmarshall.FloatArg,) }
    @property
    def memory_gb(self) -> float:
        """Get the GPU memory in GB."""
        return self._intf.get_property(GpuProperties._metadata, GpuProperties._get_memory_gb_metadata)

    _property_names[name] = "name"
    _property_names[compute_capability] = "compute_capability"
    _property_names[device_id] = "device_id"
    _property_names[processor_count] = "processor_count"
    _property_names[speed_mhz] = "speed_mhz"
    _property_names[memory_gb] = "memory_gb"

    def __init__(self, source_object=None):
        """Construct an object of type GpuProperties."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, GpuProperties)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, GpuProperties, [GpuProperties, ])

agcls.AgClassCatalog.add_catalog_entry((4703832968121801901, 9915671482244684202), GpuProperties)
agcls.AgTypeNameMap["GpuProperties"] = GpuProperties