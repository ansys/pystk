import typing
from agi.stk12.plugins.accessconstraintplugin import AgEAccessConstraintObjectType, AgEAccessConstraintDependencyFlags
from agi.stk12.plugins.utplugin import AgEUtLogMsgType
from agi.stk12.plugins.attrautomation import AgEAttrAddFlags
from agi.stk12.plugins.stkplugin import AgStkPluginSite


class CAgAccessConstraintPlugin(object):
    def __init__(self):
        self.scope = None
        self.site = None
        self.root = None
        self.scenario_name = "Scenario Name Not Found"

        # plugin configuration properties
        self.range_scale_factor = 1.0

    @property
    def DisplayName(self) -> str:
        """
        Triggered when the plugin is being registered. This is the name of the constraint used by STK.
        The DisplayName property may alternatively be defined as a member attribute (see the STK Python API Programmer's Guide).
        """
        return "PythonRangeExample"

    def Register(self, result: "IAccessConstraintPluginResultRegister") -> None:
        """
        Triggered after application start-up, in order to register the constraint for specific STK object pairs for which this constraint is applicable.
        """
        result.BaseObjectType = AgEAccessConstraintObjectType.eAircraft
        result.BaseDependency = AgEAccessConstraintDependencyFlags.eDependencyRelativePosVel
        result.Dimension = "Distance"
        result.MinValue = 0.0

        result.TargetDependency = AgEAccessConstraintDependencyFlags.eDependencyRelativePosVel
        result.AddTarget(AgEAccessConstraintObjectType.eFacility)
        result.AddTarget(AgEAccessConstraintObjectType.eGroundVehicle)
        result.AddTarget(AgEAccessConstraintObjectType.eSatellite)
        result.Register()

        result.Message(
            AgEUtLogMsgType.eUtLogMsgInfo, f"{self.DisplayName}: Register(Aircraft to Facility/GroundVehicle/Satellite)"
        )

        result.BaseObjectType = AgEAccessConstraintObjectType.eFacility
        result.ClearTargets()
        result.AddTarget(AgEAccessConstraintObjectType.eAircraft)
        result.AddTarget(AgEAccessConstraintObjectType.eSatellite)
        result.Register()

        result.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"{self.DisplayName}: Register(Facility to Aircraft/Satellite)")

        result.BaseObjectType = AgEAccessConstraintObjectType.eGroundVehicle
        result.Register()

        result.Message(
            AgEUtLogMsgType.eUtLogMsgInfo, f"{self.DisplayName}: Register(GroundVehicle to Aircraft/Satellite)"
        )

        result.BaseObjectType = AgEAccessConstraintObjectType.eSatellite
        result.ClearTargets()
        result.AddTarget(AgEAccessConstraintObjectType.eAircraft)
        result.AddTarget(AgEAccessConstraintObjectType.eFacility)
        result.AddTarget(AgEAccessConstraintObjectType.eGroundVehicle)
        result.Register()

        result.Message(
            AgEUtLogMsgType.eUtLogMsgInfo, f"{self.DisplayName}: Register(Satellite to Aircraft/Facility/GroundVehicle)"
        )

    def Init(self, site: "IAgUtPluginSite") -> bool:
        """
        Triggered just before the first computational event trigger.
        """
        self.site = AgStkPluginSite(site)
        self.root = self.site.StkRootObject
        self.site.Message(
            AgEUtLogMsgType.eUtLogMsgInfo, f"{self.DisplayName} has been initialized by {self.site.SiteName}."
        )
        return True

    def PreCompute(self, result: "IAccessConstraintPluginResultPreCompute") -> bool:
        """
        Triggered prior to the calls to the Evaluate method, to allow for any required initialization.
        """
        if self.root is not None:
            self.scenario_name = self.root.CurrentScenario.InstanceName
        self.site.Message(
            AgEUtLogMsgType.eUtLogMsgInfo,
            f"{self.DisplayName} is executing PreCompute for Scenario {self.scenario_name}.",
        )
        return True

    def Evaluate(
        self,
        result: "IAccessConstraintPluginResultEval",
        baseData: "IAccessConstraintPluginObjectData",
        targetData: "IAccessConstraintPluginObjectData",
    ) -> bool:
        """
        Triggered when the plugin is evaluated for an access constraint value
        """
        result.Value = result.LightPathRange * self.range_scale_factor
        return True

    def PostCompute(self, result: "IAccessConstraintPluginResultPostCompute") -> bool:
        """
        Triggered after the calls to the Evaluate method, to allow for any required clean up.
        """
        self.site.Message(
            AgEUtLogMsgType.eUtLogMsgInfo,
            f"{self.DisplayName} is executing PostCompute for Scenario {self.scenario_name}.",
        )
        return True

    def Free(self) -> None:
        """
        Triggered just before the plugin is destroyed.
        """
        self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"{self.DisplayName} is executing Free.")
        del self.scope
        del self.root
        del self.site

    def GetPluginConfig(self, pAttrBuilder: "IAgAttrBuilder") -> typing.Any:
        """
        Get an attribute container of the configuration settings.
        """
        if self.scope is None:
            self.scope = pAttrBuilder.NewScope()
            pAttrBuilder.AddDoubleDispatchProperty(
                self.scope,
                "Range Scale Factor",
                "A scale factor applied to LightPathRange",
                "range_scale_factor",
                AgEAttrAddFlags.eAddFlagNone,
            )
        return self.scope

    def VerifyPluginConfig(self, pPluginCfgResult: "IAgUtPluginConfigVerifyResult") -> None:
        """
        Verify the Plugin Config
        """
