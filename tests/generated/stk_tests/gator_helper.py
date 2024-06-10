import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from logger import *
from math2 import *
from ansys.stk.core.utilities.colors import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.stkutil import *


class GatorHelper(object):
    m_logger = Logger.Instance

    bIsStkX: bool = False

    @staticmethod
    def TestOrbitState(oState: "State"):
        GatorHelper.TestRuntimeTypeInfo(oState)

        coordSystemName: str = oState.coord_system_name
        oState.set_element_type(ELEMENT_TYPE.SPHERICAL)
        Assert.assertEqual(ELEMENT_TYPE.SPHERICAL, oState.element_type)
        spherical: "ElementSpherical" = ElementSpherical(oState.element)
        spherical.declination = 1
        Assert.assertAlmostEqual(1, float(spherical.declination), delta=Math2.Epsilon12)
        spherical.horizontal_flight_path_angle = 1
        Assert.assertAlmostEqual(1, float(spherical.horizontal_flight_path_angle), delta=0.001)
        spherical.radius_magnitude = 6678.2
        Assert.assertAlmostEqual(6678.2, float(spherical.radius_magnitude), delta=0.001)
        spherical.right_ascension = 1
        Assert.assertAlmostEqual(1, float(spherical.right_ascension), delta=0.001)
        spherical.velocity_azimuth = 62
        Assert.assertAlmostEqual(62, float(spherical.velocity_azimuth), delta=0.001)
        spherical.velocity_magnitude = 8
        Assert.assertAlmostEqual(8, float(spherical.velocity_magnitude), delta=0.001)

        oState.set_element_type(ELEMENT_TYPE.CARTESIAN)
        Assert.assertEqual(ELEMENT_TYPE.CARTESIAN, oState.element_type)

        cart: "ElementCartesian" = ElementCartesian(oState.element)
        GatorHelper.TestRuntimeTypeInfo(cart)

        cart.x = 6670
        Assert.assertEqual(6670, cart.x)
        cart.y = 1
        Assert.assertEqual(1, cart.y)
        cart.z = 1
        Assert.assertEqual(1, cart.z)

        cart.vx = 1
        Assert.assertEqual(1, cart.vx)
        cart.vy = 7
        Assert.assertEqual(7, cart.vy)
        cart.vz = 4
        Assert.assertEqual(4, cart.vz)

        oState.set_element_type(ELEMENT_TYPE.TARGET_VECTOR_OUTGOING_ASYMPTOTE)
        Assert.assertEqual(ELEMENT_TYPE.TARGET_VECTOR_OUTGOING_ASYMPTOTE, oState.element_type)
        outgoing: "ElementTargetVectorOutgoingAsymptote" = ElementTargetVectorOutgoingAsymptote(oState.element)

        outgoing.radius_of_periapsis = 6678.2
        Assert.assertAlmostEqual(6678.2, float(outgoing.radius_of_periapsis), delta=0.001)
        outgoing.c3_energy = -58
        Assert.assertAlmostEqual(-58, float(outgoing.c3_energy), delta=0.001)
        outgoing.ra_outgoing_asymptote = 181
        Assert.assertAlmostEqual(181, float(outgoing.ra_outgoing_asymptote), delta=0.001)
        outgoing.declination_outgoing_asymptote = 1
        Assert.assertAlmostEqual(1, float(outgoing.declination_outgoing_asymptote), delta=0.001)
        outgoing.velocity_azimuth_periapsis = 62
        Assert.assertAlmostEqual(62, float(outgoing.velocity_azimuth_periapsis), delta=0.001)
        outgoing.true_anomaly = 1
        Assert.assertAlmostEqual(1, float(outgoing.true_anomaly), delta=0.001)

        oState.set_element_type(ELEMENT_TYPE.TARGET_VECTOR_INCOMING_ASYMPTOTE)
        Assert.assertEqual(ELEMENT_TYPE.TARGET_VECTOR_INCOMING_ASYMPTOTE, oState.element_type)
        incoming: "ElementTargetVectorIncomingAsymptote" = ElementTargetVectorIncomingAsymptote(oState.element)
        incoming.radius_of_periapsis = 6678.2
        Assert.assertAlmostEqual(6678.2, float(incoming.radius_of_periapsis), delta=0.001)
        incoming.c3_energy = -58
        Assert.assertAlmostEqual(-58, float(incoming.c3_energy), delta=0.001)
        incoming.ra_incoming_asymptote = 181
        Assert.assertAlmostEqual(181, float(incoming.ra_incoming_asymptote), delta=0.001)
        incoming.declination_incoming_asymptote = 1
        Assert.assertAlmostEqual(1, float(incoming.declination_incoming_asymptote), delta=0.001)
        incoming.velocity_azimuth_periapsis = 62
        Assert.assertAlmostEqual(62, float(incoming.velocity_azimuth_periapsis), delta=0.001)
        incoming.true_anomaly = 1
        Assert.assertAlmostEqual(1, float(incoming.true_anomaly), delta=0.001)

        oState.set_element_type(ELEMENT_TYPE.KEPLERIAN)
        Assert.assertEqual(ELEMENT_TYPE.KEPLERIAN, oState.element_type)
        kep: "ElementKeplerian" = ElementKeplerian(oState.element)
        kep.arg_of_periapsis = 1
        Assert.assertAlmostEqual(1, float(kep.arg_of_periapsis), delta=0.001)

        kep.eccentricity = 0.01
        Assert.assertAlmostEqual(0.01, float(kep.eccentricity), delta=0.001)
        kep.inclination = 29
        Assert.assertAlmostEqual(29, float(kep.inclination), delta=1e-08)
        kep.raan = 358
        Assert.assertEqual(358, kep.raan)
        kep.semi_major_axis = 6680
        Assert.assertEqual(6680, Math.Round(kep.semi_major_axis, 3))
        kep.true_anomaly = 358
        Assert.assertAlmostEqual(358, float(kep.true_anomaly), delta=1e-08)

        oState.cd = 0
        Assert.assertEqual(0, oState.cd)
        oState.cr = 0.01
        Assert.assertEqual(0.01, oState.cr)
        oState.drag_area = 0.02
        Assert.assertEqual(0.02, oState.drag_area)
        oState.dry_mass = 0.03
        Assert.assertEqual(0.03, oState.dry_mass)
        oState.epoch = "1 Jul 1999 00:00:00.000"
        Assert.assertEqual("1 Jul 1999 00:00:00.000", oState.epoch)
        oState.fuel_density = 0.04
        Assert.assertEqual(0.04, oState.fuel_density)
        oState.fuel_mass = 0.05
        Assert.assertEqual(0.05, oState.fuel_mass)
        oState.k1 = 0.06
        Assert.assertEqual(0.06, oState.k1)
        oState.k2 = 0.07
        Assert.assertEqual(0.07, oState.k2)
        oState.radiation_pressure_area = 0.08
        Assert.assertEqual(0.08, oState.radiation_pressure_area)
        oState.radiation_pressure_coeff = 0.09
        Assert.assertEqual(0.09, oState.radiation_pressure_coeff)
        oState.srp_area = 0.1
        Assert.assertEqual(0.1, oState.srp_area)
        oState.tank_pressure = 0.11
        Assert.assertEqual(0.11, oState.tank_pressure)
        oState.tank_temperature = 0.12
        Assert.assertEqual(0.12, oState.tank_temperature)

    @staticmethod
    def TestStoppingConditionCollection(scc: "StoppingConditionCollection"):
        GatorHelper.TestStoppingConditionCollection2(scc, False)

    @staticmethod
    def TestStoppingConditionCollection2(scc: "StoppingConditionCollection", readOnly: bool):
        sc: "StoppingCondition" = None
        if readOnly:
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                sc = clr.CastAs(scc.add("Altitude").properties, StoppingCondition)
            return

        sc = clr.CastAs(scc.add("Altitude").properties, StoppingCondition)
        GatorHelper.TestRuntimeTypeInfo(sc)

        temp: "StoppingCondition" = clr.CastAs(scc["Altitude"].properties, StoppingCondition)
        Assert.assertEqual((IComponentInfo(sc)).name, (IComponentInfo(temp)).name)
        sc.trip = 201
        Assert.assertEqual(201, sc.trip)
        sc.criterion = CRITERION.CROSS_DECREASING
        Assert.assertEqual(CRITERION.CROSS_DECREASING, sc.criterion)
        sc.criterion = CRITERION.CROSS_EITHER
        Assert.assertEqual(CRITERION.CROSS_EITHER, sc.criterion)
        sc.criterion = CRITERION.CROSS_INCREASING
        Assert.assertEqual(CRITERION.CROSS_INCREASING, sc.criterion)
        sc.tolerance = 1
        Assert.assertEqual(1, sc.tolerance)
        sc.repeat_count = 2
        Assert.assertEqual(2, sc.repeat_count)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            sc.max_trip_times = 10001

        sc.central_body_name = "Mars"
        scx: "STOPPING_CONDITION" = sc.stopping_condition_type
        scc.remove("Altitude")

        i: int = 0
        while i < scc.count:
            cmp: "IComponentInfo" = IComponentInfo(scc[i])
            name: str = cmp.name
            userComment: str = cmp.user_comment
            desc: str = cmp.description
            isReadOnly: bool = cmp.is_read_only()

            i += 1

        sce: "StoppingConditionElement" = scc["Duration"]

        with pytest.raises(Exception):
            cmp3: "IComponentInfo" = IComponentInfo(scc[5])

        with pytest.raises(Exception):
            cmp4: "IComponentInfo" = IComponentInfo(scc["Bogus"])

        cmp: "IComponentInfo"

        for cmp in scc:
            name: str = cmp.name

        with pytest.raises(Exception):
            scc.add("Bogus")

        Assert.assertEqual(1, scc.count)
        scc.add("Argument of Latitude")
        Assert.assertEqual(2, scc.count)
        scc.remove(1)
        Assert.assertEqual(1, scc.count)
        scc.add("Argument of Latitude")
        Assert.assertEqual(2, scc.count)
        scc.remove("Argument of Latitude")

        scc.add("Argument of Latitude")
        scc.remove("Argument of Latitude")
        with pytest.raises(Exception):
            scc.remove("Bogus")

        sc = clr.CastAs(StoppingCondition(scc.add("Argument of Latitude").properties), StoppingCondition)
        sc.trip = 1
        Assert.assertEqual(1, sc.trip)
        sc.criterion = CRITERION.CROSS_DECREASING
        Assert.assertEqual(CRITERION.CROSS_DECREASING, sc.criterion)
        sc.criterion = CRITERION.CROSS_EITHER
        Assert.assertEqual(CRITERION.CROSS_EITHER, sc.criterion)
        sc.criterion = CRITERION.CROSS_INCREASING
        Assert.assertEqual(CRITERION.CROSS_INCREASING, sc.criterion)
        sc.tolerance = 1
        Assert.assertEqual(1, sc.tolerance)
        sc.repeat_count = 2
        Assert.assertEqual(2, sc.repeat_count)
        Assert.assertEqual("STOP", sc.sequence)
        sc.coord_system = "CentralBody/Earth FixedAtJ2000"
        Assert.assertEqual("CentralBody/Earth FixedAtJ2000", sc.coord_system)
        sc.user_calc_object_name = "Cartesian Elems/Vx"
        Assert.assertEqual("Vx", sc.user_calc_object_name)
        sc.user_calc_object_name = "Geodetic/AltitudeRate"
        Assert.assertEqual("AltitudeRate", sc.user_calc_object_name)

        sc.user_calc_object_link_embed_control.set_component("LongitudeRate")
        Assert.assertEqual("LongitudeRate", sc.user_calc_object_link_embed_control.component.name)
        sc.user_calc_object_link_embed_control.reference_type = COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.LINKED
        Assert.assertEqual(
            COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.LINKED, sc.user_calc_object_link_embed_control.reference_type
        )
        sc.user_calc_object_link_embed_control.reference_type = COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.UNLINKED
        Assert.assertEqual(
            COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE.UNLINKED, sc.user_calc_object_link_embed_control.reference_type
        )

        with pytest.raises(Exception):
            test: str = sc.coord_system
        sc.central_body_name = "Mars"
        Assert.assertEqual("Mars", sc.central_body_name)
        sc.inherited = False
        Assert.assertFalse(sc.inherited)
        GatorHelper.TestBeforeStoppingConditionCollection(sc.before_conditions)

    @staticmethod
    def TestBeforeStoppingConditionCollection(bscc: "StoppingConditionCollection"):
        bsc: "StoppingCondition" = clr.CastAs(bscc.add("Altitude").properties, StoppingCondition)
        bsc.trip = 202
        Assert.assertEqual(202, bsc.trip)
        bsc.criterion = CRITERION.CROSS_DECREASING
        Assert.assertEqual(CRITERION.CROSS_DECREASING, bsc.criterion)
        bsc.criterion = CRITERION.CROSS_EITHER
        Assert.assertEqual(CRITERION.CROSS_EITHER, bsc.criterion)
        bsc.criterion = CRITERION.CROSS_INCREASING
        Assert.assertEqual(CRITERION.CROSS_INCREASING, bsc.criterion)
        bsc.tolerance = 1
        Assert.assertEqual(1, bsc.tolerance)
        bsc.repeat_count = 2
        Assert.assertEqual(2, bsc.repeat_count)
        bsc.central_body_name = "Moon"
        Assert.assertEqual("Moon", bsc.central_body_name)

        i: int = 0
        while i < bscc.count:
            cmp: "IComponentInfo" = clr.CastAs(bscc[i], IComponentInfo)

            i += 1

        cmp: "IComponentInfo"

        for cmp in bscc:
            pass

        count: int = bscc.count
        bscc.remove("Altitude")
        Assert.assertEqual((count - 1), bscc.count)

    @staticmethod
    def TestAttitudeControl(attControl: "IAttitudeControl"):
        attControl.body_axis = BODY_AXIS.MINUS_Z
        Assert.assertEqual(BODY_AXIS.MINUS_Z, attControl.body_axis)
        attControl.body_axis = BODY_AXIS.MINUS_Y
        Assert.assertEqual(BODY_AXIS.MINUS_Y, attControl.body_axis)
        attControl.body_axis = BODY_AXIS.MINUS_X
        Assert.assertEqual(BODY_AXIS.MINUS_X, attControl.body_axis)
        attControl.body_axis = BODY_AXIS.PLUS_Z
        Assert.assertEqual(BODY_AXIS.PLUS_Z, attControl.body_axis)
        attControl.body_axis = BODY_AXIS.PLUS_Y
        Assert.assertEqual(BODY_AXIS.PLUS_Y, attControl.body_axis)
        attControl.body_axis = BODY_AXIS.PLUS_X
        Assert.assertEqual(BODY_AXIS.PLUS_X, attControl.body_axis)

        attControl.lead_duration = -1
        Assert.assertEqual(-1, attControl.lead_duration)
        attControl.lead_duration = 400
        Assert.assertEqual(400, attControl.lead_duration)

        attControl.trail_duration = 340
        Assert.assertEqual(340, attControl.trail_duration)

        attControl.custom_function = CUSTOM_FUNCTION.ENABLE_PAGE_DEFINITION
        Assert.assertEqual(CUSTOM_FUNCTION.ENABLE_PAGE_DEFINITION, attControl.custom_function)
        attControl.custom_function = CUSTOM_FUNCTION.ENABLE_MANEUVER_ATTITUDE
        Assert.assertEqual(CUSTOM_FUNCTION.ENABLE_MANEUVER_ATTITUDE, attControl.custom_function)

        attControl.constraint_sign = CONSTRAINT_SIGN.MINUS
        Assert.assertEqual(CONSTRAINT_SIGN.MINUS, attControl.constraint_sign)
        attControl.constraint_sign = CONSTRAINT_SIGN.PLUS
        Assert.assertEqual(CONSTRAINT_SIGN.PLUS, attControl.constraint_sign)

        attControl.constraint_vector_name = "CentralBody/Moon Moon Angular Velocity"
        Assert.assertEqual("CentralBody/Moon Moon_Angular_Velocity", attControl.constraint_vector_name)

        with pytest.raises(Exception):
            attControl.body_axis = BODY_AXIS((-1)) if ((-1) in [item.value for item in BODY_AXIS]) else (-1)
        with pytest.raises(Exception):
            attControl.custom_function = (
                CUSTOM_FUNCTION((-1)) if ((-1) in [item.value for item in CUSTOM_FUNCTION]) else (-1)
            )
        with pytest.raises(Exception):
            attControl.constraint_sign = (
                CONSTRAINT_SIGN((-1)) if ((-1) in [item.value for item in CONSTRAINT_SIGN]) else (-1)
            )
        with pytest.raises(Exception):
            attControl.constraint_vector_name = "Bogus"

    @staticmethod
    def TestSNOPTControlParameter(cp: "SNOPTControl", objName: str, decName: str):
        Assert.assertEqual(decName, cp.name)
        Console.WriteLine(cp.name)

        Assert.assertEqual(objName, cp.parent_name)
        Console.WriteLine(cp.parent_name)

        initialValue: typing.Any = cp.initial_value
        Console.WriteLine(str(cp.initial_value))

        cp.enable = False
        Assert.assertFalse(cp.enable)

        cp.enable = True
        Assert.assertTrue(cp.enable)

        cp.current_value = 5
        Assert.assertEqual(5, cp.current_value)

        cp.lower_bound = 1
        Assert.assertEqual(1, cp.lower_bound)

        cp.upper_bound = 10
        Assert.assertEqual(10, cp.upper_bound)

        cp.scaling_value = 2.0
        Assert.assertEqual(2.0, cp.scaling_value)

        cp.use_custom_display_unit = False
        Assert.assertFalse(cp.use_custom_display_unit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cp.custom_display_unit = "m"

        cp.use_custom_display_unit = True
        Assert.assertTrue(cp.use_custom_display_unit)

        cp.custom_display_unit = "min"
        Assert.assertEqual("min", cp.custom_display_unit)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid Unit")):
            cp.custom_display_unit = "m"

        GatorHelper.m_logger.WriteLine("TestSNOPTControlParameter End")

    @staticmethod
    def TestIPOPTControlParameter(cp: "IPOPTControl", objName: str, decName: str):
        Assert.assertEqual(decName, cp.name)
        Console.WriteLine(cp.name)

        Assert.assertEqual(objName, cp.parent_name)
        Console.WriteLine(cp.parent_name)

        initialValue: typing.Any = cp.initial_value
        Console.WriteLine(str(cp.initial_value))

        cp.enable = False
        Assert.assertFalse(cp.enable)

        cp.enable = True
        Assert.assertTrue(cp.enable)

        cp.current_value = 5
        Assert.assertEqual(5, cp.current_value)

        cp.lower_bound = 1
        Assert.assertEqual(1, cp.lower_bound)

        cp.upper_bound = 10
        Assert.assertEqual(10, cp.upper_bound)

        cp.scaling_value = 2.0
        Assert.assertEqual(2.0, cp.scaling_value)

        cp.use_custom_display_unit = False
        Assert.assertFalse(cp.use_custom_display_unit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cp.custom_display_unit = "m"

        cp.use_custom_display_unit = True
        Assert.assertTrue(cp.use_custom_display_unit)

        cp.custom_display_unit = "min"
        Assert.assertEqual("min", cp.custom_display_unit)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid Unit")):
            cp.custom_display_unit = "m"

    @staticmethod
    def TestBisectionControlParameter(cp: "BisectionControl", objName: str, decName: str):
        Assert.assertEqual(decName, cp.name)
        Console.WriteLine(cp.name)

        Assert.assertEqual(objName, cp.parent_name)
        Console.WriteLine(cp.parent_name)

        initialValue: typing.Any = cp.initial_value
        Console.WriteLine(str(cp.initial_value))

        cp.enable = False
        Assert.assertFalse(cp.enable)
        cp.enable = True
        Assert.assertTrue(cp.enable)

        cp.current_value = 5
        Assert.assertEqual(5, cp.current_value)

        cp.bound_search_step = 111
        Assert.assertEqual(111, cp.bound_search_step)

        cp.use_custom_display_unit = False
        Assert.assertFalse(cp.use_custom_display_unit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            cp.custom_display_unit = "m"

        cp.use_custom_display_unit = True
        Assert.assertTrue(cp.use_custom_display_unit)

        cp.custom_display_unit = "min"
        Assert.assertEqual("min", cp.custom_display_unit)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid Unit")):
            cp.custom_display_unit = "m"

    @staticmethod
    def TestDCControlParameter(cp: "DifferentialCorrectorControl"):
        GatorHelper.TestRuntimeTypeInfo(cp)

        cp.enable = True
        Assert.assertTrue(cp.enable)

        # m_logger.WriteLine(cp.Name);
        # m_logger.WriteLine(cp.ParentName);
        # m_logger.WriteLine(cp.FinalValue);
        # m_logger.WriteLine(cp.LastUpdate);
        GatorHelper.m_logger.WriteLine(cp.dimension)
        name: str = cp.name
        parentName: str = cp.parent_name
        finalValue: typing.Any = cp.final_value
        lastUpdate: typing.Any = cp.last_update

        initialValue: typing.Any = cp.initial_value

        cp.correction = 1
        Assert.assertEqual(1, cp.correction)
        # m_logger.WriteLine(cp.Correction);

        cp.tolerance = 1
        Assert.assertEqual(1, cp.tolerance)
        # m_logger.WriteLine(cp.Tolerance);

        cp.perturbation = 59
        Assert.assertAlmostEqual(59, float(cp.perturbation), delta=1e-08)
        # m_logger.WriteLine(cp.Perturbation);

        cp.max_step = 3601
        Assert.assertEqual(3601, cp.max_step)
        # m_logger.WriteLine(cp.MaxStep);

        cp.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.INITIAL_VALUE
        Assert.assertEqual(DIFFERENTIAL_CORRECTOR_SCALING_METHOD.INITIAL_VALUE, cp.scaling_method)

        cp.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.ONE_NO_SCALING
        Assert.assertEqual(DIFFERENTIAL_CORRECTOR_SCALING_METHOD.ONE_NO_SCALING, cp.scaling_method)

        cp.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.TOLERANCE
        Assert.assertEqual(DIFFERENTIAL_CORRECTOR_SCALING_METHOD.TOLERANCE, cp.scaling_method)

        cp.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.SPECIFIED_VALUE
        Assert.assertEqual(DIFFERENTIAL_CORRECTOR_SCALING_METHOD.SPECIFIED_VALUE, cp.scaling_method)

        cp.scaling_value = 1.0
        Assert.assertEqual(1.0, cp.scaling_value)

        Assert.assertEqual(0, Array.Length(cp.values))

    @staticmethod
    def TestUpdateControls(update: "MissionControlSequenceUpdate", dc: "ProfileDifferentialCorrector"):
        GatorHelper.TestRuntimeTypeInfo(dc.control_parameters)
        Assert.assertTrue(update.control_parameters_available)

        update.enable_control_parameter(CONTROL_UPDATE.CD_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.CD_VAL))
        cp: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths("myUpdate", "CdVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.CD_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.CD_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "CdVal")

        update.enable_control_parameter(CONTROL_UPDATE.CR_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.CR_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "CrVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.CR_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.CR_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "CrVal")

        update.enable_control_parameter(CONTROL_UPDATE.DRAG_AREA_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.DRAG_AREA_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "DragAreaVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.DRAG_AREA_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.DRAG_AREA_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "DragAreaVal")

        update.enable_control_parameter(CONTROL_UPDATE.DRY_MASS_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.DRY_MASS_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "DryMassVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.DRY_MASS_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.DRY_MASS_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "DryMassVal")

        update.enable_control_parameter(CONTROL_UPDATE.FUEL_DENSITY_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.FUEL_DENSITY_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "FuelDensityVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.FUEL_DENSITY_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.FUEL_DENSITY_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "FuelDensityVal")

        update.enable_control_parameter(CONTROL_UPDATE.FUEL_MASS_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.FUEL_MASS_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "FuelMassVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.FUEL_MASS_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.FUEL_MASS_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "FuelMassVal")

        update.enable_control_parameter(CONTROL_UPDATE.RADIATION_PRESSURE_AREA_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.RADIATION_PRESSURE_AREA_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "RadPressureAreaVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.RADIATION_PRESSURE_AREA_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.RADIATION_PRESSURE_AREA_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "RadPressureAreaVal")

        update.enable_control_parameter(CONTROL_UPDATE.RADIATION_PRESSURE_COEFFICIENT_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.RADIATION_PRESSURE_COEFFICIENT_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "RadPressureCoefficientVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.RADIATION_PRESSURE_COEFFICIENT_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.RADIATION_PRESSURE_COEFFICIENT_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "RadPressureCoefficientVal")

        update.enable_control_parameter(CONTROL_UPDATE.SRP_AREA_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.SRP_AREA_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "SRPAreaVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.SRP_AREA_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.SRP_AREA_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "SRPAreaVal")

        update.enable_control_parameter(CONTROL_UPDATE.TANK_PRESSURE_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.TANK_PRESSURE_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "TankPressureVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.TANK_PRESSURE_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.TANK_PRESSURE_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "TankPressureVal")

        update.enable_control_parameter(CONTROL_UPDATE.TANK_TEMP_VAL)
        Assert.assertTrue(update.is_control_parameter_enabled(CONTROL_UPDATE.TANK_TEMP_VAL))
        cp = dc.control_parameters.get_control_by_paths("myUpdate", "TankTemperatureVal")
        Assert.assertEqual(cp.parent_name, "myUpdate")
        GatorHelper.TestDCControlParameter(cp)
        update.disable_control_parameter(CONTROL_UPDATE.TANK_TEMP_VAL)
        Assert.assertFalse(update.is_control_parameter_enabled(CONTROL_UPDATE.TANK_TEMP_VAL))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myUpdate", "TankTemperatureVal")

    @staticmethod
    def TestPropagateControls(prop: "MissionControlSequencePropagate", dc: "ProfileDifferentialCorrector"):
        GatorHelper.TestRuntimeTypeInfo(prop)

        Assert.assertTrue(prop.control_parameters_available)

        prop.enable_control_parameter(CONTROL_ADVANCED.PROPAGATE_MAX_PROP_TIME)
        Assert.assertTrue(prop.is_control_parameter_enabled(CONTROL_ADVANCED.PROPAGATE_MAX_PROP_TIME))
        cp: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths("myProp", "MaxPropTime")
        Assert.assertEqual(cp.parent_name, "myProp")
        GatorHelper.TestDCControlParameter(cp)
        prop.disable_control_parameter(CONTROL_ADVANCED.PROPAGATE_MAX_PROP_TIME)
        Assert.assertFalse(prop.is_control_parameter_enabled(CONTROL_ADVANCED.PROPAGATE_MAX_PROP_TIME))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myProp", "MaxPropTime")

        prop.enable_control_parameter(CONTROL_ADVANCED.PROPAGATE_MIN_PROP_TIME)
        Assert.assertTrue(prop.is_control_parameter_enabled(CONTROL_ADVANCED.PROPAGATE_MIN_PROP_TIME))
        cp = dc.control_parameters.get_control_by_paths("myProp", "MinPropTime")
        Assert.assertEqual(cp.parent_name, "myProp")
        GatorHelper.TestDCControlParameter(cp)
        prop.disable_control_parameter(CONTROL_ADVANCED.PROPAGATE_MIN_PROP_TIME)
        Assert.assertFalse(prop.is_control_parameter_enabled(CONTROL_ADVANCED.PROPAGATE_MIN_PROP_TIME))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myProp", "MinPropTime")

    @staticmethod
    def TestFollowControls(follow: "MissionControlSequenceFollow", dc: "ProfileDifferentialCorrector"):
        GatorHelper.TestRuntimeTypeInfo(follow)
        Assert.assertTrue(follow.control_parameters_available)

        follow.enable_control_parameter(CONTROL_FOLLOW.CD)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.CD))
        cp: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.Cd")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.CD)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.CD))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.Cd")

        follow.enable_control_parameter(CONTROL_FOLLOW.CK)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.CK))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.RadPressureCoeff")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.CK)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.CK))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.RadPressureCoeff")

        follow.enable_control_parameter(CONTROL_FOLLOW.CR)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.CR))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.Cr")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.CR)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.CR))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.Cr")

        follow.enable_control_parameter(CONTROL_FOLLOW.DRAG_AREA)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.DRAG_AREA))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.DragArea")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.DRAG_AREA)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.DRAG_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.DragArea")

        follow.enable_control_parameter(CONTROL_FOLLOW.DRY_MASS)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.DRY_MASS))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.DryMass")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.DRY_MASS)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.DRY_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.DryMass")

        follow.enable_control_parameter(CONTROL_FOLLOW.FUEL_DENSITY)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.FUEL_DENSITY))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.FuelDensity")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.FUEL_DENSITY)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.FUEL_DENSITY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.FuelDensity")

        follow.enable_control_parameter(CONTROL_FOLLOW.FUEL_MASS)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.FUEL_MASS))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "FuelMass")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.FUEL_MASS)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.FUEL_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "FuelMass")

        follow.enable_control_parameter(CONTROL_FOLLOW.K1)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.K1))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.K1")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.K1)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.K1))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.K1")

        follow.enable_control_parameter(CONTROL_FOLLOW.K2)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.K2))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.K2")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.K2)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.K2))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.K2")

        follow.enable_control_parameter(CONTROL_FOLLOW.MAX_FUEL_MASS)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.MAX_FUEL_MASS))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "MaxFuelMass")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.MAX_FUEL_MASS)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.MAX_FUEL_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "MaxFuelMass")

        follow.enable_control_parameter(CONTROL_FOLLOW.RADIATION_PRESSURE_AREA)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.RADIATION_PRESSURE_AREA))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.RadPressureArea")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.RADIATION_PRESSURE_AREA)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.RADIATION_PRESSURE_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.RadPressureArea")

        follow.enable_control_parameter(CONTROL_FOLLOW.SRP_AREA)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.SRP_AREA))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.SRPArea")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.SRP_AREA)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.SRP_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.SRPArea")

        follow.enable_control_parameter(CONTROL_FOLLOW.TANK_PRESSURE)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.TANK_PRESSURE))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.TankPressure")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.TANK_PRESSURE)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.TANK_PRESSURE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.TankPressure")

        follow.enable_control_parameter(CONTROL_FOLLOW.TANK_TEMP)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.TANK_TEMP))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.TankTemperature")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.TANK_TEMP)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.TANK_TEMP))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "InitialState.TankTemperature")

        follow.enable_control_parameter(CONTROL_FOLLOW.TANK_VOLUME)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.TANK_VOLUME))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "TankVolume")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.TANK_VOLUME)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.TANK_VOLUME))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "TankVolume")

        follow.enable_control_parameter(CONTROL_FOLLOW.X_OFFSET)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.X_OFFSET))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "Xoffset")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.X_OFFSET)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.X_OFFSET))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "Xoffset")

        follow.enable_control_parameter(CONTROL_FOLLOW.Y_OFFSET)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.Y_OFFSET))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "Yoffset")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.Y_OFFSET)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.Y_OFFSET))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "Yoffset")

        follow.enable_control_parameter(CONTROL_FOLLOW.Z_OFFSET)
        Assert.assertTrue(follow.is_control_parameter_enabled(CONTROL_FOLLOW.Z_OFFSET))
        cp = dc.control_parameters.get_control_by_paths("myFollow", "Zoffset")
        Assert.assertEqual(cp.parent_name, "myFollow")
        GatorHelper.TestDCControlParameter(cp)
        follow.disable_control_parameter(CONTROL_FOLLOW.Z_OFFSET)
        Assert.assertFalse(follow.is_control_parameter_enabled(CONTROL_FOLLOW.Z_OFFSET))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myFollow", "Zoffset")

    @staticmethod
    def TestLaunchControls(launch: "MissionControlSequenceLaunch", dc: "ProfileDifferentialCorrector"):
        GatorHelper.TestRuntimeTypeInfo(launch)
        Assert.assertTrue(launch.control_parameters_available)

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_ALTITUDE)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_ALTITUDE))
        cp: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths(
            "myLaunch", "Burnout.LaunchAzDRDAlt.Altitude"
        )
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_ALTITUDE)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_ALTITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDAlt.Altitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_AZ)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_AZ))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDAlt.LaunchAz")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_AZ)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_AZ))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDAlt.LaunchAz")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_DOWNRANGE_DIST)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_DOWNRANGE_DIST))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDAlt.DownrangeDistance")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_DOWNRANGE_DIST)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_ALTITUDE_DOWNRANGE_DIST))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDAlt.DownrangeDistance")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_RAD_AZ)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_RAD_AZ))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDRadius.LaunchAz")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_RAD_AZ)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_RAD_AZ))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDRadius.LaunchAz")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_RAD_DOWNRANGE_DIST)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_RAD_DOWNRANGE_DIST))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDRadius.DownrangeDistance")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_RAD_DOWNRANGE_DIST)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_RAD_DOWNRANGE_DIST))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDRadius.DownrangeDistance")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_RAD_RAD)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_RAD_RAD))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDRadius.Radius")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_AZ_RAD_RAD)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_AZ_RAD_RAD))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.LaunchAzDRDRadius.Radius")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_FIXED_VELOCITY)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_FIXED_VELOCITY))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.FixedVelocity")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_FIXED_VELOCITY)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_FIXED_VELOCITY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.FixedVelocity")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_LAT)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_LAT))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geocentric.Latitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_LAT)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_LAT))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geocentric.Latitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_LON)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_LON))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geocentric.Longitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_LON)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_LON))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geocentric.Longitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_RAD)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_RAD))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geocentric.Radius")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_RAD)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEOCENTRIC_RAD))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geocentric.Radius")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEODETIC_ALTITUDE)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEODETIC_ALTITUDE))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geodetic.Altitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEODETIC_ALTITUDE)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEODETIC_ALTITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geodetic.Altitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEODETIC_LAT)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEODETIC_LAT))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geodetic.Latitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEODETIC_LAT)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEODETIC_LAT))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geodetic.Latitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEODETIC_LON)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEODETIC_LON))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geodetic.Longitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_GEODETIC_LON)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_GEODETIC_LON))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.Geodetic.Longitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_INERTIAL_HORIZONTAL_FPA)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_INERTIAL_HORIZONTAL_FPA))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.InertialHFPA")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_INERTIAL_HORIZONTAL_FPA)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_INERTIAL_HORIZONTAL_FPA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.InertialHFPA")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_INERTIAL_VELOCITY)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_INERTIAL_VELOCITY))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.InertialVelocity")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_INERTIAL_VELOCITY)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_INERTIAL_VELOCITY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.InertialVelocity")

        launch.enable_control_parameter(CONTROL_LAUNCH.BURNOUT_INERTIAL_VELOCITY_AZIMUTH)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_INERTIAL_VELOCITY_AZIMUTH))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.InertialVelAzimuth")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.BURNOUT_INERTIAL_VELOCITY_AZIMUTH)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.BURNOUT_INERTIAL_VELOCITY_AZIMUTH))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Burnout.InertialVelAzimuth")

        launch.enable_control_parameter(CONTROL_LAUNCH.CD)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.CD))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.Cd")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.CD)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.CD))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.Cd")

        launch.enable_control_parameter(CONTROL_LAUNCH.CK)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.CK))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.RadPressureCoeff")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.CK)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.CK))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.RadPressureCoeff")

        launch.enable_control_parameter(CONTROL_LAUNCH.CR)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.CR))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.Cr")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.CR)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.CR))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.Cr")

        launch.enable_control_parameter(CONTROL_LAUNCH.DRAG_AREA)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.DRAG_AREA))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.DragArea")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.DRAG_AREA)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.DRAG_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.DragArea")

        launch.enable_control_parameter(CONTROL_LAUNCH.DRY_MASS)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.DRY_MASS))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.DryMass")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.DRY_MASS)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.DRY_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.DryMass")

        launch.enable_control_parameter(CONTROL_LAUNCH.EPOCH)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.EPOCH))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Epoch")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.EPOCH)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.EPOCH))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Epoch")

        launch.enable_control_parameter(CONTROL_LAUNCH.FUEL_DENSITY)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.FUEL_DENSITY))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.FuelDensity")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.FUEL_DENSITY)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.FUEL_DENSITY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.FuelDensity")

        launch.enable_control_parameter(CONTROL_LAUNCH.FUEL_MASS)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.FUEL_MASS))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "FuelMass")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.FUEL_MASS)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.FUEL_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "FuelMass")

        launch.enable_control_parameter(CONTROL_LAUNCH.GEOCENTRIC_LAT)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEOCENTRIC_LAT))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geocentric.Latitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.GEOCENTRIC_LAT)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEOCENTRIC_LAT))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geocentric.Latitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.GEOCENTRIC_LON)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEOCENTRIC_LON))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geocentric.Longitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.GEOCENTRIC_LON)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEOCENTRIC_LON))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geocentric.Longitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.GEOCENTRIC_RAD)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEOCENTRIC_RAD))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geocentric.Radius")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.GEOCENTRIC_RAD)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEOCENTRIC_RAD))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geocentric.Radius")

        launch.enable_control_parameter(CONTROL_LAUNCH.GEODETIC_ALTITUDE)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEODETIC_ALTITUDE))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geodetic.Altitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.GEODETIC_ALTITUDE)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEODETIC_ALTITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geodetic.Altitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.GEODETIC_LAT)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEODETIC_LAT))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geodetic.Latitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.GEODETIC_LAT)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEODETIC_LAT))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geodetic.Latitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.GEODETIC_LON)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEODETIC_LON))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geodetic.Longitude")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.GEODETIC_LON)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.GEODETIC_LON))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "Launch.Geodetic.Longitude")

        launch.enable_control_parameter(CONTROL_LAUNCH.K1)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.K1))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.K1")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.K1)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.K1))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.K1")

        launch.enable_control_parameter(CONTROL_LAUNCH.K2)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.K2))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.K2")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.K2)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.K2))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.K2")

        launch.enable_control_parameter(CONTROL_LAUNCH.MAX_FUEL_MASS)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.MAX_FUEL_MASS))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "MaxFuelMass")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.MAX_FUEL_MASS)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.MAX_FUEL_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "MaxFuelMass")

        launch.enable_control_parameter(CONTROL_LAUNCH.RADIATION_PRESSURE_AREA)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.RADIATION_PRESSURE_AREA))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.RadPressureArea")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.RADIATION_PRESSURE_AREA)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.RADIATION_PRESSURE_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.RadPressureArea")

        launch.enable_control_parameter(CONTROL_LAUNCH.SRP_AREA)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.SRP_AREA))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.SRPArea")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.SRP_AREA)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.SRP_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.SRPArea")

        launch.enable_control_parameter(CONTROL_LAUNCH.TANK_PRESSURE)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.TANK_PRESSURE))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.TankPressure")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.TANK_PRESSURE)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.TANK_PRESSURE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.TankPressure")

        launch.enable_control_parameter(CONTROL_LAUNCH.TANK_TEMP)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.TANK_TEMP))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.TankTemperature")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.TANK_TEMP)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.TANK_TEMP))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "InitialState.TankTemperature")

        launch.enable_control_parameter(CONTROL_LAUNCH.TANK_VOLUME)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.TANK_VOLUME))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "TankVolume")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.TANK_VOLUME)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.TANK_VOLUME))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "TankVolume")

        launch.enable_control_parameter(CONTROL_LAUNCH.TIME_OF_FLIGHT)
        Assert.assertTrue(launch.is_control_parameter_enabled(CONTROL_LAUNCH.TIME_OF_FLIGHT))
        cp = dc.control_parameters.get_control_by_paths("myLaunch", "TimeOfFlight")
        Assert.assertEqual(cp.parent_name, "myLaunch")
        GatorHelper.TestDCControlParameter(cp)
        launch.disable_control_parameter(CONTROL_LAUNCH.TIME_OF_FLIGHT)
        Assert.assertFalse(launch.is_control_parameter_enabled(CONTROL_LAUNCH.TIME_OF_FLIGHT))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myLaunch", "TimeOfFlight")
        if not OSHelper.IsLinux():
            scriptingTool: "ScriptingTool" = dc.scripting_tool
            scriptingTool.enable = True
            Assert.assertTrue(scriptingTool.enable)

            GatorHelper.TestScriptingToolSegmentProperties(scriptingTool.segment_properties, "Segments.myProp")

            GatorHelper.TestScriptingToolParameters(scriptingTool.parameters)

            GatorHelper.TestScriptingToolCalcObjects(scriptingTool.calc_objects)

    @staticmethod
    def TestInitialStateControls(initState: "MissionControlSequenceInitialState", dc: "ProfileDifferentialCorrector"):
        Assert.assertTrue(initState.control_parameters_available)

        initState.enable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_VX)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_VX))
        cp: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Cartesian.Vx"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_VX)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_VX))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Vx")

        initState.enable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_VY)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_VY))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Vy")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_VY)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_VY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Vy")

        initState.enable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_VZ)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_VZ))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Vz")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_VZ)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_VZ))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Vz")

        initState.enable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_X)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_X))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.X")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_X)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_X))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.X")

        initState.enable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_Y)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_Y))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Y")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_Y)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_Y))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Y")

        initState.enable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_Z)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_Z))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Z")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CARTESIAN_Z)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CARTESIAN_Z))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cartesian.Z")

        initState.enable_control_parameter(CONTROL_INIT_STATE.CD)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CD))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cd")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CD)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CD))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cd")

        initState.enable_control_parameter(CONTROL_INIT_STATE.CK)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CK))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.RadPressureCoeff")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CK)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CK))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.RadPressureCoeff")

        initState.enable_control_parameter(CONTROL_INIT_STATE.CR)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CR))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cr")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.CR)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.CR))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Cr")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DRAG_AREA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DRAG_AREA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.DragArea")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DRAG_AREA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DRAG_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.DragArea")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DRY_MASS)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DRY_MASS))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.DryMass")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DRY_MASS)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DRY_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.DryMass")

        initState.enable_control_parameter(CONTROL_INIT_STATE.EPOCH)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EPOCH))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Epoch")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.EPOCH)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EPOCH))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Epoch")

        initState.enable_control_parameter(CONTROL_INIT_STATE.FUEL_DENSITY)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.FUEL_DENSITY))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.FuelDensity")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.FUEL_DENSITY)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.FUEL_DENSITY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.FuelDensity")

        initState.enable_control_parameter(CONTROL_INIT_STATE.FUEL_MASS)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.FUEL_MASS))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "FuelMass")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.FUEL_MASS)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.FUEL_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "FuelMass")

        initState.enable_control_parameter(CONTROL_INIT_STATE.K1)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.K1))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.K1")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.K1)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.K1))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.K1")

        initState.enable_control_parameter(CONTROL_INIT_STATE.K2)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.K2))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.K2")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.K2)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.K2))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.K2")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_ECCENTRICITY)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_ECCENTRICITY))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ecc")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_ECCENTRICITY)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_ECCENTRICITY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ecc")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_INC)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_INC))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.inc")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_INC)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_INC))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.inc")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_RAAN)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_RAAN))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.RAAN")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_RAAN)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_RAAN))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.RAAN")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_SMA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_SMA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.sma")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_SMA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_SMA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.sma")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_TA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_TA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.TA")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_TA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_TA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.TA")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_W)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_W))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.w")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_W)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_W))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.w")

        initState.enable_control_parameter(CONTROL_INIT_STATE.MAX_FUEL_MASS)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MAX_FUEL_MASS))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "MaxFuelMass")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.MAX_FUEL_MASS)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MAX_FUEL_MASS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "MaxFuelMass")

        initState.enable_control_parameter(CONTROL_INIT_STATE.RADIATION_PRESSURE_AREA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.RADIATION_PRESSURE_AREA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.RadPressureArea")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.RADIATION_PRESSURE_AREA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.RADIATION_PRESSURE_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.RadPressureArea")

        initState.enable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_AZ)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_AZ))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Azimuth")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_AZ)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_AZ))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Azimuth")

        initState.enable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_DEC)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_DEC))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Decl")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_DEC)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_DEC))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Decl")

        initState.enable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_HORIZ_FPA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_HORIZ_FPA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Horiz_FPA")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_HORIZ_FPA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_HORIZ_FPA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Horiz_FPA")

        initState.enable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_VERTICAL_FPA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_VERTICAL_FPA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Vertical_FPA")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_VERTICAL_FPA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_VERTICAL_FPA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Vertical_FPA")

        initState.enable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_RA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_RA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Right_Asc")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_RA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_RA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.Right_Asc")

        initState.enable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_R_MAGNITUDE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_R_MAGNITUDE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.RMag")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_R_MAGNITUDE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_R_MAGNITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.RMAg")

        initState.enable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_V_MAGNITUDE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_V_MAGNITUDE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.VMag")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.SPHERICAL_V_MAGNITUDE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SPHERICAL_V_MAGNITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Spherical.VMag")

        initState.enable_control_parameter(CONTROL_INIT_STATE.SRP_AREA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SRP_AREA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.SRPArea")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.SRP_AREA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.SRP_AREA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.SRPArea")

        initState.enable_control_parameter(CONTROL_INIT_STATE.TANK_PRESSURE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TANK_PRESSURE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.TankPressure")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TANK_PRESSURE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TANK_PRESSURE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.TankPressure")

        initState.enable_control_parameter(CONTROL_INIT_STATE.TANK_TEMP)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TANK_TEMP))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.TankTemperature")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TANK_TEMP)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TANK_TEMP))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.TankTemperature")

        initState.enable_control_parameter(CONTROL_INIT_STATE.TANK_VOLUME)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TANK_VOLUME))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "TankVolume")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TANK_VOLUME)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TANK_VOLUME))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "TankVolume")

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_ASYMP_DEC)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_ASYMP_DEC))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.AsymDec"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_ASYMP_DEC)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_ASYMP_DEC))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.AsymDec"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_ASYMP_RA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_ASYMP_RA))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.AsymRA"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_ASYMP_RA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_ASYMP_RA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.AsymRA"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_VEL_AZ_AT_PERIAPSIS)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_VEL_AZ_AT_PERIAPSIS))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.AzVp"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_VEL_AZ_AT_PERIAPSIS)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_VEL_AZ_AT_PERIAPSIS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.AzVp"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_C3)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_C3))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.C3"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_C3)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_C3))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.C3"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_RAD_OF_PERIAPSIS)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_RAD_OF_PERIAPSIS))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.rp"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_RAD_OF_PERIAPSIS)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_RAD_OF_PERIAPSIS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.rp"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_TRUE_ANOMALY)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_TRUE_ANOMALY))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.TA"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_IN_TRUE_ANOMALY)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_IN_TRUE_ANOMALY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Incoming_Asymptote.TA"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_ASYMP_DEC)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_ASYMP_DEC))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.AsymDec"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_ASYMP_DEC)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_ASYMP_DEC))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.AsymDec"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_ASYMP_RA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_ASYMP_RA))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.AsymRA"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_ASYMP_RA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_ASYMP_RA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.AsymRA"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_VEL_AZ_AT_PERIAPSIS)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_VEL_AZ_AT_PERIAPSIS))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.AzVp"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_VEL_AZ_AT_PERIAPSIS)
        Assert.assertFalse(
            initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_VEL_AZ_AT_PERIAPSIS)
        )
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.AzVp"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_C3)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_C3))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.C3"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_C3)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_C3))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.C3"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_RAD_OF_PERIAPSIS)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_RAD_OF_PERIAPSIS))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.rp"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_RAD_OF_PERIAPSIS)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_RAD_OF_PERIAPSIS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.rp"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_TRUE_ANOMALY)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_TRUE_ANOMALY))
        cp = dc.control_parameters.get_control_by_paths(
            "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.TA"
        )
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.TARGET_VEC_OUT_TRUE_ANOMALY)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.TARGET_VEC_OUT_TRUE_ANOMALY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths(
                "myInitState", "InitialState.Target_Vector_Outgoing_Asymptote.TA"
            )

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_G)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_G))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.G")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_G)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_G))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.G")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_H)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_H))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.H")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_H)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_H))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.H")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_INC)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_INC))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.inc")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_INC)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_INC))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.inc")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_L)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_L))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.L")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_L)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_L))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.L")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_MEAN_ANOMALY)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_MEAN_ANOMALY))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.MeanAnomaly")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_MEAN_ANOMALY)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_MEAN_ANOMALY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.MeanAnomaly")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_RAAN)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_RAAN))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.RAAN")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_RAAN)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_RAAN))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.RAAN")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_SEMI_LATUS_RECTUM)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_SEMI_LATUS_RECTUM))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.SemiLatusRectum")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_SEMI_LATUS_RECTUM)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_SEMI_LATUS_RECTUM))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.SemiLatusRectum")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_SMA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_SMA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.sma")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_SMA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_SMA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.sma")

        initState.enable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_W)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_W))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.w")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.DELAUNAY_W)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.DELAUNAY_W))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Delaunay.w")

        initState.enable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_H)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_H))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.h")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_H)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_H))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.h")

        initState.enable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_K)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_K))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.k")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_K)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_K))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.k")

        initState.enable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_MEAN_LONGITUDE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_MEAN_LONGITUDE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.MeanLongitude")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_MEAN_LONGITUDE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_MEAN_LONGITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.MeanLongitude")

        initState.enable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_MEAN_MOTION)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_MEAN_MOTION))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.MeanMotion")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_MEAN_MOTION)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_MEAN_MOTION))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.MeanMotion")

        initState.enable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_P)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_P))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.p")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_P)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_P))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.p")

        initState.enable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_Q)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_Q))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.q")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_Q)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_Q))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.q")

        initState.enable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_SMA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_SMA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.sma")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.EQUINOCTIAL_SMA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.EQUINOCTIAL_SMA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Equinoctial.sma")

        initState.enable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_ALTITUDE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_ALTITUDE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Altitude")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_ALTITUDE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_ALTITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Altitude")

        initState.enable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_AZIMUTH)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_AZIMUTH))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Azimuth")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_AZIMUTH)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_AZIMUTH))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Azimuth")

        initState.enable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_HORIZ_FPA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_HORIZ_FPA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Horiz_FPA")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_HORIZ_FPA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_HORIZ_FPA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Horiz_FPA")

        initState.enable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_LATITUDE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_LATITUDE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Latitude")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_LATITUDE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_LATITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Latitude")

        initState.enable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_LONGITUDE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_LONGITUDE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Longitude")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_LONGITUDE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_LONGITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Longitude")

        initState.enable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_VERTICAL_FPA)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_VERTICAL_FPA))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Vertical_FPA")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_VERTICAL_FPA)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_VERTICAL_FPA))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.Vertical_FPA")

        initState.enable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_V_MAGNITUDE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_V_MAGNITUDE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.VMag")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.MIXED_SPHERICAL_V_MAGNITUDE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.MIXED_SPHERICAL_V_MAGNITUDE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Mixed_Spherical.VMag")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_ALTITUDE_SHAPE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_ALTITUDE_SHAPE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ApoapsisAltShape")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_ALTITUDE_SHAPE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_ALTITUDE_SHAPE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ApoapsisAltShape")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_ALTITUDE_SIZE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_ALTITUDE_SIZE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ApoapsisAltSize")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_ALTITUDE_SIZE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_ALTITUDE_SIZE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ApoapsisAltSize")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_RAD_SHAPE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_RAD_SHAPE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ApoapsisRadShape")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_RAD_SHAPE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_RAD_SHAPE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ApoapsisRadShape")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_RAD_SIZE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_RAD_SIZE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ApoapsisRadSize")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_RAD_SIZE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_APOAPSIS_RAD_SIZE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ApoapsisRadSize")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_ARG_LAT)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_ARG_LAT))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ArgLat")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_ARG_LAT)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_ARG_LAT))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.ArgLat")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_ECCENTRICITY_ANOMALY)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_ECCENTRICITY_ANOMALY))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.EccAnomaly")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_ECCENTRICITY_ANOMALY)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_ECCENTRICITY_ANOMALY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.EccAnomaly")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_LAN)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_LAN))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.LAN")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_LAN)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_LAN))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.LAN")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_MEAN_ANOMALY)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_MEAN_ANOMALY))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.MeanAnomaly")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_MEAN_ANOMALY)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_MEAN_ANOMALY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.MeanAnomaly")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_MEAN_MOTION)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_MEAN_MOTION))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.MeanMotion")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_MEAN_MOTION)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_MEAN_MOTION))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.MeanMotion")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_ALTITUDE_SHAPE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_ALTITUDE_SHAPE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.PeriapsisAltShape")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_ALTITUDE_SHAPE)
        Assert.assertFalse(
            initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_ALTITUDE_SHAPE)
        )
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.PeriapsisAltShape")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_ALTITUDE_SIZE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_ALTITUDE_SIZE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.PeriapsisAltSize")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_ALTITUDE_SIZE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_ALTITUDE_SIZE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.PeriapsisAltSize")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_RAD_SHAPE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_RAD_SHAPE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.PeriapsisRadShape")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_RAD_SHAPE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_RAD_SHAPE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.PeriapsisRadShape")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_RAD_SIZE)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_RAD_SIZE))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.PeriapsisRadSize")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_RAD_SIZE)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIAPSIS_RAD_SIZE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.PeriapsisRadSize")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIOD)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIOD))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.Period")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_PERIOD)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_PERIOD))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.Period")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_TIME_PAST_AN)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_TIME_PAST_AN))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.TimePastAN")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_TIME_PAST_AN)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_TIME_PAST_AN))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.TimePastAN")

        initState.enable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_TIME_PAST_PERIAPSIS)
        Assert.assertTrue(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_TIME_PAST_PERIAPSIS))
        cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.TimePastPeriapsis")
        Assert.assertEqual(cp.parent_name, "myInitState")
        GatorHelper.TestDCControlParameter(cp)
        initState.disable_control_parameter(CONTROL_INIT_STATE.KEPLERIAN_TIME_PAST_PERIAPSIS)
        Assert.assertFalse(initState.is_control_parameter_enabled(CONTROL_INIT_STATE.KEPLERIAN_TIME_PAST_PERIAPSIS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("myInitState", "InitialState.Keplerian.TimePastPeriapsis")

    @staticmethod
    def TestManeuverControls(
        maneuver: "MissionControlSequenceManeuver",
        dc: "ProfileDifferentialCorrector",
        ts: "MissionControlSequenceTargetSequence",
    ):
        Assert.assertTrue(maneuver.control_parameters_available)
        maneuver.set_maneuver_type(MANEUVER_TYPE.FINITE)
        finite: "ManeuverFinite" = clr.CastAs(maneuver.maneuver, ManeuverFinite)

        GatorHelper.TestRuntimeTypeInfo(finite)

        finite.propagator.enable_center_burn = True
        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS))
        cp: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths(
            "TMan", "FiniteMnvr.BurnCenterBias"
        )
        Assert.assertEqual(cp.parent_name, "TMan")
        # TestDCControlParameter(cp);

        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.BurnCenterBias")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_THRUST_EFFICIENCY)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_THRUST_EFFICIENCY))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.ThrustEfficiency")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_THRUST_EFFICIENCY)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_THRUST_EFFICIENCY))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.ThrustEfficiency")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_CARTESIAN_X)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_CARTESIAN_X))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Cartesian.X")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_CARTESIAN_X)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_CARTESIAN_X))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Cartesian.X")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_CARTESIAN_Y)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_CARTESIAN_Y))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Cartesian.Y")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_CARTESIAN_Y)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_CARTESIAN_Y))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Cartesian.Y")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_CARTESIAN_Z)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_CARTESIAN_Z))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Cartesian.Z")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_CARTESIAN_Z)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_CARTESIAN_Z))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Cartesian.Z")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EULER_ANGLES1)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EULER_ANGLES1))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.EulerAngles.Angle1")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EULER_ANGLES1)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EULER_ANGLES1))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.EulerAngles.Angle1")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EULER_ANGLES2)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EULER_ANGLES2))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.EulerAngles.Angle2")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EULER_ANGLES2)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EULER_ANGLES2))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.EulerAngles.Angle2")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EULER_ANGLES3)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EULER_ANGLES3))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.EulerAngles.Angle3")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EULER_ANGLES3)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EULER_ANGLES3))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.EulerAngles.Angle3")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_SPHERICAL_AZ)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_SPHERICAL_AZ))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Spherical.Azimuth")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_SPHERICAL_AZ)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_SPHERICAL_AZ))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Spherical.Azimuth")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_SPHERICAL_ELEV)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_SPHERICAL_ELEV))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Spherical.Elevation")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_SPHERICAL_ELEV)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_SPHERICAL_ELEV))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.Spherical.Elevation")

        sc: "StoppingConditionElement" = finite.propagator.stopping_conditions[0]
        sc.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        Assert.assertTrue(sc.is_control_parameter_enabled(CONTROL_STOPPING_CONDITION.TRIP_VALUE))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.StoppingConditions.Duration.TripValue")
        Assert.assertEqual("TMan", cp.parent_name)
        GatorHelper.TestDCControlParameter(cp)
        sc.disable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        Assert.assertFalse(sc.is_control_parameter_enabled(CONTROL_STOPPING_CONDITION.TRIP_VALUE))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.StoppingConditions.Duration.TripValue")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_AZ0)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ0))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az0")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_AZ0)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ0))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az0")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_AZ1)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ1))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az1")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_AZ1)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ1))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az1")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_AZ2)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ2))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az2")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_AZ2)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ2))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az2")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_AZ3)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ3))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az3")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_AZ3)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ3))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az3")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_AZ4)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ4))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az4")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_AZ4)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ4))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.Az4")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_AZ_A)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ_A))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.AzA")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_AZ_A)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ_A))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.AzA")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_AZ_F)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ_F))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.AzF")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_AZ_F)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ_F))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.AzF")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_AZ_P)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ_P))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.AzP")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_AZ_P)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_AZ_P))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.AzP")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EL0)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL0))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El0")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EL0)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL0))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El0")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EL1)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL1))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El1")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EL1)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL1))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El1")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EL2)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL2))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El2")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EL2)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL2))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El2")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EL3)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL3))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El3")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EL3)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL3))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El3")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EL4)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL4))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El4")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EL4)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL4))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.El4")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EL_A)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL_A))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.ElA")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EL_A)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL_A))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.ElA")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EL_F)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL_F))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.ElF")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EL_F)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL_F))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.ElF")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_EL_P)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL_P))
        cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.ElP")
        Assert.assertEqual(cp.parent_name, "TMan")
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_EL_P)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.FINITE_EL_P))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "FiniteMnvr.TimeVarying.ElP")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X))
        cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.Cartesian.X")
        Assert.assertEqual("TMan", cp.parent_name)
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.Cartesian.X")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_Y)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_Y))
        cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.Cartesian.Y")
        Assert.assertEqual("TMan", cp.parent_name)
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_Y)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_Y))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.Cartesian.Y")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_Z)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_Z))
        cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.Cartesian.Z")
        Assert.assertEqual("TMan", cp.parent_name)
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_Z)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_Z))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.Cartesian.Z")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES1)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES1))
        cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.EulerAngles.Angle1")
        Assert.assertEqual("TMan", cp.parent_name)
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES1)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES1))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.EulerAngles.Angle1")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES2)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES2))
        cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.EulerAngles.Angle2")
        Assert.assertEqual("TMan", cp.parent_name)
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES2)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES2))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.EulerAngles.Angle2")

        maneuver.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES3)
        Assert.assertTrue(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES3))
        cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.EulerAngles.Angle3")
        Assert.assertEqual("TMan", cp.parent_name)
        GatorHelper.TestDCControlParameter(cp)
        maneuver.disable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES3)
        Assert.assertFalse(maneuver.is_control_parameter_enabled(CONTROL_MANEUVER.IMPULSIVE_EULER_ANGLES3))
        with pytest.raises(Exception):
            cp = dc.control_parameters.get_control_by_paths("TMan", "ImpulsiveMnvr.EulerAngles.Angle3")

    @staticmethod
    def TestTargetSequence(ts: "MissionControlSequenceTargetSequence", isFromCM: bool, root: "StkObjectRoot"):
        segment: "IMissionControlSequenceSegment" = clr.CastAs(ts, IMissionControlSequenceSegment)
        Assert.assertEqual(SEGMENT_TYPE.TARGET_SEQUENCE, segment.type)

        ts.action = TARGET_SEQ_ACTION.RUN_NOMINAL_SEQ
        Assert.assertEqual(TARGET_SEQ_ACTION.RUN_NOMINAL_SEQ, ts.action)

        with pytest.raises(Exception):
            ts.when_profiles_finish = PROFILES_FINISH.RUN_TO_RETURN_AND_STOP

        ts.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        Assert.assertEqual(TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES, ts.action)
        ts.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES_ONCE
        Assert.assertEqual(TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES_ONCE, ts.action)

        ts.when_profiles_finish = PROFILES_FINISH.RUN_TO_RETURN_AND_STOP
        Assert.assertEqual(PROFILES_FINISH.RUN_TO_RETURN_AND_STOP, ts.when_profiles_finish)
        ts.when_profiles_finish = PROFILES_FINISH.STOP
        Assert.assertEqual(PROFILES_FINISH.STOP, ts.when_profiles_finish)
        ts.when_profiles_finish = PROFILES_FINISH.RUN_TO_RETURN_AND_CONTINUE
        Assert.assertEqual(PROFILES_FINISH.RUN_TO_RETURN_AND_CONTINUE, ts.when_profiles_finish)

        ts.continue_on_failure = True
        Assert.assertTrue(ts.continue_on_failure)
        ts.continue_on_failure = False
        Assert.assertFalse(ts.continue_on_failure)

        ts.reset_inner_targeters = True  # not sure how to test functionality in an solely OM manner
        Assert.assertTrue(ts.reset_inner_targeters)
        ts.reset_inner_targeters = False
        Assert.assertFalse(ts.reset_inner_targeters)

        GatorHelper.TestRuntimeTypeInfo(ts.profiles)

        profile: "IProfile"

        for profile in ts.profiles:
            name: str = profile.name

        ts.reset_profiles()

        maneuver: "MissionControlSequenceManeuver" = MissionControlSequenceManeuver(
            ts.segments.insert(SEGMENT_TYPE.MANEUVER, "TMan", "-")
        )
        initState: "MissionControlSequenceInitialState" = MissionControlSequenceInitialState(
            ts.segments.insert(SEGMENT_TYPE.INITIAL_STATE, "myInitState", "-")
        )
        launch: "MissionControlSequenceLaunch" = MissionControlSequenceLaunch(
            ts.segments.insert(SEGMENT_TYPE.LAUNCH, "myLaunch", "-")
        )
        follow: "MissionControlSequenceFollow" = MissionControlSequenceFollow(
            ts.segments.insert(SEGMENT_TYPE.FOLLOW, "myFollow", "-")
        )
        prop: "MissionControlSequencePropagate" = MissionControlSequencePropagate(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "myProp", "-")
        )
        update: "MissionControlSequenceUpdate" = MissionControlSequenceUpdate(
            ts.segments.insert(SEGMENT_TYPE.UPDATE, "myUpdate", "-")
        )
        if not isFromCM:
            # PLUGINSTUFF
            #            #                string sSourceFile = TestBase.GetScenarioFile( @"Plugins\Search.xml");            #                if (!File.Exists(sSourceFile))            #                    Assert.Fail("File does not exist: " + sSourceFile);            #                string sDestFile = Path.Combine(TestBase.GetSTKHomeDir(), @"Plugins\Search.xml");            #                if (!File.Exists(sDestFile))            #                    Assert.Fail("File does not exist: " + sDestFile);            #                string sPluginFile = TestBase.GetScenarioFile( @"Plugins\Agi.Search.Plugin.CSharp.Examples.dll");            #                if (!File.Exists(sPluginFile))            #                    Assert.Fail("File does not exist: " + sPluginFile);            #

            profile: str
            # PLUGINSTUFF
            #            #                string sSourceFile = TestBase.GetScenarioFile( @"Plugins\Search.xml");            #                if (!File.Exists(sSourceFile))            #                    Assert.Fail("File does not exist: " + sSourceFile);            #                string sDestFile = Path.Combine(TestBase.GetSTKHomeDir(), @"Plugins\Search.xml");            #                if (!File.Exists(sDestFile))            #                    Assert.Fail("File does not exist: " + sDestFile);            #                string sPluginFile = TestBase.GetScenarioFile( @"Plugins\Agi.Search.Plugin.CSharp.Examples.dll");            #                if (!File.Exists(sPluginFile))            #                    Assert.Fail("File does not exist: " + sPluginFile);            #

            for profile in ts.profiles.available_profiles:
                if profile == "Change Maneuver Type":
                    GatorHelper.TestProfileChangeManeuverType(ts.profiles.add(profile), maneuver, ts)

                elif profile == "Change Stopping Condition State":
                    hold: "MissionControlSequenceHold" = MissionControlSequenceHold(
                        ts.segments.insert(SEGMENT_TYPE.HOLD, "holdts", "-")
                    )
                    GatorHelper.TestProfileChangeStoppingConditionState(
                        ts.profiles.add(profile),
                        IMissionControlSequenceSegment(maneuver),
                        hold.stopping_conditions[0],
                        ts,
                    )

                elif profile == "Change Return Segment":
                    returnSeg: "MissionControlSequenceReturn" = MissionControlSequenceReturn(
                        ts.segments.insert(SEGMENT_TYPE.RETURN, "myReturn", "-")
                    )
                    GatorHelper.TestProfileChangeReturnSegment(ts.profiles.add(profile), returnSeg, ts)

                elif profile == "Change Stop Segment":
                    stopSeg: "MissionControlSequenceStop" = MissionControlSequenceStop(
                        ts.segments.insert(SEGMENT_TYPE.STOP, "myStop", "-")
                    )
                    GatorHelper.TestProfileChangeStopSegment(ts.profiles.add(profile), stopSeg, ts)

                elif profile == "Seed Finite Maneuver":
                    GatorHelper.TestProfileSeedFiniteManeuver(ts.profiles.add(profile), maneuver, ts)

                elif profile == "Run Target Sequence Once":
                    GatorHelper.TestProfileRunOnce(ts.profiles.add(profile))

                elif profile == "Differential Corrector":
                    GatorHelper.TestProfileDifferentialCorrector(ts.profiles[profile], ts)

                elif profile == "Scripting Tool":
                    GatorHelper.TestProfileScriptingTool(ts.profiles.add(profile), ts)

                elif profile == "Change Propagator":
                    GatorHelper.TestProfileChangePropagator(ts.profiles.add(profile), maneuver)

                elif profile == "CSharp Bisection":
                    GatorHelper.TestPlugin_Bisection(ts.profiles.add(profile), ts)

                elif profile == "JSharp Bisection":
                    GatorHelper.TestPlugin_Bisection(ts.profiles.add(profile), ts)

                elif profile == "SNOPT Optimizer":
                    GatorHelper.TestProfileSNOPTOptimizer(ts.profiles.add(profile), ts)

                elif profile == "IPOPT Optimizer":
                    GatorHelper.TestProfileIPOPTOptimizer(ts.profiles.add(profile), ts)

                elif profile == "Lambert Profile":
                    GatorHelper.TestProfileLambertProfile(ts.profiles.add(profile), ts)

                elif profile == "Lambert Search Profile":
                    GatorHelper.TestProfileLambertSearchProfile(ts.profiles.add(profile), ts)

                elif profile == "Golden Section Search":
                    GatorHelper.TestProfileGoldenSection(ts.profiles.add(profile), ts, root)

                elif profile == "One Dimensional Grid Search":
                    GatorHelper.TestProfileGridSearch(ts.profiles.add(profile), ts, root)

                elif profile == "Single Parameter Bisection":
                    GatorHelper.TestProfileBisection(ts.profiles.add(profile), ts, root)

                else:
                    Console.WriteLine("*** The {0} profile does not have an a test created for it.", profile)

            count: int = ts.profiles.count

            i: int = 0
            while i < count:
                profile: "IProfile" = ts.profiles[i]
                name: str = profile.name

                i += 1

            profile2: "IProfile" = ts.profiles["Differential Corrector"]

            with pytest.raises(Exception):
                profile3: "IProfile" = ts.profiles[count]

            with pytest.raises(Exception):
                profile4: "IProfile" = ts.profiles["Bogus"]

            ts.profiles.remove(0)
            Assert.assertEqual((count - 1), ts.profiles.count)

            ts.profiles.remove_all()
            Assert.assertEqual(0, ts.profiles.count)

            with pytest.raises(Exception):
                ts.profiles.remove(0)

            with pytest.raises(Exception):
                ts.profiles.remove("Bogus")

    @staticmethod
    def TestSNOPTResult(eq: "SNOPTResult"):
        currentValue: typing.Any = eq.current_value
        Assert.assertEqual("-Not Set-", eq.current_value)

        name: str = eq.name
        Assert.assertEqual("Epoch", eq.name)

        parentName: str = eq.parent_name
        Assert.assertEqual("TMan", eq.parent_name)

        eq.enable = False
        Assert.assertFalse(eq.enable)
        eq.enable = True
        Assert.assertTrue(eq.enable)

        eq.goal = SNOPT_GOAL.MINIMIZE
        Assert.assertEqual(SNOPT_GOAL.MINIMIZE, eq.goal)

        eq.weight = 1.0
        Assert.assertEqual(1.0, eq.weight)
        eq.weight = 2.0
        Assert.assertEqual(2.0, eq.weight)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            eq.lower_bound = "1 Jul 2000 00:00:00.000"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            eq.upper_bound = "2 Jul 2000 00:00:00.000"

        eq.goal = SNOPT_GOAL.BOUND
        Assert.assertEqual(SNOPT_GOAL.BOUND, eq.goal)

        eq.lower_bound = "1 Jul 2000 00:00:00.000"
        Assert.assertEqual("1 Jul 2000 00:00:00.000", eq.lower_bound)
        eq.lower_bound = "1 Jul 1999 00:00:00.000"
        Assert.assertEqual("1 Jul 1999 00:00:00.000", eq.lower_bound)

        eq.upper_bound = "30 Jun 1999 23:59:58.000"
        Assert.assertEqual("30 Jun 1999 23:59:58.000", eq.upper_bound)
        eq.upper_bound = "30 Jun 2099 23:59:58.000"
        Assert.assertEqual("30 Jun 2099 23:59:58.000", eq.upper_bound)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eq.weight = 1.0

        eq.scaling_value = 0.01
        Assert.assertEqual(0.01, eq.scaling_value)
        eq.scaling_value = 0.001
        Assert.assertEqual(0.001, eq.scaling_value)

        eq.use_custom_display_unit = False
        Assert.assertFalse(eq.use_custom_display_unit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eq.custom_display_unit = "JDate"

        eq.use_custom_display_unit = True
        Assert.assertTrue(eq.use_custom_display_unit)

        eq.custom_display_unit = "JDate"
        Assert.assertEqual("JDate", eq.custom_display_unit)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid Unit")):
            eq.custom_display_unit = "m"

    @staticmethod
    def TestIPOPTResult(eq: "IPOPTResult"):
        currentValue: typing.Any = eq.current_value
        Assert.assertEqual("-Not Set-", eq.current_value)

        name: str = eq.name
        Assert.assertEqual("Epoch", eq.name)

        parentName: str = eq.parent_name
        Assert.assertEqual("TMan", eq.parent_name)

        eq.enable = False
        Assert.assertFalse(eq.enable)
        eq.enable = True
        Assert.assertTrue(eq.enable)

        eq.goal = IPOPT_GOAL.MINIMIZE
        Assert.assertEqual(IPOPT_GOAL.MINIMIZE, eq.goal)

        eq.weight = 1.0
        Assert.assertEqual(1.0, eq.weight)
        eq.weight = 2.0
        Assert.assertEqual(2.0, eq.weight)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            eq.lower_bound = "1 Jul 2000 00:00:00.000"
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            eq.upper_bound = "2 Jul 2000 00:00:00.000"

        eq.goal = IPOPT_GOAL.BOUND
        Assert.assertEqual(IPOPT_GOAL.BOUND, eq.goal)

        eq.lower_bound = "1 Jul 2000 00:00:00.000"
        Assert.assertEqual("1 Jul 2000 00:00:00.000", eq.lower_bound)
        eq.lower_bound = "1 Jul 1999 00:00:00.000"
        Assert.assertEqual("1 Jul 1999 00:00:00.000", eq.lower_bound)

        eq.upper_bound = "30 Jun 1999 23:59:58.000"
        Assert.assertEqual("30 Jun 1999 23:59:58.000", eq.upper_bound)
        eq.upper_bound = "30 Jun 2099 23:59:58.000"
        Assert.assertEqual("30 Jun 2099 23:59:58.000", eq.upper_bound)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eq.weight = 1.0

        eq.scaling_value = 0.01
        Assert.assertEqual(0.01, eq.scaling_value)
        eq.scaling_value = 0.001
        Assert.assertEqual(0.001, eq.scaling_value)

        eq.use_custom_display_unit = False
        Assert.assertFalse(eq.use_custom_display_unit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eq.custom_display_unit = "JDate"

        eq.use_custom_display_unit = True
        Assert.assertTrue(eq.use_custom_display_unit)

        eq.custom_display_unit = "JDate"
        Assert.assertEqual("JDate", eq.custom_display_unit)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid Unit")):
            eq.custom_display_unit = "m"

    @staticmethod
    def TestBisectionResult(eq: "BisectionResult"):
        currentValue: typing.Any = eq.current_value
        Assert.assertEqual("-Not Set-", eq.current_value)

        name: str = eq.name
        Assert.assertEqual("Epoch", eq.name)

        parentName: str = eq.parent_name
        Assert.assertEqual("TMan", eq.parent_name)

        eq.enable = False
        Assert.assertFalse(eq.enable)
        eq.enable = True
        Assert.assertTrue(eq.enable)

        eq.desired_value = "2 Jul 1999 00:00:00.000"
        Assert.assertEqual("2 Jul 1999 00:00:00.000", eq.desired_value)

        eq.tolerance = 0.02
        Assert.assertEqual(0.02, eq.tolerance)

        eq.use_custom_display_unit = False
        Assert.assertFalse(eq.use_custom_display_unit)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eq.custom_display_unit = "JDate"

        eq.use_custom_display_unit = True
        Assert.assertTrue(eq.use_custom_display_unit)

        eq.custom_display_unit = "JDate"
        Assert.assertEqual("JDate", eq.custom_display_unit)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid Unit")):
            eq.custom_display_unit = "m"

    @staticmethod
    def Test_IAgVAProfile(ts: "MissionControlSequenceTargetSequence", profile: "IProfile", mode: "PROFILE_MODE"):
        newProfile: "IProfile" = profile.copy()
        newProfile.mode = mode
        mode1: "PROFILE_MODE" = newProfile.mode
        Assert.assertEqual(mode, mode1)
        newProfile.name = "MyTestProfile"
        Assert.assertEqual("MyTestProfile", newProfile.name)
        status: str = newProfile.status
        newProfile.user_comment = "My User Comment"
        Assert.assertEqual("My User Comment", newProfile.user_comment)
        eType: "PROFILE" = profile.type
        Assert.assertEqual(profile.type, newProfile.type)

        ts.profiles.remove("MyTestProfile")

    @staticmethod
    def Test_IAgVASearchPluginControl(searchPluginControl: "SearchPluginControl", pluginID: str):
        Assert.assertEqual("StoppingConditions.Duration.TripValue", searchPluginControl.control_name)

        Assert.assertEqual(43200.0, float(searchPluginControl.current_value))
        searchPluginControl.current_value = 40000
        Assert.assertEqual(40000.0, float(searchPluginControl.current_value))
        searchPluginControl.current_value = 43200.0
        Assert.assertEqual(43200.0, float(searchPluginControl.current_value))

        searchPluginControl.use_custom_display_unit = True
        Assert.assertTrue(searchPluginControl.use_custom_display_unit)
        searchPluginControl.custom_display_unit = "min"
        Assert.assertEqual("min", searchPluginControl.custom_display_unit)

        searchPluginControl.use_custom_display_unit = False
        Assert.assertFalse(searchPluginControl.use_custom_display_unit)
        with pytest.raises(Exception):
            searchPluginControl.custom_display_unit = "hr"

        searchPluginControl.use_custom_display_unit = True
        Assert.assertTrue(searchPluginControl.use_custom_display_unit)
        searchPluginControl.custom_display_unit = "hr"
        Assert.assertEqual("hr", searchPluginControl.custom_display_unit)

        Assert.assertEqual("TimeUnit", searchPluginControl.dimension)

        Assert.assertEqual(43200.0, float(searchPluginControl.initial_value))

        Assert.assertEqual("myProp", searchPluginControl.parent_segment_name)

        pluginPropertiesX: "PluginProperties" = searchPluginControl.plugin_config
        # TODO See TST95871

        Assert.assertEqual(pluginID, searchPluginControl.plugin_identifier)
        Assert.assertEqual(0, Array.Length(searchPluginControl.values))

    @staticmethod
    def TestPlugin_Bisection(iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence"):
        GatorHelper.m_logger.WriteLine("TestPlugin_Bisection - START")

        # Enable a control and add a Result
        propSeg: "MissionControlSequencePropagate" = MissionControlSequencePropagate(ts.segments["myProp"])
        durationControl: "StoppingConditionElement" = propSeg.stopping_conditions["Duration"]
        durationControl.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        seg: "IMissionControlSequenceSegment" = clr.CastAs(propSeg, IMissionControlSequenceSegment)
        seg.results.add("Epoch")

        profileSearchPlugin: "ProfileSearchPlugin" = clr.CastAs(iAgVAProfile, ProfileSearchPlugin)

        GatorHelper.TestRuntimeTypeInfo(profileSearchPlugin)

        Assert.assertEqual(iAgVAProfile.type, PROFILE.SEARCH_PLUGIN)
        controlCollection: "SearchPluginControlCollection" = profileSearchPlugin.controls

        with pytest.raises(Exception, match=RegexSubstringMatch("could not be found")):
            control: "SearchPluginControl" = controlCollection.get_control_by_paths("myProp", "BogusControlPath")

        count: int = controlCollection.count

        i: int = 0
        while i < count:
            control: "SearchPluginControl" = controlCollection[i]
            GatorHelper.Test_IAgVASearchPluginControl(
                control, "AGI.SearchControlReal.Plugin.Examples.CSharp.BisectionControlReal"
            )

            i += 1

        with pytest.raises(Exception, match=RegexSubstringMatch("Index Out of Range")):
            spc: "SearchPluginControl" = controlCollection[5]

        searchPluginControl: "SearchPluginControl"

        for searchPluginControl in controlCollection:
            GatorHelper.Test_IAgVASearchPluginControl(
                searchPluginControl, "AGI.SearchControlReal.Plugin.Examples.CSharp.BisectionControlReal"
            )

        (profileSearchPlugin).mode = PROFILE_MODE.ITERATE
        Assert.assertEqual(PROFILE_MODE.ITERATE, profileSearchPlugin.mode)

        profileSearchPlugin.name = "MyCSharpBisection"
        Assert.assertEqual("MyCSharpBisection", profileSearchPlugin.name)

        pluginProperties: "PluginProperties" = profileSearchPlugin.plugin_config
        availableProperties = pluginProperties.available_properties
        Assert.assertEqual("PluginName", availableProperties[0])
        Assert.assertEqual("MaxIterations", availableProperties[1])

        pluginProperties.set_property("MaxIterations", 99)
        Assert.assertEqual(99, int(pluginProperties.get_property("MaxIterations")))

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pluginProperties.set_property("PluginName", "NewName")
        with pytest.raises(Exception, match=RegexSubstringMatch("Undefined symbol")):
            pluginProperties.set_property("BogusProperty", "DummyValue")
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pluginProperties.set_property("PluginName", 123)
        pluginIdentifier: str = profileSearchPlugin.plugin_identifier

        pluginResultsCollection: "SearchPluginResultCollection" = profileSearchPlugin.results
        count = pluginResultsCollection.count

        i: int = 0
        while i < count:
            result: "SearchPluginResult" = pluginResultsCollection[0]

            result.use_custom_display_unit = True
            Assert.assertTrue(result.use_custom_display_unit)
            result.use_custom_display_unit = False
            Assert.assertFalse(result.use_custom_display_unit)
            with pytest.raises(Exception):
                result.custom_display_unit = "hr"
            result.use_custom_display_unit = True
            result.custom_display_unit = "EpSec"
            Assert.assertEqual("EpSec", result.custom_display_unit)

            i += 1

        with pytest.raises(Exception):
            result2: "SearchPluginResult" = pluginResultsCollection[5]

        result: "SearchPluginResult"

        for result in pluginResultsCollection:
            sResultName: str = result.result_name
            Assert.assertEqual("Epoch", sResultName)
            currentValue: typing.Any = result.current_value
            Assert.assertEqual("-Not Set-", result.current_value)
            dimension: str = result.dimension
            Assert.assertEqual("DateFormat", result.dimension)
            parentSegmentName: str = result.parent_segment_name
            Assert.assertEqual("myProp", result.parent_segment_name)
            pluginPropertiesX: "PluginProperties" = result.plugin_config
            pluginIdentifierX: str = result.plugin_identifier
            Assert.assertEqual("AGI.SearchResult.Plugin.Examples.CSharp.BisectionResult", result.plugin_identifier)
            Assert.assertEqual(0, Array.Length(result.values))

        with pytest.raises(Exception):
            pluginResult: "SearchPluginResult" = pluginResultsCollection.get_result_by_paths("ObjectPath", "ResultPath")
        if not OSHelper.IsLinux():
            scriptingTool: "ScriptingTool" = profileSearchPlugin.scripting_tool

        status: str = profileSearchPlugin.status

        profileSearchPlugin.reset_controls_before_run = True
        Assert.assertTrue(profileSearchPlugin.reset_controls_before_run)
        profileSearchPlugin.reset_controls_before_run = False
        Assert.assertFalse(profileSearchPlugin.reset_controls_before_run)

        profileSearchPlugin.user_comment = "MyUserComment"
        Assert.assertEqual("MyUserComment", profileSearchPlugin.user_comment)

        spCopy: "ProfileSearchPlugin" = ProfileSearchPlugin(profileSearchPlugin.copy())

        seg.results.remove("Epoch")
        durationControl.disable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)

        GatorHelper.m_logger.WriteLine("TestPlugin_Bisection - END")

    @staticmethod
    def TestProfileSNOPTOptimizer(iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence"):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.SNOPT_OPTIMIZER)
        optimizer: "ProfileSNOPTOptimizer" = clr.CastAs(iAgVAProfile, ProfileSNOPTOptimizer)
        GatorHelper.Test_IAgVAProfile(ts, optimizer, PROFILE_MODE.ITERATE)
        GatorHelper.TestRuntimeTypeInfo(optimizer)

        loop: "SNOPTControl"

        for loop in optimizer.control_parameters:
            name1: str = loop.name

        i: int = 0
        while i < optimizer.control_parameters.count:
            name2: str = optimizer.control_parameters[i].name

            i += 1

        with pytest.raises(Exception):
            name3: str = optimizer.control_parameters[-1].name
        if not OSHelper.IsLinux():
            scriptingTool: "ScriptingTool" = optimizer.scripting_tool
            scriptingTool.enable = True
            Assert.assertTrue(scriptingTool.enable)

            GatorHelper.TestScriptingToolSegmentProperties(scriptingTool.segment_properties, "Segments.myProp")

            GatorHelper.TestScriptingToolParameters(scriptingTool.parameters)

            GatorHelper.TestScriptingToolCalcObjects(scriptingTool.calc_objects)

            scriptingTool.language_type = LANGUAGE.J_SCRIPT
            Assert.assertEqual(LANGUAGE.J_SCRIPT, scriptingTool.language_type)
            scriptingTool.script_text("int j = 1;")

        maneuver: "MissionControlSequenceManeuver" = clr.CastAs(ts.segments["TMan"], MissionControlSequenceManeuver)
        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)

        objName: str = "TMan"
        decName: str = "FiniteMnvr.BurnCenterBias"
        dec1: "SNOPTControl" = None
        dec1 = optimizer.control_parameters.get_control_by_paths(objName, decName)
        GatorHelper.TestSNOPTControlParameter(dec1, objName, decName)

        with pytest.raises(Exception):
            decX: "SNOPTControl" = optimizer.control_parameters.get_control_by_paths(objName, "Bogus")
        with pytest.raises(Exception):
            decY: "SNOPTControl" = optimizer.control_parameters.get_control_by_paths("Bogus", decName)

        dec2: "SNOPTControl" = None
        dec2 = optimizer.control_parameters[0]
        GatorHelper.TestSNOPTControlParameter(dec2, objName, decName)

        with pytest.raises(Exception):
            eq2: "SNOPTResult" = optimizer.results.get_result_by_paths("TMan", "ResultPath")
        with pytest.raises(Exception):
            eq2: "SNOPTResult" = optimizer.results.get_result_by_paths("ObjectPath", "Epoch")

        manSegment: "IMissionControlSequenceSegment" = clr.CastAs(maneuver, IMissionControlSequenceSegment)
        manSegment.results.add("Epoch")
        eq: "SNOPTResult" = optimizer.results.get_result_by_paths("TMan", "Epoch")

        GatorHelper.TestSNOPTResult(eq)

        i: int = 0
        while i < optimizer.results.count:
            result: "SNOPTResult" = optimizer.results[i]
            GatorHelper.m_logger.WriteLine(result.name)

            i += 1

        with pytest.raises(Exception):
            result: "SNOPTResult" = optimizer.results[10]

        result: "SNOPTResult"

        for result in optimizer.results:
            GatorHelper.m_logger.WriteLine(result.name)

        GatorHelper.TestSNOPTTargeterGraphs(optimizer.targeter_graphs)

        optimizer.reset_controls_before_run = False
        Assert.assertFalse(optimizer.reset_controls_before_run)
        optimizer.reset_controls_before_run = True
        Assert.assertTrue(optimizer.reset_controls_before_run)

        optimizer.max_major_iterations = 100
        Assert.assertEqual(100, optimizer.max_major_iterations)
        with pytest.raises(Exception):
            optimizer.max_major_iterations = -1

        optimizer.tolerance_on_major_feasibility = 1
        Assert.assertEqual(1, optimizer.tolerance_on_major_feasibility)

        optimizer.tolerance_on_major_optimality = 2
        Assert.assertEqual(2, optimizer.tolerance_on_major_optimality)

        optimizer.max_minor_iterations = 200
        Assert.assertEqual(200, optimizer.max_minor_iterations)
        with pytest.raises(Exception):
            optimizer.max_minor_iterations = -1

        optimizer.tolerance_on_minor_feasibility = 3
        Assert.assertEqual(3, optimizer.tolerance_on_minor_feasibility)

        optimizer.tolerance_on_minor_optimality = 4
        Assert.assertEqual(4, optimizer.tolerance_on_minor_optimality)

        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            optimizer.options_filename = r"C:\Pat\bogus.txt"
        optimizer.options_filename = TestBase.GetScenarioFile("gp_marker.bmp")
        Assert.assertTrue(("gp_marker.bmp" in optimizer.options_filename))

        optimizer.allow_internal_primal_infeasibility_measure_normalization = False
        Assert.assertFalse(optimizer.allow_internal_primal_infeasibility_measure_normalization)
        optimizer.allow_internal_primal_infeasibility_measure_normalization = True
        Assert.assertTrue(optimizer.allow_internal_primal_infeasibility_measure_normalization)

        spCopy: "ProfileSNOPTOptimizer" = ProfileSNOPTOptimizer(optimizer.copy())

        manSegment.results.remove("Epoch")
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)

    @staticmethod
    def TestProfileIPOPTOptimizer(iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence"):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.IPOPT_OPTIMIZER)
        optimizer: "ProfileIPOPTOptimizer" = clr.CastAs(iAgVAProfile, ProfileIPOPTOptimizer)
        GatorHelper.Test_IAgVAProfile(ts, optimizer, PROFILE_MODE.ITERATE)
        GatorHelper.TestRuntimeTypeInfo(optimizer)

        loop: "IPOPTControl"

        for loop in optimizer.control_parameters:
            name1: str = loop.name

        i: int = 0
        while i < optimizer.control_parameters.count:
            name2: str = optimizer.control_parameters[i].name

            i += 1

        with pytest.raises(Exception):
            name3: str = optimizer.control_parameters[-1].name
        if not OSHelper.IsLinux():
            scriptingTool: "ScriptingTool" = optimizer.scripting_tool
            scriptingTool.enable = True
            Assert.assertTrue(scriptingTool.enable)

            GatorHelper.TestScriptingToolSegmentProperties(scriptingTool.segment_properties, "Segments.myProp")

            GatorHelper.TestScriptingToolParameters(scriptingTool.parameters)

            GatorHelper.TestScriptingToolCalcObjects(scriptingTool.calc_objects)

            scriptingTool.language_type = LANGUAGE.J_SCRIPT
            Assert.assertEqual(LANGUAGE.J_SCRIPT, scriptingTool.language_type)
            scriptingTool.script_text("int j = 1;")

        maneuver: "MissionControlSequenceManeuver" = clr.CastAs(ts.segments["TMan"], MissionControlSequenceManeuver)
        maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)

        objName: str = "TMan"
        decName: str = "FiniteMnvr.BurnCenterBias"
        dec1: "IPOPTControl" = None
        dec1 = optimizer.control_parameters.get_control_by_paths(objName, decName)
        GatorHelper.TestIPOPTControlParameter(dec1, objName, decName)

        with pytest.raises(Exception):
            decX: "IPOPTControl" = optimizer.control_parameters.get_control_by_paths(objName, "Bogus")
        with pytest.raises(Exception):
            decY: "IPOPTControl" = optimizer.control_parameters.get_control_by_paths("Bogus", decName)

        dec2: "IPOPTControl" = None
        dec2 = optimizer.control_parameters[0]
        GatorHelper.TestIPOPTControlParameter(dec2, objName, decName)

        with pytest.raises(Exception):
            eq2: "IPOPTResult" = optimizer.results.get_result_by_paths("TMan", "ResultPath")
        with pytest.raises(Exception):
            eq2: "IPOPTResult" = optimizer.results.get_result_by_paths("ObjectPath", "Epoch")

        manSegment: "IMissionControlSequenceSegment" = clr.CastAs(maneuver, IMissionControlSequenceSegment)
        manSegment.results.add("Epoch")
        eq: "IPOPTResult" = optimizer.results.get_result_by_paths("TMan", "Epoch")

        GatorHelper.TestIPOPTResult(eq)

        i: int = 0
        while i < optimizer.results.count:
            result: "IPOPTResult" = optimizer.results[i]
            GatorHelper.m_logger.WriteLine(result.name)

            i += 1

        with pytest.raises(Exception):
            result: "IPOPTResult" = optimizer.results[10]

        result: "IPOPTResult"

        for result in optimizer.results:
            GatorHelper.m_logger.WriteLine(result.name)

        GatorHelper.TestIPOPTTargeterGraphs(optimizer.targeter_graphs)

        optimizer.reset_controls_before_run = False
        Assert.assertFalse(optimizer.reset_controls_before_run)
        optimizer.reset_controls_before_run = True
        Assert.assertTrue(optimizer.reset_controls_before_run)

        optimizer.tolerance_on_convergence = 1
        Assert.assertEqual(1, optimizer.tolerance_on_convergence)
        with pytest.raises(Exception):
            optimizer.tolerance_on_convergence = -1

        optimizer.maximum_iterations = 2
        Assert.assertEqual(2, optimizer.maximum_iterations)
        with pytest.raises(Exception):
            optimizer.maximum_iterations = -1

        optimizer.tolerance_on_constraint_violation = 3
        Assert.assertEqual(3, optimizer.tolerance_on_constraint_violation)
        with pytest.raises(Exception):
            optimizer.tolerance_on_constraint_violation = -1

        optimizer.tolerance_on_dual_infeasibility = 4
        Assert.assertEqual(4, optimizer.tolerance_on_dual_infeasibility)
        with pytest.raises(Exception):
            optimizer.tolerance_on_dual_infeasibility = -1

        optimizer.tolerance_on_complementary_infeasibility = 5
        Assert.assertEqual(5, optimizer.tolerance_on_complementary_infeasibility)
        with pytest.raises(Exception):
            optimizer.tolerance_on_complementary_infeasibility = -1

        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            optimizer.options_filename = r"C:\Pat\bogus.txt"
        optimizer.options_filename = TestBase.GetScenarioFile("gp_marker.bmp")
        Assert.assertTrue(("gp_marker.bmp" in optimizer.options_filename))

        spCopy: "ProfileIPOPTOptimizer" = ProfileIPOPTOptimizer(optimizer.copy())

        manSegment.results.remove("Epoch")
        maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)

    @staticmethod
    def TestSNOPTTargeterGraphs(tgColl: "TargeterGraphCollection"):
        Assert.assertEqual(1, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)

        tg1: "TargeterGraph" = tgColl.add_graph()
        tg1.name = "Graph2"
        Assert.assertEqual(2, tgColl.count)
        tgColl.cut(0)
        tgColl.paste()

        Assert.assertEqual("Graph2", tgColl[0].name)
        Assert.assertEqual("Graph1", tgColl[1].name)

        tgColl.insert_copy(tgColl["Graph2"])
        Assert.assertEqual(3, tgColl.count)
        Assert.assertEqual("Graph2", tgColl[0].name)
        Assert.assertEqual("Graph1", tgColl[1].name)
        Assert.assertEqual("Graph3", tgColl[2].name)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            tgColl.remove_graph(3)
        tgColl.remove_graph(0)
        Assert.assertEqual(2, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)
        Assert.assertEqual("Graph3", tgColl[1].name)

        tgColl.remove_graph(1)
        Assert.assertEqual(1, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)

        tg: "TargeterGraph"

        for tg in tgColl:
            name: str = tg.name

        GatorHelper.TestIAgVATargeterGraph(tgColl[0])

    @staticmethod
    def TestIPOPTTargeterGraphs(tgColl: "TargeterGraphCollection"):
        Assert.assertEqual(1, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)

        tg1: "TargeterGraph" = tgColl.add_graph()
        tg1.name = "Graph2"
        Assert.assertEqual(2, tgColl.count)

        tgColl.cut(0)
        tgColl.paste()
        Assert.assertEqual("Graph2", tgColl[0].name)
        Assert.assertEqual("Graph1", tgColl[1].name)

        tgColl.insert_copy(tgColl["Graph2"])
        Assert.assertEqual(3, tgColl.count)
        Assert.assertEqual("Graph2", tgColl[0].name)
        Assert.assertEqual("Graph1", tgColl[1].name)
        Assert.assertEqual("Graph3", tgColl[2].name)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            tgColl.remove_graph(3)
        tgColl.remove_graph(0)
        Assert.assertEqual(2, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)
        Assert.assertEqual("Graph3", tgColl[1].name)

        tgColl.remove_graph(1)
        Assert.assertEqual(1, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)

        tg: "TargeterGraph"

        for tg in tgColl:
            name: str = tg.name

        GatorHelper.TestIAgVATargeterGraph(tgColl[0])

    @staticmethod
    def TestBisectionTargeterGraphs(tgColl: "TargeterGraphCollection"):
        Assert.assertEqual(1, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)

        tg1: "TargeterGraph" = tgColl.add_graph()
        tg1.name = "Graph2"
        Assert.assertEqual(2, tgColl.count)
        tgColl.cut(0)
        tgColl.paste()

        Assert.assertEqual("Graph2", tgColl[0].name)
        Assert.assertEqual("Graph1", tgColl[1].name)

        tgColl.insert_copy(tgColl["Graph2"])
        Assert.assertEqual(3, tgColl.count)
        Assert.assertEqual("Graph2", tgColl[0].name)
        Assert.assertEqual("Graph1", tgColl[1].name)
        Assert.assertEqual("Graph3", tgColl[2].name)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            tgColl.remove_graph(3)
        tgColl.remove_graph(0)
        Assert.assertEqual(2, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)
        Assert.assertEqual("Graph3", tgColl[1].name)

        tgColl.remove_graph(1)
        Assert.assertEqual(1, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)

        tg: "TargeterGraph"

        for tg in tgColl:
            name: str = tg.name

        GatorHelper.TestIAgVABisectionTargeterGraph(tgColl[0])

    @staticmethod
    def TestIAgVATargeterGraph(tg: "TargeterGraph"):
        tg.name = "NewName"
        Assert.assertEqual("NewName", tg.name)

        tg.generate_on_run = False
        Assert.assertFalse(tg.generate_on_run)
        tg.generate_on_run = True
        Assert.assertTrue(tg.generate_on_run)

        tg.user_comment = "My User Comment"
        Assert.assertEqual("My User Comment", tg.user_comment)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            tg.independent_variable = "Bogus"
        tg.independent_variable = "TMan : Epoch"
        Assert.assertEqual("TMan : Epoch", tg.independent_variable)

        tg.show_label_iterations = False
        Assert.assertFalse(tg.show_label_iterations)
        tg.show_label_iterations = True
        Assert.assertTrue(tg.show_label_iterations)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tg.show_desired_value = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tg.show_tolerance_band = False

        GatorHelper.TestIAgVATargeterGraphActiveControlCollection(
            tg.active_controls, "TMan", "FiniteMnvr BurnCenterBias"
        )

        GatorHelper.TestIAgVATargeterGraphResultCollection(tg.results, "TMan", "Epoch", 0)

    @staticmethod
    def TestIAgVABisectionTargeterGraph(tg: "TargeterGraph"):
        tg.name = "NewName"
        Assert.assertEqual("NewName", tg.name)

        tg.generate_on_run = False
        Assert.assertFalse(tg.generate_on_run)
        tg.generate_on_run = True
        Assert.assertTrue(tg.generate_on_run)

        tg.user_comment = "My User Comment"
        Assert.assertEqual("My User Comment", tg.user_comment)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            tg.independent_variable = "Bogus"
        tg.independent_variable = "TMan : Epoch"
        Assert.assertEqual("TMan : Epoch", tg.independent_variable)

        tg.show_label_iterations = False
        Assert.assertFalse(tg.show_label_iterations)
        tg.show_label_iterations = True
        Assert.assertTrue(tg.show_label_iterations)

        tg.show_desired_value = False
        Assert.assertFalse(tg.show_desired_value)
        tg.show_desired_value = True
        Assert.assertTrue(tg.show_desired_value)

        tg.show_tolerance_band = False
        Assert.assertFalse(tg.show_tolerance_band)
        tg.show_tolerance_band = True
        Assert.assertTrue(tg.show_tolerance_band)

        GatorHelper.TestIAgVATargeterGraphActiveControlCollection(
            tg.active_controls, "TMan", "FiniteMnvr BurnCenterBias"
        )

        GatorHelper.TestIAgVATargeterGraphResultCollection(tg.results, "TMan", "Epoch", 0)

    @staticmethod
    def TestIAgVATargeterGraphActiveControlCollection(
        tgacc: "TargeterGraphActiveControlCollection", sObject: str, sControlName: str
    ):
        GatorHelper.TestRuntimeTypeInfo(tgacc)

        Assert.assertEqual(1, tgacc.count)
        activeControl: "TargeterGraphActiveControl"
        for activeControl in tgacc:
            # Assert.AreEqual("TMan : FiniteMnvr BurnCenterBias", activeControl.Name);
            Assert.assertEqual(((sObject + " : ") + sControlName), activeControl.name)

        active: "TargeterGraphActiveControl" = tgacc[0]
        # Assert.AreEqual("TMan : FiniteMnvr BurnCenterBias", active.Name);
        # Assert.AreEqual("TMan", active.ParentName);
        Assert.assertEqual(((sObject + " : ") + sControlName), active.name)
        Assert.assertEqual(sObject, active.parent_name)
        if TestBase.NoGraphicsMode:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                active.show_graph_value = True
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                active.line_color = Colors.Blue
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                active.point_style = "Square"
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                active.y_axis = "Y2"

        else:
            active.show_graph_value = False
            Assert.assertFalse(active.show_graph_value)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                active.line_color = Colors.Blue
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                active.point_style = "Square"
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                active.y_axis = "Y2"

            active.show_graph_value = True
            Assert.assertTrue(active.show_graph_value)

            active.line_color = Colors.Blue
            AssertEx.AreEqual(Colors.Blue, active.line_color)
            active.point_style = "Square"
            Assert.assertEqual("Square", active.point_style)
            active.y_axis = "Y2"
            Assert.assertEqual("Y2", active.y_axis)

    @staticmethod
    def TestIAgVATargeterGraphResultCollection(
        tgrc: "TargeterGraphResultCollection", sObject: str, sControlName: str, testIndex: int
    ):
        GatorHelper.TestRuntimeTypeInfo(tgrc)

        count: int = tgrc.count
        gresult: "TargeterGraphResult"
        for gresult in tgrc:
            Console.WriteLine(gresult.name)

        result: "TargeterGraphResult" = tgrc[testIndex]
        # Assert.AreEqual("TMan : Epoch", result.Name);
        # Assert.AreEqual("TMan", result.ParentName);
        Assert.assertEqual(((sObject + " : ") + sControlName), result.name)
        Assert.assertEqual(sObject, result.parent_name)
        if TestBase.NoGraphicsMode:
            result.graph_option = GRAPH_OPTION.GRAPH_VALUE
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                result.line_color = Colors.Blue
            result.point_style = "Square"
            result.y_axis = "Y2"

        else:
            result.graph_option = GRAPH_OPTION.NO_GRAPH
            Assert.assertEqual(GRAPH_OPTION.NO_GRAPH, result.graph_option)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                result.line_color = Colors.Blue
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                result.point_style = "Square"
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                result.y_axis = "Y2"

            result.graph_option = GRAPH_OPTION.GRAPH_VALUE
            Assert.assertEqual(GRAPH_OPTION.GRAPH_VALUE, result.graph_option)

            result.line_color = Colors.Blue
            AssertEx.AreEqual(Colors.Blue, result.line_color)
            result.point_style = "Square"
            Assert.assertEqual("Square", result.point_style)
            result.y_axis = "Y2"
            Assert.assertEqual("Y2", result.y_axis)

    @staticmethod
    def TestProfileChangePropagator(iAgVAProfile: "IProfile", maneuver: "MissionControlSequenceManeuver"):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.CHANGE_PROPAGATOR)
        cp: "ProfileChangePropagator" = ProfileChangePropagator(iAgVAProfile)
        GatorHelper.TestRuntimeTypeInfo(cp)

        (cp).mode = PROFILE_MODE.NOT_ACTIVE
        Assert.assertEqual(PROFILE_MODE.NOT_ACTIVE, cp.mode)
        (cp).mode = PROFILE_MODE.ACTIVE
        Assert.assertEqual(PROFILE_MODE.ACTIVE, cp.mode)
        with pytest.raises(Exception):
            (cp).mode = PROFILE_MODE.ITERATE
        with pytest.raises(Exception):
            (cp).mode = PROFILE_MODE.RUN_ONCE
        cp.name = "MyChangePropagator"
        Assert.assertEqual("MyChangePropagator", cp.name)

        cp.segment_name = (IComponentInfo(maneuver)).name
        Assert.assertEqual((IComponentInfo(maneuver)).name, cp.segment_name)
        cp.set_segment(clr.CastAs(maneuver, IMissionControlSequenceSegment))
        Assert.assertEqual((IComponentInfo(maneuver)).name, cp.segment_name)
        GatorHelper.m_logger.WriteLine(cp.status)
        cp.propagator_name = "Heliocentric"
        Assert.assertEqual("Heliocentric", cp.propagator_name)
        cp.user_comment = "My Comment"
        Assert.assertEqual("My Comment", cp.user_comment)
        cpCopy: "ProfileChangePropagator" = clr.CastAs(cp.copy(), ProfileChangePropagator)

    @staticmethod
    def TestProfileScriptingTool(iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence"):
        if not OSHelper.IsLinux():
            Assert.assertEqual(iAgVAProfile.type, PROFILE.SCRIPTING_TOOL)
            scriptingTool: "ProfileScriptingTool" = clr.CastAs(iAgVAProfile, ProfileScriptingTool)
            GatorHelper.Test_IAgVAProfile(ts, scriptingTool, PROFILE_MODE.NOT_ACTIVE)
            GatorHelper.TestRuntimeTypeInfo(scriptingTool)

            (scriptingTool).mode = PROFILE_MODE.NOT_ACTIVE
            Assert.assertEqual(PROFILE_MODE.NOT_ACTIVE, scriptingTool.mode)
            (scriptingTool).mode = PROFILE_MODE.ACTIVE
            Assert.assertEqual(PROFILE_MODE.ACTIVE, scriptingTool.mode)
            with pytest.raises(Exception):
                (scriptingTool).mode = PROFILE_MODE.ITERATE
            with pytest.raises(Exception):
                (scriptingTool).mode = PROFILE_MODE.RUN_ONCE
            scriptingTool.enable = True
            Assert.assertTrue(scriptingTool.enable)

            GatorHelper.TestScriptingToolSegmentProperties(scriptingTool.segment_properties, "Segments.myProp")

            GatorHelper.TestScriptingToolParameters(scriptingTool.parameters)

            GatorHelper.TestScriptingToolCalcObjects(scriptingTool.calc_objects)

            scriptingTool.language_type = LANGUAGE.J_SCRIPT
            Assert.assertEqual(LANGUAGE.J_SCRIPT, scriptingTool.language_type)
            scriptingTool.script_text("int j = 1;")

    @staticmethod
    def TestProfileDifferentialCorrector(iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence"):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.DIFFERENTIAL_CORRECTOR)
        dc: "ProfileDifferentialCorrector" = ProfileDifferentialCorrector(iAgVAProfile)

        GatorHelper.Test_IAgVAProfile(ts, dc, PROFILE_MODE.ITERATE)

        loopDC: "DifferentialCorrectorControl"

        for loopDC in dc.control_parameters:
            name1: str = loopDC.name

        i: int = 0
        while i < dc.control_parameters.count:
            name2: str = dc.control_parameters[i].name

            i += 1

        dc.clear_corrections_before_run = True
        Assert.assertTrue(dc.clear_corrections_before_run)
        dc.clear_corrections_before_run = False
        Assert.assertFalse(dc.clear_corrections_before_run)

        dc.convergence_criteria = (
            CONVERGENCE_CRITERIA.CONVERVENCE_CRITERIA_EITHER_EQUALITY_CONSTRAINTS_OR_CONTROL_PARAMS
        )
        Assert.assertEqual(
            CONVERGENCE_CRITERIA.CONVERVENCE_CRITERIA_EITHER_EQUALITY_CONSTRAINTS_OR_CONTROL_PARAMS,
            dc.convergence_criteria,
        )
        dc.convergence_criteria = CONVERGENCE_CRITERIA.EQUALITY_CONSTRAINT_WITHIN_TOLERANCE
        Assert.assertEqual(CONVERGENCE_CRITERIA.EQUALITY_CONSTRAINT_WITHIN_TOLERANCE, dc.convergence_criteria)

        dc.derivative_calc_method = DERIVE_CALC_METHOD.CENTRAL
        Assert.assertEqual(DERIVE_CALC_METHOD.CENTRAL, dc.derivative_calc_method)
        dc.derivative_calc_method = DERIVE_CALC_METHOD.SIGNED
        Assert.assertEqual(DERIVE_CALC_METHOD.SIGNED, dc.derivative_calc_method)
        dc.derivative_calc_method = DERIVE_CALC_METHOD.FORWARD
        Assert.assertEqual(DERIVE_CALC_METHOD.FORWARD, dc.derivative_calc_method)

        dc.draw_perturbation = DRAW_PERTURBATION.DONT_DRAW
        Assert.assertEqual(DRAW_PERTURBATION.DONT_DRAW, dc.draw_perturbation)
        dc.draw_perturbation = DRAW_PERTURBATION.TARGETER_COLOR
        Assert.assertEqual(DRAW_PERTURBATION.TARGETER_COLOR, dc.draw_perturbation)
        dc.draw_perturbation = DRAW_PERTURBATION.SEGMENT_COLOR
        Assert.assertEqual(DRAW_PERTURBATION.SEGMENT_COLOR, dc.draw_perturbation)

        dc.enable_b_plane_nominal = False
        Assert.assertFalse(dc.enable_b_plane_nominal)
        dc.enable_b_plane_nominal = True
        Assert.assertTrue(dc.enable_b_plane_nominal)

        dc.enable_b_plane_perturbations = True
        Assert.assertTrue(dc.enable_b_plane_perturbations)
        dc.enable_b_plane_perturbations = False
        Assert.assertFalse(dc.enable_b_plane_perturbations)

        dc.enable_display_status = False
        Assert.assertFalse(dc.enable_display_status)
        dc.enable_display_status = True
        Assert.assertTrue(dc.enable_display_status)

        dc.enable_homotopy = True
        Assert.assertTrue(dc.enable_homotopy)

        dc.homotopy_steps = 2
        Assert.assertEqual(2, dc.homotopy_steps)
        dc.homotopy_steps = 1
        Assert.assertEqual(1, dc.homotopy_steps)

        dc.enable_homotopy = False
        Assert.assertFalse(dc.enable_homotopy)

        dc.enable_line_search = True
        Assert.assertTrue(dc.enable_line_search)

        dc.line_search_lower_bound = 0.001
        Assert.assertEqual(0.001, dc.line_search_lower_bound)
        dc.line_search_lower_bound = 1e-06
        Assert.assertEqual(1e-06, dc.line_search_lower_bound)

        dc.line_search_tolerance = 0.001
        Assert.assertEqual(0.001, dc.line_search_tolerance)
        dc.line_search_tolerance = 1e-06
        Assert.assertEqual(1e-06, dc.line_search_tolerance)

        dc.line_search_upper_bound = 5
        Assert.assertEqual(5, dc.line_search_upper_bound)
        dc.line_search_upper_bound = 10
        Assert.assertEqual(10, dc.line_search_upper_bound)

        dc.max_line_search_iterations = 5
        Assert.assertEqual(5, dc.max_line_search_iterations)
        dc.max_line_search_iterations = 10
        Assert.assertEqual(10, dc.max_line_search_iterations)

        dc.enable_line_search = False
        Assert.assertFalse(dc.enable_line_search)

        dc.root_finding_algorithm = ROOT_FINDING_ALGORITHM.SECANT_METHOD
        Assert.assertEqual(ROOT_FINDING_ALGORITHM.SECANT_METHOD, dc.root_finding_algorithm)
        dc.root_finding_algorithm = ROOT_FINDING_ALGORITHM.NEWTON_RAPHSON_METHOD
        Assert.assertEqual(ROOT_FINDING_ALGORITHM.NEWTON_RAPHSON_METHOD, dc.root_finding_algorithm)

        dc.max_iterations = 20
        Assert.assertEqual(20, dc.max_iterations)
        dc.max_iterations = 25
        Assert.assertEqual(25, dc.max_iterations)

        dc.stop_on_limit_cycle_detection = True
        Assert.assertEqual(True, dc.stop_on_limit_cycle_detection)
        dc.stop_on_limit_cycle_detection = False
        Assert.assertEqual(False, dc.stop_on_limit_cycle_detection)

        GatorHelper.m_logger.WriteLine(("Differential Corrector status: " + dc.status))

        GatorHelper.TestManeuverControls(clr.CastAs(ts.segments["TMan"], MissionControlSequenceManeuver), dc, ts)
        GatorHelper.TestInitialStateControls(
            clr.CastAs(ts.segments["myInitState"], MissionControlSequenceInitialState), dc
        )
        GatorHelper.TestLaunchControls(clr.CastAs(ts.segments["myLaunch"], MissionControlSequenceLaunch), dc)
        GatorHelper.TestFollowControls(clr.CastAs(ts.segments["myFollow"], MissionControlSequenceFollow), dc)
        GatorHelper.TestPropagateControls(clr.CastAs(ts.segments["myProp"], MissionControlSequencePropagate), dc)
        GatorHelper.TestUpdateControls(clr.CastAs(ts.segments["myUpdate"], MissionControlSequenceUpdate), dc)

        segment: "IMissionControlSequenceSegment" = ts.segments["TMan"]
        segment.results.add("Epoch")
        segment.results.add("Geodetic/Altitude")

        i: int = 0
        while i < dc.results.count:
            result: "DifferentialCorrectorResult" = dc.results[i]

            i += 1

        with pytest.raises(Exception):
            result: "DifferentialCorrectorResult" = dc.results[10]

        result: "DifferentialCorrectorResult"

        for result in dc.results:
            pass

        with pytest.raises(Exception):
            eq2: "DifferentialCorrectorResult" = dc.results.get_result_by_paths("TMan", "ResultPath")
        with pytest.raises(Exception):
            eq2: "DifferentialCorrectorResult" = dc.results.get_result_by_paths("ObjectPath", "Epoch")

        eq: "DifferentialCorrectorResult" = dc.results.get_result_by_paths("TMan", "Epoch")
        GatorHelper.m_logger.WriteLine(eq.name)
        GatorHelper.m_logger.WriteLine(str(eq.current_value))
        eq.enable = True
        Assert.assertTrue(eq.enable)
        eq.desired_value = "1 Jul 1999 01:00:00.000"
        Assert.assertEqual("1 Jul 1999 01:00:00.000", eq.desired_value)
        Assert.assertEqual("TMan", eq.parent_name)
        GatorHelper.m_logger.WriteLine(("\tDifference=" + str(eq.difference)))
        eq.tolerance = 0.2
        Assert.assertEqual(0.2, eq.tolerance)
        eq.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.ONE_NO_SCALING
        Assert.assertEqual(DIFFERENTIAL_CORRECTOR_SCALING_METHOD.ONE_NO_SCALING, eq.scaling_method)
        eq.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.TOLERANCE
        Assert.assertEqual(DIFFERENTIAL_CORRECTOR_SCALING_METHOD.TOLERANCE, eq.scaling_method)
        eq.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.SPECIFIED_VALUE
        Assert.assertEqual(DIFFERENTIAL_CORRECTOR_SCALING_METHOD.SPECIFIED_VALUE, eq.scaling_method)
        eq.scaling_value = 2
        Assert.assertEqual(2, eq.scaling_value)
        eq.weight = 2
        Assert.assertEqual(2, eq.weight)
        eq.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.INITIAL_VALUE
        Assert.assertEqual(DIFFERENTIAL_CORRECTOR_SCALING_METHOD.INITIAL_VALUE, eq.scaling_method)
        Assert.assertEqual(0, Array.Length(eq.values))

        segment.results.remove("Epoch")
        segment.results.remove("Altitude")

    @staticmethod
    def TestProfileRunOnce(iAgVAProfile: "IProfile"):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.RUN_ONCE)
        ro: "ProfileRunOnce" = ProfileRunOnce(iAgVAProfile)
        GatorHelper.TestRuntimeTypeInfo(ro)

        (ro).mode = PROFILE_MODE.NOT_ACTIVE
        Assert.assertEqual(PROFILE_MODE.NOT_ACTIVE, ro.mode)
        (ro).mode = PROFILE_MODE.ACTIVE
        Assert.assertEqual(PROFILE_MODE.ACTIVE, ro.mode)
        with pytest.raises(Exception):
            (ro).mode = PROFILE_MODE.ITERATE
        with pytest.raises(Exception):
            (ro).mode = PROFILE_MODE.RUN_ONCE
        ro.name = "Run Target Sequence Once"
        Assert.assertEqual("Run Target Sequence Once", ro.name)
        GatorHelper.m_logger.WriteLine(ro.status)
        ro.user_comment = "Test User Comment"
        Assert.assertEqual("Test User Comment", ro.user_comment)
        GatorHelper.m_logger.WriteLine(ro.user_comment)
        roCopy: "ProfileRunOnce" = ProfileRunOnce(ro.copy())
        Assert.assertEqual(ro.mode, roCopy.mode)
        Assert.assertEqual(ro.status, roCopy.status)

    @staticmethod
    def TestProfileSeedFiniteManeuver(
        iAgVAProfile: "IProfile", maneuver: "MissionControlSequenceManeuver", ts: "MissionControlSequenceTargetSequence"
    ):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.SEED_FINITE_MANEUVER)
        sfm: "ProfileSeedFiniteManeuver" = ProfileSeedFiniteManeuver(iAgVAProfile)
        GatorHelper.Test_IAgVAProfile(ts, sfm, PROFILE_MODE.NOT_ACTIVE)
        GatorHelper.TestRuntimeTypeInfo(sfm)

        (sfm).mode = PROFILE_MODE.NOT_ACTIVE
        Assert.assertEqual(PROFILE_MODE.NOT_ACTIVE, sfm.mode)
        (sfm).mode = PROFILE_MODE.ACTIVE
        Assert.assertEqual(PROFILE_MODE.ACTIVE, sfm.mode)
        with pytest.raises(Exception):
            (sfm).mode = PROFILE_MODE.ITERATE
        with pytest.raises(Exception):
            (sfm).mode = PROFILE_MODE.RUN_ONCE
        sfm.set_segment(maneuver)
        Assert.assertEqual((IComponentInfo(maneuver)).name, sfm.segment_name)
        sfm.segment_name = (IComponentInfo(maneuver)).name
        Assert.assertEqual((IComponentInfo(maneuver)).name, sfm.segment_name)
        Assert.assertEqual("Seed Finite Maneuver", sfm.name)
        GatorHelper.m_logger.WriteLine(sfm.status)
        GatorHelper.m_logger.WriteLine(sfm.user_comment)
        sfmCopy: "ProfileSeedFiniteManeuver" = ProfileSeedFiniteManeuver(sfm.copy())
        Assert.assertEqual(sfm.mode, sfmCopy.mode)
        Assert.assertEqual(sfm.segment_name, sfmCopy.segment_name)
        Assert.assertEqual(sfm.status, sfmCopy.status)

    @staticmethod
    def TestProfileChangeStopSegment(
        iAgVAProfile: "IProfile", stopSeg: "MissionControlSequenceStop", ts: "MissionControlSequenceTargetSequence"
    ):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.CHANGE_STOP_SEGMENT)
        css: "ProfileChangeStopSegment" = ProfileChangeStopSegment(iAgVAProfile)
        GatorHelper.Test_IAgVAProfile(ts, css, PROFILE_MODE.NOT_ACTIVE)
        GatorHelper.TestRuntimeTypeInfo(css)

        css.set_segment(stopSeg)
        Assert.assertEqual("myStop", css.segment_name)
        css.segment_name = "myStop"
        Assert.assertEqual("myStop", css.segment_name)
        (css).mode = PROFILE_MODE.NOT_ACTIVE
        Assert.assertEqual(PROFILE_MODE.NOT_ACTIVE, css.mode)
        (css).mode = PROFILE_MODE.ACTIVE
        Assert.assertEqual(PROFILE_MODE.ACTIVE, css.mode)
        with pytest.raises(Exception):
            (css).mode = PROFILE_MODE.ITERATE
        with pytest.raises(Exception):
            (css).mode = PROFILE_MODE.RUN_ONCE
        css.state = STATE.DISABLED
        Assert.assertEqual(STATE.DISABLED, css.state)
        css.state = STATE.ENABLED
        Assert.assertEqual(STATE.ENABLED, css.state)
        GatorHelper.m_logger.WriteLine(css.status)
        css.user_comment = "My User Comment"
        Assert.assertEqual("My User Comment", css.user_comment)

        cssCopy: "ProfileChangeStopSegment" = ProfileChangeStopSegment(css.copy())
        Assert.assertEqual(css.mode, cssCopy.mode)
        Assert.assertEqual(css.segment_name, cssCopy.segment_name)
        Assert.assertEqual(css.state, cssCopy.state)

    @staticmethod
    def TestProfileChangeReturnSegment(
        iAgVAProfile: "IProfile", returnSeg: "MissionControlSequenceReturn", ts: "MissionControlSequenceTargetSequence"
    ):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.CHANGE_RETURN_SEGMENT)
        crs: "ProfileChangeReturnSegment" = ProfileChangeReturnSegment(iAgVAProfile)
        GatorHelper.Test_IAgVAProfile(ts, crs, PROFILE_MODE.NOT_ACTIVE)
        GatorHelper.TestRuntimeTypeInfo(crs)

        with pytest.raises(Exception):
            crs.segment_name = ""

        crs.set_segment(returnSeg)
        Assert.assertEqual("myReturn", crs.segment_name)
        crs.segment_name = "myReturn"
        (crs).mode = PROFILE_MODE.NOT_ACTIVE
        Assert.assertEqual(PROFILE_MODE.NOT_ACTIVE, crs.mode)
        (crs).mode = PROFILE_MODE.ACTIVE
        Assert.assertEqual(PROFILE_MODE.ACTIVE, crs.mode)
        with pytest.raises(Exception):
            (crs).mode = PROFILE_MODE.ITERATE
        with pytest.raises(Exception):
            (crs).mode = PROFILE_MODE.RUN_ONCE
        crs.state = RETURN_CONTROL.DISABLE
        Assert.assertEqual(RETURN_CONTROL.DISABLE, crs.state)
        crs.state = RETURN_CONTROL.ENABLE
        Assert.assertEqual(RETURN_CONTROL.ENABLE, crs.state)
        crs.state = RETURN_CONTROL.ENABLE_EXCEPT_PROFILES_BYPASS
        Assert.assertEqual(RETURN_CONTROL.ENABLE_EXCEPT_PROFILES_BYPASS, crs.state)
        GatorHelper.m_logger.WriteLine(crs.status)
        GatorHelper.m_logger.WriteLine(crs.user_comment)
        crsCopy: "ProfileChangeReturnSegment" = ProfileChangeReturnSegment(crs.copy())

        Assert.assertEqual(crs.mode, crsCopy.mode)
        Assert.assertEqual(crs.segment_name, crsCopy.segment_name)
        Assert.assertEqual(crs.state, crsCopy.state)

    @staticmethod
    def TestProfileChangeStoppingConditionState(
        iAgVAProfile: "IProfile",
        maneuver: "IMissionControlSequenceSegment",
        condition: "StoppingConditionElement",
        ts: "MissionControlSequenceTargetSequence",
    ):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.CHANGE_STOPPING_CONDITION_STATE)
        state: "ProfileChangeStoppingConditionState" = ProfileChangeStoppingConditionState(iAgVAProfile)
        GatorHelper.Test_IAgVAProfile(ts, state, PROFILE_MODE.NOT_ACTIVE)
        GatorHelper.TestRuntimeTypeInfo(condition)

        seg: "IMissionControlSequenceSegment"

        for seg in ts.segments:
            if (clr.Is(seg, MissionControlSequenceManeuver) or clr.Is(seg, MissionControlSequenceHold)) or clr.Is(
                seg, MissionControlSequencePropagate
            ):
                state.set_segment(seg)

            else:
                with pytest.raises(Exception):
                    state.set_segment(seg)

        state.set_segment(maneuver)

        state.segment_name = "TMan"
        Assert.assertEqual("TMan", state.segment_name)
        Assert.assertEqual("Change Stopping Condition State", state.name)
        GatorHelper.m_logger.WriteLine(state.status)

        (state).mode = PROFILE_MODE.NOT_ACTIVE
        Assert.assertEqual(PROFILE_MODE.NOT_ACTIVE, state.mode)
        (state).mode = PROFILE_MODE.ACTIVE
        Assert.assertEqual(PROFILE_MODE.ACTIVE, state.mode)
        with pytest.raises(Exception):
            (state).mode = PROFILE_MODE.ITERATE
        with pytest.raises(Exception):
            (state).mode = PROFILE_MODE.RUN_ONCE

        state.state = STATE.ENABLED
        Assert.assertEqual(STATE.ENABLED, state.state)
        state.state = STATE.DISABLED
        Assert.assertEqual(STATE.DISABLED, state.state)

        with pytest.raises(Exception):
            state.set_trigger(clr.CastAs(condition, StoppingCondition))

        state.set_trigger(clr.CastAs(condition.properties, StoppingCondition))
        Assert.assertEqual((IComponentInfo(condition)).name, state.trigger_name)
        state.trigger_name = "Duration"
        Assert.assertEqual("Duration", state.trigger_name)

        with pytest.raises(Exception):
            state.trigger_name = "Bogus"

        stateCopy: "ProfileChangeStoppingConditionState" = ProfileChangeStoppingConditionState(state.copy())
        Assert.assertEqual(stateCopy.segment_name, state.segment_name)
        Assert.assertEqual(stateCopy.mode, state.mode)
        Assert.assertEqual(stateCopy.state, stateCopy.state)
        Assert.assertEqual(stateCopy.status, stateCopy.status)
        Assert.assertEqual(stateCopy.trigger_name, state.trigger_name)

    @staticmethod
    def TestProfileChangeManeuverType(
        iAgVAProfile: "IProfile", maneuver: "MissionControlSequenceManeuver", ts: "MissionControlSequenceTargetSequence"
    ):
        Assert.assertEqual(iAgVAProfile.type, PROFILE.CHANGE_MANEUVER_TYPE)
        cmt: "ProfileChangeManeuverType" = ProfileChangeManeuverType(iAgVAProfile)
        GatorHelper.Test_IAgVAProfile(ts, cmt, PROFILE_MODE.NOT_ACTIVE)
        GatorHelper.TestRuntimeTypeInfo(cmt)

        cmt.name = "My Change"
        Assert.assertEqual("My Change", cmt.name)
        (cmt).mode = PROFILE_MODE.NOT_ACTIVE
        Assert.assertEqual(PROFILE_MODE.NOT_ACTIVE, cmt.mode)
        (cmt).mode = PROFILE_MODE.ACTIVE
        Assert.assertEqual(PROFILE_MODE.ACTIVE, cmt.mode)
        with pytest.raises(Exception):
            (cmt).mode = PROFILE_MODE.ITERATE
        with pytest.raises(Exception):
            (cmt).mode = PROFILE_MODE.RUN_ONCE
        cmt.segment = maneuver
        Assert.assertEqual("TMan", (IComponentInfo(cmt.segment)).name)
        cmt.maneuver_type = MANEUVER_TYPE.FINITE
        Assert.assertEqual(MANEUVER_TYPE.FINITE, cmt.maneuver_type)
        cmt.maneuver_type = MANEUVER_TYPE.IMPULSIVE
        Assert.assertEqual(MANEUVER_TYPE.IMPULSIVE, cmt.maneuver_type)
        GatorHelper.m_logger.WriteLine(cmt.status)
        GatorHelper.m_logger.WriteLine(cmt.user_comment)
        cmtCopy: "ProfileChangeManeuverType" = ProfileChangeManeuverType(cmt.copy())
        Assert.assertEqual((IComponentInfo(cmtCopy.segment)).name, (IComponentInfo(cmt.segment)).name)

    @staticmethod
    def TestSequence(sequence: "IMissionControlSequenceSequence", type: "SEGMENT_TYPE", isFromCM: bool):
        GatorHelper.TestRuntimeTypeInfo(sequence)
        segment: "IMissionControlSequenceSegment" = clr.CastAs(sequence, IMissionControlSequenceSegment)

        type1: "SEGMENT_TYPE" = segment.type
        Assert.assertEqual(type, type1)
        sequence.generate_ephemeris = False
        Assert.assertFalse(sequence.generate_ephemeris)
        sequence.repeat_count = 2
        Assert.assertEqual(2, sequence.repeat_count)
        sequence.sequence_state_to_pass = SEQUENCE_STATE_TO_PASS.FINAL
        Assert.assertEqual(SEQUENCE_STATE_TO_PASS.FINAL, sequence.sequence_state_to_pass)
        sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Prop1", "-")
        if not OSHelper.IsLinux():
            scriptingTool: "ScriptingTool" = sequence.scripting_tool
            scriptingTool.enable = True
            Assert.assertTrue(scriptingTool.enable)

            GatorHelper.TestScriptingToolSegmentProperties(scriptingTool.segment_properties, "Segments.Prop1")

            GatorHelper.TestScriptingToolParameters(scriptingTool.parameters)

            GatorHelper.TestScriptingToolCalcObjects(scriptingTool.calc_objects)

            scriptingTool.language_type = LANGUAGE.J_SCRIPT
            Assert.assertEqual(LANGUAGE.J_SCRIPT, scriptingTool.language_type)

            scriptingTool.script_text("var j = 1;")
            GatorHelper.m_logger.WriteLine("Apply Script to sequence. Start")
            sequence.apply_script()
            GatorHelper.m_logger.WriteLine("Apply Script to sequence. End")

    @staticmethod
    def TestScriptingToolSegmentProperties(segCol: "ScriptingSegmentCollection", objName: str):
        segpropname: str = "Tester1"
        scriptSeg: "ScriptingSegment" = segCol.add(segpropname)
        Assert.assertIsNotNone(scriptSeg)
        Assert.assertEqual(segpropname, scriptSeg.component_name)

        scriptSeg.component_name = "Dummy"
        Assert.assertEqual("Dummy", scriptSeg.component_name)
        scriptSeg.component_name = segpropname
        Assert.assertEqual(segpropname, scriptSeg.component_name)

        seg: "ScriptingSegment"

        for seg in segCol:
            objectName: str = seg.object_name

        i: int = 0
        while i < segCol.count:
            objectName: str = segCol[i].object_name

            i += 1

        objectName2: str = segCol["Tester1"].object_name

        with pytest.raises(Exception):
            objectName3: "ScriptingSegment" = segCol[5]

        with pytest.raises(Exception):
            objectName4: "ScriptingSegment" = segCol["Bogus"]

        # Choose segment
        objNameWantToUse: str = objName
        foundObj: bool = False
        s: str
        for s in scriptSeg.available_object_names:
            GatorHelper.m_logger.WriteLine(("Obj Choice: " + s))
            if objNameWantToUse == s:
                foundObj = True

        Assert.assertTrue(foundObj)
        scriptSeg.object_name = objNameWantToUse
        Assert.assertEqual(objNameWantToUse, scriptSeg.object_name)

        attrNameWantToUse: str = None
        foundAttr: bool = False

        # Choose Attributes
        attrNameWantToUse = "SegmentColor"
        foundAttr = False
        s: str
        for s in scriptSeg.available_attribute_values:
            GatorHelper.m_logger.WriteLine(("Attribute Choice: " + s))
            if attrNameWantToUse == s:
                foundAttr = True

        Assert.assertTrue(foundAttr)
        scriptSeg.attribute = attrNameWantToUse
        Assert.assertEqual(attrNameWantToUse, scriptSeg.attribute)

        try:
            scriptSeg.unit = "m"
            Assert.fail("Should not be able to set the unit for a SegmentColor attribute")

        except Exception as e:
            expectedMessage: str = "Cannot modify read-only attribute"
            Assert.assertEqual(expectedMessage, str(e))

        # Choose another Attributes
        # NOTE: Could also use MinPropTime, StoppingConditions.Duration.TripValue, Tolerance
        attrNameWantToUse = "MaxPropTime"
        foundAttr = False
        s: str
        for s in scriptSeg.available_attribute_values:
            GatorHelper.m_logger.WriteLine(("Attribute Choice: " + s))
            if attrNameWantToUse == s:
                foundAttr = True

        Assert.assertTrue(foundAttr)
        scriptSeg.attribute = attrNameWantToUse
        Assert.assertEqual(attrNameWantToUse, scriptSeg.attribute)

        holdUnit: str = scriptSeg.unit
        Assert.assertEqual("sec", holdUnit)
        scriptSeg.unit = "min"
        Assert.assertEqual("min", scriptSeg.unit)
        scriptSeg.unit = holdUnit
        Assert.assertEqual("sec", holdUnit)
        GatorHelper.m_logger.WriteLine(("Unit=" + scriptSeg.unit))
        scriptSeg.read_only_property = True
        Assert.assertTrue(scriptSeg.read_only_property)
        scriptSeg.read_only_property = False
        Assert.assertFalse(scriptSeg.read_only_property)

        segCol.remove(segpropname)
        Assert.assertEqual(0, segCol.count)
        segCol.add("Tester2")
        segCol.remove(0)
        Assert.assertEqual(0, segCol.count)
        segCol.add("Tester3")
        segCol.remove_all()
        Assert.assertEqual(0, segCol.count)

        with pytest.raises(Exception):
            segCol.remove(0)

        with pytest.raises(Exception):
            segCol.remove("Bogus")

        GatorHelper.TestRuntimeTypeInfo(segCol)

    @staticmethod
    def TestScriptingToolParameters(paramCol: "ScriptingParameterCollection"):
        GatorHelper.TestRuntimeTypeInfo(paramCol)

        name: str = "Tester1"
        param: "ScriptingParameter" = paramCol.add(name)
        Assert.assertIsNotNone(param)

        GatorHelper.TestRuntimeTypeInfo(param)

        holdName: str = param.name
        param.name = "MyParamName"
        Assert.assertEqual("MyParamName", param.name)
        param.name = holdName
        Assert.assertEqual(holdName, param.name)

        i: int = 0
        while i < paramCol.count:
            scriptingParamName1: str = paramCol[i].name

            i += 1

        scriptingParamName2: str = paramCol["Tester1"].name

        scriptingParam: "ScriptingParameter"

        for scriptingParam in paramCol:
            scriptingParamName3: str = scriptingParam.name

        with pytest.raises(Exception):
            comp3: "ScriptingParameter" = paramCol[5]

        with pytest.raises(Exception):
            comp4: "ScriptingParameter" = paramCol["Bogus"]

        Assert.assertEqual(name, param.name)

        param.param_value = 5
        Assert.assertEqual(5, param.param_value)

        paramCol.remove(name)
        Assert.assertEqual(0, paramCol.count)
        param2: "ScriptingParameter" = None
        param2 = paramCol.add("Tester2")
        paramCol.remove(0)
        Assert.assertEqual(0, paramCol.count)

        param3: "ScriptingParameter" = None
        param3 = paramCol.add("Tester3")
        paramCol.remove_all()
        Assert.assertEqual(0, paramCol.count)

        with pytest.raises(Exception):
            paramCol.remove(0)

        with pytest.raises(Exception):
            paramCol.remove("Bogus")

    @staticmethod
    def TestScriptingToolCalcObjects(coCol: "ScriptingCalcObjectCollection"):
        # Calc objects
        cow1name: str = "Test1"
        cow1: "ScriptingCalcObject" = coCol.add(cow1name)
        Assert.assertEqual(cow1name, cow1.component_name)

        cow2name: str = "Test2"
        cow2: "ScriptingCalcObject" = coCol.add(cow2name)
        Assert.assertEqual(cow2name, cow2.component_name)

        # Gator auto renames if the name already exists, no exception
        cow3name: str = "Test2"
        cow3: "ScriptingCalcObject" = coCol.add(cow3name)
        Assert.assertEqual("CalcObject", cow3.component_name)

        Assert.assertEqual(3, coCol.count)

        # Gator auto renames if the name already exists, no exception
        cow4name: str = "CalcObject"
        cow4: "ScriptingCalcObject" = coCol.add(cow4name)
        Assert.assertEqual("CalcObject1", cow4.component_name)

        Assert.assertEqual(4, coCol.count)

        coCol.remove("CalcObject1")
        coCol.remove("CalcObject")

        GatorHelper.m_logger.WriteLine("CalcObjectWrappers tested via indexing:")

        i: int = 0
        while i < coCol.count:
            wrapperByIndex: "ScriptingCalcObject" = coCol[i]
            Assert.assertIsNotNone(wrapperByIndex)
            calcObjectName: str = wrapperByIndex.calc_object_name
            componentName: str = wrapperByIndex.component_name
            wrapperByName: "ScriptingCalcObject" = coCol[componentName]
            Assert.assertIsNotNone(wrapperByName)

            GatorHelper.m_logger.WriteLine7("\tComponentName[{0}]={1}", i, componentName)
            GatorHelper.m_logger.WriteLine7("\tCalcObjectName[{0}]={1}", i, calcObjectName)
            GatorHelper.m_logger.WriteLine7("\tUnit[{0}]={1}", i, wrapperByIndex.unit)

            wrapperByIndexExplicit: "ScriptingCalcObject" = coCol.get_item_by_index(i)
            wrapperByNameExplicit: "ScriptingCalcObject" = coCol.get_item_by_name(componentName)
            Assert.assertEqual(calcObjectName, wrapperByIndexExplicit.calc_object_name)
            Assert.assertEqual(calcObjectName, wrapperByNameExplicit.calc_object_name)

            i += 1

        wrapper2: "ScriptingCalcObject" = coCol["Test1"]

        with pytest.raises(Exception):
            wrapper3: "ScriptingCalcObject" = coCol[5]

        with pytest.raises(Exception):
            wrapper4: "ScriptingCalcObject" = coCol["Bogus"]

        GatorHelper.m_logger.WriteLine("CalcObjectWrappers test the enumerator:")
        enumWrapper: "ScriptingCalcObject"
        for enumWrapper in coCol:
            GatorHelper.m_logger.WriteLine(("\tComponentName=" + enumWrapper.component_name))
            GatorHelper.m_logger.WriteLine(("\tCalcObjectName=" + enumWrapper.calc_object_name))
            GatorHelper.m_logger.WriteLine(("\tUnit=" + enumWrapper.unit))

        newWrapper: "ScriptingCalcObject" = coCol[cow1name]
        newWrapper.component_name = "NewTest1"
        Assert.assertEqual("NewTest1", newWrapper.component_name)
        newWrapper.calc_object_name = "Maneuver/DeltaV"
        Assert.assertEqual("DeltaV", newWrapper.calc_object_name)
        deltaV: "StateCalcDeltaV" = clr.CastAs(newWrapper.calc_object, StateCalcDeltaV)
        Assert.assertEqual("DeltaV", (IComponentInfo(deltaV)).name)
        newWrapper.unit = "m/sec"
        Assert.assertEqual("m/sec", newWrapper.unit)
        newWrapper.unit = "mi/hr"
        Assert.assertEqual("mi/hr", newWrapper.unit)

        with pytest.raises(Exception):
            newWrapper.unit = "deg/sec"

        coCol.remove(0)
        Assert.assertEqual(1, coCol.count)

        coCol.add("NewTest")
        Assert.assertEqual(2, coCol.count)

        Assert.assertEqual("Test2", coCol[0].component_name)

        coCol.remove("NewTest")
        Assert.assertEqual(1, coCol.count)

        coCol.remove_all()
        Assert.assertEqual(0, coCol.count)

        with pytest.raises(Exception):
            coCol.remove(0)

        with pytest.raises(Exception):
            coCol.remove("Bogus")

    @staticmethod
    def TestRuntimeTypeInfo(obj: typing.Any):
        Assert.assertIsNotNone(obj)
        rttip: "IRuntimeTypeInfoProvider" = clr.CastAs(obj, IRuntimeTypeInfoProvider)
        Assert.assertIsNotNone(rttip)

        rtti: "RuntimeTypeInfo" = rttip.provide_runtime_type_info
        if rtti.is_collection:
            i: int = 0
            while i < rtti.count:
                if rtti.properties.count > 0:
                    pic: "PropertyInfoCollection" = rtti.properties
                    x: "PropertyInfo" = pic[0]
                    name: str = x.name
                    y: "PropertyInfo" = pic.get_item_by_index(0)
                    z: "PropertyInfo" = pic.get_item_by_name(name)
                    Assert.assertEqual(x.name, y.name)
                    Assert.assertEqual(x.name, z.name)

                pi: "PropertyInfo" = rtti.get_item(i)
                # Console.WriteLine(pi.Name);
                GatorHelper.RecursePropertyInfo(pi)

                i += 1

        pi: "PropertyInfo"
        for pi in rtti.properties:
            Console.Write(pi.name)
            GatorHelper.RecursePropertyInfo(pi)

        i: int = 0
        while i < rtti.properties.count:
            pi: "PropertyInfo" = rtti.properties[i]
            namexx: str = pi.name
            pi2: "PropertyInfo" = rtti.properties[namexx]
            Assert.assertIsNotNone(pi2)

            i += 1

        with pytest.raises(Exception):
            pi: "PropertyInfo" = rtti.properties[rtti.properties.count]

    @staticmethod
    def RecursePropertyInfo(pi: "PropertyInfo"):
        name: str = pi.name
        if pi.has_max:
            max: typing.Any = pi.max

        else:
            pass

        if pi.has_min:
            max: typing.Any = pi.min

        else:
            pass

        if pi.property_type == PROPERTY_INFO_VALUE_TYPE.INTERFACE:
            rttip: "IRuntimeTypeInfoProvider" = clr.CastAs(pi.get_value(), IRuntimeTypeInfoProvider)
            if rttip != None:
                rtti: "RuntimeTypeInfo" = rttip.provide_runtime_type_info
                if rtti.is_collection:
                    i: int = 0
                    while i < rtti.count:
                        pi2: "PropertyInfo" = rtti.get_item(i)
                        GatorHelper.RecursePropertyInfo(pi2)

                        i += 1

                pi2: "PropertyInfo"
                for pi2 in rtti.properties:
                    GatorHelper.RecursePropertyInfo(pi2)

        elif pi.property_type == PROPERTY_INFO_VALUE_TYPE.BOOL:
            try:
                value: bool = bool(pi.get_value())

            except Exception:
                Assert.fail("Value returned was not of type bool")

        elif pi.property_type == PROPERTY_INFO_VALUE_TYPE.DATE:
            date: "Date" = clr.CastAs(pi.get_value(), Date)
            if date == None:
                Assert.fail("Property returned was not of type date.")

        elif pi.property_type == PROPERTY_INFO_VALUE_TYPE.INT:
            try:
                intValue: int = int(pi.get_value())

            except Exception:
                Assert.fail("Value returned was not of type int.")

        elif pi.property_type == PROPERTY_INFO_VALUE_TYPE.QUANTITY:
            quantity: "Quantity" = clr.CastAs(pi.get_value(), Quantity)
            if quantity == None:
                Assert.fail("Value returned was not of type Quantity.")

        elif pi.property_type == PROPERTY_INFO_VALUE_TYPE.REAL:
            try:
                doubleValue: float = float(pi.get_value())

            except Exception:
                Assert.fail("Value returned was not of type double.")

        elif pi.property_type == PROPERTY_INFO_VALUE_TYPE.STRING:
            stringValue: str = str(pi.get_value())
            if stringValue == None:
                Assert.fail("Value returned was not of type string.")

    @staticmethod
    def TestManeuver(maneuver: "MissionControlSequenceManeuver", isFromCM: bool):
        segment: "IMissionControlSequenceSegment" = clr.CastAs(maneuver, IMissionControlSequenceSegment)
        Assert.assertEqual(SEGMENT_TYPE.MANEUVER, segment.type)

        # IMPULSIVE
        maneuver.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
        Assert.assertEqual(MANEUVER_TYPE.IMPULSIVE, maneuver.maneuver_type)
        impulse: "ManeuverImpulsive" = ManeuverImpulsive(maneuver.maneuver)

        impulse.set_propulsion_method(PROPULSION_METHOD.THRUSTER_SET, "Thruster Set")
        Assert.assertEqual(PROPULSION_METHOD.THRUSTER_SET, impulse.propulsion_method)
        Assert.assertEqual("Thruster Set", impulse.propulsion_method_value)

        impulse.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, "Polynomial Thrust and Isp")
        Assert.assertEqual(PROPULSION_METHOD.ENGINE_MODEL, impulse.propulsion_method)
        Assert.assertEqual("Polynomial Thrust and Isp", impulse.propulsion_method_value)

        impulse.update_mass = False
        Assert.assertFalse(impulse.update_mass)
        impulse.update_mass = True
        Assert.assertTrue(impulse.update_mass)

        # VELOCITY_VECTOR
        impulse.set_attitude_control_type(ATTITUDE_CONTROL.VELOCITY_VECTOR)
        Assert.assertEqual(ATTITUDE_CONTROL.VELOCITY_VECTOR, impulse.attitude_control_type)
        velVec: "AttitudeControlImpulsiveVelocityVector" = AttitudeControlImpulsiveVelocityVector(
            impulse.attitude_control
        )
        GatorHelper.TestAttitudeControl(velVec)
        GatorHelper.TestRuntimeTypeInfo(velVec)

        velVec.delta_v_magnitude = 1
        Assert.assertEqual(1, velVec.delta_v_magnitude)

        direction: "IDirection" = velVec.body_constraint_vector
        Assert.assertIsNotNone(direction)
        direction.assign_xyz(1, 2, 3)

        x: float = 0
        y: float = 0
        z: float = 0

        (x, y, z) = direction.query_xyz()
        Assert.assertEqual(1, x)
        Assert.assertEqual(2, y)
        Assert.assertEqual(3, z)

        # ANTI_VELOCITY_VECTOR
        impulse.set_attitude_control_type(ATTITUDE_CONTROL.ANTI_VELOCITY_VECTOR)
        Assert.assertEqual(ATTITUDE_CONTROL.ANTI_VELOCITY_VECTOR, impulse.attitude_control_type)
        antiVelVec: "AttitudeControlImpulsiveAntiVelocityVector" = AttitudeControlImpulsiveAntiVelocityVector(
            impulse.attitude_control
        )
        GatorHelper.TestAttitudeControl(antiVelVec)
        GatorHelper.TestRuntimeTypeInfo(antiVelVec)

        antiVelVec.delta_v_magnitude = 2
        Assert.assertEqual(2, antiVelVec.delta_v_magnitude)

        direction = antiVelVec.body_constraint_vector
        Assert.assertIsNotNone(direction)
        direction.assign_xyz(4, 5, 6)
        (x, y, z) = direction.query_xyz()
        Assert.assertEqual(4, x)
        Assert.assertEqual(5, y)
        Assert.assertEqual(6, z)

        # ATTITUDE
        impulse.set_attitude_control_type(ATTITUDE_CONTROL.ATTITUDE)
        Assert.assertEqual(ATTITUDE_CONTROL.ATTITUDE, impulse.attitude_control_type)
        att: "AttitudeControlImpulsiveAttitude" = AttitudeControlImpulsiveAttitude(impulse.attitude_control)
        GatorHelper.TestAttitudeControl(att)
        GatorHelper.TestRuntimeTypeInfo(att)

        att.delta_v_magnitude = 3
        Assert.assertEqual(3, att.delta_v_magnitude)

        att.reference_axes_name = "Satellite/Satellite1 LVLH(Earth)"
        Assert.assertEqual("Satellite/Satellite1 LVLH(Earth)", att.reference_axes_name)
        with pytest.raises(Exception):
            att.reference_axes_name = "Bogus"

        orientation: "IOrientation" = att.orientation
        Assert.assertIsNotNone(orientation)
        orientation.assign_quaternion(0.0, 0.0, 0.0, 1.0)

        qx: float = 0
        qy: float = 0
        qz: float = 0
        qs: float = 0

        (qx, qy, qz, qs) = orientation.query_quaternion()
        Assert.assertEqual(0.0, qx)
        Assert.assertEqual(0.0, qy)
        Assert.assertEqual(0.0, qz)
        Assert.assertEqual(1.0, qs)

        # FILE
        impulse.set_attitude_control_type(ATTITUDE_CONTROL.FILE)
        Assert.assertEqual(ATTITUDE_CONTROL.FILE, impulse.attitude_control_type)
        file: "AttitudeControlImpulsiveFile" = AttitudeControlImpulsiveFile(impulse.attitude_control)
        GatorHelper.TestAttitudeControl(file)
        GatorHelper.TestRuntimeTypeInfo(file)

        file.delta_v_magnitude = 4
        Assert.assertEqual(4, file.delta_v_magnitude)

        file.file_time_offset = 1
        Assert.assertEqual(1, file.file_time_offset)

        file.filename = TestBase.GetScenarioFile("Satellite1.a")
        Assert.assertEqual("Satellite1.a", file.filename)

        GatorHelper.m_logger.WriteLine(file.full_filename)

        # THRUST_VECTOR
        impulse.set_attitude_control_type(ATTITUDE_CONTROL.THRUST_VECTOR)
        Assert.assertEqual(ATTITUDE_CONTROL.THRUST_VECTOR, impulse.attitude_control_type)
        thrust: "AttitudeControlImpulsiveThrustVector" = AttitudeControlImpulsiveThrustVector(impulse.attitude_control)
        GatorHelper.TestAttitudeControl(thrust)
        GatorHelper.TestRuntimeTypeInfo(thrust)

        thrust.thrust_axes_name = "Satellite/Satellite1/Sensor/Sensor2 J2000"
        Assert.assertEqual("Satellite/Satellite1/Sensor/Sensor2 J2000", thrust.thrust_axes_name)

        direction = thrust.body_constraint_vector
        Assert.assertIsNotNone(direction)
        direction.assign_xyz(1, 2, 3)
        (x, y, z) = direction.query_xyz()
        Assert.assertEqual(1, x)
        Assert.assertEqual(2, y)
        Assert.assertEqual(3, z)

        thrust.assign_cartesian(7, 8, 9)
        x = thrust.x
        y = thrust.y
        z = thrust.z

        thrust.assign_spherical(10, 20, 30)

        az: typing.Any = None
        el: typing.Any = None

        mag: float = 0
        az = thrust.azimuth
        el = thrust.elevation
        mag = thrust.magnitude
        Assert.assertAlmostEqual(10, float(az), delta=Math2.Epsilon12)
        Assert.assertAlmostEqual(20, float(el), delta=Math2.Epsilon12)
        Assert.assertAlmostEqual(30, mag, delta=Math2.Epsilon12)

        thrust.allow_negative_spherical_magnitude = False
        Assert.assertEqual(False, thrust.allow_negative_spherical_magnitude)
        thrust.allow_negative_spherical_magnitude = True
        Assert.assertEqual(True, thrust.allow_negative_spherical_magnitude)

        # thrust.Position  DEPRECATED

        # PLUGIN (not supported for Impulsive)
        with pytest.raises(Exception):
            impulse.set_attitude_control_type(ATTITUDE_CONTROL.PLUGIN)

        # FINITE
        maneuver.set_maneuver_type(MANEUVER_TYPE.FINITE)
        Assert.assertEqual(MANEUVER_TYPE.FINITE, maneuver.maneuver_type)
        finite: "ManeuverFinite" = ManeuverFinite(maneuver.maneuver)

        finite.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, "Polynomial Thrust and Isp")
        Assert.assertEqual("Polynomial Thrust and Isp", finite.propulsion_method_value)
        Assert.assertEqual(PROPULSION_METHOD.ENGINE_MODEL, finite.propulsion_method)
        finite.pressure_mode = PRESSURE_MODE.BLOW_DOWN
        Assert.assertEqual(PRESSURE_MODE.BLOW_DOWN, finite.pressure_mode)
        finite.pressure_mode = PRESSURE_MODE.PRESSURE_REGULATED
        Assert.assertEqual(PRESSURE_MODE.PRESSURE_REGULATED, finite.pressure_mode)

        finite.thrust_efficiency = 2
        Assert.assertEqual(2, finite.thrust_efficiency)

        finite.thrust_efficiency_mode = THRUST_TYPE.AFFECTS_ACCEL_AND_MASS_FLOW
        Assert.assertEqual(THRUST_TYPE.AFFECTS_ACCEL_AND_MASS_FLOW, finite.thrust_efficiency_mode)
        finite.thrust_efficiency_mode = THRUST_TYPE.AFFECTS_ACCEL_ONLY
        Assert.assertEqual(THRUST_TYPE.AFFECTS_ACCEL_ONLY, finite.thrust_efficiency_mode)

        # ANTI_VELOCITY_VECTOR
        finite.set_attitude_control_type(ATTITUDE_CONTROL.ANTI_VELOCITY_VECTOR)
        Assert.assertEqual(ATTITUDE_CONTROL.ANTI_VELOCITY_VECTOR, finite.attitude_control_type)
        fAntiVel: "AttitudeControlFiniteAntiVelocityVector" = AttitudeControlFiniteAntiVelocityVector(
            finite.attitude_control
        )
        GatorHelper.TestAttitudeControl(fAntiVel)
        GatorHelper.TestRuntimeTypeInfo(fAntiVel)

        fAntiVel.attitude_update = ATTITUDE_UPDATE.DURING_BURN
        Assert.assertEqual(ATTITUDE_UPDATE.DURING_BURN, fAntiVel.attitude_update)
        fAntiVel.attitude_update = ATTITUDE_UPDATE.INERTIAL_AT_IGNITION
        Assert.assertEqual(ATTITUDE_UPDATE.INERTIAL_AT_IGNITION, fAntiVel.attitude_update)
        fAntiVel.attitude_update = ATTITUDE_UPDATE.INERTIAL_AT_START
        Assert.assertEqual(ATTITUDE_UPDATE.INERTIAL_AT_START, fAntiVel.attitude_update)

        direction = fAntiVel.body_constraint_vector
        Assert.assertIsNotNone(direction)
        direction.assign_xyz(1, 2, 3)
        (x, y, z) = direction.query_xyz()
        Assert.assertEqual(1, x)
        Assert.assertEqual(2, y)
        Assert.assertEqual(3, z)

        # VELOCITY_VECTOR
        finite.set_attitude_control_type(ATTITUDE_CONTROL.VELOCITY_VECTOR)
        Assert.assertEqual(ATTITUDE_CONTROL.VELOCITY_VECTOR, finite.attitude_control_type)
        fVelVec: "AttitudeControlFiniteVelocityVector" = AttitudeControlFiniteVelocityVector(finite.attitude_control)
        GatorHelper.TestAttitudeControl(fVelVec)
        GatorHelper.TestRuntimeTypeInfo(fVelVec)

        fVelVec.attitude_update = ATTITUDE_UPDATE.DURING_BURN
        Assert.assertEqual(ATTITUDE_UPDATE.DURING_BURN, fVelVec.attitude_update)
        fVelVec.attitude_update = ATTITUDE_UPDATE.INERTIAL_AT_IGNITION
        Assert.assertEqual(ATTITUDE_UPDATE.INERTIAL_AT_IGNITION, fVelVec.attitude_update)
        fVelVec.attitude_update = ATTITUDE_UPDATE.INERTIAL_AT_START
        Assert.assertEqual(ATTITUDE_UPDATE.INERTIAL_AT_START, fVelVec.attitude_update)

        direction = fVelVec.body_constraint_vector
        Assert.assertIsNotNone(direction)
        direction.assign_xyz(1, 2, 3)
        (x, y, z) = direction.query_xyz()
        Assert.assertEqual(1, x)
        Assert.assertEqual(2, y)
        Assert.assertEqual(3, z)

        # ATTITUDE
        finite.set_attitude_control_type(ATTITUDE_CONTROL.ATTITUDE)
        Assert.assertEqual(ATTITUDE_CONTROL.ATTITUDE, finite.attitude_control_type)
        fAtt: "AttitudeControlFiniteAttitude" = AttitudeControlFiniteAttitude(finite.attitude_control)
        GatorHelper.TestAttitudeControl(fAtt)
        GatorHelper.TestRuntimeTypeInfo(fAtt)

        fAtt.attitude_update = ATTITUDE_UPDATE.DURING_BURN
        Assert.assertEqual(ATTITUDE_UPDATE.DURING_BURN, fAtt.attitude_update)
        fAtt.attitude_update = ATTITUDE_UPDATE.INERTIAL_AT_IGNITION
        Assert.assertEqual(ATTITUDE_UPDATE.INERTIAL_AT_IGNITION, fAtt.attitude_update)
        fAtt.attitude_update = ATTITUDE_UPDATE.INERTIAL_AT_START
        Assert.assertEqual(ATTITUDE_UPDATE.INERTIAL_AT_START, fAtt.attitude_update)

        fAtt.reference_axes_name = "Satellite/Satellite1 LVLH(Earth)"
        Assert.assertEqual("Satellite/Satellite1 LVLH(Earth)", fAtt.reference_axes_name)
        with pytest.raises(Exception):
            fAtt.reference_axes_name = "Bogus"

        orientation = fAtt.orientation
        Assert.assertIsNotNone(orientation)
        orientation.assign_quaternion(0.0, 0.0, 0.0, 1.0)
        (qx, qy, qz, qs) = orientation.query_quaternion()
        Assert.assertEqual(0.0, qx)
        Assert.assertEqual(0.0, qy)
        Assert.assertEqual(0.0, qz)
        Assert.assertEqual(1.0, qs)

        # THRUST_VECTOR
        finite.set_attitude_control_type(ATTITUDE_CONTROL.THRUST_VECTOR)
        Assert.assertEqual(ATTITUDE_CONTROL.THRUST_VECTOR, finite.attitude_control_type)
        fthrust: "AttitudeControlFiniteThrustVector" = AttitudeControlFiniteThrustVector(finite.attitude_control)
        GatorHelper.TestAttitudeControl(fthrust)
        GatorHelper.TestRuntimeTypeInfo(fthrust)

        fthrust.attitude_update = ATTITUDE_UPDATE.DURING_BURN
        Assert.assertEqual(ATTITUDE_UPDATE.DURING_BURN, fthrust.attitude_update)
        fthrust.attitude_update = ATTITUDE_UPDATE.INERTIAL_AT_IGNITION
        Assert.assertEqual(ATTITUDE_UPDATE.INERTIAL_AT_IGNITION, fthrust.attitude_update)
        fthrust.attitude_update = ATTITUDE_UPDATE.INERTIAL_AT_START
        Assert.assertEqual(ATTITUDE_UPDATE.INERTIAL_AT_START, fthrust.attitude_update)

        fthrust.thrust_axes_name = "Satellite/Satellite1 LVLH(Earth)"
        Assert.assertEqual("Satellite/Satellite1 LVLH(Earth)", fthrust.thrust_axes_name)
        with pytest.raises(Exception):
            fthrust.thrust_axes_name = "Bogus"

        direction = fthrust.thrust_vector
        Assert.assertIsNotNone(direction)
        direction.assign_xyz(1, 2, 3)
        (x, y, z) = direction.query_xyz()
        Assert.assertEqual(1, x)
        Assert.assertEqual(2, y)
        Assert.assertEqual(3, z)

        direction = fthrust.body_constraint_vector
        Assert.assertIsNotNone(direction)
        direction.assign_xyz(1, 2, 3)
        (x, y, z) = direction.query_xyz()
        Assert.assertEqual(1, x)
        Assert.assertEqual(2, y)
        Assert.assertEqual(3, z)

        # TIME_VARYING
        finite.set_attitude_control_type(ATTITUDE_CONTROL.TIME_VARYING)
        Assert.assertEqual(ATTITUDE_CONTROL.TIME_VARYING, finite.attitude_control_type)
        ftimevary: "AttitudeControlFiniteTimeVarying" = AttitudeControlFiniteTimeVarying(finite.attitude_control)
        GatorHelper.TestAttitudeControl(ftimevary)
        GatorHelper.TestRuntimeTypeInfo(ftimevary)

        ftimevary.thrust_axes_name = "Satellite/Satellite1 LVLH(Earth)"
        Assert.assertEqual("Satellite/Satellite1 LVLH(Earth)", ftimevary.thrust_axes_name)
        with pytest.raises(Exception):
            ftimevary.thrust_axes_name = "Bogus"

        ftimevary.az0 = 0.1
        Assert.assertAlmostEqual(0.1, ftimevary.az0, delta=Math2.Epsilon12)
        ftimevary.az1 = 0.01
        Assert.assertAlmostEqual(0.01, ftimevary.az1, delta=Math2.Epsilon12)
        ftimevary.az2 = 0.02
        Assert.assertAlmostEqual(0.02, ftimevary.az2, delta=Math2.Epsilon12)
        ftimevary.az3 = 0.03
        Assert.assertAlmostEqual(0.03, ftimevary.az3, delta=Math2.Epsilon12)
        ftimevary.az4 = 0.04
        Assert.assertAlmostEqual(0.04, ftimevary.az4, delta=Math2.Epsilon12)
        ftimevary.az_a = 0.01
        Assert.assertAlmostEqual(0.01, ftimevary.az_a, delta=Math2.Epsilon12)
        ftimevary.az_f = 0.02
        Assert.assertAlmostEqual(0.02, ftimevary.az_f, delta=Math2.Epsilon12)
        ftimevary.az_p = 0.03
        Assert.assertAlmostEqual(0.03, ftimevary.az_p, delta=Math2.Epsilon12)

        ftimevary.el0 = 0.1
        Assert.assertAlmostEqual(0.1, ftimevary.el0, delta=Math2.Epsilon12)
        ftimevary.el1 = 0.01
        Assert.assertAlmostEqual(0.01, ftimevary.el1, delta=Math2.Epsilon12)
        ftimevary.el2 = 0.02
        Assert.assertAlmostEqual(0.02, ftimevary.el2, delta=Math2.Epsilon12)
        ftimevary.el3 = 0.03
        Assert.assertAlmostEqual(0.03, ftimevary.el3, delta=Math2.Epsilon12)
        ftimevary.el4 = 0.04
        Assert.assertAlmostEqual(0.04, ftimevary.el4, delta=Math2.Epsilon12)
        ftimevary.el_a = 0.01
        Assert.assertAlmostEqual(0.01, ftimevary.el_a, delta=Math2.Epsilon12)
        ftimevary.el_f = 0.02
        Assert.assertAlmostEqual(0.02, ftimevary.el_f, delta=Math2.Epsilon12)
        ftimevary.el_p = 0.03
        Assert.assertAlmostEqual(0.03, ftimevary.el_p, delta=Math2.Epsilon12)

        # FILE
        finite.set_attitude_control_type(ATTITUDE_CONTROL.FILE)
        Assert.assertEqual(ATTITUDE_CONTROL.FILE, finite.attitude_control_type)
        ffile: "AttitudeControlFiniteFile" = AttitudeControlFiniteFile(finite.attitude_control)
        GatorHelper.TestAttitudeControl(ffile)
        GatorHelper.TestRuntimeTypeInfo(ffile)

        ffile.filename = "Satellite1.a"
        Assert.assertEqual(r"Satellite1.a", ffile.filename)

        GatorHelper.m_logger.WriteLine(ffile.full_filename)

        ffile.file_time_offset = 2
        Assert.assertEqual(2, ffile.file_time_offset)

        # PLUGIN
        finite.set_attitude_control_type(ATTITUDE_CONTROL.PLUGIN)
        Assert.assertEqual(ATTITUDE_CONTROL.PLUGIN, finite.attitude_control_type)
        plugin: "AttitudeControlFinitePlugin" = AttitudeControlFinitePlugin(finite.attitude_control)
        GatorHelper.TestAttitudeControl(plugin)
        GatorHelper.TestRuntimeTypeInfo(plugin)

        pluginProperties: "PluginProperties" = plugin.plugin_config
        Assert.assertIsNotNone(pluginProperties)

        plugin.select_plugin_by_name("Plugin Attitude Controller")  # Built in
        Assert.assertEqual("Plugin Attitude Controller", plugin.plugin_name)
        with pytest.raises(Exception):
            plugin.select_plugin_by_name("Plugin Bogus")

        propagate: "ManeuverFinitePropagator" = finite.propagator

        propagate.propagator_name = "Earth Point Mass"
        Assert.assertEqual("Earth Point Mass", propagate.propagator_name)

        propagate.min_propagation_time = 0
        Assert.assertEqual(0, propagate.min_propagation_time)
        propagate.max_propagation_time = 2
        Assert.assertEqual(2, propagate.max_propagation_time)
        propagate.enable_warning_message = False
        Assert.assertFalse(propagate.enable_warning_message)
        propagate.override_max_propagation_time = True
        Assert.assertTrue(propagate.override_max_propagation_time)
        propagate.override_max_propagation_time = False
        Assert.assertFalse(propagate.override_max_propagation_time)
        propagate.enable_max_propagation_time = False
        Assert.assertFalse(propagate.enable_max_propagation_time)

        propagate.should_stop_for_initially_surpassed_epoch_stopping_conditions = True
        Assert.assertTrue(propagate.should_stop_for_initially_surpassed_epoch_stopping_conditions)
        propagate.should_stop_for_initially_surpassed_epoch_stopping_conditions = False
        Assert.assertFalse(propagate.should_stop_for_initially_surpassed_epoch_stopping_conditions)

        propagate.enable_center_burn = True
        Assert.assertTrue(propagate.enable_center_burn)
        propagate.bias = 1
        Assert.assertEqual(1, propagate.bias)
        propagate.enable_center_burn = False
        Assert.assertFalse(propagate.enable_center_burn)
        GatorHelper.TestStoppingConditionCollection(propagate.stopping_conditions)

    @staticmethod
    def TestManeuver_OptimalFinite(maneuver: "MissionControlSequenceManeuver", isFromCM: bool, root: "StkObjectRoot"):
        # Initialize the optimal finite maneuver from  a default finite maneuver
        maneuver.set_maneuver_type(MANEUVER_TYPE.FINITE)
        Assert.assertEqual(MANEUVER_TYPE.FINITE, maneuver.maneuver_type)
        sat: "Satellite" = clr.CastAs(root.current_scenario.children["Satellite1"], Satellite)
        mcs: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        mcs.run_mission_control_sequence()

        maneuver.set_maneuver_type(MANEUVER_TYPE.OPTIMAL_FINITE)
        Assert.assertEqual(MANEUVER_TYPE.OPTIMAL_FINITE, maneuver.maneuver_type)
        optFinite: "ManeuverOptimalFinite" = clr.CastAs(maneuver.maneuver, ManeuverOptimalFinite)
        optFinite.seed_method = OPTIMAL_FINITE_SEED_METHOD.FINITE_MANEUVER
        optFinite.run_seed()

        # Engine tab

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            optFinite.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, "bogus")
        optFinite.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, "Polynomial Thrust and Isp")
        Assert.assertEqual(PROPULSION_METHOD.ENGINE_MODEL, optFinite.propulsion_method)
        Assert.assertEqual("Polynomial Thrust and Isp", optFinite.propulsion_method_value)
        optFinite.set_propulsion_method(PROPULSION_METHOD.ENGINE_MODEL, "Throttle Table Engine")
        Assert.assertEqual(PROPULSION_METHOD.ENGINE_MODEL, optFinite.propulsion_method)
        Assert.assertEqual("Throttle Table Engine", optFinite.propulsion_method_value)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            optFinite.set_propulsion_method(PROPULSION_METHOD.THRUSTER_SET, "bogus")
        optFinite.set_propulsion_method(PROPULSION_METHOD.THRUSTER_SET, "Single Thruster")
        Assert.assertEqual(PROPULSION_METHOD.THRUSTER_SET, optFinite.propulsion_method)
        Assert.assertEqual("Single Thruster", optFinite.propulsion_method_value)
        optFinite.set_propulsion_method(PROPULSION_METHOD.THRUSTER_SET, "Thruster Set")
        Assert.assertEqual(PROPULSION_METHOD.THRUSTER_SET, optFinite.propulsion_method)
        Assert.assertEqual("Thruster Set", optFinite.propulsion_method_value)

        optFinite.pressure_mode = PRESSURE_MODE.BLOW_DOWN
        Assert.assertEqual(PRESSURE_MODE.BLOW_DOWN, optFinite.pressure_mode)
        optFinite.pressure_mode = PRESSURE_MODE.PRESSURE_REGULATED
        Assert.assertEqual(PRESSURE_MODE.PRESSURE_REGULATED, optFinite.pressure_mode)

        optFinite.thrust_efficiency = 0
        Assert.assertEqual(0, optFinite.thrust_efficiency)
        optFinite.thrust_efficiency = 10
        Assert.assertEqual(10, optFinite.thrust_efficiency)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            optFinite.thrust_efficiency = -1

        optFinite.thrust_efficiency_mode = THRUST_TYPE.AFFECTS_ACCEL_AND_MASS_FLOW
        Assert.assertEqual(THRUST_TYPE.AFFECTS_ACCEL_AND_MASS_FLOW, optFinite.thrust_efficiency_mode)
        optFinite.thrust_efficiency_mode = THRUST_TYPE.AFFECTS_ACCEL_ONLY
        Assert.assertEqual(THRUST_TYPE.AFFECTS_ACCEL_ONLY, optFinite.thrust_efficiency_mode)

        # Solver tab

        optFinite.number_of_nodes = 3
        Assert.assertEqual(3, optFinite.number_of_nodes)
        optFinite.number_of_nodes = 10
        Assert.assertEqual(10, optFinite.number_of_nodes)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            optFinite.number_of_nodes = 2

        optFinite.discretization_strategy = OPTIMAL_FINITE_DISCRETIZATION_STRATEGY.LEGENDRE_GAUSS_LOBATTO
        Assert.assertEqual(
            OPTIMAL_FINITE_DISCRETIZATION_STRATEGY.LEGENDRE_GAUSS_LOBATTO, optFinite.discretization_strategy
        )
        optFinite.discretization_strategy = OPTIMAL_FINITE_DISCRETIZATION_STRATEGY.LEGENDRE_GAUSS_RADAU
        Assert.assertEqual(
            OPTIMAL_FINITE_DISCRETIZATION_STRATEGY.LEGENDRE_GAUSS_RADAU, optFinite.discretization_strategy
        )

        optFinite.working_variables = OPTIMAL_FINITE_WORKING_VARIABLES.EQUINOCTIAL
        Assert.assertEqual(OPTIMAL_FINITE_WORKING_VARIABLES.EQUINOCTIAL, optFinite.working_variables)
        optFinite.working_variables = OPTIMAL_FINITE_WORKING_VARIABLES.MODIFIED_EQUINOCTIAL
        Assert.assertEqual(OPTIMAL_FINITE_WORKING_VARIABLES.MODIFIED_EQUINOCTIAL, optFinite.working_variables)

        optFinite.scaling_options = OPTIMAL_FINITE_SCALING_OPTIONS.NO_SCALING
        Assert.assertEqual(OPTIMAL_FINITE_SCALING_OPTIONS.NO_SCALING, optFinite.scaling_options)
        optFinite.scaling_options = OPTIMAL_FINITE_SCALING_OPTIONS.INITIAL_STATE_BASED
        Assert.assertEqual(OPTIMAL_FINITE_SCALING_OPTIONS.INITIAL_STATE_BASED, optFinite.scaling_options)
        optFinite.scaling_options = OPTIMAL_FINITE_SCALING_OPTIONS.CANONICAL_UNITS
        Assert.assertEqual(OPTIMAL_FINITE_SCALING_OPTIONS.CANONICAL_UNITS, optFinite.scaling_options)

        optFinite.initial_guess_interpolation_method = OPTIMAL_FINITE_GUESS_METHOD.LAGRANGE_POLYNOMIAL
        Assert.assertEqual(
            OPTIMAL_FINITE_GUESS_METHOD.LAGRANGE_POLYNOMIAL, optFinite.initial_guess_interpolation_method
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            optFinite.initial_guess_interpolation_method = OPTIMAL_FINITE_GUESS_METHOD.PIECEWISE_LINEAR

        optFinite.enable_unit_vector_controls = True
        Assert.assertTrue(optFinite.enable_unit_vector_controls)
        optFinite.enable_unit_vector_controls = False
        Assert.assertFalse(optFinite.enable_unit_vector_controls)

        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            optFinite.initial_guess_file_name = TestBase.GetScenarioFile("bogus.nod")
        optFinite.initial_guess_file_name = TestBase.GetScenarioFile("intervals.int")  # invalid file
        Assert.assertTrue(("intervals.int" in optFinite.initial_guess_file_name))

        optFinite.seed_method = OPTIMAL_FINITE_SEED_METHOD.INITIAL_GUESS_FILE
        Assert.assertEqual(OPTIMAL_FINITE_SEED_METHOD.INITIAL_GUESS_FILE, optFinite.seed_method)
        optFinite.seed_method = OPTIMAL_FINITE_SEED_METHOD.FINITE_MANEUVER
        Assert.assertEqual(OPTIMAL_FINITE_SEED_METHOD.FINITE_MANEUVER, optFinite.seed_method)

        Assert.assertEqual("50 nodes seeded from finite maneuver.", optFinite.node_status_message)

        GatorHelper.Test_IAgVAManeuverOptimalFiniteInitialBoundaryConditions(optFinite.initial_boundary_conditions)
        GatorHelper.Test_IAgVAManeuverOptimalFiniteFinalBoundaryConditions(optFinite.final_boundary_conditions)
        GatorHelper.Test_IAgVAManeuverOptimalFinitePathBoundaryConditions(optFinite.path_boundary_conditions)

        optFinite.run_mode = OPTIMAL_FINITE_RUN_MODE.RUN_CURRENT_NODES
        Assert.assertEqual(OPTIMAL_FINITE_RUN_MODE.RUN_CURRENT_NODES, optFinite.run_mode)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            optFinite.halt_mission_control_sequence_when_no_convergence = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            GatorHelper.Test_IAgVAManeuverOptimalFiniteSNOPTOptimizer(optFinite.snopt_optimizer)

        optFinite.run_mode = OPTIMAL_FINITE_RUN_MODE.OPTIMIZE_VIA_DIRECT_TRANSCRIPTION
        Assert.assertEqual(OPTIMAL_FINITE_RUN_MODE.OPTIMIZE_VIA_DIRECT_TRANSCRIPTION, optFinite.run_mode)

        GatorHelper.Test_IAgVAManeuverOptimalFiniteSNOPTOptimizer(optFinite.snopt_optimizer)

        optFinite.halt_mission_control_sequence_when_no_convergence = False
        Assert.assertFalse(optFinite.halt_mission_control_sequence_when_no_convergence)
        optFinite.halt_mission_control_sequence_when_no_convergence = True
        Assert.assertTrue(optFinite.halt_mission_control_sequence_when_no_convergence)

        # Log tab
        Assert.assertEqual(" -log file not available- ", optFinite.log_file_name)

        # Steering/Nodes tab

        optFinite.export_format = OPTIMAL_FINITE_EXPORT_NODES_FORMAT.AZIMUTH_ELEVATION
        Assert.assertEqual(OPTIMAL_FINITE_EXPORT_NODES_FORMAT.AZIMUTH_ELEVATION, optFinite.export_format)
        filename: str = Path.Combine(Path.GetTempPath(), "AzimuthElevation.nod")
        optFinite.export_nodes(filename)

        optFinite.export_format = OPTIMAL_FINITE_EXPORT_NODES_FORMAT.UNIT_VECTOR
        Assert.assertEqual(OPTIMAL_FINITE_EXPORT_NODES_FORMAT.UNIT_VECTOR, optFinite.export_format)
        filename = Path.Combine(Path.GetTempPath(), "UnitVector.nod")
        optFinite.export_nodes(filename)

        steeringNodesColl: "ManeuverOptimalFiniteSteeringNodeCollection" = optFinite.steering_nodes

        i: int = 0
        while i < steeringNodesColl.count:
            elem: "ManeuverOptimalFiniteSteeringNodeElement" = steeringNodesColl[i]
            Console.WriteLine(
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            (
                                                                                (
                                                                                    (
                                                                                        (
                                                                                            (
                                                                                                (
                                                                                                    (
                                                                                                        (
                                                                                                            (
                                                                                                                (
                                                                                                                    (
                                                                                                                        (
                                                                                                                            str(
                                                                                                                                elem.node_index
                                                                                                                            )
                                                                                                                            + "  "
                                                                                                                        )
                                                                                                                        + Double.ToString(
                                                                                                                            elem.time
                                                                                                                        )
                                                                                                                    )
                                                                                                                    + "  "
                                                                                                                )
                                                                                                                + Double.ToString(
                                                                                                                    elem.mass
                                                                                                                )
                                                                                                            )
                                                                                                            + "  "
                                                                                                        )
                                                                                                        + Double.ToString(
                                                                                                            elem.azimuth
                                                                                                        )
                                                                                                    )
                                                                                                    + "  "
                                                                                                )
                                                                                                + Double.ToString(
                                                                                                    elem.elevation
                                                                                                )
                                                                                            )
                                                                                            + "  "
                                                                                        )
                                                                                        + Double.ToString(
                                                                                            elem.direction_cos_x
                                                                                        )
                                                                                    )
                                                                                    + "  "
                                                                                )
                                                                                + Double.ToString(elem.direction_cos_y)
                                                                            )
                                                                            + "  "
                                                                        )
                                                                        + Double.ToString(elem.direction_cos_z)
                                                                    )
                                                                    + "  "
                                                                )
                                                                + Double.ToString(elem.position_x)
                                                            )
                                                            + "  "
                                                        )
                                                        + Double.ToString(elem.position_y)
                                                    )
                                                    + "  "
                                                )
                                                + Double.ToString(elem.position_z)
                                            )
                                            + "  "
                                        )
                                        + Double.ToString(elem.vel_x)
                                    )
                                    + "  "
                                )
                                + Double.ToString(elem.vel_y)
                            )
                            + "  "
                        )
                        + Double.ToString(elem.vel_z)
                    )
                    + "  "
                )
            )

            i += 1

        elem: "ManeuverOptimalFiniteSteeringNodeElement"

        for elem in steeringNodesColl:
            Console.WriteLine(
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            (
                                                                                (
                                                                                    (
                                                                                        (
                                                                                            (
                                                                                                (
                                                                                                    (
                                                                                                        (
                                                                                                            (
                                                                                                                (
                                                                                                                    (
                                                                                                                        (
                                                                                                                            str(
                                                                                                                                elem.node_index
                                                                                                                            )
                                                                                                                            + "  "
                                                                                                                        )
                                                                                                                        + Double.ToString(
                                                                                                                            elem.time
                                                                                                                        )
                                                                                                                    )
                                                                                                                    + "  "
                                                                                                                )
                                                                                                                + Double.ToString(
                                                                                                                    elem.mass
                                                                                                                )
                                                                                                            )
                                                                                                            + "  "
                                                                                                        )
                                                                                                        + Double.ToString(
                                                                                                            elem.azimuth
                                                                                                        )
                                                                                                    )
                                                                                                    + "  "
                                                                                                )
                                                                                                + Double.ToString(
                                                                                                    elem.elevation
                                                                                                )
                                                                                            )
                                                                                            + "  "
                                                                                        )
                                                                                        + Double.ToString(
                                                                                            elem.direction_cos_x
                                                                                        )
                                                                                    )
                                                                                    + "  "
                                                                                )
                                                                                + Double.ToString(elem.direction_cos_y)
                                                                            )
                                                                            + "  "
                                                                        )
                                                                        + Double.ToString(elem.direction_cos_z)
                                                                    )
                                                                    + "  "
                                                                )
                                                                + Double.ToString(elem.position_x)
                                                            )
                                                            + "  "
                                                        )
                                                        + Double.ToString(elem.position_y)
                                                    )
                                                    + "  "
                                                )
                                                + Double.ToString(elem.position_z)
                                            )
                                            + "  "
                                        )
                                        + Double.ToString(elem.vel_x)
                                    )
                                    + "  "
                                )
                                + Double.ToString(elem.vel_y)
                            )
                            + "  "
                        )
                        + Double.ToString(elem.vel_z)
                    )
                    + "  "
                )
            )

        # Steering/Nodes tab - "Advanced" button - (More Attitude Options)

        lagrange: "AttitudeControlOptimalFiniteLagrange" = clr.CastAs(
            optFinite.attitude_control, AttitudeControlOptimalFiniteLagrange
        )

        lagrange.custom_function = CUSTOM_FUNCTION.ENABLE_PAGE_DEFINITION
        Assert.assertEqual(CUSTOM_FUNCTION.ENABLE_PAGE_DEFINITION, lagrange.custom_function)
        lagrange.custom_function = CUSTOM_FUNCTION.ENABLE_MANEUVER_ATTITUDE
        Assert.assertEqual(CUSTOM_FUNCTION.ENABLE_MANEUVER_ATTITUDE, lagrange.custom_function)

        optFinite.set_propulsion_method(
            PROPULSION_METHOD.ENGINE_MODEL, "Polynomial Thrust and Isp"
        )  # needed to see BodyAxis
        Assert.assertEqual(PROPULSION_METHOD.ENGINE_MODEL, optFinite.propulsion_method)
        lagrange.body_axis = BODY_AXIS.MINUS_X
        Assert.assertEqual(BODY_AXIS.MINUS_X, lagrange.body_axis)
        lagrange.body_axis = BODY_AXIS.MINUS_Y
        Assert.assertEqual(BODY_AXIS.MINUS_Y, lagrange.body_axis)
        lagrange.body_axis = BODY_AXIS.MINUS_Z
        Assert.assertEqual(BODY_AXIS.MINUS_Z, lagrange.body_axis)
        lagrange.body_axis = BODY_AXIS.PLUS_X
        Assert.assertEqual(BODY_AXIS.PLUS_X, lagrange.body_axis)
        lagrange.body_axis = BODY_AXIS.PLUS_Y
        Assert.assertEqual(BODY_AXIS.PLUS_Y, lagrange.body_axis)
        lagrange.body_axis = BODY_AXIS.PLUS_Z
        Assert.assertEqual(BODY_AXIS.PLUS_Z, lagrange.body_axis)

        lagrange.body_constraint_vector.assign_xyz(1, 2, 3)

        x: float = 0
        y: float = 0
        z: float = 0

        (x, y, z) = lagrange.body_constraint_vector.query_xyz()
        Assert.assertEqual(1, x)
        Assert.assertEqual(2, y)
        Assert.assertEqual(3, z)

        lagrange.constraint_sign = CONSTRAINT_SIGN.MINUS
        Assert.assertEqual(CONSTRAINT_SIGN.MINUS, lagrange.constraint_sign)
        lagrange.constraint_sign = CONSTRAINT_SIGN.PLUS
        Assert.assertEqual(CONSTRAINT_SIGN.PLUS, lagrange.constraint_sign)

        lagrange.constraint_vector_name = "CentralBody/Earth ICRF-Z"
        Assert.assertEqual("CentralBody/Earth ICRF-Z", lagrange.constraint_vector_name)

        lagrange.lead_duration = 10
        Assert.assertEqual(10, lagrange.lead_duration)

        lagrange.trail_duration = 20
        Assert.assertEqual(20, lagrange.trail_duration)

    @staticmethod
    def Test_IAgVAManeuverOptimalFiniteInitialBoundaryConditions(
        initBoundary: "ManeuverOptimalFiniteInitialBoundaryConditions",
    ):
        initBoundary.set_from_initial_guess = True
        Assert.assertTrue(initBoundary.set_from_initial_guess)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.a.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.a.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.h.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.h.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.k.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.k.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.p.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.p.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.q.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.q.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.l.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            initBoundary.l.upper_bound = 1

        initBoundary.set_from_initial_guess = False
        Assert.assertFalse(initBoundary.set_from_initial_guess)

        initBoundary.a.lower_bound = 6000
        Assert.assertEqual(6000, initBoundary.a.lower_bound)
        initBoundary.a.upper_bound = 7000
        Assert.assertEqual(7000, initBoundary.a.upper_bound)

        initBoundary.h.lower_bound = -0.5
        Assert.assertEqual(-0.5, initBoundary.h.lower_bound)
        initBoundary.h.upper_bound = 0.5
        Assert.assertEqual(0.5, initBoundary.h.upper_bound)

        initBoundary.k.lower_bound = -0.5
        Assert.assertEqual(-0.5, initBoundary.k.lower_bound)
        initBoundary.k.upper_bound = 0.5
        Assert.assertEqual(0.5, initBoundary.k.upper_bound)

        initBoundary.p.lower_bound = -10
        Assert.assertEqual(-10, initBoundary.p.lower_bound)
        initBoundary.p.upper_bound = 10
        Assert.assertEqual(10, initBoundary.p.upper_bound)

        initBoundary.q.lower_bound = -5
        Assert.assertEqual(-5, initBoundary.q.lower_bound)
        initBoundary.q.upper_bound = 5
        Assert.assertEqual(5, initBoundary.q.upper_bound)

        initBoundary.l.lower_bound = -20
        Assert.assertEqual(-20, initBoundary.l.lower_bound)
        initBoundary.l.upper_bound = 20
        Assert.assertEqual(20, initBoundary.l.upper_bound)

    @staticmethod
    def Test_IAgVAManeuverOptimalFiniteFinalBoundaryConditions(
        finalBoundary: "ManeuverOptimalFiniteFinalBoundaryConditions",
    ):
        finalBoundary.set_from_final_guess = True
        Assert.assertTrue(finalBoundary.set_from_final_guess)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.a.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.a.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.h.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.h.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.k.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.k.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.p.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.p.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.q.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.q.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.l.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            finalBoundary.l.upper_bound = 1

        finalBoundary.set_from_final_guess = False
        Assert.assertFalse(finalBoundary.set_from_final_guess)

        finalBoundary.a.lower_bound = 6000
        Assert.assertEqual(6000, finalBoundary.a.lower_bound)
        finalBoundary.a.upper_bound = 7000
        Assert.assertEqual(7000, finalBoundary.a.upper_bound)

        finalBoundary.h.lower_bound = -0.5
        Assert.assertEqual(-0.5, finalBoundary.h.lower_bound)
        finalBoundary.h.upper_bound = 0.5
        Assert.assertEqual(0.5, finalBoundary.h.upper_bound)

        finalBoundary.k.lower_bound = -0.5
        Assert.assertEqual(-0.5, finalBoundary.k.lower_bound)
        finalBoundary.k.upper_bound = 0.5
        Assert.assertEqual(0.5, finalBoundary.k.upper_bound)

        finalBoundary.p.lower_bound = -10
        Assert.assertEqual(-10, finalBoundary.p.lower_bound)
        finalBoundary.p.upper_bound = 10
        Assert.assertEqual(10, finalBoundary.p.upper_bound)

        finalBoundary.q.lower_bound = -5
        Assert.assertEqual(-5, finalBoundary.q.lower_bound)
        finalBoundary.q.upper_bound = 5
        Assert.assertEqual(5, finalBoundary.q.upper_bound)

        finalBoundary.l.lower_bound = -20
        Assert.assertEqual(-20, finalBoundary.l.lower_bound)
        finalBoundary.l.upper_bound = 20
        Assert.assertEqual(20, finalBoundary.l.upper_bound)

        finalBoundary.lower_delta_final_time = 1.0
        Assert.assertEqual(1.0, finalBoundary.lower_delta_final_time)
        finalBoundary.upper_delta_final_time = 2.0
        Assert.assertEqual(2.0, finalBoundary.upper_delta_final_time)

    @staticmethod
    def Test_IAgVAManeuverOptimalFinitePathBoundaryConditions(
        pathBoundary: "ManeuverOptimalFinitePathBoundaryConditions",
    ):
        pathBoundary.compute_from_initial_guess = True
        Assert.assertTrue(pathBoundary.compute_from_initial_guess)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.a.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.a.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.h.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.h.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.k.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.k.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.p.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.p.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.q.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.q.upper_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.l.lower_bound = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            pathBoundary.l.upper_bound = 1

        pathBoundary.compute_from_initial_guess = False
        Assert.assertFalse(pathBoundary.compute_from_initial_guess)

        pathBoundary.a.lower_bound = 6000
        Assert.assertEqual(6000, pathBoundary.a.lower_bound)
        pathBoundary.a.upper_bound = 7000
        Assert.assertEqual(7000, pathBoundary.a.upper_bound)

        pathBoundary.h.lower_bound = -0.5
        Assert.assertEqual(-0.5, pathBoundary.h.lower_bound)
        pathBoundary.h.upper_bound = 0.5
        Assert.assertEqual(0.5, pathBoundary.h.upper_bound)

        pathBoundary.k.lower_bound = -0.5
        Assert.assertEqual(-0.5, pathBoundary.k.lower_bound)
        pathBoundary.k.upper_bound = 0.5
        Assert.assertEqual(0.5, pathBoundary.k.upper_bound)

        pathBoundary.p.lower_bound = -10
        Assert.assertEqual(-10, pathBoundary.p.lower_bound)
        pathBoundary.p.upper_bound = 10
        Assert.assertEqual(10, pathBoundary.p.upper_bound)

        pathBoundary.q.lower_bound = -5
        Assert.assertEqual(-5, pathBoundary.q.lower_bound)
        pathBoundary.q.upper_bound = 5
        Assert.assertEqual(5, pathBoundary.q.upper_bound)

        pathBoundary.l.lower_bound = -20
        Assert.assertEqual(-20, pathBoundary.l.lower_bound)
        pathBoundary.l.upper_bound = 20
        Assert.assertEqual(20, pathBoundary.l.upper_bound)

        pathBoundary.lower_bound_azimuth = 1.0
        Assert.assertEqual(1.0, pathBoundary.lower_bound_azimuth)
        pathBoundary.upper_bound_azimuth = 2.0
        Assert.assertEqual(2.0, pathBoundary.upper_bound_azimuth)

        # EnableUnitVectorControls must be false to see the below properties
        # ModifiedEquinoctial must be set to see the below properties?

        pathBoundary.upper_bound_azimuth = 3.0
        Assert.assertEqual(3.0, pathBoundary.upper_bound_azimuth)
        pathBoundary.lower_bound_azimuth = 2.0
        Assert.assertEqual(2.0, pathBoundary.lower_bound_azimuth)

        pathBoundary.upper_bound_elevation = 20.0
        Assert.assertEqual(20.0, pathBoundary.upper_bound_elevation)
        pathBoundary.lower_bound_elevation = 10.0
        Assert.assertEqual(10.0, pathBoundary.lower_bound_elevation)

    @staticmethod
    def Test_IAgVAManeuverOptimalFiniteSNOPTOptimizer(optimizer: "ManeuverOptimalFiniteSNOPTOptimizer"):
        optimizer.objective = OPTIMAL_FINITE_SNOPT_OBJECTIVE.MINIMIZE_TOF
        Assert.assertEqual(OPTIMAL_FINITE_SNOPT_OBJECTIVE.MINIMIZE_TOF, optimizer.objective)
        optimizer.objective = OPTIMAL_FINITE_SNOPT_OBJECTIVE.MINIMIZE_PROPELLANT_USE
        Assert.assertEqual(OPTIMAL_FINITE_SNOPT_OBJECTIVE.MINIMIZE_PROPELLANT_USE, optimizer.objective)
        optimizer.objective = OPTIMAL_FINITE_SNOPT_OBJECTIVE.MAXIMIZE_FINAL_RAD
        Assert.assertEqual(OPTIMAL_FINITE_SNOPT_OBJECTIVE.MAXIMIZE_FINAL_RAD, optimizer.objective)

        optimizer.max_major_iterations = 1
        Assert.assertEqual(1, optimizer.max_major_iterations)
        optimizer.max_major_iterations = 10
        Assert.assertEqual(10, optimizer.max_major_iterations)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            optimizer.max_major_iterations = 0

        optimizer.tolerance_on_major_feasibility = 1e-15
        Assert.assertEqual(1e-15, optimizer.tolerance_on_major_feasibility)
        optimizer.tolerance_on_major_feasibility = 1e-05
        Assert.assertEqual(1e-05, optimizer.tolerance_on_major_feasibility)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            optimizer.tolerance_on_major_feasibility = 0

        optimizer.tolerance_on_major_optimality = 1e-15
        Assert.assertEqual(1e-15, optimizer.tolerance_on_major_optimality)
        optimizer.tolerance_on_major_optimality = 0.0001
        Assert.assertEqual(0.0001, optimizer.tolerance_on_major_optimality)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            optimizer.tolerance_on_major_optimality = 0

        optimizer.max_minor_iterations = 1
        Assert.assertEqual(1, optimizer.max_minor_iterations)
        optimizer.max_minor_iterations = 10
        Assert.assertEqual(10, optimizer.max_minor_iterations)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            optimizer.max_minor_iterations = 0

        optimizer.tolerance_on_minor_feasibility = 1e-15
        Assert.assertEqual(1e-15, optimizer.tolerance_on_minor_feasibility)
        optimizer.tolerance_on_minor_feasibility = 0.001
        Assert.assertEqual(0.001, optimizer.tolerance_on_minor_feasibility)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            optimizer.tolerance_on_minor_feasibility = 0

        optimizer.snopt_scaling = OPTIMAL_FINITE_SNOPT_SCALING.NONE
        Assert.assertEqual(OPTIMAL_FINITE_SNOPT_SCALING.NONE, optimizer.snopt_scaling)
        optimizer.snopt_scaling = OPTIMAL_FINITE_SNOPT_SCALING.LINEAR
        Assert.assertEqual(OPTIMAL_FINITE_SNOPT_SCALING.LINEAR, optimizer.snopt_scaling)
        optimizer.snopt_scaling = OPTIMAL_FINITE_SNOPT_SCALING.ALL
        Assert.assertEqual(OPTIMAL_FINITE_SNOPT_SCALING.ALL, optimizer.snopt_scaling)

        optimizer.allow_internal_primal_infeasibility_measure_normalization = False
        Assert.assertFalse(optimizer.allow_internal_primal_infeasibility_measure_normalization)
        optimizer.allow_internal_primal_infeasibility_measure_normalization = True
        Assert.assertTrue(optimizer.allow_internal_primal_infeasibility_measure_normalization)

        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            optimizer.options_filename = r"C:\Pat\bogus.txt"
        optimizer.options_filename = TestBase.GetScenarioFile("gp_marker.bmp")
        Assert.assertTrue(("gp_marker.bmp" in optimizer.options_filename))

        optimizer.use_console_monitor = False
        Assert.assertFalse(optimizer.use_console_monitor)
        optimizer.use_console_monitor = True
        Assert.assertTrue(optimizer.use_console_monitor)

    @staticmethod
    def TestPropagate(propagate: "MissionControlSequencePropagate", isFromCM: bool):
        segment: "IMissionControlSequenceSegment" = clr.CastAs(propagate, IMissionControlSequenceSegment)

        Assert.assertEqual(SEGMENT_TYPE.PROPAGATE, segment.type)
        GatorHelper.m_logger.WriteLine(propagate.propagator_name)
        propagate.propagator_name = "Earth Point Mass"
        Assert.assertEqual("Earth Point Mass", propagate.propagator_name)
        GatorHelper.TestStoppingConditionCollection(propagate.stopping_conditions)

        propagate.min_propagation_time = 0
        Assert.assertEqual(0, propagate.min_propagation_time)
        propagate.max_propagation_time = 2
        Assert.assertEqual(2, propagate.max_propagation_time)
        propagate.enable_warning_message = False
        Assert.assertFalse(propagate.enable_warning_message)
        propagate.override_max_propagation_time = False
        Assert.assertFalse(propagate.override_max_propagation_time)
        propagate.override_max_propagation_time = True
        Assert.assertTrue(propagate.override_max_propagation_time)
        propagate.enable_max_propagation_time = False
        Assert.assertFalse(propagate.enable_max_propagation_time)

        propagate.should_stop_for_initially_surpassed_epoch_stopping_conditions = True
        Assert.assertTrue(propagate.should_stop_for_initially_surpassed_epoch_stopping_conditions)
        propagate.should_stop_for_initially_surpassed_epoch_stopping_conditions = False
        Assert.assertFalse(propagate.should_stop_for_initially_surpassed_epoch_stopping_conditions)

    @staticmethod
    def TestSpaceCraftParameters(scParams: "SpacecraftParameters", isReadOnly: bool):
        GatorHelper.TestRuntimeTypeInfo(scParams)
        if isReadOnly:
            with pytest.raises(Exception):
                scParams.cd = 2.3
            with pytest.raises(Exception):
                scParams.ck = 1.1
            with pytest.raises(Exception):
                scParams.cr = 1.3
            with pytest.raises(Exception):
                scParams.drag_area = 21
            with pytest.raises(Exception):
                scParams.dry_mass = 501
            with pytest.raises(Exception):
                scParams.k1 = 2
            with pytest.raises(Exception):
                scParams.k2 = 3
            with pytest.raises(Exception):
                scParams.radiation_pressure_area = 23
            with pytest.raises(Exception):
                scParams.solar_radiation_pressure_area = 2.3

        else:
            scParams.cd = 2.3
            Assert.assertEqual(2.3, scParams.cd)
            scParams.ck = 1.1
            Assert.assertEqual(1.1, scParams.ck)
            scParams.cr = 1.3
            Assert.assertEqual(1.3, scParams.cr)
            scParams.drag_area = 21
            Assert.assertEqual(21, scParams.drag_area)
            scParams.dry_mass = 501
            Assert.assertEqual(501, scParams.dry_mass)
            scParams.k1 = 2
            Assert.assertEqual(2, scParams.k1)
            scParams.k2 = 3
            Assert.assertEqual(3, scParams.k2)
            scParams.radiation_pressure_area = 23
            Assert.assertEqual(23, scParams.radiation_pressure_area)
            scParams.solar_radiation_pressure_area = 22
            Assert.assertEqual(22, scParams.solar_radiation_pressure_area)

    @staticmethod
    def TestFuelTank(fuel: "FuelTank", isReadOnly: bool, isFromCM: bool):
        GatorHelper.TestRuntimeTypeInfo(fuel)
        if isReadOnly:
            with pytest.raises(Exception):
                fuel.fuel_density = 1001
            with pytest.raises(Exception):
                fuel.fuel_mass = 500
            with pytest.raises(Exception):
                fuel.maximum_fuel_mass = 1501
            with pytest.raises(Exception):
                fuel.tank_pressure = 5001
            with pytest.raises(Exception):
                fuel.tank_temperature = 292
            with pytest.raises(Exception):
                fuel.tank_volume = 1.4
            GatorHelper.m_logger.WriteLine2(fuel.fuel_density)
            GatorHelper.m_logger.WriteLine2(fuel.fuel_mass)
            GatorHelper.m_logger.WriteLine2(fuel.maximum_fuel_mass)
            GatorHelper.m_logger.WriteLine2(fuel.tank_pressure)
            GatorHelper.m_logger.WriteLine2(fuel.tank_temperature)
            GatorHelper.m_logger.WriteLine2(fuel.tank_volume)

        else:
            fuel.fuel_density = 1001
            Assert.assertEqual(1001, fuel.fuel_density)
            fuel.fuel_mass = 501
            Assert.assertEqual(501, fuel.fuel_mass)
            fuel.tank_pressure = 5001
            Assert.assertEqual(5001, fuel.tank_pressure)
            fuel.tank_temperature = 292
            Assert.assertEqual(292, fuel.tank_temperature)
            if isFromCM:
                with pytest.raises(Exception):
                    fuel.tank_volume = 1.4
                with pytest.raises(Exception):
                    fuel.maximum_fuel_mass = 1501

            else:
                fuel.maximum_fuel_mass = 1501
                Assert.assertEqual(1501, fuel.maximum_fuel_mass)
                fuel.tank_volume = 1.4
                Assert.assertEqual(1.4, fuel.tank_volume)

    # TODO check readonly as well.
    @staticmethod
    def TestLaunch(launch: "MissionControlSequenceLaunch", isFromCM: bool):
        segment: "IMissionControlSequenceSegment" = clr.CastAs(launch, IMissionControlSequenceSegment)

        Assert.assertEqual(SEGMENT_TYPE.LAUNCH, segment.type)
        launch.central_body_name = "Mars"
        Assert.assertEqual("Mars", launch.central_body_name)
        GatorHelper.TestFuelTank(launch.fuel_tank, False, isFromCM)
        GatorHelper.TestSpaceCraftParameters(launch.spacecraft_parameters, False)
        launch.epoch = "1 Jul 2006 14:00:01.000"
        Assert.assertEqual("1 Jul 2006 14:00:01.000", launch.epoch)
        sEpoch: str = str(segment.get_result_value("Epoch"))
        launch.step_size = 6
        Assert.assertEqual(6, launch.step_size)
        launch.pre_launch_time = 1
        Assert.assertEqual(1, launch.pre_launch_time)

        launch.time_of_flight = 500
        Assert.assertEqual(500, launch.time_of_flight)
        launch.time_of_flight = 600
        Assert.assertEqual(600, launch.time_of_flight)

        launch.use_previous_segment_state = True
        Assert.assertTrue(launch.use_previous_segment_state)
        launch.use_previous_segment_state = False
        Assert.assertFalse(launch.use_previous_segment_state)

        launch.set_display_system_type(LAUNCH_DISPLAY_SYSTEM.DISPLAY_SYSTEM_GEOCENTRIC)
        Assert.assertEqual(LAUNCH_DISPLAY_SYSTEM.DISPLAY_SYSTEM_GEOCENTRIC, launch.display_system_type)
        llr: "DisplaySystemGeocentric" = DisplaySystemGeocentric(launch.display_system)
        llr.latitude = 29
        Assert.assertAlmostEqual(29, float(llr.latitude), delta=1e-08)
        llr.longitude = -81
        Assert.assertEqual(-81, llr.longitude)
        llr.radius = 3400
        Assert.assertAlmostEqual(3400, float(llr.radius), delta=1e-08)

        launch.set_display_system_type(LAUNCH_DISPLAY_SYSTEM.DISPLAY_SYSTEM_GEODETIC)
        Assert.assertEqual(LAUNCH_DISPLAY_SYSTEM.DISPLAY_SYSTEM_GEODETIC, launch.display_system_type)
        lla: "DisplaySystemGeodetic" = DisplaySystemGeodetic(launch.display_system)
        lla.latitude = 30
        Assert.assertAlmostEqual(30, float(lla.latitude), delta=1e-08)
        lla.longitude = -82
        Assert.assertEqual(-82, lla.longitude)
        lla.altitude = 1
        Assert.assertEqual(1, lla.altitude)

        launch.ascent_type = ASCENT_TYPE.ELLIPSE_QUARTIC_MOTION
        Assert.assertEqual(ASCENT_TYPE.ELLIPSE_QUARTIC_MOTION, launch.ascent_type)
        launch.initial_acceleration = 0.02
        Assert.assertEqual(0.02, launch.initial_acceleration)
        launch.ascent_type = ASCENT_TYPE.ELLIPSE_CUBIC_MOTION
        Assert.assertEqual(ASCENT_TYPE.ELLIPSE_CUBIC_MOTION, launch.ascent_type)

        launch.set_burnout_type(BURNOUT_TYPE.GEOCENTRIC)
        Assert.assertEqual(BURNOUT_TYPE.GEOCENTRIC, launch.burnout_type)
        bLLR: "BurnoutGeocentric" = BurnoutGeocentric(launch.burnout)
        bLLR.latitude = 30
        Assert.assertAlmostEqual(30, float(bLLR.latitude), delta=1e-08)
        bLLR.longitude = 31
        Assert.assertAlmostEqual(31, float(bLLR.longitude), delta=Math2.Epsilon12)
        bLLR.radius = 3000
        Assert.assertAlmostEqual(3000, bLLR.radius, delta=Math2.Epsilon10)

        launch.set_burnout_type(BURNOUT_TYPE.GEODETIC)
        Assert.assertEqual(BURNOUT_TYPE.GEODETIC, launch.burnout_type)
        bLLA: "BurnoutGeodetic" = BurnoutGeodetic(launch.burnout)
        bLLA.latitude = 32
        Assert.assertEqual(32, bLLA.latitude)
        bLLA.longitude = 34
        Assert.assertEqual(34, bLLA.longitude)
        bLLA.altitude = 20
        Assert.assertEqual(20, bLLA.altitude)

        launch.set_burnout_type(BURNOUT_TYPE.LAUNCH_AZ_ALTITUDE)
        Assert.assertEqual(BURNOUT_TYPE.LAUNCH_AZ_ALTITUDE, launch.burnout_type)
        azAlt: "BurnoutLaunchAzAltitude" = BurnoutLaunchAzAltitude(launch.burnout)
        azAlt.azimuth = 30
        Assert.assertAlmostEqual(30, float(azAlt.azimuth), delta=1e-08)
        azAlt.down_range_dist = 1
        Assert.assertAlmostEqual(1, float(azAlt.down_range_dist), delta=0.001)
        azAlt.altitude_radius = 2000
        Assert.assertEqual(2000, azAlt.altitude_radius)

        launch.set_burnout_type(BURNOUT_TYPE.LAUNCH_AZ_RAD)
        Assert.assertEqual(BURNOUT_TYPE.LAUNCH_AZ_RAD, launch.burnout_type)
        azRad: "BurnoutLaunchAzRadius" = BurnoutLaunchAzRadius(launch.burnout)
        azRad.azimuth = 30
        Assert.assertAlmostEqual(30, float(azRad.azimuth), delta=0.001)
        azRad.down_range_dist = 1
        Assert.assertAlmostEqual(1, float(azRad.down_range_dist), delta=0.001)
        azRad.radius = 2000
        Assert.assertAlmostEqual(2000, azRad.radius, delta=Math2.Epsilon11)

        launch.set_burnout_type(BURNOUT_TYPE.CBF_CARTESIAN)
        Assert.assertEqual(BURNOUT_TYPE.CBF_CARTESIAN, launch.burnout_type)
        cartesian: "BurnoutCBFCartesian" = clr.CastAs(launch.burnout, BurnoutCBFCartesian)
        cartesian.cartesian_burnout_x = 1
        Assert.assertEqual(1, cartesian.cartesian_burnout_x)
        cartesian.cartesian_burnout_y = 2
        Assert.assertEqual(2, cartesian.cartesian_burnout_y)
        cartesian.cartesian_burnout_z = 3
        Assert.assertEqual(3, cartesian.cartesian_burnout_z)
        cartesian.cartesian_burnout_vx = 4
        Assert.assertEqual(4, cartesian.cartesian_burnout_vx)
        cartesian.cartesian_burnout_vy = 5
        Assert.assertEqual(5, cartesian.cartesian_burnout_vy)
        cartesian.cartesian_burnout_vz = 6
        Assert.assertEqual(6, cartesian.cartesian_burnout_vz)

        velocity: "BurnoutVelocity" = launch.burnout_velocity
        velocity.burnout_option = BURNOUT_OPTIONS.INERTIAL_VELOCITY
        velocity.inertial_velocity = 20
        Assert.assertEqual(20, velocity.inertial_velocity)
        velocity.inertial_horizontal_fpa = 22
        Assert.assertEqual(22, velocity.inertial_horizontal_fpa)
        velocity.inertial_velocity_azimuth = 55
        Assert.assertEqual(55, velocity.inertial_velocity_azimuth)
        velocity.burnout_option = BURNOUT_OPTIONS.FIXED_VELOCITY
        Assert.assertEqual(BURNOUT_OPTIONS.FIXED_VELOCITY, velocity.burnout_option)
        velocity.fixed_velocity = 20
        Assert.assertEqual(20, velocity.fixed_velocity)

        launch.set_met_epoch = True
        Assert.assertEqual(True, launch.set_met_epoch)
        launch.set_met_epoch = False
        Assert.assertEqual(False, launch.set_met_epoch)

    # TODO check readonly as well.
    @staticmethod
    def TestInitialState(initState: "MissionControlSequenceInitialState", isFromCM: bool, root: "StkObjectRoot"):
        segment: "IMissionControlSequenceSegment" = clr.CastAs(initState, IMissionControlSequenceSegment)

        Assert.assertEqual(SEGMENT_TYPE.INITIAL_STATE, segment.type)
        initState.coord_system_name = "CentralBody/Earth Fixed"
        Assert.assertEqual("CentralBody/Earth Fixed", initState.coord_system_name)

        initState.orbit_epoch = "1 Jul 2006 10:00:00.000"
        Assert.assertEqual("1 Jul 2006 10:00:00.000", initState.orbit_epoch)
        sEpoch: str = str(segment.get_result_value("Epoch"))

        GatorHelper.TestFuelTank(initState.fuel_tank, False, isFromCM)

        GatorHelper.TestSpaceCraftParameters(initState.spacecraft_parameters, False)

        # Test spherical and cartesian because only these two work for centralbody/fixed
        initState.set_element_type(ELEMENT_TYPE.SPHERICAL)
        Assert.assertEqual(ELEMENT_TYPE.SPHERICAL, initState.element_type)
        spherical: "ElementSpherical" = ElementSpherical(initState.element)
        spherical.declination = 1
        Assert.assertAlmostEqual(1.0, float(spherical.declination), delta=0.0001)
        spherical.horizontal_flight_path_angle = 1
        Assert.assertAlmostEqual(1, float(spherical.horizontal_flight_path_angle), delta=0.001)
        spherical.radius_magnitude = 6678.2
        Assert.assertAlmostEqual(6678.2, float(spherical.radius_magnitude), delta=0.001)
        spherical.right_ascension = 1
        Assert.assertAlmostEqual(1, float(spherical.right_ascension), delta=0.001)
        spherical.velocity_azimuth = 62
        Assert.assertAlmostEqual(62, float(spherical.velocity_azimuth), delta=0.001)
        spherical.velocity_magnitude = 8
        Assert.assertAlmostEqual(8, float(spherical.velocity_magnitude), delta=0.001)
        spherical.vertical_flight_path_angle = 8
        Assert.assertAlmostEqual(8, float(spherical.vertical_flight_path_angle), delta=0.001)
        GatorHelper.m_logger.WriteLine("Spherical Bad Values")
        with pytest.raises(Exception):
            spherical.declination = 100
        with pytest.raises(Exception):
            spherical.declination = -100
        with pytest.raises(Exception):
            spherical.radius_magnitude = -10
        with pytest.raises(Exception):
            spherical.horizontal_flight_path_angle = 100
        with pytest.raises(Exception):
            spherical.horizontal_flight_path_angle = -100
        with pytest.raises(Exception):
            spherical.velocity_magnitude = -5

        initState.set_element_type(ELEMENT_TYPE.CARTESIAN)
        Assert.assertEqual(ELEMENT_TYPE.CARTESIAN, initState.element_type)
        cart: "ElementCartesian" = ElementCartesian(initState.element)
        cart.x = 6670
        Assert.assertEqual(6670, cart.x)
        cart.y = 1
        Assert.assertEqual(1, cart.y)
        cart.z = 1
        Assert.assertEqual(1, cart.z)

        cart.vx = 1
        Assert.assertEqual(1, cart.vx)
        cart.vy = 7
        Assert.assertEqual(7, cart.vy)
        cart.vz = 4
        Assert.assertEqual(4, cart.vz)

        # now change to another coordinate system to test the other element types
        initState.coord_system_name = "CentralBody/Earth B1950"
        Assert.assertEqual("CentralBody/Earth B1950", initState.coord_system_name)

        initState.set_element_type(ELEMENT_TYPE.TARGET_VECTOR_OUTGOING_ASYMPTOTE)
        Assert.assertEqual(ELEMENT_TYPE.TARGET_VECTOR_OUTGOING_ASYMPTOTE, initState.element_type)
        outgoing: "ElementTargetVectorOutgoingAsymptote" = ElementTargetVectorOutgoingAsymptote(initState.element)

        outgoing.radius_of_periapsis = 6678.2
        Assert.assertAlmostEqual(6678.2, float(outgoing.radius_of_periapsis), delta=0.001)
        outgoing.c3_energy = -58
        Assert.assertAlmostEqual(-58, float(outgoing.c3_energy), delta=0.001)
        outgoing.ra_outgoing_asymptote = 181
        Assert.assertAlmostEqual(181, float(outgoing.ra_outgoing_asymptote), delta=0.001)
        outgoing.declination_outgoing_asymptote = 1
        Assert.assertAlmostEqual(1, float(outgoing.declination_outgoing_asymptote), delta=0.001)
        outgoing.velocity_azimuth_periapsis = 62
        Assert.assertAlmostEqual(62, float(outgoing.velocity_azimuth_periapsis), delta=0.001)
        outgoing.true_anomaly = 1
        Assert.assertAlmostEqual(1, float(outgoing.true_anomaly), delta=0.001)
        GatorHelper.m_logger.WriteLine("Target Vector Outgoing bad values")
        with pytest.raises(Exception):
            outgoing.radius_of_periapsis = -5
        with pytest.raises(Exception):
            outgoing.declination_outgoing_asymptote = 120
        with pytest.raises(Exception):
            outgoing.declination_outgoing_asymptote = -120

        initState.set_element_type(ELEMENT_TYPE.TARGET_VECTOR_INCOMING_ASYMPTOTE)
        Assert.assertEqual(ELEMENT_TYPE.TARGET_VECTOR_INCOMING_ASYMPTOTE, initState.element_type)
        incoming: "ElementTargetVectorIncomingAsymptote" = ElementTargetVectorIncomingAsymptote(initState.element)
        incoming.radius_of_periapsis = 6678.2
        Assert.assertAlmostEqual(6678.2, float(incoming.radius_of_periapsis), delta=0.001)
        incoming.c3_energy = -58
        Assert.assertAlmostEqual(-58, float(incoming.c3_energy), delta=0.001)
        incoming.ra_incoming_asymptote = 181
        Assert.assertAlmostEqual(181, float(incoming.ra_incoming_asymptote), delta=0.001)
        incoming.declination_incoming_asymptote = 1
        Assert.assertAlmostEqual(1, float(incoming.declination_incoming_asymptote), delta=0.001)
        incoming.velocity_azimuth_periapsis = 62
        Assert.assertAlmostEqual(62, float(incoming.velocity_azimuth_periapsis), delta=0.001)
        incoming.true_anomaly = 1
        Assert.assertAlmostEqual(1, float(incoming.true_anomaly), delta=0.001)
        GatorHelper.m_logger.WriteLine("Target vector incoming bad values")
        with pytest.raises(Exception):
            incoming.radius_of_periapsis = -5
        with pytest.raises(Exception):
            incoming.declination_incoming_asymptote = 300
        with pytest.raises(Exception):
            incoming.declination_incoming_asymptote = -300

        initState.set_element_type(ELEMENT_TYPE.KEPLERIAN)
        Assert.assertEqual(ELEMENT_TYPE.KEPLERIAN, initState.element_type)
        kep: "ElementKeplerian" = ElementKeplerian(initState.element)
        kep.arg_of_periapsis = 1
        Assert.assertAlmostEqual(1, float(kep.arg_of_periapsis), delta=0.001)
        kep.eccentricity = 0.01
        Assert.assertAlmostEqual(0.01, float(kep.eccentricity), delta=0.001)
        kep.inclination = 29
        Assert.assertAlmostEqual(29, float(kep.inclination), delta=1e-08)
        kep.raan = 358
        Assert.assertEqual(358, kep.raan)
        kep.semi_major_axis = 6680
        Assert.assertAlmostEqual(6680, float(kep.semi_major_axis), delta=0.001)
        kep.true_anomaly = 358
        Assert.assertAlmostEqual(358, float(kep.true_anomaly), delta=1e-08)
        kep.apoapsis_altitude_size = 301
        Assert.assertAlmostEqual(301, kep.apoapsis_altitude_size, delta=0.0001)
        kep.apoapsis_radius_size = 6679
        Assert.assertAlmostEqual(6679, kep.apoapsis_radius_size, delta=0.0001)
        kep.mean_motion = 58
        Assert.assertAlmostEqual(58, kep.mean_motion, delta=0.0001)
        kep.periapsis_altitude_size = 301
        Assert.assertAlmostEqual(301, kep.periapsis_altitude_size, delta=0.0001)
        kep.periapsis_radius_size = 6680
        Assert.assertAlmostEqual(6680, kep.periapsis_radius_size, delta=0.0001)
        kep.period = 5430
        Assert.assertAlmostEqual(5430, kep.period, delta=0.0001)

        kep.apoapsis_altitude_shape = 302
        Assert.assertAlmostEqual(302, kep.apoapsis_altitude_shape, delta=0.0001)
        kep.apoapsis_radius_shape = 6681
        Assert.assertAlmostEqual(6681, kep.apoapsis_radius_shape, delta=0.0001)
        kep.periapsis_altitude_shape = 100
        Assert.assertAlmostEqual(100, kep.periapsis_altitude_shape, delta=0.0001)
        kep.periapsis_radius_shape = 105
        Assert.assertAlmostEqual(105, kep.periapsis_radius_shape, delta=0.0001)

        kep.lan = 82
        Assert.assertAlmostEqual(82, float(kep.lan), delta=0.0001)

        kep.arg_of_latitude = 1
        Assert.assertAlmostEqual(1, float(kep.arg_of_latitude), delta=0.0001)
        kep.eccentric_anomaly = 2
        Assert.assertAlmostEqual(2, float(kep.eccentric_anomaly), delta=0.0001)
        kep.mean_anomaly = 3
        Assert.assertAlmostEqual(3, float(kep.mean_anomaly), delta=0.0001)
        kep.time_past_asc_node = 4
        Assert.assertAlmostEqual(4, float(kep.time_past_asc_node), delta=0.0001)
        kep.time_past_periapsis = 5
        Assert.assertAlmostEqual(5, float(kep.time_past_periapsis), delta=0.0001)

        kep.element_type = ELEMENT.BROUWER_LYDDANE_MEAN_LONG
        Assert.assertEqual(ELEMENT.BROUWER_LYDDANE_MEAN_LONG, kep.element_type)
        kep.element_type = ELEMENT.BROUWER_LYDDANE_MEAN_SHORT
        Assert.assertEqual(ELEMENT.BROUWER_LYDDANE_MEAN_SHORT, kep.element_type)
        kep.element_type = ELEMENT.KOZAI_IZSAK_MEAN
        Assert.assertEqual(ELEMENT.KOZAI_IZSAK_MEAN, kep.element_type)
        kep.element_type = ELEMENT.OSCULATING
        Assert.assertEqual(ELEMENT.OSCULATING, kep.element_type)

        GatorHelper.m_logger.WriteLine("Keplerian bad values")
        with pytest.raises(Exception):
            kep.eccentricity = -0.1
        with pytest.raises(Exception):
            kep.eccentricity = 1
        with pytest.raises(Exception):
            kep.inclination = -2
        with pytest.raises(Exception):
            kep.inclination = 200

        initState.set_element_type(ELEMENT_TYPE.DELAUNAY)
        Assert.assertEqual(ELEMENT_TYPE.DELAUNAY, initState.element_type)
        delaunay: "ElementDelaunay" = clr.CastAs(initState.element, ElementDelaunay)
        delaunay.mean_anomaly = 1
        Assert.assertEqual(1, Math.Round(float(delaunay.mean_anomaly)))
        delaunay.arg_of_periapsis = 2
        Assert.assertEqual(2, Math.Round(float(delaunay.arg_of_periapsis)))
        delaunay.raan = 3
        Assert.assertEqual(3, Math.Round(float(delaunay.raan)))

        delaunay.delaunay_l = 51600
        Assert.assertEqual(51600, Math.Round(delaunay.delaunay_l, 0))
        delaunay.delaunay_g = 51591
        Assert.assertEqual(51591, Math.Round(delaunay.delaunay_g, 0))
        delaunay.delaunay_h = 45340
        Assert.assertEqual(45340, Math.Round(delaunay.delaunay_h, 0))
        delaunay.semi_major_axis = 6700
        Assert.assertEqual(6700, Math.Round(delaunay.semi_major_axis))
        delaunay.semilatus_rectum = 6690
        Assert.assertEqual(6690, Math.Round(delaunay.semilatus_rectum))
        delaunay.inclination = 29
        Assert.assertEqual(29, Math.Round(float(delaunay.inclination)))

        initState.set_element_type(ELEMENT_TYPE.EQUINOCTIAL)
        Assert.assertEqual(ELEMENT_TYPE.EQUINOCTIAL, initState.element_type)
        equinoctial: "ElementEquinoctial" = clr.CastAs(initState.element, ElementEquinoctial)
        equinoctial.semi_major_axis = 6679
        Assert.assertAlmostEqual(6679, equinoctial.semi_major_axis, delta=0.0001)
        equinoctial.mean_motion = 64
        Assert.assertAlmostEqual(64, equinoctial.mean_motion, delta=0.0001)
        equinoctial.h = 0.01
        Assert.assertAlmostEqual(0.01, equinoctial.h, delta=0.0001)
        equinoctial.k = 0.1
        Assert.assertAlmostEqual(0.1, equinoctial.k, delta=0.0001)
        equinoctial.p = 0.2
        Assert.assertAlmostEqual(0.2, equinoctial.p, delta=0.0001)
        equinoctial.q = 0.28
        Assert.assertAlmostEqual(0.28, equinoctial.q, delta=0.0001)
        equinoctial.mean_longitude = 3
        Assert.assertAlmostEqual(3, float(equinoctial.mean_longitude), delta=0.0001)
        equinoctial.formulation = FORMULATION.RETROGRADE
        Assert.assertEqual(FORMULATION.RETROGRADE, equinoctial.formulation)
        equinoctial.formulation = FORMULATION.POSIGRADE
        Assert.assertEqual(FORMULATION.POSIGRADE, equinoctial.formulation)

        initState.set_element_type(ELEMENT_TYPE.MIXED_SPHERICAL)
        Assert.assertEqual(ELEMENT_TYPE.MIXED_SPHERICAL, initState.element_type)
        mixedSpherical: "ElementMixedSpherical" = clr.CastAs(initState.element, ElementMixedSpherical)
        mixedSpherical.altitude = 303
        Assert.assertAlmostEqual(303, float(mixedSpherical.altitude), delta=0.0001)
        mixedSpherical.longitude = 82
        Assert.assertAlmostEqual(82, float(mixedSpherical.longitude), delta=0.0001)
        mixedSpherical.latitude = 0.4
        Assert.assertAlmostEqual(0.4, float(mixedSpherical.latitude), delta=0.0001)
        mixedSpherical.horizontal_flight_path_angle = 2
        Assert.assertAlmostEqual(2, float(mixedSpherical.horizontal_flight_path_angle), delta=0.0001)
        mixedSpherical.vertical_flight_path_angle = 89
        Assert.assertAlmostEqual(89, float(mixedSpherical.vertical_flight_path_angle), delta=0.0001)
        mixedSpherical.velocity_azimuth = 63
        Assert.assertAlmostEqual(63, float(mixedSpherical.velocity_azimuth), delta=0.0001)
        mixedSpherical.velocity_magnitude = 7.9
        Assert.assertAlmostEqual(7.9, float(mixedSpherical.velocity_magnitude), delta=0.0001)

        initState.set_element_type(ELEMENT_TYPE.SPHERICAL_RANGE_RATE)
        Assert.assertEqual(ELEMENT_TYPE.SPHERICAL_RANGE_RATE, initState.element_type)
        sphericalRangeRate: "ElementSphericalRangeRate" = clr.CastAs(initState.element, ElementSphericalRangeRate)

        sphericalRangeRate.right_ascension = 10.0
        Assert.assertAlmostEqual(10, float(sphericalRangeRate.right_ascension), delta=0.0001)

        sphericalRangeRate.declination = -90
        Assert.assertAlmostEqual(-90, float(sphericalRangeRate.declination), delta=0.0001)
        sphericalRangeRate.declination = 90
        Assert.assertAlmostEqual(90, float(sphericalRangeRate.declination), delta=0.0001)
        sphericalRangeRate.declination = 80
        Assert.assertAlmostEqual(80, float(sphericalRangeRate.declination), delta=0.0001)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            sphericalRangeRate.declination = -91
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            sphericalRangeRate.declination = 91

        sphericalRangeRate.range = 1e-13
        Assert.assertAlmostEqual(1e-13, sphericalRangeRate.range, delta=0.0001)
        sphericalRangeRate.range = 100
        Assert.assertAlmostEqual(100, sphericalRangeRate.range, delta=0.0001)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            sphericalRangeRate.range = 0

        sphericalRangeRate.right_ascension_rate = 110
        Assert.assertAlmostEqual(110, float(sphericalRangeRate.right_ascension_rate), delta=0.0001)

        sphericalRangeRate.declination_rate = 120
        Assert.assertAlmostEqual(120, float(sphericalRangeRate.declination_rate), delta=0.0001)

        sphericalRangeRate.range_rate = 130
        Assert.assertAlmostEqual(130, sphericalRangeRate.range_rate, delta=0.0001)

        # //////////////////////////////////////////////////////////////////////////////////

        oSat: "Satellite" = clr.CastAs(
            root.current_scenario.children.import_object(TestBase.GetScenarioFile("FEA118980", "Open_BPlane.sa")),
            Satellite,
        )
        driver: "DriverMissionControlSequence" = DriverMissionControlSequence(oSat.propagator)
        _is: "MissionControlSequenceInitialState" = clr.CastAs(
            driver.main_sequence["Initial State"], MissionControlSequenceInitialState
        )
        Assert.assertEqual(ELEMENT_TYPE.B_PLANE, _is.element_type)
        elemBPlane: "ElementBPlane" = clr.CastAs(_is.element, ElementBPlane)

        elemBPlane.right_ascension_of_b_plane = 70.0
        Assert.assertAlmostEqual(70.0, elemBPlane.right_ascension_of_b_plane, delta=0.0001)

        elemBPlane.declination_of_b_plane = 30.0
        Assert.assertAlmostEqual(30.0, elemBPlane.declination_of_b_plane, delta=0.0001)

        elemBPlane.true_anomaly = 226.0
        Assert.assertAlmostEqual(226.0, elemBPlane.true_anomaly, delta=0.0001)

        elemBPlane.b_dot_r_first_b_vector = 840.0
        Assert.assertAlmostEqual(840.0, elemBPlane.b_dot_r_first_b_vector, delta=0.0001)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("Can't set B Magnitude in combination with B dot R or B dot T.")
        ):
            elemBPlane.b_magnitude_second_b_vector = 29000.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "Cannot set B dot R when B dot R is already being used as the first B Vector option."
            ),
        ):
            elemBPlane.b_dot_r_second_b_vector = 2000.0
        elemBPlane.b_dot_t_second_b_vector = 30000.0
        Assert.assertAlmostEqual(30000.0, elemBPlane.b_dot_t_second_b_vector, delta=0.0001)

        elemBPlane.hyperbolic_v_infinity = 3.0
        Assert.assertAlmostEqual(3.0, elemBPlane.hyperbolic_v_infinity, delta=0.0001)

        elemBPlane.hyperbolic_turning_angle = 100.0
        Assert.assertAlmostEqual(100.0, elemBPlane.hyperbolic_turning_angle, delta=0.0001)
        elemBPlane.orbital_c3_energy = 12.0
        Assert.assertAlmostEqual(12.0, elemBPlane.orbital_c3_energy, delta=0.0001)
        elemBPlane.semi_major_axis = 35000.0
        Assert.assertAlmostEqual(35000.0, elemBPlane.semi_major_axis, delta=0.0001)

        elemBPlane.b_theta_first_b_vector = 5.0
        Assert.assertAlmostEqual(5.0, elemBPlane.b_theta_first_b_vector, delta=0.0001)

        elemBPlane.b_magnitude_second_b_vector = 29000.0
        Assert.assertAlmostEqual(29000.0, elemBPlane.b_magnitude_second_b_vector, delta=0.0001)

        elemBPlane.b_dot_r_second_b_vector = 2000.0
        Assert.assertAlmostEqual(2000.0, elemBPlane.b_dot_r_second_b_vector, delta=0.0001)

        elemBPlane.b_dot_t_second_b_vector = 30000.0
        Assert.assertAlmostEqual(30000.0, elemBPlane.b_dot_t_second_b_vector, delta=0.0001)

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set hyperbolic V infinity for closed orbits.")):
            elemBPlane.hyperbolic_v_infinity = 3.0
        with pytest.raises(
            Exception, match=RegexSubstringMatch("Cannot set hyperbolic turning angle for closed orbits.")
        ):
            elemBPlane.hyperbolic_turning_angle = 100.0
        elemBPlane.orbital_c3_energy = 12.0
        Assert.assertAlmostEqual(12.0, elemBPlane.orbital_c3_energy, delta=0.0001)
        elemBPlane.semi_major_axis = 35000.0
        Assert.assertAlmostEqual(35000.0, elemBPlane.semi_major_axis, delta=0.0001)

        elemBPlane.b_dot_r_second_b_vector = 2000.0  # setup for below
        Assert.assertAlmostEqual(2000.0, elemBPlane.b_dot_r_second_b_vector, delta=0.0001)

        elemBPlane.b_dot_t_first_b_vector = 30000.0
        Assert.assertAlmostEqual(30000.0, elemBPlane.b_dot_t_first_b_vector, delta=0.0001)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("Can't set B Magnitude in combination with B dot R or B dot T.")
        ):
            elemBPlane.b_magnitude_second_b_vector = 29000.0

        elemBPlane.b_dot_r_second_b_vector = 2000.0
        Assert.assertAlmostEqual(2000.0, elemBPlane.b_dot_r_second_b_vector, delta=0.0001)

        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "Cannot set B dot T when B dot T is already being used as the first B Vector option."
            ),
        ):
            elemBPlane.b_dot_t_second_b_vector = 30000.0

        with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set hyperbolic V infinity for closed orbits.")):
            elemBPlane.hyperbolic_v_infinity = 3.0
        with pytest.raises(
            Exception, match=RegexSubstringMatch("Cannot set hyperbolic turning angle for closed orbits.")
        ):
            elemBPlane.hyperbolic_turning_angle = 100.0
        elemBPlane.orbital_c3_energy = 12.0
        Assert.assertAlmostEqual(12.0, elemBPlane.orbital_c3_energy, delta=0.0001)
        elemBPlane.semi_major_axis = 35000.0
        Assert.assertAlmostEqual(35000.0, elemBPlane.semi_major_axis, delta=0.0001)

        root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "Open_BPlane")

    @staticmethod
    def TestUpdate(update: "MissionControlSequenceUpdate", isFromCM: bool):
        segment: "IMissionControlSequenceSegment" = clr.CastAs(update, IMissionControlSequenceSegment)
        GatorHelper.TestRuntimeTypeInfo(update)

        Assert.assertEqual(SEGMENT_TYPE.UPDATE, segment.type)
        update.set_action_and_value(UPDATE_PARAM.CD, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.CD))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.CD))

        update.set_action_and_value(UPDATE_PARAM.CK, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.CK))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.CK))

        update.set_action_and_value(UPDATE_PARAM.CR, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.CR))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.CR))

        update.set_action_and_value(UPDATE_PARAM.DRAG_AREA, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.DRAG_AREA))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.DRAG_AREA))

        update.set_action_and_value(UPDATE_PARAM.DRY_MASS, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.DRY_MASS))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.DRY_MASS))

        update.set_action_and_value(UPDATE_PARAM.FUEL_DENSITY, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.FUEL_DENSITY))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.FUEL_DENSITY))

        update.set_action_and_value(UPDATE_PARAM.FUEL_MASS, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.FUEL_MASS))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.FUEL_MASS))

        update.set_action_and_value(UPDATE_PARAM.RADIATION_PRESSURE_AREA, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.RADIATION_PRESSURE_AREA))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.RADIATION_PRESSURE_AREA))

        update.set_action_and_value(UPDATE_PARAM.SRP_AREA, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.SRP_AREA))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.SRP_AREA))

        update.set_action_and_value(UPDATE_PARAM.TANK_PRESSURE, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.TANK_PRESSURE))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.TANK_PRESSURE))

        update.set_action_and_value(UPDATE_PARAM.TANK_TEMP, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.TANK_TEMP))
        Assert.assertEqual(1, update.get_value(UPDATE_PARAM.TANK_TEMP))

        # Test the action enums
        update.set_action_and_value(UPDATE_PARAM.CD, UPDATE_ACTION.ADD_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.CD))

        update.set_action_and_value(UPDATE_PARAM.CD, UPDATE_ACTION.NO_CHANGE, 1)
        Assert.assertEqual(UPDATE_ACTION.NO_CHANGE, update.get_action(UPDATE_PARAM.CD))

        update.set_action_and_value(UPDATE_PARAM.CD, UPDATE_ACTION.SET_TO_NEW_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.SET_TO_NEW_VALUE, update.get_action(UPDATE_PARAM.CD))

        update.set_action_and_value(UPDATE_PARAM.CD, UPDATE_ACTION.SUBTRACT_VALUE, 1)
        Assert.assertEqual(UPDATE_ACTION.SUBTRACT_VALUE, update.get_action(UPDATE_PARAM.CD))

        update.set_action(UPDATE_PARAM.CD, UPDATE_ACTION.ADD_VALUE)
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.get_action(UPDATE_PARAM.CD))

        update.set_action(UPDATE_PARAM.CD, UPDATE_ACTION.NO_CHANGE)
        Assert.assertEqual(UPDATE_ACTION.NO_CHANGE, update.get_action(UPDATE_PARAM.CD))

        update.set_action(UPDATE_PARAM.CD, UPDATE_ACTION.SET_TO_NEW_VALUE)
        Assert.assertEqual(UPDATE_ACTION.SET_TO_NEW_VALUE, update.get_action(UPDATE_PARAM.CD))

        update.set_action(UPDATE_PARAM.CD, UPDATE_ACTION.SUBTRACT_VALUE)
        Assert.assertEqual(UPDATE_ACTION.SUBTRACT_VALUE, update.get_action(UPDATE_PARAM.CD))

        update.set_value(UPDATE_PARAM.CR, 2)
        Assert.assertEqual(2, update.get_value(UPDATE_PARAM.CR))

    @staticmethod
    def TestProfileLambertProfile(iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence"):
        maneuver: "MissionControlSequenceManeuver" = MissionControlSequenceManeuver(
            ts.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-")
        )
        propagate: "MissionControlSequencePropagate" = MissionControlSequencePropagate(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        )
        maneuver1: "MissionControlSequenceManeuver" = MissionControlSequenceManeuver(
            ts.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver1", "-")
        )
        propagate1: "MissionControlSequencePropagate" = MissionControlSequencePropagate(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate1", "-")
        )

        Assert.assertEqual(iAgVAProfile.type, PROFILE.LAMBERT_PROFILE)
        lambert: "ProfileLambertProfile" = ProfileLambertProfile(iAgVAProfile)
        GatorHelper.Test_IAgVAProfile(ts, lambert, PROFILE_MODE.ACTIVE)

        lambert.coord_system_name = "CentralBody/Earth Fixed"
        Assert.assertEqual("CentralBody/Earth Fixed", lambert.coord_system_name)
        with pytest.raises(
            Exception, match=RegexSubstringMatch("only available when an inertial Coordinate System is chosen")
        ):
            lambert.set_target_coord_type(LAMBERT_TARGET_COORD_TYPE.CARTESIAN)

        lambert.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", lambert.coord_system_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("link assignment failed")):
            lambert.coord_system_name = "CentralBody/Earth Bogus"

        lambert.set_target_coord_type(LAMBERT_TARGET_COORD_TYPE.CARTESIAN)
        Assert.assertEqual(LAMBERT_TARGET_COORD_TYPE.CARTESIAN, lambert.target_coord_type)

        lambert.enable_second_maneuver = False
        Assert.assertFalse(lambert.enable_second_maneuver)

        lambert.target_position_x = 10.0
        Assert.assertEqual(10.0, lambert.target_position_x)
        lambert.target_position_y = 20.0
        Assert.assertEqual(20.0, lambert.target_position_y)
        lambert.target_position_z = 30.0
        Assert.assertEqual(30.0, lambert.target_position_z)

        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "only allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_x = 40.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "only allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_y = 50.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "only allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_z = 60.0

        lambert.enable_second_maneuver = True
        Assert.assertTrue(lambert.enable_second_maneuver)

        lambert.target_position_x = 10.0
        Assert.assertEqual(10.0, lambert.target_position_x)
        lambert.target_position_y = 20.0
        Assert.assertEqual(20.0, lambert.target_position_y)
        lambert.target_position_z = 30.0
        Assert.assertEqual(30.0, lambert.target_position_z)
        lambert.target_velocity_x = 40.0
        Assert.assertEqual(40.0, lambert.target_velocity_x)
        lambert.target_velocity_y = 50.0
        Assert.assertEqual(50.0, lambert.target_velocity_y)
        lambert.target_velocity_z = 60.0
        Assert.assertEqual(60.0, lambert.target_velocity_z)

        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_semimajor_axis = 70.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_eccentricity = 80.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_inclination = 90.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_right_ascension_of_ascending_node = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_argument_of_periapsis = 110.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_true_anomaly = 120.0

        lambert.set_target_coord_type(LAMBERT_TARGET_COORD_TYPE.KEPLERIAN)
        Assert.assertEqual(LAMBERT_TARGET_COORD_TYPE.KEPLERIAN, lambert.target_coord_type)

        lambert.target_semimajor_axis = 70.0
        Assert.assertEqual(70.0, lambert.target_semimajor_axis)
        lambert.target_eccentricity = 80.0
        Assert.assertEqual(80.0, lambert.target_eccentricity)
        lambert.target_inclination = 90.0
        Assert.assertEqual(90.0, lambert.target_inclination)
        lambert.target_right_ascension_of_ascending_node = 100.0
        Assert.assertEqual(100.0, lambert.target_right_ascension_of_ascending_node)
        lambert.target_argument_of_periapsis = 110.0
        Assert.assertEqual(110.0, lambert.target_argument_of_periapsis)
        lambert.target_true_anomaly = 120.0
        Assert.assertEqual(120.0, lambert.target_true_anomaly)

        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Cartesian")):
            lambert.target_position_x = 10.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Cartesian")):
            lambert.target_position_y = 20.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Cartesian")):
            lambert.target_position_z = 30.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_x = 40.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_y = 50.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_z = 60.0

        lambert.solution_option = LAMBERT_SOLUTION_OPTION_TYPE.FIXED_TIME
        Assert.assertEqual(LAMBERT_SOLUTION_OPTION_TYPE.FIXED_TIME, lambert.solution_option)

        Assert.assertEqual(0.0, lambert.time_of_flight)
        Assert.assertEqual(0, lambert.revolutions)
        Assert.assertEqual(LAMBERT_ORBITAL_ENERGY_TYPE.LOW, lambert.orbital_energy)
        with pytest.raises(
            Exception, match=RegexSubstringMatch("only available when Number of Revolutions is greater than zero")
        ):
            lambert.orbital_energy = LAMBERT_ORBITAL_ENERGY_TYPE.HIGH

        lambert.time_of_flight = 10.0
        Assert.assertEqual(10.0, lambert.time_of_flight)
        lambert.revolutions = 10
        Assert.assertEqual(10, lambert.revolutions)
        lambert.orbital_energy = LAMBERT_ORBITAL_ENERGY_TYPE.LOW
        Assert.assertEqual(LAMBERT_ORBITAL_ENERGY_TYPE.LOW, lambert.orbital_energy)
        lambert.orbital_energy = LAMBERT_ORBITAL_ENERGY_TYPE.HIGH
        Assert.assertEqual(LAMBERT_ORBITAL_ENERGY_TYPE.HIGH, lambert.orbital_energy)

        lambert.solution_option = LAMBERT_SOLUTION_OPTION_TYPE.MIN_ECCENTRICITY
        Assert.assertEqual(LAMBERT_SOLUTION_OPTION_TYPE.MIN_ECCENTRICITY, lambert.solution_option)

        lambert.time_of_flight = 20.0
        Assert.assertEqual(20.0, lambert.time_of_flight)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            lambert.revolutions = 10
        with pytest.raises(
            Exception, match=RegexSubstringMatch("only available when Number of Revolutions is greater than zero")
        ):
            lambert.orbital_energy = LAMBERT_ORBITAL_ENERGY_TYPE.HIGH

        lambert.solution_option = LAMBERT_SOLUTION_OPTION_TYPE.MIN_ENERGY
        Assert.assertEqual(LAMBERT_SOLUTION_OPTION_TYPE.MIN_ENERGY, lambert.solution_option)

        lambert.time_of_flight = 30.0
        Assert.assertEqual(30.0, lambert.time_of_flight)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            lambert.revolutions = 10
        with pytest.raises(
            Exception, match=RegexSubstringMatch("only available when Number of Revolutions is greater than zero")
        ):
            lambert.orbital_energy = LAMBERT_ORBITAL_ENERGY_TYPE.HIGH

        lambert.direction_of_motion = LAMBERT_DIRECTION_OF_MOTION_TYPE.SHORT
        Assert.assertEqual(LAMBERT_DIRECTION_OF_MOTION_TYPE.SHORT, lambert.direction_of_motion)
        lambert.direction_of_motion = LAMBERT_DIRECTION_OF_MOTION_TYPE.LONG
        Assert.assertEqual(LAMBERT_DIRECTION_OF_MOTION_TYPE.LONG, lambert.direction_of_motion)

        lambert.central_body_collision_altitude_padding = 150.0
        Assert.assertEqual(150.0, lambert.central_body_collision_altitude_padding)
        lambert.central_body_collision_altitude_padding = 250.0
        Assert.assertEqual(250.0, lambert.central_body_collision_altitude_padding)

        lambert.enable_write_to_first_maneuver = False
        Assert.assertFalse(lambert.enable_write_to_first_maneuver)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Initial Delta-V to Maneuver is enabled")
        ):
            lambert.first_maneuver_segment = "Maneuver"

        lambert.enable_write_to_first_maneuver = True
        Assert.assertTrue(lambert.enable_write_to_first_maneuver)

        lambert.first_maneuver_segment = "TMan"
        Assert.assertEqual("TMan", lambert.first_maneuver_segment)
        lambert.first_maneuver_segment = "Maneuver"
        Assert.assertEqual("Maneuver", lambert.first_maneuver_segment)

        lambert.enable_write_duration_to_propagate = False
        Assert.assertFalse(lambert.enable_write_duration_to_propagate)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Duration to Propagate is enabled")
        ):
            lambert.disable_non_lambert_propagate_stop_conditions = True
        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Duration to Propagate is enabled")
        ):
            lambert.propagate_segment = "myProp"

        lambert.enable_write_duration_to_propagate = True
        Assert.assertTrue(lambert.enable_write_duration_to_propagate)

        lambert.disable_non_lambert_propagate_stop_conditions = True
        Assert.assertTrue(lambert.disable_non_lambert_propagate_stop_conditions)
        lambert.disable_non_lambert_propagate_stop_conditions = False
        Assert.assertFalse(lambert.disable_non_lambert_propagate_stop_conditions)

        lambert.propagate_segment = "myProp"
        Assert.assertEqual("myProp", lambert.propagate_segment)
        lambert.propagate_segment = "Propagate1"
        Assert.assertEqual("Propagate1", lambert.propagate_segment)

        lambert.enable_second_maneuver = False
        Assert.assertFalse(lambert.enable_second_maneuver)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Calculate Second Maneuver at Destination is enabled")
        ):
            lambert.enable_write_to_second_maneuver = True
        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Calculate Second Maneuver at Destination is enabled")
        ):
            lambert.second_maneuver_segment = "Maneuver1"

        lambert.enable_second_maneuver = True
        Assert.assertTrue(lambert.enable_second_maneuver)

        lambert.enable_write_to_second_maneuver = False
        Assert.assertFalse(lambert.enable_write_to_second_maneuver)
        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Final Delta-V to Maneuver is enabled")
        ):
            lambert.second_maneuver_segment = "Maneuver1"

        lambert.enable_write_to_second_maneuver = True
        Assert.assertTrue(lambert.enable_write_to_second_maneuver)

        lambert.second_maneuver_segment = "Maneuver1"
        Assert.assertEqual("Maneuver1", lambert.second_maneuver_segment)
        lambert.second_maneuver_segment = "TMan"
        Assert.assertEqual("TMan", lambert.second_maneuver_segment)

        ts.segments.remove("Maneuver")
        ts.segments.remove("Propagate")
        ts.segments.remove("Maneuver1")
        ts.segments.remove("Propagate1")

    @staticmethod
    def TestProfileLambertSearchProfile(iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence"):
        maneuver: "MissionControlSequenceManeuver" = MissionControlSequenceManeuver(
            ts.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-")
        )
        propagate: "MissionControlSequencePropagate" = MissionControlSequencePropagate(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        )
        maneuver1: "MissionControlSequenceManeuver" = MissionControlSequenceManeuver(
            ts.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver1", "-")
        )
        propagate1: "MissionControlSequencePropagate" = MissionControlSequencePropagate(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate1", "-")
        )

        Assert.assertEqual(iAgVAProfile.type, PROFILE.LAMBERT_SEARCH_PROFILE)
        lambert: "ProfileLambertSearchProfile" = ProfileLambertSearchProfile(iAgVAProfile)

        GatorHelper.Test_IAgVAProfile(ts, lambert, PROFILE_MODE.ACTIVE)

        lambert.coord_system_name = "CentralBody/Earth Fixed"
        Assert.assertEqual("CentralBody/Earth Fixed", lambert.coord_system_name)
        with pytest.raises(
            Exception, match=RegexSubstringMatch("only available when an inertial Coordinate System is chosen")
        ):
            lambert.set_target_coord_type(LAMBERT_TARGET_COORD_TYPE.CARTESIAN)

        lambert.coord_system_name = "CentralBody/Earth Inertial"
        Assert.assertEqual("CentralBody/Earth Inertial", lambert.coord_system_name)
        with pytest.raises(Exception, match=RegexSubstringMatch("link assignment failed")):
            lambert.coord_system_name = "CentralBody/Earth Bogus"

        lambert.enable_target_match_phase = True
        Assert.assertTrue(lambert.enable_target_match_phase)
        lambert.enable_target_match_phase = False
        Assert.assertFalse(lambert.enable_target_match_phase)

        lambert.set_target_coord_type(LAMBERT_TARGET_COORD_TYPE.CARTESIAN)
        Assert.assertEqual(LAMBERT_TARGET_COORD_TYPE.CARTESIAN, lambert.target_coord_type)

        lambert.enable_second_maneuver = False
        Assert.assertFalse(lambert.enable_second_maneuver)

        lambert.target_position_x = 10.0
        Assert.assertEqual(10.0, lambert.target_position_x)
        lambert.target_position_y = 20.0
        Assert.assertEqual(20.0, lambert.target_position_y)
        lambert.target_position_z = 30.0
        Assert.assertEqual(30.0, lambert.target_position_z)

        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "only allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_x = 40.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "only allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_y = 50.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "only allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_z = 60.0

        lambert.enable_second_maneuver = True
        Assert.assertTrue(lambert.enable_second_maneuver)

        lambert.target_position_x = 10.0
        Assert.assertEqual(10.0, lambert.target_position_x)
        lambert.target_position_y = 20.0
        Assert.assertEqual(20.0, lambert.target_position_y)
        lambert.target_position_z = 30.0
        Assert.assertEqual(30.0, lambert.target_position_z)
        lambert.target_velocity_x = 40.0
        Assert.assertEqual(40.0, lambert.target_velocity_x)
        lambert.target_velocity_y = 50.0
        Assert.assertEqual(50.0, lambert.target_velocity_y)
        lambert.target_velocity_z = 60.0
        Assert.assertEqual(60.0, lambert.target_velocity_z)

        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_semimajor_axis = 70.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_eccentricity = 80.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_inclination = 90.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_right_ascension_of_ascending_node = 100.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_argument_of_periapsis = 110.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Keplerian")):
            lambert.target_true_anomaly = 120.0

        lambert.set_target_coord_type(LAMBERT_TARGET_COORD_TYPE.KEPLERIAN)
        Assert.assertEqual(LAMBERT_TARGET_COORD_TYPE.KEPLERIAN, lambert.target_coord_type)

        lambert.target_semimajor_axis = 70.0
        Assert.assertEqual(70.0, lambert.target_semimajor_axis)
        lambert.target_eccentricity = 80.0
        Assert.assertEqual(80.0, lambert.target_eccentricity)
        lambert.target_inclination = 90.0
        Assert.assertEqual(90.0, lambert.target_inclination)
        lambert.target_right_ascension_of_ascending_node = 100.0
        Assert.assertEqual(100.0, lambert.target_right_ascension_of_ascending_node)
        lambert.target_argument_of_periapsis = 110.0
        Assert.assertEqual(110.0, lambert.target_argument_of_periapsis)
        lambert.target_true_anomaly = 120.0
        Assert.assertEqual(120.0, lambert.target_true_anomaly)

        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Cartesian")):
            lambert.target_position_x = 10.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Cartesian")):
            lambert.target_position_y = 20.0
        with pytest.raises(Exception, match=RegexSubstringMatch("allowed when Target Coordinate Type is Cartesian")):
            lambert.target_position_z = 30.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_x = 40.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_y = 50.0
        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "allowed when Calculate Second Maneuver at Destination is enabled and Target Coordinate Type is Cartesian"
            ),
        ):
            lambert.target_velocity_z = 60.0

        lambert.enable_write_departure_delay_to_first_propagate = False
        Assert.assertFalse(lambert.enable_write_departure_delay_to_first_propagate)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Departure Delay to First Propagate is enabled")
        ):
            lambert.disable_first_propagate_non_lambert_stop_conditions = True
        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Departure Delay to First Propagate is enabled")
        ):
            lambert.first_propagate_segment = "Propagate"

        lambert.enable_write_departure_delay_to_first_propagate = True
        Assert.assertTrue(lambert.enable_write_departure_delay_to_first_propagate)

        lambert.disable_first_propagate_non_lambert_stop_conditions = True
        Assert.assertTrue(lambert.disable_first_propagate_non_lambert_stop_conditions)
        lambert.disable_first_propagate_non_lambert_stop_conditions = False
        Assert.assertFalse(lambert.disable_first_propagate_non_lambert_stop_conditions)

        lambert.first_propagate_segment = "Propagate"
        Assert.assertEqual("Propagate", lambert.first_propagate_segment)
        lambert.first_propagate_segment = "Propagate1"
        Assert.assertEqual("Propagate1", lambert.first_propagate_segment)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            lambert.first_propagate_segment = "Bogus"

        lambert.enable_write_to_first_maneuver = False
        Assert.assertFalse(lambert.enable_write_to_first_maneuver)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Initial Delta-V to Maneuver is enabled")
        ):
            lambert.first_maneuver_segment = "Maneuver"

        lambert.enable_write_to_first_maneuver = True
        Assert.assertTrue(lambert.enable_write_to_first_maneuver)

        lambert.first_maneuver_segment = "TMan"
        Assert.assertEqual("TMan", lambert.first_maneuver_segment)
        lambert.first_maneuver_segment = "Maneuver"
        Assert.assertEqual("Maneuver", lambert.first_maneuver_segment)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            lambert.first_maneuver_segment = "Bogus"

        lambert.enable_write_duration_to_second_propagate = False
        Assert.assertFalse(lambert.enable_write_duration_to_second_propagate)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Flight Duration to Second Propagate is enabled")
        ):
            lambert.disable_second_propagate_non_lambert_stop_conditions = True
        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Flight Duration to Second Propagate is enabled")
        ):
            lambert.second_propagate_segment = "Propagate"

        lambert.enable_write_duration_to_second_propagate = True
        Assert.assertTrue(lambert.enable_write_duration_to_second_propagate)

        lambert.disable_second_propagate_non_lambert_stop_conditions = True
        Assert.assertTrue(lambert.disable_second_propagate_non_lambert_stop_conditions)
        lambert.disable_second_propagate_non_lambert_stop_conditions = False
        Assert.assertFalse(lambert.disable_second_propagate_non_lambert_stop_conditions)

        lambert.second_propagate_segment = "Propagate"
        Assert.assertEqual("Propagate", lambert.second_propagate_segment)
        lambert.second_propagate_segment = "Propagate1"
        Assert.assertEqual("Propagate1", lambert.second_propagate_segment)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            lambert.second_propagate_segment = "Bogus"

        lambert.enable_write_to_second_maneuver = False
        Assert.assertFalse(lambert.enable_write_to_second_maneuver)

        with pytest.raises(
            Exception, match=RegexSubstringMatch("available when Write Final Inertial Delta-V to Maneuver is enabled")
        ):
            lambert.second_maneuver_segment = "Maneuver"

        lambert.enable_write_to_second_maneuver = True
        Assert.assertTrue(lambert.enable_write_to_second_maneuver)

        lambert.second_maneuver_segment = "TMan"
        Assert.assertEqual("TMan", lambert.second_maneuver_segment)
        lambert.second_maneuver_segment = "Maneuver"
        Assert.assertEqual("Maneuver", lambert.second_maneuver_segment)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            lambert.second_maneuver_segment = "Bogus"

        lambert.latest_departure_time = 200.0
        Assert.assertEqual(200.0, lambert.latest_departure_time)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            lambert.latest_departure_time = -1.0

        lambert.earliest_arrival_time = 300.0
        Assert.assertEqual(300.0, lambert.earliest_arrival_time)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            lambert.earliest_arrival_time = -1.0

        lambert.latest_arrival_time = 400.0
        Assert.assertEqual(400.0, lambert.latest_arrival_time)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            lambert.latest_arrival_time = -1.0

        lambert.grid_search_time_step = 500.0
        Assert.assertEqual(500.0, lambert.grid_search_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            lambert.grid_search_time_step = -1.0

        lambert.max_revolutions = 600
        Assert.assertEqual(600, lambert.max_revolutions)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            lambert.max_revolutions = -1

        lambert.central_body_collision_altitude_padding = 700.0
        Assert.assertEqual(700.0, lambert.central_body_collision_altitude_padding)

        ts.segments.remove("Maneuver")
        ts.segments.remove("Propagate")
        ts.segments.remove("Maneuver1")
        ts.segments.remove("Propagate1")

    @staticmethod
    def TestProfileGoldenSection(
        iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence", root: "StkObjectRoot"
    ):
        if root != None:
            oSat: "Satellite" = clr.CastAs(
                root.current_scenario.children.import_object(TestBase.GetScenarioFile("ENG116918", "GoldenSection.sa")),
                Satellite,
            )
            driver: "DriverMissionControlSequence" = DriverMissionControlSequence(oSat.propagator)
            _ts: "MissionControlSequenceTargetSequence" = clr.CastAs(
                driver.main_sequence["Target Sequence"], MissionControlSequenceTargetSequence
            )
            profGoldenSection: "ProfileGoldenSection" = ProfileGoldenSection(_ts.profiles["Golden Section Search"])
            Assert.assertEqual("Golden Section Search", profGoldenSection.name)

            GatorHelper.TestRuntimeTypeInfo(profGoldenSection)
            GatorHelper.Test_IAgVAProfile(ts, iAgVAProfile, PROFILE_MODE.NOT_ACTIVE)

            Assert.assertEqual(10000, profGoldenSection.max_iterations)
            profGoldenSection.max_iterations = 5000
            Assert.assertEqual(5000, profGoldenSection.max_iterations)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                profGoldenSection.max_iterations = -5000

            Assert.assertEqual(
                TestBase.GetScenarioFile("ENG116918", "GoldenSection_Target_Sequence._Golden_Section_Search_Log.txt"),
                profGoldenSection.log_file,
            )

            profGoldenSection.enable_display_status = False
            Assert.assertFalse(profGoldenSection.enable_display_status)
            profGoldenSection.enable_display_status = True
            Assert.assertTrue(profGoldenSection.enable_display_status)

            GatorHelper.Test_IAgVATargeterGraphCollection(profGoldenSection.targeter_graphs, "GoldenSection")

            GatorHelper.Test_IAgVAScriptingTool(profGoldenSection.scripting_tool, "Segments.Maneuver")

            # available controls

            GoldenSectionControlCollection: "GoldenSectionControlCollection" = profGoldenSection.controls
            Assert.assertEqual(1, GoldenSectionControlCollection.count)

            with pytest.raises(Exception, match=RegexSubstringMatch("could not be found")):
                GoldenSectionControlByPathsX: "GoldenSectionControl" = (
                    GoldenSectionControlCollection.get_control_by_paths("Maneuver", "Bogus")
                )

            GoldenSectionControlByPaths: "GoldenSectionControl" = GoldenSectionControlCollection.get_control_by_paths(
                "Maneuver", "ImpulsiveMnvr.Pointing.Spherical.Magnitude"
            )
            Assert.assertEqual("ImpulsiveMnvr.Pointing.Spherical.Magnitude", GoldenSectionControlByPaths.name)

            GoldenSectionControl: "GoldenSectionControl" = GoldenSectionControlCollection[0]
            Assert.assertEqual("ImpulsiveMnvr.Pointing.Spherical.Magnitude", GoldenSectionControl.name)
            Assert.assertEqual("Maneuver", GoldenSectionControl.parent_name)

            GoldenSectionControl.enable = False
            Assert.assertFalse(GoldenSectionControl.enable)
            GoldenSectionControl.enable = True
            Assert.assertTrue(GoldenSectionControl.enable)

            Assert.assertEqual(0, GoldenSectionControl.current_value)

            GoldenSectionControl.lower_bound = 0.2
            Assert.assertEqual(0.2, GoldenSectionControl.lower_bound)
            GoldenSectionControl.lower_bound = 0.33
            Assert.assertEqual(0.33, GoldenSectionControl.lower_bound)

            GoldenSectionControl.upper_bound = 2.0
            Assert.assertEqual(2.0, GoldenSectionControl.upper_bound)
            GoldenSectionControl.upper_bound = 55.0
            Assert.assertEqual(55.0, GoldenSectionControl.upper_bound)

            GoldenSectionControl.use_custom_display_unit = False
            Assert.assertFalse(GoldenSectionControl.use_custom_display_unit)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                GoldenSectionControl.custom_display_unit = "km/sec"

            GoldenSectionControl.use_custom_display_unit = True
            Assert.assertTrue(GoldenSectionControl.use_custom_display_unit)

            GoldenSectionControl.custom_display_unit = "km/sec"
            Assert.assertEqual("km/sec", GoldenSectionControl.custom_display_unit)
            GoldenSectionControl.custom_display_unit = "m/sec"
            Assert.assertEqual("m/sec", GoldenSectionControl.custom_display_unit)

            GoldenSectionControl.tolerance = 2e-06
            Assert.assertEqual(2e-06, GoldenSectionControl.tolerance)
            GoldenSectionControl.tolerance = 9e-06
            Assert.assertEqual(9e-06, GoldenSectionControl.tolerance)

            # available results

            GoldenSectionResultCollection: "GoldenSectionResultCollection" = profGoldenSection.results
            Assert.assertEqual(2, GoldenSectionResultCollection.count)

            GoldenSectionResultByPaths: "GoldenSectionResult" = GoldenSectionResultCollection.get_result_by_paths(
                "Maneuver", "DeltaV"
            )
            Assert.assertEqual("DeltaV", GoldenSectionResultByPaths.name)
            Assert.assertEqual("Maneuver", GoldenSectionResultByPaths.parent_name)

            GoldenSectionResult: "GoldenSectionResult" = GoldenSectionResultCollection[0]
            Assert.assertEqual("DeltaV", GoldenSectionResult.name)
            Assert.assertEqual("Maneuver", GoldenSectionResult.parent_name)
            Assert.assertFalse(GoldenSectionResult.enable)
            Assert.assertAlmostEqual(1.5, float(GoldenSectionResult.current_value), delta=0.0001)

            GoldenSectionResult.enable = False
            Assert.assertFalse(GoldenSectionResult.enable)
            GoldenSectionResult.enable = True
            Assert.assertTrue(GoldenSectionResult.enable)

            GoldenSectionResult.desired_operation = GOLDEN_SECTION_DESIRED_OPERATION.MINIMIZE_VALUE
            Assert.assertEqual(GOLDEN_SECTION_DESIRED_OPERATION.MINIMIZE_VALUE, GoldenSectionResult.desired_operation)
            GoldenSectionResult.desired_operation = GOLDEN_SECTION_DESIRED_OPERATION.MAXIMIZE_VALUE
            Assert.assertEqual(GOLDEN_SECTION_DESIRED_OPERATION.MAXIMIZE_VALUE, GoldenSectionResult.desired_operation)

            GoldenSectionResult.use_custom_display_unit = False
            Assert.assertFalse(GoldenSectionResult.use_custom_display_unit)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                GoldenSectionResult.custom_display_unit = "km/sec"

            GoldenSectionResult.use_custom_display_unit = True
            Assert.assertTrue(GoldenSectionResult.use_custom_display_unit)

            GoldenSectionResult.custom_display_unit = "km/sec"
            Assert.assertEqual("km/sec", GoldenSectionResult.custom_display_unit)
            GoldenSectionResult.custom_display_unit = "m/sec"
            Assert.assertEqual("m/sec", GoldenSectionResult.custom_display_unit)

    @staticmethod
    def TestProfileGridSearch(
        iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence", root: "StkObjectRoot"
    ):
        if root != None:
            GatorHelper.Test_IAgVAProfile(ts, iAgVAProfile, PROFILE_MODE.NOT_ACTIVE)

            # Enable a Control param and add a Result for use below
            man1: "MissionControlSequenceManeuver" = clr.CastAs(ts.segments["TMan"], MissionControlSequenceManeuver)
            man1.enable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)
            (IMissionControlSequenceSegment(man1)).results.add("Epoch")

            Assert.assertEqual(iAgVAProfile.type, PROFILE.GRID_SEARCH)
            profGridSearch: "ProfileGridSearch" = ProfileGridSearch(iAgVAProfile)
            Assert.assertEqual("One Dimensional Grid Search", profGridSearch.name)
            GatorHelper.TestRuntimeTypeInfo(profGridSearch)

            Assert.assertEqual("--Log file not in use--", profGridSearch.log_file)

            profGridSearch.enable_display_status = False
            Assert.assertFalse(profGridSearch.enable_display_status)
            profGridSearch.enable_display_status = True
            Assert.assertTrue(profGridSearch.enable_display_status)

            profGridSearch.should_generate_graph = False
            Assert.assertFalse(profGridSearch.should_generate_graph)
            profGridSearch.should_generate_graph = True
            Assert.assertTrue(profGridSearch.should_generate_graph)

            # available controls
            GridSearchControl: "GridSearchControl" = profGridSearch.controls[0]
            Assert.assertEqual("FiniteMnvr.BurnCenterBias", GridSearchControl.name)
            Assert.assertEqual("TMan", GridSearchControl.parent_name)

            GridSearchControl.enable = False
            Assert.assertFalse(GridSearchControl.enable)
            GridSearchControl.enable = True
            Assert.assertTrue(GridSearchControl.enable)

            Assert.assertEqual(0.0, GridSearchControl.current_value)

            GridSearchControl.lower_bound = 1800
            Assert.assertEqual(1800, GridSearchControl.lower_bound)
            GridSearchControl.lower_bound = 3600
            Assert.assertEqual(3600, GridSearchControl.lower_bound)

            GridSearchControl.upper_bound = 18000
            Assert.assertEqual(18000, GridSearchControl.upper_bound)
            GridSearchControl.upper_bound = 36000
            Assert.assertEqual(36000, GridSearchControl.upper_bound)

            GridSearchControl.step = 180
            Assert.assertEqual(180, GridSearchControl.step)
            GridSearchControl.step = 7200
            Assert.assertEqual(7200, GridSearchControl.step)

            GridSearchControl.use_custom_display_unit = False
            Assert.assertFalse(GridSearchControl.use_custom_display_unit)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                GridSearchControl.custom_display_unit = "min"

            GridSearchControl.use_custom_display_unit = True
            Assert.assertTrue(GridSearchControl.use_custom_display_unit)

            GridSearchControl.custom_display_unit = "hr"
            Assert.assertEqual("hr", GridSearchControl.custom_display_unit)

            GatorHelper.Test_IAgVATargeterGraphCollection(profGridSearch.targeter_graphs, "GridSearch")
            GatorHelper.Test_IAgVAScriptingTool(profGridSearch.scripting_tool, "Segments.TMan")

            # available results
            GridSearchResult: "GridSearchResult" = profGridSearch.results[0]

            Assert.assertEqual("Epoch", GridSearchResult.name)
            Assert.assertEqual("TMan", GridSearchResult.parent_name)
            Assert.assertFalse(GridSearchResult.enable)
            Assert.assertEqual("-Not Set-", GridSearchResult.current_value)

            GridSearchResult.desired_operation = GRID_SEARCH_DESIRED_OPERATION.MAXIMIZE_VALUE
            Assert.assertEqual(GRID_SEARCH_DESIRED_OPERATION.MAXIMIZE_VALUE, GridSearchResult.desired_operation)

            GridSearchResult.use_custom_display_unit = False
            Assert.assertFalse(GridSearchResult.use_custom_display_unit)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                GridSearchResult.custom_display_unit = "UTCJ"

            GridSearchResult.use_custom_display_unit = True
            Assert.assertTrue(GridSearchResult.use_custom_display_unit)

            GridSearchResult.custom_display_unit = "UTCJ"
            Assert.assertEqual("UTCJ", GridSearchResult.custom_display_unit)
            with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
                GridSearchResult.custom_display_unit = "Bogus"

            # Cleanup
            (IMissionControlSequenceSegment(man1)).results.remove("Epoch")
            man1.disable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)

    @staticmethod
    def TestProfileBisection(
        iAgVAProfile: "IProfile", ts: "MissionControlSequenceTargetSequence", root: "StkObjectRoot"
    ):
        if root != None:
            profBisection: "ProfileBisection" = clr.CastAs(ts.profiles["Single Parameter Bisection"], ProfileBisection)
            Assert.assertEqual("Single Parameter Bisection", profBisection.name)

            GatorHelper.TestRuntimeTypeInfo(profBisection)
            GatorHelper.Test_IAgVAProfile(ts, iAgVAProfile, PROFILE_MODE.NOT_ACTIVE)

            loop: "BisectionControl"

            for loop in profBisection.control_parameters:
                name1: str = loop.name

            i: int = 0
            while i < profBisection.control_parameters.count:
                name2: str = profBisection.control_parameters[i].name

                i += 1

            with pytest.raises(Exception):
                name3: str = profBisection.control_parameters[-1].name
            if not OSHelper.IsLinux():
                scriptingTool: "ScriptingTool" = profBisection.scripting_tool
                scriptingTool.enable = True
                Assert.assertTrue(scriptingTool.enable)

                GatorHelper.TestScriptingToolSegmentProperties(scriptingTool.segment_properties, "Segments.myProp")

                GatorHelper.TestScriptingToolParameters(scriptingTool.parameters)

                GatorHelper.TestScriptingToolCalcObjects(scriptingTool.calc_objects)

                scriptingTool.language_type = LANGUAGE.J_SCRIPT
                Assert.assertEqual(LANGUAGE.J_SCRIPT, scriptingTool.language_type)
                scriptingTool.script_text("int j = 2;")

            maneuver: "MissionControlSequenceManeuver" = clr.CastAs(ts.segments["TMan"], MissionControlSequenceManeuver)
            maneuver.enable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)

            objName: str = "TMan"
            decName: str = "FiniteMnvr.BurnCenterBias"
            dec1: "BisectionControl" = None
            dec1 = profBisection.control_parameters.get_control_by_paths(objName, decName)

            GatorHelper.TestBisectionControlParameter(dec1, objName, decName)

            with pytest.raises(Exception):
                decX: "BisectionControl" = profBisection.control_parameters.get_control_by_paths(objName, "Bogus")
            with pytest.raises(Exception):
                decY: "BisectionControl" = profBisection.control_parameters.get_control_by_paths("Bogus", decName)

            dec2: "BisectionControl" = None
            dec2 = profBisection.control_parameters[0]
            GatorHelper.TestBisectionControlParameter(dec2, objName, decName)

            with pytest.raises(Exception):
                eq2: "BisectionResult" = profBisection.results.get_result_by_paths("TMan", "ResultPath")
            with pytest.raises(Exception):
                eq2: "BisectionResult" = profBisection.results.get_result_by_paths("ObjectPath", "Epoch")

            manSegment: "IMissionControlSequenceSegment" = clr.CastAs(maneuver, IMissionControlSequenceSegment)
            manSegment.results.add("Epoch")
            eq: "BisectionResult" = profBisection.results.get_result_by_paths("TMan", "Epoch")

            GatorHelper.TestBisectionResult(eq)

            i: int = 0
            while i < profBisection.results.count:
                result: "BisectionResult" = profBisection.results[i]
                GatorHelper.m_logger.WriteLine(result.name)

                i += 1

            with pytest.raises(Exception):
                result: "BisectionResult" = profBisection.results[10]

            result: "BisectionResult"

            for result in profBisection.results:
                GatorHelper.m_logger.WriteLine(result.name)

            GatorHelper.TestBisectionTargeterGraphs(profBisection.targeter_graphs)

            profBisection.reset_controls_before_run = False
            Assert.assertFalse(profBisection.reset_controls_before_run)
            profBisection.reset_controls_before_run = True
            Assert.assertTrue(profBisection.reset_controls_before_run)

            profBisection.maximum_iterations = 100
            Assert.assertEqual(100, profBisection.maximum_iterations)
            profBisection.maximum_iterations = 200
            Assert.assertEqual(200, profBisection.maximum_iterations)
            with pytest.raises(Exception):
                profBisection.maximum_iterations = -1

            spCopy: "ProfileBisection" = ProfileBisection(profBisection.copy())

            manSegment.results.remove("Epoch")
            maneuver.disable_control_parameter(CONTROL_MANEUVER.FINITE_BURN_CENTER_BIAS)

    @staticmethod
    def Test_IAgVATargeterGraphCollection(tgColl: "TargeterGraphCollection", profileName: str):
        GatorHelper.TestRuntimeTypeInfo(tgColl)

        Assert.assertEqual(1, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)

        tg1: "TargeterGraph" = tgColl.add_graph()
        tg1.name = "Graph2"
        Assert.assertEqual(2, tgColl.count)
        tgColl.cut(0)
        tgColl.paste()

        Assert.assertEqual("Graph2", tgColl[0].name)
        Assert.assertEqual("Graph1", tgColl[1].name)

        tgColl.insert_copy(tgColl["Graph2"])
        Assert.assertEqual(3, tgColl.count)
        Assert.assertEqual("Graph2", tgColl[0].name)
        Assert.assertEqual("Graph1", tgColl[1].name)
        Assert.assertEqual("Graph3", tgColl[2].name)

        Assert.assertEqual("Graph1", tgColl["Graph1"].name)
        Assert.assertEqual("Graph3", tgColl.get_item_by_index(2).name)
        Assert.assertEqual("Graph3", tgColl.get_item_by_name("Graph3").name)

        allNames: str = ""
        tg: "TargeterGraph"
        for tg in tgColl:
            allNames += tg.name

        Assert.assertEqual("Graph2Graph1Graph3", allNames)

        allNames = ""

        i: int = 0
        while i <= 2:
            allNames += tgColl[i].name

            i += 1

        Assert.assertEqual("Graph2Graph1Graph3", allNames)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            tgColl.remove_graph(3)
        tgColl.remove_graph(0)
        Assert.assertEqual(2, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)
        Assert.assertEqual("Graph3", tgColl[1].name)

        tgColl.remove_graph(1)
        Assert.assertEqual(1, tgColl.count)
        Assert.assertEqual("Graph1", tgColl[0].name)

        GatorHelper.Test_IAgVATargeterGraph(tgColl[0], profileName)

    @staticmethod
    def Test_IAgVATargeterGraph(tg: "TargeterGraph", profileName: str):
        tg.name = "NewName"
        Assert.assertEqual("NewName", tg.name)

        tg.generate_on_run = False
        Assert.assertFalse(tg.generate_on_run)
        tg.generate_on_run = True
        Assert.assertTrue(tg.generate_on_run)

        tg.user_comment = "My User Comment"
        Assert.assertEqual("My User Comment", tg.user_comment)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tg.show_desired_value = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tg.show_tolerance_band = True

        Assert.assertEqual("Iteration", tg.independent_variable)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            tg.show_label_iterations = True
        if profileName == "GoldenSection":
            tg.independent_variable = "Maneuver : DeltaV"
            Assert.assertEqual("Maneuver : DeltaV", tg.independent_variable)

            tg.show_label_iterations = False
            Assert.assertFalse(tg.show_label_iterations)
            tg.show_label_iterations = True
            Assert.assertTrue(tg.show_label_iterations)

            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                tg.independent_variable = "Bogus"

            GatorHelper.TestIAgVATargeterGraphActiveControlCollection(
                tg.active_controls, "Maneuver", "ImpulsiveMnvr Pointing Spherical Magnitude"
            )

            GatorHelper.TestIAgVATargeterGraphResultCollection(tg.results, "Propagate", "R Mag", 1)

        elif profileName == "GridSearch":
            tg.independent_variable = "TMan : FiniteMnvr.BurnCenterBias"
            Assert.assertEqual("TMan : FiniteMnvr.BurnCenterBias", tg.independent_variable)

            tg.show_label_iterations = False
            Assert.assertFalse(tg.show_label_iterations)
            tg.show_label_iterations = True
            Assert.assertTrue(tg.show_label_iterations)

            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                tg.independent_variable = "Bogus"

            GatorHelper.TestIAgVATargeterGraphActiveControlCollection(
                tg.active_controls, "TMan", "FiniteMnvr BurnCenterBias"
            )

            GatorHelper.TestIAgVATargeterGraphResultCollection(tg.results, "TMan", "Epoch", 0)

        elif profileName == "Python Search":
            tg.independent_variable = "myProp : Epoch"
            Assert.assertEqual("myProp : Epoch", tg.independent_variable)

            tg.show_label_iterations = False
            Assert.assertFalse(tg.show_label_iterations)
            tg.show_label_iterations = True
            Assert.assertTrue(tg.show_label_iterations)

            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                tg.independent_variable = "Bogus"

            GatorHelper.TestIAgVATargeterGraphActiveControlCollection(
                tg.active_controls, "myProp", "StoppingConditions Duration TripValue"
            )

            GatorHelper.TestIAgVATargeterGraphResultCollection(tg.results, "myProp", "Epoch", 0)

    @staticmethod
    def Test_IAgVAScriptingTool(scriptingTool: "ScriptingTool", obj: str):
        scriptingTool.enable = True
        Assert.assertTrue(scriptingTool.enable)

        GatorHelper.TestScriptingToolSegmentProperties(scriptingTool.segment_properties, obj)

        GatorHelper.TestScriptingToolParameters(scriptingTool.parameters)

        GatorHelper.TestScriptingToolCalcObjects(scriptingTool.calc_objects)

        scriptingTool.language_type = LANGUAGE.J_SCRIPT
        Assert.assertEqual(LANGUAGE.J_SCRIPT, scriptingTool.language_type)
        scriptingTool.script_text("int j = 1;")
