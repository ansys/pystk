################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################ 

"""Object Model components specifically designed to support STK RF Channel Modeler."""

__all__ = ["IStkRfcmAnalysisConfigurationModel", "IStkRfcmAnalysisLink", "IStkRfcmAntenna", "IStkRfcmProgressTrackCancel", 
"IStkRfcmRadarAnalysisConfigurationModel", "IStkRfcmResponse", "IStkRfcmSceneContributor", "IStkRfcmTransceiverModel", "RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE", 
"RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE", "RFCM_ANALYSIS_RESULTS_FILE_MODE", "RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE", "RFCM_ANALYSIS_SUBTYPE", 
"RFCM_ANALYSIS_TYPE", "RFCM_CHANNEL_RESPONSE_TYPE", "RFCM_IMAGE_WINDOW_TYPE", "RFCM_POLARIZATION_TYPE", "RFCM_TRANSCEIVER_MODE", 
"RFCM_TRANSCEIVER_MODEL_TYPE", "StkRFChannelModeler", "StkRfcmAnalysis", "StkRfcmAnalysisConfiguration", "StkRfcmAnalysisConfigurationCollection", 
"StkRfcmAnalysisLink", "StkRfcmAnalysisLinkCollection", "StkRfcmCommunicationsAnalysisConfigurationModel", "StkRfcmCommunicationsTransceiverConfiguration", 
"StkRfcmCommunicationsTransceiverConfigurationCollection", "StkRfcmCommunicationsTransceiverModel", "StkRfcmCommunicationsWaveform", 
"StkRfcmComputeOptions", "StkRfcmElementExportPatternAntenna", "StkRfcmExtent", "StkRfcmFacetTileset", "StkRfcmFacetTilesetCollection", 
"StkRfcmFarFieldDataPatternAntenna", "StkRfcmFrequencyPulseResponse", "StkRfcmGpuProperties", "StkRfcmMaterial", "StkRfcmParametricBeamAntenna", 
"StkRfcmRadarISarAnalysisConfigurationModel", "StkRfcmRadarISarAnalysisLink", "StkRfcmRadarImagingDataProduct", "StkRfcmRadarSarAnalysisConfigurationModel", 
"StkRfcmRadarSarAnalysisLink", "StkRfcmRadarSarImageLocation", "StkRfcmRadarSarImageLocationCollection", "StkRfcmRadarTarget", 
"StkRfcmRadarTargetCollection", "StkRfcmRadarTransceiverConfiguration", "StkRfcmRadarTransceiverConfigurationCollection", 
"StkRfcmRadarTransceiverModel", "StkRfcmRadarWaveform", "StkRfcmRangeDopplerResponse", "StkRfcmSceneContributor", "StkRfcmSceneContributorCollection", 
"StkRfcmTransceiver", "StkRfcmTransceiverCollection", "StkRfcmValidationResponse"]


from ctypes   import POINTER
from enum     import IntEnum

from ..internal  import comutil          as agcom
from ..internal  import coclassutil      as agcls
from ..internal  import marshall         as agmarshall
from ..internal.comutil     import IUnknown, IDispatch
from ..internal.apiutil     import (InterfaceProxy, EnumeratorProxy, OutArg, 
    initialize_from_source_object, get_interface_property, set_interface_attribute, 
    set_class_attribute, SupportsDeleteCallback)
from ..utilities.exceptions import STKRuntimeError


def _raise_uninitialized_error(*args):
    raise STKRuntimeError("Valid STK object model classes are returned from STK methods and should not be created independently.")

class RFCM_ANALYSIS_TYPE(IntEnum):
    """Analysis Type"""
   
    COMMUNICATIONS = 0
    """Communications"""
    RADAR = 1
    """Radar"""

RFCM_ANALYSIS_TYPE.COMMUNICATIONS.__doc__ = "Communications"
RFCM_ANALYSIS_TYPE.RADAR.__doc__ = "Radar"

agcls.AgTypeNameMap["RFCM_ANALYSIS_TYPE"] = RFCM_ANALYSIS_TYPE

class RFCM_ANALYSIS_SUBTYPE(IntEnum):
    """Analysis Subtype"""
   
    NONE = 0
    """None"""
    SAR = 1
    """SAR"""
    ISAR = 2
    """ISAR"""

RFCM_ANALYSIS_SUBTYPE.NONE.__doc__ = "None"
RFCM_ANALYSIS_SUBTYPE.SAR.__doc__ = "SAR"
RFCM_ANALYSIS_SUBTYPE.ISAR.__doc__ = "ISAR"

agcls.AgTypeNameMap["RFCM_ANALYSIS_SUBTYPE"] = RFCM_ANALYSIS_SUBTYPE

class RFCM_CHANNEL_RESPONSE_TYPE(IntEnum):
    """Channel Response Type"""
   
    FREQUENCY_PULSE = 0
    """Frequency-Pulse"""
    RANGE_DOPPLER = 1
    """Range-Doppler"""

RFCM_CHANNEL_RESPONSE_TYPE.FREQUENCY_PULSE.__doc__ = "Frequency-Pulse"
RFCM_CHANNEL_RESPONSE_TYPE.RANGE_DOPPLER.__doc__ = "Range-Doppler"

agcls.AgTypeNameMap["RFCM_CHANNEL_RESPONSE_TYPE"] = RFCM_CHANNEL_RESPONSE_TYPE

class RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE(IntEnum):
    """Analysis Configuration Model Type"""
   
    COMMUNICATIONS = 0
    """Communications"""
    RADAR_I_SAR = 1
    """Radar ISAR"""
    RADAR_SAR = 2
    """Radar SAR"""

RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE.COMMUNICATIONS.__doc__ = "Communications"
RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE.RADAR_I_SAR.__doc__ = "Radar ISAR"
RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE.RADAR_SAR.__doc__ = "Radar SAR"

agcls.AgTypeNameMap["RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE"] = RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE

class RFCM_TRANSCEIVER_MODE(IntEnum):
    """Transceiver Mode"""
   
    TRANSCEIVE = 0
    """Transceive"""
    TRANSMIT_ONLY = 1
    """Transmit Only"""
    RECEIVE_ONLY = 2
    """Receive Only"""

RFCM_TRANSCEIVER_MODE.TRANSCEIVE.__doc__ = "Transceive"
RFCM_TRANSCEIVER_MODE.TRANSMIT_ONLY.__doc__ = "Transmit Only"
RFCM_TRANSCEIVER_MODE.RECEIVE_ONLY.__doc__ = "Receive Only"

agcls.AgTypeNameMap["RFCM_TRANSCEIVER_MODE"] = RFCM_TRANSCEIVER_MODE

class RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE(IntEnum):
    """Analysis configuration compute step mode."""
   
    FIXED_STEP_SIZE = 0
    """Fixed Step size"""
    FIXED_STEP_COUNT = 1
    """Fixed Step count"""
    CONTINUOUS_CHANNEL_SOUNDINGS = 0
    """Continuous channel soundings"""

RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE.FIXED_STEP_SIZE.__doc__ = "Fixed Step size"
RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE.FIXED_STEP_COUNT.__doc__ = "Fixed Step count"
RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE.CONTINUOUS_CHANNEL_SOUNDINGS.__doc__ = "Continuous channel soundings"

agcls.AgTypeNameMap["RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE"] = RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE

class RFCM_ANALYSIS_RESULTS_FILE_MODE(IntEnum):
    """Analysis results file mode."""
   
    SINGLE_FILE = 0
    """Single file"""
    ONE_FILE_PER_LINK = 1
    """One file per link"""

RFCM_ANALYSIS_RESULTS_FILE_MODE.SINGLE_FILE.__doc__ = "Single file"
RFCM_ANALYSIS_RESULTS_FILE_MODE.ONE_FILE_PER_LINK.__doc__ = "One file per link"

agcls.AgTypeNameMap["RFCM_ANALYSIS_RESULTS_FILE_MODE"] = RFCM_ANALYSIS_RESULTS_FILE_MODE

class RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE(IntEnum):
    """Analysis solver bounding box mode."""
   
    DEFAULT = 0
    """Default"""
    FULL_SCENE = 1
    """Full Scene"""
    CUSTOM = 2
    """Custom"""

RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE.DEFAULT.__doc__ = "Default"
RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE.FULL_SCENE.__doc__ = "Full Scene"
RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE.CUSTOM.__doc__ = "Custom"

agcls.AgTypeNameMap["RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE"] = RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE

class RFCM_TRANSCEIVER_MODEL_TYPE(IntEnum):
    """Transceiver Model Type"""
   
    COMMUNICATIONS = 0
    """Communications"""
    RADAR = 1
    """Radar"""

RFCM_TRANSCEIVER_MODEL_TYPE.COMMUNICATIONS.__doc__ = "Communications"
RFCM_TRANSCEIVER_MODEL_TYPE.RADAR.__doc__ = "Radar"

agcls.AgTypeNameMap["RFCM_TRANSCEIVER_MODEL_TYPE"] = RFCM_TRANSCEIVER_MODEL_TYPE

class RFCM_POLARIZATION_TYPE(IntEnum):
    """Polarization Type"""
   
    VERTICAL = 0
    """Vertical"""
    HORIZONTAL = 1
    """Horizontal"""
    RHCP = 2
    """RHCP"""
    LHCP = 3
    """LHCP"""

RFCM_POLARIZATION_TYPE.VERTICAL.__doc__ = "Vertical"
RFCM_POLARIZATION_TYPE.HORIZONTAL.__doc__ = "Horizontal"
RFCM_POLARIZATION_TYPE.RHCP.__doc__ = "RHCP"
RFCM_POLARIZATION_TYPE.LHCP.__doc__ = "LHCP"

agcls.AgTypeNameMap["RFCM_POLARIZATION_TYPE"] = RFCM_POLARIZATION_TYPE

class RFCM_IMAGE_WINDOW_TYPE(IntEnum):
    """Polarization Type"""
   
    FLAT = 0
    """Flat"""
    HANN = 1
    """Hann"""
    HAMMING = 2
    """Hamming"""
    TAYLOR = 3
    """Taylor"""

RFCM_IMAGE_WINDOW_TYPE.FLAT.__doc__ = "Flat"
RFCM_IMAGE_WINDOW_TYPE.HANN.__doc__ = "Hann"
RFCM_IMAGE_WINDOW_TYPE.HAMMING.__doc__ = "Hamming"
RFCM_IMAGE_WINDOW_TYPE.TAYLOR.__doc__ = "Taylor"

agcls.AgTypeNameMap["RFCM_IMAGE_WINDOW_TYPE"] = RFCM_IMAGE_WINDOW_TYPE


class IStkRfcmProgressTrackCancel(object):
    """Control for progress tracker."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_cancel_requested_method_offset = 1
    _update_progress_method_offset = 2
    _metadata = {
        "iid_data" : (5390916084034846203, 17403183235954599586),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IStkRfcmProgressTrackCancel."""
        initialize_from_source_object(self, source_object, IStkRfcmProgressTrackCancel)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IStkRfcmProgressTrackCancel)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IStkRfcmProgressTrackCancel, None)
    
    _get_cancel_requested_metadata = { "offset" : _get_cancel_requested_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def cancel_requested(self) -> bool:
        """Get whether or not cancel was requested."""
        return self._intf.get_property(IStkRfcmProgressTrackCancel._metadata, IStkRfcmProgressTrackCancel._get_cancel_requested_metadata)

    _update_progress_metadata = { "offset" : _update_progress_method_offset,
            "arg_types" : (agcom.INT, agcom.BSTR,),
            "marshallers" : (agmarshall.IntArg, agmarshall.BStrArg,) }
    def update_progress(self, progress:int, message:str) -> None:
        """Update progress."""
        return self._intf.invoke(IStkRfcmProgressTrackCancel._metadata, IStkRfcmProgressTrackCancel._update_progress_metadata, progress, message)

    _property_names[cancel_requested] = "cancel_requested"


agcls.AgClassCatalog.add_catalog_entry((5390916084034846203, 17403183235954599586), IStkRfcmProgressTrackCancel)
agcls.AgTypeNameMap["IStkRfcmProgressTrackCancel"] = IStkRfcmProgressTrackCancel

class IStkRfcmAntenna(object):
    """Base interface for a transceiver antenna model."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _metadata = {
        "iid_data" : (5683541619882775739, 9487067282181233037),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IStkRfcmAntenna."""
        initialize_from_source_object(self, source_object, IStkRfcmAntenna)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IStkRfcmAntenna)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IStkRfcmAntenna, None)
    
    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def type(self) -> str:
        """Get the antenna type."""
        return self._intf.get_property(IStkRfcmAntenna._metadata, IStkRfcmAntenna._get_type_metadata)

    _property_names[type] = "type"


agcls.AgClassCatalog.add_catalog_entry((5683541619882775739, 9487067282181233037), IStkRfcmAntenna)
agcls.AgTypeNameMap["IStkRfcmAntenna"] = IStkRfcmAntenna

