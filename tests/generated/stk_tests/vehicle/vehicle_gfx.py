from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from logger import *
from math2 import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


# region GfxAttributesBasicHelper
class GfxAttributesBasicHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oBasic: "IVehicleGraphics2DAttributesBasic"):
        Assert.assertIsNotNone(oBasic)
        self.m_logger.WriteLine("GfxAttributesBasicHelper test:")
        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oBasic.is_visible)
        oBasic.is_visible = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBasic.is_visible)
        Assert.assertEqual(False, oBasic.is_visible)

        def action1():
            oBasic.color = Color.FromArgb(16711935)

        TryCatchAssertBlock.ExpectedException("read-only", action1)

        def action2():
            oBasic.marker_style = "Square"

        TryCatchAssertBlock.ExpectedException("read-only", action2)

        def action3():
            oBasic.label_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action3)

        def action4():
            oBasic.inherit = False

        TryCatchAssertBlock.ExpectedException("read-only", action4)

        def action5():
            oBasic.line.style = LINE_STYLE.LMS_DASH

        TryCatchAssertBlock.ExpectedException("read-only", action5)

        def action6():
            oBasic.line.width = LINE_WIDTH.WIDTH5

        TryCatchAssertBlock.ExpectedException("read-only", action6)

        # IsVisible (true)
        oBasic.is_visible = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBasic.is_visible)
        Assert.assertEqual(True, oBasic.is_visible)
        # Color
        self.m_logger.WriteLine6("\t\tCurrent Color is: {0}", oBasic.color)
        oBasic.color = Color.FromArgb(16711935)
        self.m_logger.WriteLine6("\t\tNew Color is: {0}", oBasic.color)
        AssertEx.AreEqual(Color.FromArgb(16711935), oBasic.color)
        # MarkerStyle
        self.m_logger.WriteLine5("\t\tCurrent MarkerStyle is: {0}", oBasic.marker_style)
        oBasic.marker_style = "Square"
        self.m_logger.WriteLine5("\t\tNew MarkerStyle is: {0}", oBasic.marker_style)
        Assert.assertEqual("Square", oBasic.marker_style)
        # Line.Style
        self.m_logger.WriteLine6("\t\tCurrent Line.Style is: {0}", oBasic.line.style)
        oBasic.line.style = LINE_STYLE.M_DASH_DOT
        self.m_logger.WriteLine6("\t\tNew Line.Style is: {0}", oBasic.line.style)
        Assert.assertEqual(LINE_STYLE.M_DASH_DOT, oBasic.line.style)
        # Line.Width
        self.m_logger.WriteLine6("\t\tCurrent Line.Width is: {0}", oBasic.line.width)
        oBasic.line.width = LINE_WIDTH.WIDTH5
        self.m_logger.WriteLine6("\t\tNew Line.Width is: {0}", oBasic.line.width)
        Assert.assertEqual(LINE_WIDTH.WIDTH5, oBasic.line.width)
        # Inherit (true)
        self.m_logger.WriteLine4("\t\tCurrent Inherit flag is: {0}", oBasic.inherit)
        oBasic.inherit = True
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oBasic.inherit)
        Assert.assertEqual(True, oBasic.inherit)

        def action7():
            oBasic.label_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action7)

        # Inherit (false)
        oBasic.inherit = False
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oBasic.inherit)
        Assert.assertEqual(False, oBasic.inherit)
        # LabelVisible
        self.m_logger.WriteLine4("\t\tCurrent LabelVisible flag is: {0}", oBasic.label_visible)
        oBasic.label_visible = True
        self.m_logger.WriteLine4("\t\tNew LabelVisible flag is: {0}", oBasic.label_visible)
        Assert.assertEqual(True, oBasic.label_visible)
        oBasic.label_visible = False
        self.m_logger.WriteLine4("\t\tNew LabelVisible flag is: {0}", oBasic.label_visible)
        Assert.assertEqual(False, oBasic.label_visible)


# endregion


# region GfxAttributesRouteHelper
class GfxAttributesRouteHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oRoute: "IVehicleGraphics2DAttributesRoute"):
        Assert.assertIsNotNone(oRoute)

        # Basic
        oHelper = GfxAttributesBasicHelper()
        oHelper.Run(clr.Convert(oRoute, IVehicleGraphics2DAttributesBasic))

        self.m_logger.WriteLine("GfxAttributesRouteHelper test:")

        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oRoute.is_visible)
        oRoute.is_visible = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oRoute.is_visible)
        Assert.assertEqual(False, oRoute.is_visible)

        def action8():
            oRoute.is_route_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action8)

        def action9():
            oRoute.is_route_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action9)

        # IsVisible (true)
        oRoute.is_visible = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oRoute.is_visible)
        Assert.assertEqual(True, oRoute.is_visible)
        # Inherit (true)
        self.m_logger.WriteLine4("\t\tCurrent Inherit flag is: {0}", oRoute.inherit)
        oRoute.inherit = True
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oRoute.inherit)
        Assert.assertEqual(True, oRoute.inherit)

        def action10():
            oRoute.is_route_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action10)

        def action11():
            oRoute.is_route_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action11)

        # Inherit (false)
        oRoute.inherit = False
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oRoute.inherit)
        Assert.assertEqual(False, oRoute.inherit)
        # IsRouteVisible
        self.m_logger.WriteLine4("\t\tCurrent IsRouteVisible flag is: {0}", oRoute.is_route_visible)
        oRoute.is_route_visible = True
        self.m_logger.WriteLine4("\t\tNew IsRouteVisible flag is: {0}", oRoute.is_route_visible)
        Assert.assertEqual(True, oRoute.is_route_visible)
        # IsRouteMarkerVisible
        self.m_logger.WriteLine4("\t\tCurrent IsRouteMarkerVisible flag is: {0}", oRoute.is_route_marker_visible)
        oRoute.is_route_marker_visible = True
        self.m_logger.WriteLine4("\t\tNew IsRouteMarkerVisible flag is: {0}", oRoute.is_route_marker_visible)
        Assert.assertEqual(True, oRoute.is_route_marker_visible)


# endregion


# region GfxAttributesOrbitHelper
class GfxAttributesOrbitHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oOrbit: "IVehicleGraphics2DAttributesOrbit"):
        Assert.assertIsNotNone(oOrbit)

        # Basic
        oHelper = GfxAttributesBasicHelper()
        oHelper.Run(clr.Convert(oOrbit, IVehicleGraphics2DAttributesBasic))

        self.m_logger.WriteLine("GfxAttributesOrbitHelper test:")

        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oOrbit.is_visible)
        oOrbit.is_visible = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oOrbit.is_visible)
        Assert.assertEqual(False, oOrbit.is_visible)

        def action12():
            oOrbit.is_ground_track_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action12)

        def action13():
            oOrbit.is_ground_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action13)

        def action14():
            oOrbit.is_orbit_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action14)

        def action15():
            oOrbit.is_orbit_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action15)

        # IsVisible (true)
        oOrbit.is_visible = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oOrbit.is_visible)
        Assert.assertEqual(True, oOrbit.is_visible)
        # Inherit (true)
        self.m_logger.WriteLine4("\t\tCurrent Inherit flag is: {0}", oOrbit.inherit)
        oOrbit.inherit = True
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oOrbit.inherit)
        Assert.assertEqual(True, oOrbit.inherit)

        def action16():
            oOrbit.is_ground_track_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action16)

        def action17():
            oOrbit.is_ground_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action17)

        def action18():
            oOrbit.is_orbit_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action18)

        def action19():
            oOrbit.is_orbit_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action19)

        # Inherit (false)
        oOrbit.inherit = False
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oOrbit.inherit)
        Assert.assertEqual(False, oOrbit.inherit)
        # IsGroundTrackVisible
        self.m_logger.WriteLine4("\t\tCurrent IsGroundTrackVisible flag is: {0}", oOrbit.is_ground_track_visible)
        oOrbit.is_ground_track_visible = True
        self.m_logger.WriteLine4("\t\tNew IsGroundTrackVisible flag is: {0}", oOrbit.is_ground_track_visible)
        Assert.assertEqual(True, oOrbit.is_ground_track_visible)
        # IsGroundMarkerVisible
        self.m_logger.WriteLine4("\t\tCurrent IsGroundMarkerVisible flag is: {0}", oOrbit.is_ground_marker_visible)
        oOrbit.is_ground_marker_visible = True
        self.m_logger.WriteLine4("\t\tNew IsGroundMarkerVisible flag is: {0}", oOrbit.is_ground_marker_visible)
        Assert.assertEqual(True, oOrbit.is_ground_marker_visible)
        # IsOrbitVisible
        self.m_logger.WriteLine4("\t\tCurrent IsOrbitVisible flag is: {0}", oOrbit.is_orbit_visible)
        oOrbit.is_orbit_visible = True
        self.m_logger.WriteLine4("\t\tNew IsOrbitVisible flag is: {0}", oOrbit.is_orbit_visible)
        Assert.assertEqual(True, oOrbit.is_orbit_visible)
        # IsOrbitMarkerVisible
        self.m_logger.WriteLine4("\t\tCurrent IsOrbitMarkerVisible flag is: {0}", oOrbit.is_orbit_marker_visible)
        oOrbit.is_orbit_marker_visible = True
        self.m_logger.WriteLine4("\t\tNew IsOrbitMarkerVisible flag is: {0}", oOrbit.is_orbit_marker_visible)
        Assert.assertEqual(True, oOrbit.is_orbit_marker_visible)


# endregion


# region GfxAttributesTrajectoryHelper
class GfxAttributesTrajectoryHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oTrajectory: "IVehicleGraphics2DAttributesTrajectory"):
        Assert.assertIsNotNone(oTrajectory)

        # Basic
        oHelper = GfxAttributesBasicHelper()
        oHelper.Run(clr.Convert(oTrajectory, IVehicleGraphics2DAttributesBasic))

        self.m_logger.WriteLine("GfxAttributesTrajectoryHelper test:")

        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oTrajectory.is_visible)
        oTrajectory.is_visible = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oTrajectory.is_visible)
        Assert.assertEqual(False, oTrajectory.is_visible)

        def action20():
            oTrajectory.is_ground_track_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action20)

        def action21():
            oTrajectory.is_ground_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action21)

        def action22():
            oTrajectory.is_trajectory_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action22)

        def action23():
            oTrajectory.is_trajectory_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action23)

        # IsVisible (true)
        oTrajectory.is_visible = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oTrajectory.is_visible)
        Assert.assertEqual(True, oTrajectory.is_visible)
        # Inherit (true)
        self.m_logger.WriteLine4("\t\tCurrent Inherit flag is: {0}", oTrajectory.inherit)
        oTrajectory.inherit = True
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oTrajectory.inherit)
        Assert.assertEqual(True, oTrajectory.inherit)

        def action24():
            oTrajectory.is_ground_track_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action24)

        def action25():
            oTrajectory.is_ground_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action25)

        def action26():
            oTrajectory.is_trajectory_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action26)

        def action27():
            oTrajectory.is_trajectory_marker_visible = False

        TryCatchAssertBlock.ExpectedException("read-only", action27)

        # Inherit (false)
        oTrajectory.inherit = False
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oTrajectory.inherit)
        Assert.assertEqual(False, oTrajectory.inherit)
        # IsGroundTrackVisible
        self.m_logger.WriteLine4("\t\tCurrent IsGroundTrackVisible flag is: {0}", oTrajectory.is_ground_track_visible)
        oTrajectory.is_ground_track_visible = True
        self.m_logger.WriteLine4("\t\tNew IsGroundTrackVisible flag is: {0}", oTrajectory.is_ground_track_visible)
        Assert.assertEqual(True, oTrajectory.is_ground_track_visible)
        # IsGroundMarkerVisible
        self.m_logger.WriteLine4("\t\tCurrent IsGroundMarkerVisible flag is: {0}", oTrajectory.is_ground_marker_visible)
        oTrajectory.is_ground_marker_visible = True
        self.m_logger.WriteLine4("\t\tNew IsGroundMarkerVisible flag is: {0}", oTrajectory.is_ground_marker_visible)
        Assert.assertEqual(True, oTrajectory.is_ground_marker_visible)
        # IsTrajectoryVisible
        self.m_logger.WriteLine4("\t\tCurrent IsTrajectoryVisible flag is: {0}", oTrajectory.is_trajectory_visible)
        oTrajectory.is_trajectory_visible = True
        self.m_logger.WriteLine4("\t\tNew IsTrajectoryVisible flag is: {0}", oTrajectory.is_trajectory_visible)
        Assert.assertEqual(True, oTrajectory.is_trajectory_visible)
        # IsTrajectoryMarkerVisible
        self.m_logger.WriteLine4(
            "\t\tCurrent IsTrajectoryMarkerVisible flag is: {0}", oTrajectory.is_trajectory_marker_visible
        )
        oTrajectory.is_trajectory_marker_visible = True
        self.m_logger.WriteLine4(
            "\t\tNew IsTrajectoryMarkerVisible flag is: {0}", oTrajectory.is_trajectory_marker_visible
        )
        Assert.assertEqual(True, oTrajectory.is_trajectory_marker_visible)


