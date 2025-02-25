# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from logger import *
from math2 import *
from ansys.stk.core.utilities.colors import *
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
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oBasic.show_graphics)
        oBasic.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBasic.show_graphics)
        Assert.assertEqual(False, oBasic.show_graphics)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBasic.color = Colors.from_argb(16711935)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBasic.marker_style = "Square"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBasic.show_label = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBasic.inherit = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBasic.line.style = LineStyle.LMS_DASH

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBasic.line.width = LineWidth.WIDTH5

        # IsVisible (true)
        oBasic.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBasic.show_graphics)
        Assert.assertEqual(True, oBasic.show_graphics)
        # Color
        self.m_logger.WriteLine6("\t\tCurrent Color is: {0}", oBasic.color)
        oBasic.color = Colors.from_argb(16711935)
        self.m_logger.WriteLine6("\t\tNew Color is: {0}", oBasic.color)
        AssertEx.AreEqual(Colors.from_argb(16711935), oBasic.color)
        # MarkerStyle
        self.m_logger.WriteLine5("\t\tCurrent MarkerStyle is: {0}", oBasic.marker_style)
        oBasic.marker_style = "Square"
        self.m_logger.WriteLine5("\t\tNew MarkerStyle is: {0}", oBasic.marker_style)
        Assert.assertEqual("Square", oBasic.marker_style)
        # Line.Style
        self.m_logger.WriteLine6("\t\tCurrent Line.Style is: {0}", oBasic.line.style)
        oBasic.line.style = LineStyle.M_DASH_DOT
        self.m_logger.WriteLine6("\t\tNew Line.Style is: {0}", oBasic.line.style)
        Assert.assertEqual(LineStyle.M_DASH_DOT, oBasic.line.style)
        # Line.Width
        self.m_logger.WriteLine6("\t\tCurrent Line.Width is: {0}", oBasic.line.width)
        oBasic.line.width = LineWidth.WIDTH5
        self.m_logger.WriteLine6("\t\tNew Line.Width is: {0}", oBasic.line.width)
        Assert.assertEqual(LineWidth.WIDTH5, oBasic.line.width)
        # Inherit (true)
        self.m_logger.WriteLine4("\t\tCurrent Inherit flag is: {0}", oBasic.inherit)
        oBasic.inherit = True
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oBasic.inherit)
        Assert.assertEqual(True, oBasic.inherit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBasic.show_label = False

        # Inherit (false)
        oBasic.inherit = False
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oBasic.inherit)
        Assert.assertEqual(False, oBasic.inherit)
        # LabelVisible
        self.m_logger.WriteLine4("\t\tCurrent LabelVisible flag is: {0}", oBasic.show_label)
        oBasic.show_label = True
        self.m_logger.WriteLine4("\t\tNew LabelVisible flag is: {0}", oBasic.show_label)
        Assert.assertEqual(True, oBasic.show_label)
        oBasic.show_label = False
        self.m_logger.WriteLine4("\t\tNew LabelVisible flag is: {0}", oBasic.show_label)
        Assert.assertEqual(False, oBasic.show_label)


# endregion


# region GfxAttributesRouteHelper
class GfxAttributesRouteHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oRoute: "VehicleGraphics2DAttributesRoute"):
        Assert.assertIsNotNone(oRoute)

        # Basic
        oHelper = GfxAttributesBasicHelper()
        oHelper.Run(oRoute)

        self.m_logger.WriteLine("GfxAttributesRouteHelper test:")

        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oRoute.show_graphics)
        oRoute.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oRoute.show_graphics)
        Assert.assertEqual(False, oRoute.show_graphics)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oRoute.show_route = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oRoute.show_route_marker = False

        # IsVisible (true)
        oRoute.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oRoute.show_graphics)
        Assert.assertEqual(True, oRoute.show_graphics)
        # Inherit (true)
        self.m_logger.WriteLine4("\t\tCurrent Inherit flag is: {0}", oRoute.inherit)
        oRoute.inherit = True
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oRoute.inherit)
        Assert.assertEqual(True, oRoute.inherit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oRoute.show_route = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oRoute.show_route_marker = False

        # Inherit (false)
        oRoute.inherit = False
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oRoute.inherit)
        Assert.assertEqual(False, oRoute.inherit)
        # IsRouteVisible
        self.m_logger.WriteLine4("\t\tCurrent IsRouteVisible flag is: {0}", oRoute.show_route)
        oRoute.show_route = True
        self.m_logger.WriteLine4("\t\tNew IsRouteVisible flag is: {0}", oRoute.show_route)
        Assert.assertEqual(True, oRoute.show_route)
        # IsRouteMarkerVisible
        self.m_logger.WriteLine4("\t\tCurrent IsRouteMarkerVisible flag is: {0}", oRoute.show_route_marker)
        oRoute.show_route_marker = True
        self.m_logger.WriteLine4("\t\tNew IsRouteMarkerVisible flag is: {0}", oRoute.show_route_marker)
        Assert.assertEqual(True, oRoute.show_route_marker)


# endregion


# region GfxAttributesOrbitHelper
class GfxAttributesOrbitHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oOrbit: "VehicleGraphics2DAttributesOrbit"):
        Assert.assertIsNotNone(oOrbit)

        # Basic
        oHelper = GfxAttributesBasicHelper()
        oHelper.Run(oOrbit)

        self.m_logger.WriteLine("GfxAttributesOrbitHelper test:")

        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oOrbit.show_graphics)
        oOrbit.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oOrbit.show_graphics)
        Assert.assertEqual(False, oOrbit.show_graphics)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oOrbit.show_ground_track = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oOrbit.show_ground_marker = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oOrbit.show_orbit = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oOrbit.show_orbit_marker = False

        # IsVisible (true)
        oOrbit.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oOrbit.show_graphics)
        Assert.assertEqual(True, oOrbit.show_graphics)
        # Inherit (true)
        self.m_logger.WriteLine4("\t\tCurrent Inherit flag is: {0}", oOrbit.inherit)
        oOrbit.inherit = True
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oOrbit.inherit)
        Assert.assertEqual(True, oOrbit.inherit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oOrbit.show_ground_track = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oOrbit.show_ground_marker = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oOrbit.show_orbit = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oOrbit.show_orbit_marker = False

        # Inherit (false)
        oOrbit.inherit = False
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oOrbit.inherit)
        Assert.assertEqual(False, oOrbit.inherit)
        # IsGroundTrackVisible
        self.m_logger.WriteLine4("\t\tCurrent IsGroundTrackVisible flag is: {0}", oOrbit.show_ground_track)
        oOrbit.show_ground_track = True
        self.m_logger.WriteLine4("\t\tNew IsGroundTrackVisible flag is: {0}", oOrbit.show_ground_track)
        Assert.assertEqual(True, oOrbit.show_ground_track)
        # IsGroundMarkerVisible
        self.m_logger.WriteLine4("\t\tCurrent IsGroundMarkerVisible flag is: {0}", oOrbit.show_ground_marker)
        oOrbit.show_ground_marker = True
        self.m_logger.WriteLine4("\t\tNew IsGroundMarkerVisible flag is: {0}", oOrbit.show_ground_marker)
        Assert.assertEqual(True, oOrbit.show_ground_marker)
        # IsOrbitVisible
        self.m_logger.WriteLine4("\t\tCurrent IsOrbitVisible flag is: {0}", oOrbit.show_orbit)
        oOrbit.show_orbit = True
        self.m_logger.WriteLine4("\t\tNew IsOrbitVisible flag is: {0}", oOrbit.show_orbit)
        Assert.assertEqual(True, oOrbit.show_orbit)
        # IsOrbitMarkerVisible
        self.m_logger.WriteLine4("\t\tCurrent IsOrbitMarkerVisible flag is: {0}", oOrbit.show_orbit_marker)
        oOrbit.show_orbit_marker = True
        self.m_logger.WriteLine4("\t\tNew IsOrbitMarkerVisible flag is: {0}", oOrbit.show_orbit_marker)
        Assert.assertEqual(True, oOrbit.show_orbit_marker)


# endregion


