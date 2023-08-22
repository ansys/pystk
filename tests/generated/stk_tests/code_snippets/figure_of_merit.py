from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class FigureOfMerit(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_CovDefObject: "ICoverageDefinition" = None
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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eCoverageDefinition, FigureOfMerit.m_CovDefDefaultName
            ),
            ICoverageDefinition,
        )
        covdefObject: "IStkObject" = clr.CastAs(self.m_CovDefObject, IStkObject)
        FigureOfMerit.m_Object = clr.CastAs(
            covdefObject.children.new(AgESTKObjectType.eFigureOfMerit, FigureOfMerit.m_DefaultName), IFigureOfMerit
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        covdefObject: "IStkObject" = clr.CastAs(self.m_CovDefObject, IStkObject)
        covdefObject.children.unload(AgESTKObjectType.eFigureOfMerit, FigureOfMerit.m_DefaultName)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eCoverageDefinition, FigureOfMerit.m_CovDefDefaultName
        )
        FigureOfMerit.m_Object = None
        self.m_CovDefObject = None
        if TestBase.Application.current_scenario.children.contains(AgESTKObjectType.eFacility, "Facility1"):
            TestBase.Application.current_scenario.children.unload(AgESTKObjectType.eFacility, "Facility1")

    # endregion

    # region CreateFigureOfMeritOnCoverageDefinition
    def test_CreateFigureOfMeritOnCoverageDefinition(self):
        self.CreateFigureOfMeritOnCoverageDefinition(self.m_CovDefObject)

    def CreateFigureOfMeritOnCoverageDefinition(self, covdef: "ICoverageDefinition"):
        # Get the coverage definition as a IStkObject interface
        covdefObject: "IStkObject" = clr.CastAs(covdef, IStkObject)

        # Create the figure of merit
        fom: "IFigureOfMerit" = clr.CastAs(
            covdefObject.children.new(AgESTKObjectType.eFigureOfMerit, "MyFigureOfMerit"), IFigureOfMerit
        )

    # endregion

    # region ConfigureAccessDurationFigureOfMerit
    def test_ConfigureAccessDurationFigureOfMerit(self):
        self.ConfigureAccessDurationFigureOfMerit(FigureOfMerit.m_Object)

    def ConfigureAccessDurationFigureOfMerit(self, fom: "IFigureOfMerit"):
        # Set figure of merit definition to eFmAccessDuration
        fom.set_definition_type(AgEFmDefinitionType.eFmAccessDuration)

        # Get IFigureOfMeritDefinitionCompute interface
        defComp: "IFigureOfMeritDefinitionCompute" = clr.CastAs(fom.definition, IFigureOfMeritDefinitionCompute)
        if defComp.is_compute_type_supported(AgEFmCompute.ePercentAbove):
            # Set Compute type to supported compute option
            defComp.set_compute_type(AgEFmCompute.ePercentAbove)

            # Get compute option compute interface
            fomData: "IFigureOfMeritDefinitionDataPercentLevel" = clr.CastAs(
                defComp.compute, IFigureOfMeritDefinitionDataPercentLevel
            )
            fomData.percent_level = 0.25

    # endregion

    # region ConfigureCoverageTimeFigureOfMerit
    def test_ConfigureCoverageTimeFigureOfMerit(self):
        self.ConfigureCoverageTimeFigureOfMerit(FigureOfMerit.m_Object)

    def ConfigureCoverageTimeFigureOfMerit(self, fom: "IFigureOfMerit"):
        # Set figure of merit definition to eFmCoverageTime
        fom.set_definition_type(AgEFmDefinitionType.eFmCoverageTime)

        # Get IFigureOfMeritDefinitionCompute interface
        defComp: "IFigureOfMeritDefinitionCompute" = clr.CastAs(fom.definition, IFigureOfMeritDefinitionCompute)
        if defComp.is_compute_type_supported(AgEFmCompute.eTotalTimeAbove):
            # Set Compute type to supported compute option
            defComp.set_compute_type(AgEFmCompute.eTotalTimeAbove)

            # Get compute option compute interface
            fomData: "IFigureOfMeritDefinitionDataMinAssets" = clr.CastAs(
                defComp.compute, IFigureOfMeritDefinitionDataMinAssets
            )
            fomData.min_assets = 15

    # endregion

    # region SetFigureOfMeritDefToAccessConstraintByEnum
    def test_SetFigureOfMeritDefToAccessConstraintByEnum(self):
        self.SetFigureOfMeritDefToAccessConstraintByEnum(FigureOfMerit.m_Object)

    def SetFigureOfMeritDefToAccessConstraintByEnum(self, fom: "IFigureOfMerit"):
        acd: "IFigureOfMeritDefinitionAccessConstraint" = fom.set_access_constraint_definition(
            AgEFmConstraintName.eFmAzimuthRate
        )

    # endregion

    # region SetFigureOfMeritDefToAccessConstraintByName
    def test_SetFigureOfMeritDefToAccessConstraintByName(self):
        self.SetFigureOfMeritDefToAccessConstraintByName(FigureOfMerit.m_Object)

    def SetFigureOfMeritDefToAccessConstraintByName(self, fom: "IFigureOfMerit"):
        defAccessCnstr: "IFigureOfMeritDefinitionAccessConstraint" = fom.set_access_constraint_definition_name(
            "AzimuthRate"
        )

        # Confiure access constraint properties
        defAccessCnstr.set_compute_type(AgEFmCompute.eMaximum)
        defAccessCnstr.across_assets = AgEFmAcrossAssets.eFmMinimum
        defAccessCnstr.time_step = 60.0

    # endregion

    # region ConfigureFigureOfMeritDefToAccessConstraint
    def test_ConfigureFigureOfMeritDefToAccessConstraint(self):
        self.ConfigureFigureOfMeritDefToAccessConstraint(FigureOfMerit.m_Object)

    def ConfigureFigureOfMeritDefToAccessConstraint(self, fom: "IFigureOfMerit"):
        # Set access constraint definition to altitude
        fom.set_access_constraint_definition(AgEFmConstraintName.eFmAltitude)

        # Get IFigureOfMeritDefinitionAccessConstraint interface
        defAccessCnstr: "IFigureOfMeritDefinitionAccessConstraint" = clr.CastAs(
            fom.definition, IFigureOfMeritDefinitionAccessConstraint
        )

        # Confiure access constraint properties
        defAccessCnstr.set_compute_type(AgEFmCompute.eMaximum)
        defAccessCnstr.across_assets = AgEFmAcrossAssets.eFmMinimum
        defAccessCnstr.time_step = 60.0

    # endregion

    # region InspectGridWithSelectPoint
    def test_InspectGridWithSelectPoint(self):
        self.InspectGridWithSelectPoint(FigureOfMerit.m_Object)

    def InspectGridWithSelectPoint(self, fom: "IFigureOfMerit"):
        gridInspector: "IFigureOfMeritGridInspector" = fom.grid_inspector
        gridInspector.select_point(-13.864, -51.088)

        pointFom: "IDataProviderTimeVarying" = clr.CastAs(gridInspector.point_fom, IDataProviderTimeVarying)
        pointFomResult: "IDataProviderResult" = pointFom.exec_single("1 Jan 2012 12:00:00.00")

        pointSatisfaction: "IDataProviderInterval" = clr.CastAs(gridInspector.point_satisfaction, IDataProviderInterval)
        pointSatisfactionResult: "IDataProviderResult" = pointSatisfaction.exec(
            "1 Jan 2012 12:00:00.00", "2 Jan 2012 12:00:00.00"
        )

        regionFom: "IDataProviderTimeVarying" = clr.CastAs(gridInspector.region_fom, IDataProviderTimeVarying)
        regionFomResult: "IDataProviderResult" = regionFom.exec_single("1 Jan 2012 12:00:00.00")

        regionSatisfaction: "IDataProviderInterval" = clr.CastAs(
            gridInspector.region_satisfaction, IDataProviderInterval
        )
        regionSatisfactionResult: "IDataProviderResult" = regionSatisfaction.exec(
            "1 Jan 2012 12:00:00.00", "2 Jan 2012 12:00:00.00"
        )

    # endregion

    # region ConfigureFigureOfMeritContours
    @category("Graphics Tests")
    def test_ConfigureFigureOfMeritContours(self):
        FigureOfMerit.m_Object.set_access_constraint_definition_name("AzimuthRate")
        self.ConfigureFigureOfMeritContours(FigureOfMerit.m_Object.graphics.static.contours)

    def ConfigureFigureOfMeritContours(self, contours: "IFigureOfMeritGfxContours"):
        contours.is_visible = True
        contours.contour_type = AgEFmGfxContourType.eSmoothFill
        contours.color_method = AgEFmGfxColorMethod.eExplicit

        # Add level ranges (batch)
        contours.level_attributes.add_level_range(25, 35, 1)
        firstLevel: "IFigureOfMeritGfxLevelAttributesElement" = contours.level_attributes[0]
        firstLevel.color = Color.Blue

        # Add one level (individually)
        level: "IFigureOfMeritGfxLevelAttributesElement" = contours.level_attributes.add_level(55)
        level.color = Color.Red

    # endregion

    # region FigureOfMeritDefinitionAgeOfData
    def test_FigureOfMeritDefinitionAgeOfData(self):
        self.FigureOfMeritDefinitionAgeOfData(FigureOfMerit.m_Object)

    def FigureOfMeritDefinitionAgeOfData(self, fom: "IFigureOfMerit"):
        # Get the IFigureOfMeritDefinitionAgeOfData interface
        fom.set_definition_type(AgEFmDefinitionType.eFmAgeOfData)
        ageOfData: "IFigureOfMeritDefinitionAgeOfData" = clr.CastAs(fom.definition, IFigureOfMeritDefinitionAgeOfData)

        # Set the minimum number of assets for computing
        ageOfData.min_assets = 2

    # endregion

    # region FigureOfMeritDefinitionScalarCalculation
    def test_FigureOfMeritDefinitionScalarCalculation(self):
        self.FigureOfMeritDefinitionScalarCalculation(FigureOfMerit.m_Object)

    def FigureOfMeritDefinitionScalarCalculation(self, fom: "IFigureOfMerit"):
        # Set the Scalar Calculation definition.
        scalarCalculation: "IFigureOfMeritDefinitionScalarCalculation" = fom.set_scalar_calculation_definition(
            "CentralBody/Earth ElapsedTimeFromStart"
        )

    # endregion

    # region FigureOfMeritDefinitionScalarCalculationFromVGT
    def test_FigureOfMeritDefinitionScalarCalculationFromVGT(self):
        self.FigureOfMeritDefinitionScalarCalculationFromVGT(
            FigureOfMerit.m_Object, clr.Convert(TestBase.Application, IStkObjectRoot)
        )

    def FigureOfMeritDefinitionScalarCalculationFromVGT(self, fom: "IFigureOfMerit", stkRoot: "IStkObjectRoot"):
        # Get the qualified path of a Scalar Calculation (e.g.
        provider: "IAnalysisWorkbenchProvider" = stkRoot.vgt_root.get_provider("CentralBody/Sun")
        calcScalar: "ICalculationToolScalar" = provider.calc_scalars[0]
        calcScalarQualifiedPath: str = (clr.CastAs(calcScalar, IAnalysisWorkbenchComponent)).qualified_path

        # Set the Scalar Calculation definition using the qualified path
        scalarCalculation: "IFigureOfMeritDefinitionScalarCalculation" = fom.set_scalar_calculation_definition(
            calcScalarQualifiedPath
        )

    # endregion

    # region FigureOfMeritDefinitionSystemResponseTime
    def test_FigureOfMeritDefinitionSystemResponseTime(self):
        TestBase.Application.current_scenario.children.new(AgESTKObjectType.eFacility, "Facility1")
        self.FigureOfMeritDefinitionSystemResponseTime(FigureOfMerit.m_Object)

    def FigureOfMeritDefinitionSystemResponseTime(self, fom: "IFigureOfMerit"):
        fom.set_definition_type(AgEFmDefinitionType.eFmSystemResponseTime)
        systemResponseTime: "IFigureOfMeritDefinitionSystemResponseTime" = clr.CastAs(
            fom.definition, IFigureOfMeritDefinitionSystemResponseTime
        )

        systemResponseTime.command_station_path = r"/Application/STK/Scenario/CodeSnippetScenario/Facility/Facility1"

    # endregion

    # region FigureOfMeritDefinitionSystemResponseTimeReset
    def test_FigureOfMeritDefinitionSystemResponseTimeReset(self):
        TestBase.Application.current_scenario.children.new(AgESTKObjectType.eFacility, "Facility1")
        self.FigureOfMeritDefinitionSystemResponseTimeReset(FigureOfMerit.m_Object)

    def FigureOfMeritDefinitionSystemResponseTimeReset(self, fom: "IFigureOfMerit"):
        fom.set_definition_type(AgEFmDefinitionType.eFmSystemResponseTime)
        systemResponseTime: "IFigureOfMeritDefinitionSystemResponseTime" = clr.CastAs(
            fom.definition, IFigureOfMeritDefinitionSystemResponseTime
        )

        systemResponseTime.command_station_path = "NONE"

    # endregion