# endregion


# region GfxAttributesType enum
class GfxAttributesType:
    eOrbit = 0
    eRoute = 1
    eTrajectory = 2


# endregion


# region GfxAttributesAccessHelper
class GfxAttributesAccessHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oAccess: "IVehicleGraphics2DAttributesAccess", eType, oRoot: "IStkObjectRoot"):
        Assert.assertIsNotNone(oAccess)

        # AccessObjects
        oLinkCollection: "IObjectLinkCollection" = oAccess.access_objects
        Assert.assertIsNotNone(oLinkCollection)
        oOLCHelper = ObjectLinkCollectionHelper()
        oOLCHelper.Run(oLinkCollection, oRoot)
        if oLinkCollection.count == 0:
            # DuringAccess (readonly)
            oBasic: "IVehicleGraphics2DAttributesBasic" = oAccess.during_access
            Assert.assertIsNotNone(oBasic)

            def action28():
                oBasic.is_visible = False

            TryCatchAssertBlock.ExpectedException("read-only", action28)

            # NoAccess (readonly)
            oBasic = oAccess.no_access
            Assert.assertIsNotNone(oBasic)

            def action29():
                oBasic.is_visible = False

            TryCatchAssertBlock.ExpectedException("read-only", action29)

        if oLinkCollection.count == 0:
            arObjects = oLinkCollection.available_objects
            if Array.Length(arObjects) == 0:
                self.m_logger.WriteLine("No available objects for Access Intervals test!")
                return

            oLinkCollection.add(str(arObjects[0]))
            Assert.assertEqual(1, oLinkCollection.count)

        if eType == GfxAttributesType.eOrbit:
            # DuringAccess
            oHelper = GfxAttributesOrbitHelper()
            oHelper.Run(clr.Convert(oAccess.during_access, IVehicleGraphics2DAttributesOrbit))

            # NoAccess
            oHelper.Run(clr.Convert(oAccess.no_access, IVehicleGraphics2DAttributesOrbit))
        elif eType == GfxAttributesType.eRoute:
            # DuringAccess
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(clr.Convert(oAccess.during_access, IVehicleGraphics2DAttributesRoute))

            # NoAccess
            oHelper.Run(clr.Convert(oAccess.no_access, IVehicleGraphics2DAttributesRoute))
        elif eType == GfxAttributesType.eTrajectory:
            # DuringAccess
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(clr.Convert(oAccess.during_access, IVehicleGraphics2DAttributesTrajectory))

            # NoAccess
            oHelper.Run(clr.Convert(oAccess.no_access, IVehicleGraphics2DAttributesTrajectory))
        else:
            Assert.fail("Invalid type!")


# endregion


# region GfxAttributesCustomHelper
class GfxAttributesCustomHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCustom: "IVehicleGraphics2DAttributesCustom", eType):
        Assert.assertIsNotNone(oCustom)

        # PreemptiveIntervals
        self.m_logger.WriteLine4("\tThe current PreemptiveIntervals flag is: {0}", oCustom.preemptive_intervals)
        oCustom.preemptive_intervals = False
        self.m_logger.WriteLine4("\tThe new PreemptiveIntervals flag is: {0}", oCustom.preemptive_intervals)
        Assert.assertFalse(oCustom.preemptive_intervals)
        oCustom.preemptive_intervals = True
        self.m_logger.WriteLine4("\tThe new PreemptiveIntervals flag is: {0}", oCustom.preemptive_intervals)
        Assert.assertTrue(oCustom.preemptive_intervals)
        if eType == GfxAttributesType.eOrbit:
            oHelper = GfxAttributesOrbitHelper()
            oHelper.Run(clr.Convert(oCustom.default, IVehicleGraphics2DAttributesOrbit))
        elif eType == GfxAttributesType.eRoute:
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(clr.Convert(oCustom.default, IVehicleGraphics2DAttributesRoute))
        elif eType == GfxAttributesType.eTrajectory:
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(clr.Convert(oCustom.default, IVehicleGraphics2DAttributesTrajectory))
        else:
            Assert.fail("Invalid type!")

        # Intervals
        oICHelper = GfxIntervalsCollectionHelper()
        oICHelper.Run(oCustom.intervals, eType)

        # Deconflict
        oCustom.deconflict()


# endregion


# region GfxAttributesTimeComponentsHelper
class GfxAttributesTimeComponentsHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oTimeComponents: "IVehicleGraphics2DAttributesTimeComponents", eType, oRoot: "IStkObjectRoot"):
        Assert.assertIsNotNone(oTimeComponents)

        tcColl: "IVehicleGraphics2DTimeComponentsCollection" = oTimeComponents.time_components
        Assert.assertIsNotNone(tcColl)

        tcColl.remove_all()
        Assert.assertEqual(0, tcColl.count)

        def action30():
            tcColl.add((("Scenario/" + oRoot.current_scenario.instance_name) + " AnalysisStartTime Event"))

        # Should not be able to add Event, EventArray, or invalid components
        TryCatchAssertBlock.DoAssert("Added Event", action30)

        def action31():
            tcColl.add((("Scenario/" + oRoot.current_scenario.instance_name) + " OneMinuteSampleTimes EventArray"))

        TryCatchAssertBlock.DoAssert("Added EventArray", action31)

        def action32():
            tcColl.add("Scenario/Scenario1 Bogus EventInterval")

        TryCatchAssertBlock.DoAssert("Added invalid component", action32)

        # Should be able to add EventInterval, EventIntervalList, or EventIntervalCollection
        tcElement1: "IVehicleGraphics2DTimeComponentsElement" = tcColl.add(
            (("Scenario/" + oRoot.current_scenario.instance_name) + " AnalysisInterval EventInterval")
        )
        tcElement2: "IVehicleGraphics2DTimeComponentsElement" = tcColl.add(
            (("Scenario/" + oRoot.current_scenario.instance_name) + " AvailabilityIntervals EventIntervalList")
        )
        tcElement3: "IVehicleGraphics2DTimeComponentsElement" = tcColl.add(
            "Aircraft/Boing737 LightingIntervals EventIntervalCollection"
        )
        Assert.assertEqual(3, tcColl.count)

        # The default is priority -1, the rest are -2, -3.
        Assert.assertEqual(-1, tcElement1.priority)
        Assert.assertEqual(-2, tcElement2.priority)
        Assert.assertEqual(-3, tcElement3.priority)

        # Increase the top priority or decrease the bottom should not result in any change from above
        tcElement1.increase_priority()
        tcElement3.decrease_priority()
        Assert.assertEqual(-1, tcElement1.priority)
        Assert.assertEqual(-2, tcElement2.priority)
        Assert.assertEqual(-3, tcElement3.priority)

        # SetHighestPriority
        tcElement3.set_highest_priority()
        Assert.assertEqual(-1, tcElement3.priority)
        Assert.assertEqual(-2, tcElement1.priority)
        Assert.assertEqual(-3, tcElement2.priority)

        # SetLowestPriority
        tcElement1.set_lowest_priority()
        Assert.assertEqual(-1, tcElement3.priority)
        Assert.assertEqual(-2, tcElement2.priority)
        Assert.assertEqual(-3, tcElement1.priority)

        # IncreasePriority
        tcElement2.increase_priority()
        Assert.assertEqual(-1, tcElement2.priority)
        Assert.assertEqual(-2, tcElement3.priority)
        Assert.assertEqual(-3, tcElement1.priority)

        # DecreasePriority
        tcElement3.decrease_priority()
        Assert.assertEqual(-1, tcElement2.priority)
        Assert.assertEqual(-2, tcElement1.priority)
        Assert.assertEqual(-3, tcElement3.priority)

        # iterate
        Assert.assertEqual(
            (("Scenario/" + oRoot.current_scenario.instance_name) + " AvailabilityIntervals EventIntervalList"),
            tcColl[0].qualified_path,
        )
        Assert.assertEqual(
            (("Scenario/" + oRoot.current_scenario.instance_name) + " AnalysisInterval EventInterval"),
            tcColl[1].qualified_path,
        )
        Assert.assertEqual("Aircraft/Boing737 LightingIntervals EventIntervalCollection", tcColl[2].qualified_path)

        def action33():
            Console.WriteLine(tcColl[3].qualified_path)

        TryCatchAssertBlock.DoAssert("bad index", action33)

        # enumerate
        ele: "IVehicleGraphics2DTimeComponentsElement"

        # enumerate
        for ele in tcColl:
            Console.WriteLine(ele.qualified_path)

        evCollEle1: "IVehicleGraphics2DTimeComponentsEventCollectionElement" = clr.CastAs(
            tcElement1, IVehicleGraphics2DTimeComponentsEventCollectionElement
        )
        Assert.assertIsNone(evCollEle1)  # should not support this interface
        evEle1: "IVehicleGraphics2DTimeComponentsEventElement" = clr.CastAs(
            tcElement1, IVehicleGraphics2DTimeComponentsEventElement
        )
        Assert.assertIsNotNone(evEle1)

        crdn: "IAnalysisWorkbenchComponent" = evEle1.get_time_component()
        Assert.assertEqual(
            (("Scenario/" + oRoot.current_scenario.instance_name) + " AnalysisInterval EventInterval"),
            crdn.qualified_path,
        )

        oHelper1 = GfxAttributesBasicHelper()
        oHelper1.Run(evEle1.attributes)

        evCollEle2: "IVehicleGraphics2DTimeComponentsEventCollectionElement" = clr.CastAs(
            tcElement2, IVehicleGraphics2DTimeComponentsEventCollectionElement
        )
        Assert.assertIsNone(evCollEle2)  # should not support this interface
        evEle2: "IVehicleGraphics2DTimeComponentsEventElement" = clr.CastAs(
            tcElement2, IVehicleGraphics2DTimeComponentsEventElement
        )
        Assert.assertIsNotNone(evEle2)
        oHelper2 = GfxAttributesBasicHelper()
        oHelper2.Run(evEle2.attributes)

        evEle3: "IVehicleGraphics2DTimeComponentsEventElement" = clr.CastAs(
            tcElement3, IVehicleGraphics2DTimeComponentsEventElement
        )
        Assert.assertIsNone(evEle3)  # should not support this interface
        evCollEle3: "IVehicleGraphics2DTimeComponentsEventCollectionElement" = clr.CastAs(
            tcElement3, IVehicleGraphics2DTimeComponentsEventCollectionElement
        )
        Assert.assertIsNotNone(evCollEle3)

        crdn = evCollEle3.get_time_component()
        Assert.assertEqual("Aircraft/Boing737 LightingIntervals EventIntervalCollection", crdn.qualified_path)

        evCollEle3.use_color_ramp = True
        Assert.assertTrue(evCollEle3.use_color_ramp)
        evCollEle3.color_ramp_start_color = Color.AliceBlue
        AssertEx.AreEqual(Color.AliceBlue, evCollEle3.color_ramp_start_color)
        evCollEle3.color_ramp_end_color = Color.AntiqueWhite
        AssertEx.AreEqual(Color.AntiqueWhite, evCollEle3.color_ramp_end_color)

        evCollEle3.use_color_ramp = False
        Assert.assertFalse(evCollEle3.use_color_ramp)
        evCollEle3.color_ramp_start_color = Color.Black
        AssertEx.AreEqual(Color.Black, evCollEle3.color_ramp_start_color)
        evCollEle3.color_ramp_end_color = Color.Blue
        AssertEx.AreEqual(Color.Blue, evCollEle3.color_ramp_end_color)
        evCollEle3.use_color_ramp = True

        oBasicHelper = GfxAttributesBasicHelper()
        oBasicHelper.Run(evCollEle3.umbra)
        oBasicHelper.Run(evCollEle3.penumbra)
        oBasicHelper.Run(evCollEle3.sunlight)

        def action34():
            tcColl.remove_at(3)

        # RemoveAt
        TryCatchAssertBlock.DoAssert("RemoveAt bad index", action34)

        tcColl.remove_at(1)
        Assert.assertEqual(2, tcColl.count)
        Assert.assertEqual(
            (("Scenario/" + oRoot.current_scenario.instance_name) + " AvailabilityIntervals EventIntervalList"),
            tcColl[0].qualified_path,
        )
        Assert.assertEqual("Aircraft/Boing737 LightingIntervals EventIntervalCollection", tcColl[1].qualified_path)

        tcColl.remove_at(0)
        Assert.assertEqual(1, tcColl.count)
        Assert.assertEqual("Aircraft/Boing737 LightingIntervals EventIntervalCollection", tcColl[0].qualified_path)

        # RemoveAll
        tcColl.remove_all()
        Assert.assertEqual(0, tcColl.count)
        if eType == GfxAttributesType.eOrbit:
            oHelper = GfxAttributesOrbitHelper()
            oHelper.Run(clr.Convert(oTimeComponents.default, IVehicleGraphics2DAttributesOrbit))
        elif eType == GfxAttributesType.eRoute:
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(clr.Convert(oTimeComponents.default, IVehicleGraphics2DAttributesRoute))
        elif eType == GfxAttributesType.eTrajectory:
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(clr.Convert(oTimeComponents.default, IVehicleGraphics2DAttributesTrajectory))
        else:
            Assert.fail("Invalid type!")


