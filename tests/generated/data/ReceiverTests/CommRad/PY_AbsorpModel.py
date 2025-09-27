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

# -*- coding: utf-8 -*-

global PY_AbsorpModel_init
global PY_AbsorpModel_Inputs

PY_AbsorpModel_init = -1


# ==========================================================================
# PY_AbsorpModel() fctn
# ==========================================================================
def PY_AbsorpModel(argList):

    callMode = str(argList[0])
    if callMode == "None":
        retVal = PY_AbsorpModel_compute(argList)  # do compute
    elif callMode == "register":
        global PY_AbsorpModel_init
        PY_AbsorpModel_init = -1
        retVal = PY_AbsorpModel_register()
    elif callMode == "compute":
        retVal = PY_AbsorpModel_compute(argList)  # do compute
    else:
        retVal = []  # # bad call, return empty list
    return retVal


def PY_AbsorpModel_register():
    return [
        ["ArgumentType = Output; Name = AbsorpLoss; ArgumentName = AbsorpLoss"],
        ["ArgumentType = Output; Name = NoiseTemp; ArgumentName = NoiseTemp"],
        ["ArgumentType = Input; Name = EpochSec; ArgumentName = EpochSec"],
        ["ArgumentType = Input; Name = DateUTC; ArgumentName = DateUTC; Type = Value"],
        ["ArgumentType = Input; Name = CbName; ArgumentName = CbName; Type = Value"],
        ["ArgumentType = Input; Name = Frequency; ArgumentName = Frequency; Type = Value"],
        ["ArgumentType = Input; Name = XmtrPosCBF; ArgumentName = XmtrPosCBF; Type = Value"],
        ["ArgumentType = Input; Name = RcvrPosCBF; ArgumentName = RcvrPosCBF; Type = Value"],
        ["ArgumentType = Input; Name = XmtrPath; ArgumentName = XmtrPath; Type = Value"],
        ["ArgumentType = Input; Name = RcvrPath; ArgumentName = RcvrPath; Type = Value"],
    ]


def PY_AbsorpModel_compute(inputData):
    # NOTE: argList[0] is the call Mode, which is either None or 'compute'
    global debug
    global PY_AbsorpModel_init
    global PY_AbsorpModel_Inputs
    if PY_AbsorpModel_init < 0:

        PY_AbsorpModel_init = 1
        PY_AbsorpModel_Inputs = g_PluginArrayInterfaceHash["PY_AbsorpModel_Inputs"]

    xmtrPos = inputData[PY_AbsorpModel_Inputs["XmtrPosCBF"]]
    rcvrPos = inputData[PY_AbsorpModel_Inputs["RcvrPosCBF"]]
    freq = float(inputData[PY_AbsorpModel_Inputs["Frequency"]])

    range = sqrt((xmtrPos[0] - rcvrPos[0]) ** 2 + (xmtrPos[1] - rcvrPos[1]) ** 2 + (xmtrPos[2] - rcvrPos[2]) ** 2)
    freeSpace = (4 * 3.141592 * range * freq) / 299792458.0
    loss = 10 ** (log10(freeSpace * freeSpace) / 10)
    noiseTemp = 273.15 * (1 - 1.0 / loss)
    abLoss = 1.0 / loss

    return [abLoss, noiseTemp]
