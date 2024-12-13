from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class FigureOfMeritSnipets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_CovDefObject: "CoverageDefinition" = None
        super(FigureOfMeritSnipets, self).__init__(*args, **kwargs)

    m_CovDefDefaultName: str = "cd1"

    m_Object: "FigureOfMerit" = None
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
                STKObjectType.COVERAGE_DEFINITION, FigureOfMeritSnipets.m_CovDefDefaultName
            ),
            CoverageDefinition,
        )
        covdefObject: "IStkObject" = clr.CastAs(self.m_CovDefObject, IStkObject)
        FigureOfMeritSnipets.m_Object = clr.CastAs(
            covdefObject.children.new(STKObjectType.FIGURE_OF_MERIT, FigureOfMeritSnipets.m_DefaultName), FigureOfMerit
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        covdefObject: "IStkObject" = clr.CastAs(self.m_CovDefObject, IStkObject)
        covdefObject.children.unload(STKObjectType.FIGURE_OF_MERIT, FigureOfMeritSnipets.m_DefaultName)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.COVERAGE_DEFINITION, FigureOfMeritSnipets.m_CovDefDefaultName
        )
        FigureOfMeritSnipets.m_Object = None
        self.m_CovDefObject = None
        if TestBase.Application.current_scenario.children.contains(STKObjectType.FACILITY, "Facility1"):
            TestBase.Application.current_scenario.children.unload(STKObjectType.FACILITY, "Facility1")

    # endregion

    # region CreateFigureOfMeritOnCoverageDefinition
    def test_CreateFigureOfMeritOnCoverageDefinition(self):
        self.CreateFigureOfMeritOnCoverageDefinition(self.m_CovDefObject)

    def CreateFigureOfMeritOnCoverageDefinition(self, covdef: "CoverageDefinition"):
        # Get the coverage definition as a IStkObject interface
        covdefObject: "IStkObject" = clr.CastAs(covdef, IStkObject)

        # Create the figure of merit
        fom: "FigureOfMerit" = clr.CastAs(
            covdefObject.children.new(STKObjectType.FIGURE_OF_MERIT, "MyFigureOfMerit"), FigureOfMerit
        )

    # endregion

    # region ConfigureAccessDurationFigureOfMerit
    def test_ConfigureAccessDurationFigureOfMerit(self):
        self.ConfigureAccessDurationFigureOfMerit(FigureOfMeritSnipets.m_Object)

    def ConfigureAccessDurationFigureOfMerit(self, fom: "FigureOfMerit"):
        # Set figure of merit definition to ACCESS_DURATION
        fom.set_definition_type(FigureOfMeritDefinitionType.ACCESS_DURATION)

        # Get IFigureOfMeritDefinitionCompute interface
        defComp: "IFigureOfMeritDefinitionCompute" = clr.CastAs(fom.definition, IFigureOfMeritDefinitionCompute)
        if defComp.is_compute_type_supported(FigureOfMeritCompute.PERCENT_ABOVE):
            # Set Compute type to supported compute option
            defComp.set_compute_type(FigureOfMeritCompute.PERCENT_ABOVE)

            # Get compute option compute interface
            fomData: "FigureOfMeritDefinitionDataPercentLevel" = clr.CastAs(
                defComp.compute, FigureOfMeritDefinitionDataPercentLevel
            )
            fomData.percent_level = 0.25

    # endregion

    # region ConfigureCoverageTimeFigureOfMerit
    def test_ConfigureCoverageTimeFigureOfMerit(self):
        self.ConfigureCoverageTimeFigureOfMerit(FigureOfMeritSnipets.m_Object)

    def ConfigureCoverageTimeFigureOfMerit(self, fom: "FigureOfMerit"):
        # Set figure of merit definition to COVERAGE_TIME
        fom.set_definition_type(FigureOfMeritDefinitionType.COVERAGE_TIME)

        # Get IFigureOfMeritDefinitionCompute interface
        defComp: "IFigureOfMeritDefinitionCompute" = clr.CastAs(fom.definition, IFigureOfMeritDefinitionCompute)
        if defComp.is_compute_type_supported(FigureOfMeritCompute.TOTAL_TIME_ABOVE):
            # Set Compute type to supported compute option
            defComp.set_compute_type(FigureOfMeritCompute.TOTAL_TIME_ABOVE)

            # Get compute option compute interface
            fomData: "FigureOfMeritDefinitionDataMinimumNumberOfAssets" = clr.CastAs(
                defComp.compute, FigureOfMeritDefinitionDataMinimumNumberOfAssets
            )
            fomData.minimum_assets = 15

    # endregion

    # region SetFigureOfMeritDefToAccessConstraintByEnum
    def test_SetFigureOfMeritDefToAccessConstraintByEnum(self):
        self.SetFigureOfMeritDefToAccessConstraintByEnum(FigureOfMeritSnipets.m_Object)

    def SetFigureOfMeritDefToAccessConstraintByEnum(self, fom: "FigureOfMerit"):
        acd: "FigureOfMeritDefinitionAccessConstraint" = fom.set_access_constraint_definition(
            FigureOfMeritConstraintName.AZIMUTH_RATE
        )

    # endregion

    # region SetFigureOfMeritDefToAccessConstraintByName
    def test_SetFigureOfMeritDefToAccessConstraintByName(self):
        self.SetFigureOfMeritDefToAccessConstraintByName(FigureOfMeritSnipets.m_Object)

    def SetFigureOfMeritDefToAccessConstraintByName(self, fom: "FigureOfMerit"):
        defAccessCnstr: "FigureOfMeritDefinitionAccessConstraint" = fom.set_access_constraint_definition_name(
            "AzimuthRate"
        )

        # Confiure access constraint properties
        defAccessCnstr.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        defAccessCnstr.across_assets = FigureOfMeritAcrossAssets.MINIMUM
        defAccessCnstr.time_step = 60.0

    # endregion

    # region ConfigureFigureOfMeritDefToAccessConstraint
    def test_ConfigureFigureOfMeritDefToAccessConstraint(self):
        self.ConfigureFigureOfMeritDefToAccessConstraint(FigureOfMeritSnipets.m_Object)

    def ConfigureFigureOfMeritDefToAccessConstraint(self, fom: "FigureOfMerit"):
        # Set access constraint definition to altitude
        fom.set_access_constraint_definition(FigureOfMeritConstraintName.ALTITUDE)

        # Get FigureOfMeritDefinitionAccessConstraint interface
        defAccessCnstr: "FigureOfMeritDefinitionAccessConstraint" = clr.CastAs(
            fom.definition, FigureOfMeritDefinitionAccessConstraint
        )

        # Confiure access constraint properties
        defAccessCnstr.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        defAccessCnstr.across_assets = FigureOfMeritAcrossAssets.MINIMUM
        defAccessCnstr.time_step = 60.0

    # endregion

    # region InspectGridWithSelectPoint
    def test_InspectGridWithSelectPoint(self):
        self.InspectGridWithSelectPoint(FigureOfMeritSnipets.m_Object)

    def InspectGridWithSelectPoint(self, fom: "FigureOfMerit"):
        gridInspector: "FigureOfMeritGridInspector" = fom.grid_inspector
        gridInspector.select_point(-13.864, -51.088)

        pointFom: "DataProviderTimeVarying" = clr.CastAs(gridInspector.point_figure_of_merit, DataProviderTimeVarying)
        pointFomResult: "DataProviderResult" = pointFom.execute_single("1 Jan 2012 12:00:00.00")

        pointSatisfaction: "DataProviderInterval" = clr.CastAs(gridInspector.point_satisfaction, DataProviderInterval)
        pointSatisfactionResult: "DataProviderResult" = pointSatisfaction.execute(
            "1 Jan 2012 12:00:00.00", "2 Jan 2012 12:00:00.00"
        )

        regionFom: "DataProviderTimeVarying" = clr.CastAs(gridInspector.region_figure_of_merit, DataProviderTimeVarying)
        regionFomResult: "DataProviderResult" = regionFom.execute_single("1 Jan 2012 12:00:00.00")

        regionSatisfaction: "DataProviderInterval" = clr.CastAs(gridInspector.region_satisfaction, DataProviderInterval)
        regionSatisfactionResult: "DataProviderResult" = regionSatisfaction.execute(
            "1 Jan 2012 12:00:00.00", "2 Jan 2012 12:00:00.00"
        )

    # endregion

    # region ConfigureFigureOfMeritContours
    @category("Graphics Tests")
    def test_ConfigureFigureOfMeritContours(self):
        FigureOfMeritSnipets.m_Object.set_access_constraint_definition_name("AzimuthRate")
        self.ConfigureFigureOfMeritContours(FigureOfMeritSnipets.m_Object.graphics.static.contours)

    def ConfigureFigureOfMeritContours(self, contours: "IFigureOfMeritGraphics2DContours"):
        contours.show_graphics = True
        contours.contour_type = FigureOfMeritGraphics2DContourType.SMOOTH_FILL
        contours.color_method = FigureOfMeritGraphics2DColorMethod.EXPLICIT

        # Add level ranges (batch)
        contours.level_attributes.add_level_range(25, 35, 1)
        firstLevel: "FigureOfMeritGraphics2DLevelAttributesElement" = contours.level_attributes[0]
        firstLevel.color = Colors.Blue

        # Add one level (individually)
        level: "FigureOfMeritGraphics2DLevelAttributesElement" = contours.level_attributes.add_level(55)
        level.color = Colors.Red

    # endregion

    # region FigureOfMeritDefinitionAgeOfData
    def test_FigureOfMeritDefinitionAgeOfData(self):
        self.FigureOfMeritDefinitionAgeOfData(FigureOfMeritSnipets.m_Object)

    def FigureOfMeritDefinitionAgeOfData(self, fom: "FigureOfMerit"):
        # Get the FigureOfMeritDefinitionAgeOfData interface
        fom.set_definition_type(FigureOfMeritDefinitionType.AGE_OF_DATA)
        ageOfData: "FigureOfMeritDefinitionAgeOfData" = clr.CastAs(fom.definition, FigureOfMeritDefinitionAgeOfData)

        # Set the minimum number of assets for computing
        ageOfData.minimum_assets = 2

    # endregion

    # region FigureOfMeritDefinitionScalarCalculation
    def test_FigureOfMeritDefinitionScalarCalculation(self):
        self.FigureOfMeritDefinitionScalarCalculation(FigureOfMeritSnipets.m_Object)

    def FigureOfMeritDefinitionScalarCalculation(self, fom: "FigureOfMerit"):
        # Set the Scalar Calculation definition.
        scalarCalculation: "FigureOfMeritDefinitionScalarCalculation" = fom.set_scalar_calculation_definition(
            "CentralBody/Earth ElapsedTimeFromStart"
        )

    # endregion

    # region FigureOfMeritDefinitionScalarCalculationFromVGT
    def test_FigureOfMeritDefinitionScalarCalculationFromVGT(self):
        self.FigureOfMeritDefinitionScalarCalculationFromVGT(FigureOfMeritSnipets.m_Object, TestBase.Application)

    def FigureOfMeritDefinitionScalarCalculationFromVGT(self, fom: "FigureOfMerit", stkRoot: "StkObjectRoot"):
        # Get the qualified path of a Scalar Calculation (e.g.
        provider: "AnalysisWorkbenchComponentProvider" = stkRoot.analysis_workbench_components_root.get_provider(
            "CentralBody/Sun"
        )
        calcScalar: "ICalculationToolScalar" = provider.calculation_scalars[0]
        calcScalarQualifiedPath: str = (clr.CastAs(calcScalar, IAnalysisWorkbenchComponent)).qualified_path

        # Set the Scalar Calculation definition using the qualified path
        scalarCalculation: "FigureOfMeritDefinitionScalarCalculation" = fom.set_scalar_calculation_definition(
            calcScalarQualifiedPath
        )

    # endregion

    # region FigureOfMeritDefinitionSystemResponseTime
    def test_FigureOfMeritDefinitionSystemResponseTime(self):
        TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Facility1")
        self.FigureOfMeritDefinitionSystemResponseTime(FigureOfMeritSnipets.m_Object)

    def FigureOfMeritDefinitionSystemResponseTime(self, fom: "FigureOfMerit"):
        fom.set_definition_type(FigureOfMeritDefinitionType.SYSTEM_RESPONSE_TIME)
        systemResponseTime: "FigureOfMeritDefinitionSystemResponseTime" = clr.CastAs(
            fom.definition, FigureOfMeritDefinitionSystemResponseTime
        )

        systemResponseTime.command_station_path = r"/Application/STK/Scenario/CodeSnippetScenario/Facility/Facility1"

    # endregion

    # region FigureOfMeritDefinitionSystemResponseTimeReset
    def test_FigureOfMeritDefinitionSystemResponseTimeReset(self):
        TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Facility1")
        self.FigureOfMeritDefinitionSystemResponseTimeReset(FigureOfMeritSnipets.m_Object)

    def FigureOfMeritDefinitionSystemResponseTimeReset(self, fom: "FigureOfMerit"):
        fom.set_definition_type(FigureOfMeritDefinitionType.SYSTEM_RESPONSE_TIME)
        systemResponseTime: "FigureOfMeritDefinitionSystemResponseTime" = clr.CastAs(
            fom.definition, FigureOfMeritDefinitionSystemResponseTime
        )

        systemResponseTime.command_station_path = "NONE"

    # endregion
