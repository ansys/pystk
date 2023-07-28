from test_util import *
from assert_extension import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects import *


# region LinkToObjectHelper
class LinkToObjectHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oLink: "ILinkToObject", strObjectName: str):
        Assert.assertIsNotNone(oLink)
        self.m_logger.WriteLine("LinkToObject test:")
        # Name
        self.m_logger.WriteLine5("\tCurrent linked object name is: {0}", oLink.Name)
        # IsIntrinsic
        self.m_logger.WriteLine4("\tCurrent IsIntrinsic flag is: {0}", oLink.IsIntrinsic)
        # LinkedObject
        oObject = oLink.LinkedObject
        if oObject != None:
            self.m_logger.WriteLine7("\t{0} is linked to: {1}", strObjectName, oObject.Path)

        else:
            self.m_logger.WriteLine5("\t{0} is not linked to any objects.", strObjectName)

        # AvailableObjects
        arObjects = oLink.AvailableObjects
        self.m_logger.WriteLine3("\tAvailable Objects array contains: {0} elements", Array.Length(arObjects))
        if Array.Length(arObjects) > 0:
            strObject = str(arObjects[0])
            self.m_logger.WriteLine7("\t\tAvailable object {0} is: {1}", 0, strObject)
            # BindTo
            oLink.BindTo(strObject)
            if not oLink.IsIntrinsic:
                oObject = oLink.LinkedObject
                if strObject != "None":
                    if oObject != None:
                        self.m_logger.WriteLine7("\t\t\tNow {0} is linked to: {1}", strObjectName, oObject.Path)
                        self.m_logger.WriteLine5("\t\t\tLinked object name is: {0}", oLink.Name)
                        self.m_logger.WriteLine4("\t\t\tIsIntrinsic flag is: {0}", oLink.IsIntrinsic)

                    else:
                        Assert.assertIsNone(oObject)
                        self.m_logger.WriteLine5("\t\t\tNow {0} is not linked to any other objects.", strObjectName)

            else:
                self.m_logger.WriteLine7(
                    "\t\t\tNow {0} is linked to an intrinsic object {1}.", strObjectName, oLink.Name
                )
                self.m_logger.WriteLine4("\t\t\tIsIntrinsic flag is: {0}", oLink.IsIntrinsic)

        def action1():
            oLink.BindTo("WrongObject")

        TryCatchAssertBlock.DoAssert("", action1)


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
        strValue = oObject.InstanceName
        self.m_logger.WriteLine5("\tThe current InstanceName is: {0}", oObject.InstanceName)
        oObject.InstanceName = "Instance"
        self.m_logger.WriteLine5("\tThe new InstanceName is: {0}", oObject.InstanceName)
        Assert.assertEqual("Instance", oObject.InstanceName)

        def action2():
            oObject.InstanceName = ""

        TryCatchAssertBlock.DoAssert("", action2)

        def action3():
            oObject.InstanceName = "Invalid Name"

        TryCatchAssertBlock.DoAssert("", action3)
        oObject.InstanceName = strValue
        self.m_logger.WriteLine5("\tThe new InstanceName is: {0}", oObject.InstanceName)
        Assert.assertEqual(strValue, oObject.InstanceName)
        # ClassType
        self.m_logger.WriteLine6("\tThe ClassType is: {0}", oObject.ClassType)
        # ClassName
        self.m_logger.WriteLine5("\tThe ClassName is: {0}", oObject.ClassName)
        # Path
        self.m_logger.WriteLine5("\tThe Path is: {0}", oObject.Path)
        if oObject.ClassType != AgESTKObjectType.eMTO:
            # ShortDescription
            self.m_logger.WriteLine5("\tThe current ShortDescription is: {0}", oObject.ShortDescription)
            oObject.ShortDescription = "This is a new short description."
            self.m_logger.WriteLine5("\tThe new ShortDescription is: {0}", oObject.ShortDescription)
            Assert.assertEqual("This is a new short description.", oObject.ShortDescription)
            oObject.ShortDescription = ""
            self.m_logger.WriteLine5("\tThe new ShortDescription is: {0}", oObject.ShortDescription)
            Assert.assertEqual("", oObject.ShortDescription)
            # LongDescription
            self.m_logger.WriteLine5("\tThe current LongDescription is: {0}", oObject.LongDescription)
            oObject.LongDescription = "This is a new long description."
            self.m_logger.WriteLine5("\tThe new LongDescription is: {0}", oObject.LongDescription)
            Assert.assertEqual("This is a new long description.", oObject.LongDescription)
            oObject.LongDescription = ""
            self.m_logger.WriteLine5("\tThe new LongDescription is: {0}", oObject.LongDescription)
            Assert.assertEqual("", oObject.LongDescription)

        # Export
        strValue = oObject.InstanceName
        oObject.Export(TestBase.GetScenarioFile(Path.Combine("Export", "ExportedObject")))
        oObject.InstanceName = strValue
        # Parent
        oParent = oObject.Parent
        Assert.assertIsNotNone(oParent)
        self.m_logger.WriteLine7("\tThe parent object for {0} is {1}", oObject.InstanceName, oParent.InstanceName)
        # DataProviders

        oDPHelper = DataProviderCollectionHelper()
        oDPHelper.Run(oObject.DataProviders)

        # Children
        self.Children(oObject)
        if oObject.IsObjectCoverageSupported():
            self.m_logger.WriteLine5("\tThe {0} supports an ObjectCoverage.", oObject.InstanceName)
            # ObjectCoverage
            oCoverage = oObject.ObjectCoverage
            Assert.assertIsNotNone(oCoverage)
            # DataProviders
            oDPHelper.Run(oCoverage.DataProviders)

        else:
            self.m_logger.WriteLine5("\tThe {0} does not support an ObjectCoverage.", oObject.InstanceName)

            def action4():
                oCoverage = oObject.ObjectCoverage

            TryCatchAssertBlock.DoAssert("", action4)

        # create an additional Satellite
        oSatellite = clr.Convert(
            oObject.Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "MIR"), ISatellite
        )
        Assert.assertIsNotNone(oSatellite)
        oSatellite.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        Assert.assertEqual(AgEVePropagatorType.ePropagatorTwoBody, oSatellite.PropagatorType)
        oPropagator = clr.Convert(oSatellite.Propagator, IVehiclePropagatorTwoBody)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.Propagate()
        if oObject.IsAccessSupported():
            self.m_logger.WriteLine5("\tThe {0} supports an Access.", oObject.InstanceName)
            # GetAccess
            oAccess = oObject.GetAccess((clr.Convert(oSatellite, IStkObject)).Path)
            Assert.assertIsNotNone(oAccess)
            oAHelper = StkAccessHelper()
            oAHelper.Run(oAccess, oObject.Root)

            # GetAccessToObject
            oAccess = oObject.GetAccessToObject(clr.CastAs(oSatellite, IStkObject))
            Assert.assertIsNotNone(oAccess)
            oAHelper.Run(oAccess, oObject.Root)

            acc = oObject.AccessConstraints
            Assert.assertIsNotNone(acc)
            opa = oObject.CreateOnePointAccess("Satellite/MIR")
            Assert.assertIsNotNone(opa)

        else:
            self.m_logger.WriteLine5("\tThe {0} does not support an Access.", oObject.InstanceName)

            def action5():
                oAccess = oObject.GetAccess((clr.Convert(oSatellite, IStkObject)).Path)

            TryCatchAssertBlock.DoAssert("", action5)

            def action6():
                oAccess = oObject.GetAccessToObject(clr.CastAs(oSatellite, IStkObject))

            TryCatchAssertBlock.DoAssert("", action6)

            def action7():
                acc = oObject.AccessConstraints

            TryCatchAssertBlock.DoAssert("", action7)

            def action8():
                opa = oObject.CreateOnePointAccess("Satellite/MIR")

            TryCatchAssertBlock.DoAssert("", action8)

        oObject.Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "MIR")
        # Root
        oRoot = oObject.Root
        Assert.assertIsNotNone(oRoot)

        # Object Files
        self.TestObjectFilesArray(oObject.ObjectFiles)
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
                                                ((oObject.ClassName != "AdvCAT") and (oObject.ClassName != "Chain"))
                                                and (oObject.ClassName != "CommSystem")
                                            )
                                            and (oObject.ClassName != "Constellation")
                                        )
                                        and (oObject.ClassName != "Coverage")
                                    )
                                    and (oObject.ClassName != "CoverageDefinition")
                                )
                                and (oObject.ClassName != "FigureOfMerit")
                            )
                            and (oObject.ClassName != "MTO")
                        )
                        and (oObject.ClassName != "Satellite")
                    )
                    and (oObject.ClassName != "Scenario")
                )
                and (oObject.ClassName != "Sensor")
            )
            and (oObject.ClassName != "LineTarget")
        ) and (oObject.ClassName != "Volumetric"):
            self.OnePtAccess(oObject)

        self.Metadata(oObject)

        self.m_logger.WriteLine("----- STK OBJECT TEST ----- END -----")

    # endregion

    # region OnePtAccess
    def OnePtAccess(self, oObj: "IStkObject"):
        onePtAccess = oObj.CreateOnePointAccess("Satellite/Satellite1")
        onePtAccess.StartTime = "1 Jul 2007 00:00:00.000"
        Assert.assertEqual("1 Jul 2007 00:00:00.000", onePtAccess.StartTime)
        onePtAccess.StopTime = "1 Jul 2007 01:00:00.000"
        Assert.assertEqual("1 Jul 2007 01:00:00.000", onePtAccess.StopTime)
        onePtAccess.StepSize = 120
        Assert.assertEqual(120, onePtAccess.StepSize)
        onePtAccess.SummaryOption = AgEOnePtAccessSummary.eOnePtAccessSummaryDetailed
        Assert.assertEqual(AgEOnePtAccessSummary.eOnePtAccessSummaryDetailed, onePtAccess.SummaryOption)
        results = onePtAccess.Compute()

        i = 0
        while i < results.Count:
            result = results[i]
            self.m_logger.WriteLine2(result.Time)
            self.m_logger.WriteLine2(result.AccessSatisfied)

            j = 0
            while j < result.Constraints.Count:
                constraint = result.Constraints[j]
                self.dumpOnePtAccessConstraint(constraint)

                j += 1

            i += 1

        for r in results:
            self.m_logger.WriteLine2(r.Time)
            self.m_logger.WriteLine2(r.AccessSatisfied)
            for c in r.Constraints:
                self.dumpOnePtAccessConstraint(c)

        onePtAccess.SummaryOption = AgEOnePtAccessSummary.eOnePtAccessSummaryFast
        Assert.assertEqual(AgEOnePtAccessSummary.eOnePtAccessSummaryFast, onePtAccess.SummaryOption)
        results = onePtAccess.Compute()
        Assert.assertGreater(results.Count, 1)
        result = results[0]
        if (oObj.ClassName != "Star") and (oObj.ClassName != "Planet"):
            Assert.assertEqual(1, result.Constraints.Count)
            self.dumpOnePtAccessConstraint(result.Constraints[0])

        onePtAccess.SummaryOption = AgEOnePtAccessSummary.eOnePtAccessSummaryResultOnly
        Assert.assertEqual(AgEOnePtAccessSummary.eOnePtAccessSummaryResultOnly, onePtAccess.SummaryOption)
        results = onePtAccess.Compute()
        Assert.assertGreater(results.Count, 1)
        result = results[0]
        Assert.assertEqual(0, result.Constraints.Count)

        onePtAccess.OutputFile = r"C:\Dummy\File.out"
        Assert.assertEqual(r"C:\Dummy\File.out", onePtAccess.OutputFile)
        onePtAccess.OutputToFile = True
        Assert.assertTrue(onePtAccess.OutputToFile)
        onePtAccess.OutputToFile = False
        Assert.assertFalse(onePtAccess.OutputToFile)

        onePtAccess.Remove()

    # endregion

    def dumpOnePtAccessConstraint(self, constraint: "IOnePointAccessConstraint"):
        self.m_logger.WriteLine2(constraint.Constraint)
        self.m_logger.WriteLine(constraint.ObjectPath)
        self.m_logger.WriteLine2(constraint.Status)
        self.m_logger.WriteLine2(constraint.Value)

    def TestObjectFilesArray(self, arrFiles):
        Assert.assertIsNotNone(arrFiles)

        Assert.assertNotEqual(0, Array.Length(arrFiles))
        self.m_logger.WriteLine("Object Files are...")
        for file in arrFiles:
            self.m_logger.WriteLine(("\t" + str(file)))

    # region Children
    def Children(self, oObject: "IStkObject"):
        Assert.assertIsNotNone(oObject)
        # Children
        oCollection = oObject.Children
        Assert.assertIsNotNone(oCollection)
        if oCollection.Count > 0:
            x = oCollection[0]
            name = x.InstanceName
            y = oCollection.GetItemByIndex(0)
            z = oCollection.GetItemByName(name)
            Assert.assertEqual(x.InstanceName, y.InstanceName)
            Assert.assertEqual(x.InstanceName, z.InstanceName)

        # HasChildren
        self.m_logger.WriteLine4("\tThe HasChildren flag is: {0}", oObject.HasChildren)
        # Count
        self.m_logger.WriteLine7("\tThe {0} has: {1} children", oObject.InstanceName, oCollection.Count)
        if oObject.HasChildren:
            Assert.assertTrue((oCollection.Count > 0))

        else:
            Assert.assertTrue((oCollection.Count == 0))

        SupportedChildTypes = oObject.Children.SupportedChildTypes
        if (
            (
                (
                    (
                        (
                            (
                                (
                                    (oObject.ClassType == AgESTKObjectType.eAircraft)
                                    or (oObject.ClassType == AgESTKObjectType.eFacility)
                                )
                                or (oObject.ClassType == AgESTKObjectType.eGroundVehicle)
                            )
                            or (oObject.ClassType == AgESTKObjectType.eLaunchVehicle)
                        )
                        or (oObject.ClassType == AgESTKObjectType.eMissile)
                    )
                    or (oObject.ClassType == AgESTKObjectType.eSatellite)
                )
                or (oObject.ClassType == AgESTKObjectType.eShip)
            )
            or (oObject.ClassType == AgESTKObjectType.eTarget)
        ) or (oObject.ClassType == AgESTKObjectType.eSubmarine):
            found = False

            j = 0
            while j < Array.Length(SupportedChildTypes):
                objType = clr.Convert(int(SupportedChildTypes[j]), AgESTKObjectType)
                if objType == AgESTKObjectType.eSensor:
                    found = True

                j += 1

            if not found:
                Assert.fail(
                    "Sensor should be an available child object of the {0} object",
                    clr.Convert(oObject.ClassType, AgESTKObjectType),
                )

            # New
            oSensor = oCollection.New(AgESTKObjectType.eSensor, "Radar")
            Assert.assertIsNotNone(oSensor)
            # Unload
            oCollection.Unload(AgESTKObjectType.eSensor, "Radar")

        if oObject.ClassType == AgESTKObjectType.eScenario:
            oCollection.ImportObject(TestBase.GetScenarioFile(Path.Combine("AreaTargetTest", "at2.at")))

        else:

            def action9():
                oCollection.ImportObject(TestBase.GetScenarioFile(Path.Combine("AreaTargetTest", "at2.at")))

            TryCatchAssertBlock.DoAssert("", action9)

        # _NewEnum
        for oElement in oCollection:
            self.m_logger.WriteLine5("\t\tChildren: {0}", oElement.InstanceName)

        if oCollection.Count > 0:
            # Item
            oEObject = oCollection[0]
            Assert.assertIsNotNone(oEObject)

        # GetElements
        oOECollection = oCollection.GetElements(AgESTKObjectType.eSensor)
        Assert.assertIsNotNone(oOECollection)
        # Count
        self.m_logger.WriteLine3("\tThe ObjectElement collection contains: {0}", oOECollection.Count)
        # _NewEnum
        for oElement in oOECollection:
            self.m_logger.WriteLine5("\t\tElement: {0}", oElement.InstanceName)

        if oOECollection.Count > 0:
            # Item
            oEObject = oOECollection[0]
            Assert.assertIsNotNone(oEObject)

    # endregion

    # region Metadata
    def Metadata(self, oObject: "IStkObject"):
        metadata = oObject.Metadata

        Assert.assertEqual(0, metadata.Count)

        metadata.Set("Key1", "Value1")
        metadata.Set("Key2", "Value2")
        metadata.Set("Key3", "")
        Assert.assertEqual(3, metadata.Count)
        Assert.assertEqual("Value1", metadata["Key1"])
        Assert.assertEqual("Value2", metadata["Key2"])
        Assert.assertEqual("", metadata["Key3"])

        Assert.assertFalse(metadata.GetReadOnly("Key1"))

        metadata.SetReadOnly("Key1", True)
        Assert.assertTrue(metadata.GetReadOnly("Key1"))

        def action10():
            metadata.Set("Key1", "Changed1")

        TryCatchAssertBlock.ExpectedException("read-only", action10)

        metadata.SetReadOnly("Key1", False)
        Assert.assertFalse(metadata.GetReadOnly("Key1"))
        metadata.Set("Key1", "Changed1")
        Assert.assertEqual("Changed1", metadata["Key1"])

        def action11():
            metadata.SetReadOnly("BogusKey", True)

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action11)

        def action12():
            metadata.Set("", "Value1")

        TryCatchAssertBlock.ExpectedException("empty string", action12)

        metadata.Set("Key1", "Changed1")
        metadata.Set("Key2", "Changed2")
        metadata.Set("Key3", "Changed3")
        Assert.assertEqual("Changed1", metadata["Key1"])
        Assert.assertEqual("Changed2", metadata["Key2"])
        Assert.assertEqual("Changed3", metadata["Key3"])

        for key in metadata:
            Assert.assertTrue((len(metadata[key]) > 5))
            Assert.assertTrue(metadata.Contains(key))

        # Testing the keys property
        keys = metadata.Keys
        Assert.assertEqual(metadata.Count, Array.Length(keys))

        i = 0
        while i < Array.Length(keys):
            key = clr.Convert(keys[i], str)
            Assert.assertTrue((len(metadata[key]) > 5))
            Assert.assertTrue(metadata.Contains(key))

            i += 1

        Assert.assertFalse(metadata.Contains("Key4"))

        def action13():
            dummy = metadata["Key4"]

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action13)

        metadata.RemoveKey("Key2")
        Assert.assertEqual(2, metadata.Count)
        Assert.assertEqual("Changed1", metadata["Key1"])
        Assert.assertEqual("Changed3", metadata["Key3"])

        metadata.RemoveAll()
        Assert.assertEqual(0, metadata.Count)


