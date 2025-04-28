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

import os
import sys

from ansys.stk.core.stkobjects import SensorLocation, STKObjectType
from ansys.stk.core.stkutil import AzElAboutBoresight, EulerOrientationSequenceType, YPRAnglesSequence

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class SensorSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_root(self):
        return CodeSnippetsTestBase.m_Root

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.current_scenario

    def test_CreateSensorSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.CreateSensorSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="CreateSensor",
        description="Attach a Sensor Object to a Vehicle",
        category="STK Objects | Sensor",
        eid="stkobjects~Sensor",
    )
    def CreateSensorSnippet(self, satellite):
        # Satellite satellite: Satellite object
        sensor = satellite.children.new(STKObjectType.SENSOR, "MySensor")

    def test_SensorPropertiesSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.SensorPropertiesSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="SensorProperties",
        description="Set Sensor Properties",
        category="STK Objects | Sensor",
        eid="stkobjects~Sensor",
    )
    def SensorPropertiesSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pattern and set
        sensor.common_tasks.set_pattern_rectangular(20, 25)
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_az_el(90, 60, AzElAboutBoresight.ROTATE)
        # Change location and set
        sensor.set_location_type(SensorLocation.FIXED)
        sensor.location_data.assign_cartesian(-0.0004, -0.0004, 0.004)

    def test_DefineSensorPointingFixedAzElSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.DefineSensorPointingFixedAzElSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="DefineSensorPointingFixedAzEl",
        description="Define sensor pointing fixed AzEl",
        category="STK Objects | Sensor",
        eid="stkobjects~SensorPointingFixed|stkobjects~SensorCommonTasks|stkobjects~SensorCommonTasks~set_pointing_fixed_az_el",
    )
    def DefineSensorPointingFixedAzElSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_az_el(4.5, -45.0, AzElAboutBoresight.ROTATE)

    def test_DefineSensorPointingFixedAxesAzElSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.DefineSensorPointingFixedAxesAzElSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="DefineSensorPointingFixedAxesAzEl",
        description="Define sensor pointing fixed axes AzEl",
        category="STK Objects | Sensor",
        eid="stkobjects~SensorPointingFixedInAxes|stkobjects~SensorCommonTasks|stkobjects~SensorCommonTasks~set_pointing_fixed_axes_az_el",
    )
    def DefineSensorPointingFixedAxesAzElSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_axes_az_el("CentralBody/Sun J2000 Axes", 11, 22, AzElAboutBoresight.HOLD)

    def test_DefineSensorPointingFixedEulerSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.DefineSensorPointingFixedEulerSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="DefineSensorPointingFixedEuler",
        description="Define sensor pointing fixed Euler",
        category="STK Objects | Sensor",
        eid="stkobjects~SensorPointingFixed|stkobjects~SensorCommonTasks|stkobjects~SensorCommonTasks~set_pointing_fixed_euler",
    )
    def DefineSensorPointingFixedEulerSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_euler(EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50)

    def test_DefineSensorPointingFixedAxesEulerSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.DefineSensorPointingFixedAxesEulerSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="DefineSensorPointingFixedAxesEuler",
        description="Define sensor pointing fixed axes Euler",
        category="STK Objects | Sensor",
        eid="stkobjects~SensorPointingFixedInAxes|stkobjects~SensorCommonTasks|stkobjects~SensorCommonTasks~set_pointing_fixed_axes_euler",
    )
    def DefineSensorPointingFixedAxesEulerSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_axes_euler(
            "CentralBody/Sun J2000 Axes", EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50
        )

    def test_DefineSensorPointingFixedQuaternionSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.DefineSensorPointingFixedQuaternionSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="DefineSensorPointingFixedQuaternion",
        description="Define sensor pointing fixed Quaternion",
        category="STK Objects | Sensor",
        eid="stkobjects~SensorPointingFixed|stkobjects~SensorCommonTasks|stkobjects~SensorCommonTasks~set_pointing_fixed_quaternion",
    )
    def DefineSensorPointingFixedQuaternionSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_quaternion(0.1, 0.2, 0.3, 0.4)

    def test_DefineSensorPointingFixedAxesQuaternionSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.DefineSensorPointingFixedAxesQuaternionSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="DefineSensorPointingFixedAxesQuaternion",
        description="Define sensor pointing fixed axes Quaternion",
        category="STK Objects | Sensor",
        eid="stkobjects~SensorPointingFixedInAxes|stkobjects~SensorCommonTasks|stkobjects~SensorCommonTasks~set_pointing_fixed_axes_quaternion",
    )
    def DefineSensorPointingFixedAxesQuaternionSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_axes_quaternion("CentralBody/Sun J2000 Axes", 0.1, 0.2, 0.3, 0.4)

    def test_DefineSensorPointingFixedYPRSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.DefineSensorPointingFixedYPRSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="DefineSensorPointingFixedYPR",
        description="Define sensor pointing fixed YPR",
        category="STK Objects | Sensor",
        eid="stkobjects~SensorPointingFixed|stkobjects~SensorCommonTasks|stkobjects~SensorCommonTasks~set_pointing_fixed_ypr",
    )
    def DefineSensorPointingFixedYPRSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_ypr(YPRAnglesSequence.RPY, 12, 24, 36)

    def test_DefineSensorPointingFixedAxesYPRSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.DefineSensorPointingFixedAxesYPRSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="DefineSensorPointingFixedAxesYPR",
        description="Define sensor pointing fixed axes YPR",
        category="STK Objects | Sensor",
        eid="stkobjects~SensorPointingFixedInAxes|stkobjects~SensorCommonTasks|stkobjects~SensorCommonTasks~set_pointing_fixed_axes_ypr",
    )
    def DefineSensorPointingFixedAxesYPRSnippet(self, sensor):
        # Sensor sensor: Sensor object
        # Change pointing and set
        sensor.common_tasks.set_pointing_fixed_axes_ypr("CentralBody/Sun J2000 Axes", YPRAnglesSequence.RYP, 11, 22, 33)

    def test_SensorBodyMaskSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.SensorBodyMaskSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="SensorBodyMask",
        description="Sensor Body Mask",
        category="STK Objects | Sensor",
        eid="stkobjects~Sensor",
    )
    def SensorBodyMaskSnippet(self, sensor):
        # Sensor sensor: Sensor object
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        sensor.set_az_el_mask_file(
            os.path.join(installPath, "Data", "Resources", "stktraining", "text", "BodyMask_hga.bmsk")
        )

    @category("Graphics Tests")
    def test_SensorPersistenceSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            sensor = parent.children.new(STKObjectType.SENSOR, "sensor")

            self.SensorPersistenceSnippet(sensor)
        finally:
            parent.unload()

    @code_snippet(
        name="SensorPersistence",
        description="Sensor Persistence",
        category="STK Objects | Sensor | Graphics",
        eid="stkobjects~SensorProjection",
    )
    def SensorPersistenceSnippet(self, sensor):
        # Sensor sensor: Sensor object
        projection = sensor.graphics.projection
        projection.persistence = 7200  # sec
        projection.forward_persistence = True
        projection.fill_persistence = True
        sensor.graphics.show_fill = True
        sensor.graphics.percent_translucency = 50
