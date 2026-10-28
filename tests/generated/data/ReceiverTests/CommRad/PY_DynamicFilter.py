# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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
import numpy as np
import math as math

global PY_DynamicFilter_init
global PY_DynamicFilter_Inputs
PY_DynamicFilter_init = -1


# ==========================================================================
# PY_DynamicFilter() fctn
# ==========================================================================
def PY_DynamicFilter(argList):
    callMode = str(argList[0])
    if callMode == "None":
        retVal = PY_DynamicFilter_compute(argList)  # do compute
    elif callMode == "register":
        global PY_DynamicFilter_init
        PY_DynamicFilter_init = -1
        retVal = PY_DynamicFilter_register()
    elif callMode == "compute":
        retVal = PY_DynamicFilter_compute(argList)  # do compute
    else:
        retVal = []  # # bad call, return empty list

    return retVal


def PY_DynamicFilter_register():
    return [
        ["ArgumentType = Output; Name = IsDynamic; ArgumentName = IsDynamic"],
        ["ArgumentType = Output; Name = LowerBandlimit; ArgumentName = LowerBandlimit"],
        ["ArgumentType = Output; Name = UpperBandlimit; ArgumentName = UpperBandlimit"],
        ["ArgumentType = Output; Name = NumPoints; ArgumentName = NumPoints"],
        ["ArgumentType = Output; Name = Attenuation; ArgumentName = Attenuation"],
        ["ArgumentType = Input; Name = ObjectPath; ArgumentName = ObjectPath; Type = Value"],
        ["ArgumentType = Input; Name = EpochSec; ArgumentName = EpochSec"],
        ["ArgumentType = Input; Name = DateUTC; ArgumentName = DateUTC; Type = Value"],
        ["ArgumentType = Input; Name = CbName; ArgumentName = CbName; Type = Value"],
        ["ArgumentType = Input; Name = ObjectPosLLA; ArgumentName = ObjectPosLLA; Type = Value"],
        ["ArgumentType = Input; Name = CenterFreq; ArgumentName = CenterFreq; Type = Value"],
        ["ArgumentType = Input; Name = FreqStepSize; ArgumentName = FreqStepSize; Type = Value"],
    ]


def PY_DynamicFilter_compute(inputData):
    # NOTE: argList[0] is the call Mode, which is either None or 'compute'
    global debug
    global PY_DynamicFilter_init
    global PY_DynamicFilter_Inputs
    if PY_DynamicFilter_init < 0:
        PY_DynamicFilter_init = 1
        PY_DynamicFilter_Inputs = g_PluginArrayInterfaceHash["PY_DynamicFilter_Inputs"]

    epochSec = inputData[PY_DynamicFilter_Inputs["EpochSec"]]
    dateUTC = inputData[PY_DynamicFilter_Inputs["DateUTC"]]
    cbName = inputData[PY_DynamicFilter_Inputs["CbName"]]
    objectPath = inputData[PY_DynamicFilter_Inputs["ObjectPath"]]
    objectPosLLA = inputData[PY_DynamicFilter_Inputs["ObjectPosLLA"]]
    centerFreq = float(inputData[PY_DynamicFilter_Inputs["CenterFreq"]])
    freqStepSize = inputData[PY_DynamicFilter_Inputs["FreqStepSize"]]

    # Start model here
    isDynamic = 1
    lowerBandlimit = -20e6
    upperBandlimit = 20e6
    numPoints = 100
    attenuationDb = np.zeros(100000)

    freqStepSize = 10000
    filterSelector = math.floor(epochSec % 3)

    # First filter is...
    # 60 MHz wide w/ zero attenuation at center frequency
    # and -60 dB down at edges
    if filterSelector == 0:
        lowerBandlimit = -30e6
        upperBandlimit = 30e6
    # Second filter is...
    # 30 MHz wide w/ zero attenuation at center frequency
    # and -60 dB down at edges

    elif filterSelector == 1:
        lowerBandlimit = -15e6
        upperBandlimit = 15e6

    # Third filter is...
    # 10 MHz wide w/ zero attenuation at center frequency
    # and -60 dB down at edges
    elif filterSelector == 2:
        lowerBandlimit = -5e6
        upperBandlimit = 5e6

    numPoints = int(1 + (upperBandlimit - lowerBandlimit) / freqStepSize)

    # Make sure we don't blow out the fixed array size
    if numPoints > 100000:
        numPoints = 100000
        freqStepSize = (upperBandlimit - lowerBandlimit) / (numPoints - 1)

    temp = int((numPoints - 1) / 2)
    for i in range(0, temp, 1):
        attenDB = -2
        attenuationDb[int(i)] = attenDB
        attenuationDb[numPoints - 1 - int(i)] = attenDB

    # End model here

    return [isDynamic, lowerBandlimit, upperBandlimit, numPoints, attenuationDb]
