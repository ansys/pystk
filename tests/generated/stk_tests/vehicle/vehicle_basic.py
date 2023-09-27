from test_util import *
from antenna.antenna_helper import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from orbit_state_helper import *
from orientation_helper import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


# region ExportDataFileHelper
class ExportDataFileHelper(object):
    def __init__(self, obj: "IStkObject", root: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        self._oObj: "IStkObject" = obj
        self._root: "IStkObjectRoot" = root

    # region AttitudeExport
    def AttitudeExportTool(self, attitude: "IVehicleAttitudeExportTool"):
        customAxes: "IVehicleCoordinateAxesCustom" = None

        def action1():
            attitude.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT410

        TryCatchAssertBlock.DoAssert("Invalid version number", action1)

        def action2():
            attitude.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT420

        TryCatchAssertBlock.DoAssert("Invalid version number", action2)

        def action3():
            attitude.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT620

        TryCatchAssertBlock.DoAssert("Invalid version number", action3)
        attitude.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT430
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.FORMAT430, attitude.version_format)
        attitude.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT600
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.FORMAT600, attitude.version_format)
        attitude.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT800
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.FORMAT800, attitude.version_format)
        attitude.version_format = EXPORT_TOOL_VERSION_FORMAT.CURRENT
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.CURRENT, attitude.version_format)

        # ****************************
        # Testing the Coordinate Axes
        # ****************************

        # Export for Attitude file type only supports versions 4.3, 6, 8, and current
        arSupportedVersionFormats: "EXPORT_TOOL_VERSION_FORMAT[]" = [
            EXPORT_TOOL_VERSION_FORMAT.FORMAT430,
            EXPORT_TOOL_VERSION_FORMAT.FORMAT600,
            EXPORT_TOOL_VERSION_FORMAT.FORMAT800,
            EXPORT_TOOL_VERSION_FORMAT.CURRENT,
        ]

        eFormat: "EXPORT_TOOL_VERSION_FORMAT"

        for eFormat in arSupportedVersionFormats:
            attitude.version_format = eFormat
            self.m_logger.WriteLine6("Version Format: {0}", attitude.version_format)
            if eFormat == EXPORT_TOOL_VERSION_FORMAT.CURRENT:
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.J2000)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.J2000, attitude.coordinate_axes_type)
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.FIXED)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.FIXED, attitude.coordinate_axes_type)
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.ICRF)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.ICRF, attitude.coordinate_axes_type)
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.CUSTOM)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.CUSTOM, attitude.coordinate_axes_type)
                customAxes = clr.Convert(attitude.coordinate_axes, IVehicleCoordinateAxesCustom)
                customAxes.reference_axes_name = "CentralBody/Sun J2000 Axes"
                Assert.assertEqual("CentralBody/Sun J2000 Axes", customAxes.reference_axes_name)

                def action4():
                    customAxes.reference_axes_name = "CentralBody/Sun Bogus Axes"

                TryCatchAssertBlock.DoAssert("IVehicleCoordinateAxesCustom.ReferenceAxesName - invalid choice", action4)
                if attitude.central_body_name != "Earth":
                    attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.INERTIAL)
                    Assert.assertEqual(ATTITUDE_COORDINATE_AXES.INERTIAL, attitude.coordinate_axes_type)

            elif eFormat == EXPORT_TOOL_VERSION_FORMAT.FORMAT800:
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.FIXED)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.FIXED, attitude.coordinate_axes_type)
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.CUSTOM)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.CUSTOM, attitude.coordinate_axes_type)
                customAxes = clr.Convert(attitude.coordinate_axes, IVehicleCoordinateAxesCustom)
                customAxes.reference_axes_name = "CentralBody/Sun J2000 Axes"
                if attitude.central_body_name == "Earth":
                    attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.J2000)
                    Assert.assertEqual(ATTITUDE_COORDINATE_AXES.J2000, attitude.coordinate_axes_type)

                else:
                    attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.INERTIAL)
                    Assert.assertEqual(ATTITUDE_COORDINATE_AXES.INERTIAL, attitude.coordinate_axes_type)

            else:
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.INERTIAL)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.INERTIAL, attitude.coordinate_axes_type)
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.FIXED)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.FIXED, attitude.coordinate_axes_type)
                attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.CUSTOM)
                Assert.assertEqual(ATTITUDE_COORDINATE_AXES.CUSTOM, attitude.coordinate_axes_type)
                customAxes = clr.Convert(attitude.coordinate_axes, IVehicleCoordinateAxesCustom)
                customAxes.reference_axes_name = "CentralBody/Sun J2000 Axes"

            supportedCoordinateAxes = attitude.supported_coordinate_axes
            ocoordAxis: typing.Any
            for ocoordAxis in supportedCoordinateAxes:
                coordAxis: "ATTITUDE_COORDINATE_AXES" = clr.Convert(int(ocoordAxis), ATTITUDE_COORDINATE_AXES)
                self.m_logger.WriteLine6("Supported coordinate axes: {0}", coordAxis)
                if eFormat == EXPORT_TOOL_VERSION_FORMAT.CURRENT:
                    if (
                        (
                            ((coordAxis == ATTITUDE_COORDINATE_AXES.FIXED))
                            or ((coordAxis == ATTITUDE_COORDINATE_AXES.ICRF))
                        )
                        or ((coordAxis == ATTITUDE_COORDINATE_AXES.J2000))
                    ) or ((coordAxis == ATTITUDE_COORDINATE_AXES.CUSTOM)):
                        pass
                    else:
                        if attitude.central_body_name == "Earth":
                            Assert.fail("Coordinate axis should not be supported.")

                elif eFormat == EXPORT_TOOL_VERSION_FORMAT.FORMAT800:
                    if ((coordAxis == ATTITUDE_COORDINATE_AXES.FIXED)) or (
                        (coordAxis == ATTITUDE_COORDINATE_AXES.CUSTOM)
                    ):
                        pass
                    else:
                        if (attitude.central_body_name == "Earth") and (coordAxis != ATTITUDE_COORDINATE_AXES.J2000):
                            Assert.fail("Coordinate axis should not be supported.")

                        elif (attitude.central_body_name != "Earth") and (
                            coordAxis != ATTITUDE_COORDINATE_AXES.INERTIAL
                        ):
                            Assert.fail("Coordinate axis should not be supported.")

                elif ((eFormat == EXPORT_TOOL_VERSION_FORMAT.FORMAT600)) or (
                    (eFormat == EXPORT_TOOL_VERSION_FORMAT.FORMAT430)
                ):
                    if (
                        ((coordAxis == ATTITUDE_COORDINATE_AXES.FIXED))
                        or ((coordAxis == ATTITUDE_COORDINATE_AXES.INERTIAL))
                    ) or ((coordAxis == ATTITUDE_COORDINATE_AXES.CUSTOM)):
                        pass
                    else:
                        Assert.fail("Coordinate axis should not be supported.")

        # Restore the version format and the coordinate axes
        attitude.version_format = EXPORT_TOOL_VERSION_FORMAT.CURRENT
        attitude.set_coordinate_axes_type(ATTITUDE_COORDINATE_AXES.CUSTOM)
        Assert.assertEqual(ATTITUDE_COORDINATE_AXES.CUSTOM, attitude.coordinate_axes_type)
        customAxes = clr.Convert(attitude.coordinate_axes, IVehicleCoordinateAxesCustom)
        customAxes.reference_axes_name = "CentralBody/Sun J2000 Axes"

        attitude.include = ATTITUDE_INCLUDE.QUATERNIONS
        Assert.assertEqual(ATTITUDE_INCLUDE.QUATERNIONS, attitude.include)
        attitude.include = ATTITUDE_INCLUDE.QUATERNIONS_ANGULAR_VELOCITY
        Assert.assertEqual(ATTITUDE_INCLUDE.QUATERNIONS_ANGULAR_VELOCITY, attitude.include)

        attitude.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS, attitude.time_period.time_period_type)
        attitude.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.SPECIFY, attitude.time_period.time_period_type)

        attitude.time_period.start = (clr.Convert(self._root.current_scenario, IScenario)).start_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).start_time, attitude.time_period.start)
        attitude.time_period.stop = (clr.Convert(self._root.current_scenario, IScenario)).stop_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).stop_time, attitude.time_period.stop)

        attitude.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.EPHEM
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.EPHEM, attitude.step_size.step_size_type)

        attitude.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.SPECIFY, attitude.step_size.step_size_type)
        attitude.step_size.value = 3600
        Assert.assertEqual(3600, attitude.step_size.value)

        attitude.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.NATIVE
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.NATIVE, attitude.step_size.step_size_type)

        attitude.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.TIME_ARRAY
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.TIME_ARRAY, attitude.step_size.step_size_type)

        objName: str = (self._oObj.class_name + "/") + self._oObj.instance_name

        attitude.step_size.time_array = objName + " OneMinuteSampleTimes EventArray"
        Assert.assertEqual((objName + " OneMinuteSampleTimes EventArray"), attitude.step_size.time_array)

        def action5():
            attitude.step_size.time_array = objName + " Bogus EventArray"

        TryCatchAssertBlock.DoAssert("IExportToolStepSize.TimeArray - invalid choice", action5)

        attitude.export(TestBase.GetScenarioFile("OMExternalFileAttitude.a"))

        self._root.execute_command(
            (
                (
                    (
                        (
                            (("ExportDataFile " + self._oObj.path) + ' Attitude "')
                            + TestBase.GetScenarioFile("ConnectExternalFileAttitude.a")
                        )
                        + '" Details QuatAngVel CoordAxes Custom "CentralBody/Sun J2000" TimeSteps "'
                    )
                    + objName
                )
                + ' OneMinuteSampleTimes Time Array"'
            )
        )

        omFileContent = File.ReadAllBytes(TestBase.GetScenarioFile("OMExternalFileAttitude.a"))
        connectFileContent = File.ReadAllBytes(TestBase.GetScenarioFile("ConnectExternalFileAttitude.a"))

        Assert.assertEqual(omFileContent, connectFileContent)

        File.Delete(TestBase.GetScenarioFile("OMExternalFileAttitude.a"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileAttitude.a"))

    # endregion

    # region PropDefExportTool
    def PropDefExportTool(self, dataFile: "IVehiclePropDefinitionExportTool"):
        dataFile.export(TestBase.GetScenarioFile("OMExternalFilePropDef.pg"))
        self._root.execute_command(
            (
                (
                    (("ExportDataFile " + self._oObj.path) + ' PropDef "')
                    + TestBase.GetScenarioFile("ConnectExternalFilePropDef.pg")
                )
                + '"'
            )
        )

        omFileContent = File.ReadAllBytes(TestBase.GetScenarioFile("OMExternalFilePropDef.pg"))
        connectFileContent = File.ReadAllBytes(TestBase.GetScenarioFile("ConnectExternalFilePropDef.pg"))
        Assert.assertEqual(omFileContent, connectFileContent)

    # endregion

    def CompareCCSDSWithOneSecondTolerance(self, omFile: str, connectFile: str):
        try:
            Assert.assertEqual(omFile, connectFile)

        except Exception:
            # The creation date might have spanned a second boundary between the OM run and the Connect run.

            # Format:  "CREATION_DATE  = 2010-09-21T14:00:06"
            pos: int = connectFile.find("CREATION_DATE")
            oldCreationDate: str = connectFile[pos:36]  # e.g. "2010-09-21T14:00:06"

            s: str = oldCreationDate[17:4]

            year: int = Convert.ToInt16(oldCreationDate[17:4])
            mon: int = Convert.ToInt16(oldCreationDate[22:2])
            day: int = Convert.ToInt16(oldCreationDate[25:2])
            hour: int = Convert.ToInt16(oldCreationDate[28:2])
            min: int = Convert.ToInt16(oldCreationDate[31:2])
            sec: int = Convert.ToInt16(oldCreationDate[34:2])

            dt = DateTime(year, mon, day, hour, min, sec)
            dt2 = dt.AddSeconds(-1)

            newCreationDate: str = (
                (
                    (
                        (
                            (
                                (
                                    (((("CREATION_DATE  = " + str(dt2.Year)) + "-") + dt2.Month.ToString("D2")) + "-")
                                    + dt2.Day.ToString("D2")
                                )
                                + "T"
                            )
                            + dt2.Hour.ToString("D2")
                        )
                        + ":"
                    )
                    + dt2.Minute.ToString("D2")
                )
                + ":"
            ) + dt2.Second.ToString("D2")

            connectFile = connectFile.replace(oldCreationDate, newCreationDate)

            Assert.assertEqual(omFile, connectFile)

    # region EphemerisSTKExportTool
    def EphemerisSTKExportTool(self, stkEphem: "IVehicleEphemerisStkExportTool", isSat: bool):
        # "Satellite1.e"
        stkEphem.coordinate_system = STK_EPHEM_COORDINATE_SYSTEM.FIXED
        Assert.assertEqual(STK_EPHEM_COORDINATE_SYSTEM.FIXED, stkEphem.coordinate_system)
        # only works with Earth cb validates it when it gets exported.
        stkEphem.coordinate_system = STK_EPHEM_COORDINATE_SYSTEM.INERTIAL
        Assert.assertEqual(STK_EPHEM_COORDINATE_SYSTEM.INERTIAL, stkEphem.coordinate_system)
        stkEphem.coordinate_system = STK_EPHEM_COORDINATE_SYSTEM.J2000
        Assert.assertEqual(STK_EPHEM_COORDINATE_SYSTEM.J2000, stkEphem.coordinate_system)

        Assert.assertTrue(stkEphem.use_vehicle_central_body)
        Assert.assertEqual("Earth", stkEphem.central_body_name)
        if isSat:

            def action6():
                stkEphem.central_body_name = "Europa"

            TryCatchAssertBlock.ExpectedException("read-only", action6)

            stkEphem.use_vehicle_central_body = False
            Assert.assertFalse(stkEphem.use_vehicle_central_body)

            stkEphem.central_body_name = "Europa"
            Assert.assertEqual("Europa", stkEphem.central_body_name)

            def action7():
                stkEphem.central_body_name = "Uvanus"

            TryCatchAssertBlock.ExpectedException("must be in", action7)

        else:

            def action8():
                stkEphem.central_body_name = "Europa"

            TryCatchAssertBlock.ExpectedException("read-only", action8)

        stkEphem.include_interp = False
        Assert.assertFalse(stkEphem.include_interp)
        stkEphem.include_interp = True
        Assert.assertTrue(stkEphem.include_interp)

        def action9():
            stkEphem.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT600

        TryCatchAssertBlock.ExpectedException("must be in", action9)
        stkEphem.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT410
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.FORMAT410, stkEphem.version_format)
        stkEphem.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT420
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.FORMAT420, stkEphem.version_format)
        stkEphem.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT430
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.FORMAT430, stkEphem.version_format)
        stkEphem.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT620
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.FORMAT620, stkEphem.version_format)
        stkEphem.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT800
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.FORMAT800, stkEphem.version_format)
        stkEphem.version_format = EXPORT_TOOL_VERSION_FORMAT.CURRENT
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.CURRENT, stkEphem.version_format)

        stkEphem.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS, stkEphem.time_period.time_period_type)
        stkEphem.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.SPECIFY, stkEphem.time_period.time_period_type)
        stkEphem.time_period.start = (clr.Convert(self._root.current_scenario, IScenario)).start_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).start_time, stkEphem.time_period.start)
        stkEphem.time_period.stop = (clr.Convert(self._root.current_scenario, IScenario)).stop_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).stop_time, stkEphem.time_period.stop)

        def action10():
            stkEphem.covariance_type = STK_EPHEM_COVARIANCE_TYPE.POSITION3_X3

        TryCatchAssertBlock.ExpectedException("read-only", action10)

        def action11():
            stkEphem.covariance_type = STK_EPHEM_COVARIANCE_TYPE.POSITION_VELOCITY6_X6

        TryCatchAssertBlock.ExpectedException("read-only", action11)

        stkEphem.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.EPHEM
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.EPHEM, stkEphem.step_size.step_size_type)
        stkEphem.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.SPECIFY, stkEphem.step_size.step_size_type)
        stkEphem.step_size.value = 3600
        Assert.assertEqual(3600, stkEphem.step_size.value)

        def action12():
            stkEphem.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.NATIVE

        TryCatchAssertBlock.ExpectedException("must be in", action12)

        stkEphem.export(TestBase.GetScenarioFile("OMExternalFileStk.e"))
        if isSat:
            self._root.execute_command(
                (
                    (
                        (
                            (
                                (
                                    (
                                        (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                        + TestBase.GetScenarioFile("ConnectExternalFileStk.e")
                                    )
                                    + '" Type STK CentralBody Europa CoordSys J2000 InterpBoundaries Include StepSize 3600 TimePeriod "'
                                )
                                + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                            )
                            + '" "'
                        )
                        + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                    )
                    + '"'
                )
            )

        else:
            self._root.execute_command(
                (
                    (
                        (
                            (
                                (
                                    (
                                        (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                        + TestBase.GetScenarioFile("ConnectExternalFileStk.e")
                                    )
                                    + '" Type STK CentralBody Earth CoordSys J2000 InterpBoundaries Include StepSize 3600 TimePeriod "'
                                )
                                + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                            )
                            + '" "'
                        )
                        + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                    )
                    + '"'
                )
            )

        omFileContent = File.ReadAllBytes(TestBase.GetScenarioFile("OMExternalFileStk.e"))
        connectFileContent = File.ReadAllBytes(TestBase.GetScenarioFile("ConnectExternalFileStk.e"))

        Assert.assertEqual(omFileContent, connectFileContent)

    # endregion

    # region EphemerisCCSDSExportTool
    def EphemerisCCSDSExportTool(self, ccsds: "IVehicleEphemerisCCSDSExportTool"):
        # Test "UseSatelliteCenterAndFrame"
        ccsds.use_satellite_center_and_frame = False
        Assert.assertFalse(ccsds.use_satellite_center_and_frame)

        # Check that the CentralBody and ReferenceFrame are writable
        ccsds.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", ccsds.central_body_name)
        ccsds.reference_frame = CCSDS_REFERENCE_FRAME.EME2000
        Assert.assertEqual(CCSDS_REFERENCE_FRAME.EME2000, ccsds.reference_frame)

        ccsds.use_satellite_center_and_frame = True
        Assert.assertTrue(ccsds.use_satellite_center_and_frame)

        def action13():
            ccsds.central_body_name = "Earth"

        TryCatchAssertBlock.ExpectedException("read-only", action13)

        def action14():
            ccsds.reference_frame = CCSDS_REFERENCE_FRAME.FIXED

        TryCatchAssertBlock.ExpectedException("read-only", action14)

        ccsds.use_satellite_center_and_frame = False

        ccsds.originator = "Test1"
        Assert.assertEqual("Test1", ccsds.originator)
        ccsds.object_id = "2000-000B"
        Assert.assertEqual("2000-000B", ccsds.object_id)
        ccsds.object_name = "TestSatellite"
        Assert.assertEqual("TestSatellite", ccsds.object_name)
        ccsds.central_body_name = "Moon"
        Assert.assertEqual("Moon", ccsds.central_body_name)

        def action15():
            ccsds.central_body_name = "Uvanus"

        TryCatchAssertBlock.ExpectedException("must be in", action15)

        # specific central bodies have specific reference frames  (See 42071)
        # Earth:  ICRF, J2000, TOD, ITRF, Fixed, TEME, ITRF frames
        ccsds.central_body_name = "Earth"
        RefsSupported = ccsds.reference_frames_supported
        refTypeObj: typing.Any
        for refTypeObj in RefsSupported:
            refType: "CCSDS_REFERENCE_FRAME" = clr.Convert(int(refTypeObj), CCSDS_REFERENCE_FRAME)
            ccsds.reference_frame = refType
            Assert.assertEqual(refType, ccsds.reference_frame)

        def action16():
            ccsds.reference_frame = CCSDS_REFERENCE_FRAME.MEAN_EARTH

        TryCatchAssertBlock.ExpectedException("must be in ", action16)

        # Moon: ICRF, J2000, TOD, MeanEarth, Fixed
        ccsds.central_body_name = "Moon"
        RefsSupported = ccsds.reference_frames_supported
        refTypeObj: typing.Any
        for refTypeObj in RefsSupported:
            refType: "CCSDS_REFERENCE_FRAME" = clr.Convert(int(refTypeObj), CCSDS_REFERENCE_FRAME)
            ccsds.reference_frame = refType
            Assert.assertEqual(refType, ccsds.reference_frame)

        def action17():
            ccsds.reference_frame = CCSDS_REFERENCE_FRAME.ITRF

        TryCatchAssertBlock.ExpectedException("must be in", action17)

        # other cb's: ICRF, J2000, TOD, Fixed
        ccsds.central_body_name = "Sun"
        RefsSupported = ccsds.reference_frames_supported
        refTypeObj: typing.Any
        for refTypeObj in RefsSupported:
            refType: "CCSDS_REFERENCE_FRAME" = clr.Convert(int(refTypeObj), CCSDS_REFERENCE_FRAME)
            ccsds.reference_frame = refType
            Assert.assertEqual(refType, ccsds.reference_frame)

        def action18():
            ccsds.reference_frame = CCSDS_REFERENCE_FRAME.ITRF

        TryCatchAssertBlock.ExpectedException("must be in", action18)

        def action19():
            ccsds.reference_frame = CCSDS_REFERENCE_FRAME.MEAN_EARTH

        TryCatchAssertBlock.ExpectedException("must be in", action19)

        # pick a valid combination
        ccsds.central_body_name = "Moon"
        ccsds.reference_frame = CCSDS_REFERENCE_FRAME.EME2000

        ccsds.time_precision = 7
        Assert.assertEqual(7, ccsds.time_precision)
        ccsds.date_format = CCSDS_DATE_FORMAT.YDOY
        Assert.assertEqual(CCSDS_DATE_FORMAT.YDOY, ccsds.date_format)
        ccsds.date_format = CCSDS_DATE_FORMAT.YMD
        Assert.assertEqual(CCSDS_DATE_FORMAT.YMD, ccsds.date_format)
        ccsds.ephemeris_format = CCSDS_EPHEM_FORMAT.FLOATING_POINT
        Assert.assertEqual(CCSDS_EPHEM_FORMAT.FLOATING_POINT, ccsds.ephemeris_format)
        ccsds.ephemeris_format = CCSDS_EPHEM_FORMAT.SCI_NOTATION
        Assert.assertEqual(CCSDS_EPHEM_FORMAT.SCI_NOTATION, ccsds.ephemeris_format)

        ccsds.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS, ccsds.time_period.time_period_type)
        ccsds.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.SPECIFY, ccsds.time_period.time_period_type)
        ccsds.time_period.start = (clr.Convert(self._root.current_scenario, IScenario)).start_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).start_time, ccsds.time_period.start)
        ccsds.time_period.stop = (clr.Convert(self._root.current_scenario, IScenario)).stop_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).stop_time, ccsds.time_period.stop)

        ccsds.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.EPHEM
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.EPHEM, ccsds.step_size.step_size_type)
        ccsds.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.SPECIFY, ccsds.step_size.step_size_type)
        ccsds.step_size.value = 3600
        Assert.assertEqual(3600, ccsds.step_size.value)

        def action20():
            ccsds.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.NATIVE

        TryCatchAssertBlock.DoAssert("must be in", action20)

        ccsds.time_system = CCSDS_TIME_SYSTEM.GPS
        Assert.assertEqual(CCSDS_TIME_SYSTEM.GPS, ccsds.time_system)
        ccsds.time_system = CCSDS_TIME_SYSTEM.TAI
        Assert.assertEqual(CCSDS_TIME_SYSTEM.TAI, ccsds.time_system)
        ccsds.time_system = CCSDS_TIME_SYSTEM.TDB
        Assert.assertEqual(CCSDS_TIME_SYSTEM.TDB, ccsds.time_system)
        ccsds.time_system = CCSDS_TIME_SYSTEM.TT
        Assert.assertEqual(CCSDS_TIME_SYSTEM.TT, ccsds.time_system)
        ccsds.time_system = CCSDS_TIME_SYSTEM.UTC
        Assert.assertEqual(CCSDS_TIME_SYSTEM.UTC, ccsds.time_system)

        ccsds.export(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem")
                                )
                                + '" Type CCSDS CenterName Moon RefFrame EME2000 Originator Test1 ObjectName TestSatellite ObjectID 2000-000B TimePrecision 7 DateFormat YMD EphFormat SciNotation StepSize 3600 TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '"'
            )
        )

        om = FileInfo(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        omSr = om.OpenText()
        omFile: str = omSr.ReadToEnd()
        omSr.Close()

        connect = FileInfo(TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem"))
        connectSr = connect.OpenText()
        connectFile: str = connectSr.ReadToEnd()
        connectSr.Close()
        self.CompareCCSDSWithOneSecondTolerance(omFile, connectFile)

        # Test whether the names with ws are handled
        ccsds.originator = "Originator with ws"
        Assert.assertEqual(ccsds.originator, "Originator with ws")
        ccsds.object_id = "ObjectID with ws"
        Assert.assertEqual(ccsds.object_id, "ObjectID with ws")
        ccsds.object_name = "ObjectName with ws"
        Assert.assertEqual(ccsds.object_name, "ObjectName with ws")
        ccsds.export(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem")
                                )
                                + '" Type CCSDS CenterName Moon RefFrame EME2000 Originator "Originator with ws" ObjectName "ObjectName with ws" ObjectID "ObjectID with ws" TimePrecision 7 DateFormat YMD EphFormat SciNotation StepSize 3600 TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '"'
            )
        )

        om = FileInfo(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        omSr = om.OpenText()
        omFile = omSr.ReadToEnd()
        omSr.Close()

        connect = FileInfo(TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem"))
        connectSr = connect.OpenText()
        connectFile = connectSr.ReadToEnd()
        connectSr.Close()
        self.CompareCCSDSWithOneSecondTolerance(omFile, connectFile)

        # export CCSDS ephemeris using the satellite's center and reference frame
        ccsds.use_satellite_center_and_frame = True
        ccsds.export(TestBase.GetScenarioFile("OMExternalFileCCSDS_1.oem"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCCSDS_1.oem")
                                )
                                + '" Type CCSDS CenterName Moon RefFrame EME2000 Originator "Originator with ws" ObjectName "ObjectName with ws" ObjectID "ObjectID with ws" TimePrecision 7 DateFormat YMD EphFormat SciNotation StepSize 3600 TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '" UseSatCenterAndFrame Yes'
            )
        )

        om = FileInfo(TestBase.GetScenarioFile("OMExternalFileCCSDS_1.oem"))
        omSr = om.OpenText()
        omFile = omSr.ReadToEnd()
        omSr.Close()

        connect = FileInfo(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_1.oem"))
        connectSr = connect.OpenText()
        connectFile = connectSr.ReadToEnd()
        connectSr.Close()
        self.CompareCCSDSWithOneSecondTolerance(omFile, connectFile)

    # endregion

    # region EphemerisCCSDSv2ExportTool
    def EphemerisCCSDSv2ExportTool(self, ccsdsv2: "IVehicleEphemerisCCSDSv2ExportTool"):
        # Test "UseSatelliteCenterAndFrame"
        ccsdsv2.use_satellite_center_and_frame = False
        Assert.assertFalse(ccsdsv2.use_satellite_center_and_frame)

        # Check that the CentralBody and ReferenceFrame are writable
        ccsdsv2.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", ccsdsv2.central_body_name)
        ccsdsv2.reference_frame = CCSDS_REFERENCE_FRAME.EME2000
        Assert.assertEqual(CCSDS_REFERENCE_FRAME.EME2000, ccsdsv2.reference_frame)

        ccsdsv2.use_satellite_center_and_frame = True
        Assert.assertTrue(ccsdsv2.use_satellite_center_and_frame)

        def action21():
            ccsdsv2.central_body_name = "Earth"

        TryCatchAssertBlock.ExpectedException("read-only", action21)

        def action22():
            ccsdsv2.reference_frame = CCSDS_REFERENCE_FRAME.FIXED

        TryCatchAssertBlock.ExpectedException("read-only", action22)

        ccsdsv2.use_satellite_center_and_frame = False

        ccsdsv2.originator = "Test1"
        Assert.assertEqual("Test1", ccsdsv2.originator)
        ccsdsv2.object_id = "2000-000B"
        Assert.assertEqual("2000-000B", ccsdsv2.object_id)
        ccsdsv2.object_name = "TestSatellite"
        Assert.assertEqual("TestSatellite", ccsdsv2.object_name)
        ccsdsv2.central_body_name = "Moon"
        Assert.assertEqual("Moon", ccsdsv2.central_body_name)

        def action23():
            ccsdsv2.central_body_name = "Uvanus"

        TryCatchAssertBlock.ExpectedException("must be in", action23)

        # specific central bodies have specific reference frames  (See 42071)
        # Earth:  ICRF, J2000, TOD, ITRF, Fixed, ITRF frames
        ccsdsv2.central_body_name = "Earth"
        RefsSupported = ccsdsv2.reference_frames_supported
        refTypeObj: typing.Any
        for refTypeObj in RefsSupported:
            refType: "CCSDS_REFERENCE_FRAME" = clr.Convert(int(refTypeObj), CCSDS_REFERENCE_FRAME)
            ccsdsv2.reference_frame = refType
            Assert.assertEqual(refType, ccsdsv2.reference_frame)

        def action24():
            ccsdsv2.reference_frame = CCSDS_REFERENCE_FRAME.MEAN_EARTH

        TryCatchAssertBlock.ExpectedException("must be in", action24)

        # Moon: ICRF, J2000, TOD, MeanEarth, Fixed
        ccsdsv2.central_body_name = "Moon"
        RefsSupported = ccsdsv2.reference_frames_supported
        refTypeObj: typing.Any
        for refTypeObj in RefsSupported:
            refType: "CCSDS_REFERENCE_FRAME" = clr.Convert(int(refTypeObj), CCSDS_REFERENCE_FRAME)
            ccsdsv2.reference_frame = refType
            Assert.assertEqual(refType, ccsdsv2.reference_frame)

        def action25():
            ccsdsv2.reference_frame = CCSDS_REFERENCE_FRAME.ITRF

        TryCatchAssertBlock.ExpectedException("must be in", action25)

        # other cb's: ICRF, J2000, TOD, Fixed
        ccsdsv2.central_body_name = "Sun"
        RefsSupported = ccsdsv2.reference_frames_supported
        refTypeObj: typing.Any
        for refTypeObj in RefsSupported:
            refType: "CCSDS_REFERENCE_FRAME" = clr.Convert(int(refTypeObj), CCSDS_REFERENCE_FRAME)
            ccsdsv2.reference_frame = refType
            Assert.assertEqual(refType, ccsdsv2.reference_frame)

        def action26():
            ccsdsv2.reference_frame = CCSDS_REFERENCE_FRAME.ITRF

        TryCatchAssertBlock.ExpectedException("must be in", action26)

        def action27():
            ccsdsv2.reference_frame = CCSDS_REFERENCE_FRAME.MEAN_EARTH

        TryCatchAssertBlock.ExpectedException("must be in", action27)

        # pick a valid combination
        ccsdsv2.central_body_name = "Moon"
        ccsdsv2.reference_frame = CCSDS_REFERENCE_FRAME.EME2000

        ccsdsv2.time_precision = 7
        Assert.assertEqual(7, ccsdsv2.time_precision)
        ccsdsv2.date_format = CCSDS_DATE_FORMAT.YDOY
        Assert.assertEqual(CCSDS_DATE_FORMAT.YDOY, ccsdsv2.date_format)
        ccsdsv2.date_format = CCSDS_DATE_FORMAT.YMD
        Assert.assertEqual(CCSDS_DATE_FORMAT.YMD, ccsdsv2.date_format)
        ccsdsv2.ephemeris_format = CCSDS_EPHEM_FORMAT.FLOATING_POINT
        Assert.assertEqual(CCSDS_EPHEM_FORMAT.FLOATING_POINT, ccsdsv2.ephemeris_format)
        ccsdsv2.ephemeris_format = CCSDS_EPHEM_FORMAT.SCI_NOTATION
        Assert.assertEqual(CCSDS_EPHEM_FORMAT.SCI_NOTATION, ccsdsv2.ephemeris_format)

        ccsdsv2.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS, ccsdsv2.time_period.time_period_type)
        ccsdsv2.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.SPECIFY, ccsdsv2.time_period.time_period_type)
        ccsdsv2.time_period.start = (clr.Convert(self._root.current_scenario, IScenario)).start_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).start_time, ccsdsv2.time_period.start)
        ccsdsv2.time_period.stop = (clr.Convert(self._root.current_scenario, IScenario)).stop_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).stop_time, ccsdsv2.time_period.stop)

        ccsdsv2.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.EPHEM
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.EPHEM, ccsdsv2.step_size.step_size_type)
        ccsdsv2.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.SPECIFY, ccsdsv2.step_size.step_size_type)
        ccsdsv2.step_size.value = 3600
        Assert.assertEqual(3600, ccsdsv2.step_size.value)

        def action28():
            ccsdsv2.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.NATIVE

        TryCatchAssertBlock.DoAssert("Invalid Step size type", action28)

        ccsdsv2.time_system = CCSDS_TIME_SYSTEM.GPS
        Assert.assertEqual(CCSDS_TIME_SYSTEM.GPS, ccsdsv2.time_system)
        ccsdsv2.time_system = CCSDS_TIME_SYSTEM.TAI
        Assert.assertEqual(CCSDS_TIME_SYSTEM.TAI, ccsdsv2.time_system)
        ccsdsv2.time_system = CCSDS_TIME_SYSTEM.TDB
        Assert.assertEqual(CCSDS_TIME_SYSTEM.TDB, ccsdsv2.time_system)
        ccsdsv2.time_system = CCSDS_TIME_SYSTEM.TT
        Assert.assertEqual(CCSDS_TIME_SYSTEM.TT, ccsdsv2.time_system)
        ccsdsv2.time_system = CCSDS_TIME_SYSTEM.UTC
        Assert.assertEqual(CCSDS_TIME_SYSTEM.UTC, ccsdsv2.time_system)

        ccsdsv2.export(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem")
                                )
                                + '" Type CCSDSv2 CenterName Moon RefFrame EME2000 Originator Test1 ObjectName TestSatellite ObjectID 2000-000B TimePrecision 7 DateFormat YMD EphFormat SciNotation StepSize 3600 TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '"'
            )
        )

        om = FileInfo(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        omSr = om.OpenText()
        omFile: str = omSr.ReadToEnd()
        omSr.Close()

        connect = FileInfo(TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem"))
        connectSr = connect.OpenText()
        connectFile: str = connectSr.ReadToEnd()
        connectSr.Close()
        self.CompareCCSDSWithOneSecondTolerance(omFile, connectFile)

        # Test whether the names with ws are handled
        ccsdsv2.originator = "Originator with ws"
        Assert.assertEqual(ccsdsv2.originator, "Originator with ws")
        ccsdsv2.object_id = "ObjectID with ws"
        Assert.assertEqual(ccsdsv2.object_id, "ObjectID with ws")
        ccsdsv2.object_name = "ObjectName with ws"
        Assert.assertEqual(ccsdsv2.object_name, "ObjectName with ws")
        ccsdsv2.export(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem")
                                )
                                + '" Type CCSDSv2 CenterName Moon RefFrame EME2000 Originator "Originator with ws" ObjectName "ObjectName with ws" ObjectID "ObjectID with ws" TimePrecision 7 DateFormat YMD EphFormat SciNotation StepSize 3600 TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '"'
            )
        )

        om = FileInfo(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        omSr = om.OpenText()
        omFile = omSr.ReadToEnd()
        omSr.Close()

        connect = FileInfo(TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem"))
        connectSr = connect.OpenText()
        connectFile = connectSr.ReadToEnd()
        connectSr.Close()
        self.CompareCCSDSWithOneSecondTolerance(omFile, connectFile)

        # export CCSDS ephemeris using the satellite's center and reference frame
        ccsdsv2.use_satellite_center_and_frame = True
        ccsdsv2.export(TestBase.GetScenarioFile("OMExternalFileCCSDS_1.oem"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCCSDS_1.oem")
                                )
                                + '" Type CCSDSv2 CenterName Moon RefFrame EME2000 Originator "Originator with ws" ObjectName "ObjectName with ws" ObjectID "ObjectID with ws" TimePrecision 7 DateFormat YMD EphFormat SciNotation StepSize 3600 TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '" UseSatCenterAndFrame Yes'
            )
        )

        om = FileInfo(TestBase.GetScenarioFile("OMExternalFileCCSDS_1.oem"))
        omSr = om.OpenText()
        omFile = omSr.ReadToEnd()
        omSr.Close()

        connect = FileInfo(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_1.oem"))
        connectSr = connect.OpenText()
        connectFile = connectSr.ReadToEnd()
        connectSr.Close()
        self.CompareCCSDSWithOneSecondTolerance(omFile, connectFile)

        # Properties specific to v2

        Assert.assertFalse(ccsdsv2.has_covariance_data)
        Assert.assertFalse(ccsdsv2.include_covariance)

        def action29():
            ccsdsv2.include_covariance = True

        TryCatchAssertBlock.ExpectedException("read-only", action29)

        ccsdsv2.include_acceleration = False
        Assert.assertFalse(ccsdsv2.include_acceleration)
        ccsdsv2.include_acceleration = True
        Assert.assertTrue(ccsdsv2.include_acceleration)

        ccsdsv2.file_format = EPHEM_EXPORT_TOOL_FILE_FORMAT.CCSD_SV2_ORBIT_EPHEMERIS_MESSAGE
        Assert.assertEqual(EPHEM_EXPORT_TOOL_FILE_FORMAT.CCSD_SV2_ORBIT_EPHEMERIS_MESSAGE, ccsdsv2.file_format)

        ccsdsv2.export(TestBase.GetScenarioFile("OMExternalFileCCSDS_2.oem"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCCSDS_2.oem")
                                )
                                + '" Type CCSDSv2 CenterName Moon RefFrame EME2000 Originator "Originator with ws" ObjectName "ObjectName with ws" ObjectID "ObjectID with ws" TimePrecision 7 DateFormat YMD EphFormat SciNotation StepSize 3600 IncludeAcceleration Yes FileFormat KVN TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '" UseSatCenterAndFrame Yes'
            )
        )

        om = FileInfo(TestBase.GetScenarioFile("OMExternalFileCCSDS_2.oem"))
        omSr = om.OpenText()
        omFile = omSr.ReadToEnd()
        omSr.Close()

        connect = FileInfo(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_2.oem"))
        connectSr = connect.OpenText()
        connectFile = connectSr.ReadToEnd()
        connectSr.Close()
        self.CompareCCSDSWithOneSecondTolerance(omFile, connectFile)

        ccsdsv2.file_format = EPHEM_EXPORT_TOOL_FILE_FORMAT.CCSD_SV2_XML
        Assert.assertEqual(EPHEM_EXPORT_TOOL_FILE_FORMAT.CCSD_SV2_XML, ccsdsv2.file_format)

        ccsdsv2.export(TestBase.GetScenarioFile("OMExternalFileCCSDS_3.oem"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCCSDS_3.oem")
                                )
                                + '" Type CCSDSv2 CenterName Moon RefFrame EME2000 Originator "Originator with ws" ObjectName "ObjectName with ws" ObjectID "ObjectID with ws" TimePrecision 7 DateFormat YMD EphFormat SciNotation StepSize 3600 IncludeAcceleration Yes FileFormat XML TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '" UseSatCenterAndFrame Yes'
            )
        )

        om = FileInfo(TestBase.GetScenarioFile("OMExternalFileCCSDS_3.oem"))
        omSr = om.OpenText()
        omFile = omSr.ReadToEnd()
        omSr.Close()

        connect = FileInfo(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_3.oem"))
        connectSr = connect.OpenText()
        connectFile = connectSr.ReadToEnd()
        connectSr.Close()
        self.CompareCCSDSWithOneSecondTolerance(omFile, connectFile)

    # endregion

    # region EphemerisCode500ExportTool
    def EphemerisCode500ExportTool(self, code500: "IVehicleEphemerisCode500ExportTool"):
        code500.sat_id = 40
        Assert.assertEqual(40, code500.sat_id)

        code500.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS, code500.time_period.time_period_type)
        code500.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.SPECIFY, code500.time_period.time_period_type)
        code500.time_period.start = (clr.Convert(self._root.current_scenario, IScenario)).start_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).start_time, code500.time_period.start)
        code500.time_period.stop = (clr.Convert(self._root.current_scenario, IScenario)).stop_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).stop_time, code500.time_period.stop)

        code500.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.EPHEM
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.EPHEM, code500.step_size.step_size_type)
        code500.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.SPECIFY, code500.step_size.step_size_type)
        code500.step_size.value = 3600
        Assert.assertEqual(3600, code500.step_size.value)

        def action30():
            code500.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.NATIVE

        TryCatchAssertBlock.DoAssert("Invalid Step size type", action30)

        # this part only works if you have the code500 dll loaded.
        code500.export(TestBase.GetScenarioFile("OMExternalFileCode500.eph"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileCode500.eph")
                                )
                                + '" Type Code500 StepSize 3600 SatelliteID 40 TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '"'
            )
        )

        omFile = File.ReadAllBytes(TestBase.GetScenarioFile("OMExternalFileCode500.eph"))
        connectFile = File.ReadAllBytes(TestBase.GetScenarioFile("ConnectExternalFileCode500.eph"))

        Assert.assertEqual(omFile, connectFile)

    # endregion

    # region EphemerisSpiceExportTool
    def EphemerisSpiceExportTool(self, spice: "IVehicleEphemerisSpiceExportTool"):
        Assert.assertTrue(spice.use_vehicle_central_body)
        Assert.assertEqual("Earth", spice.central_body_name)

        def action31():
            spice.central_body_name = "Sun"

        TryCatchAssertBlock.ExpectedException("read-only", action31)

        spice.use_vehicle_central_body = False
        Assert.assertFalse(spice.use_vehicle_central_body)

        spice.central_body_name = "Sun"
        Assert.assertEqual("Sun", spice.central_body_name)

        def action32():
            spice.central_body_name = "Uvanus"

        TryCatchAssertBlock.ExpectedException("must be in", action32)

        spice.sat_id = -200001
        Assert.assertEqual(-200001, spice.sat_id)
        spice.interpolation_type = SPICE_INTERPOLATION.INTERPOLATION09_LANGRANGIAN
        Assert.assertEqual(SPICE_INTERPOLATION.INTERPOLATION09_LANGRANGIAN, spice.interpolation_type)
        spice.interpolation_type = SPICE_INTERPOLATION.INTERPOLATION13_HERMITIAN
        Assert.assertEqual(SPICE_INTERPOLATION.INTERPOLATION13_HERMITIAN, spice.interpolation_type)
        spice.interpolation = 7
        Assert.assertEqual(7, spice.interpolation)

        spice.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS, spice.time_period.time_period_type)
        spice.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.SPECIFY, spice.time_period.time_period_type)
        spice.time_period.start = (clr.Convert(self._root.current_scenario, IScenario)).start_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).start_time, spice.time_period.start)
        spice.time_period.stop = (clr.Convert(self._root.current_scenario, IScenario)).stop_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).stop_time, spice.time_period.stop)

        spice.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.EPHEM
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.EPHEM, spice.step_size.step_size_type)
        spice.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.SPECIFY, spice.step_size.step_size_type)
        spice.step_size.value = 3600
        Assert.assertEqual(3600, spice.step_size.value)

        def action33():
            spice.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.NATIVE

        TryCatchAssertBlock.ExpectedException("must be in", action33)

        spice.export(TestBase.GetScenarioFile("OMExternalFileSpice.bsp"))
        self._root.execute_command(
            (
                (
                    (
                        (
                            (
                                (
                                    (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                    + TestBase.GetScenarioFile("ConnectExternalFileSpice.bsp")
                                )
                                + '" Type Spice CentralBody Sun SatelliteID -200001 InterpType Type13 InterpOrder 7 StepSize 3600 TimePeriod "'
                            )
                            + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                        )
                        + '" "'
                    )
                    + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                )
                + '"'
            )
        )

        omFile = File.ReadAllBytes(TestBase.GetScenarioFile("OMExternalFileSpice.bsp"))
        connectFile = File.ReadAllBytes(TestBase.GetScenarioFile("ConnectExternalFileSpice.bsp"))

        Assert.assertEqual(omFile, connectFile)

    # endregion

    @staticmethod
    def IndexOf(array, pattern, offset: int):
        success: int = 0

        index: int = offset
        while index < Array.Length(array):
            if array[index] == pattern[success]:
                success += 1

            else:
                success = 0

            if Array.Length(pattern) == success:
                return (index - Array.Length(pattern)) + 1

            index += 1

        return -1

    @staticmethod
    def RedactCreationDate(array):
        # The STK binary ephemeris files contains a header with metadata including the creation date
        # in an XML section:
        #     <CreationDate Format = "Gregorian" TimeStandard = "UTC">
        #        <Value> 20190124133655.000000 </Value>
        #     </CreationDate>
        # The problem is that the EphemerisStkBinaryExportTool test compares a file generated by the object
        # model to a file generated by connect. If the current second changes in between the two file
        # generations, we end up with differences, i.e.
        #    <Value>20190124133655.000000</Value> vs. <Value>20190124133656.000000</Value>
        # This function erases the time stamp to prevent those differences, i.e.
        #        <Value>XXXXXXXXXXXXXXXXXXXXX</Value>

        creationDateBeginTag: int = ExportDataFileHelper.IndexOf(array, Encoding.ASCII.GetBytes("<CreationDate"), 0)
        creationDateValueBeginTag: int = ExportDataFileHelper.IndexOf(
            array, Encoding.ASCII.GetBytes("<Value>"), creationDateBeginTag
        )
        creationDateValueEndTag: int = ExportDataFileHelper.IndexOf(
            array, Encoding.ASCII.GetBytes("</Value>"), creationDateValueBeginTag
        )
        creationDateEndTag: int = ExportDataFileHelper.IndexOf(
            array, Encoding.ASCII.GetBytes("</CreationDate>"), creationDateValueEndTag
        )

        Assert.assertGreater(creationDateBeginTag, 0)
        Assert.assertGreater(creationDateValueBeginTag, 0)
        Assert.assertGreater(creationDateValueEndTag, 0)
        Assert.assertGreater(creationDateEndTag, 0)

        index: int = creationDateValueBeginTag + len("<Value>")
        while index < creationDateValueEndTag:
            array[index] = 88  # 'X'

            index += 1

    # region EphemerisStkBinaryExportTool
    def EphemerisStkBinaryExportTool(self, binary: "IVehicleEphemerisStkBinaryExportTool", isSat: bool):
        # "Satellite1.be"
        binary.coordinate_system = STK_EPHEM_COORDINATE_SYSTEM.FIXED
        Assert.assertEqual(STK_EPHEM_COORDINATE_SYSTEM.FIXED, binary.coordinate_system)
        binary.coordinate_system = STK_EPHEM_COORDINATE_SYSTEM.ICRF
        Assert.assertEqual(STK_EPHEM_COORDINATE_SYSTEM.ICRF, binary.coordinate_system)
        binary.coordinate_system = STK_EPHEM_COORDINATE_SYSTEM.INERTIAL
        Assert.assertEqual(STK_EPHEM_COORDINATE_SYSTEM.INERTIAL, binary.coordinate_system)
        binary.coordinate_system = STK_EPHEM_COORDINATE_SYSTEM.J2000
        Assert.assertEqual(STK_EPHEM_COORDINATE_SYSTEM.J2000, binary.coordinate_system)

        Assert.assertTrue(binary.use_vehicle_central_body)
        Assert.assertEqual("Earth", binary.central_body_name)
        if isSat:

            def action34():
                binary.central_body_name = "Europa"

            TryCatchAssertBlock.ExpectedException("read-only", action34)

            binary.use_vehicle_central_body = False
            Assert.assertFalse(binary.use_vehicle_central_body)

            binary.central_body_name = "Europa"
            Assert.assertEqual("Europa", binary.central_body_name)

            def action35():
                binary.central_body_name = "Uvanus"

            TryCatchAssertBlock.ExpectedException("must be in", action35)

        else:

            def action36():
                binary.central_body_name = "Europa"

            TryCatchAssertBlock.ExpectedException("read-only", action36)

        binary.include_interp = False
        Assert.assertFalse(binary.include_interp)
        binary.include_interp = True
        Assert.assertTrue(binary.include_interp)

        binary.version_format = EXPORT_TOOL_VERSION_FORMAT.CURRENT
        Assert.assertEqual(EXPORT_TOOL_VERSION_FORMAT.CURRENT, binary.version_format)

        def action37():
            binary.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT410

        TryCatchAssertBlock.DoAssert("Invalid version number", action37)

        def action38():
            binary.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT420

        TryCatchAssertBlock.DoAssert("Invalid version number", action38)

        def action39():
            binary.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT430

        TryCatchAssertBlock.DoAssert("Invalid version number", action39)

        def action40():
            binary.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT600

        TryCatchAssertBlock.DoAssert("Invalid version number", action40)

        def action41():
            binary.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT620

        TryCatchAssertBlock.DoAssert("Invalid version number", action41)

        def action42():
            binary.version_format = EXPORT_TOOL_VERSION_FORMAT.FORMAT800

        TryCatchAssertBlock.DoAssert("Invalid version number", action42)

        binary.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.USE_ENTIRE_EPHEMERIS, binary.time_period.time_period_type)
        binary.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_TIME_PERIOD.SPECIFY, binary.time_period.time_period_type)
        binary.time_period.start = (clr.Convert(self._root.current_scenario, IScenario)).start_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).start_time, binary.time_period.start)
        binary.time_period.stop = (clr.Convert(self._root.current_scenario, IScenario)).stop_time
        Assert.assertEqual((clr.Convert(self._root.current_scenario, IScenario)).stop_time, binary.time_period.stop)

        def action43():
            binary.covariance_type = STK_EPHEM_COVARIANCE_TYPE.NONE

        TryCatchAssertBlock.ExpectedException("read-only", action43)

        def action44():
            binary.covariance_type = STK_EPHEM_COVARIANCE_TYPE.POSITION3_X3

        TryCatchAssertBlock.ExpectedException("read-only", action44)

        def action45():
            binary.covariance_type = STK_EPHEM_COVARIANCE_TYPE.POSITION_VELOCITY6_X6

        TryCatchAssertBlock.ExpectedException("read-only", action45)

        binary.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.EPHEM
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.EPHEM, binary.step_size.step_size_type)
        binary.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.SPECIFY
        Assert.assertEqual(EXPORT_TOOL_STEP_SIZE.SPECIFY, binary.step_size.step_size_type)
        binary.step_size.value = 3600
        Assert.assertEqual(3600, binary.step_size.value)

        def action46():
            binary.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.NATIVE

        TryCatchAssertBlock.DoAssert("must be in", action46)

        binary.export(TestBase.GetScenarioFile("OMExternalFileStk.be"))
        if isSat:
            self._root.execute_command(
                (
                    (
                        (
                            (
                                (
                                    (
                                        (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                        + TestBase.GetScenarioFile("ConnectExternalFileStk.be")
                                    )
                                    + '" Type STKBinary CentralBody Europa CoordSys J2000 InterpBoundaries Include StepSize 3600 TimePeriod "'
                                )
                                + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                            )
                            + '" "'
                        )
                        + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                    )
                    + '"'
                )
            )

        else:
            self._root.execute_command(
                (
                    (
                        (
                            (
                                (
                                    (
                                        (("ExportDataFile " + self._oObj.path) + ' Ephemeris "')
                                        + TestBase.GetScenarioFile("ConnectExternalFileStk.be")
                                    )
                                    + '" Type STKBinary CentralBody Earth CoordSys J2000 InterpBoundaries Include StepSize 3600 TimePeriod "'
                                )
                                + str((clr.Convert(self._root.current_scenario, IScenario)).start_time)
                            )
                            + '" "'
                        )
                        + str((clr.Convert(self._root.current_scenario, IScenario)).stop_time)
                    )
                    + '"'
                )
            )

        omFileBytes = File.ReadAllBytes(TestBase.GetScenarioFile("OMExternalFileStk.be"))
        connectFileBytes = File.ReadAllBytes(TestBase.GetScenarioFile("ConnectExternalFileStk.be"))

        ExportDataFileHelper.RedactCreationDate(omFileBytes)
        ExportDataFileHelper.RedactCreationDate(connectFileBytes)

        File.WriteAllBytes(TestBase.GetScenarioFile("OMExternalFileStk_diff.be"), omFileBytes)
        File.WriteAllBytes(TestBase.GetScenarioFile("ConnectExternalFileStk_diff.be"), connectFileBytes)

        Assert.assertEqual(omFileBytes, connectFileBytes)


# endregion


# region BasicGroundEllipsesHelper
class BasicGroundEllipsesHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oCollection: "IVehicleGroundEllipsesCollection", bClearCollection: bool):
        self.m_logger.WriteLine("----- THE BASIC GROUND ELLIPSES TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        iCount: int = oCollection.count
        self.m_logger.WriteLine3("\tGroundEllipses collection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            oEllipse: "IVehicleGroundEllipseElement" = oCollection[iIndex]
            # EllipseSetName
            self.m_logger.WriteLine7("\t\tEllipse {0}: EllipseName = {1}", iIndex, oEllipse.ellipse_name)
            # EllipseData
            oDataCollection: "IVehicleEllipseDataCollection" = oEllipse.ellipse_data
            Assert.assertIsNotNone(oDataCollection)
            # Count
            self.m_logger.WriteLine3("\t\t\tData collection contains: {0} elements", oDataCollection.count)

            i: int = 0
            while i < oDataCollection.count:
                # Item
                ellipseDataElement: "IVehicleEllipseDataElement" = oDataCollection[i]
                Assert.assertIsNotNone(ellipseDataElement)
                self.m_logger.WriteLine10(
                    "\t\t\t\tElement {0}: Time = {1}, Latitude = {2}, Longitude = {3}, Bearing = {4}, SemiMajorAxis = {5}, SemiMinorAxis = {6}, CustomPosition = {7}",
                    iIndex,
                    ellipseDataElement.time,
                    ellipseDataElement.latitude,
                    ellipseDataElement.longitude,
                    ellipseDataElement.bearing,
                    ellipseDataElement.semi_major_axis,
                    ellipseDataElement.semi_minor_axis,
                    ellipseDataElement.custom_position,
                )

                i += 1

            iIndex += 1

        # Add 1
        oGEElement: "IVehicleGroundEllipseElement" = oCollection.add("Ellipse1")
        Assert.assertIsNotNone(oGEElement)
        Assert.assertEqual((iCount + 1), oCollection.count)
        self.m_logger.WriteLine7(
            "\tAfter Add({1}) the GroundEllipses collection contains: {0} elements",
            oCollection.count,
            oGEElement.ellipse_name,
        )

        def action47():
            oGEElement = oCollection.add("Ellipse1")

        TryCatchAssertBlock.DoAssert("Should not allow to add element with the same name.", action47)
        Assert.assertEqual((iCount + 1), oCollection.count)
        # Add 2
        oGEElement = oCollection.add("Ellipse2")
        Assert.assertIsNotNone(oGEElement)
        Assert.assertEqual((iCount + 2), oCollection.count)
        self.m_logger.WriteLine7(
            "\tAfter Add({1}) the GroundEllipses collection contains: {0} elements",
            oCollection.count,
            oGEElement.ellipse_name,
        )
        # _NewEnum
        groundEllipseElement: "IVehicleGroundEllipseElement"
        # _NewEnum
        for groundEllipseElement in oCollection:
            self.m_logger.WriteLine5("\t\tEllipse: EllipseName = {0}", groundEllipseElement.ellipse_name)

        # RemoveAt
        strName: str = oCollection[(oCollection.count - 1)].ellipse_name
        oCollection.remove_at((oCollection.count - 1))
        self.m_logger.WriteLine7(
            "\tAfter RemoveAt({1}) the GroundEllipses collection contains: {0} elements", oCollection.count, strName
        )
        Assert.assertEqual((iCount + 1), oCollection.count)

        def action48():
            oCollection.remove_at(oCollection.count)

        TryCatchAssertBlock.DoAssert("Should not allow to remove element by invalid index.", action48)
        # EllipseName
        oCollection[(oCollection.count - 1)].ellipse_name = "ModifiedEllipse1"
        Assert.assertEqual("ModifiedEllipse1", oCollection[(oCollection.count - 1)].ellipse_name)
        self.m_logger.WriteLine3("\tGroundEllipses collection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            oEllipse: "IVehicleGroundEllipseElement" = oCollection[iIndex]
            # EllipseSetName
            self.m_logger.WriteLine7("\t\tEllipse {0}: EllipseName = {1}", iIndex, oEllipse.ellipse_name)
            # EllipseData
            oDataCollection: "IVehicleEllipseDataCollection" = oEllipse.ellipse_data
            Assert.assertIsNotNone(oDataCollection)
            # Count
            self.m_logger.WriteLine3("\t\t\tData collection contains: {0} elements", oDataCollection.count)
            # RemoveAll
            oDataCollection.remove_all()
            Assert.assertEqual(0, oDataCollection.count)
            self.m_logger.WriteLine3(
                "\t\t\tAfter RemoveAll() Data collection contains: {0} elements", oDataCollection.count
            )
            # Add
            oDataElement: "IVehicleEllipseDataElement" = oDataCollection.add()
            Assert.assertIsNotNone(oDataElement)
            Assert.assertEqual(1, oDataCollection.count)
            self.m_logger.WriteLine3("\t\t\tAfter Add() Data collection contains: {0} elements", oDataCollection.count)
            # _NewEnum
            ellipseDataElement: "IVehicleEllipseDataElement"
            # _NewEnum
            for ellipseDataElement in oDataCollection:
                Assert.assertIsNotNone(ellipseDataElement)

            # RemoveAt
            oDataCollection.remove_at(0)
            Assert.assertEqual(0, oDataCollection.count)
            self.m_logger.WriteLine3(
                "\t\t\tAfter RemoveAt(0) Data collection contains: {0} elements", oDataCollection.count
            )
            # Add
            oDataElement = oDataCollection.add()
            Assert.assertIsNotNone(oDataElement)
            Assert.assertEqual(1, oDataCollection.count)
            self.m_logger.WriteLine3("\t\t\tAfter Add() Data collection contains: {0} elements", oDataCollection.count)

            i: int = 0
            while i < oDataCollection.count:
                # Item
                ellipseDataElement: "IVehicleEllipseDataElement" = oDataCollection[i]
                Assert.assertIsNotNone(ellipseDataElement)
                self.m_logger.WriteLine10(
                    "\t\t\t\tElement {0} (Before): Time = {1}, Latitude = {2}, Longitude = {3}, Bearing = {4}, SemiMajorAxis = {5}, SemiMinorAxis = {6}, CustomPosition = {7}",
                    i,
                    ellipseDataElement.time,
                    ellipseDataElement.latitude,
                    ellipseDataElement.longitude,
                    ellipseDataElement.bearing,
                    ellipseDataElement.semi_major_axis,
                    ellipseDataElement.semi_minor_axis,
                    ellipseDataElement.custom_position,
                )
                # Time
                oDataElement.time = "2 Jul 1999 10:00:00.000"
                oDataElement.custom_position = not oDataElement.custom_position

                def action49():
                    oDataElement.latitude = 123

                TryCatchAssertBlock.DoAssert("Should be readonly!", action49)

                def action50():
                    oDataElement.longitude = 123

                TryCatchAssertBlock.DoAssert("Should be readonly!", action50)
                oDataElement.semi_major_axis = 1234
                oDataElement.semi_minor_axis = 123

                def action51():
                    oDataElement.semi_major_axis = 12

                TryCatchAssertBlock.DoAssert("Should be more then SemiMinorAxis!", action51)

                def action52():
                    oDataElement.semi_major_axis = -12345

                TryCatchAssertBlock.DoAssert("Cannot set invalid value!", action52)

                def action53():
                    oDataElement.semi_minor_axis = 12345

                TryCatchAssertBlock.DoAssert("Should be less then SemiMajorAxis!", action53)

                def action54():
                    oDataElement.semi_minor_axis = -12345

                TryCatchAssertBlock.DoAssert("Cannot set invalid value!", action54)
                oDataElement.bearing = 123

                def action55():
                    oDataElement.bearing = 12345

                TryCatchAssertBlock.DoAssert("Cannot set invalid value!", action55)
                self.m_logger.WriteLine10(
                    "\t\t\t\tElement {0} (After):  Time = {1}, Latitude = {2}, Longitude = {3}, Bearing = {4}, SemiMajorAxis = {5}, SemiMinorAxis = {6}, CustomPosition = {7}",
                    i,
                    ellipseDataElement.time,
                    ellipseDataElement.latitude,
                    ellipseDataElement.longitude,
                    ellipseDataElement.bearing,
                    ellipseDataElement.semi_major_axis,
                    ellipseDataElement.semi_minor_axis,
                    ellipseDataElement.custom_position,
                )

                i += 1

            iIndex += 1

        # Add 3
        iCount = oCollection.count
        oGEElement = oCollection.add("Ellipse3")
        Assert.assertIsNotNone(oGEElement)
        Assert.assertEqual((iCount + 1), oCollection.count)
        # GetEllipseSet
        oGEElement = oCollection.get_ellipse_set("Ellipse3")
        Assert.assertIsNotNone(oGEElement)

        def action56():
            oCollection.get_ellipse_set("")

        TryCatchAssertBlock.DoAssert("Should throw an exception in case of empty string!", action56)

        def action57():
            oCollection.get_ellipse_set(None)

        TryCatchAssertBlock.DoAssert("Should throw an exception in case of NULL pointer!", action57)

        def action58():
            oCollection.remove_ellipse_set("")

        # RemoveEllipseSet
        TryCatchAssertBlock.DoAssert("Should throw an exception in case of empty string!", action58)

        def action59():
            oCollection.remove_ellipse_set(None)

        TryCatchAssertBlock.DoAssert("Should throw an exception in case of NULL pointer!", action59)
        oCollection.remove_ellipse_set(oGEElement.ellipse_name)  # oGEElement is now invalid
        Assert.assertEqual(iCount, oCollection.count)

        def action60():
            oCollection.remove_ellipse_set("InvalidName")

        TryCatchAssertBlock.DoAssert("Should throw an exception in case of invalid name!", action60)
        if bClearCollection:
            oCollection.remove_all()
            Assert.assertEqual(0, oCollection.count)

        self.m_logger.WriteLine("----- THE BASIC GROUND ELLIPSES TEST ----- END -----")


# endregion


# region BasicPropagatorHelper
class BasicPropagatorHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oApplication.unit_preferences
        self.m_oUnits.reset_units()

    # endregion

    # region Run method
    def Run(
        self, obj: "IStkObject", oPropagator: "IVehiclePropagator", eType: "VEHICLE_PROPAGATOR_TYPE", EarthGravModel
    ):
        self.m_logger.WriteLine6("----- THE BASIC PROPAGATOR TEST ({0})----- BEGIN -----", eType)
        Assert.assertIsNotNone(oPropagator)
        if eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC:
            oHelper = PropagatorGreatArcHelper(obj, self.m_oUnits)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorGreatArc))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_STK_EXTERNAL:
            oHelper = PropagatorStkExternalHelper(self.m_oUnits)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorStkExternal))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT:
            oHelper = PropagatorSimpleAscentHelper(obj, self.m_oUnits)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorSimpleAscent))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY:
            oHelper = PropagatorTwoBodyHelper(self.m_oApplication)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorTwoBody))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_LOP:
            oHelper = PropagatorLOPHelper(self.m_oApplication)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorLOP))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION:
            oHelper = PropagatorJ2PerturbationHelper(self.m_oApplication)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorJ2Perturbation))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION:
            oHelper = PropagatorJ4PerturbationHelper(self.m_oApplication)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorJ4Perturbation))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4:
            oHelper = PropagatorSGP4Helper(self.m_oApplication)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorSGP4))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SPICE:
            oHelper = PropagatorSPICEHelper(self.m_oApplication)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorSPICE))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_USER_EXTERNAL:
            oHelper = PropagatorUserExternalHelper(self.m_oApplication)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorUserExternal))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP:
            oHelper = PropagatorHPOPHelper(self.m_oApplication, obj, EarthGravModel)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorHPOP), False)
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_BALLISTIC:
            oHelper = PropagatorBallisticHelper(obj, self.m_oUnits)
            oHelper.Run(clr.Convert(oPropagator, IVehiclePropagatorBallistic))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR:
            pass
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME:
            helper = PropagatorRealtimeHelper()
            helper.Run(obj, clr.CastAs(oPropagator, IVehiclePropagatorRealtime))
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GPS:
            helper = PropagatorGPSHelper(TestBase.GetSTKDBDir())
            helper.Run(obj, clr.CastAs(oPropagator, IVehiclePropagatorGPS))

        elif ((eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR11_PARAM)) or (
            (eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SP3)
        ):
            pass
        elif eType == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_AVIATOR:
            pass
        else:
            Assert.fail("Invalid propagator type: {0}", eType)
        self.m_logger.WriteLine6("----- THE BASIC PROPAGATOR TEST ({0})----- END -----", eType)


# endregion


# region PropagatorStkExternalHelper
class PropagatorStkExternalHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        oUnits.reset_units()

    # endregion

    # region Run method
    def Run(self, oStkExternal: "IVehiclePropagatorStkExternal"):
        self.m_logger.WriteLine("----- STK EXTERNAL PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oStkExternal)
        # StartTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oStkExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oStkExternal.stop_time)
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oStkExternal.step)
        # Override (false)
        self.m_logger.WriteLine4("\tThe current Override is: {0}", oStkExternal.override)
        oStkExternal.override = False
        self.m_logger.WriteLine4("\tThe new Override is: {0}", oStkExternal.override)
        Assert.assertEqual(False, oStkExternal.override)
        # Override (false)
        oStkExternal.override = True
        self.m_logger.WriteLine4("\tThe new Override is: {0}", oStkExternal.override)
        Assert.assertEqual(True, oStkExternal.override)
        # EphemStart
        self.m_logger.WriteLine6("\tThe current EphemStart is: {0}", oStkExternal.ephemeris_start_epoch.time_instant)
        oStkExternal.ephemeris_start_epoch.set_explicit_time("2 Jul 1999 17:00:00.000")
        self.m_logger.WriteLine6("\tThe new EphemStart is: {0}", oStkExternal.ephemeris_start_epoch.time_instant)
        Assert.assertEqual("2 Jul 1999 17:00:00.000", oStkExternal.ephemeris_start_epoch.time_instant)

        # FileFormat / Filename
        oStkExternal.file_format = STK_EXTERNAL_EPHEMERIS_FORMAT.CCSDS
        Assert.assertEqual(STK_EXTERNAL_EPHEMERIS_FORMAT.CCSDS, oStkExternal.file_format)
        externalFile: str = TestBase.GetScenarioFile("External", "Satellite1.oem")
        oStkExternal.filename = externalFile
        Assert.assertEqual(TestBase.PathCombine("External", "Satellite1.oem"), oStkExternal.filename)

        oStkExternal.file_format = STK_EXTERNAL_EPHEMERIS_FORMAT.ITC
        Assert.assertEqual(STK_EXTERNAL_EPHEMERIS_FORMAT.ITC, oStkExternal.file_format)
        externalFile = TestBase.GetScenarioFile("External", "Satellite1.bsp")
        oStkExternal.filename = externalFile
        Assert.assertEqual(TestBase.PathCombine("External", "Satellite1.bsp"), oStkExternal.filename)

        oStkExternal.file_format = STK_EXTERNAL_EPHEMERIS_FORMAT.STK
        Assert.assertEqual(STK_EXTERNAL_EPHEMERIS_FORMAT.STK, oStkExternal.file_format)
        externalFile = TestBase.GetScenarioFile("External", "Satellite1.e")
        oStkExternal.filename = externalFile
        Assert.assertEqual(TestBase.PathCombine("External", "Satellite1.e"), oStkExternal.filename)

        oStkExternal.file_format = STK_EXTERNAL_EPHEMERIS_FORMAT.STK_BINARY
        Assert.assertEqual(STK_EXTERNAL_EPHEMERIS_FORMAT.STK_BINARY, oStkExternal.file_format)
        externalFile = TestBase.GetScenarioFile("External", "Satellite1.be")
        oStkExternal.filename = externalFile
        Assert.assertEqual(TestBase.PathCombine("External", "Satellite1.be"), oStkExternal.filename)

        oStkExternal.file_format = STK_EXTERNAL_EPHEMERIS_FORMAT.CODE500
        Assert.assertEqual(STK_EXTERNAL_EPHEMERIS_FORMAT.CODE500, oStkExternal.file_format)
        externalFile = TestBase.GetScenarioFile("External", "Satellite1.EPH")
        oStkExternal.filename = externalFile
        Assert.assertEqual(TestBase.PathCombine("External", "Satellite1.EPH"), oStkExternal.filename)

        def action61():
            oStkExternal.file_format = STK_EXTERNAL_EPHEMERIS_FORMAT.UNKNOWN

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action61)

        def action62():
            oStkExternal.filename = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action62)

        def action63():
            oStkExternal.filename = "IllegalFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action63)

        # LimitEphemerisToScenarioInterval (false)
        self.m_logger.WriteLine4(
            "\tThe current LimitEphemerisToScenarioInterval is: {0}", oStkExternal.limit_ephemeris_to_scenario_interval
        )
        oStkExternal.limit_ephemeris_to_scenario_interval = False
        self.m_logger.WriteLine4(
            "\tThe new LimitEphemerisToScenarioInterval is: {0}", oStkExternal.limit_ephemeris_to_scenario_interval
        )
        Assert.assertEqual(False, oStkExternal.limit_ephemeris_to_scenario_interval)
        # LimitEphemerisToScenarioInterval (true)
        oStkExternal.limit_ephemeris_to_scenario_interval = True
        self.m_logger.WriteLine4(
            "\tThe new LimitEphemerisToScenarioInterval is: {0}", oStkExternal.limit_ephemeris_to_scenario_interval
        )
        Assert.assertEqual(True, oStkExternal.limit_ephemeris_to_scenario_interval)

        # Propagate
        oStkExternal.propagate()
        self.m_logger.WriteLine("----- STK EXTERNAL PROPAGATOR TEST ----- END -----")


# endregion


# region PropagatorTwoBodyHelper
class PropagatorTwoBodyHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        oApplication.unit_preferences.reset_units()

    # endregion

    # region Run method
    def Run(self, oTwoBody: "IVehiclePropagatorTwoBody"):
        self.m_logger.WriteLine("----- TWO BODY PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oTwoBody)
        # StartTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oTwoBody.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oTwoBody.ephemeris_interval.find_stop_time())
        oTwoBody.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "19 Jan 2003 02:46:24.680")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oTwoBody.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oTwoBody.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oTwoBody.ephemeris_interval.find_stop_time())
        Assert.assertEqual("19 Jan 2003 02:46:24.680", oTwoBody.ephemeris_interval.find_stop_time())
        oTwoBody.ephemeris_interval.set_explicit_interval(
            oTwoBody.ephemeris_interval.find_start_time(), "19 Jan 2003 01:46:24.680"
        )
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oTwoBody.ephemeris_interval.find_stop_time())
        Assert.assertEqual("19 Jan 2003 01:46:24.680", oTwoBody.ephemeris_interval.find_stop_time())
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oTwoBody.step)
        oTwoBody.step = 12
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oTwoBody.step)
        Assert.assertEqual(12, oTwoBody.step)

        # InitialState
        oInitState: "IVehicleInitialState" = oTwoBody.initial_state
        Assert.assertIsNotNone(oInitState)
        # Epoch was  deprecated
        # m_logger.WriteLine("\tThe current Epoch is:  {0}", oInitState.Epoch);
        # oInitState.Epoch = "18 Jan 2003 01:23:45.678";
        # m_logger.WriteLine("\tThe new Epoch is:  {0}", oInitState.Epoch);
        # Assert.AreEqual("18 Jan 2003 01:23:45.678", oInitState.Epoch);
        cart: "IOrbitStateCartesian" = clr.Convert(
            oInitState.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN), IOrbitStateCartesian
        )
        (clr.Convert(cart, IOrbitState)).epoch = "18 Jan 2003 01:23:45.678"
        self.m_logger.WriteLine6("\tThe new Epoch is:  {0}", cart.epoch)
        Assert.assertEqual("18 Jan 2003 01:23:45.678", cart.epoch)
        oInitState.representation.assign(cart)
        # Propagate
        oTwoBody.propagate()
        # Representation
        oHelper = OrbitStateHelper(self.m_oApplication)
        oHelper.Run(oInitState.representation)
        # Propagate
        oTwoBody.propagate()

        # Verify "Use Scenario Analysis Time" to make sure it works as expected
        # By setting UseScenarioAnalysisTime the propagator's
        # start/stop times are overriden with the scenario's start/stop times.
        sc: "IScenario" = clr.Convert(self.m_oApplication.current_scenario, IScenario)
        oTwoBody.ephemeris_interval.set_explicit_interval("1 Jul 2005 12:00:00.000", "2 Jul 2005 12:00:00.000")
        Assert.assertEqual("1 Jul 2005 12:00:00.000", oTwoBody.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2005 12:00:00.000", oTwoBody.ephemeris_interval.find_stop_time())

        Assert.assertNotEqual(sc.start_time, oTwoBody.ephemeris_interval.find_start_time())
        Assert.assertNotEqual(sc.stop_time, oTwoBody.ephemeris_interval.find_stop_time())

        oTwoBody.propagate()

        Assert.assertEqual("1 Jul 2005 12:00:00.000", oTwoBody.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2005 12:00:00.000", oTwoBody.ephemeris_interval.find_stop_time())

        oTwoBody.ephemeris_interval.set_implicit_interval(
            (clr.Convert(sc, IStkObject)).vgt.event_intervals["AnalysisInterval"]
        )
        oTwoBody.propagate()

        Assert.assertEqual(sc.start_time, oTwoBody.ephemeris_interval.find_start_time())
        Assert.assertEqual(sc.stop_time, oTwoBody.ephemeris_interval.find_stop_time())

        self.m_logger.WriteLine("----- TWO BODY PROPAGATOR TEST ----- END -----")


# endregion


# region PropagatorLOPHelper
class PropagatorLOPHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        oApplication.unit_preferences.reset_units()

    # endregion

    # region Run method
    def Run(self, oLOP: "IVehiclePropagatorLOP"):
        self.m_logger.WriteLine("----- LOP PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oLOP)
        # StartTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oLOP.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oLOP.ephemeris_interval.find_stop_time())
        oLOP.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "18 Jan 2003 02:46:24.680")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oLOP.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oLOP.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oLOP.ephemeris_interval.find_stop_time())
        Assert.assertEqual("18 Jan 2003 02:46:24.680", oLOP.ephemeris_interval.find_stop_time())
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oLOP.step)
        oLOP.step = 87000
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oLOP.step)
        Assert.assertEqual(87000, oLOP.step)

        def action64():
            oLOP.step = 1200000000000.0

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action64)
        # InitialState
        oInitState: "IVehicleInitialState" = oLOP.initial_state
        Assert.assertIsNotNone(oInitState)
        # Epoch was deprecated
        #            m_logger.WriteLine("\tThe current Epoch is:  {0}", oInitState.Epoch);
        # oInitState.Epoch = "18 Jan 2003 01:23:45.678";
        # m_logger.WriteLine("\tThe new Epoch is:  {0}", oInitState.Epoch);
        # Assert.AreEqual("18 Jan 2003 01:23:45.678", oInitState.Epoch);
        cart: "IOrbitStateCartesian" = clr.Convert(
            oInitState.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN), IOrbitStateCartesian
        )
        (clr.Convert(cart, IOrbitState)).epoch = "18 Jan 2003 01:23:45.678"
        Assert.assertEqual("18 Jan 2003 01:23:45.678", cart.epoch)
        oInitState.representation.assign(cart)
        # Propagate
        # CHANGE: Propagation step must not exceed the propagation
        # interval, otherwise the propagation will fail.
        oLOP.step = 86400
        oLOP.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "19 Jan 2003 01:23:45.678")
        oLOP.propagate()
        # Representation
        oHelper = OrbitStateHelper(self.m_oApplication)
        oHelper.Run(oInitState.representation)
        # Propagate
        oLOP.propagate()
        # ForceModel
        oForceModel: "IVehicleLOPForceModel" = oLOP.force_model
        Assert.assertIsNotNone(oForceModel)
        # CentralBodyGravity
        self.CentralBodyGravityTest(oForceModel.central_body_gravity)
        # ThirdBodyGravity
        self.ThirdBodyGravityTest(oForceModel.third_body_gravity)
        # Drag
        self.DragTest(oForceModel.drag)
        # SolarRadiationPressure
        self.SolarRadiationPressureTest(oForceModel.solar_radiation_pressure)
        # PhysicalData
        self.PhysicalDataTest(oForceModel.physical_data)
        self.m_logger.WriteLine("----- LOP PROPAGATOR TEST ----- END -----")

    # endregion

    # region CentralBodyGravityTest
    def CentralBodyGravityTest(self, oGravity: "IVehicleLOPCentralBodyGravity"):
        Assert.assertIsNotNone(oGravity)
        # MaxDegree
        self.m_logger.WriteLine3("\tThe current MaxDegree is:  {0}", oGravity.max_degree)
        oGravity.max_degree = 25
        self.m_logger.WriteLine3("\tThe new MaxDegree is:  {0}", oGravity.max_degree)
        Assert.assertEqual(25, oGravity.max_degree)

        def action65():
            oGravity.max_degree = 12345

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action65)
        # MaxOrder
        self.m_logger.WriteLine3("\tThe current MaxOrder is:  {0}", oGravity.max_order)
        oGravity.max_order = 22
        self.m_logger.WriteLine3("\tThe new MaxOrder is:  {0}", oGravity.max_order)
        Assert.assertEqual(22, oGravity.max_order)

        def action66():
            oGravity.max_order = 12345

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action66)

    # endregion

    # region ThirdBodyGravityTest
    def ThirdBodyGravityTest(self, oGravity: "IVehicleThirdBodyGravity"):
        Assert.assertIsNotNone(oGravity)
        # UseSolarGravity
        self.m_logger.WriteLine4("\tThe current UseSolarGravity is:  {0}", oGravity.use_solar_gravity)
        oGravity.use_solar_gravity = False
        self.m_logger.WriteLine4("\tThe new UseSolarGravity is:  {0}", oGravity.use_solar_gravity)
        Assert.assertEqual(False, oGravity.use_solar_gravity)
        oGravity.use_solar_gravity = True
        self.m_logger.WriteLine4("\tThe new UseSolarGravity is:  {0}", oGravity.use_solar_gravity)
        Assert.assertEqual(True, oGravity.use_solar_gravity)
        # UseLunarGravity
        self.m_logger.WriteLine4("\tThe current UseLunarGravity is:  {0}", oGravity.use_lunar_gravity)
        oGravity.use_lunar_gravity = False
        self.m_logger.WriteLine4("\tThe new UseLunarGravity is:  {0}", oGravity.use_lunar_gravity)
        Assert.assertEqual(False, oGravity.use_lunar_gravity)
        oGravity.use_lunar_gravity = True
        self.m_logger.WriteLine4("\tThe new UseLunarGravity is:  {0}", oGravity.use_lunar_gravity)
        Assert.assertEqual(True, oGravity.use_lunar_gravity)

    # endregion

    # region DragTest
    def DragTest(self, oDrag: "IVehicleLOPForceModelDrag"):
        Assert.assertIsNotNone(oDrag)
        # Use (false)
        self.m_logger.WriteLine4("\tThe current Use is:  {0}", oDrag.use)
        oDrag.use = False
        self.m_logger.WriteLine4("\tThe new Use is:  {0}", oDrag.use)
        Assert.assertEqual(False, oDrag.use)

        def action67():
            oDrag.cd = 4.321

        # Cd (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action67)
        # Advanced (readonly)
        self.ForceModelAdvancedTest(oDrag.advanced, True)
        # Use (true)
        self.m_logger.WriteLine4("\tThe current Use is:  {0}", oDrag.use)
        oDrag.use = True
        self.m_logger.WriteLine4("\tThe new Use is:  {0}", oDrag.use)
        Assert.assertEqual(True, oDrag.use)
        # Cd
        self.m_logger.WriteLine6("\tThe current Cd is:  {0}", oDrag.cd)
        oDrag.cd = 4.321
        self.m_logger.WriteLine6("\tThe new Cd is:  {0}", oDrag.cd)
        Assert.assertEqual(4.321, oDrag.cd)

        def action68():
            oDrag.cd = 43.21

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action68)
        # Advanced
        self.ForceModelAdvancedTest(oDrag.advanced, False)

    # endregion

    # region ForceModelAdvancedTest
    def ForceModelAdvancedTest(self, oAdvanved: "IVehicleAdvanced", bIsReadOnly: bool):
        Assert.assertIsNotNone(oAdvanved)
        if bIsReadOnly:

            def action69():
                oAdvanved.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.STANDARD_ATMOS_MODEL_1976

            # AtmosphericDensityModel
            TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action69)

            def action70():
                oAdvanved.use_osculating_altitude = True

            # UseOsculatingAlt
            TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action70)

            def action71():
                oAdvanved.max_drag_altitude = 43.21

            # MaxDragAlt
            TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action71)

            def action72():
                oAdvanved.density_weighing_factor = 43.21

            # DensityWeighingFactor
            TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action72)
            # ExpDensModelParams
            self.ExponentialModelParamsTest(oAdvanved.exp_dens_model_params, True)

        else:
            # AtmosphericDensityModel (e1976StandardAtmosModel)
            self.m_logger.WriteLine6(
                "\tThe current AtmosphericDensityModel is:  {0}", oAdvanved.atmospheric_density_model
            )
            oAdvanved.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.STANDARD_ATMOS_MODEL_1976
            self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is:  {0}", oAdvanved.atmospheric_density_model)
            Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.STANDARD_ATMOS_MODEL_1976, oAdvanved.atmospheric_density_model)

            def action73():
                oAdvanved.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.HARRIS_PRIESTER

            TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action73)

            # AtmosDensityModel (e1976StandardAtmosModel)
            self.m_logger.WriteLine6("\tThe current AtmosphericDensityModel is:  {0}", oAdvanved.atmos_density_model)
            oAdvanved.atmos_density_model = LOP_ATMOSPHERIC_DENSITY_MODEL.LOP1976_STANDARD_ATMOS_MODEL
            self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is:  {0}", oAdvanved.atmos_density_model)
            Assert.assertEqual(
                LOP_ATMOSPHERIC_DENSITY_MODEL.LOP1976_STANDARD_ATMOS_MODEL, oAdvanved.atmos_density_model
            )

            # UseOsculatingAlt
            self.m_logger.WriteLine4("\tThe current UseOsculatingAlt is:  {0}", oAdvanved.use_osculating_altitude)
            oAdvanved.use_osculating_altitude = False
            self.m_logger.WriteLine4("\tThe new UseOsculatingAlt is:  {0}", oAdvanved.use_osculating_altitude)
            Assert.assertEqual(False, oAdvanved.use_osculating_altitude)
            oAdvanved.use_osculating_altitude = True
            self.m_logger.WriteLine4("\tThe new UseOsculatingAlt is:  {0}", oAdvanved.use_osculating_altitude)
            Assert.assertEqual(True, oAdvanved.use_osculating_altitude)
            # MaxDragAlt
            self.m_logger.WriteLine6("\tThe current MaxDragAlt is:  {0}", oAdvanved.max_drag_altitude)
            oAdvanved.max_drag_altitude = 43.21
            self.m_logger.WriteLine6("\tThe new MaxDragAlt is:  {0}", oAdvanved.max_drag_altitude)
            Assert.assertEqual(43.21, oAdvanved.max_drag_altitude)

            def action74():
                oAdvanved.max_drag_altitude = -43.21

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action74)
            # DensityWeighingFactor
            self.m_logger.WriteLine6("\tThe current DensityWeighingFactor is:  {0}", oAdvanved.density_weighing_factor)
            oAdvanved.density_weighing_factor = 43.21
            self.m_logger.WriteLine6("\tThe new DensityWeighingFactor is:  {0}", oAdvanved.density_weighing_factor)
            Assert.assertEqual(43.21, oAdvanved.density_weighing_factor)

            def action75():
                oAdvanved.density_weighing_factor = -43.21

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action75)
            # AtmosphericDensityModel (eExponentialModel)
            oAdvanved.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.EXPONENTIAL_MODEL
            self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is:  {0}", oAdvanved.atmospheric_density_model)
            Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.EXPONENTIAL_MODEL, oAdvanved.atmospheric_density_model)
            # AtmosDensityModel (eExponentialModel)
            oAdvanved.atmos_density_model = LOP_ATMOSPHERIC_DENSITY_MODEL.EXPONENTIAL_MODEL
            self.m_logger.WriteLine6("\tThe new AtmosDensityModel is:  {0}", oAdvanved.atmos_density_model)
            Assert.assertEqual(LOP_ATMOSPHERIC_DENSITY_MODEL.EXPONENTIAL_MODEL, oAdvanved.atmos_density_model)
            # ExpDensModelParams
            self.ExponentialModelParamsTest(oAdvanved.exp_dens_model_params, False)

    # endregion

    # region ExponentialModelParamsTest
    def ExponentialModelParamsTest(self, oParams: "IVehicleExpDensModelParams", bIsReadOnly: bool):
        Assert.assertIsNotNone(oParams)
        if bIsReadOnly:

            def action76():
                oParams.reference_density = 43.21

            # ReferenceDensity
            TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action76)

            def action77():
                oParams.reference_height = 43.21

            # ReferenceHeight
            TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action77)

            def action78():
                oParams.scale_height = 43.21

            # ScaleHeight
            TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action78)

        else:
            # ReferenceDensity
            self.m_logger.WriteLine6("\tThe current ReferenceDensity is:  {0}", oParams.reference_density)
            oParams.reference_density = 43.21
            self.m_logger.WriteLine6("\tThe new ReferenceDensity is:  {0}", oParams.reference_density)
            Assert.assertEqual(43.21, oParams.reference_density)

            def action79():
                oParams.reference_density = -43.21

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action79)
            # ReferenceHeight
            self.m_logger.WriteLine6("\tThe current ReferenceHeight is:  {0}", oParams.reference_height)
            oParams.reference_height = 43.21
            self.m_logger.WriteLine6("\tThe new ReferenceHeight is:  {0}", oParams.reference_height)
            Assert.assertEqual(43.21, oParams.reference_height)

            def action80():
                oParams.reference_height = -43.21

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action80)
            # ScaleHeight
            self.m_logger.WriteLine6("\tThe current ScaleHeight is:  {0}", oParams.scale_height)
            oParams.scale_height = 43.21
            self.m_logger.WriteLine6("\tThe new ScaleHeight is:  {0}", oParams.scale_height)
            Assert.assertEqual(43.21, oParams.scale_height)

            def action81():
                oParams.scale_height = -43.21

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action81)

    # endregion

    # region SolarRadiationPressureTest
    def SolarRadiationPressureTest(self, oPressure: "IVehicleLOPSolarRadiationPressure"):
        Assert.assertIsNotNone(oPressure)
        # Use (false)
        self.m_logger.WriteLine4("\tThe current Use is:  {0}", oPressure.use)
        oPressure.use = False
        self.m_logger.WriteLine4("\tThe new Use is:  {0}", oPressure.use)
        Assert.assertEqual(False, oPressure.use)

        def action82():
            oPressure.cp = 43.21

        # Cp (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action82)

        def action83():
            oPressure.atmos_height = 432.1

        # AtmosHeight (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action83)
        # Use (true)
        self.m_logger.WriteLine4("\tThe current Use is:  {0}", oPressure.use)
        oPressure.use = True
        self.m_logger.WriteLine4("\tThe new Use is:  {0}", oPressure.use)
        Assert.assertEqual(True, oPressure.use)
        # Cp
        self.m_logger.WriteLine6("\tThe current Cp is:  {0}", oPressure.cp)
        oPressure.cp = 43.21
        self.m_logger.WriteLine6("\tThe new Cp is:  {0}", oPressure.cp)
        Assert.assertEqual(43.21, oPressure.cp)

        def action84():
            oPressure.cp = 432.1

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action84)
        # AtmosHeight
        self.m_logger.WriteLine6("\tThe current AtmosHeight is:  {0}", oPressure.atmos_height)
        oPressure.atmos_height = 432.1
        self.m_logger.WriteLine6("\tThe new AtmosHeight is:  {0}", oPressure.atmos_height)
        Assert.assertEqual(432.1, oPressure.atmos_height)

        def action85():
            oPressure.atmos_height = -432.1

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action85)

    # endregion

    # region PhysicalDataTest
    def PhysicalDataTest(self, physicalData: "IVehiclePhysicalData"):
        Assert.assertIsNotNone(physicalData)
        # DragCrossSectionalArea
        self.m_logger.WriteLine6(
            "\tThe current DragCrossSectionalArea is:  {0}", physicalData.drag_cross_sectional_area
        )
        physicalData.drag_cross_sectional_area = 0.0004321
        self.m_logger.WriteLine6("\tThe new DragCrossSectionalArea is:  {0}", physicalData.drag_cross_sectional_area)
        Assert.assertEqual(0.0004321, physicalData.drag_cross_sectional_area)

        def action86():
            physicalData.drag_cross_sectional_area = -43.21

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action86)
        # SRPCrossSectionalArea
        self.m_logger.WriteLine6("\tThe current SRPCrossSectionalArea is:  {0}", physicalData.srp_cross_sectional_area)
        physicalData.srp_cross_sectional_area = 4.321e-07
        self.m_logger.WriteLine6("\tThe new SRPCrossSectionalArea is:  {0}", physicalData.srp_cross_sectional_area)
        Assert.assertAlmostEqual(4.321e-07, physicalData.srp_cross_sectional_area, delta=1e-09)

        def action87():
            physicalData.srp_cross_sectional_area = -432.1

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action87)
        # SatelliteMass
        self.m_logger.WriteLine6("\tThe current SatelliteMass is:  {0}", physicalData.satellite_mass)
        physicalData.satellite_mass = 432.1
        self.m_logger.WriteLine6("\tThe new SatelliteMass is:  {0}", physicalData.satellite_mass)
        Assert.assertEqual(432.1, physicalData.satellite_mass)

        def action88():
            physicalData.satellite_mass = -432.1

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action88)


# endregion


# region PropagatorJ2PerturbationHelper
class PropagatorJ2PerturbationHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        oApplication.unit_preferences.reset_units()

    # endregion

    # region Run method
    def Run(self, oJ2: "IVehiclePropagatorJ2Perturbation"):
        cart: "IOrbitStateCartesian" = None
        self.m_logger.WriteLine("----- J2 PERTURBATION PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oJ2)
        # EphemerisInterval
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oJ2.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oJ2.ephemeris_interval.find_stop_time())
        oJ2.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "19 Jan 2003 02:46:24.680")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oJ2.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oJ2.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oJ2.ephemeris_interval.find_stop_time())
        Assert.assertEqual("19 Jan 2003 02:46:24.680", oJ2.ephemeris_interval.find_stop_time())
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oJ2.step)
        oJ2.step = 12
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oJ2.step)
        Assert.assertEqual(12, oJ2.step)
        # CHANGE: Step can now be any number up to AgCHuge. The previous
        # limit 1200.0 sec has been removed
        oJ2.step = 12345
        Assert.assertEqual(12345, oJ2.step)
        # InitialState
        oInitState: "IVehicleJxInitialState" = oJ2.initial_state
        Assert.assertIsNotNone(oInitState)
        # Epoch is deprecated
        # m_logger.WriteLine("\tThe current Epoch is:  {0}", oInitState.Epoch);
        # oInitState.Epoch = "18 Jan 2003 01:23:45.678";
        # m_logger.WriteLine("\tThe new Epoch is:  {0}", oInitState.Epoch);
        # Assert.AreEqual("18 Jan 2003 01:23:45.678", oInitState.Epoch);
        cart = clr.Convert(oInitState.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN), IOrbitStateCartesian)
        (clr.Convert(cart, IOrbitState)).epoch = "18 Jan 2003 01:23:45.678"
        Assert.assertEqual("18 Jan 2003 01:23:45.678", cart.epoch)

        # EllipseOptions (eOsculating)
        self.m_logger.WriteLine6("\tThe current EllipseOptions is:  {0}", oInitState.ellipse_options)
        oInitState.ellipse_options = VEHICLE_ELLIPSE_OPTIONS.OSCULATING
        self.m_logger.WriteLine6("\tThe new EllipseOptions is:  {0}", oInitState.ellipse_options)
        Assert.assertEqual(VEHICLE_ELLIPSE_OPTIONS.OSCULATING, oInitState.ellipse_options)
        # EllipseOptions (eSecularlyPrecessing)
        oInitState.ellipse_options = VEHICLE_ELLIPSE_OPTIONS.SECULARLY_PRECESSING
        self.m_logger.WriteLine6("\tThe new EllipseOptions is:  {0}", oInitState.ellipse_options)
        Assert.assertEqual(VEHICLE_ELLIPSE_OPTIONS.SECULARLY_PRECESSING, oInitState.ellipse_options)
        # Propagate
        oJ2.propagate()
        # Representation
        oHelper = OrbitStateHelper(self.m_oApplication)
        oHelper.Run(oInitState.representation)
        # Propagate
        oJ2.propagate()

        # Verify "Use Scenario Analysis Time" to make sure it works as expected
        # By setting UseScenarioAnalysisTime the propagator's
        # start/stop times are overriden with the scenario's start/stop times.
        sc: "IScenario" = clr.Convert(self.m_oApplication.current_scenario, IScenario)
        oJ2.ephemeris_interval.set_explicit_interval("1 Jul 2005 12:00:00.000", "2 Jul 2005 12:00:00.000")
        Assert.assertEqual("1 Jul 2005 12:00:00.000", oJ2.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2005 12:00:00.000", oJ2.ephemeris_interval.find_stop_time())

        Assert.assertNotEqual(sc.start_time, oJ2.ephemeris_interval.find_start_time())
        Assert.assertNotEqual(sc.stop_time, oJ2.ephemeris_interval.find_stop_time())

        oJ2.propagate()

        Assert.assertEqual("1 Jul 2005 12:00:00.000", oJ2.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2005 12:00:00.000", oJ2.ephemeris_interval.find_stop_time())

        oJ2.ephemeris_interval.set_implicit_interval(
            self.m_oApplication.current_scenario.vgt.event_intervals["AnalysisInterval"]
        )
        oJ2.propagate()

        Assert.assertEqual(sc.start_time, oJ2.ephemeris_interval.find_start_time())
        Assert.assertEqual(sc.stop_time, oJ2.ephemeris_interval.find_stop_time())

        self.m_logger.WriteLine("----- J2 PERTURBATION PROPAGATOR TEST ----- END -----")


# endregion


# region PropagatorJ4PerturbationHelper
class PropagatorJ4PerturbationHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        oApplication.unit_preferences.reset_units()

    # endregion

    # region Run method
    def Run(self, oJ4: "IVehiclePropagatorJ4Perturbation"):
        cart: "IOrbitStateCartesian" = None
        self.m_logger.WriteLine("----- J4 PERTURBATION PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oJ4)
        # EphemerisInterval
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oJ4.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oJ4.ephemeris_interval.find_stop_time())
        oJ4.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "19 Jan 2003 02:46:24.680")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oJ4.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oJ4.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oJ4.ephemeris_interval.find_stop_time())
        Assert.assertEqual("19 Jan 2003 02:46:24.680", oJ4.ephemeris_interval.find_stop_time())
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oJ4.step)
        oJ4.step = 12
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oJ4.step)
        Assert.assertEqual(12, oJ4.step)
        # CHANGE: the step can now be any number up to AgCHuge.
        # The previous limitation of max of 1200.0 has been removed.
        oJ4.step = 12345
        Assert.assertEqual(12345, oJ4.step)
        # InitialState
        oInitState: "IVehicleJxInitialState" = oJ4.initial_state
        Assert.assertIsNotNone(oInitState)
        # Epoch is deprecated
        # m_logger.WriteLine("\tThe current Epoch is:  {0}", oInitState.Epoch);
        # oInitState.Epoch = "18 Jan 2003 01:23:45.678";
        # m_logger.WriteLine("\tThe new Epoch is:  {0}", oInitState.Epoch);
        # Assert.AreEqual("18 Jan 2003 01:23:45.678", oInitState.Epoch);
        cart = clr.Convert(oInitState.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN), IOrbitStateCartesian)
        (clr.Convert(cart, IOrbitState)).epoch = "18 Jan 2003 01:23:45.678"
        Assert.assertEqual("18 Jan 2003 01:23:45.678", cart.epoch)
        oInitState.representation.assign(cart)
        # EllipseOptions (eOsculating)
        self.m_logger.WriteLine6("\tThe current EllipseOptions is:  {0}", oInitState.ellipse_options)
        oInitState.ellipse_options = VEHICLE_ELLIPSE_OPTIONS.OSCULATING
        self.m_logger.WriteLine6("\tThe new EllipseOptions is:  {0}", oInitState.ellipse_options)
        Assert.assertEqual(VEHICLE_ELLIPSE_OPTIONS.OSCULATING, oInitState.ellipse_options)
        # EllipseOptions (eSecularlyPrecessing)
        oInitState.ellipse_options = VEHICLE_ELLIPSE_OPTIONS.SECULARLY_PRECESSING
        self.m_logger.WriteLine6("\tThe new EllipseOptions is:  {0}", oInitState.ellipse_options)
        Assert.assertEqual(VEHICLE_ELLIPSE_OPTIONS.SECULARLY_PRECESSING, oInitState.ellipse_options)
        # Propagate
        oJ4.propagate()
        # Representation
        oHelper = OrbitStateHelper(self.m_oApplication)
        oHelper.Run(oInitState.representation)
        # Propagate
        oJ4.propagate()

        # Verify "Use Scenario Analysis Time" to make sure it works as expected
        # By setting UseScenarioAnalysisTime the propagator's
        # start/stop times are overriden with the scenario's start/stop times.
        sc: "IScenario" = clr.Convert(self.m_oApplication.current_scenario, IScenario)
        oJ4.ephemeris_interval.set_explicit_interval("1 Jul 2005 12:00:00.000", "2 Jul 2005 12:00:00.000")
        Assert.assertEqual("1 Jul 2005 12:00:00.000", oJ4.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2005 12:00:00.000", oJ4.ephemeris_interval.find_stop_time())

        Assert.assertNotEqual(sc.start_time, oJ4.ephemeris_interval.find_start_time())
        Assert.assertNotEqual(sc.stop_time, oJ4.ephemeris_interval.find_stop_time())

        oJ4.propagate()

        Assert.assertEqual("1 Jul 2005 12:00:00.000", oJ4.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2005 12:00:00.000", oJ4.ephemeris_interval.find_stop_time())

        oJ4.ephemeris_interval.set_implicit_interval(
            self.m_oApplication.current_scenario.vgt.event_intervals["AnalysisInterval"]
        )
        oJ4.propagate()

        Assert.assertEqual(sc.start_time, oJ4.ephemeris_interval.find_start_time())
        Assert.assertEqual(sc.stop_time, oJ4.ephemeris_interval.find_stop_time())

        self.m_logger.WriteLine("----- J4 PERTURBATION PROPAGATOR TEST ----- END -----")


# endregion


# region PropagatorSGP4Helper
class PropagatorSGP4Helper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        oApplication.unit_preferences.reset_units()

    # endregion

    # region Run method
    def Run(self, oSGP4: "IVehiclePropagatorSGP4"):
        self.m_logger.WriteLine("----- SGP4 PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oSGP4)

        oSGP4.settings.use_sgp4_one_point_interpolation = False
        oSGP4.settings.use_sgp4_one_point_validation = True
        oSGP4.settings.use_sgp4_one_point_warning = True
        Assert.assertFalse(oSGP4.settings.use_sgp4_one_point_interpolation)
        Assert.assertTrue(oSGP4.settings.use_sgp4_one_point_validation)
        Assert.assertTrue(oSGP4.settings.use_sgp4_one_point_warning)

        # StartTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oSGP4.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oSGP4.ephemeris_interval.find_stop_time())
        oSGP4.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "19 Jan 2003 02:46:24.680")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oSGP4.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oSGP4.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oSGP4.ephemeris_interval.find_stop_time())
        Assert.assertEqual("19 Jan 2003 02:46:24.680", oSGP4.ephemeris_interval.find_stop_time())
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oSGP4.step)
        oSGP4.step = 12
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oSGP4.step)
        Assert.assertEqual(12, oSGP4.step)
        if oSGP4.segments.routine_type != "SGP4":
            oSGP4.segments.routine_type = "SGP4"
            Assert.assertEqual("SGP4", oSGP4.segments.routine_type)

        def action89():
            oSGP4.step = 12345

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action89)
        # Segments
        oSegments: "IVehicleSGP4SegmentCollection" = oSGP4.segments
        Assert.assertIsNotNone(oSegments)
        # RemoveAllSegs
        oSegments.remove_all_segs()
        Assert.assertEqual(0, oSegments.count)
        # Count
        self.m_logger.WriteLine3("\tThe current Segment collection contains: {0} elements.", oSegments.count)
        # AddSeg
        oSegments.ssc_number = "123"
        oSegment: "IVehicleSGP4Segment" = oSegments.add_seg()
        Assert.assertIsNotNone(oSegment)
        Assert.assertEqual(1, oSegments.count)
        self.m_logger.WriteLine3("\tThe new Segment collection contains: {0} elements.", oSegments.count)
        # _NewEnum
        sgp4Segment: "IVehicleSGP4Segment"
        # _NewEnum
        for sgp4Segment in oSegments:
            self.m_logger.WriteLine7(
                "\t\tSegment 0(Enum): SSCNum = {0}, Epoch = {1}", sgp4Segment.ssc_num, sgp4Segment.epoch
            )

        self.m_logger.WriteLine7(
            "\t\tSegment 0(Item): SSCNum = {0}, Epoch = {1}", oSegments[0].ssc_num, oSegments[0].epoch
        )
        # Item
        self.SegmentTest(oSegment)

        # MaxTLELimit
        self.m_logger.WriteLine3("\tThe current MaxTLELimit is:  {0}", oSegments.max_tle_limit)
        oSegments.max_tle_limit = 123
        self.m_logger.WriteLine3("\tThe new MaxTLELimit is:  {0}", oSegments.max_tle_limit)
        Assert.assertEqual(123, oSegments.max_tle_limit)

        def action90():
            oSegments.max_tle_limit = 12345

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action90)
        # AvailableRoutines
        arRoutines = oSegments.available_routines
        self.m_logger.WriteLine3("\tThe Segment collection contains: {0} available routines.", Array.Length(arRoutines))

        iIndex: int = 0
        while iIndex < Array.Length(arRoutines):
            self.m_logger.WriteLine7("\t\tRoutine {0}: {1}", iIndex, arRoutines[iIndex])

            iIndex += 1

        # RoutineType
        self.m_logger.WriteLine5("\tThe current RoutineType is:  {0}", oSegments.routine_type)
        if Array.Length(arRoutines) > 1:
            oSegments.routine_type = str(arRoutines[0])
            self.m_logger.WriteLine5("\tThe new RoutineType is:  {0}", oSegments.routine_type)
            Assert.assertEqual(str(arRoutines[0]), oSegments.routine_type)

            def action91():
                oSegments.routine_type = "InvalidRoutineType"

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action91)

        else:
            if Array.Length(arRoutines) == 1:

                def action92():
                    oSegments.routine_type = str(arRoutines[0])

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action92)

        def action93():
            oSegments.remove_seg(12)

        # RemoveSeg
        TryCatchAssertBlock.DoAssert("Should not allow to remove an illegal segment.", action93)
        oSegments.remove_seg(0)
        Assert.assertEqual(0, oSegments.count)
        # LoadMethodType (eAutoLoad)
        self.m_logger.WriteLine6("\tThe current LoadMethodType is:  {0}", oSegments.load_method_type)
        oSegments.load_method_type = LOAD_METHOD_TYPE.AUTO_LOAD
        self.m_logger.WriteLine6("\tThe new LoadMethodType is:  {0}", oSegments.load_method_type)
        Assert.assertEqual(LOAD_METHOD_TYPE.AUTO_LOAD, oSegments.load_method_type)
        # LoadMethod
        self.LoadFileTest(clr.CastAs(oSegments.load_method, IVehicleSGP4LoadFile))
        # Propagate
        oSGP4.propagate()
        # RemoveAllSegs
        oSegments.remove_all_segs()
        Assert.assertEqual(0, oSegments.count)
        # LoadMethodType (eFileInsert)
        oSegments.load_method_type = LOAD_METHOD_TYPE.FILE_INSERT
        self.m_logger.WriteLine6("\tThe new LoadMethodType is:  {0}", oSegments.load_method_type)
        Assert.assertEqual(LOAD_METHOD_TYPE.FILE_INSERT, oSegments.load_method_type)
        # LoadMethod
        self.LoadFileTest(clr.CastAs(oSegments.load_method, IVehicleSGP4LoadFile))
        # Propagate
        oSGP4.propagate()
        # RemoveAllSegs
        oSegments.remove_all_segs()
        Assert.assertEqual(0, oSegments.count)
        # LoadMethodType (eFileLoad)
        oSegments.load_method_type = LOAD_METHOD_TYPE.FILE_LOAD
        self.m_logger.WriteLine6("\tThe new LoadMethodType is:  {0}", oSegments.load_method_type)
        Assert.assertEqual(LOAD_METHOD_TYPE.FILE_LOAD, oSegments.load_method_type)
        # LoadMethod
        self.LoadFileTest(clr.CastAs(oSegments.load_method, IVehicleSGP4LoadFile))
        # Propagate
        oSGP4.propagate()

        # test csv format
        oSGP4.ephemeris_interval.set_explicit_interval("7 May 2010 12:00:00", "10 May 2010 12:00:00")
        oSegments.remove_all_segs()
        Assert.assertEqual(0, oSegments.count)
        self.m_logger.WriteLine("\tThe new filetype is : csv")
        oFile: "IVehicleSGP4LoadFile" = clr.CastAs(oSegments.load_method, IVehicleSGP4LoadFile)
        file: str = TestBase.GetScenarioFile("smallSet_unsorted.OMM.csv")
        self.m_logger.WriteLine5("\t\tThe current File is: {0}", oFile.file)
        oFile.file = file
        self.m_logger.WriteLine5("\t\tThe new File is: {0}", oFile.file)
        # GetSSCNumsFromFile
        arSSCNumbers = oFile.get_ssc_nums_from_file()
        self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} SSC Numbers", Array.Length(arSSCNumbers))
        if Array.Length(arSSCNumbers) > 0:
            arSegments = oFile.get_segs_from_file("1749")
            self.m_logger.WriteLine3(
                "\t\tThe loaded file contains: {0} segments for SSC 1749", Array.Length(arSegments)
            )

            iIndex: int = 0
            while iIndex < Array.Length(arSegments):
                self.m_logger.WriteLine7("\t\t\tSegment {0}: {1}", iIndex, arSegments[iIndex])

                iIndex += 1

            # AddSegsFromFile
            oFile.add_segs_from_file(arSegments)

        self.m_logger.WriteLine5("\t\t\tSSC Number: {0}", oSegments.ssc_number)
        oSGP4.propagate()

        # test 9 digit ssc numbers
        oSegments.remove_all_segs()
        Assert.assertEqual(0, oSegments.count)
        self.m_logger.WriteLine("\tThe new filetype is : csv")
        oFile = clr.CastAs(oSegments.load_method, IVehicleSGP4LoadFile)
        file = TestBase.GetScenarioFile("799501749.csv")
        self.m_logger.WriteLine5("\t\tThe current File is: {0}", oFile.file)
        oFile.file = file
        self.m_logger.WriteLine5("\t\tThe new File is: {0}", oFile.file)
        # GetSSCNumsFromFile
        arSSCNumbers = oFile.get_ssc_nums_from_file()
        self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} SSC Numbers", Array.Length(arSSCNumbers))
        if Array.Length(arSSCNumbers) > 0:
            arSegments = oFile.get_segs_from_file("799501749")
            self.m_logger.WriteLine3(
                "\t\tThe loaded file contains: {0} segments for SSC 799501749", Array.Length(arSegments)
            )

            iIndex: int = 0
            while iIndex < Array.Length(arSegments):
                self.m_logger.WriteLine7("\t\t\tSegment {0}: {1}", iIndex, arSegments[iIndex])

                iIndex += 1

            # AddSegsFromFile
            oFile.add_segs_from_file(arSegments)

        self.m_logger.WriteLine5("\t\t\tSSC Number: {0}", oSegments.ssc_number)
        oSGP4.propagate()
        segAlpha: "IVehicleSGP4Segment" = oSGP4.segments[0]
        Assert.assertTrue(segAlpha.enabled)
        Assert.assertTrue((segAlpha.ssc_num == "799501749"))

        # test alpha5, alphaOnly
        oSegments.remove_all_segs()
        Assert.assertEqual(0, oSegments.count)
        self.m_logger.WriteLine("\ttesting use of alpha5 and alphaOnly SSCs")
        oFile = clr.CastAs(oSegments.load_method, IVehicleSGP4LoadFile)
        file = TestBase.GetScenarioFile("smallSet_unsorted_alpha5.tce")
        self.m_logger.WriteLine5("\t\tThe current File is: {0}", oFile.file)
        oFile.file = file
        self.m_logger.WriteLine5("\t\tThe new File is: {0}", oFile.file)
        # GetSSCNumsFromFile
        arSSCNumbers = oFile.get_ssc_nums_from_file()
        self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} SSC Numbers", Array.Length(arSSCNumbers))
        if Array.Length(arSSCNumbers) > 0:
            arSegments = oFile.get_segs_from_file("A0058")
            self.m_logger.WriteLine3(
                "\t\tThe loaded file contains: {0} segments for SSC A0058", Array.Length(arSegments)
            )

            iIndex: int = 0
            while iIndex < Array.Length(arSegments):
                self.m_logger.WriteLine7("\t\t\tSegment {0}: {1}", iIndex, arSegments[iIndex])

                iIndex += 1

            # AddSegsFromFile
            oFile.add_segs_from_file(arSegments)

        self.m_logger.WriteLine5("\t\t\tSSC Number: {0}", oSegments.ssc_number)
        oSGP4.propagate()
        segAlpha = oSGP4.segments[0]
        Assert.assertTrue(segAlpha.enabled)
        Assert.assertTrue((segAlpha.ssc_num == "A0058"))

        oSegments.remove_all_segs()
        Assert.assertEqual(0, oSegments.count)
        oFile = clr.CastAs(oSegments.load_method, IVehicleSGP4LoadFile)
        oFile.file = file
        if Array.Length(arSSCNumbers) > 0:
            arSegments = oFile.get_segs_from_file("NotA5")
            self.m_logger.WriteLine3(
                "\t\tThe loaded file contains: {0} segments for SSC NotA5", Array.Length(arSegments)
            )

            iIndex: int = 0
            while iIndex < Array.Length(arSegments):
                self.m_logger.WriteLine7("\t\t\tSegment {0}: {1}", iIndex, arSegments[iIndex])

                iIndex += 1

            # AddSegsFromFile
            oFile.add_segs_from_file(arSegments)

        self.m_logger.WriteLine5("\t\t\tSSC Number: {0}", oSegments.ssc_number)
        oSGP4.propagate()
        segAlpha = oSGP4.segments[0]
        Assert.assertTrue(segAlpha.enabled)
        Assert.assertTrue((segAlpha.ssc_num == "NotA5"))

        # 9 digit ssc number
        tasks: "IVehiclePropagatorSGP4CommonTasks" = oSGP4.common_tasks
        oSGP4.auto_update_enabled = False
        fn: str = TestBase.GetScenarioFile("799501749.csv")
        tasks.add_segs_from_file("799501749", fn)
        oSGP4.propagate()
        Assert.assertTrue((oSGP4.segments.ssc_number == "799501749"))

        # test assignment of 9 digits
        oSGP4.segments.ssc_number = "111101749"
        Assert.assertTrue((oSGP4.segments.ssc_number == "111101749"))
        oSGP4.segments.ssc_number = "901749"
        Assert.assertTrue((oSGP4.segments.ssc_number == "000901749"))

        # auto-update using alpha5 ssc number
        oSGP4.segments.ssc_number = "B0058"
        oSGP4.auto_update_enabled = True
        oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        oSGP4.auto_update.file_source.filename = TestBase.GetScenarioFile("smallSet_unsorted_alpha5.tce")
        preview = oSGP4.auto_update.file_source.preview()
        oSGP4.propagate()

        # auto-update using csv file
        oSGP4.segments.ssc_number = "24836"
        oSGP4.auto_update_enabled = True
        oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        oSGP4.auto_update.file_source.filename = TestBase.GetScenarioFile("smallSet_unsorted.OMM.csv")
        preview = oSGP4.auto_update.file_source.preview()
        oSGP4.propagate()

        # LoadMethodType (eOnlineAutoLoad)
        oSGP4.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "19 Jan 2003 02:46:24.680")
        oSegments.load_method_type = LOAD_METHOD_TYPE.ONLINE_AUTO_LOAD
        self.m_logger.WriteLine6("\tThe new LoadMethodType is:  {0}", oSegments.load_method_type)
        Assert.assertEqual(LOAD_METHOD_TYPE.ONLINE_AUTO_LOAD, oSegments.load_method_type)

        # this is backwards compatability using a deprecated interface
        # the current interface is IVehicleSGP4OnlineLoad

        # LoadMethod
        oLoader: "IVehicleSGP4OnlineAutoLoad" = clr.CastAs(oSegments.load_method, IVehicleSGP4OnlineAutoLoad)
        Assert.assertIsNotNone(oLoader)
        # AddLatestSegFromOnline
        oLoader.add_latest_seg_from_online("123")  # this curently does nothing!
        # Propagate
        oSGP4.propagate()

        # LoadMethodType (eOnlineLoad)
        oSegments.load_method_type = LOAD_METHOD_TYPE.ONLINE_LOAD
        self.m_logger.WriteLine6("\tThe new LoadMethodType is:  {0}", oSegments.load_method_type)
        Assert.assertEqual(LOAD_METHOD_TYPE.ONLINE_LOAD, oSegments.load_method_type)
        # LoadMethod
        self.OnlineLoadTest(clr.CastAs(oSegments.load_method, IVehicleSGP4OnlineLoad))
        # Propagate
        oSGP4.propagate()

        # ----------------------------------------------------
        # New SGP4 functionality
        # ----------------------------------------------------

        Assert.assertFalse(oSGP4.auto_update_enabled)
        Assert.assertEqual(VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_NONE, oSGP4.auto_update.selected_source)

        def action94():
            oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_NONE

        TryCatchAssertBlock.DoAssert("Setting read-only attribute.", action94)

        def action95():
            oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_UNKNOWN

        TryCatchAssertBlock.DoAssert("Setting read-only attribute.", action95)

        oSGP4.auto_update_enabled = True
        Assert.assertTrue(oSGP4.auto_update_enabled)

        oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_ONLINE
        Assert.assertEqual(
            oSGP4.auto_update.selected_source, VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_ONLINE
        )

        oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        Assert.assertEqual(
            oSGP4.auto_update.selected_source, VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        )

        def action96():
            oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_NONE

        TryCatchAssertBlock.DoAssert("Must not allow setting the enumeration.", action96)

        def action97():
            oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_UNKNOWN

        TryCatchAssertBlock.DoAssert("Must not allow setting the enumeration.", action97)

        def action98():
            oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_ONLINE_SPACE_TRACK

        TryCatchAssertBlock.DoAssert("Auto updates from space track are not currently supported.", action98)

        Assert.assertTrue(oSGP4.auto_update_enabled)
        oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        Assert.assertEqual(
            oSGP4.auto_update.selected_source, VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        )
        Assert.assertTrue(oSGP4.auto_update_enabled)

        # ----------------------------------------------------
        # Auto-update the satellite using the external file.
        # ----------------------------------------------------
        oSGP4.ephemeris_interval.set_explicit_interval("1 Jul 2007 12:00", "2 Jul 2007 12:00")
        oSGP4.step = 60
        oSGP4.segments.ssc_number = "5"
        oSGP4.auto_update_enabled = True
        oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        oSGP4.auto_update.file_source.filename = TestBase.GetScenarioFile("stkAllTLE.tce")
        preview = oSGP4.auto_update.file_source.preview()
        oSGP4.propagate()

        preview = oSGP4.auto_update.file_source.preview()

        Assert.assertTrue((oSGP4.segments.count == 1))

        # ----------------------------------------------------
        # Auto-update the satellite using the online source.
        # ----------------------------------------------------
        oSGP4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_ONLINE
        preview = oSGP4.auto_update.online_source.preview()
        oSGP4.propagate()
        preview = oSGP4.auto_update.online_source.preview()

        # ----------------------------------------------------
        # Validate the segments
        # ----------------------------------------------------
        segment: "IVehicleSGP4Segment" = oSGP4.segments[0]
        Assert.assertTrue(segment.enabled)
        Assert.assertTrue((segment.ssc_num == "00005"))
        Assert.assertTrue((segment.rev_number == 69126), String.Format("{0}", segment.rev_number))
        Assert.assertTrue(segment.intl_designator.startswith("1958-002B"))
        Assert.assertEqual(segment.switching_method, VEHICLE_SGP4_SWITCH_METHOD.SGP4_EPOCH)
        Assert.assertEqual(segment.switch_time, "30 Jun 2007 21:06:05.884")

        oSGP4.auto_update.properties.selection = VEHICLE_SGP4TLE_SELECTION.SGP4TLE_SELECTION_USE_ALL
        Assert.assertEqual(VEHICLE_SGP4TLE_SELECTION.SGP4TLE_SELECTION_USE_ALL, oSGP4.auto_update.properties.selection)
        oSGP4.auto_update.properties.switch_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4_EPOCH
        Assert.assertEqual(VEHICLE_SGP4_SWITCH_METHOD.SGP4_EPOCH, oSGP4.auto_update.properties.switch_method)
        oSGP4.auto_update.properties.switch_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4_MIDPOINT
        Assert.assertEqual(VEHICLE_SGP4_SWITCH_METHOD.SGP4_MIDPOINT, oSGP4.auto_update.properties.switch_method)
        # Override is not supported
        # oSGP4.AutoUpdate.Properties.SwitchMethod = VEHICLE_SGP4_SWITCH_METHOD.eSGP4Override;
        # Assert.AreEqual(VEHICLE_SGP4_SWITCH_METHOD.eSGP4Override, oSGP4.AutoUpdate.Properties.SwitchMethod);
        oSGP4.auto_update.properties.switch_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4TCA
        Assert.assertEqual(VEHICLE_SGP4_SWITCH_METHOD.SGP4TCA, oSGP4.auto_update.properties.switch_method)

        oSGP4.auto_update.properties.selection = VEHICLE_SGP4TLE_SELECTION.SGP4TLE_SELECTION_USE_FIRST
        Assert.assertEqual(
            VEHICLE_SGP4TLE_SELECTION.SGP4TLE_SELECTION_USE_FIRST, oSGP4.auto_update.properties.selection
        )

        def action99():
            oSGP4.auto_update.properties.switch_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4_EPOCH

        TryCatchAssertBlock.DoAssert("Must not allow changing the SwitchMethod.", action99)

        oSGP4.settings.use_sgp4_one_point_interpolation = True
        oSGP4.settings.use_sgp4_one_point_validation = True
        oSGP4.settings.use_sgp4_one_point_warning = True
        Assert.assertTrue(oSGP4.settings.use_sgp4_one_point_interpolation)
        Assert.assertTrue(oSGP4.settings.use_sgp4_one_point_validation)
        Assert.assertTrue(oSGP4.settings.use_sgp4_one_point_warning)

        oSGP4.settings.use_sgp4_one_point_interpolation = False
        oSGP4.settings.use_sgp4_one_point_validation = False
        oSGP4.settings.use_sgp4_one_point_warning = False
        Assert.assertTrue((not oSGP4.settings.use_sgp4_one_point_interpolation))
        Assert.assertTrue((not oSGP4.settings.use_sgp4_one_point_validation))
        Assert.assertTrue((not oSGP4.settings.use_sgp4_one_point_warning))

        self.m_logger.WriteLine("----- SGP4 PROPAGATOR TEST ----- END -----")

    # endregion

    # region SegmentTest
    def SegmentTest(self, oSegment: "IVehicleSGP4Segment"):
        Assert.assertIsNotNone(oSegment)

        # Enabled
        self.m_logger.WriteLine4("\tThe current Enabled is:  {0}", oSegment.enabled)
        oSegment.enabled = False
        Assert.assertFalse(oSegment.enabled)
        oSegment.enabled = True
        Assert.assertTrue(oSegment.enabled)

        # Epoch
        self.m_logger.WriteLine6("\tThe current Epoch is:  {0}", oSegment.epoch)
        oSegment.epoch = 123
        self.m_logger.WriteLine6("\tThe new Epoch is:  {0}", oSegment.epoch)
        Assert.assertEqual(123, oSegment.epoch)

        def action100():
            oSegment.epoch = 123456

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action100)

        # SSCNum
        self.m_logger.WriteLine5("\tThe current SSCNum is:  {0}", oSegment.ssc_num)
        Assert.assertEqual("00123", oSegment.ssc_num)

        # RevNumber
        self.m_logger.WriteLine3("\tThe current RevNumber is:  {0}", oSegment.rev_number)
        oSegment.rev_number = 321
        self.m_logger.WriteLine3("\tThe new RevNumber is:  {0}", oSegment.rev_number)
        Assert.assertEqual(321, oSegment.rev_number)

        def action101():
            oSegment.rev_number = 1234567890

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action101)

        # Inclination
        self.m_logger.WriteLine6("\tThe current Inclination is:  {0}", oSegment.inclination)
        oSegment.inclination = 123
        self.m_logger.WriteLine6("\tThe new Inclination is:  {0}", oSegment.inclination)
        Assert.assertEqual(123, oSegment.inclination)

        def action102():
            oSegment.inclination = 1234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action102)

        # ArgOfPerigee
        self.m_logger.WriteLine6("\tThe current ArgOfPerigee is:  {0}", oSegment.arg_of_perigee)
        oSegment.arg_of_perigee = 123
        self.m_logger.WriteLine6("\tThe new ArgOfPerigee is:  {0}", oSegment.arg_of_perigee)
        Assert.assertEqual(123, oSegment.arg_of_perigee)

        def action103():
            oSegment.arg_of_perigee = 1234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action103)

        # RAAN
        self.m_logger.WriteLine6("\tThe current RAAN is:  {0}", oSegment.raan)
        oSegment.raan = 123
        self.m_logger.WriteLine6("\tThe new RAAN is:  {0}", oSegment.raan)
        Assert.assertEqual(123, oSegment.raan)

        def action104():
            oSegment.raan = 1234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action104)

        # Eccentricity
        self.m_logger.WriteLine6("\tThe current Eccentricity is:  {0}", oSegment.eccentricity)
        oSegment.eccentricity = 0.123
        self.m_logger.WriteLine6("\tThe new Eccentricity is:  {0}", oSegment.eccentricity)
        Assert.assertEqual(0.123, oSegment.eccentricity)

        def action105():
            oSegment.eccentricity = 1.234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action105)

        # MeanMotion
        self.m_logger.WriteLine6("\tThe current MeanMotion is:  {0}", oSegment.mean_motion)
        oSegment.mean_motion = 0.0123
        self.m_logger.WriteLine6("\tThe new MeanMotion is:  {0}", oSegment.mean_motion)
        Assert.assertAlmostEqual(0.0123, float(oSegment.mean_motion), delta=1e-05)

        def action106():
            oSegment.mean_motion = 1.234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action106)

        # MeanAnomaly
        self.m_logger.WriteLine6("\tThe current MeanAnomaly is:  {0}", oSegment.mean_anomaly)
        oSegment.mean_anomaly = 123
        self.m_logger.WriteLine6("\tThe new MeanAnomaly is:  {0}", oSegment.mean_anomaly)
        Assert.assertEqual(123, oSegment.mean_anomaly)

        def action107():
            oSegment.mean_anomaly = 1234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action107)

        # MeanMotionDot
        self.m_logger.WriteLine6("\tThe current MeanMotionDot is:  {0}", oSegment.mean_motion_dot)
        # MotionDotDot
        self.m_logger.WriteLine6("\tThe current MotionDotDot is:  {0}", oSegment.motion_dot_dot)

        # BStar
        self.m_logger.WriteLine6("\tThe current BStar is:  {0}", oSegment.b_star)
        oSegment.b_star = 0.321
        self.m_logger.WriteLine6("\tThe new BStar is:  {0}", oSegment.b_star)
        Assert.assertEqual(0.321, oSegment.b_star)

        def action108():
            oSegment.b_star = 1.234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action108)

        # Classification
        self.m_logger.WriteLine5("\tThe current Classification is:  {0}", oSegment.classification)
        oSegment.classification = "S"
        self.m_logger.WriteLine5("\tThe new Classification is:  {0}", oSegment.classification)
        Assert.assertEqual("S", oSegment.classification)

        def action109():
            oSegment.classification = "SS"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action109)

        # IntlDesignator
        self.m_logger.WriteLine5("\tThe current IntlDesignator is:  {0}", oSegment.intl_designator)
        oSegment.intl_designator = "Test"
        self.m_logger.WriteLine5("\tThe new IntlDesignator is:  {0}", oSegment.intl_designator)
        Assert.assertEqual("Test", oSegment.intl_designator)

        def action110():
            oSegment.intl_designator = "InvalidDesignator"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action110)

        # Range
        self.m_logger.WriteLine6("\tThe current Range is:  {0}", oSegment.range)

        # SwitchingMethod (eSGP4Disable)
        self.m_logger.WriteLine6("\tThe current SwitchingMethod is:  {0}", oSegment.switching_method)
        oSegment.switching_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4_DISABLE
        self.m_logger.WriteLine6("\tThe new SwitchingMethod is:  {0}", oSegment.switching_method)
        Assert.assertEqual(VEHICLE_SGP4_SWITCH_METHOD.SGP4_DISABLE, oSegment.switching_method)

        def action111():
            oSegment.switch_time = "24 Jan 2003 02:46:24.680"

        TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action111)

        # SwitchingMethod (eSGP4Epoch)
        oSegment.switching_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4_EPOCH
        self.m_logger.WriteLine6("\tThe new SwitchingMethod is:  {0}", oSegment.switching_method)
        Assert.assertEqual(VEHICLE_SGP4_SWITCH_METHOD.SGP4_EPOCH, oSegment.switching_method)

        def action112():
            oSegment.switch_time = "24 Jan 2003 02:46:24.680"

        TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action112)

        # SwitchingMethod (eSGP4Midpoint)
        oSegment.switching_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4_MIDPOINT
        self.m_logger.WriteLine6("\tThe new SwitchingMethod is:  {0}", oSegment.switching_method)
        Assert.assertEqual(VEHICLE_SGP4_SWITCH_METHOD.SGP4_MIDPOINT, oSegment.switching_method)

        def action113():
            oSegment.switch_time = "24 Jan 2003 02:46:24.680"

        TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action113)

        # SwitchingMethod (eSGP4Override)
        oSegment.switching_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4_OVERRIDE
        self.m_logger.WriteLine6("\tThe new SwitchingMethod is:  {0}", oSegment.switching_method)
        Assert.assertEqual(VEHICLE_SGP4_SWITCH_METHOD.SGP4_OVERRIDE, oSegment.switching_method)

        # SwitchTime
        self.m_logger.WriteLine6("\tThe current SwitchTime is:  {0}", oSegment.switch_time)
        oSegment.switch_time = "24 Jan 2003 02:46:24.680"
        self.m_logger.WriteLine6("\tThe new SwitchTime is:  {0}", oSegment.switch_time)
        Assert.assertEqual("24 Jan 2003 02:46:24.680", oSegment.switch_time)

        # SwitchingMethod (eSGP4TCA)
        oSegment.switching_method = VEHICLE_SGP4_SWITCH_METHOD.SGP4TCA
        self.m_logger.WriteLine6("\tThe new SwitchingMethod is:  {0}", oSegment.switching_method)
        Assert.assertEqual(VEHICLE_SGP4_SWITCH_METHOD.SGP4TCA, oSegment.switching_method)

        def action114():
            oSegment.switch_time = "24 Jan 2003 02:46:24.680"

        TryCatchAssertBlock.DoAssert("Should not allow to modify readonly property.", action114)

    # endregion

    # region LoadFileTest
    def LoadFileTest(self, oFile: "IVehicleSGP4LoadFile"):
        Assert.assertIsNotNone(oFile)
        file: str = TestBase.GetScenarioFile("stkAllTLE.tce")
        # File (*.tce)
        self.m_logger.WriteLine5("\t\tThe current File is: {0}", oFile.file)
        oFile.file = file
        self.m_logger.WriteLine5("\t\tThe new File is: {0}", oFile.file)

        def action115():
            oFile.file = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action115)

        def action116():
            oFile.file = "InvalidFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action116)
        # GetSSCNumsFromFile (.tce)
        arSSCNumbers = oFile.get_ssc_nums_from_file()
        self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} SSC Numbers", Array.Length(arSSCNumbers))
        # File (*.tle)
        file = TestBase.GetScenarioFile("stkAllTLE.tle")
        oFile.file = file
        self.m_logger.WriteLine5("\t\tThe new File is: {0}", oFile.file)
        # GetSSCNumsFromFile (.tle)
        arSSCNumbers = oFile.get_ssc_nums_from_file()
        self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} SSC Numbers", Array.Length(arSSCNumbers))
        # File (*.gz)
        file = TestBase.GetScenarioFile("stkAllTLE.gz")
        oFile.file = file
        self.m_logger.WriteLine5("\t\tThe new File is: {0}", oFile.file)
        # GetSSCNumsFromFile (.gz)
        arSSCNumbers = oFile.get_ssc_nums_from_file()
        self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} SSC Numbers", Array.Length(arSSCNumbers))
        # File (*.txt)
        file = TestBase.GetScenarioFile("stkAllTLE.txt")
        oFile.file = file
        self.m_logger.WriteLine5("\t\tThe new File is: {0}", oFile.file)
        # GetSSCNumsFromFile (.txt)
        arSSCNumbers = oFile.get_ssc_nums_from_file()
        self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} SSC Numbers", Array.Length(arSSCNumbers))
        if Array.Length(arSSCNumbers) > 0:
            arSegments = oFile.get_segs_from_file(str(arSSCNumbers[0]))
            self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} segments", Array.Length(arSegments))

            iIndex: int = 0
            while iIndex < Array.Length(arSegments):
                self.m_logger.WriteLine7("\t\t\tSegment {0}: {1}", iIndex, arSegments[iIndex])

                iIndex += 1

            # AddSegsFromFile
            oFile.add_segs_from_file(arSegments)

        # File (*.tce)
        file = TestBase.GetScenarioFile("stkAllTLE.tce")
        oFile.file = file
        self.m_logger.WriteLine5("\t\tThe new File is: {0}", oFile.file)
        # GetSSCNumsFromFile (.tce)
        arSSCNumbers = oFile.get_ssc_nums_from_file()
        self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} SSC Numbers", Array.Length(arSSCNumbers))
        if Array.Length(arSSCNumbers) > 0:
            # GetSegsFromFile
            arSegments = oFile.get_segs_from_file(str(arSSCNumbers[0]))
            self.m_logger.WriteLine3("\t\tThe loaded file contains: {0} Segments", Array.Length(arSegments))

            iIndex: int = 0
            while iIndex < Array.Length(arSegments):
                self.m_logger.WriteLine7("\t\t\tSegment {0}: {1}", iIndex, arSegments[iIndex])

                iIndex += 1

            def action117():
                oFile.add_segs_from_file(arSegments)

            # AddSegsFromFile (duplicate)
            TryCatchAssertBlock.DoAssert("Should not allow to load duplicated segments.", action117)

    # endregion

    # region OnlineLoadTest
    def OnlineLoadTest(self, oLoader: "IVehicleSGP4OnlineLoad"):
        Assert.assertIsNotNone(oLoader)
        # LoadNewest (true)
        self.m_logger.WriteLine4("\t\tThe current LoadNewest is: {0}", oLoader.load_newest)
        oLoader.load_newest = True
        self.m_logger.WriteLine4("\t\tThe new LoadNewest is: {0}", oLoader.load_newest)
        Assert.assertEqual(True, oLoader.load_newest)

        def action118():
            oLoader.start_time = "28 Jun 2000 15:15:16.789"

        # StartTime (readonly)
        TryCatchAssertBlock.DoAssert("The StartTime should be readonly when LoadNewest is True.", action118)

        def action119():
            oLoader.stop_time = "20 Jul 2000 15:00:00.000"

        # StopTime (readonly)
        TryCatchAssertBlock.DoAssert("The StopTime should be readonly when LoadNewest is True.", action119)
        # LoadNewest (false)
        oLoader.load_newest = False
        self.m_logger.WriteLine4("\t\tThe new LoadNewest is: {0}", oLoader.load_newest)
        Assert.assertEqual(False, oLoader.load_newest)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe current StartTime is: {0}", oLoader.start_time)
        oLoader.start_time = "28 Jun 2000 15:15:16.789"
        self.m_logger.WriteLine6("\t\tThe new StartTime is: {0}", oLoader.start_time)
        Assert.assertEqual("28 Jun 2000 15:15:16.789", oLoader.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe current StopTime is: {0}", oLoader.stop_time)
        oLoader.stop_time = "20 Jul 2000 15:00:00.000"
        self.m_logger.WriteLine6("\t\tThe new StopTime is: {0}", oLoader.stop_time)
        Assert.assertEqual("20 Jul 2000 15:00:00.000", oLoader.stop_time)
        # GetSegsFromOnline
        # 2006-11-02 panlvyayko: changed the SSCNumber to a number of one of USA's GPS satellites.
        # This way the unit test wont fail here for a few (million) years.
        arSegs = oLoader.get_segs_from_online("11054")
        self.m_logger.WriteLine3("\t\tThe Segs array contains: {0} elements.", Array.Length(arSegs))

        iIndex: int = 0
        while iIndex < Array.Length(arSegs):
            self.m_logger.WriteLine7("\t\t\tElement {0}: {1}", iIndex, arSegs[iIndex])

            iIndex += 1

        # AddSegsFromOnline
        oLoader.add_segs_from_online(arSegs)


# endregion


# region PropagatorSPICEHelper
class PropagatorSPICEHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        oApplication.unit_preferences.reset_units()

    # endregion

    # region Run method
    def Run(self, oSPICE: "IVehiclePropagatorSPICE"):
        self.m_logger.WriteLine("----- SPICE PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oSPICE)
        # StartTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oSPICE.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oSPICE.ephemeris_interval.find_stop_time())
        oSPICE.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "19 Jan 2003 02:46:24.680")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oSPICE.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oSPICE.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oSPICE.ephemeris_interval.find_stop_time())
        Assert.assertEqual("19 Jan 2003 02:46:24.680", oSPICE.ephemeris_interval.find_stop_time())
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oSPICE.step)
        oSPICE.step = 58
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oSPICE.step)
        Assert.assertEqual(58, oSPICE.step)

        def action120():
            oSPICE.step = -1.23

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action120)
        # Spice
        strFilename: str = TestBase.GetScenarioFile("de405_2000-2050.bsp")
        self.m_logger.WriteLine5("\tThe current Spice is:  {0}", oSPICE.spice)
        oSPICE.spice = strFilename
        self.m_logger.WriteLine5("\tThe new Spice is:  {0}", oSPICE.spice)
        Assert.assertEqual("de405_2000-2050.bsp", Path.GetFileName(oSPICE.spice))

        def action121():
            oSPICE.spice = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action121)

        def action122():
            oSPICE.spice = "InvalidFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action122)

        def action123():
            oSPICE.propagate()

        TryCatchAssertBlock.DoAssert("A satellite id has not been set.", action123)  # must first set body name

        # BodyName
        self.m_logger.WriteLine5("\tThe current BodyName is:  {0}", oSPICE.body_name)
        oSPICE.body_name = "VENUS"
        self.m_logger.WriteLine5("\tThe new BodyName is:  {0}", oSPICE.body_name)
        Assert.assertEqual("VENUS", oSPICE.body_name)

        def action124():
            oSPICE.body_name = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action124)

        def action125():
            oSPICE.body_name = "InvalidBodyName"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action125)
        # AvailableBodyNames
        arNames = oSPICE.available_body_names
        self.m_logger.WriteLine3("\tThe AvailableBodyNames array contains: {0} elements.", Array.Length(arNames))

        iIndex: int = 0
        while iIndex < Array.Length(arNames):
            oSPICE.body_name = str(arNames[iIndex])
            self.m_logger.WriteLine7("\t\tElement {0}: {1}", iIndex, oSPICE.body_name)
            Assert.assertEqual(arNames[iIndex], oSPICE.body_name)

            iIndex += 1

        # Segments
        oCollection: "IVehicleSegmentsCollection" = oSPICE.segments
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\tThe Segments collection contains: {0} elements.", oCollection.count)
        # _NewEnum
        spiceSegment: "IVehicleSPICESegment"
        # _NewEnum
        for spiceSegment in oCollection:
            self.m_logger.WriteLine10(
                "\t\tSegment: SegmentName = {0}, SegmentType = {1}, CoordAxes = {2}, CentralBody = {3}, StartTime = {4}, StopTime = {5}",
                spiceSegment.segment_name,
                spiceSegment.segment_type,
                spiceSegment.coord_axes,
                spiceSegment.central_body,
                spiceSegment.start_time,
                spiceSegment.stop_time,
            )

        if oCollection.count > 0:
            # Item
            oSegment: "IVehicleSPICESegment" = oCollection[0]
            Assert.assertIsNotNone(oSegment)
            self.m_logger.WriteLine10(
                "\tSegment 0: SegmentName = {0}, SegmentType = {1}, CoordAxes = {2}, CentralBody = {3}, StartTime = {4}, StopTime = {5}",
                oSegment.segment_name,
                oSegment.segment_type,
                oSegment.coord_axes,
                oSegment.central_body,
                oSegment.start_time,
                oSegment.stop_time,
            )

        def action126():
            oSegment: "IVehicleSPICESegment" = oCollection[-5]

        TryCatchAssertBlock.ExpectedException("Index is out of range.", action126)

        def action127():
            oSegment: "IVehicleSPICESegment" = oCollection[500]

        TryCatchAssertBlock.ExpectedException("Index is out of range.", action127)

        # Propagate
        oSPICE.propagate()

        # BUG59850 - Try to propagate SPICE using a SatelliteID as a BodyName
        sat: "ISatellite" = clr.Convert(self.m_oApplication.get_object_from_path("Satellite/Satellite1"), ISatellite)
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SPICE)
        spice: "IVehiclePropagatorSPICE" = clr.Convert(sat.propagator, IVehiclePropagatorSPICE)
        spice.spice = TestBase.GetScenarioFile("Satellite1.bsp")
        spice.body_name = "-200000"
        spice.ephemeris_interval.set_explicit_interval(
            (clr.Convert(self.m_oApplication.current_scenario, IScenario)).start_time,
            (clr.Convert(self.m_oApplication.current_scenario, IScenario)).stop_time,
        )
        spice.propagate()

        self.m_logger.WriteLine("----- SPICE PROPAGATOR TEST ----- END -----")


# endregion


# region PropagatorUserExternalHelper
class PropagatorUserExternalHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        oApplication.unit_preferences.reset_units()

    # endregion

    # region Run method
    def Run(self, oUser: "IVehiclePropagatorUserExternal"):
        self.m_logger.WriteLine("----- USER EXTERNAL PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oUser)
        # StartTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oUser.ephemeris_interval.find_start_time())
        oUser.start_time = "18 Jan 2003 01:23:45.678"
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oUser.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oUser.ephemeris_interval.find_start_time())
        # StopTime
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oUser.stop_time)
        oUser.stop_time = "19 Jan 2003 02:46:24.680"
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oUser.stop_time)
        Assert.assertEqual("19 Jan 2003 02:46:24.680", oUser.stop_time)
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oUser.step)
        oUser.step = 12
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oUser.step)
        Assert.assertEqual(12, oUser.step)
        # File
        strFilename: str = "stkAllTLE.tle"
        self.m_logger.WriteLine5("\tThe current File is:  {0}", oUser.file)
        oUser.file = strFilename
        self.m_logger.WriteLine5("\tThe new File is:  {0}", oUser.file)
        Assert.assertEqual("stkAllTLE.tle", oUser.file)

        def action128():
            oUser.file = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action128)

        def action129():
            oUser.file = "InvalidFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action129)
        # AvailablePropagators
        arPropagators = oUser.available_propagators
        self.m_logger.WriteLine("\tAvailable {0} propagators:")

        iIndex: int = 0
        while iIndex < Array.Length(arPropagators):
            self.m_logger.WriteLine7("\t\tPropagator {0}: {1}", iIndex, arPropagators[iIndex])

            iIndex += 1

        # Propagator
        self.m_logger.WriteLine5("\tThe current Propagator is:  {0}", oUser.propagator)
        if Array.Length(arPropagators) > 0:
            oUser.propagator = str(arPropagators[0])
            self.m_logger.WriteLine5("\tThe new Propagator is:  {0}", oUser.propagator)
            Assert.assertEqual(str(arPropagators[0]), oUser.propagator)

        def action130():
            oUser.propagator = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action130)

        def action131():
            oUser.propagator = "InvalidName"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action131)

        # AvailableVehicleIDs
        arIDs = oUser.available_vehicle_i_ds
        self.m_logger.WriteLine("\tAvailable {0} VehicleIDs:")

        iIndex: int = 0
        while iIndex < Array.Length(arIDs):
            self.m_logger.WriteLine7("\t\tVehicleID {0}: {1}", iIndex, arIDs[iIndex])

            iIndex += 1

        # VehicleID
        self.m_logger.WriteLine5("\tThe current VehicleID is:  {0}", oUser.vehicle_id)
        if Array.Length(arIDs) > 0:
            oUser.vehicle_id = str(arIDs[0])
            self.m_logger.WriteLine5("\tThe new VehicleID is:  {0}", oUser.vehicle_id)
            Assert.assertEqual(str(arIDs[0]), oUser.vehicle_id)

            def action132():
                oUser.vehicle_id = ""

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action132)

            def action133():
                oUser.vehicle_id = "InvalidName"

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action133)

        def action134():
            oUser.vehicle_id = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action134)

        def action135():
            oUser.vehicle_id = "InvalidName"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action135)

        # Description
        self.m_logger.WriteLine5("\tThe current Description is:  {0}", oUser.description)
        if (oUser.propagator == None) or (len(oUser.propagator) == 0):

            def action136():
                oUser.propagate()

            TryCatchAssertBlock.DoAssert("UserExternal propagator must have failed.", action136)

        else:
            self.m_logger.WriteLine5("EXTERNAL PROPAGATOR: {0}", oUser.propagator)
            oUser.propagate()

        self.m_logger.WriteLine("----- USER EXTERNAL PROPAGATOR TEST ----- END -----")


# endregion


# region PropagatorHPOPHelper
class PropagatorHPOPHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot", vehicle: "IStkObject", EarthGravModel):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        oApplication.unit_preferences.reset_units()
        self._vehicle: "IStkObject" = vehicle
        self.m_EarthGravModel = EarthGravModel

    # endregion

    # region Run method
    def Run(self, oHPOP: "IVehiclePropagatorHPOP", isNotEarthCentralBody: bool):
        self.m_logger.WriteLine("----- HPOP PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oHPOP)

        # Select specific GravModel which tests were written for
        result: "IExecCmdResult" = self.m_oApplication.execute_command("GetSTKHomeDir /")
        fi = FileInfo(TestBase.PathCombine(result[0], "STKData", "CentralBodies", "Earth", "WGS84_EGM96.grv"))
        if fi.Exists:
            oHPOP.force_model.central_body_gravity.file = fi.FullName
        else:
            raise Exception("Error finding grav file.")
        # oHPOP.Propagate();

        # EphemerisInterval
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oHPOP.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oHPOP.ephemeris_interval.find_stop_time())
        oHPOP.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "18 Jan 2003 02:46:24.680")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oHPOP.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oHPOP.ephemeris_interval.find_start_time())
        self.m_logger.WriteLine6("\tThe new StopTime is:  {0}", oHPOP.ephemeris_interval.find_stop_time())
        Assert.assertEqual("18 Jan 2003 02:46:24.680", oHPOP.ephemeris_interval.find_stop_time())
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oHPOP.step)
        oHPOP.step = 12
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oHPOP.step)
        Assert.assertEqual(12, oHPOP.step)

        def action137():
            oHPOP.step = 1234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action137)
        # InitialState
        self.InitialState(oHPOP.initial_state)
        # ForceModel
        self.ForceModel(oHPOP.force_model, isNotEarthCentralBody)
        # Integrator
        self.Integrator(oHPOP.integrator, oHPOP.covariance)
        # Covariance
        self.Covariance(oHPOP.covariance)

        bodies: "IVehicleEclipsingBodies" = oHPOP.force_model.eclipsing_bodies
        eclipsingBodies = bodies.assigned_eclipsing_bodies
        eclipseBody: str
        for eclipseBody in eclipsingBodies:
            self.m_logger.WriteLine(eclipseBody)

        Assert.assertTrue(bodies.is_eclipsing_body_assigned("Earth"))
        bodies.assign_eclipsing_body("Ceres")
        Assert.assertTrue(bodies.is_eclipsing_body_assigned("Ceres"))

        def action138():
            bodies.assign_eclipsing_body("Sun")

        TryCatchAssertBlock.DoAssert("Can not add sun as an eclipsing body.", action138)
        bodies.remove_eclipsing_body("Ceres")
        Assert.assertFalse(bodies.is_eclipsing_body_assigned("Ceres"))
        bodies.remove_all_eclipsing_bodies()
        Assert.assertFalse(bodies.is_eclipsing_body_assigned("Earth"))
        availableBodies = bodies.available_eclipsing_bodies
        body: str
        for body in availableBodies:
            self.m_logger.WriteLine(body)

        # Propagate
        oHPOP.propagate()
        self.m_logger.WriteLine("----- HPOP PROPAGATOR TEST ----- END -----")

    # endregion

    # region InitialState
    def InitialState(self, oState: "IVehicleInitialState"):
        cart: "IOrbitStateCartesian" = None
        Assert.assertIsNotNone(oState)
        # Epoch is deprecated
        # m_logger.WriteLine("\tThe current Epoch is: {0}", oState.Epoch);
        # oState.Epoch = "18 Jan 2003 02:40:24.680";
        # m_logger.WriteLine("\tThe new Epoch is: {0}", oState.Epoch);
        # Assert.AreEqual("18 Jan 2003 02:40:24.680", oState.Epoch);
        cart = clr.Convert(oState.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN), IOrbitStateCartesian)
        (clr.Convert(cart, IOrbitState)).epoch = "18 Jan 2003 02:40:24.680"
        Assert.assertEqual("18 Jan 2003 02:40:24.680", cart.epoch)
        oState.representation.assign(cart)
        # Representation
        oHelper = OrbitStateHelper(self.m_oApplication)
        oHelper.Run(oState.representation)

    # endregion

    # region ForceModel
    def ForceModel(self, oModel: "IVehicleHPOPForceModel", isNotEarthCentralBody: bool):
        Assert.assertIsNotNone(oModel)
        # CentralBodyGravity
        self.CentralBodyGravity(oModel.central_body_gravity, isNotEarthCentralBody)
        # SolarRadiationPressure
        self.SolarRadiationPressure(oModel.solar_radiation_pressure)
        # Drag
        self.Drag(oModel.drag)
        # ThirdBodyGravity
        self.ThirdBodyGravity(oModel.third_body_gravity)
        # MoreOptions
        self.MoreOptions(oModel.more_options)

    # endregion

    # region CentralBodyGravity
    def CentralBodyGravity(self, oGravity: "IVehicleHPOPCentralBodyGravity", isNotEarthCentralBody: bool):
        holdMaxDegree: int = oGravity.max_degree
        holdMaxOrder: int = oGravity.max_order

        # MaxDegree (default 21, range 0-70, must be >= MaxOrder, will be changed if needed when MaxOrder changes.)
        oGravity.max_degree = 30
        Assert.assertEqual(30, oGravity.max_degree)
        oGravity.max_degree = 70
        Assert.assertEqual(70, oGravity.max_degree)
        oGravity.max_degree = 21
        Assert.assertEqual(holdMaxOrder, oGravity.max_order)  # does not change

        def action139():
            oGravity.max_degree = 1

        TryCatchAssertBlock.ExpectedException("is invalid", action139)

        def action140():
            oGravity.max_degree = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action140)

        def action141():
            oGravity.max_degree = 71

        TryCatchAssertBlock.ExpectedException("is invalid", action141)

        # MaxOrder (default 21, range 0-70, must be <= MaxOrder, will be changed if needed when MaxDegree changes.)
        oGravity.max_order = 15
        Assert.assertEqual(15, oGravity.max_order)
        oGravity.max_order = 0
        Assert.assertEqual(0, oGravity.max_order)
        oGravity.max_order = 21
        Assert.assertEqual(21, oGravity.max_degree)

        def action142():
            oGravity.max_order = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action142)

        def action143():
            oGravity.max_order = 71

        TryCatchAssertBlock.ExpectedException("is invalid", action143)

        # SetMaximumDegreeAndOrder
        oGravity.set_maximum_degree_and_order(50, 45)
        Assert.assertEqual(50, oGravity.max_degree)
        Assert.assertEqual(45, oGravity.max_order)
        oGravity.set_maximum_degree_and_order(45, 45)
        Assert.assertEqual(45, oGravity.max_degree)
        Assert.assertEqual(45, oGravity.max_order)
        oGravity.set_maximum_degree_and_order(70, 0)
        Assert.assertEqual(70, oGravity.max_degree)
        Assert.assertEqual(0, oGravity.max_order)
        oGravity.set_maximum_degree_and_order(holdMaxDegree, holdMaxOrder)  # restore to original
        Assert.assertEqual(holdMaxDegree, oGravity.max_degree)
        Assert.assertEqual(holdMaxOrder, oGravity.max_order)

        def action144():
            oGravity.set_maximum_degree_and_order(45, 50)

        TryCatchAssertBlock.ExpectedException("must be greater or equal", action144)

        def action145():
            oGravity.set_maximum_degree_and_order(71, 0)

        TryCatchAssertBlock.ExpectedException("Invalid values", action145)

        def action146():
            oGravity.set_maximum_degree_and_order(70, -1)

        TryCatchAssertBlock.ExpectedException("Invalid values", action146)

        # UseOceanTides
        # See: 47217 UseOceanTides is grayed out in GUI but writtable via the Object Model
        # UseOceanTides can only be set(not-grayed out) if the central body is earth.
        oGravity.use_ocean_tides = True
        Assert.assertEqual(True, oGravity.use_ocean_tides)
        oGravity.use_ocean_tides = False
        Assert.assertEqual(False, oGravity.use_ocean_tides)

        # SolidTideType
        oGravity.solid_tide_type = SOLID_TIDE.FULL
        Assert.assertEqual(SOLID_TIDE.FULL, oGravity.solid_tide_type)
        oGravity.solid_tide_type = SOLID_TIDE.NONE
        Assert.assertEqual(SOLID_TIDE.NONE, oGravity.solid_tide_type)
        oGravity.solid_tide_type = SOLID_TIDE.PERMANENT
        Assert.assertEqual(SOLID_TIDE.PERMANENT, oGravity.solid_tide_type)

        # File
        oGravity.file = "WGS84_EGM96.grv"
        Assert.assertEqual("WGS84_EGM96.grv", oGravity.file)
        oGravity.file = r"STKData\CentralBodies\Earth\EGM2008.grv"
        Assert.assertEqual(TestBase.PathCombine("STKData", "CentralBodies", "Earth", "EGM2008.grv"), oGravity.file)

        def action147():
            oGravity.file = ""

        TryCatchAssertBlock.ExpectedException("file does not exist", action147)

        def action148():
            oGravity.file = "InvalidFile.Name"

        TryCatchAssertBlock.ExpectedException("file does not exist", action148)

        # UseSecularVariations
        # Note: oGravity.File must be set to "EGM2008.grv" so that the property below is visible in GUI (on More Options panel).
        oGravity.use_secular_variations = True
        Assert.assertTrue(oGravity.use_secular_variations)
        oGravity.use_secular_variations = False
        Assert.assertFalse(oGravity.use_secular_variations)

    # endregion

    # region SolarRadiationPressure
    def SolarRadiationPressure(self, oPressure: "IVehicleHPOPSolarRadiationPressure"):
        Assert.assertIsNotNone(oPressure)
        # Use (false)
        self.m_logger.WriteLine4("\tThe current Use is: {0}", oPressure.use)
        oPressure.use = False
        self.m_logger.WriteLine4("\tThe new Use is: {0}", oPressure.use)
        Assert.assertEqual(False, oPressure.use)

        def action149():
            oPressure.use_boundary_mitigation = False

        # UseBoundaryMitigation (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action149)

        def action150():
            oPressure.shadow_model = SHADOW_MODEL.MOD_CYLINDRICAL

        # ShadowModel (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action150)
        # Use (true)
        oPressure.use = True
        self.m_logger.WriteLine4("\tThe new Use is: {0}", oPressure.use)
        Assert.assertEqual(True, oPressure.use)
        # UseBoundaryMitigation
        self.m_logger.WriteLine4("\tThe current UseBoundaryMitigation is: {0}", oPressure.use_boundary_mitigation)
        oPressure.use_boundary_mitigation = False
        self.m_logger.WriteLine4("\tThe new UseBoundaryMitigation is: {0}", oPressure.use_boundary_mitigation)
        Assert.assertEqual(False, oPressure.use_boundary_mitigation)
        oPressure.use_boundary_mitigation = True
        self.m_logger.WriteLine4("\tThe new UseBoundaryMitigation is: {0}", oPressure.use_boundary_mitigation)
        Assert.assertEqual(True, oPressure.use_boundary_mitigation)
        # ShadowModel
        self.m_logger.WriteLine6("\tThe current ShadowModel is: {0}", oPressure.shadow_model)
        oPressure.shadow_model = SHADOW_MODEL.MOD_CYLINDRICAL
        self.m_logger.WriteLine6("\tThe new ShadowModel is: {0}", oPressure.shadow_model)
        Assert.assertEqual(SHADOW_MODEL.MOD_CYLINDRICAL, oPressure.shadow_model)
        oPressure.shadow_model = SHADOW_MODEL.MOD_DUAL_CONE
        self.m_logger.WriteLine6("\tThe new ShadowModel is: {0}", oPressure.shadow_model)
        Assert.assertEqual(SHADOW_MODEL.MOD_DUAL_CONE, oPressure.shadow_model)
        oPressure.shadow_model = SHADOW_MODEL.MOD_NONE
        self.m_logger.WriteLine6("\tThe new ShadowModel is: {0}", oPressure.shadow_model)
        Assert.assertEqual(SHADOW_MODEL.MOD_NONE, oPressure.shadow_model)

        # Testing new SRP models
        self.m_logger.WriteLine("***************** SRP MODELS ***********")
        oSrpModel: "IVehicleHPOPSRPModel" = oPressure.srp_model
        oSrpModel.set_model_type(SRP_MODEL.SPHERICAL)
        Assert.assertEqual(SRP_MODEL.SPHERICAL, oSrpModel.model_type)

        oSrpModel.set_model_type(SRP_MODEL.SPHERICAL)
        Assert.assertEqual(SRP_MODEL.SPHERICAL, oSrpModel.model_type)
        oSrpModelChoices = oSrpModel.model_supported_types
        Assert.assertIsNotNone(oSrpModelChoices)

        i: int = 0
        while i < len(oSrpModelChoices):
            eModel: "SRP_MODEL" = clr.Convert(int(oSrpModelChoices[i][0]), SRP_MODEL)
            self.m_logger.WriteLine6("SRP Model: {0}", eModel)
            oSrpModel.set_model_type(eModel)
            eModel1: "SRP_MODEL" = oSrpModel.model_type
            Assert.assertEqual(eModel, eModel1)
            Assert.assertTrue(oSrpModel.is_model_type_supported(eModel))
            if eModel == SRP_MODEL.SPHERICAL:
                oSphericalSRP: "ISRPModelSpherical" = clr.CastAs(oSrpModel.model, ISRPModelSpherical)
                Assert.assertIsNotNone(oSphericalSRP)

                oSphericalSRP.area_mass_ratio = 12.0
                Assert.assertEqual(12.0, oSphericalSRP.area_mass_ratio)
                oSphericalSRP.cr = 99
                Assert.assertEqual(99, oSphericalSRP.cr)
                type1: "SRP_MODEL" = oSphericalSRP.type

                def action151():
                    oSphericalSRP.cr = -101

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action151)

                def action152():
                    oSphericalSRP.cr = 101

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action152)

                def action153():
                    oSphericalSRP.area_mass_ratio = 10000

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action153)

                def action154():
                    oSphericalSRP.area_mass_ratio = -10000

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action154)
            elif (
                (
                    (
                        (
                            ((eModel == SRP_MODEL.G_P_S_BLK_I_I_A_AERO_T20))
                            or ((eModel == SRP_MODEL.G_P_S_BLK_I_I_A_G_S_P_M_04_A))
                        )
                        or ((eModel == SRP_MODEL.G_P_S_BLK_I_I_A_G_S_P_M_04_AE))
                    )
                    or ((eModel == SRP_MODEL.G_P_S_BLK_I_I_R_AERO_T30))
                )
                or ((eModel == SRP_MODEL.G_P_S_BLK_I_I_R_G_S_P_M_04_A))
            ) or ((eModel == SRP_MODEL.G_P_S_BLK_I_I_R_G_S_P_M_04_AE)):
                oGPSSRP: "ISRPModelGPS" = clr.CastAs(oSrpModel.model, ISRPModelGPS)
                Assert.assertIsNotNone(oGPSSRP)
                oGPSSRP.scale = -100
                Assert.assertEqual(-100, oGPSSRP.scale)
                oGPSSRP.scale = 100
                Assert.assertEqual(100, oGPSSRP.scale)
                oGPSSRP.y_bias = 0
                Assert.assertEqual(0, oGPSSRP.y_bias)
                oGPSSRP.y_bias = 1000000000000000000000000000000.0
                Assert.assertEqual(1000000000000000000000000000000.0, oGPSSRP.y_bias)
                type2: "SRP_MODEL" = oGPSSRP.type

                def action155():
                    oGPSSRP.scale = -101

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action155)

                def action156():
                    oGPSSRP.scale = 101

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action156)

                def action157():
                    oGPSSRP.y_bias = -1

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action157)

                def action158():
                    oGPSSRP.y_bias = 10000000000000000000000000000000.0

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action158)

            i += 1

        oSrpModel.set_model_type(SRP_MODEL.SPHERICAL)

        def action159():
            oSrpModel.set_model_type(SRP_MODEL.UNKNOWN)

        TryCatchAssertBlock.DoAssert("Should not have allowed setting invalid SRP model.", action159)
        self.m_logger.WriteLine("***************** END OF SRP MODELS ***********")

    # endregion

    # region Drag
    def Drag(self, oDrag: "IVehicleHPOPForceModelDrag"):
        Assert.assertIsNotNone(oDrag)
        # Use (false)
        self.m_logger.WriteLine4("\tThe current Use is: {0}", oDrag.use)
        oDrag.use = False
        self.m_logger.WriteLine4("\tThe new Use is: {0}", oDrag.use)
        Assert.assertEqual(False, oDrag.use)

        def action160():
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).cd = 5.6

        # Cd (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action160)

        def action161():
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio = 12.34

        # AreaMassRatio (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action161)

        def action162():
            oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.STANDARD_ATMOS_MODEL_1976

        # AtmosphericDensityModel (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action162)

        def action163():
            oDrag.set_solar_flux_geo_magnitude_type(
                VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
            )

        # SetSolarFluxGeoMagType (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action163)

        def action164():
            oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS00

        # LowAltAtmosphericDensityModel
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action164)

        def action165():
            oDrag.blending_range = 20

        # BlendingRange
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action165)
        if (
            oDrag.solar_flux_geo_magnitude_type
            == VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        ):
            self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, True)
        else:
            self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, True)

        # Use (true)
        oDrag.use = True
        self.m_logger.WriteLine4("\tThe new Use is: {0}", oDrag.use)
        Assert.assertEqual(True, oDrag.use)

        # Cd

        (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).cd = -1.24
        self.m_logger.WriteLine6(
            "\tThe new Cd is: {0}", (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).cd
        )
        Assert.assertEqual(-1.24, (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).cd)

        def action166():
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).cd = 120.34

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action166)

        def action167():
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).cd = 120.34

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action167)

        # AreaMassRatio
        self.m_logger.WriteLine6(
            "\tThe current AreaMassRatio is: {0}",
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio,
        )
        (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio = 123
        self.m_logger.WriteLine6(
            "\tThe new AreaMassRatio is: {0}",
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio,
        )
        Assert.assertEqual(123, (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio)

        (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio = 124
        self.m_logger.WriteLine6(
            "\tThe new AreaMassRatio is: {0}",
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio,
        )
        Assert.assertEqual(124, (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio)

        def action168():
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio = -12.34

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action168)

        def action169():
            (clr.Convert((oDrag.drag_model), IVehicleHPOPDragModelSpherical)).area_mass_ratio = -12.34

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action169)

        oDrag.set_drag_model_type(DRAG_MODEL.PLUGIN)
        Assert.assertEqual(DRAG_MODEL.PLUGIN, oDrag.drag_model_type)

        self.m_logger.WriteLine6("\tThe current AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)

        def action170():
            oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.EXPONENTIAL_MODEL

        # AtmosphericDensityModel (eExponentialModel)
        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action170)

        def action171():
            oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.USER_DEFINED

        # AtmosphericDensityModel (eUserDefined)
        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action171)

        def action172():
            oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.UNKNOWN_DENS_MODEL

        # AtmosphericDensityModel (eUnknownDensModel)
        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action172)

        # AtmosphericDensityModel (eCira72)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.CIRA72
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.CIRA72, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (eHarrisPriester)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.HARRIS_PRIESTER
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.HARRIS_PRIESTER, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (eJacchia60)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.JACCHIA60
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.JACCHIA60, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)

        def action173():
            oDrag.set_solar_flux_geo_magnitude_type(
                VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
            )

        # SetSolarFluxGeoMagType (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action173)
        if (
            oDrag.solar_flux_geo_magnitude_type
            == VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        ):
            self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, True)
        else:
            self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, True)

        # AtmosphericDensityModel (eJacchia70)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.JACCHIA70
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.JACCHIA70, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (eJacchia71)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.JACCHIA71
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.JACCHIA71, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (eJacchiaRoberts)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.JACCHIA_ROBERTS
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.JACCHIA_ROBERTS, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (eMSIS00)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS00
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.MSIS00, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (eMSIS86)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS86
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.MSIS86, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (eMSIS90)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS90
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.MSIS90, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (eDTM2012)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.DTM2012
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.DTM2012, oDrag.atmospheric_density_model)
        # SolarFluxGeoMagType
        self.m_logger.WriteLine6("\t\tThe current SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        # SetSolarFluxGeoMagType (Manually)
        oDrag.set_solar_flux_geo_magnitude_type(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        )
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY,
            oDrag.solar_flux_geo_magnitude_type,
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        # SetSolarFluxGeoMagType (File)
        oDrag.set_solar_flux_geo_magnitude_type(VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE)
        self.m_logger.WriteLine6("\t\tThe new SolarFluxGeoMagType is: {0}", oDrag.solar_flux_geo_magnitude_type)
        Assert.assertEqual(
            VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_USE_FILE, oDrag.solar_flux_geo_magnitude_type
        )
        # SolarFluxGeoMag
        self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # AtmosphericDensityModel (e1976StandardAtmosModel)
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.STANDARD_ATMOS_MODEL_1976
        self.m_logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.STANDARD_ATMOS_MODEL_1976, oDrag.atmospheric_density_model)

        def action174():
            oDrag.set_solar_flux_geo_magnitude_type(
                VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
            )

        # SetSolarFluxGeoMagType (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action174)
        if (
            oDrag.solar_flux_geo_magnitude_type
            == VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE.SOLAR_FLUX_GEO_MAGNITUDE_ENTER_MANUALLY
        ):
            self.SolarFluxGeoMagEnterManually(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)
        else:
            self.SolarFluxGeoMagUseFile(oDrag.solar_flux_geo_magnitude, oDrag.atmospheric_density_model, False)

        # LowAltAtmosphericDensityModel (eUnknownDensModel)
        oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.UNKNOWN_DENS_MODEL
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.UNKNOWN_DENS_MODEL, oDrag.low_altitude_atmospheric_density_model)
        self.m_logger.WriteLine6(
            "\tThe new LowAltAtmosphericDensityModel is: {0}", oDrag.low_altitude_atmospheric_density_model
        )

        def action175():
            oDrag.blending_range = 50.0

        TryCatchAssertBlock.DoAssert("Should not allow to set an read-only.", action175)

        # LowAltAtmosphericDensityModel (eMSIS90)
        oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS90
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.MSIS90, oDrag.low_altitude_atmospheric_density_model)
        self.m_logger.WriteLine6(
            "\tThe new LowAltAtmosphericDensityModel is: {0}", oDrag.low_altitude_atmospheric_density_model
        )
        self.m_logger.WriteLine6("\t\tThe current BlendingRange is: {0}", oDrag.blending_range)
        # BlendingRange
        oDrag.blending_range = 50.0
        self.m_logger.WriteLine6("\t\tThe new BlendingRange is: {0}", oDrag.blending_range)

        # LowAltAtmosphericDensityModel (eMSIS00)
        oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS00
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.MSIS00, oDrag.low_altitude_atmospheric_density_model)
        self.m_logger.WriteLine6(
            "\tThe new LowAltAtmosphericDensityModel is: {0}", oDrag.low_altitude_atmospheric_density_model
        )
        self.m_logger.WriteLine6("\t\tThe current BlendingRange is: {0}", oDrag.blending_range)
        # BlendingRange
        oDrag.blending_range = 30.0
        self.m_logger.WriteLine6("\t\tThe new BlendingRange is: {0}", oDrag.blending_range)
        # Reset LowAltAtmosphericDensityModel
        oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.UNKNOWN_DENS_MODEL

        # LowAltAtmosDensityModel (eUnknownDensModel)
        oDrag.low_altitude_atmos_density_model = LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_NONE
        Assert.assertEqual(
            LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_NONE, oDrag.low_altitude_atmos_density_model
        )
        self.m_logger.WriteLine6("\tThe new LowAltAtmosDensityModel is: {0}", oDrag.low_altitude_atmos_density_model)

        def action176():
            oDrag.blending_range = 50.0

        TryCatchAssertBlock.DoAssert("Should not allow to set an read-only.", action176)

        # LowAltAtmosDensityModel (eMSIS90)
        oDrag.low_altitude_atmos_density_model = LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_MSISE1990
        Assert.assertEqual(
            LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_MSISE1990, oDrag.low_altitude_atmos_density_model
        )
        self.m_logger.WriteLine6("\tThe new LowAltAtmosDensityModel is: {0}", oDrag.low_altitude_atmos_density_model)
        self.m_logger.WriteLine6("\t\tThe current BlendingRange is: {0}", oDrag.blending_range)
        # BlendingRange
        oDrag.blending_range = 50.0
        self.m_logger.WriteLine6("\t\tThe new BlendingRange is: {0}", oDrag.blending_range)

        # LowAltAtmosDensityModel (eMSIS00)
        oDrag.low_altitude_atmos_density_model = LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_NRLMSISE2000
        Assert.assertEqual(
            LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_NRLMSISE2000, oDrag.low_altitude_atmos_density_model
        )
        self.m_logger.WriteLine6("\tThe new LowAltAtmosDensityModel is: {0}", oDrag.low_altitude_atmos_density_model)
        self.m_logger.WriteLine6("\t\tThe current BlendingRange is: {0}", oDrag.blending_range)
        # BlendingRange
        oDrag.blending_range = 30.0
        self.m_logger.WriteLine6("\t\tThe new BlendingRange is: {0}", oDrag.blending_range)
        # Reset LowAltAtmosDensityModel
        oDrag.low_altitude_atmos_density_model = LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_NONE
        Assert.assertEqual(
            LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_NONE, oDrag.low_altitude_atmos_density_model
        )

        # LowAltAtmosphericDensityModel
        # Try to set to equivalent of "None"
        oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.UNKNOWN_DENS_MODEL
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.UNKNOWN_DENS_MODEL, oDrag.low_altitude_atmospheric_density_model)

        def action177():
            oDrag.blending_range = 30

        # If None above, then shouldn't be able to set the Blending Range
        TryCatchAssertBlock.ExpectedException("read only", action177)

        oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS00
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.MSIS00, oDrag.low_altitude_atmospheric_density_model)
        oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS90
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.MSIS90, oDrag.low_altitude_atmospheric_density_model)

        def action178():
            oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.CIRA72

        TryCatchAssertBlock.ExpectedException("must be in", action178)

        # BlendingRange
        oDrag.blending_range = 30
        Assert.assertEqual(30, oDrag.blending_range)
        oDrag.blending_range = 40
        Assert.assertEqual(40, oDrag.blending_range)

        # Testing new drag models
        self.m_logger.WriteLine("***************** DRAG MODELS ***********")
        # IVehicleHPOPDragModel oDragModel = oDrag.DragModel;
        oDrag.set_drag_model_type(DRAG_MODEL.SPHERICAL)
        Assert.assertEqual(DRAG_MODEL.SPHERICAL, oDrag.drag_model_type)
        oDragModelChoices = oDrag.drag_model_supported_types
        Assert.assertIsNotNone(oDragModelChoices)

        i: int = 0
        while i < len(oDragModelChoices):
            eModel: "DRAG_MODEL" = clr.Convert(int(oDragModelChoices[i][0]), DRAG_MODEL)
            self.m_logger.WriteLine6("Drag Model: {0}", eModel)
            oDrag.set_drag_model_type(eModel)
            Assert.assertEqual(eModel, oDrag.drag_model_type)
            Assert.assertTrue(oDrag.is_drag_model_type_supported(eModel))
            if eModel == DRAG_MODEL.SPHERICAL:
                oSphericalDrag: "IVehicleHPOPDragModelSpherical" = clr.CastAs(
                    oDrag.drag_model, IVehicleHPOPDragModelSpherical
                )
                Assert.assertIsNotNone(oSphericalDrag)

                oSphericalDrag.area_mass_ratio = 9999.0
                Assert.assertEqual(9999.0, oSphericalDrag.area_mass_ratio)

                oSphericalDrag.cd = 99
                Assert.assertEqual(99, oSphericalDrag.cd)

                def action179():
                    oSphericalDrag.cd = -101

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action179)

                def action180():
                    oSphericalDrag.cd = 101

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action180)

                def action181():
                    oSphericalDrag.area_mass_ratio = 10000

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action181)

                def action182():
                    oSphericalDrag.area_mass_ratio = -1

                TryCatchAssertBlock.DoAssert("Should have thrown 'Out of range' exception.", action182)

            i += 1

        oDrag.set_drag_model_type(DRAG_MODEL.SPHERICAL)

        def action183():
            oDrag.set_drag_model_type(DRAG_MODEL.UNKNOWN)

        TryCatchAssertBlock.DoAssert("Should not have allowed setting invalid Drag model.", action183)
        self.m_logger.WriteLine("***************** END OF Drag MODELS ***********")

    # endregion

    # region SolarFluxGeoMagEnterManually
    def SolarFluxGeoMagEnterManually(
        self, oSolar: "IVehicleSolarFluxGeoMagnitude", eModel: "ATMOSPHERIC_DENSITY_MODEL", bReadOnly: bool
    ):
        Assert.assertIsNotNone(oSolar)
        oManually: "IVehicleSolarFluxGeoMagnitudeEnterManually" = clr.CastAs(
            oSolar, IVehicleSolarFluxGeoMagnitudeEnterManually
        )
        Assert.assertIsNotNone(oManually)
        if (bReadOnly or (eModel == ATMOSPHERIC_DENSITY_MODEL.STANDARD_ATMOS_MODEL_1976)) or (
            eModel == ATMOSPHERIC_DENSITY_MODEL.JACCHIA60
        ):

            def action184():
                oManually.daily_f107 = 123.4

            # DailyF107
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action184)

            def action185():
                oManually.average_f107 = 123.4

            # AverageF107
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action185)

            def action186():
                oManually.geomagnetic_index = 1.234

            # GeomagneticIndex
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action186)

        else:
            # AverageF107
            self.m_logger.WriteLine6("\t\tThe current AverageF107 is: {0}", oManually.average_f107)
            oManually.average_f107 = 123.4
            self.m_logger.WriteLine6("\t\tThe new AverageF107 is: {0}", oManually.average_f107)
            Assert.assertEqual(123.4, oManually.average_f107)

            def action187():
                oManually.average_f107 = 12345.6

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action187)
            if eModel == ATMOSPHERIC_DENSITY_MODEL.HARRIS_PRIESTER:

                def action188():
                    oManually.daily_f107 = 123.4

                # DailyF107
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action188)

                def action189():
                    oManually.geomagnetic_index = 1.234

                # GeomagneticIndex
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action189)
            elif (
                (
                    (
                        (
                            (
                                (
                                    ((eModel == ATMOSPHERIC_DENSITY_MODEL.CIRA72))
                                    or ((eModel == ATMOSPHERIC_DENSITY_MODEL.JACCHIA70))
                                )
                                or ((eModel == ATMOSPHERIC_DENSITY_MODEL.JACCHIA71))
                            )
                            or ((eModel == ATMOSPHERIC_DENSITY_MODEL.JACCHIA_ROBERTS))
                        )
                        or ((eModel == ATMOSPHERIC_DENSITY_MODEL.MSIS00))
                    )
                    or ((eModel == ATMOSPHERIC_DENSITY_MODEL.MSIS86))
                )
                or ((eModel == ATMOSPHERIC_DENSITY_MODEL.MSIS90))
            ) or ((eModel == ATMOSPHERIC_DENSITY_MODEL.DTM2012)):
                # DailyF107
                self.m_logger.WriteLine6("\t\tThe current DailyF107 is: {0}", oManually.daily_f107)
                oManually.daily_f107 = 123.4
                self.m_logger.WriteLine6("\t\tThe new DailyF107 is: {0}", oManually.daily_f107)
                Assert.assertEqual(123.4, oManually.daily_f107)

                def action190():
                    oManually.daily_f107 = 12345.6

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action190)
                # GeomagneticIndex
                self.m_logger.WriteLine6("\t\tThe current GeomagneticIndex is: {0}", oManually.geomagnetic_index)
                oManually.geomagnetic_index = 3.4
                self.m_logger.WriteLine6("\t\tThe new GeomagneticIndex is: {0}", oManually.geomagnetic_index)
                Assert.assertEqual(3.4, oManually.geomagnetic_index)

                def action191():
                    oManually.geomagnetic_index = 12.34

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action191)
            else:
                Assert.fail("Invalid AtmosphericDensityModel type!")

    # endregion

    # region SolarFluxGeoMagUseFile
    def SolarFluxGeoMagUseFile(
        self, oSolar: "IVehicleSolarFluxGeoMagnitude", eModel: "ATMOSPHERIC_DENSITY_MODEL", bReadOnly: bool
    ):
        Assert.assertIsNotNone(oSolar)
        oFile: "IVehicleSolarFluxGeoMagnitudeUseFile" = clr.CastAs(oSolar, IVehicleSolarFluxGeoMagnitudeUseFile)
        Assert.assertIsNotNone(oFile)
        if (bReadOnly or (eModel == ATMOSPHERIC_DENSITY_MODEL.STANDARD_ATMOS_MODEL_1976)) or (
            eModel == ATMOSPHERIC_DENSITY_MODEL.JACCHIA60
        ):

            def action192():
                oFile.file = r"DynamicEarthData\EOP-v1.1.txt"

            # File
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action192)

            def action193():
                oFile.geomag_flux_src = VEHICLE_GEOMAG_FLUX_SRC.READ_AP_FROM_FILE

            # GeomagFluxSrc
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action193)

            def action194():
                oFile.geomag_flux_update_rate = VEHICLE_GEOMAG_FLUX_UPDATE_RATE.DAILY

            # GeomagFluxUpdateRate
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action194)

        else:
            # GeomagFluxSrc
            self.m_logger.WriteLine6("\t\tThe current GeomagFluxSrc is: {0}", oFile.geomag_flux_src)
            oFile.geomag_flux_src = VEHICLE_GEOMAG_FLUX_SRC.READ_AP_FROM_FILE
            self.m_logger.WriteLine6("\t\tThe new GeomagFluxSrc is: {0}", oFile.geomag_flux_src)
            Assert.assertEqual(VEHICLE_GEOMAG_FLUX_SRC.READ_AP_FROM_FILE, oFile.geomag_flux_src)
            # GeomagFluxUpdateRate
            self.m_logger.WriteLine6("\t\tThe current GeomagFluxUpdateRate is: {0}", oFile.geomag_flux_update_rate)
            oFile.geomag_flux_update_rate = VEHICLE_GEOMAG_FLUX_UPDATE_RATE.DAILY
            self.m_logger.WriteLine6("\t\tThe new GeomagFluxUpdateRate is: {0}", oFile.geomag_flux_update_rate)
            Assert.assertEqual(VEHICLE_GEOMAG_FLUX_UPDATE_RATE.DAILY, oFile.geomag_flux_update_rate)
            # File
            self.m_logger.WriteLine5("\t\tThe current File is: {0}", oFile.file)
            if (
                (
                    (
                        (
                            (
                                (
                                    (
                                        ((eModel == ATMOSPHERIC_DENSITY_MODEL.HARRIS_PRIESTER))
                                        or ((eModel == ATMOSPHERIC_DENSITY_MODEL.CIRA72))
                                    )
                                    or ((eModel == ATMOSPHERIC_DENSITY_MODEL.JACCHIA70))
                                )
                                or ((eModel == ATMOSPHERIC_DENSITY_MODEL.JACCHIA71))
                            )
                            or ((eModel == ATMOSPHERIC_DENSITY_MODEL.JACCHIA_ROBERTS))
                        )
                        or ((eModel == ATMOSPHERIC_DENSITY_MODEL.MSIS00))
                    )
                    or ((eModel == ATMOSPHERIC_DENSITY_MODEL.MSIS86))
                )
                or ((eModel == ATMOSPHERIC_DENSITY_MODEL.MSIS90))
            ) or ((eModel == ATMOSPHERIC_DENSITY_MODEL.DTM2012)):
                oFile.file = r"EOP-v1.1.txt"
                Assert.assertEqual("EOP-v1.1.txt", oFile.file)

                oFile.file = r"DynamicEarthData\EOP-v1.1.txt"
                Assert.assertEqual("EOP-v1.1.txt", oFile.file)

                # BUG86710 oFile.File = @"BogusDir\EOP-v1.1.txt";  // This succeeds, but it should fail

                Assert.assertEqual("EOP-v1.1.txt", oFile.file)

                def action195():
                    oFile.file = ""

                TryCatchAssertBlock.ExpectedException("does not exist", action195)

                def action196():
                    oFile.file = "InvalidFile.Name"

                TryCatchAssertBlock.ExpectedException("does not exist", action196)
            else:
                Assert.fail("Invalid AtmosphericDensityModel type!")

    # endregion

    # region ThirdBodyGravity
    def ThirdBodyGravity(self, oGravity: "IVehicleThirdBodyGravityCollection"):
        Assert.assertIsNotNone(oGravity)
        # Count
        self.m_logger.WriteLine3("\tThe current ThirdBodyGravity collection contains: {0} elements.", oGravity.count)
        # _NewEnum
        thirdBodyGravityElement: "IVehicleThirdBodyGravityElement"
        # _NewEnum
        for thirdBodyGravityElement in oGravity:
            self.m_logger.WriteLine8(
                "\t\tElement: Name = {0}, Source = {1}, GravityValue = {2}",
                thirdBodyGravityElement.central_body,
                thirdBodyGravityElement.source,
                thirdBodyGravityElement.gravity_value,
            )

        # RemoveAll
        oGravity.remove_all()
        self.m_logger.WriteLine3("\tThe new ThirdBodyGravity collection contains: {0} elements.", oGravity.count)
        Assert.assertEqual(0, oGravity.count)
        # AvailableThirdBodies
        arBodies = oGravity.available_third_body_names
        self.m_logger.WriteLine3("\tAvailable {0} ThirdBodies.", Array.Length(arBodies))

        iIndex: int = 0
        while iIndex < Array.Length(arBodies):
            centralBody: str = clr.Convert(arBodies[iIndex], str)
            self.m_logger.WriteLine7("\t\tBody {0}: {1}", iIndex, centralBody)
            # Add
            thirdBodyGravityElement: "IVehicleThirdBodyGravityElement" = oGravity.add_third_body(centralBody)
            Assert.assertIsNotNone(thirdBodyGravityElement)
            self.m_logger.WriteLine8(
                "\t\t\tAdded: Name = {0}, Source = {1}, GravityValue = {2}",
                thirdBodyGravityElement.central_body,
                thirdBodyGravityElement.source,
                thirdBodyGravityElement.gravity_value,
            )
            gravValue: float = thirdBodyGravityElement.gravity_value
            thirdBodyGravityElement.source = THIRD_BODY_GRAV_SOURCE_TYPE.HPOP_HISTORICAL
            Assert.assertFalse((gravValue == thirdBodyGravityElement.gravity_value))

            def action197():
                oGravity.add_third_body(centralBody)

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action197)

            iIndex += 1

        oGravity.remove_all()
        # AvailableThirdBodyNames
        arrBodyNames = oGravity.available_third_body_names
        centralBody: str
        for centralBody in arrBodyNames:
            thirdBodyGravityElement: "IVehicleThirdBodyGravityElement" = oGravity.add_third_body(centralBody)
            Assert.assertIsNotNone(thirdBodyGravityElement)
            Assert.assertEqual(thirdBodyGravityElement.central_body, centralBody)
            self.m_logger.WriteLine8(
                "\t\t\tAdded: CentralBody = {0}, Source = {1}, GravityValue = {2}",
                thirdBodyGravityElement.central_body,
                thirdBodyGravityElement.source,
                thirdBodyGravityElement.gravity_value,
            )
            gravValue: float = thirdBodyGravityElement.gravity_value
            thirdBodyGravityElement.source = THIRD_BODY_GRAV_SOURCE_TYPE.HPOP_HISTORICAL
            Assert.assertFalse((gravValue == thirdBodyGravityElement.gravity_value))

            def action198():
                oGravity.add_third_body(centralBody)

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action198)

        self.m_logger.WriteLine3("\tThe new ThirdBodyGravity collection contains: {0} elements.", oGravity.count)
        Assert.assertEqual(Array.Length(arBodies), oGravity.count)
        # Item
        oBody: "IVehicleThirdBodyGravityElement" = oGravity[0]
        Assert.assertIsNotNone(oBody)
        # Source (eCBFile)
        oBody.source = THIRD_BODY_GRAV_SOURCE_TYPE.CB_FILE

        def action199():
            oBody.gravity_value = 123.456

        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action199)
        self.m_logger.WriteLine8(
            "\t\tUpdated: Name = {0}, Source = {1}, GravityValue = {2}",
            oBody.central_body,
            oBody.source,
            oBody.gravity_value,
        )
        # Source (eHPOPHistorical)
        oBody.source = THIRD_BODY_GRAV_SOURCE_TYPE.HPOP_HISTORICAL

        def action200():
            oBody.gravity_value = 123.456

        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action200)
        self.m_logger.WriteLine8(
            "\t\tUpdated: Name = {0}, Source = {1}, GravityValue = {2}",
            oBody.central_body,
            oBody.source,
            oBody.gravity_value,
        )
        # Source (eJPLDE)
        oBody.source = THIRD_BODY_GRAV_SOURCE_TYPE.JPLDE

        def action201():
            oBody.gravity_value = 123.456

        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action201)
        self.m_logger.WriteLine8(
            "\t\tUpdated: Name = {0}, Source = {1}, GravityValue = {2}",
            oBody.central_body,
            oBody.source,
            oBody.gravity_value,
        )
        # Source (eUserSpecified)
        oBody.source = THIRD_BODY_GRAV_SOURCE_TYPE.USER_SPECIFIED
        oBody.gravity_value = 123.456
        Assert.assertEqual(123.456, oBody.gravity_value)

        def action202():
            oBody.gravity_value = -123.456

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action202)
        self.m_logger.WriteLine8(
            "\t\tUpdated: Name = {0}, Source = {1}, GravityValue = {2}",
            oBody.central_body,
            oBody.source,
            oBody.gravity_value,
        )

        # RemoveAt
        oGravity.remove_at(0)
        self.m_logger.WriteLine3("\tThe new ThirdBodyGravity collection contains: {0} elements.", oGravity.count)
        Assert.assertEqual((Array.Length(arBodies) - 1), oGravity.count)
        # RemoveByType
        centralBody1: str = oGravity[1].central_body
        oGravity.remove_third_body(centralBody1)
        self.m_logger.WriteLine3("\tThe new ThirdBodyGravity collection contains: {0} elements.", oGravity.count)
        Assert.assertEqual((Array.Length(arBodies) - 2), oGravity.count)

        def action203():
            oGravity.remove_third_body(centralBody1)

        TryCatchAssertBlock.DoAssert("Should not allow to remove an invalid element.", action203)
        # Remove by name
        oGravity.remove_third_body(oGravity[1].central_body)
        self.m_logger.WriteLine3("\tThe new ThirdBodyGravity collection contains: {0} elements.", oGravity.count)
        Assert.assertEqual((Array.Length(arBodies) - 3), oGravity.count)
        # RemoveAll
        oGravity.remove_all()
        self.m_logger.WriteLine3("\tThe new ThirdBodyGravity collection contains: {0} elements.", oGravity.count)
        Assert.assertEqual(0, oGravity.count)

    # endregion

    # region MoreOptions
    def MoreOptions(self, oMore: "IVehicleHPOPForceModelMoreOptions"):
        Assert.assertIsNotNone(oMore)
        # Drag
        self.MoreOptionsDrag(oMore.drag)
        # SolarRadiationPressure
        self.MoreOptionsSolarRadiationPressure(oMore.solar_radiation_pressure)
        # Static
        self.MoreOptionsStatic(oMore.static)
        # SolidTides
        self.MoreOptionsSolidTides(oMore.solid_tides)
        # OceanTides
        self.MoreOptionsOceanTides(oMore.ocean_tides)
        # RadiationPressure
        self.MoreOptionsRadiationPressure(oMore.radiation_pressure)
        self.MoreOptionsPluginPropagator(oMore.plugin_propagator)

    # endregion

    # region MoreOptionsPluginPropagator
    def MoreOptionsPluginPropagator(self, oPlugin: "IVehiclePluginPropagator"):
        Assert.assertIsNotNone(oPlugin)
        # UsePlugin (false)
        self.m_logger.WriteLine4("\tThe current UsePlugin is: {0}", oPlugin.use_plugin)
        oPlugin.use_plugin = False
        self.m_logger.WriteLine4("\tThe new UsePlugin is: {0}", oPlugin.use_plugin)
        Assert.assertFalse(oPlugin.use_plugin)

        def action204():
            oPlugin.plugin_name = "bogus name"

        # PluginName (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action204)
        # UsePlugin (true)
        oPlugin.use_plugin = True
        self.m_logger.WriteLine4("\tThe new UsePlugin is: {0}", oPlugin.use_plugin)
        Assert.assertTrue(oPlugin.use_plugin)
        # PluginName
        self.m_logger.WriteLine5("\tThe current PluginName is: {0}", oPlugin.plugin_name)

        def action205():
            oPlugin.plugin_name = "bogus name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action205)

        def action206():
            oPlugin.plugin_name = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action206)
        # AvailablePlugins
        arPlugins = oPlugin.available_plugins
        self.m_logger.WriteLine3("\tNow available {0} plugins:", Array.Length(arPlugins))
        strPluginName: str
        for strPluginName in arPlugins:
            # PluginName
            oPlugin.plugin_name = strPluginName
            self.m_logger.WriteLine5("\tThe new PluginName is: {0}", oPlugin.plugin_name)
            Assert.assertEqual(strPluginName, oPlugin.plugin_name)
            # PluginSettings
            oSettings: "IVehiclePluginSettings" = oPlugin.plugin_settings
            Assert.assertIsNotNone(oSettings)
            # AvailableProperties
            arProperties = oSettings.available_properties
            self.m_logger.WriteLine7(
                "\t\tThe {0} propagator has {1} properties:", oPlugin.plugin_name, Array.Length(arProperties)
            )
            strPropertyName: str
            for strPropertyName in arProperties:
                # GetProperty
                self.m_logger.WriteLine7(
                    "\t\t\tProperty: Name = {0}, Value = {1}", strPropertyName, oSettings.get_property(strPropertyName)
                )
                o: typing.Any = oSettings.get_property(strPropertyName)

            # GetRawPluginObject
            oRawPluginObject: typing.Any = oPlugin.get_raw_plugin_object()
            Assert.assertIsNotNone(oRawPluginObject)

        # ApplyPluginChanges
        oPlugin.apply_plugin_changes()

    # endregion

    # region MoreOptionsDrag
    def MoreOptionsDrag(self, oDrag: "IVehicleHPOPForceModelDragOptions"):
        Assert.assertIsNotNone(oDrag)
        # UseApproxAlt
        self.m_logger.WriteLine4("\tThe current UseApproxAlt is: {0}", oDrag.use_approx_altitude)
        oDrag.use_approx_altitude = False
        self.m_logger.WriteLine4("\tThe new UseApproxAlt is: {0}", oDrag.use_approx_altitude)
        Assert.assertEqual(False, oDrag.use_approx_altitude)
        oDrag.use_approx_altitude = True
        self.m_logger.WriteLine4("\tThe new UseApproxAlt is: {0}", oDrag.use_approx_altitude)
        Assert.assertEqual(True, oDrag.use_approx_altitude)
        # UseApparentSunPosition
        self.m_logger.WriteLine4("\tThe current UseApparentSunPosition is: {0}", oDrag.use_apparent_sun_position)
        oDrag.use_apparent_sun_position = False
        self.m_logger.WriteLine4("\tThe new UseApparentSunPosition is: {0}", oDrag.use_apparent_sun_position)
        Assert.assertEqual(False, oDrag.use_apparent_sun_position)
        oDrag.use_apparent_sun_position = True
        self.m_logger.WriteLine4("\tThe new UseApparentSunPosition is: {0}", oDrag.use_apparent_sun_position)
        Assert.assertEqual(True, oDrag.use_apparent_sun_position)

    # endregion

    # region MoreOptionsSolarRadiationPressure
    def MoreOptionsSolarRadiationPressure(self, oOptions: "IVehicleHPOPSolarRadiationPressureOptions"):
        Assert.assertIsNotNone(oOptions)
        # MethodToComputeSunPosition
        self.m_logger.WriteLine6(
            "\tThe current MethodToComputeSunPosition is: {0}", oOptions.method_to_compute_sun_position
        )
        oOptions.method_to_compute_sun_position = METHOD_TO_COMPUTE_SUN_POSITION.MTCSP_APPARENT
        self.m_logger.WriteLine6(
            "\tThe new MethodToComputeSunPosition is: {0}", oOptions.method_to_compute_sun_position
        )
        Assert.assertEqual(METHOD_TO_COMPUTE_SUN_POSITION.MTCSP_APPARENT, oOptions.method_to_compute_sun_position)
        oOptions.method_to_compute_sun_position = METHOD_TO_COMPUTE_SUN_POSITION.MTCSP_APPARENT_TO_TRUE_CB
        self.m_logger.WriteLine6(
            "\tThe new MethodToComputeSunPosition is: {0}", oOptions.method_to_compute_sun_position
        )
        Assert.assertEqual(
            METHOD_TO_COMPUTE_SUN_POSITION.MTCSP_APPARENT_TO_TRUE_CB, oOptions.method_to_compute_sun_position
        )
        oOptions.method_to_compute_sun_position = METHOD_TO_COMPUTE_SUN_POSITION.MTCSP_TRUE
        self.m_logger.WriteLine6(
            "\tThe new MethodToComputeSunPosition is: {0}", oOptions.method_to_compute_sun_position
        )
        Assert.assertEqual(METHOD_TO_COMPUTE_SUN_POSITION.MTCSP_TRUE, oOptions.method_to_compute_sun_position)
        # AtmosAltOfEarthShapeForEclipse
        self.m_logger.WriteLine6(
            "\tThe current AtmosAltOfEarthShapeForEclipse is: {0}", oOptions.atmos_altitude_of_earth_shape_for_eclipse
        )
        oOptions.atmos_altitude_of_earth_shape_for_eclipse = 12.34
        self.m_logger.WriteLine6(
            "\tThe new AtmosAltOfEarthShapeForEclipse is: {0}", oOptions.atmos_altitude_of_earth_shape_for_eclipse
        )
        Assert.assertEqual(12.34, oOptions.atmos_altitude_of_earth_shape_for_eclipse)

        def action207():
            oOptions.atmos_altitude_of_earth_shape_for_eclipse = -1234.5

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action207)

    # endregion

    # region MoreOptionsStatic
    def MoreOptionsStatic(self, oOptions: "IVehicleStatic"):
        Assert.assertIsNotNone(oOptions)
        # IncRelativisticAcc
        self.m_logger.WriteLine4("\tThe current IncRelativisticAcc is: {0}", oOptions.inc_relativistic_acc)
        oOptions.inc_relativistic_acc = False
        self.m_logger.WriteLine4("\tThe new IncRelativisticAcc is: {0}", oOptions.inc_relativistic_acc)
        Assert.assertEqual(False, oOptions.inc_relativistic_acc)
        oOptions.inc_relativistic_acc = True
        self.m_logger.WriteLine4("\tThe new IncRelativisticAcc is: {0}", oOptions.inc_relativistic_acc)
        Assert.assertEqual(True, oOptions.inc_relativistic_acc)
        # SatelliteMass
        self.m_logger.WriteLine6("\tThe current SatelliteMass is: {0}", oOptions.satellite_mass)
        oOptions.satellite_mass = 123.456
        self.m_logger.WriteLine6("\tThe new SatelliteMass is: {0}", oOptions.satellite_mass)
        Assert.assertEqual(123.456, oOptions.satellite_mass)

        def action208():
            oOptions.satellite_mass = -123.456

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action208)

    # endregion

    # region MoreOptionsSolidTides
    def MoreOptionsSolidTides(self, oOptions: "IVehicleSolidTides"):
        Assert.assertIsNotNone(oOptions)
        # IncTimeDepSolidTides (false)
        self.m_logger.WriteLine4("\tThe current IncTimeDepSolidTides is: {0}", oOptions.inc_time_dep_solid_tides)
        oOptions.inc_time_dep_solid_tides = False
        self.m_logger.WriteLine4("\tThe new IncTimeDepSolidTides is: {0}", oOptions.inc_time_dep_solid_tides)
        Assert.assertEqual(False, oOptions.inc_time_dep_solid_tides)

        def action209():
            oOptions.min_amplitude = 0.123

        # MinAmplitude (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action209)
        # IncTimeDepSolidTides (true)
        oOptions.inc_time_dep_solid_tides = True
        self.m_logger.WriteLine4("\tThe new IncTimeDepSolidTides is: {0}", oOptions.inc_time_dep_solid_tides)
        Assert.assertEqual(True, oOptions.inc_time_dep_solid_tides)
        # MinAmplitude
        self.m_logger.WriteLine6("\tThe current MinAmplitude is: {0}", oOptions.min_amplitude)
        oOptions.min_amplitude = 0.123
        self.m_logger.WriteLine6("\tThe new MinAmplitude is: {0}", oOptions.min_amplitude)
        Assert.assertEqual(0.123, oOptions.min_amplitude)

        def action210():
            oOptions.min_amplitude = -123.456

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action210)
        # TruncateSolidTides
        oOptions.truncate_solid_tides = False
        self.m_logger.WriteLine4("\tThe new TruncateSolidTides is: {0}", oOptions.truncate_solid_tides)
        Assert.assertEqual(False, oOptions.truncate_solid_tides)
        oOptions.truncate_solid_tides = True
        self.m_logger.WriteLine4("\tThe new TruncateSolidTides is: {0}", oOptions.truncate_solid_tides)
        Assert.assertEqual(True, oOptions.truncate_solid_tides)

    # endregion

    # region MoreOptionsOceanTides
    def MoreOptionsOceanTides(self, oOptions: "IVehicleOceanTides"):
        Assert.assertIsNotNone(oOptions)
        # MaxDegree
        self.m_logger.WriteLine3("\tThe current MaxDegree is: {0}", oOptions.max_degree)
        oOptions.max_degree = 23
        self.m_logger.WriteLine3("\tThe new MaxDegree is: {0}", oOptions.max_degree)
        Assert.assertEqual(23, oOptions.max_degree)

        def action211():
            oOptions.max_degree = -1

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action211)
        # MaxOrder
        self.m_logger.WriteLine3("\tThe current MaxOrder is: {0}", oOptions.max_order)
        oOptions.max_order = 12
        self.m_logger.WriteLine3("\tThe new MaxOrder is: {0}", oOptions.max_order)
        Assert.assertEqual(12, oOptions.max_order)

        def action212():
            oOptions.max_order = 26

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action212)
        # MinAmplitude
        self.m_logger.WriteLine6("\tThe current MinAmplitude is: {0}", oOptions.min_amplitude)
        oOptions.min_amplitude = 0.123
        self.m_logger.WriteLine6("\tThe new MinAmplitude is: {0}", oOptions.min_amplitude)
        Assert.assertEqual(0.123, oOptions.min_amplitude)

        def action213():
            oOptions.min_amplitude = -123.456

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action213)

    # endregion

    # region MoreOptionsRadiationPressure
    def MoreOptionsRadiationPressure(self, oOptions: "IVehicleRadiationPressure"):
        Assert.assertIsNotNone(oOptions)
        # IncludeAlbedo (false)
        self.m_logger.WriteLine4("\tThe current IncludeAlbedo is: {0}", oOptions.include_albedo)
        oOptions.include_albedo = False
        self.m_logger.WriteLine4("\tThe new IncludeAlbedo is: {0}", oOptions.include_albedo)
        Assert.assertEqual(False, oOptions.include_albedo)
        # IncludeThermal (false)
        self.m_logger.WriteLine4("\tThe current IncludeThermal is: {0}", oOptions.include_thermal)
        oOptions.include_thermal = False
        self.m_logger.WriteLine4("\tThe new IncludeThermal is: {0}", oOptions.include_thermal)
        Assert.assertEqual(False, oOptions.include_thermal)

        def action214():
            oOptions.ck = 12.34

        # Ck
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action214)

        def action215():
            oOptions.area_mass_ratio = 12.34

        # AreaMassRatio
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action215)

        def action216():
            oOptions.file = "JGM3.grv"

        # File
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action216)
        # IncludeAlbedo (true)
        oOptions.include_albedo = True
        self.m_logger.WriteLine4("\tThe new IncludeAlbedo is: {0}", oOptions.include_albedo)
        Assert.assertEqual(True, oOptions.include_albedo)
        # IncludeThermal (true)
        oOptions.include_thermal = True
        self.m_logger.WriteLine4("\tThe new IncludeThermal is: {0}", oOptions.include_thermal)
        Assert.assertEqual(True, oOptions.include_thermal)
        # Ck
        self.m_logger.WriteLine6("\tThe current Ck is: {0}", oOptions.ck)
        oOptions.ck = 23
        self.m_logger.WriteLine6("\tThe new Ck is: {0}", oOptions.ck)
        Assert.assertEqual(23, oOptions.ck)

        def action217():
            oOptions.ck = -1234

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action217)
        # AreaMassRatio
        self.m_logger.WriteLine6("\tThe current AreaMassRatio is: {0}", oOptions.area_mass_ratio)
        oOptions.area_mass_ratio = 12
        self.m_logger.WriteLine6("\tThe new AreaMassRatio is: {0}", oOptions.area_mass_ratio)
        Assert.assertEqual(12, oOptions.area_mass_ratio)

        def action218():
            oOptions.area_mass_ratio = -26

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action218)
        # File
        self.m_logger.WriteLine5("\tThe current File is: {0}", oOptions.file)
        oOptions.file = r"STKData\CentralBodies\Earth\JGM3.grv"
        self.m_logger.WriteLine5("\tThe new File is: {0}", oOptions.file)
        Assert.assertEqual(TestBase.PathCombine("STKData", "CentralBodies", "Earth", "JGM3.grv"), oOptions.file)

        def action219():
            oOptions.file = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action219)

        def action220():
            oOptions.file = "InvalidFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action220)

    # endregion

    # region Integrator
    def Integrator(self, oIntegrator: "IVehicleIntegrator", oCovariance: "IVehicleCovariance"):
        Assert.assertIsNotNone(oIntegrator)
        # DoNotPropagateBelowAlt
        self.m_logger.WriteLine6(
            "\tThe current DoNotPropagateBelowAlt is: {0}", oIntegrator.do_not_propagate_below_altitude
        )
        oIntegrator.do_not_propagate_below_altitude = 123.45
        self.m_logger.WriteLine6(
            "\tThe new DoNotPropagateBelowAlt is: {0}", oIntegrator.do_not_propagate_below_altitude
        )
        Assert.assertEqual(123.45, oIntegrator.do_not_propagate_below_altitude)

        def action221():
            oIntegrator.do_not_propagate_below_altitude = 12345.6

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action221)
        # TimeRegularization
        oTime: "IVehicleTimeRegularization" = oIntegrator.time_regularization
        Assert.assertIsNotNone(oTime)
        # Use (false)
        self.m_logger.WriteLine4("\tThe current Use is: {0}", oTime.use)
        oTime.use = False
        self.m_logger.WriteLine4("\tThe new Use is: {0}", oTime.use)
        Assert.assertEqual(False, oTime.use)

        def action222():
            oTime.exponent = 2.34

        # Exponent
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action222)

        def action223():
            oTime.steps_per_orbit = 1234

        # StepsPerOrbit
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action223)
        # ReportEphemOnFixedTimeStep
        self.m_logger.WriteLine4(
            "\tThe current ReportEphemOnFixedTimeStep is: {0}", oIntegrator.report_ephem_on_fixed_time_step
        )
        oIntegrator.report_ephem_on_fixed_time_step = False
        self.m_logger.WriteLine4(
            "\tThe new ReportEphemOnFixedTimeStep is: {0}", oIntegrator.report_ephem_on_fixed_time_step
        )
        Assert.assertEqual(False, oIntegrator.report_ephem_on_fixed_time_step)
        oIntegrator.report_ephem_on_fixed_time_step = True
        self.m_logger.WriteLine4(
            "\tThe new ReportEphemOnFixedTimeStep is: {0}", oIntegrator.report_ephem_on_fixed_time_step
        )
        Assert.assertEqual(True, oIntegrator.report_ephem_on_fixed_time_step)
        # Use (true)
        oTime.use = True
        self.m_logger.WriteLine4("\tThe new Use is: {0}", oTime.use)
        Assert.assertEqual(True, oTime.use)

        def action224():
            oIntegrator.report_ephem_on_fixed_time_step = False

        # ReportEphemOnFixedTimeStep
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action224)
        # Exponent
        self.m_logger.WriteLine6("\tThe current Exponent is: {0}", oTime.exponent)
        oTime.exponent = 4.5
        self.m_logger.WriteLine6("\tThe new Exponent is: {0}", oTime.exponent)
        Assert.assertEqual(4.5, oTime.exponent)

        def action225():
            oTime.exponent = 12.34

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action225)
        # StepsPerOrbit
        self.m_logger.WriteLine3("\tThe current StepsPerOrbit is: {0}", oTime.steps_per_orbit)
        oTime.steps_per_orbit = 9
        self.m_logger.WriteLine3("\tThe new StepsPerOrbit is: {0}", oTime.steps_per_orbit)
        Assert.assertEqual(9, oTime.steps_per_orbit)

        def action226():
            oTime.steps_per_orbit = -12

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action226)
        # UseVOP (false)
        self.m_logger.WriteLine4("\tThe current UseVOP is: {0}", oIntegrator.use_graphics3_dp)
        oIntegrator.use_graphics3_dp = False
        self.m_logger.WriteLine4("\tThe new UseVOP is: {0}", oIntegrator.use_graphics3_dp)
        Assert.assertEqual(False, oIntegrator.use_graphics3_dp)
        # Interpolation
        self.Interpolation(oIntegrator.interpolation, oIntegrator.use_graphics3_dp)
        # UseVOP (true)
        oIntegrator.use_graphics3_dp = True
        self.m_logger.WriteLine4("\tThe new UseVOP is: {0}", oIntegrator.use_graphics3_dp)
        Assert.assertEqual(True, oIntegrator.use_graphics3_dp)
        # Interpolation
        self.Interpolation(oIntegrator.interpolation, oIntegrator.use_graphics3_dp)

        # IntegrationModel (eBulirschStoer)
        self.m_logger.WriteLine6("\tThe current IntegrationModel is: {0}", oIntegrator.integration_model)
        oIntegrator.integration_model = VEHICLE_INTEGRATION_MODEL.BULIRSCH_STOER
        self.m_logger.WriteLine6("\tThe new IntegrationModel is: {0}", oIntegrator.integration_model)
        Assert.assertEqual(VEHICLE_INTEGRATION_MODEL.BULIRSCH_STOER, oIntegrator.integration_model)

        def action227():
            oIntegrator.predictor_corrector_scheme = VEHICLE_PREDICTOR_CORRECTOR_SCHEME.PSEUDO_CORRECTION

        # PredictorCorrectorScheme (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action227)
        # StepSizeControl
        self.StepSizeControl(oIntegrator.step_size_control, False)

        # IntegrationModel (eGaussJackson)
        oIntegrator.integration_model = VEHICLE_INTEGRATION_MODEL.GAUSS_JACKSON
        self.m_logger.WriteLine6("\tThe new IntegrationModel is: {0}", oIntegrator.integration_model)
        Assert.assertEqual(VEHICLE_INTEGRATION_MODEL.GAUSS_JACKSON, oIntegrator.integration_model)
        # PredictorCorrectorScheme
        self.m_logger.WriteLine6(
            "\t\tThe current PredictorCorrectorScheme is: {0}", oIntegrator.predictor_corrector_scheme
        )
        oIntegrator.predictor_corrector_scheme = VEHICLE_PREDICTOR_CORRECTOR_SCHEME.FULL_CORRECTION
        self.m_logger.WriteLine6("\t\tThe new PredictorCorrectorScheme is: {0}", oIntegrator.predictor_corrector_scheme)
        Assert.assertEqual(VEHICLE_PREDICTOR_CORRECTOR_SCHEME.FULL_CORRECTION, oIntegrator.predictor_corrector_scheme)
        oIntegrator.predictor_corrector_scheme = VEHICLE_PREDICTOR_CORRECTOR_SCHEME.PSEUDO_CORRECTION
        self.m_logger.WriteLine6("\t\tThe new PredictorCorrectorScheme is: {0}", oIntegrator.predictor_corrector_scheme)
        Assert.assertEqual(VEHICLE_PREDICTOR_CORRECTOR_SCHEME.PSEUDO_CORRECTION, oIntegrator.predictor_corrector_scheme)
        # StepSizeControl
        self.StepSizeControl(oIntegrator.step_size_control, True)

        # IntegrationModel (eRK4)
        oIntegrator.integration_model = VEHICLE_INTEGRATION_MODEL.RUNGE_KUTTA4
        self.m_logger.WriteLine6("\tThe new IntegrationModel is: {0}", oIntegrator.integration_model)
        Assert.assertEqual(VEHICLE_INTEGRATION_MODEL.RUNGE_KUTTA4, oIntegrator.integration_model)

        def action228():
            oIntegrator.predictor_corrector_scheme = VEHICLE_PREDICTOR_CORRECTOR_SCHEME.PSEUDO_CORRECTION

        # PredictorCorrectorScheme (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action228)
        # StepSizeControl
        self.StepSizeControl(oIntegrator.step_size_control, True)

        # IntegrationModel (eRKF78)
        oIntegrator.integration_model = VEHICLE_INTEGRATION_MODEL.RUNGE_KUTTA_F78
        self.m_logger.WriteLine6("\tThe new IntegrationModel is: {0}", oIntegrator.integration_model)
        Assert.assertEqual(VEHICLE_INTEGRATION_MODEL.RUNGE_KUTTA_F78, oIntegrator.integration_model)

        def action229():
            oIntegrator.predictor_corrector_scheme = VEHICLE_PREDICTOR_CORRECTOR_SCHEME.PSEUDO_CORRECTION

        # PredictorCorrectorScheme (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action229)
        # StepSizeControl
        self.StepSizeControl(oIntegrator.step_size_control, False)

        # IntegrationModel (eRKF89Efficient)
        oIntegrator.integration_model = VEHICLE_INTEGRATION_MODEL.RUNGE_KUTTA_V89_EFFICIENT
        self.m_logger.WriteLine6("\tThe new IntegrationModel is: {0}", oIntegrator.integration_model)
        Assert.assertEqual(VEHICLE_INTEGRATION_MODEL.RUNGE_KUTTA_V89_EFFICIENT, oIntegrator.integration_model)

        def action230():
            oIntegrator.predictor_corrector_scheme = VEHICLE_PREDICTOR_CORRECTOR_SCHEME.PSEUDO_CORRECTION

        # PredictorCorrectorScheme (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action230)
        # StepSizeControl
        self.StepSizeControl(oIntegrator.step_size_control, False)

        # AllowPosVelCovInterpolation
        oCovariance.compute_covariance = False

        def action231():
            oIntegrator.allow_position_vel_cov_interpolation = True

        TryCatchAssertBlock.DoAssert("readonly", action231)
        oCovariance.compute_covariance = True
        oIntegrator.allow_position_vel_cov_interpolation = False
        Assert.assertFalse(oIntegrator.allow_position_vel_cov_interpolation)
        oIntegrator.allow_position_vel_cov_interpolation = True
        Assert.assertTrue(oIntegrator.allow_position_vel_cov_interpolation)

    # endregion

    # region Interpolation
    def Interpolation(self, oInterpolation: "IVehicleInterpolation", bUseVOP: bool):
        Assert.assertIsNotNone(oInterpolation)
        self.m_logger.WriteLine6("\tThe current Method is: {0}", oInterpolation.method)
        if bUseVOP:

            def action232():
                oInterpolation.method = VEHICLE_INTERPOLATION_METHOD.HERMITIAN

            # Method
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action232)

        else:
            # Test Hermitian/Lagrange interpolation orders
            # When Hermitian, the order's lower bound is 3 and the upper bound is 29
            # For Lagrange, the lower bound is 0 and the upper bound is 29.
            oInterpolation.method = VEHICLE_INTERPOLATION_METHOD.HERMITIAN

            def action233():
                oInterpolation.order = 2

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action233)

            def action234():
                oInterpolation.order = 30

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action234)
            oInterpolation.order = 3
            Assert.assertEqual(3, oInterpolation.order)
            oInterpolation.order = 29
            Assert.assertEqual(29, oInterpolation.order)

            oInterpolation.method = VEHICLE_INTERPOLATION_METHOD.LAGRANGE

            def action235():
                oInterpolation.order = -1

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action235)

            def action236():
                oInterpolation.order = 30

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action236)
            oInterpolation.order = 0
            Assert.assertEqual(0, oInterpolation.order)
            oInterpolation.order = 29
            Assert.assertEqual(29, oInterpolation.order)

            # Method (eHermitian)
            oInterpolation.method = VEHICLE_INTERPOLATION_METHOD.HERMITIAN
            self.m_logger.WriteLine6("\tThe new Method is: {0}", oInterpolation.method)
            Assert.assertEqual(VEHICLE_INTERPOLATION_METHOD.HERMITIAN, oInterpolation.method)
            # Order
            self.m_logger.WriteLine3("\t\tThe current Order is: {0}", oInterpolation.order)
            oInterpolation.order = 12
            self.m_logger.WriteLine3("\t\tThe new Order is: {0}", oInterpolation.order)
            Assert.assertEqual(12, oInterpolation.order)

            def action237():
                oInterpolation.order = 321

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action237)

            def action238():
                oInterpolation.graphics3_d_pmu = 12.34

            # VOPmu
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action238)
            # Method (eLagrange)
            oInterpolation.method = VEHICLE_INTERPOLATION_METHOD.LAGRANGE
            self.m_logger.WriteLine6("\tThe new Method is: {0}", oInterpolation.method)
            Assert.assertEqual(VEHICLE_INTERPOLATION_METHOD.LAGRANGE, oInterpolation.method)
            # Order
            self.m_logger.WriteLine3("\t\tThe current Order is: {0}", oInterpolation.order)
            oInterpolation.order = 13
            self.m_logger.WriteLine3("\t\tThe new Order is: {0}", oInterpolation.order)
            Assert.assertEqual(13, oInterpolation.order)

            def action239():
                oInterpolation.order = 321

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action239)

            def action240():
                oInterpolation.graphics3_d_pmu = 12.34

            # VOPmu
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action240)
            # Method (eVOP)
            oInterpolation.method = VEHICLE_INTERPOLATION_METHOD.GRAPHICS3_DP
            self.m_logger.WriteLine6("\tThe new Method is: {0}", oInterpolation.method)
            Assert.assertEqual(VEHICLE_INTERPOLATION_METHOD.GRAPHICS3_DP, oInterpolation.method)

        # Order
        self.m_logger.WriteLine3("\t\tThe current Order is: {0}", oInterpolation.order)
        oInterpolation.order = 14
        self.m_logger.WriteLine3("\t\tThe new Order is: {0}", oInterpolation.order)
        Assert.assertEqual(14, oInterpolation.order)

        def action241():
            oInterpolation.order = 321

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action241)
        # VOPmu
        self.m_logger.WriteLine6("\t\tThe current VOPmu is: {0}", oInterpolation.graphics3_d_pmu)
        if self.m_EarthGravModel == TestBase.GravModel.EGM2008:
            oInterpolation.graphics3_d_pmu = 199300220750000
            self.m_logger.WriteLine6("\t\tThe new VOPmu is: {0}", oInterpolation.graphics3_d_pmu)
            Assert.assertEqual(199300220750000, oInterpolation.graphics3_d_pmu)
            oInterpolation.graphics3_d_pmu = 797200883000000
            self.m_logger.WriteLine6("\t\tThe new VOPmu is: {0}", oInterpolation.graphics3_d_pmu)
            Assert.assertEqual(797200883000000, oInterpolation.graphics3_d_pmu)

        else:
            oInterpolation.graphics3_d_pmu = 199300220900000
            self.m_logger.WriteLine6("\t\tThe new VOPmu is: {0}", oInterpolation.graphics3_d_pmu)
            Assert.assertEqual(199300220900000, oInterpolation.graphics3_d_pmu)
            oInterpolation.graphics3_d_pmu = 797200883600000
            self.m_logger.WriteLine6("\t\tThe new VOPmu is: {0}", oInterpolation.graphics3_d_pmu)
            Assert.assertEqual(797200883600000, oInterpolation.graphics3_d_pmu)

        def action242():
            oInterpolation.graphics3_d_pmu = 199300220749999

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action242)

        def action243():
            oInterpolation.graphics3_d_pmu = 797200883600001

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action243)

    # endregion

    # region StepSizeControl
    def StepSizeControl(self, oControl: "IVehicleStepSizeControl", bReadOnly: bool):
        Assert.assertIsNotNone(oControl)
        self.m_logger.WriteLine6("\tThe current Method is: {0}", oControl.method)
        if not bReadOnly:
            # Method (eRelativeError)
            oControl.method = VEHICLE_METHOD.RELATIVE_ERROR
            self.m_logger.WriteLine6("\tThe new Method is: {0}", oControl.method)
            Assert.assertEqual(VEHICLE_METHOD.RELATIVE_ERROR, oControl.method)
            # ErrorTolerance
            self.m_logger.WriteLine6("\t\tThe current ErrorTolerance is: {0}", oControl.error_tolerance)
            oControl.error_tolerance = 1e-06
            self.m_logger.WriteLine6("\t\tThe new ErrorTolerance is: {0}", oControl.error_tolerance)
            Assert.assertEqual(1e-06, oControl.error_tolerance)

            def action244():
                oControl.error_tolerance = -12.34

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action244)
            # MinStepSize
            self.m_logger.WriteLine6("\t\tThe current MinStepSize is: {0}", oControl.min_step_size)
            oControl.min_step_size = 12
            self.m_logger.WriteLine6("\t\tThe new MinStepSize is: {0}", oControl.min_step_size)
            Assert.assertEqual(12, oControl.min_step_size)

            def action245():
                oControl.min_step_size = -12

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action245)
            # MaxStepSize
            self.m_logger.WriteLine6("\t\tThe current MaxStepSize is: {0}", oControl.max_step_size)
            oControl.max_step_size = 21
            self.m_logger.WriteLine6("\t\tThe new MaxStepSize is: {0}", oControl.max_step_size)
            Assert.assertEqual(21, oControl.max_step_size)

            def action246():
                oControl.max_step_size = -12

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action246)

            def action247():
                oControl.min_step_size = 23

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action247)

            def action248():
                oControl.max_step_size = 2

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action248)
            # Method (eFixedStep)
            oControl.method = VEHICLE_METHOD.FIXED_STEP
            self.m_logger.WriteLine6("\tThe new Method is: {0}", oControl.method)
            Assert.assertEqual(VEHICLE_METHOD.FIXED_STEP, oControl.method)

        else:

            def action249():
                oControl.method = VEHICLE_METHOD.FIXED_STEP

            # Method (eFixedStep)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action249)

        def action250():
            oControl.error_tolerance = 0.0001

        # ErrorTolerance
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action250)

        def action251():
            oControl.min_step_size = 3

        # MinStepSize
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action251)

        def action252():
            oControl.max_step_size = 34

        # MaxStepSize
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action252)

    # endregion

    # region Covariance
    def Covariance(self, oCovariance: "IVehicleCovariance"):
        Assert.assertIsNotNone(oCovariance)
        # ComputeCovariance (false)
        self.m_logger.WriteLine4("\tThe current ComputeCovariance is: {0}", oCovariance.compute_covariance)
        oCovariance.compute_covariance = False
        self.m_logger.WriteLine4("\tThe new ComputeCovariance is: {0}", oCovariance.compute_covariance)
        Assert.assertEqual(False, oCovariance.compute_covariance)

        def action253():
            oCovariance.frame = VEHICLE_FRAME.LVLH

        # Frame (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action253)
        # Gravity
        self.CovarianceGravity(oCovariance.gravity, True)
        # PositionVelocity
        self.CovariancePositionVelocity(oCovariance.position_velocity, True)

        def action254():
            oCovariance.include_consider_analysis = False

        # IncludeConsiderAnalysis (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action254)
        # ConsiderAnalysisList
        self.CovarianceConsiderAnalysis(oCovariance.consider_analysis_list, True)

        def action255():
            oCovariance.include_consider_cross_correlation = True

        # IncludeConsiderCrossCorrelation (readonly)
        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action255)
        # ConsiderCorrelation
        self.CovarianceCorrelation(oCovariance.correlation_list, True)
        # Validate
        oCovariance.validate()

        # ComputeCovariance (true)
        oCovariance.compute_covariance = True
        self.m_logger.WriteLine4("\tThe new ComputeCovariance is: {0}", oCovariance.compute_covariance)
        Assert.assertEqual(True, oCovariance.compute_covariance)
        # Representation
        self.m_logger.WriteLine5("\t\tThe current Representation is: {0}", oCovariance.representation)
        # Frame
        self.m_logger.WriteLine6("\t\tThe current Frame is: {0}", oCovariance.frame)
        oCovariance.frame = VEHICLE_FRAME.FRENET
        self.m_logger.WriteLine6("\t\tThe new Frame is: {0}", oCovariance.frame)
        Assert.assertEqual(VEHICLE_FRAME.FRENET, oCovariance.frame)
        oCovariance.frame = VEHICLE_FRAME.J2000
        self.m_logger.WriteLine6("\t\tThe new Frame is: {0}", oCovariance.frame)
        Assert.assertEqual(VEHICLE_FRAME.J2000, oCovariance.frame)
        oCovariance.frame = VEHICLE_FRAME.LVLH
        self.m_logger.WriteLine6("\t\tThe new Frame is: {0}", oCovariance.frame)
        Assert.assertEqual(VEHICLE_FRAME.LVLH, oCovariance.frame)
        oCovariance.frame = VEHICLE_FRAME.TRUE_OF_DATE
        self.m_logger.WriteLine6("\t\tThe new Frame is: {0}", oCovariance.frame)
        Assert.assertEqual(VEHICLE_FRAME.TRUE_OF_DATE, oCovariance.frame)

        # Gravity
        self.CovarianceGravity(oCovariance.gravity, False)
        # PositionVelocity
        self.CovariancePositionVelocity(oCovariance.position_velocity, False)
        # IncludeConsiderAnalysis (false)
        self.m_logger.WriteLine4(
            "\t\tThe current IncludeConsiderAnalysis is: {0}", oCovariance.include_consider_analysis
        )
        oCovariance.include_consider_analysis = False
        self.m_logger.WriteLine4("\t\tThe new IncludeConsiderAnalysis is: {0}", oCovariance.include_consider_analysis)
        Assert.assertEqual(False, oCovariance.include_consider_analysis)
        # ConsiderAnalysisList
        self.CovarianceConsiderAnalysis(oCovariance.consider_analysis_list, True)
        # IncludeConsiderAnalysis (true)
        oCovariance.include_consider_analysis = True
        self.m_logger.WriteLine4("\t\tThe new IncludeConsiderAnalysis is: {0}", oCovariance.include_consider_analysis)
        Assert.assertEqual(True, oCovariance.include_consider_analysis)
        # ConsiderAnalysisList
        self.CovarianceConsiderAnalysis(oCovariance.consider_analysis_list, False)
        # IncludeConsiderCrossCorrelation (false)
        self.m_logger.WriteLine4(
            "\t\tThe current IncludeConsiderCrossCorrelation is: {0}", oCovariance.include_consider_cross_correlation
        )
        oCovariance.include_consider_cross_correlation = False
        self.m_logger.WriteLine4(
            "\t\tThe new IncludeConsiderCrossCorrelation is: {0}", oCovariance.include_consider_cross_correlation
        )
        Assert.assertEqual(False, oCovariance.include_consider_cross_correlation)
        # ConsiderCorrelation
        self.CovarianceCorrelation(oCovariance.correlation_list, True)
        # IncludeConsiderCrossCorrelation (true)
        oCovariance.include_consider_cross_correlation = True
        self.m_logger.WriteLine4(
            "\t\tThe new IncludeConsiderCrossCorrelation is: {0}", oCovariance.include_consider_cross_correlation
        )
        Assert.assertEqual(True, oCovariance.include_consider_cross_correlation)
        # ConsiderCorrelation
        self.CovarianceCorrelation(oCovariance.correlation_list, False)
        # Validate
        oCovariance.validate()

    # endregion

    # region CovarianceGravity
    def CovarianceGravity(self, oGravity: "IVehicleGravity", bReadOnly: bool):
        Assert.assertIsNotNone(oGravity)
        if bReadOnly:

            def action256():
                oGravity.maximum_degree = 5

            # MaximumDegree (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action256)

            def action257():
                oGravity.maximum_order = 2

            # MaximumOrder (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action257)

        else:
            # MaximumDegree
            self.m_logger.WriteLine3("\t\tThe current MaximumDegree is: {0}", oGravity.maximum_degree)
            oGravity.maximum_degree = 23
            self.m_logger.WriteLine3("\t\tThe new MaximumDegree is: {0}", oGravity.maximum_degree)
            Assert.assertEqual(23, oGravity.maximum_degree)

            def action258():
                oGravity.maximum_degree = 123

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action258)
            # MaximumOrder
            self.m_logger.WriteLine3("\t\tThe current MaximumOrder is: {0}", oGravity.maximum_order)
            oGravity.maximum_order = 12
            self.m_logger.WriteLine3("\t\tThe new MaximumOrder is: {0}", oGravity.maximum_order)
            Assert.assertEqual(12, oGravity.maximum_order)

            def action259():
                oGravity.maximum_order = 123

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action259)

    # endregion

    # region CovariancePositionVelocity
    def CovariancePositionVelocity(self, oCollection: "IVehiclePositionVelocityCollection", bReadOnly: bool):
        Assert.assertIsNotNone(oCollection)
        if bReadOnly:
            Assert.assertEqual(6, oCollection.count)
            positionVelocityElement: "IVehiclePositionVelocityElement"
            for positionVelocityElement in oCollection:
                self.m_logger.WriteLine10(
                    "\t\tElement: X = {0}, Y = {1}, Z = {2}, Vx = {3}, Vy = {4}, Vz = {5}",
                    positionVelocityElement.x,
                    positionVelocityElement.y,
                    positionVelocityElement.z,
                    positionVelocityElement.vx,
                    positionVelocityElement.vy,
                    positionVelocityElement.vz,
                )

                def action260():
                    positionVelocityElement.x = 25

                # X (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action260)

                def action261():
                    positionVelocityElement.y = 25

                # Y (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action261)

                def action262():
                    positionVelocityElement.z = 25

                # Z (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action262)

                def action263():
                    positionVelocityElement.vx = 0.01

                # Vx (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action263)

                def action264():
                    positionVelocityElement.vy = 0.01

                # Vy (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action264)

                def action265():
                    positionVelocityElement.vz = 0.01

                # Vz (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action265)

        else:
            self.m_logger.WriteLine3("\tThe PositionVelocity collection contains: {0} elements.", oCollection.count)

            iIndex: int = 0
            while iIndex < oCollection.count:
                positionVelocityElement: "IVehiclePositionVelocityElement" = oCollection[iIndex]
                Assert.assertIsNotNone(positionVelocityElement)
                self.m_logger.WriteLine10(
                    "\t\tElement {6}: X = {0}, Y = {1}, Z = {2}, Vx = {3}, Vy = {4}, Vz = {5}",
                    positionVelocityElement.x,
                    positionVelocityElement.y,
                    positionVelocityElement.z,
                    positionVelocityElement.vx,
                    positionVelocityElement.vy,
                    positionVelocityElement.vz,
                    iIndex,
                )
                if iIndex == 0:
                    positionVelocityElement.x = 21
                    self.m_logger.WriteLine6("\t\tThe new X is: {0}", positionVelocityElement.x)
                    Assert.assertEqual(21, positionVelocityElement.x)

                else:
                    positionVelocityElement.x = 0.0
                    self.m_logger.WriteLine6("\t\tThe new X is: {0}", positionVelocityElement.x)
                    Assert.assertEqual(0.0, positionVelocityElement.x)

                if iIndex == 0:

                    def action266():
                        positionVelocityElement.y = 22

                    # Y (readonly)
                    TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action266)

                else:
                    if iIndex == 1:
                        positionVelocityElement.y = 22
                        self.m_logger.WriteLine6("\t\tThe new Y is: {0}", positionVelocityElement.y)
                        Assert.assertEqual(22, positionVelocityElement.y)

                    else:
                        positionVelocityElement.y = 0.0
                        self.m_logger.WriteLine6("\t\tThe new Y is: {0}", positionVelocityElement.y)
                        Assert.assertEqual(0.0, positionVelocityElement.y)

                if iIndex < 2:

                    def action267():
                        positionVelocityElement.z = 23

                    # Z (readonly)
                    TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action267)

                else:
                    if iIndex == 2:
                        positionVelocityElement.z = 23
                        self.m_logger.WriteLine6("\t\tThe new Z is: {0}", positionVelocityElement.z)
                        Assert.assertEqual(23, positionVelocityElement.z)

                    else:
                        positionVelocityElement.z = 0.0
                        self.m_logger.WriteLine6("\t\tThe new Z is: {0}", positionVelocityElement.z)
                        Assert.assertEqual(0.0, positionVelocityElement.z)

                if iIndex < 3:

                    def action268():
                        positionVelocityElement.vx = 0.001

                    # Vx (readonly)
                    TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action268)

                else:
                    if iIndex == 3:
                        positionVelocityElement.vx = 0.01
                        self.m_logger.WriteLine6("\t\tThe new Vx is: {0}", positionVelocityElement.vx)
                        Assert.assertEqual(0.01, positionVelocityElement.vx)

                    else:
                        positionVelocityElement.vx = 0.0
                        self.m_logger.WriteLine6("\t\tThe new Vx is: {0}", positionVelocityElement.vx)
                        Assert.assertEqual(0.0, positionVelocityElement.vx)

                if iIndex < 4:

                    def action269():
                        positionVelocityElement.vy = 0.001

                    # Vy (readonly)
                    TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action269)

                else:
                    if iIndex == 4:
                        positionVelocityElement.vy = 0.02
                        self.m_logger.WriteLine6("\t\tThe new Vy is: {0}", positionVelocityElement.vy)
                        Assert.assertEqual(0.02, positionVelocityElement.vy)

                    else:
                        positionVelocityElement.vy = 0.0
                        self.m_logger.WriteLine6("\t\tThe new Vy is: {0}", positionVelocityElement.vy)
                        Assert.assertEqual(0.0, positionVelocityElement.vy)

                if iIndex < 5:

                    def action270():
                        positionVelocityElement.vz = 0.001

                    # Vz (readonly)
                    TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action270)

                else:
                    positionVelocityElement.vz = 0.03
                    self.m_logger.WriteLine6("\t\tThe new Vz is: {0}", positionVelocityElement.vz)
                    Assert.assertEqual(0.03, positionVelocityElement.vz)

                iIndex += 1

    # endregion

    # region CovarianceConsiderAnalysis
    def CovarianceConsiderAnalysis(self, oCollection: "IVehicleConsiderAnalysisCollection", bReadOnly: bool):
        Assert.assertIsNotNone(oCollection)
        if bReadOnly:

            def action271():
                oCollection.remove_all()

            # RemoveAll (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action271)

            def action272():
                oCollection.add(VEHICLE_CONSIDER_ANALYSIS_TYPE.CONSIDER_ANALYSIS_DRAG)

            # Add (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action272)
            if oCollection.count > 0:

                def action273():
                    oCollection.remove_at(0)

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action273)

            if oCollection.count > 0:

                def action274():
                    oCollection.remove_by_type(oCollection[0].type)

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action274)

            if oCollection.count > 0:
                self.CovarianceConsiderAnalysisElement(oCollection[0], True)

        else:
            # Count
            self.m_logger.WriteLine3(
                "\t\tThe current ConsiderAnalysis collection contains: {0} elements", oCollection.count
            )
            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3(
                "\t\tThe new ConsiderAnalysis collection contains: {0} elements", oCollection.count
            )
            Assert.assertEqual(0, oCollection.count)
            # Add (eConsiderAnalysisDrag)
            oCollection.add(VEHICLE_CONSIDER_ANALYSIS_TYPE.CONSIDER_ANALYSIS_DRAG)
            Assert.assertEqual(1, oCollection.count)

            def action275():
                oCollection.add(VEHICLE_CONSIDER_ANALYSIS_TYPE.CONSIDER_ANALYSIS_DRAG)

            TryCatchAssertBlock.DoAssert("Should not allow to add duplicated elements.", action275)
            self.m_logger.WriteLine3(
                "\t\tThe new ConsiderAnalysis collection contains: {0} elements", oCollection.count
            )
            # Add (eConsiderAnalysisSRP)
            oCollection.add(VEHICLE_CONSIDER_ANALYSIS_TYPE.CONSIDER_ANALYSIS_SRP)
            Assert.assertEqual(2, oCollection.count)

            def action276():
                oCollection.add(VEHICLE_CONSIDER_ANALYSIS_TYPE.CONSIDER_ANALYSIS_SRP)

            TryCatchAssertBlock.DoAssert("Should not allow to add duplicated elements.", action276)
            self.m_logger.WriteLine3(
                "\t\tThe new ConsiderAnalysis collection contains: {0} elements", oCollection.count
            )
            # _NewEnum
            considerAnalysisCollectionElement: "IVehicleConsiderAnalysisCollectionElement"
            # _NewEnum
            for considerAnalysisCollectionElement in oCollection:
                self.CovarianceConsiderAnalysisElement(considerAnalysisCollectionElement, False)

            # RemoveAt
            oCollection.remove_at(0)
            self.m_logger.WriteLine3(
                "\t\tThe new ConsiderAnalysis collection contains: {0} elements", oCollection.count
            )
            Assert.assertEqual(1, oCollection.count)

            def action277():
                oCollection.remove_at(12)

            TryCatchAssertBlock.DoAssert("Should not allow to remove an invalid element.", action277)
            # RemoveByType
            oCollection.remove_by_type(oCollection[0].type)
            self.m_logger.WriteLine3(
                "\t\tThe new ConsiderAnalysis collection contains: {0} elements", oCollection.count
            )
            Assert.assertEqual(0, oCollection.count)

            def action278():
                oCollection.remove_by_type(VEHICLE_CONSIDER_ANALYSIS_TYPE.CONSIDER_ANALYSIS_SRP)

            TryCatchAssertBlock.DoAssert("Should not allow to remove an invalid element.", action278)

    # endregion

    # region CovarianceConsiderAnalysisElement
    def CovarianceConsiderAnalysisElement(
        self, oVeConsiderAnalysisCollectionElement: "IVehicleConsiderAnalysisCollectionElement", bReadOnly: bool
    ):
        Assert.assertIsNotNone(oVeConsiderAnalysisCollectionElement)
        if bReadOnly:

            def action279():
                oVeConsiderAnalysisCollectionElement.value = 123.456

            # Value (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action279)

            def action280():
                oVeConsiderAnalysisCollectionElement.x = 12.34

            # X (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action280)

            def action281():
                oVeConsiderAnalysisCollectionElement.y = 12.34

            # Y (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action281)

            def action282():
                oVeConsiderAnalysisCollectionElement.z = 12.34

            # Z (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action282)

            def action283():
                oVeConsiderAnalysisCollectionElement.vx = 12.34

            # Vx (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action283)

            def action284():
                oVeConsiderAnalysisCollectionElement.vy = 12.34

            # Vy (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action284)

            def action285():
                oVeConsiderAnalysisCollectionElement.vz = 12.34

            # Vz (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action285)

        else:
            self.m_logger.WriteLine10(
                "\t\t\tElement (before): Name = {0}, Type = {1}, Value = {2}, X = {3}, Y = {4}, Z = {5}, Vx = {6}, Vy = {7}, Vz = {8}",
                oVeConsiderAnalysisCollectionElement.name,
                oVeConsiderAnalysisCollectionElement.type,
                oVeConsiderAnalysisCollectionElement.value,
                oVeConsiderAnalysisCollectionElement.x,
                oVeConsiderAnalysisCollectionElement.y,
                oVeConsiderAnalysisCollectionElement.z,
                oVeConsiderAnalysisCollectionElement.vx,
                oVeConsiderAnalysisCollectionElement.vy,
                oVeConsiderAnalysisCollectionElement.vz,
            )
            # Value
            oVeConsiderAnalysisCollectionElement.value = 123.456
            Assert.assertEqual(123.456, oVeConsiderAnalysisCollectionElement.value)
            # X
            oVeConsiderAnalysisCollectionElement.x = 1.23
            Assert.assertEqual(1.23, oVeConsiderAnalysisCollectionElement.x)
            # Y
            oVeConsiderAnalysisCollectionElement.y = 2.34
            Assert.assertEqual(2.34, oVeConsiderAnalysisCollectionElement.y)
            # Z
            oVeConsiderAnalysisCollectionElement.z = 3.45
            Assert.assertEqual(3.45, oVeConsiderAnalysisCollectionElement.z)
            # Vx
            oVeConsiderAnalysisCollectionElement.vx = 0.123
            Assert.assertEqual(0.123, oVeConsiderAnalysisCollectionElement.vx)
            # Vy
            oVeConsiderAnalysisCollectionElement.vy = 0.234
            Assert.assertEqual(0.234, oVeConsiderAnalysisCollectionElement.vy)
            # Vz
            oVeConsiderAnalysisCollectionElement.vz = 0.345
            Assert.assertEqual(0.345, oVeConsiderAnalysisCollectionElement.vz)
            self.m_logger.WriteLine10(
                "\t\t\tElement (after): Name = {0}, Type = {1}, Value = {2}, X = {3}, Y = {4}, Z = {5}, Vx = {6}, Vy = {7}, Vz = {8}",
                oVeConsiderAnalysisCollectionElement.name,
                oVeConsiderAnalysisCollectionElement.type,
                oVeConsiderAnalysisCollectionElement.value,
                oVeConsiderAnalysisCollectionElement.x,
                oVeConsiderAnalysisCollectionElement.y,
                oVeConsiderAnalysisCollectionElement.z,
                oVeConsiderAnalysisCollectionElement.vx,
                oVeConsiderAnalysisCollectionElement.vy,
                oVeConsiderAnalysisCollectionElement.vz,
            )

    # endregion

    # region CovarianceCorrelation
    def CovarianceCorrelation(self, oCollection: "IVehicleCorrelationListCollection", bReadOnly: bool):
        Assert.assertIsNotNone(oCollection)
        if bReadOnly:

            def action286():
                oCollection.remove_all()

            # RemoveAll (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action286)

            def action287():
                oCollection.add()

            # Add (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action287)
            if oCollection.count > 0:

                def action288():
                    oCollection.remove_at(0)

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action288)

            if oCollection.count > 0:
                self.CovarianceCorrelationElement(oCollection[0], True)

        else:
            # Count
            self.m_logger.WriteLine3("\t\tThe current Correlation collection contains: {0} elements", oCollection.count)
            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3("\t\tThe new Correlation collection contains: {0} elements", oCollection.count)
            Assert.assertEqual(0, oCollection.count)
            # Add
            oCollection.add()
            Assert.assertEqual(1, oCollection.count)
            self.m_logger.WriteLine3("\t\tThe new Correlation collection contains: {0} elements", oCollection.count)
            # RemoveAt
            oCollection.remove_at(0)
            self.m_logger.WriteLine3("\t\tThe new Correlation collection contains: {0} elements", oCollection.count)
            Assert.assertEqual(0, oCollection.count)

            def action289():
                oCollection.remove_at(12)

            TryCatchAssertBlock.DoAssert("Should not allow to remove an invalid element.", action289)
            # Add
            oCollection.add()
            Assert.assertEqual(1, oCollection.count)
            self.m_logger.WriteLine3("\t\tThe new Correlation collection contains: {0} elements", oCollection.count)
            # _NewEnum
            correlationListElement: "IVehicleCorrelationListElement"
            # _NewEnum
            for correlationListElement in oCollection:
                self.CovarianceCorrelationElement(correlationListElement, False)

            # Item
            oElem: "IVehicleCorrelationListElement" = oCollection[0]
            Assert.assertIsNotNone(oElem)
            self.m_logger.WriteLine8(
                "\t\t\tElement: Row = {0}, Column = {1}, Value = {2}", oElem.row, oElem.column, oElem.value
            )
            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3("\t\tThe new Correlation collection contains: {0} elements", oCollection.count)
            Assert.assertEqual(0, oCollection.count)

    # endregion

    # region CovarianceCorrelationElement
    def CovarianceCorrelationElement(
        self, oVeCorrelationListElement: "IVehicleCorrelationListElement", bReadOnly: bool
    ):
        Assert.assertIsNotNone(oVeCorrelationListElement)
        if bReadOnly:

            def action290():
                oVeCorrelationListElement.value = 123.456

            # Value (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action290)

            def action291():
                oVeCorrelationListElement.row = VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_DRAG

            # Row (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action291)

            def action292():
                oVeCorrelationListElement.column = VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_SRP

            # Column (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action292)

        else:
            # Value
            self.m_logger.WriteLine6("\t\tThe current Value is: {0}", oVeCorrelationListElement.value)
            oVeCorrelationListElement.value = 123.456
            self.m_logger.WriteLine6("\t\tThe new Value is: {0}", oVeCorrelationListElement.value)
            Assert.assertEqual(123.456, oVeCorrelationListElement.value)
            # Row
            self.m_logger.WriteLine6("\t\tThe current Row is: {0}", oVeCorrelationListElement.row)
            oVeCorrelationListElement.row = VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_DRAG
            self.m_logger.WriteLine6("\t\tThe new Row is: {0}", oVeCorrelationListElement.row)
            Assert.assertEqual(VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_DRAG, oVeCorrelationListElement.row)
            oVeCorrelationListElement.row = VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_SRP
            self.m_logger.WriteLine6("\t\tThe new Row is: {0}", oVeCorrelationListElement.row)
            Assert.assertEqual(VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_SRP, oVeCorrelationListElement.row)

            def action293():
                oVeCorrelationListElement.row = VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_NONE

            TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action293)
            # Column
            self.m_logger.WriteLine6("\t\tThe current Column is: {0}", oVeCorrelationListElement.column)
            oVeCorrelationListElement.column = VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_DRAG
            self.m_logger.WriteLine6("\t\tThe new Column is: {0}", oVeCorrelationListElement.column)
            Assert.assertEqual(VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_DRAG, oVeCorrelationListElement.column)
            oVeCorrelationListElement.column = VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_SRP
            self.m_logger.WriteLine6("\t\tThe new Column is: {0}", oVeCorrelationListElement.column)
            Assert.assertEqual(VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_SRP, oVeCorrelationListElement.column)

            def action294():
                oVeCorrelationListElement.column = VEHICLE_CORRELATION_LIST_TYPE.CORRELATION_LIST_NONE

            TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action294)


# endregion


# region PropagatorBallisticHelper
class PropagatorBallisticHelper(object):
    def __init__(self, owner: "IStkObject", oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(owner)
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits
        self.m_oUnits.reset_units()
        self._owner: "IStkObject" = owner

    # endregion

    # region Run method
    def Run(self, oBallistic: "IVehiclePropagatorBallistic"):
        self.m_logger.WriteLine("----- BALLISTIC PROPAGATOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oBallistic)
        # StartTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oBallistic.ephemeris_interval.find_start_time())
        oBallistic.ephemeris_interval.set_explicit_interval("18 Jan 2003 01:23:45.678", "18 Jan 2003 01:23:45.678")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oBallistic.ephemeris_interval.find_start_time())
        Assert.assertEqual("18 Jan 2003 01:23:45.678", oBallistic.ephemeris_interval.find_start_time())
        # StopTime
        self.m_logger.WriteLine6("\tThe current StopTime is:  {0}", oBallistic.ephemeris_interval.find_stop_time())
        # Step
        self.m_logger.WriteLine6("\tThe current Step is:  {0}", oBallistic.step)
        oBallistic.step = 12
        self.m_logger.WriteLine6("\tThe new Step is:  {0}", oBallistic.step)
        Assert.assertEqual(12, oBallistic.step)

        def action295():
            oBallistic.step = 123456789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action295)
        # LaunchType
        self.m_logger.WriteLine6("\tThe current LunchType is: {0}", oBallistic.launch_type)
        # LaunchSupportedTypes
        arLanchTypes = oBallistic.launch_supported_types
        self.m_logger.WriteLine3("\tThe Missile supports: {0} Lunch types", len(arLanchTypes))

        iIndex: int = 0
        while iIndex < len(arLanchTypes):
            eLaunch: "VEHICLE_LAUNCH" = clr.Convert(int(arLanchTypes[iIndex][0]), VEHICLE_LAUNCH)
            self.m_logger.WriteLine8("\t\tType {0} is: {1} ({2})", iIndex, arLanchTypes[iIndex][1], eLaunch)
            if not oBallistic.is_launch_type_supported(eLaunch):
                Assert.fail("The {0} type should be supported!", eLaunch)

            # SetLaunchType
            oBallistic.set_launch_type(eLaunch)
            self.m_logger.WriteLine6("\t\tThe new Lunch type is: {0}", oBallistic.launch_type)
            Assert.assertEqual(eLaunch, oBallistic.launch_type)
            if eLaunch == VEHICLE_LAUNCH.LAUNCH_LLA:
                # Launch
                launchLLA: "IVehicleLaunchLLA" = clr.Convert(oBallistic.launch, IVehicleLaunchLLA)
                Assert.assertIsNotNone(launchLLA)
                # Lat
                self.m_logger.WriteLine6("\t\t\tThe current Lat is: {0}", launchLLA.lat)
                launchLLA.lat = 12.34
                self.m_logger.WriteLine6("\t\t\tThe new Lat is: {0}", launchLLA.lat)
                Assert.assertEqual(12.34, launchLLA.lat)

                def action296():
                    launchLLA.lat = 90.1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action296)
                # Lon
                self.m_logger.WriteLine6("\t\t\tThe current Lon is: {0}", launchLLA.lon)
                launchLLA.lon = 12.34
                self.m_logger.WriteLine6("\t\t\tThe new Lon is: {0}", launchLLA.lon)
                Assert.assertEqual(12.34, launchLLA.lon)

                def action297():
                    launchLLA.lon = 360.1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action297)
                # Alt
                self.m_logger.WriteLine6("\t\t\tThe current Alt is: {0}", launchLLA.altitude)
                launchLLA.altitude = 123.4
                self.m_logger.WriteLine6("\t\t\tThe new Alt is: {0}", launchLLA.altitude)
                Assert.assertEqual(123.4, launchLLA.altitude)

                def action298():
                    launchLLA.altitude = -1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action298)
            elif eLaunch == VEHICLE_LAUNCH.LAUNCH_LLR:
                oLLR: "IVehicleLaunchLLR" = clr.Convert(oBallistic.launch, IVehicleLaunchLLR)
                Assert.assertIsNotNone(oLLR)
                # Lat
                self.m_logger.WriteLine6("\t\t\tThe current Lat is: {0}", oLLR.lat)
                oLLR.lat = 12.34
                self.m_logger.WriteLine6("\t\t\tThe new Lat is: {0}", oLLR.lat)
                Assert.assertEqual(12.34, oLLR.lat)

                def action299():
                    oLLR.lat = 90.1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action299)
                # Lon
                self.m_logger.WriteLine6("\t\t\tThe current Lon is: {0}", oLLR.lon)
                oLLR.lon = 12.4
                self.m_logger.WriteLine6("\t\t\tThe new Lon is: {0}", oLLR.lon)
                Assert.assertEqual(12.4, oLLR.lon)

                def action300():
                    oLLR.lon = 360.1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action300)
                # Radius
                self.m_logger.WriteLine6("\t\t\tThe current Radius is: {0}", oLLR.radius)
                oLLR.radius = 6400.789
                self.m_logger.WriteLine6("\t\t\tThe new Radius is: {0}", oLLR.radius)
                Assert.assertEqual(6400.789, oLLR.radius)

                def action301():
                    oLLR.radius = -1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action301)
            else:
                Assert.fail("Invalid type!")
            # need the deltaV to be set in order to propagate without exception
            oBallistic.set_impact_location_type(VEHICLE_IMPACT_LOCATION.IMPACT_LOCATION_LAUNCH_AZ_EL)
            oAzEl: "IVehicleImpactLocationLaunchAzEl" = clr.Convert(
                oBallistic.impact_location, IVehicleImpactLocationLaunchAzEl
            )
            oAzEl.delta_v = 4
            oAzEl.elevation = 88
            oAzEl.azimuth = 46
            # Propagate
            oBallistic.propagate()

            iIndex += 1

        # ImpactLocationType
        self.m_logger.WriteLine6("\tThe current ImpactLocation type is: {0}", oBallistic.impact_location_type)
        # ImpactLocationSupportedTypes
        arImpactTypes = oBallistic.impact_location_supported_types
        self.m_logger.WriteLine3("\tThe Missile supports: {0} ImpactLocatioin types", len(arImpactTypes))

        iIndex: int = 0
        while iIndex < len(arImpactTypes):
            eImpact: "VEHICLE_IMPACT_LOCATION" = clr.Convert(int(arImpactTypes[iIndex][0]), VEHICLE_IMPACT_LOCATION)
            self.m_logger.WriteLine8("\t\tType {0} is: {1} ({2})", iIndex, arImpactTypes[iIndex][1], eImpact)
            if not oBallistic.is_impact_location_type_supported(eImpact):
                Assert.fail("The {0} type should be supported!", eImpact)

            # SetImpactLocationType
            oBallistic.set_impact_location_type(eImpact)
            self.m_logger.WriteLine6("\t\tThe new ImpactLocation type is: {0}", oBallistic.impact_location_type)
            Assert.assertEqual(eImpact, oBallistic.impact_location_type)
            if eImpact == VEHICLE_IMPACT_LOCATION.IMPACT_LOCATION_LAUNCH_AZ_EL:
                # ImpactLocation
                oAzEl: "IVehicleImpactLocationLaunchAzEl" = clr.Convert(
                    oBallistic.impact_location, IVehicleImpactLocationLaunchAzEl
                )
                Assert.assertIsNotNone(oAzEl)
                # Azimuth
                self.m_logger.WriteLine6("\t\t\tThe current Azimuth is: {0}", oAzEl.azimuth)
                oAzEl.azimuth = 324.4
                self.m_logger.WriteLine6("\t\t\tThe new Azimuth is: {0}", oAzEl.azimuth)
                Assert.assertEqual(324.4, oAzEl.azimuth)

                def action302():
                    oAzEl.azimuth = 390.1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action302)
                # Elevation
                self.m_logger.WriteLine6("\t\t\tThe current Elevation is: {0}", oAzEl.elevation)
                oAzEl.elevation = 87.34
                self.m_logger.WriteLine6("\t\t\tThe new Elevation is: {0}", oAzEl.elevation)
                Assert.assertEqual(87.34, oAzEl.elevation)

                def action303():
                    oAzEl.elevation = 390.1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action303)
                # DeltaV
                self.m_logger.WriteLine6("\t\t\tThe current DeltaV is: {0}", oAzEl.delta_v)
                oAzEl.delta_v = 5
                self.m_logger.WriteLine6("\t\t\tThe new DeltaV is: {0}", oAzEl.delta_v)
                Assert.assertEqual(5, oAzEl.delta_v)

                def action304():
                    oAzEl.delta_v = 390.1

                TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action304)
            elif eImpact == VEHICLE_IMPACT_LOCATION.IMPACT_LOCATION_POINT:
                # ImpactLocation
                oPoint: "IVehicleImpactLocationPoint" = clr.Convert(
                    oBallistic.impact_location, IVehicleImpactLocationPoint
                )
                Assert.assertIsNotNone(oPoint)
                # ImpactType
                self.m_logger.WriteLine6("\t\tThe current ImpactType is: {0}", oPoint.impact_type)
                # ImpactSupportedTypes
                arPITypes = oPoint.impact_supported_types
                self.m_logger.WriteLine3("\t\tThe Point supports: {0} Impact types", len(arPITypes))

                j: int = 0
                while j < len(arPITypes):
                    eI: "VEHICLE_IMPACT" = clr.Convert(int(arPITypes[j][0]), VEHICLE_IMPACT)
                    self.m_logger.WriteLine8("\t\t\tType {0} is: {1} ({2})", j, arPITypes[j][1], eI)
                    if not oPoint.is_impact_type_supported(eI):
                        Assert.fail("The {0} type should be supported!", eI)

                    # SetImpactType
                    oPoint.set_impact_type(eI)
                    self.m_logger.WriteLine6("\t\t\tThe new Impact type is: {0}", oPoint.impact_type)
                    Assert.assertEqual(eI, oPoint.impact_type)
                    if eI == VEHICLE_IMPACT.IMPACT_LLA:
                        impactLLA: "IVehicleImpactLLA" = clr.Convert(oPoint.impact, IVehicleImpactLLA)
                        Assert.assertIsNotNone(impactLLA)
                        # Lat
                        self.m_logger.WriteLine6("\t\t\t\tThe current Lat is: {0}", impactLLA.lat)
                        impactLLA.lat = 20.34
                        self.m_logger.WriteLine6("\t\t\t\tThe new Lat is: {0}", impactLLA.lat)
                        Assert.assertEqual(20.34, impactLLA.lat)

                        def action305():
                            impactLLA.lat = 90.1

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action305)
                        # Lon
                        self.m_logger.WriteLine6("\t\t\t\tThe current Lon is: {0}", impactLLA.lon)
                        impactLLA.lon = 20.4
                        self.m_logger.WriteLine6("\t\t\t\tThe new Lon is: {0}", impactLLA.lon)
                        Assert.assertEqual(20.4, impactLLA.lon)

                        def action306():
                            impactLLA.lon = 360.1

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action306)
                        # Alt
                        self.m_logger.WriteLine6("\t\t\t\tThe current Alt is: {0}", impactLLA.altitude)
                        impactLLA.altitude = 10
                        self.m_logger.WriteLine6("\t\t\t\tThe new Alt is: {0}", impactLLA.altitude)
                        Assert.assertEqual(10, impactLLA.altitude)

                        def action307():
                            impactLLA.altitude = -1

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action307)
                    elif eI == VEHICLE_IMPACT.IMPACT_LLR:
                        oLLR: "IVehicleImpactLLR" = clr.Convert(oPoint.impact, IVehicleImpactLLR)
                        Assert.assertIsNotNone(oLLR)
                        # Lat
                        self.m_logger.WriteLine6("\t\t\t\tThe current Lat is: {0}", oLLR.lat)
                        oLLR.lat = 20.34
                        self.m_logger.WriteLine6("\t\t\t\tThe new Lat is: {0}", oLLR.lat)
                        Assert.assertEqual(20.34, oLLR.lat)

                        def action308():
                            oLLR.lat = 90.1

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action308)
                        # Lon
                        self.m_logger.WriteLine6("\t\t\t\tThe current Lon is: {0}", oLLR.lon)
                        oLLR.lon = 20.4
                        self.m_logger.WriteLine6("\t\t\t\tThe new Lon is: {0}", oLLR.lon)
                        Assert.assertEqual(20.4, oLLR.lon)

                        def action309():
                            oLLR.lon = 360.1

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action309)
                        # Radius
                        self.m_logger.WriteLine6("\t\t\t\tThe current Radius is: {0}", oLLR.radius)
                        oLLR.radius = 6500.789
                        self.m_logger.WriteLine6("\t\t\t\tThe new Radius is: {0}", oLLR.radius)
                        Assert.assertEqual(6500.789, oLLR.radius)

                        def action310():
                            oLLR.radius = -1

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action310)
                    else:
                        Assert.fail("Invalid type!")
                    deltaV: "IVehicleLaunchControlFixedDeltaV" = clr.Convert(
                        oPoint.launch_control, IVehicleLaunchControlFixedDeltaV
                    )
                    deltaV.delta_v = 4
                    # Propagate
                    oBallistic.propagate()

                    j += 1

                # LaunchControlType
                self.m_logger.WriteLine6("\t\tThe current LaunchControlType is: {0}", oPoint.launch_control_type)
                # LaunchControlSupportedTypes
                arLCTypes = oPoint.launch_control_supported_types
                self.m_logger.WriteLine3("\t\tThe Point supports: {0} LaunchControl types", len(arLCTypes))

                j: int = 0
                while j < len(arLCTypes):
                    eI: "VEHICLE_LAUNCH_CONTROL" = clr.Convert(int(arLCTypes[j][0]), VEHICLE_LAUNCH_CONTROL)
                    self.m_logger.WriteLine8("\t\t\tType {0} is: {1} ({2})", j, arLCTypes[j][1], eI)
                    if not oPoint.is_launch_control_type_supported(eI):
                        Assert.fail("The {0} type should be supported!", eI)

                    # SetLaunchControlType
                    oPoint.set_launch_control_type(eI)
                    self.m_logger.WriteLine6("\t\t\tThe new LaunchControl type is: {0}", oPoint.launch_control_type)
                    Assert.assertEqual(eI, oPoint.launch_control_type)
                    if eI == VEHICLE_LAUNCH_CONTROL.LAUNCH_CONTROL_FIXED_APOGEE_ALTITUDE:
                        launchControlFixedApogeeAlt: "IVehicleLaunchControlFixedApogeeAltitude" = clr.Convert(
                            oPoint.launch_control, IVehicleLaunchControlFixedApogeeAltitude
                        )
                        Assert.assertIsNotNone(launchControlFixedApogeeAlt)
                        # ApogeeAlt
                        self.m_logger.WriteLine6(
                            "\t\t\t\tThe current ApogeeAlt is: {0}", launchControlFixedApogeeAlt.apogee_altitude
                        )
                        launchControlFixedApogeeAlt.apogee_altitude = 12345.6
                        self.m_logger.WriteLine6(
                            "\t\t\t\tThe new ApogeeAlt is: {0}", launchControlFixedApogeeAlt.apogee_altitude
                        )
                        Assert.assertEqual(12345.6, launchControlFixedApogeeAlt.apogee_altitude)

                        def action311():
                            launchControlFixedApogeeAlt.apogee_altitude = -1

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action311)
                    elif eI == VEHICLE_LAUNCH_CONTROL.LAUNCH_CONTROL_FIXED_DELTA_V:
                        launchControlFixedDeltaV: "IVehicleLaunchControlFixedDeltaV" = clr.Convert(
                            oPoint.launch_control, IVehicleLaunchControlFixedDeltaV
                        )
                        Assert.assertIsNotNone(launchControlFixedDeltaV)
                        # DeltaV
                        self.m_logger.WriteLine6("\t\t\t\tThe current DeltaV is: {0}", launchControlFixedDeltaV.delta_v)
                        launchControlFixedDeltaV.delta_v = 8.6
                        self.m_logger.WriteLine6("\t\t\t\tThe new DeltaV is: {0}", launchControlFixedDeltaV.delta_v)
                        Assert.assertEqual(8.6, launchControlFixedDeltaV.delta_v)

                        def action312():
                            launchControlFixedDeltaV.delta_v = 23

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action312)
                    elif eI == VEHICLE_LAUNCH_CONTROL.LAUNCH_CONTROL_FIXED_DELTA_V_MIN_ECCENTRICITY:
                        launchControlFixedDeltaVMinEcc: "IVehicleLaunchControlFixedDeltaVMinEccentricity" = clr.Convert(
                            oPoint.launch_control, IVehicleLaunchControlFixedDeltaVMinEccentricity
                        )
                        Assert.assertIsNotNone(launchControlFixedDeltaVMinEcc)
                        # DeltaVMin
                        self.m_logger.WriteLine6(
                            "\t\t\t\tThe current DeltaVMin is: {0}", launchControlFixedDeltaVMinEcc.delta_v_min
                        )
                        launchControlFixedDeltaVMinEcc.delta_v_min = 10
                        self.m_logger.WriteLine6(
                            "\t\t\t\tThe new DeltaVMin is: {0}", launchControlFixedDeltaVMinEcc.delta_v_min
                        )
                        Assert.assertEqual(10, launchControlFixedDeltaVMinEcc.delta_v_min)

                        def action313():
                            launchControlFixedDeltaVMinEcc.delta_v_min = 12

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action313)
                    elif eI == VEHICLE_LAUNCH_CONTROL.LAUNCH_CONTROL_FIXED_TIME_OF_FLIGHT:
                        launchControlFixedTimeOfFlight: "IVehicleLaunchControlFixedTimeOfFlight" = clr.Convert(
                            oPoint.launch_control, IVehicleLaunchControlFixedTimeOfFlight
                        )
                        Assert.assertIsNotNone(launchControlFixedTimeOfFlight)
                        # TimeOfFlight
                        self.m_logger.WriteLine6(
                            "\t\t\t\tThe current TimeOfFlight is: {0}", launchControlFixedTimeOfFlight.time_of_flight
                        )
                        launchControlFixedTimeOfFlight.time_of_flight = 1024.456
                        self.m_logger.WriteLine6(
                            "\t\t\t\tThe new TimeOfFlight is: {0}", launchControlFixedTimeOfFlight.time_of_flight
                        )
                        Assert.assertEqual(1024.456, launchControlFixedTimeOfFlight.time_of_flight)

                        def action314():
                            launchControlFixedTimeOfFlight.time_of_flight = 123456789

                        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action314)
                    else:
                        Assert.fail("Invalid type!")
                    # Propagate
                    oBallistic.propagate()

                    j += 1

            else:
                Assert.fail("Invalid type!")
            # Propagate
            oBallistic.propagate()

            iIndex += 1

        # Propagate
        oBallistic.propagate()

        # Verify "Use Scenario Analysis Time" to make sure it works as expected
        # By setting UseScenarioAnalysisTime the propagator's
        # start/stop times are overriden with the scenario's start/stop times.
        sc: "IScenario" = clr.Convert(self._owner.root.current_scenario, IScenario)
        oBallistic.ephemeris_interval.set_explicit_interval("1 Jul 2005 12:00:00.000", "1 Jul 2005 12:00:00.000")
        Assert.assertEqual("1 Jul 2005 12:00:00.000", oBallistic.ephemeris_interval.find_start_time())
        # oBallistic.StopTime = "2 Jul 2005 12:00:00.000";
        # Assert.AreEqual("2 Jul 2005 12:00:00.000", oBallistic.StopTime);

        Assert.assertNotEqual(sc.start_time, oBallistic.ephemeris_interval.find_start_time())
        # Assert.AreNotEqual(sc.StopTime, oBallistic.StopTime);

        oBallistic.propagate()

        Assert.assertEqual("1 Jul 2005 12:00:00.000", oBallistic.ephemeris_interval.find_start_time())
        # Assert.AreEqual("2 Jul 2005 12:00:00.000", oBallistic.StopTime);

        oBallistic.ephemeris_interval.set_implicit_interval(
            (clr.Convert(sc, IStkObject)).vgt.event_intervals["AnalysisInterval"]
        )
        oBallistic.ephemeris_interval.set_explicit_interval(
            (clr.Convert(sc, IStkObject)).vgt.event_intervals["AnalysisInterval"].find_interval().interval.start,
            (clr.Convert(sc, IStkObject)).vgt.event_intervals["AnalysisInterval"].find_interval().interval.start,
        )
        oBallistic.propagate()

        Assert.assertEqual(sc.start_time, oBallistic.ephemeris_interval.find_start_time())
        # Assert.AreEqual(sc.StopTime, oBallistic.StopTime);

        self.m_logger.WriteLine("----- BALLISTIC PROPAGATOR TEST ----- END -----")


# endregion


# region LLAReportReader
class LLAReportReader(object):
    def __init__(self, *args, **kwargs):
        pass

    def ReadLines(self, filepath: str):
        results = []

        sr = File.OpenText(filepath)
        # Skip first two lines (Header and a line separating the header and the data)
        sr.ReadLine()
        sr.ReadLine()

        # Start reading data
        line: str = sr.ReadLine()
        while (line != None) and (len(line) != 0):
            columns = Array.Create(7)
            columns[0] = line[0:24]
            line = line[24:]
            line = line.strip()

            pos: int = 1
            while (pos < Array.Length(columns)) and (len(line) != 0):
                ws: int = line.find(" ")
                if ws != -1:
                    columns[pos] = float(line[0:ws])
                    line = line[ws:]
                    line = line.strip()

                elif len(line) != 0:
                    columns[pos] = float(line)
                    line = ""

                else:
                    columns[pos] = 0.0

                pos += 1

            results.append(columns)

            line = sr.ReadLine()

        sr.Close()

        return results


# endregion


# region ConnectRealtimePointBuilderHelper
class ConnectRealtimePointBuilderHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    def Run(self, obj: "IStkObject"):
        reader = LLAReportReader()
        data = reader.ReadLines(TestBase.GetScenarioFile("LLAPosition.txt"))

        root: "IStkObjectRoot" = obj.root
        Assert.assertIsNotNone(root)
        path: str = obj.path
        for row in data:
            Assert.assertEqual(7, Array.Length(row))

            self.m_logger.WriteLine10(
                "TIME: {0} DATA: {1} {2} {3} {4} {5} {6}", row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            )

            cmd: str = String.Format(
                'SetPosition {0} LLA "{1}" {2} {3} {4} {5} {6} {7}',
                path,
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
            )
            root.execute_command(cmd)


# endregion


# region OMRealtimePointBuilderHelper
class OMRealtimePointBuilderHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    def Run(self, obj: "IStkObject", pb: "IVehicleRealtimePointBuilder"):
        reader = LLAReportReader()
        data = reader.ReadLines(TestBase.GetScenarioFile("LLAPosition.txt"))
        # Configure the unit preferences
        obj.root.unit_preferences.set_current_unit("DateFormat", "UTCG")
        obj.root.unit_preferences.set_current_unit("Latitude", "deg")
        obj.root.unit_preferences.set_current_unit("Longitude", "deg")
        obj.root.unit_preferences.set_current_unit("Distance", "km")

        point: "IVehicleRealtimeLLAPoints" = pb.lla
        for row in data:
            Assert.assertEqual(7, Array.Length(row))

            self.m_logger.WriteLine10(
                "TIME: {0} DATA: {1} {2} {3} {4} {5} {6}", row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            )

            point.add(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]))


# endregion


# region BoostedOMRealtimePointBuilderHelper
class BoostedOMRealtimePointBuilderHelper(object):
    BATCH_SIZE: int = 10

    def __init__(self, root: "IStkObjectRoot", includeVelocities: bool):
        self.m_logger = Logger.Instance
        self._root: "IStkObjectRoot" = root
        self._includeVelocities: bool = includeVelocities

    def Run(self, obj: "IStkObject", point: "IVehicleRealtimeLLAPoints"):
        reader = LLAReportReader()
        data = reader.ReadLines(TestBase.GetScenarioFile("LLAPosition.txt"))
        # Configure the unit preferences
        obj.root.unit_preferences.set_current_unit("DateFormat", "UTCG")
        obj.root.unit_preferences.set_current_unit("Latitude", "deg")
        obj.root.unit_preferences.set_current_unit("Longitude", "deg")
        obj.root.unit_preferences.set_current_unit("Distance", "km")

        times = None
        lat = None
        lon = None
        alt = None
        latrate = None
        lonrate = None
        altrate = None

        times = Array.Create(BoostedOMRealtimePointBuilderHelper.BATCH_SIZE)
        lat = Array.Create(BoostedOMRealtimePointBuilderHelper.BATCH_SIZE)
        lon = Array.Create(BoostedOMRealtimePointBuilderHelper.BATCH_SIZE)
        alt = Array.Create(BoostedOMRealtimePointBuilderHelper.BATCH_SIZE)
        latrate = Array.Create(BoostedOMRealtimePointBuilderHelper.BATCH_SIZE)
        lonrate = Array.Create(BoostedOMRealtimePointBuilderHelper.BATCH_SIZE)
        altrate = Array.Create(BoostedOMRealtimePointBuilderHelper.BATCH_SIZE)

        batchIndex: int = 0
        for row in data:
            Assert.assertEqual(7, Array.Length(row))

            self.m_logger.WriteLine10(
                "TIME: {0} DATA: {1} {2} {3} {4} {5} {6}", row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            )
            if batchIndex > (BoostedOMRealtimePointBuilderHelper.BATCH_SIZE - 1):
                if self._includeVelocities:
                    point.add_batch(times, lat, lon, alt, latrate, lonrate, altrate)

                else:
                    point.add_position_batch(times, lat, lon, alt)

                batchIndex = 0

            else:
                times[batchIndex] = row[0]
                lat[batchIndex] = row[1]
                lon[batchIndex] = row[2]
                alt[batchIndex] = row[3]
                latrate[batchIndex] = row[4]
                lonrate[batchIndex] = row[5]
                altrate[batchIndex] = row[6]
                batchIndex += 1

        if batchIndex != 0:
            dtStart: "IDate" = self._root.conversion_utility.new_date(
                self._root.unit_preferences.get_current_unit_abbrv("DateFormat"),
                str((clr.Convert(self._root.current_scenario, IScenario)).stop_time),
            )
            lasttime: float = float(dtStart.format("EpSec"))
            if self._includeVelocities:
                point.add_batch(times, lat, lon, alt, latrate, lonrate, altrate)

            else:
                point.add_position_batch(times, lat, lon, alt)


# endregion

# region PropagatorRealtimeHelper


class PropagatorRealtimeHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    def Run(self, obj: "IStkObject", realtime: "IVehiclePropagatorRealtime"):
        Assert.assertIsNotNone(realtime)
        realtime.interpolation_order = 1
        Assert.assertEqual(1, realtime.interpolation_order)
        realtime.interpolation_order = 7
        Assert.assertEqual(7, realtime.interpolation_order)

        def action315():
            realtime.interpolation_order = 8

        TryCatchAssertBlock.DoAssert("Should not allow illegal interpolation order.", action315)
        realtime.time_step = 10
        Assert.assertEqual(10, realtime.time_step)
        realtime.timeout_gap = 10
        Assert.assertEqual(10, realtime.timeout_gap)

        supportedPropagators = realtime.supported_look_ahead_propagators
        Assert.assertEqual(1, Array.Rank(supportedPropagators), "rank should be 1")

        i: int = 0
        while i < len(supportedPropagators):
            supportedType: "LOOK_AHEAD_PROPAGATOR" = clr.Convert(int(supportedPropagators[i]), LOOK_AHEAD_PROPAGATOR)
            self.m_logger.WriteLine6("Supported lookahead propagator: {0}", supportedType)
            if ((supportedType == LOOK_AHEAD_PROPAGATOR.HOLD_CBI_POSITION)) or (
                (supportedType == LOOK_AHEAD_PROPAGATOR.HOLD_CBF_POSITION)
            ):
                Assert.assertTrue(
                    (
                        (
                            (
                                (
                                    (
                                        (obj.class_type == STK_OBJECT_TYPE.SHIP)
                                        or (obj.class_type == STK_OBJECT_TYPE.AIRCRAFT)
                                    )
                                    or (obj.class_type == STK_OBJECT_TYPE.GROUND_VEHICLE)
                                )
                                or (obj.class_type == STK_OBJECT_TYPE.MISSILE)
                            )
                            or (obj.class_type == STK_OBJECT_TYPE.LAUNCH_VEHICLE)
                        )
                        or (obj.class_type == STK_OBJECT_TYPE.SATELLITE)
                    ),
                    String.Format("Object is not expected to support {0} look ahead propagator.", supportedType),
                )
                Assert.assertTrue(realtime.is_look_ahead_propagator_supported(supportedType))
                realtime.look_ahead_propagator = supportedType
                Assert.assertEqual(supportedType, realtime.look_ahead_propagator)
            elif (
                ((supportedType == LOOK_AHEAD_PROPAGATOR.TWO_BODY))
                or ((supportedType == LOOK_AHEAD_PROPAGATOR.J2_PERTURBATION))
            ) or ((supportedType == LOOK_AHEAD_PROPAGATOR.J4_PERTURBATION)):
                Assert.assertTrue(
                    (
                        (
                            (obj.class_type == STK_OBJECT_TYPE.MISSILE)
                            or (obj.class_type == STK_OBJECT_TYPE.LAUNCH_VEHICLE)
                        )
                        or (obj.class_type == STK_OBJECT_TYPE.SATELLITE)
                    ),
                    String.Format("Object is not expected to support {0} look ahead propagator.", supportedType),
                )
                Assert.assertTrue(realtime.is_look_ahead_propagator_supported(supportedType))
                realtime.look_ahead_propagator = supportedType
                Assert.assertEqual(supportedType, realtime.look_ahead_propagator)
            elif supportedType == LOOK_AHEAD_PROPAGATOR.BALLISTIC:
                Assert.assertTrue(
                    ((obj.class_type == STK_OBJECT_TYPE.MISSILE) or (obj.class_type == STK_OBJECT_TYPE.LAUNCH_VEHICLE)),
                    String.Format("Object is not expected to support {0} look ahead propagator.", supportedType),
                )
                Assert.assertTrue(realtime.is_look_ahead_propagator_supported(supportedType))
                realtime.look_ahead_propagator = supportedType
                Assert.assertEqual(supportedType, realtime.look_ahead_propagator)
            elif supportedType == LOOK_AHEAD_PROPAGATOR.DEAD_RECKON:
                Assert.assertTrue(
                    (
                        (
                            (
                                (
                                    (obj.class_type == STK_OBJECT_TYPE.SHIP)
                                    or (obj.class_type == STK_OBJECT_TYPE.AIRCRAFT)
                                )
                                or (obj.class_type == STK_OBJECT_TYPE.GROUND_VEHICLE)
                            )
                            or (obj.class_type == STK_OBJECT_TYPE.MISSILE)
                        )
                        or (obj.class_type == STK_OBJECT_TYPE.LAUNCH_VEHICLE)
                    ),
                    String.Format("Object is not expected to support {0} look ahead propagator.", supportedType),
                )
                Assert.assertTrue(realtime.is_look_ahead_propagator_supported(supportedType))
                realtime.look_ahead_propagator = supportedType
                Assert.assertEqual(supportedType, realtime.look_ahead_propagator)
            else:
                Assert.assertFalse(realtime.is_look_ahead_propagator_supported(supportedType))

            i += 1

        # Duration
        oDuration: "IVehicleDuration" = realtime.duration
        Assert.assertIsNotNone(oDuration)
        # LookAhead
        self.m_logger.WriteLine6("\tThe current LookAhead is: {0}", oDuration.look_ahead)
        oDuration.look_ahead = 123.456
        self.m_logger.WriteLine6("\tThe new LookAhead is: {0}", oDuration.look_ahead)
        Assert.assertEqual(123.456, oDuration.look_ahead)

        def action316():
            oDuration.look_ahead = 0

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action316)
        # LookBehind
        self.m_logger.WriteLine6("\tThe current LookBehind is: {0}", oDuration.look_behind)
        oDuration.look_behind = 456.789
        self.m_logger.WriteLine6("\tThe new LookBehind is: {0}", oDuration.look_behind)
        Assert.assertEqual(456.789, oDuration.look_behind)

        def action317():
            oDuration.look_behind = 123456789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action317)

        realtime.propagate()


# endregion


# region PropagatorGPSHelper
class PropagatorGPSHelper(object):
    def __init__(self, dataDir: str):
        self.m_logger = Logger.Instance
        self._dataDir: str = dataDir

    def Run(self, obj: "IStkObject", gps: "IVehiclePropagatorGPS"):
        Assert.assertIsNotNone(gps)

        sSEMAlmanacPath: str = TestBase.GetScenarioFile("GPSAlmanac.al3")
        sYUMAAlmanacPath: str = TestBase.GetScenarioFile("GPSAlmanac.alm")
        sSP3AlmanacPath: str = TestBase.GetScenarioFile("GPSAlmanac.sp3")

        # -------------------------------------------------------------------------
        # Specify a catalog
        # -------------------------------------------------------------------------
        gps.prn = 5
        Assert.assertEqual(5, gps.prn)
        gps.auto_update_enabled = False
        Assert.assertFalse(gps.auto_update_enabled)

        gps.specify_catalog.filename = sYUMAAlmanacPath
        Assert.assertEqual("GPSAlmanac.alm", gps.specify_catalog.filename)
        Assert.assertEqual(gps.specify_catalog.properties.type, VEHICLE_GPS_ALMANAC_TYPE.GPS_ALMANAC_TYPE_YUMA)

        yuma: "IVehicleGPSAlmanacPropertiesYUMA" = clr.CastAs(
            gps.specify_catalog.properties, IVehicleGPSAlmanacPropertiesYUMA
        )
        Assert.assertIsNotNone(yuma)

        yumaType: "VEHICLE_GPS_ALMANAC_TYPE" = yuma.type

        yuma.reference_week = GPS_REFERENCE_WEEK.WEEK06_JAN1980
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK06_JAN1980, yuma.reference_week)
        yuma.reference_week = GPS_REFERENCE_WEEK.WEEK07_APR2019
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK07_APR2019, yuma.reference_week)
        yuma.reference_week = GPS_REFERENCE_WEEK.WEEK22_AUG1999
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK22_AUG1999, yuma.reference_week)

        def action318():
            yuma.reference_week = GPS_REFERENCE_WEEK.UNKNOWN

        TryCatchAssertBlock.DoAssert("bad yuma.ReferenceWeek.", action318)

        self.m_logger.WriteLine10(
            "Almanac week: {0}, Date of almanac: {1}, Time of almanac: {2}, Ref.Week: {3}, Health: {4}, WeekNumber:{5}",
            yuma.almanac_week,
            yuma.date_of_almanac,
            yuma.time_of_almanac,
            yuma.reference_week,
            yuma.health,
            yuma.week_number,
        )

        gps.specify_catalog.filename = sSP3AlmanacPath
        Assert.assertEqual("GPSAlmanac.sp3", gps.specify_catalog.filename)
        Assert.assertEqual(gps.specify_catalog.properties.type, VEHICLE_GPS_ALMANAC_TYPE.GPS_ALMANAC_TYPE_SP3)

        sp3: "IVehicleGPSAlmanacPropertiesSP3" = clr.CastAs(
            gps.specify_catalog.properties, IVehicleGPSAlmanacPropertiesSP3
        )
        Assert.assertIsNotNone(sp3)

        sp3Type: "VEHICLE_GPS_ALMANAC_TYPE" = sp3.type

        self.m_logger.WriteLine8(
            "Almanac week: {0}, Date of almanac: {1}, Time of almanac: {2}",
            sp3.almanac_week,
            sp3.date_of_almanac,
            sp3.time_of_almanac,
        )

        gps.specify_catalog.filename = sSEMAlmanacPath
        Assert.assertEqual("GPSAlmanac.al3", gps.specify_catalog.filename)
        Assert.assertEqual(gps.specify_catalog.properties.type, VEHICLE_GPS_ALMANAC_TYPE.GPS_ALMANAC_TYPE_SEM)

        availPRNs = gps.available_pr_ns
        Assert.assertIsNotNone(availPRNs)

        i: int = 0
        while i < Array.Length(availPRNs):
            gps.prn = int(clr.Convert(availPRNs[i], str))
            Assert.assertEqual(gps.prn, int(clr.Convert(availPRNs[i], str)))

            i += 1

        gps.auto_update_enabled = True

        properties: "IVehicleGPSAutoUpdateProperties" = gps.auto_update.properties

        properties.selection = VEHICLE_GPS_ELEM_SELECTION.GPS_ELEM_SELECTION_USE_ALL
        Assert.assertEqual(VEHICLE_GPS_ELEM_SELECTION.GPS_ELEM_SELECTION_USE_ALL, properties.selection)
        properties.selection = VEHICLE_GPS_ELEM_SELECTION.GPS_ELEM_SELECTION_USE_FIRST
        Assert.assertEqual(VEHICLE_GPS_ELEM_SELECTION.GPS_ELEM_SELECTION_USE_FIRST, properties.selection)

        properties.switch_method = VEHICLE_GPS_SWITCH_METHOD.GPS_SWITCH_METHOD_TCA
        Assert.assertEqual(VEHICLE_GPS_SWITCH_METHOD.GPS_SWITCH_METHOD_TCA, properties.switch_method)
        properties.switch_method = VEHICLE_GPS_SWITCH_METHOD.GPS_SWITCH_METHOD_MIDPOINT
        Assert.assertEqual(VEHICLE_GPS_SWITCH_METHOD.GPS_SWITCH_METHOD_MIDPOINT, properties.switch_method)
        properties.switch_method = VEHICLE_GPS_SWITCH_METHOD.GPS_SWITCH_METHOD_EPOCH
        Assert.assertEqual(VEHICLE_GPS_SWITCH_METHOD.GPS_SWITCH_METHOD_EPOCH, properties.switch_method)

        gps.auto_update_enabled = False

        sem: "IVehicleGPSAlmanacPropertiesSEM" = clr.CastAs(
            gps.specify_catalog.properties, IVehicleGPSAlmanacPropertiesSEM
        )
        Assert.assertIsNotNone(sem)

        semType: "VEHICLE_GPS_ALMANAC_TYPE" = yuma.type

        sem.reference_week = GPS_REFERENCE_WEEK.WEEK06_JAN1980
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK06_JAN1980, sem.reference_week)
        sem.reference_week = GPS_REFERENCE_WEEK.WEEK07_APR2019
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK07_APR2019, sem.reference_week)
        sem.reference_week = GPS_REFERENCE_WEEK.WEEK22_AUG1999
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK22_AUG1999, sem.reference_week)

        def action319():
            sem.reference_week = GPS_REFERENCE_WEEK.UNKNOWN

        TryCatchAssertBlock.DoAssert("bad sem.ReferenceWeek.", action319)

        self.m_logger.WriteLine10(
            "Almanac week: {0}, Date of almanac: {1}, Time of almanac: {2}, Ref.Week: {3}, Health: {4}, AvgURA:{5}",
            sem.almanac_week,
            sem.date_of_almanac,
            sem.time_of_almanac,
            sem.reference_week,
            sem.health,
            sem.avg_ura,
        )

        sem.reference_week = GPS_REFERENCE_WEEK.WEEK06_JAN1980
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK06_JAN1980, sem.reference_week)
        sem.reference_week = GPS_REFERENCE_WEEK.WEEK07_APR2019
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK07_APR2019, sem.reference_week)
        sem.reference_week = GPS_REFERENCE_WEEK.WEEK22_AUG1999
        Assert.assertEqual(GPS_REFERENCE_WEEK.WEEK22_AUG1999, sem.reference_week)

        self.m_logger.WriteLine8(
            "Start time: {0}, Stop time: {1}, Step: {2}",
            gps.ephemeris_interval.find_start_time(),
            gps.ephemeris_interval.find_stop_time(),
            gps.step,
        )

        gps.propagate()

        # -------------------------------------------------------------------------
        # Exercise the auto-update feature
        # -------------------------------------------------------------------------
        gps.auto_update_enabled = True
        Assert.assertTrue(gps.auto_update_enabled)

        availPRNs = gps.available_pr_ns
        Assert.assertIsNotNone(availPRNs)

        i: int = 0
        while i < Array.Length(availPRNs):
            gps.prn = int(clr.Convert(availPRNs[i], str))
            Assert.assertEqual(gps.prn, int(clr.Convert(availPRNs[i], str)))

            i += 1

        # Reset the PRN
        gps.prn = 5

        #
        # Auto-update from file
        #

        try:
            gps.auto_update.selected_source = VEHICLE_GPS_AUTO_UPDATE_SOURCE.GPS_AUTO_UPDATE_SOURCE_UNKNOWN
            Assert.fail("Should have failed - eGPSAutoUpdateSourceUnknown.")

        except AssertionError:
            raise

        except Exception as ex:
            self.m_logger.WriteLine(str(ex))

        try:
            gps.auto_update.selected_source = VEHICLE_GPS_AUTO_UPDATE_SOURCE.GPS_AUTO_UPDATE_SOURCE_NONE
            Assert.fail("Should have failed - eGPSAutoUpdateSourceNone.")

        except AssertionError:
            raise

        except Exception as ex:
            self.m_logger.WriteLine(str(ex))

        gps.auto_update.selected_source = VEHICLE_GPS_AUTO_UPDATE_SOURCE.GPS_AUTO_UPDATE_SOURCE_FILE
        Assert.assertEqual(VEHICLE_GPS_AUTO_UPDATE_SOURCE.GPS_AUTO_UPDATE_SOURCE_FILE, gps.auto_update.selected_source)

        gps.auto_update.file_source.filename = sSEMAlmanacPath
        Assert.assertEqual("GPSAlmanac.al3", gps.auto_update.file_source.filename)
        records: "IVehicleGPSElementCollection" = gps.auto_update.file_source.preview()
        Assert.assertTrue((records.count > 0))

        i: int = 0
        while i < records.count:
            age: float = records[i].age

            i += 1

        def action320():
            age: float = records[records.count].age

        TryCatchAssertBlock.DoAssert("Should have failed referencing bad index.", action320)

        element: "IVehicleGPSElement"

        for element in records:
            age: float = element.age
            epoch: typing.Any = element.epoch
            toa: float = element.time_of_almanac
            week: int = element.week

        gps.auto_update.file_source.filename = sYUMAAlmanacPath
        Assert.assertEqual("GPSAlmanac.alm", gps.auto_update.file_source.filename)
        records = gps.auto_update.file_source.preview()
        Assert.assertTrue((records.count > 0))

        def action321():
            gps.auto_update.file_source.filename = sSP3AlmanacPath

        TryCatchAssertBlock.DoAssert("Should have failed.", action321)
        # Verify that the file name has not been updated
        Assert.assertEqual("GPSAlmanac.alm", gps.auto_update.file_source.filename)

        gps.propagate()


# endregion


# region BasicAttitudeStandardHelper
class BasicAttitudeStandardHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "IStkObjectRoot" = oApplication
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oApplication.unit_preferences
        self.m_oUnits.reset_units()

    # endregion

    # region Run method
    def Run(self, oAttitude: "IVehicleAttitudeStandard"):
        self.m_logger.WriteLine("----- STANDARD ATTITUDE TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oAttitude)
        # Type
        self.m_logger.WriteLine6("\tThe current Type is: {0}", oAttitude.type)
        if oAttitude.type == ATTITUDE_STANDARD_TYPE.TRAJECTORY_ATTITUDE_STANDARD:
            oTrajectory: "IVehicleTrajectoryAttitudeStandard" = clr.Convert(
                oAttitude, IVehicleTrajectoryAttitudeStandard
            )
            Assert.assertIsNotNone(oTrajectory)
            # Basic
            self.Basic(oTrajectory.basic)
            # External
            self.External(oTrajectory.external)
            # Pointing
            self.Pointing(oTrajectory.pointing)
        elif oAttitude.type == ATTITUDE_STANDARD_TYPE.ORBIT_ATTITUDE_STANDARD:
            oOrbit: "IVehicleOrbitAttitudeStandard" = clr.Convert(oAttitude, IVehicleOrbitAttitudeStandard)
            Assert.assertIsNotNone(oOrbit)
            # Basic
            self.Basic(oOrbit.basic)
            # Pointing
            self.Pointing(oOrbit.pointing)
            # IntegratedAttitude
            self.IntegratedAttitude(oOrbit.integrated_attitude)
            # External
            self.External(oOrbit.external)
        elif oAttitude.type == ATTITUDE_STANDARD_TYPE.ROUTE_ATTITUDE_STANDARD:
            oRoute: "IVehicleRouteAttitudeStandard" = clr.Convert(oAttitude, IVehicleRouteAttitudeStandard)
            Assert.assertIsNotNone(oRoute)
            # Basic
            self.Basic(oRoute.basic)
            # External
            self.External(oRoute.external)
        else:
            Assert.fail("Invalid type - {0}!", oAttitude.type)
        self.m_logger.WriteLine("----- STANDARD ATTITUDE TEST ----- END -----")

    # endregion

    # region Basic
    def Basic(self, oBasic: "IVehicleStandardBasic"):
        self.m_logger.WriteLine("----- STANDARD BASIC TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oBasic)
        # ProfileType
        self.m_logger.WriteLine6("\tThe current ProfileType is: {0}", oBasic.profile_type)
        # ProfileSupportedTypes
        arTypes = oBasic.profile_supported_types
        self.m_logger.WriteLine3("\tThe current object supports: {0} profile types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_PROFILE" = clr.Convert(int(arTypes[iIndex][0]), VEHICLE_PROFILE)
            self.m_logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not oBasic.is_profile_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetProfileType
            oBasic.set_profile_type(eType)
            self.m_logger.WriteLine6("\t\tThe new Profile type is: {0}", oBasic.profile_type)
            veProfile: "VEHICLE_PROFILE" = oBasic.profile_type
            Assert.assertEqual(eType, veProfile)
            # Profile
            self.Profile(oBasic.profile)

            iIndex += 1

        self.m_logger.WriteLine("----- STANDARD BASIC TEST ----- END -----")

    # endregion

    # region Profile
    def Profile(self, oProfile: "IVehicleAttitudeProfile"):
        Assert.assertIsNotNone(oProfile)
        # Type
        self.m_logger.WriteLine5("\t\t\tThe current Type is: {0}", oProfile.type)
        if oProfile.type == "Aligned and Constrained":
            oAAC: "IVehicleProfileAlignedAndConstrained" = clr.Convert(oProfile, IVehicleProfileAlignedAndConstrained)
            Assert.assertIsNotNone(oAAC)
            # AlignedVector
            self.Vector(oAAC.aligned_vector)
            # ConstrainedVector
            self.Vector(oAAC.constrained_vector)

        if oProfile.type == "Coordinated Turn":
            oCTurn: "IVehicleProfileCoordinatedTurn" = clr.Convert(oProfile, IVehicleProfileCoordinatedTurn)
            Assert.assertIsNotNone(oCTurn)
            # TimeOffset
            self.m_logger.WriteLine6("\t\t\t\tThe current TimeOffset is: {0}", oCTurn.time_offset)
            oCTurn.time_offset = 123.456
            self.m_logger.WriteLine6("\t\t\t\tThe new TimeOffset is: {0}", oCTurn.time_offset)
            Assert.assertEqual(123.456, oCTurn.time_offset)

            def action322():
                oCTurn.time_offset = 0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action322)

        if (
            (
                (
                    (
                        (
                            (oProfile.type == "ECF velocity alignment with nadir constraint")
                            or (oProfile.type == "ECF velocity alignment with radial constraint")
                        )
                        or (oProfile.type == "ECI velocity alignment with nadir constraint")
                    )
                    or (oProfile.type == "Nadir alignment with ECF velocity constraint")
                )
                or (oProfile.type == "Nadir alignment with ECI velocity constraint")
            )
            or (oProfile.type == "Nadir alignment with Sun constraint")
        ) or (oProfile.type == "Nadir alignment with orbit normal constraint"):
            oCOffset: "IVehicleProfileConstraintOffset" = clr.Convert(oProfile, IVehicleProfileConstraintOffset)
            Assert.assertIsNotNone(oCOffset)
            # ConstraintOffset
            self.m_logger.WriteLine6("\t\t\t\tThe current ConstraintOffset is: {0}", oCOffset.constraint_offset)
            oCOffset.constraint_offset = 123.456
            self.m_logger.WriteLine6("\t\t\t\tThe new ConstraintOffset is: {0}", oCOffset.constraint_offset)
            Assert.assertAlmostEqual(123.456, oCOffset.constraint_offset, delta=0.0001)

            def action323():
                oCOffset.constraint_offset = 1234.56

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action323)

        if oProfile.type == "Fixed in Axes":
            oFixed: "IVehicleProfileFixedInAxes" = clr.Convert(oProfile, IVehicleProfileFixedInAxes)
            Assert.assertIsNotNone(oFixed)
            arAvailRefAxes = oFixed.available_reference_axes
            # ReferenceAxes
            self.m_logger.WriteLine5("\t\t\t\tThe current ReferenceAxes is: {0}", oFixed.reference_axes)
            oFixed.reference_axes = "Star/Star1 MeanEclpJ2000"
            self.m_logger.WriteLine5("\t\t\t\tThe new ReferenceAxes is: {0}", oFixed.reference_axes)
            Assert.assertEqual("Star/Star1 MeanEclpJ2000", oFixed.reference_axes)

            def action324():
                oFixed.reference_axes = ""

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action324)

            def action325():
                oFixed.reference_axes = "InvalidReferenceAxes"

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action325)
            # Orientation
            oHelper = OrientationTest(self.m_oUnits)
            oHelper.Run(
                oFixed.orientation, ((Orientations.Quaternion | Orientations.EulerAngles) | Orientations.YPRAngles)
            )

        if oProfile.type == "Precessing Spin":
            profilePrecessingSpin: "IVehicleProfilePrecessingSpin" = clr.Convert(
                oProfile, IVehicleProfilePrecessingSpin
            )
            Assert.assertIsNotNone(profilePrecessingSpin)
            # Epoch
            self.m_logger.WriteLine6(
                "\t\t\t\tThe current Epoch is: {0}", profilePrecessingSpin.smart_epoch.time_instant
            )
            profilePrecessingSpin.smart_epoch.set_explicit_time("1 Jul 1999 05:00:00.000")
            self.m_logger.WriteLine6("\t\t\t\tThe new Epoch is: {0}", profilePrecessingSpin.smart_epoch.time_instant)
            Assert.assertEqual("1 Jul 1999 05:00:00.000", profilePrecessingSpin.smart_epoch.time_instant)
            # NutationAngle
            self.m_logger.WriteLine6("\t\t\t\tThe current NutationAngle is: {0}", profilePrecessingSpin.nutation_angle)
            profilePrecessingSpin.nutation_angle = 12.34
            self.m_logger.WriteLine6("\t\t\t\tThe new NutationAngle is: {0}", profilePrecessingSpin.nutation_angle)
            Assert.assertEqual(12.34, profilePrecessingSpin.nutation_angle)

            def action326():
                profilePrecessingSpin.nutation_angle = 123.4

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action326)
            # Precession
            self.RateOffset(profilePrecessingSpin.precession)
            # Spin
            self.RateOffset(profilePrecessingSpin.spin)
            # Body
            oHelper = DirectionsTest()
            oHelper.Run(profilePrecessingSpin.body)
            # InertialPrecession
            oHelper.Run(profilePrecessingSpin.inertial_precession)

            profilePrecessingSpin.reference_axes = "CentralBody/Earth ICRF"
            Assert.assertEqual("CentralBody/Earth ICRF", profilePrecessingSpin.reference_axes)
            profilePrecessingSpin.reference_axes = "CentralBody/Earth Inertial"
            Assert.assertEqual("CentralBody/Earth Inertial", profilePrecessingSpin.reference_axes)

            def action327():
                profilePrecessingSpin.reference_axes = "bogus"

            TryCatchAssertBlock.DoAssert("Should not allow a bogus reference axes.", action327)

        if oProfile.type == "Spinning":
            profileSpinning: "IVehicleProfileSpinning" = clr.Convert(oProfile, IVehicleProfileSpinning)
            Assert.assertIsNotNone(profileSpinning)
            # Epoch
            self.m_logger.WriteLine6("\t\t\t\tThe current Epoch is: {0}", profileSpinning.smart_epoch.time_instant)
            profileSpinning.smart_epoch.set_explicit_time("1 Jul 1999 05:00:00.000")
            self.m_logger.WriteLine6("\t\t\t\tThe new Epoch is: {0}", profileSpinning.smart_epoch.time_instant)
            Assert.assertEqual("1 Jul 1999 05:00:00.000", profileSpinning.smart_epoch.time_instant)
            # Rate
            self.m_logger.WriteLine6("\t\t\t\tThe current Rate is: {0}", profileSpinning.rate)
            profileSpinning.rate = 123.4
            self.m_logger.WriteLine6("\t\t\t\tThe new Rate is: {0}", profileSpinning.rate)
            Assert.assertEqual(123.4, profileSpinning.rate)

            def action328():
                profileSpinning.rate = 123456.789

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action328)
            # Offset
            self.m_logger.WriteLine6("\t\t\t\tThe current Offset is: {0}", profileSpinning.offset)
            profileSpinning.offset = 12.34
            self.m_logger.WriteLine6("\t\t\t\tThe new Offset is: {0}", profileSpinning.offset)
            Assert.assertEqual(12.34, profileSpinning.offset)

            def action329():
                profileSpinning.offset = 1234.5

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action329)
            # Body
            oHelper = DirectionsTest()
            oHelper.Run(profileSpinning.body)
            # Inertial
            oHelper.Run(profileSpinning.inertial)

        if (
            (
                (
                    (
                        (
                            (oProfile.type == "ECI velocity alignment with Sun constraint")
                            or (oProfile.type == "Sun alignment with Z in orbit plane")
                        )
                        or (oProfile.type == "Sun alignment with nadir constraint")
                    )
                    or (oProfile.type == "Sun alignment - occultation normal constraint")
                )
                or (oProfile.type == "Sun alignment with ECI Z axis constraint")
            )
            or (oProfile.type == "Sun alignment with ecliptic normal constraint")
        ) or (oProfile.type == "XPOP Inertial Attitude"):
            oAOffset: "IVehicleProfileAlignmentOffset" = clr.Convert(oProfile, IVehicleProfileAlignmentOffset)
            Assert.assertIsNotNone(oAOffset)
            # AlignmentOffset
            self.m_logger.WriteLine6("\t\t\t\tThe current AlignmentOffset is: {0}", oAOffset.alignment_offset)
            oAOffset.alignment_offset = 123.456
            self.m_logger.WriteLine6("\t\t\t\tThe new AlignmentOffset is: {0}", oAOffset.alignment_offset)
            Assert.assertAlmostEqual(123.456, oAOffset.alignment_offset, delta=0.0001)

            def action330():
                oAOffset.alignment_offset = 1234.56

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action330)

        if oProfile.type == "Inertially fixed":
            oInertial: "IVehicleProfileInertial" = clr.Convert(oProfile, IVehicleProfileInertial)
            Assert.assertIsNotNone(oInertial)
            # Inertial
            oHelper = OrientationTest(self.m_oUnits)
            oHelper.Run(
                oInertial.inertial, ((Orientations.EulerAngles | Orientations.Quaternion) | Orientations.YPRAngles)
            )

        if oProfile.type == "Yaw to nadir":
            oYTN: "IVehicleProfileYawToNadir" = clr.Convert(oProfile, IVehicleProfileYawToNadir)
            Assert.assertIsNotNone(oYTN)
            # Inertial
            oHelper = DirectionsTest()
            oHelper.Run(oYTN.inertial)

        if (oProfile.type == "Spin about Sun vector") or (oProfile.type == "Spin about nadir"):
            profileSpinAboutXxx: "IVehicleProfileSpinAboutXXX" = clr.Convert(oProfile, IVehicleProfileSpinAboutXXX)
            Assert.assertIsNotNone(profileSpinAboutXxx)
            # Epoch
            self.m_logger.WriteLine6("\t\t\t\tThe current Epoch is: {0}", profileSpinAboutXxx.smart_epoch.time_instant)
            profileSpinAboutXxx.smart_epoch.set_explicit_time("1 Jul 1999 05:00:00.000")
            self.m_logger.WriteLine6("\t\t\t\tThe new Epoch is: {0}", profileSpinAboutXxx.smart_epoch.time_instant)
            Assert.assertEqual("1 Jul 1999 05:00:00.000", profileSpinAboutXxx.smart_epoch.time_instant)
            # Rate
            self.m_logger.WriteLine6("\t\t\t\tThe current Rate is: {0}", profileSpinAboutXxx.rate)
            profileSpinAboutXxx.rate = 123.4
            self.m_logger.WriteLine6("\t\t\t\tThe new Rate is: {0}", profileSpinAboutXxx.rate)
            Assert.assertEqual(123.4, profileSpinAboutXxx.rate)

            def action331():
                profileSpinAboutXxx.rate = 123456.789

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action331)
            # Offset
            self.m_logger.WriteLine6("\t\t\t\tThe current Offset is: {0}", profileSpinAboutXxx.offset)
            profileSpinAboutXxx.offset = 12.34
            self.m_logger.WriteLine6("\t\t\t\tThe new Offset is: {0}", profileSpinAboutXxx.offset)
            Assert.assertEqual(12.34, profileSpinAboutXxx.offset)

            def action332():
                profileSpinAboutXxx.offset = 1234.5

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action332)

        if oProfile.type == "GPS":
            oGPS: "IVehicleProfileGPS" = clr.Convert(oProfile, IVehicleProfileGPS)
            Assert.assertIsNotNone(oGPS)
            # ModelType
            self.m_logger.WriteLine6("\t\t\t\tThe current ModelType is: {0}", oGPS.model_type)
            oGPS.model_type = GPS_ATTITUDE_MODEL_TYPE.GSP_MODEL_BLOCK_IIA_NOMINAL
            self.m_logger.WriteLine6("\t\t\t\tThe new ModelType is: {0}", oGPS.model_type)
            Assert.assertEqual(GPS_ATTITUDE_MODEL_TYPE.GSP_MODEL_BLOCK_IIA_NOMINAL, oGPS.model_type)
            oGPS.model_type = GPS_ATTITUDE_MODEL_TYPE.GSP_MODEL_BLOCK_IIR_NOMINAL
            self.m_logger.WriteLine6("\t\t\t\tThe new ModelType is: {0}", oGPS.model_type)
            Assert.assertEqual(GPS_ATTITUDE_MODEL_TYPE.GSP_MODEL_BLOCK_IIR_NOMINAL, oGPS.model_type)
            oGPS.model_type = GPS_ATTITUDE_MODEL_TYPE.GSP_MODEL_GYM95
            self.m_logger.WriteLine6("\t\t\t\tThe new ModelType is: {0}", oGPS.model_type)
            Assert.assertEqual(GPS_ATTITUDE_MODEL_TYPE.GSP_MODEL_GYM95, oGPS.model_type)

            def action333():
                oGPS.model_type = GPS_ATTITUDE_MODEL_TYPE.MODEL_TYPE_UNKNOWN

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action333)

    # endregion

    # region Vector
    def Vector(self, oVector: "IVehicleVector"):
        Assert.assertIsNotNone(oVector)

        # AvailableReferenceVectors
        arAvailableReferenceVectors = oVector.available_reference_vectors

        # ReferenceVector
        self.m_logger.WriteLine5("\t\t\t\tThe current ReferenceVector is: {0}", oVector.reference_vector)
        oVector.reference_vector = "CentralBody/Moon Earth"
        self.m_logger.WriteLine5("\t\t\t\tThe new ReferenceVector is: {0}", oVector.reference_vector)
        Assert.assertEqual("CentralBody/Moon Earth", oVector.reference_vector)

        def action334():
            oVector.reference_vector = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action334)

        def action335():
            oVector.reference_vector = "InvalidReferenceVector"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action335)

        # Body
        oHelper = DirectionsTest()
        oHelper.Run(oVector.body)

    # endregion

    # region External
    def External(self, oExternal: "IVehicleAttitudeExternal"):
        self.m_logger.WriteLine("----- EXTERNAL ATT TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oExternal)
        # starting
        self.m_logger.WriteLine("\tStart of test")
        # Enabled
        self.m_logger.WriteLine4("\t\tThe current Enabled is: {0}", oExternal.enabled)
        # Filename
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oExternal.filename)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe current StartTime is: {0}", oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe current StopTime is: {0}", oExternal.stop_time)
        # override
        self.m_logger.WriteLine4("\t\tThe current Override value is: {0}", oExternal.override)

        self.m_logger.WriteLine("\tTest Reload")
        # Reload
        oExternal.reload()
        self.m_logger.WriteLine4("\t\tThe current Enabled is: {0}", oExternal.enabled)
        # Filename
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oExternal.filename)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe current StartTime is: {0}", oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe current StopTime is: {0}", oExternal.stop_time)
        # override
        self.m_logger.WriteLine4("\t\tThe current Override value is: {0}", oExternal.override)

        self.m_logger.WriteLine("\tTest Load - sets enabled, sets filename, then reloads")
        # Load
        oExternal.load(r"Scenario\Satellite1.a")

        def action336():
            oExternal.load("InvalidFileName.a")

        TryCatchAssertBlock.DoAssert("Should not allow to load an invalid file.", action336)

        def action337():
            oExternal.load("")

        TryCatchAssertBlock.DoAssert("Should not allow to load an invalid file.", action337)
        # Enabled
        self.m_logger.WriteLine4("\t\tThe new Enabled is: {0}", oExternal.enabled)
        # Filename
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oExternal.filename)
        # FilePath
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oExternal.file_path)
        Assert.assertEqual(TestBase.GetScenarioFile(oExternal.filename), oExternal.file_path)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe new StartTime is: {0}", oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe new StopTime is: {0}", oExternal.stop_time)
        # override
        self.m_logger.WriteLine4("\t\tThe new Override value is: {0}", oExternal.override)

        self.m_logger.WriteLine("\tTest Disable")
        # Disable
        oExternal.disable()
        # Enabled
        self.m_logger.WriteLine4("\t\tThe current Enabled is: {0}", oExternal.enabled)
        # Filename
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oExternal.filename)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe current StartTime is: {0}", oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe current StopTime is: {0}", oExternal.stop_time)
        # override
        self.m_logger.WriteLine4("\t\tThe current Override value is: {0}", oExternal.override)

        self.m_logger.WriteLine("\tTest Reload again")
        # Reload
        oExternal.reload()
        # Enabled
        self.m_logger.WriteLine4("\t\tThe new Enabled is: {0}", oExternal.enabled)
        # Filename
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oExternal.filename)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe new StartTime is: {0}", oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe new StopTime is: {0}", oExternal.stop_time)
        # override
        self.m_logger.WriteLine4("\t\tThe new Override value is: {0}", oExternal.override)

        startTimeNoOverride: str = str(oExternal.start_time)

        # test overriding the the times in the file
        self.m_logger.WriteLine("\tLoad and set Override to true")
        # Load
        oExternal.load(r"Scenario\Satellite1.a")
        oExternal.override = True
        # override
        self.m_logger.WriteLine4("\t\tThe current Override value is: {0}", oExternal.override)
        # Enabled
        self.m_logger.WriteLine4("\t\tThe current Enabled is: {0}", oExternal.enabled)
        # Filename
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oExternal.filename)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe current StartTime is: {0}", oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe current StopTime is: {0}", oExternal.stop_time)
        # AttStart
        self.m_logger.WriteLine6("\t\tThe current AttitudeStart is: {0}", oExternal.attitude_start_epoch.time_instant)

        # set an explicit time
        attStart: str = "1 Jul 1999 11:11:11.000"
        self.m_logger.WriteLine5("\tSet AttitudeStart to: {0}", attStart)
        oExternal.attitude_start_epoch.set_explicit_time(attStart)
        self.m_logger.WriteLine6("\t\tThe new AttitudeStart is: {0}", oExternal.attitude_start_epoch.time_instant)
        Assert.assertEqual(attStart, oExternal.attitude_start_epoch.time_instant)
        # Enabled
        self.m_logger.WriteLine4("\t\tThe new Enabled is: {0}", oExternal.enabled)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe new StartTime is: {0}", oExternal.start_time)
        Assert.assertEqual(attStart, oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe new StopTime is: {0}", oExternal.stop_time)

        # turn override off
        self.m_logger.WriteLine("\tTurn override off")
        oExternal.override = False
        # override
        self.m_logger.WriteLine4("\t\tThe new Override value is: {0}", oExternal.override)
        # Enabled
        self.m_logger.WriteLine4("\t\tThe new Enabled is: {0}", oExternal.enabled)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe new StartTime is: {0}", oExternal.start_time)
        Assert.assertEqual(startTimeNoOverride, oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe new StopTime is: {0}", oExternal.stop_time)
        # AttStart
        self.m_logger.WriteLine6("\t\tThe new AttitudeStart is: {0}", oExternal.attitude_start_epoch.time_instant)

        # set a new time instant but since not overriden, file times are unchanged
        self.m_logger.WriteLine("\tWhile override off, set new time instant--should have no effect")
        attStart2: str = "1 Jul 1999 22:22:22.000"
        oExternal.attitude_start_epoch.set_explicit_time(attStart2)
        self.m_logger.WriteLine6("\t\tThe new AttitudeStart is: {0}", oExternal.attitude_start_epoch.time_instant)
        # override
        self.m_logger.WriteLine4("\t\tThe current Override value is: {0}", oExternal.override)
        # Enabled
        self.m_logger.WriteLine4("\t\tThe current Enabled is: {0}", oExternal.enabled)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe current StartTime is: {0}", oExternal.start_time)
        Assert.assertEqual(startTimeNoOverride, oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe current StopTime is: {0}", oExternal.stop_time)

        # test overriding the the times in the file
        self.m_logger.WriteLine("\tSet Override to true again, uses updated time that was set previously")
        oExternal.override = True
        # override
        self.m_logger.WriteLine4("\t\tThe new Override value is: {0}", oExternal.override)
        # Enabled
        self.m_logger.WriteLine4("\t\tThe new Enabled is: {0}", oExternal.enabled)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe new StartTime is: {0}", oExternal.start_time)
        Assert.assertEqual(attStart2, oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe new StopTime is: {0}", oExternal.stop_time)
        # AttStart
        self.m_logger.WriteLine6("\t\tThe new AttitudeStart is: {0}", oExternal.attitude_start_epoch.time_instant)

        # use a time component
        attStart3: str = "1 Jul 1999 03:33:33.000"
        self.m_logger.WriteLine("\tCreate a time component for use with att overrride")
        scen: "IStkObject" = self.m_oApplication.current_scenario
        prv: "IAnalysisWorkbenchProvider" = scen.vgt
        grp: "ITimeToolEventGroup" = prv.events
        evt: "ITimeToolEvent" = prv.events.factory.create_event_epoch(
            "AttOverrideTest", "External Attitude - Override testing"
        )
        evtEpoch: "ITimeToolEventEpoch" = clr.CastAs(evt, ITimeToolEventEpoch)
        evtEpoch.epoch = attStart3

        self.m_logger.WriteLine("\tUse the time component for att overrride")
        oExternal.attitude_start_epoch.set_implicit_time(evt)
        # override
        self.m_logger.WriteLine4("\t\tThe new Override value is: {0}", oExternal.override)
        # Enabled
        self.m_logger.WriteLine4("\t\tThe new Enabled is: {0}", oExternal.enabled)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe new StartTime is: {0}", oExternal.start_time)
        Assert.assertEqual(attStart3, oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe new StopTime is: {0}", oExternal.stop_time)
        # AttStart
        refEvt: "ITimeToolEvent" = oExternal.attitude_start_epoch.reference_event
        res: "ITimeToolEventFindOccurrenceResult" = refEvt.find_occurrence()
        self.m_logger.WriteLine7("\t\tThe new AttitudeStart is: {0} and isValid: {1}", res.epoch, res.is_valid)

        # delete the time component
        self.m_logger.WriteLine("\tRemove the time component used with att overrride")
        grp.remove("AttOverrideTest")
        self.m_logger.WriteLine("\tAtt overrride should mainatin previous value, but be an explicit time")
        # override
        self.m_logger.WriteLine4("\t\tThe current Override value is: {0}", oExternal.override)
        # Enabled
        self.m_logger.WriteLine4("\t\tThe current Enabled is: {0}", oExternal.enabled)
        # StartTime
        self.m_logger.WriteLine6("\t\tThe current StartTime is: {0}", oExternal.start_time)
        Assert.assertEqual(attStart3, oExternal.start_time)
        # StopTime
        self.m_logger.WriteLine6("\t\tThe current StopTime is: {0}", oExternal.stop_time)
        # AttStart
        self.m_logger.WriteLine6("\t\tThe current AttitudeStart is: {0}", oExternal.attitude_start_epoch.time_instant)
        Assert.assertEqual(attStart3, oExternal.attitude_start_epoch.time_instant)

        self.m_logger.WriteLine("----- EXTERNAL ATT TEST ----- END -----")

    # endregion

    # region RateOffset
    def RateOffset(self, oOffset: "IVehicleRateOffset"):
        Assert.assertIsNotNone(oOffset)
        # Rate
        self.m_logger.WriteLine6("\t\t\t\tThe current Rate is: {0}", oOffset.rate)
        oOffset.rate = 123.4
        self.m_logger.WriteLine6("\t\t\t\tThe new Rate is: {0}", oOffset.rate)
        Assert.assertEqual(123.4, oOffset.rate)

        def action338():
            oOffset.rate = 123456.789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action338)
        # Offset
        self.m_logger.WriteLine6("\t\t\t\tThe current Offset is: {0}", oOffset.offset)
        oOffset.offset = 12.34
        self.m_logger.WriteLine6("\t\t\t\tThe new Offset is: {0}", oOffset.offset)
        Assert.assertEqual(12.34, oOffset.offset)

        def action339():
            oOffset.offset = 1234.5

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action339)

    # endregion

    # region Pointing
    def Pointing(self, oPointing: "IVehicleAttitudePointing"):
        self.m_logger.WriteLine("----- POINTING TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oPointing)
        # UseTargetPointing (false)
        self.m_logger.WriteLine4("\tThe current UseTargetPointing is: {0}", oPointing.use_target_pointing)
        oPointing.use_target_pointing = False
        self.m_logger.WriteLine4("\tThe new UseTargetPointing is: {0}", oPointing.use_target_pointing)
        Assert.assertFalse(oPointing.use_target_pointing)
        # Targets (readonly)
        self.Targets(oPointing, True)
        # TargetTimes (readonly)
        self.TargetTimes(oPointing.target_times, True)
        # Advanced (readonly)
        self.Advanced(oPointing.advanced, True)

        # UseTargetPointing (true)
        oPointing.use_target_pointing = True
        self.m_logger.WriteLine4("\tThe new UseTargetPointing is: {0}", oPointing.use_target_pointing)
        Assert.assertTrue(oPointing.use_target_pointing)
        # Targets
        self.Targets(oPointing, False)
        # TargetTimes
        self.TargetTimes(oPointing.target_times, False)
        # Advanced
        self.Advanced(oPointing.advanced, False)
        self.m_logger.WriteLine("----- POINTING TEST ----- END -----")

    # endregion

    # region Advanced
    def Advanced(self, oAdvanced: "IVehicleAccessAdvanced", bReadOnly: bool):
        self.m_logger.WriteLine4("----- ADVANCED ACCESS TEST (ReadOnly = {0}) ----- BEGIN -----", bReadOnly)
        oEDHelper = AccessEventDetectionHelper()
        oSHelper = AccessSamplingHelper()
        if bReadOnly:

            def action340():
                oAdvanced.use_light_time_delay = True

            # UseLightTimeDelay (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action340)

            def action341():
                oAdvanced.time_sense = IV_TIME_SENSE.RECEIVE

            # TimeSense (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action341)

            def action342():
                oAdvanced.time_delay_convergence = 0.1

            # TimeDelayConvergence (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action342)

            def action343():
                (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.ANNUAL

            # AberrationType (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action343)
            # EventDetection (readonly)
            oEDHelper.Run(oAdvanced.event_detection, bReadOnly)
            # Sampling (readonly)
            oSHelper.Run(oAdvanced.sampling, bReadOnly)

        else:
            # UseLightTimeDelay (false)
            self.m_logger.WriteLine4("\tThe current UseLightTimeDelay is: {0}", oAdvanced.use_light_time_delay)
            oAdvanced.use_light_time_delay = False
            self.m_logger.WriteLine4("\tThe new UseLightTimeDelay is: {0}", oAdvanced.use_light_time_delay)
            Assert.assertFalse(oAdvanced.use_light_time_delay)

            def action344():
                oAdvanced.time_sense = IV_TIME_SENSE.RECEIVE

            # TimeSense (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action344)

            def action345():
                oAdvanced.time_delay_convergence = 0.1

            # TimeDelayConvergence (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action345)

            def action346():
                (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.ANNUAL

            # AberrationType (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action346)
            # UseLightTimeDelay (true)
            oAdvanced.use_light_time_delay = True
            self.m_logger.WriteLine4("\tThe new UseLightTimeDelay is: {0}", oAdvanced.use_light_time_delay)
            Assert.assertTrue(oAdvanced.use_light_time_delay)
            # AberrationType
            self.m_logger.WriteLine6("\tThe current AberrationType is: {0}", oAdvanced.aberration_type)
            (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.ANNUAL
            self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
            Assert.assertEqual(ABERRATION_TYPE.ANNUAL, oAdvanced.aberration_type)
            (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.NONE
            self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
            Assert.assertEqual(ABERRATION_TYPE.NONE, oAdvanced.aberration_type)
            (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.TOTAL
            self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
            Assert.assertEqual(ABERRATION_TYPE.TOTAL, oAdvanced.aberration_type)

            def action347():
                (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.UNKNOWN

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action347)
            # TimeDelayConvergence
            self.m_logger.WriteLine6("\tThe current TimeDelayConvergence is: {0}", oAdvanced.time_delay_convergence)
            oAdvanced.time_delay_convergence = 0.1
            self.m_logger.WriteLine6("\tThe new TimeDelayConvergence is: {0}", oAdvanced.time_delay_convergence)
            Assert.assertEqual(0.1, oAdvanced.time_delay_convergence)

            def action348():
                oAdvanced.time_delay_convergence = 0.5

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action348)
            # TimeSense
            self.m_logger.WriteLine6("\tThe current TimeSense is: {0}", oAdvanced.time_sense)
            oAdvanced.time_sense = IV_TIME_SENSE.RECEIVE
            self.m_logger.WriteLine6("\tThe new TimeSense is: {0}", oAdvanced.time_sense)
            Assert.assertEqual(IV_TIME_SENSE.RECEIVE, oAdvanced.time_sense)
            oAdvanced.time_sense = IV_TIME_SENSE.TRANSMIT
            self.m_logger.WriteLine6("\tThe new TimeSense is: {0}", oAdvanced.time_sense)
            Assert.assertEqual(IV_TIME_SENSE.TRANSMIT, oAdvanced.time_sense)

            def action349():
                oAdvanced.time_sense = IV_TIME_SENSE.UNKNOWN

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action349)
            # EventDetection
            oEDHelper.Run(oAdvanced.event_detection, bReadOnly)
            # Sampling
            oSHelper.Run(oAdvanced.sampling, bReadOnly)

        self.m_logger.WriteLine4("----- ADVANCED ACCESS TEST (ReadOnly = {0}) ----- END -----", bReadOnly)

    # endregion

    # region Targets
    def Targets(self, oPointing: "IVehicleAttitudePointing", bReadOnly: bool):
        oCollection: "IVehicleTargetPointingCollection" = oPointing.targets

        self.m_logger.WriteLine("----- TARGETS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        self.m_logger.WriteLine3("\tThe current TargetPointing collection contains: {0} elements.", oCollection.count)

        i: int = 0
        while i < oCollection.count:
            element: "IVehicleTargetPointingElement" = oCollection[i]

            i += 1

        element: "IVehicleTargetPointingElement"
        for element in oCollection:
            lat: float = element.latitude

        def action350():
            element2: "IVehicleTargetPointingElement" = oCollection[oCollection.count]

        TryCatchAssertBlock.DoAssert("IVehicleTargetPointingCollection bad index", action350)

        arTargets = oCollection.available_targets
        self.m_logger.WriteLine3("\tThe TargetPointing collection has: {0} available targets.", Array.Length(arTargets))
        if bReadOnly:
            if Array.Length(arTargets) > 0:

                def action351():
                    oCollection.add(str(arTargets[0]))

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action351)

            if Array.Length(arTargets) > 0:
                oCollection.add_position_as_target(10.0, 20.0, 30.0)
                e0: "IVehicleTargetPointingElement" = oCollection[0]

                def action352():
                    oCollection.add_position_as_target(-10000.0, -10000.0, -10000.0)

                TryCatchAssertBlock.DoAssert("AddPositionAsTarget bad params.", action352)

            if oCollection.count > 0:

                def action353():
                    oCollection.remove_at(0)

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action353)

            if oCollection.count > 0:

                def action354():
                    oCollection.remove(str(arTargets[0]))

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action354)

            def action355():
                oCollection.remove_all()

            # RemoveAll
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action355)

        else:
            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3("\tThe new TargetPointing collection contains: {0} elements.", oCollection.count)
            Assert.assertEqual(0, oCollection.count)

            def action356():
                oCollection.add("Bogus")

            TryCatchAssertBlock.DoAssert("Should not allow to add a bad target.", action356)

            strTarget: str = ""

            iIndex: int = 0
            while iIndex < Array.Length(arTargets):
                strTarget = str(arTargets[iIndex])
                if oCollection.contains(strTarget):
                    Assert.fail("Collection should not contain Target: {0}", strTarget)

                # Add
                oElem: "IVehicleTargetPointingElement" = oCollection.add(strTarget)
                Assert.assertIsNotNone(oElem)
                self.m_logger.WriteLine5("\t\tThe {0} Target was added into the collection.", strTarget)
                if not oCollection.contains(strTarget):
                    Assert.fail("Collection should contain Target: {0}", strTarget)

                iIndex += 1

            self.m_logger.WriteLine3("\tThe new TargetPointing collection contains: {0} elements.", oCollection.count)
            Assert.assertEqual(Array.Length(arTargets), oCollection.count)

            # Remove
            oCollection.remove(strTarget)
            Assert.assertEqual((Array.Length(arTargets) - 1), oCollection.count)
            self.m_logger.WriteLine3("\tThe new TargetPointing collection contains: {0} elements.", oCollection.count)

            def action357():
                oCollection.remove("Bogus")

            TryCatchAssertBlock.DoAssert("Should not remove thru bad name.", action357)

            # RemoveAt
            oCollection.remove_at(0)
            Assert.assertEqual((Array.Length(arTargets) - 2), oCollection.count)
            self.m_logger.WriteLine3("\tThe new TargetPointing collection contains: {0} elements.", oCollection.count)

            def action358():
                oCollection.remove_at(-1)

            TryCatchAssertBlock.DoAssert("Should not remove thru bad index -1.", action358)

            def action359():
                oCollection.remove_at(oCollection.count)

            TryCatchAssertBlock.DoAssert("Should not remove thru bad index.", action359)

            # Item
            targetPointingElement: "IVehicleTargetPointingElement" = oCollection[0]
            Assert.assertIsNotNone(targetPointingElement)

            # AlignedVector
            oHelper = DirectionsTest()
            oHelper.Run(targetPointingElement.aligned_vector)
            # ConstrainedVector
            oHelper.Run(targetPointingElement.constrained_vector)
            # ConstrainedVectorReference
            self.m_logger.WriteLine5(
                "\tThe current ConstrainedVectorReference is: {0}", targetPointingElement.constrained_vector_reference
            )
            targetPointingElement.constrained_vector_reference = "CentralBody/Io Sun(True)"
            self.m_logger.WriteLine5(
                "\tThe new ConstrainedVectorReference is: {0}", targetPointingElement.constrained_vector_reference
            )
            Assert.assertEqual("CentralBody/Io Sun(True)", targetPointingElement.constrained_vector_reference)

            def action360():
                targetPointingElement.constrained_vector_reference = ""

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action360)

            def action361():
                targetPointingElement.constrained_vector_reference = "InvalidReferenceVector"

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action361)
            # ResetConstrainedVectorReference
            self.m_logger.WriteLine4(
                "\tThe current ResetConstrainedVectorReference is: {0}",
                targetPointingElement.reset_constrained_vector_reference(),
            )
            Assert.assertTrue(targetPointingElement.reset_constrained_vector_reference())
            # Target
            oLTO = LinkToObjectHelper()
            oLTO.Run(targetPointingElement.target, targetPointingElement.target.name)
            # -----------------------------------------------------
            # LLA points as pointing attitude targets
            # -----------------------------------------------------
            self.m_logger.WriteLine8(
                "Latitude: {0}, Longitude: {1}, Altitude: {2}",
                targetPointingElement.latitude,
                targetPointingElement.longitude,
                targetPointingElement.altitude,
            )
            intervals: "IVehicleTargetPointingIntervalCollection" = targetPointingElement.intervals

            useAccessTimes: bool = oPointing.target_times.use_access_times
            oPointing.target_times.use_access_times = False
            prevCount: int = intervals.count
            # -----------------------------------------------------
            # Verify the adding and removing of intervals
            # -----------------------------------------------------
            intervals.add("1 Jul 2005 13:00", "1 Jul 2005 13:30")
            intervals.add("1 Jul 2005 13:40", "1 Jul 2005 13:50")
            Assert.assertEqual(intervals.count, (prevCount + 2))

            ste: "IVehicleScheduleTimesElement"

            for ste in intervals:
                steString: str = str(ste)

            i: int = 0
            while i < intervals.count:
                steString: str = str(intervals[i])

                i += 1

            intervals.remove_at((intervals.count - 1))
            intervals.remove_at((intervals.count - 1))
            Assert.assertEqual(intervals.count, prevCount)
            # -----------------------------------------------------
            # Verify the data integrity
            # -----------------------------------------------------
            prevCount = oPointing.target_times.schedule_times.count
            intervals.add("1 Jul 2005 13:00", "1 Jul 2005 13:30")
            intervals.add("1 Jul 2005 13:40", "1 Jul 2005 13:50")
            Assert.assertEqual((prevCount + 2), oPointing.target_times.schedule_times.count)
            intervals.remove_at((intervals.count - 1))
            intervals.remove_at((intervals.count - 1))
            Assert.assertEqual(prevCount, oPointing.target_times.schedule_times.count)

            intervals.remove_all()
            Assert.assertEqual(0, intervals.count)

            oPointing.target_times.use_access_times = useAccessTimes

        self.m_logger.WriteLine("----- TARGETS TEST ----- END -----")

    # endregion

    # region TargetTimes
    def TargetTimes(self, oTimes: "IVehicleTargetTimes", bReadOnly: bool):
        self.m_logger.WriteLine("----- TARGET TIMES TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oTimes)

        oATH = AccessTimeHelper()
        oSTH = ScheduleTimesHelper()
        if bReadOnly:

            def action362():
                oTimes.use_access_times = True

            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action362)
            # AccessTimes
            oATH.Run(oTimes.access_times)
            # ScheduleTimes (readonly)
            oSTH.Run(oTimes.schedule_times, True)

        else:
            # UseAccessTimes (true)
            self.m_logger.WriteLine4("\tThe current UseAccessTimes is: {0}", oTimes.use_access_times)
            oTimes.use_access_times = True
            self.m_logger.WriteLine4("\tThe new UseAccessTimes is: {0}", oTimes.use_access_times)
            Assert.assertTrue(oTimes.use_access_times)
            # AccessTimes
            oATH.Run(oTimes.access_times)
            # ScheduleTimes (readonly)
            oSTH.Run(oTimes.schedule_times, True)
            # UseAccessTimes (false)
            oTimes.use_access_times = False
            self.m_logger.WriteLine4("\tThe new UseAccessTimes is: {0}", oTimes.use_access_times)
            Assert.assertFalse(oTimes.use_access_times)
            # AccessTimes
            oATH.Run(oTimes.access_times)
            # ScheduleTimes
            oSTH.Run(oTimes.schedule_times, False)
            # Deconflict
            oTimes.use_access_times = True
            oATH.Run(oTimes.access_times)
            oTimes.deconflict()

        self.m_logger.WriteLine("----- TARGET TIMES TEST ----- END -----")

    # endregion

    # region IntegratedAttitude
    def IntegratedAttitude(self, oAttitude: "IVehicleIntegratedAttitude"):
        self.m_logger.WriteLine("----- THE INTEGRATED ATTITUDE TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oAttitude)
        # StartTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oAttitude.start_time)
        oAttitude.start_time = "1 Jul 1999 00:00:00.000"
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oAttitude.start_time)
        Assert.assertEqual("1 Jul 1999 00:00:00.000", oAttitude.start_time)
        # StopTime
        self.m_logger.WriteLine6("\tThe current StopTime is: {0}", oAttitude.stop_time)
        oAttitude.stop_time = "1 Jul 1999 01:00:00.000"
        self.m_logger.WriteLine6("\tThe new StopTime is: {0}", oAttitude.stop_time)
        Assert.assertEqual("1 Jul 1999 01:00:00.000", oAttitude.stop_time)
        # Epoch
        self.m_logger.WriteLine6("\tThe current Epoch is: {0}", oAttitude.epoch)
        oAttitude.epoch = "1 Jul 1999 00:00:00.100"
        self.m_logger.WriteLine6("\tThe new Epoch is: {0}", oAttitude.epoch)
        Assert.assertEqual("1 Jul 1999 00:00:00.100", oAttitude.epoch)
        # Orientation
        oHelper = OrientationTest(self.m_oUnits)
        oHelper.Run(
            oAttitude.orientation, ((Orientations.EulerAngles | Orientations.Quaternion) | Orientations.YPRAngles)
        )
        # Wx
        self.m_logger.WriteLine6("\tThe current Wx is: {0}", oAttitude.wx)
        oAttitude.wx = 0.000174533
        self.m_logger.WriteLine6("\tThe new Wx is: {0}", oAttitude.wx)
        Assert.assertEqual(0.000174533, oAttitude.wx)

        def action363():
            oAttitude.wx = 1234567.89

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action363)
        # Wy
        self.m_logger.WriteLine6("\tThe current Wy is: {0}", oAttitude.wy)
        oAttitude.wy = 0.000349066
        self.m_logger.WriteLine6("\tThe new Wy is: {0}", oAttitude.wy)
        Assert.assertEqual(0.000349066, oAttitude.wy)

        def action364():
            oAttitude.wy = 1234567.89

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action364)
        # Wz
        self.m_logger.WriteLine6("\tThe current Wz is: {0}", oAttitude.wz)
        oAttitude.wz = 0.000523599
        self.m_logger.WriteLine6("\tThe new Wz is: {0}", oAttitude.wz)
        Assert.assertEqual(0.000523599, oAttitude.wz)

        def action365():
            oAttitude.wz = 1234567.89

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action365)

        oAttitude.save_to_file("Satellite2.a")

        # InitFromAtt
        oAttitude.init_from_attitude()

        oAttitude.save_to_file("Satellite2.a")

        # Torque
        oTorque: "IVehicleTorque" = oAttitude.torque
        Assert.assertIsNotNone(oTorque)
        # UseTorqueFile
        self.m_logger.WriteLine4("\tThe current UseTorqueFile is: {0}", oTorque.use_torque_file)
        oTorque.use_torque_file = False
        self.m_logger.WriteLine4("\tThe new UseTorqueFile is: {0}", oTorque.use_torque_file)
        Assert.assertFalse(oTorque.use_torque_file)

        def action366():
            oTorque.torque_file = r"..\..\..\Scenario\TorquesTimeBodyFixed.tq"

        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action366)
        oTorque.use_torque_file = True
        self.m_logger.WriteLine4("\tThe new UseTorqueFile is: {0}", oTorque.use_torque_file)
        Assert.assertTrue(oTorque.use_torque_file)
        # TorqueFile
        self.m_logger.WriteLine5("\tThe current TorqueFile is: {0}", oTorque.torque_file)
        oTorque.torque_file = TestBase.GetScenarioFile(r"TorquesTimeBodyFixed.tq")
        self.m_logger.WriteLine5("\tThe new TorqueFile is: {0}", oTorque.torque_file)
        Assert.assertEqual("TorquesTimeBodyFixed.tq", oTorque.torque_file)

        def action367():
            oTorque.torque_file = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action367)

        def action368():
            oTorque.torque_file = "InvalidFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action368)
        oAttitude.save_to_file("Satellite2.a")
        self.m_logger.WriteLine("----- THE INTEGRATED ATTITUDE TEST ----- END -----")


# endregion


# region AccessTimeHelper
class AccessTimeHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "IAccessTimeCollection"):
        self.m_logger.WriteLine("----- ACCESS TIME COLLECTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\tThe current AccessTime collection contains: {0} elements.", oCollection.count)
        # _NewEnum
        accessTime: "IAccessTime"
        # _NewEnum
        for accessTime in oCollection:
            self.m_logger.WriteLine8(
                "\t\tElement: Target = {0}, StartTime = {1}, StopTime = {2}",
                accessTime.target,
                accessTime.start_time,
                accessTime.stop_time,
            )

        def action369():
            oTime: "IAccessTime" = oCollection[oCollection.count]

        # Item
        TryCatchAssertBlock.DoAssert("Bad IAccessTimeCollection index", action369)
        if oCollection.count > 0:
            oTime: "IAccessTime" = oCollection[0]
            Assert.assertIsNotNone(oTime)
            self.m_logger.WriteLine8(
                "\tThe first element: Target = {0}, StartTime = {1}, StopTime = {2}",
                oTime.target,
                oTime.start_time,
                oTime.stop_time,
            )

        self.m_logger.WriteLine("----- ACCESS TIME COLLECTION TEST ----- END -----")


# endregion


# region ScheduleTimesHelper
class ScheduleTimesHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "IVehicleScheduleTimesCollection", bReadOnly: bool):
        self.m_logger.WriteLine("----- SCHEDULE TIMES COLLECTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\tThe current ScheduleTimes collection contains: {0} elements.", oCollection.count)
        if bReadOnly:

            def action370():
                oCollection.add("Satellite/Satellite1")

            # Add
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action370)

            def action371():
                oCollection.remove_at(0)

            # RemoveAt
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action371)

            def action372():
                oCollection.remove_all()

            # RemoveAll
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action372)

        else:
            arAvailTargets = oCollection.available_targets

            i: int = 0
            while i < Array.Length(arAvailTargets):
                name: str = clr.Convert(arAvailTargets[i], str)

                i += 1

            # Add
            oNew: "IVehicleScheduleTimesElement" = oCollection.add(r"AreaTarget/AreaTarget1")
            Assert.assertIsNotNone(oNew)

            i: int = 0
            while i < oCollection.count:
                element: "IVehicleScheduleTimesElement" = oCollection[i]

                i += 1

            # _NewEnum
            scheduleTimesElement: "IVehicleScheduleTimesElement"
            # _NewEnum
            for scheduleTimesElement in oCollection:
                self.m_logger.WriteLine8(
                    "\t\tElement: Target = {0}, Start = {1}, Stop = {2}",
                    scheduleTimesElement.target.name,
                    scheduleTimesElement.start,
                    scheduleTimesElement.stop,
                )

            def action373():
                element: "IVehicleScheduleTimesElement" = oCollection[oCollection.count]

            TryCatchAssertBlock.DoAssert("IVehicleScheduleTimesCollection bad index", action373)

            def action374():
                oCollection.add("bogus")

            TryCatchAssertBlock.DoAssert("bogus schedule time element", action374)

            # Item
            oTime: "IVehicleScheduleTimesElement" = oCollection[0]
            nameX: str = oTime.target.name
            start: str = clr.Convert(oTime.start, str)
            stop: str = clr.Convert(oTime.stop, str)
            Assert.assertIsNotNone(oTime)

            # Start
            self.m_logger.WriteLine6("\tThe current Start is: {0}", oNew.start)
            oNew.start = start
            self.m_logger.WriteLine6("\tThe new Start is: {0}", oNew.start)
            Assert.assertEqual(start, oNew.start)
            # Stop
            self.m_logger.WriteLine6("\tThe current Stop is: {0}", oNew.stop)
            oNew.stop = stop
            self.m_logger.WriteLine6("\tThe new Stop is: {0}", oNew.stop)
            Assert.assertEqual(stop, oNew.stop)
            # Target
            oLTO = LinkToObjectHelper()
            oLTO.Run(oNew.target, nameX)

            def action375():
                oCollection.remove_at(oCollection.count)

            # RemoveAt
            TryCatchAssertBlock.DoAssert("oCollection.RemoveAt(oCollection.Count)", action375)

            oCollection.remove_at(0)
            self.m_logger.WriteLine3("\tThe new ScheduleTimes collection contains: {0} elements.", oCollection.count)

            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3("\tThe new ScheduleTimes collection contains: {0} elements.", oCollection.count)
            Assert.assertEqual(0, oCollection.count)

        self.m_logger.WriteLine("----- SCHEDULE TIMES COLLECTION TEST ----- END -----")


# endregion


# region BasicAttitudeRealTimeHelper
class BasicAttitudeRealTimeHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot", o: "IStkObject"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        Assert.assertIsNotNone(o)
        self._application: "IStkObjectRoot" = oApplication
        self._obj: "IStkObject" = o
        oApplication.unit_preferences.reset_units()

    # endregion

    def FindDataSet(self, datasets: "IDataProviderResultDataSetCollection", dsName: str):
        Assert.assertIsNotNone(datasets)
        Assert.assertIsNotNone(dsName)
        ds: "IDataProviderResultDataSet"
        for ds in datasets:
            if ds.element_name == dsName:
                return ds

        return None

    def CreateTrajectory(self, ga: "IVehiclePropagatorGreatArc", startTime: typing.Any, stopTime: typing.Any):
        MAX_POINTS: int = 100

        Assert.assertIsNotNone(startTime)
        Assert.assertIsNotNone(stopTime)
        Assert.assertIsNotNone(ga)

        dtStart: "IDate" = self._application.conversion_utility.new_date(
            self._application.unit_preferences.get_current_unit_abbrv("DateFormat"), str(startTime)
        )
        dtStop: "IDate" = self._application.conversion_utility.new_date(
            self._application.unit_preferences.get_current_unit_abbrv("DateFormat"), str(stopTime)
        )
        #
        # dtIncrement is used to add waypoints to aircraft, groundvehicle and ship objects
        #
        dtSpan: "IQuantity" = dtStop.span(dtStart)
        dtSpan.convert_to_unit("sec")

        ga.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME
        # ga.StartTime = startTime;
        # ga.StopTime = stopTime;
        increment: float = dtSpan.value / MAX_POINTS
        dtTime: "IDate" = self._application.conversion_utility.new_date(
            self._application.unit_preferences.get_current_unit_abbrv("DateFormat"), str(startTime)
        )

        i: int = 0
        while i < MAX_POINTS:
            wp: "IVehicleWaypointsElement" = ga.waypoints.add()
            wp.longitude = Math.Sin((i / 180))
            wp.latitude = Math.Sin((i / 360))
            dtTime = dtTime.add("sec", increment)
            wp.time = dtTime.format(self._application.unit_preferences.get_current_unit_abbrv("DateFormat"))

            i += 1

    # region Run method
    def Run(self, oAttitude: "IVehicleAttitudeRealTime"):
        resultA: "IDataProviderResult" = None
        resultB: "IDataProviderResult" = None

        dpi: "IDataProviderInfo" = None
        tvdp: "IDataProviderTimeVarying" = None
        reportStep: float = 600
        reportedStartTime: typing.Any = None
        reportedStopTime: typing.Any = None
        times = None
        dtIncrement: int = 600  #  (int)((dtSpan.Value + 100) / (data.Length >> 2));

        # Attitude data
        data = [
            -1.8e-05,
            0.259177,
            -5e-06,
            0.96583,
            0.064406,
            0.250368,
            -0.745037,
            -0.614889,
            0.125592,
            0.226451,
            0.948322,
            -0.183388,
            0.177673,
            0.188329,
            -0.462312,
            0.848075,
            0.219083,
            0.13728,
            -0.360035,
            -0.896399,
            0.246968,
            0.078609,
            0.920358,
            0.292864,
            0.258109,
            0.014546,
            -0.811851,
            0.523514,
            0.253873,
            -0.051011,
            0.112796,
            -0.959283,
            0.233338,
            -0.1122,
            0.667966,
            0.697701,
            0.19725,
            -0.16714,
            -0.963367,
            0.071278,
            0.149797,
            -0.211503,
            0.558148,
            -0.788225,
            0.092129,
            -0.241546,
            0.252697,
            0.932369,
            0.028373,
            -0.257388,
            -0.879918,
            -0.39836,
            -0.036161,
            -0.256375,
            0.867394,
            -0.424961,
            -0.099458,
            -0.238645,
            -0.22419,
            0.939625,
            -0.156121,
            -0.206878,
            -0.581874,
            -0.770876,
            -0.202236,
            -0.161036,
            0.965096,
            0.041913,
            -0.236665,
            -0.105086,
            -0.646415,
            0.717701,
            -0.255269,
            -0.043283,
            -0.141942,
            -0.955414,
            -0.257568,
            0.02241,
            0.827409,
            0.498549,
            -0.244479,
            0.086038,
            -0.91102,
            0.320734,
        ]

        startTime: typing.Any = None
        stopTime: typing.Any = None

        elements = ["Time", "q1", "q2", "q3", "q4"]

        startTime = "1 Jul 2007 12:00:00.000"
        #
        # Define a span of 60000 seconds
        #
        dtStart: "IDate" = self._application.conversion_utility.new_date(
            self._application.unit_preferences.get_current_unit_abbrv("DateFormat"), str(startTime)
        )
        dtStop: "IDate" = dtStart.add("sec", 60000)
        #
        # stopTime is used in the following code to propagate the vehicle's ephemeris
        #
        stopTime = dtStop.format(self._application.unit_preferences.get_current_unit_abbrv("DateFormat"))
        #
        # dtTime is a sliding time used when adding attitude quaternions
        #
        dtTime: "IDate" = self._application.conversion_utility.new_date(
            self._application.unit_preferences.get_current_unit_abbrv("DateFormat"), str(startTime)
        )

        self.m_logger.WriteLine6("Ephemeris and attitude start time: {0}", startTime)
        self.m_logger.WriteLine6("Ephemeris and attitude stop time:  {0}", stopTime)
        self.m_logger.WriteLine5("Start time in seconds: {0} ", dtStart.format("EpSec"))
        self.m_logger.WriteLine5(" Stop time in seconds: {0} ", dtStop.format("EpSec"))
        if self._obj.class_type == STK_OBJECT_TYPE.SATELLITE:
            # Re-propagate the satellite
            AG_SAT: "ISatellite" = clr.Convert(self._obj, ISatellite)
            AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
            tb: "IVehiclePropagatorTwoBody" = clr.CastAs(AG_SAT.propagator, IVehiclePropagatorTwoBody)
            tb.ephemeris_interval.set_explicit_interval(startTime, stopTime)
            tb.propagate()
            startTime = tb.ephemeris_interval.find_start_time()
            stopTime = tb.ephemeris_interval.find_stop_time()

        elif self._obj.class_type == STK_OBJECT_TYPE.SHIP:
            AG_SH: "IShip" = clr.Convert(self._obj, IShip)
            AG_SH.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            ga: "IVehiclePropagatorGreatArc" = clr.CastAs(AG_SH.route, IVehiclePropagatorGreatArc)
            self.CreateTrajectory(ga, startTime, stopTime)
            startTime = ga.ephemeris_interval.find_start_time()
            stopTime = ga.ephemeris_interval.find_stop_time()

        elif self._obj.class_type == STK_OBJECT_TYPE.AIRCRAFT:
            AG_AC: "IAircraft" = clr.Convert(self._obj, IAircraft)
            AG_AC.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            ga: "IVehiclePropagatorGreatArc" = clr.CastAs(AG_AC.route, IVehiclePropagatorGreatArc)
            self.CreateTrajectory(ga, startTime, stopTime)
            startTime = ga.ephemeris_interval.find_start_time()
            stopTime = ga.ephemeris_interval.find_stop_time()

        elif self._obj.class_type == STK_OBJECT_TYPE.GROUND_VEHICLE:
            AG_GV: "IGroundVehicle" = clr.Convert(self._obj, IGroundVehicle)
            AG_GV.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            ga: "IVehiclePropagatorGreatArc" = clr.CastAs(AG_GV.route, IVehiclePropagatorGreatArc)
            self.CreateTrajectory(ga, startTime, stopTime)
            startTime = ga.ephemeris_interval.find_start_time()
            stopTime = ga.ephemeris_interval.find_stop_time()

        elif self._obj.class_type == STK_OBJECT_TYPE.MISSILE:
            AG_MS: "IMissile" = clr.Convert(self._obj, IMissile)
            AG_MS.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
            tb: "IVehiclePropagatorTwoBody" = clr.CastAs(AG_MS.trajectory, IVehiclePropagatorTwoBody)
            tb.ephemeris_interval.set_explicit_interval(startTime, stopTime)
            tb.propagate()
            startTime = tb.ephemeris_interval.find_start_time()
            stopTime = tb.ephemeris_interval.find_stop_time()

        elif self._obj.class_type == STK_OBJECT_TYPE.LAUNCH_VEHICLE:
            AG_LV: "ILaunchVehicle" = clr.Convert(self._obj, ILaunchVehicle)
            AG_LV.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT)
            sa: "IVehiclePropagatorSimpleAscent" = clr.CastAs(AG_LV.trajectory, IVehiclePropagatorSimpleAscent)
            sa.ephemeris_interval.set_explicit_interval(startTime, stopTime)
            sa.propagate()

            startTime = sa.ephemeris_interval.find_start_time()
            stopTime = sa.ephemeris_interval.find_stop_time()

        self.m_logger.WriteLine("----- REALTIME ATTITUDE TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oAttitude)
        # LookAheadMethod (eExtrapolate)
        self.m_logger.WriteLine6("\tThe current LookAheadMethod is: {0}", oAttitude.look_ahead_method)
        oAttitude.look_ahead_method = VEHICLE_LOOK_AHEAD_METHOD.EXTRAPOLATE
        self.m_logger.WriteLine6("\tThe new LookAheadMethod is: {0}", oAttitude.look_ahead_method)
        Assert.assertEqual(VEHICLE_LOOK_AHEAD_METHOD.EXTRAPOLATE, oAttitude.look_ahead_method)
        # LookAheadMethod (eHold)
        oAttitude.look_ahead_method = VEHICLE_LOOK_AHEAD_METHOD.HOLD
        self.m_logger.WriteLine6("\tThe new LookAheadMethod is: {0}", oAttitude.look_ahead_method)
        Assert.assertEqual(VEHICLE_LOOK_AHEAD_METHOD.HOLD, oAttitude.look_ahead_method)
        # Duration
        oDuration: "IVehicleDuration" = oAttitude.duration
        Assert.assertIsNotNone(oDuration)
        # LookAhead
        self.m_logger.WriteLine6("\tThe current LookAhead is: {0}", oDuration.look_ahead)
        oDuration.look_ahead = 123.456
        self.m_logger.WriteLine6("\tThe new LookAhead is: {0}", oDuration.look_ahead)
        Assert.assertEqual(123.456, oDuration.look_ahead)

        def action376():
            oDuration.look_ahead = 0

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action376)
        # LookBehind
        self.m_logger.WriteLine6("\tThe current LookBehind is: {0}", oDuration.look_behind)
        oDuration.look_behind = 456.789
        self.m_logger.WriteLine6("\tThe new LookBehind is: {0}", oDuration.look_behind)
        Assert.assertEqual(456.789, oDuration.look_behind)

        def action377():
            oDuration.look_behind = 123456789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action377)

        # BlockFactor
        oAttitude.block_factor = 20
        Assert.assertEqual(20, oAttitude.block_factor)
        oAttitude.block_factor = 40
        Assert.assertEqual(40, oAttitude.block_factor)

        def action378():
            oAttitude.block_factor = 19

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action378)
        if oAttitude.data_reference.profile_type == VEHICLE_PROFILE.PROFILE_UNKNOWN:
            Assert.assertIsNone(oAttitude.data_reference.profile)

        # Enumerate supported profiles and verify each one by setting it
        # as a datareference profile.
        supportedProfileTypes = oAttitude.data_reference.profile_supported_types

        i: int = 0
        while i < len(supportedProfileTypes):
            profileid: "VEHICLE_PROFILE" = clr.Convert(int(supportedProfileTypes[i][0]), VEHICLE_PROFILE)
            self.m_logger.WriteLine6("DataReference: {0}", profileid)
            oAttitude.data_reference.set_profile_type(profileid)
            Assert.assertIsNotNone(oAttitude.data_reference.profile)

            i += 1

        # Reset datareference profile
        oAttitude.clear_all()

        Assert.assertIsNone(oAttitude.data_reference.profile)
        Assert.assertEqual(oAttitude.data_reference.profile_type, VEHICLE_PROFILE.PROFILE_UNKNOWN)

        pos: int = 0
        while pos < Array.Length(data):
            time: str = dtTime.format("UTCG")
            oAttitude.add_quaternion(
                time, float(data[pos]), float(data[(pos + 1)]), float(data[(pos + 2)]), float(data[(pos + 3)])
            )

            oAttitude.add_cbf_quaternion(
                time, float(data[pos]), float(data[(pos + 1)]), float(data[(pos + 2)]), float(data[(pos + 3)])
            )

            oAttitude.add_ypr(time, "123", float(data[(pos + 1)]), float(data[(pos + 2)]), float(data[(pos + 3)]))

            oAttitude.add_eciypr(time, "123", float(data[(pos + 1)]), float(data[(pos + 2)]), float(data[(pos + 3)]))

            oAttitude.add_euler(time, "123", float(data[(pos + 1)]), float(data[(pos + 2)]), float(data[(pos + 3)]))

            dtTime = dtTime.add("sec", float(dtIncrement))

            pos += 4

        # Get a report using the data providers API
        try:
            dpi = self._obj.data_providers["Attitude Quaternions"]
            Assert.assertFalse(dpi.is_group())

        except AssertionError:
            raise

        except Exception as ex:
            if str(ex).startswith("Index is out of range"):
                self.m_logger.WriteLine(str(ex))

            else:
                raise

        if dpi != None:
            tvdp = clr.Convert(dpi, IDataProviderTimeVarying)
            resultA = tvdp.exec_elements(startTime, stopTime, reportStep, elements)
            Assert.assertEqual(5, resultA.data_sets.count)
            ds1: "IDataProviderResultDataSet" = self.FindDataSet(resultA.data_sets, "Time")
            times = ds1.get_values()
            # Check if the start/stop times of the report match the
            # times used to add the attitude data.
            reportedStartTime = str(times[0])[0 : len(str(startTime))]
            reportedStopTime = str(times[(Array.Length(times) - 1)])[0 : len(str(stopTime))]
            Assert.assertEqual(reportedStartTime, startTime)
            Assert.assertEqual(reportedStopTime, stopTime)
            if oAttitude.data_reference.is_profile_type_supported(VEHICLE_PROFILE.PROFILE_FIXED_IN_AXES):
                oAttitude.data_reference.set_profile_type(VEHICLE_PROFILE.PROFILE_FIXED_IN_AXES)
                fixed: "IVehicleProfileFixedInAxes" = clr.CastAs(
                    oAttitude.data_reference.profile, IVehicleProfileFixedInAxes
                )
                if fixed != None:
                    fixed.reference_axes = "CentralBody/Earth Fixed"

                oAttitude.clear_all()

                pos: int = 0
                while pos < Array.Length(data):
                    time: str = dtTime.format("UTCG")
                    oAttitude.add_quaternion(
                        time, float(data[pos]), float(data[(pos + 1)]), float(data[(pos + 2)]), float(data[(pos + 3)])
                    )
                    dtTime = dtTime.add("sec", float(dtIncrement))

                    pos += 4

                dpi = self._obj.data_providers["Attitude Quaternions"]
                tvdp = clr.Convert(dpi, IDataProviderTimeVarying)
                resultB = tvdp.exec_elements(startTime, stopTime, reportStep, elements)
                ds2: "IDataProviderResultDataSet" = self.FindDataSet(resultB.data_sets, "Time")
                times = ds2.get_values()
                reportedStartTime = str(times[0])[0 : len(str(startTime))]
                reportedStopTime = str(times[(Array.Length(times) - 1)])[0 : len(str(stopTime))]
                Assert.assertEqual(reportedStartTime, startTime)
                Assert.assertEqual(reportedStopTime, stopTime)

        self.m_logger.WriteLine("----- REALTIME ATTITUDE TEST ----- END -----")


# endregion


# region BasicAttitudeDifferenceHelper
class BasicAttitudeDifferenceHelper(object):
    def __init__(self, oApplication: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        oApplication.unit_preferences.reset_units()
        self.m_oApplication: "IStkObjectRoot" = oApplication

    # endregion

    # region Run method
    def Run(self, oAny: "IStkObject"):
        self.m_logger.WriteLine("----- DIFFERENCE ATTITUDE TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oAny)
        strObject: str = String.Format("*/{0}/{1}", oAny.class_name, oAny.instance_name)

        # Removes all profiles except for the first one
        self.m_oApplication.execute_command((("SetAttitude " + strObject) + " ClearData AllProfiles"))
        self.m_oApplication.execute_command((("SetAttitude " + strObject) + " Standard"))

        # check a RealTime Attitude
        self.m_oApplication.execute_command((("SetAttitude " + strObject) + " RealTime Extrapolate 300 120"))

        oRealTime: "IVehicleAttitudeRealTime" = clr.CastAs(self.GetAttitude(oAny), IVehicleAttitudeRealTime)
        Assert.assertIsNotNone(oRealTime)
        Assert.assertEqual(VEHICLE_LOOK_AHEAD_METHOD.EXTRAPOLATE, oRealTime.look_ahead_method)
        Assert.assertEqual(300, oRealTime.duration.look_ahead)
        Assert.assertEqual(120, oRealTime.duration.look_behind)

        # check a Standard Attitude
        self.m_oApplication.execute_command((("SetAttitude " + strObject) + " Standard"))

        oStandard: "IVehicleAttitudeStandard" = clr.CastAs(self.GetAttitude(oAny), IVehicleAttitudeStandard)
        Assert.assertIsNotNone(oStandard)

        self.m_oApplication.execute_command((("SetAttitude " + strObject) + " Profile ECFVelNadir Offset 12.5"))
        veProfile: "VEHICLE_PROFILE" = self.GetCurrentBasicProfileType(oStandard)
        Assert.assertEqual(VEHICLE_PROFILE.PROFILE_ECF_VELOCITY_ALIGNMENT_WITH_NADIR_CONSTRAINT, veProfile)
        Assert.assertEqual(
            12.5,
            (clr.Convert(self.GetCurrentBasicProfile(oStandard), IVehicleProfileConstraintOffset)).constraint_offset,
        )

        self.m_oApplication.execute_command(
            (("AttitudeSegment " + strObject) + ' Add Profile Test1 "2 Jul 1999 01:00:00.000" ECFVelNadir Offset 12.5')
        )

        oMultiSegment: "IVehicleAttitude" = self.GetAttitude(oAny)
        Assert.assertIsNone(oMultiSegment, "Unexpected attitude")

        self.m_oApplication.execute_command((("SetAttitude " + strObject) + " ClearData AllProfiles"))
        oStandard = clr.CastAs(self.GetAttitude(oAny), IVehicleAttitudeStandard)
        Assert.assertIsNotNone(oStandard)

        self.m_logger.WriteLine("----- DIFFERENCE ATTITUDE TEST ----- END -----")

    # endregion

    # region GetAttitude
    def GetAttitude(self, oAny: "IStkObject"):
        oAttitude: "IVehicleAttitude" = None
        if oAny.class_type == STK_OBJECT_TYPE.SATELLITE:
            oAttitude = (clr.Convert(oAny, ISatellite)).attitude
        elif oAny.class_type == STK_OBJECT_TYPE.SHIP:
            oAttitude = (clr.Convert(oAny, IShip)).attitude
        elif oAny.class_type == STK_OBJECT_TYPE.AIRCRAFT:
            oAttitude = (clr.Convert(oAny, IAircraft)).attitude
        elif oAny.class_type == STK_OBJECT_TYPE.MISSILE:
            oAttitude = (clr.Convert(oAny, IMissile)).attitude
        elif oAny.class_type == STK_OBJECT_TYPE.GROUND_VEHICLE:
            oAttitude = (clr.Convert(oAny, IGroundVehicle)).attitude
        elif oAny.class_type == STK_OBJECT_TYPE.LAUNCH_VEHICLE:
            oAttitude = (clr.Convert(oAny, ILaunchVehicle)).attitude
        return oAttitude

    # endregion

    # region GetCurrentBasicProfileType
    def GetCurrentBasicProfileType(self, oStandard: "IVehicleAttitudeStandard"):
        if oStandard.type == ATTITUDE_STANDARD_TYPE.ORBIT_ATTITUDE_STANDARD:
            orbit: "IVehicleOrbitAttitudeStandard" = clr.Convert(oStandard, IVehicleOrbitAttitudeStandard)
            return orbit.basic.profile_type
        elif oStandard.type == ATTITUDE_STANDARD_TYPE.ROUTE_ATTITUDE_STANDARD:
            route: "IVehicleRouteAttitudeStandard" = clr.Convert(oStandard, IVehicleRouteAttitudeStandard)
            return route.basic.profile_type
        elif oStandard.type == ATTITUDE_STANDARD_TYPE.TRAJECTORY_ATTITUDE_STANDARD:
            traj: "IVehicleTrajectoryAttitudeStandard" = clr.Convert(oStandard, IVehicleTrajectoryAttitudeStandard)
            return traj.basic.profile_type
        else:
            return VEHICLE_PROFILE.PROFILE_UNKNOWN

    # endregion

    # region GetCurrentBasicProfile
    def GetCurrentBasicProfile(self, oStandard: "IVehicleAttitudeStandard"):
        if oStandard.type == ATTITUDE_STANDARD_TYPE.ORBIT_ATTITUDE_STANDARD:
            orbit: "IVehicleOrbitAttitudeStandard" = clr.Convert(oStandard, IVehicleOrbitAttitudeStandard)
            return orbit.basic.profile
        elif oStandard.type == ATTITUDE_STANDARD_TYPE.ROUTE_ATTITUDE_STANDARD:
            route: "IVehicleRouteAttitudeStandard" = clr.Convert(oStandard, IVehicleRouteAttitudeStandard)
            return route.basic.profile
        elif oStandard.type == ATTITUDE_STANDARD_TYPE.TRAJECTORY_ATTITUDE_STANDARD:
            traj: "IVehicleTrajectoryAttitudeStandard" = clr.Convert(oStandard, IVehicleTrajectoryAttitudeStandard)
            return traj.basic.profile
        else:
            return None


# endregion


# region AccessEventDetectionHelper
class AccessEventDetectionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oDetection: "IAccessEventDetection", bReadOnly: bool):
        self.m_logger.WriteLine4("----- ACCESS EVENT DETECTION TEST (ReadOnly = {0}) ----- BEGIN -----", bReadOnly)
        if bReadOnly:

            def action379():
                oDetection.set_type(oDetection.type)

            # SetType (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action379)
            if oDetection.type == EVENT_DETECTION.NO_SUB_SAMPLING:
                oNoSubSampling: "IEventDetectionNoSubSampling" = clr.CastAs(
                    oDetection.strategy, IEventDetectionNoSubSampling
                )
                Assert.assertIsNotNone(oNoSubSampling)
            elif oDetection.type == EVENT_DETECTION.USE_SUB_SAMPLING:
                oSubSampling: "IEventDetectionSubSampling" = clr.CastAs(oDetection.strategy, IEventDetectionSubSampling)
                Assert.assertIsNotNone(oSubSampling)

                def action380():
                    oSubSampling.abs_value_convergence = 0.1

                # AbsValueConvergence (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action380)

                def action381():
                    oSubSampling.rel_value_convergence = 0.1

                # RelValueConvergence (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action381)

                def action382():
                    oSubSampling.time_convergence = 0.01

                # TimeConvergence (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action382)
            else:
                Assert.fail("Invalid type!")

        else:
            # Type
            self.m_logger.WriteLine6("\tThe current Type is: {0}", oDetection.type)
            # SupportedTypes
            arTypes = oDetection.supported_types
            self.m_logger.WriteLine3("\tThe Access Event Detection supports: {0} types", len(arTypes))

            iIndex: int = 0
            while iIndex < len(arTypes):
                eType: "EVENT_DETECTION" = clr.Convert(int(arTypes[iIndex][0]), EVENT_DETECTION)
                self.m_logger.WriteLine8("\t\tType {0}: {1} ({2})", iIndex, eType, arTypes[iIndex][1])
                if not oDetection.is_type_supported(eType):
                    Assert.fail("{0} type should be supported!", eType)

                # SetType
                oDetection.set_type(eType)
                self.m_logger.WriteLine6("\t\t\tThe new Type is: {0}", oDetection.type)
                eType1: "EVENT_DETECTION" = oDetection.type
                Assert.assertEqual(eType, eType1)
                if oDetection.type == EVENT_DETECTION.NO_SUB_SAMPLING:
                    # Strategy
                    oNoSubSampling: "IEventDetectionNoSubSampling" = clr.CastAs(
                        oDetection.strategy, IEventDetectionNoSubSampling
                    )
                    Assert.assertIsNotNone(oNoSubSampling)
                elif oDetection.type == EVENT_DETECTION.USE_SUB_SAMPLING:
                    # Strategy
                    oSubSampling: "IEventDetectionSubSampling" = clr.CastAs(
                        oDetection.strategy, IEventDetectionSubSampling
                    )
                    Assert.assertIsNotNone(oSubSampling)
                    # TimeConvergence
                    self.m_logger.WriteLine6("\t\t\tThe current TimeConvergence is: {0}", oSubSampling.time_convergence)
                    oSubSampling.time_convergence = 0.5
                    self.m_logger.WriteLine6("\t\t\tThe new TimeConvergence is: {0}", oSubSampling.time_convergence)
                    Assert.assertEqual(0.5, oSubSampling.time_convergence)

                    def action383():
                        oSubSampling.time_convergence = -0.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action383)
                    # AbsValueConvergence
                    self.m_logger.WriteLine6(
                        "\t\t\tThe current AbsValueConvergence is: {0}", oSubSampling.abs_value_convergence
                    )
                    oSubSampling.abs_value_convergence = 0.5
                    self.m_logger.WriteLine6(
                        "\t\t\tThe new AbsValueConvergence is: {0}", oSubSampling.abs_value_convergence
                    )
                    Assert.assertEqual(0.5, oSubSampling.abs_value_convergence)

                    def action384():
                        oSubSampling.abs_value_convergence = -0.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action384)
                    # RelValueConvergence
                    self.m_logger.WriteLine6(
                        "\t\t\tThe current RelValueConvergence is: {0}", oSubSampling.rel_value_convergence
                    )
                    oSubSampling.rel_value_convergence = 0.5
                    self.m_logger.WriteLine6(
                        "\t\t\tThe new RelValueConvergence is: {0}", oSubSampling.rel_value_convergence
                    )
                    Assert.assertEqual(0.5, oSubSampling.rel_value_convergence)

                    def action385():
                        oSubSampling.rel_value_convergence = -0.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action385)
                else:
                    Assert.fail("Invalid type!")

                iIndex += 1

        self.m_logger.WriteLine4("----- ACCESS EVENT DETECTION TEST (ReadOnly = {0}) ----- END -----", bReadOnly)


# endregion


# region AccessSamplingHelper
class AccessSamplingHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oSampling: "IAccessSampling", bReadOnly: bool):
        self.m_logger.WriteLine4("----- ACCESS SAMPLING TEST (ReadOnly = {0}) ----- BEGIN -----", bReadOnly)
        if bReadOnly:

            def action386():
                oSampling.set_type(oSampling.type)

            # SetType (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action386)
            if oSampling.type == SAMPLING_METHOD.ADAPTIVE:
                oAdaptive: "ISamplingMethodAdaptive" = clr.CastAs(oSampling.strategy, ISamplingMethodAdaptive)
                Assert.assertIsNotNone(oAdaptive)

                def action387():
                    oAdaptive.min_time_step = 0.1

                # MinTimeStep (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action387)

                def action388():
                    oAdaptive.max_time_step = 1.1

                # MaxTimeStep (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action388)
            elif oSampling.type == SAMPLING_METHOD.FIXED_STEP:
                oFixedStep: "ISamplingMethodFixedStep" = clr.CastAs(oSampling.strategy, ISamplingMethodFixedStep)
                Assert.assertIsNotNone(oFixedStep)

                def action389():
                    oFixedStep.fixed_time_step = 123

                # FixedTimeStep (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action389)

                def action390():
                    oFixedStep.time_bound = 123

                # TimeBound (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action390)
            else:
                Assert.fail("Invalid type!")

        else:
            # Type
            self.m_logger.WriteLine6("\tThe current Type is: {0}", oSampling.type)
            # SupportedTypes
            arTypes = oSampling.supported_types
            self.m_logger.WriteLine3("\tThe Access Sampling supports: {0} types", len(arTypes))

            iIndex: int = 0
            while iIndex < len(arTypes):
                eType: "SAMPLING_METHOD" = clr.Convert(int(arTypes[iIndex][0]), SAMPLING_METHOD)
                self.m_logger.WriteLine8("\t\tType {0}: {1} ({2})", iIndex, eType, arTypes[iIndex][1])
                if not oSampling.is_type_supported(eType):
                    Assert.fail("{0} type should be supported!", eType)

                # SetType
                oSampling.set_type(eType)
                self.m_logger.WriteLine6("\t\t\tThe new Type is: {0}", oSampling.type)
                eType1: "SAMPLING_METHOD" = oSampling.type
                Assert.assertEqual(eType, eType1)
                if oSampling.type == SAMPLING_METHOD.ADAPTIVE:
                    # Strategy
                    oAdaptive: "ISamplingMethodAdaptive" = clr.CastAs(oSampling.strategy, ISamplingMethodAdaptive)
                    Assert.assertIsNotNone(oAdaptive)
                    # MinTimeStep
                    self.m_logger.WriteLine6("\t\t\tThe current MinTimeStep is: {0}", oAdaptive.min_time_step)
                    oAdaptive.min_time_step = 12.5
                    self.m_logger.WriteLine6("\t\t\tThe new MinTimeStep is: {0}", oAdaptive.min_time_step)
                    Assert.assertEqual(12.5, oAdaptive.min_time_step)

                    def action391():
                        oAdaptive.min_time_step = -12.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action391)
                    # MaxTimeStep
                    self.m_logger.WriteLine6("\t\t\tThe current MaxTimeStep is: {0}", oAdaptive.max_time_step)
                    oAdaptive.max_time_step = 12.5
                    self.m_logger.WriteLine6("\t\t\tThe new MaxTimeStep is: {0}", oAdaptive.max_time_step)
                    Assert.assertEqual(12.5, oAdaptive.max_time_step)

                    def action392():
                        oAdaptive.max_time_step = -12.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action392)
                elif oSampling.type == SAMPLING_METHOD.FIXED_STEP:
                    # Strategy
                    oFixedStep: "ISamplingMethodFixedStep" = clr.CastAs(oSampling.strategy, ISamplingMethodFixedStep)
                    Assert.assertIsNotNone(oFixedStep)
                    # FixedTimeStep
                    self.m_logger.WriteLine6("\t\t\tThe current FixedTimeStep is: {0}", oFixedStep.fixed_time_step)
                    oFixedStep.fixed_time_step = 34.5
                    self.m_logger.WriteLine6("\t\t\tThe new FixedTimeStep is: {0}", oFixedStep.fixed_time_step)
                    Assert.assertEqual(34.5, oFixedStep.fixed_time_step)

                    def action393():
                        oFixedStep.fixed_time_step = -34.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action393)
                    # TimeBound
                    self.m_logger.WriteLine6("\t\t\tThe current TimeBound is: {0}", oFixedStep.time_bound)
                    oFixedStep.time_bound = 34.5
                    self.m_logger.WriteLine6("\t\t\tThe new TimeBound is: {0}", oFixedStep.time_bound)
                    Assert.assertEqual(34.5, oFixedStep.time_bound)

                    def action394():
                        oFixedStep.time_bound = -34.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action394)
                else:
                    Assert.fail("Invalid type!")

                iIndex += 1

        self.m_logger.WriteLine4("----- ACCESS SAMPLING TEST (ReadOnly = {0}) ----- END -----", bReadOnly)


# endregion


# region Spatial Info Helper
class SpatialInfoHelper(object):
    def __init__(self, app: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        self.m_app: "IStkObjectRoot" = app

    @property
    def Application(self):
        return self.m_app

    def InternalRun(self, oObj: "IStkObject"):
        Assert.assertIsNotNone(oObj)
        Assert.assertIsNotNone(clr.CastAs(oObj, IProvideSpatialInfo))
        oSpatialInfo: "IVehicleSpatialInfo" = (clr.CastAs(oObj, IProvideSpatialInfo)).get_spatial_info(False)
        Assert.assertIsNotNone(oSpatialInfo)
        Assert.assertFalse(oSpatialInfo.recycle)

        Assert.assertIsNotNone(oSpatialInfo)
        Assert.assertIsNotNone(oObj)

        spatialState: "ISpatialState" = oSpatialInfo.get_state(
            (clr.CastAs(self.Application.current_scenario, IScenario)).start_time
        )
        Assert.assertIsNotNone(spatialState)

        Assert.assertIsNotNone(spatialState.central_body)
        Assert.assertEqual(
            spatialState.current_time, (clr.CastAs(self.Application.current_scenario, IScenario)).start_time
        )

        # spatial data should not be available for non-propagated vehicles

        ga: "IVehiclePropagatorGreatArc" = None
        wpe: "IVehicleWaypointsElement" = None
        oParentObj: "IStkObject" = oObj
        oParentType: "STK_OBJECT_TYPE" = oObj.class_type
        objTypeToPropagate: "STK_OBJECT_TYPE" = None
        if oObj.class_type == STK_OBJECT_TYPE.SENSOR:
            oParentObj = oObj.parent
            oParentType = oParentObj.class_type
            objTypeToPropagate = oParentObj.class_type

        else:
            # If not a sensor, then the object must be
            # an instance of a vehicle created to test
            # the spatial information and by default
            # the vehicles are not propagated.
            Assert.assertFalse(spatialState.is_available)
            objTypeToPropagate = oObj.class_type
            if objTypeToPropagate == STK_OBJECT_TYPE.AIRCRAFT:
                (clr.Convert(oParentObj, IAircraft)).set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
                ga = clr.Convert((clr.Convert(oParentObj, IAircraft)).route, IVehiclePropagatorGreatArc)
                wpe = ga.waypoints.add()
                wpe.latitude = 10
                wpe.longitude = 11
                wpe = ga.waypoints.add()
                wpe.latitude = 11
                wpe.longitude = 12
                wpe = ga.waypoints.add()
                wpe.latitude = 13
                wpe.longitude = 14
                ga.propagate()
            elif objTypeToPropagate == STK_OBJECT_TYPE.GROUND_VEHICLE:
                (clr.Convert(oParentObj, IGroundVehicle)).set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
                ga = clr.Convert((clr.Convert(oParentObj, IGroundVehicle)).route, IVehiclePropagatorGreatArc)
                wpe = ga.waypoints.add()
                wpe.latitude = 16
                wpe.longitude = 17
                wpe = ga.waypoints.add()
                wpe.latitude = 18
                wpe.longitude = 19
                wpe = ga.waypoints.add()
                wpe.latitude = 20
                wpe.longitude = 21
                ga.propagate()
            elif objTypeToPropagate == STK_OBJECT_TYPE.LAUNCH_VEHICLE:
                (clr.Convert(oParentObj, ILaunchVehicle)).set_trajectory_type(
                    VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT
                )
                ascent: "IVehiclePropagatorSimpleAscent" = clr.CastAs(
                    (clr.Convert(oParentObj, ILaunchVehicle)).trajectory, IVehiclePropagatorSimpleAscent
                )
                Assert.assertIsNotNone(ascent)
                ascent.propagate()
            elif objTypeToPropagate == STK_OBJECT_TYPE.MISSILE:
                (clr.Convert(oParentObj, IMissile)).set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
                ballistic: "IVehiclePropagatorTwoBody" = clr.CastAs(
                    (clr.Convert(oParentObj, IMissile)).trajectory, IVehiclePropagatorTwoBody
                )
                Assert.assertIsNotNone(ballistic)
                ballistic.propagate()
            elif objTypeToPropagate == STK_OBJECT_TYPE.SATELLITE:
                (clr.Convert(oParentObj, ISatellite)).set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
                tb: "IVehiclePropagatorTwoBody" = clr.CastAs(
                    (clr.Convert(oParentObj, ISatellite)).propagator, IVehiclePropagatorTwoBody
                )
                Assert.assertIsNotNone(tb)
                tb.step = 120
                tb.propagate()
            elif objTypeToPropagate == STK_OBJECT_TYPE.SHIP:
                (clr.Convert(oParentObj, IShip)).set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
                ga = clr.Convert((clr.Convert(oParentObj, IShip)).route, IVehiclePropagatorGreatArc)
                wpe = ga.waypoints.add()
                wpe.latitude = 22
                wpe.longitude = 23
                wpe = ga.waypoints.add()
                wpe.latitude = 24
                wpe.longitude = 25
                wpe = ga.waypoints.add()
                wpe.latitude = 26
                wpe.longitude = 27
                ga.propagate()

        # Verify the available intervals
        intervals: "IImmutableIntervalCollection" = oSpatialInfo.get_available_times()
        Assert.assertIsNotNone(intervals)

        self.spatialTimeHelper(
            oObj, oSpatialInfo, (clr.CastAs(self.Application.current_scenario, IScenario)).start_time
        )

        Logger.Instance.WriteLine3("# of available intervals: {0}", intervals.count)

        arIntervals = intervals.to_array()
        Assert.assertEqual(intervals.count, len(arIntervals))

        i: int = 0
        while i < intervals.count:
            dateFormat: str = self.Application.unit_preferences.get_current_unit_abbrv("DateFormat")

            start: typing.Any = None
            stop: typing.Any = None

            (start, stop) = intervals.get_interval(i)
            Logger.Instance.WriteLine7("Interval [{0},{1}]", start, stop)

            self.spatialTimeHelper(oObj, oSpatialInfo, start)
            dtStop: "IDate" = self.Application.conversion_utility.new_date(dateFormat, str(stop))
            # Modify the stop time by decrementing it by 60 seconds to avoid the
            # test failures.
            dtStopModified: "IDate" = dtStop.subtract("sec", 60)
            dtStopModifiedStr: str = dtStopModified.format(dateFormat)
            self.spatialTimeHelper(oObj, oSpatialInfo, dtStopModifiedStr)

            # Test availability within and outside of intervals

            Console.WriteLine(((("Interval: " + str(start)) + "   ") + str(stop)))
            Console.WriteLine(oSpatialInfo.get_state("1 Jul 1999 00:00:00.000").is_available)  # start
            Console.WriteLine(oSpatialInfo.get_state("1 Jul 1999 01:40:42.750").is_available)
            Console.WriteLine(oSpatialInfo.get_state("1 Jul 1999 01:40:42.751").is_available)  # stop

            Assert.assertTrue(oSpatialInfo.get_state(start).is_available)
            # BUG59737 Assert.IsTrue(oSpatialInfo.GetState(stop).IsAvailable);

            dateStart: "IDate" = self.Application.conversion_utility.new_date(dateFormat, str(start))
            dateStart = dateStart.subtract("sec", 1)
            Assert.assertFalse(oSpatialInfo.get_state(dateStart.format(dateFormat)).is_available)

            dateStop: "IDate" = self.Application.conversion_utility.new_date(dateFormat, str(stop))
            dateStop = dateStop.add("sec", 1)
            Assert.assertFalse(oSpatialInfo.get_state(dateStop.format(dateFormat)).is_available)

            i += 1

    def spatialTimeHelper(self, oObj: "IStkObject", oSpatialInfo: "IVehicleSpatialInfo", param0: typing.Any):
        spatialState: "ISpatialState" = None

        oSpatialInfo = (clr.CastAs(oObj, IProvideSpatialInfo)).get_spatial_info(False)

        # Once the vehicle's ephemeris is generated,
        # the spatial data should now be available
        spatialState = oSpatialInfo.get_state(param0)
        Assert.assertIsNotNone(spatialState)
        Assert.assertTrue(spatialState.is_available)

        Assert.assertIsNotNone(spatialState.central_body)
        Assert.assertEqual(spatialState.current_time, param0)

        Assert.assertIsNotNone(spatialState.fixed_orientation)
        Assert.assertIsNotNone(spatialState.fixed_position)
        Assert.assertIsNotNone(spatialState.inertial_orientation)
        Assert.assertIsNotNone(spatialState.inertial_position)

        # Text the orientation
        fo: "IOrientation" = spatialState.fixed_orientation.convert_to(ORIENTATION_TYPE.AZ_EL)
        Assert.assertIsNotNone(fo)

        def action395():
            spatialState.fixed_orientation.assign(fo)

        TryCatchAssertBlock.DoAssert("Should not allow assignment to read-only attributes.", action395)

        vx: float = 0.0
        vy: float = 0.0
        vz: float = 0.0

        (vx, vy, vz) = spatialState.query_velocity_fixed()
        self.m_logger.WriteLine8("VX={0}, VY={1}, VZ={2}", vx, vy, vz)

        (vx, vy, vz) = spatialState.query_velocity_inertial()
        self.m_logger.WriteLine8("VX={0}, VY={1}, VZ={2}", vx, vy, vz)

        del oSpatialInfo
        # /////////////////////
        #
        # Test state recycling
        #
        # /////////////////////

        # Create a spatial object that recylces the same spatial state
        # instead of creating a new state object
        oSpatialInfo = (clr.Convert(oObj, IProvideSpatialInfo)).get_spatial_info(True)
        Assert.assertIsNotNone(oSpatialInfo)
        Assert.assertTrue(oSpatialInfo.recycle)

        spatialState = oSpatialInfo.get_state(param0)
        Assert.assertIsNotNone(spatialState)
        Assert.assertTrue(spatialState.is_available)

        # Convert the spatial state time to 'epSec'
        oCurDate: "IDate" = self.Application.conversion_utility.new_date(
            self.Application.unit_preferences.get_current_unit_abbrv("DateFormat"), str(spatialState.current_time)
        )
        oNewDate: "IDate" = oCurDate.add("sec", 60)  # 1 min
        # When recycling, the calls to GetState reuse the same instance
        # of the spatial state.
        oSpatialInfo.get_state(oNewDate.format(self.Application.unit_preferences.get_current_unit_abbrv("DateFormat")))
        # The spatialState object references new date
        Assert.assertEqual(
            spatialState.current_time,
            oNewDate.format(self.Application.unit_preferences.get_current_unit_abbrv("DateFormat")),
        )
        Assert.assertNotEqual(
            spatialState.current_time,
            oCurDate.format(self.Application.unit_preferences.get_current_unit_abbrv("DateFormat")),
        )

    def Run(self, oOrigObj: "IStkObject"):
        oNewObj: "IStkObject" = None
        try:
            if oOrigObj.class_type != STK_OBJECT_TYPE.SENSOR:
                oNewObj = self.Application.current_scenario.children.new(
                    oOrigObj.class_type, (oOrigObj.class_type.name + "_1")
                )

            else:
                oNewObj = oOrigObj.parent.children.new(oOrigObj.class_type, (oOrigObj.class_type.name + "_1"))

            self.InternalRun(oNewObj)

        finally:
            Assert.assertIsNotNone(oNewObj)
            oNewObj.unload()


# endregion


# region EclipsingBodiesHelper
class EclipsingBodiesHelper(object):
    def __init__(self, *args, **kwargs):
        self.logger = Logger.Instance

    def Run(self, oBodies: "IVehicleEclipseBodies"):
        self.logger.WriteLine("----- THE EclipsingBodiesHelper TEST ----- BEGIN -----")
        # IVehicleEclipseBodies oBodies = AG_SAT.EclipseBodies;
        Assert.assertIsNotNone(oBodies)
        # UseCustomizedList (false)
        self.logger.WriteLine4("The current UseCustomizedList flag is: {0}", oBodies.use_customized_list)
        oBodies.use_customized_list = False
        self.logger.WriteLine4("The new UseCustomizedList flag is: {0}", oBodies.use_customized_list)
        Assert.assertEqual(False, oBodies.use_customized_list)
        # AvailableCentralBodies
        arAvailableBodies = oBodies.available_central_bodies
        self.logger.WriteLine3(
            "The Available CentralBodies array contains: {0} elements", Array.Length(arAvailableBodies)
        )

        iIndex: int = 0
        while iIndex < Array.Length(arAvailableBodies):
            # IsCentralBodyAssigned
            strBody: str = str(arAvailableBodies[iIndex])
            self.logger.WriteLine8(
                "\tElement {0}: CentralBody = {1}, IsAssigned = {2}",
                iIndex,
                strBody,
                oBodies.is_central_body_assigned(strBody),
            )

            iIndex += 1

        # AssignedCentralBodies
        arAssignedBodies = oBodies.assigned_central_bodies
        self.logger.WriteLine3(
            "The Assigned CentralBodies array contains: {0} elements", Array.Length(arAssignedBodies)
        )

        iIndex: int = 0
        while iIndex < Array.Length(arAssignedBodies):
            # IsCentralBodyAssigned
            strBody: str = str(arAssignedBodies[iIndex])
            self.logger.WriteLine8(
                "\tElement {0}: CentralBody = {1}, IsAssigned = {2}",
                iIndex,
                strBody,
                oBodies.is_central_body_assigned(strBody),
            )

            iIndex += 1

        # AssignCentralBody (readonly)
        try:
            oBodies.assign_central_body(str(arAvailableBodies[0]))
            Assert.fail("Should not allow to call AssignCentralBody().")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.logger.WriteLine5("Expected exception: {0}", str(e))

        # RemoveCentralBody (readonly)
        try:
            oBodies.remove_central_body(str(arAssignedBodies[0]))
            Assert.fail("Should not allow to call RemoveCentralBody().")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.logger.WriteLine5("Expected exception: {0}", str(e))

        # RemoveAll (readonly)
        try:
            oBodies.remove_all()
            Assert.fail("Should not allow to call RemoveAll().")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.logger.WriteLine5("Expected exception: {0}", str(e))

        # UseCustomizedList (true)
        oBodies.use_customized_list = True
        self.logger.WriteLine4("The new UseCustomizedList flag is: {0}", oBodies.use_customized_list)
        Assert.assertEqual(True, oBodies.use_customized_list)
        # AvailableCentralBodies
        arAvailableBodies = oBodies.available_central_bodies
        self.logger.WriteLine3(
            "The Available CentralBodies array contains: {0} elements", Array.Length(arAvailableBodies)
        )

        iIndex: int = 0
        while iIndex < Array.Length(arAvailableBodies):
            strBody: str = str(arAvailableBodies[iIndex])
            self.logger.WriteLine8(
                "\tElement {0}: CentralBody = {1}, IsAssigned = {2}",
                iIndex,
                strBody,
                oBodies.is_central_body_assigned(strBody),
            )
            if not oBodies.is_central_body_assigned(strBody):
                # AssignCentralBody
                oBodies.assign_central_body(strBody)
                if oBodies.is_central_body_assigned(strBody):
                    self.logger.WriteLine5("\t\tThe {0} CentralBody was assigned.", strBody)

                else:
                    Assert.fail("The {0} CentralBody should be assigned!", strBody)

            else:
                self.logger.WriteLine("\t\tThe {0} CentralBody is already assigned.")

            iIndex += 1

        # AssignedCentralBodies
        arAssignedBodies = oBodies.assigned_central_bodies
        self.logger.WriteLine3(
            "The Assigned CentralBodies array contains: {0} elements", Array.Length(arAssignedBodies)
        )

        iIndex: int = 0
        while iIndex < Array.Length(arAssignedBodies):
            strBody: str = str(arAssignedBodies[iIndex])
            self.logger.WriteLine8(
                "\tElement {0}: CentralBody = {1}, IsAssigned = {2}",
                iIndex,
                strBody,
                oBodies.is_central_body_assigned(strBody),
            )

            iIndex += 1

        # the length should be the same
        Assert.assertEqual(Array.Length(arAvailableBodies), Array.Length(arAssignedBodies))
        # RemoveCentralBody
        iLength: int = Array.Length(arAssignedBodies)
        self.logger.WriteLine3(
            "Before RemoveCentralBody the Assigned CentralBodies array contains: {0} elements", iLength
        )
        oBodies.remove_central_body(str(arAssignedBodies[0]))
        arAssignedBodies = oBodies.assigned_central_bodies
        self.logger.WriteLine3(
            "After RemoveCentralBody the Assigned CentralBodies array contains: {0} elements",
            Array.Length(arAssignedBodies),
        )
        Assert.assertEqual((iLength - 1), Array.Length(arAssignedBodies))
        # RemoveAll
        self.logger.WriteLine3(
            "Before RemoveAll the Assigned CentralBodies array contains: {0} elements", Array.Length(arAssignedBodies)
        )
        oBodies.remove_all()
        arAssignedBodies = oBodies.assigned_central_bodies
        self.logger.WriteLine3(
            "After RemoveAll the Assigned CentralBodies array contains: {0} elements", Array.Length(arAssignedBodies)
        )
        Assert.assertEqual(0, Array.Length(arAssignedBodies))
        # IsCentralBodyAssigned
        Assert.assertFalse(oBodies.is_central_body_assigned("Invalid CentralBody"))
        # AssignCentralBody
        try:
            oBodies.assign_central_body("Invalid CentralBody")
            Assert.fail("Should return error.")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.logger.WriteLine5("Expected exception: {0}", str(e))

        # RemoveCentralBody
        try:
            oBodies.remove_central_body("Invalid CentralBody")
            Assert.fail("Should return error.")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.logger.WriteLine5("Expected exception: {0}", str(e))

        self.logger.WriteLine("----- THE EclipsingBodiesHelper TEST ----- END -----")


# endregion


# region PlatformLaserEnvAtmosLossBBLLHelper
class PlatformLaserEnvAtmosLossBBLLHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model

        def action396():
            laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")

        TryCatchAssertBlock.ExpectedException("read-only", action396)

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model
        laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")
        Assert.assertEqual("Beer-Bouguer-Lambert Law", laserPropChan.atmospheric_loss_model.name)
        Assert.assertEqual(
            LASER_PROPAGATION_LOSS_MODEL_TYPE.BEER_BOUGUER_LAMBERT_LAW, laserPropChan.atmospheric_loss_model.type
        )

        bbll: "ILaserAtmosphericLossModelBeerBouguerLambertLaw" = clr.CastAs(
            laserPropChan.atmospheric_loss_model, ILaserAtmosphericLossModelBeerBouguerLambertLaw
        )

        bbll.create_evenly_spaced_layers(5, 100)
        Assert.assertTrue(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)
        bbllLayerColl: "IBeerBouguerLambertLawLayerCollection" = bbll.atmosphere_layers
        Assert.assertEqual(5, bbllLayerColl.count)
        Assert.assertEqual(100, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(80, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(60, bbllLayerColl[2].top_height)
        Assert.assertEqual(0, bbllLayerColl[2].extinction_coefficient)
        Assert.assertEqual(40, bbllLayerColl[3].top_height)
        Assert.assertEqual(0, bbllLayerColl[3].extinction_coefficient)
        Assert.assertEqual(20, bbllLayerColl[4].top_height)
        Assert.assertEqual(0, bbllLayerColl[4].extinction_coefficient)

        def action397():
            bbllLayerColl[3].top_height = 41

        TryCatchAssertBlock.ExpectedException("read only", action397)
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        bbll.create_unevenly_spaced_layers([5, 25, 55, 95])
        Assert.assertFalse(bbll.enable_evenly_spaced_heights)
        Assert.assertEqual(100, bbll.maximum_altitude)

        bbllLayerColl = bbll.atmosphere_layers
        Assert.assertEqual(4, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(25, bbllLayerColl[2].top_height)
        Assert.assertEqual(0, bbllLayerColl[2].extinction_coefficient)
        Assert.assertEqual(5, bbllLayerColl[3].top_height)
        Assert.assertEqual(0, bbllLayerColl[3].extinction_coefficient)

        def action398():
            bbllLayerColl[3].top_height = 101

        TryCatchAssertBlock.ExpectedException("invalid", action398)
        bbllLayerColl[3].top_height = 6
        Assert.assertEqual(6, bbllLayerColl[3].top_height)

        def action399():
            bbllLayerColl[3].extinction_coefficient = -1

        TryCatchAssertBlock.ExpectedException("invalid", action399)
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        def action400():
            bbllLayerColl.remove_at(5)

        TryCatchAssertBlock.ExpectedException("out of range", action400)
        bbllLayerColl.remove_at(2)
        Assert.assertEqual(3, bbllLayerColl.count)
        Assert.assertEqual(95, bbllLayerColl[0].top_height)
        Assert.assertEqual(0, bbllLayerColl[0].extinction_coefficient)
        Assert.assertEqual(55, bbllLayerColl[1].top_height)
        Assert.assertEqual(0, bbllLayerColl[1].extinction_coefficient)
        Assert.assertEqual(6, bbllLayerColl[2].top_height)
        Assert.assertEqual(1.5, bbllLayerColl[2].extinction_coefficient)


# endregion


# region PlatformLaserEnvAtmosLossModtranHelper
class PlatformLaserEnvAtmosLossModtranHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_atmospheric_loss_model = False
        Assert.assertFalse(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel: "ILaserAtmosphericLossModel" = laserPropChan.atmospheric_loss_model

        def action401():
            laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        TryCatchAssertBlock.ExpectedException("read-only", action401)

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model

        def action402():
            laserPropChan.set_atmospheric_loss_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action402)
        laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        Assert.assertEqual("MODTRAN-derived Lookup Table", laserPropChan.atmospheric_loss_model.name)
        Assert.assertEqual(
            LASER_PROPAGATION_LOSS_MODEL_TYPE.MODTRAN_LOOKUP_TABLE_TYPE, laserPropChan.atmospheric_loss_model.type
        )

        modtran: "IModtranLookupTablePropagationModel" = clr.CastAs(
            laserPropChan.atmospheric_loss_model, IModtranLookupTablePropagationModel
        )

        modtran.aerosol_model_type = MODTRAN_AEROSOL_MODEL_TYPE.MARITIME
        Assert.assertEqual(MODTRAN_AEROSOL_MODEL_TYPE.MARITIME, modtran.aerosol_model_type)
        modtran.aerosol_model_type = MODTRAN_AEROSOL_MODEL_TYPE.RURAL_HI_VIS
        Assert.assertEqual(MODTRAN_AEROSOL_MODEL_TYPE.RURAL_HI_VIS, modtran.aerosol_model_type)
        modtran.aerosol_model_type = MODTRAN_AEROSOL_MODEL_TYPE.TROPOSPHERIC
        Assert.assertEqual(MODTRAN_AEROSOL_MODEL_TYPE.TROPOSPHERIC, modtran.aerosol_model_type)
        modtran.aerosol_model_type = MODTRAN_AEROSOL_MODEL_TYPE.URBAN
        Assert.assertEqual(MODTRAN_AEROSOL_MODEL_TYPE.URBAN, modtran.aerosol_model_type)

        modtran.visibility = 0.5
        Assert.assertEqual(0.5, modtran.visibility)
        modtran.visibility = 50
        Assert.assertEqual(50, modtran.visibility)

        def action403():
            modtran.visibility = 0.1

        TryCatchAssertBlock.ExpectedException("invalid", action403)

        def action404():
            modtran.visibility = 51

        TryCatchAssertBlock.ExpectedException("invalid", action404)

        modtran.relative_humidity = 0
        Assert.assertEqual(0, modtran.relative_humidity)
        modtran.relative_humidity = 100
        Assert.assertEqual(100, modtran.relative_humidity)

        def action405():
            modtran.relative_humidity = -1

        TryCatchAssertBlock.ExpectedException("invalid", action405)

        def action406():
            modtran.relative_humidity = 101

        TryCatchAssertBlock.ExpectedException("invalid", action406)

        modtran.surface_temperature = 190
        Assert.assertEqual(190, modtran.surface_temperature)
        modtran.surface_temperature = 320
        Assert.assertEqual(320, modtran.surface_temperature)

        def action407():
            modtran.surface_temperature = 189

        TryCatchAssertBlock.ExpectedException("invalid", action407)

        def action408():
            modtran.surface_temperature = 321

        TryCatchAssertBlock.ExpectedException("invalid", action408)


# endregion


# region PlatformLaserEnvTropoScintLossHelper
class PlatformLaserEnvTropoScintLossHelper(object):
    # region Run
    def Run(self, laserEnv: "IPlatformLaserEnvironment"):
        laserPropChan: "ILaserPropagationChannel" = laserEnv.propagation_channel

        laserPropChan.enable_tropospheric_scintillation_loss_model = False
        Assert.assertFalse(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint: "ILaserTroposphericScintillationLossModel" = (
            laserPropChan.tropospheric_scintillation_loss_model
        )

        def action409():
            laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")

        TryCatchAssertBlock.ExpectedException("read-only", action409)

        laserPropChan.enable_tropospheric_scintillation_loss_model = True
        Assert.assertTrue(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint = laserPropChan.tropospheric_scintillation_loss_model

        def action410():
            laserPropChan.set_atmospheric_loss_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action410)
        laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")
        Assert.assertEqual("ITU-R P1814", laserPropChan.tropospheric_scintillation_loss_model.name)
        Assert.assertEqual(
            LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE.ITURP1814,
            laserPropChan.tropospheric_scintillation_loss_model.type,
        )

        iturp1814: "ILaserTroposphericScintillationLossModelITURP1814" = clr.CastAs(
            laserTropoScint, ILaserTroposphericScintillationLossModelITURP1814
        )

        iturp1814.set_atmospheric_turbulence_model_type(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.CONSTANT)
        Assert.assertEqual(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.CONSTANT, iturp1814.atmospheric_turbulence_model.type)

        cnst: "IAtmosphericTurbulenceModelConstant" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, IAtmosphericTurbulenceModelConstant
        )
        cnst.constant_refractive_index_structure_parameter = 99
        Assert.assertEqual(99, cnst.constant_refractive_index_structure_parameter)

        iturp1814.set_atmospheric_turbulence_model_type(ATMOSPHERIC_TURBULENCE_MODEL_TYPE.HUFNAGEL_VALLEY)
        Assert.assertEqual(
            ATMOSPHERIC_TURBULENCE_MODEL_TYPE.HUFNAGEL_VALLEY, iturp1814.atmospheric_turbulence_model.type
        )

        huf: "IAtmosphericTurbulenceModelHufnagelValley" = clr.CastAs(
            iturp1814.atmospheric_turbulence_model, IAtmosphericTurbulenceModelHufnagelValley
        )
        huf.wind_speed = 98
        Assert.assertEqual(98, huf.wind_speed)
        huf.nominal_ground_refractive_index_structure_parameter = 97
        Assert.assertEqual(97, huf.nominal_ground_refractive_index_structure_parameter)


# endregion


# region PlatformRF_Environment_EnvironmentalDataHelper
class PlatformRF_Environment_EnvironmentalDataHelper(object):
    # region Run
    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_itu618_section2_p5 = False
        Assert.assertFalse(propChan.enable_itu618_section2_p5)
        propChan.enable_itu618_section2_p5 = True
        Assert.assertTrue(propChan.enable_itu618_section2_p5)


# endregion


# region PlatformRF_Environment_RainCloudFog_RainModelHelper
class PlatformRF_Environment_RainCloudFog_RainModelHelper(object):
    # region Run
    def Run(self, rfEnv: "IPlatformRFEnvironment", root: "IStkObjectRoot"):
        holdUnit: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_rain_loss = False
        Assert.assertFalse(propChan.enable_rain_loss)

        def action411():
            propChan.set_rain_loss_model("Crane 1985")

        TryCatchAssertBlock.ExpectedException("read-only", action411)

        propChan.enable_rain_loss = True
        Assert.assertTrue(propChan.enable_rain_loss)

        arSupportedRainLossModels = propChan.supported_rain_loss_models
        rainLossModelName: str
        for rainLossModelName in arSupportedRainLossModels:
            propChan.set_rain_loss_model(rainLossModelName)
            rainLossModel: "IRainLossModel" = propChan.rain_loss_model
            Assert.assertEqual(rainLossModelName, rainLossModel.name)
            if rainLossModelName == "Crane 1985":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CRANE1985, rainLossModel.type)
                crane85: "IRainLossModelCrane1985" = clr.CastAs(rainLossModel, IRainLossModelCrane1985)
                crane85.surface_temperature = -100
                Assert.assertEqual(-100, crane85.surface_temperature)
                crane85.surface_temperature = 100
                Assert.assertEqual(100, crane85.surface_temperature)

                def action412():
                    crane85.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action412)

                def action413():
                    crane85.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action413)

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.SCRIPT_PLUGIN, rainLossModel.type)
                    scriptPlugin: "IRainLossModelScriptPlugin" = clr.CastAs(rainLossModel, IRainLossModelScriptPlugin)

                    def action414():
                        scriptPlugin.filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action414)

                    def action415():
                        scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action415)
                    scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RainLossModel.vbs")
                    Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_RainLossModel.vbs"), scriptPlugin.filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CCIR1983, rainLossModel.type)
                ccir83: "IRainLossModelCCIR1983" = clr.CastAs(rainLossModel, IRainLossModelCCIR1983)
                ccir83.surface_temperature = -100
                Assert.assertEqual(-100, ccir83.surface_temperature)
                ccir83.surface_temperature = 100
                Assert.assertEqual(100, ccir83.surface_temperature)

                def action416():
                    ccir83.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action416)

                def action417():
                    ccir83.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action417)

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CRANE1982, rainLossModel.type)
                crane82: "IRainLossModelCrane1982" = clr.CastAs(rainLossModel, IRainLossModelCrane1982)
                crane82.surface_temperature = -100
                Assert.assertEqual(-100, crane82.surface_temperature)
                crane82.surface_temperature = 100
                Assert.assertEqual(100, crane82.surface_temperature)

                def action418():
                    crane82.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action418)

                def action419():
                    crane82.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action419)

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.I_T_U_R_P_618_10, rainLossModel.type)
                itu618_10: "IRainLossModelITURP618_10" = clr.CastAs(rainLossModel, IRainLossModelITURP618_10)
                itu618_10.surface_temperature = -100
                Assert.assertEqual(-100, itu618_10.surface_temperature)
                itu618_10.surface_temperature = 100
                Assert.assertEqual(100, itu618_10.surface_temperature)

                def action420():
                    itu618_10.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action420)

                def action421():
                    itu618_10.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action421)
                itu618_10.enable_depolarization_loss = False
                Assert.assertFalse(itu618_10.enable_depolarization_loss)
                itu618_10.enable_depolarization_loss = True
                Assert.assertTrue(itu618_10.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-12":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.I_T_U_R_P_618_12, rainLossModel.type)
                itu618_12: "IRainLossModelITURP618_12" = clr.CastAs(rainLossModel, IRainLossModelITURP618_12)
                itu618_12.surface_temperature = -100
                Assert.assertEqual(-100, itu618_12.surface_temperature)
                itu618_12.surface_temperature = 100
                Assert.assertEqual(100, itu618_12.surface_temperature)

                def action422():
                    itu618_12.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action422)

                def action423():
                    itu618_12.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action423)
                itu618_12.enable_depolarization_loss = False
                Assert.assertFalse(itu618_12.enable_depolarization_loss)
                itu618_12.enable_depolarization_loss = True
                Assert.assertTrue(itu618_12.enable_depolarization_loss)

            elif rainLossModelName == "ITU-R P618-13":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.I_T_U_R_P_618_13, rainLossModel.type)
                itu618_13: "IRainLossModelITURP618_13" = clr.CastAs(rainLossModel, IRainLossModelITURP618_13)

                itu618_13.enable_itu1510 = False
                Assert.assertFalse(itu618_13.enable_itu1510)

                itu618_13.surface_temperature = -100
                Assert.assertEqual(-100, itu618_13.surface_temperature)
                itu618_13.surface_temperature = 100
                Assert.assertEqual(100, itu618_13.surface_temperature)

                def action424():
                    itu618_13.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action424)

                def action425():
                    itu618_13.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action425)

                def action426():
                    itu618_13.use_annual_itu1510 = True

                TryCatchAssertBlock.ExpectedException("read-only", action426)

                def action427():
                    itu618_13.itu1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action427)

                itu618_13.enable_itu1510 = True
                Assert.assertTrue(itu618_13.enable_itu1510)

                def action428():
                    itu618_13.surface_temperature = 100

                TryCatchAssertBlock.ExpectedException("read only", action428)

                itu618_13.use_annual_itu1510 = False
                Assert.assertFalse(itu618_13.use_annual_itu1510)

                itu618_13.itu1510_month = 1
                Assert.assertEqual(1, itu618_13.itu1510_month)
                itu618_13.itu1510_month = 12
                Assert.assertEqual(12, itu618_13.itu1510_month)

                def action429():
                    itu618_13.itu1510_month = 0

                TryCatchAssertBlock.ExpectedException("must be in", action429)

                def action430():
                    itu618_13.itu1510_month = 13

                TryCatchAssertBlock.ExpectedException("must be in", action430)

                itu618_13.use_annual_itu1510 = True
                Assert.assertTrue(itu618_13.use_annual_itu1510)

                def action431():
                    itu618_13.itu1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action431)

                itu618_13.enable_depolarization_loss = False
                Assert.assertFalse(itu618_13.enable_depolarization_loss)
                itu618_13.enable_depolarization_loss = True
                Assert.assertTrue(itu618_13.enable_depolarization_loss)

            else:
                Assert.fail("Unknown Rain Loss Model name")

        def action432():
            propChan.set_rain_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action432)
        root.unit_preferences.set_current_unit("Temperature", holdUnit)


# endregion


# region PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper
class PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper(object):
    def Run(self, rfEnv: "IPlatformRFEnvironment", root: "IStkObjectRoot"):
        holdUnit: str = root.unit_preferences.get_current_unit_abbrv("Temperature")
        root.unit_preferences.set_current_unit("Temperature", "degC")
        root.unit_preferences.set_current_unit("MassUnit", "g")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        arSupportedCFFLM = propChan.supported_clouds_and_fog_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedCFFLM))
        Assert.assertEqual("ITU-R P840-7", arSupportedCFFLM[0])
        Assert.assertEqual("ITU-R P840-6", arSupportedCFFLM[1])

        propChan.enable_clouds_and_fog_fading_loss = False
        Assert.assertFalse(propChan.enable_clouds_and_fog_fading_loss)

        propChan.enable_clouds_and_fog_fading_loss = True
        Assert.assertTrue(propChan.enable_clouds_and_fog_fading_loss)

        def action433():
            propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-5")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action433)

        propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-7")
        cfflm: "ICloudsAndFogFadingLossModel" = propChan.clouds_and_fog_fading_loss_model
        Assert.assertEqual("ITU-R P840-7", cfflm.name)
        Assert.assertEqual(CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE.P_840_7_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_7(clr.CastAs(cfflm, ICloudsAndFogFadingLossModelP840_7))

        propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-6")
        cfflm = propChan.clouds_and_fog_fading_loss_model
        Assert.assertEqual("ITU-R P840-6", cfflm.name)
        Assert.assertEqual(CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE.P_840_6_TYPE, cfflm.type)
        self.Test_IAgCloudsAndFogFadingLossModelP840_6(clr.CastAs(cfflm, ICloudsAndFogFadingLossModelP840_6))

        root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgCloudsAndFogFadingLossModelP840_7(self, cfflm7: "ICloudsAndFogFadingLossModelP840_7"):
        cfflm7.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm7.cloud_ceiling)
        cfflm7.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm7.cloud_ceiling)
        cfflm7.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm7.cloud_ceiling)

        def action434():
            cfflm7.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action434)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)

        def action435():
            cfflm7.cloud_layer_thickness = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action435)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = 100
        Assert.assertEqual(100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)

        def action436():
            cfflm7.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action436)

        def action437():
            cfflm7.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action437)

        def action438():
            cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action438)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)

        def action439():
            cfflm7.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action439)

        def action440():
            cfflm7.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action440)

        def action441():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action441)

        def action442():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action442)

        def action443():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action443)

        def action444():
            cfflm7.use_rain_height_as_cloud_layer_thickness = True

        TryCatchAssertBlock.ExpectedException("read-only", action444)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm7.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        def action445():
            cfflm7.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action445)

        def action446():
            cfflm7.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action446)

        def action447():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action447)

        def action448():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action448)

        def action449():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action449)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.FOGL_LIQ_WATER_CHOICE_MONTHLY_EXCEEDED
        cfflm7.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm7.liquid_water_percent_monthly_exceeded)
        cfflm7.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm7.liquid_water_percent_monthly_exceeded)
        cfflm7.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm7.average_data_month)
        cfflm7.average_data_month = 12
        Assert.assertEqual(12, cfflm7.average_data_month)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        def action450():
            cfflm7.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action450)

        def action451():
            cfflm7.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action451)

        def action452():
            cfflm7.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action452)

        def action453():
            cfflm7.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action453)

        def action454():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action454)

        def action455():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action455)

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "ICloudsAndFogFadingLossModelP840_6"):
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)

        def action456():
            cfflm6.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action456)

        def action457():
            cfflm6.cloud_ceiling = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action457)

        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)

        def action458():
            cfflm6.cloud_layer_thickness = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action458)

        def action459():
            cfflm6.cloud_layer_thickness = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action459)

        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = 100
        Assert.assertEqual(100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)

        def action460():
            cfflm6.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action460)

        def action461():
            cfflm6.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action461)

        def action462():
            cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action462)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)

        def action463():
            cfflm6.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action463)

        def action464():
            cfflm6.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action464)

        def action465():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action465)

        def action466():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action466)

        def action467():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action467)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm6.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.liquid_water_percent_annual_exceeded)
        cfflm6.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm6.liquid_water_percent_annual_exceeded)

        def action468():
            cfflm6.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action468)

        def action469():
            cfflm6.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action469)

        def action470():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action470)

        def action471():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action471)

        def action472():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action472)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.FOGL_LIQ_WATER_CHOICE_MONTHLY_EXCEEDED
        cfflm6.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm6.average_data_month)
        cfflm6.average_data_month = 12
        Assert.assertEqual(12, cfflm6.average_data_month)

        def action473():
            cfflm6.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action473)

        def action474():
            cfflm6.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action474)

        def action475():
            cfflm6.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action475)

        def action476():
            cfflm6.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action476)

        def action477():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action477)

        def action478():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action478)


# endregion


# region PlatformRF_Environment_AtmosphericAbsorptionHelper
class PlatformRF_Environment_AtmosphericAbsorptionHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel
        atmosAbsorb: "IAtmosphericAbsorptionModel" = propChan.atmos_absorption_model

        propChan.enable_atmos_absorption = False
        Assert.assertFalse(propChan.enable_atmos_absorption)

        def action479():
            propChan.set_atmos_absorption_model("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action479)

        propChan.enable_atmos_absorption = True
        Assert.assertTrue(propChan.enable_atmos_absorption)

        supportedAtmosAbsorptionModels = propChan.supported_atmos_absorption_models
        aaModelName: str
        for aaModelName in supportedAtmosAbsorptionModels:
            propChan.set_atmos_absorption_model(aaModelName)
            aaModel: "IAtmosphericAbsorptionModel" = propChan.atmos_absorption_model
            Assert.assertEqual(aaModelName, aaModel.name)
            if aaModelName == "ITU-R P676-9":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.I_T_U_R_P_676_9, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelITURP676(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelITURP676)
                )
            elif aaModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SCRIPT_PLUGIN, aaModel.type)
                    self.Test_IAgAtmosphericAbsorptionModelScriptPlugin(
                        clr.CastAs(aaModel, IAtmosphericAbsorptionModelScriptPlugin)
                    )

            elif aaModelName == "Simple Satcom":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.SIMPLE_SATCOM, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelSimpleSatcom(
                    clr.CastAs(aaModel, IAtmosphericAbsorptionModelSimpleSatcom)
                )
            elif aaModelName == "TIREM 3.31":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM331, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 3.20":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM320, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "TIREM 5.50":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.TIREM550, aaModel.type)
                self.Test_IAgAtmosphericAbsorptionModelTirem(clr.CastAs(aaModel, IAtmosphericAbsorptionModelTirem))
            elif aaModelName == "VOACAP":
                Assert.assertEqual(ATMOSPHERIC_ABSORPTION_MODEL_TYPE.VOACAP, aaModel.type)
                helper = AtmosphereHelper(self._root)
                helper.Test_IAgAtmosphericAbsorptionModelVoacap(clr.CastAs(aaModel, IAtmosphericAbsorptionModelVoacap))
            else:
                Assert.fail("Unknown model type")

        def action480():
            propChan.set_atmos_absorption_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action480)

        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgAtmosphericAbsorptionModelITURP676(self, iturp676: "IAtmosphericAbsorptionModelITURP676"):
        iturp676.fast_approximation_method = False
        Assert.assertFalse(iturp676.fast_approximation_method)
        iturp676.fast_approximation_method = True
        Assert.assertTrue(iturp676.fast_approximation_method)

        iturp676.seasonal_regional_method = False
        Assert.assertFalse(iturp676.seasonal_regional_method)
        iturp676.seasonal_regional_method = True
        Assert.assertTrue(iturp676.seasonal_regional_method)

    def Test_IAgAtmosphericAbsorptionModelScriptPlugin(self, scriptPlugin: "IAtmosphericAbsorptionModelScriptPlugin"):
        def action481():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action481)

        def action482():
            scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Could not initialize", action482)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)

        def action483():
            simpleSatcom.water_vapor_concentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action483)

        def action484():
            simpleSatcom.water_vapor_concentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action484)

        simpleSatcom.surface_temperature = -100
        Assert.assertEqual(-100, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)

        def action485():
            simpleSatcom.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action485)

        def action486():
            simpleSatcom.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action486)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        tirem.surface_temperature = -100
        Assert.assertEqual(-100, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)

        def action487():
            tirem.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action487)

        def action488():
            tirem.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action488)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)

        def action489():
            tirem.surface_humidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action489)

        def action490():
            tirem.surface_humidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action490)

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)

        def action491():
            tirem.surface_conductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action491)

        def action492():
            tirem.surface_conductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action492)

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)

        def action493():
            tirem.surface_refractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action493)

        def action494():
            tirem.surface_refractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action494)

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)

        def action495():
            tirem.relative_permittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action495)

        def action496():
            tirem.relative_permittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action496)

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        def action497():
            tirem.terrain_sample_resolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action497)

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)

        def action498():
            tirem.terrain_sample_resolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action498)

        def action499():
            tirem.terrain_sample_resolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action499)


# endregion


# region PlatformRF_Environment_UrbanAndTerrestrialHelper
class PlatformRF_Environment_UrbanAndTerrestrialHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        propChan.enable_urban_terrestrial_loss = False
        Assert.assertFalse(propChan.enable_urban_terrestrial_loss)

        def action500():
            propChan.set_urban_terrestrial_loss_model("Two Ray")

        TryCatchAssertBlock.ExpectedException("read-only", action500)

        propChan.enable_urban_terrestrial_loss = True
        Assert.assertTrue(propChan.enable_urban_terrestrial_loss)

        supportedUrbTerrModels = propChan.supported_urban_terrestrial_loss_models
        utModelName: str
        for utModelName in supportedUrbTerrModels:
            propChan.set_urban_terrestrial_loss_model(utModelName)
            utModel: "IUrbanTerrestrialLossModel" = propChan.urban_terrestrial_loss_model
            Assert.assertEqual(utModelName, utModel.name)
            if utModelName == "Two Ray":
                Assert.assertEqual(URBAN_TERRESTRIAL_LOSS_MODEL_TYPE.TWO_RAY, utModel.type)
                self.Test_IAgUrbanTerrestrialLossModelTwoRay(clr.CastAs(utModel, IUrbanTerrestrialLossModelTwoRay))
            elif utModelName == "Urban Propagation Wireless InSite RT":
                Assert.assertEqual(URBAN_TERRESTRIAL_LOSS_MODEL_TYPE.WIRELESS_IN_SITE_RT, utModel.type)
                self.Test_IAgUrbanTerrestrialLossModelWirelessInSiteRT(
                    clr.CastAs(utModel, IUrbanTerrestrialLossModelWirelessInSiteRT)
                )
            else:
                Assert.fail("Unknown model type")

        def action501():
            propChan.set_urban_terrestrial_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action501)
        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "IUrbanTerrestrialLossModelTwoRay"):
        twoRay.loss_factor = 0.1
        Assert.assertEqual(0.1, twoRay.loss_factor)
        twoRay.loss_factor = 10
        Assert.assertEqual(10, twoRay.loss_factor)

        def action502():
            twoRay.loss_factor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action502)

        def action503():
            twoRay.loss_factor = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action503)

        twoRay.surface_temperature = -100
        Assert.assertEqual(-100, twoRay.surface_temperature)
        twoRay.surface_temperature = 100
        Assert.assertEqual(100, twoRay.surface_temperature)

        def action504():
            twoRay.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action504)

        def action505():
            twoRay.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action505)

    def Test_IAgUrbanTerrestrialLossModelWirelessInSiteRT(self, wisRT: "IUrbanTerrestrialLossModelWirelessInSiteRT"):
        arSupportedCalculationMethods = wisRT.supported_calculation_methods
        Assert.assertEqual(5, Array.Length(arSupportedCalculationMethods))
        sCalcMethod: str
        for sCalcMethod in arSupportedCalculationMethods:
            if (
                ((((sCalcMethod == "COST_HATA")) or ((sCalcMethod == "HATA"))) or ((sCalcMethod == "OPAR")))
                or ((sCalcMethod == "TPGEODESIC"))
            ) or ((sCalcMethod == "WALFISCH_IKEGAMI")):
                wisRT.calculation_method = sCalcMethod
                Assert.assertEqual(sCalcMethod, wisRT.calculation_method)
            else:
                Assert.fail("Unknown Calculation Method")

            wisRT.enable_ground_reflection = False
            Assert.assertFalse(wisRT.enable_ground_reflection)
            wisRT.enable_ground_reflection = True
            Assert.assertTrue(wisRT.enable_ground_reflection)

            wisRT.surface_temperature = -100
            Assert.assertEqual(-100, wisRT.surface_temperature)
            wisRT.surface_temperature = 100
            Assert.assertEqual(100, wisRT.surface_temperature)

            def action506():
                wisRT.surface_temperature = -101

            TryCatchAssertBlock.ExpectedException("is invalid", action506)

            def action507():
                wisRT.surface_temperature = 101

            TryCatchAssertBlock.ExpectedException("is invalid", action507)

            geometryData: "IWirelessInSiteRTGeometryData" = wisRT.geometry_data

            def action508():
                geometryData.filename = TestBase.GetScenarioFile("Bogus.shp")

            TryCatchAssertBlock.ExpectedException("does not exist", action508)
            geometryData.filename = TestBase.GetScenarioFile("Cochise.shp")

            geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84
            Assert.assertEqual(PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84, geometryData.projection_horizontal_datum)

            def action509():
                geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.UTMWGS84

            TryCatchAssertBlock.ExpectedException("must be in", action509)

            geometryData.building_height_data_attribute = "STATE_NAME"
            Assert.assertEqual("STATE_NAME", geometryData.building_height_data_attribute)

            def action510():
                geometryData.building_height_data_attribute = "Some"

            TryCatchAssertBlock.ExpectedException("must be in", action510)

            geometryData.building_height_reference_method = BUILD_HEIGHT_REFERENCE_METHOD.HEIGHT_ABOVE_SEA_LEVEL
            Assert.assertEqual(
                BUILD_HEIGHT_REFERENCE_METHOD.HEIGHT_ABOVE_SEA_LEVEL, geometryData.building_height_reference_method
            )
            geometryData.building_height_reference_method = BUILD_HEIGHT_REFERENCE_METHOD.HEIGHT_ABOVE_TERRAIN
            Assert.assertEqual(
                BUILD_HEIGHT_REFERENCE_METHOD.HEIGHT_ABOVE_TERRAIN, geometryData.building_height_reference_method
            )

            geometryData.override_geometry_tile_origin = False
            Assert.assertFalse(geometryData.override_geometry_tile_origin)

            def action511():
                geometryData.geometry_tile_origin_latitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action511)

            def action512():
                geometryData.geometry_tile_origin_longitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action512)

            geometryData.override_geometry_tile_origin = True
            Assert.assertTrue(geometryData.override_geometry_tile_origin)

            geometryData.geometry_tile_origin_latitude = -90
            Assert.assertEqual(-90, geometryData.geometry_tile_origin_latitude)
            geometryData.geometry_tile_origin_latitude = 90
            Assert.assertEqual(90, geometryData.geometry_tile_origin_latitude)

            def action513():
                geometryData.geometry_tile_origin_latitude = -91

            TryCatchAssertBlock.ExpectedException("is invalid", action513)

            def action514():
                geometryData.geometry_tile_origin_latitude = 91

            TryCatchAssertBlock.ExpectedException("is invalid", action514)

            geometryData.geometry_tile_origin_longitude = -180
            Assert.assertEqual(-180, geometryData.geometry_tile_origin_longitude)
            geometryData.geometry_tile_origin_longitude = 360
            Assert.assertEqual(360, geometryData.geometry_tile_origin_longitude)

            def action515():
                geometryData.geometry_tile_origin_longitude = -181

            TryCatchAssertBlock.ExpectedException("is invalid", action515)

            def action516():
                geometryData.geometry_tile_origin_longitude = 361

            TryCatchAssertBlock.ExpectedException("is invalid", action516)

            geometryData.use_terrain_data = False
            Assert.assertFalse(geometryData.use_terrain_data)

            Assert.assertAlmostEqual(32.43, float(geometryData.terrain_extent_max_latitude), delta=0.01)
            Assert.assertAlmostEqual(-109.05, float(geometryData.terrain_extent_max_longitude), delta=0.01)
            Assert.assertAlmostEqual(31.33, float(geometryData.terrain_extent_min_latitude), delta=0.01)
            Assert.assertAlmostEqual(-110.46, float(geometryData.terrain_extent_min_longitude), delta=0.01)

            geometryData.use_terrain_data = True
            Assert.assertTrue(geometryData.use_terrain_data)

            Assert.assertAlmostEqual(32.43, float(geometryData.terrain_extent_max_latitude), delta=0.01)
            Assert.assertAlmostEqual(-109.05, float(geometryData.terrain_extent_max_longitude), delta=0.01)
            Assert.assertAlmostEqual(31.33, float(geometryData.terrain_extent_min_latitude), delta=0.01)
            Assert.assertAlmostEqual(-110.46, float(geometryData.terrain_extent_min_longitude), delta=0.01)


# endregion


# region PlatformRF_Environment_TropoScintillationHelper
class PlatformRF_Environment_TropoScintillationHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        holdUnit: str = self._root.unit_preferences.get_current_unit_abbrv("Temperature")
        self._root.unit_preferences.set_current_unit("Temperature", "degC")

        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        arSupportedTSFLM = propChan.supported_tropospheric_scintillation_fading_loss_models
        Assert.assertEqual(2, Array.Length(arSupportedTSFLM))
        Assert.assertEqual("ITU-R P618-12", arSupportedTSFLM[0])
        Assert.assertEqual("ITU-R P618-8", arSupportedTSFLM[1])

        propChan.enable_tropospheric_scintillation_fading_loss = False
        Assert.assertFalse(propChan.enable_tropospheric_scintillation_fading_loss)

        def action517():
            propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")

        TryCatchAssertBlock.ExpectedException("read-only", action517)

        propChan.enable_tropospheric_scintillation_fading_loss = True
        Assert.assertTrue(propChan.enable_tropospheric_scintillation_fading_loss)

        propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")
        tsflm: "ITroposphericScintillationFadingLossModel" = propChan.tropospheric_scintillation_fading_loss_model
        Assert.assertEqual("ITU-R P618-12", tsflm.name)
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE.P_618_12_TYPE, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_12(
            clr.CastAs(tsflm, ITroposphericScintillationFadingLossModelP618_12)
        )

        propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-8")
        tsflm = propChan.tropospheric_scintillation_fading_loss_model
        Assert.assertEqual("ITU-R P618-8", tsflm.name)
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE.P_618_8_TYPE, tsflm.type)
        self.Test_IAgTroposphericScintillationFadingLossModelP618_8(
            clr.CastAs(tsflm, ITroposphericScintillationFadingLossModelP618_8)
        )

    def Test_IAgTroposphericScintillationFadingLossModelP618_12(
        self, tsflm12: "ITroposphericScintillationFadingLossModelP618_12"
    ):
        def action518():
            tsflm12.compute_deep_fade = True

        TryCatchAssertBlock.ExpectedException("read-only", action518)  # Deprecated and should not be used.

        tsflm12.surface_temperature = -100
        Assert.assertEqual(-100, tsflm12.surface_temperature)
        tsflm12.surface_temperature = 100
        Assert.assertEqual(100, tsflm12.surface_temperature)

        def action519():
            tsflm12.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action519)

        def action520():
            tsflm12.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action520)

        tsflm12.fade_outage = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_outage)
        tsflm12.fade_outage = 40
        Assert.assertEqual(40, tsflm12.fade_outage)

        def action521():
            tsflm12.fade_outage = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action521)

        def action522():
            tsflm12.fade_outage = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action522)

        tsflm12.fade_exceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_exceeded)
        tsflm12.fade_exceeded = 50
        Assert.assertEqual(50, tsflm12.fade_exceeded)

        def action523():
            tsflm12.fade_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action523)

        def action524():
            tsflm12.fade_exceeded = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action524)

        tsflm12.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm12.percent_time_refractivity_gradient)
        tsflm12.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm12.percent_time_refractivity_gradient)

        def action525():
            tsflm12.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action525)

        def action526():
            tsflm12.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action526)

        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH, tsflm12.average_time_choice)
        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR, tsflm12.average_time_choice)

        def action527():
            tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action527)

    def Test_IAgTroposphericScintillationFadingLossModelP618_8(
        self, tsflm8: "ITroposphericScintillationFadingLossModelP618_8"
    ):
        tsflm8.compute_deep_fade = False
        Assert.assertFalse(tsflm8.compute_deep_fade)
        tsflm8.compute_deep_fade = True
        Assert.assertTrue(tsflm8.compute_deep_fade)

        tsflm8.surface_temperature = -100
        Assert.assertEqual(-100, tsflm8.surface_temperature)
        tsflm8.surface_temperature = 100
        Assert.assertEqual(100, tsflm8.surface_temperature)
        tsflm8.surface_temperature = -100
        Assert.assertEqual(-100, tsflm8.surface_temperature)

        def action528():
            tsflm8.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action528)

        def action529():
            tsflm8.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action529)

        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        tsflm8.fade_outage = 100
        Assert.assertEqual(100, tsflm8.fade_outage)
        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)

        def action530():
            tsflm8.fade_outage = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action530)

        def action531():
            tsflm8.fade_outage = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action531)

        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)

        def action532():
            tsflm8.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action532)

        def action533():
            tsflm8.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action533)


# endregion


# region PlatformRF_Environment_CustomModelsHelper
class PlatformRF_Environment_CustomModelsHelper(object):
    def __init__(self, root: "IStkObjectRoot"):
        self._root: "IStkObjectRoot" = root

    # endregion

    def Run(self, rfEnv: "IPlatformRFEnvironment"):
        propChan: "IPropagationChannel" = rfEnv.propagation_channel

        self.Test_IAgCustomPropagationModel(propChan.custom_a)
        self.Test_IAgCustomPropagationModel(propChan.custom_b)
        self.Test_IAgCustomPropagationModel(propChan.custom_c)

    def Test_IAgCustomPropagationModel(self, customModel: "ICustomPropagationModel"):
        if not OSHelper.IsLinux():
            customModel.enable = False
            Assert.assertFalse(customModel.enable)

            def action534():
                customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")

            TryCatchAssertBlock.ExpectedException("read-only", action534)

            customModel.enable = True
            Assert.assertTrue(customModel.enable)

            def action535():
                customModel.filename = r"C:\bogus.vbs"

            TryCatchAssertBlock.ExpectedException("does not exist", action535)

            def action536():
                customModel.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

            TryCatchAssertBlock.ExpectedException("Could not initialize", action536)
            customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.filename)


# endregion
# endregion
# endregion