# region GfxAttributesTrajectoryHelper
class GfxAttributesTrajectoryHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oTrajectory: "VehicleGraphics2DAttributesTrajectory"):
        Assert.assertIsNotNone(oTrajectory)

        # Basic
        oHelper = GfxAttributesBasicHelper()
        oHelper.Run(oTrajectory)

        self.m_logger.WriteLine("GfxAttributesTrajectoryHelper test:")

        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oTrajectory.show_graphics)
        oTrajectory.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oTrajectory.show_graphics)
        Assert.assertEqual(False, oTrajectory.show_graphics)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oTrajectory.show_ground_track = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oTrajectory.show_ground_marker = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oTrajectory.show_trajectory = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oTrajectory.show_trajectory_marker = False

        # IsVisible (true)
        oTrajectory.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oTrajectory.show_graphics)
        Assert.assertEqual(True, oTrajectory.show_graphics)
        # Inherit (true)
        self.m_logger.WriteLine4("\t\tCurrent Inherit flag is: {0}", oTrajectory.inherit)
        oTrajectory.inherit = True
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oTrajectory.inherit)
        Assert.assertEqual(True, oTrajectory.inherit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oTrajectory.show_ground_track = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oTrajectory.show_ground_marker = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oTrajectory.show_trajectory = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oTrajectory.show_trajectory_marker = False

        # Inherit (false)
        oTrajectory.inherit = False
        self.m_logger.WriteLine4("\t\tNew Inherit flag is: {0}", oTrajectory.inherit)
        Assert.assertEqual(False, oTrajectory.inherit)
        # IsGroundTrackVisible
        self.m_logger.WriteLine4("\t\tCurrent IsGroundTrackVisible flag is: {0}", oTrajectory.show_ground_track)
        oTrajectory.show_ground_track = True
        self.m_logger.WriteLine4("\t\tNew IsGroundTrackVisible flag is: {0}", oTrajectory.show_ground_track)
        Assert.assertEqual(True, oTrajectory.show_ground_track)
        # IsGroundMarkerVisible
        self.m_logger.WriteLine4("\t\tCurrent IsGroundMarkerVisible flag is: {0}", oTrajectory.show_ground_marker)
        oTrajectory.show_ground_marker = True
        self.m_logger.WriteLine4("\t\tNew IsGroundMarkerVisible flag is: {0}", oTrajectory.show_ground_marker)
        Assert.assertEqual(True, oTrajectory.show_ground_marker)
        # IsTrajectoryVisible
        self.m_logger.WriteLine4("\t\tCurrent IsTrajectoryVisible flag is: {0}", oTrajectory.show_trajectory)
        oTrajectory.show_trajectory = True
        self.m_logger.WriteLine4("\t\tNew IsTrajectoryVisible flag is: {0}", oTrajectory.show_trajectory)
        Assert.assertEqual(True, oTrajectory.show_trajectory)
        # IsTrajectoryMarkerVisible
        self.m_logger.WriteLine4(
            "\t\tCurrent IsTrajectoryMarkerVisible flag is: {0}", oTrajectory.show_trajectory_marker
        )
        oTrajectory.show_trajectory_marker = True
        self.m_logger.WriteLine4("\t\tNew IsTrajectoryMarkerVisible flag is: {0}", oTrajectory.show_trajectory_marker)
        Assert.assertEqual(True, oTrajectory.show_trajectory_marker)


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
    def Run(self, oAccess: "VehicleGraphics2DAttributesAccess", eType, oRoot: "StkObjectRoot"):
        Assert.assertIsNotNone(oAccess)

        # AccessObjects
        oLinkCollection: "ObjectLinkCollection" = oAccess.access_objects
        Assert.assertIsNotNone(oLinkCollection)
        oOLCHelper = ObjectLinkCollectionHelper()
        oOLCHelper.Run(oLinkCollection, oRoot)
        if oLinkCollection.count == 0:
            # DuringAccess (readonly)
            oBasic: "IVehicleGraphics2DAttributesBasic" = oAccess.during_access
            Assert.assertIsNotNone(oBasic)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oBasic.show_graphics = False

            # NoAccess (readonly)
            oBasic = oAccess.no_access
            Assert.assertIsNotNone(oBasic)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oBasic.show_graphics = False

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
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oAccess.during_access))

            # NoAccess
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oAccess.no_access))
        elif eType == GfxAttributesType.eRoute:
            # DuringAccess
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(VehicleGraphics2DAttributesRoute(oAccess.during_access))

            # NoAccess
            oHelper.Run(VehicleGraphics2DAttributesRoute(oAccess.no_access))
        elif eType == GfxAttributesType.eTrajectory:
            # DuringAccess
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oAccess.during_access))

            # NoAccess
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oAccess.no_access))
        else:
            Assert.fail("Invalid type!")


# endregion


# region GfxAttributesCustomHelper
class GfxAttributesCustomHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCustom: "VehicleGraphics2DAttributesCustom", eType):
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
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oCustom.default))
        elif eType == GfxAttributesType.eRoute:
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(VehicleGraphics2DAttributesRoute(oCustom.default))
        elif eType == GfxAttributesType.eTrajectory:
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oCustom.default))
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
    def Run(self, oTimeComponents: "VehicleGraphics2DAttributesTimeComponents", eType, oRoot: "StkObjectRoot"):
        Assert.assertIsNotNone(oTimeComponents)

        tcColl: "VehicleGraphics2DTimeComponentsCollection" = oTimeComponents.time_components
        Assert.assertIsNotNone(tcColl)

        tcColl.remove_all()
        Assert.assertEqual(0, tcColl.count)

        # Should not be able to add Event, EventArray, or invalid components
        with pytest.raises(Exception):
            tcColl.add((("Scenario/" + oRoot.current_scenario.instance_name) + " AnalysisStartTime Event"))
        with pytest.raises(Exception):
            tcColl.add((("Scenario/" + oRoot.current_scenario.instance_name) + " OneMinuteSampleTimes EventArray"))
        with pytest.raises(Exception):
            tcColl.add("Scenario/Scenario1 Bogus EventInterval")

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
        with pytest.raises(Exception):
            Console.WriteLine(tcColl[3].qualified_path)

        # enumerate
        ele: "IVehicleGraphics2DTimeComponentsElement"

        # enumerate
        for ele in tcColl:
            Console.WriteLine(ele.qualified_path)

        evCollEle1: "VehicleGraphics2DTimeComponentsEventCollectionElement" = clr.CastAs(
            tcElement1, VehicleGraphics2DTimeComponentsEventCollectionElement
        )
        Assert.assertIsNone(evCollEle1)  # should not support this interface
        evEle1: "VehicleGraphics2DTimeComponentsEventElement" = clr.CastAs(
            tcElement1, VehicleGraphics2DTimeComponentsEventElement
        )
        Assert.assertIsNotNone(evEle1)

        crdn: "IAnalysisWorkbenchComponent" = evEle1.get_time_component()
        Assert.assertEqual(
            (("Scenario/" + oRoot.current_scenario.instance_name) + " AnalysisInterval EventInterval"),
            crdn.qualified_path,
        )

        oHelper1 = GfxAttributesBasicHelper()
        oHelper1.Run(evEle1.attributes)

        evCollEle2: "VehicleGraphics2DTimeComponentsEventCollectionElement" = clr.CastAs(
            tcElement2, VehicleGraphics2DTimeComponentsEventCollectionElement
        )
        Assert.assertIsNone(evCollEle2)  # should not support this interface
        evEle2: "VehicleGraphics2DTimeComponentsEventElement" = clr.CastAs(
            tcElement2, VehicleGraphics2DTimeComponentsEventElement
        )
        Assert.assertIsNotNone(evEle2)
        oHelper2 = GfxAttributesBasicHelper()
        oHelper2.Run(evEle2.attributes)

        evEle3: "VehicleGraphics2DTimeComponentsEventElement" = clr.CastAs(
            tcElement3, VehicleGraphics2DTimeComponentsEventElement
        )
        Assert.assertIsNone(evEle3)  # should not support this interface
        evCollEle3: "VehicleGraphics2DTimeComponentsEventCollectionElement" = clr.CastAs(
            tcElement3, VehicleGraphics2DTimeComponentsEventCollectionElement
        )
        Assert.assertIsNotNone(evCollEle3)

        crdn = evCollEle3.get_time_component()
        Assert.assertEqual("Aircraft/Boing737 LightingIntervals EventIntervalCollection", crdn.qualified_path)

        evCollEle3.use_color_ramp = True
        Assert.assertTrue(evCollEle3.use_color_ramp)
        evCollEle3.color_ramp_start_color = Colors.AliceBlue
        AssertEx.AreEqual(Colors.AliceBlue, evCollEle3.color_ramp_start_color)
        evCollEle3.color_ramp_end_color = Colors.AntiqueWhite
        AssertEx.AreEqual(Colors.AntiqueWhite, evCollEle3.color_ramp_end_color)

        evCollEle3.use_color_ramp = False
        Assert.assertFalse(evCollEle3.use_color_ramp)
        evCollEle3.color_ramp_start_color = Colors.Black
        AssertEx.AreEqual(Colors.Black, evCollEle3.color_ramp_start_color)
        evCollEle3.color_ramp_end_color = Colors.Blue
        AssertEx.AreEqual(Colors.Blue, evCollEle3.color_ramp_end_color)
        evCollEle3.use_color_ramp = True

        oBasicHelper = GfxAttributesBasicHelper()
        oBasicHelper.Run(evCollEle3.umbra)
        oBasicHelper.Run(evCollEle3.penumbra)
        oBasicHelper.Run(evCollEle3.sunlight)

        # RemoveAt
        with pytest.raises(Exception):
            tcColl.remove_at(3)

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
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oTimeComponents.default))
        elif eType == GfxAttributesType.eRoute:
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(VehicleGraphics2DAttributesRoute(oTimeComponents.default))
        elif eType == GfxAttributesType.eTrajectory:
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oTimeComponents.default))
        else:
            Assert.fail("Invalid type!")


