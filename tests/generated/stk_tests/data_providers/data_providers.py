import pytest
from test_util import *
from app_provider import *
from assertion_harness import *
from logger import *
from math2 import *
from parameterized import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


@category("Excluded From RegFree")
@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        TestBase.Uninitialize()

    # endregion

    # region CompoundUnits
    def test_CompoundUnits(self):
        obj: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        transmitter: "IStkObject" = obj.children.new(STK_OBJECT_TYPE.TRANSMITTER, "Transmitter1")

        # Run the specific data provider that is known to return data using compound units.
        # The columns containing the compound units are "Data Rate" and "Saturated Flux Density".
        # "Data Rate" is a number;
        # "Saturated Flux Density" can be a number or a non-numeric string "N/A".
        # The unit test verifies that
        try:
            dpInfo: "IDataProviderInfo" = transmitter.data_providers["Basic Properties"]
            resInfo: "DataProviderResult" = (clr.CastAs(dpInfo, DataProviderFixed)).exec()

            #
            root: "StkObjectRoot" = None
            if TestBase.ApplicationProvider.Target == TestTarget.eStk:
                root = TestBase.Application
            else:
                root = TestBase.ApplicationProvider.CreateApplication("")

            root.isolate()
            root.unit_preferences.set_current_unit("Bits", "Mb")
            root.unit_preferences.set_current_unit("SmallTime", "sec")

            dataset: "DataProviderResultDataSet"

            for dataset in resInfo.data_sets:
                TestBase.logger.WriteLine5("ElementName: {0}", dataset.element_name)
                TestBase.logger.WriteLine3("Count: {0}", dataset.count)
                TestBase.logger.WriteLine3("ElementType: {0}", dataset.element_type)
                TestBase.logger.WriteLine5("DimensionName: {0}", dataset.dimension_name)

                values = dataset.get_values()
                if String.Compare(dataset.element_name, "Data Rate", True) == 0:
                    dblVal: float = 0
                    value: typing.Any
                    for value in values:
                        (generated1, dblVal) = Double.TryParse(str(value))
                        # Ensure the values returned are numeric
                        Assert.assertTrue(generated1)

                elif String.Compare(dataset.element_name, "Saturated Flux Density", True) == 0:
                    value: typing.Any
                    for value in values:
                        # Ensure the values returned are symbolic
                        Assert.assertTrue((String.Compare(str(value), "N/A", True) == 0))

                #'Iterate through the array of values
                sb = StringBuilder(1024)
                value: typing.Any
                for value in values:
                    sb.AppendFormat("  {0}", value)

                TestBase.logger.WriteLine5("Values: {0}", sb.ToString())

        finally:
            transmitter.unload()

    # endregion

    # region DateUnits_Local
    @parameterized.expand(
        [
            ("LCLG", "1 Jun 2004 07:00:00.000", "2 Jun 2004 07:00:00.000"),
            ("LCLJ", "153/04 07:00:00.000", "154/04 07:00:00.000"),
        ]
    )
    def test_DateUnits_Local(self, dateFormat: str, startTime: typing.Any, stopTime: typing.Any):
        if dateFormat == "LCLG":
            if TimeZoneInfo.Local.IsDaylightSavingTime(DateTime.Now):
                startTime = "1 Jun 2004 08:00:00.000"
                stopTime = "2 Jun 2004 08:00:00.000"

        elif dateFormat == "LCLJ":
            if TimeZoneInfo.Local.IsDaylightSavingTime(DateTime.Now):
                startTime = "153/04 08:00:00.000"
                stopTime = "154/04 08:00:00.000"

        self.DateUnitsInternal(dateFormat, startTime, stopTime)

    # endregion

    # region DateUnits
    @parameterized.expand(
        [
            ("EpDay", 0, 1),
            ("EpHr", 0, 24),
            ("EpMin", 0, 1440),
            ("EpSec", 0, 84600),
            ("EpYr", 0, 0.00273785079),
            ("UTCG", "1 Jun 2004 12:00:00.000", "2 Jun 2004 12:00:00.000"),
            ("TDTG", "1 Jun 2004 12:01:04.184", "2 Jun 2004 12:01:04.184"),
            ("TAIG", "1 Jun 2004 12:00:32.000", "2 Jun 2004 12:00:32.000"),
            ("TDBG", "1 Jun 2004 12:01:04.185", "2 Jun 2004 12:01:04.185"),
            ("UTCJ", "153/04 12:00:00.000", "154/04 12:00:00.000"),
            ("UTCJFOUR", "153/2004 12:00:00.000", "154/2004 12:00:00.000"),
            ("TAIJ", "153/04 12:00:32.000", "154/04 12:00:32.000"),
            ("YYDDD", 4153.5, 4154.5),
            ("YYYYDDD", 2004153.12, 2004154.12),
            ("YYYYMMDD", 20040601.5, 20040602.5),
            ("DD/MM/YYYY", "01/06/2004 12:00:00.000", "02/06/2004 12:00:00.000"),
            ("YYYY/MM/DD", "2004/06/01 12:00:00.000", "2004/06/02 12:00:00.000"),
            ("YYYY:MM:DD", "2004:06:01:12:00:00.000", "2004:06:02:12:00:00.000"),
            ("JDate", 2453158.0, 2453159.0),
            ("JDateOff", 2453158.0, 2453159.0),
            ("ModJDate", 53157.5, 53158.5),
            ("JED", 2453158.00074287, 2453159.00074287),
            ("JDTDB", 2453158.00074287, 2453159.00074287),
            ("GPSG", "1 Jun 2004 12:00:13.000", "2 Jun 2004 12:00:13.000"),
            ("GPS", "1273:216013.000", "1273:302413.000"),
            ("GPSZ", "513417608.667", "513475208.667"),
            ("MisElap", "0/00:00:00.000", "1/00:00:00.000"),
            ("GMT", "153/43200 2004", "154/43200 2004"),
            ("EarthEpTU", 0.0, 107.088),
            ("SunEpTU", 0.0, 0.017),
            ("ISO-YMD", "2004-06-01T12:00:00.000", "2004-06-02T12:00:00.000"),
            ("ISO-YD", "2004-153T12:00:00.000", "2004-154T12:00:00.000"),
        ]
    )
    def test_DateUnits(self, dateFormat: str, startTime: typing.Any, stopTime: typing.Any):
        self.DateUnitsInternal(dateFormat, startTime, stopTime)

    def DateUnitsInternal(self, dateFormat: str, startTime: typing.Any, stopTime: typing.Any):
        dpGroup: "DataProviderGroup" = clr.CastAs(
            TestBase.Application.current_scenario.children["Satellite1"].data_providers["LLA State"], DataProviderGroup
        )
        dp: "IDataProvider" = clr.CastAs(dpGroup.group["Fixed"], IDataProvider)
        dpTimeVar: "DataProviderTimeVarying" = clr.CastAs(dp, DataProviderTimeVarying)
        elems = ["Time", "Lat", "Lon"]

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", dateFormat)
        result: "DataProviderResult" = dpTimeVar.exec_elements(startTime, stopTime, 60, elems)
        arLat = result.data_sets[1].get_values()
        arLon = result.data_sets[2].get_values()

        Assert.assertAlmostEqual(0.0233, float(arLat[0]), delta=0.0001)
        Assert.assertAlmostEqual(1.9321, float(arLat[1]), delta=0.0001)
        Assert.assertAlmostEqual(3.8336, float(arLat[2]), delta=0.0001)
        Assert.assertAlmostEqual(5.7206, float(arLat[3]), delta=0.0001)
        Assert.assertAlmostEqual(7.586, float(arLat[4]), delta=0.0001)
        Assert.assertAlmostEqual(9.4222, float(arLat[5]), delta=0.0001)
        Assert.assertAlmostEqual(11.2218, float(arLat[6]), delta=0.0001)
        Assert.assertAlmostEqual(12.9773, float(arLat[7]), delta=0.0001)
        Assert.assertAlmostEqual(14.6807, float(arLat[8]), delta=0.0001)
        Assert.assertAlmostEqual(16.3243, float(arLat[9]), delta=0.0001)

        Assert.assertAlmostEqual(-70.2513, float(arLon[0]), delta=0.0001)
        Assert.assertAlmostEqual(-67.0056, float(arLon[1]), delta=0.0001)
        Assert.assertAlmostEqual(-63.7522, float(arLon[2]), delta=0.0001)
        Assert.assertAlmostEqual(-60.4834, float(arLon[3]), delta=0.0001)
        Assert.assertAlmostEqual(-57.1918, float(arLon[4]), delta=0.0001)
        Assert.assertAlmostEqual(-53.8699, float(arLon[5]), delta=0.0001)
        Assert.assertAlmostEqual(-50.5107, float(arLon[6]), delta=0.0001)
        Assert.assertAlmostEqual(-47.1074, float(arLon[7]), delta=0.0001)
        Assert.assertAlmostEqual(-43.6535, float(arLon[8]), delta=0.0001)
        Assert.assertAlmostEqual(-40.1432, float(arLon[9]), delta=0.0001)

    # endregion

    # region RowsVSColumns
    def test_TestRowsAgainstColumns(self):
        obj: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        dpName: str = "Sunlight"
        dpPath: str = "Lighting Times//" + dpName
        info: "IDataProviderInfo" = obj.data_providers.get_data_provider_info_from_path(dpPath)
        Assert.assertEqual(dpName, info.name)
        Assert.assertEqual(DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_INTVL, info.type)
        intvl: "DataProviderInterval" = obj.data_providers.get_data_provider_interval_from_path(dpPath)
        result: "DataProviderResult" = intvl.exec("1 Jun 2004 12:00:00.000", "1 Jun 2004 12:00:20.000")
        ElementNames = result.data_sets.element_names
        Assert.assertEqual(result.data_sets.count, Array.Length(ElementNames))

        with pytest.raises(Exception):
            array = result.data_sets.get_row(-1)
        with pytest.raises(Exception):
            array = result.data_sets.get_row(result.data_sets.row_count)

        i: int = 0
        while i < result.data_sets.count:
            set: "DataProviderResultDataSet" = result.data_sets[i]
            # logger.WriteLine(set.ElementName);
            Assert.assertEqual(set.count, result.data_sets.row_count)
            Assert.assertEqual(set.element_name, clr.Convert(ElementNames[i], str))
            setValues = set.get_values()

            j: int = 0
            while j < Array.Length(setValues):
                Assert.assertEqual(setValues[j], result.data_sets.get_row(j)[i])

                j += 1

            i += 1

        rows = result.data_sets.to_array()

        i: int = 0
        while i < len(rows):
            j: int = 0
            while j < len(rows[0]):
                values = result.data_sets[j].get_values()
                Assert.assertEqual(values[i], rows[i][j])

                j += 1

            i += 1

    # endregion

    # region CoarseGrainedDataProviders
    def test_CoarseGrainedDPs(self):
        obj: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]

        elems = ["Time", "Azimuth"]

        times = ["1 Jun 2004 12:00:00.000", "1 Jun 2004 12:00:20.000", "1 Jun 2004 12:00:40.000"]

        timeVar: "DataProviderTimeVarying" = clr.CastAs(obj.data_providers["Lighting AER"], DataProviderTimeVarying)
        result: "DataProviderResult" = timeVar.exec_single_elements("1 Jun 2004 12:00:00.000", elems)
        dpName: str = "Lighting AER"
        dpPath: str = dpName
        info: "IDataProviderInfo" = obj.data_providers.get_data_provider_info_from_path(dpPath)
        Assert.assertEqual(dpName, info.name)
        Assert.assertEqual(DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_TIME_VARYING, info.type)
        timevar: "DataProviderTimeVarying" = obj.data_providers.get_data_provider_time_varying_from_path(dpPath)
        timearray: "DataProviderResultTimeArrayElements" = timevar.exec_single_elements_array(times, elems)
        Assert.assertEqual(timearray.count, Array.Length(elems))  # elements

        Assert.assertEqual(Array.Length(timearray.get_array(0)), Array.Length(times))  # times

        Assert.assertEqual(timearray.get_array(0)[0], timearray.get_array("Time")[0])  # time
        Assert.assertEqual(result.data_sets[0].get_values()[0], timearray.get_array(0)[0])  # time

        Assert.assertEqual(timearray.get_array(1)[0], timearray.get_array("Azimuth")[0])  # azimuth
        Assert.assertEqual(result.data_sets[1].get_values()[0], timearray.get_array(1)[0])  # azimuth

        with pytest.raises(Exception):
            timearray.get_array(timearray.count)
        with pytest.raises(Exception):
            timearray.get_array("Bogus")

        result = timeVar.exec_single_elements("1 Jun 2004 12:00:00.000", elems)

        # System.logger.WriteLine(timearray.Count);
        # System.logger.WriteLine(timearray.GetArray(1).Length);

        # System.logger.WriteLine("Time2: "+timearray.GetArray(0).GetValue(1));
        # System.logger.WriteLine("Time2: "+timearray.GetArray("Time").GetValue(1));
        Assert.assertEqual(timearray.get_array(0)[1], timearray.get_array("Time")[1])  # time
        Assert.assertEqual(result.data_sets[0].get_values()[0], timearray.get_array(0)[0])  # time

        # System.logger.WriteLine("SunAzimuth Angle2: " + timearray.GetArray(1).GetValue(1));
        # System.logger.WriteLine("SunAzimuth Angle2: " + timearray.GetArray("SunAzimuth Angle").GetValue(1));
        Assert.assertEqual(timearray.get_array(1)[1], timearray.get_array("Azimuth")[1])  # sun azimuth
        Assert.assertEqual(result.data_sets[1].get_values()[0], timearray.get_array(1)[0])  # sun azimuth

        # System.logger.WriteLine("SunAzimuth Angle1: " + result.DataSets.GetDataSetByName("SunAzimuth Angle").GetValues().GetValue(0));
        # System.logger.WriteLine("SunAzimuth Angle1: " + result.DataSets[1].GetValues().GetValue(0));
        # System.logger.WriteLine("SunAzimuth Angle1: " + timearray.GetArray(1).GetValue(0));

        Assert.assertEqual(
            result.data_sets.get_data_set_by_name("Azimuth").get_values()[0], result.data_sets[1].get_values()[0]
        )
        Assert.assertEqual(result.data_sets.get_data_set_by_name("Azimuth").get_values()[0], timearray.get_array(1)[0])
        Assert.assertEqual(result.data_sets[1].get_values()[0], timearray.get_array(1)[0])

        elems = ["Normal x", "Azimuth"]

        dpName = "LocalHorizontal"
        dpPath = "Terrain Info//" + dpName
        info = obj.data_providers.get_data_provider_info_from_path(dpPath)
        Assert.assertEqual(dpName, info.name)
        Assert.assertEqual(DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_FIXED, info.type)
        dpfixed: "DataProviderFixed" = obj.data_providers.get_data_provider_fixed_from_path(dpPath)
        result = dpfixed.exec_elements(elems)
        group: "DataProviderGroup" = clr.CastAs(obj.data_providers["Terrain Info"], DataProviderGroup)
        fixedDp: "DataProviderFixed" = clr.CastAs(group.group["LocalHorizontal"], DataProviderFixed)
        result2: "DataProviderResult" = fixedDp.exec_elements(elems)
        Assert.assertEqual(result2.data_sets[0].get_values()[0], result.data_sets[0].get_values()[0])
        Assert.assertEqual(result2.data_sets[1].get_values()[0], result.data_sets[1].get_values()[0])

        dpName = "Sunlight"
        dpPath = "Lighting Times//" + dpName
        info = obj.data_providers.get_data_provider_info_from_path(dpPath)
        Assert.assertEqual(dpName, info.name)
        Assert.assertEqual(DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_INTVL, info.type)
        intvl: "DataProviderInterval" = obj.data_providers.get_data_provider_interval_from_path(dpPath)
        result = intvl.exec("1 Jun 2004 12:00:00.000", "1 Jun 2004 12:00:20.000")

        group = clr.CastAs(obj.data_providers["Lighting Times"], DataProviderGroup)
        intv: "DataProviderInterval" = clr.CastAs(group.group["Sunlight"], DataProviderInterval)
        result2 = intv.exec("1 Jun 2004 12:00:00.000", "1 Jun 2004 12:00:20.000")
        Assert.assertEqual(result2.data_sets[0].get_values()[0], result.data_sets[0].get_values()[0])
        Assert.assertEqual(result2.data_sets[1].get_values()[0], result.data_sets[1].get_values()[0])
        Assert.assertEqual(result2.data_sets[2].get_values()[0], result.data_sets[2].get_values()[0])
        Assert.assertEqual(result2.data_sets[3].get_values()[0], result.data_sets[3].get_values()[0])

        elems = ["Start Time", "Duration"]

        dpName = "Sunlight"
        dpPath = "Lighting Times//" + dpName
        info = obj.data_providers.get_data_provider_info_from_path(dpPath)
        Assert.assertEqual(dpName, info.name)
        Assert.assertEqual(DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_INTVL, info.type)
        intvl = obj.data_providers.get_data_provider_interval_from_path(dpPath)
        result = intvl.exec_elements("1 Jun 2004 12:00:00.000", "1 Jun 2004 12:00:20.000", elems)

        group = clr.CastAs(obj.data_providers["Lighting Times"], DataProviderGroup)
        intv = clr.CastAs(group.group["Sunlight"], DataProviderInterval)
        result2 = intv.exec_elements("1 Jun 2004 12:00:00.000", "1 Jun 2004 12:00:20.000", elems)
        Assert.assertEqual(result2.data_sets[0].get_values()[0], result.data_sets[0].get_values()[0])
        Assert.assertEqual(result2.data_sets[1].get_values()[0], result.data_sets[1].get_values()[0])

        # ==============
        # Test failures
        # ==============

        # ------------------
        # Incorrect paths
        # ------------------
        with pytest.raises(Exception):
            info1: "IDataProviderInfo" = obj.data_providers.get_data_provider_info_from_path(
                "I'm is not a Data Provider"
            )
        with pytest.raises(Exception):
            fixed1: "DataProviderFixed" = obj.data_providers.get_data_provider_fixed_from_path("I'm not either")
        with pytest.raises(Exception):
            intv1: "DataProviderInterval" = obj.data_providers.get_data_provider_interval_from_path(
                "Me neither//I think"
            )
        with pytest.raises(Exception):
            timevar1: "DataProviderTimeVarying" = obj.data_providers.get_data_provider_time_varying_from_path(
                "That makes 4 of us"
            )

        # -----------------
        # Incorrect types
        # -----------------
        with pytest.raises(Exception):
            fixed1: "DataProviderFixed" = obj.data_providers.get_data_provider_fixed_from_path(
                "Lighting Times//Sunlight"
            )
        with pytest.raises(Exception):
            intv1: "DataProviderInterval" = obj.data_providers.get_data_provider_interval_from_path(
                "Terrain Info//LocalHorizontal"
            )
        with pytest.raises(Exception):
            timevar1: "DataProviderTimeVarying" = obj.data_providers.get_data_provider_time_varying_from_path(
                "Lighting Times//Sunlight"
            )

    # endregion

    # region SatelliteCartPosFixed
    def test_SatelliteCartPosFixed(self):
        # Runs Cartesian Position//Fixed Data Provider for a satellite using DataProviderTimeVarying.Exec
        TestBase.logger.WriteLine(
            "----- Cartesian Position//Fixed Data Provider for a satellite TEST ----- BEGIN -----"
        )
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oSatellite: "IStkObject" = oScenario.children["Satellite1"]
        Assert.assertEqual(oScenario.children["Satellite1"], oSatellite)

        oGroup: "DataProviderGroup" = clr.Convert(oSatellite.data_providers["Cartesian Position"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        oProvider.allow_user_interface = False
        Assert.assertFalse(oProvider.allow_user_interface)
        oProvider.pre_data = ""
        Assert.assertEqual("", oProvider.pre_data)
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0
        )
        Assert.assertIsNotNone(oResult)

        # Verifying random datasets and their values
        # logger.WriteLine("\tSections count: {0}", oResult.Sections.Count);
        Assert.assertEqual(0, oResult.sections.count)
        # logger.WriteLine("\tIntervals count: {0}", oResult.Intervals.Count);
        Assert.assertEqual(1, oResult.intervals.count)

        iIndex: int = 0
        while iIndex < oResult.intervals.count:
            start: typing.Any = oResult.intervals[iIndex].start_time
            stop: typing.Any = oResult.intervals[iIndex].stop_time

            iIndex += 1

        # logger.WriteLine("\tDataSets count: {0}", oResult.DataSets.Count);
        Assert.assertEqual(4, oResult.data_sets.count)

        iIndex: int = 0
        while iIndex < oResult.data_sets.count:
            elem: typing.Any = oResult.data_sets[iIndex].element_name
            elemtype: typing.Any = oResult.data_sets[iIndex].element_type

            iIndex += 1

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[0] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(16, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        Assert.assertEqual("1 Jun 2004 12:04:00.000000000", clr.Convert(arValues[1], str))
        Assert.assertEqual("1 Jun 2004 12:16:00.000000000", clr.Convert(arValues[4], str))

        iIndex: int = 0
        while iIndex < Array.Length(arValues):
            stuff: typing.Any = arValues[iIndex]

            iIndex += 1

        oDataSet = oResult.intervals[0].data_sets[2]
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[2] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(16, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("y", oDataSet.element_name)
        Assert.assertEqual(-6285.353143, Math.Round(float(arValues[0]), 6))
        Assert.assertEqual(5609.665723, Math.Round(float(arValues[13]), 6))

        iIndex: int = 0
        while iIndex < Array.Length(arValues):
            stuff: typing.Any = arValues[iIndex]

            iIndex += 1

        del oResult
        TestBase.logger.WriteLine("----- Cartesian Position//Fixed Data Provider for a satellite TEST ----- END -----")

    # endregion

    # region SatelliteCartPosFixedUsingDefault
    def test_SatelliteCartPosFixedUsingDefault(self):
        # Runs Cartesian Position//Fixed Data Provider for a satellite using DataProviderTimeVarying.Exec
        TestBase.logger.WriteLine(
            "----- Cartesian Position//Fixed Data Provider for a satellite TEST ----- BEGIN -----"
        )
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oSatellite: "IStkObject" = oScenario.children["Satellite1"]
        Assert.assertEqual(oScenario.children["Satellite1"], oSatellite)

        oGroup: "DataProviderGroup" = clr.Convert(oSatellite.data_providers["Cartesian Position"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        oProvider.allow_user_interface = False
        Assert.assertFalse(oProvider.allow_user_interface)
        oProvider.pre_data = ""
        Assert.assertEqual("", oProvider.pre_data)
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_native_times(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00"
        )
        Assert.assertIsNotNone(oResult)

        # Verifying random datasets and their values
        # logger.WriteLine("\tSections count: {0}", oResult.Sections.Count);
        Assert.assertEqual(0, oResult.sections.count)
        # logger.WriteLine("\tIntervals count: {0}", oResult.Intervals.Count);
        Assert.assertEqual(1, oResult.intervals.count)

        iIndex: int = 0
        while iIndex < oResult.intervals.count:
            start: typing.Any = oResult.intervals[iIndex].start_time
            stop: typing.Any = oResult.intervals[iIndex].stop_time

            iIndex += 1

        # logger.WriteLine("\tDataSets count: {0}", oResult.DataSets.Count);
        Assert.assertEqual(4, oResult.data_sets.count)

        iIndex: int = 0
        while iIndex < oResult.data_sets.count:
            elem: typing.Any = oResult.data_sets[iIndex].element_name
            elemtype: typing.Any = oResult.data_sets[iIndex].element_type

            iIndex += 1

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[0] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(61, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        Assert.assertEqual("1 Jun 2004 12:01:00.000000000", clr.Convert(arValues[1], str))
        Assert.assertEqual("1 Jun 2004 12:04:00.000000000", clr.Convert(arValues[4], str))

        iIndex: int = 0
        while iIndex < Array.Length(arValues):
            stuff: typing.Any = arValues[iIndex]

            iIndex += 1

        oDataSet = oResult.intervals[0].data_sets[2]
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[2] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(61, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("y", oDataSet.element_name)
        Assert.assertEqual(-6285.353143, Math.Round(float(arValues[0]), 6))
        Assert.assertEqual(-2660.314094, Math.Round(float(arValues[13]), 6))

        iIndex: int = 0
        while iIndex < Array.Length(arValues):
            stuff: typing.Any = arValues[iIndex]

            iIndex += 1

        del oResult
        TestBase.logger.WriteLine("----- Cartesian Position//Fixed Data Provider for a satellite TEST ----- END -----")

    # endregion

    # region AircraftCartPosFixedUsingDefault
    def test_AircraftCartPosFixedUsingDefault(self):
        # Runs Cartesian Position//Fixed Data Provider for a satellite using DataProviderTimeVarying.Exec
        TestBase.logger.WriteLine("----- Cartesian Position//Fixed Data Provider for a aircraft TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oAir: "IStkObject" = oScenario.children["a340"]
        Assert.assertEqual(oScenario.children["a340"], oAir)

        oGroup: "DataProviderGroup" = clr.Convert(oAir.data_providers["Cartesian Position"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        oProvider.allow_user_interface = False
        Assert.assertFalse(oProvider.allow_user_interface)
        oProvider.pre_data = ""
        Assert.assertEqual("", oProvider.pre_data)
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_native_times(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00"
        )
        Assert.assertIsNotNone(oResult)

        # Verifying random datasets and their values
        # logger.WriteLine("\tSections count: {0}", oResult.Sections.Count);
        Assert.assertEqual(0, oResult.sections.count)
        # logger.WriteLine("\tIntervals count: {0}", oResult.Intervals.Count);
        Assert.assertEqual(1, oResult.intervals.count)

        iIndex: int = 0
        while iIndex < oResult.intervals.count:
            start: typing.Any = oResult.intervals[iIndex].start_time
            stop: typing.Any = oResult.intervals[iIndex].stop_time

            iIndex += 1

        # logger.WriteLine("\tDataSets count: {0}", oResult.DataSets.Count);
        Assert.assertEqual(4, oResult.data_sets.count)

        iIndex: int = 0
        while iIndex < oResult.data_sets.count:
            elem: typing.Any = oResult.data_sets[iIndex].element_name
            elemtype: typing.Any = oResult.data_sets[iIndex].element_type

            iIndex += 1

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[0] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(199, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", clr.Convert(arValues[0], str))
        Assert.assertEqual("1 Jun 2004 12:00:19.531224281", clr.Convert(arValues[1], str))
        Assert.assertEqual("1 Jun 2004 12:00:35.335125888", clr.Convert(arValues[2], str))
        Assert.assertEqual("1 Jun 2004 12:00:52.900970419", clr.Convert(arValues[3], str))
        Assert.assertEqual("1 Jun 2004 12:00:56.812066962", clr.Convert(arValues[4], str))
        Assert.assertEqual("1 Jun 2004 12:01:30.188313568", clr.Convert(arValues[8], str))
        Assert.assertEqual("1 Jun 2004 12:01:35.887349506", clr.Convert(arValues[9], str))
        Assert.assertEqual("1 Jun 2004 12:05:01.726211163", clr.Convert(arValues[19], str))

        iIndex: int = 0
        while iIndex < Array.Length(arValues):
            stuff: typing.Any = arValues[iIndex]

            iIndex += 1

        oDataSet = oResult.intervals[0].data_sets[2]
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[2] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(199, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("y", oDataSet.element_name)
        Assert.assertEqual(24.44683, Math.Round(float(arValues[0]), 6))
        Assert.assertEqual(40.338076, Math.Round(float(arValues[13]), 6))

        iIndex: int = 0
        while iIndex < Array.Length(arValues):
            stuff: typing.Any = arValues[iIndex]

            iIndex += 1

        del oResult
        TestBase.logger.WriteLine("----- Cartesian Position//Fixed Data Provider for a aircraft TEST ----- END -----")

    # endregion

    # region TestDataProviderInterface
    def test_TestDataProviderInterface(self):
        TestBase.logger.WriteLine("----- DATA PROVIDER INTERFACE TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.reset_units()
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oSatellite: "IStkObject" = oScenario.children["Satellite1"]
        Assert.assertEqual(oScenario.children["Satellite1"], oSatellite)

        oGroup: "DataProviderGroup" = clr.Convert(oSatellite.data_providers["Cartesian Position"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        oProvider.allow_user_interface = True
        Assert.assertTrue(oProvider.allow_user_interface)

        oProvider.pre_data = "This is a test"
        Assert.assertEqual("This is a test", oProvider.pre_data)

        oElements: "DataProviderElements" = oProvider.elements
        Assert.assertIsNotNone(oElements)

        x: "DataProviderElement" = oElements[0]
        name: str = x.name
        y: "DataProviderElement" = oElements.get_item_by_index(0)
        z: "DataProviderElement" = oElements.get_item_by_name(name)
        Assert.assertEqual(x.name, y.name)
        Assert.assertEqual(x.name, z.name)

        # logger.WriteLine("\tThe DataProvider contains: {0} elements.", oElements.Count);
        dataPrvElement: "DataProviderElement"

        # logger.WriteLine("\tThe DataProvider contains: {0} elements.", oElements.Count);
        for dataPrvElement in oElements:
            # logger.WriteLine("\t\tElement: Name = {0}, Type = {1}, DimensionName = {2}",
            # 	dataPrvElement.Name, dataPrvElement.Type, dataPrvElement.DimensionName );
            Assert.assertIsNotNone(dataPrvElement.name)
            Assert.assertIsNotNone(dataPrvElement.type)
            Assert.assertIsNotNone(dataPrvElement.dimension_name)

        TestBase.logger.WriteLine("----- DATA PROVIDER INTERFACE TEST ----- END -----")

    # endregion

    # region TestDataSetNames
    def test_TestDataSetNames(self):
        # Running Cartesian Position for a facility using DataProviderFixed.ExecElements
        TestBase.logger.WriteLine("----- TestDataSetNames ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", "mi")

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oFacility: "IStkObject" = oScenario.children["Facility1"]
        Assert.assertEqual(oScenario.children["Facility1"], oFacility)

        oProvider: "IDataProvider" = clr.Convert(oFacility.data_providers["Cartesian Position"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        # Verifying random datasets and their values
        arCols = ["x", "z"]
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderFixed)).exec_elements(arCols)
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(2, oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets.get_data_set_by_name("x")
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(1, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("x", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(7689.837955, Math.Round(float(arValues[0]), 6))

        oDataSet = oResult.intervals[0].data_sets.get_data_set_by_name("z")
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(1, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("z", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(26529.061236, Math.Round(float(arValues[0]), 6))

        with pytest.raises(Exception):
            oResult.intervals[0].data_sets.get_data_set_by_name("g")
        del oResult
        TestBase.logger.WriteLine("----- TestDataSetNames ----- END -----")

    # endregion

    # region FacilityLightingAER
    def test_FacilityLightingAER(self):
        # Runs Angles//SunAzimuth Data Provider for a facility using DataProviderTimeVarying.Exec
        TestBase.logger.WriteLine("----- FacilityLightingAER ----- BEGIN -----")
        TestBase.Application.unit_preferences.reset_units()
        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")
        Assert.assertEqual("deg", TestBase.Application.unit_preferences.get_current_unit_abbrv("AngleUnit"))
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "min")
        Assert.assertEqual("min", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oFacility: "IStkObject" = oScenario.children["Facility1"]
        Assert.assertEqual(oScenario.children["Facility1"], oFacility)

        oAngles: "IDataProvider" = clr.Convert(oFacility.data_providers["Lighting AER"], IDataProvider)
        Assert.assertIsNotNone(oAngles)

        oResult: "DataProviderResult" = (clr.Convert(oAngles, DataProviderTimeVarying)).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 4
        )
        Assert.assertIsNotNone(oResult)

        # Verifying random datasets and their values
        # logger.WriteLine("\tSections count: {0}", oResult.Sections.Count);
        Assert.assertEqual(0, oResult.sections.count)
        # logger.WriteLine("\tIntervals count: {0}", oResult.Intervals.Count);
        Assert.assertEqual(1, oResult.intervals.count)

        iIndex: int = 0
        while iIndex < oResult.intervals.count:
            pass

            iIndex += 1

        # logger.WriteLine("\tDataSets count: {0}", oResult.DataSets.Count);
        Assert.assertEqual(4, oResult.data_sets.count)

        iIndex: int = 0
        while iIndex < oResult.data_sets.count:
            pass

            iIndex += 1

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[0] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(16, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        Assert.assertEqual("1 Jun 2004 12:04:00.000000000", clr.Convert(arValues[1], str))
        Assert.assertEqual("1 Jun 2004 12:16:00.000000000", clr.Convert(arValues[4], str))

        iIndex: int = 0
        while iIndex < Array.Length(arValues):
            pass

            iIndex += 1

        oDataSet = oResult.intervals[0].data_sets[2]
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[2] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(16, oDataSet.count)
        Assert.assertEqual("Angle", oDataSet.dimension_name)
        Assert.assertEqual("Elevation", oDataSet.element_name)
        Assert.assertAlmostEqual(23.702, float(arValues[0]), delta=0.001)
        Assert.assertAlmostEqual(24.479, float(arValues[1]), delta=0.001)

        iIndex: int = 0
        while iIndex < Array.Length(arValues):
            pass

            iIndex += 1

        del oResult
        TestBase.logger.WriteLine("----- FacilityLightingAER ----- END -----")

    # endregion

    # region DPNames
    @category("SEET")
    @category("VO Tests")
    def test_DPNames(self):
        o: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children[0].children["Satellite1"]
        # string sInstanceName = o.InstanceName;
        sAllNames: str = ""
        count: int = o.data_providers.count

        i: int = 1
        while i < o.data_providers.count:
            sName: str = o.data_providers[i].name
            # bool b1 = o.DataProviders[i].IsGroup();
            # Console.WriteLine(sName);
            sAllNames += sName

            i += 1

        # Console.WriteLine(sAllNames);
        Assert.assertEqual(
            "All ConstraintsAnglesArticulationAstrogator Accel HistAstrogator LogAstrogator MCS Ephemeris SegmentsAstrogator Maneuver Ephemeris Block FinalAstrogator Maneuver Ephemeris Block HistoryAstrogator Maneuver Ephemeris Block InitialAstrogator Pass DataAstrogator Script SummaryAstrogator Targeter DataAstrogator ValuesAttitude QuaternionsAttitude Segment DescriptionAttitude Segment ECF QuaternionsAttitude Segment Euler AnglesAttitude Segment QuaternionsAttitude Segment ScheduleAttitude Segment YPRAttitude YPRAvailable TimesAxes Choose AxesBeta AngleBody Axes OrientationBody Axes Orientation:YPR 123Body Axes Orientation:YPR 132Body Axes Orientation:YPR 213Body Axes Orientation:YPR 231Body Axes Orientation:YPR 312Body Axes Orientation:YPR 321Brouwer-Lyd Mean LongBrouwer-Lyd Mean ShortCartesian AccelerationCartesian PositionCartesian VelocityClassical ElementsClose Approach Compute ResultsClose Approach DefinitionClose Approach Filter SettingsCloseApproachCloseApproachByMinRangeCloseApproachBySSCCollection of Interval ListsConditionCondition SetCrdn Available TimesData Provider DetailData Provider SummaryDeckAccessDeckAccess DataDelaunay ElementsECF Attitude QuaternionsEclipse DefinitionEclipse Solar IntensityEclipse SummaryEclipse TimesEcliptic CrossingsElement SetEphemeris DiffEphemeris Diff in Curvilinear CoordinatesEquinoctial ElementsEuler AnglesGeo Station Keeping ElementsGravity ModelGround Ellipse DefinitionHeadingIIRV User InputIntervalInterval ListKozai-Izsak MeanLLA StateLLR StateLOP Mean ElementsLaunch Window DefinitionLifetimeLighting AERLighting TimesLunar Eclipse Solar IntensityMCS SummaryManeuver SummaryMassMixed Spherical ElementsModel AreaModel LOD 0 ArticulationsModel LOD 1 ArticulationsModified Equinoctial ElementsMoon AERMoon VectorParameter Set: AttitudeParameter Set: Cartographic TrajectoryParameter Set: OrbitParameter Set: TrajectoryParameter Set: VectorPass Event TimesPassesPlanes Choose SystemPlanes(Fixed)Planes(ICRF)Planes(Inertial)Planes(J2000)Pointing Covariance (Projection)Points Choose PlanePoints Choose SystemPoints(Fixed)Points(ICRF)Points(Inertial)Points(J2000)Pos Vel Projected CovariancePos Vel Rotated CovariancePosition CovariancePosition Covariance Choose AxesPosition Covariance CrossSectionPosition Covariance CrossSection Choose PlanePosition Covariance ProjectionPosition Covariance Projection Choose PlanePosition Covariance in AxesPrecision PassesPropagator InputsRIC CoordinatesRelative MotionSEET Debris FluxSEET GCR Differential Fluence by EnergySEET GCR Differential Flux by EnergySEET GCR Integral Fluence by EnergySEET GCR Integral Flux by EnergySEET GCR ModelSEET Magnetic ConjugacySEET Magnetic CoordinatesSEET Magnetic FieldSEET Magnetic Field ModelSEET Meteor FluxSEET Particle Distribution FluenceSEET Particle FluenceSEET Particle Flux ModelSEET Radiation Accumulated DoseSEET Radiation Accumulated Dose By ThicknessSEET Radiation Average Dose RateSEET Radiation Average Dose Rate By ThicknessSEET Radiation Dose DepthSEET Radiation Dose RateSEET Radiation Dose Rate By ThicknessSEET Radiation FluxSEET Radiation Flux by EnergySEET Radiation Integral FluxSEET Radiation Integral Flux by EnergySEET Radiation ModelSEET SAA Contour SettingsSEET SAA Crossing TimesSEET SAA Flux IntensitySEET SEP Energy by FluenceSEET SEP Fluence by Probability per EnergySEET SEP ModelSEET Vehicle TemperatureSEET Vehicle Temperature ModelSTM EigendecompositionScalar CalculationsSegment SummaryShadow LLASolar Apparent TimeSolar IntensitySolar Panel AnglesSolar Panel AreaSolar Panel Area No SumSolar Panel PowerSolar Panel Power No SumSolar Specular PointSpherical ElementsState Transition MatrixSun VectorSwath PointsTLE Residual DataTLE Set DataTLE Summary DataTime ArrayTime InstantTrue Anomaly StepUser Supplied DataVector Choose AxesVector Choose PlaneVectors(Body)Vectors(Fixed)Vectors(Fixed_VVLH)Vectors(ICRF)Vectors(Inertial)Vectors(J2000)Vectors(LVLH)Vectors(VNC)Vectors(VVLH(CBF))Vectors(VVLH)Velocity Projected Covariance",
            sAllNames,
        )

    # endregion

    def DPSchemaEntriesChecker(self, schema: str, someSchemaEntries: "List[str]"):
        searchEntry: str
        for searchEntry in someSchemaEntries:
            TestBase.logger.WriteLine(("Searching for: " + searchEntry))
            Assert.assertTrue((searchEntry in schema))
            searchIndex: int = schema.find(searchEntry)

    # region DPSchemaAdvCat
    def test_DPSchemaAdvCat(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        acObj: "IStkObject" = scenChildren["AdvCAT1"]

        schema: str = None
        schema = acObj.data_providers.get_schema()
        # logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="AdvCAT">',
            '<DataPrv Name="DpDetailData" Desc="Data Provider Detail" PropBitMask="17">',
            '<Element Name="Info" Type="2" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="ACatEncounterRpt" Desc="Encounter Warnings" PropBitMask="529">',
            '<Element Name="Report" Type="2" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="ACatErrorData" Desc="Errors" PropBitMask="529">',
            '<Element Name="Name" Type="2" Dim=""/>',
            '<Element Name="SSC" Type="2" Dim=""/>',
            '<Element Name="Error" Type="2" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="ACatEventEphem" Desc="Event Ephemeris" PropBitMask="530">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="Secondary StringID" Type="2" Dim=""/>',
            '<Element Name="Range wrt Primary - Tangential" Type="0" Dim="DistanceUnit"/>',
            "</DataPrv>",
            '<DataPrv Name="ACatCARpt" Desc="Events Unsorted" PropBitMask="532">',
            '<Element Name="Object Name" Type="2" Dim=""/>',
            '<Element Name="TCA Uncertainty" Type="0" Dim="TimeUnit"/>',
            '<Element Name="Sec: Lat (TCA)" Type="0" Dim="LatitudeUnit"/>',
            "</DataPrv>",
            '<DataPrv Name="ACatCARptByDuration" Desc="Events by Duration" PropBitMask="532">',
            '<Element Name="Object Name" Type="2" Dim=""/>',
            '<Element Name="Prim: Lat (TMS)" Type="0" Dim="LatitudeUnit"/>',
            '<Element Name="Sec: Long (TCA)" Type="0" Dim="LongitudeUnit"/>',
            "</DataPrv>",
            '<DataPrv Name="ACatCARptByMinRange" Desc="Events by Min Range" PropBitMask="532">',
            '<Element Name="Min Range - Tangential" Type="0" Dim="DistanceUnit"/>',
            '<Element Name="Collision Probability (Analytic)" Type="0" Dim=""/>',
            '<Element Name="Prim: Speed (TMS)" Type="0" Dim="Rate"/>',
            "</DataPrv>",
            '<DataPrv Name="ACatCARptByMinSep" Desc="Events by Min Sep" PropBitMask="532">',
            '<Element Name="StringID" Type="2" Dim=""/>',
            '<Element Name="Range Uncertainty (TCA)" Type="0" Dim="DistanceUnit"/>',
            '<Element Name="Probability Linearity Speed (Coarse)" Type="0" Dim="Rate"/>',
            "</DataPrv>",
            '<DataPrv Name="ACatCARptBySSC" Desc="Events by SSC" PropBitMask="532">',
            '<Element Name="ConjTCA" Type="0" Dim="DateFormat"/>',
            "</DataPrv>",
            '<DataPrv Name="ACatCARptByTimeIn" Desc="Events by Time In" PropBitMask="532">',
            '<DataPrv Name="ACatFilterSettings" Desc="Filter Settings" PropBitMask="529">',
            '<DataPrv Name="ACatGenInfo" Desc="General Info" PropBitMask="529">',
            '<DataPrv Name="ACatPrimNameRpt" Desc="Primary Data" PropBitMask="529">',
            '<DataPrv Name="ACatPrimaryEphem" Desc="Primary Ephemeris" PropBitMask="530">',
            '<Element Name="NumberID" Type="2" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="ACatPrimListRpt" Desc="Primary Vehicles" PropBitMask="529">',
            '<Element Name="Events" Type="1" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="ACatSecNameRpt" Desc="Secondary Data" PropBitMask="529">',
            '<DataPrv Name="ACatSecListRpt" Desc="Secondary Vehicles" PropBitMask="529">',
            '<DataPrv Name="ACatRptByTimeEvent" Desc="Time Events" PropBitMask="532" UsesSameElements="true">',
            "<DataPrvGroup>",
            '<DataPrv Name="TimeIn" Desc="TimeIn">',
            '<Element Name="Ellipsoid Norm wrt Secondary" Type="3" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="TCA" Desc="TCA">',
            '<Element Name="Range wrt Secondary - CrossTrack" Type="0" Dim="DistanceUnit"/>',
            "</DataPrv>",
            '<DataPrv Name="TMS" Desc="TMS">',
            '<Element Name="Primary Ellipsoid - Tangential" Type="0" Dim="DistanceUnit"/>',
            "</DataPrv>",
            "</DataPrvGroup>",
            "</DataPrv>",
            "</DataProviderCollection>",
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

    # endregion

    # region DPSchemaAircraft
    @category("Graphics Tests")
    def test_DPSchemaAircraft(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren["a340"]

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Aircraft">',
            '<DataPrv Name="ConstraintData" Desc="Active Constraints"',
            '<DataPrv Name="Astrogator" Desc="Astrogator Values"',
            "<DataPrvGroup>",
            '<DataPrv Name="Top" Desc="Top">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="Formation" Desc="Formation">',
            '<Element Name="CloseApproachX" Type="0" Dim="DistanceUnit"/>',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<Element Name="Start Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="Stop Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="RelEph" Desc="Ephemeris Diff" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Fixed" Desc="Fixed">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="FlightProfileDownRange" Desc="Flight Profile By Down Range" PropBitMask="513">',
            '<PreData Desc="&quot;&lt;MinDownRange&gt; &lt;MaxDownRange&gt; &lt;DownRangeStep&gt;&quot; - Minimum/Maximum Down Range: Defines the upper and lower bounds of the profile report; the down range distance is the ground distance from the starting point to the aircraft&apos;s position at its current point. Down Range Step: The down range distance interval between each data point in the report. All values must either be entered in Object Model AviatorDistance Units (when using Object Model) or Scenario AviatorDistance units."/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointingCovar" Desc="Pointing Covariance (Projection)" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;GroundVehicle/Veh1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="SolarAnglesData" Desc="Solar Panel Angles" PropBitMask="10258">',
            '<PreData Desc="&quot;&lt;Time&gt;&quot; - in epoch secs"/>',
            '<Element Name="Angle" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="CrossWindAxis" Desc="CrossWindAxis">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="CrossWindAxis" Desc="CrossWindAxis">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="Waypoints" Desc="Waypoints" PropBitMask="17">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="Latitude" Type="0" Dim="LatitudeUnit"/>',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

    # endregion

    # region DPSchemaAntenna
    def test_DPSchemaAntenna(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        satObj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.SATELLITE, "tempSat1")
        antObj: "IStkObject" = satObj.children.new(STK_OBJECT_TYPE.ANTENNA, "tempAnt1")

        schema: str = None
        schema = antObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Antenna">',
            '<DataPrv Name="AntennaGain" Desc="Antenna Gain" PropBitMask="513">',
            '<PreData Desc="&quot;GainCutType { Azimuth | Elevation } {Parameters}&quot;. {Parameters} can be entered in any order. If GainCutType is Azimuth, then the following {Parameters} are required: MinElevation &lt;Value&gt; MaxElevation &lt;Value&gt; ElevationStep &lt;Value&gt; AzimuthValue &lt;Value&gt;. If GainCutType is Elevation, then the following {Parameters} are required: MinAzimuth &lt;Value&gt; MaxAzimuth &lt;Value&gt; AzimuthStep &lt;Value&gt; ElevationValue &lt;Value&gt;. In both cases, the following {Parameters} are optional: Time &apos;&lt;DateTimeValue&gt;&apos; CoordinateSystem { Polar | Rectangular | &apos;Spherical Az/El&apos; | &apos;UV Grid&apos; | &apos;Elev Over Azi&apos;}. All above &lt;Value&gt; are entered in scenario angle units. The Min, Max, AzimuthValue and ElevationValue values should be between 0 and 360 degrees. The Min must be less than the Max. The Step value should be between 0.001 and 30.0 degrees. The Time option allows the user to enter the time of the computation. If not entered the current scenario animation time will be used. If entered, the &apos;&lt;DateTimeValue&gt;&apos; is either in Object Model Date units (when using Object Model) or Scenario Date units, and is enclosed in single quotes."/>',
            '<Element Name="Elevation" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="AntennaGainMatrix" Desc="Antenna Gain Matrix" PropBitMask="513">',
            '<PreData Desc="&quot;{Parameters}&quot;. {Parameters} can be entered in any order. The following {Parameters} are required: MinElevation &lt;Value&gt; MaxElevation &lt;Value&gt; ElevationStep &lt;Value&gt; MinAzimuth &lt;Value&gt; MaxAzimuth &lt;Value&gt; AzimuthStep &lt;Value&gt;. The following {Parameters} are optional: Time &apos;&lt;DateTimeValue&gt;&apos; CoordinateSystem { Polar | Rectangular | &apos;Spherical Az/El&apos; | &apos;UV Grid&apos; | &apos;Elev Over Azi&apos; }. The Min, Max and Step &lt;Value&gt; are entered in scenario angle units. The Min and Max values should be between 0 and 360 degrees. The Min must be less than the Max. The Step value should be between 0.001 and 30.0 degrees. The Time option allows the user to enter the time of the computation. If not entered the current scenario animation time will be used. If entered, the &apos;&lt;DateTimeValue&gt;&apos; is either in Object Model Date units (when using Object Model) or Scenario Date units, and is enclosed in single quotes."/>',
            '<Element Name="Elevation" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" Applicable="false">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Boresight" Desc="Boresight">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Boresight" Desc="Boresight">',
        ]

        try:
            self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        finally:
            antObj.unload()
            satObj.unload()

    # endregion

    # region DPSchemaAreaTarget
    def test_DPSchemaAreaTarget(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        atObj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.AREA_TARGET, "WardsAreaTarget1")

        schema: str = None
        schema = atObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="AreaTarget">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<Element Name="Start Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" Applicable="false">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="East" Desc="East">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="East" Desc="East">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="ECFVectors" Desc="Vectors(Fixed)" PropBitMask="2">',
            "<DataPrvGroup>",
            '<DataPrv Name="East" Desc="East">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="EME2000Vectors" Desc="Vectors(J2000)" PropBitMask="2">',
            "<DataPrvGroup>",
            '<DataPrv Name="ZenithDetic" Desc="Zenith(Detic)">',
            '<Element Name="Derivative Magnitude" Type="0" Dim="Unitless Per Time"/>',
            "</DataPrv>",
            "</DataPrvGroup>",
            "</DataPrv>",
            "</DataProviderCollection>",
        ]

        try:
            self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        finally:
            atObj.unload()

    # endregion

    # region DPSchemaChain
    def test_DPSchemaChain(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.CHAIN, "chain1")

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Chain">',
            '<DataPrv Name="ChainAERData" Desc="Access AER Data" PropBitMask="2562">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="Azimuth" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="AngleBetween" Desc="Angle Between" PropBitMask="2562" UsesSameElements="true">',
            "<DataPrvGroup>",
            '<DataPrv Name="GranularityDetermined" Desc="Granularity Determined">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="EventAngleBetween" Desc="Event Angle Between" PropBitMask="20" UsesSameElements="true">',
            "<DataPrvGroup>",
            '<DataPrv Name="AOS" Desc="AOS">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="TimeOrdAcc" Desc="Time Ordered Access" PropBitMask="516">',
            '<Element Name="Access Number" Type="1" Dim=""/>',
            "</DataPrv>",
            "</DataProviderCollection>",
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        obj.unload()

    # endregion

    # region DPSchemaCommSystem
    def test_DPSchemaCommSystem(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.COMM_SYSTEM, "CommSystem1")

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="CommSystem">',
            '<DataPrv Name="BasicProps" Desc="Basic Properties" PropBitMask="17">',
            '<Element Name="No. of Transmitters" Type="1" Dim=""/>',
            '<DataPrv Name="CDF" Desc="Cumulative Density Function" PropBitMask="',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1/Receiver/Receiver1&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="RcvdIsoPower" Desc="Rcvd. Iso. Power">',
            '<Element Name="Value" Type="0" Dim="RatioUnit"/>',
            '<DataPrv Name="EbNoIo" Desc="Eb/(No+Io)">',
            '<Element Name="Percentage" Type="0" Dim="Percent"/>',
            '<DataPrv Name="PwrFluxDensity" Desc="Pwr Flux Density">',
            '<Element Name="Log Percent" Type="0" Dim=""/>',
            "</DataPrv>",
            "</DataPrvGroup>",
            "</DataPrv>",
            '<DataPrv Name="DpDetailData" Desc="Data Provider Detail" PropBitMask="17">',
            '<DataPrv Name="DpSummaryData" Desc="Data Provider Summary" PropBitMask="17">',
            '<DataPrv Name="JamInfo" Desc="Interference Information" PropBitMask="786">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1/Receiver/Receiver1&quot;"/>',
            '<Element Name="Link To ID" Type="1" Dim=""/>',
            '<Element Name="Xmtr Power" Type="0" Dim="PowerUnit"/>',
            '<Element Name="Freq. Doppler Shift" Type="0" Dim="FrequencyUnit"/>',
            '<Element Name="Pol. Rel. Angle" Type="0" Dim="AngleUnit"/>',
            '<Element Name="Atmos Loss" Type="0" Dim="RatioUnit"/>',
            '<DataPrv Name="Interferers" Desc="Interferer Information" PropBitMask="17">',
            '<DataPrv Name="LinkInfo" Desc="Link Information" PropBitMask="770">',
            '<Element Name="EIRP" Type="0" Dim="PowerUnit"/>',
            '<Element Name="Rcvd. Frequency" Type="0" Dim="FrequencyUnit"/>',
            '<Element Name="Tantenna" Type="0" Dim="Temperature"/>',
            '<Element Name="C/(N+I)" Type="0" Dim="RatioUnit"/>',
            '<Element Name="TropoScintill Loss" Type="0" Dim="RatioUnit"/>',
            '<DataPrv Name="PDF" Desc="Probability Density Function" PropBitMask="',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1/Receiver/Receiver1&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="RcvdIsoPower" Desc="Rcvd. Iso. Power">',
            '<Element Name="Value" Type="0" Dim="RatioUnit"/>',
            '<DataPrv Name="Tequivalent" Desc="Tequivalent">',
            '<Element Name="Percentage" Type="0" Dim="Percent"/>',
            '<DataPrv Name="DeltaTT" Desc="Delta T/T">',
            '<Element Name="Value" Type="0" Dim="RatioUnit"/>',
            '<DataPrv Name="Receivers" Desc="Receiver Information" PropBitMask="17">',
            '<Element Name="Receiver ID" Type="1" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="Transmitters" Desc="Transmitter Information" PropBitMask="17">',
            "</DataProviderCollection>",
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        obj.unload()

    # endregion

    # region DPSchemaConstellation
    def test_DPSchemaConstellation(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        constObj: "IStkObject" = scenChildren["gps_const"]

        schema: str = None
        schema = constObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Constellation">',
            "</DataProviderCollection>",
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

    # endregion

    # region DPSchemaCoverageDef
    def test_DPSchemaCoverageDef(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "covdef1")

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="CoverageDefinition">',
            '<DataPrv Name="Accesses" Desc="Access Duration" PropBitMask="513">',
            '<Element Name="Duration" Type="0" Dim="TimeUnit"/>',
            '<Element Name="Percent Under" Type="0" Dim=""/>',
            '<DataPrv Name="CoverageByAsset" Desc="Coverage By Asset" PropBitMask="529">',
            '<Element Name="Asset Name" Type="2" Dim=""/>',
            '<DataPrv Name="GlobalCov" Desc="Global Coverage" PropBitMask="516">',
            '<Element Name="Global Coverage Number" Type="1" Dim=""/>',
            '<Element Name="Global Coverage Start" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="RegionByPass" Desc="Selected Region By Pass" PropBitMask="529">',
            '<Element Name="Access Number" Type="1" Dim=""/>',
            '<DataPrv Name="RegionFullCov" Desc="Selected Region Full Coverage" PropBitMask="516">',
            '<Element Name="Coverage Number" Type="1" Dim=""/>',
            '<DataPrv Name="TotCovByRegion" Desc="Time To Cover By Region" PropBitMask="529">',
            '<Element Name="Region Name" Type="2" Dim=""/>',
            "</DataPrv>",
            "</DataProviderCollection>",
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        obj.unload()

    # endregion

    # region DPSchemaFacility
    def test_DPSchemaFacility(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        facObj: "IStkObject" = scenChildren["Facility1"]

        schema: str = None
        schema = facObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Facility">',
            '<DataPrv Name="ConstraintData" Desc="Active Constraints" PropBitMask="17">',
            '<Element Name="Constraint" Type="2" Dim=""/>',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<Element Name="Start Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" Applicable="false">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="East" Desc="East">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="East" Desc="East">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="BodyVectors" Desc="Vectors(Body)" PropBitMask="2">',
            "<DataPrvGroup>",
            '<DataPrv Name="East" Desc="East">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            "</DataPrvGroup>",
            "</DataPrv>",
            "</DataProviderCollection>",
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

    # endregion

    # region DPSchemaFigureOfMerit
    def test_DPSchemaFigureOfMerit(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        cd: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "cv1")
        fom: "IStkObject" = cd.children.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, "fom1")

        schema: str = None
        schema = fom.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="FigureOfMerit">',
            '<DataPrv Name="CovGenInfo" Desc="Coverage Definition" PropBitMask="17">',
            '<Element Name="Coverage Properties" Type="2" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="CurrentValue" Desc="Overall Value by Time" PropBitMask="2">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="Minimum" Type="0" Dim=""/>',
            '<Element Name="Maximum" Type="0" Dim=""/>',
            "</DataPrv>",
            '<DataPrv Name="PointAllNavAcc" Desc="Selected Point All Nav Accs" PropBitMask="514">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="GACC" Type="0" Dim="DistanceUnit"/>',
            '<Element Name="PACC" Type="0" Dim="DistanceUnit"/>',
            '<DataPrv Name="PercentVal" Desc="Selected Point Percent Val" PropBitMask="513" UsesSameElements="true">',
            "<DataPrvGroup>",
            '<DataPrv Name="AllTimes" Desc="All Times">',
            '<Element Name="Value" Type="0" Dim=""/>',
            '<DataPrv Name="StaticSatisfaction" Desc="Static Satisfaction" PropBitMask="529">',
            '<Element Name="Percent Satisfied" Type="0" Dim=""/>',
            '<Element Name="Area Satisfied" Type="0" Dim="Area"/>',
            "</DataPrv>",
            '<DataPrv Name="TimeValByPoint" Desc="Time Value By Point" PropBitMask="529">',
            '<PreData Desc="&quot;&lt;DateTime&gt;&quot; - entered in Object Model Date units (when using Object Model) or Scenario Date units."/>',
            '<Element Name="Latitude" Type="0" Dim="LatitudeUnit"/>',
            '<Element Name="Longitude" Type="0" Dim="LongitudeUnit"/>',
            '<DataPrv Name="ValByPoint" Desc="Value By Point" PropBitMask="529">',
            '<Element Name="Latitude" Type="0" Dim="LatitudeUnit"/>',
            '<Element Name="Longitude" Type="0" Dim="LongitudeUnit"/>',
            '<Element Name="Altitude" Type="0" Dim="DistanceUnit"/>',
            "</DataProviderCollection>",
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        fom.unload()
        cd.unload()

    # endregion

    # region DPSchemaGrndVeh
    @category("Graphics Tests")
    def test_DPSchemaGrndVeh(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "grndveh")

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="GroundVehicle">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<Element Name="Start Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="RelEph" Desc="Ephemeris Diff" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="LLRState" Desc="LLR State" PropBitMask="2" UsesSameElements="true">',
            "<DataPrvGroup>",
            '<DataPrv Name="Fixed" Desc="Fixed">',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointingCovar" Desc="Pointing Covariance (Projection)" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;GroundVehicle/Veh1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="SolarAnglesData" Desc="Solar Panel Angles" PropBitMask="10258">',
            '<PreData Desc="&quot;&lt;Time&gt;&quot; - in epoch secs"/>',
            '<Element Name="Angle" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="East" Desc="East">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="East" Desc="East">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        obj.unload()

    # endregion

    # region DPSchemaLnchVeh
    def test_DPSchemaLnchVeh(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "lnchveh")

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="LaunchVehicle">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="RIC" Desc="RIC">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<DataPrv Name="BodyOrient123" Desc="Body Axes Orientation:YPR 123" PropBitMask="2" UsesSameElements="true">',
            "<DataPrvGroup>",
            '<DataPrv Name="RIC" Desc="RIC">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="RelEph" Desc="Ephemeris Diff" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Fixed" Desc="Fixed">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="PointingCovar" Desc="Pointing Covariance (Projection)" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;GroundVehicle/Veh1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="Ric" Desc="Relative Motion" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="AngVelocity" Desc="AngVelocity">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="AngVelocity" Desc="AngVelocity">',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        obj.unload()

    # endregion

    # region DPSchemaMissile
    def test_DPSchemaMissile(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.MISSILE, "mis")

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Missile">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="RIC" Desc="RIC">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<DataPrv Name="BodyOrient123" Desc="Body Axes Orientation:YPR 123" PropBitMask="2" UsesSameElements="true">',
            "<DataPrvGroup>",
            '<DataPrv Name="RIC" Desc="RIC">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="RelEph" Desc="Ephemeris Diff" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Fixed" Desc="Fixed">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="PointingCovar" Desc="Pointing Covariance (Projection)" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;GroundVehicle/Veh1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="Ric" Desc="Relative Motion" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="AngVelocity" Desc="AngVelocity">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="AngVelocity" Desc="AngVelocity">',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        obj.unload()

    # endregion

    # region DPSchemaPlanet
    def test_DPSchemaPlanet(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.PLANET, "plnt")

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Planet">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="ICRF" Desc="ICRF">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="MeanEclpJ2000" Desc="MeanEclpJ2000">',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Earth" Desc="Earth">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Earth" Desc="Earth">',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        obj.unload()

    # endregion

    # region DPSchemaRadar
    def test_DPSchemaRadar(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        satObj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.SATELLITE, "tempSat1")
        radarObj: "IStkObject" = satObj.children.new(STK_OBJECT_TYPE.RADAR, "tempRadar1")

        schema: str = None
        schema = radarObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Radar">',
            '<DataPrv Name="AntennaGain" Desc="Antenna Gain" PropBitMask="513">',
            '<PreData Desc="&quot;GainCutType { Azimuth | Elevation } {Parameters}&quot;. {Parameters} can be entered in any order. If GainCutType is Azimuth, then the following {Parameters} are required: MinElevation &lt;Value&gt; MaxElevation &lt;Value&gt; ElevationStep &lt;Value&gt; AzimuthValue &lt;Value&gt;. If GainCutType is Elevation, then the following {Parameters} are required: MinAzimuth &lt;Value&gt; MaxAzimuth &lt;Value&gt; AzimuthStep &lt;Value&gt; ElevationValue &lt;Value&gt;. In both cases, the following {Parameters} are optional: Time &apos;&lt;DateTimeValue&gt;&apos; CoordinateSystem { Polar | Rectangular | &apos;Spherical Az/El&apos; | &apos;UV Grid&apos; | &apos;Elev Over Azi&apos;}. All above &lt;Value&gt; are entered in scenario angle units. The Min, Max, AzimuthValue and ElevationValue values should be between 0 and 360 degrees. The Min must be less than the Max. The Step value should be between 0.001 and 30.0 degrees. The Time option allows the user to enter the time of the computation. If not entered the current scenario animation time will be used. If entered, the &apos;&lt;DateTimeValue&gt;&apos; is either in Object Model Date units (when using Object Model) or Scenario Date units, and is enclosed in single quotes."/>',
            '<Element Name="Elevation" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" Applicable="false">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Boresight" Desc="Boresight">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Boresight" Desc="Boresight">',
        ]

        try:
            self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        finally:
            radarObj.unload()
            satObj.unload()

    # endregion

    # region DPSchemaReceiver
    def test_DPSchemaReceiver(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        satObj: "IStkObject" = scenChildren["Satellite1"]
        satChildren: "IStkObjectCollection" = satObj.children
        recObj: "IStkObject" = satChildren["Receiver1"]

        schema: str = None
        schema = recObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Receiver">',
            '<DataPrv Name="AntennaGain" Desc="Antenna Gain" PropBitMask="513">',
            '<PreData Desc="&quot;GainCutType { Azimuth | Elevation } {Parameters}&quot;. {Parameters} can be entered in any order. If GainCutType is Azimuth, then the following {Parameters} are required: MinElevation &lt;Value&gt; MaxElevation &lt;Value&gt; ElevationStep &lt;Value&gt; AzimuthValue &lt;Value&gt;. If GainCutType is Elevation, then the following {Parameters} are required: MinAzimuth &lt;Value&gt; MaxAzimuth &lt;Value&gt; AzimuthStep &lt;Value&gt; ElevationValue &lt;Value&gt;. In both cases, the following {Parameters} are optional: Time &apos;&lt;DateTimeValue&gt;&apos; CoordinateSystem { Polar | Rectangular | &apos;Spherical Az/El&apos; | &apos;UV Grid&apos; | &apos;Elev Over Azi&apos;}. All above &lt;Value&gt; are entered in scenario angle units. The Min, Max, AzimuthValue and ElevationValue values should be between 0 and 360 degrees. The Min must be less than the Max. The Step value should be between 0.001 and 30.0 degrees. The Time option allows the user to enter the time of the computation. If not entered the current scenario animation time will be used. If entered, the &apos;&lt;DateTimeValue&gt;&apos; is either in Object Model Date units (when using Object Model) or Scenario Date units, and is enclosed in single quotes."/>',
            '<Element Name="Elevation" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="AntennaGainMatrix" Desc="Antenna Gain Matrix" PropBitMask="513">',
            '<PreData Desc="&quot;{Parameters}&quot;. {Parameters} can be entered in any order. The following {Parameters} are required: MinElevation &lt;Value&gt; MaxElevation &lt;Value&gt; ElevationStep &lt;Value&gt; MinAzimuth &lt;Value&gt; MaxAzimuth &lt;Value&gt; AzimuthStep &lt;Value&gt;. The following {Parameters} are optional: Time &apos;&lt;DateTimeValue&gt;&apos; CoordinateSystem { Polar | Rectangular | &apos;Spherical Az/El&apos; | &apos;UV Grid&apos; | &apos;Elev Over Azi&apos; }. The Min, Max and Step &lt;Value&gt; are entered in scenario angle units. The Min and Max values should be between 0 and 360 degrees. The Min must be less than the Max. The Step value should be between 0.001 and 30.0 degrees. The Time option allows the user to enter the time of the computation. If not entered the current scenario animation time will be used. If entered, the &apos;&lt;DateTimeValue&gt;&apos; is either in Object Model Date units (when using Object Model) or Scenario Date units, and is enclosed in single quotes."/>',
            '<Element Name="Elevation" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" Applicable="false">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Boresight" Desc="Boresight">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Boresight" Desc="Boresight">',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

    # endregion

    # region DPSchemaSatellite
    @category("Graphics Tests")
    def test_DPSchemaSatellite(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        satObj: "IStkObject" = scenChildren["Satellite1"]

        schema: str = None
        schema = satObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Satellite">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="RIC" Desc="RIC">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="RelEph" Desc="Ephemeris Diff" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Fixed" Desc="Fixed">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="PointingCovar" Desc="Pointing Covariance (Projection)" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;GroundVehicle/Veh1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="Ric" Desc="RIC Coordinates" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="Ric" Desc="Relative Motion" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt;&quot; - e.g. &quot;Satellite/Sat1&quot;"/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="SolarAnglesData" Desc="Solar Panel Angles" PropBitMask="10258">',
            '<PreData Desc="&quot;&lt;Time&gt;&quot; - in epoch secs"/>',
            '<Element Name="Angle" Type="0" Dim="AngleUnit"/>',
            '<Element Name="Area" Type="0" Dim="Area"/>',
            '<Element Name="Effective Area" Type="0" Dim="Area"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="AngMomentum" Desc="AngMomentum">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="AngMomentum" Desc="AngMomentum">',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

    # endregion

    # region DPSchemaScenario
    def test_DPSchemaScenario(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children

        schema: str = None
        schema = scenObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Scenario">',
            '<DataPrv Name="ScenarioConstraintData" Desc="Active Constraints" PropBitMask="17">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Earth2VectorUserDefined" Desc="Earth 2-Vector_User_Defined">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="OldTle" Desc="Out Of Date TLE" PropBitMask="17">',
            '<PreData Desc="&quot;&lt;FilePath&gt;, &lt;DateTime&gt;&quot; - e.g. &lt;FilePath&gt; is the TLE file path and &lt;DateTime&gt; uses either the Object Model Date units (when using the Object Model) or the Scenario&apos;s current Date units format"/>',
            '<Element Name="SSC" Type="2" Dim=""/>',
            '<Element Name="TLE Epoch" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="EarthEquator" Desc="Earth Equator">',
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="EarthCenter" Desc="Earth Center">',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="EarthCenter" Desc="Earth Center">',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="EarthAngularVelocity" Desc="Earth Angular_Velocity">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="EarthAngularVelocity" Desc="Earth Angular_Velocity">',
        ]
        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

    # endregion

    # region DPSchemaSensor
    def test_DPSchemaSensor(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        satObj: "IStkObject" = scenChildren["Satellite1"]
        satChildren: "IStkObjectCollection" = satObj.children
        senObj: "IStkObject" = satChildren["Sensor1"]

        schema: str = None
        schema = senObj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Sensor">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Body" Desc="Body">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="FootprintAtDist" Desc="Footprint Area At Distance" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;Altitude&gt;&quot; - one of the altitude level steps set in 2d graphics projection extension distances panel."/>',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<Element Name="Area" Type="0" Dim="Area"/>',
            '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" Applicable="false">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<DataPrv Name="PointChooseSystem" Desc="Points Choose System" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Sun ICRF&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Center" Desc="Center">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Boresight" Desc="Boresight">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="Boresight" Desc="Boresight">',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

    # endregion

    # region DPSchemaStar
    def test_DPSchemaStar(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        obj: "IStkObject" = scenChildren.new(STK_OBJECT_TYPE.STAR, "star1")

        schema: str = None
        schema = obj.data_providers.get_schema()
        # System.logger.WriteLine(schema);

        # Some Random text searches within the XML to try to get some accountability for the
        # stability of the data returned.  Could try to compare the entire XML, but it is subject
        # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
        # schema's into this test as text or possibly a file.

        # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
        # that we in a way test the "order" coherency of the data provider schema string as well.

        someSchemaEntries: "List[str]" = [
            '<DataProviderCollection STKObject="Star">',
            '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="ICRF" Desc="ICRF">',
            '<Element Name="Time" Type="0" Dim="DateFormat"/>',
            '<DataPrv Name="MeanEclpJ2000" Desc="MeanEclpJ2000">',
            '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
            '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
            '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="EclipticNormal" Desc="EclipticNormal">',
            '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
            '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
            "<DataPrvGroup>",
            '<DataPrv Name="EclipticNormal" Desc="EclipticNormal">',
        ]

        self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        obj.unload()

    # endregion

    # region DPSchemaTransmitter
    def test_DPSchemaTransmitter(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        satObj: "IStkObject" = scenChildren["Satellite1"]
        tranObj: "IStkObject" = None
        try:
            tranObj = satObj.children.new(STK_OBJECT_TYPE.TRANSMITTER, "Transmitter1")

            schema: str = None
            schema = tranObj.data_providers.get_schema()

            # Some Random text searches within the XML to try to get some accountability for the
            # stability of the data returned.  Could try to compare the entire XML, but it is subject
            # to change as Data Providers are added or removed.  Also is a pain to get the bigger XML
            # schema's into this test as text or possibly a file.

            # NOTE: We slowly widdle away at the schema string ( using substring/indexof ) so
            # that we in a way test the "order" coherency of the data provider schema string as well.

            someSchemaEntries: "List[str]" = [
                '<DataProviderCollection STKObject="Transmitter">',
                '<DataPrv Name="AntennaGain" Desc="Antenna Gain" PropBitMask="513">',
                '<PreData Desc="&quot;GainCutType { Azimuth | Elevation } {Parameters}&quot;. {Parameters} can be entered in any order. If GainCutType is Azimuth, then the following {Parameters} are required: MinElevation &lt;Value&gt; MaxElevation &lt;Value&gt; ElevationStep &lt;Value&gt; AzimuthValue &lt;Value&gt;. If GainCutType is Elevation, then the following {Parameters} are required: MinAzimuth &lt;Value&gt; MaxAzimuth &lt;Value&gt; AzimuthStep &lt;Value&gt; ElevationValue &lt;Value&gt;. In both cases, the following {Parameters} are optional: Time &apos;&lt;DateTimeValue&gt;&apos; CoordinateSystem { Polar | Rectangular | &apos;Spherical Az/El&apos; | &apos;UV Grid&apos; | &apos;Elev Over Azi&apos;}. All above &lt;Value&gt; are entered in scenario angle units. The Min, Max, AzimuthValue and ElevationValue values should be between 0 and 360 degrees. The Min must be less than the Max. The Step value should be between 0.001 and 30.0 degrees. The Time option allows the user to enter the time of the computation. If not entered the current scenario animation time will be used. If entered, the &apos;&lt;DateTimeValue&gt;&apos; is either in Object Model Date units (when using Object Model) or Scenario Date units, and is enclosed in single quotes."/>',
                '<Element Name="Elevation" Type="0" Dim="AngleUnit"/>',
                '<DataPrv Name="AntennaGainMatrix" Desc="Antenna Gain Matrix" PropBitMask="513">',
                '<PreData Desc="&quot;{Parameters}&quot;. {Parameters} can be entered in any order. The following {Parameters} are required: MinElevation &lt;Value&gt; MaxElevation &lt;Value&gt; ElevationStep &lt;Value&gt; MinAzimuth &lt;Value&gt; MaxAzimuth &lt;Value&gt; AzimuthStep &lt;Value&gt;. The following {Parameters} are optional: Time &apos;&lt;DateTimeValue&gt;&apos; CoordinateSystem { Polar | Rectangular | &apos;Spherical Az/El&apos; | &apos;UV Grid&apos; | &apos;Elev Over Azi&apos; }. The Min, Max and Step &lt;Value&gt; are entered in scenario angle units. The Min and Max values should be between 0 and 360 degrees. The Min must be less than the Max. The Step value should be between 0.001 and 30.0 degrees. The Time option allows the user to enter the time of the computation. If not entered the current scenario animation time will be used. If entered, the &apos;&lt;DateTimeValue&gt;&apos; is either in Object Model Date units (when using Object Model) or Scenario Date units, and is enclosed in single quotes."/>',
                '<Element Name="Elevation" Type="0" Dim="AngleUnit"/>',
                '<DataPrv Name="AxesChooseAxes" Desc="Axes Choose Axes" PropBitMask="2" UsesSameElements="true">',
                '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g. &quot;CentralBody/Moon J2000&quot;"/>',
                "<DataPrvGroup>",
                '<DataPrv Name="Body" Desc="Body">',
                '<Element Name="Time" Type="0" Dim="DateFormat"/>',
                '<Element Name="YPR321 yaw" Type="0" Dim="AngleUnit"/>',
                '<DataPrv Name="CrdnAvailableTimes" Desc="Crdn Available Times" PropBitMask="8196">',
                '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;VectorName&gt;&quot; - e.g. &quot;CentralBody/Earth Angular_Velocity&quot;"/>',
                '<DataPrv Name="PlaneChooseSystem" Desc="Planes Choose System" PropBitMask="2" Applicable="false">',
                '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;SystemName&gt;&quot; - e.g. &quot;CentralBody/Earth Fixed&quot;"/>',
                "<DataPrvGroup>",
                '<DataPrv Name="BasicProps" Desc="Basic Properties" PropBitMask="17">',
                '<Element Name="Gains &amp; Losses" Type="3" Dim="RatioUnit"/>',
                '<DataPrv Name="PointChoosePlane" Desc="Points Choose Plane" PropBitMask="2" UsesSameElements="true">',
                '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
                "<DataPrvGroup>",
                '<DataPrv Name="Center" Desc="Center">',
                '<DataPrv Name="VectorChooseAxes" Desc="Vector Choose Axes" PropBitMask="2">',
                '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;AxesName&gt;&quot; - e.g &quot;CentralBody/Earth Fixed&quot;"/>',
                "<DataPrvGroup>",
                '<DataPrv Name="Boresight" Desc="Boresight">',
                '<DataPrv Name="VectorChoosePlane" Desc="Vector Choose Plane" PropBitMask="2">',
                '<PreData Desc="&quot;&lt;TruncObjectPath&gt; &lt;PlaneName&gt;&quot; - e.g. &quot;CentralBody/Earth Equator&quot;"/>',
                "<DataPrvGroup>",
                '<DataPrv Name="Boresight" Desc="Boresight">',
            ]

            self.DPSchemaEntriesChecker(schema, someSchemaEntries)

        finally:
            if tranObj != None:
                tranObj.unload()

    # endregion

    # region DPEnumerateConstraints
    def test_DPEnumerateConstraints(self):
        o: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children[0].children["Satellite1"]
        count: int = o.data_providers.count

        i: int = 0
        while i < count:
            dp: "IDataProviderInfo" = o.data_providers[i]
            sName: str = dp.name
            b: bool = dp.is_group()

            i += 1

    # endregion

    # region DPEnumProviders
    def test_DPEnumProviders(self):
        o: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children[0].children["Satellite1"]
        count: int = o.data_providers.count

        i: int = 0
        while i < count:
            dp: "IDataProviderInfo" = o.data_providers[i]
            sName: str = dp.name
            type: "DATA_PROVIDER_TYPE" = dp.type

            i += 1

    # endregion

    # region IAgDataPrvTimeVar_ExecEventArray
    def test_IAgDataPrvTimeVar_ExecEventArray(self):
        try:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("DataProvidersTests", "ENG88167", "OMTestScenario.sc"))

            scenObj: "IStkObject" = TestBase.Application.current_scenario
            oSatellite: "IStkObject" = scenObj.children["Satellite1"]
            oGroup: "DataProviderGroup" = clr.Convert(
                oSatellite.data_providers["Cartesian Position"], DataProviderGroup
            )
            oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)

            # Get the EventArray that will be used for testing
            # TimeToolEventArrayStartStopTimes _eventArray;
            EventArrayName: str = "TestArray1"

            _EventArrayProvider: "AnalysisWorkbenchProvider" = TestBase.Application.vgt_root.get_provider(
                "Satellite/Satellite1"
            )
            EventArrayTestObject: "ITimeToolEventArray" = _EventArrayProvider.event_arrays[EventArrayName]

            # Arguments are the EventArray and the object's start and stop times
            oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_event_array(
                EventArrayTestObject, "5 Mar 2010 17:00:00.000", "6 Mar 2010 17:00:00.000"
            )

            ds: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
            arValues = ds.get_values()
            Assert.assertEqual("5 Mar 2010 17:00:00.000000000", arValues[0])
            Assert.assertEqual("5 Mar 2010 17:25:45.790152528", arValues[1])
            Assert.assertEqual("5 Mar 2010 18:01:28.239198420", arValues[2])
            Assert.assertEqual("5 Mar 2010 19:00:19.704529159", arValues[3])

            ds = oResult.intervals[0].data_sets[1]
            arValues = ds.get_values()
            Assert.assertAlmostEqual(3610.4823, float(arValues[0]), delta=1.0)
            Assert.assertAlmostEqual(3945.0858, float(arValues[1]), delta=1.0)
            Assert.assertAlmostEqual(-4902.211, float(arValues[2]), delta=1.0)
            Assert.assertAlmostEqual(4791.2327, float(arValues[3]), delta=1.0)

            ds = oResult.intervals[0].data_sets[2]
            arValues = ds.get_values()
            Assert.assertAlmostEqual(-5854.3305, float(arValues[0]), delta=1.0)
            Assert.assertAlmostEqual(2927.0119, float(arValues[1]), delta=1.0)
            Assert.assertAlmostEqual(2777.0014, float(arValues[2]), delta=1.0)
            Assert.assertAlmostEqual(1100.742, float(arValues[3]), delta=1.0)

            ds = oResult.intervals[0].data_sets[3]
            arValues = ds.get_values()
            Assert.assertAlmostEqual(-0.0095, float(arValues[0]), delta=1.0)
            Assert.assertAlmostEqual(4814.319, float(arValues[1]), delta=1.0)
            Assert.assertAlmostEqual(-3945.2958, float(arValues[2]), delta=1.0)
            Assert.assertAlmostEqual(4810.5327, float(arValues[3]), delta=1.0)

            # BUG108403

            _EventArrayProvider2: "AnalysisWorkbenchProvider" = TestBase.Application.vgt_root.get_provider(
                "Place/Place1"
            )
            EventArrayTestObject2: "ITimeToolEventArray" = _EventArrayProvider2.event_arrays[EventArrayName]

            oResult2: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_event_array(
                EventArrayTestObject2, "5 Mar 2010 17:00:00.000", "6 Mar 2010 17:00:00.000"
            )

            ds2: "DataProviderResultDataSet" = oResult2.intervals[0].data_sets[0]
            arValues2 = ds2.get_values()
            Assert.assertEqual("5 Mar 2010 17:10:00.000000000", arValues2[0])
            Assert.assertEqual("5 Mar 2010 17:20:00.000000000", arValues2[1])
            Assert.assertEqual("5 Mar 2010 17:30:00.000000000", arValues2[2])
            Assert.assertEqual("5 Mar 2010 17:40:00.000000000", arValues2[3])

            ds2 = oResult2.intervals[0].data_sets[1]
            arValues2 = ds2.get_values()
            Assert.assertAlmostEqual(5255.7356, float(arValues2[0]), delta=1.0)
            Assert.assertAlmostEqual(4958.0505, float(arValues2[1]), delta=1.0)
            Assert.assertAlmostEqual(2895.4577, float(arValues2[2]), delta=1.0)
            Assert.assertAlmostEqual(-136.5607, float(arValues2[3]), delta=1.0)

            ds2 = oResult2.intervals[0].data_sets[2]
            arValues2 = ds2.get_values()
            Assert.assertAlmostEqual(-3267.9377, float(arValues2[0]), delta=1.0)
            Assert.assertAlmostEqual(646.0801, float(arValues2[1]), delta=1.0)
            Assert.assertAlmostEqual(4390.6513, float(arValues2[2]), delta=1.0)
            Assert.assertAlmostEqual(6497.3007, float(arValues2[3]), delta=1.0)

            ds2 = oResult2.intervals[0].data_sets[3]
            arValues2 = ds2.get_values()
            Assert.assertAlmostEqual(3001.0988, float(arValues2[0]), delta=1.0)
            Assert.assertAlmostEqual(4723.2492, float(arValues2[1]), delta=1.0)
            Assert.assertAlmostEqual(4432.5245, float(arValues2[2]), delta=1.0)
            Assert.assertAlmostEqual(2252.8211, float(arValues2[3]), delta=1.0)

        finally:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    # endregion

    # region IAgDataPrvTimeVar_ExecElementsEventArray
    def test_IAgDataPrvTimeVar_ExecElementsEventArray(self):
        try:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("DataProvidersTests", "ENG88167", "OMTestScenario.sc"))

            scenObj: "IStkObject" = TestBase.Application.current_scenario
            oSatellite: "IStkObject" = scenObj.children["Satellite1"]
            oGroup: "DataProviderGroup" = clr.Convert(
                oSatellite.data_providers["Cartesian Position"], DataProviderGroup
            )
            oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)

            # Get the EventArray that will be used for testing
            # TimeToolEventArrayStartStopTimes _eventArray;
            EventArrayName: str = "TestArray1"

            _EventArrayProvider: "AnalysisWorkbenchProvider" = TestBase.Application.vgt_root.get_provider(
                "Satellite/Satellite1"
            )
            EventArrayTestObject: "ITimeToolEventArray" = _EventArrayProvider.event_arrays[EventArrayName]

            elemCols = ["Time", "z"]
            oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements_event_array(
                EventArrayTestObject, "5 Mar 2010 17:00:00.000", "6 Mar 2010 17:00:00.000", elemCols
            )

            ds: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
            arValues = ds.get_values()
            Assert.assertEqual("5 Mar 2010 17:00:00.000000000", arValues[0])
            Assert.assertEqual("5 Mar 2010 17:25:45.790152528", arValues[1])
            Assert.assertEqual("5 Mar 2010 18:01:28.239198420", arValues[2])
            Assert.assertEqual("5 Mar 2010 19:00:19.704529159", arValues[3])

            ds = oResult.intervals[0].data_sets[1]
            arValues = ds.get_values()
            Assert.assertAlmostEqual(-0.0095, float(arValues[0]), delta=0.01)
            Assert.assertAlmostEqual(4814.319, float(arValues[1]), delta=1.0)
            Assert.assertAlmostEqual(-3945.2958, float(arValues[2]), delta=1.0)
            Assert.assertAlmostEqual(4810.5327, float(arValues[3]), delta=1.0)

            # BUG108403

            _EventArrayProvider2: "AnalysisWorkbenchProvider" = TestBase.Application.vgt_root.get_provider(
                "Place/Place1"
            )
            EventArrayTestObject2: "ITimeToolEventArray" = _EventArrayProvider2.event_arrays[EventArrayName]

            # DataProviderResult oResult2 = ((DataProviderTimeVarying)oProvider).ExecEventArray(EventArrayTestObject2, "5 Mar 2010 17:00:00.000", "6 Mar 2010 17:00:00.000");
            oResult2: "DataProviderResult" = (
                clr.Convert(oProvider, DataProviderTimeVarying)
            ).exec_elements_event_array(
                EventArrayTestObject2, "5 Mar 2010 17:00:00.000", "6 Mar 2010 17:00:00.000", elemCols
            )

            ds2: "DataProviderResultDataSet" = oResult2.intervals[0].data_sets[0]
            arValues2 = ds2.get_values()
            Assert.assertEqual("5 Mar 2010 17:10:00.000000000", arValues2[0])
            Assert.assertEqual("5 Mar 2010 17:20:00.000000000", arValues2[1])
            Assert.assertEqual("5 Mar 2010 17:30:00.000000000", arValues2[2])
            Assert.assertEqual("5 Mar 2010 17:40:00.000000000", arValues2[3])

            ds2 = oResult2.intervals[0].data_sets[1]
            arValues2 = ds2.get_values()
            Assert.assertAlmostEqual(3001.0988, float(arValues2[0]), delta=1.0)
            Assert.assertAlmostEqual(4723.2492, float(arValues2[1]), delta=1.0)
            Assert.assertAlmostEqual(4432.5245, float(arValues2[2]), delta=1.0)
            Assert.assertAlmostEqual(2252.8211, float(arValues2[3]), delta=1.0)

        finally:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    # endregion

    # region IAgDataPrvTimeVar_ExecSingleElementsArray
    def test_IAgDataPrvTimeVar_ExecSingleElementsArray(self):
        TestBase.logger.WriteLine("----- ExecSingleElementsArray TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.reset_units()

        scenObj: "IStkObject" = TestBase.Application.current_scenario
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        oGroup: "DataProviderGroup" = clr.Convert(oSatellite.data_providers["Cartesian Position"], DataProviderGroup)
        oProvider: "DataProviderTimeVarying" = clr.Convert(oGroup.group["Fixed"], DataProviderTimeVarying)

        arTimes = Array.CreateInstance(clr.TypeOf(object), 3)
        arTimes[0] = "1 Jun 2004 12:00:00.000000000"
        arTimes[1] = "1 Jun 2001 12:00:00.000000000"  # out of range
        arTimes[2] = "1 Jun 2004 13:00:00.000000000"

        arFields = Array.CreateInstance(clr.TypeOf(object), 2)
        arFields[0] = "Time"
        arFields[1] = "x"

        data: "DataProviderResultTimeArrayElements" = oProvider.exec_single_elements_array(arTimes, arFields)

        arResult = data.get_array("x")

        Assert.assertEqual(2256.51110552601, arResult[0])
        Assert.assertIsNone(arResult[1])
        Assert.assertEqual(-5278.85394979558, arResult[2])

        TestBase.logger.WriteLine("----- ExecSingleElementsArray TEST ----- END -----")

    # endregion

    # region IAgDataPrvTimeVar_ExecElementsEventArrayOnly
    def test_IAgDataPrvTimeVar_ExecElementsEventArrayOnly(self):
        try:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("DataProvidersTests", "ENG88167", "OMTestScenario.sc"))

            scenObj: "IStkObject" = TestBase.Application.current_scenario
            oSatellite: "IStkObject" = scenObj.children["Satellite1"]
            oGroup: "DataProviderGroup" = clr.Convert(
                oSatellite.data_providers["Cartesian Position"], DataProviderGroup
            )
            oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)

            # Get the Time Event Array that will be used for testing
            EventArrayName: str = "TestTimeArray"

            _EventArrayProvider: "AnalysisWorkbenchProvider" = TestBase.Application.vgt_root.get_provider(
                "Satellite/Satellite1"
            )
            EventArrayTestObject: "ITimeToolEventArray" = _EventArrayProvider.event_arrays[EventArrayName]

            elemCols = ["Time", "z"]
            oResult: "DataProviderResult" = (
                clr.Convert(oProvider, DataProviderTimeVarying)
            ).exec_elements_event_array_only(EventArrayTestObject, elemCols)

            ds: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
            arValues = ds.get_values()
            Assert.assertEqual("5 Mar 2010 17:00:00.123656000", arValues[0])
            Assert.assertEqual("5 Mar 2010 17:20:00.000000000", arValues[1])
            Assert.assertEqual("5 Mar 2010 17:30:00.000000000", arValues[2])
            Assert.assertEqual("6 Mar 2010 16:00:00.123456000", arValues[3])

            ds = oResult.intervals[0].data_sets[1]
            arValues = ds.get_values()
            Assert.assertAlmostEqual(0.6576857019143554, float(arValues[0]), delta=1.0)
            Assert.assertAlmostEqual(4723.248101769223, float(arValues[1]), delta=1.0)
            Assert.assertAlmostEqual(4432.522791342938, float(arValues[2]), delta=1.0)
            Assert.assertAlmostEqual(-2995.723486981184, float(arValues[3]), delta=1.0)

            _EventArrayProvider2: "AnalysisWorkbenchProvider" = TestBase.Application.vgt_root.get_provider(
                "Place/Place1"
            )
            EventArrayTestObject2: "ITimeToolEventArray" = _EventArrayProvider2.event_arrays[EventArrayName]

            oResult2: "DataProviderResult" = (
                clr.Convert(oProvider, DataProviderTimeVarying)
            ).exec_elements_event_array_only(EventArrayTestObject2, elemCols)

            ds2: "DataProviderResultDataSet" = oResult2.intervals[0].data_sets[0]
            arValues2 = ds2.get_values()

            Assert.assertEqual("5 Mar 2010 17:00:00.123656000", arValues2[0])
            Assert.assertEqual("5 Mar 2010 17:20:00.000000000", arValues2[1])
            Assert.assertEqual("5 Mar 2010 17:30:00.000000000", arValues2[2])
            Assert.assertEqual("6 Mar 2010 16:00:00.123456000", arValues2[3])

            ds2 = oResult2.intervals[0].data_sets[1]
            arValues2 = ds2.get_values()
            Assert.assertAlmostEqual(0.6576857019143554, float(arValues2[0]), delta=1.0)
            Assert.assertAlmostEqual(4723.248101769223, float(arValues2[1]), delta=1.0)
            Assert.assertAlmostEqual(4432.522791342938, float(arValues2[2]), delta=1.0)
            Assert.assertAlmostEqual(-2995.723486981184, float(arValues2[3]), delta=1.0)

        finally:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    # endregion

    # region TestStartStopTimes
    def test_TestStartStopTimes(self):
        TestBase.logger.WriteLine("----- START STOP TIME TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.reset_units()

        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        Assert.assertIsNotNone(oSa)

        oScenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)
        Assert.assertIsNotNone(oScenario)
        oProvider: "IDataProvider" = clr.Convert(oSa.data_providers["Available Times"], IDataProvider)
        Assert.assertIsNotNone(oProvider)
        oInterval: "DataProviderInterval" = clr.Convert(oProvider, DataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult: "DataProviderResult" = oInterval.exec(oScenario.start_time, oScenario.stop_time)
        Assert.assertIsNotNone(oResult)

        oList: "DataProviderResultIntervalCollection" = oResult.intervals
        Assert.assertIsNotNone(oList)
        drInterval: "DataProviderResultInterval"
        for drInterval in oList:
            oDataSet: "DataProviderResultDataSet" = drInterval.data_sets[0]
            Assert.assertIsNotNone(oDataSet)
            if oDataSet.element_name == "Start Time":
                strTime: str = clr.Convert(oDataSet.get_values()[0], str)
                Assert.assertEqual("1 Jun 2004 12:00:00.000000000", strTime)

            oDataSet = drInterval.data_sets[1]
            Assert.assertIsNotNone(oDataSet)
            if oDataSet.element_name == "Stop Time":
                strTime: str = clr.Convert(oDataSet.get_values()[0], str)
                Assert.assertEqual("2 Jun 2004 12:00:00.000000000", strTime)

        TestBase.logger.WriteLine("----- START STOP TIME TEST ----- END -----")

    # endregion

    # region FacilityLightingTimes
    def test_FacilityLightingTimes(self):
        # Running Lighting Times//Sunlight for a facility using DataProviderInterval.Exec
        TestBase.logger.WriteLine("----- FACILITY LIGHTING TIMES TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")
        Assert.assertEqual("deg", TestBase.Application.unit_preferences.get_current_unit_abbrv("AngleUnit"))
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oFacility: "IStkObject" = oScenario.children["Facility1"]
        Assert.assertEqual(oScenario.children["Facility1"], oFacility)

        oGroup: "DataProviderGroup" = clr.Convert(oFacility.data_providers["Lighting Times"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Sunlight"], IDataProvider)
        Assert.assertIsNotNone(oProvider)
        oProvider.allow_user_interface = False
        Assert.assertFalse(oProvider.allow_user_interface)
        oProvider.pre_data = ""
        Assert.assertEqual("", oProvider.pre_data)

        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderInterval)).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00"
        )
        Assert.assertIsNotNone(oResult)

        # Verifying random datasets and their values
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(4, oResult.data_sets.count)
        Assert.assertEqual(1, oResult.intervals[0].data_sets[0].count)
        Assert.assertEqual("Date", oResult.intervals[0].data_sets[0].dimension_name)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        Assert.assertEqual("Start Time", oDataSet.element_name)
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", clr.Convert(arValues[0], str))

        oDataSet = oResult.intervals[0].data_sets[1]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        Assert.assertEqual("Stop Time", oDataSet.element_name)
        Assert.assertEqual("1 Jun 2004 13:00:00.000000000", clr.Convert(arValues[0], str))

        oDataSet = oResult.intervals[0].data_sets[2]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        Assert.assertEqual("Duration", oDataSet.element_name)
        Assert.assertEqual(3600.0, float(arValues[0]))

        del oResult
        TestBase.logger.WriteLine("----- FACILITY LIGHTING TIMES TEST ----- END -----")

    # endregion

    # region FacilityCartPos
    def test_FacilityCartPos(self):
        # Running Cartesian Position for a facility using DataProviderFixed.Exec
        TestBase.logger.WriteLine("----- FACILITY CARTESIAN POSITION TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", "mi")

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oFacility: "IStkObject" = oScenario.children["Facility1"]
        Assert.assertEqual(oScenario.children["Facility1"], oFacility)

        oProvider: "IDataProvider" = clr.Convert(oFacility.data_providers["Cartesian Position"], IDataProvider)
        Assert.assertIsNotNone(oProvider)
        oProvider.allow_user_interface = False
        Assert.assertFalse(oProvider.allow_user_interface)

        # Test unneeded PreData
        oProvider.pre_data = "Not Needed"
        Assert.assertEqual("Not Needed", oProvider.pre_data)
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderFixed)).exec()
        Assert.assertIsNotNone(oResult)
        Assert.assertFalse(oResult.message.is_failure)

        # Test without PreData
        oProvider.pre_data = ""
        Assert.assertEqual("", oProvider.pre_data)
        oResult = (clr.Convert(oProvider, DataProviderFixed)).exec()
        Assert.assertIsNotNone(oResult)
        Assert.assertFalse(oResult.message.is_failure)

        # Verifying random datasets and their values
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(3, oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(1, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("x", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(7689.837955, Math.Round(float(arValues[0]), 6))

        oDataSet = oResult.intervals[0].data_sets[2]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        Assert.assertEqual(1, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("z", oDataSet.element_name)
        Assert.assertEqual(26529.061236, Math.Round(float(arValues[0]), 6))

        del oResult
        TestBase.logger.WriteLine("----- FACILITY CARTESIAN POSITION TEST ----- END -----")

    # endregion

    # region SensorPatternIntersection
    def test_SensorPatternIntersection(self):
        # Running PatternIntersection report for a sensor using DataProviderTimeVarying.Exec
        TestBase.logger.WriteLine("----- SENSOR PATTERN INTERSECTION TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oSatellite: "IStkObject" = oScenario.children["Satellite1"]
        Assert.assertEqual(oScenario.children["Satellite1"], oSatellite)

        oSensor: "IStkObject" = oSatellite.children["Sensor1"]
        Assert.assertEqual(oSatellite.children["Sensor1"], oSensor)

        oProvider: "IDataProvider" = clr.Convert(oSensor.data_providers["Pattern Intersection"], IDataProvider)
        Assert.assertIsNotNone(oProvider)
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0
        )
        Assert.assertIsNotNone(oResult)

        # Verifying random datasets and their values
        Assert.assertEqual(16, oResult.sections.count)
        Assert.assertEqual(16, oResult.intervals.count)
        Assert.assertEqual((16 * 13), oResult.data_sets.count)
        Assert.assertEqual(91, oResult.intervals[0].data_sets[0].count)
        Assert.assertEqual("Latitude", oResult.intervals[0].data_sets[0].dimension_name)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        Assert.assertEqual("Latitude", oDataSet.element_name)
        Assert.assertEqual(1.079482, Math.Round(float(arValues[2]), 6))
        Assert.assertEqual(-1.003569, Math.Round(float(arValues[13]), 6))

        oDataSet = oResult.intervals[0].data_sets[3]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        Assert.assertEqual("CBF X", oDataSet.element_name)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual(2420.269347, Math.Round(float(arValues[2]), 6))
        Assert.assertEqual(2421.532535, Math.Round(float(arValues[13]), 6))

        del oResult
        TestBase.logger.WriteLine("----- SENSOR PATTERN INTERSECTION TEST ----- END -----")

    # endregion

    # region SatelliteBetaAngle
    def test_SatelliteBetaAngle(self):
        TestBase.logger.WriteLine("----- SATELLITE BETA ANGLE TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        Assert.assertEqual("EpSec", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))

        arStartTime = Array.CreateInstance(clr.TypeOf(object), 5)
        arStartTime[0] = 0
        arStartTime[1] = 2000
        arStartTime[2] = 500
        arStartTime[3] = 1000
        arStartTime[4] = 976

        arStopTime = Array.CreateInstance(clr.TypeOf(object), 5)
        arStopTime[0] = 90000
        arStopTime[1] = 87888
        arStopTime[2] = 99786
        arStopTime[3] = 100000
        arStopTime[4] = 94199

        # Verifying random datasets and their values
        oResult: "DataProviderResult" = (
            clr.Convert(
                (clr.Convert(TestBase.Application, IStkObject))
                .children[0]
                .children["Satellite1"]
                .data_providers["Beta Angle"],
                DataProviderTimeVarying,
            )
        ).exec(arStartTime, arStopTime, 998)
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(5, oResult.intervals.count)
        Assert.assertEqual((5 * 3), oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(88, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(4990, float(arValues[5]))
        Assert.assertEqual(85828, float(arValues[86]))

        oDataSet = oResult.intervals[0].data_sets[1]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual("Beta Angle", oDataSet.element_name)
        Assert.assertEqual(88, oDataSet.count)
        Assert.assertEqual("Angle", oDataSet.dimension_name)
        arValues = oDataSet.get_values()
        # Just check the first three decimal points to avoid
        # changing the unit test each time the underlying data is changed.
        Assert.assertAlmostEqual(-4.792449, float(arValues[0]), delta=Math2.Epsilon2)
        Assert.assertAlmostEqual(-4.793077, float(arValues[2]), delta=Math2.Epsilon2)

        oDataSet = oResult.intervals[2].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(88, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(5490, float(arValues[5]))
        Assert.assertEqual(85330, float(arValues[85]))

        oDataSet = oResult.intervals[2].data_sets[1]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual("Beta Angle", oDataSet.element_name)
        Assert.assertEqual(88, oDataSet.count)
        Assert.assertEqual("Angle", oDataSet.dimension_name)
        arValues = oDataSet.get_values()
        # Just check the first three decimal points to avoid
        # changing the unit test each time the underlying data is changed.
        Assert.assertAlmostEqual(-4.79260648978819, float(arValues[0]), delta=Math2.Epsilon2)
        Assert.assertAlmostEqual(-4.793236, float(arValues[2]), delta=Math2.Epsilon2)

        del oResult
        TestBase.logger.WriteLine("----- SATELLITE BETA ANGLE TEST ----- END -----")

    # endregion

    # region SatelliteArticulation
    @category("VO Tests")
    def test_SatelliteArticulation(self):
        # Running Articulation report for a satellite using DataProviderFixed.Exec
        TestBase.logger.WriteLine("----- SATELLITE ARTICULATION TEST ----- BEGIN -----")
        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oSatellite: "IStkObject" = oScenario.children["Satellite1"]
        Assert.assertEqual(oScenario.children["Satellite1"], oSatellite)

        oProvider: "IDataProvider" = clr.Convert(oSatellite.data_providers["Articulation"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        # Verifying random datasets and their values
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderFixed)).exec()
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(0, oResult.intervals.count)
        Assert.assertEqual(0, oResult.data_sets.count)
        Assert.assertEqual(1, oResult.message.count)

        oMessage: "DataProviderResultTextMessage" = oResult.message
        Assert.assertIsNotNone(oMessage)
        arValues = oMessage.messages
        Assert.assertEqual("Data Unavailable", clr.Convert(arValues[0], str))

        del oResult
        TestBase.logger.WriteLine("----- SATELLITE ARTICULATION TEST ----- END -----")

    # endregion

    # region SatelliteRICCoordinates
    def test_SatelliteRICCoordinates(self):
        num_RIC_datasets: int = 25

        TestBase.logger.WriteLine("----- SATELLITE RIC COORDINATES TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        Assert.assertEqual("EpSec", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))

        TestBase.logger.WriteLine("************************************************************************")
        TestBase.logger.WriteLine("This example demonstrates the usage of PreService For <RIC Coordinates>.")
        TestBase.logger.WriteLine("RIC Coordinates is a TimeVariant Satellite DataProvider, ")
        TestBase.logger.WriteLine("and therefore may be executed")
        TestBase.logger.WriteLine("for an interval, a list of intervals or single values of input data.")
        TestBase.logger.WriteLine("************************************************************************")

        oProviderInfo: "IDataProviderInfo" = clr.Convert(
            (clr.Convert(TestBase.Application, IStkObject))
            .children[0]
            .children["Satellite2"]
            .data_providers["RIC Coordinates"],
            IDataProviderInfo,
        )
        Assert.assertIsNotNone(oProviderInfo)
        TestBase.logger.WriteLine("Default Settings:")
        TestBase.logger.WriteLine5("RIC-Name: {0}", oProviderInfo.name)
        TestBase.logger.WriteLine4("RIC-IsGroup: {0}", oProviderInfo.is_group())
        TestBase.logger.WriteLine6("RIC-Type: {0}", oProviderInfo.type)
        TestBase.logger.WriteLine5("RIC-PreData: {0}", (clr.Convert(oProviderInfo, IDataProvider)).pre_data)
        TestBase.logger.WriteLine4("RIC-AllowUI: {0}", (clr.Convert(oProviderInfo, IDataProvider)).allow_user_interface)

        # Test missing PreData
        (clr.Convert(oProviderInfo, IDataProvider)).pre_data = ""
        oResult: "DataProviderResult" = (clr.Convert(oProviderInfo, DataProviderTimeVarying)).exec(0, 90000, 1000)
        Assert.assertIsNotNone(oResult)
        Assert.assertTrue(oResult.message.is_failure)
        Assert.assertEqual("Another vehicle must be selected in order to compute this data.", oResult.message[0])
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(0, oResult.intervals.count)
        Assert.assertEqual(0, oResult.data_sets.count)

        # Test invalid PreData
        (clr.Convert(oProviderInfo, IDataProvider)).pre_data = "Satellite/Bogus"
        oResult = (clr.Convert(oProviderInfo, DataProviderTimeVarying)).exec(0, 90000, 1000)
        Assert.assertIsNotNone(oResult)
        Assert.assertTrue(oResult.message.is_failure)
        Assert.assertEqual("Another vehicle must be selected in order to compute this data.", oResult.message[0])
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(0, oResult.intervals.count)
        Assert.assertEqual(0, oResult.data_sets.count)

        # Test valid PreData
        (clr.Convert(oProviderInfo, IDataProvider)).pre_data = "Satellite/Satellite1"

        TestBase.logger.WriteLine5("**** new RIC-PreData: {0}", (clr.Convert(oProviderInfo, IDataProvider)).pre_data)
        TestBase.logger.WriteLine4(
            "**** new RIC-AllowUI: {0}", (clr.Convert(oProviderInfo, IDataProvider)).allow_user_interface
        )
        TestBase.logger.WriteLine("This will run RIC Coordinates for an interval")

        # Verifying random datasets and their values
        oResult = (clr.Convert(oProviderInfo, DataProviderTimeVarying)).exec(0, 90000, 1000)
        Assert.assertIsNotNone(oResult)
        Assert.assertFalse(oResult.message.is_failure)
        Assert.assertEqual("OK", oResult.message[0])
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(num_RIC_datasets, oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(88, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(8000.0, float(arValues[8]))
        Assert.assertEqual(86400.0, float(arValues[87]))

        oDataSet = oResult.intervals[0].data_sets[3]
        arValues = oDataSet.get_values()
        Assert.assertEqual("Cross-Track", oDataSet.element_name)
        Assert.assertEqual(88, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)

        Assert.assertEqual(0.000164, Math.Round(float(arValues[0]), 6))

        Assert.assertEqual(Math.Round(-1738.526, 6), Math.Round(float(arValues[87]), 3))

        TestBase.logger.WriteLine("This will run RIC Coordinates for a list of interval input")

        arStartTime = Array.CreateInstance(clr.TypeOf(object), 5)
        arStartTime[0] = 0
        arStartTime[1] = 2000
        arStartTime[2] = 500
        arStartTime[2] = 1000
        arStartTime[3] = 976

        arStopTime = Array.CreateInstance(clr.TypeOf(object), 5)
        arStopTime[0] = 90000
        arStopTime[1] = 87888
        arStopTime[2] = 99786
        arStopTime[3] = 100000
        arStopTime[4] = 94199

        (clr.Convert(oProviderInfo, IDataProvider)).pre_data = "Satellite/Satellite1"
        oResult = (clr.Convert(oProviderInfo, DataProviderTimeVarying)).exec(arStartTime, arStopTime, 887)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(5, oResult.intervals.count)
        Assert.assertEqual((5 * num_RIC_datasets), oResult.data_sets.count)

        oDataSet = oResult.intervals[0].data_sets[0]
        arValues = oDataSet.get_values()
        Assert.assertEqual(99, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        Assert.assertEqual(4435.0, float(arValues[5]))
        Assert.assertEqual(86039.0, float(arValues[97]))

        oDataSet = oResult.intervals[0].data_sets[2]
        arValues = oDataSet.get_values()
        Assert.assertEqual("In-Track", oDataSet.element_name)
        Assert.assertEqual(99, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual(3313.669838, Math.Round(float(arValues[0]), 6))
        Assert.assertEqual(133.271, Math.Round(float(arValues[6]), 3))

        del oResult
        TestBase.logger.WriteLine("----- SATELLITE RIC COORDINATES TEST ----- END -----")

    # endregion

    # region SatelliteCartPosFixedElements
    def test_SatelliteCartPosFixedElements(self):
        # Runs Cartesian Position//Fixed Data Provider for a satellite using DataProviderTimeVarying.ExecElements
        TestBase.logger.WriteLine("----- SATELLITE CARTESIAN POSITION FIXED ELEMENTS TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oSatellite: "IStkObject" = oScenario.children["Satellite1"]
        Assert.assertEqual(oScenario.children["Satellite1"], oSatellite)

        oGroup: "DataProviderGroup" = clr.Convert(oSatellite.data_providers["Cartesian Position"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        temp = ["Time", "y"]
        with pytest.raises(Exception):
            (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements(
                "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 0, temp
            )

        arStartTime = Array.CreateInstance(clr.TypeOf(object), 1)
        arStartTime[0] = 0
        arStopTime = Array.CreateInstance(clr.TypeOf(object), 1)
        arStopTime[0] = 90000

        with pytest.raises(Exception):
            (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements(arStartTime, arStopTime, 0, temp)

        with pytest.raises(Exception):
            (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements(
                "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", -1, temp
            )

        # Verifying random datasets and their values
        arCols = ["Time", "y"]

        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0, arCols
        )

        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(2, oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(16, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual("1 Jun 2004 12:04:00.000000000", clr.Convert(arValues[1], str))
        Assert.assertEqual("1 Jun 2004 12:16:00.000000000", clr.Convert(arValues[4], str))

        oDataSet = oResult.intervals[0].data_sets[1]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(16, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("y", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(-6285.353143, Math.Round(float(arValues[0]), 6))
        Assert.assertEqual(5609.665723, Math.Round(float(arValues[13]), 6))

        del oResult
        TestBase.logger.WriteLine("----- SATELLITE CARTESIAN POSITION FIXED ELEMENTS TEST ----- END -----")

    # endregion

    # region SatelliteCartPosFixedElementsUsingDefault
    def test_SatelliteCartPosFixedElementsUsingDefault(self):
        # Runs Cartesian Position//Fixed Data Provider for a satellite using DataProviderTimeVarying.ExecElements
        TestBase.logger.WriteLine("----- SATELLITE CARTESIAN POSITION FIXED ELEMENTS TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oSatellite: "IStkObject" = oScenario.children["Satellite1"]
        Assert.assertEqual(oScenario.children["Satellite1"], oSatellite)

        oGroup: "DataProviderGroup" = clr.Convert(oSatellite.data_providers["Cartesian Position"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        arStartTime = Array.CreateInstance(clr.TypeOf(object), 1)
        arStartTime[0] = 0
        arStopTime = Array.CreateInstance(clr.TypeOf(object), 1)
        arStopTime[0] = 90000
        temp = ["Time", "y"]
        with pytest.raises(Exception):
            (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements_native_times(arStartTime, arStopTime, temp)

        # Verifying random datasets and their values
        arCols = ["Time", "y"]

        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements_native_times(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", arCols
        )
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(2, oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(61, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual("1 Jun 2004 12:01:00.000000000", clr.Convert(arValues[1], str))
        Assert.assertEqual("1 Jun 2004 12:04:00.000000000", clr.Convert(arValues[4], str))

        oDataSet = oResult.intervals[0].data_sets[1]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(61, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("y", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(-6285.353143, Math.Round(float(arValues[0]), 6))
        Assert.assertEqual(-2660.314094, Math.Round(float(arValues[13]), 6))

        del oResult
        TestBase.logger.WriteLine("----- SATELLITE CARTESIAN POSITION FIXED ELEMENTS TEST ----- END -----")

    # endregion

    # region AircraftCartPosFixedElementsUsingDefault
    def test_AircraftCartPosFixedElementsUsingDefault(self):
        # Runs Cartesian Position//Fixed Data Provider for a satellite using DataProviderTimeVarying.ExecElements
        TestBase.logger.WriteLine("----- Aircraft CARTESIAN POSITION FIXED ELEMENTS TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oAir: "IStkObject" = oScenario.children["a340"]
        Assert.assertEqual(oScenario.children["a340"], oAir)

        oGroup: "DataProviderGroup" = clr.Convert(oAir.data_providers["Cartesian Position"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Fixed"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        arStartTime = Array.CreateInstance(clr.TypeOf(object), 1)
        arStartTime[0] = 0
        arStopTime = Array.CreateInstance(clr.TypeOf(object), 1)
        arStopTime[0] = 90000
        temp = ["Time", "y"]
        with pytest.raises(Exception):
            (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements_native_times(arStartTime, arStopTime, temp)

        # Verifying random datasets and their values
        arCols = ["Time", "y"]

        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements_native_times(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", arCols
        )
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(2, oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        # logger.WriteLine("\tThe Intervals[0].DataSets[0] contains: {0} values", oDataSet.Count);
        Assert.assertEqual(199, oDataSet.count)
        Assert.assertEqual("Date", oDataSet.dimension_name)
        Assert.assertEqual("Time", oDataSet.element_name)
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", clr.Convert(arValues[0], str))
        Assert.assertEqual("1 Jun 2004 12:00:19.531224281", clr.Convert(arValues[1], str))
        Assert.assertEqual("1 Jun 2004 12:00:35.335125888", clr.Convert(arValues[2], str))
        Assert.assertEqual("1 Jun 2004 12:00:52.900970419", clr.Convert(arValues[3], str))
        Assert.assertEqual("1 Jun 2004 12:00:56.812066962", clr.Convert(arValues[4], str))
        Assert.assertEqual("1 Jun 2004 12:01:30.188313568", clr.Convert(arValues[8], str))
        Assert.assertEqual("1 Jun 2004 12:01:35.887349506", clr.Convert(arValues[9], str))
        Assert.assertEqual("1 Jun 2004 12:05:01.726211163", clr.Convert(arValues[19], str))

        oDataSet = oResult.intervals[0].data_sets[1]
        Assert.assertIsNotNone(oDataSet)
        arValues = oDataSet.get_values()
        Assert.assertEqual(199, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("y", oDataSet.element_name)
        Assert.assertEqual(24.44683, Math.Round(float(arValues[0]), 6))
        Assert.assertEqual(40.338076, Math.Round(float(arValues[13]), 6))

        del oResult
        TestBase.logger.WriteLine("----- Aircraft CARTESIAN POSITION FIXED ELEMENTS TEST ----- END -----")

    # endregion

    # region AreaTargetAreaGroupElements
    def test_AreaTargetAreaGroupElements(self):
        TestBase.logger.WriteLine("----- AREATARGET AREA GROUP ELEMENTS TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", "mi")

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oAreaTarget: "IStkObject" = oScenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget1")
        Assert.assertEqual(oScenario.children["AreaTarget1"], oAreaTarget)

        oAT: "AreaTarget" = clr.Convert(oScenario.children["AreaTarget1"], AreaTarget)
        oAT.area_type = AREA_TYPE.ELLIPSE
        ellipseData: "AreaTypeEllipse" = clr.Convert(oAT.area_type_data, AreaTypeEllipse)
        ellipseData.semi_minor_axis = 150
        ellipseData.semi_major_axis = 300
        ellipseData.bearing = 0.0

        oProviderGroup: "DataProviderGroup" = clr.Convert(
            oAreaTarget.data_providers["Bounding Rectangle"], DataProviderGroup
        )
        oProvider: "IDataProvider" = clr.Convert(oProviderGroup.group["Geometry"], IDataProvider)

        arCols = ["Area"]
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderFixed)).exec_elements(arCols)

        # Verifying random datasets and their values
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(1, oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(1, oDataSet.count)
        Assert.assertEqual("Area", oDataSet.dimension_name)
        Assert.assertEqual("Area", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertAlmostEqual(179781.7194, float(arValues[0]), delta=0.01)  # tolerance is 100 cm^2

        del oResult
        TestBase.logger.WriteLine("----- AREATARGET AREA GROUP ELEMENTS TEST ----- END -----")

    # endregion

    # region FacilityCartPosElements
    def test_FacilityCartPosElements(self):
        # Running Cartesian Position for a facility using DataProviderFixed.ExecElements
        TestBase.logger.WriteLine("----- FACILITY CARTESIAN POSITION ELEMENTS TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", "mi")

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oFacility: "IStkObject" = oScenario.children["Facility1"]
        Assert.assertEqual(oScenario.children["Facility1"], oFacility)

        oProvider: "IDataProvider" = clr.Convert(oFacility.data_providers["Cartesian Position"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        # Verifying random datasets and their values
        arCols = ["x", "z"]
        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderFixed)).exec_elements(arCols)
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(2, oResult.data_sets.count)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(1, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("x", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(7689.837955, Math.Round(float(arValues[0]), 6))

        oDataSet = oResult.intervals[0].data_sets[1]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual(1, oDataSet.count)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual("z", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(26529.061236, Math.Round(float(arValues[0]), 6))

        del oResult
        TestBase.logger.WriteLine("----- FACILITY CARTESIAN POSITION ELEMENTS TEST ----- END -----")

    # endregion

    # region FacilityLightingTimesElements
    def test_FacilityLightingTimesElements(self):
        # Running Lighting Times//Sunlight for a facility using DataProviderInterval.ExecElements
        TestBase.logger.WriteLine("----- FACILITY LIGHTING TIMES ELEMENTS TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")
        Assert.assertEqual("deg", TestBase.Application.unit_preferences.get_current_unit_abbrv("AngleUnit"))
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oFacility: "IStkObject" = oScenario.children["Facility1"]
        Assert.assertEqual(oScenario.children["Facility1"], oFacility)

        oGroup: "DataProviderGroup" = clr.Convert(oFacility.data_providers["Lighting Times"], DataProviderGroup)
        Assert.assertIsNotNone(oGroup)

        oProvider: "IDataProvider" = clr.Convert(oGroup.group["Sunlight"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        # Verifying random datasets and their values
        arCols = ["Start Time", "Stop Time", "Duration"]

        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderInterval)).exec_elements(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", arCols
        )
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(0, oResult.sections.count)
        Assert.assertEqual(1, oResult.intervals.count)
        Assert.assertEqual(3, oResult.data_sets.count)
        Assert.assertEqual(1, oResult.intervals[0].data_sets[0].count)
        Assert.assertEqual("Date", oResult.intervals[0].data_sets[0].dimension_name)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertIsNotNone(oDataSet)
        Assert.assertEqual("Start Time", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", clr.Convert(arValues[0], str))

        oDataSet = oResult.intervals[0].data_sets[1]
        arValues = oDataSet.get_values()
        Assert.assertEqual("Stop Time", oDataSet.element_name)
        Assert.assertEqual("1 Jun 2004 13:00:00.000000000", clr.Convert(arValues[0], str))

        oDataSet = oResult.intervals[0].data_sets[2]
        arValues = oDataSet.get_values()
        Assert.assertEqual("Duration", oDataSet.element_name)
        Assert.assertEqual(3600.0, float(arValues[0]))

        del oResult
        TestBase.logger.WriteLine("----- FACILITY LIGHTING TIMES ELEMENTS TEST ----- END -----")

    # endregion

    # region SensorPatternIntersectionElements
    def test_SensorPatternIntersectionElements(self):
        # Running PatternIntersection report for a sensor using DataProviderTimeVarying.ExecElements
        TestBase.logger.WriteLine("----- SENSOR PATTERN INTERSECTION ELEMENTS TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertEqual("sec", TestBase.Application.unit_preferences.get_current_unit_abbrv("TimeUnit"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        Assert.assertEqual("UTCG", TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat"))

        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oSatellite: "IStkObject" = oScenario.children["Satellite1"]
        Assert.assertEqual(oScenario.children["Satellite1"], oSatellite)

        oSensor: "IStkObject" = oSatellite.children["Sensor1"]
        Assert.assertEqual(oSatellite.children["Sensor1"], oSensor)

        oProvider: "IDataProvider" = clr.Convert(oSensor.data_providers["Pattern Intersection"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        # Verifying random datasets and their values
        arCols = ["Latitude", "CBF X"]

        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec_elements(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0, arCols
        )
        Assert.assertIsNotNone(oResult)
        Assert.assertEqual(16, oResult.sections.count)
        Assert.assertEqual(16, oResult.intervals.count)
        Assert.assertEqual((16 * 2), oResult.data_sets.count)
        Assert.assertEqual(91, oResult.intervals[0].data_sets[0].count)
        Assert.assertEqual("Latitude", oResult.intervals[0].data_sets[0].dimension_name)

        oDataSet: "DataProviderResultDataSet" = oResult.intervals[0].data_sets[0]
        Assert.assertEqual("Latitude", oDataSet.element_name)
        arValues = oDataSet.get_values()
        Assert.assertEqual(1.079482, Math.Round(float(arValues[2]), 6))
        Assert.assertEqual(-1.003569, Math.Round(float(arValues[13]), 6))

        oDataSet = oResult.intervals[0].data_sets[1]
        arValues = oDataSet.get_values()
        Assert.assertEqual("CBF X", oDataSet.element_name)
        Assert.assertEqual("Distance", oDataSet.dimension_name)
        Assert.assertEqual(2420.269347, Math.Round(float(arValues[2]), 6))
        Assert.assertEqual(2421.532535, Math.Round(float(arValues[13]), 6))

        del oResult
        TestBase.logger.WriteLine("----- SENSOR PATTERN INTERSECTION ELEMENTS TEST ----- END -----")

    # endregion

    # region TestElements
    def test_TestElements(self):
        TestBase.logger.WriteLine("----- ELEMENTS TEST ----- BEGIN -----")
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        Assert.assertIsNotNone(oSatellite)

        # Active Constraints
        oInfo: "IDataProviderInfo" = oSatellite.data_providers["Active Constraints"]
        Assert.assertIsNotNone(oInfo)
        # logger.WriteLine("\tName = {0}, Type = {1}, IsGroup = {2}",
        # 	oInfo.Name, oInfo.Type, oInfo.IsGroup());
        Assert.assertFalse(oInfo.is_group())

        oProvider: "IDataProvider" = clr.Convert(oInfo, IDataProvider)
        Assert.assertIsNotNone(oProvider)
        Assert.assertEqual(6, oProvider.elements.count)
        Assert.assertEqual("Constraint", oProvider.elements[0].name)
        Assert.assertEqual("Value", oProvider.elements[1].name)
        Assert.assertEqual("Value with Units", oProvider.elements[2].name)
        Assert.assertEqual("Action", oProvider.elements[3].name)
        Assert.assertEqual("Max Time Step", oProvider.elements[4].name)
        Assert.assertEqual("Max Relative Motion", oProvider.elements[5].name)

        iIndex: int = 0
        while iIndex < oProvider.elements.count:
            pass

            iIndex += 1

        # Lighting AER
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oInfo = oFacility.data_providers["Lighting AER"]
        Assert.assertIsNotNone(oInfo)
        # logger.WriteLine("\tName = {0}, Type = {1}, IsGroup = {2}",
        # 	oInfo.Name, oInfo.Type, oInfo.IsGroup());
        oProvider = clr.Convert(oInfo, IDataProvider)
        Assert.assertIsNotNone(oProvider)
        Assert.assertEqual(4, oProvider.elements.count)
        Assert.assertEqual("Time", oProvider.elements[0].name)
        Assert.assertEqual("Azimuth", oProvider.elements[1].name)
        Assert.assertEqual("Elevation", oProvider.elements[2].name)
        Assert.assertEqual("Range", oProvider.elements[3].name)

        iIndex: int = 0
        while iIndex < oProvider.elements.count:
            pass

            iIndex += 1

        # Lighting Times
        oInfo = oSatellite.data_providers["Lighting Times"]
        Assert.assertIsNotNone(oInfo)
        # logger.WriteLine("\tName = {0}, Type = {1}, IsGroup = {2}", oInfo.Name, oInfo.Type, oInfo.IsGroup());
        Assert.assertTrue(oInfo.is_group())
        oGroup: "DataProviderGroup" = clr.Convert(oInfo, DataProviderGroup)
        Assert.assertEqual(6, oGroup.group.count)

        iIndex: int = 0
        while iIndex < oGroup.group.count:
            # logger.WriteLine("\t\t\tGroup {0}: Name = {1}, Type = {2}, IsGroup = {3}", iIndex,
            # 	oGroup.Group[iIndex].Name, oGroup.Group[iIndex].Type, oGroup.Group[iIndex].IsGroup() );
            oProvider = clr.Convert(oGroup.group[iIndex], IDataProvider)
            Assert.assertIsNotNone(oProvider)

            i: int = 0
            while i < oProvider.elements.count:
                pass

                i += 1

            iIndex += 1

        Assert.assertEqual("Sunlight", oGroup.group[0].name)

        dateDataPrv: "IDataProvider" = clr.Convert(oGroup.group[1], IDataProvider)
        Assert.assertEqual("Date", dateDataPrv.elements[0].dimension_name)

        realDataPrv: "IDataProvider" = clr.Convert(oGroup.group[3], IDataProvider)
        Assert.assertEqual(DATA_PROVIDER_ELEMENT_TYPE.REAL, realDataPrv.elements[2].type)
        TestBase.logger.WriteLine("----- ELEMENTS TEST ----- END -----")

    # endregion

    # region TestExecMethod
    def test_TestExecMethod(self):
        TestBase.logger.WriteLine("----- EXEC METHOD TEST ----- BEGIN -----")
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")

        dtStart: typing.Any = "1 Jun 2004 12:00:00.00"
        dtStop: typing.Any = "1 Jun 2004 13:00:00.00"

        oGroup: "DataProviderGroup" = clr.CastAs(
            (clr.Convert(TestBase.Application, IStkObject))
            .children["DataProvidersTests"]
            .children["Satellite1"]
            .data_providers["Cartesian Position"],
            DataProviderGroup,
        )
        Assert.assertIsNotNone(oGroup)
        oTimeVar: "DataProviderTimeVarying" = clr.CastAs(oGroup.group["Fixed"], DataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult: "DataProviderResult" = oTimeVar.exec(dtStart, dtStop, 240.0)
        Assert.assertIsNotNone(oResult)

        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")

        oObject: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children[0].children["Satellite1"]
        Assert.assertIsNotNone(oObject)
        oDataProvider: "IDataProvider" = clr.Convert(oObject.data_providers["Beta Angle"], IDataProvider)
        Assert.assertIsNotNone(oDataProvider)
        oTimeVar = clr.CastAs(oDataProvider, DataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = oTimeVar.exec([0, 2000, 500, 1000, 976], [90000, 87888, 99786, 1000000, 94199], 998)
        Assert.assertIsNotNone(oResult)

        with pytest.raises(Exception):
            oTimeVar.exec([0, 2000, 500, 1000, 976], 1000000, 998)

        with pytest.raises(Exception):
            oTimeVar.exec(0, [90000, 87888, 99786, 1000000, 94199], 998)

        oScenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)
        Assert.assertIsNotNone(oScenario)
        oDataProvider = clr.Convert(oObject.data_providers["Available Times"], IDataProvider)
        Assert.assertIsNotNone(oDataProvider)
        oInterval: "DataProviderInterval" = clr.Convert(oDataProvider, DataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = oInterval.exec(oScenario.start_time, oScenario.stop_time)
        Assert.assertIsNotNone(oResult)

        with pytest.raises(Exception):
            oInterval.exec([0, 2000, 500, 1000, 976], 1000000)

        with pytest.raises(Exception):
            oInterval.exec(0, [0, 2000, 500, 1000, 976])

        TestBase.logger.WriteLine("----- EXEC METHOD TEST ----- END -----")

    # endregion

    # region ObjectCoverage
    def test_ObjectCoverage(self):
        oScenario: "IStkObject" = (clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"]
        Assert.assertEqual((clr.Convert(TestBase.Application, IStkObject)).children["DataProvidersTests"], oScenario)

        oAircraft: "IStkObject" = oScenario.children["a340"]
        Assert.assertEqual(oScenario.children["a340"], oAircraft)
        # Assign the gps constellation as the asset for the a340 single object coverage calculation.
        # Assert.IsNotNull(Application.ExecuteCommand("Cov */Aircraft/a340 Asset */Constellation/gps_const Assign"));

        # Set the a340 single object coverage calculation figure of merrit to use GDOP.
        # Note: 1.0 second is currently the smallest time increment that can be used here.
        oObjectCoverage: "StkObjectCoverage" = oAircraft.object_coverage
        oObjectCoverage.clear()
        Assert.assertIsNotNone(oObjectCoverage)
        oObjectCoverage.assets.add("Constellation/gps_const")

        oObjectCoverage.figure_of_merit.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.DILUTION_OF_PRECISION)
        dop: "IFigureOfMeritDefinitionDilutionOfPrecision" = clr.CastAs(
            oObjectCoverage.figure_of_merit.definition, IFigureOfMeritDefinitionDilutionOfPrecision
        )
        dop.set_type(FIGURE_OF_MERIT_COMPUTE_TYPE.OVER_DETERMINED)
        dop.set_compute_type(FIGURE_OF_MERIT_COMPUTE.MAXIMUM)
        dop.set_method(FIGURE_OF_MERIT_METHOD.GDOP)
        dop.time_step = 600
        oObjectCoverage.compute()

        oProvider: "IDataProvider" = clr.Convert(oObjectCoverage.data_providers["FOM by Time"], IDataProvider)
        Assert.assertIsNotNone(oProvider)

        oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 1
        )
        Assert.assertIsNotNone(oResult)

        tu: typing.Any = oResult.value
        col: "DataProviderResultSubSectionCollection" = clr.Convert(tu, DataProviderResultSubSectionCollection)

        oSection: "DataProviderResultSubSection"

        for oSection in col:
            oCollection: "DataProviderResultIntervalCollection" = clr.Convert(
                oSection.intervals, DataProviderResultIntervalCollection
            )
            Assert.assertEqual(clr.Convert(oSection.intervals, DataProviderResultIntervalCollection), oCollection)

            oInterval: "DataProviderResultInterval" = oCollection[0]
            Assert.assertEqual(oCollection[0], oInterval)

            Assert.assertEqual("11 Jun 2004 12:33:44.5-1", self.DumpRawCrossingData(oInterval, 1.0))
            Assert.assertEqual("21 Jun 2004 12:33:44.5-1", self.DumpRawCrossingData(oInterval, 2.0))
            Assert.assertEqual("31 Jun 2004 12:33:44.5-1", self.DumpRawCrossingData(oInterval, 3.0))
            Assert.assertEqual("4", self.DumpRawCrossingData(oInterval, 4.0))
            Assert.assertEqual("5", self.DumpRawCrossingData(oInterval, 5.0))

            arBoundaries = [1.0, 2.0, 3.0, 4.0, 5.0]
            arRanges = oInterval.multiple_threshold_crossings("FOM Value", arBoundaries)
            outStr: str = ""

            iRange: int = 0
            while iRange < len(arRanges):
                TestBase.logger.Write3("\nRange: {0}\n", iRange)
                outStr += str(iRange) + "#"

                arTimeSpans = arRanges[iRange]

                iSpan: int = 0
                while iSpan < len(arTimeSpans):
                    strStart: str = str(arTimeSpans[iSpan][0])
                    Assert.assertEqual(str(arTimeSpans[iSpan][0]), strStart)
                    strStop: str = str(arTimeSpans[iSpan][1])
                    Assert.assertEqual(str(arTimeSpans[iSpan][1]), strStop)

                    # Console.WriteLine("Start: {0}	Stop: {1}\n", strStart, strStop);
                    # Start: 1 Jun 2004 12:52:46.038708817	Stop: 1 Jun 2004 13:00:00.000000000
                    # Start: 1 Jun 2004 12:00:00.000000000	Stop: 1 Jun 2004 12:05:23.937332035
                    # Start: 1 Jun 2004 12:34:51.826911345	Stop: 1 Jun 2004 12:52:46.038708817
                    # Start: 1 Jun 2004 12:05:23.937332035	Stop: 1 Jun 2004 12:05:23.938821071
                    # Start: 1 Jun 2004 12:17:03.619606475	Stop: 1 Jun 2004 12:34:51.826911345
                    # Start: 1 Jun 2004 12:05:23.938821071	Stop: 1 Jun 2004 12:17:03.619606475
                    strStartTrunc: str = strStart[0 : (0 + 22)]  # trunc to 2 dec places
                    strStopTrunc: str = strStart[0 : (0 + 22)]  # trunc to 2 dec places
                    outStr += ((strStartTrunc + "#") + strStopTrunc) + "#"

                    iSpan += 1

                iRange += 1

            Assert.assertEqual(
                "0#1#1 Jun 2004 12:33:44.55#1 Jun 2004 12:33:44.55#1 Jun 2004 12:33:44.55#1 Jun 2004 12:33:44.55#2#1 Jun 2004 12:33:44.55#1 Jun 2004 12:33:44.55#3#1 Jun 2004 12:00:00.00#1 Jun 2004 12:00:00.00#4#5#",
                outStr,
            )

    # endregion

    # region TestElementPastNames
    def test_TestElementPastNames(self):
        scenObj: "IStkObject" = TestBase.Application.current_scenario
        scenChildren: "IStkObjectCollection" = scenObj.children
        satObj: "IStkObject" = scenChildren["Satellite1"]
        satChildren: "IStkObjectCollection" = satObj.children
        recObj: "IStkObject" = satChildren["Receiver1"]

        recDP: "IDataProvider" = clr.CastAs(recObj.data_providers["Basic Properties"], IDataProvider)
        Assert.assertIsNotNone(recDP)

        element: "DataProviderElement" = recDP.elements["g/T"]
        Assert.assertIsNotNone(element)

        element = recDP.elements["g Over T"]  # Past name for g/T
        Assert.assertIsNotNone(element)

        recFixedPrv: "DataProviderFixed" = clr.CastAs(recDP, DataProviderFixed)
        Assert.assertIsNotNone(recFixedPrv)

        elems = ["g/T"]
        result: "DataProviderResult" = recFixedPrv.exec_elements(elems)
        Assert.assertIsNotNone(result)

        elemNames = result.data_sets.element_names
        Assert.assertEqual(1, Array.Length(elemNames))
        Assert.assertEqual("g/T", clr.Convert(elemNames[0], str))

        Assert.assertEqual(1, result.data_sets.count)
        ds: "DataProviderResultDataSet" = result.data_sets[0]
        Assert.assertIsNotNone(ds)

        Assert.assertEqual("g/T", ds.element_name)
        Assert.assertEqual("GainTempRatio", ds.dimension_name)  # AgCGainNoiseTempRatio

        vals = ds.get_values()
        Assert.assertEqual(1, Array.Length(vals))

        val: float = Convert.ToDouble(vals[0])
        Assert.assertEqual(20.0, val)

        elems = ["g Over T"]
        result = recFixedPrv.exec_elements(elems)
        Assert.assertIsNotNone(result)

        elemNames = result.data_sets.element_names
        Assert.assertEqual(1, Array.Length(elemNames))
        Assert.assertEqual("g Over T", clr.Convert(elemNames[0], str))

        Assert.assertEqual(1, result.data_sets.count)
        ds = result.data_sets[0]
        Assert.assertIsNotNone(ds)

        Assert.assertEqual("g Over T", ds.element_name)
        Assert.assertEqual("Unitless", ds.dimension_name)  # AgCUnitless

        vals = ds.get_values()
        Assert.assertEqual(1, Array.Length(vals))

        val = Convert.ToDouble(vals[0])
        Assert.assertEqual(20.0, val)

    # endregion

    def test_TestAllDataProviders(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Test")
        scene: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)
        scene.set_time_period("1 Jul 2008 12:00:00.000", "2 Jul 2008 12:00:00.000")
        fac: "IStkObject" = None
        fac = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "Facility1")
        self.RunAllDataProviders(fac)
        sat: "Satellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1"), Satellite
        )
        twoBody: "VehiclePropagatorTwoBody" = clr.Convert(sat.propagator, VehiclePropagatorTwoBody)
        twoBody.ephemeris_interval.set_explicit_interval("1 Jul 2008 12:00:00.000", "2 Jul 2008 12:00:00.000")
        twoBody.propagate()
        self.RunAllDataProviders(clr.Convert(sat, IStkObject))
        self.RunAllDataProviders(TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.ADV_CAT, "AdvCat1"))
        ac: "Aircraft" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "Aircraft1"), Aircraft
        )
        self.GenerateGreatArcVeh(clr.Convert(ac.route, VehiclePropagatorGreatArc))
        self.RunAllDataProviders(clr.Convert(ac, IStkObject))
        self.RunAllDataProviders((clr.Convert(sat, IStkObject)).children.new(STK_OBJECT_TYPE.ANTENNA, "Antenna1"))
        at: "AreaTarget" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget1"), AreaTarget
        )
        at.area_type = AREA_TYPE.ELLIPSE
        self.RunAllDataProviders(clr.Convert(at, IStkObject))
        attCov: "IStkObject" = (clr.Convert(sat, IStkObject)).children.new(
            STK_OBJECT_TYPE.ATTITUDE_COVERAGE, "AttitudeCoverage1"
        )
        self.RunAllDataProviders(attCov)
        self.RunAllDataProviders(attCov.children.new(STK_OBJECT_TYPE.ATTITUDE_FIGURE_OF_MERIT, "AttitudeFOM1"))
        chain: "Chain" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.CHAIN, "Chain1"), Chain
        )
        chain.objects.add_object(clr.Convert(sat, IStkObject))
        chain.objects.add_object(clr.Convert(ac, IStkObject))
        self.RunAllDataProviders(clr.Convert(chain, IStkObject))
        constellation: "Constellation" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.CONSTELLATION, "Constellation1"),
            Constellation,
        )
        constellation.objects.add_object(clr.Convert(sat, IStkObject))
        self.RunAllDataProviders(clr.Convert(constellation, IStkObject))
        covDef: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef1"
        )
        self.RunAllDataProviders(covDef)
        self.RunAllDataProviders(covDef.children.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, "FOM1"))
        gv: "GroundVehicle" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "GroundVehicle1"),
            GroundVehicle,
        )
        self.GenerateGreatArcVeh(clr.Convert(gv.route, VehiclePropagatorGreatArc))
        self.RunAllDataProviders(clr.Convert(gv, IStkObject))
        lv: "LaunchVehicle" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "LaunchVehicle1"),
            LaunchVehicle,
        )
        ascent: "VehiclePropagatorSimpleAscent" = clr.Convert(lv.trajectory, VehiclePropagatorSimpleAscent)
        ascent.propagate()
        self.RunAllDataProviders(clr.Convert(lv, IStkObject))
        lt: "LineTarget" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.LINE_TARGET, "LineTarget1"), LineTarget
        )
        lt.points.add(0, 0)
        lt.points.add(10, 10)
        lt.points.anchor_point = 0
        self.RunAllDataProviders(clr.Convert(lt, IStkObject))
        missile: "Missile" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile1"), Missile
        )
        ballistic: "VehiclePropagatorBallistic" = clr.Convert(missile.trajectory, VehiclePropagatorBallistic)
        ballistic.propagate()
        self.RunAllDataProviders(clr.Convert(missile, IStkObject))
        self.RunAllDataProviders(TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.PLANET, "Planet1"))
        self.RunAllDataProviders((clr.Convert(sat, IStkObject)).children.new(STK_OBJECT_TYPE.RADAR, "Radar1"))
        self.RunAllDataProviders((clr.Convert(sat, IStkObject)).children.new(STK_OBJECT_TYPE.RECEIVER, "Receiver1"))
        self.RunAllDataProviders((clr.Convert(sat, IStkObject)).children.new(STK_OBJECT_TYPE.SENSOR, "Sensor1"))
        ship: "Ship" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, "Ship1"), Ship
        )
        self.GenerateGreatArcVeh(clr.Convert(ship.route, VehiclePropagatorGreatArc))
        self.RunAllDataProviders(clr.Convert(ship, IStkObject))
        self.RunAllDataProviders(TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.STAR, "Star1"))
        self.RunAllDataProviders(TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.TARGET, "Target1"))
        self.RunAllDataProviders(
            (clr.Convert(sat, IStkObject)).children.new(STK_OBJECT_TYPE.TRANSMITTER, "Transmitter1")
        )
        self.RunAllDataProviders(fac.children.new(STK_OBJECT_TYPE.TRANSMITTER, "Transmitter1"))
        access: "StkAccess" = (clr.Convert(sat, IStkObject)).get_access("Facility/Facility1")
        access.compute_access()
        self.ExecDataProviders(access.data_providers, "")
        coverage: "StkObjectCoverage" = (clr.Convert(sat, IStkObject)).object_coverage
        coverage.assets.add("Facility/Facility1")
        coverage.compute()
        self.ExecDataProviders(coverage.data_providers, "")
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    def GenerateGreatArcVeh(self, ga: "VehiclePropagatorGreatArc"):
        ga.method = VEHICLE_WAYPOINT_COMP_METHOD.DETERMINE_VEL_FROM_TIME
        elem: "VehicleWaypointsElement" = ga.waypoints.add()
        elem.latitude = 0
        elem.longitude = 0
        elem.altitude = 1
        elem.time = "1 Jul 2008 12:00:00.000"
        elem = ga.waypoints.add()
        elem.latitude = 2
        elem.longitude = 60
        elem.time = "1 Jul 2008 14:00:00.000"
        ga.propagate()

    # region IAgDataPrvInterval_SmartIntervals
    def test_IAgDataPrvInterval_SmartIntervals(self):
        TestBase.logger.WriteLine("----- DataProviderInterval_SmartIntervals ----- BEGIN -----")
        TestBase.Application.unit_preferences.reset_units()

        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        oScenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)

        startTime: typing.Any = (clr.Convert(TestBase.Application.current_scenario, Scenario)).start_time
        stopTime: typing.Any = (clr.Convert(TestBase.Application.current_scenario, Scenario)).stop_time
        startEpoch: "TimeToolEventSmartEpoch" = (
            TestBase.Application.current_scenario.vgt.events.factory.create_smart_epoch_from_time(startTime)
        )
        stopEpoch: "TimeToolEventSmartEpoch" = (
            TestBase.Application.current_scenario.vgt.events.factory.create_smart_epoch_from_time(stopTime)
        )
        oScenario.analysis_interval.set_start_and_stop_epochs(startEpoch, stopEpoch)

        oInterval: "DataProviderInterval" = clr.CastAs(
            clr.Convert(oSa.data_providers["Available Times"], IDataProvider), DataProviderInterval
        )

        oResult: "DataProviderResult" = oInterval.exec(
            oScenario.analysis_interval.get_start_epoch(), oScenario.analysis_interval.get_stop_epoch()
        )
        Assert.assertIsNotNone(oResult)
        oList: "DataProviderResultIntervalCollection" = oResult.intervals
        Assert.assertIsNotNone(oList)
        drInterval: "DataProviderResultInterval"
        for drInterval in oList:
            drDataSet: "DataProviderResultDataSet" = drInterval.data_sets[0]
            Assert.assertIsNotNone(drDataSet)
            if drDataSet.element_name == "Start Time":
                strTime: str = clr.Convert(drDataSet.get_values()[0], str)
                Assert.assertEqual("1 Jun 2004 12:00:00.000000000", strTime)

            drDataSet = drInterval.data_sets[1]
            Assert.assertIsNotNone(drDataSet)
            if drDataSet.element_name == "Stop Time":
                strTime: str = clr.Convert(drDataSet.get_values()[0], str)
                Assert.assertEqual("2 Jun 2004 12:00:00.000000000", strTime)

        arFields = ["Start Time", "Stop Time"]

        oResult = oInterval.exec_elements(
            oScenario.analysis_interval.get_start_epoch(), oScenario.analysis_interval.get_stop_epoch(), arFields
        )

        Assert.assertIsNotNone(oResult)
        oList = oResult.intervals
        Assert.assertIsNotNone(oList)
        drInterval: "DataProviderResultInterval"
        for drInterval in oList:
            oDataSet: "DataProviderResultDataSet" = drInterval.data_sets[0]
            Assert.assertIsNotNone(oDataSet)
            if oDataSet.element_name == "Start Time":
                strTime: str = clr.Convert(oDataSet.get_values()[0], str)
                Assert.assertEqual("1 Jun 2004 12:00:00.000000000", strTime)

            oDataSet = drInterval.data_sets[1]
            Assert.assertIsNotNone(oDataSet)
            if oDataSet.element_name == "Stop Time":
                strTime: str = clr.Convert(oDataSet.get_values()[0], str)
                Assert.assertEqual("2 Jun 2004 12:00:00.000000000", strTime)

        TestBase.logger.WriteLine("----- DataProviderInterval_SmartIntervals ----- END -----")

    # endregion

    # region IAgDataPrvInterval_ExecElementsEventArray
    def test_IAgDataPrvInterval_ExecElementsEventArray(self):
        try:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("DataProvidersTests", "ENG88167", "OMTestScenario.sc"))

            scenObj: "IStkObject" = TestBase.Application.current_scenario
            oSatellite: "IStkObject" = scenObj.children["Satellite1"]
            oGroup: "DataProviderGroup" = clr.Convert(oSatellite.data_providers["Lighting Times"], DataProviderGroup)
            oProvider: "IDataProvider" = clr.Convert(oGroup.group["Sunlight"], IDataProvider)

            EventArrayName: str = "TestIntervalArray"

            _EventArrayProvider: "AnalysisWorkbenchProvider" = TestBase.Application.vgt_root.get_provider(
                "Satellite/Satellite1"
            )
            EventArrayTestObject: "ITimeToolEventArray" = _EventArrayProvider.event_arrays[EventArrayName]

            elemCols = ["Start Time", "Stop Time", "Duration"]
            oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderInterval)).exec_elements_event_array(
                EventArrayTestObject, "5 Mar 2010 17:00:00.000", "6 Mar 2010 17:00:00.000", elemCols
            )

            arValues1 = oResult.intervals[0].data_sets[0].get_values()
            arValues2 = oResult.intervals[0].data_sets[1].get_values()
            arValues3 = oResult.intervals[0].data_sets[2].get_values()

            Assert.assertEqual("5 Mar 2010 18:01:28.24036", str(arValues1[1])[0 : (0 + 25)])
            Assert.assertEqual(
                ("5 Mar 2010 19:00:19.70308" if TestBase.UsingLatestICRFDataFiles else "5 Mar 2010 19:00:19.70130"),
                str(arValues2[1])[0 : (0 + 25)],
            )
            Assert.assertAlmostEqual(3531.462992230383, float(arValues3[1]), delta=0.01)

        finally:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    # endregion

    # region IAgDataPrvInterval_ExecEventArray
    def test_IAgDataPrvInterval_ExecEventArray(self):
        try:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("DataProvidersTests", "ENG88167", "OMTestScenario.sc"))

            scenObj: "IStkObject" = TestBase.Application.current_scenario
            oSatellite: "IStkObject" = scenObj.children["Satellite1"]
            oGroup: "DataProviderGroup" = clr.Convert(oSatellite.data_providers["Lighting Times"], DataProviderGroup)
            oProvider: "IDataProvider" = clr.Convert(oGroup.group["Sunlight"], IDataProvider)

            EventArrayName: str = "TestIntervalArray"

            _EventArrayProvider: "AnalysisWorkbenchProvider" = TestBase.Application.vgt_root.get_provider(
                "Satellite/Satellite1"
            )
            EventArrayTestObject: "ITimeToolEventArray" = _EventArrayProvider.event_arrays[EventArrayName]

            oResult: "DataProviderResult" = (clr.Convert(oProvider, DataProviderInterval)).exec_event_array(
                EventArrayTestObject, "5 Mar 2010 17:00:00.000", "6 Mar 2010 17:00:00.000"
            )

            arValues1 = oResult.intervals[0].data_sets[0].get_values()
            arValues2 = oResult.intervals[0].data_sets[1].get_values()
            arValues3 = oResult.intervals[0].data_sets[2].get_values()

            Assert.assertEqual("5 Mar 2010 18:01:28.24036", str(arValues1[1])[0 : (0 + 25)])
            Assert.assertEqual(
                ("5 Mar 2010 19:00:19.70308" if TestBase.UsingLatestICRFDataFiles else "5 Mar 2010 19:00:19.70130"),
                str(arValues2[1])[0 : (0 + 25)],
            )
            Assert.assertAlmostEqual(3531.462992230383, float(arValues3[1]), delta=0.01)

        finally:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    # endregion

    # region IAgDataPrvTimeVar_SmartIntervals
    def test_IAgDataPrvTimeVar_SmartIntervals(self):
        TestBase.logger.WriteLine("----- DataProviderTimeVarying_SmartIntervals ----- BEGIN -----")
        TestBase.Application.unit_preferences.reset_units()

        oSa: "Satellite" = clr.Convert(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        oScenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)

        startTime: typing.Any = (clr.Convert(TestBase.Application.current_scenario, Scenario)).start_time
        stopTime: typing.Any = (clr.Convert(TestBase.Application.current_scenario, Scenario)).stop_time
        startEpoch: "TimeToolEventSmartEpoch" = (
            TestBase.Application.current_scenario.vgt.events.factory.create_smart_epoch_from_time(startTime)
        )
        stopEpoch: "TimeToolEventSmartEpoch" = (
            TestBase.Application.current_scenario.vgt.events.factory.create_smart_epoch_from_time(stopTime)
        )
        oScenario.analysis_interval.set_start_and_stop_epochs(startEpoch, stopEpoch)

        times = [oScenario.analysis_interval.get_start_epoch(), oScenario.analysis_interval.get_stop_epoch()]
        elems = ["Time", "Azimuth"]

        obj: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        timeVar: "DataProviderTimeVarying" = clr.CastAs(obj.data_providers["Lighting AER"], DataProviderTimeVarying)

        result: "DataProviderResult" = timeVar.exec(
            oScenario.analysis_interval.get_start_epoch(), oScenario.analysis_interval.get_stop_epoch(), 60
        )
        Assert.assertEqual("Time", result.data_sets.element_names[0])
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", result.data_sets[0].get_values()[0])
        Assert.assertEqual("Azimuth", result.data_sets.element_names[1])
        Assert.assertAlmostEqual(79.63, float(result.data_sets[1].get_values()[0]), delta=0.01)

        result = timeVar.exec_elements(
            oScenario.analysis_interval.get_start_epoch(), oScenario.analysis_interval.get_stop_epoch(), 60, elems
        )
        Assert.assertEqual("Time", result.data_sets.element_names[0])
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", result.data_sets[0].get_values()[0])
        Assert.assertEqual("Azimuth", result.data_sets.element_names[1])
        Assert.assertAlmostEqual(79.63, float(result.data_sets[1].get_values()[0]), delta=0.01)

        result = timeVar.exec_elements_native_times(
            oScenario.analysis_interval.get_start_epoch(), oScenario.analysis_interval.get_stop_epoch(), elems
        )
        Assert.assertEqual("Time", result.data_sets.element_names[0])
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", result.data_sets[0].get_values()[0])
        Assert.assertEqual("Azimuth", result.data_sets.element_names[1])
        Assert.assertAlmostEqual(79.63, float(result.data_sets[1].get_values()[0]), delta=0.01)

        result = timeVar.exec_native_times(
            oScenario.analysis_interval.get_start_epoch(), oScenario.analysis_interval.get_stop_epoch()
        )
        Assert.assertEqual("Time", result.data_sets.element_names[0])
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", result.data_sets[0].get_values()[0])
        Assert.assertEqual("Azimuth", result.data_sets.element_names[1])
        Assert.assertAlmostEqual(79.63, float(result.data_sets[1].get_values()[0]), delta=0.01)

        result = timeVar.exec_single(oScenario.analysis_interval.get_start_epoch())
        Assert.assertEqual("Time", result.data_sets.element_names[0])
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", result.data_sets[0].get_values()[0])
        Assert.assertEqual("Azimuth", result.data_sets.element_names[1])
        Assert.assertAlmostEqual(79.63, float(result.data_sets[1].get_values()[0]), delta=0.01)

        result = timeVar.exec_single_elements(oScenario.analysis_interval.get_start_epoch(), elems)
        Assert.assertEqual("Time", result.data_sets.element_names[0])
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", result.data_sets[0].get_values()[0])
        Assert.assertEqual("Azimuth", result.data_sets.element_names[1])
        Assert.assertAlmostEqual(79.63, float(result.data_sets[1].get_values()[0]), delta=0.01)

        arrayElements: "DataProviderResultTimeArrayElements" = timeVar.exec_single_elements_array(times, elems)
        Assert.assertTrue(arrayElements.valid)
        Assert.assertEqual("1 Jun 2004 12:00:00.000000000", arrayElements.get_array(0)[0])
        Assert.assertAlmostEqual(79.63, float(arrayElements.get_array(1)[0]), delta=0.01)

        TestBase.logger.WriteLine("----- DataProviderTimeVarying_SmartIntervals ----- END -----")

    # endregion

    def ExecDataProviders(self, dpCollection: "DataProviderCollection", path: str):
        dp: "IDataProviderInfo"
        for dp in dpCollection:
            dpName: str = dp.name
            if dp.is_group():
                group: "DataProviderGroup" = clr.Convert(dp, DataProviderGroup)
                dProviders: "DataProviders" = group.group

                x: "IDataProviderInfo" = dpCollection[0]
                name: str = x.name
                y: "IDataProviderInfo" = dpCollection.get_item_by_index(0)
                z: "IDataProviderInfo" = dpCollection.get_item_by_name(name)
                Assert.assertEqual(x.name, y.name)
                Assert.assertEqual(x.name, z.name)

                dpInfo: "IDataProviderInfo"

                for dpInfo in dProviders:
                    dpInfoName: str = dpInfo.name
                    self.ExecDataPrv(dpInfo, path)
                    Assert.assertTrue(dProviders.contains(dpInfoName))

                Assert.assertFalse(dProviders.contains("ThisIsBogus"))

            else:
                self.ExecDataPrv(dp, path)

    def RunAllDataProviders(self, oObj: "IStkObject"):
        path: str = oObj.path[
            31:
        ]  # e.g.,  strip off:  /Application/STK/Scenario/Test/   to leave:   Satellite/Satellite1
        self.ExecDataProviders(oObj.data_providers, path)

    def ExecDataPrv(self, dp: "IDataProviderInfo", path: str):
        drResult: "DataProviderResult" = None
        dProvider: "IDataProvider" = clr.Convert(dp, IDataProvider)
        if dp.type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_FIXED:
            dpFixed: "DataProviderFixed" = clr.Convert(dp, DataProviderFixed)
            if dProvider.is_valid:
                drResult = dpFixed.exec()

            else:
                with pytest.raises(Exception):
                    dpFixed.exec()

        elif dp.type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_INTVL:
            dpIntvl: "DataProviderInterval" = clr.Convert(dp, DataProviderInterval)
            if dProvider.is_valid:
                drResult = dpIntvl.exec("1 Jul 2008 12:00:00.000", "1 Jul 2008 14:00:00.000")

            else:
                with pytest.raises(Exception):
                    dpIntvl.exec("1 Jul 2008 12:00:00.000", "1 Jul 2008 14:00:00.000")

        elif dp.type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_TIME_VARYING:
            dpTimeVar: "DataProviderTimeVarying" = clr.Convert(dp, DataProviderTimeVarying)
            if dProvider.is_valid:
                drResult = dpTimeVar.exec("1 Jul 2008 12:00:00.000", "1 Jul 2008 14:00:00.000", 60)

            else:
                with pytest.raises(Exception):
                    drResult = dpTimeVar.exec("1 Jul 2008 12:00:00.000", "1 Jul 2008 14:00:00.000", 60)

        if "DistanceAlong" in dp.name:
            # (See 91515) For these dataproviders, call the "Clear" command to free memory:
            #      - DistanceAlongGroundTrack
            #      - DistanceAlongTrajectory
            #      - DistanceAlongTrajectory(CBF)
            #
            s: str = ((('CalculationTool * Clear "' + path) + " ") + dp.name) + ' Scalar Calculation"'
            TestBase.Application.execute_command(s)

        if drResult != None:
            del drResult

    # region DumpRawCrossingData
    def DumpRawCrossingData(self, oInterval: "DataProviderResultInterval", dThreshold: float):
        outStr: str = None

        arCrossings = oInterval.threshold_crossings("FOM Value", dThreshold)  # kilometers
        Assert.assertIsNotNone(arCrossings)

        # logger.WriteLine("Crossings of value: {0}", dThreshold);
        outStr = Double.ToString(dThreshold)

        iIndex: int = 0
        while iIndex < len(arCrossings):
            strTime: str = str(arCrossings[iIndex][0])
            i: int = strTime.find(".")
            if i > 0:
                strTime = strTime[: (i + 2)] + strTime[((i + 2) + ((len(strTime) - i) - 2)) :]

            iDirection: int = int(arCrossings[iIndex][1])
            # logger.Write("Time: {0}	Direction: {1}\n", strTime, iDirection);
            outStr += strTime + str(iDirection)

            iIndex += 1

        return outStr

    # endregion

    # region Enumerate invalid data providers
    def DoInvalidDataProvider(self, dpi: "IDataProviderInfo"):
        dp: "IDataProvider" = clr.CastAs(dpi, IDataProvider)
        Assert.assertIsNotNone(dp, "Cannot cast to IDataProvider!")
        if not dp.is_valid:
            pass

    # endregion

    def DoValidDataProvider(self, dpi: "IDataProviderInfo"):
        # Console.WriteLine("Provider Name: {0}", dpi.Name);

        dp: "IDataProvider" = clr.CastAs(dpi, IDataProvider)
        Assert.assertIsNotNone(dp, "Cannot cast to IDataProvider!")
        if not dp.is_valid:
            # logger.WriteLine("Specified provider \"{0}\" is invalid.", dpi.Name);
            return

        dp.allow_user_interface = False

        startTime: typing.Any = (clr.Convert(TestBase.Application.current_scenario, Scenario)).start_time
        stopTime: typing.Any = (clr.Convert(TestBase.Application.current_scenario, Scenario)).stop_time
        if dpi.type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_TIME_VARYING:
            tv: "DataProviderTimeVarying" = clr.Convert(dp, DataProviderTimeVarying)
            result: "DataProviderResult" = tv.exec(startTime, stopTime, 60)
            del result
        elif dpi.type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_FIXED:
            fixed: "DataProviderFixed" = clr.Convert(dp, DataProviderFixed)
            result: "DataProviderResult" = fixed.exec()
            del result
        elif dpi.type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_INTVL:
            interval: "DataProviderInterval" = clr.Convert(dp, DataProviderInterval)
            result: "DataProviderResult" = interval.exec(startTime, stopTime)
            del result

    # region Enumerate available data providers for all objects

    def EnumerateObjectDataProviders(self, obj: "IStkObject", action):
        # logger.WriteLine("****** {0}  ********", obj.Path);
        dpi: "IDataProviderInfo"
        # logger.WriteLine("****** {0}  ********", obj.Path);
        for dpi in obj.data_providers:
            if dpi.is_group():
                ddpi: "IDataProviderInfo"
                for ddpi in (clr.Convert(dpi, DataProviderGroup)).group:
                    action(ddpi)

            else:
                action(dpi)

    def RecursiveObjectWalk(self, parent: "IStkObject", action):
        self.EnumerateObjectDataProviders(parent, action)
        child: "IStkObject"
        for child in parent.children:
            self.RecursiveObjectWalk(child, action)

    def test_EnumerateDataProviders(self):
        if r"debug" in TestContext.CurrentContext.TestDirectory.lower():
            Assert.skipTest(
                "BUG64435"
            )  # This test is memory intensive and in debug it runs out of memory and a malloc failure causes it to assert later in code.
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))
        sc: "IStkObject" = TestBase.Application.current_scenario
        Assert.assertIsNotNone(sc, "Load a scenario first.")
        try:
            self.RecursiveObjectWalk(sc, (self.DoValidDataProvider))

        finally:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    def test_EnumerateInvalidDataProviders(self):
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))
        sc: "IStkObject" = TestBase.Application.current_scenario
        Assert.assertIsNotNone(sc, "Load a scenario first.")
        try:
            self.RecursiveObjectWalk(sc, (self.DoInvalidDataProvider))

        finally:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(Path.Combine("DataProvidersTests", "DataProvidersTests.sc"))

    # endregion

    @parameterized.expand(
        [
            ("Lighting Times/Umbra", "Duration", STATISTICS.MEAN, 1736.502),
            ("Lighting Times/Umbra", "Duration", STATISTICS.STD_DEV, 777.829),
            ("Lighting Times/Umbra", "Duration", STATISTICS.TOTAL, 5209.5),
            ("Lighting Times/Umbra", "Duration", STATISTICS.PERCENT_INTVL, 36.177),
            ("Lighting Times/Umbra", "Duration", STATISTICS.PERCENT_NOT_INTVL, 63.823),
        ]
    )
    def test_TestComputeStatistic(self, dataPrv: str, elemName: str, stat: "STATISTICS", val: float):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        res: "DataProviderResult" = oSa.data_providers.get_data_provider_interval_from_path(dataPrv).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 16:00:00.00"
        )
        statRes: "DataProviderResultStatisticResult" = res.data_sets.get_data_set_by_name(
            elemName
        ).statistics.compute_statistic(stat)
        Assert.assertTrue(res.data_sets.get_data_set_by_name(elemName).statistics.is_statistic_available(stat))
        Assert.assertAlmostEqual(val, statRes.value, delta=0.005)

    @parameterized.expand(
        [
            ("LLR State/Fixed", "Lat", TIME_VARYING_EXTREMUM.MAX, 28.502, "1 Jun 2004 12:22:37.061"),
            ("LLR State/Fixed", "Lat", TIME_VARYING_EXTREMUM.MAX_OF_SAMPLES, 28.359, "1 Jun 2004 12:24:00.000"),
            ("LLR State/Fixed", "Lat", TIME_VARYING_EXTREMUM.MIN, -24.055, "1 Jun 2004 13:00:00.000"),
            ("LLR State/Fixed", "Lat", TIME_VARYING_EXTREMUM.MIN_OF_SAMPLES, -24.055, "1 Jun 2004 13:00:00.000"),
        ]
    )
    def test_TestComputeTimeVarExtremum(
        self, dataPrv: str, elemName: str, stat: "TIME_VARYING_EXTREMUM", val: float, time: str
    ):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        res: "DataProviderResult" = oSa.data_providers.get_data_provider_time_varying_from_path(dataPrv).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0
        )
        statRes: "DataProviderResultTimeVaryingExtremumResult" = res.data_sets.get_data_set_by_name(
            elemName
        ).statistics.compute_time_varying_extremum(stat)
        Assert.assertTrue(
            res.data_sets.get_data_set_by_name(elemName).statistics.is_time_varying_extremum_available(stat)
        )
        Assert.assertAlmostEqual(val, statRes.value, delta=0.001)
        Assert.assertEqual(time, str(statRes.time)[0 : (0 + len(time))])

    @parameterized.expand(
        [
            ("Shadow LLA/Fixed", "Lat", STATISTICS.MEAN),
            ("Shadow LLA/Fixed", "Lat", STATISTICS.STD_DEV),
            ("Shadow LLA/Fixed", "Lat", STATISTICS.TOTAL),
            ("Shadow LLA/Fixed", "Lat", STATISTICS.PERCENT_INTVL),
            ("Shadow LLA/Fixed", "Lat", STATISTICS.PERCENT_NOT_INTVL),
        ]
    )
    def test_TestIsStatisticAvailableFalse(self, dataPrv: str, elemName: str, stat: "STATISTICS"):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        res: "DataProviderResult" = oSa.data_providers.get_data_provider_time_varying_from_path(dataPrv).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0
        )
        Assert.assertFalse(res.data_sets.get_data_set_by_name(elemName).statistics.is_statistic_available(stat))

    @parameterized.expand(
        [
            ("Shadow LLA/Fixed", "Lat", TIME_VARYING_EXTREMUM.MAX),
            ("Shadow LLA/Fixed", "Lat", TIME_VARYING_EXTREMUM.MAX_OF_SAMPLES),
            ("Shadow LLA/Fixed", "Lat", TIME_VARYING_EXTREMUM.MIN),
            ("Shadow LLA/Fixed", "Lat", TIME_VARYING_EXTREMUM.MIN_OF_SAMPLES),
        ]
    )
    def test_TestIsTimeVarExtremumAvailableFalse(self, dataPrv: str, elemName: str, stat: "TIME_VARYING_EXTREMUM"):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        res: "DataProviderResult" = oSa.data_providers.get_data_provider_time_varying_from_path(dataPrv).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0
        )
        Assert.assertFalse(
            res.data_sets.get_data_set_by_name(elemName).statistics.is_time_varying_extremum_available(stat)
        )

    @parameterized.expand(
        [
            ("Active Constraints", False),
            ("Astrogator Script Summary", True),
            ("Crdn Available Times", True),
            ("Ephemeris Diff in Curvilinear Coordinates", True),
        ]
    )
    def test_TestPreDataRequired(self, dataPrv: str, expected: bool):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        dp: "IDataProvider" = clr.CastAs(oSa.data_providers[dataPrv], IDataProvider)
        Assert.assertEqual(expected, dp.pre_data_required)

    @parameterized.expand(
        [
            ("Active Constraints", ""),
            ("Astrogator Script Summary", '"<Scripting Tool Path>"'),
            ("Crdn Available Times", '"<TruncObjectPath> <VectorName>" - e.g. "CentralBody/Earth Angular_Velocity"'),
            ("Ephemeris Diff in Curvilinear Coordinates", '"<TruncObjectPath>" - e.g. "Satellite/Sat1"'),
        ]
    )
    def test_TestPreDataDescription(self, dataPrv: str, expected: str):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        dp: "IDataProvider" = clr.CastAs(oSa.data_providers[dataPrv], IDataProvider)
        Assert.assertEqual(expected, dp.pre_data_description)

    def test_TestComputeTimeVarWithMultipleIntvls(self):
        expectedValues = [-18.233, -19.07, -18.102]

        expectedTimes = ["1 Jun 2004 16:49:45.864", "1 Jun 2004 18:24:55.776", "1 Jun 2004 20:00:05.225"]

        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        oFac: "IStkObject" = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "Facility2")
        acc: "StkAccess" = oSa.get_access_to_object(oFac)
        acc.compute_access()
        res: "DataProviderResult" = acc.data_providers.get_data_provider_time_varying_from_path(
            "AER Data/Default"
        ).exec("1 Jun 2004 12:00:00.00", "2 Jun 2004 12:00:00.00", 60.0)

        i: int = 0
        while i < res.intervals.count:
            statRes: "DataProviderResultTimeVaryingExtremumResult" = (
                res.intervals[i]
                .data_sets.get_data_set_by_name("Elevation")
                .statistics.compute_time_varying_extremum(TIME_VARYING_EXTREMUM.MIN)
            )
            Assert.assertAlmostEqual(float(expectedValues[i]), statRes.value, delta=0.001)
            Assert.assertEqual(expectedTimes[i], str(statRes.time)[0 : (0 + len(str(expectedTimes[i])))])

            i += 1

    def test_TestFailComputeTimeVarExtremum(self):
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        oSensor: "IStkObject" = oSatellite.children["Sensor1"]

        oProvider: "IDataProvider" = clr.Convert(oSensor.data_providers["Pattern Intersection"], IDataProvider)
        res: "DataProviderResult" = (clr.Convert(oProvider, DataProviderTimeVarying)).exec(
            "1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0
        )

        with pytest.raises(Exception, match=RegexSubstringMatch("Time Varying Extremum not available for element")):
            res.data_sets.get_data_set_by_name("UTM Easting").statistics.compute_time_varying_extremum(
                TIME_VARYING_EXTREMUM.MIN
            )

    def test_TestFailComputeStatistic(self):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        res: "DataProviderResult" = oSa.data_providers.get_data_provider_time_varying_from_path(
            "Shadow LLA/Fixed"
        ).exec("1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.0)
        with pytest.raises(Exception, match=RegexSubstringMatch("Statistic not available for element")):
            res.data_sets.get_data_set_by_name("Lat").statistics.compute_statistic(STATISTICS.PERCENT_INTVL)

    @parameterized.expand(
        [
            ("Shadow LLA/Fixed", "Lat", STATISTICS.MEAN),
            ("Shadow LLA/Fixed", "Lat", STATISTICS.STD_DEV),
            ("Shadow LLA/Fixed", "Lat", STATISTICS.TOTAL),
            ("Shadow LLA/Fixed", "Lat", STATISTICS.PERCENT_INTVL),
            ("Shadow LLA/Fixed", "Lat", STATISTICS.PERCENT_NOT_INTVL),
        ]
    )
    def test_TestDPIsStatisticAvailableFalse(self, dataPrv: str, elemName: str, stat: "STATISTICS"):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        dp: "IDataProvider" = clr.CastAs(oSa.data_providers.get_data_provider_info_from_path(dataPrv), IDataProvider)
        Assert.assertFalse(dp.is_statistic_available(stat, elemName))

    @parameterized.expand(
        [
            ("Shadow LLA/Fixed", "Lat", TIME_VARYING_EXTREMUM.MAX),
            ("Shadow LLA/Fixed", "Lat", TIME_VARYING_EXTREMUM.MAX_OF_SAMPLES),
            ("Shadow LLA/Fixed", "Lat", TIME_VARYING_EXTREMUM.MIN),
            ("Shadow LLA/Fixed", "Lat", TIME_VARYING_EXTREMUM.MIN_OF_SAMPLES),
        ]
    )
    def test_TestDPIsTimeVarExtremumAvailableFalse(self, dataPrv: str, elemName: str, stat: "TIME_VARYING_EXTREMUM"):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        dp: "IDataProvider" = clr.CastAs(oSa.data_providers.get_data_provider_info_from_path(dataPrv), IDataProvider)
        Assert.assertFalse(dp.is_time_varying_extremum_available(stat, elemName))

    @parameterized.expand(
        [
            ("Lighting Times/Umbra", "Duration", STATISTICS.MEAN),
            ("Lighting Times/Umbra", "Duration", STATISTICS.STD_DEV),
            ("Lighting Times/Umbra", "Duration", STATISTICS.TOTAL),
            ("Lighting Times/Umbra", "Duration", STATISTICS.PERCENT_INTVL),
            ("Lighting Times/Umbra", "Duration", STATISTICS.PERCENT_NOT_INTVL),
        ]
    )
    def test_TestDPIsStatisticAvailableTrue(self, dataPrv: str, elemName: str, stat: "STATISTICS"):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        dp: "IDataProvider" = clr.CastAs(oSa.data_providers.get_data_provider_info_from_path(dataPrv), IDataProvider)
        Assert.assertTrue(dp.is_statistic_available(stat, elemName))

    @parameterized.expand(
        [
            ("LLR State/Fixed", "Lat", TIME_VARYING_EXTREMUM.MAX),
            ("LLR State/Fixed", "Lat", TIME_VARYING_EXTREMUM.MAX_OF_SAMPLES),
            ("LLR State/Fixed", "Lat", TIME_VARYING_EXTREMUM.MIN),
            ("LLR State/Fixed", "Lat", TIME_VARYING_EXTREMUM.MIN_OF_SAMPLES),
        ]
    )
    def test_TestDPIsTimeVarExtremumAvailableTrue(self, dataPrv: str, elemName: str, stat: "TIME_VARYING_EXTREMUM"):
        oSa: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        dp: "IDataProvider" = clr.CastAs(oSa.data_providers.get_data_provider_info_from_path(dataPrv), IDataProvider)
        Assert.assertTrue(dp.is_time_varying_extremum_available(stat, elemName))
