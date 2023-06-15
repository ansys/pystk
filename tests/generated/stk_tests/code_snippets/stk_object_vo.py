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
        satellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        model = satellite.VO.Model

        self.ConfigureVOModelFile(model)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "satellite1")

    def ConfigureVOModelFile(self, model: "IVOModel"):
        # Set new ModelFile.Filename
        model.ModelType = AgEModelType.eModelFile
        modelFile = clr.CastAs(model.ModelData, IVOModelFile)
        modelFile.Filename = r"\STKData\VO\Models\Space\alexis.mdl"

        # Configure basic settings
        model.Visible = True
        model.ScaleValue = 4.8

    # endregion

    # region ConfigureVOArticulations
    def test_ConfigureVOArticulations(self):
        satellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        model = satellite.VO.Model

        # Set new ModelFile.Filename
        model.ModelType = AgEModelType.eModelFile
        modelFile = clr.CastAs(model.ModelData, IVOModelFile)
        modelFile.Filename = r"\STKData\VO\Models\Space\satellite.dae"

        self.ConfigureVOModelArticulations(model)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "satellite1")

    def ConfigureVOModelArticulations(self, model: "IVOModel"):
        # Configure articulation
        modelArticulation = model.Articulation
        modelArticulation.EnableDefaultSave = False
        modelArticulation.SaveArticFileOnSave = True

        # Set our articulation and transformations
        # For this sample, these articulations exist for a default satellite model
        levelOfDetail = 0
        articulation = "Satellite"
        transformation = "Size"

        # Get the current transition value
        currentTransVal = modelArticulation.GetTransValue(levelOfDetail, articulation, transformation)

        # Change the value
        newTransVal = currentTransVal * 0.5

        # Set our new transition value
        modelArticulation.SetTransValue(levelOfDetail, articulation, transformation, newTransVal)

    # endregion

    # region ListVOModelArticulations
    def test_ListVOModelArticulations(self):
        satellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        model = satellite.VO.Model

        self.ListVOModelArticulations(satellite, model)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "satellite1")

    def ListVOModelArticulations(self, satellite: "ISatellite", model: "IVOModel"):
        # Enumerating through the transformation collection is helpful if you do not
        # know what tranformations exist or their value ranges

        modelArticulation = model.Articulation

        lod = 0
        while lod < modelArticulation.LODCount:
            # Get all articulations
            # GetAvailableArticulations returns a one dimensional array of articulation names
            articulations = modelArticulation.GetAvailableArticulations(lod)

            articulation = 0
            while articulation < Array.Length(articulations):
                # We need the articulation string to call the GetAvailableTransformations function
                articulationString = str(articulations[articulation])

                # Get all transformations
                transformations = modelArticulation.GetAvailableTransformations(lod, articulationString)

                # Enumerate through available transformations
                for trans in transformations:
                    Console.WriteLine(
                        "Name: {0}, Current {1}, Max {2}, Min {3}", trans.Name, trans.Value, trans.Max, trans.Min
                    )

                articulation += 1

            lod += 1

    # endregion

    # region ConfigureVOModelLevelOfDetail
    def test_ConfigureVOModelLevelOfDetail(self):
        satellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        model = satellite.VO.Model

        self.ConfigureVOModelLevelOfDetail(model)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "satellite1")

    def ConfigureVOModelLevelOfDetail(self, model: "IVOModel"):
        # Configure level of details
        detail = model.DetailThreshold
        detail.EnableDetailThreshold = True

        # (assuming unit preferences set to km)
        detail.All = 2.51189
        detail.ModelLabel = 158489
        detail.MarkerLabel = 2511890.0
        detail.Marker = 25110000.0
        detail.Point = 1000000000000.0

    # endregion

    # region ConfigureVOVector
    def test_ConfigureVOVector(self):
        vehicle = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )

        self.ConfigureVOVector(vehicle.VO.Vector)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eGroundVehicle, "gv1")

    def ConfigureVOVector(self, vector: "IVOVector"):
        # See AvailableCrdns for supported elements
        vector.RefCrdns.Add(
            AgEGeometricElemType.eVectorElem,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.CentralBodies["Earth"].Vgt.Vectors["Moon"], IAnalysisWorkbenchComponent
                )
            ).QualifiedPath,
        )
        vector.RefCrdns.Add(
            AgEGeometricElemType.eAxesElem,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.CentralBodies["Moon"].Vgt.Vectors["Position"],
                    IAnalysisWorkbenchComponent,
                )
            ).QualifiedPath,
        )
        vector.RefCrdns.Add(
            AgEGeometricElemType.eVectorElem,
            (
                clr.Convert(
                    CodeSnippetsTestBase.m_Root.CentralBodies["Sun"].Vgt.Vectors["Velocity(Barycenter)"],
                    IAnalysisWorkbenchComponent,
                )
            ).QualifiedPath,
        )

        # Draw on Central Body
        body = clr.CastAs(
            vector.RefCrdns.GetCrdnByName(
                AgEGeometricElemType.eAxesElem,
                (
                    clr.Convert(
                        CodeSnippetsTestBase.m_Root.CentralBodies["Earth"].Vgt.Vectors["Moon"],
                        IAnalysisWorkbenchComponent,
                    )
                ).QualifiedPath,
            ),
            IVOReferenceVectorGeometryToolVector,
        )
        (clr.Convert(body, IVOReferenceAnalysisWorkbenchComponent)).Color = Color.Yellow
        body.DrawAtCB = True
        body.Axes = "CentralBody/Earth Fixed Axes"

        vector.ScaleRelativeToModel = True
        vector.AngleSizeScale = 4.5

    # endregion

    # region ConfigureVODataDisplay
    def test_ConfigureVODataDisplay(self):
        sat = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        (clr.Convert(sat, ISatellite)).SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        tb = clr.CastAs((clr.Convert(sat, ISatellite)).Propagator, IVehiclePropagatorTwoBody)
        tb.Propagate()
        ddc = sat.VO.DataDisplay
        self.ConfigureVODataDisplay(ddc)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")

    def ConfigureVODataDisplay(self, datadisplaycol: "IVODataDisplayCollection"):
        # Add existing data display
        # See AvailableData property for available data display
        displayElement = datadisplaycol.Add("Solar Intensity")

        # Configure data display as needed
        displayElement.TitleText = "Sol. Intensity"
        displayElement.IsVisible = True
        displayElement.Location = AgEVOLocation.e3DWindow
        displayElement.FontColor = Color.White
        displayElement.FontSize = AgEVOFontSize.eSmall
        displayElement.UseBackground = True
        displayElement.BgColor = Color.Orange
        displayElement.UseAutoSizeWidth = False
        displayElement.UseAutoSizeHeight = False
        displayElement.BgHeight = 55
        displayElement.BgWidth = 260
        displayElement.BackgroundTranslucency = 0.5
        displayElement.UseBackgroundTexture = False
        displayElement.UseBackgroundBorder = True
        displayElement.BackgroundBorderColor = Color.White

    # endregion
