from test_util import *
from assert_extension import *
from assertion_harness import *
from logger import *
from math2 import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class FOMHelper(object):
    def __init__(self, oRoot: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oRoot)
        self.m_oRoot: "IStkObjectRoot" = oRoot

    # region Definition
    def Definition(
        self,
        oDefinition: "IFigureOfMeritDefinition",
        eType: "FIGURE_OF_MERIT_DEFINITION_TYPE",
        assets: "ICoverageAssetListCollection",
    ):
        Assert.assertIsNotNone(oDefinition)

        # Satisfaction
        self.Satisfaction(oDefinition.satisfaction, eType)
        if eType == FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_CONSTRAINT:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionCompute))
            # AccessConstraint
            oConstraint: "IFigureOfMeritDefinitionAccessConstraint" = clr.CastAs(
                oDefinition, IFigureOfMeritDefinitionAccessConstraint
            )
            Assert.assertIsNotNone(oConstraint)
            # AcrossAssets
            self.m_logger.WriteLine6("\t\t\tThe current AcrossAssets is: {0}", oConstraint.across_assets)
            oConstraint.across_assets = FIGURE_OF_MERIT_ACROSS_ASSETS.AVERAGE
            self.m_logger.WriteLine6("\t\t\tThe new AcrossAssets is: {0}", oConstraint.across_assets)
            Assert.assertEqual(FIGURE_OF_MERIT_ACROSS_ASSETS.AVERAGE, oConstraint.across_assets)
            oConstraint.across_assets = FIGURE_OF_MERIT_ACROSS_ASSETS.MAXIMUM
            self.m_logger.WriteLine6("\t\t\tThe new AcrossAssets is: {0}", oConstraint.across_assets)
            Assert.assertEqual(FIGURE_OF_MERIT_ACROSS_ASSETS.MAXIMUM, oConstraint.across_assets)
            oConstraint.across_assets = FIGURE_OF_MERIT_ACROSS_ASSETS.MINIMUM
            self.m_logger.WriteLine6("\t\t\tThe new AcrossAssets is: {0}", oConstraint.across_assets)
            Assert.assertEqual(FIGURE_OF_MERIT_ACROSS_ASSETS.MINIMUM, oConstraint.across_assets)

            def action1():
                oConstraint.across_assets = FIGURE_OF_MERIT_ACROSS_ASSETS.UNKNOWN

            TryCatchAssertBlock.DoAssert("", action1)

            # TimeStep
            self.m_logger.WriteLine6("\t\t\tThe current TimeStep is: {0}", oConstraint.time_step)
            oConstraint.time_step = 123.456
            self.m_logger.WriteLine6("\t\t\tThe new TimeStep is: {0}", oConstraint.time_step)
            Assert.assertEqual(123.456, oConstraint.time_step)
            oConstraint.time_step = 315576000  # max. 10 years

            def action2():
                oConstraint.time_step = 315576001

            TryCatchAssertBlock.DoAssert("", action2)
            oConstraint.time_step = 0.1  # min. 0.1

            def action3():
                oConstraint.time_step = 0.099

            TryCatchAssertBlock.DoAssert("", action3)

            # ConstraintName and Constraint
            oConstraint.constraint = "AngularRate"
            Assert.assertEqual("AngularRate", oConstraint.constraint)
            self.m_logger.WriteLine6("\t\t\tThe current ConstraintName is: {0}", oConstraint.constraint_name)
            oConstraint.constraint_name = FIGURE_OF_MERIT_CONSTRAINT_NAME.ALTITUDE
            self.m_logger.WriteLine6("\t\t\tThe new ConstraintName is: {0}", oConstraint.constraint_name)
            Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.ALTITUDE, oConstraint.constraint_name)

            def action4():
                oConstraint.constraint_name = FIGURE_OF_MERIT_CONSTRAINT_NAME.UNKNOWN

            TryCatchAssertBlock.DoAssert("", action4)
        elif (
            (
                (
                    ((eType == FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_DURATION))
                    or ((eType == FIGURE_OF_MERIT_DEFINITION_TYPE.COVERAGE_TIME))
                )
                or ((eType == FIGURE_OF_MERIT_DEFINITION_TYPE.N_ASSET_COVERAGE))
            )
            or ((eType == FIGURE_OF_MERIT_DEFINITION_TYPE.NUMBER_OF_ACCESSES))
        ) or ((eType == FIGURE_OF_MERIT_DEFINITION_TYPE.NUMBER_OF_GAPS)):
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionCompute))
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_SEPARATION:
            oSeparation: "IFigureOfMeritDefinitionAccessSeparation" = clr.CastAs(
                oDefinition, IFigureOfMeritDefinitionAccessSeparation
            )
            Assert.assertIsNotNone(oSeparation)
            # MinMaxData
            self.DataMinMax(oSeparation.min_max_data)
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.DILUTION_OF_PRECISION:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionCompute))
            # DilutionOfPrecision
            self.DilutionOfPrecision(clr.CastAs(oDefinition, IFigureOfMeritDefinitionDilutionOfPrecision))
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.NAVIGATION_ACCURACY:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionCompute))
            # DilutionOfPrecision
            self.DilutionOfPrecision(clr.CastAs(oDefinition, IFigureOfMeritDefinitionDilutionOfPrecision))
            # NavigationAccuracy
            oNA: "IFigureOfMeritDefinitionNavigationAccuracy" = clr.CastAs(
                oDefinition, IFigureOfMeritDefinitionNavigationAccuracy
            )
            Assert.assertIsNotNone(oNA)
            # Uncertainties
            oUncertainties: "IFigureOfMeritUncertainties" = oNA.uncertainties
            Assert.assertIsNotNone(oUncertainties)
            # ReceiverRange
            self.m_logger.WriteLine6("\t\t\tThe current ReceiverRange is: {0}", oUncertainties.receiver_range)
            oUncertainties.receiver_range = 123.456
            self.m_logger.WriteLine6("\t\t\tThe new ReceiverRange is: {0}", oUncertainties.receiver_range)
            Assert.assertEqual(123.456, oUncertainties.receiver_range)

            def action5():
                oUncertainties.receiver_range = -1.2

            TryCatchAssertBlock.DoAssert("", action5)
            # AssetList (empty)
            assets.remove_all()
            Assert.assertEqual(0, assets.count)
            oList: "IFigureOfMeritAssetListCollection" = oUncertainties.asset_list
            Assert.assertIsNotNone(oList)
            self.m_logger.WriteLine3("\t\t\tThe current AssetList collection contains: {0} elements", oList.count)
            Assert.assertEqual(0, oList.count)
            #
            arAssets = assets.available_assets
            Assert.assertTrue((Array.Length(arAssets) > 0))
            assets.add(str(arAssets[0]))
            Assert.assertEqual(1, assets.count)
            # AssetList
            oList = oUncertainties.asset_list
            Assert.assertIsNotNone(oList)
            self.m_logger.WriteLine3("\t\t\tThe new AssetList collection contains: {0} elements", oList.count)
            Assert.assertEqual(1, oList.count)
            # _NewEnum
            oElem: "IFigureOfMeritAssetListElement"
            # _NewEnum
            for oElem in oList:
                self.m_logger.WriteLine7(
                    "\t\t\t\tElement: Asset = {0}, MethodType = {1}", oElem.asset, oElem.method_type
                )

            # Item
            assetListElement: "IFigureOfMeritAssetListElement" = oList[0]
            Assert.assertIsNotNone(assetListElement)
            # MethodType
            self.m_logger.WriteLine6("\t\t\tThe current MethodType is: {0}", assetListElement.method_type)
            # SetMethodType (eFmNAConstant)
            assetListElement.method_type = FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE.CONSTANT
            self.m_logger.WriteLine6("\t\t\tThe new MethodType is: {0}", assetListElement.method_type)
            Assert.assertEqual(FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE.CONSTANT, assetListElement.method_type)
            # Method
            oMC: "IFigureOfMeritNavigationAccuracyMethodConstant" = clr.CastAs(
                assetListElement.method, IFigureOfMeritNavigationAccuracyMethodConstant
            )
            Assert.assertIsNotNone(oMC)
            # Value
            self.m_logger.WriteLine6("\t\t\t\tThe current Value is: {0}", oMC.value)
            oMC.value = 12.34
            self.m_logger.WriteLine6("\t\t\t\tThe new Value is: {0}", oMC.value)
            Assert.assertEqual(12.34, oMC.value)

            def action6():
                oMC.value = -1.2

            TryCatchAssertBlock.DoAssert("", action6)
            # SetMethodType (eFmNAConstant)
            assetListElement.method_type = FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE.ELEVATION_ANGLE
            self.m_logger.WriteLine6("\t\t\tThe new MethodType is: {0}", assetListElement.method_type)
            Assert.assertEqual(
                FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE.ELEVATION_ANGLE, assetListElement.method_type
            )
            # Method
            oMEA: "IFigureOfMeritNavigationAccuracyMethodElevationAngle" = clr.CastAs(
                assetListElement.method, IFigureOfMeritNavigationAccuracyMethodElevationAngle
            )
            Assert.assertIsNotNone(oMEA)
            # Filename
            self.m_logger.WriteLine5("\t\t\t\tThe current Filename is: {0}", oMEA.filename)
            oMEA.filename = "fom.re"
            self.m_logger.WriteLine5("\t\t\t\tThe new Filename is: {0}", oMEA.filename)
            Assert.assertEqual("fom.re", oMEA.filename)
            Assert.assertEqual(TestBase.GetScenarioFile(oMEA.filename), oMEA.file_path)

            def action7():
                oMEA.filename = ""

            TryCatchAssertBlock.DoAssert("", action7)

            def action8():
                oMEA.filename = "InvalidFile.Name"

            TryCatchAssertBlock.DoAssert("", action8)
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.RESPONSE_TIME:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionCompute))
            # ResponseTime
            oTime: "IFigureOfMeritDefinitionResponseTime" = clr.CastAs(
                oDefinition, IFigureOfMeritDefinitionResponseTime
            )
            Assert.assertIsNotNone(oTime)
            # MinAssets
            self.m_logger.WriteLine3("\t\t\tThe current MinAssets is: {0}", oTime.min_assets)
            oTime.min_assets = 123
            self.m_logger.WriteLine3("\t\t\tThe new MinAssets is: {0}", oTime.min_assets)
            Assert.assertEqual(123, oTime.min_assets)
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.REVISIT_TIME:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionCompute))
            # RevisitTime
            oTime: "IFigureOfMeritDefinitionRevisitTime" = clr.CastAs(oDefinition, IFigureOfMeritDefinitionRevisitTime)
            Assert.assertIsNotNone(oTime)
            # MinAssets
            self.m_logger.WriteLine3("\t\t\tThe current MinAssets is: {0}", oTime.min_assets)
            oTime.min_assets = 123
            self.m_logger.WriteLine3("\t\t\tThe new MinAssets is: {0}", oTime.min_assets)
            Assert.assertEqual(123, oTime.min_assets)
            # EndGapOption
            self.m_logger.WriteLine6("\t\t\tThe current EndGapOption is: {0}", oTime.end_gap_option)
            oTime.end_gap_option = FIGURE_OF_MERIT_END_GAP_OPTION.IGNORE
            self.m_logger.WriteLine6("\t\t\tThe new EndGapOption is: {0}", oTime.end_gap_option)
            Assert.assertEqual(FIGURE_OF_MERIT_END_GAP_OPTION.IGNORE, oTime.end_gap_option)
            oTime.end_gap_option = FIGURE_OF_MERIT_END_GAP_OPTION.INCLUDE
            self.m_logger.WriteLine6("\t\t\tThe new EndGapOption is: {0}", oTime.end_gap_option)
            Assert.assertEqual(FIGURE_OF_MERIT_END_GAP_OPTION.INCLUDE, oTime.end_gap_option)
        elif ((eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SIMPLE_COVERAGE)) or (
            (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.TIME_AVERAGE_GAP)
        ):
            pass
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SYSTEM_RESPONSE_TIME:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionCompute))

            # SystemResponseTime
            srt: "IFigureOfMeritDefinitionSystemResponseTime" = clr.CastAs(
                oDefinition, IFigureOfMeritDefinitionSystemResponseTime
            )
            Assert.assertIsNotNone(srt)

            srt.allow_forward_crosslink = True
            Assert.assertTrue(srt.allow_forward_crosslink)
            srt.allow_forward_crosslink = False
            Assert.assertFalse(srt.allow_forward_crosslink)

            srt.collection_time = 10
            Assert.assertEqual(10, srt.collection_time)

            def action9():
                srt.collection_time = -10

            TryCatchAssertBlock.DoAssert("shouldn't allow negative", action9)

            srt.commanding_time = 20
            Assert.assertEqual(20, srt.commanding_time)

            def action10():
                srt.commanding_time = -10

            TryCatchAssertBlock.DoAssert("shouldn't allow negative", action10)

            srt.command_perp_time = 30
            Assert.assertEqual(30, srt.command_perp_time)

            def action11():
                srt.command_perp_time = -10

            TryCatchAssertBlock.DoAssert("shouldn't allow negative", action11)

            srt.command_station_path = (
                r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name
            ) + "/Satellite/Satellite1"
            Assert.assertEqual(
                (
                    (r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name)
                    + "/Satellite/Satellite1"
                ),
                srt.command_station_path,
            )

            srt.command_station_path = r"NONE"
            Assert.assertEqual(r"", srt.command_station_path)

            def action12():
                srt.command_station_path = r"bogus"

            TryCatchAssertBlock.DoAssert("bogus CommandStationPath", action12)

            srt.downlink_time = 40
            Assert.assertEqual(40, srt.downlink_time)

            def action13():
                srt.downlink_time = -10

            TryCatchAssertBlock.DoAssert("shouldn't allow negative", action13)

            srt.post_collection_time = 50
            Assert.assertEqual(50, srt.post_collection_time)

            def action14():
                srt.post_collection_time = -10

            TryCatchAssertBlock.DoAssert("shouldn't allow negative", action14)

            srt.pre_collection_time = 60
            Assert.assertEqual(60, srt.pre_collection_time)

            def action15():
                srt.pre_collection_time = -10

            TryCatchAssertBlock.DoAssert("shouldn't allow negative", action15)

            srt.receive_station_path = (
                r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name
            ) + "/Satellite/Satellite1"
            Assert.assertEqual(
                (
                    (r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name)
                    + "/Satellite/Satellite1"
                ),
                srt.receive_station_path,
            )

            srt.receive_station_path = r"NONE"
            Assert.assertEqual(r"", srt.receive_station_path)

            def action16():
                srt.receive_station_path = r"bogus"

            TryCatchAssertBlock.DoAssert("bogus ReceiveStationPath", action16)

            srt.time_step = 60
            Assert.assertEqual(60, srt.time_step)

            def action17():
                srt.time_step = -10

            TryCatchAssertBlock.DoAssert("shouldn't allow negative", action17)
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.AGE_OF_DATA:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionAgeOfData))

            # AgeOfData
            aod: "IFigureOfMeritDefinitionAgeOfData" = clr.CastAs(oDefinition, IFigureOfMeritDefinitionAgeOfData)
            Assert.assertIsNotNone(aod)

            aod.min_assets = 1
            Assert.assertEqual(1, aod.min_assets)
            aod.min_assets = 9999
            Assert.assertEqual(9999, aod.min_assets)

            def action18():
                aod.min_assets = 0

            TryCatchAssertBlock.DoAssert("MinAssets below min", action18)

            def action19():
                aod.min_assets = 10000

            TryCatchAssertBlock.DoAssert("MinAssets above max", action19)
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SCALAR_CALCULATION:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionScalarCalculation))

            # Scalar Calculation
            sd: "IFigureOfMeritDefinitionScalarCalculation" = clr.CastAs(
                oDefinition, IFigureOfMeritDefinitionScalarCalculation
            )
            Assert.assertIsNotNone(sd)

            sd.calc_scalar = "CentralBody/Earth ElapsedTimeFromStart"
            Assert.assertEqual("CentralBody/Earth ElapsedTimeFromStart", sd.calc_scalar)

            def action20():
                sd.calc_scalar = "Bogus"

            TryCatchAssertBlock.DoAssert("bogus calcscalar", action20)

            sd.should_update_accesses = True
            Assert.assertTrue(sd.should_update_accesses)
            sd.should_update_accesses = False
            Assert.assertFalse(sd.should_update_accesses)
        elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SYSTEM_AGE_OF_DATA:
            # Compute
            self.Compute(clr.CastAs(oDefinition, IFigureOfMeritDefinitionCompute))

            # SystemAgeOfData
            saod: "IFigureOfMeritDefinitionSystemAgeOfData" = clr.CastAs(
                oDefinition, IFigureOfMeritDefinitionSystemAgeOfData
            )
            Assert.assertIsNotNone(saod)

            saod.command_station_path = (
                r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name
            ) + "/Satellite/Satellite1"
            Assert.assertEqual(
                (
                    (r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name)
                    + "/Satellite/Satellite1"
                ),
                saod.command_station_path,
            )
            saod.command_station_path = r"NONE"
            Assert.assertEqual(r"", saod.command_station_path)

            def action21():
                saod.command_station_path = (
                    r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name
                ) + "/Satellite/Bogus"

            TryCatchAssertBlock.ExpectedException("must be in", action21)

            saod.receive_station_path = (
                r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name
            ) + "/Satellite/Satellite1"
            Assert.assertEqual(
                (
                    (r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name)
                    + "/Satellite/Satellite1"
                ),
                saod.receive_station_path,
            )
            saod.receive_station_path = r"NONE"
            Assert.assertEqual(r"", saod.receive_station_path)

            def action22():
                saod.receive_station_path = (
                    r"/Application/STK/Scenario/" + self.m_oRoot.current_scenario.instance_name
                ) + "/Satellite/Bogus"

            TryCatchAssertBlock.ExpectedException("must be in", action22)

            saod.command_prep_time = 0
            Assert.assertEqual(0, saod.command_prep_time)
            saod.command_prep_time = 10
            Assert.assertEqual(10, saod.command_prep_time)

            def action23():
                saod.command_prep_time = -10

            TryCatchAssertBlock.ExpectedException("invalid", action23)

            saod.commanding_time = 0
            Assert.assertEqual(0, saod.commanding_time)
            saod.commanding_time = 20
            Assert.assertEqual(20, saod.commanding_time)

            def action24():
                saod.commanding_time = -10

            TryCatchAssertBlock.ExpectedException("invalid", action24)

            saod.pre_collection_time = 0
            Assert.assertEqual(0, saod.pre_collection_time)
            saod.pre_collection_time = 30
            Assert.assertEqual(30, saod.pre_collection_time)

            def action25():
                saod.pre_collection_time = -10

            TryCatchAssertBlock.ExpectedException("invalid", action25)

            saod.collection_time = 0
            Assert.assertEqual(0, saod.collection_time)
            saod.collection_time = 40
            Assert.assertEqual(40, saod.collection_time)

            def action26():
                saod.collection_time = -10

            TryCatchAssertBlock.ExpectedException("invalid", action26)

            saod.post_collection_time = 0
            Assert.assertEqual(0, saod.post_collection_time)
            saod.post_collection_time = 50
            Assert.assertEqual(50, saod.post_collection_time)

            def action27():
                saod.post_collection_time = -10

            TryCatchAssertBlock.ExpectedException("invalid", action27)

            saod.downlink_time = 0
            Assert.assertEqual(0, saod.downlink_time)
            saod.downlink_time = 60
            Assert.assertEqual(60, saod.downlink_time)

            def action28():
                saod.downlink_time = -10

            TryCatchAssertBlock.ExpectedException("invalid", action28)

            saod.allow_forward_crosslink = False
            Assert.assertFalse(saod.allow_forward_crosslink)
            saod.allow_forward_crosslink = True
            Assert.assertTrue(saod.allow_forward_crosslink)

            saod.time_step = 1
            Assert.assertEqual(1, saod.time_step)
            saod.time_step = 3600
            Assert.assertEqual(3600, saod.time_step)

            def action29():
                saod.time_step = 0

            TryCatchAssertBlock.ExpectedException("invalid", action29)

            def action30():
                saod.time_step = 3601

            TryCatchAssertBlock.ExpectedException("invalid", action30)
        else:
            Assert.fail("Invalid definition type - {0}", eType)

    # endregion

    # region Compute
    def Compute(self, oCompute: "IFigureOfMeritDefinitionCompute"):
        Assert.assertIsNotNone(oCompute)
        # ComputeType
        self.m_logger.WriteLine6("\t\t\tThe current ComputeType is: {0}", oCompute.compute_type)
        # ComputeSupportedTypes
        arTypes = oCompute.compute_supported_types
        self.m_logger.WriteLine3("\t\t\tThe Compute supports: {0} types", Array.Length(arTypes))

        iIndex: int = 0
        while iIndex < Array.Length(arTypes):
            eComputeType: "FIGURE_OF_MERIT_COMPUTE" = clr.Convert(int(arTypes[iIndex]), FIGURE_OF_MERIT_COMPUTE)
            if not oCompute.is_compute_type_supported(eComputeType):
                Assert.fail("The {0} Compute Type should be supported!", eComputeType)

            # SetComputeType
            oCompute.set_compute_type(eComputeType)
            self.m_logger.WriteLine6("\t\t\t\tThe new ComputeType is: {0}", oCompute.compute_type)
            Assert.assertEqual(eComputeType, oCompute.compute_type)
            if (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    (
                                                        (
                                                            (
                                                                (
                                                                    (
                                                                        (
                                                                            (
                                                                                eComputeType
                                                                                == FIGURE_OF_MERIT_COMPUTE.AVERAGE
                                                                            )
                                                                        )
                                                                        or (
                                                                            (
                                                                                eComputeType
                                                                                == FIGURE_OF_MERIT_COMPUTE.MAXIMUM
                                                                            )
                                                                        )
                                                                    )
                                                                    or (
                                                                        (
                                                                            eComputeType
                                                                            == FIGURE_OF_MERIT_COMPUTE.MINIMUM
                                                                        )
                                                                    )
                                                                )
                                                                or (
                                                                    (
                                                                        eComputeType
                                                                        == FIGURE_OF_MERIT_COMPUTE.STD_DEVIATION
                                                                    )
                                                                )
                                                            )
                                                            or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.MAX_PER_DAY))
                                                        )
                                                        or (
                                                            (
                                                                eComputeType
                                                                == FIGURE_OF_MERIT_COMPUTE.MAX_PERCENT_PER_DAY
                                                            )
                                                        )
                                                    )
                                                    or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.MIN_PER_DAY))
                                                )
                                                or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.MIN_PERCENT_PER_DAY))
                                            )
                                            or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PER_DAY))
                                        )
                                        or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PER_DAY_STD_DEV))
                                    )
                                    or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PERCENT))
                                )
                                or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PERCENT_PER_DAY))
                            )
                            or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PERCENT_PER_DAY_STD_DEV))
                        )
                        or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.TOTAL))
                    )
                    or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.AVG_PER_DAY))
                )
                or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.SUM))
            ) or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.UNIQUE)):

                def action31():
                    definitionData: "IFigureOfMeritDefinitionData" = oCompute.compute

                TryCatchAssertBlock.DoAssert("", action31)
            elif ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PERCENT_TIME_ABOVE)) or (
                (eComputeType == FIGURE_OF_MERIT_COMPUTE.TOTAL_TIME_ABOVE)
            ):
                # IFigureOfMeritDefinitionDataMinAssets
                dataMinAssets: "IFigureOfMeritDefinitionDataMinAssets" = clr.CastAs(
                    oCompute.compute, IFigureOfMeritDefinitionDataMinAssets
                )
                Assert.assertIsNotNone(dataMinAssets)
                # MinAssets
                self.m_logger.WriteLine3("\t\t\t\t\tThe current MinAssets is: {0}", dataMinAssets.min_assets)
                dataMinAssets.min_assets = 123
                self.m_logger.WriteLine3("\t\t\t\t\tThe new MinAssets is: {0}", dataMinAssets.min_assets)
                Assert.assertEqual(123, dataMinAssets.min_assets)

                def action32():
                    dataMinAssets.min_assets = 1234

                TryCatchAssertBlock.DoAssert("", action32)
            elif ((eComputeType == FIGURE_OF_MERIT_COMPUTE.IN_SPAN)) or (
                (eComputeType == FIGURE_OF_MERIT_COMPUTE.IN_SPAN_PER_DAY)
            ):
                self.DataMinMax(clr.CastAs(oCompute.compute, IFigureOfMeritDefinitionDataMinMax))
            elif (
                (
                    ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PERCENT_ABOVE))
                    or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PERCENT_BELOW))
                )
                or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.PERCENT_BELOW_GAPS_ONLY))
            ) or ((eComputeType == FIGURE_OF_MERIT_COMPUTE.NUM_PERCENT_BELOW)):
                dataPercentLevel: "IFigureOfMeritDefinitionDataPercentLevel" = clr.CastAs(
                    oCompute.compute, IFigureOfMeritDefinitionDataPercentLevel
                )
                Assert.assertIsNotNone(dataPercentLevel)
                # PercentLevel
                self.m_logger.WriteLine6("\t\t\t\t\tThe current PercentLevel is: {0}", dataPercentLevel.percent_level)
                dataPercentLevel.percent_level = 23.45
                self.m_logger.WriteLine6("\t\t\t\t\tThe new PercentLevel is: {0}", dataPercentLevel.percent_level)
                Assert.assertEqual(23.45, dataPercentLevel.percent_level)

                def action33():
                    dataPercentLevel.percent_level = 123.456

                TryCatchAssertBlock.DoAssert("", action33)
            else:
                Assert.fail("Invalid definition type - {0}", eComputeType)

            iIndex += 1

    # endregion

    # region Satisfaction
    def Satisfaction(self, oSatisfaction: "IFigureOfMeritSatisfaction", eType: "FIGURE_OF_MERIT_DEFINITION_TYPE"):
        Assert.assertIsNotNone(oSatisfaction)

        bReadOnly: bool = False
        if (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_SEPARATION) or (
            eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SIMPLE_COVERAGE
        ):
            bReadOnly = True

        if bReadOnly:

            def action34():
                oSatisfaction.enable_satisfaction = True

            # EnableSatisfaction
            TryCatchAssertBlock.DoAssert("", action34)

            def action35():
                oSatisfaction.satisfaction_type = FIGURE_OF_MERIT_SATISFACTION_TYPE.AT_LEAST

            # SatisfactionType
            TryCatchAssertBlock.DoAssert("", action35)

            def action36():
                oSatisfaction.satisfaction_threshold = 123.456

            # SatisfactionThreshold
            TryCatchAssertBlock.DoAssert("", action36)

            def action37():
                oSatisfaction.invalid_data_indicator = 1.2

            # InvalidDataIndicator
            TryCatchAssertBlock.DoAssert("", action37)

            def action38():
                oSatisfaction.use_value_range_check = True

            # UseValueRangeCheck
            TryCatchAssertBlock.DoAssert("", action38)

            def action39():
                oSatisfaction.min_value_range = 1.2

            # MinValueRange
            TryCatchAssertBlock.DoAssert("", action39)

            def action40():
                oSatisfaction.max_value_range = 1.2

            # MaxValueRange
            TryCatchAssertBlock.DoAssert("", action40)

            def action41():
                oSatisfaction.exclude_value_range = True

            # ExcludeValueRange
            TryCatchAssertBlock.DoAssert("", action41)

        else:
            # EnableSatisfaction (false)
            self.m_logger.WriteLine4("\t\t\tThe current EnableSatisfaction is: {0}", oSatisfaction.enable_satisfaction)
            oSatisfaction.enable_satisfaction = False
            self.m_logger.WriteLine4("\t\t\tThe new EnableSatisfaction is: {0}", oSatisfaction.enable_satisfaction)
            Assert.assertFalse(oSatisfaction.enable_satisfaction)

            def action42():
                oSatisfaction.satisfaction_type = FIGURE_OF_MERIT_SATISFACTION_TYPE.AT_LEAST

            # SatisfactionType
            TryCatchAssertBlock.DoAssert("", action42)

            def action43():
                oSatisfaction.satisfaction_threshold = 123.456

            # SatisfactionThreshold
            TryCatchAssertBlock.DoAssert("", action43)
            # EnableSatisfaction (true)
            oSatisfaction.enable_satisfaction = True
            self.m_logger.WriteLine4("\t\t\tThe new EnableSatisfaction is: {0}", oSatisfaction.enable_satisfaction)
            Assert.assertTrue(oSatisfaction.enable_satisfaction)
            # SatisfactionType
            self.m_logger.WriteLine6("\t\t\t\tThe current SatisfactionType is: {0}", oSatisfaction.satisfaction_type)
            oSatisfaction.satisfaction_type = FIGURE_OF_MERIT_SATISFACTION_TYPE.AT_LEAST
            self.m_logger.WriteLine6("\t\t\t\tThe new SatisfactionType is: {0}", oSatisfaction.satisfaction_type)
            Assert.assertEqual(FIGURE_OF_MERIT_SATISFACTION_TYPE.AT_LEAST, oSatisfaction.satisfaction_type)
            # SatisfactionThreshold
            self.m_logger.WriteLine6(
                "\t\t\t\tThe current SatisfactionThreshold is: {0}", oSatisfaction.satisfaction_threshold
            )
            if (
                (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.N_ASSET_COVERAGE)
                or (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.NUMBER_OF_ACCESSES)
            ) or (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.NUMBER_OF_GAPS):
                oSatisfaction.satisfaction_threshold = 12
                self.m_logger.WriteLine6(
                    "\t\t\t\tThe new SatisfactionThreshold is: {0}", oSatisfaction.satisfaction_threshold
                )
                Assert.assertEqual(12, oSatisfaction.satisfaction_threshold)

            else:
                oSatisfaction.satisfaction_threshold = 12.34
                self.m_logger.WriteLine6(
                    "\t\t\t\tThe new SatisfactionThreshold is: {0}", oSatisfaction.satisfaction_threshold
                )
                Assert.assertEqual(12.34, oSatisfaction.satisfaction_threshold)

            if eType == FIGURE_OF_MERIT_DEFINITION_TYPE.COVERAGE_TIME:

                def action44():
                    oSatisfaction.satisfaction_threshold = 123.456

                TryCatchAssertBlock.DoAssert("", action44)

            # InvalidDataIndicator
            self.m_logger.WriteLine6(
                "\t\t\t\tThe current InvalidDataIndicator is: {0}", oSatisfaction.invalid_data_indicator
            )
            if (
                (
                    (
                        (
                            (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_CONSTRAINT)
                            or (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.DILUTION_OF_PRECISION)
                        )
                        or (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.NAVIGATION_ACCURACY)
                    )
                    or (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SCALAR_CALCULATION)
                )
                or (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SYSTEM_RESPONSE_TIME)
            ) or (eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SYSTEM_AGE_OF_DATA):
                oSatisfaction.invalid_data_indicator = 12.34
                self.m_logger.WriteLine6(
                    "\t\t\t\tThe new InvalidDataIndicator is: {0}", oSatisfaction.invalid_data_indicator
                )
                Assert.assertEqual(12.34, oSatisfaction.invalid_data_indicator)
                # UseValueRangeCheck (false)
                self.m_logger.WriteLine4(
                    "\t\t\t\tThe current UseValueRangeCheck is: {0}", oSatisfaction.use_value_range_check
                )
                oSatisfaction.use_value_range_check = False
                self.m_logger.WriteLine4(
                    "\t\t\t\tThe new UseValueRangeCheck is: {0}", oSatisfaction.use_value_range_check
                )
                Assert.assertFalse(oSatisfaction.use_value_range_check)

                def action45():
                    oSatisfaction.min_value_range = 1.2

                # MinValueRange
                TryCatchAssertBlock.DoAssert("", action45)

                def action46():
                    oSatisfaction.max_value_range = 1.2

                # MaxValueRange
                TryCatchAssertBlock.DoAssert("", action46)

                def action47():
                    oSatisfaction.exclude_value_range = True

                # ExcludeValueRange
                TryCatchAssertBlock.DoAssert("", action47)
                # UseValueRangeCheck (true)
                oSatisfaction.use_value_range_check = True
                self.m_logger.WriteLine4(
                    "\t\t\t\tThe new UseValueRangeCheck is: {0}", oSatisfaction.use_value_range_check
                )
                Assert.assertTrue(oSatisfaction.use_value_range_check)
                # MinValueRange
                self.m_logger.WriteLine6("\t\t\t\tThe current MinValueRange is: {0}", oSatisfaction.min_value_range)
                oSatisfaction.min_value_range = 1
                self.m_logger.WriteLine6("\t\t\t\tThe new MinValueRange is: {0}", oSatisfaction.min_value_range)
                Assert.assertEqual(1, oSatisfaction.min_value_range)
                # MaxValueRange
                self.m_logger.WriteLine6("\t\t\t\tThe current MaxValueRange is: {0}", oSatisfaction.max_value_range)
                oSatisfaction.max_value_range = 3
                self.m_logger.WriteLine6("\t\t\t\tThe new MaxValueRange is: {0}", oSatisfaction.max_value_range)
                Assert.assertEqual(3, oSatisfaction.max_value_range)
                # ExcludeValueRange
                self.m_logger.WriteLine4(
                    "\t\t\t\tThe current ExcludeValueRange is: {0}", oSatisfaction.exclude_value_range
                )
                oSatisfaction.exclude_value_range = True
                self.m_logger.WriteLine4("\t\t\t\tThe new ExcludeValueRange is: {0}", oSatisfaction.exclude_value_range)
                Assert.assertTrue(oSatisfaction.exclude_value_range)
                oSatisfaction.exclude_value_range = False
                self.m_logger.WriteLine4("\t\t\t\tThe new ExcludeValueRange is: {0}", oSatisfaction.exclude_value_range)
                Assert.assertFalse(oSatisfaction.exclude_value_range)

            else:

                def action48():
                    oSatisfaction.invalid_data_indicator = 1.2

                TryCatchAssertBlock.DoAssert("", action48)

                def action49():
                    oSatisfaction.use_value_range_check = True

                # UseValueRangeCheck
                TryCatchAssertBlock.DoAssert("", action49)

                def action50():
                    oSatisfaction.min_value_range = 1.2

                # MinValueRange
                TryCatchAssertBlock.DoAssert("", action50)

                def action51():
                    oSatisfaction.max_value_range = 1.2

                # MaxValueRange
                TryCatchAssertBlock.DoAssert("", action51)

                def action52():
                    oSatisfaction.exclude_value_range = True

                # ExcludeValueRange
                TryCatchAssertBlock.DoAssert("", action52)

    # endregion

    # region DataMinMax
    def DataMinMax(self, dataMinMax: "IFigureOfMeritDefinitionDataMinMax"):
        Assert.assertIsNotNone(dataMinMax)
        # MinValue
        min: float = dataMinMax.min_value
        max: float = dataMinMax.max_value
        self.m_logger.WriteLine6("\t\t\tThe current MinValue is: {0}", min)
        if (min == 0) and (max == 0):
            dataMinMax.max_value = 200
            Assert.assertEqual(200, dataMinMax.max_value)

        dataMinMax.min_value = 123.456
        self.m_logger.WriteLine6("\t\t\tThe new MinValue is: {0}", dataMinMax.min_value)
        Assert.assertEqual(123.456, dataMinMax.min_value)
        # MaxValue
        self.m_logger.WriteLine6("\t\t\tThe current MaxValue is: {0}", dataMinMax.max_value)
        dataMinMax.max_value = 456.123
        self.m_logger.WriteLine6("\t\t\tThe new MaxValue is: {0}", dataMinMax.max_value)
        Assert.assertEqual(456.123, dataMinMax.max_value)

        def action53():
            dataMinMax.min_value = 1234.56

        TryCatchAssertBlock.DoAssert("", action53)

        def action54():
            dataMinMax.max_value = 45.6123

        TryCatchAssertBlock.DoAssert("", action54)

    # endregion

    # region DilutionOfPrecision
    def DilutionOfPrecision(self, oDOP: "IFigureOfMeritDefinitionDilutionOfPrecision"):
        Assert.assertIsNotNone(oDOP)
        # Method
        self.m_logger.WriteLine6("\t\t\tThe current Method is: {0}", oDOP.method)
        # SupportedMethods
        arMethods = oDOP.supported_methods
        self.m_logger.WriteLine3("\t\t\tThe DilutionOfPrecision supports: {0} methods", Array.Length(arMethods))

        iIndex: int = 0
        while iIndex < Array.Length(arMethods):
            eMethod: "FIGURE_OF_MERIT_METHOD" = clr.Convert(int(arMethods[iIndex]), FIGURE_OF_MERIT_METHOD)
            if not oDOP.is_method_supported(eMethod):
                Assert.fail("The {0} Method should be supported!", eMethod)

            # SetMethod
            oDOP.set_method(eMethod)
            self.m_logger.WriteLine6("\t\t\t\tThe new Method is: {0}", oDOP.method)
            Assert.assertEqual(eMethod, oDOP.method)

            iIndex += 1

        # Type
        self.m_logger.WriteLine6("\t\t\tThe current Type is: {0}", oDOP.type)
        # SupportedTypes
        arTypes = oDOP.supported_types
        self.m_logger.WriteLine3("\t\t\tThe DilutionOfPrecision supports: {0} types", Array.Length(arTypes))

        iIndex: int = 0
        while iIndex < Array.Length(arTypes):
            eType: "FIGURE_OF_MERIT_COMPUTE_TYPE" = clr.Convert(int(arTypes[iIndex]), FIGURE_OF_MERIT_COMPUTE_TYPE)
            if not oDOP.is_type_supported(eType):
                Assert.fail("The {0} Type should be supported!", eType)

            # SetType
            oDOP.set_type(eType)
            self.m_logger.WriteLine6("\t\t\t\tThe new Type is: {0}", oDOP.type)
            Assert.assertEqual(eType, oDOP.type)
            if ((eType == FIGURE_OF_MERIT_COMPUTE_TYPE.BEST_FOUR_ACC)) or (
                (eType == FIGURE_OF_MERIT_COMPUTE_TYPE.OVER_DETERMINED)
            ):

                def action55():
                    definitionData: "IFigureOfMeritDefinitionData" = oDOP.type_data

                TryCatchAssertBlock.DoAssert("", action55)
            elif eType == FIGURE_OF_MERIT_COMPUTE_TYPE.BEST4:
                definitionData: "IFigureOfMeritDefinitionData" = clr.CastAs(
                    oDOP.type_data, IFigureOfMeritDefinitionData
                )
                oBest4: "IFigureOfMeritDefinitionDataBest4" = clr.CastAs(
                    definitionData, IFigureOfMeritDefinitionDataBest4
                )
                Assert.assertIsNotNone(oBest4)
                # BestN
                self.m_logger.WriteLine6("\t\t\t\t\tThe current Best4 metric is: {0}", oBest4.best4_metric)
                oBest4.best4_metric = FIGURE_OF_MERIT_METHOD.NDOP
                self.m_logger.WriteLine6("\t\t\t\t\tThe new Best4 metric is: {0}", oBest4.best4_metric)
                supportedTypes = oBest4.best4_metric_supported_types
                omethod: typing.Any
                for omethod in supportedTypes:
                    method: "FIGURE_OF_MERIT_METHOD" = clr.Convert(int(omethod), FIGURE_OF_MERIT_METHOD)
                    Assert.assertTrue(oBest4.is_best4_metric_supported(method))
                    oBest4.best4_metric = method
                    Assert.assertEqual(method, oBest4.best4_metric)

                Assert.assertFalse(oBest4.is_best4_metric_supported(FIGURE_OF_MERIT_METHOD.HDOP3))

                def action56():
                    oBest4.best4_metric = FIGURE_OF_MERIT_METHOD.HDOP3

                TryCatchAssertBlock.DoAssert("Best 4 metric is not supported", action56)
            elif ((eType == FIGURE_OF_MERIT_COMPUTE_TYPE.BEST_N)) or (
                (eType == FIGURE_OF_MERIT_COMPUTE_TYPE.BEST_N_ACC)
            ):
                oBestN: "IFigureOfMeritDefinitionDataBestN" = clr.CastAs(
                    oDOP.type_data, IFigureOfMeritDefinitionDataBestN
                )
                Assert.assertIsNotNone(oBestN)
                # BestN
                self.m_logger.WriteLine3("\t\t\t\t\tThe current BestN is: {0}", oBestN.best_n)
                oBestN.best_n = 12
                self.m_logger.WriteLine3("\t\t\t\t\tThe new BestN is: {0}", oBestN.best_n)
                Assert.assertEqual(12, oBestN.best_n)

                def action57():
                    oBestN.best_n = 123

                TryCatchAssertBlock.DoAssert("", action57)
                supportedTypes = oBestN.best_n_metric_supported_types
                omethod: typing.Any
                for omethod in supportedTypes:
                    method: "FIGURE_OF_MERIT_METHOD" = clr.Convert(int(omethod), FIGURE_OF_MERIT_METHOD)
                    Assert.assertTrue(oBestN.is_best_n_metric_supported(method))
                    oBestN.best_n_metric = method
                    Assert.assertEqual(method, oBestN.best_n_metric)

                Assert.assertFalse(oBestN.is_best_n_metric_supported(FIGURE_OF_MERIT_METHOD.HDOP3))

                def action58():
                    oBestN.best_n_metric = FIGURE_OF_MERIT_METHOD.HDOP3

                TryCatchAssertBlock.DoAssert("Best N metric is not supported", action58)
            else:
                Assert.fail("Invalid Type - {0}!", eType)

            iIndex += 1

        # Invalid Value Action
        oDOP.invalid_value_action = FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE.INVALID_VALUE_ACTION_IGNORE
        Assert.assertEqual(
            FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE.INVALID_VALUE_ACTION_IGNORE, oDOP.invalid_value_action
        )
        oDOP.invalid_value_action = FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE.INVALID_VALUE_ACTION_INCLUDE
        Assert.assertEqual(
            FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE.INVALID_VALUE_ACTION_INCLUDE, oDOP.invalid_value_action
        )

        # TimeStep
        self.m_logger.WriteLine6("\t\t\tThe current TimeStep is: {0}", oDOP.time_step)
        oDOP.time_step = 12.34
        self.m_logger.WriteLine6("\t\t\tThe new TimeStep is: {0}", oDOP.time_step)
        Assert.assertEqual(12.34, oDOP.time_step)

        def action59():
            oDOP.time_step = 12345.67

        TryCatchAssertBlock.DoAssert("", action59)

    # endregion

    # region GfxAttributes
    def GfxAttributes(self, oAttributes: "IFigureOfMeritGraphics2DAttributes", bReadOnly: bool):
        self.m_logger.WriteLine4("----- GRAPHICS ATTRIBUTES TEST (ReadOnly = {0}) ----- BEGIN -----", bReadOnly)
        Assert.assertIsNotNone(oAttributes)
        if bReadOnly:

            def action60():
                oAttributes.is_visible = True

            # IsVisible
            TryCatchAssertBlock.DoAssert("", action60)

            def action61():
                oAttributes.fill_points = True

            # FillPoints
            TryCatchAssertBlock.DoAssert("", action61)

            def action62():
                oAttributes.marker_style = "X"

            # MarkerStyle
            TryCatchAssertBlock.DoAssert("", action62)

            def action63():
                oAttributes.color = Color.FromArgb(1122867)

            # Color
            TryCatchAssertBlock.DoAssert("", action63)

        else:
            # IsVisible (false)
            self.m_logger.WriteLine4("\tThe current IsVisible is: {0}", oAttributes.is_visible)
            oAttributes.is_visible = False
            self.m_logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.is_visible)
            Assert.assertFalse(oAttributes.is_visible)

            def action64():
                oAttributes.fill_points = True

            # FillPoints (readonly)
            TryCatchAssertBlock.DoAssert("", action64)

            def action65():
                oAttributes.marker_style = "X"

            # MarkerStyle (readonly)
            TryCatchAssertBlock.DoAssert("", action65)

            def action66():
                oAttributes.color = Color.FromArgb(1122867)

            # Color (readonly)
            TryCatchAssertBlock.DoAssert("", action66)
            # IsVisible (true)
            oAttributes.is_visible = True
            self.m_logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.is_visible)
            Assert.assertTrue(oAttributes.is_visible)
            # FillPoints
            self.m_logger.WriteLine4("\tThe current FillPoints is: {0}", oAttributes.fill_points)
            oAttributes.fill_points = True
            self.m_logger.WriteLine4("\tThe new FillPoints is: {0}", oAttributes.fill_points)
            Assert.assertTrue(oAttributes.fill_points)

            oAttributes.fill_translucency = 55.0
            Assert.assertAlmostEqual(55.0, oAttributes.fill_translucency, delta=Math2.Epsilon12)

            def action67():
                oAttributes.marker_style = "X"

            TryCatchAssertBlock.DoAssert("", action67)
            oAttributes.fill_points = False
            self.m_logger.WriteLine4("\tThe new FillPoints is: {0}", oAttributes.fill_points)
            Assert.assertFalse(oAttributes.fill_points)

            # MarkerStyle
            self.m_logger.WriteLine5("\tThe current MarkerStyle is: {0}", oAttributes.marker_style)
            oAttributes.marker_style = "Square"
            self.m_logger.WriteLine5("\tThe new MarkerStyle is: {0}", oAttributes.marker_style)
            Assert.assertEqual("Square", oAttributes.marker_style)
            # Color
            self.m_logger.WriteLine6("\tThe current Color is: 0x{0:X}", oAttributes.color)
            oAttributes.color = Color.FromArgb(1122867)
            self.m_logger.WriteLine6("\tThe new Color is: 0x{0:X}", oAttributes.color)
            AssertEx.AreEqual(Color.FromArgb(1122867), oAttributes.color)

        self.m_logger.WriteLine("----- GRAPHICS ATTRIBUTES TEST ----- END -----")

    # endregion

    # region GfxAnimationAttributes
    def GfxAnimationAttributes(self, oAttributes: "IFigureOfMeritGraphics2DAttributesAnimation", bReadOnly: bool):
        self.m_logger.WriteLine4(
            "----- GRAPHICS ATTRIBUTES ANIMATION TEST (ReadOnly = {0}) ----- BEGIN -----", bReadOnly
        )
        Assert.assertIsNotNone(oAttributes)
        if bReadOnly:
            # base class properties test
            self.GfxAttributes(clr.CastAs(oAttributes, IFigureOfMeritGraphics2DAttributes), bReadOnly)

            def action68():
                oAttributes.accumulation = FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.NOT_CURRENT

            # Accumulation (readonly)
            TryCatchAssertBlock.DoAssert("", action68)

        else:
            klass: "IFigureOfMeritGraphics2DAttributesAnimation" = clr.CastAs(
                oAttributes, IFigureOfMeritGraphics2DAttributesAnimation
            )
            dispatch: "FigureOfMeritGraphics2DAttributesAnimation" = clr.CastAs(
                oAttributes, FigureOfMeritGraphics2DAttributesAnimation
            )
            # Verify that the color is accessible through the managed class
            cr = klass.color
            AssertEx.AreEqual(cr, klass.color)
            AssertEx.AreEqual(cr, dispatch.color)
            # base class properties test
            self.GfxAttributes(clr.CastAs(oAttributes, IFigureOfMeritGraphics2DAttributes), bReadOnly)
            # Accumulation
            self.m_logger.WriteLine6("\tThe current Accumulation is: {0}", oAttributes.accumulation)
            oAttributes.accumulation = FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.CURRENT_TIME
            self.m_logger.WriteLine6("\tThe new Accumulation is: {0}", oAttributes.accumulation)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.CURRENT_TIME, oAttributes.accumulation)
            oAttributes.accumulation = FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.NOT_CURRENT
            self.m_logger.WriteLine6("\tThe new Accumulation is: {0}", oAttributes.accumulation)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.NOT_CURRENT, oAttributes.accumulation)
            oAttributes.accumulation = FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.NOT_UP_TO_CURRENT
            self.m_logger.WriteLine6("\tThe new Accumulation is: {0}", oAttributes.accumulation)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.NOT_UP_TO_CURRENT, oAttributes.accumulation)
            oAttributes.accumulation = FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.UP_TO_CURRENT
            self.m_logger.WriteLine6("\tThe new Accumulation is: {0}", oAttributes.accumulation)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.UP_TO_CURRENT, oAttributes.accumulation)

            oAttributes.fill_points = True
            oAttributes.fill_translucency = 55.0
            Assert.assertAlmostEqual(55.0, oAttributes.fill_translucency, delta=Math2.Epsilon12)

        self.m_logger.WriteLine("----- GRAPHICS ATTRIBUTES ANIMATION TEST ----- END -----")

    # endregion

    # region GfxContours
    def GfxContours(self, oContours: "IFigureOfMeritGraphics2DContours", bReadOnly: bool, bIsVisibleReadOnly: bool):
        self.m_logger.WriteLine4("----- GRAPHICS CONTOURS TEST (ReadOnly = {0})----- BEGIN -----", bReadOnly)
        Assert.assertIsNotNone(oContours)
        if bReadOnly:
            if bIsVisibleReadOnly:

                def action69():
                    oContours.is_visible = True

                TryCatchAssertBlock.DoAssert("", action69)

            def action70():
                oContours.contour_type = FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.BLOCK_FILL

            # ContourType (readonly)
            TryCatchAssertBlock.DoAssert("", action70)

            def action71():
                oContours.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT

            # ColorMethod (readonly)
            TryCatchAssertBlock.DoAssert("", action71)
            # RampColor (readonly)
            self.GfxRampColor(oContours.ramp_color, bReadOnly)
            # LevelAttributes (readonly)
            self.GfxLevelAttributes(oContours.level_attributes, oContours.color_method, bReadOnly)
            # Legend (readonly)
            self.GfxLegend(oContours.legend, bReadOnly, bIsVisibleReadOnly)

        else:
            # IsVisible (false)
            self.m_logger.WriteLine4("\tThe current IsVisible is: {0}", oContours.is_visible)
            oContours.is_visible = False
            self.m_logger.WriteLine4("\tThe new IsVisible is: {0}", oContours.is_visible)
            Assert.assertFalse(oContours.is_visible)

            def action72():
                oContours.contour_type = FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.BLOCK_FILL

            # ContourType (readonly)
            TryCatchAssertBlock.DoAssert("", action72)

            def action73():
                oContours.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT

            # ColorMethod (readonly)
            TryCatchAssertBlock.DoAssert("", action73)
            # IsVisible (true)
            oContours.is_visible = True
            self.m_logger.WriteLine4("\tThe new IsVisible is: {0}", oContours.is_visible)
            Assert.assertTrue(oContours.is_visible)
            # ContourType
            self.m_logger.WriteLine6("\tThe current ContourType is: {0}", oContours.contour_type)
            oContours.contour_type = FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.BLOCK_FILL
            self.m_logger.WriteLine6("\tThe new ContourType is: {0}", oContours.contour_type)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.BLOCK_FILL, oContours.contour_type)
            oContours.contour_type = FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.SMOOTH_FILL
            self.m_logger.WriteLine6("\tThe new ContourType is: {0}", oContours.contour_type)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.SMOOTH_FILL, oContours.contour_type)
            # ColorMethod
            self.m_logger.WriteLine6("\tThe current ColorMethod is: {0}", oContours.color_method)
            oContours.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
            self.m_logger.WriteLine6("\tThe new ColorMethod is: {0}", oContours.color_method)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT, oContours.color_method)
            # LevelAttributes
            self.GfxLevelAttributes(oContours.level_attributes, oContours.color_method, bReadOnly)
            oContours.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP
            self.m_logger.WriteLine6("\tThe new ColorMethod is: {0}", oContours.color_method)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.COLOR_RAMP, oContours.color_method)
            # RampColor
            self.GfxRampColor(oContours.ramp_color, bReadOnly)
            # LevelAttributes
            self.GfxLevelAttributes(oContours.level_attributes, oContours.color_method, bReadOnly)
            # Legend
            self.GfxLegend(oContours.legend, bReadOnly, bIsVisibleReadOnly)

            # Show up to max only option
            oContours.show_up_to_max_only = True
            Assert.assertTrue(oContours.show_up_to_max_only)
            oContours.show_up_to_max_only = False
            Assert.assertFalse(oContours.show_up_to_max_only)

        self.m_logger.WriteLine("----- GRAPHICS CONTOURS TEST ----- END -----")

    # endregion

    # region GfxContours
    def GfxContourLines(self, oContours: "IFigureOfMeritGraphics2DContours", bReadOnly: bool):
        self.m_logger.WriteLine4("----- GRAPHICS CONTOUR LiNES TEST (ReadOnly = {0})----- BEGIN -----", bReadOnly)
        Assert.assertIsNotNone(oContours)
        if bReadOnly:

            def action74():
                oContours.show_contour_lines = True

            # ShowContourLines (readonly)
            TryCatchAssertBlock.DoAssert("", action74)

            def action75():
                oContours.line_width = 3

            # LineWidth (readonly)
            TryCatchAssertBlock.DoAssert("", action75)

        else:
            # Show contour lines
            oContours.show_contour_lines = True
            Assert.assertTrue(oContours.show_contour_lines)
            oContours.show_contour_lines = False
            Assert.assertFalse(oContours.show_contour_lines)

            # Show contour lines
            oContours.show_contour_lines = True
            oContours.line_width = 5
            Assert.assertEqual(5, oContours.line_width)
            oContours.line_width = 1
            Assert.assertEqual(1, oContours.line_width)

        self.m_logger.WriteLine("----- GRAPHICS CONTOUR LINES TEST ----- END -----")

    # endregion

    # region GfxAnimationContours
    def GfxAnimationContours(
        self, oBaseContours: "IFigureOfMeritGraphics2DContours", bReadOnly: bool, bIsVisibleReadOnly: bool
    ):
        self.m_logger.WriteLine4("----- GRAPHICS CONTOURS ANIMATION TEST (ReadOnly = {0})----- BEGIN -----", bReadOnly)
        Assert.assertIsNotNone(oBaseContours)
        oContours: "IFigureOfMeritGraphics2DContoursAnimation" = clr.CastAs(
            oBaseContours, IFigureOfMeritGraphics2DContoursAnimation
        )
        Assert.assertIsNotNone(oContours)
        if bReadOnly:
            # base class properties test
            self.GfxContours(oContours, bReadOnly, bIsVisibleReadOnly)

            def action76():
                oContours.use_static_contours = True

            # UseStaticContours (readonly)
            TryCatchAssertBlock.DoAssert("", action76)

        else:
            # UseStaticContours (false)
            self.m_logger.WriteLine4("\tThe current UseStaticContours is: {0}", oContours.use_static_contours)
            oContours.use_static_contours = False
            self.m_logger.WriteLine4("\tThe new UseStaticContours is: {0}", oContours.use_static_contours)
            Assert.assertFalse(oContours.use_static_contours)
            # base class properties test
            self.GfxContours(oContours, False, bIsVisibleReadOnly)
            # UseStaticContours (true)
            oContours.use_static_contours = True
            self.m_logger.WriteLine4("\tThe new UseStaticContours is: {0}", oContours.use_static_contours)
            Assert.assertTrue(oContours.use_static_contours)
            # base class properties test
            self.GfxContours(oContours, True, bIsVisibleReadOnly)

        self.m_logger.WriteLine("----- GRAPHICS CONTOURS ANIMATION TEST ----- END -----")

    # endregion

    # region GfxRampColor
    def GfxRampColor(self, oColor: "IFigureOfMeritGraphics2DRampColor", bReadOnly: bool):
        self.m_logger.WriteLine("----- GRAPHICS RAMP COLOR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oColor)
        if bReadOnly:

            def action77():
                oColor.start_color = Color.FromArgb(10061943)

            # StartColor
            TryCatchAssertBlock.DoAssert("", action77)

            def action78():
                oColor.end_color = Color.FromArgb(13426158)

            # EndColor
            TryCatchAssertBlock.DoAssert("", action78)

        else:
            # StartColor
            self.m_logger.WriteLine6("\tThe current StartColor is: 0x{0:X}", oColor.start_color)
            oColor.start_color = Color.FromArgb(10061943)
            self.m_logger.WriteLine6("\tThe new StartColor is: 0x{0:X}", oColor.start_color)
            AssertEx.AreEqual(Color.FromArgb(10061943), oColor.start_color)
            # EndColor
            self.m_logger.WriteLine6("\tThe current EndColor is: 0x{0:X}", oColor.end_color)
            oColor.end_color = Color.FromArgb(13426158)
            self.m_logger.WriteLine6("\tThe new EndColor is: 0x{0:X}", oColor.end_color)
            AssertEx.AreEqual(Color.FromArgb(13426158), oColor.end_color)

        self.m_logger.WriteLine("----- GRAPHICS RAMP COLOR TEST ----- END -----")

    # endregion

    # region GfxLevelAttributes
    def GfxLevelAttributes(
        self,
        oCollection: "IFigureOfMeritGraphics2DLevelAttributesCollection",
        eMethod: "FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD",
        bReadOnly: bool,
    ):
        self.m_logger.WriteLine("----- GRAPHICS LEVEL ATTRIBUTES TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        if bReadOnly:

            def action79():
                oCollection.add_level(123)

            # AddLevel
            TryCatchAssertBlock.DoAssert("", action79)

            def action80():
                oCollection.add_level_range(1, 25, 5)

            # AddLevelRange
            TryCatchAssertBlock.DoAssert("", action80)
            if oCollection.count > 0:

                def action81():
                    oCollection.remove_at(0)

                TryCatchAssertBlock.DoAssert("", action81)

            def action82():
                oCollection.remove_all()

            # RemoveAll
            TryCatchAssertBlock.DoAssert("", action82)

        else:
            # Count
            self.m_logger.WriteLine3(
                "\tThe current LevelAttributes collection contains: {0} elements.", oCollection.count
            )
            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3("\tThe new LevelAttributes collection contains: {0} elements.", oCollection.count)
            Assert.assertEqual(0, oCollection.count)
            # AddLevelRange
            oCollection.add_level_range(20, 40, 5)
            Assert.assertEqual(5, oCollection.count)

            def action83():
                oCollection.add_level_range(50, 10, 5)

            TryCatchAssertBlock.DoAssert("", action83)

            def action84():
                oCollection.add_level_range(10, 20, -5)

            TryCatchAssertBlock.DoAssert("", action84)
            self.m_logger.WriteLine3("\tThe new LevelAttributes collection contains: {0} elements.", oCollection.count)
            oElem: "IFigureOfMeritGraphics2DLevelAttributesElement"
            for oElem in oCollection:
                # _NewEnum
                self.m_logger.WriteLine7("\t\tElement: Level = {0}, Color = 0x{1:X}", oElem.level, oElem.color)

            # AddLevel
            gfxLevelAttributesElement: "IFigureOfMeritGraphics2DLevelAttributesElement" = oCollection.add_level(37)
            Assert.assertIsNotNone(gfxLevelAttributesElement)
            Assert.assertEqual(6, oCollection.count)
            self.m_logger.WriteLine3("\tThe new LevelAttributes collection contains: {0} elements.", oCollection.count)
            oElem: "IFigureOfMeritGraphics2DLevelAttributesElement"
            for oElem in oCollection:
                self.m_logger.WriteLine7("\t\tElement: Level = {0}, Color = 0x{1:X}", oElem.level, oElem.color)

            # Level
            self.m_logger.WriteLine6("\tThe current Level is: {0}", gfxLevelAttributesElement.level)
            gfxLevelAttributesElement.level = 47
            self.m_logger.WriteLine6("\tThe new Level is: {0}", gfxLevelAttributesElement.level)
            Assert.assertEqual(47, gfxLevelAttributesElement.level)
            # Color
            self.m_logger.WriteLine6("\tThe current Color is: 0x{0:X}", gfxLevelAttributesElement.color)
            if eMethod == FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT:
                gfxLevelAttributesElement.color = Color.FromArgb(13426158)
                self.m_logger.WriteLine6("\tThe new Color is: 0x{0:X}", gfxLevelAttributesElement.color)
                AssertEx.AreEqual(Color.FromArgb(13426158), gfxLevelAttributesElement.color)

            else:

                def action85():
                    gfxLevelAttributesElement.color = Color.FromArgb(13426158)

                TryCatchAssertBlock.DoAssert("", action85)

            self.m_logger.WriteLine3("\tThe new LevelAttributes collection contains: {0} elements.", oCollection.count)

            iIndex: int = 0
            while iIndex < oCollection.count:
                # Item
                self.m_logger.WriteLine8(
                    "\t\tElement {2}: Level = {0}, Color = 0x{1:X}",
                    oCollection[iIndex].level,
                    oCollection[iIndex].color,
                    iIndex,
                )

                iIndex += 1

            # RemoveAt
            oCollection.remove_at(0)
            Assert.assertEqual(5, oCollection.count)
            self.m_logger.WriteLine3("\tThe new LevelAttributes collection contains: {0} elements.", oCollection.count)

            iIndex: int = 0
            while iIndex < oCollection.count:
                # Item
                self.m_logger.WriteLine8(
                    "\t\tElement {2}: Level = {0}, Color = 0x{1:X}",
                    oCollection[iIndex].level,
                    oCollection[iIndex].color,
                    iIndex,
                )

                iIndex += 1

            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3("\tThe new LevelAttributes collection contains: {0} elements.", oCollection.count)
            Assert.assertEqual(0, oCollection.count)

        self.m_logger.WriteLine("----- GRAPHICS LEVEL ATTRIBUTES TEST ----- END -----")

    # endregion

    # region GfxLegend
    def GfxLegend(self, oLegend: "IFigureOfMeritGraphics2DLegend", bReadOnly: bool, bIsVisibleReadOnly: bool):
        self.m_logger.WriteLine4("----- GRAPHICS LEGEND TEST (ReadOnly = {0})----- BEGIN -----", bReadOnly)
        Assert.assertIsNotNone(oLegend)
        if bReadOnly:
            # ColorOptions
            self.GfxLegendColorOptions(oLegend.color_options, bReadOnly, bIsVisibleReadOnly)
            # TextOptions
            self.GfxLegendTextOptions(oLegend.text_options, bReadOnly, bIsVisibleReadOnly)
            # RangeColorOptions
            self.GfxLegendRangeColorOptions(oLegend.range_color_options, bReadOnly, bIsVisibleReadOnly)
            # GfxWindow
            self.GfxLegend2DWindowLayout(oLegend.graphics_2d_window, bReadOnly, bIsVisibleReadOnly)
            # VOWindow
            self.GfxLegend3DWindowLayout(oLegend.graphics_3d_window, bReadOnly, bIsVisibleReadOnly)

        else:
            # ColorOptions
            self.GfxLegendColorOptions(oLegend.color_options, bReadOnly, bIsVisibleReadOnly)
            # TextOptions
            self.GfxLegendTextOptions(oLegend.text_options, bReadOnly, bIsVisibleReadOnly)
            # RangeColorOptions
            self.GfxLegendRangeColorOptions(oLegend.range_color_options, bReadOnly, bIsVisibleReadOnly)
            # GfxWindow
            self.GfxLegend2DWindowLayout(oLegend.graphics_2d_window, bReadOnly, bIsVisibleReadOnly)
            # VOWindow
            self.GfxLegend3DWindowLayout(oLegend.graphics_3d_window, bReadOnly, bIsVisibleReadOnly)

        self.m_logger.WriteLine("----- GRAPHICS LEGENT TEST ----- END -----")

    # endregion

    # region GfxLegendColorOptions
    def GfxLegendColorOptions(
        self, oOptions: "IFigureOfMeritGraphics2DColorOptions", bReadOnly: bool, bIsVisibleReadOnly: bool
    ):
        Assert.assertIsNotNone(oOptions)
        if bReadOnly and bIsVisibleReadOnly:

            def action86():
                oOptions.background = 3430008

            # Background
            TryCatchAssertBlock.DoAssert("", action86)

            def action87():
                oOptions.text = 5666960

            # Text
            TryCatchAssertBlock.DoAssert("", action87)

        else:
            # BackgroundColor
            self.m_logger.WriteLine6("\tThe current Background is: {0}", oOptions.background_color)
            oOptions.background_color = Color.Blue
            self.m_logger.WriteLine6("\tThe new Background is: {0}", oOptions.background_color)
            Assert.assertEqual(Color.Blue, oOptions.background_color)
            # TextColor
            self.m_logger.WriteLine6("\tThe current Text is: {0}", oOptions.text_color)
            oOptions.text_color = Color.Green
            self.m_logger.WriteLine6("\tThe new Text is: {0}", oOptions.text_color)
            Assert.assertEqual(Color.Green, oOptions.text_color)

    @staticmethod
    def GetColor(color: int):
        return color

    # endregion

    # region GfxLegendTextOptions
    def GfxLegendTextOptions(
        self, oOptions: "IFigureOfMeritGraphics2DTextOptions", bReadOnly: bool, bIsVisibleReadOnly: bool
    ):
        Assert.assertIsNotNone(oOptions)
        if bReadOnly and bIsVisibleReadOnly:

            def action88():
                oOptions.title = "Text Options ReadOnly Title"

            # Title
            TryCatchAssertBlock.DoAssert("", action88)

            def action89():
                oOptions.num_decimal_digits = 12

            # NumDecimalDigits
            TryCatchAssertBlock.DoAssert("", action89)

            def action90():
                oOptions.floating_point_format = FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT.FLOATING_POINT

            # FloatingPointFormat
            TryCatchAssertBlock.DoAssert("", action90)

        else:
            # Title
            self.m_logger.WriteLine5("\tThe current Title is: {0}", oOptions.title)
            oOptions.title = ""
            self.m_logger.WriteLine5("\tThe new Title is: {0}", oOptions.title)
            Assert.assertEqual("", oOptions.title)
            oOptions.title = "A new Legend title"
            self.m_logger.WriteLine5("\tThe new Title is: {0}", oOptions.title)
            Assert.assertEqual("A new Legend title", oOptions.title)
            # NumDecimalDigits
            self.m_logger.WriteLine3("\tThe current NumDecimalDigits is: {0}", oOptions.num_decimal_digits)
            oOptions.num_decimal_digits = 12
            self.m_logger.WriteLine3("\tThe new NumDecimalDigits is: {0}", oOptions.num_decimal_digits)
            Assert.assertEqual(12, oOptions.num_decimal_digits)

            def action91():
                oOptions.num_decimal_digits = 123

            TryCatchAssertBlock.DoAssert("", action91)
            # FloatingPointFormat
            self.m_logger.WriteLine6("\tThe current FloatingPointFormat is: {0}", oOptions.floating_point_format)
            oOptions.floating_point_format = FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT.FLOATING_POINT
            self.m_logger.WriteLine6("\tThe new FloatingPointFormat is: {0}", oOptions.floating_point_format)
            Assert.assertEqual(
                FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT.FLOATING_POINT, oOptions.floating_point_format
            )
            oOptions.floating_point_format = FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT.SCIENTIFIC_LOWERCASE_E
            self.m_logger.WriteLine6("\tThe new FloatingPointFormat is: {0}", oOptions.floating_point_format)
            Assert.assertEqual(
                FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT.SCIENTIFIC_LOWERCASE_E, oOptions.floating_point_format
            )
            oOptions.floating_point_format = FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT.SCIENTIFIC_UPPERCASE_E
            self.m_logger.WriteLine6("\tThe new FloatingPointFormat is: {0}", oOptions.floating_point_format)
            Assert.assertEqual(
                FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT.SCIENTIFIC_UPPERCASE_E, oOptions.floating_point_format
            )

    # endregion

    # region GfxLegendRangeColorOptions
    def GfxLegendRangeColorOptions(
        self, oOptions: "IFigureOfMeritGraphics2DRangeColorOptions", bReadOnly: bool, bIsVisibleReadOnly: bool
    ):
        Assert.assertIsNotNone(oOptions)
        if bReadOnly and bIsVisibleReadOnly:

            def action92():
                oOptions.color_square_height = 12

            # ColorSquareHeight
            TryCatchAssertBlock.DoAssert("", action92)

            def action93():
                oOptions.color_square_width = 34

            # ColorSquareWidth
            TryCatchAssertBlock.DoAssert("", action93)

            def action94():
                oOptions.direction = FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.HORIZONTAL_MAX_TO_MIN

            # Direction
            TryCatchAssertBlock.DoAssert("", action94)

            def action95():
                oOptions.max_squares_per_row = 12

            # MaxSquaresPerRow
            TryCatchAssertBlock.DoAssert("", action95)

            def action96():
                oOptions.max_squares_per_column = 34

            # MaxSquaresPerColumn
            TryCatchAssertBlock.DoAssert("", action96)

        else:
            # ColorSquareHeight
            self.m_logger.WriteLine3("\tThe current ColorSquareHeight is: {0}", oOptions.color_square_height)
            oOptions.color_square_height = 12
            self.m_logger.WriteLine3("\tThe new ColorSquareHeight is: {0}", oOptions.color_square_height)
            Assert.assertEqual(12, oOptions.color_square_height)

            def action97():
                oOptions.color_square_height = 123

            TryCatchAssertBlock.DoAssert("", action97)
            # ColorSquareWidth
            self.m_logger.WriteLine3("\tThe current ColorSquareWidth is: {0}", oOptions.color_square_width)
            oOptions.color_square_width = 34
            self.m_logger.WriteLine3("\tThe new ColorSquareWidth is: {0}", oOptions.color_square_width)
            Assert.assertEqual(34, oOptions.color_square_width)

            def action98():
                oOptions.color_square_width = 123

            TryCatchAssertBlock.DoAssert("", action98)
            # Direction (eHorizontalMaxToMin)
            self.m_logger.WriteLine6("\tThe current Direction is: {0}", oOptions.direction)
            oOptions.direction = FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.HORIZONTAL_MAX_TO_MIN
            self.m_logger.WriteLine6("\tThe new Direction is: {0}", oOptions.direction)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.HORIZONTAL_MAX_TO_MIN, oOptions.direction)
            # MaxSquaresPerRow
            self.m_logger.WriteLine3("\tThe current MaxSquaresPerRow is: {0}", oOptions.max_squares_per_row)
            oOptions.max_squares_per_row = 34
            self.m_logger.WriteLine3("\tThe new MaxSquaresPerRow is: {0}", oOptions.max_squares_per_row)
            Assert.assertEqual(34, oOptions.max_squares_per_row)

            def action99():
                oOptions.max_squares_per_row = 123456

            TryCatchAssertBlock.DoAssert("", action99)

            def action100():
                oOptions.max_squares_per_column = 34

            # MaxSquaresPerColumn
            TryCatchAssertBlock.DoAssert("", action100)
            # Direction (eHorizontalMinToMax)
            oOptions.direction = FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.HORIZONTAL_MIN_TO_MAX
            self.m_logger.WriteLine6("\tThe new Direction is: {0}", oOptions.direction)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.HORIZONTAL_MIN_TO_MAX, oOptions.direction)
            # MaxSquaresPerRow
            self.m_logger.WriteLine3("\tThe current MaxSquaresPerRow is: {0}", oOptions.max_squares_per_row)
            oOptions.max_squares_per_row = 56
            self.m_logger.WriteLine3("\tThe new MaxSquaresPerRow is: {0}", oOptions.max_squares_per_row)
            Assert.assertEqual(56, oOptions.max_squares_per_row)

            def action101():
                oOptions.max_squares_per_row = 12345

            TryCatchAssertBlock.DoAssert("", action101)

            def action102():
                oOptions.max_squares_per_column = 12

            # MaxSquaresPerColumn
            TryCatchAssertBlock.DoAssert("", action102)
            # Direction (eVerticalMaxToMin)
            oOptions.direction = FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.VERTICAL_MAX_TO_MIN
            self.m_logger.WriteLine6("\tThe new Direction is: {0}", oOptions.direction)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.VERTICAL_MAX_TO_MIN, oOptions.direction)
            # MaxSquaresPerColumn
            self.m_logger.WriteLine3("\tThe current MaxSquaresPerColumn is: {0}", oOptions.max_squares_per_column)
            oOptions.max_squares_per_column = 56
            self.m_logger.WriteLine3("\tThe new MaxSquaresPerColumn is: {0}", oOptions.max_squares_per_column)
            Assert.assertEqual(56, oOptions.max_squares_per_column)

            def action103():
                oOptions.max_squares_per_column = 12345

            TryCatchAssertBlock.DoAssert("", action103)

            def action104():
                oOptions.max_squares_per_row = 12

            # MaxSquaresPerRow
            TryCatchAssertBlock.DoAssert("", action104)
            # Direction (eVerticalMinToMax)
            oOptions.direction = FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.VERTICAL_MIN_TO_MAX
            self.m_logger.WriteLine6("\tThe new Direction is: {0}", oOptions.direction)
            Assert.assertEqual(FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION.VERTICAL_MIN_TO_MAX, oOptions.direction)
            # MaxSquaresPerColumn
            self.m_logger.WriteLine3("\tThe current MaxSquaresPerColumn is: {0}", oOptions.max_squares_per_column)
            oOptions.max_squares_per_column = 32
            self.m_logger.WriteLine3("\tThe new MaxSquaresPerColumn is: {0}", oOptions.max_squares_per_column)
            Assert.assertEqual(32, oOptions.max_squares_per_column)

            def action105():
                oOptions.max_squares_per_column = 12345

            TryCatchAssertBlock.DoAssert("", action105)

            def action106():
                oOptions.max_squares_per_row = 34

            # MaxSquaresPerRow
            TryCatchAssertBlock.DoAssert("", action106)

    # endregion

    # region GfxLegend2DWindowLayout
    def GfxLegend2DWindowLayout(
        self, oWindow: "IFigureOfMeritGraphics2DLegendWindow", bReadOnly: bool, bIsVisibleReadOnly: bool
    ):
        Assert.assertIsNotNone(oWindow)
        if bReadOnly and bIsVisibleReadOnly:

            def action107():
                oWindow.is_visible_on_map = True

            # IsVisibleOnMap (readonly)
            TryCatchAssertBlock.DoAssert("", action107)
            # PositionOnMap (readonly)
            self.GfxLegendPositionOnMap(oWindow.position_on_map, bReadOnly)

        else:
            # IsVisibleOnMap (false)
            self.m_logger.WriteLine4("\tThe current IsVisibleOnMap is: {0}", oWindow.is_visible_on_map)
            oWindow.is_visible_on_map = False
            self.m_logger.WriteLine4("\tThe new IsVisibleOnMap is: {0}", oWindow.is_visible_on_map)
            Assert.assertFalse(oWindow.is_visible_on_map)
            # PositionOnMap (readonly)
            self.GfxLegendPositionOnMap(oWindow.position_on_map, True)
            # IsVisibleOnMap (true)
            oWindow.is_visible_on_map = True
            self.m_logger.WriteLine4("\tThe new IsVisibleOnMap is: {0}", oWindow.is_visible_on_map)
            Assert.assertTrue(oWindow.is_visible_on_map)
            # PositionOnMap
            self.GfxLegendPositionOnMap(oWindow.position_on_map, False)

    # endregion

    # region GfxLegend3DWindowLayout
    def GfxLegend3DWindowLayout(
        self, oWindow: "IFigureOfMeritGraphics3DLegendWindow", bReadOnly: bool, bIsVisibleReadOnly: bool
    ):
        Assert.assertIsNotNone(oWindow)
        if bReadOnly and bIsVisibleReadOnly:

            def action108():
                oWindow.is_visible_on_map = True

            # IsVisibleOnMap (readonly)
            TryCatchAssertBlock.DoAssert("", action108)

            def action109():
                oWindow.translucency = 67.89

            # Translucency (readonly)
            TryCatchAssertBlock.DoAssert("", action109)
            # PositionOnMap (readonly)
            self.GfxLegendPositionOnMap(oWindow.position_on_map, bReadOnly)

        else:
            # IsVisibleOnMap (false)
            self.m_logger.WriteLine4("\tThe current IsVisibleOnMap is: {0}", oWindow.is_visible_on_map)
            oWindow.is_visible_on_map = False
            self.m_logger.WriteLine4("\tThe new IsVisibleOnMap is: {0}", oWindow.is_visible_on_map)
            Assert.assertFalse(oWindow.is_visible_on_map)
            # PositionOnMap (readonly)
            self.GfxLegendPositionOnMap(oWindow.position_on_map, True)
            # IsVisibleOnMap (true)
            oWindow.is_visible_on_map = True
            self.m_logger.WriteLine4("\tThe new IsVisibleOnMap is: {0}", oWindow.is_visible_on_map)
            Assert.assertTrue(oWindow.is_visible_on_map)
            # PositionOnMap
            self.GfxLegendPositionOnMap(oWindow.position_on_map, False)
            # Translucency
            self.m_logger.WriteLine6("\tThe current Translucency is: {0}", oWindow.translucency)
            oWindow.translucency = 23.456
            self.m_logger.WriteLine6("\tThe new Translucency is: {0}", oWindow.translucency)
            Assert.assertEqual(23.456, oWindow.translucency)

            def action110():
                oWindow.translucency = 123.456

            TryCatchAssertBlock.DoAssert("", action110)

    # endregion

    # region GfxLegendPositionOnMap
    def GfxLegendPositionOnMap(self, oPosition: "IFigureOfMeritGraphics2DPositionOnMap", bReadOnly: bool):
        Assert.assertIsNotNone(oPosition)
        if bReadOnly:

            def action111():
                oPosition.x = 123

            # X (readonly)
            TryCatchAssertBlock.DoAssert("", action111)

            def action112():
                oPosition.y = 123

            # Y (readonly)
            TryCatchAssertBlock.DoAssert("", action112)

        else:
            # X
            self.m_logger.WriteLine3("\tThe current X is: {0}", oPosition.x)
            oPosition.x = 123
            self.m_logger.WriteLine3("\tThe new X is: {0}", oPosition.x)
            Assert.assertEqual(123, oPosition.x)

            def action113():
                oPosition.x = -123

            TryCatchAssertBlock.DoAssert("", action113)
            # Y
            self.m_logger.WriteLine3("\tThe current Y is: {0}", oPosition.y)
            oPosition.y = 234
            self.m_logger.WriteLine3("\tThe new Y is: {0}", oPosition.y)
            Assert.assertEqual(234, oPosition.y)

            def action114():
                oPosition.y = -123

            TryCatchAssertBlock.DoAssert("", action114)

    # endregion

    # region GfxObjectCoverage
    def GfxObjectCoverage(self, oStkObjectCoverage: "IStkObjectCoverage"):
        self.m_logger.WriteLine("----- OBJECT COVERAGE GRAPHICS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oStkObjectCoverage)
        oObjCovFOM: "IObjectCoverageFigureOfMerit" = clr.CastAs(
            oStkObjectCoverage.figure_of_merit, IObjectCoverageFigureOfMerit
        )
        Assert.assertIsNotNone(oObjCovFOM)

        facAssetName: str = "Facility/Facility1"
        oObjCovFOM.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.ALTITUDE)
        oCollection: "ICoverageAssetListCollection" = oStkObjectCoverage.assets
        if Array.IndexOf(oCollection.available_assets, facAssetName) != -1:
            if oCollection.can_assign_asset(facAssetName):
                assetListElement: "ICoverageAssetListElement" = oCollection.add(facAssetName)
                assetListElement.required = True
                oStkObjectCoverage.compute()

                # static
                self.m_logger.WriteLine3(
                    "\tThe current object coverage (static) contour LineWidth is: {0}",
                    oObjCovFOM.graphics.static.contours.line_width,
                )
                oObjCovFOM.graphics.static.contours.line_width = 4
                self.m_logger.WriteLine3(
                    "\tThe new object coverage (static) contour LineWidth is: {0}",
                    oObjCovFOM.graphics.static.contours.line_width,
                )
                Assert.assertEqual(4, oObjCovFOM.graphics.static.contours.line_width)

                self.m_logger.WriteLine6(
                    "\tThe current object coverage (static) contour LineStyle is: {0}",
                    oObjCovFOM.graphics.static.contours.line_style,
                )
                oObjCovFOM.graphics.static.contours.line_style = LINE_STYLE.DOT_DASHED
                self.m_logger.WriteLine6(
                    "\tThe new object coverage (static)  contour LineStyle is: {0}",
                    oObjCovFOM.graphics.static.contours.line_style,
                )
                Assert.assertEqual(LINE_STYLE.DOT_DASHED, oObjCovFOM.graphics.static.contours.line_style)

                # animation
                self.m_logger.WriteLine3(
                    "\tThe current object coverage (animation) contour LineWidth is: {0}",
                    oObjCovFOM.graphics.animation.contours.line_width,
                )
                oObjCovFOM.graphics.animation.contours.line_width = 4
                self.m_logger.WriteLine3(
                    "\tThe new object coverage (animation) contour LineWidth is: {0}",
                    oObjCovFOM.graphics.animation.contours.line_width,
                )
                Assert.assertEqual(4, oObjCovFOM.graphics.animation.contours.line_width)

                self.m_logger.WriteLine6(
                    "\tThe current object coverage (animation) contour LineStyle is: {0}",
                    oObjCovFOM.graphics.animation.contours.line_style,
                )
                oObjCovFOM.graphics.animation.contours.line_style = LINE_STYLE.DOT_DASHED
                self.m_logger.WriteLine6(
                    "\tThe new object coverage (animation)  contour LineStyle is: {0}",
                    oObjCovFOM.graphics.animation.contours.line_style,
                )
                Assert.assertEqual(LINE_STYLE.DOT_DASHED, oObjCovFOM.graphics.animation.contours.line_style)

                oStkObjectCoverage.clear_coverage()

        else:
            Assert.fail("Asset not found. GfxObjectCoverage Failed")

        self.m_logger.WriteLine("----- OBJECT COVERAGE GRAPHICS TEST ----- END -----")

    # endregion
