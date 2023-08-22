from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class AreaTarget(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object: "IAreaTarget" = None
        super(AreaTarget, self).__init__(*args, **kwargs)

    m_DefaultName: str = "MyAreaTarget"

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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eAreaTarget, AreaTarget.m_DefaultName
            ),
            IAreaTarget,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eAreaTarget, AreaTarget.m_DefaultName
        )
        self.m_Object = None

    # endregion

    # region CreateAreaTargetOnCurrentScenarioCentralBody
    def test_CreateAreaTargetOnCurrentScenarioCentralBody(self):
        (clr.Convert(self.m_Object, IStkObject)).unload()
        self.CreateAreaTargetOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)
        self.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children[AreaTarget.m_DefaultName], IAreaTarget
        )

    def CreateAreaTargetOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the AreaTarget on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        areaTarget: "IAreaTarget" = clr.CastAs(
            root.current_scenario.children.new(AgESTKObjectType.eAreaTarget, "MyAreaTarget"), IAreaTarget
        )

    # endregion

    # region SetAreaTargetBoundaryAndPosition
    def test_SetAreaTargetBoundaryAndPosition(self):
        self.SetAreaTargetBoundaryAndPosition(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetAreaTargetBoundaryAndPosition(self, root: "IStkObjectRoot", areaTarget: "IAreaTarget"):
        # By using the fine grained interfaces,
        # BeginUpdate/EndUpdate prevent intermediate redraws
        root.begin_update()
        areaTarget.area_type = AgEAreaType.ePattern
        patterns: "IAreaTypePatternCollection" = clr.CastAs(areaTarget.area_type_data, IAreaTypePatternCollection)
        patterns.add(40.04, -76.304)
        patterns.add(40.337, -75.922)
        patterns.add(40.028, -75.628)
        root.end_update()

    # endregion

    # region SetAreaTargetBoundaryAndPositionCommonTask
    def test_SetAreaTargetBoundaryAndPositionCommonTask(self):
        self.SetAreaTargetBoundaryAndPositionCommonTask(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetAreaTargetBoundaryAndPositionCommonTask(self, root: "IStkObjectRoot", areaTarget: "IAreaTarget"):
        # By using the CommonTasks interface,
        # make an array of lattitude and longitude boundary points
        boundary = [[40.04, -76.304], [40.337, -75.922], [40.028, -75.628]]

        # SetAreaTypePattern expects a two dimensional array of latitude and longitude values
        areaTarget.common_tasks.set_area_type_pattern(boundary)

    # endregion

    # region SetEllipticalAreaTarget
    def test_SetEllipticalAreaTarget(self):
        self.SetEllipticalAreaTarget(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetEllipticalAreaTarget(self, root: "IStkObjectRoot", areaTarget: "IAreaTarget"):
        # By using the fine grained interfaces,
        # BeginUpdate/EndUpdate prevent intermediate redraws
        root.begin_update()
        areaTarget.area_type = AgEAreaType.eEllipse
        ellipse: "IAreaTypeEllipse" = clr.CastAs(areaTarget.area_type_data, IAreaTypeEllipse)
        ellipse.semi_major_axis = 85.25  # in km (distance dimension)
        ellipse.semi_minor_axis = 80.75  # in km (distance dimension)
        ellipse.bearing = 44  # in deg (angle dimension)
        root.end_update()

    # endregion

    # region SetEllipticalAreaTargetCommonTask
    def test_SetEllipticalAreaTargetCommonTask(self):
        self.SetEllipticalAreaTargetCommonTask(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetEllipticalAreaTargetCommonTask(self, root: "IStkObjectRoot", areaTarget: "IAreaTarget"):
        # By using the CommonTasks interface
        areaTarget.common_tasks.set_area_type_ellipse(85.25, 80.75, 44)

    # endregion

    # region ListAllPointsInAnAreaTarget
    def test_ListAllPointsInAnAreaTarget(self):
        self.SetAreaTargetBoundaryAndPosition(CodeSnippetsTestBase.m_Root, self.m_Object)
        self.ListAllPointsInAnAreaTarget(self.m_Object)

    def ListAllPointsInAnAreaTarget(self, areaTarget: "IAreaTarget"):
        if areaTarget.area_type == AgEAreaType.ePattern:
            # Get IAreaTypePatternCollection interface from AreaTypeData
            patternPoints: "IAreaTypePatternCollection" = clr.CastAs(
                areaTarget.area_type_data, IAreaTypePatternCollection
            )

            # ToArray returns a two dimensional array of latitude and longitude points
            areaTargetPoints = patternPoints.to_array()

            Console.WriteLine("All points in Area Target")

            i: int = 0
            while i < len(areaTargetPoints):
                Console.WriteLine(
                    "  Latitude {0} Longitude: {1}",
                    Convert.ToDouble(areaTargetPoints[i][0]),
                    Convert.ToDouble(areaTargetPoints[i][1]),
                )

                i += 1

    # endregion