class IStkRfcmTransceiverModel(object):
    """Base interface which defines common properties for a transceiver model."""

    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _set_antenna_type_method_offset = 2
    _get_supported_antenna_types_method_offset = 3
    _get_antenna_method_offset = 4
    _metadata = {
        "iid_data" : (5260850364807721395, 1562001126796197285),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IStkRfcmTransceiverModel."""
        initialize_from_source_object(self, source_object, IStkRfcmTransceiverModel)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IStkRfcmTransceiverModel)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IStkRfcmTransceiverModel, None)
    
    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_TRANSCEIVER_MODEL_TYPE),) }
    @property
    def type(self) -> "RFCM_TRANSCEIVER_MODEL_TYPE":
        """Get the transceiver unique identifier."""
        return self._intf.get_property(IStkRfcmTransceiverModel._metadata, IStkRfcmTransceiverModel._get_type_metadata)

    _set_antenna_type_metadata = { "offset" : _set_antenna_type_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def set_antenna_type(self, antenna_type:str) -> None:
        """Set the transceiver's antenna type."""
        return self._intf.invoke(IStkRfcmTransceiverModel._metadata, IStkRfcmTransceiverModel._set_antenna_type_metadata, antenna_type)

    _get_supported_antenna_types_metadata = { "offset" : _get_supported_antenna_types_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_antenna_types(self) -> list:
        """Get the supported antenna types."""
        return self._intf.get_property(IStkRfcmTransceiverModel._metadata, IStkRfcmTransceiverModel._get_supported_antenna_types_metadata)

    _get_antenna_metadata = { "offset" : _get_antenna_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def antenna(self) -> "IStkRfcmAntenna":
        """Get the transceiver's antenna settings."""
        return self._intf.get_property(IStkRfcmTransceiverModel._metadata, IStkRfcmTransceiverModel._get_antenna_metadata)

    _property_names[type] = "type"
    _property_names[supported_antenna_types] = "supported_antenna_types"
    _property_names[antenna] = "antenna"


agcls.AgClassCatalog.add_catalog_entry((5260850364807721395, 1562001126796197285), IStkRfcmTransceiverModel)
agcls.AgTypeNameMap["IStkRfcmTransceiverModel"] = IStkRfcmTransceiverModel

class IStkRfcmSceneContributor(object):
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
        "iid_data" : (5289282663936466784, 6187411627788191675),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IStkRfcmSceneContributor."""
        initialize_from_source_object(self, source_object, IStkRfcmSceneContributor)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IStkRfcmSceneContributor)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IStkRfcmSceneContributor, None)
    
    _get_stk_object_path_metadata = { "offset" : _get_stk_object_path_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def stk_object_path(self) -> str:
        """Get or set the scene contributor path."""
        return self._intf.get_property(IStkRfcmSceneContributor._metadata, IStkRfcmSceneContributor._get_stk_object_path_metadata)

    _set_stk_object_path_metadata = { "offset" : _set_stk_object_path_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @stk_object_path.setter
    def stk_object_path(self, stk_object_path:str) -> None:
        """Get or set the scene contributor path."""
        return self._intf.set_property(IStkRfcmSceneContributor._metadata, IStkRfcmSceneContributor._set_stk_object_path_metadata, stk_object_path)

    _get_material_metadata = { "offset" : _get_material_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def material(self) -> str:
        """Get or set the scene contributor material."""
        return self._intf.get_property(IStkRfcmSceneContributor._metadata, IStkRfcmSceneContributor._get_material_metadata)

    _set_material_metadata = { "offset" : _set_material_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @material.setter
    def material(self, value:str) -> None:
        """Get or set the scene contributor material."""
        return self._intf.set_property(IStkRfcmSceneContributor._metadata, IStkRfcmSceneContributor._set_material_metadata, value)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the tileset central body name."""
        return self._intf.get_property(IStkRfcmSceneContributor._metadata, IStkRfcmSceneContributor._get_central_body_name_metadata)

    _get_focused_ray_density_metadata = { "offset" : _get_focused_ray_density_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def focused_ray_density(self) -> float:
        """Get or set the target focused ray density."""
        return self._intf.get_property(IStkRfcmSceneContributor._metadata, IStkRfcmSceneContributor._get_focused_ray_density_metadata)

    _set_focused_ray_density_metadata = { "offset" : _set_focused_ray_density_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @focused_ray_density.setter
    def focused_ray_density(self, value:float) -> None:
        """Get or set the target focused ray density."""
        return self._intf.set_property(IStkRfcmSceneContributor._metadata, IStkRfcmSceneContributor._set_focused_ray_density_metadata, value)

    _property_names[stk_object_path] = "stk_object_path"
    _property_names[material] = "material"
    _property_names[central_body_name] = "central_body_name"
    _property_names[focused_ray_density] = "focused_ray_density"


agcls.AgClassCatalog.add_catalog_entry((5289282663936466784, 6187411627788191675), IStkRfcmSceneContributor)
agcls.AgTypeNameMap["IStkRfcmSceneContributor"] = IStkRfcmSceneContributor

class IStkRfcmResponse(object):
    """Properties and data for a channel characaterization response."""

    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _get_data_method_offset = 2
    _get_transmit_antenna_count_method_offset = 3
    _get_receive_antenna_count_method_offset = 4
    _metadata = {
        "iid_data" : (5273345876967495470, 8911670956953360542),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IStkRfcmResponse."""
        initialize_from_source_object(self, source_object, IStkRfcmResponse)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IStkRfcmResponse)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IStkRfcmResponse, None)
    
    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_CHANNEL_RESPONSE_TYPE),) }
    @property
    def type(self) -> "RFCM_CHANNEL_RESPONSE_TYPE":
        """Get the response type."""
        return self._intf.get_property(IStkRfcmResponse._metadata, IStkRfcmResponse._get_type_metadata)

    _get_data_metadata = { "offset" : _get_data_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def data(self) -> list:
        """Get the response data."""
        return self._intf.get_property(IStkRfcmResponse._metadata, IStkRfcmResponse._get_data_metadata)

    _get_transmit_antenna_count_metadata = { "offset" : _get_transmit_antenna_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def transmit_antenna_count(self) -> int:
        """Get the transmit antenna count."""
        return self._intf.get_property(IStkRfcmResponse._metadata, IStkRfcmResponse._get_transmit_antenna_count_metadata)

    _get_receive_antenna_count_metadata = { "offset" : _get_receive_antenna_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def receive_antenna_count(self) -> int:
        """Get the receive antenna count."""
        return self._intf.get_property(IStkRfcmResponse._metadata, IStkRfcmResponse._get_receive_antenna_count_metadata)

    _property_names[type] = "type"
    _property_names[data] = "data"
    _property_names[transmit_antenna_count] = "transmit_antenna_count"
    _property_names[receive_antenna_count] = "receive_antenna_count"


agcls.AgClassCatalog.add_catalog_entry((5273345876967495470, 8911670956953360542), IStkRfcmResponse)
agcls.AgTypeNameMap["IStkRfcmResponse"] = IStkRfcmResponse

class IStkRfcmAnalysisLink(object):
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
        "iid_data" : (5200039314651946484, 7207498084283752120),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IStkRfcmAnalysisLink."""
        initialize_from_source_object(self, source_object, IStkRfcmAnalysisLink)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IStkRfcmAnalysisLink)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IStkRfcmAnalysisLink, None)
    
    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the analysis link name."""
        return self._intf.get_property(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._get_name_metadata)

    _get_transmit_transceiver_identifier_metadata = { "offset" : _get_transmit_transceiver_identifier_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def transmit_transceiver_identifier(self) -> str:
        """Get the transmit tranceiver identifier."""
        return self._intf.get_property(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._get_transmit_transceiver_identifier_metadata)

    _get_transmit_transceiver_name_metadata = { "offset" : _get_transmit_transceiver_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def transmit_transceiver_name(self) -> str:
        """Get the transmit tranceiver name."""
        return self._intf.get_property(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._get_transmit_transceiver_name_metadata)

    _get_receive_transceiver_identifier_metadata = { "offset" : _get_receive_transceiver_identifier_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def receive_transceiver_identifier(self) -> str:
        """Get the receive tranceiver identifier."""
        return self._intf.get_property(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._get_receive_transceiver_identifier_metadata)

    _get_receive_transceiver_name_metadata = { "offset" : _get_receive_transceiver_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def receive_transceiver_name(self) -> str:
        """Get the receive tranceiver name."""
        return self._intf.get_property(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._get_receive_transceiver_name_metadata)

    _get_transmit_antenna_count_metadata = { "offset" : _get_transmit_antenna_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def transmit_antenna_count(self) -> int:
        """Get the transmit antenna count."""
        return self._intf.get_property(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._get_transmit_antenna_count_metadata)

    _get_receive_antenna_count_metadata = { "offset" : _get_receive_antenna_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def receive_antenna_count(self) -> int:
        """Get the receive antenna count."""
        return self._intf.get_property(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._get_receive_antenna_count_metadata)

    _get_analysis_intervals_metadata = { "offset" : _get_analysis_intervals_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def analysis_intervals(self) -> list:
        """Get the analysis intervals array."""
        return self._intf.get_property(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._get_analysis_intervals_metadata)

    _compute_metadata = { "offset" : _compute_method_offset,
            "arg_types" : (agcom.DOUBLE, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.DoubleArg, agmarshall.InterfaceOutArg,) }
    def compute(self, time:float) -> "IStkRfcmResponse":
        """Compute the analysis link at the given time."""
        return self._intf.invoke(IStkRfcmAnalysisLink._metadata, IStkRfcmAnalysisLink._compute_metadata, time, OutArg())

    _property_names[name] = "name"
    _property_names[transmit_transceiver_identifier] = "transmit_transceiver_identifier"
    _property_names[transmit_transceiver_name] = "transmit_transceiver_name"
    _property_names[receive_transceiver_identifier] = "receive_transceiver_identifier"
    _property_names[receive_transceiver_name] = "receive_transceiver_name"
    _property_names[transmit_antenna_count] = "transmit_antenna_count"
    _property_names[receive_antenna_count] = "receive_antenna_count"
    _property_names[analysis_intervals] = "analysis_intervals"


agcls.AgClassCatalog.add_catalog_entry((5200039314651946484, 7207498084283752120), IStkRfcmAnalysisLink)
agcls.AgTypeNameMap["IStkRfcmAnalysisLink"] = IStkRfcmAnalysisLink

class IStkRfcmAnalysisConfigurationModel(object):
    """Base interface for all analysis configuration models."""

    _num_methods = 26
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
    _get_results_file_write_block_size_method_offset = 18
    _set_results_file_write_block_size_method_offset = 19
    _get_use_scenario_analysis_interval_method_offset = 20
    _set_use_scenario_analysis_interval_method_offset = 21
    _get_hide_incompatible_tilesets_method_offset = 22
    _set_hide_incompatible_tilesets_method_offset = 23
    _get_supported_facet_tilesets_method_offset = 24
    _get_facet_tileset_collection_method_offset = 25
    _get_analysis_extent_method_offset = 26
    _metadata = {
        "iid_data" : (5297348179628469644, 14335374035294896569),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IStkRfcmAnalysisConfigurationModel."""
        initialize_from_source_object(self, source_object, IStkRfcmAnalysisConfigurationModel)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IStkRfcmAnalysisConfigurationModel)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IStkRfcmAnalysisConfigurationModel, None)
    
    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE),) }
    @property
    def type(self) -> "RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE":
        """Get the analysis configuration model type."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_type_metadata)

    _get_scene_contributor_collection_metadata = { "offset" : _get_scene_contributor_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def scene_contributor_collection(self) -> "StkRfcmSceneContributorCollection":
        """Get the collection of scene contributors."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_scene_contributor_collection_metadata)

    _get_link_count_metadata = { "offset" : _get_link_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def link_count(self) -> int:
        """Get the link count."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_link_count_metadata)

    _get_validate_configuration_metadata = { "offset" : _get_validate_configuration_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def validate_configuration(self) -> "StkRfcmValidationResponse":
        """Validates whether or not the configuration is ready to run."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_validate_configuration_metadata)

    _get_validate_platform_facets_metadata = { "offset" : _get_validate_platform_facets_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def validate_platform_facets(self) -> "StkRfcmValidationResponse":
        """Validates the configuration platforms which provide facets are configured properly."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_validate_platform_facets_metadata)

    _get_interval_start_metadata = { "offset" : _get_interval_start_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def interval_start(self) -> float:
        """Get or set the interval start time."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_interval_start_metadata)

    _set_interval_start_metadata = { "offset" : _set_interval_start_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @interval_start.setter
    def interval_start(self, interval_start:float) -> None:
        """Get or set the interval start time."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_interval_start_metadata, interval_start)

    _get_interval_stop_metadata = { "offset" : _get_interval_stop_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def interval_stop(self) -> float:
        """Get or set the interval stop time."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_interval_stop_metadata)

    _set_interval_stop_metadata = { "offset" : _set_interval_stop_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @interval_stop.setter
    def interval_stop(self, interval_stop:float) -> None:
        """Get or set the interval stop time."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_interval_stop_metadata, interval_stop)

    _get_compute_step_mode_metadata = { "offset" : _get_compute_step_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE),) }
    @property
    def compute_step_mode(self) -> "RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE":
        """Get or set the compute step mode."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_compute_step_mode_metadata)

    _set_compute_step_mode_metadata = { "offset" : _set_compute_step_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE),) }
    @compute_step_mode.setter
    def compute_step_mode(self, compute_step_mode:"RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE") -> None:
        """Get or set the compute step mode."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_compute_step_mode_metadata, compute_step_mode)

    _get_fixed_step_count_metadata = { "offset" : _get_fixed_step_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def fixed_step_count(self) -> int:
        """Get or set the step count."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_fixed_step_count_metadata)

    _set_fixed_step_count_metadata = { "offset" : _set_fixed_step_count_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @fixed_step_count.setter
    def fixed_step_count(self, step_count:int) -> None:
        """Get or set the step count."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_fixed_step_count_metadata, step_count)

    _get_fixed_step_size_metadata = { "offset" : _get_fixed_step_size_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def fixed_step_size(self) -> float:
        """Get or set the step size."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_fixed_step_size_metadata)

    _set_fixed_step_size_metadata = { "offset" : _set_fixed_step_size_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @fixed_step_size.setter
    def fixed_step_size(self, step_size:float) -> None:
        """Get or set the step size."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_fixed_step_size_metadata, step_size)

    _get_results_file_mode_metadata = { "offset" : _get_results_file_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_ANALYSIS_RESULTS_FILE_MODE),) }
    @property
    def results_file_mode(self) -> "RFCM_ANALYSIS_RESULTS_FILE_MODE":
        """Get or set the results file mode."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_results_file_mode_metadata)

    _set_results_file_mode_metadata = { "offset" : _set_results_file_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(RFCM_ANALYSIS_RESULTS_FILE_MODE),) }
    @results_file_mode.setter
    def results_file_mode(self, value:"RFCM_ANALYSIS_RESULTS_FILE_MODE") -> None:
        """Get or set the results file mode."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_results_file_mode_metadata, value)

    _get_results_file_write_block_size_metadata = { "offset" : _get_results_file_write_block_size_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def results_file_write_block_size(self) -> int:
        """Get or set the results file write block size."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_results_file_write_block_size_metadata)

    _set_results_file_write_block_size_metadata = { "offset" : _set_results_file_write_block_size_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @results_file_write_block_size.setter
    def results_file_write_block_size(self, value:int) -> None:
        """Get or set the results file write block size."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_results_file_write_block_size_metadata, value)

    _get_use_scenario_analysis_interval_metadata = { "offset" : _get_use_scenario_analysis_interval_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def use_scenario_analysis_interval(self) -> bool:
        """Get or set whether or not to use the scenario analysis interval."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_use_scenario_analysis_interval_metadata)

    _set_use_scenario_analysis_interval_metadata = { "offset" : _set_use_scenario_analysis_interval_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @use_scenario_analysis_interval.setter
    def use_scenario_analysis_interval(self, value:bool) -> None:
        """Get or set whether or not to use the scenario analysis interval."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_use_scenario_analysis_interval_metadata, value)

    _get_hide_incompatible_tilesets_metadata = { "offset" : _get_hide_incompatible_tilesets_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def hide_incompatible_tilesets(self) -> bool:
        """Get or set the show all tilesets indicator."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_hide_incompatible_tilesets_metadata)

    _set_hide_incompatible_tilesets_metadata = { "offset" : _set_hide_incompatible_tilesets_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @hide_incompatible_tilesets.setter
    def hide_incompatible_tilesets(self, value:bool) -> None:
        """Get or set the show all tilesets indicator."""
        return self._intf.set_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._set_hide_incompatible_tilesets_metadata, value)

    _get_supported_facet_tilesets_metadata = { "offset" : _get_supported_facet_tilesets_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_facet_tilesets(self) -> list:
        """Get an array of available facet tilesets."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_supported_facet_tilesets_metadata)

    _get_facet_tileset_collection_metadata = { "offset" : _get_facet_tileset_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def facet_tileset_collection(self) -> "StkRfcmFacetTilesetCollection":
        """Get the collection of facet tilesets."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_facet_tileset_collection_metadata)

    _get_analysis_extent_metadata = { "offset" : _get_analysis_extent_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def analysis_extent(self) -> "StkRfcmExtent":
        """Get the facet tileset extent."""
        return self._intf.get_property(IStkRfcmAnalysisConfigurationModel._metadata, IStkRfcmAnalysisConfigurationModel._get_analysis_extent_metadata)

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
    _property_names[results_file_write_block_size] = "results_file_write_block_size"
    _property_names[use_scenario_analysis_interval] = "use_scenario_analysis_interval"
    _property_names[hide_incompatible_tilesets] = "hide_incompatible_tilesets"
    _property_names[supported_facet_tilesets] = "supported_facet_tilesets"
    _property_names[facet_tileset_collection] = "facet_tileset_collection"
    _property_names[analysis_extent] = "analysis_extent"


agcls.AgClassCatalog.add_catalog_entry((5297348179628469644, 14335374035294896569), IStkRfcmAnalysisConfigurationModel)
agcls.AgTypeNameMap["IStkRfcmAnalysisConfigurationModel"] = IStkRfcmAnalysisConfigurationModel

class IStkRfcmRadarAnalysisConfigurationModel(object):
    """Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis."""

    _num_methods = 3
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _duplicate_transceiver_configuration_method_offset = 1
    _get_transceiver_configuration_collection_method_offset = 2
    _get_imaging_data_product_list_method_offset = 3
    _metadata = {
        "iid_data" : (4635842407038885586, 5216845520973926036),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def __init__(self, source_object=None):
        """Construct an object of type IStkRfcmRadarAnalysisConfigurationModel."""
        initialize_from_source_object(self, source_object, IStkRfcmRadarAnalysisConfigurationModel)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def _get_property(self, attrname):
        return get_interface_property(attrname, IStkRfcmRadarAnalysisConfigurationModel)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_interface_attribute(self, attrname, value, IStkRfcmRadarAnalysisConfigurationModel, None)
    
    _duplicate_transceiver_configuration_metadata = { "offset" : _duplicate_transceiver_configuration_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmRadarTransceiverConfiguration"), agmarshall.InterfaceOutArg,) }
    def duplicate_transceiver_configuration(self, transceiver_configuration:"StkRfcmRadarTransceiverConfiguration") -> "StkRfcmRadarTransceiverConfiguration":
        """Duplicates a transceiver configuration instance."""
        return self._intf.invoke(IStkRfcmRadarAnalysisConfigurationModel._metadata, IStkRfcmRadarAnalysisConfigurationModel._duplicate_transceiver_configuration_metadata, transceiver_configuration, OutArg())

    _get_transceiver_configuration_collection_metadata = { "offset" : _get_transceiver_configuration_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver_configuration_collection(self) -> "StkRfcmRadarTransceiverConfigurationCollection":
        """Get the collection of transceiver configurations."""
        return self._intf.get_property(IStkRfcmRadarAnalysisConfigurationModel._metadata, IStkRfcmRadarAnalysisConfigurationModel._get_transceiver_configuration_collection_metadata)

    _get_imaging_data_product_list_metadata = { "offset" : _get_imaging_data_product_list_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def imaging_data_product_list(self) -> list:
        """Get the imaging product list."""
        return self._intf.get_property(IStkRfcmRadarAnalysisConfigurationModel._metadata, IStkRfcmRadarAnalysisConfigurationModel._get_imaging_data_product_list_metadata)

    _property_names[transceiver_configuration_collection] = "transceiver_configuration_collection"
    _property_names[imaging_data_product_list] = "imaging_data_product_list"


agcls.AgClassCatalog.add_catalog_entry((4635842407038885586, 5216845520973926036), IStkRfcmRadarAnalysisConfigurationModel)
agcls.AgTypeNameMap["IStkRfcmRadarAnalysisConfigurationModel"] = IStkRfcmRadarAnalysisConfigurationModel



class StkRfcmRadarImagingDataProduct(SupportsDeleteCallback):
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
    _get_enable_imaging_method_offset = 10
    _set_enable_imaging_method_offset = 11
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
        "iid_data" : (5142214519392837796, 6233112050034224043),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarImagingDataProduct)
    
    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the image product name."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_name_metadata)

    _get_enable_sensor_fixed_distance_metadata = { "offset" : _get_enable_sensor_fixed_distance_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def enable_sensor_fixed_distance(self) -> bool:
        """Enable or disables the fixed disatance mode."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_enable_sensor_fixed_distance_metadata)

    _set_enable_sensor_fixed_distance_metadata = { "offset" : _set_enable_sensor_fixed_distance_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @enable_sensor_fixed_distance.setter
    def enable_sensor_fixed_distance(self, value:bool) -> None:
        """Enable or disables the fixed disatance mode."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_enable_sensor_fixed_distance_metadata, value)

    _get_desired_sensor_fixed_distance_metadata = { "offset" : _get_desired_sensor_fixed_distance_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def desired_sensor_fixed_distance(self) -> float:
        """Get or set the fixed disatance."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_desired_sensor_fixed_distance_metadata)

    _set_desired_sensor_fixed_distance_metadata = { "offset" : _set_desired_sensor_fixed_distance_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @desired_sensor_fixed_distance.setter
    def desired_sensor_fixed_distance(self, value:float) -> None:
        """Get or set the fixed disatance."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_desired_sensor_fixed_distance_metadata, value)

    _get_distance_to_range_window_start_metadata = { "offset" : _get_distance_to_range_window_start_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def distance_to_range_window_start(self) -> float:
        """Get or set the distance to the range window start."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_distance_to_range_window_start_metadata)

    _get_distance_to_range_window_center_metadata = { "offset" : _get_distance_to_range_window_center_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def distance_to_range_window_center(self) -> float:
        """Get or set the distance to the range window center."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_distance_to_range_window_center_metadata)

    _get_center_image_in_range_window_metadata = { "offset" : _get_center_image_in_range_window_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def center_image_in_range_window(self) -> bool:
        """Enable or disables whether the image will be centered in the range window."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_center_image_in_range_window_metadata)

    _set_center_image_in_range_window_metadata = { "offset" : _set_center_image_in_range_window_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @center_image_in_range_window.setter
    def center_image_in_range_window(self, value:bool) -> None:
        """Enable or disables whether the image will be centered in the range window."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_center_image_in_range_window_metadata, value)

    _get_enable_imaging_metadata = { "offset" : _get_enable_imaging_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def enable_imaging(self) -> bool:
        """Enable radar imaging."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_enable_imaging_metadata)

    _set_enable_imaging_metadata = { "offset" : _set_enable_imaging_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @enable_imaging.setter
    def enable_imaging(self, value:bool) -> None:
        """Enable radar imaging."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_enable_imaging_metadata, value)

    _get_range_pixel_count_metadata = { "offset" : _get_range_pixel_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def range_pixel_count(self) -> int:
        """Get or set the range pixel count."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_range_pixel_count_metadata)

    _set_range_pixel_count_metadata = { "offset" : _set_range_pixel_count_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @range_pixel_count.setter
    def range_pixel_count(self, value:int) -> None:
        """Get or set the range pixel count."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_range_pixel_count_metadata, value)

    _get_velocity_pixel_count_metadata = { "offset" : _get_velocity_pixel_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def velocity_pixel_count(self) -> int:
        """Get or set the velocity pixel count."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_velocity_pixel_count_metadata)

    _set_velocity_pixel_count_metadata = { "offset" : _set_velocity_pixel_count_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @velocity_pixel_count.setter
    def velocity_pixel_count(self, value:int) -> None:
        """Get or set the velocity pixel count."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_velocity_pixel_count_metadata, value)

    _get_range_window_type_metadata = { "offset" : _get_range_window_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_IMAGE_WINDOW_TYPE),) }
    @property
    def range_window_type(self) -> "RFCM_IMAGE_WINDOW_TYPE":
        """Get or set the range window type."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_range_window_type_metadata)

    _set_range_window_type_metadata = { "offset" : _set_range_window_type_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(RFCM_IMAGE_WINDOW_TYPE),) }
    @range_window_type.setter
    def range_window_type(self, value:"RFCM_IMAGE_WINDOW_TYPE") -> None:
        """Get or set the range window type."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_range_window_type_metadata, value)

    _get_range_window_side_lobe_level_metadata = { "offset" : _get_range_window_side_lobe_level_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def range_window_side_lobe_level(self) -> float:
        """Get or set the range window side lobe level."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_range_window_side_lobe_level_metadata)

    _set_range_window_side_lobe_level_metadata = { "offset" : _set_range_window_side_lobe_level_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @range_window_side_lobe_level.setter
    def range_window_side_lobe_level(self, value:float) -> None:
        """Get or set the range window side lobe level."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_range_window_side_lobe_level_metadata, value)

    _get_velocity_window_type_metadata = { "offset" : _get_velocity_window_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_IMAGE_WINDOW_TYPE),) }
    @property
    def velocity_window_type(self) -> "RFCM_IMAGE_WINDOW_TYPE":
        """Get or set the velocity window type."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_velocity_window_type_metadata)

    _set_velocity_window_type_metadata = { "offset" : _set_velocity_window_type_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(RFCM_IMAGE_WINDOW_TYPE),) }
    @velocity_window_type.setter
    def velocity_window_type(self, value:"RFCM_IMAGE_WINDOW_TYPE") -> None:
        """Get or set the velocity window type."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_velocity_window_type_metadata, value)

    _get_velocity_window_side_lobe_level_metadata = { "offset" : _get_velocity_window_side_lobe_level_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def velocity_window_side_lobe_level(self) -> float:
        """Get or set the velocity window side lobe level."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_velocity_window_side_lobe_level_metadata)

    _set_velocity_window_side_lobe_level_metadata = { "offset" : _set_velocity_window_side_lobe_level_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @velocity_window_side_lobe_level.setter
    def velocity_window_side_lobe_level(self, value:float) -> None:
        """Get or set the velocity window side lobe level."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_velocity_window_side_lobe_level_metadata, value)

    _get_range_resolution_metadata = { "offset" : _get_range_resolution_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def range_resolution(self) -> float:
        """Get or set the range resolution."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_range_resolution_metadata)

    _set_range_resolution_metadata = { "offset" : _set_range_resolution_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @range_resolution.setter
    def range_resolution(self, value:float) -> None:
        """Get or set the range resolution."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_range_resolution_metadata, value)

    _get_range_window_size_metadata = { "offset" : _get_range_window_size_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def range_window_size(self) -> float:
        """Get or set the range window size."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_range_window_size_metadata)

    _set_range_window_size_metadata = { "offset" : _set_range_window_size_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @range_window_size.setter
    def range_window_size(self, value:float) -> None:
        """Get or set the range window size."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_range_window_size_metadata, value)

    _get_cross_range_resolution_metadata = { "offset" : _get_cross_range_resolution_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def cross_range_resolution(self) -> float:
        """Get or set the cross range resolution."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_cross_range_resolution_metadata)

    _set_cross_range_resolution_metadata = { "offset" : _set_cross_range_resolution_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @cross_range_resolution.setter
    def cross_range_resolution(self, value:float) -> None:
        """Get or set the cross range resolution."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_cross_range_resolution_metadata, value)

    _get_cross_range_window_size_metadata = { "offset" : _get_cross_range_window_size_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def cross_range_window_size(self) -> float:
        """Get or set the cross range window size."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_cross_range_window_size_metadata)

    _set_cross_range_window_size_metadata = { "offset" : _set_cross_range_window_size_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @cross_range_window_size.setter
    def cross_range_window_size(self, value:float) -> None:
        """Get or set the cross range window size."""
        return self._intf.set_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._set_cross_range_window_size_metadata, value)

    _get_required_bandwidth_metadata = { "offset" : _get_required_bandwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def required_bandwidth(self) -> float:
        """Get the waveform product's required bandwidth."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_required_bandwidth_metadata)

    _get_collection_angle_metadata = { "offset" : _get_collection_angle_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def collection_angle(self) -> float:
        """Get the waveform collection angle."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_collection_angle_metadata)

    _get_frequency_samples_per_pulse_metadata = { "offset" : _get_frequency_samples_per_pulse_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def frequency_samples_per_pulse(self) -> int:
        """Get the number of frequency samples per pulse."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_frequency_samples_per_pulse_metadata)

    _get_minimum_pulse_count_metadata = { "offset" : _get_minimum_pulse_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def minimum_pulse_count(self) -> int:
        """Get the minimum pulse count."""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_minimum_pulse_count_metadata)

    _get_identifier_metadata = { "offset" : _get_identifier_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def identifier(self) -> str:
        """Get the unique identifier for the data product"""
        return self._intf.get_property(StkRfcmRadarImagingDataProduct._metadata, StkRfcmRadarImagingDataProduct._get_identifier_metadata)

    _property_names[name] = "name"
    _property_names[enable_sensor_fixed_distance] = "enable_sensor_fixed_distance"
    _property_names[desired_sensor_fixed_distance] = "desired_sensor_fixed_distance"
    _property_names[distance_to_range_window_start] = "distance_to_range_window_start"
    _property_names[distance_to_range_window_center] = "distance_to_range_window_center"
    _property_names[center_image_in_range_window] = "center_image_in_range_window"
    _property_names[enable_imaging] = "enable_imaging"
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
        """Construct an object of type StkRfcmRadarImagingDataProduct."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarImagingDataProduct)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarImagingDataProduct, [StkRfcmRadarImagingDataProduct, ])

agcls.AgClassCatalog.add_catalog_entry((5074933986252676529, 8852701032538182291), StkRfcmRadarImagingDataProduct)
agcls.AgTypeNameMap["StkRfcmRadarImagingDataProduct"] = StkRfcmRadarImagingDataProduct

class StkRfcmMaterial(SupportsDeleteCallback):
    """Properties for a material."""

    _num_methods = 4
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_type_method_offset = 1
    _set_type_method_offset = 2
    _get_properties_method_offset = 3
    _set_properties_method_offset = 4
    _metadata = {
        "iid_data" : (5106970972732140092, 12345568409569237644),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmMaterial)
    
    _get_type_metadata = { "offset" : _get_type_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def type(self) -> str:
        """Get material type."""
        return self._intf.get_property(StkRfcmMaterial._metadata, StkRfcmMaterial._get_type_metadata)

    _set_type_metadata = { "offset" : _set_type_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @type.setter
    def type(self, value:str) -> None:
        """Set material type."""
        return self._intf.set_property(StkRfcmMaterial._metadata, StkRfcmMaterial._set_type_metadata, value)

    _get_properties_metadata = { "offset" : _get_properties_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def properties(self) -> str:
        """Get material properties."""
        return self._intf.get_property(StkRfcmMaterial._metadata, StkRfcmMaterial._get_properties_metadata)

    _set_properties_metadata = { "offset" : _set_properties_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @properties.setter
    def properties(self, value:str) -> None:
        """Set material properties."""
        return self._intf.set_property(StkRfcmMaterial._metadata, StkRfcmMaterial._set_properties_metadata, value)

    _property_names[type] = "type"
    _property_names[properties] = "properties"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmMaterial."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmMaterial)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmMaterial, [StkRfcmMaterial, ])

agcls.AgClassCatalog.add_catalog_entry((5585828003287260468, 16548653199708755882), StkRfcmMaterial)
agcls.AgTypeNameMap["StkRfcmMaterial"] = StkRfcmMaterial

class StkRfcmFacetTileset(SupportsDeleteCallback):
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
        "iid_data" : (4789527447108154914, 637873324861092488),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmFacetTileset)
    
    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the facet tileset name."""
        return self._intf.get_property(StkRfcmFacetTileset._metadata, StkRfcmFacetTileset._get_name_metadata)

    _get_uri_metadata = { "offset" : _get_uri_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def uri(self) -> str:
        """Get the facet tileset uri."""
        return self._intf.get_property(StkRfcmFacetTileset._metadata, StkRfcmFacetTileset._get_uri_metadata)

    _get_material_metadata = { "offset" : _get_material_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def material(self) -> str:
        """Get or set the tileset material."""
        return self._intf.get_property(StkRfcmFacetTileset._metadata, StkRfcmFacetTileset._get_material_metadata)

    _set_material_metadata = { "offset" : _set_material_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @material.setter
    def material(self, value:str) -> None:
        """Get or set the tileset material."""
        return self._intf.set_property(StkRfcmFacetTileset._metadata, StkRfcmFacetTileset._set_material_metadata, value)

    _get_reference_frame_metadata = { "offset" : _get_reference_frame_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def reference_frame(self) -> str:
        """Get the tileset reference frame."""
        return self._intf.get_property(StkRfcmFacetTileset._metadata, StkRfcmFacetTileset._get_reference_frame_metadata)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the tileset central body name."""
        return self._intf.get_property(StkRfcmFacetTileset._metadata, StkRfcmFacetTileset._get_central_body_name_metadata)

    _property_names[name] = "name"
    _property_names[uri] = "uri"
    _property_names[material] = "material"
    _property_names[reference_frame] = "reference_frame"
    _property_names[central_body_name] = "central_body_name"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmFacetTileset."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmFacetTileset)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmFacetTileset, [StkRfcmFacetTileset, ])

agcls.AgClassCatalog.add_catalog_entry((4888196436732093925, 11141857126072407213), StkRfcmFacetTileset)
agcls.AgTypeNameMap["StkRfcmFacetTileset"] = StkRfcmFacetTileset

class StkRfcmValidationResponse(SupportsDeleteCallback):
    """Properties of the response from validating an analysis configuration."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_value_method_offset = 1
    _get_message_method_offset = 2
    _metadata = {
        "iid_data" : (4994438691132779782, 1415141693988703135),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmValidationResponse)
    
    _get_value_metadata = { "offset" : _get_value_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def value(self) -> bool:
        """Get the validation indicator."""
        return self._intf.get_property(StkRfcmValidationResponse._metadata, StkRfcmValidationResponse._get_value_metadata)

    _get_message_metadata = { "offset" : _get_message_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def message(self) -> str:
        """Get the validation message."""
        return self._intf.get_property(StkRfcmValidationResponse._metadata, StkRfcmValidationResponse._get_message_metadata)

    _property_names[value] = "value"
    _property_names[message] = "message"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmValidationResponse."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmValidationResponse)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmValidationResponse, [StkRfcmValidationResponse, ])

agcls.AgClassCatalog.add_catalog_entry((4804640472049572896, 16088033728626929551), StkRfcmValidationResponse)
agcls.AgTypeNameMap["StkRfcmValidationResponse"] = StkRfcmValidationResponse

class StkRfcmExtent(SupportsDeleteCallback):
    """Properties for a cartographic extent definition. One use of this interface is for defining the facet tile set analysis extent."""

    _num_methods = 8
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_north_latitude_method_offset = 1
    _set_north_latitude_method_offset = 2
    _get_south_latitude_method_offset = 3
    _set_south_latitude_method_offset = 4
    _get_east_longitude_method_offset = 5
    _set_east_longitude_method_offset = 6
    _get_west_longitude_method_offset = 7
    _set_west_longitude_method_offset = 8
    _metadata = {
        "iid_data" : (4919157609295249505, 12211194950299458230),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmExtent)
    
    _get_north_latitude_metadata = { "offset" : _get_north_latitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def north_latitude(self) -> float:
        """Get or set the north latitude."""
        return self._intf.get_property(StkRfcmExtent._metadata, StkRfcmExtent._get_north_latitude_metadata)

    _set_north_latitude_metadata = { "offset" : _set_north_latitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @north_latitude.setter
    def north_latitude(self, value:float) -> None:
        """Get or set the north latitude."""
        return self._intf.set_property(StkRfcmExtent._metadata, StkRfcmExtent._set_north_latitude_metadata, value)

    _get_south_latitude_metadata = { "offset" : _get_south_latitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def south_latitude(self) -> float:
        """Get or set the south latitude."""
        return self._intf.get_property(StkRfcmExtent._metadata, StkRfcmExtent._get_south_latitude_metadata)

    _set_south_latitude_metadata = { "offset" : _set_south_latitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @south_latitude.setter
    def south_latitude(self, value:float) -> None:
        """Get or set the south latitude."""
        return self._intf.set_property(StkRfcmExtent._metadata, StkRfcmExtent._set_south_latitude_metadata, value)

    _get_east_longitude_metadata = { "offset" : _get_east_longitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def east_longitude(self) -> float:
        """Get or set the east longitude."""
        return self._intf.get_property(StkRfcmExtent._metadata, StkRfcmExtent._get_east_longitude_metadata)

    _set_east_longitude_metadata = { "offset" : _set_east_longitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @east_longitude.setter
    def east_longitude(self, value:float) -> None:
        """Get or set the east longitude."""
        return self._intf.set_property(StkRfcmExtent._metadata, StkRfcmExtent._set_east_longitude_metadata, value)

    _get_west_longitude_metadata = { "offset" : _get_west_longitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def west_longitude(self) -> float:
        """Get or set the west longitude."""
        return self._intf.get_property(StkRfcmExtent._metadata, StkRfcmExtent._get_west_longitude_metadata)

    _set_west_longitude_metadata = { "offset" : _set_west_longitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @west_longitude.setter
    def west_longitude(self, value:float) -> None:
        """Get or set the west longitude."""
        return self._intf.set_property(StkRfcmExtent._metadata, StkRfcmExtent._set_west_longitude_metadata, value)

    _property_names[north_latitude] = "north_latitude"
    _property_names[south_latitude] = "south_latitude"
    _property_names[east_longitude] = "east_longitude"
    _property_names[west_longitude] = "west_longitude"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmExtent."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmExtent)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmExtent, [StkRfcmExtent, ])

agcls.AgClassCatalog.add_catalog_entry((4900388743329603538, 7944534523141337986), StkRfcmExtent)
agcls.AgTypeNameMap["StkRfcmExtent"] = StkRfcmExtent

class StkRfcmCommunicationsWaveform(SupportsDeleteCallback):
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
        "iid_data" : (5073231083378675674, 13078442724957062319),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmCommunicationsWaveform)
    
    _get_frequency_samples_per_sounding_metadata = { "offset" : _get_frequency_samples_per_sounding_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def frequency_samples_per_sounding(self) -> int:
        """Get or set the waveform number of samples."""
        return self._intf.get_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._get_frequency_samples_per_sounding_metadata)

    _set_frequency_samples_per_sounding_metadata = { "offset" : _set_frequency_samples_per_sounding_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @frequency_samples_per_sounding.setter
    def frequency_samples_per_sounding(self, value:int) -> None:
        """Get or set the waveform number of samples."""
        return self._intf.set_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._set_frequency_samples_per_sounding_metadata, value)

    _get_channel_bandwidth_metadata = { "offset" : _get_channel_bandwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def channel_bandwidth(self) -> float:
        """Get or set the waveform bandwidth."""
        return self._intf.get_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._get_channel_bandwidth_metadata)

    _set_channel_bandwidth_metadata = { "offset" : _set_channel_bandwidth_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @channel_bandwidth.setter
    def channel_bandwidth(self, value:float) -> None:
        """Get or set the waveform bandwidth."""
        return self._intf.set_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._set_channel_bandwidth_metadata, value)

    _get_rf_channel_frequency_metadata = { "offset" : _get_rf_channel_frequency_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def rf_channel_frequency(self) -> float:
        """Get or set the waveform frequency."""
        return self._intf.get_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._get_rf_channel_frequency_metadata)

    _set_rf_channel_frequency_metadata = { "offset" : _set_rf_channel_frequency_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @rf_channel_frequency.setter
    def rf_channel_frequency(self, value:float) -> None:
        """Get or set the waveform frequency."""
        return self._intf.set_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._set_rf_channel_frequency_metadata, value)

    _get_sounding_interval_metadata = { "offset" : _get_sounding_interval_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def sounding_interval(self) -> float:
        """Get or set the waveform pulse interval."""
        return self._intf.get_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._get_sounding_interval_metadata)

    _set_sounding_interval_metadata = { "offset" : _set_sounding_interval_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @sounding_interval.setter
    def sounding_interval(self, value:float) -> None:
        """Get or set the waveform pulse interval."""
        return self._intf.set_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._set_sounding_interval_metadata, value)

    _get_soundings_per_analysis_time_step_metadata = { "offset" : _get_soundings_per_analysis_time_step_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def soundings_per_analysis_time_step(self) -> int:
        """Get or set the waveform number of pulses."""
        return self._intf.get_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._get_soundings_per_analysis_time_step_metadata)

    _set_soundings_per_analysis_time_step_metadata = { "offset" : _set_soundings_per_analysis_time_step_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @soundings_per_analysis_time_step.setter
    def soundings_per_analysis_time_step(self, value:int) -> None:
        """Get or set the waveform number of pulses."""
        return self._intf.set_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._set_soundings_per_analysis_time_step_metadata, value)

    _get_complete_simulation_interval_metadata = { "offset" : _get_complete_simulation_interval_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def complete_simulation_interval(self) -> float:
        """Get the complete simulation interval."""
        return self._intf.get_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._get_complete_simulation_interval_metadata)

    _get_unambiguous_channel_delay_metadata = { "offset" : _get_unambiguous_channel_delay_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def unambiguous_channel_delay(self) -> float:
        """Get the unambiguous channel delay."""
        return self._intf.get_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._get_unambiguous_channel_delay_metadata)

    _get_unambiguous_channel_distance_metadata = { "offset" : _get_unambiguous_channel_distance_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def unambiguous_channel_distance(self) -> float:
        """Get the unambiguous channel distance."""
        return self._intf.get_property(StkRfcmCommunicationsWaveform._metadata, StkRfcmCommunicationsWaveform._get_unambiguous_channel_distance_metadata)

    _property_names[frequency_samples_per_sounding] = "frequency_samples_per_sounding"
    _property_names[channel_bandwidth] = "channel_bandwidth"
    _property_names[rf_channel_frequency] = "rf_channel_frequency"
    _property_names[sounding_interval] = "sounding_interval"
    _property_names[soundings_per_analysis_time_step] = "soundings_per_analysis_time_step"
    _property_names[complete_simulation_interval] = "complete_simulation_interval"
    _property_names[unambiguous_channel_delay] = "unambiguous_channel_delay"
    _property_names[unambiguous_channel_distance] = "unambiguous_channel_distance"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmCommunicationsWaveform."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmCommunicationsWaveform)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmCommunicationsWaveform, [StkRfcmCommunicationsWaveform, ])

agcls.AgClassCatalog.add_catalog_entry((5578603191846218821, 13050805049586632106), StkRfcmCommunicationsWaveform)
agcls.AgTypeNameMap["StkRfcmCommunicationsWaveform"] = StkRfcmCommunicationsWaveform

class StkRfcmRadarWaveform(SupportsDeleteCallback):
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
        "iid_data" : (5372724197743564578, 12276101041325134501),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarWaveform)
    
    _get_rf_channel_frequency_metadata = { "offset" : _get_rf_channel_frequency_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def rf_channel_frequency(self) -> float:
        """Get or set the waveform frequency."""
        return self._intf.get_property(StkRfcmRadarWaveform._metadata, StkRfcmRadarWaveform._get_rf_channel_frequency_metadata)

    _set_rf_channel_frequency_metadata = { "offset" : _set_rf_channel_frequency_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @rf_channel_frequency.setter
    def rf_channel_frequency(self, value:float) -> None:
        """Get or set the waveform frequency."""
        return self._intf.set_property(StkRfcmRadarWaveform._metadata, StkRfcmRadarWaveform._set_rf_channel_frequency_metadata, value)

    _get_pulse_repetition_frequency_metadata = { "offset" : _get_pulse_repetition_frequency_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def pulse_repetition_frequency(self) -> float:
        """Get or set the pulse repetition frequency."""
        return self._intf.get_property(StkRfcmRadarWaveform._metadata, StkRfcmRadarWaveform._get_pulse_repetition_frequency_metadata)

    _set_pulse_repetition_frequency_metadata = { "offset" : _set_pulse_repetition_frequency_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @pulse_repetition_frequency.setter
    def pulse_repetition_frequency(self, value:float) -> None:
        """Get or set the pulse repetition frequency."""
        return self._intf.set_property(StkRfcmRadarWaveform._metadata, StkRfcmRadarWaveform._set_pulse_repetition_frequency_metadata, value)

    _get_bandwidth_metadata = { "offset" : _get_bandwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def bandwidth(self) -> float:
        """Get or set the waveform bandwidth."""
        return self._intf.get_property(StkRfcmRadarWaveform._metadata, StkRfcmRadarWaveform._get_bandwidth_metadata)

    _set_bandwidth_metadata = { "offset" : _set_bandwidth_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @bandwidth.setter
    def bandwidth(self, value:float) -> None:
        """Get or set the waveform bandwidth."""
        return self._intf.set_property(StkRfcmRadarWaveform._metadata, StkRfcmRadarWaveform._set_bandwidth_metadata, value)

    _property_names[rf_channel_frequency] = "rf_channel_frequency"
    _property_names[pulse_repetition_frequency] = "pulse_repetition_frequency"
    _property_names[bandwidth] = "bandwidth"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarWaveform."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarWaveform)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarWaveform, [StkRfcmRadarWaveform, ])

agcls.AgClassCatalog.add_catalog_entry((4703831939351115472, 12881818140868134074), StkRfcmRadarWaveform)
agcls.AgTypeNameMap["StkRfcmRadarWaveform"] = StkRfcmRadarWaveform

class StkRfcmParametricBeamAntenna(IStkRfcmAntenna, SupportsDeleteCallback):
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
        "iid_data" : (5066231717385365390, 5698936586915315868),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmParametricBeamAntenna)
    
    _get_polarization_type_metadata = { "offset" : _get_polarization_type_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_POLARIZATION_TYPE),) }
    @property
    def polarization_type(self) -> "RFCM_POLARIZATION_TYPE":
        """Get or set the polarization type"""
        return self._intf.get_property(StkRfcmParametricBeamAntenna._metadata, StkRfcmParametricBeamAntenna._get_polarization_type_metadata)

    _set_polarization_type_metadata = { "offset" : _set_polarization_type_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(RFCM_POLARIZATION_TYPE),) }
    @polarization_type.setter
    def polarization_type(self, value:"RFCM_POLARIZATION_TYPE") -> None:
        """Get or set the polarization type"""
        return self._intf.set_property(StkRfcmParametricBeamAntenna._metadata, StkRfcmParametricBeamAntenna._set_polarization_type_metadata, value)

    _get_vertical_beamwidth_metadata = { "offset" : _get_vertical_beamwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def vertical_beamwidth(self) -> float:
        """Get or set the vertical beamwidth"""
        return self._intf.get_property(StkRfcmParametricBeamAntenna._metadata, StkRfcmParametricBeamAntenna._get_vertical_beamwidth_metadata)

    _set_vertical_beamwidth_metadata = { "offset" : _set_vertical_beamwidth_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @vertical_beamwidth.setter
    def vertical_beamwidth(self, value:float) -> None:
        """Get or set the vertical beamwidth"""
        return self._intf.set_property(StkRfcmParametricBeamAntenna._metadata, StkRfcmParametricBeamAntenna._set_vertical_beamwidth_metadata, value)

    _get_horizontal_beamwidth_metadata = { "offset" : _get_horizontal_beamwidth_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def horizontal_beamwidth(self) -> float:
        """Get or set the horizontal beamwidth"""
        return self._intf.get_property(StkRfcmParametricBeamAntenna._metadata, StkRfcmParametricBeamAntenna._get_horizontal_beamwidth_metadata)

    _set_horizontal_beamwidth_metadata = { "offset" : _set_horizontal_beamwidth_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @horizontal_beamwidth.setter
    def horizontal_beamwidth(self, value:float) -> None:
        """Get or set the horizontal beamwidth"""
        return self._intf.set_property(StkRfcmParametricBeamAntenna._metadata, StkRfcmParametricBeamAntenna._set_horizontal_beamwidth_metadata, value)

    _property_names[polarization_type] = "polarization_type"
    _property_names[vertical_beamwidth] = "vertical_beamwidth"
    _property_names[horizontal_beamwidth] = "horizontal_beamwidth"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmParametricBeamAntenna."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmParametricBeamAntenna)
        IStkRfcmAntenna.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAntenna._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmParametricBeamAntenna, [StkRfcmParametricBeamAntenna, IStkRfcmAntenna])

agcls.AgClassCatalog.add_catalog_entry((5281565447641177900, 16732104418991711902), StkRfcmParametricBeamAntenna)
agcls.AgTypeNameMap["StkRfcmParametricBeamAntenna"] = StkRfcmParametricBeamAntenna

class StkRfcmElementExportPatternAntenna(IStkRfcmAntenna, SupportsDeleteCallback):
    """Properties for an HFSS element export pattern (EEP) antenna model. This model accepts an EEP file which is exported from the Ansys HFSS software package."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_hfss_element_export_pattern_file_method_offset = 1
    _set_hfss_element_export_pattern_file_method_offset = 2
    _metadata = {
        "iid_data" : (4766319250734673987, 12312688800869503421),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmElementExportPatternAntenna)
    
    _get_hfss_element_export_pattern_file_metadata = { "offset" : _get_hfss_element_export_pattern_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def hfss_element_export_pattern_file(self) -> str:
        """Get or set the HFSS element export pattern file."""
        return self._intf.get_property(StkRfcmElementExportPatternAntenna._metadata, StkRfcmElementExportPatternAntenna._get_hfss_element_export_pattern_file_metadata)

    _set_hfss_element_export_pattern_file_metadata = { "offset" : _set_hfss_element_export_pattern_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @hfss_element_export_pattern_file.setter
    def hfss_element_export_pattern_file(self, value:str) -> None:
        """Get or set the HFSS element export pattern file."""
        return self._intf.set_property(StkRfcmElementExportPatternAntenna._metadata, StkRfcmElementExportPatternAntenna._set_hfss_element_export_pattern_file_metadata, value)

    _property_names[hfss_element_export_pattern_file] = "hfss_element_export_pattern_file"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmElementExportPatternAntenna."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmElementExportPatternAntenna)
        IStkRfcmAntenna.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAntenna._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmElementExportPatternAntenna, [StkRfcmElementExportPatternAntenna, IStkRfcmAntenna])

agcls.AgClassCatalog.add_catalog_entry((4825374820807761942, 16197124924034080433), StkRfcmElementExportPatternAntenna)
agcls.AgTypeNameMap["StkRfcmElementExportPatternAntenna"] = StkRfcmElementExportPatternAntenna

class StkRfcmFarFieldDataPatternAntenna(IStkRfcmAntenna, SupportsDeleteCallback):
    """Properties for an HFSS far field data (FFD) antenna model. This model accepts an FFD file which is exported from the Ansys HFSS software package."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_hfss_far_field_data_pattern_file_method_offset = 1
    _set_hfss_far_field_data_pattern_file_method_offset = 2
    _metadata = {
        "iid_data" : (5411664539639735101, 603918576028509367),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmFarFieldDataPatternAntenna)
    
    _get_hfss_far_field_data_pattern_file_metadata = { "offset" : _get_hfss_far_field_data_pattern_file_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def hfss_far_field_data_pattern_file(self) -> str:
        """Get or set the HFSS far field data pattern file."""
        return self._intf.get_property(StkRfcmFarFieldDataPatternAntenna._metadata, StkRfcmFarFieldDataPatternAntenna._get_hfss_far_field_data_pattern_file_metadata)

    _set_hfss_far_field_data_pattern_file_metadata = { "offset" : _set_hfss_far_field_data_pattern_file_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @hfss_far_field_data_pattern_file.setter
    def hfss_far_field_data_pattern_file(self, value:str) -> None:
        """Get or set the HFSS far field data pattern file."""
        return self._intf.set_property(StkRfcmFarFieldDataPatternAntenna._metadata, StkRfcmFarFieldDataPatternAntenna._set_hfss_far_field_data_pattern_file_metadata, value)

    _property_names[hfss_far_field_data_pattern_file] = "hfss_far_field_data_pattern_file"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmFarFieldDataPatternAntenna."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmFarFieldDataPatternAntenna)
        IStkRfcmAntenna.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAntenna._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmFarFieldDataPatternAntenna, [StkRfcmFarFieldDataPatternAntenna, IStkRfcmAntenna])

agcls.AgClassCatalog.add_catalog_entry((5592290011870032292, 2726481583475271050), StkRfcmFarFieldDataPatternAntenna)
agcls.AgTypeNameMap["StkRfcmFarFieldDataPatternAntenna"] = StkRfcmFarFieldDataPatternAntenna

class StkRfcmTransceiver(SupportsDeleteCallback):
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
        "iid_data" : (5558123964013987462, 4268831737052389557),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmTransceiver)
    
    _get_identifier_metadata = { "offset" : _get_identifier_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def identifier(self) -> str:
        """Get the transceiver unique identifier."""
        return self._intf.get_property(StkRfcmTransceiver._metadata, StkRfcmTransceiver._get_identifier_metadata)

    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get or set the transceiver name."""
        return self._intf.get_property(StkRfcmTransceiver._metadata, StkRfcmTransceiver._get_name_metadata)

    _set_name_metadata = { "offset" : _set_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @name.setter
    def name(self, name:str) -> None:
        """Get or set the transceiver name."""
        return self._intf.set_property(StkRfcmTransceiver._metadata, StkRfcmTransceiver._set_name_metadata, name)

    _get_parent_object_path_metadata = { "offset" : _get_parent_object_path_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def parent_object_path(self) -> str:
        """Get or set the transceiver's parent object path."""
        return self._intf.get_property(StkRfcmTransceiver._metadata, StkRfcmTransceiver._get_parent_object_path_metadata)

    _set_parent_object_path_metadata = { "offset" : _set_parent_object_path_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @parent_object_path.setter
    def parent_object_path(self, parent_object:str) -> None:
        """Get or set the transceiver's parent object path."""
        return self._intf.set_property(StkRfcmTransceiver._metadata, StkRfcmTransceiver._set_parent_object_path_metadata, parent_object)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the tileset central body name."""
        return self._intf.get_property(StkRfcmTransceiver._metadata, StkRfcmTransceiver._get_central_body_name_metadata)

    _get_model_metadata = { "offset" : _get_model_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def model(self) -> "IStkRfcmTransceiverModel":
        """Get the transceiver model."""
        return self._intf.get_property(StkRfcmTransceiver._metadata, StkRfcmTransceiver._get_model_metadata)

    _property_names[identifier] = "identifier"
    _property_names[name] = "name"
    _property_names[parent_object_path] = "parent_object_path"
    _property_names[central_body_name] = "central_body_name"
    _property_names[model] = "model"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmTransceiver."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmTransceiver)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmTransceiver, [StkRfcmTransceiver, ])

agcls.AgClassCatalog.add_catalog_entry((4774390769497310370, 10087295320591673777), StkRfcmTransceiver)
agcls.AgTypeNameMap["StkRfcmTransceiver"] = StkRfcmTransceiver

class StkRfcmCommunicationsTransceiverConfiguration(SupportsDeleteCallback):
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
        "iid_data" : (5172902671839407480, 8994840099133695906),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmCommunicationsTransceiverConfiguration)
    
    _get_supported_transceivers_metadata = { "offset" : _get_supported_transceivers_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_transceivers(self) -> list:
        """Get an array of available transceiver instances."""
        return self._intf.get_property(StkRfcmCommunicationsTransceiverConfiguration._metadata, StkRfcmCommunicationsTransceiverConfiguration._get_supported_transceivers_metadata)

    _get_transceiver_metadata = { "offset" : _get_transceiver_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver(self) -> "StkRfcmTransceiver":
        """Get or set the transceiver."""
        return self._intf.get_property(StkRfcmCommunicationsTransceiverConfiguration._metadata, StkRfcmCommunicationsTransceiverConfiguration._get_transceiver_metadata)

    _set_transceiver_metadata = { "offset" : _set_transceiver_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"),) }
    @transceiver.setter
    def transceiver(self, transceiver:"StkRfcmTransceiver") -> None:
        """Get or set the transceiver."""
        return self._intf.set_property(StkRfcmCommunicationsTransceiverConfiguration._metadata, StkRfcmCommunicationsTransceiverConfiguration._set_transceiver_metadata, transceiver)

    _get_mode_metadata = { "offset" : _get_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_TRANSCEIVER_MODE),) }
    @property
    def mode(self) -> "RFCM_TRANSCEIVER_MODE":
        """Get or set the tranceiver mode."""
        return self._intf.get_property(StkRfcmCommunicationsTransceiverConfiguration._metadata, StkRfcmCommunicationsTransceiverConfiguration._get_mode_metadata)

    _set_mode_metadata = { "offset" : _set_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(RFCM_TRANSCEIVER_MODE),) }
    @mode.setter
    def mode(self, value:"RFCM_TRANSCEIVER_MODE") -> None:
        """Get or set the tranceiver mode."""
        return self._intf.set_property(StkRfcmCommunicationsTransceiverConfiguration._metadata, StkRfcmCommunicationsTransceiverConfiguration._set_mode_metadata, value)

    _get_include_parent_object_facets_metadata = { "offset" : _get_include_parent_object_facets_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def include_parent_object_facets(self) -> bool:
        """Get or set an indicator of whether or not to include the parent object facets."""
        return self._intf.get_property(StkRfcmCommunicationsTransceiverConfiguration._metadata, StkRfcmCommunicationsTransceiverConfiguration._get_include_parent_object_facets_metadata)

    _set_include_parent_object_facets_metadata = { "offset" : _set_include_parent_object_facets_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @include_parent_object_facets.setter
    def include_parent_object_facets(self, value:bool) -> None:
        """Get or set an indicator of whether or not to include the parent object facets."""
        return self._intf.set_property(StkRfcmCommunicationsTransceiverConfiguration._metadata, StkRfcmCommunicationsTransceiverConfiguration._set_include_parent_object_facets_metadata, value)

    _property_names[supported_transceivers] = "supported_transceivers"
    _property_names[transceiver] = "transceiver"
    _property_names[mode] = "mode"
    _property_names[include_parent_object_facets] = "include_parent_object_facets"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmCommunicationsTransceiverConfiguration."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmCommunicationsTransceiverConfiguration)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmCommunicationsTransceiverConfiguration, [StkRfcmCommunicationsTransceiverConfiguration, ])

agcls.AgClassCatalog.add_catalog_entry((4989635995711489442, 13106208359506057875), StkRfcmCommunicationsTransceiverConfiguration)
agcls.AgTypeNameMap["StkRfcmCommunicationsTransceiverConfiguration"] = StkRfcmCommunicationsTransceiverConfiguration

class StkRfcmRadarTransceiverConfiguration(SupportsDeleteCallback):
    """Properties for a radar transceiver configuration. A transceiver configuration allows for changing the transceiver mode to one of three options, Transmit Only, Receive Only, or Transceive."""

    _num_methods = 5
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_supported_transceivers_method_offset = 1
    _get_transceiver_method_offset = 2
    _set_transceiver_method_offset = 3
    _get_mode_method_offset = 4
    _set_mode_method_offset = 5
    _metadata = {
        "iid_data" : (4659302401260160265, 11650713832413966732),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarTransceiverConfiguration)
    
    _get_supported_transceivers_metadata = { "offset" : _get_supported_transceivers_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_transceivers(self) -> list:
        """Get an array of available transceiver instances."""
        return self._intf.get_property(StkRfcmRadarTransceiverConfiguration._metadata, StkRfcmRadarTransceiverConfiguration._get_supported_transceivers_metadata)

    _get_transceiver_metadata = { "offset" : _get_transceiver_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver(self) -> "StkRfcmTransceiver":
        """Get or set the transceiver."""
        return self._intf.get_property(StkRfcmRadarTransceiverConfiguration._metadata, StkRfcmRadarTransceiverConfiguration._get_transceiver_metadata)

    _set_transceiver_metadata = { "offset" : _set_transceiver_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"),) }
    @transceiver.setter
    def transceiver(self, transceiver:"StkRfcmTransceiver") -> None:
        """Get or set the transceiver."""
        return self._intf.set_property(StkRfcmRadarTransceiverConfiguration._metadata, StkRfcmRadarTransceiverConfiguration._set_transceiver_metadata, transceiver)

    _get_mode_metadata = { "offset" : _get_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_TRANSCEIVER_MODE),) }
    @property
    def mode(self) -> "RFCM_TRANSCEIVER_MODE":
        """Get or set the tranceiver mode."""
        return self._intf.get_property(StkRfcmRadarTransceiverConfiguration._metadata, StkRfcmRadarTransceiverConfiguration._get_mode_metadata)

    _set_mode_metadata = { "offset" : _set_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(RFCM_TRANSCEIVER_MODE),) }
    @mode.setter
    def mode(self, value:"RFCM_TRANSCEIVER_MODE") -> None:
        """Get or set the tranceiver mode."""
        return self._intf.set_property(StkRfcmRadarTransceiverConfiguration._metadata, StkRfcmRadarTransceiverConfiguration._set_mode_metadata, value)

    _property_names[supported_transceivers] = "supported_transceivers"
    _property_names[transceiver] = "transceiver"
    _property_names[mode] = "mode"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarTransceiverConfiguration."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarTransceiverConfiguration)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarTransceiverConfiguration, [StkRfcmRadarTransceiverConfiguration, ])

agcls.AgClassCatalog.add_catalog_entry((5302182047077719402, 6821497016786865593), StkRfcmRadarTransceiverConfiguration)
agcls.AgTypeNameMap["StkRfcmRadarTransceiverConfiguration"] = StkRfcmRadarTransceiverConfiguration

class StkRfcmRadarTransceiverConfigurationCollection(SupportsDeleteCallback):
    """Represents a collection of radar transceiver configurations."""

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
    _contains_method_offset = 9
    _metadata = {
        "iid_data" : (4807842543420809634, 14097660371338695355),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarTransceiverConfigurationCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmRadarTransceiverConfigurationCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "StkRfcmRadarTransceiverConfiguration":
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
        return self._intf.get_property(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "StkRfcmRadarTransceiverConfiguration":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the configuration with the supplied index."""
        return self._intf.invoke(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"),) }
    def remove(self, transceiver:"StkRfcmTransceiver") -> None:
        """Remove the supplied transceiver from the collection."""
        return self._intf.invoke(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._remove_metadata, transceiver)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def add_new(self) -> "StkRfcmRadarTransceiverConfiguration":
        """Add and returns a new configuration."""
        return self._intf.invoke(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._add_new_metadata, OutArg())

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmRadarTransceiverConfiguration"),) }
    def add(self, value:"StkRfcmRadarTransceiverConfiguration") -> None:
        """Add a configuration."""
        return self._intf.invoke(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._add_metadata, value)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all configurations from the collection."""
        return self._intf.invoke(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"), agmarshall.VariantBoolArg,) }
    def contains(self, transceiver:"StkRfcmTransceiver") -> bool:
        """Check to see if a given configuration exists in the collection."""
        return self._intf.invoke(StkRfcmRadarTransceiverConfigurationCollection._metadata, StkRfcmRadarTransceiverConfigurationCollection._contains_metadata, transceiver, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarTransceiverConfigurationCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarTransceiverConfigurationCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarTransceiverConfigurationCollection, [StkRfcmRadarTransceiverConfigurationCollection, ])

agcls.AgClassCatalog.add_catalog_entry((4790458976272477186, 15304866967432392352), StkRfcmRadarTransceiverConfigurationCollection)
agcls.AgTypeNameMap["StkRfcmRadarTransceiverConfigurationCollection"] = StkRfcmRadarTransceiverConfigurationCollection

class StkRfcmAnalysisConfiguration(SupportsDeleteCallback):
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
        "iid_data" : (5101846457140874039, 3763858361601011076),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmAnalysisConfiguration)
    
    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get or set the configuration name."""
        return self._intf.get_property(StkRfcmAnalysisConfiguration._metadata, StkRfcmAnalysisConfiguration._get_name_metadata)

    _set_name_metadata = { "offset" : _set_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @name.setter
    def name(self, name:str) -> None:
        """Get or set the configuration name."""
        return self._intf.set_property(StkRfcmAnalysisConfiguration._metadata, StkRfcmAnalysisConfiguration._set_name_metadata, name)

    _get_description_metadata = { "offset" : _get_description_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def description(self) -> str:
        """Get or set the configuration description."""
        return self._intf.get_property(StkRfcmAnalysisConfiguration._metadata, StkRfcmAnalysisConfiguration._get_description_metadata)

    _set_description_metadata = { "offset" : _set_description_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @description.setter
    def description(self, description:str) -> None:
        """Get or set the configuration description."""
        return self._intf.set_property(StkRfcmAnalysisConfiguration._metadata, StkRfcmAnalysisConfiguration._set_description_metadata, description)

    _get_supported_central_bodies_metadata = { "offset" : _get_supported_central_bodies_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_central_bodies(self) -> list:
        """Get an array of available central bodies."""
        return self._intf.get_property(StkRfcmAnalysisConfiguration._metadata, StkRfcmAnalysisConfiguration._get_supported_central_bodies_metadata)

    _get_central_body_name_metadata = { "offset" : _get_central_body_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def central_body_name(self) -> str:
        """Get the configured central body name."""
        return self._intf.get_property(StkRfcmAnalysisConfiguration._metadata, StkRfcmAnalysisConfiguration._get_central_body_name_metadata)

    _set_central_body_name_metadata = { "offset" : _set_central_body_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @central_body_name.setter
    def central_body_name(self, value:str) -> None:
        """Set the configured central body name."""
        return self._intf.set_property(StkRfcmAnalysisConfiguration._metadata, StkRfcmAnalysisConfiguration._set_central_body_name_metadata, value)

    _get_model_metadata = { "offset" : _get_model_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def model(self) -> "IStkRfcmAnalysisConfigurationModel":
        """Get the analysis configuration model."""
        return self._intf.get_property(StkRfcmAnalysisConfiguration._metadata, StkRfcmAnalysisConfiguration._get_model_metadata)

    _property_names[name] = "name"
    _property_names[description] = "description"
    _property_names[supported_central_bodies] = "supported_central_bodies"
    _property_names[central_body_name] = "central_body_name"
    _property_names[model] = "model"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmAnalysisConfiguration."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmAnalysisConfiguration)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmAnalysisConfiguration, [StkRfcmAnalysisConfiguration, ])

agcls.AgClassCatalog.add_catalog_entry((5392730798104370011, 563428922600983438), StkRfcmAnalysisConfiguration)
agcls.AgTypeNameMap["StkRfcmAnalysisConfiguration"] = StkRfcmAnalysisConfiguration

class StkRfcmCommunicationsAnalysisConfigurationModel(IStkRfcmAnalysisConfigurationModel, SupportsDeleteCallback):
    """Properties for an analysis configuration model for a communications analysis. This contains a collection of the transceiver configurations belonging to the communications analysis."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _duplicate_transceiver_configuration_method_offset = 1
    _get_transceiver_configuration_collection_method_offset = 2
    _metadata = {
        "iid_data" : (4842510040248443164, 4420140607317663404),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmCommunicationsAnalysisConfigurationModel)
    
    _duplicate_transceiver_configuration_metadata = { "offset" : _duplicate_transceiver_configuration_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmCommunicationsTransceiverConfiguration"), agmarshall.InterfaceOutArg,) }
    def duplicate_transceiver_configuration(self, transceiver_configuration:"StkRfcmCommunicationsTransceiverConfiguration") -> "StkRfcmCommunicationsTransceiverConfiguration":
        """Duplicates a transceiver configuration instance."""
        return self._intf.invoke(StkRfcmCommunicationsAnalysisConfigurationModel._metadata, StkRfcmCommunicationsAnalysisConfigurationModel._duplicate_transceiver_configuration_metadata, transceiver_configuration, OutArg())

    _get_transceiver_configuration_collection_metadata = { "offset" : _get_transceiver_configuration_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver_configuration_collection(self) -> "StkRfcmCommunicationsTransceiverConfigurationCollection":
        """Get the collection of transceiver configurations."""
        return self._intf.get_property(StkRfcmCommunicationsAnalysisConfigurationModel._metadata, StkRfcmCommunicationsAnalysisConfigurationModel._get_transceiver_configuration_collection_metadata)

    _property_names[transceiver_configuration_collection] = "transceiver_configuration_collection"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmCommunicationsAnalysisConfigurationModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmCommunicationsAnalysisConfigurationModel)
        IStkRfcmAnalysisConfigurationModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAnalysisConfigurationModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmCommunicationsAnalysisConfigurationModel, [StkRfcmCommunicationsAnalysisConfigurationModel, IStkRfcmAnalysisConfigurationModel])

agcls.AgClassCatalog.add_catalog_entry((5515277576377628430, 13436450372685581228), StkRfcmCommunicationsAnalysisConfigurationModel)
agcls.AgTypeNameMap["StkRfcmCommunicationsAnalysisConfigurationModel"] = StkRfcmCommunicationsAnalysisConfigurationModel

class StkRfcmRadarISarAnalysisConfigurationModel(IStkRfcmAnalysisConfigurationModel, IStkRfcmRadarAnalysisConfigurationModel, SupportsDeleteCallback):
    """The analysis configuration model for an ISar analysis. This contains a collection of the transceiver configurations belonging to the ISar analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_radar_target_collection_method_offset = 1
    _metadata = {
        "iid_data" : (4699547487188819079, 7119029616558802341),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarISarAnalysisConfigurationModel)
    
    _get_radar_target_collection_metadata = { "offset" : _get_radar_target_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def radar_target_collection(self) -> "StkRfcmRadarTargetCollection":
        """Get the collection of radar targets."""
        return self._intf.get_property(StkRfcmRadarISarAnalysisConfigurationModel._metadata, StkRfcmRadarISarAnalysisConfigurationModel._get_radar_target_collection_metadata)

    _property_names[radar_target_collection] = "radar_target_collection"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarISarAnalysisConfigurationModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarISarAnalysisConfigurationModel)
        IStkRfcmAnalysisConfigurationModel.__init__(self, source_object)
        IStkRfcmRadarAnalysisConfigurationModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAnalysisConfigurationModel._private_init(self, intf)
        IStkRfcmRadarAnalysisConfigurationModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarISarAnalysisConfigurationModel, [StkRfcmRadarISarAnalysisConfigurationModel, IStkRfcmAnalysisConfigurationModel, IStkRfcmRadarAnalysisConfigurationModel])

agcls.AgClassCatalog.add_catalog_entry((5228864121001253272, 11476005751415570308), StkRfcmRadarISarAnalysisConfigurationModel)
agcls.AgTypeNameMap["StkRfcmRadarISarAnalysisConfigurationModel"] = StkRfcmRadarISarAnalysisConfigurationModel

class StkRfcmRadarSarAnalysisConfigurationModel(IStkRfcmAnalysisConfigurationModel, IStkRfcmRadarAnalysisConfigurationModel, SupportsDeleteCallback):
    """The analysis configuration model for a Sar analysis. This contains a collection of the transceiver configurations belonging to the Sar analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_image_location_collection_method_offset = 1
    _metadata = {
        "iid_data" : (4854169440574638134, 10421576952529875864),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarSarAnalysisConfigurationModel)
    
    _get_image_location_collection_metadata = { "offset" : _get_image_location_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def image_location_collection(self) -> "StkRfcmRadarSarImageLocationCollection":
        """Get the collection of image locations."""
        return self._intf.get_property(StkRfcmRadarSarAnalysisConfigurationModel._metadata, StkRfcmRadarSarAnalysisConfigurationModel._get_image_location_collection_metadata)

    _property_names[image_location_collection] = "image_location_collection"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarSarAnalysisConfigurationModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarSarAnalysisConfigurationModel)
        IStkRfcmAnalysisConfigurationModel.__init__(self, source_object)
        IStkRfcmRadarAnalysisConfigurationModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAnalysisConfigurationModel._private_init(self, intf)
        IStkRfcmRadarAnalysisConfigurationModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarSarAnalysisConfigurationModel, [StkRfcmRadarSarAnalysisConfigurationModel, IStkRfcmAnalysisConfigurationModel, IStkRfcmRadarAnalysisConfigurationModel])

agcls.AgClassCatalog.add_catalog_entry((5764377955799592933, 16878723110774774148), StkRfcmRadarSarAnalysisConfigurationModel)
agcls.AgTypeNameMap["StkRfcmRadarSarAnalysisConfigurationModel"] = StkRfcmRadarSarAnalysisConfigurationModel

class StkRfcmTransceiverCollection(SupportsDeleteCallback):
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
        "iid_data" : (5453563073797309057, 6941833189803444112),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmTransceiverCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmTransceiverCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "StkRfcmTransceiver":
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
        return self._intf.get_property(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "StkRfcmTransceiver":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the transceiver with the supplied index."""
        return self._intf.invoke(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"),) }
    def remove(self, transceiver:"StkRfcmTransceiver") -> None:
        """Remove the supplied transceiver from the collection."""
        return self._intf.invoke(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._remove_metadata, transceiver)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (agcom.LONG, agcom.BSTR, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(RFCM_TRANSCEIVER_MODEL_TYPE), agmarshall.BStrArg, agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def add_new(self, type:"RFCM_TRANSCEIVER_MODEL_TYPE", name:str, parent_object_path:str) -> "StkRfcmTransceiver":
        """Add and returns a new transceiver."""
        return self._intf.invoke(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._add_new_metadata, type, name, parent_object_path, OutArg())

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"),) }
    def add(self, value:"StkRfcmTransceiver") -> None:
        """Add the supplied transceiver to the collection."""
        return self._intf.invoke(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._add_metadata, value)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Remove all transceivers from the collection."""
        return self._intf.invoke(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._remove_all_metadata, )

    _find_by_identifier_metadata = { "offset" : _find_by_identifier_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def find_by_identifier(self, identifier:str) -> "StkRfcmTransceiver":
        """Return the transciever in the collection with the supplied identifier or Null if not found or invalid."""
        return self._intf.invoke(StkRfcmTransceiverCollection._metadata, StkRfcmTransceiverCollection._find_by_identifier_metadata, identifier, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmTransceiverCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmTransceiverCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmTransceiverCollection, [StkRfcmTransceiverCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5274798942248124582, 15790306252761209771), StkRfcmTransceiverCollection)
agcls.AgTypeNameMap["StkRfcmTransceiverCollection"] = StkRfcmTransceiverCollection

class StkRfcmFacetTilesetCollection(SupportsDeleteCallback):
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
        "iid_data" : (5753655749563624094, 7998985330621454980),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmFacetTilesetCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmFacetTilesetCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "StkRfcmFacetTileset":
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
        return self._intf.get_property(StkRfcmFacetTilesetCollection._metadata, StkRfcmFacetTilesetCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "StkRfcmFacetTileset":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmFacetTilesetCollection._metadata, StkRfcmFacetTilesetCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmFacetTilesetCollection._metadata, StkRfcmFacetTilesetCollection._get__new_enum_metadata)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmFacetTileset"),) }
    def remove(self, value:"StkRfcmFacetTileset") -> None:
        """Remove the supplied facet tileset from the collection."""
        return self._intf.invoke(StkRfcmFacetTilesetCollection._metadata, StkRfcmFacetTilesetCollection._remove_metadata, value)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the facet tileset with the supplied index."""
        return self._intf.invoke(StkRfcmFacetTilesetCollection._metadata, StkRfcmFacetTilesetCollection._remove_at_metadata, index)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all facet tilesets from the collection."""
        return self._intf.invoke(StkRfcmFacetTilesetCollection._metadata, StkRfcmFacetTilesetCollection._remove_all_metadata, )

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmFacetTileset"),) }
    def add(self, value:"StkRfcmFacetTileset") -> None:
        """Add a facet tile set to the collection."""
        return self._intf.invoke(StkRfcmFacetTilesetCollection._metadata, StkRfcmFacetTilesetCollection._add_metadata, value)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmFacetTilesetCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmFacetTilesetCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmFacetTilesetCollection, [StkRfcmFacetTilesetCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5307708137821167772, 1526680685227976082), StkRfcmFacetTilesetCollection)
agcls.AgTypeNameMap["StkRfcmFacetTilesetCollection"] = StkRfcmFacetTilesetCollection

class StkRfcmSceneContributor(IStkRfcmSceneContributor, SupportsDeleteCallback):
    """A scene contributor object."""
    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmSceneContributor."""
        SupportsDeleteCallback.__init__(self)
        IStkRfcmSceneContributor.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmSceneContributor._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmSceneContributor, [IStkRfcmSceneContributor])

agcls.AgClassCatalog.add_catalog_entry((4973272663297336587, 5054245476557569700), StkRfcmSceneContributor)
agcls.AgTypeNameMap["StkRfcmSceneContributor"] = StkRfcmSceneContributor

class StkRfcmRadarTarget(IStkRfcmSceneContributor, SupportsDeleteCallback):
    """Properties of a radar target object."""

    _num_methods = 0
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _metadata = {
        "iid_data" : (5504796988167435012, 17004012237123312822),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarTarget)
    

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarTarget."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarTarget)
        IStkRfcmSceneContributor.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmSceneContributor._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarTarget, [StkRfcmRadarTarget, IStkRfcmSceneContributor])

agcls.AgClassCatalog.add_catalog_entry((5540179625930776689, 2564433932983714712), StkRfcmRadarTarget)
agcls.AgTypeNameMap["StkRfcmRadarTarget"] = StkRfcmRadarTarget

class StkRfcmSceneContributorCollection(SupportsDeleteCallback):
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
        "iid_data" : (4727679194678330883, 10823296216059869100),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmSceneContributorCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmSceneContributorCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IStkRfcmSceneContributor":
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
        return self._intf.get_property(StkRfcmSceneContributorCollection._metadata, StkRfcmSceneContributorCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "IStkRfcmSceneContributor":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmSceneContributorCollection._metadata, StkRfcmSceneContributorCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmSceneContributorCollection._metadata, StkRfcmSceneContributorCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the scene contributor with the supplied index."""
        return self._intf.invoke(StkRfcmSceneContributorCollection._metadata, StkRfcmSceneContributorCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def remove(self, stk_object_path:str) -> None:
        """Remove the supplied scene contributor from the collection."""
        return self._intf.invoke(StkRfcmSceneContributorCollection._metadata, StkRfcmSceneContributorCollection._remove_metadata, stk_object_path)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def add_new(self, stk_object_path:str) -> "IStkRfcmSceneContributor":
        """Add and returns a new scene contributor."""
        return self._intf.invoke(StkRfcmSceneContributorCollection._metadata, StkRfcmSceneContributorCollection._add_new_metadata, stk_object_path, OutArg())

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all scene contributors from the collection."""
        return self._intf.invoke(StkRfcmSceneContributorCollection._metadata, StkRfcmSceneContributorCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def contains(self, stk_object_path:str) -> bool:
        """Check to see if a given scene contributor exists in the collection."""
        return self._intf.invoke(StkRfcmSceneContributorCollection._metadata, StkRfcmSceneContributorCollection._contains_metadata, stk_object_path, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmSceneContributorCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmSceneContributorCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmSceneContributorCollection, [StkRfcmSceneContributorCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5079782350604257666, 16703292362421634220), StkRfcmSceneContributorCollection)
agcls.AgTypeNameMap["StkRfcmSceneContributorCollection"] = StkRfcmSceneContributorCollection

class StkRfcmRadarTargetCollection(SupportsDeleteCallback):
    """Represents a collection of radar targets."""

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
        "iid_data" : (5649556021813001527, 3784966151514835858),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarTargetCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmRadarTargetCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "StkRfcmRadarTarget":
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
        return self._intf.get_property(StkRfcmRadarTargetCollection._metadata, StkRfcmRadarTargetCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "StkRfcmRadarTarget":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmRadarTargetCollection._metadata, StkRfcmRadarTargetCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmRadarTargetCollection._metadata, StkRfcmRadarTargetCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the radar target with the supplied index."""
        return self._intf.invoke(StkRfcmRadarTargetCollection._metadata, StkRfcmRadarTargetCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def remove(self, stk_object_path:str) -> None:
        """Remove the supplied radar target from the collection."""
        return self._intf.invoke(StkRfcmRadarTargetCollection._metadata, StkRfcmRadarTargetCollection._remove_metadata, stk_object_path)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def add_new(self, stk_object_path:str) -> "StkRfcmRadarTarget":
        """Add and returns a new radar target."""
        return self._intf.invoke(StkRfcmRadarTargetCollection._metadata, StkRfcmRadarTargetCollection._add_new_metadata, stk_object_path, OutArg())

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all radar targets from the collection."""
        return self._intf.invoke(StkRfcmRadarTargetCollection._metadata, StkRfcmRadarTargetCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def contains(self, stk_object_path:str) -> bool:
        """Check to see if a given radar target exists in the collection."""
        return self._intf.invoke(StkRfcmRadarTargetCollection._metadata, StkRfcmRadarTargetCollection._contains_metadata, stk_object_path, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarTargetCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarTargetCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarTargetCollection, [StkRfcmRadarTargetCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5310760862917692294, 11829976016985872805), StkRfcmRadarTargetCollection)
agcls.AgTypeNameMap["StkRfcmRadarTargetCollection"] = StkRfcmRadarTargetCollection

class StkRfcmRadarSarImageLocation(SupportsDeleteCallback):
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
        "iid_data" : (4928415407610984061, 7191108097270096522),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarSarImageLocation)
    
    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get or set the image location name."""
        return self._intf.get_property(StkRfcmRadarSarImageLocation._metadata, StkRfcmRadarSarImageLocation._get_name_metadata)

    _set_name_metadata = { "offset" : _set_name_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    @name.setter
    def name(self, value:str) -> None:
        """Get or set the image location name."""
        return self._intf.set_property(StkRfcmRadarSarImageLocation._metadata, StkRfcmRadarSarImageLocation._set_name_metadata, value)

    _get_latitude_metadata = { "offset" : _get_latitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def latitude(self) -> float:
        """Get or set the location latitude."""
        return self._intf.get_property(StkRfcmRadarSarImageLocation._metadata, StkRfcmRadarSarImageLocation._get_latitude_metadata)

    _set_latitude_metadata = { "offset" : _set_latitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @latitude.setter
    def latitude(self, value:float) -> None:
        """Get or set the location latitude."""
        return self._intf.set_property(StkRfcmRadarSarImageLocation._metadata, StkRfcmRadarSarImageLocation._set_latitude_metadata, value)

    _get_longitude_metadata = { "offset" : _get_longitude_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def longitude(self) -> float:
        """Get or set the location longitude."""
        return self._intf.get_property(StkRfcmRadarSarImageLocation._metadata, StkRfcmRadarSarImageLocation._get_longitude_metadata)

    _set_longitude_metadata = { "offset" : _set_longitude_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @longitude.setter
    def longitude(self, value:float) -> None:
        """Get or set the location longitude."""
        return self._intf.set_property(StkRfcmRadarSarImageLocation._metadata, StkRfcmRadarSarImageLocation._set_longitude_metadata, value)

    _property_names[name] = "name"
    _property_names[latitude] = "latitude"
    _property_names[longitude] = "longitude"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarSarImageLocation."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarSarImageLocation)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarSarImageLocation, [StkRfcmRadarSarImageLocation, ])

agcls.AgClassCatalog.add_catalog_entry((5444737755923510910, 18321320075764662437), StkRfcmRadarSarImageLocation)
agcls.AgTypeNameMap["StkRfcmRadarSarImageLocation"] = StkRfcmRadarSarImageLocation

class StkRfcmRadarSarImageLocationCollection(SupportsDeleteCallback):
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
        "iid_data" : (5715838980280879821, 3014522816578550712),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarSarImageLocationCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmRadarSarImageLocationCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "StkRfcmRadarSarImageLocation":
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
        return self._intf.get_property(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "StkRfcmRadarSarImageLocation":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the SAR image location with the supplied index."""
        return self._intf.invoke(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.BSTR,),
            "marshallers" : (agmarshall.BStrArg,) }
    def remove(self, image_location_name:str) -> None:
        """Remove the supplied SAR image location from the collection."""
        return self._intf.invoke(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._remove_metadata, image_location_name)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def add_new(self) -> "StkRfcmRadarSarImageLocation":
        """Add and returns a new SAR image location."""
        return self._intf.invoke(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._add_new_metadata, OutArg())

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all SAR image locations from the collection."""
        return self._intf.invoke(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def contains(self, image_location_name:str) -> bool:
        """Check to see if a given SAR image location exists in the collection."""
        return self._intf.invoke(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._contains_metadata, image_location_name, OutArg())

    _find_metadata = { "offset" : _find_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def find(self, image_location_name:str) -> "StkRfcmRadarSarImageLocation":
        """Find a SAR image location by name. Returns Null if the image location name does not exist in the collection."""
        return self._intf.invoke(StkRfcmRadarSarImageLocationCollection._metadata, StkRfcmRadarSarImageLocationCollection._find_metadata, image_location_name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarSarImageLocationCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarSarImageLocationCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarSarImageLocationCollection, [StkRfcmRadarSarImageLocationCollection, ])

agcls.AgClassCatalog.add_catalog_entry((4952796876820433574, 17254855614936067770), StkRfcmRadarSarImageLocationCollection)
agcls.AgTypeNameMap["StkRfcmRadarSarImageLocationCollection"] = StkRfcmRadarSarImageLocationCollection

class StkRfcmCommunicationsTransceiverConfigurationCollection(SupportsDeleteCallback):
    """Represents a collection of communication transceiver configurations."""

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
    _contains_method_offset = 9
    _metadata = {
        "iid_data" : (5571394370622903367, 10058552235130119822),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmCommunicationsTransceiverConfigurationCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmCommunicationsTransceiverConfigurationCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "StkRfcmCommunicationsTransceiverConfiguration":
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
        return self._intf.get_property(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "StkRfcmCommunicationsTransceiverConfiguration":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the configuration with the supplied index."""
        return self._intf.invoke(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"),) }
    def remove(self, transceiver:"StkRfcmTransceiver") -> None:
        """Remove the supplied configuration from the collection."""
        return self._intf.invoke(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._remove_metadata, transceiver)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    def add_new(self) -> "StkRfcmCommunicationsTransceiverConfiguration":
        """Add and returns a new configuration."""
        return self._intf.invoke(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._add_new_metadata, OutArg())

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmCommunicationsTransceiverConfiguration"),) }
    def add(self, value:"StkRfcmCommunicationsTransceiverConfiguration") -> None:
        """Add a configuration."""
        return self._intf.invoke(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._add_metadata, value)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear all configurations from the collection."""
        return self._intf.invoke(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"), agmarshall.VariantBoolArg,) }
    def contains(self, transceiver:"StkRfcmTransceiver") -> bool:
        """Check to see if a given configuration exists in the collection."""
        return self._intf.invoke(StkRfcmCommunicationsTransceiverConfigurationCollection._metadata, StkRfcmCommunicationsTransceiverConfigurationCollection._contains_metadata, transceiver, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmCommunicationsTransceiverConfigurationCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmCommunicationsTransceiverConfigurationCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmCommunicationsTransceiverConfigurationCollection, [StkRfcmCommunicationsTransceiverConfigurationCollection, ])

agcls.AgClassCatalog.add_catalog_entry((4918177005773267776, 5330117875639860627), StkRfcmCommunicationsTransceiverConfigurationCollection)
agcls.AgTypeNameMap["StkRfcmCommunicationsTransceiverConfigurationCollection"] = StkRfcmCommunicationsTransceiverConfigurationCollection

class StkRfcmAnalysisConfigurationCollection(SupportsDeleteCallback):
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
        "iid_data" : (4662220020043770228, 1775359325286225077),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmAnalysisConfigurationCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmAnalysisConfigurationCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "StkRfcmAnalysisConfiguration":
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
        return self._intf.get_property(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "StkRfcmAnalysisConfiguration":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._get__new_enum_metadata)

    _remove_at_metadata = { "offset" : _remove_at_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    def remove_at(self, index:int) -> None:
        """Remove the analysis configuration at the supplied index."""
        return self._intf.invoke(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._remove_at_metadata, index)

    _remove_metadata = { "offset" : _remove_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmAnalysisConfiguration"),) }
    def remove(self, value:"StkRfcmAnalysisConfiguration") -> None:
        """Remove the supplied analysis configuration."""
        return self._intf.invoke(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._remove_metadata, value)

    _add_new_metadata = { "offset" : _add_new_method_offset,
            "arg_types" : (agcom.LONG, agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.EnumArg(RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE), agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def add_new(self, model_type:"RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE", configuration_name:str) -> "StkRfcmAnalysisConfiguration":
        """Add and returns a new analysis configuration."""
        return self._intf.invoke(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._add_new_metadata, model_type, configuration_name, OutArg())

    _add_metadata = { "offset" : _add_method_offset,
            "arg_types" : (agcom.PVOID,),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmAnalysisConfiguration"),) }
    def add(self, value:"StkRfcmAnalysisConfiguration") -> None:
        """Add the supplied analysis configuration."""
        return self._intf.invoke(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._add_metadata, value)

    _remove_all_metadata = { "offset" : _remove_all_method_offset,
            "arg_types" : (),
            "marshallers" : () }
    def remove_all(self) -> None:
        """Clear the collection."""
        return self._intf.invoke(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._remove_all_metadata, )

    _contains_metadata = { "offset" : _contains_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.VariantBoolArg,) }
    def contains(self, configuration_name:str) -> bool:
        """Determine if the collection contains an analysis configuration with the given name."""
        return self._intf.invoke(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._contains_metadata, configuration_name, OutArg())

    _find_metadata = { "offset" : _find_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def find(self, configuration_name:str) -> "StkRfcmAnalysisConfiguration":
        """Find an analysis configuration by name. Returns Null if the configuration name does not exist in the collection."""
        return self._intf.invoke(StkRfcmAnalysisConfigurationCollection._metadata, StkRfcmAnalysisConfigurationCollection._find_metadata, configuration_name, OutArg())

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmAnalysisConfigurationCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmAnalysisConfigurationCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmAnalysisConfigurationCollection, [StkRfcmAnalysisConfigurationCollection, ])

agcls.AgClassCatalog.add_catalog_entry((4928253720090755449, 12599536154964304772), StkRfcmAnalysisConfigurationCollection)
agcls.AgTypeNameMap["StkRfcmAnalysisConfigurationCollection"] = StkRfcmAnalysisConfigurationCollection

class StkRfcmComputeOptions(SupportsDeleteCallback):
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
        "iid_data" : (5486226833155479016, 11259931109832989631),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmComputeOptions)
    
    _get_ray_density_metadata = { "offset" : _get_ray_density_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def ray_density(self) -> float:
        """Get or set the ray density."""
        return self._intf.get_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._get_ray_density_metadata)

    _set_ray_density_metadata = { "offset" : _set_ray_density_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @ray_density.setter
    def ray_density(self, value:float) -> None:
        """Get or set the ray density"""
        return self._intf.set_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._set_ray_density_metadata, value)

    _get_geometrical_optics_blockage_metadata = { "offset" : _get_geometrical_optics_blockage_method_offset,
            "arg_types" : (POINTER(agcom.VARIANT_BOOL),),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @property
    def geometrical_optics_blockage(self) -> bool:
        """Get or set the geometrical optics blockage."""
        return self._intf.get_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._get_geometrical_optics_blockage_metadata)

    _set_geometrical_optics_blockage_metadata = { "offset" : _set_geometrical_optics_blockage_method_offset,
            "arg_types" : (agcom.VARIANT_BOOL,),
            "marshallers" : (agmarshall.VariantBoolArg,) }
    @geometrical_optics_blockage.setter
    def geometrical_optics_blockage(self, value:bool) -> None:
        """Get or set the geometrical optics blockage."""
        return self._intf.set_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._set_geometrical_optics_blockage_metadata, value)

    _get_geometrical_optics_blockage_starting_bounce_metadata = { "offset" : _get_geometrical_optics_blockage_starting_bounce_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def geometrical_optics_blockage_starting_bounce(self) -> int:
        """Get or set the geometrical optics blockage starting bounce."""
        return self._intf.get_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._get_geometrical_optics_blockage_starting_bounce_metadata)

    _set_geometrical_optics_blockage_starting_bounce_metadata = { "offset" : _set_geometrical_optics_blockage_starting_bounce_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @geometrical_optics_blockage_starting_bounce.setter
    def geometrical_optics_blockage_starting_bounce(self, value:int) -> None:
        """Get or set the geometrical optics blockage starting bounce."""
        return self._intf.set_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._set_geometrical_optics_blockage_starting_bounce_metadata, value)

    _get_maximum_reflections_metadata = { "offset" : _get_maximum_reflections_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def maximum_reflections(self) -> int:
        """Get or set the maximum number of reflections."""
        return self._intf.get_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._get_maximum_reflections_metadata)

    _set_maximum_reflections_metadata = { "offset" : _set_maximum_reflections_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @maximum_reflections.setter
    def maximum_reflections(self, value:int) -> None:
        """Get or set the maximum number of reflections."""
        return self._intf.set_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._set_maximum_reflections_metadata, value)

    _get_maximum_transmissions_metadata = { "offset" : _get_maximum_transmissions_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def maximum_transmissions(self) -> int:
        """Get or set the maximum number of transmissions."""
        return self._intf.get_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._get_maximum_transmissions_metadata)

    _set_maximum_transmissions_metadata = { "offset" : _set_maximum_transmissions_method_offset,
            "arg_types" : (agcom.INT,),
            "marshallers" : (agmarshall.IntArg,) }
    @maximum_transmissions.setter
    def maximum_transmissions(self, value:int) -> None:
        """Get or set the maximum number of transmissions."""
        return self._intf.set_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._set_maximum_transmissions_metadata, value)

    _get_bounding_box_mode_metadata = { "offset" : _get_bounding_box_mode_method_offset,
            "arg_types" : (POINTER(agcom.LONG),),
            "marshallers" : (agmarshall.EnumArg(RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE),) }
    @property
    def bounding_box_mode(self) -> "RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE":
        """Get or set the bounding box."""
        return self._intf.get_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._get_bounding_box_mode_metadata)

    _set_bounding_box_mode_metadata = { "offset" : _set_bounding_box_mode_method_offset,
            "arg_types" : (agcom.LONG,),
            "marshallers" : (agmarshall.EnumArg(RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE),) }
    @bounding_box_mode.setter
    def bounding_box_mode(self, value:"RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE") -> None:
        """Get or set the bounding box."""
        return self._intf.set_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._set_bounding_box_mode_metadata, value)

    _get_bounding_box_side_length_metadata = { "offset" : _get_bounding_box_side_length_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def bounding_box_side_length(self) -> float:
        """Get or set the bounding box side length."""
        return self._intf.get_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._get_bounding_box_side_length_metadata)

    _set_bounding_box_side_length_metadata = { "offset" : _set_bounding_box_side_length_method_offset,
            "arg_types" : (agcom.DOUBLE,),
            "marshallers" : (agmarshall.DoubleArg,) }
    @bounding_box_side_length.setter
    def bounding_box_side_length(self, value:float) -> None:
        """Get or set the bounding box side length"""
        return self._intf.set_property(StkRfcmComputeOptions._metadata, StkRfcmComputeOptions._set_bounding_box_side_length_metadata, value)

    _property_names[ray_density] = "ray_density"
    _property_names[geometrical_optics_blockage] = "geometrical_optics_blockage"
    _property_names[geometrical_optics_blockage_starting_bounce] = "geometrical_optics_blockage_starting_bounce"
    _property_names[maximum_reflections] = "maximum_reflections"
    _property_names[maximum_transmissions] = "maximum_transmissions"
    _property_names[bounding_box_mode] = "bounding_box_mode"
    _property_names[bounding_box_side_length] = "bounding_box_side_length"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmComputeOptions."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmComputeOptions)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmComputeOptions, [StkRfcmComputeOptions, ])

agcls.AgClassCatalog.add_catalog_entry((5519048876673409941, 3923537089545973176), StkRfcmComputeOptions)
agcls.AgTypeNameMap["StkRfcmComputeOptions"] = StkRfcmComputeOptions

class StkRFChannelModeler(SupportsDeleteCallback):
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
        "iid_data" : (5326550927957697862, 7805227810553142921),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRFChannelModeler)
    
    _get_transceiver_collection_metadata = { "offset" : _get_transceiver_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def transceiver_collection(self) -> "StkRfcmTransceiverCollection":
        """Get the collection of transceiver objects."""
        return self._intf.get_property(StkRFChannelModeler._metadata, StkRFChannelModeler._get_transceiver_collection_metadata)

    _get_analysis_configuration_collection_metadata = { "offset" : _get_analysis_configuration_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def analysis_configuration_collection(self) -> "StkRfcmAnalysisConfigurationCollection":
        """Get the collection of analysis configurations."""
        return self._intf.get_property(StkRFChannelModeler._metadata, StkRFChannelModeler._get_analysis_configuration_collection_metadata)

    _duplicate_transceiver_metadata = { "offset" : _duplicate_transceiver_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmTransceiver"), agmarshall.InterfaceOutArg,) }
    def duplicate_transceiver(self, transceiver:"StkRfcmTransceiver") -> "StkRfcmTransceiver":
        """Duplicates a transceiver instance."""
        return self._intf.invoke(StkRFChannelModeler._metadata, StkRFChannelModeler._duplicate_transceiver_metadata, transceiver, OutArg())

    _duplicate_analysis_configuration_metadata = { "offset" : _duplicate_analysis_configuration_method_offset,
            "arg_types" : (agcom.PVOID, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceInArg("StkRfcmAnalysisConfiguration"), agmarshall.InterfaceOutArg,) }
    def duplicate_analysis_configuration(self, analysis_configuration:"StkRfcmAnalysisConfiguration") -> "StkRfcmAnalysisConfiguration":
        """Duplicates an analysis configuration instance."""
        return self._intf.invoke(StkRFChannelModeler._metadata, StkRFChannelModeler._duplicate_analysis_configuration_metadata, analysis_configuration, OutArg())

    _get_supported_materials_metadata = { "offset" : _get_supported_materials_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_materials(self) -> list:
        """Get the supported tileset materials"""
        return self._intf.get_property(StkRFChannelModeler._metadata, StkRFChannelModeler._get_supported_materials_metadata)

    _get_default_materials_metadata = { "offset" : _get_default_materials_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def default_materials(self) -> list:
        """Get the default tileset materials"""
        return self._intf.get_property(StkRFChannelModeler._metadata, StkRFChannelModeler._get_default_materials_metadata)

    _get_compute_options_metadata = { "offset" : _get_compute_options_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def compute_options(self) -> "StkRfcmComputeOptions":
        """Get the compute options."""
        return self._intf.get_property(StkRFChannelModeler._metadata, StkRFChannelModeler._get_compute_options_metadata)

    _get_supported_gpu_properties_list_metadata = { "offset" : _get_supported_gpu_properties_list_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def supported_gpu_properties_list(self) -> list:
        """Get the GPU properties list."""
        return self._intf.get_property(StkRFChannelModeler._metadata, StkRFChannelModeler._get_supported_gpu_properties_list_metadata)

    _set_gpu_devices_metadata = { "offset" : _set_gpu_devices_method_offset,
            "arg_types" : (agcom.LPSAFEARRAY,),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    def set_gpu_devices(self, gpu_device_ids:list) -> None:
        """Set the desired GPU device IDs"""
        return self._intf.invoke(StkRFChannelModeler._metadata, StkRFChannelModeler._set_gpu_devices_metadata, gpu_device_ids)

    _construct_analysis_metadata = { "offset" : _construct_analysis_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def construct_analysis(self, analysis_configuration_name:str) -> "StkRfcmAnalysis":
        """Construct an Analysis for an analysis configuration."""
        return self._intf.invoke(StkRFChannelModeler._metadata, StkRFChannelModeler._construct_analysis_metadata, analysis_configuration_name, OutArg())

    _validate_analysis_metadata = { "offset" : _validate_analysis_method_offset,
            "arg_types" : (agcom.BSTR, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.BStrArg, agmarshall.InterfaceOutArg,) }
    def validate_analysis(self, analysis_configuration_name:str) -> "StkRfcmValidationResponse":
        """Validates an analysis configuration."""
        return self._intf.invoke(StkRFChannelModeler._metadata, StkRFChannelModeler._validate_analysis_metadata, analysis_configuration_name, OutArg())

    _property_names[transceiver_collection] = "transceiver_collection"
    _property_names[analysis_configuration_collection] = "analysis_configuration_collection"
    _property_names[supported_materials] = "supported_materials"
    _property_names[default_materials] = "default_materials"
    _property_names[compute_options] = "compute_options"
    _property_names[supported_gpu_properties_list] = "supported_gpu_properties_list"

    def __init__(self, source_object=None):
        """Construct an object of type StkRFChannelModeler."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRFChannelModeler)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRFChannelModeler, [StkRFChannelModeler, ])

agcls.AgClassCatalog.add_catalog_entry((5711907369548252697, 4711585359054994589), StkRFChannelModeler)
agcls.AgTypeNameMap["StkRFChannelModeler"] = StkRFChannelModeler

class StkRfcmCommunicationsTransceiverModel(IStkRfcmTransceiverModel, SupportsDeleteCallback):
    """Properties for configuring a communications transceiver model."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_waveform_method_offset = 1
    _metadata = {
        "iid_data" : (5551616547060849613, 1549009027122701441),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmCommunicationsTransceiverModel)
    
    _get_waveform_metadata = { "offset" : _get_waveform_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def waveform(self) -> "StkRfcmCommunicationsWaveform":
        """Get the transceiver's waveform settings."""
        return self._intf.get_property(StkRfcmCommunicationsTransceiverModel._metadata, StkRfcmCommunicationsTransceiverModel._get_waveform_metadata)

    _property_names[waveform] = "waveform"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmCommunicationsTransceiverModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmCommunicationsTransceiverModel)
        IStkRfcmTransceiverModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmTransceiverModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmCommunicationsTransceiverModel, [StkRfcmCommunicationsTransceiverModel, IStkRfcmTransceiverModel])

agcls.AgClassCatalog.add_catalog_entry((5460540020574842430, 12586276357591230339), StkRfcmCommunicationsTransceiverModel)
agcls.AgTypeNameMap["StkRfcmCommunicationsTransceiverModel"] = StkRfcmCommunicationsTransceiverModel

class StkRfcmRadarTransceiverModel(IStkRfcmTransceiverModel, SupportsDeleteCallback):
    """Properties for configuring a radar transceiver model."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_waveform_method_offset = 1
    _metadata = {
        "iid_data" : (5397355634120071946, 14881756830326487198),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarTransceiverModel)
    
    _get_waveform_metadata = { "offset" : _get_waveform_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def waveform(self) -> "StkRfcmRadarWaveform":
        """Get the radar transceiver's waveform settings."""
        return self._intf.get_property(StkRfcmRadarTransceiverModel._metadata, StkRfcmRadarTransceiverModel._get_waveform_metadata)

    _property_names[waveform] = "waveform"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarTransceiverModel."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarTransceiverModel)
        IStkRfcmTransceiverModel.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmTransceiverModel._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarTransceiverModel, [StkRfcmRadarTransceiverModel, IStkRfcmTransceiverModel])

agcls.AgClassCatalog.add_catalog_entry((5535067053932425138, 5002300541366460048), StkRfcmRadarTransceiverModel)
agcls.AgTypeNameMap["StkRfcmRadarTransceiverModel"] = StkRfcmRadarTransceiverModel

class StkRfcmRangeDopplerResponse(IStkRfcmResponse, SupportsDeleteCallback):
    """The properties for a range doppler channel characterization response."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_range_values_method_offset = 1
    _get_range_count_method_offset = 2
    _get_velocity_values_method_offset = 3
    _get_velocity_count_method_offset = 4
    _get_pulse_count_method_offset = 5
    _get_angular_velocity_method_offset = 6
    _metadata = {
        "iid_data" : (4709129566781506392, 18419786988973210803),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRangeDopplerResponse)
    
    _get_range_values_metadata = { "offset" : _get_range_values_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def range_values(self) -> list:
        """Get the range values."""
        return self._intf.get_property(StkRfcmRangeDopplerResponse._metadata, StkRfcmRangeDopplerResponse._get_range_values_metadata)

    _get_range_count_metadata = { "offset" : _get_range_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def range_count(self) -> int:
        """Get the range count."""
        return self._intf.get_property(StkRfcmRangeDopplerResponse._metadata, StkRfcmRangeDopplerResponse._get_range_count_metadata)

    _get_velocity_values_metadata = { "offset" : _get_velocity_values_method_offset,
            "arg_types" : (POINTER(agcom.LPSAFEARRAY),),
            "marshallers" : (agmarshall.LPSafearrayArg,) }
    @property
    def velocity_values(self) -> list:
        """Get the velocity values."""
        return self._intf.get_property(StkRfcmRangeDopplerResponse._metadata, StkRfcmRangeDopplerResponse._get_velocity_values_metadata)

    _get_velocity_count_metadata = { "offset" : _get_velocity_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def velocity_count(self) -> int:
        """Get the velocity count."""
        return self._intf.get_property(StkRfcmRangeDopplerResponse._metadata, StkRfcmRangeDopplerResponse._get_velocity_count_metadata)

    _get_pulse_count_metadata = { "offset" : _get_pulse_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def pulse_count(self) -> int:
        """Get the pulse count."""
        return self._intf.get_property(StkRfcmRangeDopplerResponse._metadata, StkRfcmRangeDopplerResponse._get_pulse_count_metadata)

    _get_angular_velocity_metadata = { "offset" : _get_angular_velocity_method_offset,
            "arg_types" : (POINTER(agcom.DOUBLE),),
            "marshallers" : (agmarshall.DoubleArg,) }
    @property
    def angular_velocity(self) -> float:
        """Get the angular velocity."""
        return self._intf.get_property(StkRfcmRangeDopplerResponse._metadata, StkRfcmRangeDopplerResponse._get_angular_velocity_metadata)

    _property_names[range_values] = "range_values"
    _property_names[range_count] = "range_count"
    _property_names[velocity_values] = "velocity_values"
    _property_names[velocity_count] = "velocity_count"
    _property_names[pulse_count] = "pulse_count"
    _property_names[angular_velocity] = "angular_velocity"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRangeDopplerResponse."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRangeDopplerResponse)
        IStkRfcmResponse.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmResponse._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRangeDopplerResponse, [StkRfcmRangeDopplerResponse, IStkRfcmResponse])

agcls.AgClassCatalog.add_catalog_entry((5543401830740382270, 3545126179169781131), StkRfcmRangeDopplerResponse)
agcls.AgTypeNameMap["StkRfcmRangeDopplerResponse"] = StkRfcmRangeDopplerResponse

class StkRfcmFrequencyPulseResponse(IStkRfcmResponse, SupportsDeleteCallback):
    """The properties for a frequency pulse channel characterization response."""

    _num_methods = 2
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_pulse_count_method_offset = 1
    _get_frequency_sample_count_method_offset = 2
    _metadata = {
        "iid_data" : (5226211774985697343, 303850293307315840),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmFrequencyPulseResponse)
    
    _get_pulse_count_metadata = { "offset" : _get_pulse_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def pulse_count(self) -> int:
        """Get the pulse count."""
        return self._intf.get_property(StkRfcmFrequencyPulseResponse._metadata, StkRfcmFrequencyPulseResponse._get_pulse_count_metadata)

    _get_frequency_sample_count_metadata = { "offset" : _get_frequency_sample_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def frequency_sample_count(self) -> int:
        """Get the frequency sample count."""
        return self._intf.get_property(StkRfcmFrequencyPulseResponse._metadata, StkRfcmFrequencyPulseResponse._get_frequency_sample_count_metadata)

    _property_names[pulse_count] = "pulse_count"
    _property_names[frequency_sample_count] = "frequency_sample_count"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmFrequencyPulseResponse."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmFrequencyPulseResponse)
        IStkRfcmResponse.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmResponse._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmFrequencyPulseResponse, [StkRfcmFrequencyPulseResponse, IStkRfcmResponse])

agcls.AgClassCatalog.add_catalog_entry((5371909063848130331, 188560514196819341), StkRfcmFrequencyPulseResponse)
agcls.AgTypeNameMap["StkRfcmFrequencyPulseResponse"] = StkRfcmFrequencyPulseResponse

class StkRfcmAnalysisLink(IStkRfcmAnalysisLink, SupportsDeleteCallback):
    """A transceiver link for an analysis."""
    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmAnalysisLink."""
        SupportsDeleteCallback.__init__(self)
        IStkRfcmAnalysisLink.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAnalysisLink._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmAnalysisLink, [IStkRfcmAnalysisLink])

agcls.AgClassCatalog.add_catalog_entry((5035691807805684055, 1039028034256790706), StkRfcmAnalysisLink)
agcls.AgTypeNameMap["StkRfcmAnalysisLink"] = StkRfcmAnalysisLink

class StkRfcmRadarSarAnalysisLink(IStkRfcmAnalysisLink, SupportsDeleteCallback):
    """Properties for a transceiver link for a Sar analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_image_location_name_method_offset = 1
    _metadata = {
        "iid_data" : (5684254587119606851, 6835131856690226323),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarSarAnalysisLink)
    
    _get_image_location_name_metadata = { "offset" : _get_image_location_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def image_location_name(self) -> str:
        """Get the analysis link image location name."""
        return self._intf.get_property(StkRfcmRadarSarAnalysisLink._metadata, StkRfcmRadarSarAnalysisLink._get_image_location_name_metadata)

    _property_names[image_location_name] = "image_location_name"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarSarAnalysisLink."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarSarAnalysisLink)
        IStkRfcmAnalysisLink.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAnalysisLink._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarSarAnalysisLink, [StkRfcmRadarSarAnalysisLink, IStkRfcmAnalysisLink])

agcls.AgClassCatalog.add_catalog_entry((5067638514630488731, 265473950441651589), StkRfcmRadarSarAnalysisLink)
agcls.AgTypeNameMap["StkRfcmRadarSarAnalysisLink"] = StkRfcmRadarSarAnalysisLink

class StkRfcmRadarISarAnalysisLink(IStkRfcmAnalysisLink, SupportsDeleteCallback):
    """Properties for a transceiver link for an ISar analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_target_object_path_method_offset = 1
    _metadata = {
        "iid_data" : (4668749688519013855, 7019281282042502068),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmRadarISarAnalysisLink)
    
    _get_target_object_path_metadata = { "offset" : _get_target_object_path_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def target_object_path(self) -> str:
        """Get the analysis link target object path."""
        return self._intf.get_property(StkRfcmRadarISarAnalysisLink._metadata, StkRfcmRadarISarAnalysisLink._get_target_object_path_metadata)

    _property_names[target_object_path] = "target_object_path"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmRadarISarAnalysisLink."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmRadarISarAnalysisLink)
        IStkRfcmAnalysisLink.__init__(self, source_object)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
        IStkRfcmAnalysisLink._private_init(self, intf)
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmRadarISarAnalysisLink, [StkRfcmRadarISarAnalysisLink, IStkRfcmAnalysisLink])

agcls.AgClassCatalog.add_catalog_entry((5167524712546203694, 8283996936521855423), StkRfcmRadarISarAnalysisLink)
agcls.AgTypeNameMap["StkRfcmRadarISarAnalysisLink"] = StkRfcmRadarISarAnalysisLink

class StkRfcmAnalysisLinkCollection(SupportsDeleteCallback):
    """Represents a collection of analysis links between transceivers objects."""

    _num_methods = 3
    _vtable_offset = IDispatch._vtable_offset + IDispatch._num_methods
    _get_count_method_offset = 1
    _item_method_offset = 2
    _get__new_enum_method_offset = 3
    _metadata = {
        "iid_data" : (5753809382164761882, 12578733845637557142),
        "vtable_reference" : IDispatch._vtable_offset + IDispatch._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmAnalysisLinkCollection)
    def __iter__(self):
        """Create an iterator for the StkRfcmAnalysisLinkCollection object."""
        self.__dict__["_enumerator"] = self._new_enum
        self._enumerator.reset()
        return self
    def __next__(self) -> "IStkRfcmAnalysisLink":
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
        return self._intf.get_property(StkRfcmAnalysisLinkCollection._metadata, StkRfcmAnalysisLinkCollection._get_count_metadata)

    _item_metadata = { "offset" : _item_method_offset,
            "arg_types" : (agcom.INT, POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IntArg, agmarshall.InterfaceOutArg,) }
    def item(self, index:int) -> "IStkRfcmAnalysisLink":
        """Given an index, returns the element in the collection."""
        return self._intf.invoke(StkRfcmAnalysisLinkCollection._metadata, StkRfcmAnalysisLinkCollection._item_metadata, index, OutArg())

    _get__new_enum_metadata = { "offset" : _get__new_enum_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.IEnumVariantArg,) }
    @property
    def _new_enum(self) -> EnumeratorProxy:
        """Return an enumerator for the collection."""
        return self._intf.get_property(StkRfcmAnalysisLinkCollection._metadata, StkRfcmAnalysisLinkCollection._get__new_enum_metadata)

    __getitem__ = item


    _property_names[count] = "count"
    _property_names[_new_enum] = "_new_enum"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmAnalysisLinkCollection."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmAnalysisLinkCollection)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmAnalysisLinkCollection, [StkRfcmAnalysisLinkCollection, ])

agcls.AgClassCatalog.add_catalog_entry((5590692282349627472, 14211210503561071262), StkRfcmAnalysisLinkCollection)
agcls.AgTypeNameMap["StkRfcmAnalysisLinkCollection"] = StkRfcmAnalysisLinkCollection

class StkRfcmAnalysis(SupportsDeleteCallback):
    """Properties of an analysis."""

    _num_methods = 1
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_analysis_link_collection_method_offset = 1
    _metadata = {
        "iid_data" : (5641135177332540089, 160659604875743665),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmAnalysis)
    
    _get_analysis_link_collection_metadata = { "offset" : _get_analysis_link_collection_method_offset,
            "arg_types" : (POINTER(agcom.PVOID),),
            "marshallers" : (agmarshall.InterfaceOutArg,) }
    @property
    def analysis_link_collection(self) -> "StkRfcmAnalysisLinkCollection":
        """Get the analysis link collection."""
        return self._intf.get_property(StkRfcmAnalysis._metadata, StkRfcmAnalysis._get_analysis_link_collection_metadata)

    _property_names[analysis_link_collection] = "analysis_link_collection"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmAnalysis."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmAnalysis)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmAnalysis, [StkRfcmAnalysis, ])

agcls.AgClassCatalog.add_catalog_entry((4803344109459367919, 15926375216492296123), StkRfcmAnalysis)
agcls.AgTypeNameMap["StkRfcmAnalysis"] = StkRfcmAnalysis

class StkRfcmGpuProperties(SupportsDeleteCallback):
    """Properties of a GPU that pertain to RF Channel Modeler."""

    _num_methods = 6
    _vtable_offset = IUnknown._vtable_offset + IUnknown._num_methods
    _get_name_method_offset = 1
    _get_compute_capability_method_offset = 2
    _get_device_id_method_offset = 3
    _get_processor_count_method_offset = 4
    _get_speed_m_hz_method_offset = 5
    _get_memory_gb_method_offset = 6
    _metadata = {
        "iid_data" : (4721899476075187212, 4888009188086501010),
        "vtable_reference" : IUnknown._vtable_offset + IUnknown._num_methods - 1,
    }
    _property_names = {}
    def _get_property(self, attrname):
        return get_interface_property(attrname, StkRfcmGpuProperties)
    
    _get_name_metadata = { "offset" : _get_name_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def name(self) -> str:
        """Get the GPU name."""
        return self._intf.get_property(StkRfcmGpuProperties._metadata, StkRfcmGpuProperties._get_name_metadata)

    _get_compute_capability_metadata = { "offset" : _get_compute_capability_method_offset,
            "arg_types" : (POINTER(agcom.BSTR),),
            "marshallers" : (agmarshall.BStrArg,) }
    @property
    def compute_capability(self) -> str:
        """Get the GPU compute capability."""
        return self._intf.get_property(StkRfcmGpuProperties._metadata, StkRfcmGpuProperties._get_compute_capability_metadata)

    _get_device_id_metadata = { "offset" : _get_device_id_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def device_id(self) -> int:
        """Get the GPU device ID."""
        return self._intf.get_property(StkRfcmGpuProperties._metadata, StkRfcmGpuProperties._get_device_id_metadata)

    _get_processor_count_metadata = { "offset" : _get_processor_count_method_offset,
            "arg_types" : (POINTER(agcom.INT),),
            "marshallers" : (agmarshall.IntArg,) }
    @property
    def processor_count(self) -> int:
        """Get the GPU processor count."""
        return self._intf.get_property(StkRfcmGpuProperties._metadata, StkRfcmGpuProperties._get_processor_count_metadata)

    _get_speed_m_hz_metadata = { "offset" : _get_speed_m_hz_method_offset,
            "arg_types" : (POINTER(agcom.FLOAT),),
            "marshallers" : (agmarshall.FloatArg,) }
    @property
    def speed_m_hz(self) -> float:
        """Get the GPU speed in MHz."""
        return self._intf.get_property(StkRfcmGpuProperties._metadata, StkRfcmGpuProperties._get_speed_m_hz_metadata)

    _get_memory_gb_metadata = { "offset" : _get_memory_gb_method_offset,
            "arg_types" : (POINTER(agcom.FLOAT),),
            "marshallers" : (agmarshall.FloatArg,) }
    @property
    def memory_gb(self) -> float:
        """Get the GPU memory in GB."""
        return self._intf.get_property(StkRfcmGpuProperties._metadata, StkRfcmGpuProperties._get_memory_gb_metadata)

    _property_names[name] = "name"
    _property_names[compute_capability] = "compute_capability"
    _property_names[device_id] = "device_id"
    _property_names[processor_count] = "processor_count"
    _property_names[speed_m_hz] = "speed_m_hz"
    _property_names[memory_gb] = "memory_gb"

    def __init__(self, source_object=None):
        """Construct an object of type StkRfcmGpuProperties."""
        SupportsDeleteCallback.__init__(self)
        initialize_from_source_object(self, source_object, StkRfcmGpuProperties)
    def _private_init(self, intf:InterfaceProxy):
        self.__dict__["_intf"] = intf
    def __eq__(self, other):
        """Check equality of the underlying STK references."""
        return agcls.compare_com_objects(self, other)
    def __setattr__(self, attrname, value):
        """Attempt to assign an attribute."""
        set_class_attribute(self, attrname, value, StkRfcmGpuProperties, [StkRfcmGpuProperties, ])

agcls.AgClassCatalog.add_catalog_entry((4745059216132635585, 4320058157532729488), StkRfcmGpuProperties)
agcls.AgTypeNameMap["StkRfcmGpuProperties"] = StkRfcmGpuProperties


################################################################################
#          Copyright 2020-2023, Ansys Government Initiatives
################################################################################