# endregion


# region DataProviderCollectionHelper
class DataProviderCollectionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "IDataProviderCollection"):
        self.m_logger.WriteLine("----- DATA PROVIDER COLLECTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\tThe DataProvider collection contains: {0} elements.", oCollection.Count)
        if oCollection.Count > 0:
            x = oCollection[0]
            name = x.Name
            y = oCollection.GetItemByIndex(0)
            z = oCollection.GetItemByName(name)
            Assert.assertEqual(x.Name, y.Name)
            Assert.assertEqual(x.Name, z.Name)

        # _NewEnum
        for oDPInfo in oCollection:
            self.m_logger.WriteLine8(
                "\t\tElement: Name = {0}, Type = {1}, IsGroup = {2}", oDPInfo.Name, oDPInfo.Type, oDPInfo.IsGroup()
            )

            Assert.assertNotEqual(0, int(oDPInfo.Type))

        iIndex = 0
        while iIndex < oCollection.Count:
            if oCollection[iIndex].IsGroup():
                self.DataProviderGroup(clr.CastAs(oCollection[iIndex], IDataProviderGroup), oCollection[iIndex].Name)

            else:
                # we need to use a try-catch block here, because some data providers
                # can't be created without specific settings
                try:
                    # IAgDataProvider
                    # Console.WriteLine(oCollection[iIndex].Name);
                    self.DataProvider(clr.CastAs(oCollection[iIndex], IDataProvider), oCollection[iIndex].Name)
                    if oCollection[iIndex].Type == AgEDataProviderType.eDrFixed:
                        self.DataProviderFixed(
                            clr.CastAs(oCollection[iIndex], IDataProviderFixed), oCollection[iIndex].Name
                        )
                    elif oCollection[iIndex].Type == AgEDataProviderType.eDrIntvl:
                        self.DataProviderInterval(
                            clr.CastAs(oCollection[iIndex], IDataProviderInterval), oCollection[iIndex].Name
                        )
                    elif ((oCollection[iIndex].Type == AgEDataProviderType.eDrTimeVar)) or (
                        (oCollection[iIndex].Type == AgEDataProviderType.eDrIntvlDefined)
                    ):
                        self.DataProviderTimeVar(
                            clr.CastAs(oCollection[iIndex], IDataProviderTimeVarying), oCollection[iIndex].Name
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
    def DataProviderGroup(self, oGroup: "IDataProviderGroup", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER GROUP TEST ({0}) ----- BEGIN -----", strName)
        Assert.assertIsNotNone(oGroup)
        # Group
        oProviders = oGroup.Group
        Assert.assertIsNotNone(oProviders)
        # Count
        self.m_logger.WriteLine3("\tThe DataProvider collection contains: {0} elements.", oProviders.Count)
        # _NewEnum
        for oDPInfo in oProviders:
            self.m_logger.WriteLine8(
                "\t\tElement: Name = {0}, Type = {1}, IsGroup = {2}", oDPInfo.Name, oDPInfo.Type, oDPInfo.IsGroup()
            )

        iIndex = 0
        while iIndex < oProviders.Count:
            if oProviders[iIndex].IsGroup():
                Assert.fail("An unexpected group of DataProviders!")

            iIndex += 1

        self.m_logger.WriteLine5("----- DATA PROVIDER GROUP TEST ({0}) ----- END -----", strName)

    # endregion

    # region DataProvider
    def DataProvider(self, oProvider: "IDataProvider", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER TEST ({0}) ----- BEGIN -----", strName)
        Assert.assertIsNotNone(oProvider)
        # AllowUI
        self.m_logger.WriteLine4("\tThe current AllowUI is: {0}", oProvider.AllowUI)
        oProvider.AllowUI = False
        self.m_logger.WriteLine4("\tThe new AllowUI is: {0}", oProvider.AllowUI)
        Assert.assertFalse(oProvider.AllowUI)
        oProvider.AllowUI = True
        self.m_logger.WriteLine4("\tThe new AllowUI is: {0}", oProvider.AllowUI)
        Assert.assertTrue(oProvider.AllowUI)
        # PreData
        self.m_logger.WriteLine5("\tThe current PreData is: {0}", oProvider.PreData)
        oProvider.PreData = "Some PreData string"
        self.m_logger.WriteLine5("\tThe new PreData is: {0}", oProvider.PreData)
        Assert.assertEqual("Some PreData string", oProvider.PreData)
        oProvider.PreData = ""
        self.m_logger.WriteLine5("\tThe new PreData is: {0}", oProvider.PreData)
        Assert.assertEqual("", oProvider.PreData)
        # Elements
        oElements = oProvider.Elements
        Assert.assertIsNotNone(oElements)
        self.m_logger.WriteLine3("\tThe current Elements collection contains: {0} elements.", oElements.Count)
        # _NewEnum
        for oElement in oElements:
            self.m_logger.WriteLine8(
                "\t\tElement: Name = {0}, Type = {1}, DimensionName = {2}",
                oElement.Name,
                oElement.Type,
                oElement.DimensionName,
            )

        iIndex = 0
        while iIndex < oElements.Count:
            strElementName = oElements[iIndex].Name
            eType = oElements[iIndex].Type
            Assert.assertFalse(String.IsNullOrEmpty(oElements[iIndex].DimensionName))

            iIndex += 1

        self.m_logger.WriteLine5("----- DATA PROVIDER TEST ({0}) ----- END -----", strName)

    # endregion

    # region DataProviderFixed
    def DataProviderFixed(self, oProvider: "IDataProviderFixed", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER FIXED TEST ({0}) ----- BEGIN -----", strName)
        Assert.assertIsNotNone(oProvider)
        if (clr.CastAs(oProvider, IDataProvider)).IsValid:
            oResult = oProvider.Exec()
            Assert.assertIsNotNone(oResult)

            self.m_logger.WriteLine("\tExec:")
            self.DrResult(oResult)
            arCols = Array.CreateInstance(Type.GetType("System.Object"), oResult.DataSets.Count)

            i = 0
            while i < oResult.DataSets.Count:
                arCols[i] = oResult.DataSets[i].ElementName

                i += 1

            oResult = oProvider.ExecElements(arCols)
            Assert.assertIsNotNone(oResult)
            self.m_logger.WriteLine("\tExecElements:")
            self.DrResult(oResult)

        else:

            def action14():
                oResult = oProvider.Exec()

            TryCatchAssertBlock.DoAssert(("Able to execute invalid DP: " + strName), action14)

        self.m_logger.WriteLine5("----- DATA PROVIDER FIXED TEST ({0}) ----- END -----", strName)

    # endregion

    # region DrResult
    def DrResult(self, oResult: "IDataProviderResult"):
        Assert.assertIsNotNone(oResult)
        # Category
        self.m_logger.WriteLine6("\t\tThe current Category is: {0}", oResult.Category)
        # Sections
        self.DrResultSections(oResult.Sections)
        # Intervals
        self.DrResultIntervals(oResult.Intervals)
        # DataSets
        self.DrResultDataSets(oResult.DataSets)
        # Message
        self.DrResultMessage(oResult.Message)
        if oResult.Category == AgEDrCategories.eDrCatDataSetList:
            self.DrResultDataSets(clr.CastAs(oResult.Value, IDataProviderResultDataSetCollection))
        elif oResult.Category == AgEDrCategories.eDrCatIntervalList:
            self.DrResultIntervals(clr.CastAs(oResult.Value, IDataProviderResultIntervalCollection))
        elif oResult.Category == AgEDrCategories.eDrCatMessage:
            self.DrResultMessage(clr.CastAs(oResult.Value, IDataProviderResultTextMessage))
        elif oResult.Category == AgEDrCategories.eDrCatSubSectionList:
            self.DrResultSections(clr.CastAs(oResult.Value, IDataProviderResultSubSectionCollection))
        else:
            Assert.fail("Invalid type!")

    # endregion

    # region DrResultSections
    def DrResultSections(self, oCollection: "IDataProviderResultSubSectionCollection"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe SubSection collection contains: {0} elements.", oCollection.Count)
        # _NewEnum
        for oSection in oCollection:
            # Title
            self.m_logger.WriteLine5("\t\t\tElement: Title = {0}", oSection.Title)

        iIndex = 0
        while iIndex < oCollection.Count:
            # Intervals
            self.DrResultIntervals(oCollection[iIndex].Intervals)

            iIndex += 1

    # endregion

    # region DrResultIntervals
    def DrResultIntervals(self, oCollection: "IDataProviderResultIntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe Interval collection contains: {0} elements.", oCollection.Count)
        # _NewEnum
        for oInterval in oCollection:
            # StartTime, StopTime
            self.m_logger.WriteLine7(
                "\t\t\tElement: StartTime = {0}, StopTime = {1}", oInterval.StartTime, oInterval.StopTime
            )
            self.m_logger.WriteLine7(
                "\t\t\tElement: StartTime2 = {0}, StopTime2 = {1}", oInterval.StartTime, oInterval.StopTime
            )

        if oCollection.Count > 0:
            # ThresholdCrossings (see DataProviders.ObjectCoverage test)
            # MultipleThresholdCrossings (see DataProviders.ObjectCoverage test)
            # DataSets
            self.DrResultDataSets(oCollection[0].DataSets)

    # endregion

    # region DrResultDataSets
    def DrResultDataSets(self, oCollection: "IDataProviderResultDataSetCollection"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe DataSet collection contains: {0} elements.", oCollection.Count)
        # _NewEnum
        for oSet in oCollection:
            # ElementName, ElementType, Count, UnitType
            self.m_logger.WriteLine9(
                "\t\t\tElement: ElementName = {0}, ElementType = {1}, Count = {2}, DimensionName = {3}",
                oSet.ElementName,
                oSet.ElementType,
                oSet.Count,
                oSet.DimensionName,
            )

        if oCollection.Count > 0:
            # GetValues
            arValues = oCollection[0].GetValues()
            self.m_logger.WriteLine3("\t\tThe Values array contains: {0} elements.", Array.Length(arValues))
            # GetInternalUnitValues
            arValues = oCollection[0].GetInternalUnitValues()
            self.m_logger.WriteLine3("\t\tThe InternalUnitValues array contains: {0} elements.", Array.Length(arValues))

    # endregion

    # region DrResultMessage
    def DrResultMessage(self, oCollection: "IDataProviderResultTextMessage"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe TextMessages collection contains: {0} elements.", oCollection.Count)
        # _NewEnum
        for strText in oCollection:
            self.m_logger.WriteLine5("\t\t\tElement: {0}", strText)

        # Messages
        arStrings = oCollection.Messages
        self.m_logger.WriteLine3("\t\tThe Messages array contains: {0} elements.", Array.Length(arStrings))
        # IsFailure
        self.m_logger.WriteLine4("\t\tThe IsFailure flag is: {0}", oCollection.IsFailure)
        if oCollection.Count > 0:
            self.m_logger.WriteLine5("\t\tThe first message text string: {0}", oCollection[0])

    # endregion

    # region DataProviderInterval
    def DataProviderInterval(self, oProvider: "IDataProviderInterval", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER INTERVAL TEST ({0}) ----- BEGIN -----", strName)
        Assert.assertIsNotNone(oProvider)
        dtStart = "1 Jun 2004 12:00:00.00"
        dtStop = "1 Jun 2004 13:00:00.00"
        if (clr.CastAs(oProvider, IDataProvider)).IsValid:
            # Exec
            oResult = oProvider.Exec(dtStart, dtStop)
            Assert.assertIsNotNone(oResult)
            self.m_logger.WriteLine("\tExec:")
            self.DrResult(oResult)
            arCols = Array.CreateInstance(Type.GetType("System.Object"), oResult.DataSets.Count)

            i = 0
            while i < oResult.DataSets.Count:
                arCols[i] = oResult.DataSets[i].ElementName

                i += 1

            # Array arCols = new object[] { "Time", "y" };
            oResult = oProvider.ExecElements("1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", arCols)
            Assert.assertIsNotNone(oResult)
            self.m_logger.WriteLine("\tExecElements:")
            self.DrResult(oResult)
            self.m_logger.WriteLine5("----- DATA PROVIDER INTERVAL TEST ({0}) ----- END -----", strName)

        else:

            def action15():
                oResult = oProvider.Exec(dtStart, dtStop)

            TryCatchAssertBlock.DoAssert(("Able to execute invalid DP: " + strName), action15)

    # endregion

    # region DataProviderTimeVar
    def DataProviderTimeVar(self, oProvider: "IDataProviderTimeVarying", strName: str):
        self.m_logger.WriteLine5("----- DATA PROVIDER TIMEVAR TEST ({0}) ----- BEGIN -----", strName)
        if strName != "User Supplied Data":
            Assert.assertIsNotNone(oProvider)
            dtStart = "1 Jun 2004 12:00:00.00"
            dtStop = "1 Jun 2004 13:00:00.00"
            # Exec
            dp = clr.Convert(oProvider, IDataProvider)
            dp.PreData = "Missile/Missile1"
            if (clr.CastAs(oProvider, IDataProvider)).IsValid:
                oResult = oProvider.Exec(dtStart, dtStop, 240.0)
                Assert.assertIsNotNone(oResult)
                self.m_logger.WriteLine("\tExec:")
                self.DrResult(oResult)
                arCols = Array.CreateInstance(Type.GetType("System.Object"), oResult.DataSets.Count)

                i = 0
                while i < oResult.DataSets.Count:
                    arCols[i] = oResult.DataSets[i].ElementName

                    i += 1

                oResult = oProvider.ExecElements("1 Jun 2004 12:00:00.00", "1 Jun 2004 13:00:00.00", 240.9, arCols)
                Assert.assertIsNotNone(oResult)
                self.m_logger.WriteLine("\tExecElements:")
                self.DrResult(oResult)
                # ExecSingle
                oResult = oProvider.ExecSingle(dtStart)
                Assert.assertIsNotNone(oResult)
                self.m_logger.WriteLine("\tExecSingle:")
                self.DrResult(oResult)
                # ExecSingleElements
                oResult = oProvider.ExecSingleElements("1 Jun 2004 12:00:00.00", arCols)
                Assert.assertIsNotNone(oResult)
                self.m_logger.WriteLine("\tExecSingleElements:")
                self.DrResult(oResult)

            else:

                def action16():
                    oResult = oProvider.Exec(dtStart, dtStop, 240.0)

                TryCatchAssertBlock.DoAssert(("Able to execute invalid DP: " + strName), action16)

        self.m_logger.WriteLine5("----- DATA PROVIDER TIMEVAR TEST ({0}) ----- END -----", strName)


# endregion


# region StkAccessHelper
class StkAccessHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oAccess: "IStkAccess", oRoot: "IStkObjectRoot"):
        self.m_logger.WriteLine("----- STK ACCESS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oAccess)
        Assert.assertIsNotNone(oRoot)
        # AccessTimePeriod
        self.m_logger.WriteLine6("\tThe current AccessTimePeriod is: {0}", oAccess.AccessTimePeriod)
        oAccess.AccessTimePeriod = AgEAccessTimeType.eObjectAccessTime
        self.m_logger.WriteLine6("\tThe new AccessTimePeriod is: {0}", oAccess.AccessTimePeriod)
        Assert.assertEqual(AgEAccessTimeType.eObjectAccessTime, oAccess.AccessTimePeriod)
        # ComputeAccess
        oAccess.ComputeAccess()
        oAccess.AccessTimePeriod = AgEAccessTimeType.eScenarioAccessTime
        self.m_logger.WriteLine6("\tThe new AccessTimePeriod is: {0}", oAccess.AccessTimePeriod)
        Assert.assertEqual(AgEAccessTimeType.eScenarioAccessTime, oAccess.AccessTimePeriod)
        oAccess.ComputeAccess()
        oAccess.AccessTimePeriod = AgEAccessTimeType.eUserSpecAccessTime
        self.m_logger.WriteLine6("\tThe new AccessTimePeriod is: {0}", oAccess.AccessTimePeriod)
        Assert.assertEqual(AgEAccessTimeType.eUserSpecAccessTime, oAccess.AccessTimePeriod)
        oAccess.ComputeAccess()
        # SpecifyAccessTimePeriod
        dtStart = "1 Jul 1999 00:00:00.00"
        dtStop = "1 Jul 1999 00:09:00.00"
        oAccess.SpecifyAccessTimePeriod(dtStart, dtStop)
        oAccess.ComputeAccess()
        if not TestBase.NoGraphicsMode:
            self.Graphics(oAccess.Graphics)

        else:

            def action17():
                self.Graphics(oAccess.Graphics)

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action17)

        # Advanced
        self.Advanced(oAccess)
        if not TestBase.NoGraphicsMode:
            oDDHelper = VODataDisplayHelper(oRoot)
            oDDHelper.Run(oAccess.DataDisplays, True, False)

        else:

            def action18():
                oDDHelper = VODataDisplayHelper(oRoot)
                oDDHelper.Run(oAccess.DataDisplays, True, False)

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action18)

        # DataProviders
        oDPHelper = DataProviderCollectionHelper()
        oDPHelper.Run(oAccess.DataProviders)
        # RemoveAccess
        oAccess.RemoveAccess()
        self.m_logger.WriteLine("----- STK ACCESS TEST ----- END -----")

    # endregion

    # region Graphics
    def Graphics(self, oGraphics: "IStkAccessGraphics"):
        Assert.assertIsNotNone(oGraphics)
        # Inherit (true)
        self.m_logger.WriteLine4("\tThe current Inherit is: {0}", oGraphics.Inherit)
        oGraphics.Inherit = True
        self.m_logger.WriteLine4("\tThe new Inherit is: {0}", oGraphics.Inherit)
        Assert.assertTrue(oGraphics.Inherit)

        def action19():
            oGraphics.AnimateGfx = True

        # AnimateGfx (readonly)
        TryCatchAssertBlock.DoAssert("", action19)

        def action20():
            oGraphics.LineVisible = True

        # LineVisible (readonly)
        TryCatchAssertBlock.DoAssert("", action20)

        def action21():
            oGraphics.StaticGfx = True

        # StaticGfx (readonly)
        TryCatchAssertBlock.DoAssert("", action21)

        def action22():
            oGraphics.LineWidth = 2

        # LineWidth (readonly)
        TryCatchAssertBlock.DoAssert("", action22)
        # Inherit (false)
        oGraphics.Inherit = False
        self.m_logger.WriteLine4("\tThe new Inherit is: {0}", oGraphics.Inherit)
        Assert.assertFalse(oGraphics.Inherit)
        # AnimateGfx
        self.m_logger.WriteLine4("\tThe current AnimateGfx is: {0}", oGraphics.AnimateGfx)
        oGraphics.AnimateGfx = True
        self.m_logger.WriteLine4("\tThe new AnimateGfx is: {0}", oGraphics.AnimateGfx)
        Assert.assertTrue(oGraphics.AnimateGfx)
        oGraphics.AnimateGfx = False
        self.m_logger.WriteLine4("\tThe new AnimateGfx is: {0}", oGraphics.AnimateGfx)
        Assert.assertFalse(oGraphics.AnimateGfx)
        # LineVisible
        self.m_logger.WriteLine4("\tThe current LineVisible is: {0}", oGraphics.LineVisible)
        oGraphics.LineVisible = True
        self.m_logger.WriteLine4("\tThe new LineVisible is: {0}", oGraphics.LineVisible)
        Assert.assertTrue(oGraphics.LineVisible)
        oGraphics.LineVisible = False
        self.m_logger.WriteLine4("\tThe new LineVisible is: {0}", oGraphics.LineVisible)
        Assert.assertFalse(oGraphics.LineVisible)

        def action23():
            oGraphics.LineWidth = 2

        # LineWidth
        # LineVisible is false so LineWidth can't be set (readonly)
        TryCatchAssertBlock.DoAssert("", action23)
        oGraphics.LineVisible = True
        self.m_logger.WriteLine3("\tThe current LineWidth is: {0}", oGraphics.LineWidth)
        oGraphics.LineWidth = 2
        self.m_logger.WriteLine3("\tThe new LineWidth is: {0}", oGraphics.LineWidth)
        Assert.assertTrue((oGraphics.LineWidth == 2))
        oGraphics.LineWidth = 1
        self.m_logger.WriteLine3("\tThe new LineWidth is: {0}", oGraphics.LineWidth)
        Assert.assertTrue((oGraphics.LineWidth == 1))
        # Restore LineVisible (false)
        oGraphics.LineVisible = False

        # StaticGfx
        self.m_logger.WriteLine4("\tThe current StaticGfx is: {0}", oGraphics.StaticGfx)
        oGraphics.StaticGfx = True
        self.m_logger.WriteLine4("\tThe new StaticGfx is: {0}", oGraphics.StaticGfx)
        Assert.assertTrue(oGraphics.StaticGfx)
        oGraphics.StaticGfx = False
        self.m_logger.WriteLine4("\tThe new StaticGfx is: {0}", oGraphics.StaticGfx)
        Assert.assertFalse(oGraphics.StaticGfx)

    # endregion

    # region Advanced
    def Advanced(self, oAccess: "IStkAccess"):
        oAdvanced = oAccess.Advanced
        Assert.assertIsNotNone(oAdvanced)

        # Event Detection
        oAdvanced.UsePreciseEventTimes = True
        Assert.assertTrue(oAdvanced.UsePreciseEventTimes)

        oAdvanced.TimeConvergence = 0.123
        Assert.assertEqual(0.123, oAdvanced.TimeConvergence)
        oAdvanced.RelativeTolerance = 0.456
        Assert.assertEqual(0.456, oAdvanced.RelativeTolerance)
        oAdvanced.AbsoluteTolerance = 0.789
        Assert.assertEqual(0.789, oAdvanced.AbsoluteTolerance)

        oAdvanced.UsePreciseEventTimes = False  # Use Samples Only
        Assert.assertFalse(oAdvanced.UsePreciseEventTimes)

        def action24():
            oAdvanced.TimeConvergence = 0.123

        TryCatchAssertBlock.ExpectedException("read only", action24)

        def action25():
            oAdvanced.RelativeTolerance = 0.456

        TryCatchAssertBlock.ExpectedException("read-only", action25)

        def action26():
            oAdvanced.AbsoluteTolerance = 0.789

        TryCatchAssertBlock.ExpectedException("read-only", action26)

        # Light Time Delay
        oAdvanced.EnableLightTimeDelay = False
        Assert.assertFalse(oAdvanced.EnableLightTimeDelay)

        def action27():
            oAdvanced.TimeLightDelayConvergence = 0.01234

        TryCatchAssertBlock.ExpectedException("read only", action27)

        def action28():
            oAdvanced.AberrationType = AgEAberrationType.eAberrationAnnual

        TryCatchAssertBlock.ExpectedException("read-only", action28)

        def action29():
            oAdvanced.UseDefaultClockHostAndSignalSense = False

        TryCatchAssertBlock.ExpectedException("read-only", action29)

        def action30():
            oAdvanced.ClockHost = AgEIvClockHost.eIvBase

        TryCatchAssertBlock.ExpectedException("read-only", action30)

        def action31():
            oAdvanced.SignalSenseOfClockHost = AgEIvTimeSense.eIvTransmit

        TryCatchAssertBlock.ExpectedException("read-only", action31)

        oAdvanced.EnableLightTimeDelay = True
        Assert.assertTrue(oAdvanced.EnableLightTimeDelay)

        oAdvanced.TimeLightDelayConvergence = 0.0123
        Assert.assertEqual(0.0123, oAdvanced.TimeLightDelayConvergence)

        def action32():
            oAdvanced.TimeLightDelayConvergence = 12.34

        TryCatchAssertBlock.ExpectedException("", action32)

        oAdvanced.AberrationType = AgEAberrationType.eAberrationAnnual
        Assert.assertEqual(AgEAberrationType.eAberrationAnnual, oAdvanced.AberrationType)
        oAdvanced.AberrationType = AgEAberrationType.eAberrationNone
        Assert.assertEqual(AgEAberrationType.eAberrationNone, oAdvanced.AberrationType)
        oAdvanced.AberrationType = AgEAberrationType.eAberrationTotal
        Assert.assertEqual(AgEAberrationType.eAberrationTotal, oAdvanced.AberrationType)

        def action33():
            oAdvanced.AberrationType = AgEAberrationType.eAberrationUnknown

        TryCatchAssertBlock.ExpectedException("", action33)

        # Signal Path
        oAdvanced.UseDefaultClockHostAndSignalSense = True
        Assert.assertTrue(oAdvanced.UseDefaultClockHostAndSignalSense)

        def action34():
            oAdvanced.ClockHost = AgEIvClockHost.eIvBase

        TryCatchAssertBlock.ExpectedException("read-only", action34)

        def action35():
            oAdvanced.SignalSenseOfClockHost = AgEIvTimeSense.eIvTransmit

        TryCatchAssertBlock.ExpectedException("read-only", action35)

        oAdvanced.UseDefaultClockHostAndSignalSense = False
        Assert.assertFalse(oAdvanced.UseDefaultClockHostAndSignalSense)

        oAdvanced.ClockHost = AgEIvClockHost.eIvBase
        Assert.assertEqual(AgEIvClockHost.eIvBase, oAdvanced.ClockHost)
        oAdvanced.ClockHost = AgEIvClockHost.eIvTarget
        Assert.assertEqual(AgEIvClockHost.eIvTarget, oAdvanced.ClockHost)

        def action36():
            oAdvanced.SignalSenseOfClockHost = AgEIvTimeSense.eIvTimeSenseUnknown

        TryCatchAssertBlock.ExpectedException("must be in", action36)
        oAdvanced.SignalSenseOfClockHost = AgEIvTimeSense.eIvTransmit
        Assert.assertEqual(AgEIvTimeSense.eIvTransmit, oAdvanced.SignalSenseOfClockHost)
        oAdvanced.SignalSenseOfClockHost = AgEIvTimeSense.eIvReceive
        Assert.assertEqual(AgEIvTimeSense.eIvReceive, oAdvanced.SignalSenseOfClockHost)

        # Step Size Control
        oAdvanced.UseFixedTimeStep = False  # Adaptive
        Assert.assertFalse(oAdvanced.UseFixedTimeStep)

        oAdvanced.MaxTimeStep = 123.456
        Assert.assertEqual(123.456, oAdvanced.MaxTimeStep)

        def action37():
            oAdvanced.MaxTimeStep = 0

        TryCatchAssertBlock.ExpectedException("invalid", action37)

        oAdvanced.MinTimeStep = 456.123
        Assert.assertEqual(456.123, oAdvanced.MinTimeStep)

        def action38():
            oAdvanced.MinTimeStep = 0

        TryCatchAssertBlock.ExpectedException("invalid", action38)

        def action39():
            oAdvanced.FixedStepSize = 789

        TryCatchAssertBlock.ExpectedException("read only", action39)

        def action40():
            oAdvanced.FixedTimeBound = 789

        TryCatchAssertBlock.ExpectedException("read only", action40)

        oAdvanced.UseFixedTimeStep = True  # Fixed Step
        Assert.assertTrue(oAdvanced.UseFixedTimeStep)

        oAdvanced.FixedStepSize = 123.456
        Assert.assertEqual(123.456, oAdvanced.FixedStepSize)

        def action41():
            oAdvanced.FixedStepSize = 0

        TryCatchAssertBlock.ExpectedException("invalid", action41)

        oAdvanced.FixedTimeBound = 56.123
        Assert.assertEqual(56.123, oAdvanced.FixedTimeBound)

        def action42():
            oAdvanced.FixedTimeBound = 0

        TryCatchAssertBlock.ExpectedException("invalid", action42)

        def action43():
            oAdvanced.MaxTimeStep = 123.456

        TryCatchAssertBlock.ExpectedException("read only", action43)

        def action44():
            oAdvanced.MinTimeStep = 56.123

        TryCatchAssertBlock.ExpectedException("read only", action44)

        oAccess.ComputeAccess()  # to make changes show in GUI


# endregion


# region VODataDisplayHelper
class VODataDisplayHelper(object):
    def __init__(self, oRoot: "IStkObjectRoot"):
        self.m_bIsAccessRequired = None
        self.m_bIsChain = None
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oRoot)
        self.m_oRoot = oRoot

    # endregion

    # region Run method
    def Run(self, oDataCollection: "IVODataDisplayCollection", bIsAccessRequired: bool, bIsChain: bool):
        self.m_logger.WriteLine("----- THE VO DATA DISPLAY TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oDataCollection)
        # save AccessRequired flag
        self.m_bIsAccessRequired = bIsAccessRequired
        # save IsChain flag
        self.m_bIsChain = bIsChain
        # Count
        iSize = oDataCollection.Count
        self.m_logger.WriteLine3("The current Data Display collection contains: {0} elements.", iSize)

        iIndex = 0
        while iIndex < iSize:
            self.m_logger.WriteLine7("\tElement {0} is: {1}", iIndex, oDataCollection[iIndex].Name)

            iIndex += 1

        if oDataCollection.Count > 0:
            oDataCollection.RemoveAt(0)
            self.m_logger.WriteLine3(
                "After Remove(0) the Data Display collection contains: {0} elements.", oDataCollection.Count
            )

            iIndex = 0
            while iIndex < oDataCollection.Count:
                self.m_logger.WriteLine7("\tElement {0} is: {1}", iIndex, oDataCollection[iIndex].Name)

                iIndex += 1

            Assert.assertEqual((iSize - 1), oDataCollection.Count)

        oDataCollection.RemoveAll()
        self.m_logger.WriteLine3(
            "After RemoveAll() the Data Display collection contains: {0} elements.", oDataCollection.Count
        )
        Assert.assertEqual(0, oDataCollection.Count)

        arAvailable = oDataCollection.AvailableData
        self.m_logger.WriteLine3("Available Data list contains: {0} elements", Array.Length(arAvailable))

        iIndex = 0
        while iIndex < Array.Length(arAvailable):
            self.m_logger.WriteLine7("\tAvailable element {0} is: {1}", iIndex, arAvailable[iIndex])

            iIndex += 1

        self.m_oRoot.BeginUpdate()
        self.m_logger.WriteLine3("The current Data Display collection contains: {0} elements.", oDataCollection.Count)

        iIndex = 0
        while iIndex < Array.Length(arAvailable):
            strAvailable = str(arAvailable[iIndex])
            if oDataCollection.IsPreDataRequired(strAvailable):
                preData = "Missile/Missile1"
                if strAvailable.startswith("Crdn") or ("EphemerisChooseAxes" == strAvailable):
                    preData = "Satellite/Satellite1 Body Axes"

                oDataDisp = oDataCollection.AddDataDisplayRequiringPreData(strAvailable, preData)
                Assert.assertIsNotNone(oDataDisp)
                self.m_logger.WriteLine7("\tAdded element: {0} (with PreData - {1})", oDataDisp.Name, preData)
                break

            if (not oDataCollection.IsPreDataRequired(strAvailable)) and (oDataCollection.Count == 0):
                oDataDisp = oDataCollection.Add(strAvailable)
                Assert.assertIsNotNone(oDataDisp)
                self.m_logger.WriteLine5("\tAdded element: {0}", oDataDisp.Name)

            iIndex += 1

        # Count
        iSize = oDataCollection.Count
        self.m_logger.WriteLine3("The new Data Display collection contains: {0} elements.", iSize)
        for oElement in oDataCollection:
            self.m_logger.WriteLine5("\tElement: {0}", oElement.Name)

            self.ElementTest(oElement)

        self.m_oRoot.EndUpdate()
        if oDataCollection.Count > 0:
            # RemoveAt
            oDataCollection.RemoveAt(0)
            self.m_logger.WriteLine3(
                "After Remove(0) the Data Display collection contains: {0} elements.", oDataCollection.Count
            )
            Assert.assertEqual((iSize - 1), oDataCollection.Count)
            for oElement in oDataCollection:
                self.m_logger.WriteLine5("\tElement: {0}", oElement.Name)

        # RemoveAll
        oDataCollection.RemoveAll()
        self.m_logger.WriteLine3(
            "After RemoveAll() the Data Display collection contains: {0} elements.", oDataCollection.Count
        )
        Assert.assertEqual(0, oDataCollection.Count)

        self.m_logger.WriteLine("----- THE VO DATA DISPLAY TEST ----- END -----")

    # endregion

    # region ElementTest
    def ElementTest(self, oVODataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)
        # IsVisible
        self.m_logger.WriteLine4("\t\tCurrent IsVisible flag: {0}", oVODataDisplayElement.IsVisible)
        oVODataDisplayElement.IsVisible = False
        self.m_logger.WriteLine4("\t\tNew IsVisible flag: {0}", oVODataDisplayElement.IsVisible)
        Assert.assertFalse(oVODataDisplayElement.IsVisible)
        self.NotVisibleCheck(oVODataDisplayElement)

        oVODataDisplayElement.IsVisible = True
        self.m_logger.WriteLine4("\t\tNew IsVisible flag: {0}", oVODataDisplayElement.IsVisible)
        Assert.assertTrue(oVODataDisplayElement.IsVisible)
        self.VisibleCheck(oVODataDisplayElement)

        self.m_logger.WriteLine4("\t\tCurrent UseBackground flag: {0}", oVODataDisplayElement.UseBackground)
        oVODataDisplayElement.UseBackground = False
        self.m_logger.WriteLine4("\t\tNew UseBackground flag: {0}", oVODataDisplayElement.UseBackground)
        Assert.assertFalse(oVODataDisplayElement.UseBackground)
        self.NotUseBackgroundCheck(oVODataDisplayElement)

        oVODataDisplayElement.UseBackground = True
        self.m_logger.WriteLine4("\t\tNew UseBackground flag: {0}", oVODataDisplayElement.UseBackground)
        Assert.assertTrue(oVODataDisplayElement.UseBackground)
        self.UseBackgroundCheck(oVODataDisplayElement)

        oVODataDisplayElement.UseAutoSizeWidth = False
        oVODataDisplayElement.UseAutoSizeHeight = False
        self.m_logger.WriteLine4("\t\tNew UseAutoSizeWidth flag: {0}", oVODataDisplayElement.UseAutoSizeWidth)
        self.m_logger.WriteLine4("\t\tNew UseAutoSizeHeight flag: {0}", oVODataDisplayElement.UseAutoSizeHeight)
        Assert.assertFalse(oVODataDisplayElement.UseAutoSizeWidth)
        Assert.assertFalse(oVODataDisplayElement.UseAutoSizeHeight)
        self.NotUseAutoSizeCheck(oVODataDisplayElement)

        oVODataDisplayElement.UseAutoSizeWidth = True
        oVODataDisplayElement.UseAutoSizeHeight = True
        self.m_logger.WriteLine4("\t\tNew UseAutoSizeWidth flag: {0}", oVODataDisplayElement.UseAutoSizeWidth)
        self.m_logger.WriteLine4("\t\tNew UseAutoSizeHeight flag: {0}", oVODataDisplayElement.UseAutoSizeHeight)
        Assert.assertTrue(oVODataDisplayElement.UseAutoSizeWidth)
        Assert.assertTrue(oVODataDisplayElement.UseAutoSizeHeight)
        self.UseAutoSizeCheck(oVODataDisplayElement)

        oVODataDisplayElement.UseBackgroundBorder = False
        self.m_logger.WriteLine4("\t\tNew UseBackgroundBorder flag: {0}", oVODataDisplayElement.UseBackgroundBorder)
        Assert.assertFalse(oVODataDisplayElement.UseBackgroundBorder)
        self.NotUseBackgroundBorderCheck(oVODataDisplayElement)

        oVODataDisplayElement.UseBackgroundBorder = True
        self.m_logger.WriteLine4("\t\tNew UseBackgroundBorder flag: {0}", oVODataDisplayElement.UseBackgroundBorder)
        Assert.assertTrue(oVODataDisplayElement.UseBackgroundBorder)
        self.UseBackgroundBorderCheck(oVODataDisplayElement)

        oVODataDisplayElement.UseBackgroundTexture = False
        self.m_logger.WriteLine4("\t\tNew UseBackgroundTexture flag: {0}", oVODataDisplayElement.UseBackgroundTexture)
        Assert.assertFalse(oVODataDisplayElement.UseBackgroundTexture)
        self.NotUseBackgroundTextureCheck(oVODataDisplayElement)

        oVODataDisplayElement.UseBackgroundTexture = True
        self.m_logger.WriteLine4("\t\tNew UseBackgroundTexture flag: {0}", oVODataDisplayElement.UseBackgroundTexture)
        Assert.assertTrue(oVODataDisplayElement.UseBackgroundTexture)
        self.UseBackgroundTextureCheck(oVODataDisplayElement)

        oVODataDisplayElement.Title = False
        self.m_logger.WriteLine4("\t\tNew Title flag: {0}", oVODataDisplayElement.Title)
        Assert.assertFalse(oVODataDisplayElement.Title)
        self.NotUseTitleCheck(oVODataDisplayElement)

        oVODataDisplayElement.Title = True
        self.m_logger.WriteLine4("\t\tNew Title flag: {0}", oVODataDisplayElement.Title)
        Assert.assertTrue(oVODataDisplayElement.Title)
        self.UseTitleCheck(oVODataDisplayElement)

        arAvailableWindows = oVODataDisplayElement.AvailableWindows
        self.m_logger.WriteLine3("\t\tAvailable {0} Windows:", Array.Length(arAvailableWindows))

        i = 0
        while i < Array.Length(arAvailableWindows):
            self.m_logger.WriteLine6("\t\t\tWindow: {0}", arAvailableWindows[i])

            i += 1

        Assert.assertEqual(2, Array.Length(arAvailableWindows))

        sAll = "All"
        sTitle = clr.Convert(arAvailableWindows[1], str)
        Assert.assertEqual(True, oVODataDisplayElement.IsDisplayedInWindow(sAll))
        Assert.assertEqual(False, oVODataDisplayElement.IsDisplayedInWindow(sTitle))
        oVODataDisplayElement.AddToWindow(sTitle)
        Assert.assertEqual(False, oVODataDisplayElement.IsDisplayedInWindow(sAll))
        Assert.assertEqual(True, oVODataDisplayElement.IsDisplayedInWindow(sTitle))
        oVODataDisplayElement.RemoveFromWindow(sTitle)
        Assert.assertEqual(True, oVODataDisplayElement.IsDisplayedInWindow(sAll))
        Assert.assertEqual(False, oVODataDisplayElement.IsDisplayedInWindow(sTitle))
        oVODataDisplayElement.AddToWindow(sTitle)
        Assert.assertEqual(False, oVODataDisplayElement.IsDisplayedInWindow(sAll))
        Assert.assertEqual(True, oVODataDisplayElement.IsDisplayedInWindow(sTitle))
        oVODataDisplayElement.AddToAllWindows()
        Assert.assertEqual(True, oVODataDisplayElement.IsDisplayedInWindow(sAll))
        Assert.assertEqual(False, oVODataDisplayElement.IsDisplayedInWindow(sTitle))

    # endregion

    # region NotVisibleCheck
    def NotVisibleCheck(self, oVODataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)

        def action45():
            oVODataDisplayElement.Location = AgEVOLocation.e3DWindow

        # Location
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action45)

        def action46():
            oVODataDisplayElement.FontColor = Color.FromArgb(11254443)

        # FontColor
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action46)

        def action47():
            oVODataDisplayElement.XOrigin = AgEVOXOrigin.eXOriginLeft

        # XOrigin
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action47)

        def action48():
            oVODataDisplayElement.YOrigin = AgEVOYOrigin.eYOriginBottom

        # YOrigin
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action48)

        def action49():
            oVODataDisplayElement.X = 12

        # X
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action49)

        def action50():
            oVODataDisplayElement.Y = 21

        # Y
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action50)

        def action51():
            oVODataDisplayElement.Title = True

        # Title
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action51)

        def action52():
            oVODataDisplayElement.FontSize = AgEVOFontSize.eSmall

        # FontSize
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action52)

        def action53():
            oVODataDisplayElement.Format = AgEVOFormat.eHorizontal

        # Format
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action53)

        def action54():
            oVODataDisplayElement.UseBackground = True

        # UseBackground
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action54)

        def action55():
            oVODataDisplayElement.TransparentBg = True

        # TransparentBg
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action55)

        def action56():
            oVODataDisplayElement.BgWidth = 34

        # BgWidth
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action56)

        def action57():
            oVODataDisplayElement.BgHeight = 43

        # BgHeight
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action57)

        def action58():
            oVODataDisplayElement.BgColor = Color.FromArgb(13491405)

        # BgColor
        TryCatchAssertBlock.DoAssert("The property should be readonly when IsVisible is False.", action58)

    # endregion

    # region VisibleCheck
    def VisibleCheck(self, oVODataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)
        # Location
        self.m_logger.WriteLine6("\t\t\tThe current Location is: {0}", oVODataDisplayElement.Location)
        if self.m_bIsAccessRequired:
            oVODataDisplayElement.Location = AgEVOLocation.eOffsetFromAccessObject
            self.m_logger.WriteLine6("\t\t\tThe new Location is: {0}", oVODataDisplayElement.Location)
            Assert.assertEqual(AgEVOLocation.eOffsetFromAccessObject, oVODataDisplayElement.Location)

        else:

            def action59():
                oVODataDisplayElement.Location = AgEVOLocation.eOffsetFromAccessObject

            TryCatchAssertBlock.DoAssert("Should not allow to set eOffsetFromAccessObject.", action59)

        if self.m_bIsChain:

            def action60():
                oVODataDisplayElement.Location = AgEVOLocation.eOffsetFromObject

            TryCatchAssertBlock.DoAssert("Chains should not allow to set eOffsetFromObject.", action60)

        else:
            oVODataDisplayElement.Location = AgEVOLocation.eOffsetFromObject
            self.m_logger.WriteLine6("\t\t\tThe new Location is: {0}", oVODataDisplayElement.Location)
            Assert.assertEqual(AgEVOLocation.eOffsetFromObject, oVODataDisplayElement.Location)

        oVODataDisplayElement.Location = AgEVOLocation.eDataDisplayArea
        self.m_logger.WriteLine6("\t\t\tThe new Location is: {0}", oVODataDisplayElement.Location)
        Assert.assertEqual(AgEVOLocation.eDataDisplayArea, oVODataDisplayElement.Location)
        oVODataDisplayElement.Location = AgEVOLocation.e3DWindow
        self.m_logger.WriteLine6("\t\t\tThe new Location is: {0}", oVODataDisplayElement.Location)
        Assert.assertEqual(AgEVOLocation.e3DWindow, oVODataDisplayElement.Location)
        # Font Color
        self.m_logger.WriteLine6("\t\t\tThe current Font Color is: {0}", oVODataDisplayElement.FontColor)
        oVODataDisplayElement.FontColor = Color.FromArgb(65280)
        self.m_logger.WriteLine6("\t\t\tThe new Font Color is: {0}", oVODataDisplayElement.FontColor)
        AssertEx.AreEqual(Color.FromArgb(65280), oVODataDisplayElement.FontColor)
        # XOrigin
        self.m_logger.WriteLine6("\t\t\tThe current X Origin is: {0}", oVODataDisplayElement.XOrigin)
        oVODataDisplayElement.XOrigin = AgEVOXOrigin.eXOriginLeft
        self.m_logger.WriteLine6("\t\t\tThe new X Origin is: {0}", oVODataDisplayElement.XOrigin)
        Assert.assertEqual(AgEVOXOrigin.eXOriginLeft, oVODataDisplayElement.XOrigin)
        oVODataDisplayElement.XOrigin = AgEVOXOrigin.eXOriginRight
        self.m_logger.WriteLine6("\t\t\tThe new X Origin is: {0}", oVODataDisplayElement.XOrigin)
        Assert.assertEqual(AgEVOXOrigin.eXOriginRight, oVODataDisplayElement.XOrigin)
        # YOrigin
        self.m_logger.WriteLine6("\t\t\tThe current Y Origin is: {0}", oVODataDisplayElement.YOrigin)
        oVODataDisplayElement.YOrigin = AgEVOYOrigin.eYOriginTop
        self.m_logger.WriteLine6("\t\t\tThe new Y Origin is: {0}", oVODataDisplayElement.YOrigin)
        Assert.assertEqual(AgEVOYOrigin.eYOriginTop, oVODataDisplayElement.YOrigin)
        oVODataDisplayElement.YOrigin = AgEVOYOrigin.eYOriginBottom
        self.m_logger.WriteLine6("\t\t\tThe new Y Origin is: {0}", oVODataDisplayElement.YOrigin)
        Assert.assertEqual(AgEVOYOrigin.eYOriginBottom, oVODataDisplayElement.YOrigin)
        # X
        self.m_logger.WriteLine3("\t\t\tThe current X is: {0}", oVODataDisplayElement.X)
        oVODataDisplayElement.X = 12
        self.m_logger.WriteLine3("\t\t\tThe new X is: {0}", oVODataDisplayElement.X)
        Assert.assertEqual(12, oVODataDisplayElement.X)
        # Y
        self.m_logger.WriteLine3("\t\t\tThe current Y is: {0}", oVODataDisplayElement.Y)
        oVODataDisplayElement.Y = 21
        self.m_logger.WriteLine3("\t\t\tThe new Y is: {0}", oVODataDisplayElement.Y)
        Assert.assertEqual(21, oVODataDisplayElement.Y)
        # Title
        self.m_logger.WriteLine4("\t\t\tThe current Title is: {0}", oVODataDisplayElement.Title)
        oVODataDisplayElement.Title = False
        self.m_logger.WriteLine4("\t\t\tThe new Title is: {0}", oVODataDisplayElement.Title)
        Assert.assertEqual(False, oVODataDisplayElement.Title)
        oVODataDisplayElement.Title = True
        self.m_logger.WriteLine4("\t\t\tThe new Title is: {0}", oVODataDisplayElement.Title)
        Assert.assertEqual(True, oVODataDisplayElement.Title)
        # FontSize
        self.m_logger.WriteLine6("\t\t\tThe current Font Size is: {0}", oVODataDisplayElement.FontSize)
        oVODataDisplayElement.FontSize = AgEVOFontSize.eLarge
        self.m_logger.WriteLine6("\t\t\tThe new Font Size is: {0}", oVODataDisplayElement.FontSize)
        Assert.assertEqual(AgEVOFontSize.eLarge, oVODataDisplayElement.FontSize)
        oVODataDisplayElement.FontSize = AgEVOFontSize.eSmall
        self.m_logger.WriteLine6("\t\t\tThe new Font Size is: {0}", oVODataDisplayElement.FontSize)
        Assert.assertEqual(AgEVOFontSize.eSmall, oVODataDisplayElement.FontSize)
        oVODataDisplayElement.FontSize = AgEVOFontSize.eMedium
        self.m_logger.WriteLine6("\t\t\tThe new Font Size is: {0}", oVODataDisplayElement.FontSize)
        Assert.assertEqual(AgEVOFontSize.eMedium, oVODataDisplayElement.FontSize)
        # Format
        self.m_logger.WriteLine6("\t\t\tThe current Font Format is: {0}", oVODataDisplayElement.Format)
        oVODataDisplayElement.Format = AgEVOFormat.eHorizontal
        self.m_logger.WriteLine6("\t\t\tThe new Font Format is: {0}", oVODataDisplayElement.Format)
        Assert.assertEqual(AgEVOFormat.eHorizontal, oVODataDisplayElement.Format)
        oVODataDisplayElement.Format = AgEVOFormat.eNoLabels
        self.m_logger.WriteLine6("\t\t\tThe new Font Format is: {0}", oVODataDisplayElement.Format)
        Assert.assertEqual(AgEVOFormat.eNoLabels, oVODataDisplayElement.Format)
        oVODataDisplayElement.Format = AgEVOFormat.eVertical
        self.m_logger.WriteLine6("\t\t\tThe new Font Format is: {0}", oVODataDisplayElement.Format)
        Assert.assertEqual(AgEVOFormat.eVertical, oVODataDisplayElement.Format)

    # endregion

    # region NotUseBackgroundCheck
    def NotUseBackgroundCheck(self, oVODataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)

        def action61():
            oVODataDisplayElement.TransparentBg = True

        # TransparentBg
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action61)

        def action62():
            oVODataDisplayElement.BackgroundTranslucency = 0.33

        # BackgroundTranslucency
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action62)

        def action63():
            oVODataDisplayElement.UseBackgroundTexture = True

        # UseBackgroundTexture
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action63)

        def action64():
            oVODataDisplayElement.BackgroundTextureFilename = "foo.png"

        # BackgroundTextureFileName
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action64)

        def action65():
            oVODataDisplayElement.UseBackgroundBorder = True

        # UseBackgroundBorder
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action65)

        def action66():
            oVODataDisplayElement.BackgroundBorderColor = Color.FromArgb(13491405)

        # BackgroundBorderColor
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action66)

        def action67():
            oVODataDisplayElement.UseAutoSizeWidth = True

        # UseAutoSizeWidth
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action67)

        def action68():
            oVODataDisplayElement.UseAutoSizeHeight = True

        # UseAutoSizeHeight
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action68)

        def action69():
            oVODataDisplayElement.BgColor = Color.FromArgb(13491405)

        # BgColor
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackground is False.", action69)

    # endregion

    # region UseBackgroundCheck
    def UseBackgroundCheck(self, oVODataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oVODataDisplayElement)
        # TransparentBg
        self.m_logger.WriteLine4(
            "\t\t\tThe current Background Transparency is: {0}", oVODataDisplayElement.TransparentBg
        )
        oVODataDisplayElement.TransparentBg = False
        self.m_logger.WriteLine4("\t\t\tThe new Background Transparency is: {0}", oVODataDisplayElement.TransparentBg)
        Assert.assertEqual(False, oVODataDisplayElement.TransparentBg)
        oVODataDisplayElement.TransparentBg = True
        self.m_logger.WriteLine4("\t\t\tThe new Background Transparency is: {0}", oVODataDisplayElement.TransparentBg)
        Assert.assertEqual(True, oVODataDisplayElement.TransparentBg)
        # UseAutoSizeWidth
        self.m_logger.WriteLine4(
            "\t\t\tThe current Background UseAutoSizeWidth is: {0}", oVODataDisplayElement.UseAutoSizeWidth
        )
        oVODataDisplayElement.UseAutoSizeWidth = False
        self.m_logger.WriteLine4("\t\t\tThe new Background Width is: {0}", oVODataDisplayElement.UseAutoSizeWidth)
        Assert.assertEqual(False, oVODataDisplayElement.UseAutoSizeWidth)
        # UseAutoSizeHeight
        self.m_logger.WriteLine4(
            "\t\t\tThe current Background UseAutoSizeHeight is: {0}", oVODataDisplayElement.UseAutoSizeHeight
        )
        oVODataDisplayElement.UseAutoSizeHeight = False
        self.m_logger.WriteLine4(
            "\t\t\tThe new Background UseAutoSizeHeight is: {0}", oVODataDisplayElement.UseAutoSizeHeight
        )
        Assert.assertEqual(False, oVODataDisplayElement.UseAutoSizeHeight)
        # BgWidth
        self.m_logger.WriteLine3("\t\t\tThe current Background Width is: {0}", oVODataDisplayElement.BgWidth)
        oVODataDisplayElement.BgWidth = 34
        self.m_logger.WriteLine3("\t\t\tThe new Background Width is: {0}", oVODataDisplayElement.BgWidth)
        Assert.assertEqual(34, oVODataDisplayElement.BgWidth)
        # BgHeight
        self.m_logger.WriteLine3("\t\t\tThe current Background Height is: {0}", oVODataDisplayElement.BgHeight)
        oVODataDisplayElement.BgHeight = 12
        self.m_logger.WriteLine3("\t\t\tThe new Background Height is: {0}", oVODataDisplayElement.BgHeight)
        Assert.assertEqual(12, oVODataDisplayElement.BgHeight)
        # BgColor
        self.m_logger.WriteLine6("\t\t\tThe current Background Color is: {0}", oVODataDisplayElement.BgColor)
        oVODataDisplayElement.BgColor = Color.FromArgb(255)
        self.m_logger.WriteLine6("\t\t\tThe new Background Color is: {0}", oVODataDisplayElement.BgColor)
        AssertEx.AreEqual(Color.FromArgb(255), oVODataDisplayElement.BgColor)
        # UseBackgroundBorder
        self.m_logger.WriteLine4("\t\t\tThe new Background Border is: {0}", oVODataDisplayElement.UseBackgroundBorder)
        Assert.assertEqual(False, oVODataDisplayElement.UseBackgroundBorder)
        oVODataDisplayElement.UseBackgroundBorder = True
        self.m_logger.WriteLine4("\t\t\tThe new Background Border is: {0}", oVODataDisplayElement.UseBackgroundBorder)
        Assert.assertEqual(True, oVODataDisplayElement.UseBackgroundBorder)
        # BackgroundBorderColor
        self.m_logger.WriteLine6(
            "\t\t\tThe current Background Color is: {0}", oVODataDisplayElement.BackgroundBorderColor
        )
        oVODataDisplayElement.BackgroundBorderColor = Color.FromArgb(255)
        self.m_logger.WriteLine6(
            "\t\t\tThe new Background Border Color is: {0}", oVODataDisplayElement.BackgroundBorderColor
        )
        AssertEx.AreEqual(Color.FromArgb(255), oVODataDisplayElement.BackgroundBorderColor)
        # UseBackgroundTexture
        self.m_logger.WriteLine4("\t\t\tThe new Background Texture is: {0}", oVODataDisplayElement.UseBackgroundTexture)
        Assert.assertEqual(False, oVODataDisplayElement.UseBackgroundTexture)
        oVODataDisplayElement.UseBackgroundTexture = True
        self.m_logger.WriteLine4("\t\t\tThe new Background Texture is: {0}", oVODataDisplayElement.UseBackgroundTexture)
        Assert.assertEqual(True, oVODataDisplayElement.UseBackgroundTexture)
        # BackgroundTextureFileName
        self.m_logger.WriteLine5(
            "\t\t\tThe new Background Texture is: {0}", oVODataDisplayElement.BackgroundTextureFilename
        )
        Assert.assertEqual("", oVODataDisplayElement.BackgroundTextureFilename)

        oVODataDisplayElement.BackgroundTextureFilename = TestBase.GetScenarioFile("Fire.bmp")
        self.m_logger.WriteLine5(
            "\t\t\tThe new Background Texture is: {0}", oVODataDisplayElement.BackgroundTextureFilename
        )
        StringAssert.Contains("Fire.bmp", oVODataDisplayElement.BackgroundTextureFilename)

    # endregion

    # region NotUseTitleCheck
    def NotUseTitleCheck(self, oDataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)

        def action70():
            oDataDisplayElement.TitleText = "New Title"

        # TitleText
        TryCatchAssertBlock.DoAssert("The property should be readonly when Title is False.", action70)

        def action71():
            oDataDisplayElement.IsShowNameEnabled = False

        # IsShowNameEnabled
        TryCatchAssertBlock.DoAssert("The property should be readonly when Title is False.", action71)

    # endregion

    # region UseTitleCheck
    def UseTitleCheck(self, oDataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # TitleText
        self.m_logger.WriteLine5("\t\t\tThe current TitleText is: {0}", oDataDisplayElement.TitleText)
        oldTitle = oDataDisplayElement.TitleText
        oDataDisplayElement.TitleText = "foobar"
        self.m_logger.WriteLine5("\t\t\tThe new TitleText is: {0}", oDataDisplayElement.TitleText)
        Assert.assertEqual("foobar", oDataDisplayElement.TitleText)
        oDataDisplayElement.TitleText = oldTitle
        # IsShowNameEnabled
        self.m_logger.WriteLine4("\t\t\tThe current IsShowNameEnabled is: {0}", oDataDisplayElement.IsShowNameEnabled)
        oDataDisplayElement.IsShowNameEnabled = False
        self.m_logger.WriteLine4("\t\t\tThe new IsShowNameEnabled is: {0}", oDataDisplayElement.IsShowNameEnabled)
        Assert.assertEqual(False, oDataDisplayElement.IsShowNameEnabled)

    # endregion

    # region NotUseAutoSizeCheck
    def NotUseAutoSizeCheck(self, oDataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # BgWidth
        self.m_logger.WriteLine3("\t\t\tThe current BgWidth is: {0}", oDataDisplayElement.BgWidth)
        oDataDisplayElement.BgWidth = 300
        self.m_logger.WriteLine3("\t\t\tThe new BgWidth is: {0}", oDataDisplayElement.BgWidth)
        Assert.assertEqual(300, oDataDisplayElement.BgWidth)
        # BgHeight
        self.m_logger.WriteLine3("\t\t\tThe current BgHeight is: {0}", oDataDisplayElement.BgHeight)
        oDataDisplayElement.BgHeight = 150
        self.m_logger.WriteLine3("\t\t\tThe new BgHeight is: {0}", oDataDisplayElement.BgHeight)
        Assert.assertEqual(150, oDataDisplayElement.BgHeight)

    # endregion

    # region UseAutoSizeCheck
    def UseAutoSizeCheck(self, oDataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)

        def action72():
            oDataDisplayElement.BgWidth = 500

        TryCatchAssertBlock.DoAssert("The property should be readonly when UseAutoSizeWidth is False.", action72)

        def action73():
            oDataDisplayElement.BgHeight = 500

        TryCatchAssertBlock.DoAssert("The property should be readonly when UseAutoSizeHeight is False.", action73)

    # endregion

    # region NotUseBackgroundBorderCheck
    def NotUseBackgroundBorderCheck(self, oDataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)

        def action74():
            oDataDisplayElement.BackgroundBorderColor = Color.Black

        # BackgroundBorderColor
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackgroundBorder is False.", action74)

    # endregion

    # region UseBackgroundBorderCheck
    def UseBackgroundBorderCheck(self, oDataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # BackgroundBorderColor
        self.m_logger.WriteLine6(
            "\t\t\tThe current BackgroundBorderColor is: {0}", oDataDisplayElement.BackgroundBorderColor
        )
        oDataDisplayElement.BackgroundBorderColor = Color.Black
        self.m_logger.WriteLine6(
            "\t\t\tThe new BackgroundBorderColor is: {0}", oDataDisplayElement.BackgroundBorderColor
        )
        Assert.assertEqual(Color.Black, oDataDisplayElement.BackgroundBorderColor)

    # endregion

    # region NotUseBackgroundTextureCheck
    def NotUseBackgroundTextureCheck(self, oDataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)

        def action75():
            oDataDisplayElement.BackgroundTextureFilename = "foo.png"

        # BackgroundTextureFileName
        TryCatchAssertBlock.DoAssert("The property should be readonly when UseBackgroundTexture is False.", action75)

    # endregion

    # region UseBackgroundTextureCheck
    def UseBackgroundTextureCheck(self, oDataDisplayElement: "IVODataDisplayElement"):
        Assert.assertIsNotNone(oDataDisplayElement)
        # BackgroundTextureFileName
        self.m_logger.WriteLine5(
            "\t\t\tThe current BackgroundTextureFileName is: {0}", oDataDisplayElement.BackgroundTextureFilename
        )
        oDataDisplayElement.BackgroundTextureFilename = "Scenario\\Fire.bmp"
        self.m_logger.WriteLine5(
            "\t\t\tThe new BackgroundTextureFileName is: {0}", oDataDisplayElement.BackgroundTextureFilename
        )
        StringAssert.Contains("Fire.bmp", oDataDisplayElement.BackgroundTextureFilename)

    # endregion
