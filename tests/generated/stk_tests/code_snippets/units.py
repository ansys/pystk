from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkx import *


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

    def GetCurrentUnitPreference(self, root: "IStkObjectRoot"):
        # DistanceUnit
        dimensionName: str = "Distance"
        unitAbbreviation: str = root.unit_preferences.get_current_unit_abbrv(dimensionName)

    # endregion

    # region SetCurrentUnitPreference
    def test_SetCurrentUnitPreference(self):
        self.SetCurrentUnitPreference(CodeSnippetsTestBase.m_Root)

        # reverse any changes we made to Unit Preferences
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    def SetCurrentUnitPreference(self, root: "IStkObjectRoot"):
        # DistanceUnit
        root.unit_preferences.set_current_unit("Distance", "m")

    # endregion

    # region ResetCurrentUnitPreferences
    def test_ResetCurrentUnitPreferences(self):
        self.ResetCurrentUnitPreferences(CodeSnippetsTestBase.m_Root)

    def ResetCurrentUnitPreferences(self, root: "IStkObjectRoot"):
        # Reset Units
        root.unit_preferences.reset_units()

    # endregion

    # region ConvertSingleQuantityUnit
    def test_ConvertSingleQuantityUnit(self):
        self.ConvertSingleQuantityUnit(CodeSnippetsTestBase.m_Root)

    def ConvertSingleQuantityUnit(self, root: "IStkObjectRoot"):
        converter: "IConversionUtility" = root.conversion_utility

        # Old value in miles, new value in km
        newValue: float = converter.convert_quantity("DistanceUnit", "mi", "km", 1.0)

    # endregion

    # region ConvertMultipleQuantityUnits
    def test_ConvertMultipleQuantityUnits(self):
        self.ConvertMultipleQuantityUnits(CodeSnippetsTestBase.m_Root)

    def ConvertMultipleQuantityUnits(self, root: "IStkObjectRoot"):
        converter: "IConversionUtility" = root.conversion_utility

        # ConvertQuantityArray expects a one dimensional array of values to be converted
        # An array of km/sec units
        kmsecUnits = [100, 23]

        # Convert to mi/sec units
        # ConvertQuantityArray returns a one dimensional array of converted values
        misecUnits = converter.convert_quantity_array("Rate", "km/sec", "mi/sec", kmsecUnits)

    # endregion

    # region ConvertSingleDateFormat
    def test_ConvertSingleDateFormat(self):
        self.ConvertSingleDateFormat(CodeSnippetsTestBase.m_Root)

    def ConvertSingleDateFormat(self, root: "IStkObjectRoot"):
        converter: "IConversionUtility" = root.conversion_utility

        # Individually
        epsec: str = converter.convert_date("UTCG", "Epsec", "1 Jan 2012 12:00:00.000")
        utcg: str = converter.convert_date("EpSec", "UTCG", "230126401.000")

    # endregion

    # region ConvertMulitpleDateFormats
    def test_ConvertMulitpleDateFormats(self):
        self.ConvertMulitpleDateFormats(CodeSnippetsTestBase.m_Root)

    def ConvertMulitpleDateFormats(self, root: "IStkObjectRoot"):
        converter: "IConversionUtility" = root.conversion_utility

        # In batches
        # ConvertDateArray expects a one dimensional array of dates
        # An array of UTCG dates
        tempDates = ["1 Jan 2012 12:00:00.000", "1 Jan 2012 14:00:00.000"]

        # Convert UTCG array to EpSec
        # ConvertDateArray returns a one dimensional array of converted dates
        converted = converter.convert_date_array("UTCG", "Epsec", tempDates)

        i: int = 0
        while i < Array.Length(converted):
            Console.WriteLine("Date: {0}", converted[i])

            i += 1

    # endregion

    # region CalculateDateSubtraction
    def test_CalculateDateSubtraction(self):
        self.CalculateDateSubtraction(CodeSnippetsTestBase.m_Root)

    def CalculateDateSubtraction(self, root: "IStkObjectRoot"):
        # Create a date representing now
        nowDate: "IDate" = root.conversion_utility.new_date(
            "DD/MM/YYYY", DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss.fff")
        )

        # Dates can be modified using Subtract 52 days
        newDate: "IDate" = nowDate.subtract("day", 52.0)

        # Differences between dates are calculated from Span function
        span: "IQuantity" = newDate.span(nowDate)

        # IAgDate also provides formatting functionalities
        span.convert_to_unit("min")
        Console.WriteLine("Date(now) in UTCG is: {0}", nowDate.format("UTCG"))
        Console.WriteLine("Date(52 days before now) in UTCG is: {0}", newDate.format("UTCG"))
        Console.WriteLine("The difference between now and 52 days ago is {0} minutes!", span.value)

    # endregion

    # region CalculateDateAddition
    def test_CalculateDateAddition(self):
        self.CalculateDateAddition(CodeSnippetsTestBase.m_Root)

    def CalculateDateAddition(self, root: "IStkObjectRoot"):
        # Create a date representing now
        nowDate: "IDate" = root.conversion_utility.new_date(
            "DD/MM/YYYY", DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss.fff")
        )

        # Dates can be modified using Add 52 days
        newDate: "IDate" = nowDate.add("day", 52.0)

        # Differences between dates are calculated from Span function
        span: "IQuantity" = newDate.span(nowDate)

        # IAgDate also provides formatting functionalities
        span.convert_to_unit("min")
        Console.WriteLine("Date(now) in UTCG is: {0}", nowDate.format("UTCG"))
        Console.WriteLine("Date(52 days from now) in UTCG is: {0}", newDate.format("UTCG"))
        Console.WriteLine("The difference between now and 52 days to come is {0} minutes!", span.value)

    # endregion

    # region CalculateQuantityAddition
    def test_CalculateQuantityAddition(self):
        self.CalculateQuantityAddition(CodeSnippetsTestBase.m_Root)

    def CalculateQuantityAddition(self, root: "IStkObjectRoot"):
        # Create a quantity representing a 3.1 mile/ 5 km fun run race
        race3mi: "IQuantity" = root.conversion_utility.new_quantity("Distance", "mi", 3.1)
        race5km: "IQuantity" = root.conversion_utility.new_quantity("Distance", "km", 5)

        # Add the two 3.1 mile/ 5 km runs
        race10km: "IQuantity" = race5km.add(race3mi)
        Console.Write("The {0} {1} race is also called a ", race10km.value, race10km.unit)

        # Convert 10k run to 6.2 mile run internally within the quantity
        race10km.convert_to_unit("mi")
        Console.WriteLine("{0} {1} race", race10km.value, race10km.unit)

    # endregion
