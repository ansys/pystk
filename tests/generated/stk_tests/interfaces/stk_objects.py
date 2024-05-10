import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from logger import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


# region LinkToObjectHelper
class LinkToObjectHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oLink: "LinkToObject", strObjectName: str):
        Assert.assertIsNotNone(oLink)
        self.m_logger.WriteLine("LinkToObject test:")
        # Name
        self.m_logger.WriteLine5("\tCurrent linked object name is: {0}", oLink.name)
        # IsIntrinsic
        self.m_logger.WriteLine4("\tCurrent IsIntrinsic flag is: {0}", oLink.is_intrinsic)
        # LinkedObject
        oObject: "IStkObject" = oLink.linked_object
        if oObject != None:
            self.m_logger.WriteLine7("\t{0} is linked to: {1}", strObjectName, oObject.path)

        else:
            self.m_logger.WriteLine5("\t{0} is not linked to any objects.", strObjectName)

        # AvailableObjects
        arObjects = oLink.available_objects
        self.m_logger.WriteLine3("\tAvailable Objects array contains: {0} elements", Array.Length(arObjects))
        if Array.Length(arObjects) > 0:
            strObject: str = str(arObjects[0])
            self.m_logger.WriteLine7("\t\tAvailable object {0} is: {1}", 0, strObject)
            # BindTo
            oLink.bind_to(strObject)
            if not oLink.is_intrinsic:
                oObject = oLink.linked_object
                if strObject != "None":
                    if oObject != None:
                        self.m_logger.WriteLine7("\t\t\tNow {0} is linked to: {1}", strObjectName, oObject.path)
                        self.m_logger.WriteLine5("\t\t\tLinked object name is: {0}", oLink.name)
                        self.m_logger.WriteLine4("\t\t\tIsIntrinsic flag is: {0}", oLink.is_intrinsic)

                    else:
                        Assert.assertIsNone(oObject)
                        self.m_logger.WriteLine5("\t\t\tNow {0} is not linked to any other objects.", strObjectName)

            else:
                self.m_logger.WriteLine7(
                    "\t\t\tNow {0} is linked to an intrinsic object {1}.", strObjectName, oLink.name
                )
                self.m_logger.WriteLine4("\t\t\tIsIntrinsic flag is: {0}", oLink.is_intrinsic)

        with pytest.raises(Exception):
            oLink.bind_to("WrongObject")


# endregion