# endregion


# region GfxIntervalsCollectionHelper
class GfxIntervalsCollectionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "IVehicleGraphics2DIntervalsCollection", eType):
        Assert.assertIsNotNone(oCollection)

        self.m_logger.WriteLine("GfxIntervalsCollectionHelper test:")

        # Count
        iCount: int = oCollection.count
        self.m_logger.WriteLine3("\tThe current IntervalCollection contain: {0} elements", iCount)
        # _NewEnum
        gfxInterval: "IVehicleGraphics2DInterval"
        # _NewEnum
        for gfxInterval in oCollection:
            self.m_logger.WriteLine7(
                "\t\tElement: StartTime = {0}, StopTime = {1}", gfxInterval.start_time, gfxInterval.stop_time
            )

        # Add
        oInterval: "IVehicleGraphics2DInterval" = oCollection.add("1 Jul 1999 01:00:00.000", "1 Jul 1999 03:00:00.000")
        Assert.assertIsNotNone(oInterval)
        Assert.assertEqual("1 Jul 1999 01:00:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 03:00:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 1), oCollection.count)
        self.m_logger.WriteLine8(
            "\tAdded element: {0} - {1} (Color = {2})",
            oInterval.start_time,
            oInterval.stop_time,
            oInterval.graphics_2d_attributes.color,
        )
        # StartTime
        oInterval.start_time = "1 Jul 1999 01:12:34.000"
        Assert.assertEqual("1 Jul 1999 01:12:34.000", oInterval.start_time)
        # StopTime
        oInterval.stop_time = "1 Jul 1999 03:43:21.000"
        Assert.assertEqual("1 Jul 1999 03:43:21.000", oInterval.stop_time)
        self.m_logger.WriteLine8(
            "\tModified element: {0} - {1} (Color = {2})",
            oInterval.start_time,
            oInterval.stop_time,
            oInterval.graphics_2d_attributes.color,
        )
        if eType == GfxAttributesType.eOrbit:
            oHelper = GfxAttributesOrbitHelper()
            oHelper.Run(clr.Convert(oInterval.graphics_2d_attributes, IVehicleGraphics2DAttributesOrbit))
        elif eType == GfxAttributesType.eRoute:
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(clr.Convert(oInterval.graphics_2d_attributes, IVehicleGraphics2DAttributesRoute))
        elif eType == GfxAttributesType.eTrajectory:
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(clr.Convert(oInterval.graphics_2d_attributes, IVehicleGraphics2DAttributesTrajectory))
        else:
            Assert.fail("Invalid type!")

        # Add additional elements
        oInterval = oCollection.add("1 Jul 1999 00:00:00.000", "1 Jul 1999 00:04:00.000")
        oInterval.graphics_2d_attributes.color = Color.Yellow
        Assert.assertIsNotNone(oInterval)
        Assert.assertEqual("1 Jul 1999 00:00:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 00:04:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 2), oCollection.count)
        oInterval = oCollection.add("1 Jul 1999 00:20:00.000", "1 Jul 1999 00:25:00.000")
        Assert.assertIsNotNone(oInterval)
        oInterval.graphics_2d_attributes.color = Color.Red
        Assert.assertEqual("1 Jul 1999 00:20:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 00:25:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 3), oCollection.count)
        oInterval = oCollection.add("1 Jul 1999 00:10:00.000", "1 Jul 1999 00:15:00.000")
        Assert.assertIsNotNone(oInterval)
        oInterval.graphics_2d_attributes.color = Color.RoyalBlue
        Assert.assertEqual("1 Jul 1999 00:10:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 00:15:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 4), oCollection.count)
        oInterval = oCollection.add("1 Jul 1999 00:30:00.000", "1 Jul 1999 00:35:00.000")
        Assert.assertIsNotNone(oInterval)
        oInterval.graphics_2d_attributes.color = Color.Yellow
        Assert.assertEqual("1 Jul 1999 00:30:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 00:35:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 5), oCollection.count)

        def action35():
            oCollection.add("1 Jul 1999 00:20:00.000", "1 Jul 1999 00:25:00.000")

        TryCatchAssertBlock.ExpectedException("already exists", action35)

        # Item
        self.m_logger.WriteLine3("\tThe new IntervalCollection contain: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            oInterval = oCollection[iIndex]
            Assert.assertIsNotNone(oInterval)
            self.m_logger.WriteLine9(
                "\t\tElement {0}: {1} - {2} (Color = {3})",
                iIndex,
                oInterval.start_time,
                oInterval.stop_time,
                oInterval.graphics_2d_attributes.color,
            )

            iIndex += 1

        # RemoveAt
        iCount = oCollection.count
        self.m_logger.WriteLine3("\tBefore RemoveAt(0) collection contains {0} elements.", iCount)
        oCollection.remove_at(0)
        self.m_logger.WriteLine3("\tAfter RemoveAt(0) collection contains {0} elements.", oCollection.count)
        Assert.assertEqual((iCount - 1), oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            oInterval = oCollection[iIndex]
            Assert.assertIsNotNone(oInterval)
            self.m_logger.WriteLine9(
                "\t\tElement {0}: {1} - {2} (Color = {3})",
                iIndex,
                oInterval.start_time,
                oInterval.stop_time,
                oInterval.graphics_2d_attributes.color,
            )

            iIndex += 1

        # remove last interval
        self.m_logger.WriteLine3("\tBefore RemoveAt(3) collection contains {0} elements.", oCollection.count)
        oCollection.remove_at(3)
        self.m_logger.WriteLine3("\tAfter RemoveAt(3) collection contains {0} elements.", oCollection.count)
        Assert.assertEqual((iCount - 2), oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            oInterval = oCollection[iIndex]
            Assert.assertIsNotNone(oInterval)
            self.m_logger.WriteLine9(
                "\t\tElement {0}: {1} - {2} (Color = {3})",
                iIndex,
                oInterval.start_time,
                oInterval.stop_time,
                oInterval.graphics_2d_attributes.color,
            )

            iIndex += 1

        # remove second interval
        self.m_logger.WriteLine3("\tBefore RemoveAt(1) collection contains {0} elements.", oCollection.count)
        oCollection.remove_at(1)
        self.m_logger.WriteLine3("\tAfter RemoveAt(1) collection contains {0} elements.", oCollection.count)
        Assert.assertEqual((iCount - 3), oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            oInterval = oCollection[iIndex]
            Assert.assertIsNotNone(oInterval)
            self.m_logger.WriteLine9(
                "\t\tElement {0}: {1} - {2} (Color = {3})",
                iIndex,
                oInterval.start_time,
                oInterval.stop_time,
                oInterval.graphics_2d_attributes.color,
            )

            iIndex += 1

        # RemoveAll
        oCollection.remove_all()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains {0} elements.", oCollection.count)
        Assert.assertEqual(0, oCollection.count)


# endregion


# region GfxAttributesRealTimeHelper
class GfxAttributesRealTimeHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oRealTime: "IVehicleGraphics2DAttributesRealtime", eType):
        Assert.assertIsNotNone(oRealTime)
        if eType == GfxAttributesType.eOrbit:
            # DropOut
            oHelper = GfxAttributesOrbitHelper()
            oHelper.Run(clr.Convert(oRealTime.drop_out, IVehicleGraphics2DAttributesOrbit))
            # History
            oHelper.Run(clr.Convert(oRealTime.history, IVehicleGraphics2DAttributesOrbit))
            # LookAhead
            oHelper.Run(clr.Convert(oRealTime.look_ahead, IVehicleGraphics2DAttributesOrbit))
            # Spline
            oHelper.Run(clr.Convert(oRealTime.spline, IVehicleGraphics2DAttributesOrbit))
        elif eType == GfxAttributesType.eRoute:
            # DropOut
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(clr.Convert(oRealTime.drop_out, IVehicleGraphics2DAttributesRoute))
            # History
            oHelper.Run(clr.Convert(oRealTime.history, IVehicleGraphics2DAttributesRoute))
            # LookAhead
            oHelper.Run(clr.Convert(oRealTime.look_ahead, IVehicleGraphics2DAttributesRoute))
            # Spline
            oHelper.Run(clr.Convert(oRealTime.spline, IVehicleGraphics2DAttributesRoute))
        elif eType == GfxAttributesType.eTrajectory:
            # DropOut
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(clr.Convert(oRealTime.drop_out, IVehicleGraphics2DAttributesTrajectory))
            # History
            oHelper.Run(clr.Convert(oRealTime.history, IVehicleGraphics2DAttributesTrajectory))
            # LookAhead
            oHelper.Run(clr.Convert(oRealTime.look_ahead, IVehicleGraphics2DAttributesTrajectory))
            # Spline
            oHelper.Run(clr.Convert(oRealTime.spline, IVehicleGraphics2DAttributesTrajectory))
        else:
            Assert.fail("Invalid type!")


# endregion


# region GfxElevationContoursHelper
class GfxElevationContoursHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "IVehicleGraphics2DElevContours"):
        self.m_logger.WriteLine("----- THE GRAPHICS ELEVATION CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        self.m_oUnits.reset_units()
        # IsVisible
        self.m_logger.WriteLine4("The current IsVisible flag is: {0}", oContours.is_visible)
        oContours.is_visible = False
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", oContours.is_visible)
        Assert.assertEqual(False, oContours.is_visible)
        oContours.is_visible = True
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", oContours.is_visible)
        Assert.assertEqual(True, oContours.is_visible)
        # IsFillVisible
        self.m_logger.WriteLine4("The current IsFillVisible flag is: {0}", oContours.is_fill_visible)
        oContours.is_fill_visible = False
        self.m_logger.WriteLine4("The new IsFillVisible flag is: {0}", oContours.is_fill_visible)
        Assert.assertEqual(False, oContours.is_fill_visible)

        def action36():
            oContours.fill_style = FILL_STYLE.HATCH

        TryCatchAssertBlock.DoAssert("The FillStyle should be readonly when IsFillVisible flag is False.", action36)
        oContours.is_fill_visible = True
        self.m_logger.WriteLine4("The new IsFillVisible flag is: {0}", oContours.is_fill_visible)
        Assert.assertEqual(True, oContours.is_fill_visible)
        # FillStyle
        self.m_logger.WriteLine6("The current FillStyle is: {0}", oContours.fill_style)
        oContours.fill_style = FILL_STYLE.DIAGONAL_HATCH
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.DIAGONAL_HATCH, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.DIAGONAL_STRIPE1
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.DIAGONAL_STRIPE1, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.DIAGONAL_STRIPE2
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.DIAGONAL_STRIPE2, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.HATCH
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.HATCH, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.HORIZONTAL_STRIPE
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.HORIZONTAL_STRIPE, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.SCREEN
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.SCREEN, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.SOLID
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.SOLID, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.VERTICAL_STRIPE
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.VERTICAL_STRIPE, oContours.fill_style)

        oContours.fill_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oContours.fill_translucency, delta=Math2.Epsilon12)

        # NumOfDecimalDigits
        self.m_logger.WriteLine3("The current NumOfDecimalDigits is: {0}", oContours.num_of_decimal_digits)
        oContours.num_of_decimal_digits = 7
        self.m_logger.WriteLine3("The new NumOfDecimalDigits is: {0}", oContours.num_of_decimal_digits)
        Assert.assertEqual(7, oContours.num_of_decimal_digits)

        def action37():
            oContours.num_of_decimal_digits = 123

        TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action37)

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("The current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("The new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # Elevations
        oElevations: "IVehicleGraphics2DElevationsCollection" = oContours.elevations
        Assert.assertIsNotNone(oElevations)
        # Count
        self.m_logger.WriteLine3("The Elevations Collection contains: {0} elements.", oElevations.count)
        # _NewEnum
        elevationsElement: "IVehicleGraphics2DElevationsElement"
        # _NewEnum
        for elevationsElement in oElevations:
            self.m_logger.WriteLine10(
                "\tElement: Elevation = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, DistanceVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                elevationsElement.elevation,
                elevationsElement.color,
                elevationsElement.line_style,
                elevationsElement.line_width,
                elevationsElement.distance_visible,
                elevationsElement.user_text_visible,
                elevationsElement.user_text,
                elevationsElement.label_angle,
            )

        # AddLevel
        self.m_logger.WriteLine3(
            "Before AddLevel() the Elevations Collection contains: {0} elements.", oElevations.count
        )
        oAdded: "IVehicleGraphics2DElevationsElement" = oElevations.add_level(123.456)
        Assert.assertIsNotNone(oAdded)
        self.m_logger.WriteLine3(
            "After AddLevel() the Elevations Collection contains: {0} elements.", oElevations.count
        )
        elevationsElement: "IVehicleGraphics2DElevationsElement"
        for elevationsElement in oElevations:
            self.m_logger.WriteLine10(
                "\tElement: Elevation = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, DistanceVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                elevationsElement.elevation,
                elevationsElement.color,
                elevationsElement.line_style,
                elevationsElement.line_width,
                elevationsElement.distance_visible,
                elevationsElement.user_text_visible,
                elevationsElement.user_text,
                elevationsElement.label_angle,
            )

        # RemoveAt
        self.m_logger.WriteLine3(
            "Before RemoveAt() the Elevations Collection contains: {0} elements.", oElevations.count
        )
        oElevations.remove_at((oElevations.count - 1))
        self.m_logger.WriteLine3(
            "After RemoveAt() the Elevations Collection contains: {0} elements.", oElevations.count
        )
        # AddLevelRange
        oElevations.add_level_range(12.5, 34.5, 5.5)
        self.m_logger.WriteLine3(
            "After AddLevelRange() the Elevations Collection contains: {0} elements.", oElevations.count
        )

        iIndex: int = 0
        while iIndex < oElevations.count:
            # Item
            elevationsElement: "IVehicleGraphics2DElevationsElement" = oElevations[iIndex]
            Assert.assertIsNotNone(elevationsElement)
            self.m_logger.WriteLine10(
                "\tElement {0} (Before): Elevation = {1}, Color = {2}, LineStyle = {3}, LineWidth = {4}, DistanceVisible = {5}, UserTextVisible = {6}, UserText = {7}, LabelAngle = {8}",
                iIndex,
                elevationsElement.elevation,
                elevationsElement.color,
                elevationsElement.line_style,
                elevationsElement.line_width,
                elevationsElement.distance_visible,
                elevationsElement.user_text_visible,
                elevationsElement.user_text,
                elevationsElement.label_angle,
            )
            elevationsElement.color = Color.FromArgb((elevationsElement.color._ToOLECOLOR() + 250))
            elevationsElement.line_style = LINE_STYLE.M_DASH
            elevationsElement.line_width = LINE_WIDTH.WIDTH2
            elevationsElement.elevation += 1.5
            elevationsElement.distance_visible = not elevationsElement.distance_visible
            elevationsElement.user_text_visible = True
            elevationsElement.user_text = "User test Text"
            elevationsElement.label_angle = 15
            self.m_logger.WriteLine10(
                "\tElement {0} (After): Elevation = {1}, Color = {2}, LineStyle = {3}, LineWidth = {4}, DistanceVisible = {5}, UserTextVisible = {6}, UserText = {7}, LabelAngle = {8}",
                iIndex,
                elevationsElement.elevation,
                elevationsElement.color,
                elevationsElement.line_style,
                elevationsElement.line_width,
                elevationsElement.distance_visible,
                elevationsElement.user_text_visible,
                elevationsElement.user_text,
                elevationsElement.label_angle,
            )

            def action38():
                elevationsElement.label_angle = 1234

            TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action38)

            iIndex += 1

        def action39():
            oElevations.add_level_range(12.34, 34.12, 0.2)

        TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action39)

        def action40():
            oElevations.add_level_range(1.0, 200.0, 1.0)

        TryCatchAssertBlock.DoAssert("Cannot have in excess of 100 levels", action40)

        # RemoveAll
        oElevations.remove_all()
        self.m_logger.WriteLine3(
            "After RemoveAll() the Elevations Collection contains: {0} elements.", oElevations.count
        )
        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("The new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        self.m_logger.WriteLine("----- THE GRAPHICS ELEVATION CONTOURS TEST ----- END -----")


# endregion


# region GfxRangeContoursHelper
class GfxRangeContoursHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "IGraphics2DRangeContours"):
        self.m_logger.WriteLine("----- THE GRAPHICS RANGE CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # IsVisible
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oContours.is_visible)
        oContours.is_visible = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oContours.is_visible)
        Assert.assertFalse(oContours.is_visible)
        oContours.is_visible = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oContours.is_visible)
        Assert.assertTrue(oContours.is_visible)
        # IsFillVisible
        self.m_logger.WriteLine4("\tThe current IsFillVisible flag is: {0}", oContours.is_fill_visible)
        oContours.is_fill_visible = False
        self.m_logger.WriteLine4("\tThe new IsFillVisible flag is: {0}", oContours.is_fill_visible)
        Assert.assertFalse(oContours.is_fill_visible)

        def action41():
            oContours.fill_style = FILL_STYLE.HATCH

        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action41)
        oContours.is_fill_visible = True
        self.m_logger.WriteLine4("\tThe new IsFillVisible flag is: {0}", oContours.is_fill_visible)
        Assert.assertTrue(oContours.is_fill_visible)
        # FillStyle
        self.m_logger.WriteLine6("\tThe current FillStyle is: {0}", oContours.fill_style)
        oContours.fill_style = FILL_STYLE.DIAGONAL_HATCH
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.DIAGONAL_HATCH, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.DIAGONAL_STRIPE1
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.DIAGONAL_STRIPE1, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.DIAGONAL_STRIPE2
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.DIAGONAL_STRIPE2, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.HATCH
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.HATCH, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.HORIZONTAL_STRIPE
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.HORIZONTAL_STRIPE, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.SCREEN
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.SCREEN, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.SOLID
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.SOLID, oContours.fill_style)
        oContours.fill_style = FILL_STYLE.VERTICAL_STRIPE
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FILL_STYLE.VERTICAL_STRIPE, oContours.fill_style)
        # NumOfDecimalDigits
        self.m_logger.WriteLine3("\tThe current NumOfDecimalDigits is: {0}", oContours.num_of_decimal_digits)
        oContours.num_of_decimal_digits = 7
        self.m_logger.WriteLine3("\tThe new NumOfDecimalDigits is: {0}", oContours.num_of_decimal_digits)
        Assert.assertEqual(7, oContours.num_of_decimal_digits)

        def action42():
            oContours.num_of_decimal_digits = 123

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action42)

        def action43():
            oContours.label_unit = "test"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action43)

        oContours.fill_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oContours.fill_translucency, delta=Math2.Epsilon12)

        availableUnits = oContours.available_label_units
        self.m_logger.WriteLine3("The available units contains {0} units.", Array.Length(availableUnits))
        unit: str
        for unit in availableUnits:
            self.m_logger.WriteLine(unit)
            oContours.label_unit = unit
            Assert.assertEqual(unit, oContours.label_unit)

        # set DistanceUnit
        self.m_logger.WriteLine5(
            "\tThe current DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        # LevelAttributes
        oLevels: "ILevelAttributeCollection" = oContours.level_attributes
        Assert.assertIsNotNone(oLevels)
        # Count
        self.m_logger.WriteLine3("\tThe Level Attribute Collection contains: {0} elements.", oLevels.count)
        # _NewEnum
        levelAttribute: "ILevelAttribute"
        # _NewEnum
        for levelAttribute in oLevels:
            self.m_logger.WriteLine10(
                "\t\tElement: Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.label_visible,
                levelAttribute.label_visible,
                levelAttribute.user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )

        # AddLevel
        self.m_logger.WriteLine3(
            "\tBefore AddLevel() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        oAdded: "ILevelAttribute" = oLevels.add_level(123.456)
        Assert.assertIsNotNone(oAdded)
        self.m_logger.WriteLine3(
            "\tAfter AddLevel() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        levelAttribute: "ILevelAttribute"
        for levelAttribute in oLevels:
            self.m_logger.WriteLine10(
                "\t\tElement: Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.label_visible,
                levelAttribute.label_visible,
                levelAttribute.user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )

        # Remove
        self.m_logger.WriteLine3(
            "\tBefore Remove() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        oLevels.remove((oLevels.count - 1))
        self.m_logger.WriteLine3(
            "\tAfter RemoveAt() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        # AddLevelRange
        oLevels.add_level_range(12.5, 34.5, 0.5)
        self.m_logger.WriteLine3(
            "\tAfter AddLevelRange() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        if oLevels.count > 0:
            # Item
            levelAttribute: "ILevelAttribute" = oLevels[0]
            Assert.assertIsNotNone(levelAttribute)
            self.m_logger.WriteLine10(
                "\t\tElement (Before): Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.label_visible,
                levelAttribute.label_visible,
                levelAttribute.user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )
            levelAttribute.color = Color.FromArgb((levelAttribute.color._ToOLECOLOR() + 250))
            levelAttribute.line_style = LINE_STYLE.M_DASH
            levelAttribute.line_width = LINE_WIDTH.WIDTH2
            levelAttribute.level = float(levelAttribute.level) + 1.5
            levelAttribute.label_visible = not levelAttribute.label_visible
            levelAttribute.user_text_visible = True
            levelAttribute.user_text = "UserText test string"
            levelAttribute.label_angle = 15
            self.m_logger.WriteLine10(
                "\t\tElement (After): Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.label_visible,
                levelAttribute.label_visible,
                levelAttribute.user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )

            def action44():
                levelAttribute.label_angle = 1234

            TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action44)

        def action45():
            oLevels.add_level_range(12.34, 34.12, 0.2)

        TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action45)

        # RemoveAll
        oLevels.remove_all()
        self.m_logger.WriteLine3("\tAfter RemoveAll() the Elevations Collection contains: {0} elements.", oLevels.count)
        Assert.assertEqual(0, oLevels.count)
        self.m_logger.WriteLine("----- THE GRAPHICS RANGE CONTOURS TEST ----- END -----")


# endregion


# region GfxSAAContoursHelper
class GfxSAAContoursHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "IVehicleGraphics2DSAA"):
        self.m_logger.WriteLine("----- THE GRAPHICS SAA CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # IsVisible
        self.m_logger.WriteLine4("The current IsVisible flag is: {0}", oContours.is_visible)
        oContours.is_visible = False
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", oContours.is_visible)
        Assert.assertEqual(False, oContours.is_visible)
        oContours.is_visible = True
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", oContours.is_visible)
        Assert.assertEqual(True, oContours.is_visible)
        # IsFillVisible (false)
        self.m_logger.WriteLine4("The current IsFillVisible flag is: {0}", oContours.is_fill_visible)
        oContours.is_fill_visible = False
        self.m_logger.WriteLine4("The new IsFillVisible flag is: {0}", oContours.is_fill_visible)
        Assert.assertEqual(False, oContours.is_fill_visible)

        # IsFillVisible (true)
        oContours.is_fill_visible = True
        self.m_logger.WriteLine4("The new IsFillVisible flag is: {0}", oContours.is_fill_visible)
        Assert.assertEqual(True, oContours.is_fill_visible)

        # Translucency
        oContours.translucency = 73.0
        self.m_logger.WriteLine6("The new Translucency value is: {0}", oContours.translucency)
        Assert.assertAlmostEqual(73.0, oContours.translucency, delta=Math2.Epsilon3)
        oContours.translucency = 13.0
        self.m_logger.WriteLine6("The new Translucency value is: {0}", oContours.translucency)
        Assert.assertAlmostEqual(13.0, oContours.translucency, delta=Math2.Epsilon3)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("The current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("The new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # UseVehicleAlt (true)
        self.m_logger.WriteLine4("The current UseVehicleAltitude flag is: {0}", oContours.use_vehicle_altitude)
        oContours.use_vehicle_altitude = True
        self.m_logger.WriteLine4("The new UseVehicleAltitude flag is: {0}", oContours.use_vehicle_altitude)
        Assert.assertEqual(True, oContours.use_vehicle_altitude)

        def action46():
            oContours.altitude = 123.456

        TryCatchAssertBlock.ExpectedException("read only", action46)

        # UseVehicleAlt (false)
        oContours.use_vehicle_altitude = False
        self.m_logger.WriteLine4("The new UseVehicleAltitude flag is: {0}", oContours.use_vehicle_altitude)
        Assert.assertEqual(False, oContours.use_vehicle_altitude)
        # Altitude
        self.m_logger.WriteLine6("The current Altitude is: {0}", oContours.altitude)
        oContours.altitude = 345.678
        self.m_logger.WriteLine6("The new Altitude is: {0}", oContours.altitude)
        Assert.assertEqual(345.678, oContours.altitude)

        def action47():
            oContours.altitude = 1234.56

        TryCatchAssertBlock.ExpectedException("is invalid", action47)

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("The new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        self.m_logger.WriteLine("----- THE GRAPHICS SAA CONTOURS TEST ----- END -----")


# endregion


# region GfxGroundEllipsesHelper
class GfxGroundEllipsesHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "IVehicleGraphics2DGroundEllipsesCollection"):
        self.m_logger.WriteLine("----- THE GRAPHICS GROUND ELLIPSES TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\tGfxGroundEllipses collection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            oEllipse: "IVehicleGraphics2DGroundEllipsesElement" = oCollection[iIndex]
            self.m_logger.WriteLine10(
                "\t\tEllipse {0}: EllipseSetName = {1}, Color = {7}, LineWidth = {8}, StaticGfx = {2}, DynamicGfx = {3}, Interpolate = {4}, IsNameVisible = {5}, IsCenterVisible = {6}",
                iIndex,
                oEllipse.ellipse_set_name,
                oEllipse.static_graphics_2d,
                oEllipse.dynamic_graphics_2d,
                oEllipse.interpolate,
                oEllipse.is_name_visible,
                oEllipse.is_center_visible,
                oEllipse.color,
                oEllipse.line_width,
            )

            iIndex += 1

        # _NewEnum
        groundEllipsesElement: "IVehicleGraphics2DGroundEllipsesElement"
        # _NewEnum
        for groundEllipsesElement in oCollection:
            # modify properties
            groundEllipsesElement.static_graphics_2d = True
            groundEllipsesElement.dynamic_graphics_2d = True
            groundEllipsesElement.interpolate = True
            groundEllipsesElement.is_name_visible = True
            groundEllipsesElement.is_center_visible = True
            groundEllipsesElement.color = Color.FromArgb(66047)
            groundEllipsesElement.line_width = LINE_WIDTH.WIDTH2

        iIndex: int = 0
        while iIndex < oCollection.count:
            oEllipse: "IVehicleGraphics2DGroundEllipsesElement" = oCollection[iIndex]
            self.m_logger.WriteLine10(
                "\t\tModified Ellipse {0}: EllipseSetName = {1}, Color = {7}, LineWidth = {8}, StaticGfx = {2}, DynamicGfx = {3}, Interpolate = {4}, IsNameVisible = {5}, IsCenterVisible = {6}",
                iIndex,
                oEllipse.ellipse_set_name,
                oEllipse.static_graphics_2d,
                oEllipse.dynamic_graphics_2d,
                oEllipse.interpolate,
                oEllipse.is_name_visible,
                oEllipse.is_center_visible,
                oEllipse.color,
                oEllipse.line_width,
            )

            iIndex += 1

        self.m_logger.WriteLine("----- THE GRAPHICS GROUND ELLIPSES TEST ----- END -----")


# endregion


# region GfxLightingHelper
class GfxLightingHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oLighting: "IVehicleGraphics2DLighting"):
        self.m_logger.WriteLine("----- THE GRAPHICS LIGHTING TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oLighting)
        # IsSunLightPenumbraVisible
        self.m_logger.WriteLine4(
            "The current IsSunLightPenumbraVisible flag is: {0}", oLighting.is_sun_light_penumbra_visible
        )
        oLighting.is_sun_light_penumbra_visible = False
        self.m_logger.WriteLine4(
            "The new IsSunLightPenumbraVisible flag is: {0}", oLighting.is_sun_light_penumbra_visible
        )
        Assert.assertEqual(False, oLighting.is_sun_light_penumbra_visible)
        oLighting.is_sun_light_penumbra_visible = True
        self.m_logger.WriteLine4(
            "The new IsSunLightPenumbraVisible flag is: {0}", oLighting.is_sun_light_penumbra_visible
        )
        Assert.assertEqual(True, oLighting.is_sun_light_penumbra_visible)
        # IsPenumbraUmbraVisible
        self.m_logger.WriteLine4("The current IsPenumbraUmbraVisible flag is: {0}", oLighting.is_penumbra_umbra_visible)
        oLighting.is_penumbra_umbra_visible = False
        self.m_logger.WriteLine4("The new IsPenumbraUmbraVisible flag is: {0}", oLighting.is_penumbra_umbra_visible)
        Assert.assertEqual(False, oLighting.is_penumbra_umbra_visible)
        oLighting.is_penumbra_umbra_visible = True
        self.m_logger.WriteLine4("The new IsPenumbraUmbraVisible flag is: {0}", oLighting.is_penumbra_umbra_visible)
        Assert.assertEqual(True, oLighting.is_penumbra_umbra_visible)
        # IsSolarSpecularReflectionPointVisible
        self.m_logger.WriteLine4(
            "The current IsSolarSpecularReflectionPointVisible flag is: {0}",
            oLighting.is_solar_specular_reflection_point_visible,
        )
        oLighting.is_solar_specular_reflection_point_visible = False
        self.m_logger.WriteLine4(
            "The new IsSolarSpecularReflectionPointVisible flag is: {0}",
            oLighting.is_solar_specular_reflection_point_visible,
        )
        Assert.assertEqual(False, oLighting.is_solar_specular_reflection_point_visible)
        oLighting.is_solar_specular_reflection_point_visible = True
        self.m_logger.WriteLine4(
            "The new IsSolarSpecularReflectionPointVisible flag is: {0}",
            oLighting.is_solar_specular_reflection_point_visible,
        )
        Assert.assertEqual(True, oLighting.is_solar_specular_reflection_point_visible)
        # Sunlight
        self.m_logger.WriteLine("Sunlight test:")
        self.LightingElement(oLighting.sunlight)
        # Penumbra
        self.m_logger.WriteLine("Penumbra test:")
        self.LightingElement(oLighting.penumbra)
        # Umbra
        self.m_logger.WriteLine("Umbra test:")
        self.LightingElement(oLighting.umbra)
        self.m_logger.WriteLine("----- THE GRAPHICS LIGHTING TEST ----- END -----")

    # endregion

    # region LightingElement method
    def LightingElement(self, oVeGfxLightingElement: "IVehicleGraphics2DLightingElement"):
        Assert.assertIsNotNone(oVeGfxLightingElement)
        # Visible (false)
        self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oVeGfxLightingElement.visible)
        oVeGfxLightingElement.visible = False
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oVeGfxLightingElement.visible)
        Assert.assertEqual(False, oVeGfxLightingElement.visible)

        def action48():
            oVeGfxLightingElement.color = Color.FromArgb(12632256)

        TryCatchAssertBlock.ExpectedException("read-only", action48)

        def action49():
            oVeGfxLightingElement.line_style = LINE_STYLE.DOT_DASHED

        TryCatchAssertBlock.ExpectedException("read-only", action49)

        def action50():
            oVeGfxLightingElement.line_width = LINE_WIDTH.WIDTH1

        TryCatchAssertBlock.ExpectedException("read-only", action50)

        def action51():
            oVeGfxLightingElement.marker_style = "Circle"

        TryCatchAssertBlock.ExpectedException("read-only", action51)

        # Visible (true)
        oVeGfxLightingElement.visible = True
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oVeGfxLightingElement.visible)
        Assert.assertEqual(True, oVeGfxLightingElement.visible)
        # Color
        self.m_logger.WriteLine6("\tThe current Color is: {0}", oVeGfxLightingElement.color)
        oVeGfxLightingElement.color = Color.FromArgb(255)
        self.m_logger.WriteLine6("\tThe new Color is: {0}", oVeGfxLightingElement.color)
        AssertEx.AreEqual(Color.FromArgb(255), oVeGfxLightingElement.color)
        # LineStyle
        self.m_logger.WriteLine6("\tThe current LineStyle is: {0}", oVeGfxLightingElement.line_style)
        oVeGfxLightingElement.line_style = LINE_STYLE.DOT_DASHED
        self.m_logger.WriteLine6("\tThe new LineStyle is: {0}", oVeGfxLightingElement.line_style)
        Assert.assertEqual(LINE_STYLE.DOT_DASHED, oVeGfxLightingElement.line_style)

        # LineWidth
        self.m_logger.WriteLine6("\tThe current LineWidth is: {0}", oVeGfxLightingElement.line_width)
        oVeGfxLightingElement.line_width = LINE_WIDTH.WIDTH3
        self.m_logger.WriteLine6("\tThe new LineWidth is: {0}", oVeGfxLightingElement.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH3, oVeGfxLightingElement.line_width)

        def action52():
            oVeGfxLightingElement.line_width = clr.Convert((-1), LINE_WIDTH)

        TryCatchAssertBlock.DoAssert("LineWidth -1 should fail.", action52)

        def action53():
            oVeGfxLightingElement.line_width = clr.Convert((11), LINE_WIDTH)

        TryCatchAssertBlock.DoAssert("LineWidth 11 should fail.", action53)

        # MarkerStyle
        self.m_logger.WriteLine5("\tThe current MarkerStyle is: {0}", oVeGfxLightingElement.marker_style)
        oVeGfxLightingElement.marker_style = "X"
        self.m_logger.WriteLine5("\tThe new MarkerStyle is: {0}", oVeGfxLightingElement.marker_style)
        Assert.assertEqual("X", oVeGfxLightingElement.marker_style)


# endregion


# region GfxRouteResolutionHelper
class GfxRouteResolutionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oResolution: "IVehicleGraphics2DRouteResolution"):
        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oResolution)
        # Route
        self.m_logger.WriteLine6("The current Route is: {0}", oResolution.route)
        oResolution.route = 12345.6789
        self.m_logger.WriteLine6("The new Route is: {0}", oResolution.route)
        Assert.assertEqual(12345.6789, oResolution.route)

        oResolution.min_route = 1
        Assert.assertEqual(1, oResolution.min_route)

        def action54():
            oResolution.min_route = -1

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action54)

        def action55():
            oResolution.route = -12345.6789

        TryCatchAssertBlock.DoAssert("Cannot set illegal value.", action55)

        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- END -----")


