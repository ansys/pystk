# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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
from assertion_harness import *
from interfaces.stk_objects import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()

            paths: "PathCollection" = (
                TestBase.Application.preferences.python_plugins_preferences.ephemeris_file_reader_paths
            )
            paths.add(TestBase.GetScenarioFile("Plugins", "Python_Ephemeris_File_Reader_Plugin_Example.py"))

            TestBase.LoadTestScenario(Path.Combine("AdvCATTests", "AdvCATTests.sc"))
            EarlyBoundTests.AG_ACAT = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STKObjectType.ADVCAT, "TestAdvCAT"), AdvCAT
            )

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        paths: "PathCollection" = (
            TestBase.Application.preferences.python_plugins_preferences.ephemeris_file_reader_paths
        )
        paths.remove_all()
        TestBase.Application.current_scenario.children.unload(STKObjectType.ADVCAT, "TestAdvCAT")
        EarlyBoundTests.AG_ACAT = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_ACAT: "AdvCAT" = None
    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_ACAT)
        obj: "IStkObject" = IStkObject(EarlyBoundTests.AG_ACAT)

        # Short Description test
        obj.short_description = "This is a new short description."
        Assert.assertEqual("This is a new short description.", obj.short_description)
        obj.short_description = ""
        Assert.assertEqual("", obj.short_description)

        # Long Description test
        obj.long_description = "This is a new Long description."
        Assert.assertEqual("This is a new Long description.", obj.long_description)
        obj.long_description = ""
        Assert.assertEqual("", obj.long_description)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_ACAT, IStkObject))
        oHelper.TestObjectFilesArray((IStkObject(EarlyBoundTests.AG_ACAT)).object_files)

    # endregion

    # region Main
    def test_Main(self):
        eventIntSmartInterval: "TimeToolTimeIntervalSmartInterval" = EarlyBoundTests.AG_ACAT.time_period
        eventIntSmartInterval.set_implicit_interval(
            TestBase.Application.current_scenario.analysis_workbench_components.time_intervals["AnalysisInterval"]
        )
        Assert.assertEqual("1 Jul 1999 00:00:00.000", eventIntSmartInterval.find_start_time())
        Assert.assertEqual("2 Jul 1999 00:00:00.000", eventIntSmartInterval.find_stop_time())

        EarlyBoundTests.AG_ACAT.threshold = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_ACAT.threshold)
        EarlyBoundTests.AG_ACAT.threshold = 1000
        Assert.assertEqual(1000, EarlyBoundTests.AG_ACAT.threshold)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.threshold = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.threshold = 1001

        EarlyBoundTests.AG_ACAT.use_range_measure = False
        Assert.assertFalse(EarlyBoundTests.AG_ACAT.use_range_measure)
        EarlyBoundTests.AG_ACAT.use_range_measure = True
        Assert.assertTrue(EarlyBoundTests.AG_ACAT.use_range_measure)

        EarlyBoundTests.AG_ACAT.display_acknowledgement_when_done = False
        Assert.assertFalse(EarlyBoundTests.AG_ACAT.display_acknowledgement_when_done)
        EarlyBoundTests.AG_ACAT.display_acknowledgement_when_done = True
        Assert.assertTrue(EarlyBoundTests.AG_ACAT.display_acknowledgement_when_done)

        EarlyBoundTests.AG_ACAT.compute()

    # endregion

    # region Main_ChosenObject
    def test_Main_ChosenObject(self):
        primaryChosenObjColl: "AdvCATChosenObjectCollection" = EarlyBoundTests.AG_ACAT.get_primary_chosen_objects()

        with pytest.raises(Exception, match=RegexSubstringMatch("Error occurred")):
            chosenObjectX: "AdvCATChosenObject" = primaryChosenObjColl.add("bogus.al3")

        chosenObject: "AdvCATChosenObject" = primaryChosenObjColl.add("GPSAlmanac.al3")
        Assert.assertEqual("GPSAlmanac.al3", chosenObject.name)

        chosenObject.ellipsoid_class = AdvCATEllipsoidClassType.CLASS_COVARIANCE_OFFSET
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_COVARIANCE_OFFSET, chosenObject.ellipsoid_class)

        chosenObject.tangential = 0
        Assert.assertEqual(0, chosenObject.tangential)
        chosenObject.tangential = 1000
        Assert.assertEqual(1000, chosenObject.tangential)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.tangential = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.tangential = 1001

        chosenObject.cross_track = 0
        Assert.assertEqual(0, chosenObject.cross_track)
        chosenObject.cross_track = 1000
        Assert.assertEqual(1000, chosenObject.cross_track)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.cross_track = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.cross_track = 1001

        chosenObject.normal = 0
        Assert.assertEqual(0, chosenObject.normal)
        chosenObject.normal = 1000
        Assert.assertEqual(1000, chosenObject.normal)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.normal = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.normal = 1001

        chosenObject.ellipsoid_class = AdvCATEllipsoidClassType.CLASS_FIXED
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_FIXED, chosenObject.ellipsoid_class)

        chosenObject.tangential = 0
        Assert.assertEqual(0, chosenObject.tangential)
        chosenObject.tangential = 1000
        Assert.assertEqual(1000, chosenObject.tangential)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.tangential = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.tangential = 1001

        chosenObject.cross_track = 0
        Assert.assertEqual(0, chosenObject.cross_track)
        chosenObject.cross_track = 1000
        Assert.assertEqual(1000, chosenObject.cross_track)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.cross_track = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.cross_track = 1001

        chosenObject.normal = 0
        Assert.assertEqual(0, chosenObject.normal)
        chosenObject.normal = 1000
        Assert.assertEqual(1000, chosenObject.normal)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.normal = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.normal = 1001

        chosenObject.ellipsoid_class = AdvCATEllipsoidClassType.CLASS_COVARIANCE
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_COVARIANCE, chosenObject.ellipsoid_class)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.tangential = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.cross_track = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.normal = 0

        chosenObject.ellipsoid_class = AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME, chosenObject.ellipsoid_class)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.tangential = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.cross_track = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.normal = 0

        chosenObject.ellipsoid_class = AdvCATEllipsoidClassType.CLASS_ORBIT_CLASS
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_ORBIT_CLASS, chosenObject.ellipsoid_class)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.tangential = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.cross_track = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.normal = 0

        chosenObject.ellipsoid_class = AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME_BY_ORBIT_CLASS
        Assert.assertEqual(
            AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME_BY_ORBIT_CLASS, chosenObject.ellipsoid_class
        )

        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.tangential = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.cross_track = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("is not valid for Class")):
            chosenObject.normal = 0

        Assert.assertEqual("Almanac File", chosenObject.type)

        chosenObject.hard_body_radius = 0
        Assert.assertEqual(0, chosenObject.hard_body_radius)
        chosenObject.hard_body_radius = 100
        Assert.assertEqual(100, chosenObject.hard_body_radius)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.hard_body_radius = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.hard_body_radius = 101

        chosenObject.number_identifier = 0
        Assert.assertEqual(0, chosenObject.number_identifier)
        chosenObject.number_identifier = 2000000000
        Assert.assertEqual(2000000000, chosenObject.number_identifier)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            chosenObject.number_identifier = -1

        chosenObject.string_identifier = "aaa"
        Assert.assertEqual("aaa", chosenObject.string_identifier)
        chosenObject.string_identifier = "bbb"
        Assert.assertEqual("bbb", chosenObject.string_identifier)

        primaryChosenObjColl.remove_all()

    # endregion

    # region Main_PrimaryList
    def test_Main_PrimaryList(self):
        # Clean up files that might exist from other tests
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileStk.be"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileStk_diff.be"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileStk.be"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileStk_diff.be"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileStk.e"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileStk.e"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCode500.eph"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCode500.eph"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_1.oem"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_2.oem"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_3.oem"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCCSDS_1.oem"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCCSDS_2.oem"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCCSDS_3.oem"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFilePropDef.pg"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFilePropDef.pg"))

        EarlyBoundTests.AG_ACAT.primary_default_tangential = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_ACAT.primary_default_tangential)
        EarlyBoundTests.AG_ACAT.primary_default_tangential = 1000
        Assert.assertEqual(1000, EarlyBoundTests.AG_ACAT.primary_default_tangential)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.primary_default_tangential = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.primary_default_tangential = 1001

        EarlyBoundTests.AG_ACAT.primary_default_cross_track = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_ACAT.primary_default_cross_track)
        EarlyBoundTests.AG_ACAT.primary_default_cross_track = 1000
        Assert.assertEqual(1000, EarlyBoundTests.AG_ACAT.primary_default_cross_track)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.primary_default_cross_track = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.primary_default_cross_track = 1001

        EarlyBoundTests.AG_ACAT.primary_default_normal = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_ACAT.primary_default_normal)
        EarlyBoundTests.AG_ACAT.primary_default_normal = 1000
        Assert.assertEqual(1000, EarlyBoundTests.AG_ACAT.primary_default_normal)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.primary_default_normal = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.primary_default_normal = 1001

        EarlyBoundTests.AG_ACAT.primary_default_class = AdvCATEllipsoidClassType.CLASS_COVARIANCE_OFFSET
        Assert.assertEqual(
            AdvCATEllipsoidClassType.CLASS_COVARIANCE_OFFSET, EarlyBoundTests.AG_ACAT.primary_default_class
        )
        EarlyBoundTests.AG_ACAT.primary_default_class = AdvCATEllipsoidClassType.CLASS_COVARIANCE
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_COVARIANCE, EarlyBoundTests.AG_ACAT.primary_default_class)
        EarlyBoundTests.AG_ACAT.primary_default_class = AdvCATEllipsoidClassType.CLASS_FIXED
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_FIXED, EarlyBoundTests.AG_ACAT.primary_default_class)
        EarlyBoundTests.AG_ACAT.primary_default_class = AdvCATEllipsoidClassType.CLASS_ORBIT_CLASS
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_ORBIT_CLASS, EarlyBoundTests.AG_ACAT.primary_default_class)
        EarlyBoundTests.AG_ACAT.primary_default_class = AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME_BY_ORBIT_CLASS
        Assert.assertEqual(
            AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME_BY_ORBIT_CLASS,
            EarlyBoundTests.AG_ACAT.primary_default_class,
        )
        EarlyBoundTests.AG_ACAT.primary_default_class = AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME
        Assert.assertEqual(
            AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME, EarlyBoundTests.AG_ACAT.primary_default_class
        )

        availObjColl: "AdvCATAvailableObjectCollection" = EarlyBoundTests.AG_ACAT.get_available_objects()

        # Some file extensions are added to the search by CSharp plugins. These are not yet supported on all platforms for PySTK.
        Assert.assertTrue(availObjColl.count, [29, 35])
        numAvailObjs: int = availObjColl.count

        name: typing.Any = None
        date: typing.Any = None
        typeX: typing.Any = None

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            (name, date, typeX) = availObjColl.get_available_object(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            (name, date, typeX) = availObjColl.get_available_object(numAvailObjs)
        (name, date, typeX) = availObjColl.get_available_object(5)
        Assert.assertEqual("GPSAlmanac.al3", name)
        # Assert.AreEqual("11/18/22", date);   // Date varies depending on timestamp of file.
        Assert.assertEqual("Almanac File", typeX)

        arAvailObjs = availObjColl.to_array()
        Assert.assertEqual(numAvailObjs, len(arAvailObjs))
        Assert.assertEqual("GPSAlmanac.al3", arAvailObjs[5][0])
        # Assert.AreEqual("11/18/22", arAvailObjs.GetValue(5, 1));  // Date varies depending on timestamp of file.
        Assert.assertEqual("Almanac File", arAvailObjs[5][2])

        primaryChosenObjColl: "AdvCATChosenObjectCollection" = EarlyBoundTests.AG_ACAT.get_primary_chosen_objects()
        Assert.assertEqual(0, primaryChosenObjColl.count)

        primaryChosenObjColl.add("GPSAlmanac.al3")
        primaryChosenObjColl.add("GPSAlmanac.alm")
        primaryChosenObjColl.add("TestEph.e")
        Assert.assertEqual(3, primaryChosenObjColl.count)

        s: str = ""

        i: int = 0
        while i < 3:
            chosenObj: "AdvCATChosenObject" = primaryChosenObjColl[i]
            s += chosenObj.name

            i += 1

        Assert.assertEqual("GPSAlmanac.al3GPSAlmanac.almTestEph.e", s)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            x: str = str(primaryChosenObjColl[-1])
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            x: str = str(primaryChosenObjColl[3])

        s = ""
        chosenObj: "AdvCATChosenObject"
        for chosenObj in primaryChosenObjColl:
            s += chosenObj.name

        Assert.assertEqual("GPSAlmanac.al3GPSAlmanac.almTestEph.e", s)

        primaryChosenObjColl.remove_at(1)
        Assert.assertEqual(2, primaryChosenObjColl.count)
        Assert.assertEqual("GPSAlmanac.al3", primaryChosenObjColl[0].name)
        Assert.assertEqual("TestEph.e", primaryChosenObjColl[1].name)

        primaryChosenObjColl.remove_all()
        Assert.assertEqual(0, primaryChosenObjColl.count)

    # endregion

    # region Main_SecondaryList
    def test_Main_SecondaryList(self):
        # Clean up files that might exist from other tests
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileStk.be"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileStk_diff.be"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileStk.be"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileStk_diff.be"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileStk.e"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileStk.e"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCode500.eph"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCode500.eph"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCCSDS.oem"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_1.oem"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_2.oem"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFileCCSDS_3.oem"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCCSDS.oem"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCCSDS_1.oem"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCCSDS_2.oem"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFileCCSDS_3.oem"))
        File.Delete(TestBase.GetScenarioFile("ConnectExternalFilePropDef.pg"))
        File.Delete(TestBase.GetScenarioFile("OMExternalFilePropDef.pg"))

        EarlyBoundTests.AG_ACAT.secondary_default_tangential = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_ACAT.secondary_default_tangential)
        EarlyBoundTests.AG_ACAT.secondary_default_tangential = 1000
        Assert.assertEqual(1000, EarlyBoundTests.AG_ACAT.secondary_default_tangential)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.secondary_default_tangential = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.secondary_default_tangential = 1001

        EarlyBoundTests.AG_ACAT.secondary_default_cross_track = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_ACAT.secondary_default_cross_track)
        EarlyBoundTests.AG_ACAT.secondary_default_cross_track = 1000
        Assert.assertEqual(1000, EarlyBoundTests.AG_ACAT.secondary_default_cross_track)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.secondary_default_cross_track = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.secondary_default_cross_track = 1001

        EarlyBoundTests.AG_ACAT.secondary_default_normal = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_ACAT.secondary_default_normal)
        EarlyBoundTests.AG_ACAT.secondary_default_normal = 1000
        Assert.assertEqual(1000, EarlyBoundTests.AG_ACAT.secondary_default_normal)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.secondary_default_normal = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_ACAT.secondary_default_normal = 1001

        EarlyBoundTests.AG_ACAT.secondary_default_class = AdvCATEllipsoidClassType.CLASS_COVARIANCE_OFFSET
        Assert.assertEqual(
            AdvCATEllipsoidClassType.CLASS_COVARIANCE_OFFSET, EarlyBoundTests.AG_ACAT.secondary_default_class
        )
        EarlyBoundTests.AG_ACAT.secondary_default_class = AdvCATEllipsoidClassType.CLASS_COVARIANCE
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_COVARIANCE, EarlyBoundTests.AG_ACAT.secondary_default_class)
        EarlyBoundTests.AG_ACAT.secondary_default_class = AdvCATEllipsoidClassType.CLASS_FIXED
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_FIXED, EarlyBoundTests.AG_ACAT.secondary_default_class)
        EarlyBoundTests.AG_ACAT.secondary_default_class = AdvCATEllipsoidClassType.CLASS_ORBIT_CLASS
        Assert.assertEqual(AdvCATEllipsoidClassType.CLASS_ORBIT_CLASS, EarlyBoundTests.AG_ACAT.secondary_default_class)
        EarlyBoundTests.AG_ACAT.secondary_default_class = (
            AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME_BY_ORBIT_CLASS
        )
        Assert.assertEqual(
            AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME_BY_ORBIT_CLASS,
            EarlyBoundTests.AG_ACAT.secondary_default_class,
        )
        EarlyBoundTests.AG_ACAT.secondary_default_class = AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME
        Assert.assertEqual(
            AdvCATEllipsoidClassType.CLASS_QUADRATIC_IN_TIME, EarlyBoundTests.AG_ACAT.secondary_default_class
        )

        availObjColl: "AdvCATAvailableObjectCollection" = EarlyBoundTests.AG_ACAT.get_available_objects()

        # Some file extensions are added to the search by CSharp plugins. These are not yet supported on all platforms for PySTK.
        Assert.assertTrue(availObjColl.count, [29, 35])
        numAvailObjs: int = availObjColl.count

        name: typing.Any = None
        date: typing.Any = None
        typeX: typing.Any = None

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            (name, date, typeX) = availObjColl.get_available_object(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            (name, date, typeX) = availObjColl.get_available_object(numAvailObjs)
        (name, date, typeX) = availObjColl.get_available_object(5)
        Assert.assertEqual("GPSAlmanac.al3", name)
        # Assert.AreEqual("11/18/22", date);    // Date varies depending on timestamp of file.
        Assert.assertEqual("Almanac File", typeX)

        arAvailObjs = availObjColl.to_array()
        Assert.assertEqual(numAvailObjs, len(arAvailObjs))
        Assert.assertEqual("GPSAlmanac.al3", arAvailObjs[5][0])
        # Assert.AreEqual("11/18/22", arAvailObjs.GetValue(5, 1));  // Date varies depending on timestamp of file.
        Assert.assertEqual("Almanac File", arAvailObjs[5][2])

        secondaryChosenObjColl: "AdvCATChosenObjectCollection" = EarlyBoundTests.AG_ACAT.get_secondary_chosen_objects()
        Assert.assertEqual(0, secondaryChosenObjColl.count)

        secondaryChosenObjColl.add("GPSAlmanac.al3")
        secondaryChosenObjColl.add("GPSAlmanac.alm")
        secondaryChosenObjColl.add("TestEph.e")
        Assert.assertEqual(3, secondaryChosenObjColl.count)

        s: str = ""

        i: int = 0
        while i < 3:
            chosenObj: "AdvCATChosenObject" = secondaryChosenObjColl[i]
            s += chosenObj.name

            i += 1

        Assert.assertEqual("GPSAlmanac.al3GPSAlmanac.almTestEph.e", s)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            x: str = str(secondaryChosenObjColl[-1])
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            x: str = str(secondaryChosenObjColl[3])

        s = ""
        chosenObj: "AdvCATChosenObject"
        for chosenObj in secondaryChosenObjColl:
            s += chosenObj.name

        Assert.assertEqual("GPSAlmanac.al3GPSAlmanac.almTestEph.e", s)

        secondaryChosenObjColl.remove_at(1)
        Assert.assertEqual(2, secondaryChosenObjColl.count)
        Assert.assertEqual("GPSAlmanac.al3", secondaryChosenObjColl[0].name)
        Assert.assertEqual("TestEph.e", secondaryChosenObjColl[1].name)

        secondaryChosenObjColl.remove_all()
        Assert.assertEqual(0, secondaryChosenObjColl.count)

    # endregion

    # region Advanced
    def test_Advanced(self):
        advanced: "AdvCATAdvancedSettings" = EarlyBoundTests.AG_ACAT.advanced
        SatDBDir: str = TestBase.PathCombine(TestBase.GetSTKDBDir(), r"Databases\Satellite")

        advanced.use_log_file = False
        Assert.assertFalse(advanced.use_log_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            advanced.log_filename = r"C:\Temp\testlog.log"
        advanced.use_log_file = True
        Assert.assertTrue(advanced.use_log_file)
        advanced.log_filename = r"C:\Temp\testlog.log"
        Assert.assertEqual(r"C:\Temp\testlog.log", advanced.log_filename)

        advanced.use_correlation_file = False
        Assert.assertFalse(advanced.use_correlation_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            advanced.correlation_filename = TestBase.PathCombine(SatDBDir, "stkRelatedObjects.rel")
        advanced.use_correlation_file = True
        Assert.assertTrue(advanced.use_correlation_file)
        advanced.correlation_filename = TestBase.PathCombine(SatDBDir, "stkRelatedObjects.rel")
        Assert.assertEqual("stkRelatedObjects.rel", advanced.correlation_filename)

        advanced.show_message_in_message_viewer = False
        Assert.assertFalse(advanced.show_message_in_message_viewer)
        advanced.show_message_in_message_viewer = True
        Assert.assertTrue(advanced.show_message_in_message_viewer)

        advanced.force_repropagation_on_load = False
        Assert.assertFalse(advanced.force_repropagation_on_load)
        advanced.force_repropagation_on_load = True
        Assert.assertTrue(advanced.force_repropagation_on_load)

        advanced.compute_on_load = False
        Assert.assertFalse(advanced.compute_on_load)
        advanced.compute_on_load = True
        Assert.assertTrue(advanced.compute_on_load)

        advanced.allow_partial_ephemeris = False
        Assert.assertFalse(advanced.allow_partial_ephemeris)
        advanced.allow_partial_ephemeris = True
        Assert.assertTrue(advanced.allow_partial_ephemeris)

        advanced.remove_secondary_by_ssc = False
        Assert.assertFalse(advanced.remove_secondary_by_ssc)
        advanced.remove_secondary_by_ssc = True
        Assert.assertTrue(advanced.remove_secondary_by_ssc)

        advanced.use_cross_reference_database = False
        Assert.assertFalse(advanced.use_cross_reference_database)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            advanced.cross_reference_database = TestBase.PathCombine(SatDBDir, "stkSatDb.sd")
        advanced.use_cross_reference_database = True
        Assert.assertTrue(advanced.use_cross_reference_database)
        advanced.cross_reference_database = TestBase.PathCombine(SatDBDir, "stkSatDb.sd")
        Assert.assertEqual("stkSatDb.sd", advanced.cross_reference_database)

        sscHardBodyRadiusFile: str = TestBase.GetScenarioFile("SSCHardBodyRadiusFile.rad")
        advanced.use_ssc_hard_body_radius_file = False
        Assert.assertFalse(advanced.use_ssc_hard_body_radius_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            advanced.ssc_hard_body_radius_file = sscHardBodyRadiusFile
        advanced.use_ssc_hard_body_radius_file = True
        Assert.assertTrue(advanced.use_ssc_hard_body_radius_file)
        advanced.ssc_hard_body_radius_file = sscHardBodyRadiusFile
        Assert.assertEqual("SSCHardBodyRadiusFile.rad", advanced.ssc_hard_body_radius_file)

        advanced.maximum_sample_step_size = 0.0001
        Assert.assertEqual(0.0001, advanced.maximum_sample_step_size)
        advanced.maximum_sample_step_size = 10000000000
        Assert.assertEqual(10000000000, advanced.maximum_sample_step_size)

        advanced.minimum_sample_step_size = 0.0001
        Assert.assertEqual(0.0001, advanced.minimum_sample_step_size)
        advanced.minimum_sample_step_size = 10000000000
        Assert.assertEqual(10000000000, advanced.minimum_sample_step_size)

        advanced.conjunction_type = AdvCATConjunctionType.GLOBAL_PLUS_LOCAL
        Assert.assertEqual(AdvCATConjunctionType.GLOBAL_PLUS_LOCAL, advanced.conjunction_type)
        advanced.conjunction_type = AdvCATConjunctionType.LOCAL_PLUS_END_POINTS
        Assert.assertEqual(AdvCATConjunctionType.LOCAL_PLUS_END_POINTS, advanced.conjunction_type)
        advanced.conjunction_type = AdvCATConjunctionType.GLOBAL_ONLY
        Assert.assertEqual(AdvCATConjunctionType.GLOBAL_ONLY, advanced.conjunction_type)
        advanced.conjunction_type = AdvCATConjunctionType.LOCAL_ONLY
        Assert.assertEqual(AdvCATConjunctionType.LOCAL_ONLY, advanced.conjunction_type)

    # endregion

    # region Advanced_PreFilters
    def test_Advanced_PreFilters(self):
        advanced: "AdvCATAdvancedSettings" = EarlyBoundTests.AG_ACAT.advanced
        preFilters: "AdvCATPreFilters" = advanced.pre_filters

        preFilters.use_out_of_date_filter = False
        Assert.assertFalse(preFilters.use_out_of_date_filter)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            preFilters.out_of_date_pad = 86400
        preFilters.use_out_of_date_filter = True
        Assert.assertTrue(preFilters.use_out_of_date_filter)
        preFilters.out_of_date_pad = 86400
        Assert.assertEqual(86400, preFilters.out_of_date_pad)
        preFilters.out_of_date_pad = 315360000
        Assert.assertEqual(315360000, preFilters.out_of_date_pad)

        preFilters.use_apogee_perigee_filter = False
        Assert.assertFalse(preFilters.use_apogee_perigee_filter)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            preFilters.apogee_perigee_pad = 0
        preFilters.use_apogee_perigee_filter = True
        Assert.assertTrue(preFilters.use_apogee_perigee_filter)
        preFilters.apogee_perigee_pad = 0
        Assert.assertEqual(0, preFilters.apogee_perigee_pad)
        preFilters.apogee_perigee_pad = 100000
        Assert.assertEqual(100000, preFilters.apogee_perigee_pad)

        preFilters.use_orbit_path_filter = False
        Assert.assertFalse(preFilters.use_orbit_path_filter)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            preFilters.orbit_path_pad = 0
        preFilters.use_orbit_path_filter = True
        Assert.assertTrue(preFilters.use_orbit_path_filter)
        preFilters.orbit_path_pad = 0
        Assert.assertEqual(0, preFilters.orbit_path_pad)
        preFilters.orbit_path_pad = 100000
        Assert.assertEqual(100000, preFilters.orbit_path_pad)

        preFilters.use_time_filter = False
        Assert.assertFalse(preFilters.use_time_filter)
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            preFilters.time_distance_pad = 0
        preFilters.use_time_filter = True
        Assert.assertTrue(preFilters.use_time_filter)
        preFilters.time_distance_pad = 0
        Assert.assertEqual(0, preFilters.time_distance_pad)
        preFilters.time_distance_pad = 100000
        Assert.assertEqual(100000, preFilters.time_distance_pad)

    # endregion

    # region Advanced_AdvEllipsoid
    def test_Advanced_AdvEllipsoid(self):
        advanced: "AdvCATAdvancedSettings" = EarlyBoundTests.AG_ACAT.advanced
        advEllipsoid: "AdvCATAdvancedEllipsoid" = advanced.ellipsoid_advanced_settings

        SatDBDir: str = TestBase.PathCombine(TestBase.GetSTKDBDir(), r"Databases\Satellite")

        advEllipsoid.quadratic_in_time_database = TestBase.PathCombine(SatDBDir, "stkQuadDB.qdb")
        Assert.assertEqual("stkQuadDB.qdb", advEllipsoid.quadratic_in_time_database)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            advEllipsoid.quadratic_in_time_database = TestBase.PathCombine(SatDBDir, "bogus.qdb")

        advEllipsoid.fixed_by_orbit_class_database = TestBase.PathCombine(SatDBDir, "stkFxdOrbCls.foc")
        Assert.assertEqual("stkFxdOrbCls.foc", advEllipsoid.fixed_by_orbit_class_database)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            advEllipsoid.fixed_by_orbit_class_database = TestBase.PathCombine(SatDBDir, "bogus.qdb")

        advEllipsoid.quadratic_by_orbit_class_database = TestBase.PathCombine(SatDBDir, "stkQuadOrbCls.qoc")
        Assert.assertEqual("stkQuadOrbCls.qoc", advEllipsoid.quadratic_by_orbit_class_database)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            advEllipsoid.quadratic_by_orbit_class_database = TestBase.PathCombine(SatDBDir, "bogus.qdb")

        advEllipsoid.scale_factor = 0
        Assert.assertEqual(0, advEllipsoid.scale_factor)
        advEllipsoid.scale_factor = 1000
        Assert.assertEqual(1000, advEllipsoid.scale_factor)

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        advCATVO: "AdvCATGraphics3D" = EarlyBoundTests.AG_ACAT.graphics_3d

        advCATVO.show = False
        Assert.assertFalse(advCATVO.show)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            advCATVO.show_primary_ellipsoids = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            advCATVO.show_secondary_ellipsoids = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            advCATVO.show_secondary_ellipsoids_type = (
                AdvCATSecondaryEllipsoidsVisibilityType.SHOW_ALL_SECONDARY_ELLIPSOIDS
            )

        advCATVO.show = True
        Assert.assertTrue(advCATVO.show)

        advCATVO.show_primary_ellipsoids = False
        Assert.assertFalse(advCATVO.show_primary_ellipsoids)
        advCATVO.show_primary_ellipsoids = True
        Assert.assertTrue(advCATVO.show_primary_ellipsoids)

        advCATVO.show_secondary_ellipsoids = False
        Assert.assertFalse(advCATVO.show_secondary_ellipsoids)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            advCATVO.show_secondary_ellipsoids_type = (
                AdvCATSecondaryEllipsoidsVisibilityType.SHOW_ALL_SECONDARY_ELLIPSOIDS
            )

        advCATVO.show_secondary_ellipsoids = True
        Assert.assertTrue(advCATVO.show_secondary_ellipsoids)

        advCATVO.show_secondary_ellipsoids_type = AdvCATSecondaryEllipsoidsVisibilityType.SHOW_ALL_SECONDARY_ELLIPSOIDS
        Assert.assertEqual(
            AdvCATSecondaryEllipsoidsVisibilityType.SHOW_ALL_SECONDARY_ELLIPSOIDS,
            advCATVO.show_secondary_ellipsoids_type,
        )
        advCATVO.show_secondary_ellipsoids_type = (
            AdvCATSecondaryEllipsoidsVisibilityType.SHOW_SECONDARY_ELLIPSOIDS_WITH_CONJUNCTIONS
        )
        Assert.assertEqual(
            AdvCATSecondaryEllipsoidsVisibilityType.SHOW_SECONDARY_ELLIPSOIDS_WITH_CONJUNCTIONS,
            advCATVO.show_secondary_ellipsoids_type,
        )

    # endregion
