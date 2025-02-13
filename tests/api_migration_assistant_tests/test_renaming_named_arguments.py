from runner import run


def test_rename_single_method_with_one_named_argument():
    run(
        """
        class MyClass:
            def MyMethod(self, TestArg):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass.MyMethod" OldName="TestArg" NewName="new_test_arg" Category="argument" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod(TestArg=5)
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod(new_test_arg=5)
        """,
    )


def test_rename_single_method_with_multiple_named_arguments():
    run(
        """
        class MyClass:
            def MyMethod(self, TestArgOne, TestArgTwo, TestArgThree):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass.MyMethod" OldName="TestArgOne" NewName="new_test_arg1" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethod" OldName="TestArgTwo" NewName="new_test_arg2" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethod" OldName="TestArgThree" NewName="new_test_arg3" Category="argument" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod(TestArgOne=1, TestArgTwo=2, TestArgThree=3)
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod(new_test_arg1=1, new_test_arg2=2, new_test_arg3=3)
        """,
    )


def test_rename_single_method_with_mixed_positional_and_named_arguments():
    run(
        """
        class MyClass:
            def MyMethod(self, TestArgOne, TestArgTwo, TestArgThree):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass.MyMethod" OldName="TestArgOne" NewName="new_test_arg1" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethod" OldName="TestArgTwo" NewName="new_test_arg2" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethod" OldName="TestArgThree" NewName="new_test_arg3" Category="argument" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod(1, 2, TestArgThree=3)
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod(1, 2, new_test_arg3=3)
        """,
    )


def test_rename_chained_methods_with_mixed_positional_and_named_arguments():
    run(
        """
        class MyClass:
            def MyMethodOne(self, MyMethodOneArgOne, MyMethodOneArgTwo, MyMethodOneArgThree):
                return self
            def MyMethodTwo(self, MyMethodTwoArgOne, MyMethodTwoArgTwo):
                return self
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgOne" NewName="my_method_one_arg_one" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgTwo" NewName="my_method_one_arg_two" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgThree" NewName="my_method_one_arg_three" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodTwo" OldName="MyMethodTwoArgOne" NewName="my_method_two_arg_one" Category="argument" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodOne(1, 2, MyMethodOneArgThree=3).MyMethodTwo(MyMethodTwoArgOne=4, MyMethodTwoArgTwo=5)
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodOne(1, 2, my_method_one_arg_three=3).MyMethodTwo(my_method_two_arg_one=4, MyMethodTwoArgTwo=5)
        """,
    )


def test_rename_nested_methods_with_mixed_positional_and_named_arguments():
    run(
        """
        class MyClass:
            def MyMethodOne(self, MyMethodOneArgOne, MyMethodOneArgTwo, MyMethodOneArgThree):
                return 5
            def MyMethodTwo(self, MyMethodTwoArgOne, MyMethodTwoArgTwo):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgOne" NewName="my_method_one_arg_one" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgTwo" NewName="my_method_one_arg_two" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgThree" NewName="my_method_one_arg_three" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodTwo" OldName="MyMethodTwoArgOne" NewName="my_method_two_arg_one" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodTwo" OldName="MyMethodTwoArgTwo" NewName="my_method_two_arg_two" Category="argument" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodOne(1, 2, MyMethodOneArgThree=m.MyMethodTwo(MyMethodTwoArgOne=4, MyMethodTwoArgTwo=5))
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodOne(1, 2, my_method_one_arg_three=m.MyMethodTwo(my_method_two_arg_one=4, my_method_two_arg_two=5))
        """,
    )


def test_rename_nested_methods_with_mixed_positional_and_named_arguments_and_external_call():
    run(
        """
        class MyClass:
            def MyMethodOne(self, MyMethodOneArgOne, MyMethodOneArgTwo, MyMethodOneArgThree):
                return 1
            def MyMethodTwo(self, MyMethodTwoArgOne, MyMethodTwoArgTwo):
                return 2
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgOne" NewName="my_method_one_arg_one" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgTwo" NewName="my_method_one_arg_two" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodOne" OldName="MyMethodOneArgThree" NewName="my_method_one_arg_three" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodTwo" OldName="MyMethodTwoArgOne" NewName="my_method_two_arg_one" Category="argument" />
            <Mapping ParentScope="MyClass.MyMethodTwo" OldName="MyMethodTwoArgTwo" NewName="my_method_two_arg_two" Category="argument" />
        </Mappings>
        """,
        """
        from api import MyClass
        import math

        def main():
            m = MyClass()
            m.MyMethodOne(1, 2, MyMethodOneArgThree=math.sin(m.MyMethodTwo(MyMethodTwoArgOne=4, MyMethodTwoArgTwo=5)))
        """,
        """
        from api import MyClass
        import math

        def main():
            m = MyClass()
            m.MyMethodOne(1, 2, my_method_one_arg_three=math.sin(m.MyMethodTwo(my_method_two_arg_one=4, my_method_two_arg_two=5)))
        """,
    )