# endregion


# region GfxTrajectoryResolutionHelper
class GfxTrajectoryResolutionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oResolution: "IVehicleGraphics2DTrajectoryResolution"):
        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oResolution)
        # GroundTrack
        self.m_logger.WriteLine6("The current GroundTrack is: {0}", oResolution.ground_track)
        oResolution.ground_track = 12345.6789
        self.m_logger.WriteLine6("The new GroundTrack is: {0}", oResolution.ground_track)
        Assert.assertEqual(12345.6789, oResolution.ground_track)

        oResolution.min_ground_track = 1
        Assert.assertEqual(1, oResolution.min_ground_track)

        def action56():
            oResolution.min_ground_track = -1

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action56)

        def action57():
            oResolution.ground_track = -12345.6789

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action57)

        # Trajectory
        self.m_logger.WriteLine6("The current Trajectory is: {0}", oResolution.trajectory)
        oResolution.trajectory = 6789.12345
        self.m_logger.WriteLine6("The new Trajectory is: {0}", oResolution.trajectory)
        Assert.assertEqual(6789.12345, oResolution.trajectory)

        oResolution.min_trajectory = 1
        Assert.assertEqual(1, oResolution.min_trajectory)

        def action58():
            oResolution.min_trajectory = -1

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action58)

        def action59():
            oResolution.trajectory = -12345.6789

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action59)

        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- END -----")


