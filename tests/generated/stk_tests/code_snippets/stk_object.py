from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class StkObject(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_DefaultName: str = "scenario1"
        super(StkObject, self).__init__(*args, **kwargs)

    m_Object: "IScenario" = None

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.InitializeWithNewScenario(False)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        if CodeSnippetsTestBase.m_Root.current_scenario != None:
            CodeSnippetsTestBase.m_Root.close_scenario()
        CodeSnippetsTestBase.m_Root.new_scenario(self.m_DefaultName)
        StkObject.m_Object = clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, IScenario)

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.close_scenario()
        StkObject.m_Object = None

    # endregion

    # region DeleteStkObject
    def test_DeleteStkObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, "Ship1")
        self.DeleteStkObject(obj)

    def DeleteStkObject(self, stkObject: "IStkObject"):
        stkObject.unload()

    # endregion

    # region ExportObjectToFile
    def test_ExportObjectToFile(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.STAR, "star1")
        self.ExportObjectToFile(obj, TestBase.TemporaryDirectory)

    def ExportObjectToFile(self, stkObject: "IStkObject", outputPath: str):
        fileNameWithoutExtension: str = Path.Combine(outputPath, "MySatellite1")
        stkObject.export(fileNameWithoutExtension)

    # endregion

    # region RenameAnObject
    def test_RenameAnObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.STAR, "star1")
        self.RenameAnObject(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.STAR, obj.instance_name)

    def RenameAnObject(self, stkObject: "IStkObject"):
        stkObject.instance_name = "NewObjectName"

    # endregion

    # region ConfigureObjectDescription
    def test_ConfigureObjectDescription(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            STK_OBJECT_TYPE.FACILITY, "facility1"
        )

        self.ConfigureObjectDescription(stkobject)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "facility1")

    def ConfigureObjectDescription(self, stkobject: "IStkObject"):
        # Set STK Object description
        stkobject.long_description = "This is a very very very long description"
        stkobject.short_description = "This is a short description"

        # Get STK Object description
        longDescription: str = stkobject.long_description
        shortDescription: str = stkobject.short_description

    # endregion

    # region AddMetadataToObject
    def test_AddMetadataToObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        self.AddMetadataToObject(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, obj.instance_name)

    def AddMetadataToObject(self, stkObject: "IStkObject"):
        stkObject.metadata.set("key", "value")

    # endregion

    # region AddReadOnlyMetadataToObject
    def test_AddReadOnlyMetadataToObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        self.AddReadOnlyMetadataToObject(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, obj.instance_name)

    def AddReadOnlyMetadataToObject(self, stkObject: "IStkObject"):
        stkObject.metadata.set("key", "value")
        stkObject.metadata.set_read_only("key", True)

    # endregion

    # region RemoveMetadataFromObject
    def test_RemoveMetadataFromObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        obj.metadata.set("key", "value")
        self.RemoveMetadataFromObject(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, obj.instance_name)

    def RemoveMetadataFromObject(self, stkObject: "IStkObject"):
        stkObject.metadata.remove_key("key")

    # endregion

    # region IterateMetadataKeys
    def test_IterateMetadataKeys(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        obj.metadata.set("key1", "value1")
        obj.metadata.set("key2", "value1")
        obj.metadata.set("key3", "value1")
        self.IterateMetadataKeys(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, obj.instance_name)

    def IterateMetadataKeys(self, stkObject: "IStkObject"):
        key: str
        for key in stkObject.metadata.keys:
            Console.WriteLine("Key: {0}, Value: {1}", key, stkObject.metadata[key])

    # endregion

    # region CheckIfMetadataIsReadOnly
    def test_CheckIfMetadataIsReadOnly(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        obj.metadata.set("test", "value")
        obj.metadata.set_read_only("test", True)
        self.CheckIfMetadataIsReadOnly(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, obj.instance_name)

    def CheckIfMetadataIsReadOnly(self, stkObject: "IStkObject"):
        if stkObject.metadata.get_read_only("test"):
            Console.WriteLine("The test Metadata element is ReadOnly.")

    # endregion

    # region CheckIfMetadataContainsKey
    def test_CheckIfMetadataContainsKey(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        obj.metadata.set("test", "value")
        self.CheckIfMetadataContainsKey(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, obj.instance_name)

    def CheckIfMetadataContainsKey(self, stkObject: "IStkObject"):
        if stkObject.metadata.contains("test"):
            Console.WriteLine("The collection contains the test element.")

    # endregion
