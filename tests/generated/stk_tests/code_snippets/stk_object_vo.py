from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


@category("Graphics Tests")
class StkObjectVO(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkObjectVO, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region ConfigureVOModelFile
    def test_ConfigureVOModelFile(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "satellite1"),
            ISatellite,
        )
        model: "IGraphics3DModel" = satellite.graphics_3d.model

        self.ConfigureVOModelFile(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "satellite1")

    def ConfigureVOModelFile(self, model: "IGraphics3DModel"):
        # Set new ModelFile.Filename
        model.model_type = MODEL_TYPE.FILE
        modelFile: "IGraphics3DModelFile" = clr.CastAs(model.model_data, IGraphics3DModelFile)
        modelFile.filename = r"\STKData\VO\Models\Space\alexis.mdl"

        # Configure basic settings
        model.visible = True
        model.scale_value = 4.8

    # endregion

    # region ConfigureVOArticulations
    def test_ConfigureVOArticulations(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "satellite1"),
            ISatellite,
        )
        model: "IGraphics3DModel" = satellite.graphics_3d.model

        # Set new ModelFile.Filename
        model.model_type = MODEL_TYPE.FILE
        modelFile: "IGraphics3DModelFile" = clr.CastAs(model.model_data, IGraphics3DModelFile)
        modelFile.filename = r"\STKData\VO\Models\Space\satellite.dae"

        self.ConfigureVOModelArticulations(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "satellite1")

    def ConfigureVOModelArticulations(self, model: "IGraphics3DModel"):
        # Configure articulation
        modelArticulation: "IGraphics3DModelArtic" = model.articulation
        modelArticulation.enable_default_save = False
        modelArticulation.save_artic_file_on_save = True

        # Set our articulation and transformations
        # For this sample, these articulations exist for a default satellite model
        levelOfDetail: int = 0
        articulation: str = "Satellite"
        transformation: str = "Size"

        # Get the current transition value
        currentTransVal: float = modelArticulation.get_transformation_value(levelOfDetail, articulation, transformation)

        # Change the value
        newTransVal: float = currentTransVal * 0.5

        # Set our new transition value
        modelArticulation.set_transformation_value(levelOfDetail, articulation, transformation, newTransVal)

    # endregion

    # region ListVOModelArticulations
    def test_ListVOModelArticulations(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "satellite1"),
            ISatellite,
        )
        model: "IGraphics3DModel" = satellite.graphics_3d.model

        self.ListVOModelArticulations(satellite, model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "satellite1")

    def ListVOModelArticulations(self, satellite: "ISatellite", model: "IGraphics3DModel"):
        # Enumerating through the transformation collection is helpful if you do not
        # know what tranformations exist or their value ranges

        modelArticulation: "IGraphics3DModelArtic" = model.articulation

        lod: int = 0
        while lod < modelArticulation.lod_count:
            # Get all articulations
            # GetAvailableArticulations returns a one dimensional array of articulation names
            articulations = modelArticulation.get_available_articulations(lod)

            articulation: int = 0
            while articulation < Array.Length(articulations):
                # We need the articulation string to call the GetAvailableTransformations function
                articulationString: str = str(articulations[articulation])

                # Get all transformations
                transformations: "IGraphics3DModelTransformationCollection" = (
                    modelArticulation.get_available_transformations(lod, articulationString)
                )

                # Enumerate through available transformations
                trans: "IGraphics3DModelTransformation"

                # Enumerate through available transformations
                for trans in transformations:
                    Console.WriteLine(
                        "Name: {0}, Current {1}, Max {2}, Min {3}", trans.name, trans.value, trans.max, trans.min
                    )

                articulation += 1

            lod += 1

    # endregion

    # region ConfigureVOModelLevelOfDetail
    def test_ConfigureVOModelLevelOfDetail(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "satellite1"),
            ISatellite,
        )
        model: "IGraphics3DModel" = satellite.graphics_3d.model

        self.ConfigureVOModelLevelOfDetail(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "satellite1")

    def ConfigureVOModelLevelOfDetail(self, model: "IGraphics3DModel"):
        # Configure level of details
        detail: "IGraphics3DDetailThreshold" = model.detail_threshold
        detail.enable_detail_threshold = True

        # (assuming unit preferences set to km)
        detail.all = 2.51189
        detail.model_label = 158489
        detail.marker_label = 2511890.0
        detail.marker = 25110000.0
        detail.point = 1000000000000.0

    # endregion

    # region ConfigureVOVector
    def test_ConfigureVOVector(self):
        vehicle: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            IGroundVehicle,
        )

        self.ConfigureVOVector(vehicle.graphics_3d.vector)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1")

    def ConfigureVOVector(self, vector: "IGraphics3DVector"):
        # See AvailableCrdns for supported elements
        vector.reference_crdns.add(
            GEOMETRIC_ELEM_TYPE.VECTOR_ELEM,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.central_bodies["Earth"].vgt.vectors["Moon"], IAnalysisWorkbenchComponent
                )
            ).qualified_path,
        )
        vector.reference_crdns.add(
            GEOMETRIC_ELEM_TYPE.AXES_ELEM,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.central_bodies["Moon"].vgt.vectors["Position"],
                    IAnalysisWorkbenchComponent,
                )
            ).qualified_path,
        )
        vector.reference_crdns.add(
            GEOMETRIC_ELEM_TYPE.VECTOR_ELEM,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.central_bodies["Sun"].vgt.vectors["Velocity(Barycenter)"],
                    IAnalysisWorkbenchComponent,
                )
            ).qualified_path,
        )

        # Draw on Central Body
        body: "IGraphics3DReferenceVectorGeometryToolVector" = clr.CastAs(
            vector.reference_crdns.get_crdn_by_name(
                GEOMETRIC_ELEM_TYPE.AXES_ELEM,
                (
                    clr.Convert(
                        CodeSnippetsTestBase.m_Root.central_bodies["Earth"].vgt.vectors["Moon"],
                        IAnalysisWorkbenchComponent,
                    )
                ).qualified_path,
            ),
            IGraphics3DReferenceVectorGeometryToolVector,
        )
        (clr.Convert(body, IGraphics3DReferenceAnalysisWorkbenchComponent)).color = Color.Yellow
        body.draw_at_cb = True
        body.axes = "CentralBody/Earth Fixed Axes"

        vector.scale_relative_to_model = True
        vector.angle_size_scale = 4.5

    # endregion

    # region ConfigureVODataDisplay
    def test_ConfigureVODataDisplay(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), ISatellite
        )
        (clr.Convert(sat, ISatellite)).set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        tb: "IVehiclePropagatorTwoBody" = clr.CastAs(
            (clr.Convert(sat, ISatellite)).propagator, IVehiclePropagatorTwoBody
        )
        tb.propagate()
        ddc: "IGraphics3DDataDisplayCollection" = sat.graphics_3d.data_display
        self.ConfigureVODataDisplay(ddc)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")

    def ConfigureVODataDisplay(self, datadisplaycol: "IGraphics3DDataDisplayCollection"):
        # Add existing data display
        # See AvailableData property for available data display
        displayElement: "IGraphics3DDataDisplayElement" = datadisplaycol.add("Solar Intensity")

        # Configure data display as needed
        displayElement.title_text = "Sol. Intensity"
        displayElement.is_visible = True
        displayElement.location = GRAPHICS_3D_LOCATION.WINDOW_3D
        displayElement.font_color = Color.White
        displayElement.font_size = GRAPHICS_3D_FONT_SIZE.SMALL
        displayElement.use_background = True
        displayElement.bg_color = Color.Orange
        displayElement.use_auto_size_width = False
        displayElement.use_auto_size_height = False
        displayElement.bg_height = 55
        displayElement.bg_width = 260
        displayElement.background_translucency = 0.5
        displayElement.use_background_texture = False
        displayElement.use_background_border = True
        displayElement.background_border_color = Color.White

    # endregion
