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

from datetime import datetime
from agi.stk12.plugins.utplugin import AgEUtLogMsgType, AgEUtTimeScale
from agi.stk12.plugins.stkplugin import AgStkPluginSite
from agi.stk12.plugins.asplugin import (
    AgEAsEphemInterpolationMethod,
    AgEAsCovRep,
    AgEAsEphemFileDistanceUnit,
    AgEAsEphemFileTimeUnit,
)


class CAgAsEphemFileReaderPlugin(object):
    def __init__(self):
        # Interfaces
        self.Scope = None
        self.Site = None

        # member variables
        self.Extension = ".txt"

    def Init(self, Site: "IAgUtPluginSite") -> bool:
        self.Site = AgStkPluginSite(Site)
        self.Site.Message(AgEUtLogMsgType.eUtLogMsgDebug, "CAgAsEphemFileReaderPlugin.Init() executed")
        return True

    def Register(self, Result: "IAgAsEphemFileReaderPluginResultReg"):
        Result.FormatID = "EphemFileReaderPythonPlugin"
        Result.Name = "Python Ephem File Reader"
        Result.AddFileExtension(self.Extension)
        self.Site.Message(AgEUtLogMsgType.eUtLogMsgDebug, "CAgAsEphemFileReaderPlugin.Register() executed")
        return

    def Verify(self, Result: "IAgAsEphemFileReaderPluginResultVerify"):
        if not self.Extension in Result.Filename:
            Result.IsValid = False
            Result.Message = "File must have a " + self.Extension + " extension"
            return

        with open(Result.Filename) as EphemFile:
            Lines = EphemFile.readlines()
        if "ECF Position & Velocity" not in Lines[1]:
            Result.IsValid = False
            Result.Message = "File does not seem to be an ECF Position & Velocity Data Report"
        self.Site.Message(AgEUtLogMsgType.eUtLogMsgDebug, "CAgAsEphemFileReaderPlugin.Verify() executed")
        return

    def ReadEphemeris(self, Result: "IAgAsEphemFileReaderPluginResultEphem"):
        Result.CentralBody = "Earth"
        Result.CoordinateSystem = "Fixed"
        Result.InterpolationMethod = AgEAsEphemInterpolationMethod.eAsEphemInterpolationMethodLagrange
        Result.InterpolationOrder = 5
        Result.CovarianceRepresentation = AgEAsCovRep.eAsCovRepRIC
        Result.SetUnits(
            AgEAsEphemFileDistanceUnit.eAsEphemFileDistanceUnitKilometer,
            AgEAsEphemFileTimeUnit.eAsEphemFileTimeUnitSecond,
        )

        with open(Result.Filename) as EphemFile:
            Lines = EphemFile.readlines()
        NumPointsRead = 0

        for Line in Lines[6:]:
            Time = datetime.strptime(Line[:23], "%d %b %Y %H:%M:%S.%f")
            X, Y, Z, Vx, Vy, Vz = [float(item) for item in Line[24:].split()]
            if Result.AddEphemerisOnDate(
                AgEUtTimeScale.eUtTimeScaleUTC,
                Time.year,
                Time.month,
                Time.day,
                Time.hour,
                Time.minute,
                Time.second + (Time.microsecond / 1000000),
                X,
                Y,
                Z,
                Vx,
                Vy,
                Vz,
                None,
            ):
                NumPointsRead += 1
            else:
                self.Site.Message(AgEUtLogMsgType.eUtLogMsgWarning, f"Could not add point #{NumPointsRead}")

        self.Site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"ECF Data Report Reader read {NumPointsRead} points")
        self.Site.Message(AgEUtLogMsgType.eUtLogMsgDebug, "CAgAsEphemFileReaderPlugin.ReadEphemeris() executed")
        return

    def ReadMetaData(self, Result: "IAgAsEphemFileReaderPluginResultData"):
        Result.AddMetaData("My Metadata", "Custom")
        self.Site.Message(AgEUtLogMsgType.eUtLogMsgDebug, "CAgAsEphemFileReaderPlugin.ReadMetaData() executed")
        return

    def Free(self):
        self.Site.Message(AgEUtLogMsgType.eUtLogMsgDebug, "CAgAsEphemFileReaderPlugin.Free() executed")
        self.Site = None
        return
