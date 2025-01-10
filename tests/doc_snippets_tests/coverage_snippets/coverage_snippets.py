from test_util import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippets_test_base import *
from code_snippet_decorator import *


class CoverageSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(CoverageSnippets, self).__init__(*args, **kwargs)

    satellite: "Satellite" = None
    coverage: "CoverageDefinition" = None

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def setUp(self):
        CoverageSnippets.satellite: "Satellite" = Satellite(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite")
        )
        propagator: "PropagatorTwoBody" = CoverageSnippets.satellite.propagator
        propagator.propagate()
        CoverageSnippets.coverage: "CoverageDefinition" = CoverageDefinition(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")
        )

    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "satellite")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.COVERAGE_DEFINITION, "coverage")
        CoverageSnippets.satellite = None
        CoverageSnippets.coverage = None

    def test_TestCoverageComputeSnippet(self):
        self.TestCoverageComputeSnippet(CodeSnippetsTestBase.m_Root, CoverageSnippets.coverage)

    @code_snippet(
        name="CoverageCompute",
        description="Compute Coverage",
        category="STK Objects | Coverage Definition",
        eid="STKObjects~IAgCoverageDefinition",
    )
    def TestCoverageComputeSnippet(self, root: "StkObjectRoot", coverage: "CoverageDefinition"):
        # CoverageDefinition coverage: Coverage object
        coverage.compute_accesses()

    def test_TestCoverageAdvancedSnippet(self):
        self.TestCoverageAdvancedSnippet(CodeSnippetsTestBase.m_Root, CoverageSnippets.coverage)

    @code_snippet(
        name="CoverageAdvanced",
        description="Set Advanced Settings for Coverage",
        category="STK Objects | Coverage Definition",
        eid="STKObjects~IAgCoverageDefinition",
    )
    def TestCoverageAdvancedSnippet(self, root: "StkObjectRoot", coverage: "CoverageDefinition"):
        # CoverageDefinition coverage: Coverage object
        advanced: "CoverageAdvancedSettings" = coverage.advanced
        advanced.recompute_automatically = False
        advanced.data_retention = CoverageDataRetention.ALL_DATA
        advanced.save_mode = DataSaveMode.SAVE_ACCESSES

    def test_TestCoverageIntervalSnippet(self):
        self.TestCoverageIntervalSnippet(
            CodeSnippetsTestBase.m_Root, CoverageSnippets.satellite, CoverageSnippets.coverage
        )

    @code_snippet(
        name="CoverageInterval",
        description="Set the Coverage Interval to an object's availability Analysis interval",
        category="STK Objects | Coverage Definition",
        eid="STKObjects~IAgCoverageDefinition",
    )
    def TestCoverageIntervalSnippet(
        self, root: "StkObjectRoot", satellite: "Satellite", coverage: "CoverageDefinition"
    ):
        # Satellite satellite: Satellite object
        # CoverageDefinition coverage: Coverage object
        satVGT: "AnalysisWorkbenchComponentProvider" = IStkObject(satellite).analysis_workbench_components
        intervals: "TimeToolTimeIntervalGroup" = satVGT.time_intervals
        AvailTimeSpan: "ITimeToolTimeInterval" = intervals.item("AvailabilityTimeSpan")
        IntResult: "TimeToolTimeIntervalResult" = AvailTimeSpan.find_interval()
        coverage.interval.analysis_interval.set_start_and_stop_times(IntResult.interval.start, IntResult.interval.stop)
