from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class LinkBudget(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LinkBudget, self).__init__(*args, **kwargs)

    m_DefaultSatName: str = "GEO"
    m_Satellite: "IStkObject" = None
    m_DefaultFacilityName: str = "Facility1"
    m_Facility: "IStkObject" = None
    m_XmtrObject: "ITransmitter" = None
    m_DefaultXmtrName: str = "MyXmtr"
    m_RcvrObject: "IReceiver" = None
    m_DefaultRcvrName: str = "MyRcvr"
    m_AntennaObject: "IAntenna" = None
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
        scenario: "IStkObject" = clr.Convert(CodeSnippetsTestBase.m_Root.current_scenario, IStkObject)

        LinkBudget.m_Satellite = scenario.children.new(STK_OBJECT_TYPE.SATELLITE, LinkBudget.m_DefaultSatName)

        sat: "ISatellite" = clr.Convert(LinkBudget.m_Satellite, ISatellite)
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "IVehiclePropagatorTwoBody" = clr.Convert(sat.propagator, IVehiclePropagatorTwoBody)
        twoBody.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        twoBody.initial_state.representation.epoch = "1 Jan 2012 12:00:00.000"
        twoBody.initial_state.representation.assign_classical(
            COORDINATE_SYSTEM.TRUE_OF_DATE, 42166.3, 0.0, 0.0, 0.0, 190, 0.0
        )
        twoBody.propagate()

        LinkBudget.m_Facility = scenario.children.new(STK_OBJECT_TYPE.FACILITY, LinkBudget.m_DefaultFacilityName)

        LinkBudget.m_XmtrObject = clr.CastAs(
            LinkBudget.m_Satellite.children.new(STK_OBJECT_TYPE.TRANSMITTER, LinkBudget.m_DefaultXmtrName), ITransmitter
        )
        LinkBudget.m_RcvrObject = clr.CastAs(
            LinkBudget.m_Facility.children.new(STK_OBJECT_TYPE.RECEIVER, LinkBudget.m_DefaultRcvrName), IReceiver
        )
        LinkBudget.m_AntennaObject = clr.CastAs(
            LinkBudget.m_Facility.children.new(STK_OBJECT_TYPE.ANTENNA, LinkBudget.m_DefaultAntName), IAntenna
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        LinkBudget.m_Satellite.children.unload(STK_OBJECT_TYPE.TRANSMITTER, LinkBudget.m_DefaultXmtrName)
        LinkBudget.m_XmtrObject = None

        LinkBudget.m_Facility.children.unload(STK_OBJECT_TYPE.RECEIVER, LinkBudget.m_DefaultRcvrName)
        LinkBudget.m_RcvrObject = None

        LinkBudget.m_Facility.children.unload(STK_OBJECT_TYPE.ANTENNA, LinkBudget.m_DefaultAntName)
        LinkBudget.m_AntennaObject = None

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, LinkBudget.m_DefaultSatName
        )
        LinkBudget.m_Satellite = None

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.FACILITY, LinkBudget.m_DefaultFacilityName
        )
        LinkBudget.m_Facility = None

    # endregion

    # region ComputeLinkBudgetSimple
    def test_ComputeLinkBudgetSimple(self):
        self.ComputeLinkBudgetSimple(LinkBudget.m_XmtrObject, LinkBudget.m_RcvrObject)

    def ComputeLinkBudgetSimple(self, geoTransmitter: "ITransmitter", facilityReceiver: "IReceiver"):
        xmtrAsStkObject: "IStkObject" = clr.CastAs(geoTransmitter, IStkObject)
        rcvrAsStkObject: "IStkObject" = clr.CastAs(facilityReceiver, IStkObject)

        # Set the transmitter to the simple model
        geoTransmitter.set_model("Simple Transmitter Model")
        simpleTrans: "ITransmitterModelSimple" = clr.CastAs(geoTransmitter.model, ITransmitterModelSimple)

        # Set the simple transmitter model's frequency to 3.2 GHz
        simpleTrans.frequency = 3.2

        # Set the simple transmitter model's EIRP to 60 dBW
        simpleTrans.eirp = 60.0

        # Set the receiver to the simple model
        facilityReceiver.set_model("Simple Receiver Model")
        simpleRcvr: "IReceiverModelSimple" = clr.CastAs(facilityReceiver.model, IReceiverModelSimple)

        # Set the simple receiver model's G/T to 60 dB/K
        simpleRcvr.g_over_t = 60.0

        # Create an access object for the access between the transmitter and recevier objects
        linkAccess: "IStkAccess" = xmtrAsStkObject.get_access_to_object(rcvrAsStkObject)

        # Compute access
        linkAccess.compute_access()

        # Get the access intervals
        accessIntervals: "IIntervalCollection" = linkAccess.computed_access_interval_times

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "Eb/No", "BER"]

        dp: "IDataProviderTimeVarying" = clr.CastAs(
            linkAccess.data_providers["Link Information"], IDataProviderTimeVarying
        )

        index0: int = 0
        while index0 < accessIntervals.count:
            startTime: typing.Any = None
            stopTime: typing.Any = None

            (startTime, stopTime) = accessIntervals.get_interval(index0)

            result: "IDataProviderResult" = dp.exec_elements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.data_sets[0].get_values()
            ebno = result.data_sets[1].get_values()
            ber = result.data_sets[2].get_values()

            index1: int = 0
            while index1 < len(timeValues):
                time: str = clr.Convert(timeValues[index1], str)
                ebnoVal: float = float(ebno[index1])
                berVal: float = float(ber[index1])
                Console.WriteLine("{0}: Eb/No={1} BER={2}", time, ebnoVal, berVal)

                index1 += 1

            Console.WriteLine()

            index0 += 1

    # endregion

    # region ComputeLinkBudgetComplex
    def test_ComputeLinkBudgetComplex(self):
        scenario: "IScenario" = clr.Convert(CodeSnippetsTestBase.m_Root.current_scenario, IScenario)

        self.ComputeLinkBudgetComplex(
            LinkBudget.m_XmtrObject, LinkBudget.m_RcvrObject, LinkBudget.m_AntennaObject, scenario.rf_environment
        )

    def ComputeLinkBudgetComplex(
        self,
        geoTransmitter: "ITransmitter",
        facilityReceiver: "IReceiver",
        facilityDish: "IAntenna",
        scenarioRFEnv: "IRFEnvironment",
    ):
        xmtrAsStkObject: "IStkObject" = clr.CastAs(geoTransmitter, IStkObject)
        rcvrAsStkObject: "IStkObject" = clr.CastAs(facilityReceiver, IStkObject)

        # Enable the rain loss computation on the scenario RF environment
        scenarioRFEnv.propagation_channel.enable_rain_loss = True

        # Set the transmitter to the complex model
        geoTransmitter.set_model("Complex Transmitter Model")
        complexTrans: "ITransmitterModelComplex" = clr.CastAs(geoTransmitter.model, ITransmitterModelComplex)

        # Set the complex transmitter model's frequency to 3.2 GHz
        complexTrans.frequency = 3.2

        # Set the complex transmitter model's Power to 50 dBW
        complexTrans.power = 50.0

        # Set the complex transmitter's embedded antenna model to helix
        complexTrans.antenna_control.set_embedded_model("Helix")

        # Set the beamwidth of the parablic antenna to 2 degrees
        helix: "IAntennaModelHelix" = clr.CastAs(complexTrans.antenna_control.embedded_model, IAntennaModelHelix)
        helix.number_of_turns = 30.0

        # Orient the complex transmitter embedded antenna's boresight to point directly at the receiver's location
        complexTrans.antenna_control.embedded_model_orientation.assign_az_el(287.2, 83.4, AZ_EL_ABOUT_BORESIGHT.ROTATE)

        # Set the receiver to the complex model
        facilityReceiver.set_model("Complex Receiver Model")
        complexRcvr: "IReceiverModelComplex" = clr.CastAs(facilityReceiver.model, IReceiverModelComplex)

        # Configure the complex receiver to use the antenna object on the same parent facility, by linking
        complexRcvr.antenna_control.reference_type = ANTENNA_CONTROL_REFERENCE_TYPE.LINK
        complexRcvr.antenna_control.linked_antenna_object = "Antenna/FacilityDish"

        # Enable rain loss computation on the receiver
        complexRcvr.use_rain = True
        complexRcvr.rain_outage_percent = 0.001

        # Enable the receiver system noise temperature computation.
        complexRcvr.system_noise_temperature.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE

        # Enable the antenna noise temperature computation
        complexRcvr.system_noise_temperature.antenna_noise_temperature.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE
        complexRcvr.system_noise_temperature.antenna_noise_temperature.use_rain = True

        # Orient the antenna object's boresight to point directly at the transmitter's location
        facilityDish.orientation.assign_az_el(202.6, 41.2, AZ_EL_ABOUT_BORESIGHT.ROTATE)

        # Set the antenna object's model to parabolic
        facilityDish.set_model("Parabolic")

        # Set the antenan object's design frequency to match the transmitter's 3.2 GHz
        facilityDish.model.design_frequency = 3.2

        # Set the antenna object's parabolic model diameter to 5 m.
        parabolic: "IAntennaModelParabolic" = clr.CastAs(facilityDish.model, IAntennaModelParabolic)
        parabolic.input_type = ANTENNA_MODEL_INPUT_TYPE.DIAMETER
        parabolic.diameter = 5.0

        # Create an access object for the access between the transmitter and recevier objects
        linkAccess: "IStkAccess" = xmtrAsStkObject.get_access_to_object(rcvrAsStkObject)

        # Compute access
        linkAccess.compute_access()

        # Get the access intervals
        accessIntervals: "IIntervalCollection" = linkAccess.computed_access_interval_times

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "Xmtr Gain", "Rcvr Gain", "Eb/No", "BER"]

        dp: "IDataProviderTimeVarying" = clr.CastAs(
            linkAccess.data_providers["Link Information"], IDataProviderTimeVarying
        )

        index0: int = 0
        while index0 < accessIntervals.count:
            startTime: typing.Any = None
            stopTime: typing.Any = None

            (startTime, stopTime) = accessIntervals.get_interval(index0)

            result: "IDataProviderResult" = dp.exec_elements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.data_sets[0].get_values()
            xmtrGain = result.data_sets[1].get_values()
            rcvrGain = result.data_sets[2].get_values()
            ebno = result.data_sets[3].get_values()
            ber = result.data_sets[4].get_values()

            index1: int = 0
            while index1 < len(timeValues):
                time: str = clr.Convert(timeValues[index1], str)
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
