import typing
from agi.stk12.plugins.accessconstraintplugin import (
    AgEAccessConstraintObjectType,
    AgEAccessConstraintDependencyFlags,
    AgEAltitudeReference,
    AgEAccessApparentPositionType,
)
from agi.stk12.plugins.utplugin import AgEUtLogMsgType, AgEUtTimeScale, AgEUtFrame
from agi.stk12.plugins.attrautomation import AgEAttrAddFlags
from agi.stk12.plugins.stkplugin import AgStkPluginSite


class CAgAccessConstraintPlugin(object):
    def __init__(self):
        self.scope = None
        self.site = None
        self.root = None
        self.scenario_name = "Scenario Name Not Found"
        self.log_eval_message = True

        # plugin configuration properties
        self.range_scale_factor = 1.0
        self.enable_debug_messages = True

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
        self.log_eval_message = True
        if self.root is not None:
            self.scenario_name = self.root.CurrentScenario.InstanceName
        self.site.Message(
            AgEUtLogMsgType.eUtLogMsgInfo,
            f"{self.DisplayName} is executing PreCompute for Scenario {self.scenario_name}.",
        )
        return True

    def _print_result(self, name: str, method, *args):
        try:
            result = method(*args)
            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"{name}={result}")
        except Exception as e:
            self.site.Message(AgEUtLogMsgType.eUtLogMsgAlarm, f"{name} ERROR: {e}")

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

        if self.enable_debug_messages and self.log_eval_message:
            self.log_eval_message = False

            base_descriptor = baseData.Descriptor
            base_obj = base_descriptor.ObjectPath
            target_obj = targetData.Descriptor.ObjectPath
            self.site.Message(
                AgEUtLogMsgType.eUtLogMsgInfo,
                f"{self.DisplayName} is executing Evaluate between {base_obj} and {target_obj}.",
            )

            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"baseData.Descriptor={baseData.Descriptor}")
            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"baseData.CentralBodyName={baseData.CentralBodyName}")
            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"baseData.SignalSense={baseData.SignalSense}")
            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"baseData.IsClockHost={baseData.IsClockHost}")
            self.site.Message(
                AgEUtLogMsgType.eUtLogMsgInfo, f"baseData.IsRefractionComputed={baseData.IsRefractionComputed}"
            )
            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"baseData.GeometryMask={baseData.GeometryMask}")

            self._print_result("baseData.DayCount_Array", baseData.DayCount_Array, AgEUtTimeScale.eUtTimeScaleUTC)
            self._print_result("baseData.Position_Array", baseData.Position_Array, AgEUtFrame.eUtFrameInertial)
            self._print_result("baseData.Velocity_Array", baseData.Velocity_Array, AgEUtFrame.eUtFrameInertial)
            self._print_result("baseData.Acceleration_Array", baseData.Acceleration_Array, AgEUtFrame.eUtFrameInertial)
            self._print_result("baseData.LatLonAlt_Array", baseData.LatLonAlt_Array)
            self._print_result("baseData.Altitude", baseData.Altitude, AgEAltitudeReference.eEllispoidReference)
            self._print_result(
                "baseData.Range", baseData.Range, AgEAccessApparentPositionType.eLightPathApparentPosition
            )
            self._print_result(
                "baseData.RelativePosition_Array",
                baseData.RelativePosition_Array,
                AgEAccessApparentPositionType.eLightPathApparentPosition,
                AgEUtFrame.eUtFrameInertial,
            )
            self._print_result(
                "baseData.RelativeVelocity_Array",
                baseData.RelativeVelocity_Array,
                AgEAccessApparentPositionType.eLightPathApparentPosition,
                AgEUtFrame.eUtFrameInertial,
            )
            self._print_result(
                "baseData.RelativeAcceleration_Array",
                baseData.RelativeAcceleration_Array,
                AgEAccessApparentPositionType.eProperApparentPosition,
                AgEUtFrame.eUtFrameFixed,
            )
            self._print_result(
                "baseData.ApparentSunPosition_Array", baseData.ApparentSunPosition_Array, AgEUtFrame.eUtFrameInertial
            )
            self._print_result("baseData.Attitude_Array", baseData.Attitude_Array, AgEUtFrame.eUtFrameInertial)
            self._print_result(
                "baseData.AngularVelocity_Array", baseData.AngularVelocity_Array, AgEUtFrame.eUtFrameInertial
            )
            self._print_result(
                "baseData.DateElements_Array", baseData.DateElements_Array, AgEUtTimeScale.eUtTimeScaleUTC
            )
            self._print_result("baseData.DateString", baseData.DateString, "JDate")

            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"base_descriptor.IsValid={base_descriptor.IsValid}")
            self.site.Message(
                AgEUtLogMsgType.eUtLogMsgInfo,
                f"base_descriptor.VectorToolProvider.SourceNameDefault={base_descriptor.VectorToolProvider.SourceNameDefault}",
            )
            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"base_descriptor.ObjectType={base_descriptor.ObjectType}")
            self.site.Message(AgEUtLogMsgType.eUtLogMsgInfo, f"base_descriptor.ObjectPath={base_descriptor.ObjectPath}")
            self.site.Message(
                AgEUtLogMsgType.eUtLogMsgInfo, f"base_descriptor.ShortDescription={base_descriptor.ShortDescription}"
            )
            self.site.Message(
                AgEUtLogMsgType.eUtLogMsgInfo, f"base_descriptor.LongDescription={base_descriptor.LongDescription}"
            )
            self.site.Message(
                AgEUtLogMsgType.eUtLogMsgInfo, f"base_descriptor.CentralBodyName={base_descriptor.CentralBodyName}"
            )
            self.site.Message(
                AgEUtLogMsgType.eUtLogMsgInfo,
                f"base_descriptor.CalcToolProvider.SourceNameDefault={base_descriptor.CalcToolProvider.SourceNameDefault}",
            )

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
            pAttrBuilder.AddBoolDispatchProperty(
                self.scope,
                "Print Debug Messages",
                "Enable/Disable debug messages to the Message Viewer",
                "enable_debug_messages",
                AgEAttrAddFlags.eAddFlagNone,
            )
        return self.scope

    def VerifyPluginConfig(self, pPluginCfgResult: "IAgUtPluginConfigVerifyResult") -> None:
        """
        Verify the Plugin Config
        """