# endregion


# region GfxIntervalsCollectionHelper
class GfxIntervalsCollectionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "VehicleGraphics2DIntervalsCollection", eType):
        Assert.assertIsNotNone(oCollection)

        self.m_logger.WriteLine("GfxIntervalsCollectionHelper test:")

        # Count
        iCount: int = oCollection.count
        self.m_logger.WriteLine3("\tThe current IntervalCollection contain: {0} elements", iCount)
        # _NewEnum
        gfxInterval: "VehicleGraphics2DInterval"
        # _NewEnum
        for gfxInterval in oCollection:
            self.m_logger.WriteLine7(
                "\t\tElement: StartTime = {0}, StopTime = {1}", gfxInterval.start_time, gfxInterval.stop_time
            )

        # Add
        oInterval: "VehicleGraphics2DInterval" = oCollection.add("1 Jul 1999 01:00:00.000", "1 Jul 1999 03:00:00.000")
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
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oInterval.graphics_2d_attributes))
        elif eType == GfxAttributesType.eRoute:
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(VehicleGraphics2DAttributesRoute(oInterval.graphics_2d_attributes))
        elif eType == GfxAttributesType.eTrajectory:
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oInterval.graphics_2d_attributes))
        else:
            Assert.fail("Invalid type!")

        # Add additional elements
        oInterval = oCollection.add("1 Jul 1999 00:00:00.000", "1 Jul 1999 00:04:00.000")
        oInterval.graphics_2d_attributes.color = Colors.Yellow
        Assert.assertIsNotNone(oInterval)
        Assert.assertEqual("1 Jul 1999 00:00:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 00:04:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 2), oCollection.count)
        oInterval = oCollection.add("1 Jul 1999 00:20:00.000", "1 Jul 1999 00:25:00.000")
        Assert.assertIsNotNone(oInterval)
        oInterval.graphics_2d_attributes.color = Colors.Red
        Assert.assertEqual("1 Jul 1999 00:20:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 00:25:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 3), oCollection.count)
        oInterval = oCollection.add("1 Jul 1999 00:10:00.000", "1 Jul 1999 00:15:00.000")
        Assert.assertIsNotNone(oInterval)
        oInterval.graphics_2d_attributes.color = Colors.RoyalBlue
        Assert.assertEqual("1 Jul 1999 00:10:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 00:15:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 4), oCollection.count)
        oInterval = oCollection.add("1 Jul 1999 00:30:00.000", "1 Jul 1999 00:35:00.000")
        Assert.assertIsNotNone(oInterval)
        oInterval.graphics_2d_attributes.color = Colors.Yellow
        Assert.assertEqual("1 Jul 1999 00:30:00.000", oInterval.start_time)
        Assert.assertEqual("1 Jul 1999 00:35:00.000", oInterval.stop_time)
        Assert.assertEqual((iCount + 5), oCollection.count)

        with pytest.raises(Exception, match=RegexSubstringMatch("already exists")):
            oCollection.add("1 Jul 1999 00:20:00.000", "1 Jul 1999 00:25:00.000")

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
    def Run(self, oRealTime: "VehicleGraphics2DAttributesRealtime", eType):
        Assert.assertIsNotNone(oRealTime)
        if eType == GfxAttributesType.eOrbit:
            # DropOut
            oHelper = GfxAttributesOrbitHelper()
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oRealTime.drop_out))
            # History
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oRealTime.history))
            # LookAhead
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oRealTime.look_ahead))
            # Spline
            oHelper.Run(VehicleGraphics2DAttributesOrbit(oRealTime.spline))
        elif eType == GfxAttributesType.eRoute:
            # DropOut
            oHelper = GfxAttributesRouteHelper()
            oHelper.Run(VehicleGraphics2DAttributesRoute(oRealTime.drop_out))
            # History
            oHelper.Run(VehicleGraphics2DAttributesRoute(oRealTime.history))
            # LookAhead
            oHelper.Run(VehicleGraphics2DAttributesRoute(oRealTime.look_ahead))
            # Spline
            oHelper.Run(VehicleGraphics2DAttributesRoute(oRealTime.spline))
        elif eType == GfxAttributesType.eTrajectory:
            # DropOut
            oHelper = GfxAttributesTrajectoryHelper()
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oRealTime.drop_out))
            # History
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oRealTime.history))
            # LookAhead
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oRealTime.look_ahead))
            # Spline
            oHelper.Run(VehicleGraphics2DAttributesTrajectory(oRealTime.spline))
        else:
            Assert.fail("Invalid type!")


# endregion


