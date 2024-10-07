import typing, math
from agi.stk12.plugins.commrdrplugin import IAgStkCommRdrAbsorptionLossPropagateSignalParams
from agi.stk12.plugins.attrautomation import AgEAttrAddFlags
from agi.stk12.plugins.stkplugin import AgStkPluginSite


class CAgStkCommRdrAbsorpLossPlugin(object):
    def __init__(self):
        self.scope = None
        self.site = None
        self.root = None

        self.CalcToolProvider = None
        self.VectorToolProvider = None

        # plugin configuration properties
        self.MaxFoliageDepth = 400

    def __del__(self):
        pass

    def Initialize(self, site: "IAgUtPluginSite") -> bool:
        self.site = AgStkPluginSite(site)
        self.root = self.site.StkRootObject
        self.VectorToolProvider = self.site.VectorToolProvider
        self.CalcToolProvider = self.site.CalcToolProvider
        return True

    def PrePropagateSignal(self) -> bool:
        return True

    def PropagateSignal(self, params: "IAgStkCommRdrAbsorptionLossPropagateSignalParams") -> bool:
        xmtrPosCBF = params.XmtrPosCBF
        rcvrPosCBF = params.RcvrPosCBF
        deltaX = rcvrPosCBF[0] - xmtrPosCBF[0]
        deltaY = rcvrPosCBF[1] - xmtrPosCBF[1]
        deltaZ = rcvrPosCBF[2] - xmtrPosCBF[2]
        distance = math.sqrt(math.pow(deltaX, 2) + math.pow(deltaY, 2) + math.pow(deltaZ, 2))
        distance = self.MaxFoliageDepth if self.MaxFoliageDepth < distance else distance
        loss = (0.2 * math.pow((params.Frequency / 1000000), 0.3)) * math.pow(distance, 0.6)
        params.AbsorpLoss = 1 / math.pow(10, (loss / 10))
        params.NoiseTemp = 273.15 * (1 - (1 / loss))
        return True

    def PostPropagateSignal(self) -> bool:
        return True

    def Free(self) -> None:
        self.CalcToolProvider = None
        self.VectorToolProvider = None

    def GetPluginConfig(self, pAttrBuilder) -> typing.Any:
        if self.scope is None:
            self.scope = pAttrBuilder.NewScope()
            pAttrBuilder.AddDoubleDispatchProperty(
                self.scope, "MaxFoliageDepth", "MaxFoliageDepth", "MaxFoliageDepth", AgEAttrAddFlags.eAddFlagNone
            )
        return self.scope

    def VerifyPluginConfig(self, pPluginCfgResult) -> None:
        pass
