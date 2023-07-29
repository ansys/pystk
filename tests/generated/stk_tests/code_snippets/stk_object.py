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
        if CodeSnippetsTestBase.m_Root.CurrentScenario != None:
            CodeSnippetsTestBase.m_Root.CloseScenario()
        CodeSnippetsTestBase.m_Root.NewScenario(self.m_DefaultName)
        StkObject.m_Object = clr.CastAs(CodeSnippetsTestBase.m_Root.CurrentScenario, IScenario)

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CloseScenario()
        StkObject.m_Object = None

    # endregion

    # region DeleteStkObject
    def test_DeleteStkObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eShip, "Ship1")
        self.DeleteStkObject(obj)

    def DeleteStkObject(self, stkObject: "IStkObject"):
        stkObject.Unload()

    # endregion

    # region ExportObjectToFile
    def test_ExportObjectToFile(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eStar, "star1")
        self.ExportObjectToFile(obj, TestBase.TemporaryDirectory)

    def ExportObjectToFile(self, stkObject: "IStkObject", outputPath: str):
        fileNameWithoutExtension: str = Path.Combine(outputPath, "MySatellite1")
        stkObject.Export(fileNameWithoutExtension)

    # endregion

    # region RenameAnObject
    def test_RenameAnObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eStar, "star1")
        self.RenameAnObject(obj)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eStar, obj.InstanceName)

    def RenameAnObject(self, stkObject: "IStkObject"):
        stkObject.InstanceName = "NewObjectName"

    # endregion

    # region ConfigureObjectDescription
    def test_ConfigureObjectDescription(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eFacility, "facility1"
        )

        self.ConfigureObjectDescription(stkobject)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def ConfigureObjectDescription(self, stkobject: "IStkObject"):
        # Set STK Object description
        stkobject.LongDescription = "This is a very very very long description"
        stkobject.ShortDescription = "This is a short description"

        # Get STK Object description
        longDescription: str = stkobject.LongDescription
        shortDescription: str = stkobject.ShortDescription

    # endregion

    # region AddMetadataToObject
    def test_AddMetadataToObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        self.AddMetadataToObject(obj)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, obj.InstanceName)

    def AddMetadataToObject(self, stkObject: "IStkObject"):
        stkObject.Metadata.Set("key", "value")

    # endregion

    # region AddReadOnlyMetadataToObject
    def test_AddReadOnlyMetadataToObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        self.AddReadOnlyMetadataToObject(obj)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, obj.InstanceName)

    def AddReadOnlyMetadataToObject(self, stkObject: "IStkObject"):
        stkObject.Metadata.Set("key", "value")
        stkObject.Metadata.SetReadOnly("key", True)

    # endregion

    # region RemoveMetadataFromObject
    def test_RemoveMetadataFromObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        obj.Metadata.Set("key", "value")
        self.RemoveMetadataFromObject(obj)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, obj.InstanceName)

    def RemoveMetadataFromObject(self, stkObject: "IStkObject"):
        stkObject.Metadata.RemoveKey("key")

    # endregion

    # region IterateMetadataKeys
    def test_IterateMetadataKeys(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        obj.Metadata.Set("key1", "value1")
        obj.Metadata.Set("key2", "value1")
        obj.Metadata.Set("key3", "value1")
        self.IterateMetadataKeys(obj)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, obj.InstanceName)

    def IterateMetadataKeys(self, stkObject: "IStkObject"):
        key: str
        for key in stkObject.Metadata.Keys:
            Console.WriteLine("Key: {0}, Value: {1}", key, stkObject.Metadata[key])

    # endregion

    # region CheckIfMetadataIsReadOnly
    def test_CheckIfMetadataIsReadOnly(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        obj.Metadata.Set("test", "value")
        obj.Metadata.SetReadOnly("test", True)
        self.CheckIfMetadataIsReadOnly(obj)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, obj.InstanceName)

    def CheckIfMetadataIsReadOnly(self, stkObject: "IStkObject"):
        if stkObject.Metadata.GetReadOnly("test"):
            Console.WriteLine("The test Metadata element is ReadOnly.")

    # endregion

    # region CheckIfMetadataContainsKey
    def test_CheckIfMetadataContainsKey(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        obj.Metadata.Set("test", "value")
        self.CheckIfMetadataContainsKey(obj)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, obj.InstanceName)

    def CheckIfMetadataContainsKey(self, stkObject: "IStkObject"):
        if stkObject.Metadata.Contains("test"):
            Console.WriteLine("The collection contains the test element.")

    # endregion