# region GfxElevationContoursHelper
class GfxElevationContoursHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "VehicleGraphics2DElevationContours"):
        self.m_logger.WriteLine("----- THE GRAPHICS ELEVATION CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        self.m_oUnits.reset_units()
        # IsVisible
        self.m_logger.WriteLine4("The current IsVisible flag is: {0}", oContours.show_graphics)
        oContours.show_graphics = False
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", oContours.show_graphics)
        Assert.assertEqual(False, oContours.show_graphics)
        oContours.show_graphics = True
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", oContours.show_graphics)
        Assert.assertEqual(True, oContours.show_graphics)
        # IsFillVisible
        self.m_logger.WriteLine4("The current IsFillVisible flag is: {0}", oContours.show_filled_contours)
        oContours.show_filled_contours = False
        self.m_logger.WriteLine4("The new IsFillVisible flag is: {0}", oContours.show_filled_contours)
        Assert.assertEqual(False, oContours.show_filled_contours)
        with pytest.raises(Exception):
            oContours.fill_style = FillStyle.HATCH
        oContours.show_filled_contours = True
        self.m_logger.WriteLine4("The new IsFillVisible flag is: {0}", oContours.show_filled_contours)
        Assert.assertEqual(True, oContours.show_filled_contours)
        # FillStyle
        self.m_logger.WriteLine6("The current FillStyle is: {0}", oContours.fill_style)
        oContours.fill_style = FillStyle.DIAGONAL_HATCH
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.DIAGONAL_HATCH, oContours.fill_style)
        oContours.fill_style = FillStyle.DIAGONAL_STRIPE1
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.DIAGONAL_STRIPE1, oContours.fill_style)
        oContours.fill_style = FillStyle.DIAGONAL_STRIPE2
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.DIAGONAL_STRIPE2, oContours.fill_style)
        oContours.fill_style = FillStyle.HATCH
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.HATCH, oContours.fill_style)
        oContours.fill_style = FillStyle.HORIZONTAL_STRIPE
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.HORIZONTAL_STRIPE, oContours.fill_style)
        oContours.fill_style = FillStyle.SCREEN
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.SCREEN, oContours.fill_style)
        oContours.fill_style = FillStyle.SOLID
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.SOLID, oContours.fill_style)
        oContours.fill_style = FillStyle.VERTICAL_STRIPE
        self.m_logger.WriteLine6("The new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.VERTICAL_STRIPE, oContours.fill_style)

        oContours.fill_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oContours.fill_translucency, delta=Math2.Epsilon12)

        # NumOfDecimalDigits
        self.m_logger.WriteLine3("The current NumOfDecimalDigits is: {0}", oContours.number_of_decimal_digits)
        oContours.number_of_decimal_digits = 7
        self.m_logger.WriteLine3("The new NumOfDecimalDigits is: {0}", oContours.number_of_decimal_digits)
        Assert.assertEqual(7, oContours.number_of_decimal_digits)
        with pytest.raises(Exception):
            oContours.number_of_decimal_digits = 123

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("The current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("The new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # Elevations
        oElevations: "VehicleGraphics2DElevationsCollection" = oContours.elevations
        Assert.assertIsNotNone(oElevations)
        # Count
        self.m_logger.WriteLine3("The Elevations Collection contains: {0} elements.", oElevations.count)
        # _NewEnum
        elevationsElement: "VehicleGraphics2DElevationsElement"
        # _NewEnum
        for elevationsElement in oElevations:
            self.m_logger.WriteLine10(
                "\tElement: Elevation = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, DistanceVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                elevationsElement.elevation,
                elevationsElement.color,
                elevationsElement.line_style,
                elevationsElement.line_width,
                elevationsElement.show_distance_label,
                elevationsElement.show_user_text_visible,
                elevationsElement.user_text,
                elevationsElement.label_angle,
            )

        # AddLevel
        self.m_logger.WriteLine3(
            "Before AddLevel() the Elevations Collection contains: {0} elements.", oElevations.count
        )
        oAdded: "VehicleGraphics2DElevationsElement" = oElevations.add_level(123.456)
        Assert.assertIsNotNone(oAdded)
        self.m_logger.WriteLine3(
            "After AddLevel() the Elevations Collection contains: {0} elements.", oElevations.count
        )
        elevationsElement: "VehicleGraphics2DElevationsElement"
        for elevationsElement in oElevations:
            self.m_logger.WriteLine10(
                "\tElement: Elevation = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, DistanceVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                elevationsElement.elevation,
                elevationsElement.color,
                elevationsElement.line_style,
                elevationsElement.line_width,
                elevationsElement.show_distance_label,
                elevationsElement.show_user_text_visible,
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
            elevationsElement: "VehicleGraphics2DElevationsElement" = oElevations[iIndex]
            Assert.assertIsNotNone(elevationsElement)
            self.m_logger.WriteLine10(
                "\tElement {0} (Before): Elevation = {1}, Color = {2}, LineStyle = {3}, LineWidth = {4}, DistanceVisible = {5}, UserTextVisible = {6}, UserText = {7}, LabelAngle = {8}",
                iIndex,
                elevationsElement.elevation,
                elevationsElement.color,
                elevationsElement.line_style,
                elevationsElement.line_width,
                elevationsElement.show_distance_label,
                elevationsElement.show_user_text_visible,
                elevationsElement.user_text,
                elevationsElement.label_angle,
            )
            elevationsElement.color = Colors.from_argb((elevationsElement.color._to_ole_color() + 250))
            elevationsElement.line_style = LineStyle.M_DASH
            elevationsElement.line_width = LineWidth.WIDTH2
            elevationsElement.elevation += 1.5
            elevationsElement.show_distance_label = not elevationsElement.show_distance_label
            elevationsElement.show_user_text_visible = True
            elevationsElement.user_text = "User test Text"
            elevationsElement.label_angle = 15
            self.m_logger.WriteLine10(
                "\tElement {0} (After): Elevation = {1}, Color = {2}, LineStyle = {3}, LineWidth = {4}, DistanceVisible = {5}, UserTextVisible = {6}, UserText = {7}, LabelAngle = {8}",
                iIndex,
                elevationsElement.elevation,
                elevationsElement.color,
                elevationsElement.line_style,
                elevationsElement.line_width,
                elevationsElement.show_distance_label,
                elevationsElement.show_user_text_visible,
                elevationsElement.user_text,
                elevationsElement.label_angle,
            )
            with pytest.raises(Exception):
                elevationsElement.label_angle = 1234

            iIndex += 1

        with pytest.raises(Exception):
            oElevations.add_level_range(12.34, 34.12, 0.2)
        with pytest.raises(Exception):
            oElevations.add_level_range(1.0, 200.0, 1.0)

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
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "Graphics2DRangeContours"):
        self.m_logger.WriteLine("----- THE GRAPHICS RANGE CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # IsVisible
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oContours.show_graphics)
        oContours.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oContours.show_graphics)
        Assert.assertFalse(oContours.show_graphics)
        oContours.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oContours.show_graphics)
        Assert.assertTrue(oContours.show_graphics)
        # IsFillVisible
        self.m_logger.WriteLine4("\tThe current IsFillVisible flag is: {0}", oContours.show_filled_contours)
        oContours.show_filled_contours = False
        self.m_logger.WriteLine4("\tThe new IsFillVisible flag is: {0}", oContours.show_filled_contours)
        Assert.assertFalse(oContours.show_filled_contours)
        with pytest.raises(Exception):
            oContours.fill_style = FillStyle.HATCH
        oContours.show_filled_contours = True
        self.m_logger.WriteLine4("\tThe new IsFillVisible flag is: {0}", oContours.show_filled_contours)
        Assert.assertTrue(oContours.show_filled_contours)
        # FillStyle
        self.m_logger.WriteLine6("\tThe current FillStyle is: {0}", oContours.fill_style)
        oContours.fill_style = FillStyle.DIAGONAL_HATCH
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.DIAGONAL_HATCH, oContours.fill_style)
        oContours.fill_style = FillStyle.DIAGONAL_STRIPE1
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.DIAGONAL_STRIPE1, oContours.fill_style)
        oContours.fill_style = FillStyle.DIAGONAL_STRIPE2
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.DIAGONAL_STRIPE2, oContours.fill_style)
        oContours.fill_style = FillStyle.HATCH
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.HATCH, oContours.fill_style)
        oContours.fill_style = FillStyle.HORIZONTAL_STRIPE
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.HORIZONTAL_STRIPE, oContours.fill_style)
        oContours.fill_style = FillStyle.SCREEN
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.SCREEN, oContours.fill_style)
        oContours.fill_style = FillStyle.SOLID
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.SOLID, oContours.fill_style)
        oContours.fill_style = FillStyle.VERTICAL_STRIPE
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(FillStyle.VERTICAL_STRIPE, oContours.fill_style)
        # NumOfDecimalDigits
        self.m_logger.WriteLine3("\tThe current NumOfDecimalDigits is: {0}", oContours.number_of_decimal_digits)
        oContours.number_of_decimal_digits = 7
        self.m_logger.WriteLine3("\tThe new NumOfDecimalDigits is: {0}", oContours.number_of_decimal_digits)
        Assert.assertEqual(7, oContours.number_of_decimal_digits)
        with pytest.raises(Exception):
            oContours.number_of_decimal_digits = 123

        with pytest.raises(Exception):
            oContours.label_units = "test"

        oContours.fill_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oContours.fill_translucency, delta=Math2.Epsilon12)

        availableUnits = oContours.available_label_units
        self.m_logger.WriteLine3("The available units contains {0} units.", Array.Length(availableUnits))
        unit: str
        for unit in availableUnits:
            self.m_logger.WriteLine(unit)
            oContours.label_units = unit
            Assert.assertEqual(unit, oContours.label_units)

        # set DistanceUnit
        self.m_logger.WriteLine5(
            "\tThe current DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        # LevelAttributes
        oLevels: "LevelAttributeCollection" = oContours.level_attributes
        Assert.assertIsNotNone(oLevels)
        # Count
        self.m_logger.WriteLine3("\tThe Level Attribute Collection contains: {0} elements.", oLevels.count)
        # _NewEnum
        levelAttribute: "LevelAttribute"
        # _NewEnum
        for levelAttribute in oLevels:
            self.m_logger.WriteLine10(
                "\t\tElement: Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.show_label,
                levelAttribute.show_label,
                levelAttribute.show_user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )

        # AddLevel
        self.m_logger.WriteLine3(
            "\tBefore AddLevel() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        oAdded: "LevelAttribute" = oLevels.add_level(123.456)
        Assert.assertIsNotNone(oAdded)
        self.m_logger.WriteLine3(
            "\tAfter AddLevel() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        levelAttribute: "LevelAttribute"
        for levelAttribute in oLevels:
            self.m_logger.WriteLine10(
                "\t\tElement: Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.show_label,
                levelAttribute.show_label,
                levelAttribute.show_user_text_visible,
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
            levelAttribute: "LevelAttribute" = oLevels[0]
            Assert.assertIsNotNone(levelAttribute)
            self.m_logger.WriteLine10(
                "\t\tElement (Before): Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.show_label,
                levelAttribute.show_label,
                levelAttribute.show_user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )
            levelAttribute.color = Colors.from_argb((levelAttribute.color._to_ole_color() + 250))
            levelAttribute.line_style = LineStyle.M_DASH
            levelAttribute.line_width = LineWidth.WIDTH2
            levelAttribute.level = float(levelAttribute.level) + 1.5
            levelAttribute.show_label = not levelAttribute.show_label
            levelAttribute.show_user_text_visible = True
            levelAttribute.user_text = "UserText test string"
            levelAttribute.label_angle = 15
            self.m_logger.WriteLine10(
                "\t\tElement (After): Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.show_label,
                levelAttribute.show_label,
                levelAttribute.show_user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )
            with pytest.raises(Exception):
                levelAttribute.label_angle = 1234

        with pytest.raises(Exception):
            oLevels.add_level_range(12.34, 34.12, 0.2)

        # RemoveAll
        oLevels.remove_all()
        self.m_logger.WriteLine3("\tAfter RemoveAll() the Elevations Collection contains: {0} elements.", oLevels.count)
        Assert.assertEqual(0, oLevels.count)
        self.m_logger.WriteLine("----- THE GRAPHICS RANGE CONTOURS TEST ----- END -----")


# endregion


# region GfxSAAContoursHelper
class GfxSAAContoursHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "VehicleGraphics2DSAA"):
        self.m_logger.WriteLine("----- THE GRAPHICS SAA CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # IsVisible
        self.m_logger.WriteLine4("The current IsVisible flag is: {0}", oContours.show_graphics)
        oContours.show_graphics = False
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", oContours.show_graphics)
        Assert.assertEqual(False, oContours.show_graphics)
        oContours.show_graphics = True
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", oContours.show_graphics)
        Assert.assertEqual(True, oContours.show_graphics)
        # IsFillVisible (false)
        self.m_logger.WriteLine4("The current IsFillVisible flag is: {0}", oContours.show_filled_contours)
        oContours.show_filled_contours = False
        self.m_logger.WriteLine4("The new IsFillVisible flag is: {0}", oContours.show_filled_contours)
        Assert.assertEqual(False, oContours.show_filled_contours)

        # IsFillVisible (true)
        oContours.show_filled_contours = True
        self.m_logger.WriteLine4("The new IsFillVisible flag is: {0}", oContours.show_filled_contours)
        Assert.assertEqual(True, oContours.show_filled_contours)

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

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oContours.altitude = 123.456

        # UseVehicleAlt (false)
        oContours.use_vehicle_altitude = False
        self.m_logger.WriteLine4("The new UseVehicleAltitude flag is: {0}", oContours.use_vehicle_altitude)
        Assert.assertEqual(False, oContours.use_vehicle_altitude)
        # Altitude
        self.m_logger.WriteLine6("The current Altitude is: {0}", oContours.altitude)
        oContours.altitude = 345.678
        self.m_logger.WriteLine6("The new Altitude is: {0}", oContours.altitude)
        Assert.assertEqual(345.678, oContours.altitude)

        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oContours.altitude = 1234.56

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
    def Run(self, oCollection: "VehicleGraphics2DGroundEllipsesCollection"):
        self.m_logger.WriteLine("----- THE GRAPHICS GROUND ELLIPSES TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\tGfxGroundEllipses collection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            oEllipse: "VehicleGraphics2DGroundEllipsesElement" = oCollection[iIndex]
            self.m_logger.WriteLine10(
                "\t\tEllipse {0}: EllipseSetName = {1}, Color = {7}, LineWidth = {8}, StaticGfx = {2}, DynamicGfx = {3}, Interpolate = {4}, IsNameVisible = {5}, IsCenterVisible = {6}",
                iIndex,
                oEllipse.ellipse_set_name,
                oEllipse.static_graphics_2d,
                oEllipse.dynamic_graphics_2d,
                oEllipse.interpolate,
                oEllipse.show_name,
                oEllipse.show_center_point_marker,
                oEllipse.color,
                oEllipse.line_width,
            )

            iIndex += 1

        # _NewEnum
        groundEllipsesElement: "VehicleGraphics2DGroundEllipsesElement"
        # _NewEnum
        for groundEllipsesElement in oCollection:
            # modify properties
            groundEllipsesElement.static_graphics_2d = True
            groundEllipsesElement.dynamic_graphics_2d = True
            groundEllipsesElement.interpolate = True
            groundEllipsesElement.show_name = True
            groundEllipsesElement.show_center_point_marker = True
            groundEllipsesElement.color = Colors.from_argb(66047)
            groundEllipsesElement.line_width = LineWidth.WIDTH2

        iIndex: int = 0
        while iIndex < oCollection.count:
            oEllipse: "VehicleGraphics2DGroundEllipsesElement" = oCollection[iIndex]
            self.m_logger.WriteLine10(
                "\t\tModified Ellipse {0}: EllipseSetName = {1}, Color = {7}, LineWidth = {8}, StaticGfx = {2}, DynamicGfx = {3}, Interpolate = {4}, IsNameVisible = {5}, IsCenterVisible = {6}",
                iIndex,
                oEllipse.ellipse_set_name,
                oEllipse.static_graphics_2d,
                oEllipse.dynamic_graphics_2d,
                oEllipse.interpolate,
                oEllipse.show_name,
                oEllipse.show_center_point_marker,
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
    def Run(self, oLighting: "VehicleGraphics2DLighting"):
        self.m_logger.WriteLine("----- THE GRAPHICS LIGHTING TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oLighting)
        # IsSunLightPenumbraVisible
        self.m_logger.WriteLine4(
            "The current IsSunLightPenumbraVisible flag is: {0}", oLighting.show_sunlight_penumbra_divider
        )
        oLighting.show_sunlight_penumbra_divider = False
        self.m_logger.WriteLine4(
            "The new IsSunLightPenumbraVisible flag is: {0}", oLighting.show_sunlight_penumbra_divider
        )
        Assert.assertEqual(False, oLighting.show_sunlight_penumbra_divider)
        oLighting.show_sunlight_penumbra_divider = True
        self.m_logger.WriteLine4(
            "The new IsSunLightPenumbraVisible flag is: {0}", oLighting.show_sunlight_penumbra_divider
        )
        Assert.assertEqual(True, oLighting.show_sunlight_penumbra_divider)
        # IsPenumbraUmbraVisible
        self.m_logger.WriteLine4(
            "The current IsPenumbraUmbraVisible flag is: {0}", oLighting.show_penumbra_umbra_divider
        )
        oLighting.show_penumbra_umbra_divider = False
        self.m_logger.WriteLine4("The new IsPenumbraUmbraVisible flag is: {0}", oLighting.show_penumbra_umbra_divider)
        Assert.assertEqual(False, oLighting.show_penumbra_umbra_divider)
        oLighting.show_penumbra_umbra_divider = True
        self.m_logger.WriteLine4("The new IsPenumbraUmbraVisible flag is: {0}", oLighting.show_penumbra_umbra_divider)
        Assert.assertEqual(True, oLighting.show_penumbra_umbra_divider)
        # IsSolarSpecularReflectionPointVisible
        self.m_logger.WriteLine4(
            "The current IsSolarSpecularReflectionPointVisible flag is: {0}",
            oLighting.show_solar_specular_reflection_point,
        )
        oLighting.show_solar_specular_reflection_point = False
        self.m_logger.WriteLine4(
            "The new IsSolarSpecularReflectionPointVisible flag is: {0}", oLighting.show_solar_specular_reflection_point
        )
        Assert.assertEqual(False, oLighting.show_solar_specular_reflection_point)
        oLighting.show_solar_specular_reflection_point = True
        self.m_logger.WriteLine4(
            "The new IsSolarSpecularReflectionPointVisible flag is: {0}", oLighting.show_solar_specular_reflection_point
        )
        Assert.assertEqual(True, oLighting.show_solar_specular_reflection_point)
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
    def LightingElement(self, oVeGfxLightingElement: "VehicleGraphics2DLightingElement"):
        Assert.assertIsNotNone(oVeGfxLightingElement)
        # Visible (false)
        self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oVeGfxLightingElement.visible)
        oVeGfxLightingElement.visible = False
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oVeGfxLightingElement.visible)
        Assert.assertEqual(False, oVeGfxLightingElement.visible)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oVeGfxLightingElement.color = Colors.from_argb(12632256)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oVeGfxLightingElement.line_style = LineStyle.DOT_DASHED

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oVeGfxLightingElement.line_width = LineWidth.WIDTH1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oVeGfxLightingElement.marker_style = "Circle"

        # Visible (true)
        oVeGfxLightingElement.visible = True
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oVeGfxLightingElement.visible)
        Assert.assertEqual(True, oVeGfxLightingElement.visible)
        # Color
        self.m_logger.WriteLine6("\tThe current Color is: {0}", oVeGfxLightingElement.color)
        oVeGfxLightingElement.color = Colors.from_argb(255)
        self.m_logger.WriteLine6("\tThe new Color is: {0}", oVeGfxLightingElement.color)
        AssertEx.AreEqual(Colors.from_argb(255), oVeGfxLightingElement.color)
        # LineStyle
        self.m_logger.WriteLine6("\tThe current LineStyle is: {0}", oVeGfxLightingElement.line_style)
        oVeGfxLightingElement.line_style = LineStyle.DOT_DASHED
        self.m_logger.WriteLine6("\tThe new LineStyle is: {0}", oVeGfxLightingElement.line_style)
        Assert.assertEqual(LineStyle.DOT_DASHED, oVeGfxLightingElement.line_style)

        # LineWidth
        self.m_logger.WriteLine6("\tThe current LineWidth is: {0}", oVeGfxLightingElement.line_width)
        oVeGfxLightingElement.line_width = LineWidth.WIDTH3
        self.m_logger.WriteLine6("\tThe new LineWidth is: {0}", oVeGfxLightingElement.line_width)
        Assert.assertEqual(LineWidth.WIDTH3, oVeGfxLightingElement.line_width)
        with pytest.raises(Exception):
            oVeGfxLightingElement.line_width = -1
        with pytest.raises(Exception):
            oVeGfxLightingElement.line_width = 11

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
    def Run(self, oResolution: "VehicleGraphics2DRouteResolution"):
        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oResolution)
        # Route
        self.m_logger.WriteLine6("The current Route is: {0}", oResolution.route)
        oResolution.route = 12345.6789
        self.m_logger.WriteLine6("The new Route is: {0}", oResolution.route)
        Assert.assertEqual(12345.6789, oResolution.route)

        oResolution.minimum_route = 1
        Assert.assertEqual(1, oResolution.minimum_route)

        with pytest.raises(Exception):
            oResolution.minimum_route = -1

        with pytest.raises(Exception):
            oResolution.route = -12345.6789

        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- END -----")


# endregion


# region GfxTrajectoryResolutionHelper
class GfxTrajectoryResolutionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oResolution: "VehicleGraphics2DTrajectoryResolution"):
        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oResolution)
        # GroundTrack
        self.m_logger.WriteLine6("The current GroundTrack is: {0}", oResolution.ground_track)
        oResolution.ground_track = 12345.6789
        self.m_logger.WriteLine6("The new GroundTrack is: {0}", oResolution.ground_track)
        Assert.assertEqual(12345.6789, oResolution.ground_track)

        oResolution.minimum_ground_track = 1
        Assert.assertEqual(1, oResolution.minimum_ground_track)

        with pytest.raises(Exception):
            oResolution.minimum_ground_track = -1

        with pytest.raises(Exception):
            oResolution.ground_track = -12345.6789

        # Trajectory
        self.m_logger.WriteLine6("The current Trajectory is: {0}", oResolution.trajectory)
        oResolution.trajectory = 6789.12345
        self.m_logger.WriteLine6("The new Trajectory is: {0}", oResolution.trajectory)
        Assert.assertEqual(6789.12345, oResolution.trajectory)

        oResolution.minimum_trajectory = 1
        Assert.assertEqual(1, oResolution.minimum_trajectory)

        with pytest.raises(Exception):
            oResolution.minimum_trajectory = -1

        with pytest.raises(Exception):
            oResolution.trajectory = -12345.6789

        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- END -----")


# endregion


# region GfxPassResolutionHelper
class GfxPassResolutionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oResolution: "VehicleGraphics2DPassResolution"):
        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oResolution)
        # GroundTrack
        self.m_logger.WriteLine6("The current GroundTrack is: {0}", oResolution.ground_track)
        oResolution.ground_track = 12345.6789
        self.m_logger.WriteLine6("The new GroundTrack is: {0}", oResolution.ground_track)
        Assert.assertEqual(12345.6789, oResolution.ground_track)

        oResolution.minimum_ground_track = 1
        Assert.assertEqual(1, oResolution.minimum_ground_track)

        with pytest.raises(Exception):
            oResolution.minimum_ground_track = -1

        with pytest.raises(Exception):
            oResolution.ground_track = -12345.6789

        # Orbit
        self.m_logger.WriteLine6("The current Orbit is: {0}", oResolution.orbit)
        oResolution.orbit = 6789.12345
        self.m_logger.WriteLine6("The new Orbit is: {0}", oResolution.orbit)
        Assert.assertEqual(6789.12345, oResolution.orbit)

        oResolution.minimum_orbit = 1
        Assert.assertEqual(1, oResolution.minimum_orbit)

        with pytest.raises(Exception):
            oResolution.minimum_orbit = -1

        with pytest.raises(Exception):
            oResolution.orbit = -12345.6789

        self.m_logger.WriteLine("----- THE GRAPHICS RESOLUTION TEST ----- END -----")


