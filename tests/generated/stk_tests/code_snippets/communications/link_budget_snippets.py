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
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class LinkBudgetSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LinkBudgetSnippets, self).__init__(*args, **kwargs)

    m_DefaultSatName: str = "GEO"
    m_Satellite: "IStkObject" = None
    m_DefaultFacilityName: str = "Facility1"
    m_Facility: "IStkObject" = None
    m_XmtrObject: "Transmitter" = None
    m_DefaultXmtrName: str = "MyXmtr"
    m_RcvrObject: "Receiver" = None
    m_DefaultRcvrName: str = "MyRcvr"
    m_AntennaObject: "Antenna" = None
    m_DefaultAntName: str = "FacilityDish"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region SetUp
    def setUp(self):
        scenario: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario

        LinkBudgetSnippets.m_Satellite = scenario.children.new(
            STKObjectType.SATELLITE, LinkBudgetSnippets.m_DefaultSatName
        )

        sat: "Satellite" = Satellite(LinkBudgetSnippets.m_Satellite)
        sat.set_propagator_type(PropagatorType.TWO_BODY)
        twoBody: "PropagatorTwoBody" = PropagatorTwoBody(sat.propagator)
        twoBody.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        twoBody.initial_state.representation.epoch = "1 Jan 2012 12:00:00.000"
        twoBody.initial_state.representation.assign_classical(
            CoordinateSystem.TRUE_OF_DATE, 42166.3, 0.0, 0.0, 0.0, 190, 0.0
        )
        twoBody.propagate()

        LinkBudgetSnippets.m_Facility = scenario.children.new(
            STKObjectType.FACILITY, LinkBudgetSnippets.m_DefaultFacilityName
        )

        LinkBudgetSnippets.m_XmtrObject = clr.CastAs(
            LinkBudgetSnippets.m_Satellite.children.new(
                STKObjectType.TRANSMITTER, LinkBudgetSnippets.m_DefaultXmtrName
            ),
            Transmitter,
        )
        LinkBudgetSnippets.m_RcvrObject = clr.CastAs(
            LinkBudgetSnippets.m_Facility.children.new(STKObjectType.RECEIVER, LinkBudgetSnippets.m_DefaultRcvrName),
            Receiver,
        )
        LinkBudgetSnippets.m_AntennaObject = clr.CastAs(
            LinkBudgetSnippets.m_Facility.children.new(STKObjectType.ANTENNA, LinkBudgetSnippets.m_DefaultAntName),
            Antenna,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        LinkBudgetSnippets.m_Satellite.children.unload(STKObjectType.TRANSMITTER, LinkBudgetSnippets.m_DefaultXmtrName)
        LinkBudgetSnippets.m_XmtrObject = None

        LinkBudgetSnippets.m_Facility.children.unload(STKObjectType.RECEIVER, LinkBudgetSnippets.m_DefaultRcvrName)
        LinkBudgetSnippets.m_RcvrObject = None

        LinkBudgetSnippets.m_Facility.children.unload(STKObjectType.ANTENNA, LinkBudgetSnippets.m_DefaultAntName)
        LinkBudgetSnippets.m_AntennaObject = None

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, LinkBudgetSnippets.m_DefaultSatName
        )
        LinkBudgetSnippets.m_Satellite = None

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.FACILITY, LinkBudgetSnippets.m_DefaultFacilityName
        )
        LinkBudgetSnippets.m_Facility = None

    # endregion

    # region ComputeLinkBudgetSimple
    def test_ComputeLinkBudgetSimple(self):
        self.ComputeLinkBudgetSimple(LinkBudgetSnippets.m_XmtrObject, LinkBudgetSnippets.m_RcvrObject)

    def ComputeLinkBudgetSimple(self, geoTransmitter: "Transmitter", facilityReceiver: "Receiver"):
        xmtrAsStkObject: "IStkObject" = clr.CastAs(geoTransmitter, IStkObject)
        rcvrAsStkObject: "IStkObject" = clr.CastAs(facilityReceiver, IStkObject)

        # Set the transmitter to the simple model
        geoTransmitter.model_component_linking.set_component("Simple Transmitter Model")
        simpleTrans: "TransmitterModelSimple" = clr.CastAs(
            geoTransmitter.model_component_linking.component, TransmitterModelSimple
        )

        # Set the simple transmitter model's frequency to 3.2 GHz
        simpleTrans.frequency = 3.2

        # Set the simple transmitter model's EIRP to 60 dBW
        simpleTrans.eirp = 60.0

        # Set the receiver to the simple model
        facilityReceiver.model_component_linking.set_component("Simple Receiver Model")
        simpleRcvr: "ReceiverModelSimple" = clr.CastAs(
            facilityReceiver.model_component_linking.component, ReceiverModelSimple
        )

        # Set the simple receiver model's G/T to 60 dB/K
        simpleRcvr.g_over_t = 60.0

        # Create an access object for the access between the transmitter and recevier objects
        linkAccess: "Access" = xmtrAsStkObject.get_access_to_object(rcvrAsStkObject)

        # Compute access
        linkAccess.compute_access()

        # Get the access intervals
        accessIntervals: "TimeIntervalCollection" = linkAccess.computed_access_interval_times

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "Eb/No", "BER"]

        dp: "DataProviderTimeVarying" = clr.CastAs(
            linkAccess.data_providers["Link Information"], DataProviderTimeVarying
        )

        index0: int = 0
        while index0 < accessIntervals.count:
            startTime: typing.Any = None
            stopTime: typing.Any = None

            (startTime, stopTime) = accessIntervals.get_interval(index0)

            result: "DataProviderResult" = dp.execute_elements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.data_sets[0].get_values()
            ebno = result.data_sets[1].get_values()
            ber = result.data_sets[2].get_values()

            index1: int = 0
            while index1 < len(timeValues):
                time: str = str(timeValues[index1])
                ebnoVal: float = float(ebno[index1])
                berVal: float = float(ber[index1])
                Console.WriteLine("{0}: Eb/No={1} BER={2}", time, ebnoVal, berVal)

                index1 += 1

            Console.WriteLine()

            index0 += 1

    # endregion

    # region ComputeLinkBudgetComplex
    def test_ComputeLinkBudgetComplex(self):
        scenario: "Scenario" = Scenario(CodeSnippetsTestBase.m_Root.current_scenario)

        self.ComputeLinkBudgetComplex(
            LinkBudgetSnippets.m_XmtrObject,
            LinkBudgetSnippets.m_RcvrObject,
            LinkBudgetSnippets.m_AntennaObject,
            scenario.rf_environment,
        )

    def ComputeLinkBudgetComplex(
        self,
        geoTransmitter: "Transmitter",
        facilityReceiver: "Receiver",
        facilityDish: "Antenna",
        scenarioRFEnv: "RFEnvironment",
    ):
        xmtrAsStkObject: "IStkObject" = clr.CastAs(geoTransmitter, IStkObject)
        rcvrAsStkObject: "IStkObject" = clr.CastAs(facilityReceiver, IStkObject)

        # Enable the rain loss computation on the scenario RF environment
        scenarioRFEnv.propagation_channel.enable_rain_loss = True

        # Set the transmitter to the complex model
        geoTransmitter.model_component_linking.set_component("Complex Transmitter Model")
        complexTrans: "TransmitterModelComplex" = clr.CastAs(
            geoTransmitter.model_component_linking.component, TransmitterModelComplex
        )

        # Set the complex transmitter model's frequency to 3.2 GHz
        complexTrans.frequency = 3.2

        # Set the complex transmitter model's Power to 50 dBW
        complexTrans.power = 50.0

        # Set the complex transmitter's embedded antenna model to helix
        complexTrans.antenna_control.embedded_model_component_linking.set_component("Helix")

        # Set the beamwidth of the parablic antenna to 2 degrees
        helix: "AntennaModelHelix" = clr.CastAs(
            complexTrans.antenna_control.embedded_model_component_linking.component, AntennaModelHelix
        )
        helix.number_of_turns = 30.0

        # Orient the complex transmitter embedded antenna's boresight to point directly at the receiver's location
        complexTrans.antenna_control.embedded_model_orientation.assign_az_el(287.2, 83.4, AzElAboutBoresight.ROTATE)

        # Set the receiver to the complex model
        facilityReceiver.model_component_linking.set_component("Complex Receiver Model")
        complexRcvr: "ReceiverModelComplex" = clr.CastAs(
            facilityReceiver.model_component_linking.component, ReceiverModelComplex
        )

        # Configure the complex receiver to use the antenna object on the same parent facility, by linking
        complexRcvr.antenna_control.reference_type = AntennaControlReferenceType.LINK
        complexRcvr.antenna_control.linked_antenna_object = "Antenna/FacilityDish"

        # Enable rain loss computation on the receiver
        complexRcvr.use_rain = True
        complexRcvr.rain_outage_percent = 0.001

        # Enable the receiver system noise temperature computation.
        complexRcvr.system_noise_temperature.compute_type = NoiseTemperatureComputeType.CALCULATE

        # Enable the antenna noise temperature computation
        complexRcvr.system_noise_temperature.antenna_noise_temperature.compute_type = (
            NoiseTemperatureComputeType.CALCULATE
        )
        complexRcvr.system_noise_temperature.antenna_noise_temperature.use_rain = True

        # Orient the antenna object's boresight to point directly at the transmitter's location
        facilityDish.orientation.assign_az_el(202.6, 41.2, AzElAboutBoresight.ROTATE)

        # Set the antenna object's model to parabolic
        facilityDish.model_component_linking.set_component("Parabolic")

        # Set the antenan object's design frequency to match the transmitter's 3.2 GHz
        (IAntennaModel(facilityDish.model_component_linking.component)).design_frequency = 3.2

        # Set the antenna object's parabolic model diameter to 5 m.
        parabolic: "AntennaModelParabolic" = clr.CastAs(
            facilityDish.model_component_linking.component, AntennaModelParabolic
        )
        parabolic.input_type = AntennaModelInputType.DIAMETER
        parabolic.diameter = 5.0

        # Create an access object for the access between the transmitter and recevier objects
        linkAccess: "Access" = xmtrAsStkObject.get_access_to_object(rcvrAsStkObject)

        # Compute access
        linkAccess.compute_access()

        # Get the access intervals
        accessIntervals: "TimeIntervalCollection" = linkAccess.computed_access_interval_times

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "Xmtr Gain", "Rcvr Gain", "Eb/No", "BER"]

        dp: "DataProviderTimeVarying" = clr.CastAs(
            linkAccess.data_providers["Link Information"], DataProviderTimeVarying
        )

        index0: int = 0
        while index0 < accessIntervals.count:
            startTime: typing.Any = None
            stopTime: typing.Any = None

            (startTime, stopTime) = accessIntervals.get_interval(index0)

            result: "DataProviderResult" = dp.execute_elements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.data_sets[0].get_values()
            xmtrGain = result.data_sets[1].get_values()
            rcvrGain = result.data_sets[2].get_values()
            ebno = result.data_sets[3].get_values()
            ber = result.data_sets[4].get_values()

            index1: int = 0
            while index1 < len(timeValues):
                time: str = str(timeValues[index1])
                xmtrGainVal: float = float(xmtrGain[index1])
                rcvrGainVal: float = float(rcvrGain[index1])
                ebnoVal: float = float(ebno[index1])
                berVal: float = float(ber[index1])
                Console.WriteLine(
                    "{0}: Xmtr Gain = {1} Rcvr Gain = {2} Eb/No={3} BER={4}",
                    time,
                    xmtrGainVal,
                    rcvrGainVal,
                    ebnoVal,
                    berVal,
                )

                index1 += 1

            Console.WriteLine()

            index0 += 1

    # endregion
