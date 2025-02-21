# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class StkObjectSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_DefaultName: str = "scenario1"
        super(StkObjectSnippets, self).__init__(*args, **kwargs)

    m_Object: "Scenario" = None

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
        StkObjectSnippets.m_Object = clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, Scenario)

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.close_scenario()
        StkObjectSnippets.m_Object = None

    # endregion

    # region DeleteStkObject
    def test_DeleteStkObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SHIP, "Ship1")
        self.DeleteStkObject(obj)

    def DeleteStkObject(self, stkObject: "IStkObject"):
        stkObject.unload()

    # endregion

    # region ExportObjectToFile
    def test_ExportObjectToFile(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.STAR, "star1")
        self.ExportObjectToFile(obj, TestBase.TemporaryDirectory)

    def ExportObjectToFile(self, stkObject: "IStkObject", outputPath: str):
        fileNameWithoutExtension: str = Path.Combine(outputPath, "MySatellite1")
        stkObject.export(fileNameWithoutExtension)

    # endregion

    # region RenameAnObject
    def test_RenameAnObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.STAR, "star1")
        self.RenameAnObject(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.STAR, obj.instance_name)

    def RenameAnObject(self, stkObject: "IStkObject"):
        stkObject.instance_name = "NewObjectName"

    # endregion

    # region ConfigureObjectDescription
    def test_ConfigureObjectDescription(self):
        stkobject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            STKObjectType.FACILITY, "facility1"
        )

        self.ConfigureObjectDescription(stkobject)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "facility1")

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
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "fac1")
        self.AddMetadataToObject(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, obj.instance_name)

    def AddMetadataToObject(self, stkObject: "IStkObject"):
        stkObject.metadata.set("key", "value")

    # endregion

    # region AddReadOnlyMetadataToObject
    def test_AddReadOnlyMetadataToObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "fac1")
        self.AddReadOnlyMetadataToObject(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, obj.instance_name)

    def AddReadOnlyMetadataToObject(self, stkObject: "IStkObject"):
        stkObject.metadata.set("key", "value")
        stkObject.metadata.set_read_only("key", True)

    # endregion

    # region RemoveMetadataFromObject
    def test_RemoveMetadataFromObject(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "fac1")
        obj.metadata.set("key", "value")
        self.RemoveMetadataFromObject(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, obj.instance_name)

    def RemoveMetadataFromObject(self, stkObject: "IStkObject"):
        stkObject.metadata.remove_key("key")

    # endregion

    # region IterateMetadataKeys
    def test_IterateMetadataKeys(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "fac1")
        obj.metadata.set("key1", "value1")
        obj.metadata.set("key2", "value1")
        obj.metadata.set("key3", "value1")
        self.IterateMetadataKeys(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, obj.instance_name)

    def IterateMetadataKeys(self, stkObject: "IStkObject"):
        key: str
        for key in stkObject.metadata.keys:
            Console.WriteLine("Key: {0}, Value: {1}", key, stkObject.metadata[key])

    # endregion

    # region CheckIfMetadataIsReadOnly
    def test_CheckIfMetadataIsReadOnly(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "fac1")
        obj.metadata.set("test", "value")
        obj.metadata.set_read_only("test", True)
        self.CheckIfMetadataIsReadOnly(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, obj.instance_name)

    def CheckIfMetadataIsReadOnly(self, stkObject: "IStkObject"):
        if stkObject.metadata.get_read_only("test"):
            Console.WriteLine("The test Metadata element is ReadOnly.")

    # endregion

    # region CheckIfMetadataContainsKey
    def test_CheckIfMetadataContainsKey(self):
        obj: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "fac1")
        obj.metadata.set("test", "value")
        self.CheckIfMetadataContainsKey(obj)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, obj.instance_name)

    def CheckIfMetadataContainsKey(self, stkObject: "IStkObject"):
        if stkObject.metadata.contains("test"):
            Console.WriteLine("The collection contains the test element.")

    # endregion
