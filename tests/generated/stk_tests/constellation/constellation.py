import pytest
from test_util import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.stkobjects import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("ConstellationTests", "ConstellationTests.sc"))
            EarlyBoundTests.AG_CN = clr.Convert(
                TestBase.Application.current_scenario.children["Constellation1"], Constellation
            )

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_CN = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_CN: "Constellation" = None
    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        TestBase.logger.WriteLine("----- THE CONSTELLATION CONSTRAINTS TEST ----- BEGIN -----")
        # Constraints
        oConstraints: "ConstellationConstraints" = EarlyBoundTests.AG_CN.constraints
        Assert.assertIsNotNone(oConstraints)

        # FromParentConstraint
        oConstraints.from_parent_constraint = CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_ANY
        Assert.assertEqual(
            CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_ANY, oConstraints.from_parent_constraint
        )
        oConstraints.from_parent_constraint = CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_DIFFERENT
        Assert.assertEqual(
            CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_DIFFERENT, oConstraints.from_parent_constraint
        )
        oConstraints.from_parent_constraint = CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_SAME
        Assert.assertEqual(
            CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_SAME, oConstraints.from_parent_constraint
        )

        # ToParentConstraint
        oConstraints.to_parent_constraint = CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_ANY
        Assert.assertEqual(
            CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_ANY, oConstraints.to_parent_constraint
        )
        oConstraints.to_parent_constraint = CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_DIFFERENT
        Assert.assertEqual(
            CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_DIFFERENT, oConstraints.to_parent_constraint
        )
        oConstraints.to_parent_constraint = CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_SAME
        Assert.assertEqual(
            CONSTELLATION_FROM_TO_PARENT_CONSTRAINT.PARENT_CONSTRAINT_SAME, oConstraints.to_parent_constraint
        )

        # FromRestrictionType - From
        TestBase.logger.WriteLine6("\tThe current FromRestrictionType is: {0}", oConstraints.from_restriction_type)

        # SetFromRestrictionType (ALL_OF)
        oConstraints.set_from_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.ALL_OF)
        TestBase.logger.WriteLine6("\tThe new FromRestrictionType is: {0}", oConstraints.from_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.ALL_OF, oConstraints.from_restriction_type)
        Assert.assertIsNotNone(oConstraints.from_restriction)
        Assert.assertIsNone(clr.CastAs(oConstraints.from_restriction, ConstellationConstraintObjectRestriction))

        # SetFromRestrictionType (ANY_OF)
        oConstraints.set_from_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.ANY_OF)
        TestBase.logger.WriteLine6("\tThe new FromRestrictionType is: {0}", oConstraints.from_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.ANY_OF, oConstraints.from_restriction_type)
        Assert.assertIsNotNone(oConstraints.from_restriction)
        Assert.assertIsNone(clr.CastAs(oConstraints.from_restriction, ConstellationConstraintObjectRestriction))

        # SetFromRestrictionType (NONE_OF)
        oConstraints.set_from_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.NONE_OF)
        TestBase.logger.WriteLine6("\tThe new FromRestrictionType is: {0}", oConstraints.from_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.NONE_OF, oConstraints.from_restriction_type)
        Assert.assertIsNotNone(oConstraints.from_restriction)
        Assert.assertIsNone(clr.CastAs(oConstraints.from_restriction, ConstellationConstraintObjectRestriction))

        # SetFromRestrictionType (AT_LEAST_N)
        oConstraints.set_from_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.AT_LEAST_N)
        TestBase.logger.WriteLine6("\tThe new FromRestrictionType is: {0}", oConstraints.from_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.AT_LEAST_N, oConstraints.from_restriction_type)

        # FromRestriction
        self.TestObjectRestriction(clr.CastAs(oConstraints.from_restriction, ConstellationConstraintObjectRestriction))

        # SetFromRestrictionType (EXACTLY_N)
        oConstraints.set_from_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.EXACTLY_N)
        TestBase.logger.WriteLine6("\tThe new RestrictionType is: {0}", oConstraints.from_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.EXACTLY_N, oConstraints.from_restriction_type)

        # FromRestriction
        self.TestObjectRestriction(clr.CastAs(oConstraints.from_restriction, ConstellationConstraintObjectRestriction))

        with pytest.raises(Exception):
            oConstraints.set_from_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.UNKNOWN)

        # ToRestrictionType - To
        TestBase.logger.WriteLine6("\tThe current ToRestrictionType is: {0}", oConstraints.to_restriction_type)

        # SetToRestrictionType (ALL_OF)
        oConstraints.set_to_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.ALL_OF)
        TestBase.logger.WriteLine6("\tThe new ToRestrictionType is: {0}", oConstraints.to_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.ALL_OF, oConstraints.to_restriction_type)
        Assert.assertIsNotNone(oConstraints.to_restriction)
        Assert.assertIsNone(clr.CastAs(oConstraints.to_restriction, ConstellationConstraintObjectRestriction))

        # SetToRestrictionType (ANY_OF)
        oConstraints.set_to_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.ANY_OF)
        TestBase.logger.WriteLine6("\tThe new ToRestrictionType is: {0}", oConstraints.to_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.ANY_OF, oConstraints.to_restriction_type)
        Assert.assertIsNotNone(oConstraints.to_restriction)
        Assert.assertIsNone(clr.CastAs(oConstraints.to_restriction, ConstellationConstraintObjectRestriction))

        # SetToRestrictionType (NONE_OF)
        oConstraints.set_to_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.NONE_OF)
        TestBase.logger.WriteLine6("\tThe new ToRestrictionType is: {0}", oConstraints.to_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.NONE_OF, oConstraints.to_restriction_type)
        Assert.assertIsNotNone(oConstraints.to_restriction)
        Assert.assertIsNone(clr.CastAs(oConstraints.to_restriction, ConstellationConstraintObjectRestriction))

        # SetRestrictionType (AT_LEAST_N)
        oConstraints.set_to_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.AT_LEAST_N)
        TestBase.logger.WriteLine6("\tThe new ToRestrictionType is: {0}", oConstraints.to_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.AT_LEAST_N, oConstraints.to_restriction_type)

        # ToRestriction
        self.TestObjectRestriction(clr.CastAs(oConstraints.to_restriction, ConstellationConstraintObjectRestriction))

        # SetToRestrictionType (EXACTLY_N)
        oConstraints.set_to_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.EXACTLY_N)
        TestBase.logger.WriteLine6("\tThe new RestrictionType is: {0}", oConstraints.to_restriction_type)
        Assert.assertEqual(CONSTELLATION_CONSTRAINT_RESTRICTION.EXACTLY_N, oConstraints.to_restriction_type)

        # ToRestriction
        self.TestObjectRestriction(clr.CastAs(oConstraints.to_restriction, ConstellationConstraintObjectRestriction))

        with pytest.raises(Exception):
            oConstraints.set_to_restriction_type(CONSTELLATION_CONSTRAINT_RESTRICTION.UNKNOWN)

        TestBase.logger.WriteLine("----- THE CONSTELLATION CONSTRAINTS TEST ----- END -----")

    def TestObjectRestriction(self, oRestriction: "ConstellationConstraintObjectRestriction"):
        Assert.assertIsNotNone(oRestriction)
        # NumberOfObjects
        TestBase.logger.WriteLine3("\tThe current NumberOfObjects is: {0}", oRestriction.number_of_objects)
        newNumObjects: int = oRestriction.number_of_objects + 1
        oRestriction.number_of_objects = newNumObjects
        TestBase.logger.WriteLine3("\tThe new NumberOfObjects is: {0}", oRestriction.number_of_objects)
        Assert.assertEqual(newNumObjects, oRestriction.number_of_objects)
        with pytest.raises(Exception):
            oRestriction.number_of_objects = -12

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- THE CONSTELLATION GRAPHICS TEST ----- BEGIN -----")
        # Graphics
        oGraphics: "ConstellationGraphics" = EarlyBoundTests.AG_CN.graphics
        Assert.assertIsNotNone(oGraphics)
        # HideGraphics
        oGraphics.hide_graphics()
        # RestoreGraphics
        oGraphics.restore_graphics()
        TestBase.logger.WriteLine("----- THE CONSTELLATION GRAPHICS TEST ----- END -----")

    # endregion

    # region Definition
    @category("Basic Tests")
    def test_Definition(self):
        TestBase.logger.WriteLine("----- THE CONSTELLATION DEFINITION TEST ----- BEGIN -----")
        oHelper = ObjectLinkCollectionHelper()
        oHelper.Run(EarlyBoundTests.AG_CN.objects, TestBase.Application)
        TestBase.logger.WriteLine("----- THE CONSTELLATION DEFINITION TEST ----- END -----")

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_CN, IStkObject))
        oHelper.TestObjectFilesArray((clr.Convert(EarlyBoundTests.AG_CN, IStkObject)).object_files)

    # endregion

    # region ConstellationObjects
    @category("Basic Tests")
    def test_ConstellationObjects(self):
        #
        # Verify that adding a constellation to another constellation
        # only copies the objects within the constellation but
        # not the constellation itself.
        #
        newCn: "Constellation" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.CONSTELLATION, "TempConstellation"),
            Constellation,
        )
        try:
            facilities: "List[str]" = [
                "Cn_Facility_1",
                "Cn_Facility_2",
                "Cn_Facility_3",
                "Cn_Facility_4",
                "Cn_Facility_5",
            ]
            try:
                facility: str
                for facility in facilities:
                    o: "IStkObject" = TestBase.Application.current_scenario.children.new(
                        STK_OBJECT_TYPE.FACILITY, facility
                    )
                    EarlyBoundTests.AG_CN.objects.add_object(o)
                    del o

                newCn.objects.add_object(clr.CastAs(EarlyBoundTests.AG_CN, IStkObject))
                Assert.assertEqual(newCn.objects.count, EarlyBoundTests.AG_CN.objects.count)

                # Iterate the collection of objects in the constellation
                # to verify the original constellation object is not in it.
                o: "ObjectLink"

                # Iterate the collection of objects in the constellation
                # to verify the original constellation object is not in it.
                for o in newCn.objects:
                    Assert.assertNotEqual(o.linked_object.path, (clr.Convert(EarlyBoundTests.AG_CN, IStkObject)).path)

                # Remove a couple of objects from the temporary
                # constellation.
                newCn.objects.remove((newCn.objects.count - 1))
                newCn.objects.remove((newCn.objects.count - 1))
                Assert.assertEqual((EarlyBoundTests.AG_CN.objects.count - 2), newCn.objects.count)

                # Use the original constellation and copy it
                # back into the temporary to verify that
                # the objects that are already in the constellation
                # are not copied twice.
                newCn.objects.add_object(clr.CastAs(EarlyBoundTests.AG_CN, IStkObject))
                Assert.assertEqual(newCn.objects.count, EarlyBoundTests.AG_CN.objects.count)

            finally:
                facility: str
                for facility in facilities:
                    EarlyBoundTests.AG_CN.objects.remove_name(String.Format("Facility/{0}", facility))
                    TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, facility)

        finally:
            (clr.CastAs(newCn, IStkObject)).unload()

    # endregion

    # region Routing
    def test_Routing(self):
        routing: "ConstellationRouting" = EarlyBoundTests.AG_CN.routing

        routing.use_routing_file = False
        Assert.assertFalse(routing.use_routing_file)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            routing.routing_file = TestBase.GetScenarioFile("Constellation1.routing")

        routing.use_routing_file = True
        Assert.assertTrue(routing.use_routing_file)

        routing.routing_file = TestBase.GetScenarioFile("Constellation1.routing")
        Assert.assertEqual("Constellation1.routing", routing.routing_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            routing.routing_file = TestBase.GetScenarioFile("bogus.routing")

    # endregion