# endregion


# region GfxPassResolutionHelper
class GfxPassResolutionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oResolution: "IVehicleGraphics2DPassResolution"):
        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oResolution)
        # GroundTrack
        self.m_logger.WriteLine6("The current GroundTrack is: {0}", oResolution.ground_track)
        oResolution.ground_track = 12345.6789
        self.m_logger.WriteLine6("The new GroundTrack is: {0}", oResolution.ground_track)
        Assert.assertEqual(12345.6789, oResolution.ground_track)

        oResolution.min_ground_track = 1
        Assert.assertEqual(1, oResolution.min_ground_track)

        def action60():
            oResolution.min_ground_track = -1

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action60)

        def action61():
            oResolution.ground_track = -12345.6789

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action61)

        # Orbit
        self.m_logger.WriteLine6("The current Orbit is: {0}", oResolution.orbit)
        oResolution.orbit = 6789.12345
        self.m_logger.WriteLine6("The new Orbit is: {0}", oResolution.orbit)
        Assert.assertEqual(6789.12345, oResolution.orbit)

        oResolution.min_orbit = 1
        Assert.assertEqual(1, oResolution.min_orbit)

        def action62():
            oResolution.min_orbit = -1

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action62)

        def action63():
            oResolution.orbit = -12345.6789

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action63)

        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- END -----")


# endregion


