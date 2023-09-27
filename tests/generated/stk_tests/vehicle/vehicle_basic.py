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

            def action61():
                oCTurn.time_offset = 0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action61)

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

            def action62():
                oCOffset.constraint_offset = 1234.56

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action62)

        if oProfile.type == "Fixed in Axes":
            oFixed: "IVehicleProfileFixedInAxes" = clr.Convert(oProfile, IVehicleProfileFixedInAxes)
            Assert.assertIsNotNone(oFixed)
            arAvailRefAxes = oFixed.available_reference_axes
            # ReferenceAxes
            self.m_logger.WriteLine5("\t\t\t\tThe current ReferenceAxes is: {0}", oFixed.reference_axes)
            oFixed.reference_axes = "Star/Star1 MeanEclpJ2000"
            self.m_logger.WriteLine5("\t\t\t\tThe new ReferenceAxes is: {0}", oFixed.reference_axes)
            Assert.assertEqual("Star/Star1 MeanEclpJ2000", oFixed.reference_axes)

            def action63():
                oFixed.reference_axes = ""

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action63)

            def action64():
                oFixed.reference_axes = "InvalidReferenceAxes"

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action64)
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

            def action65():
                profilePrecessingSpin.nutation_angle = 123.4

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action65)
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

            def action66():
                profilePrecessingSpin.reference_axes = "bogus"

            TryCatchAssertBlock.DoAssert("Should not allow a bogus reference axes.", action66)

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

            def action67():
                profileSpinning.rate = 123456.789

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action67)
            # Offset
            self.m_logger.WriteLine6("\t\t\t\tThe current Offset is: {0}", profileSpinning.offset)
            profileSpinning.offset = 12.34
            self.m_logger.WriteLine6("\t\t\t\tThe new Offset is: {0}", profileSpinning.offset)
            Assert.assertEqual(12.34, profileSpinning.offset)

            def action68():
                profileSpinning.offset = 1234.5

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action68)
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

            def action69():
                oAOffset.alignment_offset = 1234.56

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action69)

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

            def action70():
                profileSpinAboutXxx.rate = 123456.789

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action70)
            # Offset
            self.m_logger.WriteLine6("\t\t\t\tThe current Offset is: {0}", profileSpinAboutXxx.offset)
            profileSpinAboutXxx.offset = 12.34
            self.m_logger.WriteLine6("\t\t\t\tThe new Offset is: {0}", profileSpinAboutXxx.offset)
            Assert.assertEqual(12.34, profileSpinAboutXxx.offset)

            def action71():
                profileSpinAboutXxx.offset = 1234.5

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action71)

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

            def action72():
                oGPS.model_type = GPS_ATTITUDE_MODEL_TYPE.MODEL_TYPE_UNKNOWN

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action72)

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

        def action73():
            oVector.reference_vector = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action73)

        def action74():
            oVector.reference_vector = "InvalidReferenceVector"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action74)

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

        def action75():
            oExternal.load("InvalidFileName.a")

        TryCatchAssertBlock.DoAssert("Should not allow to load an invalid file.", action75)

        def action76():
            oExternal.load("")

        TryCatchAssertBlock.DoAssert("Should not allow to load an invalid file.", action76)
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

        def action77():
            oOffset.rate = 123456.789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action77)
        # Offset
        self.m_logger.WriteLine6("\t\t\t\tThe current Offset is: {0}", oOffset.offset)
        oOffset.offset = 12.34
        self.m_logger.WriteLine6("\t\t\t\tThe new Offset is: {0}", oOffset.offset)
        Assert.assertEqual(12.34, oOffset.offset)

        def action78():
            oOffset.offset = 1234.5

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action78)

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

            def action79():
                oAdvanced.use_light_time_delay = True

            # UseLightTimeDelay (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action79)

            def action80():
                oAdvanced.time_sense = IV_TIME_SENSE.RECEIVE

            # TimeSense (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action80)

            def action81():
                oAdvanced.time_delay_convergence = 0.1

            # TimeDelayConvergence (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action81)

            def action82():
                (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.ANNUAL

            # AberrationType (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action82)
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

            def action83():
                oAdvanced.time_sense = IV_TIME_SENSE.RECEIVE

            # TimeSense (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action83)

            def action84():
                oAdvanced.time_delay_convergence = 0.1

            # TimeDelayConvergence (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action84)

            def action85():
                (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.ANNUAL

            # AberrationType (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action85)
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

            def action86():
                (clr.Convert(oAdvanced, IAccessAdvanced)).aberration_type = ABERRATION_TYPE.UNKNOWN

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action86)
            # TimeDelayConvergence
            self.m_logger.WriteLine6("\tThe current TimeDelayConvergence is: {0}", oAdvanced.time_delay_convergence)
            oAdvanced.time_delay_convergence = 0.1
            self.m_logger.WriteLine6("\tThe new TimeDelayConvergence is: {0}", oAdvanced.time_delay_convergence)
            Assert.assertEqual(0.1, oAdvanced.time_delay_convergence)

            def action87():
                oAdvanced.time_delay_convergence = 0.5

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action87)
            # TimeSense
            self.m_logger.WriteLine6("\tThe current TimeSense is: {0}", oAdvanced.time_sense)
            oAdvanced.time_sense = IV_TIME_SENSE.RECEIVE
            self.m_logger.WriteLine6("\tThe new TimeSense is: {0}", oAdvanced.time_sense)
            Assert.assertEqual(IV_TIME_SENSE.RECEIVE, oAdvanced.time_sense)
            oAdvanced.time_sense = IV_TIME_SENSE.TRANSMIT
            self.m_logger.WriteLine6("\tThe new TimeSense is: {0}", oAdvanced.time_sense)
            Assert.assertEqual(IV_TIME_SENSE.TRANSMIT, oAdvanced.time_sense)

            def action88():
                oAdvanced.time_sense = IV_TIME_SENSE.UNKNOWN

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action88)
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

        def action89():
            element2: "IVehicleTargetPointingElement" = oCollection[oCollection.count]

        TryCatchAssertBlock.DoAssert("IVehicleTargetPointingCollection bad index", action89)

        arTargets = oCollection.available_targets
        self.m_logger.WriteLine3("\tThe TargetPointing collection has: {0} available targets.", Array.Length(arTargets))
        if bReadOnly:
            if Array.Length(arTargets) > 0:

                def action90():
                    oCollection.add(str(arTargets[0]))

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action90)

            if Array.Length(arTargets) > 0:
                oCollection.add_position_as_target(10.0, 20.0, 30.0)
                e0: "IVehicleTargetPointingElement" = oCollection[0]

                def action91():
                    oCollection.add_position_as_target(-10000.0, -10000.0, -10000.0)

                TryCatchAssertBlock.DoAssert("AddPositionAsTarget bad params.", action91)

            if oCollection.count > 0:

                def action92():
                    oCollection.remove_at(0)

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action92)

            if oCollection.count > 0:

                def action93():
                    oCollection.remove(str(arTargets[0]))

                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action93)

            def action94():
                oCollection.remove_all()

            # RemoveAll
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action94)

        else:
            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3("\tThe new TargetPointing collection contains: {0} elements.", oCollection.count)
            Assert.assertEqual(0, oCollection.count)

            def action95():
                oCollection.add("Bogus")

            TryCatchAssertBlock.DoAssert("Should not allow to add a bad target.", action95)

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

            def action96():
                oCollection.remove("Bogus")

            TryCatchAssertBlock.DoAssert("Should not remove thru bad name.", action96)

            # RemoveAt
            oCollection.remove_at(0)
            Assert.assertEqual((Array.Length(arTargets) - 2), oCollection.count)
            self.m_logger.WriteLine3("\tThe new TargetPointing collection contains: {0} elements.", oCollection.count)

            def action97():
                oCollection.remove_at(-1)

            TryCatchAssertBlock.DoAssert("Should not remove thru bad index -1.", action97)

            def action98():
                oCollection.remove_at(oCollection.count)

            TryCatchAssertBlock.DoAssert("Should not remove thru bad index.", action98)

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

            def action99():
                targetPointingElement.constrained_vector_reference = ""

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action99)

            def action100():
                targetPointingElement.constrained_vector_reference = "InvalidReferenceVector"

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action100)
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

            def action101():
                oTimes.use_access_times = True

            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action101)
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

        def action102():
            oAttitude.wx = 1234567.89

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action102)
        # Wy
        self.m_logger.WriteLine6("\tThe current Wy is: {0}", oAttitude.wy)
        oAttitude.wy = 0.000349066
        self.m_logger.WriteLine6("\tThe new Wy is: {0}", oAttitude.wy)
        Assert.assertEqual(0.000349066, oAttitude.wy)

        def action103():
            oAttitude.wy = 1234567.89

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action103)
        # Wz
        self.m_logger.WriteLine6("\tThe current Wz is: {0}", oAttitude.wz)
        oAttitude.wz = 0.000523599
        self.m_logger.WriteLine6("\tThe new Wz is: {0}", oAttitude.wz)
        Assert.assertEqual(0.000523599, oAttitude.wz)

        def action104():
            oAttitude.wz = 1234567.89

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action104)

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

        def action105():
            oTorque.torque_file = r"..\..\..\Scenario\TorquesTimeBodyFixed.tq"

        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action105)
        oTorque.use_torque_file = True
        self.m_logger.WriteLine4("\tThe new UseTorqueFile is: {0}", oTorque.use_torque_file)
        Assert.assertTrue(oTorque.use_torque_file)
        # TorqueFile
        self.m_logger.WriteLine5("\tThe current TorqueFile is: {0}", oTorque.torque_file)
        oTorque.torque_file = TestBase.GetScenarioFile(r"TorquesTimeBodyFixed.tq")
        self.m_logger.WriteLine5("\tThe new TorqueFile is: {0}", oTorque.torque_file)
        Assert.assertEqual("TorquesTimeBodyFixed.tq", oTorque.torque_file)

        def action106():
            oTorque.torque_file = ""

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action106)

        def action107():
            oTorque.torque_file = "InvalidFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action107)
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

        def action108():
            oTime: "IAccessTime" = oCollection[oCollection.count]

        # Item
        TryCatchAssertBlock.DoAssert("Bad IAccessTimeCollection index", action108)
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

            def action109():
                oCollection.add("Satellite/Satellite1")

            # Add
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action109)

            def action110():
                oCollection.remove_at(0)

            # RemoveAt
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action110)

            def action111():
                oCollection.remove_all()

            # RemoveAll
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action111)

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

            def action112():
                element: "IVehicleScheduleTimesElement" = oCollection[oCollection.count]

            TryCatchAssertBlock.DoAssert("IVehicleScheduleTimesCollection bad index", action112)

            def action113():
                oCollection.add("bogus")

            TryCatchAssertBlock.DoAssert("bogus schedule time element", action113)

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

            def action114():
                oCollection.remove_at(oCollection.count)

            # RemoveAt
            TryCatchAssertBlock.DoAssert("oCollection.RemoveAt(oCollection.Count)", action114)

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

        def action115():
            oDuration.look_ahead = 0

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action115)
        # LookBehind
        self.m_logger.WriteLine6("\tThe current LookBehind is: {0}", oDuration.look_behind)
        oDuration.look_behind = 456.789
        self.m_logger.WriteLine6("\tThe new LookBehind is: {0}", oDuration.look_behind)
        Assert.assertEqual(456.789, oDuration.look_behind)

        def action116():
            oDuration.look_behind = 123456789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action116)

        # BlockFactor
        oAttitude.block_factor = 20
        Assert.assertEqual(20, oAttitude.block_factor)
        oAttitude.block_factor = 40
        Assert.assertEqual(40, oAttitude.block_factor)

        def action117():
            oAttitude.block_factor = 19

        TryCatchAssertBlock.DoAssert("Should not allow invalid values.", action117)
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

            def action118():
                oDetection.set_type(oDetection.type)

            # SetType (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action118)
            if oDetection.type == EVENT_DETECTION.NO_SUB_SAMPLING:
                oNoSubSampling: "IEventDetectionNoSubSampling" = clr.CastAs(
                    oDetection.strategy, IEventDetectionNoSubSampling
                )
                Assert.assertIsNotNone(oNoSubSampling)
            elif oDetection.type == EVENT_DETECTION.USE_SUB_SAMPLING:
                oSubSampling: "IEventDetectionSubSampling" = clr.CastAs(oDetection.strategy, IEventDetectionSubSampling)
                Assert.assertIsNotNone(oSubSampling)

                def action119():
                    oSubSampling.abs_value_convergence = 0.1

                # AbsValueConvergence (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action119)

                def action120():
                    oSubSampling.rel_value_convergence = 0.1

                # RelValueConvergence (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action120)

                def action121():
                    oSubSampling.time_convergence = 0.01

                # TimeConvergence (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action121)
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

                    def action122():
                        oSubSampling.time_convergence = -0.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action122)
                    # AbsValueConvergence
                    self.m_logger.WriteLine6(
                        "\t\t\tThe current AbsValueConvergence is: {0}", oSubSampling.abs_value_convergence
                    )
                    oSubSampling.abs_value_convergence = 0.5
                    self.m_logger.WriteLine6(
                        "\t\t\tThe new AbsValueConvergence is: {0}", oSubSampling.abs_value_convergence
                    )
                    Assert.assertEqual(0.5, oSubSampling.abs_value_convergence)

                    def action123():
                        oSubSampling.abs_value_convergence = -0.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action123)
                    # RelValueConvergence
                    self.m_logger.WriteLine6(
                        "\t\t\tThe current RelValueConvergence is: {0}", oSubSampling.rel_value_convergence
                    )
                    oSubSampling.rel_value_convergence = 0.5
                    self.m_logger.WriteLine6(
                        "\t\t\tThe new RelValueConvergence is: {0}", oSubSampling.rel_value_convergence
                    )
                    Assert.assertEqual(0.5, oSubSampling.rel_value_convergence)

                    def action124():
                        oSubSampling.rel_value_convergence = -0.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action124)
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

            def action125():
                oSampling.set_type(oSampling.type)

            # SetType (readonly)
            TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action125)
            if oSampling.type == SAMPLING_METHOD.ADAPTIVE:
                oAdaptive: "ISamplingMethodAdaptive" = clr.CastAs(oSampling.strategy, ISamplingMethodAdaptive)
                Assert.assertIsNotNone(oAdaptive)

                def action126():
                    oAdaptive.min_time_step = 0.1

                # MinTimeStep (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action126)

                def action127():
                    oAdaptive.max_time_step = 1.1

                # MaxTimeStep (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action127)
            elif oSampling.type == SAMPLING_METHOD.FIXED_STEP:
                oFixedStep: "ISamplingMethodFixedStep" = clr.CastAs(oSampling.strategy, ISamplingMethodFixedStep)
                Assert.assertIsNotNone(oFixedStep)

                def action128():
                    oFixedStep.fixed_time_step = 123

                # FixedTimeStep (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action128)

                def action129():
                    oFixedStep.time_bound = 123

                # TimeBound (readonly)
                TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action129)
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

                    def action130():
                        oAdaptive.min_time_step = -12.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action130)
                    # MaxTimeStep
                    self.m_logger.WriteLine6("\t\t\tThe current MaxTimeStep is: {0}", oAdaptive.max_time_step)
                    oAdaptive.max_time_step = 12.5
                    self.m_logger.WriteLine6("\t\t\tThe new MaxTimeStep is: {0}", oAdaptive.max_time_step)
                    Assert.assertEqual(12.5, oAdaptive.max_time_step)

                    def action131():
                        oAdaptive.max_time_step = -12.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action131)
                elif oSampling.type == SAMPLING_METHOD.FIXED_STEP:
                    # Strategy
                    oFixedStep: "ISamplingMethodFixedStep" = clr.CastAs(oSampling.strategy, ISamplingMethodFixedStep)
                    Assert.assertIsNotNone(oFixedStep)
                    # FixedTimeStep
                    self.m_logger.WriteLine6("\t\t\tThe current FixedTimeStep is: {0}", oFixedStep.fixed_time_step)
                    oFixedStep.fixed_time_step = 34.5
                    self.m_logger.WriteLine6("\t\t\tThe new FixedTimeStep is: {0}", oFixedStep.fixed_time_step)
                    Assert.assertEqual(34.5, oFixedStep.fixed_time_step)

                    def action132():
                        oFixedStep.fixed_time_step = -34.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action132)
                    # TimeBound
                    self.m_logger.WriteLine6("\t\t\tThe current TimeBound is: {0}", oFixedStep.time_bound)
                    oFixedStep.time_bound = 34.5
                    self.m_logger.WriteLine6("\t\t\tThe new TimeBound is: {0}", oFixedStep.time_bound)
                    Assert.assertEqual(34.5, oFixedStep.time_bound)

                    def action133():
                        oFixedStep.time_bound = -34.5

                    TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action133)
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

        def action134():
            spatialState.fixed_orientation.assign(fo)

        TryCatchAssertBlock.DoAssert("Should not allow assignment to read-only attributes.", action134)

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

        def action135():
            laserPropChan.set_atmospheric_loss_model("Beer-Bouguer-Lambert Law")

        TryCatchAssertBlock.ExpectedException("read-only", action135)

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

        def action136():
            bbllLayerColl[3].top_height = 41

        TryCatchAssertBlock.ExpectedException("read only", action136)
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

        def action137():
            bbllLayerColl[3].top_height = 101

        TryCatchAssertBlock.ExpectedException("invalid", action137)
        bbllLayerColl[3].top_height = 6
        Assert.assertEqual(6, bbllLayerColl[3].top_height)

        def action138():
            bbllLayerColl[3].extinction_coefficient = -1

        TryCatchAssertBlock.ExpectedException("invalid", action138)
        bbllLayerColl[3].extinction_coefficient = 1.5
        Assert.assertEqual(1.5, bbllLayerColl[3].extinction_coefficient)

        def action139():
            bbllLayerColl.remove_at(5)

        TryCatchAssertBlock.ExpectedException("out of range", action139)
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

        def action140():
            laserPropChan.set_atmospheric_loss_model("MODTRAN-derived Lookup Table")

        TryCatchAssertBlock.ExpectedException("read-only", action140)

        laserPropChan.enable_atmospheric_loss_model = True
        Assert.assertTrue(laserPropChan.enable_atmospheric_loss_model)

        laserAtmosLossModel = laserPropChan.atmospheric_loss_model

        def action141():
            laserPropChan.set_atmospheric_loss_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action141)
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

        def action142():
            modtran.visibility = 0.1

        TryCatchAssertBlock.ExpectedException("invalid", action142)

        def action143():
            modtran.visibility = 51

        TryCatchAssertBlock.ExpectedException("invalid", action143)

        modtran.relative_humidity = 0
        Assert.assertEqual(0, modtran.relative_humidity)
        modtran.relative_humidity = 100
        Assert.assertEqual(100, modtran.relative_humidity)

        def action144():
            modtran.relative_humidity = -1

        TryCatchAssertBlock.ExpectedException("invalid", action144)

        def action145():
            modtran.relative_humidity = 101

        TryCatchAssertBlock.ExpectedException("invalid", action145)

        modtran.surface_temperature = 190
        Assert.assertEqual(190, modtran.surface_temperature)
        modtran.surface_temperature = 320
        Assert.assertEqual(320, modtran.surface_temperature)

        def action146():
            modtran.surface_temperature = 189

        TryCatchAssertBlock.ExpectedException("invalid", action146)

        def action147():
            modtran.surface_temperature = 321

        TryCatchAssertBlock.ExpectedException("invalid", action147)


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

        def action148():
            laserPropChan.set_tropospheric_scintillation_loss_model("ITU-R P1814")

        TryCatchAssertBlock.ExpectedException("read-only", action148)

        laserPropChan.enable_tropospheric_scintillation_loss_model = True
        Assert.assertTrue(laserPropChan.enable_tropospheric_scintillation_loss_model)

        laserTropoScint = laserPropChan.tropospheric_scintillation_loss_model

        def action149():
            laserPropChan.set_atmospheric_loss_model("Bogus")

        TryCatchAssertBlock.ExpectedException("Invalid", action149)
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

        def action150():
            propChan.set_rain_loss_model("Crane 1985")

        TryCatchAssertBlock.ExpectedException("read-only", action150)

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

                def action151():
                    crane85.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action151)

                def action152():
                    crane85.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action152)

            elif rainLossModelName == "Script Plugin":
                if not OSHelper.IsLinux():
                    # script plugins do not work on linux
                    Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.SCRIPT_PLUGIN, rainLossModel.type)
                    scriptPlugin: "IRainLossModelScriptPlugin" = clr.CastAs(rainLossModel, IRainLossModelScriptPlugin)

                    def action153():
                        scriptPlugin.filename = r"C:\bogus.vbs"

                    TryCatchAssertBlock.ExpectedException("does not exist", action153)

                    def action154():
                        scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

                    TryCatchAssertBlock.ExpectedException("Could not initialize", action154)
                    scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_RainLossModel.vbs")
                    Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_RainLossModel.vbs"), scriptPlugin.filename)

            elif rainLossModelName == "CCIR 1983":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CCIR1983, rainLossModel.type)
                ccir83: "IRainLossModelCCIR1983" = clr.CastAs(rainLossModel, IRainLossModelCCIR1983)
                ccir83.surface_temperature = -100
                Assert.assertEqual(-100, ccir83.surface_temperature)
                ccir83.surface_temperature = 100
                Assert.assertEqual(100, ccir83.surface_temperature)

                def action155():
                    ccir83.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action155)

                def action156():
                    ccir83.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action156)

            elif rainLossModelName == "Crane 1982":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.CRANE1982, rainLossModel.type)
                crane82: "IRainLossModelCrane1982" = clr.CastAs(rainLossModel, IRainLossModelCrane1982)
                crane82.surface_temperature = -100
                Assert.assertEqual(-100, crane82.surface_temperature)
                crane82.surface_temperature = 100
                Assert.assertEqual(100, crane82.surface_temperature)

                def action157():
                    crane82.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action157)

                def action158():
                    crane82.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action158)

            elif rainLossModelName == "ITU-R P618-10":
                Assert.assertEqual(RAIN_LOSS_MODEL_TYPE.I_T_U_R_P_618_10, rainLossModel.type)
                itu618_10: "IRainLossModelITURP618_10" = clr.CastAs(rainLossModel, IRainLossModelITURP618_10)
                itu618_10.surface_temperature = -100
                Assert.assertEqual(-100, itu618_10.surface_temperature)
                itu618_10.surface_temperature = 100
                Assert.assertEqual(100, itu618_10.surface_temperature)

                def action159():
                    itu618_10.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action159)

                def action160():
                    itu618_10.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action160)
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

                def action161():
                    itu618_12.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action161)

                def action162():
                    itu618_12.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action162)
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

                def action163():
                    itu618_13.surface_temperature = -101

                TryCatchAssertBlock.ExpectedException("is invalid", action163)

                def action164():
                    itu618_13.surface_temperature = 101

                TryCatchAssertBlock.ExpectedException("is invalid", action164)

                def action165():
                    itu618_13.use_annual_itu1510 = True

                TryCatchAssertBlock.ExpectedException("read-only", action165)

                def action166():
                    itu618_13.itu1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action166)

                itu618_13.enable_itu1510 = True
                Assert.assertTrue(itu618_13.enable_itu1510)

                def action167():
                    itu618_13.surface_temperature = 100

                TryCatchAssertBlock.ExpectedException("read only", action167)

                itu618_13.use_annual_itu1510 = False
                Assert.assertFalse(itu618_13.use_annual_itu1510)

                itu618_13.itu1510_month = 1
                Assert.assertEqual(1, itu618_13.itu1510_month)
                itu618_13.itu1510_month = 12
                Assert.assertEqual(12, itu618_13.itu1510_month)

                def action168():
                    itu618_13.itu1510_month = 0

                TryCatchAssertBlock.ExpectedException("must be in", action168)

                def action169():
                    itu618_13.itu1510_month = 13

                TryCatchAssertBlock.ExpectedException("must be in", action169)

                itu618_13.use_annual_itu1510 = True
                Assert.assertTrue(itu618_13.use_annual_itu1510)

                def action170():
                    itu618_13.itu1510_month = 1

                TryCatchAssertBlock.ExpectedException("read-only", action170)

                itu618_13.enable_depolarization_loss = False
                Assert.assertFalse(itu618_13.enable_depolarization_loss)
                itu618_13.enable_depolarization_loss = True
                Assert.assertTrue(itu618_13.enable_depolarization_loss)

            else:
                Assert.fail("Unknown Rain Loss Model name")

        def action171():
            propChan.set_rain_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action171)
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

        def action172():
            propChan.set_clouds_and_fog_fading_loss_model("ITU-R P840-5")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action172)

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

        def action173():
            cfflm7.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action173)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudCeiling = 21; });   // no max

        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm7.cloud_layer_thickness)
        cfflm7.cloud_layer_thickness = 1
        Assert.assertEqual(1, cfflm7.cloud_layer_thickness)

        def action174():
            cfflm7.cloud_layer_thickness = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action174)
        # TryCatchAssertBlock.ExpectedException("is invalid", delegate () { cfflm7.CloudLayerThickness = 21; });   // no max

        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = 100
        Assert.assertEqual(100, cfflm7.cloud_temperature)
        cfflm7.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm7.cloud_temperature)

        def action175():
            cfflm7.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action175)

        def action176():
            cfflm7.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action176)

        def action177():
            cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action177)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm7.cloud_liquid_water_density)
        cfflm7.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm7.cloud_liquid_water_density)

        def action178():
            cfflm7.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action178)

        def action179():
            cfflm7.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action179)

        def action180():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action180)

        def action181():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action181)

        def action182():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action182)

        def action183():
            cfflm7.use_rain_height_as_cloud_layer_thickness = True

        TryCatchAssertBlock.ExpectedException("read-only", action183)

        cfflm7.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm7.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm7.liquid_water_percent_annual_exceeded)
        cfflm7.use_rain_height_as_cloud_layer_thickness = False
        Assert.assertFalse(cfflm7.use_rain_height_as_cloud_layer_thickness)
        cfflm7.use_rain_height_as_cloud_layer_thickness = True
        Assert.assertTrue(cfflm7.use_rain_height_as_cloud_layer_thickness)

        def action184():
            cfflm7.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action184)

        def action185():
            cfflm7.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action185)

        def action186():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action186)

        def action187():
            cfflm7.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action187)

        def action188():
            cfflm7.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action188)

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

        def action189():
            cfflm7.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action189)

        def action190():
            cfflm7.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action190)

        def action191():
            cfflm7.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action191)

        def action192():
            cfflm7.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action192)

        def action193():
            cfflm7.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action193)

        def action194():
            cfflm7.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action194)

    def Test_IAgCloudsAndFogFadingLossModelP840_6(self, cfflm6: "ICloudsAndFogFadingLossModelP840_6"):
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 20
        Assert.assertEqual(20, cfflm6.cloud_ceiling)
        cfflm6.cloud_ceiling = 0
        Assert.assertEqual(0, cfflm6.cloud_ceiling)

        def action195():
            cfflm6.cloud_ceiling = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action195)

        def action196():
            cfflm6.cloud_ceiling = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action196)

        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 20
        Assert.assertEqual(20, cfflm6.cloud_layer_thickness)
        cfflm6.cloud_layer_thickness = 0
        Assert.assertEqual(0, cfflm6.cloud_layer_thickness)

        def action197():
            cfflm6.cloud_layer_thickness = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action197)

        def action198():
            cfflm6.cloud_layer_thickness = 21

        TryCatchAssertBlock.ExpectedException("is invalid", action198)

        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = 100
        Assert.assertEqual(100, cfflm6.cloud_temperature)
        cfflm6.cloud_temperature = -100
        Assert.assertEqual(-100, cfflm6.cloud_temperature)

        def action199():
            cfflm6.cloud_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action199)

        def action200():
            cfflm6.cloud_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action200)

        def action201():
            cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action201)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_DENSITY_VALUE
        # Application.UnitPreferences.SetCurrentUnit("MassUnit", "g");
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 100
        Assert.assertEqual(100, cfflm6.cloud_liquid_water_density)
        cfflm6.cloud_liquid_water_density = 0
        Assert.assertEqual(0, cfflm6.cloud_liquid_water_density)

        def action202():
            cfflm6.cloud_liquid_water_density = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action202)

        def action203():
            cfflm6.cloud_liquid_water_density = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action203)

        def action204():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action204)

        def action205():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action205)

        def action206():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action206)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.WATER_CHOICE_ANNUAL_EXCEEDED
        cfflm6.liquid_water_percent_annual_exceeded = 0.1
        Assert.assertEqual(0.1, cfflm6.liquid_water_percent_annual_exceeded)
        cfflm6.liquid_water_percent_annual_exceeded = 99
        Assert.assertEqual(99, cfflm6.liquid_water_percent_annual_exceeded)

        def action207():
            cfflm6.liquid_water_percent_annual_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action207)

        def action208():
            cfflm6.liquid_water_percent_annual_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action208)

        def action209():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action209)

        def action210():
            cfflm6.liquid_water_percent_monthly_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action210)

        def action211():
            cfflm6.average_data_month = 1

        TryCatchAssertBlock.ExpectedException("read-only", action211)

        cfflm6.liquid_water_density_choice = CLOUDS_AND_FOG_LIQUID_WATER_CHOICES.FOGL_LIQ_WATER_CHOICE_MONTHLY_EXCEEDED
        cfflm6.liquid_water_percent_monthly_exceeded = 1.0
        Assert.assertEqual(1.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.liquid_water_percent_monthly_exceeded = 99.0
        Assert.assertEqual(99.0, cfflm6.liquid_water_percent_monthly_exceeded)
        cfflm6.average_data_month = 1  # helpstring
        Assert.assertEqual(1, cfflm6.average_data_month)
        cfflm6.average_data_month = 12
        Assert.assertEqual(12, cfflm6.average_data_month)

        def action212():
            cfflm6.liquid_water_percent_monthly_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action212)

        def action213():
            cfflm6.liquid_water_percent_monthly_exceeded = 100

        TryCatchAssertBlock.ExpectedException("is invalid", action213)

        def action214():
            cfflm6.average_data_month = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action214)

        def action215():
            cfflm6.average_data_month = 13

        TryCatchAssertBlock.ExpectedException("is invalid", action215)

        def action216():
            cfflm6.cloud_liquid_water_density = 1

        TryCatchAssertBlock.ExpectedException("read only", action216)

        def action217():
            cfflm6.liquid_water_percent_annual_exceeded = 1

        TryCatchAssertBlock.ExpectedException("read only", action217)


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

        def action218():
            propChan.set_atmos_absorption_model("ITU-R P676-9")

        TryCatchAssertBlock.ExpectedException("read-only", action218)

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

        def action219():
            propChan.set_atmos_absorption_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action219)

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
        def action220():
            scriptPlugin.filename = r"C:\bogus.vbs"

        TryCatchAssertBlock.ExpectedException("does not exist", action220)

        def action221():
            scriptPlugin.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

        TryCatchAssertBlock.ExpectedException("Could not initialize", action221)

        scriptPlugin.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
        Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), scriptPlugin.filename)

    def Test_IAgAtmosphericAbsorptionModelSimpleSatcom(self, simpleSatcom: "IAtmosphericAbsorptionModelSimpleSatcom"):
        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        simpleSatcom.water_vapor_concentration = 0
        Assert.assertEqual(0, simpleSatcom.water_vapor_concentration)
        simpleSatcom.water_vapor_concentration = 100
        Assert.assertEqual(100, simpleSatcom.water_vapor_concentration)

        def action222():
            simpleSatcom.water_vapor_concentration = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action222)

        def action223():
            simpleSatcom.water_vapor_concentration = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action223)

        simpleSatcom.surface_temperature = -100
        Assert.assertEqual(-100, simpleSatcom.surface_temperature)
        simpleSatcom.surface_temperature = 100
        Assert.assertEqual(100, simpleSatcom.surface_temperature)

        def action224():
            simpleSatcom.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action224)

        def action225():
            simpleSatcom.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action225)

    def Test_IAgAtmosphericAbsorptionModelTirem(self, tirem: "IAtmosphericAbsorptionModelTirem"):
        tirem.surface_temperature = -100
        Assert.assertEqual(-100, tirem.surface_temperature)
        tirem.surface_temperature = 100
        Assert.assertEqual(100, tirem.surface_temperature)

        def action226():
            tirem.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action226)

        def action227():
            tirem.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action227)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "m")
        tirem.surface_humidity = 0
        Assert.assertEqual(0, tirem.surface_humidity)
        tirem.surface_humidity = 13.25
        Assert.assertEqual(13.25, tirem.surface_humidity)

        def action228():
            tirem.surface_humidity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action228)

        def action229():
            tirem.surface_humidity = 14

        TryCatchAssertBlock.ExpectedException("is invalid", action229)

        tirem.surface_conductivity = 1e-05
        Assert.assertEqual(1e-05, tirem.surface_conductivity)
        tirem.surface_conductivity = 100
        Assert.assertEqual(100, tirem.surface_conductivity)

        def action230():
            tirem.surface_conductivity = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action230)

        def action231():
            tirem.surface_conductivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action231)

        tirem.surface_refractivity = 200
        Assert.assertEqual(200, tirem.surface_refractivity)
        tirem.surface_refractivity = 450
        Assert.assertEqual(450, tirem.surface_refractivity)

        def action232():
            tirem.surface_refractivity = 199

        TryCatchAssertBlock.ExpectedException("is invalid", action232)

        def action233():
            tirem.surface_refractivity = 451

        TryCatchAssertBlock.ExpectedException("is invalid", action233)

        tirem.relative_permittivity = 0
        Assert.assertEqual(0, tirem.relative_permittivity)
        tirem.relative_permittivity = 100
        Assert.assertEqual(100, tirem.relative_permittivity)

        def action234():
            tirem.relative_permittivity = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action234)

        def action235():
            tirem.relative_permittivity = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action235)

        tirem.override_terrain_sample_resolution = False
        Assert.assertFalse(tirem.override_terrain_sample_resolution)

        def action236():
            tirem.terrain_sample_resolution = 1

        TryCatchAssertBlock.ExpectedException("read only", action236)

        tirem.override_terrain_sample_resolution = True
        Assert.assertTrue(tirem.override_terrain_sample_resolution)

        self._root.unit_preferences.set_current_unit("DistanceUnit", "km")
        tirem.terrain_sample_resolution = 0.0001
        Assert.assertEqual(0.0001, tirem.terrain_sample_resolution)
        tirem.terrain_sample_resolution = 10
        Assert.assertEqual(10, tirem.terrain_sample_resolution)

        def action237():
            tirem.terrain_sample_resolution = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action237)

        def action238():
            tirem.terrain_sample_resolution = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action238)


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

        def action239():
            propChan.set_urban_terrestrial_loss_model("Two Ray")

        TryCatchAssertBlock.ExpectedException("read-only", action239)

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

        def action240():
            propChan.set_urban_terrestrial_loss_model("bogus")

        TryCatchAssertBlock.ExpectedException("Invalid model name", action240)
        self._root.unit_preferences.set_current_unit("Temperature", holdUnit)

    def Test_IAgUrbanTerrestrialLossModelTwoRay(self, twoRay: "IUrbanTerrestrialLossModelTwoRay"):
        twoRay.loss_factor = 0.1
        Assert.assertEqual(0.1, twoRay.loss_factor)
        twoRay.loss_factor = 10
        Assert.assertEqual(10, twoRay.loss_factor)

        def action241():
            twoRay.loss_factor = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action241)

        def action242():
            twoRay.loss_factor = 11

        TryCatchAssertBlock.ExpectedException("is invalid", action242)

        twoRay.surface_temperature = -100
        Assert.assertEqual(-100, twoRay.surface_temperature)
        twoRay.surface_temperature = 100
        Assert.assertEqual(100, twoRay.surface_temperature)

        def action243():
            twoRay.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action243)

        def action244():
            twoRay.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action244)

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

            def action245():
                wisRT.surface_temperature = -101

            TryCatchAssertBlock.ExpectedException("is invalid", action245)

            def action246():
                wisRT.surface_temperature = 101

            TryCatchAssertBlock.ExpectedException("is invalid", action246)

            geometryData: "IWirelessInSiteRTGeometryData" = wisRT.geometry_data

            def action247():
                geometryData.filename = TestBase.GetScenarioFile("Bogus.shp")

            TryCatchAssertBlock.ExpectedException("does not exist", action247)
            geometryData.filename = TestBase.GetScenarioFile("Cochise.shp")

            geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84
            Assert.assertEqual(PROJECTION_HORIZONTAL_DATUM_TYPE.LAT_LON_WGS84, geometryData.projection_horizontal_datum)

            def action248():
                geometryData.projection_horizontal_datum = PROJECTION_HORIZONTAL_DATUM_TYPE.UTMWGS84

            TryCatchAssertBlock.ExpectedException("must be in", action248)

            geometryData.building_height_data_attribute = "STATE_NAME"
            Assert.assertEqual("STATE_NAME", geometryData.building_height_data_attribute)

            def action249():
                geometryData.building_height_data_attribute = "Some"

            TryCatchAssertBlock.ExpectedException("must be in", action249)

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

            def action250():
                geometryData.geometry_tile_origin_latitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action250)

            def action251():
                geometryData.geometry_tile_origin_longitude = 0

            TryCatchAssertBlock.ExpectedException("read only", action251)

            geometryData.override_geometry_tile_origin = True
            Assert.assertTrue(geometryData.override_geometry_tile_origin)

            geometryData.geometry_tile_origin_latitude = -90
            Assert.assertEqual(-90, geometryData.geometry_tile_origin_latitude)
            geometryData.geometry_tile_origin_latitude = 90
            Assert.assertEqual(90, geometryData.geometry_tile_origin_latitude)

            def action252():
                geometryData.geometry_tile_origin_latitude = -91

            TryCatchAssertBlock.ExpectedException("is invalid", action252)

            def action253():
                geometryData.geometry_tile_origin_latitude = 91

            TryCatchAssertBlock.ExpectedException("is invalid", action253)

            geometryData.geometry_tile_origin_longitude = -180
            Assert.assertEqual(-180, geometryData.geometry_tile_origin_longitude)
            geometryData.geometry_tile_origin_longitude = 360
            Assert.assertEqual(360, geometryData.geometry_tile_origin_longitude)

            def action254():
                geometryData.geometry_tile_origin_longitude = -181

            TryCatchAssertBlock.ExpectedException("is invalid", action254)

            def action255():
                geometryData.geometry_tile_origin_longitude = 361

            TryCatchAssertBlock.ExpectedException("is invalid", action255)

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

        def action256():
            propChan.set_tropospheric_scintillation_fading_loss_model("ITU-R P618-12")

        TryCatchAssertBlock.ExpectedException("read-only", action256)

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
        def action257():
            tsflm12.compute_deep_fade = True

        TryCatchAssertBlock.ExpectedException("read-only", action257)  # Deprecated and should not be used.

        tsflm12.surface_temperature = -100
        Assert.assertEqual(-100, tsflm12.surface_temperature)
        tsflm12.surface_temperature = 100
        Assert.assertEqual(100, tsflm12.surface_temperature)

        def action258():
            tsflm12.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action258)

        def action259():
            tsflm12.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action259)

        tsflm12.fade_outage = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_outage)
        tsflm12.fade_outage = 40
        Assert.assertEqual(40, tsflm12.fade_outage)

        def action260():
            tsflm12.fade_outage = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action260)

        def action261():
            tsflm12.fade_outage = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action261)

        tsflm12.fade_exceeded = 0.01
        Assert.assertEqual(0.01, tsflm12.fade_exceeded)
        tsflm12.fade_exceeded = 50
        Assert.assertEqual(50, tsflm12.fade_exceeded)

        def action262():
            tsflm12.fade_exceeded = 0

        TryCatchAssertBlock.ExpectedException("is invalid", action262)

        def action263():
            tsflm12.fade_exceeded = 51

        TryCatchAssertBlock.ExpectedException("is invalid", action263)

        tsflm12.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm12.percent_time_refractivity_gradient)
        tsflm12.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm12.percent_time_refractivity_gradient)

        def action264():
            tsflm12.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action264)

        def action265():
            tsflm12.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action265)

        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.WORST_MONTH, tsflm12.average_time_choice)
        tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR
        Assert.assertEqual(TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.YEAR, tsflm12.average_time_choice)

        def action266():
            tsflm12.average_time_choice = TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES.UNKNOWN

        TryCatchAssertBlock.ExpectedException("must be in", action266)

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

        def action267():
            tsflm8.surface_temperature = -101

        TryCatchAssertBlock.ExpectedException("is invalid", action267)

        def action268():
            tsflm8.surface_temperature = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action268)

        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)
        tsflm8.fade_outage = 100
        Assert.assertEqual(100, tsflm8.fade_outage)
        tsflm8.fade_outage = 0
        Assert.assertEqual(0, tsflm8.fade_outage)

        def action269():
            tsflm8.fade_outage = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action269)

        def action270():
            tsflm8.fade_outage = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action270)

        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 100
        Assert.assertEqual(100, tsflm8.percent_time_refractivity_gradient)
        tsflm8.percent_time_refractivity_gradient = 0
        Assert.assertEqual(0, tsflm8.percent_time_refractivity_gradient)

        def action271():
            tsflm8.percent_time_refractivity_gradient = -1

        TryCatchAssertBlock.ExpectedException("is invalid", action271)

        def action272():
            tsflm8.percent_time_refractivity_gradient = 101

        TryCatchAssertBlock.ExpectedException("is invalid", action272)


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

            def action273():
                customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")

            TryCatchAssertBlock.ExpectedException("read-only", action273)

            customModel.enable = True
            Assert.assertTrue(customModel.enable)

            def action274():
                customModel.filename = r"C:\bogus.vbs"

            TryCatchAssertBlock.ExpectedException("does not exist", action274)

            def action275():
                customModel.filename = TestBase.GetScenarioFile("ChainTest", "ChainTest.sc")

            TryCatchAssertBlock.ExpectedException("Could not initialize", action275)
            customModel.filename = TestBase.GetScenarioFile("CommRad", "VB_AbsorpModel.vbs")
            Assert.assertEqual(TestBase.PathCombine("CommRad", "VB_AbsorpModel.vbs"), customModel.filename)


# endregion
# endregion
# endregion
