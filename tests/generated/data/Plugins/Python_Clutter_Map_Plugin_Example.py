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

import typing, math
from agi.stk12.plugins.stkradarplugin import IAgStkRadarClutterMapComputeParams
from agi.stk12.plugins.utplugin import AgEUtLogMsgType
from agi.stk12.plugins.attrautomation import AgEAttrAddFlags
from agi.stk12.plugins.stkplugin import AgStkPluginSite


class CAgStkRadarClutterMapPlugin(object):
    def __init__(self):
        self.scope = None
        self.site = None
        self.root = None
        self.display_name = "Python Clutter Map Plugin Example"

        self.CalcToolProvider = None
        self.VectorToolProvider = None

        self.halfPi = math.pi / 2.0

        # plugin configuration properties
        self.ConstantCoefficient = 1
        self.ApplyGrazingMask = False

    def Initialize(self, site: "IAgUtPluginSite") -> bool:
        self.site = AgStkPluginSite(site)
        self.root = self.site.StkRootObject
        if site:
            self.VectorToolProvider = self.site.VectorToolProvider
            self.CalcToolProvider = self.site.CalcToolProvider
        self.site.Message(
            AgEUtLogMsgType.eUtLogMsgInfo, f"{self.display_name} has been initialized by {self.site.SiteName}."
        )
        return True

    def PreCompute(self) -> bool:
        self.site.Message(
            AgEUtLogMsgType.eUtLogMsgInfo, f"{self.display_name} has been pre-computed by {self.site.SiteName}."
        )
        return True

    def Compute(self, result: "IAgStkRadarClutterMapComputeParams") -> bool:
        signal = result.Signal
        clutterPatch = result.ClutterPatch

        signalPower = signal.Power
        patchArea = clutterPatch.Area

        patchClutterCoeff = self.ConstantCoefficient
        if self.ApplyGrazingMask:
            patchPosVel = clutterPatch.PosVelProvider

            patchPosCBF = CartVec(patchPosVel.PositionCBFArray)

            radarLink = result.RadarLink
            radarLinkGeom = radarLink.Geometry
            rdrRcvrPosVel = radarLinkGeom.ReceiveRadarPosVelProvider

            rcvRdrPosCBF = CartVec(rdrRcvrPosVel.PositionCBFArray)
            relPosCbf = patchPosCBF - rcvRdrPosCBF

            surfaceNorm = CartVec(patchPosVel.SurfaceNormalDeticArray)

            grazingAngle = self.halfPi - surfaceNorm.AngleBetween(relPosCbf)
            if grazingAngle < 0:
                grazingAngle = self.halfPi

            patchClutterCoeff = patchClutterCoeff * (grazingAngle / self.halfPi)

        signal.Power *= patchClutterCoeff * patchArea

        signalPol = signal.Polarization
        if signalPol is not None:
            signal.Polarization = result.ConstructOrthogonalPolarization(signalPol)

        self.site.Message(
            AgEUtLogMsgType.eUtLogMsgInfo, f"{self.display_name} has been computed by {self.site.SiteName}."
        )
        return True

    def PostCompute(self) -> bool:
        self.site.Message(
            AgEUtLogMsgType.eUtLogMsgInfo, f"{self.display_name} has been post-computed by {self.site.SiteName}."
        )
        return True

    def Free(self) -> None:
        self.CalcToolProvider = None
        self.VectorToolProvider = None
        self.ConstantCoefficient = None
        self.ApplyGrazingMask = None
        self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"{self.display_name} has been freed by {self.site.SiteName}.")

    def GetPluginConfig(self, pAttrBuilder: "IAgAttrBuilder") -> typing.Any:
        if self.scope is None:
            self.scope = pAttrBuilder.NewScope()
            pAttrBuilder.AddDoubleDispatchProperty(
                self.scope,
                "ConstantCoefficient",
                "ConstantCoefficient",
                "ConstantCoefficient",
                AgEAttrAddFlags.eAddFlagNone,
            )
            pAttrBuilder.AddBoolDispatchProperty(
                self.scope, "ApplyGrazingMask", "ApplyGrazingMask", "ApplyGrazingMask", AgEAttrAddFlags.eAddFlagNone
            )
        return self.scope

    def VerifyPluginConfig(self, pPluginCfgResult: "IAgUtPluginConfigVerifyResult") -> None:
        pass


class CartVec(object):
    def __init__(self, inputArray):
        self.x = float(inputArray[0])
        self.y = float(inputArray[1])
        self.z = float(inputArray[2])

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return CartVec([new_x, new_y, new_z])

    def Mag(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def Dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def Cross(self, other):
        new_x = (self.y * other.z) - (self.z * other.y)
        new_y = (self.z * other.x) - (self.x * other.z)
        new_z = (self.x * other.y) - (self.y * other.x)
        return CartVec([new_x, new_y, new_z])

    def AngleBetween(self, other):
        crossedAngle = self.Cross(other)
        sinTheta = crossedAngle.Mag()
        cosTheta = self.Dot(other)
        return abs(math.atan2(sinTheta, cosTheta))