# region GfxLeadTrailDataHelper
class GfxLeadTrailDataHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, leadTrailData: "IVehicleGraphics2DLeadTrailData"):
        Assert.assertIsNotNone(leadTrailData)
        self.m_logger.WriteLine("GfxLeadTrailData test:")

        # LeadDataSupportedTypes
        arSupportedTypes = leadTrailData.lead_data_supported_types
        self.m_logger.WriteLine3("\tThe LeadData supports: {0} types", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            self.m_logger.WriteLine8(
                "\t\tType {0} is: {1} ({2})",
                iIndex,
                str(arSupportedTypes[iIndex][1]),
                clr.Convert(int(arSupportedTypes[iIndex][0]), LEAD_TRAIL_DATA),
            )

            iIndex += 1

        # LeadDataType
        self.m_logger.WriteLine6("\tThe current LeadDataType is: {0}", leadTrailData.lead_data_type)

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            eType: "LEAD_TRAIL_DATA" = clr.Convert(int(arSupportedTypes[iIndex][0]), LEAD_TRAIL_DATA)
            if not leadTrailData.is_lead_data_type_supported(eType):
                Assert.fail("The {0} LeadType should be supported!", eType)

            # SetLeadDataType
            leadTrailData.set_lead_data_type(eType)
            self.m_logger.WriteLine6("\tThe new LeadDataType is: {0}", leadTrailData.lead_data_type)
            Assert.assertEqual(eType, leadTrailData.lead_data_type)
            if leadTrailData.has_lead_data:
                if eType == LEAD_TRAIL_DATA.DATA_FRACTION:
                    # LeadData
                    oFraction: "IVehicleLeadTrailDataFraction" = clr.Convert(
                        leadTrailData.lead_data, IVehicleLeadTrailDataFraction
                    )
                    Assert.assertIsNotNone(oFraction)
                    # Fraction
                    self.m_logger.WriteLine6("\t\tThe current Fraction is: {0}", oFraction.fraction)
                    oFraction.fraction = 12.3456
                    self.m_logger.WriteLine6("\t\tThe new Fraction is: {0}", oFraction.fraction)
                    Assert.assertEqual(12.3456, oFraction.fraction)

                    def action64():
                        oFraction.fraction = -56.34

                    # range test
                    TryCatchAssertBlock.ExpectedException("is invalid", action64)
                elif eType == LEAD_TRAIL_DATA.DATA_TIME:
                    # LeadData
                    oTime: "IVehicleLeadTrailDataTime" = clr.Convert(leadTrailData.lead_data, IVehicleLeadTrailDataTime)
                    Assert.assertIsNotNone(oTime)
                    # set TimeUnit
                    strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
                    self.m_logger.WriteLine5("\tThe current TimeUnit is: {0}", strUnit)
                    self.m_oUnits.set_current_unit("TimeUnit", "hr")
                    self.m_logger.WriteLine5(
                        "\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
                    )
                    Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
                    # Time
                    self.m_logger.WriteLine6("\t\tThe current Time is: {0}", oTime.time)
                    oTime.time = 123.456
                    self.m_logger.WriteLine6("\t\tThe new Time is: {0}", oTime.time)
                    Assert.assertEqual(123.456, oTime.time)

                    def action65():
                        oTime.time = 56340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

                    # range test
                    TryCatchAssertBlock.ExpectedException("is invalid", action65)
                    # restore TimeUnit
                    self.m_oUnits.set_current_unit("TimeUnit", strUnit)
                    self.m_logger.WriteLine5("\tThe new TimeUnit (restored) is: {0}", strUnit)
                    Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
                else:
                    Assert.fail("Invalid LeadDataType has a LeadData!")

            else:
                self.m_logger.WriteLine6("\tThe LeadData is not supported by {0}.", leadTrailData.lead_data_type)

            iIndex += 1

        # TrailDataSupportedTypes
        arSupportedTypes = leadTrailData.trail_data_supported_types
        self.m_logger.WriteLine3("\tThe TrailData supports: {0} types", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            self.m_logger.WriteLine8(
                "\t\tType {0} is: {1} ({2})",
                iIndex,
                str(arSupportedTypes[iIndex][1]),
                clr.Convert(int(arSupportedTypes[iIndex][0]), LEAD_TRAIL_DATA),
            )

            iIndex += 1

        # TrailDataType
        self.m_logger.WriteLine6("\tThe current TrailDataType is: {0}", leadTrailData.trail_data_type)

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            eType: "LEAD_TRAIL_DATA" = clr.Convert(int(arSupportedTypes[iIndex][0]), LEAD_TRAIL_DATA)
            if not leadTrailData.is_trail_data_type_supported(eType):
                Assert.fail("The {0} TrailType should be supported!", eType)

            # SetTrailDataType
            leadTrailData.set_trail_data_type(eType)
            self.m_logger.WriteLine6("\tThe new TrailDataType is: {0}", leadTrailData.trail_data_type)
            Assert.assertEqual(eType, leadTrailData.trail_data_type)
            if leadTrailData.has_trail_data:
                if eType == LEAD_TRAIL_DATA.DATA_FRACTION:
                    # TrailData
                    oFraction: "IVehicleLeadTrailDataFraction" = clr.Convert(
                        leadTrailData.trail_data, IVehicleLeadTrailDataFraction
                    )
                    Assert.assertIsNotNone(oFraction)
                    # Fraction
                    self.m_logger.WriteLine6("\t\tThe current Fraction is: {0}", oFraction.fraction)
                    oFraction.fraction = 12.3456
                    self.m_logger.WriteLine6("\t\tThe new Fraction is: {0}", oFraction.fraction)
                    Assert.assertEqual(12.3456, oFraction.fraction)

                    def action66():
                        oFraction.fraction = -56.34

                    # range test

                    TryCatchAssertBlock.ExpectedException("is invalid", action66)
                elif eType == LEAD_TRAIL_DATA.DATA_TIME:
                    # TrailData
                    oTime: "IVehicleLeadTrailDataTime" = clr.Convert(
                        leadTrailData.trail_data, IVehicleLeadTrailDataTime
                    )
                    Assert.assertIsNotNone(oTime)
                    # set TimeUnit
                    strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
                    self.m_logger.WriteLine5("\tThe current TimeUnit is: {0}", strUnit)
                    self.m_oUnits.set_current_unit("TimeUnit", "hr")
                    self.m_logger.WriteLine5(
                        "\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
                    )
                    Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
                    # Time
                    self.m_logger.WriteLine6("\t\tThe current Time is: {0}", oTime.time)
                    oTime.time = 123.456
                    self.m_logger.WriteLine6("\t\tThe new Time is: {0}", oTime.time)
                    Assert.assertEqual(123.456, oTime.time)

                    def action67():
                        oTime.time = 56340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

                    # range test

                    TryCatchAssertBlock.ExpectedException("is invalid", action67)

                    # restore TimeUnit
                    self.m_oUnits.set_current_unit("TimeUnit", strUnit)
                    self.m_logger.WriteLine5("\tThe new TimeUnit (restored) is: {0}", strUnit)
                    Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
                else:
                    Assert.fail("Invalid TrailDataType has a TrailData!")

            else:
                self.m_logger.WriteLine6("\tThe TrailData is not supported by {0}.", leadTrailData.trail_data_type)

            iIndex += 1

        # SetTrailSameAsLead
        leadTrailData.set_trail_data_type(clr.Convert(int(arSupportedTypes[0][0]), LEAD_TRAIL_DATA))
        self.m_logger.WriteLine7(
            "\tBefore: TrailDataType = {0}, LeadDataType = {1}",
            leadTrailData.trail_data_type,
            leadTrailData.lead_data_type,
        )
        leadTrailData.set_trail_same_as_lead()
        self.m_logger.WriteLine7(
            "\tAfter:  TrailDataType = {0}, LeadDataType = {1}",
            leadTrailData.trail_data_type,
            leadTrailData.lead_data_type,
        )
        Assert.assertEqual(leadTrailData.lead_data_type, leadTrailData.trail_data_type)


# endregion


# region GfxSwathHelper
class GfxSwathHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oSwath: "IVehicleGraphics2DSwath"):
        self.m_logger.WriteLine("----- THE GRAPHICS SWATH TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oSwath)

        # ElevationType
        self.m_logger.WriteLine6("The current Elevation type is: {0}", oSwath.elevation_type)
        # ElevationSupportedTypes
        arTypes = oSwath.elevation_supported_types
        self.m_logger.WriteLine3("Available {0} Elevation types.", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_GRAPHICS_2D_ELEVATION" = clr.Convert(int(arTypes[iIndex][0]), VEHICLE_GRAPHICS_2D_ELEVATION)
            self.m_logger.WriteLine8("\tElevation type {0}: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not oSwath.is_elevation_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            oSwath.set_elevation_type(eType)
            self.m_logger.WriteLine6("\t\tThe new Elevation type is: {0}", oSwath.elevation_type)
            Assert.assertEqual(eType, oSwath.elevation_type)
            if ((oSwath.elevation_type == VEHICLE_GRAPHICS_2D_ELEVATION.ELEVATION_GROUND_ELEVATION)) or (
                (oSwath.elevation_type == VEHICLE_GRAPHICS_2D_ELEVATION.ELEVATION_GROUND_ELEVATION_ENVELOPE)
            ):
                # Elevation
                gfxElevationGroundElevation: "IVehicleGraphics2DElevationGroundElevation" = clr.Convert(
                    oSwath.elevation, IVehicleGraphics2DElevationGroundElevation
                )
                Assert.assertIsNotNone(gfxElevationGroundElevation)
                # set AngleUnit
                strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
                self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
                self.m_oUnits.set_current_unit("AngleUnit", "rad")
                self.m_logger.WriteLine5(
                    "\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit")
                )
                Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
                # Angle
                self.m_logger.WriteLine6(
                    "\t\t\tThe current GroundElevation angle is: {0}", gfxElevationGroundElevation.angle
                )
                gfxElevationGroundElevation.angle = 12.34
                self.m_logger.WriteLine6(
                    "\t\t\tThe new GroundElevation angle is: {0}", gfxElevationGroundElevation.angle
                )
                Assert.assertEqual(12.34, gfxElevationGroundElevation.angle)

                def action68():
                    gfxElevationGroundElevation.angle = -56.34

                TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action68)
                # restore AngleUnit
                self.m_oUnits.set_current_unit("AngleUnit", strUnit)
                self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
                Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
            elif oSwath.elevation_type == VEHICLE_GRAPHICS_2D_ELEVATION.ELEVATION_SWATH_HALF_WIDTH:
                # Elevation
                gfxElevationSwathHalfWidth: "IVehicleGraphics2DElevationSwathHalfWidth" = clr.Convert(
                    oSwath.elevation, IVehicleGraphics2DElevationSwathHalfWidth
                )
                Assert.assertIsNotNone(gfxElevationSwathHalfWidth)
                # set DistanceUnit
                strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
                self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
                self.m_oUnits.set_current_unit("DistanceUnit", "m")
                self.m_logger.WriteLine5(
                    "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
                )
                Assert.assertEqual("m", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
                # Distance
                self.m_logger.WriteLine6(
                    "\t\t\tThe current SwathHalfWidth distance is: {0}", gfxElevationSwathHalfWidth.distance
                )
                gfxElevationSwathHalfWidth.distance = 56.78
                self.m_logger.WriteLine6(
                    "\t\t\tThe new SwathHalfWidth distance is: {0}", gfxElevationSwathHalfWidth.distance
                )
                Assert.assertEqual(56.78, gfxElevationSwathHalfWidth.distance)

                def action69():
                    gfxElevationSwathHalfWidth.distance = -56.34

                TryCatchAssertBlock.ExpectedException("is invalid", action69)

                # restore DistanceUnit
                self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
                self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
                Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
            elif ((oSwath.elevation_type == VEHICLE_GRAPHICS_2D_ELEVATION.ELEVATION_VEHICLE_HALF_ANGLE)) or (
                (oSwath.elevation_type == VEHICLE_GRAPHICS_2D_ELEVATION.ELEVATION_VEHICLE_HALF_ANGLE_ENVELOPE)
            ):
                gfxElevationVehicleHalfAngle: "IVehicleGraphics2DElevationVehicleHalfAngle" = clr.Convert(
                    oSwath.elevation, IVehicleGraphics2DElevationVehicleHalfAngle
                )
                Assert.assertIsNotNone(gfxElevationVehicleHalfAngle)
                # set AngleUnit
                strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
                self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
                self.m_oUnits.set_current_unit("AngleUnit", "rad")
                self.m_logger.WriteLine5(
                    "\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit")
                )
                Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
                # Angle
                self.m_logger.WriteLine6(
                    "\t\t\tThe current VehicleHalfAngle angle is: {0}", gfxElevationVehicleHalfAngle.angle
                )
                gfxElevationVehicleHalfAngle.angle = 78.9
                self.m_logger.WriteLine6(
                    "\t\t\tThe new VehicleHalfAngle angle is: {0}", gfxElevationVehicleHalfAngle.angle
                )
                Assert.assertEqual(78.9, gfxElevationVehicleHalfAngle.angle)

                def action70():
                    gfxElevationVehicleHalfAngle.angle = -56.34

                TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action70)
                # restore AngleUnit
                self.m_oUnits.set_current_unit("AngleUnit", strUnit)
                self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
                Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
            else:
                Assert.fail("Invalid type: {0}!", eType)

            iIndex += 1

        def action71():
            oSwath.set_elevation_type(VEHICLE_GRAPHICS_2D_ELEVATION.ELEVATION_UNKNOWN)

        # SetElevationType(eElevationUnknown)
        TryCatchAssertBlock.ExpectedException("must be in", action71)

        oSwath.set_elevation_type(VEHICLE_GRAPHICS_2D_ELEVATION.ELEVATION_GROUND_ELEVATION)

        # Options
        self.m_logger.WriteLine6("The current Options is: {0}", oSwath.options)
        oSwath.options = VEHICLE_GRAPHICS_2D_OPTIONS.OPTIONS_EDGE_LIMITS
        self.m_logger.WriteLine6("The new Options is: {0}", oSwath.options)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_OPTIONS.OPTIONS_EDGE_LIMITS, oSwath.options)
        oSwath.options = VEHICLE_GRAPHICS_2D_OPTIONS.OPTIONS_FILLED_LIMITS
        self.m_logger.WriteLine6("The new Options is: {0}", oSwath.options)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_OPTIONS.OPTIONS_FILLED_LIMITS, oSwath.options)
        oSwath.options = VEHICLE_GRAPHICS_2D_OPTIONS.OPTIONS_NO_GRAPHICS
        self.m_logger.WriteLine6("The new Options is: {0}", oSwath.options)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_OPTIONS.OPTIONS_NO_GRAPHICS, oSwath.options)
        self.m_logger.WriteLine("----- THE GRAPHICS SWATH TEST ----- END -----")