# region STKObjectHelper
class STKObjectHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oObject: "IStkObject"):
        Assert.assertIsNotNone(oObject)
        self.m_logger.WriteLine("----- STK OBJECT TEST ----- BEGIN -----")
        # InstanceName
        strValue: str = oObject.instance_name
        self.m_logger.WriteLine5("\tThe current InstanceName is: {0}", oObject.instance_name)
        oObject.instance_name = "Instance"
        self.m_logger.WriteLine5("\tThe new InstanceName is: {0}", oObject.instance_name)
        Assert.assertEqual("Instance", oObject.instance_name)
        with pytest.raises(Exception):
            oObject.instance_name = ""
        with pytest.raises(Exception):
            oObject.instance_name = "Invalid Name"
        oObject.instance_name = strValue
        self.m_logger.WriteLine5("\tThe new InstanceName is: {0}", oObject.instance_name)
        Assert.assertEqual(strValue, oObject.instance_name)
        # ClassType
        self.m_logger.WriteLine6("\tThe ClassType is: {0}", oObject.class_type)
        # ClassName
        self.m_logger.WriteLine5("\tThe ClassName is: {0}", oObject.class_name)
        # Path
        self.m_logger.WriteLine5("\tThe Path is: {0}", oObject.path)
        if oObject.class_type != STK_OBJECT_TYPE.MTO:
            # ShortDescription
            self.m_logger.WriteLine5("\tThe current ShortDescription is: {0}", oObject.short_description)
            oObject.short_description = "This is a new short description."
            self.m_logger.WriteLine5("\tThe new ShortDescription is: {0}", oObject.short_description)
            Assert.assertEqual("This is a new short description.", oObject.short_description)
            oObject.short_description = ""
            self.m_logger.WriteLine5("\tThe new ShortDescription is: {0}", oObject.short_description)
            Assert.assertEqual("", oObject.short_description)
            # LongDescription
            self.m_logger.WriteLine5("\tThe current LongDescription is: {0}", oObject.long_description)
            oObject.long_description = "This is a new long description."
            self.m_logger.WriteLine5("\tThe new LongDescription is: {0}", oObject.long_description)
            Assert.assertEqual("This is a new long description.", oObject.long_description)
            oObject.long_description = ""
            self.m_logger.WriteLine5("\tThe new LongDescription is: {0}", oObject.long_description)
            Assert.assertEqual("", oObject.long_description)

        # Export
        strValue = oObject.instance_name
        oObject.export(TestBase.GetScenarioFile("Export", "ExportedObject"))
        oObject.instance_name = strValue
        # Parent
        oParent: "IStkObject" = oObject.parent
        Assert.assertIsNotNone(oParent)
        self.m_logger.WriteLine7("\tThe parent object for {0} is {1}", oObject.instance_name, oParent.instance_name)
        # DataProviders

        oDPHelper = DataProviderCollectionHelper()
        oDPHelper.Run(oObject.data_providers)

        # Children
        self.Children(oObject)
        if oObject.is_object_coverage_supported():
            self.m_logger.WriteLine5("\tThe {0} supports an ObjectCoverage.", oObject.instance_name)
            # ObjectCoverage
            oCoverage: "StkObjectCoverage" = oObject.object_coverage
            Assert.assertIsNotNone(oCoverage)
            # DataProviders
            oDPHelper.Run(oCoverage.data_providers)

        else:
            self.m_logger.WriteLine5("\tThe {0} does not support an ObjectCoverage.", oObject.instance_name)
            with pytest.raises(Exception):
                oCoverage: "StkObjectCoverage" = oObject.object_coverage

        # create an additional Satellite
        oSatellite: "Satellite" = Satellite(
            oObject.root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "MIR")
        )
        Assert.assertIsNotNone(oSatellite)
        oSatellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY, oSatellite.propagator_type)
        oPropagator: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(oSatellite.propagator)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.propagate()
        if oObject.is_access_supported():
            self.m_logger.WriteLine5("\tThe {0} supports an Access.", oObject.instance_name)
            # GetAccess
            oAccess: "StkAccess" = oObject.get_access((IStkObject(oSatellite)).path)
            Assert.assertIsNotNone(oAccess)
            oAHelper = StkAccessHelper()
            oAHelper.Run(oAccess, oObject.root)

            # GetAccessToObject
            oAccess = oObject.get_access_to_object(clr.CastAs(oSatellite, IStkObject))
            Assert.assertIsNotNone(oAccess)
            oAHelper.Run(oAccess, oObject.root)

            acc: "AccessConstraintCollection" = oObject.access_constraints
            Assert.assertIsNotNone(acc)
            opa: "OnePointAccess" = oObject.create_one_point_access("Satellite/MIR")
            Assert.assertIsNotNone(opa)

        else:
            self.m_logger.WriteLine5("\tThe {0} does not support an Access.", oObject.instance_name)
            with pytest.raises(Exception):
                oAccess: "StkAccess" = oObject.get_access((IStkObject(oSatellite)).path)
            with pytest.raises(Exception):
                oAccess: "StkAccess" = oObject.get_access_to_object(clr.CastAs(oSatellite, IStkObject))
            with pytest.raises(Exception):
                acc: "AccessConstraintCollection" = oObject.access_constraints
            with pytest.raises(Exception):
                opa: "OnePointAccess" = oObject.create_one_point_access("Satellite/MIR")

        oObject.root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "MIR")
        # Root
        oRoot: "StkObjectRoot" = oObject.root
        Assert.assertIsNotNone(oRoot)

        # Object Files
        self.TestObjectFilesArray(oObject.object_files)
        if (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                ((oObject.class_name != "AdvCAT") and (oObject.class_name != "Chain"))
                                                and (oObject.class_name != "CommSystem")
                                            )
                                            and (oObject.class_name != "Constellation")
                                        )
                                        and (oObject.class_name != "Coverage")
                                    )
                                    and (oObject.class_name != "CoverageDefinition")
                                )
                                and (oObject.class_name != "FigureOfMerit")
                            )
                            and (oObject.class_name != "MTO")
                        )
                        and (oObject.class_name != "Satellite")
                    )
                    and (oObject.class_name != "Scenario")
                )
                and (oObject.class_name != "Sensor")
            )
            and (oObject.class_name != "LineTarget")
        ) and (oObject.class_name != "Volumetric"):
            self.OnePtAccess(oObject)

        self.Metadata(oObject)

        self.m_logger.WriteLine("----- STK OBJECT TEST ----- END -----")

    # endregion

    # region OnePtAccess
    def OnePtAccess(self, oObj: "IStkObject"):
        onePtAccess: "OnePointAccess" = oObj.create_one_point_access("Satellite/Satellite1")
        onePtAccess.start_time = "1 Jul 2007 00:00:00.000"
        Assert.assertEqual("1 Jul 2007 00:00:00.000", onePtAccess.start_time)
        onePtAccess.stop_time = "1 Jul 2007 01:00:00.000"
        Assert.assertEqual("1 Jul 2007 01:00:00.000", onePtAccess.stop_time)
        onePtAccess.step_size = 120
        Assert.assertEqual(120, onePtAccess.step_size)
        onePtAccess.summary_option = ONE_POINT_ACCESS_SUMMARY.DETAILED
        Assert.assertEqual(ONE_POINT_ACCESS_SUMMARY.DETAILED, onePtAccess.summary_option)
        result: "OnePointAccessResult" = None
        results: "OnePointAccessResultCollection" = onePtAccess.compute()

        i: int = 0
        while i < results.count:
            result = results[i]
            self.m_logger.WriteLine2(result.time)
            self.m_logger.WriteLine2(result.access_satisfied)

            j: int = 0
            while j < result.constraints.count:
                constraint: "OnePointAccessConstraint" = result.constraints[j]
                self.dumpOnePtAccessConstraint(constraint)

                j += 1

            i += 1

        r: "OnePointAccessResult"

        for r in results:
            self.m_logger.WriteLine2(r.time)
            self.m_logger.WriteLine2(r.access_satisfied)
            c: "OnePointAccessConstraint"
            for c in r.constraints:
                self.dumpOnePtAccessConstraint(c)

        onePtAccess.summary_option = ONE_POINT_ACCESS_SUMMARY.FAST
        Assert.assertEqual(ONE_POINT_ACCESS_SUMMARY.FAST, onePtAccess.summary_option)
        results = onePtAccess.compute()
        Assert.assertGreater(results.count, 1)
        result = results[0]
        if (oObj.class_name != "Star") and (oObj.class_name != "Planet"):
            Assert.assertEqual(1, result.constraints.count)
            self.dumpOnePtAccessConstraint(result.constraints[0])

        onePtAccess.summary_option = ONE_POINT_ACCESS_SUMMARY.RESULT_ONLY
        Assert.assertEqual(ONE_POINT_ACCESS_SUMMARY.RESULT_ONLY, onePtAccess.summary_option)
        results = onePtAccess.compute()
        Assert.assertGreater(results.count, 1)
        result = results[0]
        Assert.assertEqual(0, result.constraints.count)

        onePtAccess.output_file = r"C:\Dummy\File.out"
        Assert.assertEqual(r"C:\Dummy\File.out", onePtAccess.output_file)
        onePtAccess.output_to_file = True
        Assert.assertTrue(onePtAccess.output_to_file)
        onePtAccess.output_to_file = False
        Assert.assertFalse(onePtAccess.output_to_file)

        onePtAccess.remove()

    # endregion

    def dumpOnePtAccessConstraint(self, constraint: "OnePointAccessConstraint"):
        self.m_logger.WriteLine2(constraint.constraint)
        self.m_logger.WriteLine(constraint.object_path)
        self.m_logger.WriteLine2(constraint.status)
        self.m_logger.WriteLine2(constraint.value)

    def TestObjectFilesArray(self, arrFiles):
        Assert.assertIsNotNone(arrFiles)

        Assert.assertNotEqual(0, Array.Length(arrFiles))
        self.m_logger.WriteLine("Object Files are...")
        file: typing.Any
        for file in arrFiles:
            self.m_logger.WriteLine(("\t" + str(file)))

    # region Children
    def Children(self, oObject: "IStkObject"):
        Assert.assertIsNotNone(oObject)
        # Children
        oCollection: "IStkObjectCollection" = oObject.children
        Assert.assertIsNotNone(oCollection)
        if oCollection.count > 0:
            x: "IStkObject" = oCollection[0]
            name: str = x.instance_name
            y: "IStkObject" = oCollection.get_item_by_index(0)
            z: "IStkObject" = oCollection.get_item_by_name(name)
            Assert.assertEqual(x.instance_name, y.instance_name)
            Assert.assertEqual(x.instance_name, z.instance_name)

        # HasChildren
        self.m_logger.WriteLine4("\tThe HasChildren flag is: {0}", oObject.has_children)
        # Count
        self.m_logger.WriteLine7("\tThe {0} has: {1} children", oObject.instance_name, oCollection.count)
        if oObject.has_children:
            Assert.assertTrue((oCollection.count > 0))

        else:
            Assert.assertTrue((oCollection.count == 0))

        SupportedChildTypes = oObject.children.supported_child_types
        if (
            (
                (
                    (
                        (
                            (
                                (
                                    (oObject.class_type == STK_OBJECT_TYPE.AIRCRAFT)
                                    or (oObject.class_type == STK_OBJECT_TYPE.FACILITY)
                                )
                                or (oObject.class_type == STK_OBJECT_TYPE.GROUND_VEHICLE)
                            )
                            or (oObject.class_type == STK_OBJECT_TYPE.LAUNCH_VEHICLE)
                        )
                        or (oObject.class_type == STK_OBJECT_TYPE.MISSILE)
                    )
                    or (oObject.class_type == STK_OBJECT_TYPE.SATELLITE)
                )
                or (oObject.class_type == STK_OBJECT_TYPE.SHIP)
            )
            or (oObject.class_type == STK_OBJECT_TYPE.TARGET)
        ) or (oObject.class_type == STK_OBJECT_TYPE.SUBMARINE):
            found: bool = False

            j: int = 0
            while j < Array.Length(SupportedChildTypes):
                objType: "STK_OBJECT_TYPE" = (
                    STK_OBJECT_TYPE(int(SupportedChildTypes[j]))
                    if (int(SupportedChildTypes[j]) in [item.value for item in STK_OBJECT_TYPE])
                    else int(SupportedChildTypes[j])
                )
                if objType == STK_OBJECT_TYPE.SENSOR:
                    found = True

                j += 1

            if not found:
                Assert.fail("Sensor should be an available child object of the {0} object", oObject.class_type)

            # New
            oSensor: "IStkObject" = oCollection.new(STK_OBJECT_TYPE.SENSOR, "Radar")
            Assert.assertIsNotNone(oSensor)
            # Unload
            oCollection.unload(STK_OBJECT_TYPE.SENSOR, "Radar")

        if oObject.class_type == STK_OBJECT_TYPE.SCENARIO:
            oCollection.import_object(TestBase.PathCombine(TestBase.GetScenarioRootDir(), "AreaTargetTests", "at2.at"))

        else:
            with pytest.raises(Exception):
                oCollection.import_object(
                    TestBase.PathCombine(TestBase.GetScenarioRootDir(), "AreaTargetTests", "at2.at")
                )

        # _NewEnum
        stkObject1: "IStkObject"
        # _NewEnum
        for stkObject1 in oCollection:
            self.m_logger.WriteLine5("\t\tChildren: {0}", stkObject1.instance_name)

        if oCollection.count > 0:
            # Item
            oEObject: "IStkObject" = oCollection[0]
            Assert.assertIsNotNone(oEObject)

        # GetElements
        oOECollection: "IStkObjectElementCollection" = oCollection.get_elements(STK_OBJECT_TYPE.SENSOR)
        Assert.assertIsNotNone(oOECollection)
        # Count
        self.m_logger.WriteLine3("\tThe ObjectElement collection contains: {0}", oOECollection.count)
        # _NewEnum
        stkObject2: "IStkObject"
        # _NewEnum
        for stkObject2 in oOECollection:
            self.m_logger.WriteLine5("\t\tElement: {0}", stkObject2.instance_name)

        if oOECollection.count > 0:
            # Item
            oEObject: "IStkObject" = oOECollection[0]
            Assert.assertIsNotNone(oEObject)

    # endregion

    # region Metadata
    def Metadata(self, oObject: "IStkObject"):
        metadata: "KeyValueCollection" = oObject.metadata

        Assert.assertEqual(0, metadata.count)

        metadata.set("Key1", "Value1")
        metadata.set("Key2", "Value2")
        metadata.set("Key3", "")
        Assert.assertEqual(3, metadata.count)
        Assert.assertEqual("Value1", metadata["Key1"])
        Assert.assertEqual("Value2", metadata["Key2"])
        Assert.assertEqual("", metadata["Key3"])

        Assert.assertFalse(metadata.get_read_only("Key1"))

        metadata.set_read_only("Key1", True)
        Assert.assertTrue(metadata.get_read_only("Key1"))
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            metadata.set("Key1", "Changed1")

        metadata.set_read_only("Key1", False)
        Assert.assertFalse(metadata.get_read_only("Key1"))
        metadata.set("Key1", "Changed1")
        Assert.assertEqual("Changed1", metadata["Key1"])

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            metadata.set_read_only("BogusKey", True)

        with pytest.raises(Exception, match=RegexSubstringMatch("empty string")):
            metadata.set("", "Value1")

        metadata.set("Key1", "Changed1")
        metadata.set("Key2", "Changed2")
        metadata.set("Key3", "Changed3")
        Assert.assertEqual("Changed1", metadata["Key1"])
        Assert.assertEqual("Changed2", metadata["Key2"])
        Assert.assertEqual("Changed3", metadata["Key3"])

        key: str

        for key in metadata:
            Assert.assertTrue((len(metadata[key]) > 5))
            Assert.assertTrue(metadata.contains(key))

        # Testing the keys property
        keys = metadata.keys
        Assert.assertEqual(metadata.count, Array.Length(keys))

        i: int = 0
        while i < Array.Length(keys):
            key: str = str(keys[i])
            Assert.assertTrue((len(metadata[key]) > 5))
            Assert.assertTrue(metadata.contains(key))

            i += 1

        Assert.assertFalse(metadata.contains("Key4"))
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            dummy: str = metadata["Key4"]

        metadata.remove_key("Key2")
        Assert.assertEqual(2, metadata.count)
        Assert.assertEqual("Changed1", metadata["Key1"])
        Assert.assertEqual("Changed3", metadata["Key3"])

        metadata.remove_all()
        Assert.assertEqual(0, metadata.count)


# endregion


