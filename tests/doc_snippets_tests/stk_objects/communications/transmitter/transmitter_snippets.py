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

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class TransmitterSnippets(CodeSnippetsTestBase):
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

    def test_CreateTransmitterSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.CreateTransmitterSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="CreateTransmitter",
        description="Create a New Transmitter Object",
        category="STK Objects | Communications | Transmitter",
        eid="stkobjects~Transmitter",
    )
    def CreateTransmitterSnippet(self, satellite):
        # IStkObject satellite: STK object
        transmitter = satellite.children.new(STKObjectType.TRANSMITTER, "MyTransmitter")

    def test_ModifyTransmitterSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            transmitter = parent.children.new(STKObjectType.TRANSMITTER, "transmitter")

            self.ModifyTransmitterSnippet(transmitter)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyTransmitter",
        description="Modify a Transmitter's Model Type",
        category="STK Objects | Communications | Transmitter",
        eid="stkobjects~Transmitter",
    )
    def ModifyTransmitterSnippet(self, transmitter):
        # Transmitter transmitter: Transmitter object
        transmitter.set_model("Complex Transmitter Model")
        txModel = transmitter.model
        txModel.frequency = 14  # GHz
        txModel.power = 25  # dBW
        txModel.data_rate = 15  # Mb/sec

    def test_ModifyTransmitterAntennaSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            transmitter = parent.children.new(STKObjectType.TRANSMITTER, "transmitter")

            self.ModifyTransmitterAntennaSnippet(transmitter)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyTransmitterAntenna",
        description="Modify a Transmitter's Embedded Antenna",
        category="STK Objects | Communications | Transmitter",
        eid="stkobjects~Transmitter",
    )
    def ModifyTransmitterAntennaSnippet(self, transmitter):
        # Transmitter transmitter: Transmitter object
        transmitter.set_model("Complex Transmitter Model")
        txModel = transmitter.model
        antennaControl = txModel.antenna_control
        antennaControl.set_embedded_model("Isotropic")
        antennaControl.embedded_model.efficiency = 85  # Percent

    def test_ModifyTransmitterPolarizationPropertiesSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            transmitter = parent.children.new(STKObjectType.TRANSMITTER, "transmitter")

            self.ModifyTransmitterPolarizationPropertiesSnippet(transmitter)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyTransmitterPolarizationProperties",
        description="Modify a Transmitter's Polarization Properties",
        category="STK Objects | Communications | Transmitter",
        eid="stkobjects~Transmitter",
    )
    def ModifyTransmitterPolarizationPropertiesSnippet(self, transmitter):
        # Transmitter transmitter: Transmitter object
        transmitter.set_model("Complex Transmitter Model")
        txModel = transmitter.model
        txModel.enable_polarization = True
        txModel.set_polarization_type(PolarizationType.LINEAR)
        polarization = txModel.polarization
        polarization.reference_axis = PolarizationReferenceAxis.Y
        polarization.tilt_angle = 15  # deg

    def test_ModifyTransmitterPolarizationOrientationAndPositionSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            transmitter = parent.children.new(STKObjectType.TRANSMITTER, "transmitter")

            self.ModifyTransmitterPolarizationOrientationAndPositionSnippet(transmitter)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyTransmitterPolarizationOrientationAndPosition",
        description="Modify a Transmitter's Orientation and Position",
        category="STK Objects | Communications | Transmitter",
        eid="stkobjects~Transmitter",
    )
    def ModifyTransmitterPolarizationOrientationAndPositionSnippet(self, transmitter):
        # Transmitter transmitter: Transmitter object
        transmitter.set_model("Complex Transmitter Model")
        txModel = transmitter.model
        antennaControl = txModel.antenna_control
        antOrientation = antennaControl.embedded_model_orientation
        antOrientation.assign_az_el(0, 90, 1)  # 1 represents Rotate About Boresight
        antOrientation.position_offset.x = 0.0  # m
        antOrientation.position_offset.y = 1  # m
        antOrientation.position_offset.z = 0.25  # m

    def test_ModifyTransmitterModulatorSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            transmitter = parent.children.new(STKObjectType.TRANSMITTER, "transmitter")

            self.ModifyTransmitterModulatorSnippet(transmitter)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyTransmitterModulator",
        description="Modify a Transmitter's Modulator Properties",
        category="STK Objects | Communications | Transmitter",
        eid="stkobjects~Transmitter",
    )
    def ModifyTransmitterModulatorSnippet(self, transmitter):
        # Transmitter transmitter: Transmitter object
        txModel = transmitter.model
        txModel.set_modulator("BPSK")
        txModel.modulator.scale_bandwidth_automatically = True

    def test_ModifyTransmitterFilterSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            transmitter = parent.children.new(STKObjectType.TRANSMITTER, "transmitter")

            self.ModifyTransmitterFilterSnippet(transmitter)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyTransmitterFilter",
        description="Modify a Transmitter Filter",
        category="STK Objects | Communications | Transmitter",
        eid="stkobjects~Transmitter",
    )
    def ModifyTransmitterFilterSnippet(self, transmitter):
        # Transmitter transmitter: Transmitter object
        txModel = transmitter.model
        txModel.enable_filter = True
        txModel.set_filter("Butterworth")
        recFilter = txModel.filter
        recFilter.lower_bandwidth_limit = -20
        recFilter.upper_bandwidth_limit = 20
        recFilter.cut_off_frequency = 10

    def test_TransmitteradditionalGainSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            transmitter = parent.children.new(STKObjectType.TRANSMITTER, "transmitter")

            self.TransmitteradditionalGainSnippet(transmitter)
        finally:
            parent.unload()

    @code_snippet(
        name="TransmitteradditionalGain",
        description="Transmitter additional Gain",
        category="STK Objects | Communications | Transmitter",
        eid="stkobjects~Transmitter",
    )
    def TransmitteradditionalGainSnippet(self, transmitter):
        # Transmitter transmitter: Transmitter object
        txModel = transmitter.model
        gain = txModel.post_transmit_gains_losses.add(-5)  # dB
        gain.identifier = "Example Loss"
