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

from test_util import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class ReportComparison(object):
    def __init__(self, Units: "UnitPreferencesDimensionCollection"):
        Assert.assertIsNotNone(Units)
        self._reports = []
        self._omsnapshots = []
        self._cnsnapshots = []
        self.m_oUnits: "UnitPreferencesDimensionCollection" = Units

    # region AddReport

    def AddReport(self, ReportObject: "IStkObject", ReportData: str):
        self._reports.append(ReportComparison.ReportEntry(((("GetReport " + ReportObject.path) + " ") + ReportData)))

    def AddReport2(self, ReportObject: "IStkObject", ReportData: str, Delta: float):
        self._reports.append(
            ReportComparison.ReportEntry(((("GetReport " + ReportObject.path) + " ") + ReportData), Delta)
        )

    def AddReport3(self, Report: str):
        self._reports.append(ReportComparison.ReportEntry(Report))

    def AddReport4(self, Report: str, Delta: float):
        self._reports.append(ReportComparison.ReportEntry(Report, Delta))

    # endregion

    # region TakeOMSnapshot

    def TakeOMSnapshot(self, oRoot: "StkObjectRoot"):
        for report in self._reports:
            report.Execute(oRoot)

        self._omsnapshots.append(self.InternalClone())

    # endregion

    # region TakeConnectSnapshot

    def TakeConnectSnapshot(self, oRoot: "StkObjectRoot"):
        for report in self._reports:
            report.Execute(oRoot)

        self._cnsnapshots.append(self.InternalClone())

        self.ResetUnits()  # Note: This is done to support back and forth testing strategies affected

    # endregion

    # region CompareReportSnapshots

    def CompareReportSnapshots(self):
        # logger.WriteLine("{0}:{1}", _omsnapshots.Count, _cnsnapshots.Count );
        Assert.assertTrue(
            (
                ((len(self._omsnapshots) > 0) and (len(self._cnsnapshots) > 0))
                and (len(self._omsnapshots) == len(self._cnsnapshots))
            )
        )

        i: int = 0
        while i < len(self._omsnapshots):
            # logger.WriteLine("Report {0}", i+1);
            omreps = self._omsnapshots[i]
            cnreps = self._cnsnapshots[i]
            Assert.assertTrue((((len(omreps) > 0) and (len(cnreps) > 0)) and (len(omreps) == len(cnreps))))

            j: int = 0
            while j < len(omreps):
                omrep = omreps[j]
                cnrep = cnreps[j]
                # logger.WriteLine("!Object Model\n" + omrep.Name + "\n" + omrep.FormatReport()+"!");
                # logger.WriteLine("!Connect\n" + cnrep.Name + "\n" + cnrep.FormatReport()+"!");
                omrep.AssertIsEqualTo(cnrep, 0.001)

                j += 1

            i += 1

    # endregion

    # region ResetUnits

    def ResetUnits(self):
        self.m_oUnits.set_current_unit("DistanceUnit", "m")
        self.m_oUnits.set_current_unit("TimeUnit", "sec")
        self.m_oUnits.set_current_unit("DateFormat", "UTCG")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        self.m_oUnits.set_current_unit("MassUnit", "kg")
        self.m_oUnits.set_current_unit("PowerUnit", "dBW")
        self.m_oUnits.set_current_unit("FrequencyUnit", "Ghz")
        self.m_oUnits.set_current_unit("SmallDistanceUnit", "m")
        self.m_oUnits.set_current_unit("LatitudeUnit", "deg")
        self.m_oUnits.set_current_unit("LongitudeUnit", "deg")
        self.m_oUnits.set_current_unit("DurationUnit", "HMS")
        self.m_oUnits.set_current_unit("Temperature", "K")
        self.m_oUnits.set_current_unit("SmallTimeUnit", "sec")
        self.m_oUnits.set_current_unit("RatioUnit", "dB")
        self.m_oUnits.set_current_unit("RcsUnit", "dBsm")
        self.m_oUnits.set_current_unit("DopplerVelocityUnit", "m/s")
        self.m_oUnits.set_current_unit("SARTimeResProdUnit", "m-sec")
        self.m_oUnits.set_current_unit("ForceUnit", "N")
        self.m_oUnits.set_current_unit("PressureUnit", "Pa")
        self.m_oUnits.set_current_unit("SpecificImpulseUnit", "s")
        self.m_oUnits.set_current_unit("PRFUnit", "Khz")
        self.m_oUnits.set_current_unit("BandwidthUnit", "Mhz")
        self.m_oUnits.set_current_unit("SmallVelocityUnit", "cm/s")
        self.m_oUnits.set_current_unit("BitsUnit", "Mb")
        self.m_oUnits.set_current_unit("Percent", "%")
        self.m_oUnits.set_current_unit("MagneticFieldUnit", "nT")

    # endregion

    # region Clone

    def InternalClone(self):
        tmp = []
        for report in self._reports:
            tmp.append(ReportComparison.ReportEntry.ConstructFrom(report))

        return tmp

    # endregion

    class ReportEntry(object):
        def __init__(self, ReportName: str, Delta: float = 0.0):
            self._report = []
            self._name: str = ReportName
            self._delta: float = Delta

        @staticmethod
        def ConstructFrom(other):
            newReport = ReportComparison.ReportEntry(other._name, other._delta)
            for row in other._report:
                newReport._report.append([])

            return newReport

        # region Report

        @property
        def Report(self):
            return self._report

        # endregion

        # region Name

        @property
        def Name(self):
            return self._name

        # endregion

        # region Delta

        @property
        def Delta(self):
            return self._delta

        # endregion

        # region Execute

        def Execute(self, oRoot: "StkObjectRoot"):
            Assert.assertIsNotNone(oRoot)
            self._report.clear()
            res: "ExecuteCommandResult" = oRoot.execute_command(self._name)
            row: str
            for row in res:
                s: "List[str]" = String.Split(row.replace('"', " "), ",")
                self._report.append([])

        # endregion

        # region AssertIsEqualTo

        def AssertIsEqualTo(self, rhs, dDelta: float):
            Assert.assertEqual(len(self._report), len(rhs._report))

            i: int = 0
            while i < len(rhs._report):
                lhsrow = self._report[i]
                rhsrow = rhs._report[i]
                Assert.assertEqual(len(lhsrow), len(rhsrow))

                j: int = 0
                while j < len(rhsrow):
                    lhscol: str = lhsrow[j]
                    rhscol: str = rhsrow[j]

                    lhschr = Regex.Matches(lhscol, r"[^\d\s\-\+\.]+")
                    rhschr = Regex.Matches(rhscol, r"[^\d\s\-\+\.]+")
                    Assert.assertEqual(lhschr.Count, rhschr.Count)

                    c: int = 0
                    while c < rhschr.Count:
                        Assert.assertEqual(lhschr[c].Value.replace("\\", "/"), rhschr[c].Value.replace("\\", "/"))

                        c += 1

                    if Regex.IsMatch(rhscol, r"[-+]?[\d]*\.?[\d]+"):
                        lhsnum = Regex.Matches(lhscol, r"[-+]?[\d]*\.?[\d]+")
                        rhsnum = Regex.Matches(rhscol, r"[-+]?[\d]*\.?[\d]+")
                        Assert.assertEqual(lhsnum.Count, rhsnum.Count)

                        n: int = 0
                        while n < rhsnum.Count:
                            Assert.assertAlmostEqual(
                                Convert.ToDouble(lhsnum[n].Value), Convert.ToDouble(rhsnum[n].Value), delta=dDelta
                            )

                            n += 1

                    j += 1

                i += 1

        # endregion

        # region FormatReport

        def FormatReport(self):
            repstr: str = ""
            col_len: "List[int]" = Array.Create(100)
            for row in self._report:
                i: int = 0
                while i < len(row):
                    if row[i] != None:
                        if len((row[i])) > col_len[i]:
                            col_len[i] = len((row[i]))

                    i += 1

            for row in self._report:
                rowstr: str = ""

                i: int = 0
                while i < len(row):
                    if rowstr != None:
                        rowstr += self.Indent(((col_len[i] - len((row[i]))) + 4)) + (row[i])

                    else:
                        repstr += self.Indent((col_len[i] + 4))

                    i += 1

                repstr += rowstr + "\n"

            return repstr

        # endregion

        # region Indent

        def Indent(self, n: int):
            str: str = ""

            i: int = 0
            while i < n:
                str += " "

                i += 1

            return str

        # endregion