# endregion


# region GfxLeadTrailDataHelper
class GfxLeadTrailDataHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, leadTrailData: "VehicleGraphics2DLeadTrailData"):
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
                LeadTrailData(int(arSupportedTypes[iIndex][0])),
            )

            iIndex += 1

        # LeadDataType
        self.m_logger.WriteLine6("\tThe current LeadDataType is: {0}", leadTrailData.lead_data_type)

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            eType: "LeadTrailData" = LeadTrailData(int(arSupportedTypes[iIndex][0]))
            if not leadTrailData.is_lead_data_type_supported(eType):
                Assert.fail("The {0} LeadType should be supported!", eType)

            # SetLeadDataType
            leadTrailData.set_lead_data_type(eType)
            self.m_logger.WriteLine6("\tThe new LeadDataType is: {0}", leadTrailData.lead_data_type)
            Assert.assertEqual(eType, leadTrailData.lead_data_type)
            if leadTrailData.has_lead_data:
                if eType == LeadTrailData.FRACTION:
                    # LeadData
                    oFraction: "IVehicleLeadTrailDataFraction" = IVehicleLeadTrailDataFraction(leadTrailData.lead_data)
                    Assert.assertIsNotNone(oFraction)
                    # Fraction
                    self.m_logger.WriteLine6("\t\tThe current Fraction is: {0}", oFraction.fraction)
                    oFraction.fraction = 12.3456
                    self.m_logger.WriteLine6("\t\tThe new Fraction is: {0}", oFraction.fraction)
                    Assert.assertEqual(12.3456, oFraction.fraction)
                    # range test
                    with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                        oFraction.fraction = -56.34
                elif eType == LeadTrailData.TIME:
                    # LeadData
                    oTime: "IVehicleLeadTrailDataTime" = IVehicleLeadTrailDataTime(leadTrailData.lead_data)
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
                    # range test
                    with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                        oTime.time = 56340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
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
                LeadTrailData(int(arSupportedTypes[iIndex][0])),
            )

            iIndex += 1

        # TrailDataType
        self.m_logger.WriteLine6("\tThe current TrailDataType is: {0}", leadTrailData.trail_data_type)

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            eType: "LeadTrailData" = LeadTrailData(int(arSupportedTypes[iIndex][0]))
            if not leadTrailData.is_trail_data_type_supported(eType):
                Assert.fail("The {0} TrailType should be supported!", eType)

            # SetTrailDataType
            leadTrailData.set_trail_data_type(eType)
            self.m_logger.WriteLine6("\tThe new TrailDataType is: {0}", leadTrailData.trail_data_type)
            Assert.assertEqual(eType, leadTrailData.trail_data_type)
            if leadTrailData.has_trail_data:
                if eType == LeadTrailData.FRACTION:
                    # TrailData
                    oFraction: "IVehicleLeadTrailDataFraction" = IVehicleLeadTrailDataFraction(leadTrailData.trail_data)
                    Assert.assertIsNotNone(oFraction)
                    # Fraction
                    self.m_logger.WriteLine6("\t\tThe current Fraction is: {0}", oFraction.fraction)
                    oFraction.fraction = 12.3456
                    self.m_logger.WriteLine6("\t\tThe new Fraction is: {0}", oFraction.fraction)
                    Assert.assertEqual(12.3456, oFraction.fraction)
                    # range test

                    with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                        oFraction.fraction = -56.34
                elif eType == LeadTrailData.TIME:
                    # TrailData
                    oTime: "IVehicleLeadTrailDataTime" = IVehicleLeadTrailDataTime(leadTrailData.trail_data)
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
                    # range test

                    with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                        oTime.time = 56340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

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
        leadTrailData.set_trail_data_type(LeadTrailData(int(arSupportedTypes[0][0])))
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
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oSwath: "VehicleGraphics2DSwath"):
        self.m_logger.WriteLine("----- THE GRAPHICS SWATH TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oSwath)

        # ElevationType
        self.m_logger.WriteLine6("The current Elevation type is: {0}", oSwath.elevation_type)
        # ElevationSupportedTypes
        arTypes = oSwath.elevation_supported_types
        self.m_logger.WriteLine3("Available {0} Elevation types.", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VehicleGraphics2DElevation" = VehicleGraphics2DElevation(int(arTypes[iIndex][0]))
            self.m_logger.WriteLine8("\tElevation type {0}: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not oSwath.is_elevation_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            oSwath.set_elevation_type(eType)
            self.m_logger.WriteLine6("\t\tThe new Elevation type is: {0}", oSwath.elevation_type)
            Assert.assertEqual(eType, oSwath.elevation_type)
            if ((oSwath.elevation_type == VehicleGraphics2DElevation.ELEVATION_GROUND_ELEVATION)) or (
                (oSwath.elevation_type == VehicleGraphics2DElevation.ELEVATION_GROUND_ELEVATION_ENVELOPE)
            ):
                # Elevation
                gfxElevationGroundElevation: "VehicleGraphics2DElevationGroundElevation" = (
                    VehicleGraphics2DElevationGroundElevation(oSwath.elevation)
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
                with pytest.raises(Exception):
                    gfxElevationGroundElevation.angle = -56.34
                # restore AngleUnit
                self.m_oUnits.set_current_unit("AngleUnit", strUnit)
                self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
                Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
            elif oSwath.elevation_type == VehicleGraphics2DElevation.ELEVATION_SWATH_HALF_WIDTH:
                # Elevation
                gfxElevationSwathHalfWidth: "VehicleGraphics2DElevationSwathHalfWidth" = (
                    VehicleGraphics2DElevationSwathHalfWidth(oSwath.elevation)
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

                with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                    gfxElevationSwathHalfWidth.distance = -56.34

                # restore DistanceUnit
                self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
                self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
                Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
            elif ((oSwath.elevation_type == VehicleGraphics2DElevation.ELEVATION_VEHICLE_HALF_ANGLE)) or (
                (oSwath.elevation_type == VehicleGraphics2DElevation.ELEVATION_VEHICLE_HALF_ANGLE_ENVELOPE)
            ):
                gfxElevationVehicleHalfAngle: "VehicleGraphics2DElevationVehicleHalfAngle" = (
                    VehicleGraphics2DElevationVehicleHalfAngle(oSwath.elevation)
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
                with pytest.raises(Exception):
                    gfxElevationVehicleHalfAngle.angle = -56.34
                # restore AngleUnit
                self.m_oUnits.set_current_unit("AngleUnit", strUnit)
                self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
                Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
            else:
                Assert.fail("Invalid type: {0}!", eType)

            iIndex += 1

        # SetElevationType(UNKNOWN)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            oSwath.set_elevation_type(VehicleGraphics2DElevation.UNKNOWN)

        oSwath.set_elevation_type(VehicleGraphics2DElevation.ELEVATION_GROUND_ELEVATION)

        # Options
        self.m_logger.WriteLine6("The current Options is: {0}", oSwath.options)
        oSwath.options = VehicleGraphics2DOptionType.OPTIONS_EDGE_LIMITS
        self.m_logger.WriteLine6("The new Options is: {0}", oSwath.options)
        Assert.assertEqual(VehicleGraphics2DOptionType.OPTIONS_EDGE_LIMITS, oSwath.options)
        oSwath.options = VehicleGraphics2DOptionType.OPTIONS_FILLED_LIMITS
        self.m_logger.WriteLine6("The new Options is: {0}", oSwath.options)
        Assert.assertEqual(VehicleGraphics2DOptionType.OPTIONS_FILLED_LIMITS, oSwath.options)
        oSwath.options = VehicleGraphics2DOptionType.OPTIONS_NO_GRAPHICS
        self.m_logger.WriteLine6("The new Options is: {0}", oSwath.options)
        Assert.assertEqual(VehicleGraphics2DOptionType.OPTIONS_NO_GRAPHICS, oSwath.options)
        self.m_logger.WriteLine("----- THE GRAPHICS SWATH TEST ----- END -----")


# endregion


# region GfxWaypointMarkersHelper
class GfxWaypointMarkersHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oMarker: "VehicleGraphics2DWaypointMarker"):
        self.m_logger.WriteLine("----- THE GRAPHICS WAYPOINT MARKERS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oMarker)
        # IsWaypointMarkersVisible (false)
        self.m_logger.WriteLine4("The current WaypointMarkersVisible flag is: {0}", oMarker.show_waypoint_markers)
        oMarker.show_waypoint_markers = False
        self.m_logger.WriteLine4("The new WaypointMarkersVisible flag is: {0}", oMarker.show_waypoint_markers)
        Assert.assertEqual(False, oMarker.show_waypoint_markers)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oMarker.show_turn_markers = True

        # IsWaypointMarkersVisible (true)
        oMarker.show_waypoint_markers = True
        self.m_logger.WriteLine4("The new WaypointMarkersVisible flag is: {0}", oMarker.show_waypoint_markers)
        Assert.assertEqual(True, oMarker.show_waypoint_markers)
        # IsTurnMarkersVisible
        self.m_logger.WriteLine4("The current IsTurnMarkersVisible flag is: {0}", oMarker.show_turn_markers)
        oMarker.show_turn_markers = False
        self.m_logger.WriteLine4("The new IsTurnMarkersVisible flag is: {0}", oMarker.show_turn_markers)
        Assert.assertEqual(False, oMarker.show_turn_markers)
        oMarker.show_turn_markers = True
        self.m_logger.WriteLine4("The new IsTurnMarkersVisible flag is: {0}", oMarker.show_turn_markers)
        Assert.assertEqual(True, oMarker.show_turn_markers)
        # WaypointMarkers
        oCollection: "VehicleGraphics2DWaypointMarkersCollection" = oMarker.waypoint_markers
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The WaypointMarkers collection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            if iIndex == 0:
                self.m_logger.WriteLine("\tBefore modification:")

            # Item
            waypointMarkersElement: "VehicleGraphics2DWaypointMarkersElement" = oCollection[iIndex]
            Assert.assertIsNotNone(waypointMarkersElement)
            self.m_logger.WriteLine10(
                "\t\tElement {0}: Time = {1}, Color = {2}, UseVehColor = {3}, MarkerStyle = {4}, IsLabelVisible = {5}, Label = {6}, IsVisible = {7}",
                iIndex,
                waypointMarkersElement.time,
                waypointMarkersElement.color,
                waypointMarkersElement.use_vehicle_color,
                waypointMarkersElement.marker_style,
                waypointMarkersElement.show_label,
                waypointMarkersElement.label,
                waypointMarkersElement.show_graphics,
            )

            iIndex += 1

        # _NewEnum
        waypointMarkersElement: "VehicleGraphics2DWaypointMarkersElement"
        # _NewEnum
        for waypointMarkersElement in oCollection:
            waypointMarkersElement.use_vehicle_color = True

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                waypointMarkersElement.color = Colors.from_argb(1193046)

            waypointMarkersElement.show_label = True
            waypointMarkersElement.label = "WaypointLabel"
            waypointMarkersElement.show_graphics = True
            waypointMarkersElement.use_vehicle_color = False
            waypointMarkersElement.color = Colors.from_argb(65280)
            waypointMarkersElement.marker_style = "X"

        iIndex: int = 0
        while iIndex < oCollection.count:
            if iIndex == 0:
                self.m_logger.WriteLine("\tAfter  modification:")

            # Item
            waypointMarkersElement: "VehicleGraphics2DWaypointMarkersElement" = oCollection[iIndex]
            Assert.assertIsNotNone(waypointMarkersElement)
            self.m_logger.WriteLine10(
                "\t\tElement {0}: Time = {1}, Color = {2}, UseVehColor = {3}, MarkerStyle = {4}, IsLabelVisible = {5}, Label = {6}, IsVisible = {7}",
                iIndex,
                waypointMarkersElement.time,
                waypointMarkersElement.color,
                waypointMarkersElement.use_vehicle_color,
                waypointMarkersElement.marker_style,
                waypointMarkersElement.show_label,
                waypointMarkersElement.label,
                waypointMarkersElement.show_graphics,
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
    def Run(self, AG_SAT: "Satellite", oCollection: "VehicleGraphics2DTimeEventsCollection"):
        self.m_logger.WriteLine("----- THE GRAPHICS TIME EVENTS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The TimeEvents collection contains: {0} elements.", oCollection.count)
        # Add
        timeEventsElement: "VehicleGraphics2DTimeEventsElement" = oCollection.add()
        Assert.assertIsNotNone(timeEventsElement)
        self.m_logger.WriteLine3("After Add() the Time Events collection contains: {0} elements.", oCollection.count)
        Assert.assertEqual(1, oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            self.m_logger.WriteLine8(
                "\tElement {0}: TimeEventType = {1}, IsVisible = {2}",
                iIndex,
                oCollection[iIndex].time_event_type,
                oCollection[iIndex].show_graphics,
            )

            iIndex += 1

        # IsVisible (false)
        self.m_logger.WriteLine4("The current IsVisible flag is: {0}", timeEventsElement.show_graphics)
        timeEventsElement.show_graphics = False
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", timeEventsElement.show_graphics)
        Assert.assertEqual(False, timeEventsElement.show_graphics)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            timeEventsElement.set_time_event_type(VehicleGraphics2DTimeEventType.LINE)

        # IsVisible (true)
        timeEventsElement.show_graphics = True
        self.m_logger.WriteLine4("The new IsVisible flag is: {0}", timeEventsElement.show_graphics)
        Assert.assertEqual(True, timeEventsElement.show_graphics)
        # TimeEventTypeSupportedTypes
        arTypes = timeEventsElement.time_event_type_supported_types
        self.m_logger.WriteLine3("An array of supported TimeEvent types contains: {0} elements.", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VehicleGraphics2DTimeEventType" = VehicleGraphics2DTimeEventType(int(arTypes[iIndex][0]))
            if not timeEventsElement.is_time_event_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            self.m_logger.WriteLine8("\tType {0} is: {1} ({2}).", iIndex, arTypes[iIndex][1], eType)
            # SetTimeEventType
            timeEventsElement.set_time_event_type(eType)
            # TimeEventType
            self.m_logger.WriteLine6("\t\tThe new TimeEvent type is: {0}", timeEventsElement.time_event_type)
            Assert.assertEqual(eType, timeEventsElement.time_event_type)
            if eType == VehicleGraphics2DTimeEventType.LINE:
                # TimeEventTypeData
                oLine: "VehicleGraphics2DTimeEventTypeLine" = VehicleGraphics2DTimeEventTypeLine(
                    timeEventsElement.time_event_type_data
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
                    (IStkObject(AG_SAT)).analysis_workbench_components.time_intervals["AvailabilityTimeSpan"]
                )
                Assert.assertEqual("1 Jul 1999 00:00:00.000", oLine.event_interval.find_start_time())
                Assert.assertEqual("2 Jul 1999 00:00:00.000", oLine.event_interval.find_stop_time())

                # Color
                self.m_logger.WriteLine6("\t\tThe current Color is: {0}", oLine.color)
                oLine.color = Colors.from_argb(12377850)
                self.m_logger.WriteLine6("\t\tThe new Color is: {0}", oLine.color)
                AssertEx.AreEqual(Colors.from_argb(12377850), oLine.color)
                # UniqueID
                self.m_logger.WriteLine5("\t\tThe current UniqueID is: {0}", oLine.unique_identifer)
                oLine.unique_identifer = "Test line"
                self.m_logger.WriteLine5("\t\tThe new UniqueID is: {0}", oLine.unique_identifer)
                Assert.assertEqual("Test line", oLine.unique_identifer)
                # LineStyle
                self.m_logger.WriteLine6("\t\tThe current LineStyle is: {0}", oLine.line_style)
                oLine.line_style = LineStyle.DASH_DOT_DOTTED
                self.m_logger.WriteLine6("\t\tThe new LineStyle is: {0}", oLine.line_style)
                Assert.assertEqual(LineStyle.DASH_DOT_DOTTED, oLine.line_style)
                # LineWidth
                self.m_logger.WriteLine6("\t\tThe current LineWidth is: {0}", oLine.line_width)
                oLine.line_width = LineWidth.WIDTH5
                self.m_logger.WriteLine6("\t\tThe new LineWidth is: {0}", oLine.line_width)
                Assert.assertEqual(LineWidth.WIDTH5, oLine.line_width)
                # OffsetType
                self.m_logger.WriteLine6("\t\tThe current Offset type is: {0}", oLine.offset_type)
                # OffsetSupportedTypes
                arOffsetTypes = oLine.offset_supported_types
                self.m_logger.WriteLine3(
                    "\t\tArray of supported Offset types contains: {0} elements", len(arOffsetTypes)
                )

                i: int = 0
                while i < len(arOffsetTypes):
                    eOffset: "VehicleGraphics2DOffset" = VehicleGraphics2DOffset(int(arOffsetTypes[i][0]))
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

                    with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                        oLine.offset_pixels = 123

                    i += 1

            elif eType == VehicleGraphics2DTimeEventType.MARKER:
                # TimeEventTypeData
                oMarker: "VehicleGraphics2DTimeEventTypeMarker" = VehicleGraphics2DTimeEventTypeMarker(
                    timeEventsElement.time_event_type_data
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
                    (IStkObject(AG_SAT)).analysis_workbench_components.time_intervals["AvailabilityTimeSpan"]
                )
                Assert.assertEqual("1 Jul 1999 00:00:00.000", oMarker.event_interval.find_start_time())
                # BUG66610 Assert.AreEqual("1 Jul 1999 00:00:00.000", oMarker.StopTime);

                # Color
                self.m_logger.WriteLine6("\t\tThe current Color is: {0}", oMarker.color)
                oMarker.color = Colors.from_argb(11259375)
                self.m_logger.WriteLine6("\t\tThe new Color is: {0}", oMarker.color)
                AssertEx.AreEqual(Colors.from_argb(11259375), oMarker.color)
                # MarkerStyle
                self.m_logger.WriteLine5("\t\tThe current MarkerStyle is: {0}", oMarker.marker_style)
                oMarker.marker_style = "Star"
                self.m_logger.WriteLine5("\t\tThe new MarkerStyle is: {0}", oMarker.marker_style)
                Assert.assertEqual("Star", oMarker.marker_style)
                # UniqueID
                self.m_logger.WriteLine5("\t\tThe current UniqueID is: {0}", oMarker.unique_identifer)
                oMarker.unique_identifer = "Howdy"
                self.m_logger.WriteLine5("\t\tThe new UniqueID is: {0}", oMarker.unique_identifer)
                Assert.assertEqual("Howdy", oMarker.unique_identifer)
            elif eType == VehicleGraphics2DTimeEventType.TEXT:
                # TimeEventTypeData
                oText: "VehicleGraphics2DTimeEventTypeText" = VehicleGraphics2DTimeEventTypeText(
                    timeEventsElement.time_event_type_data
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
                    (IStkObject(AG_SAT)).analysis_workbench_components.time_intervals["AvailabilityTimeSpan"]
                )
                Assert.assertEqual("1 Jul 1999 00:00:00.000", oText.event_interval.find_start_time())
                # BUG66610 Assert.AreEqual("1 Jul 1999 00:00:00.000", oText.StopTime);

                # Color
                self.m_logger.WriteLine6("\t\tThe current Color is: {0}", oText.color)
                oText.color = Colors.from_argb(12377850)
                self.m_logger.WriteLine6("\t\tThe new Color is: {0}", oText.color)
                AssertEx.AreEqual(Colors.from_argb(12377850), oText.color)
                # UniqueID
                self.m_logger.WriteLine5("\t\tThe current UniqueID is: {0}", oText.unique_identifer)
                oText.unique_identifer = "Test text"
                self.m_logger.WriteLine5("\t\tThe new UniqueID is: {0}", oText.unique_identifer)
                Assert.assertEqual("Test text", oText.unique_identifer)
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
                    eOffset: "VehicleGraphics2DOffset" = VehicleGraphics2DOffset(int(arOffsetTypes[i][0]))
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

                    with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                        oText.offset_pixels = 123

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
        oEvent: "VehicleGraphics2DTimeEventsElement"
        for oEvent in oCollection:
            self.m_logger.WriteLine7(
                "\tElement: TimeEventType = {0}, IsVisible = {1}", oEvent.time_event_type, oEvent.show_graphics
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
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oCollection: "LabelNoteCollection"):
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
                oCollection[iIndex].show_note,
                oCollection[iIndex].show_label,
            )

            iIndex += 1

        # Count
        iCount: int = oCollection.count
        # Add
        oNote: "LabelNote" = oCollection.add("Label Note 1")
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
                oCollection[iIndex].show_note,
                oCollection[iIndex].show_label,
                iIndex,
            )

            iIndex += 1

        # Remove
        self.m_logger.WriteLine3("Before Remove() the LabelNotes collection contains: {0} elements", oCollection.count)
        oCollection.remove((oCollection.count - 1))
        self.m_logger.WriteLine3("After  Remove() the LabelNotes collection contains: {0} elements", oCollection.count)
        Assert.assertEqual((iCount + 1), oCollection.count)
        with pytest.raises(Exception):
            oCollection.remove((oCollection.count + 1))
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.count)
        labelNote: "LabelNote"
        for labelNote in oCollection:
            self.m_logger.WriteLine8(
                "\tBefore: Note = {0}, NoteVisible = {1}, LabelVisible = {2}",
                labelNote.note,
                labelNote.show_note,
                labelNote.show_label,
            )
            # Note
            labelNote.note = "Modified Label Note"
            Assert.assertEqual("Modified Label Note", labelNote.note)
            # LabelVisible
            labelNote.show_label = True
            Assert.assertEqual(True, labelNote.show_label)
            # NoteVisible
            labelNote.show_note = NoteShowType.ON
            Assert.assertEqual(NoteShowType.ON, labelNote.show_note)
            labelNote.show_note = NoteShowType.INTERVALS
            Assert.assertEqual(NoteShowType.INTERVALS, labelNote.show_note)
            # Intervals
            oHelper = IntervalCollectionHelper(self.m_oUnits)
            oHelper.Run(labelNote.intervals, IntervalCollectionHelper.IntervalCollectionType.LabelNotes)
            # NoteVisible
            labelNote.show_note = NoteShowType.OFF
            Assert.assertEqual(NoteShowType.OFF, labelNote.show_note)

        self.m_logger.WriteLine("----- THE GRAPHICS LABELNOTES TEST ----- END -----")

    # endregion