# endregion


# region GfxWaypointMarkersHelper
class GfxWaypointMarkersHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oMarker: "IVehicleGraphics2DWaypointMarker"):
        self.m_logger.WriteLine("----- THE GRAPHICS WAYPOINT MARKERS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oMarker)
        # IsWaypointMarkersVisible (false)
        self.m_logger.WriteLine4("The current WaypointMarkersVisible flag is: {0}", oMarker.is_waypoint_markers_visible)
        oMarker.is_waypoint_markers_visible = False
        self.m_logger.WriteLine4("The new WaypointMarkersVisible flag is: {0}", oMarker.is_waypoint_markers_visible)
        Assert.assertEqual(False, oMarker.is_waypoint_markers_visible)

        def action72():
            oMarker.is_turn_markers_visible = True

        TryCatchAssertBlock.ExpectedException("read-only", action72)

        # IsWaypointMarkersVisible (true)
        oMarker.is_waypoint_markers_visible = True
        self.m_logger.WriteLine4("The new WaypointMarkersVisible flag is: {0}", oMarker.is_waypoint_markers_visible)
        Assert.assertEqual(True, oMarker.is_waypoint_markers_visible)
        # IsTurnMarkersVisible
        self.m_logger.WriteLine4("The current IsTurnMarkersVisible flag is: {0}", oMarker.is_turn_markers_visible)
        oMarker.is_turn_markers_visible = False
        self.m_logger.WriteLine4("The new IsTurnMarkersVisible flag is: {0}", oMarker.is_turn_markers_visible)
        Assert.assertEqual(False, oMarker.is_turn_markers_visible)
        oMarker.is_turn_markers_visible = True
        self.m_logger.WriteLine4("The new IsTurnMarkersVisible flag is: {0}", oMarker.is_turn_markers_visible)
        Assert.assertEqual(True, oMarker.is_turn_markers_visible)
        # WaypointMarkers
        oCollection: "IVehicleGraphics2DWaypointMarkersCollection" = oMarker.waypoint_markers
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The WaypointMarkers collection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            if iIndex == 0:
                self.m_logger.WriteLine("\tBefore modification:")

            # Item
            waypointMarkersElement: "IVehicleGraphics2DWaypointMarkersElement" = oCollection[iIndex]
            Assert.assertIsNotNone(waypointMarkersElement)
            self.m_logger.WriteLine10(
                "\t\tElement {0}: Time = {1}, Color = {2}, UseVehColor = {3}, MarkerStyle = {4}, IsLabelVisible = {5}, Label = {6}, IsVisible = {7}",
                iIndex,
                waypointMarkersElement.time,
                waypointMarkersElement.color,
                waypointMarkersElement.use_veh_color,
                waypointMarkersElement.marker_style,
                waypointMarkersElement.is_label_visible,
                waypointMarkersElement.label,
                waypointMarkersElement.is_visible,
            )

            iIndex += 1

        # _NewEnum
        waypointMarkersElement: "IVehicleGraphics2DWaypointMarkersElement"
        # _NewEnum
        for waypointMarkersElement in oCollection:
            waypointMarkersElement.use_veh_color = True

            def action73():
                waypointMarkersElement.color = Color.FromArgb(1193046)

            TryCatchAssertBlock.ExpectedException("read-only", action73)

            waypointMarkersElement.is_label_visible = True
            waypointMarkersElement.label = "WaypointLabel"
            waypointMarkersElement.is_visible = True
            waypointMarkersElement.use_veh_color = False
            waypointMarkersElement.color = Color.FromArgb(65280)
            waypointMarkersElement.marker_style = "X"

        iIndex: int = 0
        while iIndex < oCollection.count:
            if iIndex == 0:
                self.m_logger.WriteLine("\tAfter  modification:")

            # Item
            waypointMarkersElement: "IVehicleGraphics2DWaypointMarkersElement" = oCollection[iIndex]
            Assert.assertIsNotNone(waypointMarkersElement)
            self.m_logger.WriteLine10(
                "\t\tElement {0}: Time = {1}, Color = {2}, UseVehColor = {3}, MarkerStyle = {4}, IsLabelVisible = {5}, Label = {6}, IsVisible = {7}",
                iIndex,
                waypointMarkersElement.time,
                waypointMarkersElement.color,
                waypointMarkersElement.use_veh_color,
                waypointMarkersElement.marker_style,
                waypointMarkersElement.is_label_visible,
                waypointMarkersElement.label,
                waypointMarkersElement.is_visible,
            )

            iIndex += 1

        self.m_logger.WriteLine("----- THE GRAPHICS WAYPOINT MARKERS TEST ----- END -----")


# endregion


# region GfxTimeEventsHelper
class GfxTimeEventsHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, AG_SAT: "ISatellite", oCollection: "IVehicleGraphics2DTimeEventsCollection"):
        self.m_logger.WriteLine("----- THE GRAPHICS TIME EVENTS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The TimeEvents collection contains: {0} elements.", oCollection.count)
        # Add
        timeEventsElement: "IVehicleGraphics2DTimeEventsElement" = oCollection.add()
        Assert.assertIsNotNone(timeEventsElement)
        self.m_logger.WriteLine3("After Add() the Time Events collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual(1, oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            self.m_logger.WriteLine8(
                "\tElement {0}: TimeEventType = {1}, IsVisible = {2}",
                iIndex,
                oCollection[iIndex].time_event_type,
                oCollection[iIndex].is_visible,
            )

            iIndex += 1

        # IsVisible (false)
        self.m_logger.WriteLine4("The current IsVisible flag is: {0}", timeEventsElement.is_visible)
        timeEventsElement.is_visible = False
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", timeEventsElement.is_visible)
        Assert.assertEqual(False, timeEventsElement.is_visible)

        def action74():
            timeEventsElement.set_time_event_type(VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE.TIME_EVENT_TYPE_LINE)

        TryCatchAssertBlock.ExpectedException("read-only", action74)

        # IsVisible (true)
        timeEventsElement.is_visible = True
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", timeEventsElement.is_visible)
        Assert.assertEqual(True, timeEventsElement.is_visible)
        # TimeEventTypeSupportedTypes
        arTypes = timeEventsElement.time_event_type_supported_types
        self.m_logger.WriteLine3("An array of supported TimeEvent types contains: {0} elements.", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE" = clr.Convert(
                int(arTypes[iIndex][0]), VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE
            )
            if not timeEventsElement.is_time_event_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            self.m_logger.WriteLine8("\tType {0} is: {1} ({2}).", iIndex, arTypes[iIndex][1], eType)
            # SetTimeEventType
            timeEventsElement.set_time_event_type(eType)
            # TimeEventType
            self.m_logger.WriteLine6("\t\tThe new TimeEvent type is: {0}", timeEventsElement.time_event_type)
            Assert.assertEqual(eType, timeEventsElement.time_event_type)
            if eType == VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE.TIME_EVENT_TYPE_LINE:
                # TimeEventTypeData
                oLine: "IVehicleGraphics2DTimeEventTypeLine" = clr.Convert(
                    timeEventsElement.time_event_type_data, IVehicleGraphics2DTimeEventTypeLine
                )
                Assert.assertIsNotNone(oLine)

                # Event Interval
                oLine.event_interval.set_start_and_stop_times("2 Jul 2005 12:00:00.000", "3 Jul 2005 12:00:00.000")
                Assert.assertEqual("2 Jul 2005 12:00:00.000", oLine.event_interval.find_start_time())
                Assert.assertEqual("3 Jul 2005 12:00:00.000", oLine.event_interval.find_stop_time())

                oLine.event_interval.set_explicit_interval("23 Jul 2005 12:00:00.000", "23 Jul 2005 12:00:00.000")
                Assert.assertEqual("23 Jul 2005 12:00:00.000", oLine.event_interval.find_start_time())
                Assert.assertEqual("23 Jul 2005 12:00:00.000", oLine.event_interval.find_stop_time())

                oLine.event_interval.set_explicit_interval("24 Jul 2005 12:00:00.000", "25 Jul 2005 12:00:00.000")
                Assert.assertEqual("24 Jul 2005 12:00:00.000", oLine.event_interval.find_start_time())
                Assert.assertEqual("25 Jul 2005 12:00:00.000", oLine.event_interval.find_stop_time())

                oLine.event_interval.set_implicit_interval(
                    (clr.Convert(AG_SAT, IStkObject)).vgt.event_intervals["AvailabilityTimeSpan"]
                )
                Assert.assertEqual("1 Jul 1999 00:00:00.000", oLine.event_interval.find_start_time())
                Assert.assertEqual("2 Jul 1999 00:00:00.000", oLine.event_interval.find_stop_time())

                # Color
                self.m_logger.WriteLine6("\t\tThe current Color is: {0}", oLine.color)
                oLine.color = Color.FromArgb(12377850)
                self.m_logger.WriteLine6("\t\tThe new Color is: {0}", oLine.color)
                AssertEx.AreEqual(Color.FromArgb(12377850), oLine.color)
                # UniqueID
                self.m_logger.WriteLine5("\t\tThe current UniqueID is: {0}", oLine.unique_id)
                oLine.unique_id = "Test line"
                self.m_logger.WriteLine5("\t\tThe new UniqueID is: {0}", oLine.unique_id)
                Assert.assertEqual("Test line", oLine.unique_id)
                # LineStyle
                self.m_logger.WriteLine6("\t\tThe current LineStyle is: {0}", oLine.line_style)
                oLine.line_style = LINE_STYLE.DASH_DOT_DOTTED
                self.m_logger.WriteLine6("\t\tThe new LineStyle is: {0}", oLine.line_style)
                Assert.assertEqual(LINE_STYLE.DASH_DOT_DOTTED, oLine.line_style)
                # LineWidth
                self.m_logger.WriteLine6("\t\tThe current LineWidth is: {0}", oLine.line_width)
                oLine.line_width = LINE_WIDTH.WIDTH5
                self.m_logger.WriteLine6("\t\tThe new LineWidth is: {0}", oLine.line_width)
                Assert.assertEqual(LINE_WIDTH.WIDTH5, oLine.line_width)
                # OffsetType
                self.m_logger.WriteLine6("\t\tThe current Offset type is: {0}", oLine.offset_type)
                # OffsetSupportedTypes
                arOffsetTypes = oLine.offset_supported_types
                self.m_logger.WriteLine3(
                    "\t\tArray of supported Offset types contains: {0} elements", len(arOffsetTypes)
                )

                i: int = 0
                while i < len(arOffsetTypes):
                    eOffset: "VEHICLE_GRAPHICS_2D_OFFSET" = clr.Convert(
                        int(arOffsetTypes[i][0]), VEHICLE_GRAPHICS_2D_OFFSET
                    )
                    if not oLine.is_offset_type_supported(eOffset):
                        Assert.fail("The {0} type should be supported!")

                    self.m_logger.WriteLine8("\t\t\tType {0} is: {1} ({2})", i, arOffsetTypes[i][1], eOffset)
                    # SetOffsetType
                    oLine.set_offset_type(eOffset)
                    self.m_logger.WriteLine6("\t\t\t\tThe new Offset type is: {0}", oLine.offset_type)
                    Assert.assertEqual(eOffset, oLine.offset_type)
                    # OffsetPixels
                    self.m_logger.WriteLine3("\t\t\t\tThe current OffsetPixels is: {0}", oLine.offset_pixels)
                    oLine.offset_pixels = 17
                    self.m_logger.WriteLine3("\t\t\t\tThe new OffsetPixels is: {0}", oLine.offset_pixels)
                    Assert.assertEqual(17, oLine.offset_pixels)

                    def action75():
                        oLine.offset_pixels = 123

                    TryCatchAssertBlock.ExpectedException("is invalid", action75)

                    i += 1

            elif eType == VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE.TIME_EVENT_TYPE_MARKER:
                # TimeEventTypeData
                oMarker: "IVehicleGraphics2DTimeEventTypeMarker" = clr.Convert(
                    timeEventsElement.time_event_type_data, IVehicleGraphics2DTimeEventTypeMarker
                )
                Assert.assertIsNotNone(oMarker)
                # StartTime
                self.m_logger.WriteLine6("\t\tThe current Start time is: {0}", oMarker.event_interval.find_start_time())
                oMarker.event_interval.set_explicit_interval("22 Jul 2005 12:00:00.000", "22 Jul 2005 12:00:00.000")
                self.m_logger.WriteLine6("\t\tThe new Start time is: {0}", oMarker.event_interval.find_start_time())
                Assert.assertEqual("22 Jul 2005 12:00:00.000", oMarker.event_interval.find_start_time())
                # StopTime (read-only)
                self.m_logger.WriteLine6("\t\tThe current Stop time is: {0}", oMarker.event_interval.find_stop_time())

                # Event Interval
                oMarker.event_interval.set_explicit_interval("23 Jul 2005 12:00:00.000", "23 Jul 2005 12:00:00.000")
                Assert.assertEqual("23 Jul 2005 12:00:00.000", oMarker.event_interval.find_start_time())
                Assert.assertEqual("23 Jul 2005 12:00:00.000", oMarker.event_interval.find_stop_time())

                oMarker.event_interval.set_explicit_interval("24 Jul 2005 12:00:00.000", "25 Jul 2005 12:00:00.000")
                Assert.assertEqual("24 Jul 2005 12:00:00.000", oMarker.event_interval.find_start_time())
                # BUG66610 Assert.AreEqual("24 Jul 2005 12:00:00.000", oMarker.StopTime);

                oMarker.event_interval.set_implicit_interval(
                    (clr.Convert(AG_SAT, IStkObject)).vgt.event_intervals["AvailabilityTimeSpan"]
                )
                Assert.assertEqual("1 Jul 1999 00:00:00.000", oMarker.event_interval.find_start_time())
                # BUG66610 Assert.AreEqual("1 Jul 1999 00:00:00.000", oMarker.StopTime);

                # Color
                self.m_logger.WriteLine6("\t\tThe current Color is: {0}", oMarker.color)
                oMarker.color = Color.FromArgb(11259375)
                self.m_logger.WriteLine6("\t\tThe new Color is: {0}", oMarker.color)
                AssertEx.AreEqual(Color.FromArgb(11259375), oMarker.color)
                # MarkerStyle
                self.m_logger.WriteLine5("\t\tThe current MarkerStyle is: {0}", oMarker.marker_style)
                oMarker.marker_style = "Star"
                self.m_logger.WriteLine5("\t\tThe new MarkerStyle is: {0}", oMarker.marker_style)
                Assert.assertEqual("Star", oMarker.marker_style)
                # UniqueID
                self.m_logger.WriteLine5("\t\tThe current UniqueID is: {0}", oMarker.unique_id)
                oMarker.unique_id = "Howdy"
                self.m_logger.WriteLine5("\t\tThe new UniqueID is: {0}", oMarker.unique_id)
                Assert.assertEqual("Howdy", oMarker.unique_id)
            elif eType == VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE.TIME_EVENT_TYPE_TEXT:
                # TimeEventTypeData
                oText: "IVehicleGraphics2DTimeEventTypeText" = clr.Convert(
                    timeEventsElement.time_event_type_data, IVehicleGraphics2DTimeEventTypeText
                )
                Assert.assertIsNotNone(oText)
                # StartTime
                self.m_logger.WriteLine6("\t\tThe current Start time is: {0}", oText.event_interval.find_start_time())
                oText.event_interval.set_start_and_stop_times("12 Jul 2005 12:00:00.000", "12 Jul 2005 12:00:00.000")
                self.m_logger.WriteLine6("\t\tThe new Start time is: {0}", oText.event_interval.find_start_time())
                Assert.assertEqual("12 Jul 2005 12:00:00.000", oText.event_interval.find_start_time())
                # StopTime (read-only)
                self.m_logger.WriteLine6("\t\tThe current Stop time is: {0}", oText.event_interval.find_stop_time())

                # Event Interval
                oText.event_interval.set_explicit_interval("23 Jul 2005 12:00:00.000", "23 Jul 2005 12:00:00.000")
                Assert.assertEqual("23 Jul 2005 12:00:00.000", oText.event_interval.find_start_time())
                Assert.assertEqual("23 Jul 2005 12:00:00.000", oText.event_interval.find_stop_time())

                oText.event_interval.set_explicit_interval("24 Jul 2005 12:00:00.000", "25 Jul 2005 12:00:00.000")
                Assert.assertEqual("24 Jul 2005 12:00:00.000", oText.event_interval.find_start_time())
                # BUG66610 Assert.AreEqual("24 Jul 2005 12:00:00.000", oText.StopTime);

                oText.event_interval.set_implicit_interval(
                    (clr.Convert(AG_SAT, IStkObject)).vgt.event_intervals["AvailabilityTimeSpan"]
                )
                Assert.assertEqual("1 Jul 1999 00:00:00.000", oText.event_interval.find_start_time())
                # BUG66610 Assert.AreEqual("1 Jul 1999 00:00:00.000", oText.StopTime);

                # Color
                self.m_logger.WriteLine6("\t\tThe current Color is: {0}", oText.color)
                oText.color = Color.FromArgb(12377850)
                self.m_logger.WriteLine6("\t\tThe new Color is: {0}", oText.color)
                AssertEx.AreEqual(Color.FromArgb(12377850), oText.color)
                # UniqueID
                self.m_logger.WriteLine5("\t\tThe current UniqueID is: {0}", oText.unique_id)
                oText.unique_id = "Test text"
                self.m_logger.WriteLine5("\t\tThe new UniqueID is: {0}", oText.unique_id)
                Assert.assertEqual("Test text", oText.unique_id)
                # Text
                self.m_logger.WriteLine5("\t\tThe current Text is: {0}", oText.text)
                oText.text = "Bla-bla-bla!"
                self.m_logger.WriteLine5("\t\tThe new Text is: {0}", oText.text)
                Assert.assertEqual("Bla-bla-bla!", oText.text)
                # OffsetType
                self.m_logger.WriteLine6("\t\tThe current Offset type is: {0}", oText.offset_type)
                # OffsetSupportedTypes
                arOffsetTypes = oText.offset_supported_types
                self.m_logger.WriteLine3(
                    "\t\tArray of supported Offset types contains: {0} elements", len(arOffsetTypes)
                )

                i: int = 0
                while i < len(arOffsetTypes):
                    eOffset: "VEHICLE_GRAPHICS_2D_OFFSET" = clr.Convert(
                        int(arOffsetTypes[i][0]), VEHICLE_GRAPHICS_2D_OFFSET
                    )
                    if not oText.is_offset_type_supported(eOffset):
                        Assert.fail("The {0} type should be supported!")

                    self.m_logger.WriteLine8("\t\t\tType {0} is: {1} ({2})", i, arOffsetTypes[i][1], eOffset)
                    # SetOffsetType
                    oText.set_offset_type(eOffset)
                    self.m_logger.WriteLine6("\t\t\t\tThe new Offset type is: {0}", oText.offset_type)
                    Assert.assertEqual(eOffset, oText.offset_type)
                    # OffsetPixels
                    self.m_logger.WriteLine3("\t\t\t\tThe current OffsetPixels is: {0}", oText.offset_pixels)
                    oText.offset_pixels = 17
                    self.m_logger.WriteLine3("\t\t\t\tThe new OffsetPixels is: {0}", oText.offset_pixels)
                    Assert.assertEqual(17, oText.offset_pixels)

                    def action76():
                        oText.offset_pixels = 123

                    TryCatchAssertBlock.ExpectedException("is invalid", action76)

                    i += 1

            else:
                Assert.fail("Invalid Type!")

            iIndex += 1

        # RemoveAt
        oCollection.remove_at(0)
        self.m_logger.WriteLine3(
            "After RemoveAt(0) the TimeEvents collection contains: {0} elements.", oCollection.count
        )
        Assert.assertEqual(0, oCollection.count)
        oCollection.add()
        self.m_logger.WriteLine3("After Add() the TimeEvents collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual(1, oCollection.count)
        oEvent: "IVehicleGraphics2DTimeEventsElement"
        for oEvent in oCollection:
            self.m_logger.WriteLine7(
                "\tElement: TimeEventType = {0}, IsVisible = {1}", oEvent.time_event_type, oEvent.is_visible
            )

        # RemoveAll
        oCollection.remove_all()
        self.m_logger.WriteLine3(
            "After RemoveAll() the TimeEvents collection contains: {0} elements.", oCollection.count
        )
        Assert.assertEqual(0, oCollection.count)
        self.m_logger.WriteLine("----- THE GRAPHICS TIME EVENTS TEST ----- END -----")


# endregion


# region GfxLabelNoteHelper
class GfxLabelNoteHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oCollection: "ILabelNoteCollection"):
        self.m_logger.WriteLine("----- THE GRAPHICS LABELNOTES TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            self.m_logger.WriteLine9(
                "\tElement {0}: Note = {1}, NoteVisible = {2}, LabelVisible = {3}",
                iIndex,
                oCollection[iIndex].note,
                oCollection[iIndex].note_visible,
                oCollection[iIndex].label_visible,
            )

            iIndex += 1

        # Count
        iCount: int = oCollection.count
        # Add
        oNote: "ILabelNote" = oCollection.add("Label Note 1")
        Assert.assertIsNotNone(oNote)
        Assert.assertEqual("Label Note 1", oNote.note)
        Assert.assertEqual((iCount + 1), oCollection.count)
        # Add
        oNote = oCollection.add("Label Note 2")
        Assert.assertIsNotNone(oNote)
        Assert.assertEqual("Label Note 2", oNote.note)
        Assert.assertEqual((iCount + 2), oCollection.count)
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Note, NoteVisible, LabelVisible
            self.m_logger.WriteLine9(
                "\tElement {3}: Note = {0}, NoteVisible = {1}, LabelVisible = {2}",
                oCollection[iIndex].note,
                oCollection[iIndex].note_visible,
                oCollection[iIndex].label_visible,
                iIndex,
            )

            iIndex += 1

        # Remove
        self.m_logger.WriteLine3("Before Remove() the LabelNotes collection contains: {0} elements", oCollection.count)
        oCollection.remove((oCollection.count - 1))
        self.m_logger.WriteLine3("After  Remove() the LabelNotes collection contains: {0} elements", oCollection.count)
        Assert.assertEqual((iCount + 1), oCollection.count)

        def action77():
            oCollection.remove((oCollection.count + 1))

        TryCatchAssertBlock.DoAssert("Remove() should not allow to remove invalid elements.", action77)
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.count)
        labelNote: "ILabelNote"
        for labelNote in oCollection:
            self.m_logger.WriteLine8(
                "\tBefore: Note = {0}, NoteVisible = {1}, LabelVisible = {2}",
                labelNote.note,
                labelNote.note_visible,
                labelNote.label_visible,
            )
            # Note
            labelNote.note = "Modified Label Note"
            Assert.assertEqual("Modified Label Note", labelNote.note)
            # LabelVisible
            labelNote.label_visible = True
            Assert.assertEqual(True, labelNote.label_visible)
            # NoteVisible
            labelNote.note_visible = NOTE_SHOW_TYPE.ON
            Assert.assertEqual(NOTE_SHOW_TYPE.ON, labelNote.note_visible)
            labelNote.note_visible = NOTE_SHOW_TYPE.INTERVALS
            Assert.assertEqual(NOTE_SHOW_TYPE.INTERVALS, labelNote.note_visible)
            # Intervals
            oHelper = IntervalCollectionHelper(self.m_oUnits)
            oHelper.Run(labelNote.intervals, IntervalCollectionHelper.IntervalCollectionType.LabelNotes)
            # NoteVisible
            labelNote.note_visible = NOTE_SHOW_TYPE.OFF
            Assert.assertEqual(NOTE_SHOW_TYPE.OFF, labelNote.note_visible)

        self.m_logger.WriteLine("----- THE GRAPHICS LABELNOTES TEST ----- END -----")

    # endregion
