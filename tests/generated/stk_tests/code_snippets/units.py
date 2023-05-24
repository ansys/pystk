from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Units(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Units, self).__init__(*args, **kwargs)

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
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region GetCurrentUnitPreference
    def test_GetCurrentUnitPreference(self):
        self.GetCurrentUnitPreference(CodeSnippetsTestBase.m_Root)

    def GetCurrentUnitPreference(self, root):
        # DistanceUnit
        dimensionName = "Distance"
        unitAbbreviation = root.UnitPreferences.GetCurrentUnitAbbrv(dimensionName)

    # endregion

    # region SetCurrentUnitPreference
    def test_SetCurrentUnitPreference(self):
        self.SetCurrentUnitPreference(CodeSnippetsTestBase.m_Root)

        # reverse any changes we made to Unit Preferences
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    def SetCurrentUnitPreference(self, root):
        # DistanceUnit
        root.UnitPreferences.SetCurrentUnit("Distance", "m")

    # endregion

    # region ResetCurrentUnitPreferences
    def test_ResetCurrentUnitPreferences(self):
        self.ResetCurrentUnitPreferences(CodeSnippetsTestBase.m_Root)

    def ResetCurrentUnitPreferences(self, root):
        # Reset Units
        root.UnitPreferences.ResetUnits()

    # endregion

    # region ConvertSingleQuantityUnit
    def test_ConvertSingleQuantityUnit(self):
        self.ConvertSingleQuantityUnit(CodeSnippetsTestBase.m_Root)

    def ConvertSingleQuantityUnit(self, root):
        converter = root.ConversionUtility

        # Old value in miles, new value in km
        newValue = converter.ConvertQuantity("DistanceUnit", "mi", "km", 1.0)

    # endregion

    # region ConvertMultipleQuantityUnits
    def test_ConvertMultipleQuantityUnits(self):
        self.ConvertMultipleQuantityUnits(CodeSnippetsTestBase.m_Root)

    def ConvertMultipleQuantityUnits(self, root):
        converter = root.ConversionUtility

        # ConvertQuantityArray expects a one dimensional array of values to be converted
        # An array of km/sec units
        kmsecUnits = [100, 23]

        # Convert to mi/sec units
        # ConvertQuantityArray returns a one dimensional array of converted values
        misecUnits = converter.ConvertQuantityArray("Rate", "km/sec", "mi/sec", kmsecUnits)

    # endregion

    # region ConvertSingleDateFormat
    def test_ConvertSingleDateFormat(self):
        self.ConvertSingleDateFormat(CodeSnippetsTestBase.m_Root)

    def ConvertSingleDateFormat(self, root):
        converter = root.ConversionUtility

        # Individually
        epsec = converter.ConvertDate("UTCG", "Epsec", "1 Jan 2012 12:00:00.000")
        utcg = converter.ConvertDate("EpSec", "UTCG", "230126401.000")

    # endregion

    # region ConvertMulitpleDateFormats
    def test_ConvertMulitpleDateFormats(self):
        self.ConvertMulitpleDateFormats(CodeSnippetsTestBase.m_Root)

    def ConvertMulitpleDateFormats(self, root):
        converter = root.ConversionUtility

        # In batches
        # ConvertDateArray expects a one dimensional array of dates
        # An array of UTCG dates
        tempDates = ["1 Jan 2012 12:00:00.000", "1 Jan 2012 14:00:00.000"]

        # Convert UTCG array to EpSec
        # ConvertDateArray returns a one dimensional array of converted dates
        converted = converter.ConvertDateArray("UTCG", "Epsec", tempDates)

        i = 0
        while i < Array.Length(converted):
            Console.WriteLine("Date: {0}", converted[i])

            i += 1

    # endregion

    # region CalculateDateSubtraction
    def test_CalculateDateSubtraction(self):
        self.CalculateDateSubtraction(CodeSnippetsTestBase.m_Root)

    def CalculateDateSubtraction(self, root):
        # Create a date representing now
        nowDate = root.ConversionUtility.NewDate("DD/MM/YYYY", DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss.fff"))

        # Dates can be modified using Subtract 52 days
        newDate = nowDate.Subtract("day", 52.0)

        # Differences between dates are calculated from Span function
        span = newDate.Span(nowDate)

        # IAgDate also provides formatting functionalities
        span.ConvertToUnit("min")
        Console.WriteLine("Date(now) in UTCG is: {0}", nowDate.Format("UTCG"))
        Console.WriteLine("Date(52 days before now) in UTCG is: {0}", newDate.Format("UTCG"))
        Console.WriteLine("The difference between now and 52 days ago is {0} minutes!", span.Value)

    # endregion

    # region CalculateDateAddition
    def test_CalculateDateAddition(self):
        self.CalculateDateAddition(CodeSnippetsTestBase.m_Root)

    def CalculateDateAddition(self, root):
        # Create a date representing now
        nowDate = root.ConversionUtility.NewDate("DD/MM/YYYY", DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss.fff"))

        # Dates can be modified using Add 52 days
        newDate = nowDate.Add("day", 52.0)

        # Differences between dates are calculated from Span function
        span = newDate.Span(nowDate)

        # IAgDate also provides formatting functionalities
        span.ConvertToUnit("min")
        Console.WriteLine("Date(now) in UTCG is: {0}", nowDate.Format("UTCG"))
        Console.WriteLine("Date(52 days from now) in UTCG is: {0}", newDate.Format("UTCG"))
        Console.WriteLine("The difference between now and 52 days to come is {0} minutes!", span.Value)

    # endregion

    # region CalculateQuantityAddition
    def test_CalculateQuantityAddition(self):
        self.CalculateQuantityAddition(CodeSnippetsTestBase.m_Root)

    def CalculateQuantityAddition(self, root):
        # Create a quantity representing a 3.1 mile/ 5 km fun run race
        race3mi = root.ConversionUtility.NewQuantity("Distance", "mi", 3.1)
        race5km = root.ConversionUtility.NewQuantity("Distance", "km", 5)

        # Add the two 3.1 mile/ 5 km runs
        race10km = race5km.Add(race3mi)
        Console.Write("The {0} {1} race is also called a ", race10km.Value, race10km.Unit)

        # Convert 10k run to 6.2 mile run internally within the quantity
        race10km.ConvertToUnit("mi")
        Console.WriteLine("{0} {1} race", race10km.Value, race10km.Unit)

    # endregion
