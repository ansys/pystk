# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

from ansys.stk.core.stkobjects import PolarizationReferenceAxis, PolarizationType, STKObjectType
from ansys.stk.core.stkutil import AzElAboutBoresight

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class ReceiverSnippets(CodeSnippetsTestBase):
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

    def test_CreateReceiverSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.CreateReceiverSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="CreateReceiver",
        description="Create a New Receiver Object",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def CreateReceiverSnippet(self, satellite):
        # IStkObject satellite: STK object
        receiver = satellite.children.new(STKObjectType.RECEIVER, "MyReceiver")

    def test_ModifyReceiverModelSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            receiver = parent.children.new(STKObjectType.RECEIVER, "receiver")

            self.ModifyReceiverModelSnippet(receiver)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyReceiverModel",
        description="Modify Receiver Model Type",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def ModifyReceiverModelSnippet(self, receiver):
        # Receiver receiver: Receiver object
        receiver.set_model("Complex Receiver Model")
        recModel = receiver.model
        recModel.track_frequency_automatically = False
        recModel.frequency = 11.81

    def test_ModifyReceiverAntennaSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            receiver = parent.children.new(STKObjectType.RECEIVER, "receiver")

            self.ModifyReceiverAntennaSnippet(receiver)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyReceiverAntenna",
        description="Modify Receiver Embedded Antenna",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def ModifyReceiverAntennaSnippet(self, receiver):
        # Receiver receiver: Receiver object
        receiver.set_model("Complex Receiver Model")
        recModel = receiver.model
        antennaControl = recModel.antenna_control
        antennaControl.set_embedded_model("Hemispherical")
        antennaControl.embedded_model.efficiency = 85  # Percent

    def test_ModifyReceiverPolarizationSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            receiver = parent.children.new(STKObjectType.RECEIVER, "receiver")

            self.ModifyReceiverPolarizationSnippet(receiver)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyReceiverPolarization",
        description="Modify Receiver Polarization Properties",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def ModifyReceiverPolarizationSnippet(self, receiver):
        # Receiver receiver: Receiver object
        recModel = receiver.model
        recModel.enable_polarization = True
        recModel.set_polarization_type(PolarizationType.LINEAR)
        polarization = recModel.polarization
        polarization.reference_axis = PolarizationReferenceAxis.Z
        polarization.cross_polarization_leakage = -60  # dB

    def test_ModifyReceiverOrientationSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            receiver = parent.children.new(STKObjectType.RECEIVER, "receiver")

            self.ModifyReceiverOrientationSnippet(receiver)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyReceiverOrientation",
        description="Modify Orientation of the Receiver Antenna",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def ModifyReceiverOrientationSnippet(self, receiver):
        # Complex receivers Only
        # Receiver receiver: Receiver object
        receiver.set_model("Complex Receiver Model")
        recModel = receiver.model
        antennaControl = recModel.antenna_control
        antOrientation = antennaControl.embedded_model_orientation
        antOrientation.assign_az_el(45, 85, AzElAboutBoresight.ROTATE)
        antOrientation.position_offset.x = 0.5  # m
        antOrientation.position_offset.y = 0.75  # m
        antOrientation.position_offset.z = 1  # m

    def test_ModifyReceiverSysNoiseTempSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            receiver = parent.children.new(STKObjectType.RECEIVER, "receiver")

            self.ModifyReceiverSysNoiseTempSnippet(receiver)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyReceiverSysNoiseTemp",
        description="Modify Receiver System Noise Temperature",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def ModifyReceiverSysNoiseTempSnippet(self, receiver):
        # Receiver receiver: Receiver object
        receiver.set_model("Complex Receiver Model")
        recModel = receiver.model
        recModel.system_noise_temperature.constant_noise_temperature = 280  # K

    def test_ModifyReceiverDemodulatorSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            receiver = parent.children.new(STKObjectType.RECEIVER, "receiver")

            self.ModifyReceiverDemodulatorSnippet(receiver)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyReceiverDemodulator",
        description="Modify Receiver Demodulator Properties",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def ModifyReceiverDemodulatorSnippet(self, receiver):
        # Receiver receiver: Receiver object
        recModel = receiver.model
        recModel.select_demodulator_automatically = False
        recModel.set_demodulator("16PSK")

    def test_ModifyReceiverFilterSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            receiver = parent.children.new(STKObjectType.RECEIVER, "receiver")

            self.ModifyReceiverFilterSnippet(receiver)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyReceiverFilter",
        description="Modify Receiver Filter Properties",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def ModifyReceiverFilterSnippet(self, receiver):
        # Receiver receiver: Receiver object
        recModel = receiver.model
        recModel.enable_filter = True
        recModel.set_filter("Bessel")
        recFilter = recModel.filter
        recFilter.lower_bandwidth_limit = -20
        recFilter.upper_bandwidth_limit = 20
        recFilter.cut_off_frequency = 10

    def test_ReceiverAdditionalGainSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            receiver = parent.children.new(STKObjectType.RECEIVER, "receiver")

            self.ReceiverAdditionalGainSnippet(receiver)
        finally:
            parent.unload()

    @code_snippet(
        name="ReceiverAdditionalGain",
        description="Receiver additional Gain",
        category="STK Objects | Communications | Receiver",
        eid="stkobjects~Receiver",
    )
    def ReceiverAdditionalGainSnippet(self, receiver):
        # Receiver receiver: Receiver object
        recModel = receiver.model
        gain = recModel.pre_receive_gains_losses.add(5)  # dB
        gain.identifier = "Example Gain"