# region DataProviderCollectionHelper
class DataProviderCollectionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "DataProviderCollection"):
        self.m_logger.WriteLine("----- DATA PROVIDER COLLECTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\tThe DataProvider collection contains: {0} elements.", oCollection.count)
        if oCollection.count > 0:
            x: "IDataProviderInfo" = oCollection[0]
            name: str = x.name
            y: "IDataProviderInfo" = oCollection.get_item_by_index(0)
            z: "IDataProviderInfo" = oCollection.get_item_by_name(name)
            Assert.assertEqual(x.name, y.name)
            Assert.assertEqual(x.name, z.name)

        # _NewEnum
        oDPInfo: "IDataProviderInfo"

        # _NewEnum
        for oDPInfo in oCollection:
            self.m_logger.WriteLine8(
                "\t\tElement: Name = {0}, Type = {1}, IsGroup = {2}", oDPInfo.name, oDPInfo.type, oDPInfo.is_group()
            )

            Assert.assertNotEqual(0, int(oDPInfo.type))

        iIndex: int = 0
        while iIndex < oCollection.count:
            if oCollection[iIndex].is_group():
                self.DataProviderGroup(clr.CastAs(oCollection[iIndex], DataProviderGroup), oCollection[iIndex].name)

            else:
                # we need to use a try-catch block here, because some data providers
                # can't be created without specific settings
                try:
                    # IDataProvider
                    # Console.WriteLine(oCollection[iIndex].Name);
                    self.DataProvider(clr.CastAs(oCollection[iIndex], IDataProvider), oCollection[iIndex].name)
                    if oCollection[iIndex].type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_FIXED:
                        self.DataProviderFixed(
                            clr.CastAs(oCollection[iIndex], DataProviderFixed), oCollection[iIndex].name
                        )
                    elif oCollection[iIndex].type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_INTVL:
                        self.DataProviderInterval(
                            clr.CastAs(oCollection[iIndex], DataProviderInterval), oCollection[iIndex].name
                        )
                    elif ((oCollection[iIndex].type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_TIME_VARYING)) or (
                        (oCollection[iIndex].type == DATA_PROVIDER_TYPE.DATA_PROVIDER_RESULT_INTVL_DEFINED)
                    ):
                        self.DataProviderTimeVar(
                            clr.CastAs(oCollection[iIndex], DataProviderTimeVarying), oCollection[iIndex].name
                        )
                    else:
                        Assert.fail("Invalid type?")

                except AssertionError as e:
                    raise e

                except Exception as e:
                    # Console.WriteLine(e.Message);
                    self.m_logger.WriteLine5("\t\tEXCEPTION: {0}", str(e))

            iIndex += 1

        self.m_logger.WriteLine("----- DATA PROVIDER COLLECTION TEST ----- END -----")

    # endregion

    # region DataProviderGroup
    def DataProviderGroup(self, oGroup: "DataProviderGroup", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER GROUP TEST ({0}) ----- BEGIN -----", strName)
        Assert.assertIsNotNone(oGroup)
        # Group
        oProviders: "DataProviders" = oGroup.group
        Assert.assertIsNotNone(oProviders)
        # Count
        self.m_logger.WriteLine3("\tThe DataProvider collection contains: {0} elements.", oProviders.count)
        # _NewEnum
        oDPInfo: "IDataProviderInfo"
        # _NewEnum
        for oDPInfo in oProviders:
            self.m_logger.WriteLine8(
                "\t\tElement: Name = {0}, Type = {1}, IsGroup = {2}", oDPInfo.name, oDPInfo.type, oDPInfo.is_group()
            )

        iIndex: int = 0
        while iIndex < oProviders.count:
            if oProviders[iIndex].is_group():
                Assert.fail("An unexpected group of DataProviders!")

            iIndex += 1

        self.m_logger.WriteLine5("----- DATA PROVIDER GROUP TEST ({0}) ----- END -----", strName)

    # endregion

    # region DataProvider
    def DataProvider(self, oProvider: "IDataProvider", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER TEST ({0}) ----- BEGIN -----", strName)
        Assert.assertIsNotNone(oProvider)
        # AllowUI
        self.m_logger.WriteLine4("\tThe current AllowUI is: {0}", oProvider.allow_user_interface)
        oProvider.allow_user_interface = False
        self.m_logger.WriteLine4("\tThe new AllowUI is: {0}", oProvider.allow_user_interface)
        Assert.assertFalse(oProvider.allow_user_interface)
        oProvider.allow_user_interface = True
        self.m_logger.WriteLine4("\tThe new AllowUI is: {0}", oProvider.allow_user_interface)
        Assert.assertTrue(oProvider.allow_user_interface)
        # PreData
        self.m_logger.WriteLine5("\tThe current PreData is: {0}", oProvider.pre_data)
        oProvider.pre_data = "Some PreData string"
        self.m_logger.WriteLine5("\tThe new PreData is: {0}", oProvider.pre_data)
        Assert.assertEqual("Some PreData string", oProvider.pre_data)
        oProvider.pre_data = ""
        self.m_logger.WriteLine5("\tThe new PreData is: {0}", oProvider.pre_data)
        Assert.assertEqual("", oProvider.pre_data)
        # Elements
        oElements: "DataProviderElements" = oProvider.elements
        Assert.assertIsNotNone(oElements)
        self.m_logger.WriteLine3("\tThe current Elements collection contains: {0} elements.", oElements.count)
        # _NewEnum
        dataPrvElement: "DataProviderElement"
        # _NewEnum
        for dataPrvElement in oElements:
            self.m_logger.WriteLine8(
                "\t\tElement: Name = {0}, Type = {1}, DimensionName = {2}",
                dataPrvElement.name,
                dataPrvElement.type,
                dataPrvElement.dimension_name,
            )

        iIndex: int = 0
        while iIndex < oElements.count:
            strElementName: str = oElements[iIndex].name
            eType: "DATA_PROVIDER_ELEMENT_TYPE" = oElements[iIndex].type
            Assert.assertFalse(String.IsNullOrEmpty(oElements[iIndex].dimension_name))

            iIndex += 1

        self.m_logger.WriteLine5("----- DATA PROVIDER TEST ({0}) ----- END -----", strName)

    # endregion

    # region DataProviderFixed
    def DataProviderFixed(self, oProvider: "DataProviderFixed", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER FIXED TEST ({0}) ----- BEGIN -----", strName)
        Assert.assertIsNotNone(oProvider)

        # Exec
        oResult: "DataProviderResult" = None
        if (clr.CastAs(oProvider, IDataProvider)).is_valid:
            oResult = oProvider.exec()
            Assert.assertIsNotNone(oResult)

            self.m_logger.WriteLine("\tExec:")
            self.DrResult(oResult)
            arCols = Array.CreateInstance(Type.GetType("System.Object"), oResult.data_sets.count)

            i: int = 0
            while i < oResult.data_sets.count:
                arCols[i] = oResult.data_sets[i].element_name

                i += 1

            oResult = oProvider.exec_elements(arCols)
            Assert.assertIsNotNone(oResult)
            self.m_logger.WriteLine("\tExecElements:")
            self.DrResult(oResult)

        else:
            with pytest.raises(Exception):
                oResult = oProvider.exec()

        self.m_logger.WriteLine5("----- DATA PROVIDER FIXED TEST ({0}) ----- END -----", strName)

    # endregion

    # region DrResult
    def DrResult(self, oResult: "DataProviderResult"):
        Assert.assertIsNotNone(oResult)
        # Category
        self.m_logger.WriteLine6("\t\tThe current Category is: {0}", oResult.category)
        # Sections
        self.DrResultSections(oResult.sections)
        # Intervals
        self.DrResultIntervals(oResult.intervals)
        # DataSets
        self.DrResultDataSets(oResult.data_sets)
        # Message
        self.DrResultMessage(oResult.message)
        if oResult.category == DATA_PROVIDER_RESULT_CATEGORIES.DATA_SET_LIST:
            self.DrResultDataSets(clr.CastAs(oResult.value, DataProviderResultDataSetCollection))
        elif oResult.category == DATA_PROVIDER_RESULT_CATEGORIES.INTERVAL_LIST:
            self.DrResultIntervals(clr.CastAs(oResult.value, DataProviderResultIntervalCollection))
        elif oResult.category == DATA_PROVIDER_RESULT_CATEGORIES.MESSAGE:
            self.DrResultMessage(clr.CastAs(oResult.value, DataProviderResultTextMessage))
        elif oResult.category == DATA_PROVIDER_RESULT_CATEGORIES.SUB_SECTION_LIST:
            self.DrResultSections(clr.CastAs(oResult.value, DataProviderResultSubSectionCollection))
        else:
            Assert.fail("Invalid type!")

    # endregion

    # region DrResultSections
    def DrResultSections(self, oCollection: "DataProviderResultSubSectionCollection"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe SubSection collection contains: {0} elements.", oCollection.count)
        # _NewEnum
        oSection: "DataProviderResultSubSection"
        # _NewEnum
        for oSection in oCollection:
            # Title
            self.m_logger.WriteLine5("\t\t\tElement: Title = {0}", oSection.title)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Intervals
            self.DrResultIntervals(oCollection[iIndex].intervals)

            iIndex += 1

    # endregion

    # region DrResultIntervals
    def DrResultIntervals(self, oCollection: "DataProviderResultIntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe Interval collection contains: {0} elements.", oCollection.count)
        # _NewEnum
        oInterval: "DataProviderResultInterval"
        # _NewEnum
        for oInterval in oCollection:
            # StartTime, StopTime
            self.m_logger.WriteLine7(
                "\t\t\tElement: StartTime = {0}, StopTime = {1}", oInterval.start_time, oInterval.stop_time
            )
            self.m_logger.WriteLine7(
                "\t\t\tElement: StartTime2 = {0}, StopTime2 = {1}", oInterval.start_time, oInterval.stop_time
            )

        if oCollection.count > 0:
            # ThresholdCrossings (see DataProviders.ObjectCoverage test)
            # MultipleThresholdCrossings (see DataProviders.ObjectCoverage test)
            # DataSets
            self.DrResultDataSets(oCollection[0].data_sets)

    # endregion

    # region DrResultDataSets
    def DrResultDataSets(self, oCollection: "DataProviderResultDataSetCollection"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe DataSet collection contains: {0} elements.", oCollection.count)
        # _NewEnum
        oSet: "DataProviderResultDataSet"
        # _NewEnum
        for oSet in oCollection:
            # ElementName, ElementType, Count, UnitType
            self.m_logger.WriteLine9(
                "\t\t\tElement: ElementName = {0}, ElementType = {1}, Count = {2}, DimensionName = {3}",
                oSet.element_name,
                oSet.element_type,
                oSet.count,
                oSet.dimension_name,
            )

        if oCollection.count > 0:
            # GetValues
            arValues = oCollection[0].get_values()
            self.m_logger.WriteLine3("\t\tThe Values array contains: {0} elements.", Array.Length(arValues))
            # GetInternalUnitValues
            arValues = oCollection[0].get_internal_unit_values()
            self.m_logger.WriteLine3("\t\tThe InternalUnitValues array contains: {0} elements.", Array.Length(arValues))

    # endregion

    # region DrResultMessage
    def DrResultMessage(self, oCollection: "DataProviderResultTextMessage"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe TextMessages collection contains: {0} elements.", oCollection.count)
        # _NewEnum
        strText: str
        # _NewEnum
        for strText in oCollection:
            self.m_logger.WriteLine5("\t\t\tElement: {0}", strText)

        # Messages
        arStrings = oCollection.messages
        self.m_logger.WriteLine3("\t\tThe Messages array contains: {0} elements.", Array.Length(arStrings))
        # IsFailure
        self.m_logger.WriteLine4("\t\tThe IsFailure flag is: {0}", oCollection.is_failure)
        if oCollection.count > 0:
            self.m_logger.WriteLine5("\t\tThe first message text string: {0}", oCollection[0])

    # endregion

    # region DataProviderInterval
    def DataProviderInterval(self, oProvider: "DataProviderInterval", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER INTERVAL TEST ({0}) ----- BEGIN -----", strName)
        Assert.assertIsNotNone(oProvider)
        dtStart: typing.Any = "1 Jun 2004 12:00:00.00"
        dtStop: typing.Any = "1 Jun 2004 13:00:00.00"

        # Exec
        oResult: "DataProviderResult" = None
        if (clr.CastAs(oProvider, IDataProvider)).is_valid:
            # Exec
            oResult = oProvider.exec(dtStart, dtStop)
            Assert.assertIsNotNone(oResult)
            self.m_logger.WriteLine("\tExec:")
            self.DrResult(oResult)
            arCols = Array.CreateInstance(Type.GetType("System.Object"), oResult.data_sets.count)

            i: int = 0
            while i < oResult.data_sets.count:
                arCols[i] = oResult.data_sets[i].element_name

                i += 1

            # Array arCols = new object[] { "Time", "y" };
            oResult = oProvider.exec_elements("1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", arCols)
            Assert.assertIsNotNone(oResult)
            self.m_logger.WriteLine("\tExecElements:")
            self.DrResult(oResult)
            self.m_logger.WriteLine5("----- DATA PROVIDER INTERVAL TEST ({0}) ----- END -----", strName)

        else:
            with pytest.raises(Exception):
                oResult = oProvider.exec(dtStart, dtStop)

    # endregion

    # region DataProviderTimeVar
    def DataProviderTimeVar(self, oProvider: "DataProviderTimeVarying", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER TIMEVAR TEST ({0}) ----- BEGIN -----", strName)
        if strName != "User Supplied Data":
            Assert.assertIsNotNone(oProvider)
            dtStart: typing.Any = "1 Jun 2004 12:00:00.00"
            dtStop: typing.Any = "1 Jun 2004 13:00:00.00"
            # Exec
            dp: "IDataProvider" = IDataProvider(oProvider)
            dp.pre_data = "Missile/Missile1"

            oResult: "DataProviderResult" = None
            if (clr.CastAs(oProvider, IDataProvider)).is_valid:
                oResult = oProvider.exec(dtStart, dtStop, 240.0)
                Assert.assertIsNotNone(oResult)
                self.m_logger.WriteLine("\tExec:")
                self.DrResult(oResult)
                arCols = Array.CreateInstance(Type.GetType("System.Object"), oResult.data_sets.count)

                i: int = 0
                while i < oResult.data_sets.count:
                    arCols[i] = oResult.data_sets[i].element_name

                    i += 1

                oResult = oProvider.exec_elements("1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.9, arCols)
                Assert.assertIsNotNone(oResult)
                self.m_logger.WriteLine("\tExecElements:")
                self.DrResult(oResult)
                # ExecSingle
                oResult = oProvider.exec_single(dtStart)
                Assert.assertIsNotNone(oResult)
                self.m_logger.WriteLine("\tExecSingle:")
                self.DrResult(oResult)
                # ExecSingleElements
                oResult = oProvider.exec_single_elements("1 Jun 2004 12:00:00.00", arCols)
                Assert.assertIsNotNone(oResult)
                self.m_logger.WriteLine("\tExecSingleElements:")
                self.DrResult(oResult)

            else:
                with pytest.raises(Exception):
                    oResult = oProvider.exec(dtStart, dtStop, 240.0)

        self.m_logger.WriteLine5("----- DATA PROVIDER TIMEVAR TEST ({0}) ----- END -----", strName)


# endregion


# region StkAccessHelper
class StkAccessHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oAccess: "StkAccess", oRoot: "StkObjectRoot"):
        self.m_logger.WriteLine("----- STK ACCESS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oAccess)
        Assert.assertIsNotNone(oRoot)
        # AccessTimePeriod
        self.m_logger.WriteLine6("\tThe current AccessTimePeriod is: {0}", oAccess.access_time_period)
        oAccess.access_time_period = ACCESS_TIME_TYPE.OBJECT_ACCESS_TIME
        self.m_logger.WriteLine6("\tThe new AccessTimePeriod is: {0}", oAccess.access_time_period)
        Assert.assertEqual(ACCESS_TIME_TYPE.OBJECT_ACCESS_TIME, oAccess.access_time_period)
        # ComputeAccess
        oAccess.compute_access()
        oAccess.access_time_period = ACCESS_TIME_TYPE.SCENARIO_ACCESS_TIME
        self.m_logger.WriteLine6("\tThe new AccessTimePeriod is: {0}", oAccess.access_time_period)
        Assert.assertEqual(ACCESS_TIME_TYPE.SCENARIO_ACCESS_TIME, oAccess.access_time_period)
        oAccess.compute_access()
        oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
        self.m_logger.WriteLine6("\tThe new AccessTimePeriod is: {0}", oAccess.access_time_period)
        Assert.assertEqual(ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME, oAccess.access_time_period)
        oAccess.compute_access()
        # SpecifyAccessTimePeriod
        dtStart: typing.Any = "1 Jul 1999 00:00:00.00"
        dtStop: typing.Any = "1 Jul 1999 00:09:00.00"
        oAccess.specify_access_time_period(dtStart, dtStop)
        oAccess.compute_access()
        if not TestBase.NoGraphicsMode:
            self.Graphics(oAccess.graphics)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                self.Graphics(oAccess.graphics)

        # Advanced
        self.Advanced(oAccess)
        if not TestBase.NoGraphicsMode:
            oDDHelper = VODataDisplayHelper(oRoot)
            oDDHelper.Run(oAccess.data_displays, True, False)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                oDDHelper = VODataDisplayHelper(oRoot)
                oDDHelper.Run(oAccess.data_displays, True, False)

        # DataProviders
        oDPHelper = DataProviderCollectionHelper()
        oDPHelper.Run(oAccess.data_providers)
        # RemoveAccess
        oAccess.remove_access()
        self.m_logger.WriteLine("----- STK ACCESS TEST ----- END -----")

    # endregion

    # region Graphics
    def Graphics(self, oGraphics: "StkAccessGraphics"):
        Assert.assertIsNotNone(oGraphics)
        # Inherit (true)
        self.m_logger.WriteLine4("\tThe current Inherit is: {0}", oGraphics.inherit)
        oGraphics.inherit = True
        self.m_logger.WriteLine4("\tThe new Inherit is: {0}", oGraphics.inherit)
        Assert.assertTrue(oGraphics.inherit)
        # AnimateGfx (readonly)
        with pytest.raises(Exception):
            oGraphics.animate_graphics_2d = True
        # LineVisible (readonly)
        with pytest.raises(Exception):
            oGraphics.line_visible = True
        # StaticGfx (readonly)
        with pytest.raises(Exception):
            oGraphics.static_graphics_2d = True
        # LineWidth (readonly)
        with pytest.raises(Exception):
            oGraphics.line_width = 2
        # LineStyle (readonly)
        with pytest.raises(Exception):
            oGraphics.line_style = "Dashed"
        # Inherit (false)
        oGraphics.inherit = False
        self.m_logger.WriteLine4("\tThe new Inherit is: {0}", oGraphics.inherit)
        Assert.assertFalse(oGraphics.inherit)
        # AnimateGfx
        self.m_logger.WriteLine4("\tThe current AnimateGfx is: {0}", oGraphics.animate_graphics_2d)
        oGraphics.animate_graphics_2d = True
        self.m_logger.WriteLine4("\tThe new AnimateGfx is: {0}", oGraphics.animate_graphics_2d)
        Assert.assertTrue(oGraphics.animate_graphics_2d)
        oGraphics.animate_graphics_2d = False
        self.m_logger.WriteLine4("\tThe new AnimateGfx is: {0}", oGraphics.animate_graphics_2d)
        Assert.assertFalse(oGraphics.animate_graphics_2d)
        # LineVisible
        self.m_logger.WriteLine4("\tThe current LineVisible is: {0}", oGraphics.line_visible)
        oGraphics.line_visible = True
        self.m_logger.WriteLine4("\tThe new LineVisible is: {0}", oGraphics.line_visible)
        Assert.assertTrue(oGraphics.line_visible)
        oGraphics.line_visible = False
        self.m_logger.WriteLine4("\tThe new LineVisible is: {0}", oGraphics.line_visible)
        Assert.assertFalse(oGraphics.line_visible)

        # LineWidth
        # LineVisible is false so LineWidth can't be set (readonly)
        with pytest.raises(Exception):
            oGraphics.line_width = 2
        oGraphics.line_visible = True
        self.m_logger.WriteLine3("\tThe current LineWidth is: {0}", oGraphics.line_width)
        oGraphics.line_width = 2
        self.m_logger.WriteLine3("\tThe new LineWidth is: {0}", oGraphics.line_width)
        Assert.assertTrue((oGraphics.line_width == 2))
        oGraphics.line_width = 1
        self.m_logger.WriteLine3("\tThe new LineWidth is: {0}", oGraphics.line_width)
        Assert.assertTrue((oGraphics.line_width == 1))
        # Restore LineVisible (false)
        oGraphics.line_visible = False

        # LineStyle
        # LineVisible is false so LineStyle can't be set (readonly)
        with pytest.raises(Exception):
            oGraphics.line_style = "Dashed"
        oGraphics.line_visible = True
        self.m_logger.WriteLine5("\tThe current LineStyle is: {0}", oGraphics.line_style)
        oGraphics.line_style = "Dashed"
        self.m_logger.WriteLine5("\tThe new LineStyle is: {0}", oGraphics.line_style)
        Assert.assertEqual(oGraphics.line_style, "Dashed")
        oGraphics.line_style = "Solid"
        self.m_logger.WriteLine5("\tThe new LineStyle is: {0}", oGraphics.line_style)
        Assert.assertEqual(oGraphics.line_style, "Solid")
        # Restore LineVisible (false)
        oGraphics.line_visible = False

        # StaticGfx
        self.m_logger.WriteLine4("\tThe current StaticGfx is: {0}", oGraphics.static_graphics_2d)
        oGraphics.static_graphics_2d = True
        self.m_logger.WriteLine4("\tThe new StaticGfx is: {0}", oGraphics.static_graphics_2d)
        Assert.assertTrue(oGraphics.static_graphics_2d)
        oGraphics.static_graphics_2d = False
        self.m_logger.WriteLine4("\tThe new StaticGfx is: {0}", oGraphics.static_graphics_2d)
        Assert.assertFalse(oGraphics.static_graphics_2d)

    # endregion

    # region Advanced
    def Advanced(self, oAccess: "StkAccess"):
        oAdvanced: "StkAccessAdvanced" = oAccess.advanced
        Assert.assertIsNotNone(oAdvanced)

        # Event Detection
        oAdvanced.use_precise_event_times = True
        Assert.assertTrue(oAdvanced.use_precise_event_times)

        oAdvanced.time_convergence = 0.123
        Assert.assertEqual(0.123, oAdvanced.time_convergence)
        oAdvanced.relative_tolerance = 0.456
        Assert.assertEqual(0.456, oAdvanced.relative_tolerance)
        oAdvanced.absolute_tolerance = 0.789
        Assert.assertEqual(0.789, oAdvanced.absolute_tolerance)

        oAdvanced.use_precise_event_times = False  # Use Samples Only
        Assert.assertFalse(oAdvanced.use_precise_event_times)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oAdvanced.time_convergence = 0.123
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAdvanced.relative_tolerance = 0.456
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAdvanced.absolute_tolerance = 0.789

        # Light Time Delay
        oAdvanced.enable_light_time_delay = False
        Assert.assertFalse(oAdvanced.enable_light_time_delay)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oAdvanced.time_light_delay_convergence = 0.01234
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAdvanced.aberration_type = ABERRATION_TYPE.ANNUAL
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAdvanced.use_default_clock_host_and_signal_sense = False
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAdvanced.clock_host = IV_CLOCK_HOST.BASE
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAdvanced.signal_sense_of_clock_host = IV_TIME_SENSE.TRANSMIT

        oAdvanced.enable_light_time_delay = True
        Assert.assertTrue(oAdvanced.enable_light_time_delay)

        oAdvanced.time_light_delay_convergence = 0.0123
        Assert.assertEqual(0.0123, oAdvanced.time_light_delay_convergence)
        with pytest.raises(Exception):
            oAdvanced.time_light_delay_convergence = 12.34

        oAdvanced.aberration_type = ABERRATION_TYPE.ANNUAL
        Assert.assertEqual(ABERRATION_TYPE.ANNUAL, oAdvanced.aberration_type)
        oAdvanced.aberration_type = ABERRATION_TYPE.NONE
        Assert.assertEqual(ABERRATION_TYPE.NONE, oAdvanced.aberration_type)
        oAdvanced.aberration_type = ABERRATION_TYPE.TOTAL
        Assert.assertEqual(ABERRATION_TYPE.TOTAL, oAdvanced.aberration_type)
        with pytest.raises(Exception):
            oAdvanced.aberration_type = ABERRATION_TYPE.UNKNOWN

        # Signal Path
        oAdvanced.use_default_clock_host_and_signal_sense = True
        Assert.assertTrue(oAdvanced.use_default_clock_host_and_signal_sense)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAdvanced.clock_host = IV_CLOCK_HOST.BASE
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAdvanced.signal_sense_of_clock_host = IV_TIME_SENSE.TRANSMIT

        oAdvanced.use_default_clock_host_and_signal_sense = False
        Assert.assertFalse(oAdvanced.use_default_clock_host_and_signal_sense)

        oAdvanced.clock_host = IV_CLOCK_HOST.BASE
        Assert.assertEqual(IV_CLOCK_HOST.BASE, oAdvanced.clock_host)
        oAdvanced.clock_host = IV_CLOCK_HOST.TARGET
        Assert.assertEqual(IV_CLOCK_HOST.TARGET, oAdvanced.clock_host)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            oAdvanced.signal_sense_of_clock_host = IV_TIME_SENSE.UNKNOWN
        oAdvanced.signal_sense_of_clock_host = IV_TIME_SENSE.TRANSMIT
        Assert.assertEqual(IV_TIME_SENSE.TRANSMIT, oAdvanced.signal_sense_of_clock_host)
        oAdvanced.signal_sense_of_clock_host = IV_TIME_SENSE.RECEIVE
        Assert.assertEqual(IV_TIME_SENSE.RECEIVE, oAdvanced.signal_sense_of_clock_host)

        # Step Size Control
        oAdvanced.use_fixed_time_step = False  # Adaptive
        Assert.assertFalse(oAdvanced.use_fixed_time_step)

        oAdvanced.max_time_step = 123.456
        Assert.assertEqual(123.456, oAdvanced.max_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oAdvanced.max_time_step = 0

        oAdvanced.min_time_step = 456.123
        Assert.assertEqual(456.123, oAdvanced.min_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oAdvanced.min_time_step = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oAdvanced.fixed_step_size = 789
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oAdvanced.fixed_time_bound = 789

        oAdvanced.use_fixed_time_step = True  # Fixed Step
        Assert.assertTrue(oAdvanced.use_fixed_time_step)

        oAdvanced.fixed_step_size = 123.456
        Assert.assertEqual(123.456, oAdvanced.fixed_step_size)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oAdvanced.fixed_step_size = 0

        oAdvanced.fixed_time_bound = 56.123
        Assert.assertEqual(56.123, oAdvanced.fixed_time_bound)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oAdvanced.fixed_time_bound = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oAdvanced.max_time_step = 123.456
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oAdvanced.min_time_step = 56.123

        oAccess.compute_access()  # to make changes show in GUI


# endregion


# region VODataDisplayHelper
class VODataDisplayHelper(object):
    def __init__(self, oRoot: "StkObjectRoot"):
        self.m_bIsAccessRequired: bool = False
        self.m_bIsChain: bool = False
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oRoot)
        self.m_oRoot: "StkObjectRoot" = oRoot

    # endregion

    # region Run method
    def Run(self, oDataCollection: "Graphics3DDataDisplayCollection", bIsAccessRequired: bool, bIsChain: bool):
        self.m_logger.WriteLine("----- THE VO DATA DISPLAY TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oDataCollection)
        # save AccessRequired flag
        self.m_bIsAccessRequired = bIsAccessRequired
        # save IsChain flag
        self.m_bIsChain = bIsChain
        # Count
        iSize: int = oDataCollection.count
        self.m_logger.WriteLine3("The current Data Display collection contains: {0} elements.", iSize)

        iIndex: int = 0
        while iIndex < iSize:
            self.m_logger.WriteLine7("\tElement {0} is: {1}", iIndex, oDataCollection[iIndex].name)

            iIndex += 1

        if oDataCollection.count > 0:
            oDataCollection.remove_at(0)
            self.m_logger.WriteLine3(
                "After Remove(0) the Data Display collection contains: {0} elements.", oDataCollection.count
            )

            iIndex: int = 0
            while iIndex < oDataCollection.count:
                self.m_logger.WriteLine7("\tElement {0} is: {1}", iIndex, oDataCollection[iIndex].name)

                iIndex += 1

            Assert.assertEqual((iSize - 1), oDataCollection.count)

        oDataCollection.remove_all()
        self.m_logger.WriteLine3(
            "After RemoveAll() the Data Display collection contains: {0} elements.", oDataCollection.count
        )
        Assert.assertEqual(0, oDataCollection.count)

        arAvailable = oDataCollection.available_data
        self.m_logger.WriteLine3("Available Data list contains: {0} elements", Array.Length(arAvailable))

        iIndex: int = 0
        while iIndex < Array.Length(arAvailable):
            self.m_logger.WriteLine7("\tAvailable element {0} is: {1}", iIndex, arAvailable[iIndex])

            iIndex += 1

        self.m_oRoot.begin_update()
        self.m_logger.WriteLine3("The current Data Display collection contains: {0} elements.", oDataCollection.count)

        iIndex: int = 0
        while iIndex < Array.Length(arAvailable):
            oDataDisp: "Graphics3DDataDisplayElement" = None
            strAvailable: str = str(arAvailable[iIndex])
            if oDataCollection.is_pre_data_required(strAvailable):
                preData: str = "Missile/Missile1"
                if strAvailable.startswith("Crdn") or ("EphemerisChooseAxes" == strAvailable):
                    preData = "Satellite/Satellite1 Body Axes"

                oDataDisp = oDataCollection.add_data_display_requiring_pre_data(strAvailable, preData)
                Assert.assertIsNotNone(oDataDisp)
                self.m_logger.WriteLine7("\tAdded element: {0} (with PreData - {1})", oDataDisp.name, preData)
                break

            if (not oDataCollection.is_pre_data_required(strAvailable)) and (oDataCollection.count == 0):
                oDataDisp = oDataCollection.add(strAvailable)
                Assert.assertIsNotNone(oDataDisp)
                self.m_logger.WriteLine5("\tAdded element: {0}", oDataDisp.name)

            iIndex += 1

        # Count
        iSize = oDataCollection.count
        self.m_logger.WriteLine3("The new Data Display collection contains: {0} elements.", iSize)
        dataDisplayElement: "Graphics3DDataDisplayElement"
        for dataDisplayElement in oDataCollection:
            self.m_logger.WriteLine5("\tElement: {0}", dataDisplayElement.name)

            self.ElementTest(dataDisplayElement)

        self.m_oRoot.end_update()
        if oDataCollection.count > 0:
            # RemoveAt
            oDataCollection.remove_at(0)
            self.m_logger.WriteLine3(
                "After Remove(0) the Data Display collection contains: {0} elements.", oDataCollection.count
            )
            Assert.assertEqual((iSize - 1), oDataCollection.count)
            dataDisplayElement: "Graphics3DDataDisplayElement"
            for dataDisplayElement in oDataCollection:
                self.m_logger.WriteLine5("\tElement: {0}", dataDisplayElement.name)

        # RemoveAll
        oDataCollection.remove_all()
        self.m_logger.WriteLine3(
            "After RemoveAll() the Data Display collection contains: {0} elements.", oDataCollection.count
        )
        Assert.assertEqual(0, oDataCollection.count)

        self.m_logger.WriteLine("----- THE VO DATA DISPLAY TEST ----- END -----")

    # endregion

    # region ElementTest
    def ElementTest(self, oVODataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)
        # IsVisible
        self.m_logger.WriteLine4("\t\tCurrent IsVisible flag: {0}", oVODataDisplayElement.is_visible)
        oVODataDisplayElement.is_visible = False
        self.m_logger.WriteLine4("\t\tNew IsVisible flag: {0}", oVODataDisplayElement.is_visible)
        Assert.assertFalse(oVODataDisplayElement.is_visible)
        self.NotVisibleCheck(oVODataDisplayElement)

        oVODataDisplayElement.is_visible = True
        self.m_logger.WriteLine4("\t\tNew IsVisible flag: {0}", oVODataDisplayElement.is_visible)
        Assert.assertTrue(oVODataDisplayElement.is_visible)
        self.VisibleCheck(oVODataDisplayElement)

        self.m_logger.WriteLine4("\t\tCurrent UseBackground flag: {0}", oVODataDisplayElement.use_background)
        oVODataDisplayElement.use_background = False
        self.m_logger.WriteLine4("\t\tNew UseBackground flag: {0}", oVODataDisplayElement.use_background)
        Assert.assertFalse(oVODataDisplayElement.use_background)
        self.NotUseBackgroundCheck(oVODataDisplayElement)

        oVODataDisplayElement.use_background = True
        self.m_logger.WriteLine4("\t\tNew UseBackground flag: {0}", oVODataDisplayElement.use_background)
        Assert.assertTrue(oVODataDisplayElement.use_background)
        self.UseBackgroundCheck(oVODataDisplayElement)

        oVODataDisplayElement.use_auto_size_width = False
        oVODataDisplayElement.use_auto_size_height = False
        self.m_logger.WriteLine4("\t\tNew UseAutoSizeWidth flag: {0}", oVODataDisplayElement.use_auto_size_width)
        self.m_logger.WriteLine4("\t\tNew UseAutoSizeHeight flag: {0}", oVODataDisplayElement.use_auto_size_height)
        Assert.assertFalse(oVODataDisplayElement.use_auto_size_width)
        Assert.assertFalse(oVODataDisplayElement.use_auto_size_height)
        self.NotUseAutoSizeCheck(oVODataDisplayElement)

        oVODataDisplayElement.use_auto_size_width = True
        oVODataDisplayElement.use_auto_size_height = True
        self.m_logger.WriteLine4("\t\tNew UseAutoSizeWidth flag: {0}", oVODataDisplayElement.use_auto_size_width)
        self.m_logger.WriteLine4("\t\tNew UseAutoSizeHeight flag: {0}", oVODataDisplayElement.use_auto_size_height)
        Assert.assertTrue(oVODataDisplayElement.use_auto_size_width)
        Assert.assertTrue(oVODataDisplayElement.use_auto_size_height)
        self.UseAutoSizeCheck(oVODataDisplayElement)

        oVODataDisplayElement.use_background_border = False
        self.m_logger.WriteLine4("\t\tNew UseBackgroundBorder flag: {0}", oVODataDisplayElement.use_background_border)
        Assert.assertFalse(oVODataDisplayElement.use_background_border)
        self.NotUseBackgroundBorderCheck(oVODataDisplayElement)

        oVODataDisplayElement.use_background_border = True
        self.m_logger.WriteLine4("\t\tNew UseBackgroundBorder flag: {0}", oVODataDisplayElement.use_background_border)
        Assert.assertTrue(oVODataDisplayElement.use_background_border)
        self.UseBackgroundBorderCheck(oVODataDisplayElement)

        oVODataDisplayElement.use_background_texture = False
        self.m_logger.WriteLine4("\t\tNew UseBackgroundTexture flag: {0}", oVODataDisplayElement.use_background_texture)
        Assert.assertFalse(oVODataDisplayElement.use_background_texture)
        self.NotUseBackgroundTextureCheck(oVODataDisplayElement)

        oVODataDisplayElement.use_background_texture = True
        self.m_logger.WriteLine4("\t\tNew UseBackgroundTexture flag: {0}", oVODataDisplayElement.use_background_texture)
        Assert.assertTrue(oVODataDisplayElement.use_background_texture)
        self.UseBackgroundTextureCheck(oVODataDisplayElement)

        oVODataDisplayElement.title = False
        self.m_logger.WriteLine4("\t\tNew Title flag: {0}", oVODataDisplayElement.title)
        Assert.assertFalse(oVODataDisplayElement.title)
        self.NotUseTitleCheck(oVODataDisplayElement)

        oVODataDisplayElement.title = True
        self.m_logger.WriteLine4("\t\tNew Title flag: {0}", oVODataDisplayElement.title)
        Assert.assertTrue(oVODataDisplayElement.title)
        self.UseTitleCheck(oVODataDisplayElement)

        arAvailableWindows = oVODataDisplayElement.available_windows
        self.m_logger.WriteLine3("\t\tAvailable {0} Windows:", Array.Length(arAvailableWindows))

        i: int = 0
        while i < Array.Length(arAvailableWindows):
            self.m_logger.WriteLine6("\t\t\tWindow: {0}", arAvailableWindows[i])

            i += 1

        Assert.assertEqual(2, Array.Length(arAvailableWindows))

        sAll: str = "All"
        sTitle: str = str(arAvailableWindows[1])
        Assert.assertEqual(True, oVODataDisplayElement.is_displayed_in_window(sAll))
        Assert.assertEqual(False, oVODataDisplayElement.is_displayed_in_window(sTitle))
        oVODataDisplayElement.add_to_window(sTitle)
        Assert.assertEqual(False, oVODataDisplayElement.is_displayed_in_window(sAll))
        Assert.assertEqual(True, oVODataDisplayElement.is_displayed_in_window(sTitle))
        oVODataDisplayElement.remove_from_window(sTitle)
        Assert.assertEqual(True, oVODataDisplayElement.is_displayed_in_window(sAll))
        Assert.assertEqual(False, oVODataDisplayElement.is_displayed_in_window(sTitle))
        oVODataDisplayElement.add_to_window(sTitle)
        Assert.assertEqual(False, oVODataDisplayElement.is_displayed_in_window(sAll))
        Assert.assertEqual(True, oVODataDisplayElement.is_displayed_in_window(sTitle))
        oVODataDisplayElement.add_to_all_windows()
        Assert.assertEqual(True, oVODataDisplayElement.is_displayed_in_window(sAll))
        Assert.assertEqual(False, oVODataDisplayElement.is_displayed_in_window(sTitle))

    # endregion

    # region NotVisibleCheck
    def NotVisibleCheck(self, oVODataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)
        # Location
        with pytest.raises(Exception):
            oVODataDisplayElement.location = GRAPHICS_3D_LOCATION.WINDOW_3D
        # FontColor
        with pytest.raises(Exception):
            oVODataDisplayElement.font_color = Colors.from_argb(11254443)
        # XOrigin
        with pytest.raises(Exception):
            oVODataDisplayElement.x_origin = GRAPHICS_3D_X_ORIGIN.X_ORIGIN_LEFT
        # YOrigin
        with pytest.raises(Exception):
            oVODataDisplayElement.y_origin = GRAPHICS_3D_Y_ORIGIN.Y_ORIGIN_BOTTOM
        # X
        with pytest.raises(Exception):
            oVODataDisplayElement.x = 12
        # Y
        with pytest.raises(Exception):
            oVODataDisplayElement.y = 21
        # Title
        with pytest.raises(Exception):
            oVODataDisplayElement.title = True
        # FontSize
        with pytest.raises(Exception):
            oVODataDisplayElement.font_size = GRAPHICS_3D_FONT_SIZE.SMALL
        # Format
        with pytest.raises(Exception):
            oVODataDisplayElement.format = GRAPHICS_3D_FORMAT.HORIZONTAL
        # UseBackground
        with pytest.raises(Exception):
            oVODataDisplayElement.use_background = True
        # TransparentBg
        with pytest.raises(Exception):
            oVODataDisplayElement.transparent_bg = True
        # BgWidth
        with pytest.raises(Exception):
            oVODataDisplayElement.bg_width = 34
        # BgHeight
        with pytest.raises(Exception):
            oVODataDisplayElement.bg_height = 43
        # BgColor
        with pytest.raises(Exception):
            oVODataDisplayElement.bg_color = Colors.from_argb(13491405)

    # endregion

    # region VisibleCheck
    def VisibleCheck(self, oVODataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)
        # Location
        self.m_logger.WriteLine6("\t\t\tThe current Location is: {0}", oVODataDisplayElement.location)
        if self.m_bIsAccessRequired:
            oVODataDisplayElement.location = GRAPHICS_3D_LOCATION.OFFSET_FROM_ACCESS_OBJECT
            self.m_logger.WriteLine6("\t\t\tThe new Location is: {0}", oVODataDisplayElement.location)
            Assert.assertEqual(GRAPHICS_3D_LOCATION.OFFSET_FROM_ACCESS_OBJECT, oVODataDisplayElement.location)

        else:
            with pytest.raises(Exception):
                oVODataDisplayElement.location = GRAPHICS_3D_LOCATION.OFFSET_FROM_ACCESS_OBJECT

        if self.m_bIsChain:
            with pytest.raises(Exception):
                oVODataDisplayElement.location = GRAPHICS_3D_LOCATION.OFFSET_FROM_OBJECT

        else:
            oVODataDisplayElement.location = GRAPHICS_3D_LOCATION.OFFSET_FROM_OBJECT
            self.m_logger.WriteLine6("\t\t\tThe new Location is: {0}", oVODataDisplayElement.location)
            Assert.assertEqual(GRAPHICS_3D_LOCATION.OFFSET_FROM_OBJECT, oVODataDisplayElement.location)

        oVODataDisplayElement.location = GRAPHICS_3D_LOCATION.DATA_DISPLAY_AREA
        self.m_logger.WriteLine6("\t\t\tThe new Location is: {0}", oVODataDisplayElement.location)
        Assert.assertEqual(GRAPHICS_3D_LOCATION.DATA_DISPLAY_AREA, oVODataDisplayElement.location)
        oVODataDisplayElement.location = GRAPHICS_3D_LOCATION.WINDOW_3D
        self.m_logger.WriteLine6("\t\t\tThe new Location is: {0}", oVODataDisplayElement.location)
        Assert.assertEqual(GRAPHICS_3D_LOCATION.WINDOW_3D, oVODataDisplayElement.location)
        # Font Color
        self.m_logger.WriteLine6("\t\t\tThe current Font Color is: {0}", oVODataDisplayElement.font_color)
        oVODataDisplayElement.font_color = Colors.from_argb(65280)
        self.m_logger.WriteLine6("\t\t\tThe new Font Color is: {0}", oVODataDisplayElement.font_color)
        AssertEx.AreEqual(Colors.from_argb(65280), oVODataDisplayElement.font_color)
        # XOrigin
        self.m_logger.WriteLine6("\t\t\tThe current X Origin is: {0}", oVODataDisplayElement.x_origin)
        oVODataDisplayElement.x_origin = GRAPHICS_3D_X_ORIGIN.X_ORIGIN_LEFT
        self.m_logger.WriteLine6("\t\t\tThe new X Origin is: {0}", oVODataDisplayElement.x_origin)
        Assert.assertEqual(GRAPHICS_3D_X_ORIGIN.X_ORIGIN_LEFT, oVODataDisplayElement.x_origin)
        oVODataDisplayElement.x_origin = GRAPHICS_3D_X_ORIGIN.X_ORIGIN_RIGHT
        self.m_logger.WriteLine6("\t\t\tThe new X Origin is: {0}", oVODataDisplayElement.x_origin)
        Assert.assertEqual(GRAPHICS_3D_X_ORIGIN.X_ORIGIN_RIGHT, oVODataDisplayElement.x_origin)
        # YOrigin
        self.m_logger.WriteLine6("\t\t\tThe current Y Origin is: {0}", oVODataDisplayElement.y_origin)
        oVODataDisplayElement.y_origin = GRAPHICS_3D_Y_ORIGIN.Y_ORIGIN_TOP
        self.m_logger.WriteLine6("\t\t\tThe new Y Origin is: {0}", oVODataDisplayElement.y_origin)
        Assert.assertEqual(GRAPHICS_3D_Y_ORIGIN.Y_ORIGIN_TOP, oVODataDisplayElement.y_origin)
        oVODataDisplayElement.y_origin = GRAPHICS_3D_Y_ORIGIN.Y_ORIGIN_BOTTOM
        self.m_logger.WriteLine6("\t\t\tThe new Y Origin is: {0}", oVODataDisplayElement.y_origin)
        Assert.assertEqual(GRAPHICS_3D_Y_ORIGIN.Y_ORIGIN_BOTTOM, oVODataDisplayElement.y_origin)
        # X
        self.m_logger.WriteLine3("\t\t\tThe current X is: {0}", oVODataDisplayElement.x)
        oVODataDisplayElement.x = 12
        self.m_logger.WriteLine3("\t\t\tThe new X is: {0}", oVODataDisplayElement.x)
        Assert.assertEqual(12, oVODataDisplayElement.x)
        # Y
        self.m_logger.WriteLine3("\t\t\tThe current Y is: {0}", oVODataDisplayElement.y)
        oVODataDisplayElement.y = 21
        self.m_logger.WriteLine3("\t\t\tThe new Y is: {0}", oVODataDisplayElement.y)
        Assert.assertEqual(21, oVODataDisplayElement.y)
        # Title
        self.m_logger.WriteLine4("\t\t\tThe current Title is: {0}", oVODataDisplayElement.title)
        oVODataDisplayElement.title = False
        self.m_logger.WriteLine4("\t\t\tThe new Title is: {0}", oVODataDisplayElement.title)
        Assert.assertEqual(False, oVODataDisplayElement.title)
        oVODataDisplayElement.title = True
        self.m_logger.WriteLine4("\t\t\tThe new Title is: {0}", oVODataDisplayElement.title)
        Assert.assertEqual(True, oVODataDisplayElement.title)
        # FontSize
        self.m_logger.WriteLine6("\t\t\tThe current Font Size is: {0}", oVODataDisplayElement.font_size)
        oVODataDisplayElement.font_size = GRAPHICS_3D_FONT_SIZE.LARGE
        self.m_logger.WriteLine6("\t\t\tThe new Font Size is: {0}", oVODataDisplayElement.font_size)
        Assert.assertEqual(GRAPHICS_3D_FONT_SIZE.LARGE, oVODataDisplayElement.font_size)
        oVODataDisplayElement.font_size = GRAPHICS_3D_FONT_SIZE.SMALL
        self.m_logger.WriteLine6("\t\t\tThe new Font Size is: {0}", oVODataDisplayElement.font_size)
        Assert.assertEqual(GRAPHICS_3D_FONT_SIZE.SMALL, oVODataDisplayElement.font_size)
        oVODataDisplayElement.font_size = GRAPHICS_3D_FONT_SIZE.MEDIUM
        self.m_logger.WriteLine6("\t\t\tThe new Font Size is: {0}", oVODataDisplayElement.font_size)
        Assert.assertEqual(GRAPHICS_3D_FONT_SIZE.MEDIUM, oVODataDisplayElement.font_size)
        # Format
        self.m_logger.WriteLine6("\t\t\tThe current Font Format is: {0}", oVODataDisplayElement.format)
        oVODataDisplayElement.format = GRAPHICS_3D_FORMAT.HORIZONTAL
        self.m_logger.WriteLine6("\t\t\tThe new Font Format is: {0}", oVODataDisplayElement.format)
        Assert.assertEqual(GRAPHICS_3D_FORMAT.HORIZONTAL, oVODataDisplayElement.format)
        oVODataDisplayElement.format = GRAPHICS_3D_FORMAT.NO_LABELS
        self.m_logger.WriteLine6("\t\t\tThe new Font Format is: {0}", oVODataDisplayElement.format)
        Assert.assertEqual(GRAPHICS_3D_FORMAT.NO_LABELS, oVODataDisplayElement.format)
        oVODataDisplayElement.format = GRAPHICS_3D_FORMAT.VERTICAL
        self.m_logger.WriteLine6("\t\t\tThe new Font Format is: {0}", oVODataDisplayElement.format)
        Assert.assertEqual(GRAPHICS_3D_FORMAT.VERTICAL, oVODataDisplayElement.format)

    # endregion

    # region NotUseBackgroundCheck
    def NotUseBackgroundCheck(self, oVODataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)
        # TransparentBg
        with pytest.raises(Exception):
            oVODataDisplayElement.transparent_bg = True
        # BackgroundTranslucency
        with pytest.raises(Exception):
            oVODataDisplayElement.background_translucency = 0.33
        # UseBackgroundTexture
        with pytest.raises(Exception):
            oVODataDisplayElement.use_background_texture = True
        # BackgroundTextureFileName
        with pytest.raises(Exception):
            oVODataDisplayElement.background_texture_filename = "foo.png"
        # UseBackgroundBorder
        with pytest.raises(Exception):
            oVODataDisplayElement.use_background_border = True
        # BackgroundBorderColor
        with pytest.raises(Exception):
            oVODataDisplayElement.background_border_color = Colors.from_argb(13491405)
        # UseAutoSizeWidth
        with pytest.raises(Exception):
            oVODataDisplayElement.use_auto_size_width = True
        # UseAutoSizeHeight
        with pytest.raises(Exception):
            oVODataDisplayElement.use_auto_size_height = True
        # BgColor
        with pytest.raises(Exception):
            oVODataDisplayElement.bg_color = Colors.from_argb(13491405)

    # endregion

    # region UseBackgroundCheck
    def UseBackgroundCheck(self, oVODataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)
        # TransparentBg
        self.m_logger.WriteLine4(
            "\t\t\tThe current Background Transparency is: {0}", oVODataDisplayElement.transparent_bg
        )
        oVODataDisplayElement.transparent_bg = False
        self.m_logger.WriteLine4("\t\t\tThe new Background Transparency is: {0}", oVODataDisplayElement.transparent_bg)
        Assert.assertEqual(False, oVODataDisplayElement.transparent_bg)
        oVODataDisplayElement.transparent_bg = True
        self.m_logger.WriteLine4("\t\t\tThe new Background Transparency is: {0}", oVODataDisplayElement.transparent_bg)
        Assert.assertEqual(True, oVODataDisplayElement.transparent_bg)
        # UseAutoSizeWidth
        self.m_logger.WriteLine4(
            "\t\t\tThe current Background UseAutoSizeWidth is: {0}", oVODataDisplayElement.use_auto_size_width
        )
        oVODataDisplayElement.use_auto_size_width = False
        self.m_logger.WriteLine4("\t\t\tThe new Background Width is: {0}", oVODataDisplayElement.use_auto_size_width)
        Assert.assertEqual(False, oVODataDisplayElement.use_auto_size_width)
        # UseAutoSizeHeight
        self.m_logger.WriteLine4(
            "\t\t\tThe current Background UseAutoSizeHeight is: {0}", oVODataDisplayElement.use_auto_size_height
        )
        oVODataDisplayElement.use_auto_size_height = False
        self.m_logger.WriteLine4(
            "\t\t\tThe new Background UseAutoSizeHeight is: {0}", oVODataDisplayElement.use_auto_size_height
        )
        Assert.assertEqual(False, oVODataDisplayElement.use_auto_size_height)
        # BgWidth
        self.m_logger.WriteLine3("\t\t\tThe current Background Width is: {0}", oVODataDisplayElement.bg_width)
        oVODataDisplayElement.bg_width = 34
        self.m_logger.WriteLine3("\t\t\tThe new Background Width is: {0}", oVODataDisplayElement.bg_width)
        Assert.assertEqual(34, oVODataDisplayElement.bg_width)
        # BgHeight
        self.m_logger.WriteLine3("\t\t\tThe current Background Height is: {0}", oVODataDisplayElement.bg_height)
        oVODataDisplayElement.bg_height = 12
        self.m_logger.WriteLine3("\t\t\tThe new Background Height is: {0}", oVODataDisplayElement.bg_height)
        Assert.assertEqual(12, oVODataDisplayElement.bg_height)
        # BgColor
        self.m_logger.WriteLine6("\t\t\tThe current Background Color is: {0}", oVODataDisplayElement.bg_color)
        oVODataDisplayElement.bg_color = Colors.from_argb(255)
        self.m_logger.WriteLine6("\t\t\tThe new Background Color is: {0}", oVODataDisplayElement.bg_color)
        AssertEx.AreEqual(Colors.from_argb(255), oVODataDisplayElement.bg_color)
        # UseBackgroundBorder
        self.m_logger.WriteLine4("\t\t\tThe new Background Border is: {0}", oVODataDisplayElement.use_background_border)
        Assert.assertEqual(False, oVODataDisplayElement.use_background_border)
        oVODataDisplayElement.use_background_border = True
        self.m_logger.WriteLine4("\t\t\tThe new Background Border is: {0}", oVODataDisplayElement.use_background_border)
        Assert.assertEqual(True, oVODataDisplayElement.use_background_border)
        # BackgroundBorderColor
        self.m_logger.WriteLine6(
            "\t\t\tThe current Background Color is: {0}", oVODataDisplayElement.background_border_color
        )
        oVODataDisplayElement.background_border_color = Colors.from_argb(255)
        self.m_logger.WriteLine6(
            "\t\t\tThe new Background Border Color is: {0}", oVODataDisplayElement.background_border_color
        )
        AssertEx.AreEqual(Colors.from_argb(255), oVODataDisplayElement.background_border_color)
        # UseBackgroundTexture
        self.m_logger.WriteLine4(
            "\t\t\tThe new Background Texture is: {0}", oVODataDisplayElement.use_background_texture
        )
        Assert.assertEqual(False, oVODataDisplayElement.use_background_texture)
        oVODataDisplayElement.use_background_texture = True
        self.m_logger.WriteLine4(
            "\t\t\tThe new Background Texture is: {0}", oVODataDisplayElement.use_background_texture
        )
        Assert.assertEqual(True, oVODataDisplayElement.use_background_texture)
        # BackgroundTextureFileName
        self.m_logger.WriteLine5(
            "\t\t\tThe new Background Texture is: {0}", oVODataDisplayElement.background_texture_filename
        )
        Assert.assertEqual("", oVODataDisplayElement.background_texture_filename)

        oVODataDisplayElement.background_texture_filename = TestBase.GetScenarioFile("Fire.bmp")
        self.m_logger.WriteLine5(
            "\t\t\tThe new Background Texture is: {0}", oVODataDisplayElement.background_texture_filename
        )
        StringAssert.Contains("Fire.bmp", oVODataDisplayElement.background_texture_filename)

    # endregion

    # region NotUseTitleCheck
    def NotUseTitleCheck(self, oDataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # TitleText
        with pytest.raises(Exception):
            oDataDisplayElement.title_text = "New Title"
        # IsShowNameEnabled
        with pytest.raises(Exception):
            oDataDisplayElement.is_show_name_enabled = False

    # endregion

    # region UseTitleCheck
    def UseTitleCheck(self, oDataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # TitleText
        self.m_logger.WriteLine5("\t\t\tThe current TitleText is: {0}", oDataDisplayElement.title_text)
        oldTitle: str = oDataDisplayElement.title_text
        oDataDisplayElement.title_text = "foobar"
        self.m_logger.WriteLine5("\t\t\tThe new TitleText is: {0}", oDataDisplayElement.title_text)
        Assert.assertEqual("foobar", oDataDisplayElement.title_text)
        oDataDisplayElement.title_text = oldTitle
        # IsShowNameEnabled
        self.m_logger.WriteLine4(
            "\t\t\tThe current IsShowNameEnabled is: {0}", oDataDisplayElement.is_show_name_enabled
        )
        oDataDisplayElement.is_show_name_enabled = False
        self.m_logger.WriteLine4("\t\t\tThe new IsShowNameEnabled is: {0}", oDataDisplayElement.is_show_name_enabled)
        Assert.assertEqual(False, oDataDisplayElement.is_show_name_enabled)

    # endregion

    # region NotUseAutoSizeCheck
    def NotUseAutoSizeCheck(self, oDataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # BgWidth
        self.m_logger.WriteLine3("\t\t\tThe current BgWidth is: {0}", oDataDisplayElement.bg_width)
        oDataDisplayElement.bg_width = 300
        self.m_logger.WriteLine3("\t\t\tThe new BgWidth is: {0}", oDataDisplayElement.bg_width)
        Assert.assertEqual(300, oDataDisplayElement.bg_width)
        # BgHeight
        self.m_logger.WriteLine3("\t\t\tThe current BgHeight is: {0}", oDataDisplayElement.bg_height)
        oDataDisplayElement.bg_height = 150
        self.m_logger.WriteLine3("\t\t\tThe new BgHeight is: {0}", oDataDisplayElement.bg_height)
        Assert.assertEqual(150, oDataDisplayElement.bg_height)

    # endregion

    # region UseAutoSizeCheck
    def UseAutoSizeCheck(self, oDataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        with pytest.raises(Exception):
            oDataDisplayElement.bg_width = 500
        with pytest.raises(Exception):
            oDataDisplayElement.bg_height = 500

    # endregion

    # region NotUseBackgroundBorderCheck
    def NotUseBackgroundBorderCheck(self, oDataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # BackgroundBorderColor
        with pytest.raises(Exception):
            oDataDisplayElement.background_border_color = Colors.Black

    # endregion

    # region UseBackgroundBorderCheck
    def UseBackgroundBorderCheck(self, oDataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # BackgroundBorderColor
        self.m_logger.WriteLine6(
            "\t\t\tThe current BackgroundBorderColor is: {0}", oDataDisplayElement.background_border_color
        )
        oDataDisplayElement.background_border_color = Colors.Black
        self.m_logger.WriteLine6(
            "\t\t\tThe new BackgroundBorderColor is: {0}", oDataDisplayElement.background_border_color
        )
        Assert.assertEqual(Colors.Black, oDataDisplayElement.background_border_color)

    # endregion

    # region NotUseBackgroundTextureCheck
    def NotUseBackgroundTextureCheck(self, oDataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # BackgroundTextureFileName
        with pytest.raises(Exception):
            oDataDisplayElement.background_texture_filename = "foo.png"

    # endregion

    # region UseBackgroundTextureCheck
    def UseBackgroundTextureCheck(self, oDataDisplayElement: "Graphics3DDataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # BackgroundTextureFileName
        self.m_logger.WriteLine5(
            "\t\t\tThe current BackgroundTextureFileName is: {0}", oDataDisplayElement.background_texture_filename
        )
        oDataDisplayElement.background_texture_filename = "Scenario\\Fire.bmp"
        self.m_logger.WriteLine5(
            "\t\t\tThe new BackgroundTextureFileName is: {0}", oDataDisplayElement.background_texture_filename
        )
        StringAssert.Contains("Fire.bmp", oDataDisplayElement.background_texture_filename)

    # endregion
