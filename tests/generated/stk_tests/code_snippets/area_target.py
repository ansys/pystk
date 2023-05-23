import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class AreaTarget(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object = None
        super(AreaTarget, self).__init__(*args, **kwargs)

    m_DefaultName = "MyAreaTarget"

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
        self.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eAreaTarget, AreaTarget.m_DefaultName
            ),
            IAreaTarget,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eAreaTarget, AreaTarget.m_DefaultName
        )
        self.m_Object = None

    # endregion

    # region CreateAreaTargetOnCurrentScenarioCentralBody
    def test_CreateAreaTargetOnCurrentScenarioCentralBody(self):
        (clr.Convert(self.m_Object, IStkObject)).Unload()
        self.CreateAreaTargetOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)
        self.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children[AreaTarget.m_DefaultName], IAreaTarget
        )

    def CreateAreaTargetOnCurrentScenarioCentralBody(self, root):
        # Create the AreaTarget on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        areaTarget = clr.CastAs(
            root.CurrentScenario.Children.New(AgESTKObjectType.eAreaTarget, "MyAreaTarget"), IAreaTarget
        )

    # endregion

    # region SetAreaTargetBoundaryAndPosition
    def test_SetAreaTargetBoundaryAndPosition(self):
        self.SetAreaTargetBoundaryAndPosition(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetAreaTargetBoundaryAndPosition(self, root, areaTarget):
        # By using the fine grained interfaces,
        # BeginUpdate/EndUpdate prevent intermediate redraws
        root.BeginUpdate()
        areaTarget.AreaType = AgEAreaType.ePattern
        patterns = clr.CastAs(areaTarget.AreaTypeData, IAreaTypePatternCollection)
        patterns.Add(40.04, -76.304)
        patterns.Add(40.337, -75.922)
        patterns.Add(40.028, -75.628)
        root.EndUpdate()

    # endregion

    # region SetAreaTargetBoundaryAndPositionCommonTask
    def test_SetAreaTargetBoundaryAndPositionCommonTask(self):
        self.SetAreaTargetBoundaryAndPositionCommonTask(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetAreaTargetBoundaryAndPositionCommonTask(self, root, areaTarget):
        # By using the CommonTasks interface,
        # make an array of lattitude and longitude boundary points
        boundary = [[40.04, -76.304], [40.337, -75.922], [40.028, -75.628]]

        # SetAreaTypePattern expects a two dimensional array of latitude and longitude values
        areaTarget.CommonTasks.SetAreaTypePattern(boundary)

    # endregion

    # region SetEllipticalAreaTarget
    def test_SetEllipticalAreaTarget(self):
        self.SetEllipticalAreaTarget(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetEllipticalAreaTarget(self, root, areaTarget):
        # By using the fine grained interfaces,
        # BeginUpdate/EndUpdate prevent intermediate redraws
        root.BeginUpdate()
        areaTarget.AreaType = AgEAreaType.eEllipse
        ellipse = clr.CastAs(areaTarget.AreaTypeData, IAreaTypeEllipse)
        ellipse.SemiMajorAxis = 85.25  # in km (distance dimension)
        ellipse.SemiMinorAxis = 80.75  # in km (distance dimension)
        ellipse.Bearing = 44  # in deg (angle dimension)
        root.EndUpdate()

    # endregion

    # region SetEllipticalAreaTargetCommonTask
    def test_SetEllipticalAreaTargetCommonTask(self):
        self.SetEllipticalAreaTargetCommonTask(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetEllipticalAreaTargetCommonTask(self, root, areaTarget):
        # By using the CommonTasks interface
        areaTarget.CommonTasks.SetAreaTypeEllipse(85.25, 80.75, 44)

    # endregion

    # region ListAllPointsInAnAreaTarget
    def test_ListAllPointsInAnAreaTarget(self):
        self.SetAreaTargetBoundaryAndPosition(CodeSnippetsTestBase.m_Root, self.m_Object)
        self.ListAllPointsInAnAreaTarget(self.m_Object)

    def ListAllPointsInAnAreaTarget(self, areaTarget):
        if areaTarget.AreaType == AgEAreaType.ePattern:
            # Get IAgAreaTypePatternCollection interface from AreaTypeData
            patternPoints = clr.CastAs(areaTarget.AreaTypeData, IAreaTypePatternCollection)

            # ToArray returns a two dimensional array of latitude and longitude points
            areaTargetPoints = patternPoints.ToArray()

            Console.WriteLine("All points in Area Target")

            i = 0
            while i < len(areaTargetPoints):
                Console.WriteLine(
                    "  Latitude {0} Longitude: {1}",
                    Convert.ToDouble(areaTargetPoints[i][0]),
                    Convert.ToDouble(areaTargetPoints[i][1]),
                )

                i += 1

    # endregion
