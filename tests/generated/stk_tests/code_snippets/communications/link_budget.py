from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class LinkBudget(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LinkBudget, self).__init__(*args, **kwargs)

    m_DefaultSatName = "GEO"
    m_Satellite = None
    m_DefaultFacilityName = "Facility1"
    m_Facility = None
    m_XmtrObject = None
    m_DefaultXmtrName = "MyXmtr"
    m_RcvrObject = None
    m_DefaultRcvrName = "MyRcvr"
    m_AntennaObject = None
    m_DefaultAntName = "FacilityDish"

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
        scenario = clr.Convert(CodeSnippetsTestBase.m_Root.CurrentScenario, IStkObject)

        LinkBudget.m_Satellite = scenario.Children.New(AgESTKObjectType.eSatellite, LinkBudget.m_DefaultSatName)

        sat = clr.Convert(LinkBudget.m_Satellite, ISatellite)
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        twoBody = clr.Convert(sat.Propagator, IVehiclePropagatorTwoBody)
        twoBody.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        twoBody.InitialState.Representation.Epoch = "1 Jan 2012 12:00:00.000"
        twoBody.InitialState.Representation.AssignClassical(
            AgECoordinateSystem.eCoordinateSystemTrueOfDate, 42166.3, 0.0, 0.0, 0.0, 190, 0.0
        )
        twoBody.Propagate()

        LinkBudget.m_Facility = scenario.Children.New(AgESTKObjectType.eFacility, LinkBudget.m_DefaultFacilityName)

        LinkBudget.m_XmtrObject = clr.CastAs(
            LinkBudget.m_Satellite.Children.New(AgESTKObjectType.eTransmitter, LinkBudget.m_DefaultXmtrName),
            ITransmitter,
        )
        LinkBudget.m_RcvrObject = clr.CastAs(
            LinkBudget.m_Facility.Children.New(AgESTKObjectType.eReceiver, LinkBudget.m_DefaultRcvrName), IReceiver
        )
        LinkBudget.m_AntennaObject = clr.CastAs(
            LinkBudget.m_Facility.Children.New(AgESTKObjectType.eAntenna, LinkBudget.m_DefaultAntName), IAntenna
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        LinkBudget.m_Satellite.Children.Unload(AgESTKObjectType.eTransmitter, LinkBudget.m_DefaultXmtrName)
        LinkBudget.m_XmtrObject = None

        LinkBudget.m_Facility.Children.Unload(AgESTKObjectType.eReceiver, LinkBudget.m_DefaultRcvrName)
        LinkBudget.m_RcvrObject = None

        LinkBudget.m_Facility.Children.Unload(AgESTKObjectType.eAntenna, LinkBudget.m_DefaultAntName)
        LinkBudget.m_AntennaObject = None

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eSatellite, LinkBudget.m_DefaultSatName
        )
        LinkBudget.m_Satellite = None

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eFacility, LinkBudget.m_DefaultFacilityName
        )
        LinkBudget.m_Facility = None

    # endregion

    # region ComputeLinkBudgetSimple
    def test_ComputeLinkBudgetSimple(self):
        self.ComputeLinkBudgetSimple(LinkBudget.m_XmtrObject, LinkBudget.m_RcvrObject)

    def ComputeLinkBudgetSimple(self, geoTransmitter, facilityReceiver):
        xmtrAsStkObject = clr.CastAs(geoTransmitter, IStkObject)
        rcvrAsStkObject = clr.CastAs(facilityReceiver, IStkObject)

        # Set the transmitter to the simple model
        geoTransmitter.SetModel("Simple Transmitter Model")
        simpleTrans = clr.CastAs(geoTransmitter.Model, ITransmitterModelSimple)

        # Set the simple transmitter model's frequency to 3.2 GHz
        simpleTrans.Frequency = 3.2

        # Set the simple transmitter model's EIRP to 60 dBW
        simpleTrans.Eirp = 60.0

        # Set the receiver to the simple model
        facilityReceiver.SetModel("Simple Receiver Model")
        simpleRcvr = clr.CastAs(facilityReceiver.Model, IReceiverModelSimple)

        # Set the simple receiver model's G/T to 60 dB/K
        simpleRcvr.GOverT = 60.0

        # Create an access object for the access between the transmitter and recevier objects
        linkAccess = xmtrAsStkObject.GetAccessToObject(rcvrAsStkObject)

        # Compute access
        linkAccess.ComputeAccess()

        # Get the access intervals
        accessIntervals = linkAccess.ComputedAccessIntervalTimes

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "Eb/No", "BER"]

        dp = clr.CastAs(linkAccess.DataProviders["Link Information"], IDataProviderTimeVarying)

        index0 = 0
        while index0 < accessIntervals.Count:
            startTime = None
            stopTime = None

            (startTime, stopTime) = accessIntervals.GetInterval(index0)

            result = dp.ExecElements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.DataSets[0].GetValues()
            ebno = result.DataSets[1].GetValues()
            ber = result.DataSets[2].GetValues()

            index1 = 0
            while index1 < len(timeValues):
                time = clr.Convert(timeValues[index1], str)
                ebnoVal = float(ebno[index1])
                berVal = float(ber[index1])
                Console.WriteLine("{0}: Eb/No={1} BER={2}", time, ebnoVal, berVal)

                index1 += 1

            Console.WriteLine()

            index0 += 1

    # endregion

    # region ComputeLinkBudgetComplex
    def test_ComputeLinkBudgetComplex(self):
        scenario = clr.Convert(CodeSnippetsTestBase.m_Root.CurrentScenario, IScenario)

        self.ComputeLinkBudgetComplex(
            LinkBudget.m_XmtrObject, LinkBudget.m_RcvrObject, LinkBudget.m_AntennaObject, scenario.RFEnvironment
        )

    def ComputeLinkBudgetComplex(self, geoTransmitter, facilityReceiver, facilityDish, scenarioRFEnv):
        xmtrAsStkObject = clr.CastAs(geoTransmitter, IStkObject)
        rcvrAsStkObject = clr.CastAs(facilityReceiver, IStkObject)

        # Enable the rain loss computation on the scenario RF environment
        scenarioRFEnv.PropagationChannel.EnableRainLoss = True

        # Set the transmitter to the complex model
        geoTransmitter.SetModel("Complex Transmitter Model")
        complexTrans = clr.CastAs(geoTransmitter.Model, ITransmitterModelComplex)

        # Set the complex transmitter model's frequency to 3.2 GHz
        complexTrans.Frequency = 3.2

        # Set the complex transmitter model's Power to 50 dBW
        complexTrans.Power = 50.0

        # Set the complex transmitter's embedded antenna model to helix
        complexTrans.AntennaControl.SetEmbeddedModel("Helix")

        # Set the beamwidth of the parablic antenna to 2 degrees
        helix = clr.CastAs(complexTrans.AntennaControl.EmbeddedModel, IAntennaModelHelix)
        helix.NumberOfTurns = 30.0

        # Orient the complex transmitter embedded antenna's boresight to point directly at the receiver's location
        complexTrans.AntennaControl.EmbeddedModelOrientation.AssignAzEl(
            287.2, 83.4, AgEAzElAboutBoresight.eAzElAboutBoresightRotate
        )

        # Set the receiver to the complex model
        facilityReceiver.SetModel("Complex Receiver Model")
        complexRcvr = clr.CastAs(facilityReceiver.Model, IReceiverModelComplex)

        # Configure the complex receiver to use the antenna object on the same parent facility, by linking
        complexRcvr.AntennaControl.ReferenceType = AgEAntennaControlRefType.eAntennaControlRefTypeLink
        complexRcvr.AntennaControl.LinkedAntennaObject = "Antenna/FacilityDish"

        # Enable rain loss computation on the receiver
        complexRcvr.UseRain = True
        complexRcvr.RainOutagePercent = 0.001

        # Enable the receiver system noise temperature computation.
        complexRcvr.SystemNoiseTemperature.ComputeType = AgENoiseTempComputeType.eNoiseTempComputeTypeCalculate

        # Enable the antenna noise temperature computation
        complexRcvr.SystemNoiseTemperature.AntennaNoiseTemperature.ComputeType = (
            AgENoiseTempComputeType.eNoiseTempComputeTypeCalculate
        )
        complexRcvr.SystemNoiseTemperature.AntennaNoiseTemperature.UseRain = True

        # Orient the antenna object's boresight to point directly at the transmitter's location
        facilityDish.Orientation.AssignAzEl(202.6, 41.2, AgEAzElAboutBoresight.eAzElAboutBoresightRotate)

        # Set the antenna object's model to parabolic
        facilityDish.SetModel("Parabolic")

        # Set the antenan object's design frequency to match the transmitter's 3.2 GHz
        facilityDish.Model.DesignFrequency = 3.2

        # Set the antenna object's parabolic model diameter to 5 m.
        parabolic = clr.CastAs(facilityDish.Model, IAntennaModelParabolic)
        parabolic.InputType = AgEAntennaModelInputType.eAntennaModelInputTypeDiameter
        parabolic.Diameter = 5.0

        # Create an access object for the access between the transmitter and recevier objects
        linkAccess = xmtrAsStkObject.GetAccessToObject(rcvrAsStkObject)

        # Compute access
        linkAccess.ComputeAccess()

        # Get the access intervals
        accessIntervals = linkAccess.ComputedAccessIntervalTimes

        # Extract the access intervals and the range information for each access interval
        dataPrvElements = ["Time", "Xmtr Gain", "Rcvr Gain", "Eb/No", "BER"]

        dp = clr.CastAs(linkAccess.DataProviders["Link Information"], IDataProviderTimeVarying)

        index0 = 0
        while index0 < accessIntervals.Count:
            startTime = None
            stopTime = None

            (startTime, stopTime) = accessIntervals.GetInterval(index0)

            result = dp.ExecElements(startTime, stopTime, 60, dataPrvElements)

            timeValues = result.DataSets[0].GetValues()
            xmtrGain = result.DataSets[1].GetValues()
            rcvrGain = result.DataSets[2].GetValues()
            ebno = result.DataSets[3].GetValues()
            ber = result.DataSets[4].GetValues()

            index1 = 0
            while index1 < len(timeValues):
                time = clr.Convert(timeValues[index1], str)
                xmtrGainVal = float(xmtrGain[index1])
                rcvrGainVal = float(rcvrGain[index1])
                ebnoVal = float(ebno[index1])
                berVal = float(ber[index1])
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
