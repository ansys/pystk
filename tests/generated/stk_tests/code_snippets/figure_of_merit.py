from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class FigureOfMerit(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_CovDefObject = None
        super(FigureOfMerit, self).__init__(*args, **kwargs)

    m_CovDefDefaultName: str = "cd1"

    m_Object: "IFigureOfMerit" = None
    m_DefaultName: str = "fom1"

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
        self.m_CovDefObject = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eCoverageDefinition, FigureOfMerit.m_CovDefDefaultName
            ),
            ICoverageDefinition,
        )
        covdefObject = clr.CastAs(self.m_CovDefObject, IStkObject)
        FigureOfMerit.m_Object = clr.CastAs(
            covdefObject.Children.New(AgESTKObjectType.eFigureOfMerit, FigureOfMerit.m_DefaultName), IFigureOfMerit
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        covdefObject = clr.CastAs(self.m_CovDefObject, IStkObject)
        covdefObject.Children.Unload(AgESTKObjectType.eFigureOfMerit, FigureOfMerit.m_DefaultName)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eCoverageDefinition, FigureOfMerit.m_CovDefDefaultName
        )
        FigureOfMerit.m_Object = None
        self.m_CovDefObject = None
        if TestBase.Application.CurrentScenario.Children.Contains(AgESTKObjectType.eFacility, "Facility1"):
            TestBase.Application.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "Facility1")

    # endregion

    # region CreateFigureOfMeritOnCoverageDefinition
    def test_CreateFigureOfMeritOnCoverageDefinition(self):
        self.CreateFigureOfMeritOnCoverageDefinition(self.m_CovDefObject)

    def CreateFigureOfMeritOnCoverageDefinition(self, covdef: "ICoverageDefinition"):
        # Get the coverage definition as a IAgStkObject interface
        covdefObject = clr.CastAs(covdef, IStkObject)

        # Create the figure of merit
        fom = clr.CastAs(covdefObject.Children.New(AgESTKObjectType.eFigureOfMerit, "MyFigureOfMerit"), IFigureOfMerit)

    # endregion

    # region ConfigureAccessDurationFigureOfMerit
    def test_ConfigureAccessDurationFigureOfMerit(self):
        self.ConfigureAccessDurationFigureOfMerit(FigureOfMerit.m_Object)

    def ConfigureAccessDurationFigureOfMerit(self, fom: "IFigureOfMerit"):
        # Set figure of merit definition to eFmAccessDuration
        fom.SetDefinitionType(AgEFmDefinitionType.eFmAccessDuration)

        # Get IAgFmDefCompute interface
        defComp = clr.CastAs(fom.Definition, IFigureOfMeritDefinitionCompute)
        if defComp.IsComputeTypeSupported(AgEFmCompute.ePercentAbove):
            # Set Compute type to supported compute option
            defComp.SetComputeType(AgEFmCompute.ePercentAbove)

            # Get compute option compute interface
            fomData = clr.CastAs(defComp.Compute, IFigureOfMeritDefinitionDataPercentLevel)
            fomData.PercentLevel = 0.25

    # endregion

    # region ConfigureCoverageTimeFigureOfMerit
    def test_ConfigureCoverageTimeFigureOfMerit(self):
        self.ConfigureCoverageTimeFigureOfMerit(FigureOfMerit.m_Object)

    def ConfigureCoverageTimeFigureOfMerit(self, fom: "IFigureOfMerit"):
        # Set figure of merit definition to eFmCoverageTime
        fom.SetDefinitionType(AgEFmDefinitionType.eFmCoverageTime)

        # Get IAgFmDefCompute interface
        defComp = clr.CastAs(fom.Definition, IFigureOfMeritDefinitionCompute)
        if defComp.IsComputeTypeSupported(AgEFmCompute.eTotalTimeAbove):
            # Set Compute type to supported compute option
            defComp.SetComputeType(AgEFmCompute.eTotalTimeAbove)

            # Get compute option compute interface
            fomData = clr.CastAs(defComp.Compute, IFigureOfMeritDefinitionDataMinAssets)
            fomData.MinAssets = 15

    # endregion

    # region SetFigureOfMeritDefToAccessConstraintByEnum
    def test_SetFigureOfMeritDefToAccessConstraintByEnum(self):
        self.SetFigureOfMeritDefToAccessConstraintByEnum(FigureOfMerit.m_Object)

    def SetFigureOfMeritDefToAccessConstraintByEnum(self, fom: "IFigureOfMerit"):
        acd = fom.SetAccessConstraintDefinition(AgEFmConstraintName.eFmAzimuthRate)

    # endregion

    # region SetFigureOfMeritDefToAccessConstraintByName
    def test_SetFigureOfMeritDefToAccessConstraintByName(self):
        self.SetFigureOfMeritDefToAccessConstraintByName(FigureOfMerit.m_Object)

    def SetFigureOfMeritDefToAccessConstraintByName(self, fom: "IFigureOfMerit"):
        defAccessCnstr = fom.SetAccessConstraintDefinitionName("AzimuthRate")

        # Confiure access constraint properties
        defAccessCnstr.SetComputeType(AgEFmCompute.eMaximum)
        defAccessCnstr.AcrossAssets = AgEFmAcrossAssets.eFmMinimum
        defAccessCnstr.TimeStep = 60.0

    # endregion

    # region ConfigureFigureOfMeritDefToAccessConstraint
    def test_ConfigureFigureOfMeritDefToAccessConstraint(self):
        self.ConfigureFigureOfMeritDefToAccessConstraint(FigureOfMerit.m_Object)

    def ConfigureFigureOfMeritDefToAccessConstraint(self, fom: "IFigureOfMerit"):
        # Set access constraint definition to altitude
        fom.SetAccessConstraintDefinition(AgEFmConstraintName.eFmAltitude)

        # Get IAgFmDefAccessConstraint interface
        defAccessCnstr = clr.CastAs(fom.Definition, IFigureOfMeritDefinitionAccessConstraint)

        # Confiure access constraint properties
        defAccessCnstr.SetComputeType(AgEFmCompute.eMaximum)
        defAccessCnstr.AcrossAssets = AgEFmAcrossAssets.eFmMinimum
        defAccessCnstr.TimeStep = 60.0

    # endregion

    # region InspectGridWithSelectPoint
    def test_InspectGridWithSelectPoint(self):
        self.InspectGridWithSelectPoint(FigureOfMerit.m_Object)

    def InspectGridWithSelectPoint(self, fom: "IFigureOfMerit"):
        gridInspector = fom.GridInspector
        gridInspector.SelectPoint(-13.864, -51.088)

        pointFom = clr.CastAs(gridInspector.PointFOM, IDataProviderTimeVarying)
        pointFomResult = pointFom.ExecSingle("1 Jan 2012 12:00:00.00")

        pointSatisfaction = clr.CastAs(gridInspector.PointSatisfaction, IDataProviderInterval)
        pointSatisfactionResult = pointSatisfaction.Exec("1 Jan 2012 12:00:00.00", "2 Jan 2012 12:00:00.00")

        regionFom = clr.CastAs(gridInspector.RegionFOM, IDataProviderTimeVarying)
        regionFomResult = regionFom.ExecSingle("1 Jan 2012 12:00:00.00")

        regionSatisfaction = clr.CastAs(gridInspector.RegionSatisfaction, IDataProviderInterval)
        regionSatisfactionResult = regionSatisfaction.Exec("1 Jan 2012 12:00:00.00", "2 Jan 2012 12:00:00.00")

    # endregion

    # region ConfigureFigureOfMeritContours
    @category("Graphics Tests")
    def test_ConfigureFigureOfMeritContours(self):
        FigureOfMerit.m_Object.SetAccessConstraintDefinitionName("AzimuthRate")
        self.ConfigureFigureOfMeritContours(FigureOfMerit.m_Object.Graphics.Static.Contours)

    def ConfigureFigureOfMeritContours(self, contours: "IFigureOfMeritGfxContours"):
        contours.IsVisible = True
        contours.ContourType = AgEFmGfxContourType.eSmoothFill
        contours.ColorMethod = AgEFmGfxColorMethod.eExplicit

        # Add level ranges (batch)
        contours.LevelAttributes.AddLevelRange(25, 35, 1)
        firstLevel = contours.LevelAttributes[0]
        firstLevel.Color = Color.Blue

        # Add one level (individually)
        level = contours.LevelAttributes.AddLevel(55)
        level.Color = Color.Red

    # endregion

    # region FigureOfMeritDefinitionAgeOfData
    def test_FigureOfMeritDefinitionAgeOfData(self):
        self.FigureOfMeritDefinitionAgeOfData(FigureOfMerit.m_Object)

    def FigureOfMeritDefinitionAgeOfData(self, fom: "IFigureOfMerit"):
        # Get the IAgFmDefAgeOfData interface
        fom.SetDefinitionType(AgEFmDefinitionType.eFmAgeOfData)
        ageOfData = clr.CastAs(fom.Definition, IFigureOfMeritDefinitionAgeOfData)

        # Set the minimum number of assets for computing
        ageOfData.MinAssets = 2

    # endregion

    # region FigureOfMeritDefinitionScalarCalculation
    def test_FigureOfMeritDefinitionScalarCalculation(self):
        self.FigureOfMeritDefinitionScalarCalculation(FigureOfMerit.m_Object)

    def FigureOfMeritDefinitionScalarCalculation(self, fom: "IFigureOfMerit"):
        # Set the Scalar Calculation definition.
        scalarCalculation = fom.SetScalarCalculationDefinition("CentralBody/Earth ElapsedTimeFromStart")

    # endregion

    # region FigureOfMeritDefinitionScalarCalculationFromVGT
    def test_FigureOfMeritDefinitionScalarCalculationFromVGT(self):
        self.FigureOfMeritDefinitionScalarCalculationFromVGT(
            FigureOfMerit.m_Object, clr.Convert(TestBase.Application, IStkObjectRoot)
        )

    def FigureOfMeritDefinitionScalarCalculationFromVGT(self, fom: "IFigureOfMerit", stkRoot: "IStkObjectRoot"):
        # Get the qualified path of a Scalar Calculation (e.g.
        provider = stkRoot.VgtRoot.GetProvider("CentralBody/Sun")
        calcScalar = provider.CalcScalars[0]
        calcScalarQualifiedPath = (clr.CastAs(calcScalar, IAnalysisWorkbenchComponent)).QualifiedPath

        # Set the Scalar Calculation definition using the qualified path
        scalarCalculation = fom.SetScalarCalculationDefinition(calcScalarQualifiedPath)

    # endregion

    # region FigureOfMeritDefinitionSystemResponseTime
    def test_FigureOfMeritDefinitionSystemResponseTime(self):
        TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility1")
        self.FigureOfMeritDefinitionSystemResponseTime(FigureOfMerit.m_Object)

    def FigureOfMeritDefinitionSystemResponseTime(self, fom: "IFigureOfMerit"):
        fom.SetDefinitionType(AgEFmDefinitionType.eFmSystemResponseTime)
        systemResponseTime = clr.CastAs(fom.Definition, IFigureOfMeritDefinitionSystemResponseTime)

        systemResponseTime.CommandStationPath = r"/Application/STK/Scenario/CodeSnippetScenario/Facility/Facility1"

    # endregion

    # region FigureOfMeritDefinitionSystemResponseTimeReset
    def test_FigureOfMeritDefinitionSystemResponseTimeReset(self):
        TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility1")
        self.FigureOfMeritDefinitionSystemResponseTimeReset(FigureOfMerit.m_Object)

    def FigureOfMeritDefinitionSystemResponseTimeReset(self, fom: "IFigureOfMerit"):
        fom.SetDefinitionType(AgEFmDefinitionType.eFmSystemResponseTime)
        systemResponseTime = clr.CastAs(fom.Definition, IFigureOfMeritDefinitionSystemResponseTime)

        systemResponseTime.CommandStationPath = "NONE"

    # endregion
