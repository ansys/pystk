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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        model: "IVOModel" = satellite.vo.model

        self.ConfigureVOModelFile(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "satellite1")

    def ConfigureVOModelFile(self, model: "IVOModel"):
        # Set new ModelFile.Filename
        model.model_type = AgEModelType.eModelFile
        modelFile: "IVOModelFile" = clr.CastAs(model.model_data, IVOModelFile)
        modelFile.filename = r"\STKData\VO\Models\Space\alexis.mdl"

        # Configure basic settings
        model.visible = True
        model.scale_value = 4.8

    # endregion

    # region ConfigureVOArticulations
    def test_ConfigureVOArticulations(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        model: "IVOModel" = satellite.vo.model

        # Set new ModelFile.Filename
        model.model_type = AgEModelType.eModelFile
        modelFile: "IVOModelFile" = clr.CastAs(model.model_data, IVOModelFile)
        modelFile.filename = r"\STKData\VO\Models\Space\satellite.dae"

        self.ConfigureVOModelArticulations(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "satellite1")

    def ConfigureVOModelArticulations(self, model: "IVOModel"):
        # Configure articulation
        modelArticulation: "IVOModelArtic" = model.articulation
        modelArticulation.enable_default_save = False
        modelArticulation.save_artic_file_on_save = True

        # Set our articulation and transformations
        # For this sample, these articulations exist for a default satellite model
        levelOfDetail: int = 0
        articulation: str = "Satellite"
        transformation: str = "Size"

        # Get the current transition value
        currentTransVal: float = modelArticulation.get_trans_value(levelOfDetail, articulation, transformation)

        # Change the value
        newTransVal: float = currentTransVal * 0.5

        # Set our new transition value
        modelArticulation.set_trans_value(levelOfDetail, articulation, transformation, newTransVal)

    # endregion

    # region ListVOModelArticulations
    def test_ListVOModelArticulations(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        model: "IVOModel" = satellite.vo.model

        self.ListVOModelArticulations(satellite, model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "satellite1")

    def ListVOModelArticulations(self, satellite: "ISatellite", model: "IVOModel"):
        # Enumerating through the transformation collection is helpful if you do not
        # know what tranformations exist or their value ranges

        modelArticulation: "IVOModelArtic" = model.articulation

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
                transformations: "IVOModelTransformationCollection" = modelArticulation.get_available_transformations(
                    lod, articulationString
                )

                # Enumerate through available transformations
                trans: "IVOModelTransformation"

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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        model: "IVOModel" = satellite.vo.model

        self.ConfigureVOModelLevelOfDetail(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "satellite1")

    def ConfigureVOModelLevelOfDetail(self, model: "IVOModel"):
        # Configure level of details
        detail: "IVODetailThreshold" = model.detail_threshold
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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )

        self.ConfigureVOVector(vehicle.vo.vector)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eGroundVehicle, "gv1")

    def ConfigureVOVector(self, vector: "IVOVector"):
        # See AvailableCrdns for supported elements
        vector.ref_crdns.add(
            AgEGeometricElemType.eVectorElem,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.central_bodies["Earth"].vgt.vectors["Moon"], IAnalysisWorkbenchComponent
                )
            ).qualified_path,
        )
        vector.ref_crdns.add(
            AgEGeometricElemType.eAxesElem,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.central_bodies["Moon"].vgt.vectors["Position"],
                    IAnalysisWorkbenchComponent,
                )
            ).qualified_path,
        )
        vector.ref_crdns.add(
            AgEGeometricElemType.eVectorElem,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.central_bodies["Sun"].vgt.vectors["Velocity(Barycenter)"],
                    IAnalysisWorkbenchComponent,
                )
            ).qualified_path,
        )

        # Draw on Central Body
        body: "IVOReferenceVectorGeometryToolVector" = clr.CastAs(
            vector.ref_crdns.get_crdn_by_name(
                AgEGeometricElemType.eAxesElem,
                (
                    clr.Convert(
                        CodeSnippetsTestBase.m_Root.central_bodies["Earth"].vgt.vectors["Moon"],
                        IAnalysisWorkbenchComponent,
                    )
                ).qualified_path,
            ),
            IVOReferenceVectorGeometryToolVector,
        )
        (clr.Convert(body, IVOReferenceAnalysisWorkbenchComponent)).color = Color.Yellow
        body.draw_at_cb = True
        body.axes = "CentralBody/Earth Fixed Axes"

        vector.scale_relative_to_model = True
        vector.angle_size_scale = 4.5

    # endregion

    # region ConfigureVODataDisplay
    def test_ConfigureVODataDisplay(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        (clr.Convert(sat, ISatellite)).set_propagator_type(AgEVePropagatorType.ePropagatorTwoBody)
        tb: "IVehiclePropagatorTwoBody" = clr.CastAs(
            (clr.Convert(sat, ISatellite)).propagator, IVehiclePropagatorTwoBody
        )
        tb.propagate()
        ddc: "IVODataDisplayCollection" = sat.vo.data_display
        self.ConfigureVODataDisplay(ddc)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "sat1")

    def ConfigureVODataDisplay(self, datadisplaycol: "IVODataDisplayCollection"):
        # Add existing data display
        # See AvailableData property for available data display
        displayElement: "IVODataDisplayElement" = datadisplaycol.add("Solar Intensity")

        # Configure data display as needed
        displayElement.title_text = "Sol. Intensity"
        displayElement.is_visible = True
        displayElement.location = AgEVOLocation.e3DWindow
        displayElement.font_color = Color.White
        displayElement.font_size = AgEVOFontSize.eSmall
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
