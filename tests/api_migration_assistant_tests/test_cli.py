from runner import run


def test_out_of_process_through_cli():
    run(
        """
        from enum import IntEnum
        class XyMyEnum(IntEnum):
            Value1 = 1
            Value2 = 2
            Value3 = 3
        class MyClass:
            def MyMethod(self, my_enum):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyMethod" NewName="MyMethodRenamed" Category="method" />
            <Mapping ParentScope="XyMyEnum" OldName="Value1" NewName="VALUE1" Category="enum_value" />
            <Mapping ParentScope="XyMyEnum" OldName="Value2" NewName="VALUE2" Category="enum_value" />
            <Mapping ParentScope="XyMyEnum" OldName="Value3" NewName="VALUE3" Category="enum_value" />
            <Mapping OldName="XyMyEnum" NewName="MyEnum" Category="enum_type" />
        </Mappings>
        """,
        """
        from product.core.api import *

        def main():
            m = MyClass()
            m.MyMethod(XyMyEnum.Value1)
        """,
        """
        from product.core.api import *

        def main():
            m = MyClass()
            m.MyMethodRenamed(MyEnum.VALUE1)
        """,
        api_root=["product", "core"],
        in_process=False,
    )


def test_running_pytest_as_module():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
        """,
        """
        <Mappings>
            <Mapping OldName="MyClass" NewName="MyNewClass" Category="class" />
        </Mappings>
        """,
        """
        from product.core.api import *

        def test_constructor():
            m = MyClass()
        """,
        """
        from product.core.api import *

        def test_constructor():
            m = MyNewClass()
        """,
        api_root=["product", "core"],
        in_process=False,
        run_pytest=True,
    )


def test_forwarding_arguments_to_recordee_in_process():
    run(
        """
        from enum import IntEnum
        class XyMyEnum(IntEnum):
            Value1 = 1
            Value2 = 2
            Value3 = 3
        class MyClass:
            def MyMethod(self, my_enum):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyMethod" NewName="MyMethodRenamed" Category="method" />
            <Mapping ParentScope="XyMyEnum" OldName="Value1" NewName="VALUE1" Category="enum_value" />
            <Mapping ParentScope="XyMyEnum" OldName="Value2" NewName="VALUE2" Category="enum_value" />
            <Mapping ParentScope="XyMyEnum" OldName="Value3" NewName="VALUE3" Category="enum_value" />
            <Mapping OldName="XyMyEnum" NewName="MyEnum" Category="enum_type" />
        </Mappings>
        """,
        """
        import sys
        from product.core.api import *

        def main():
            assert len(sys.argv) == 3
            assert sys.argv[0] == "input"
            assert sys.argv[1] == "abc"
            assert sys.argv[2] == "5"
            m = MyClass()
            m.MyMethod(XyMyEnum.Value1)
        """,
        """
        import sys
        from product.core.api import *

        def main():
            assert len(sys.argv) == 3
            assert sys.argv[0] == "input"
            assert sys.argv[1] == "abc"
            assert sys.argv[2] == "5"
            m = MyClass()
            m.MyMethodRenamed(MyEnum.VALUE1)
        """,
        api_root=["product", "core"],
        in_process=True,
        extra_args=["abc", "5"],
    )


def test_forwarding_arguments_to_recordee_out_of_process():
    run(
        """
        from enum import IntEnum
        class XyMyEnum(IntEnum):
            Value1 = 1
            Value2 = 2
            Value3 = 3
        class MyClass:
            def MyMethod(self, my_enum):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyMethod" NewName="MyMethodRenamed" Category="method" />
            <Mapping ParentScope="XyMyEnum" OldName="Value1" NewName="VALUE1" Category="enum_value" />
            <Mapping ParentScope="XyMyEnum" OldName="Value2" NewName="VALUE2" Category="enum_value" />
            <Mapping ParentScope="XyMyEnum" OldName="Value3" NewName="VALUE3" Category="enum_value" />
            <Mapping OldName="XyMyEnum" NewName="MyEnum" Category="enum_type" />
        </Mappings>
        """,
        """
        import sys
        from product.core.api import *

        def main():
            assert len(sys.argv) == 3
            assert sys.argv[0] == "input"
            assert sys.argv[1] == "abc"
            assert sys.argv[2] == "5"
            m = MyClass()
            m.MyMethod(XyMyEnum.Value1)
        """,
        """
        import sys
        from product.core.api import *

        def main():
            assert len(sys.argv) == 3
            assert sys.argv[0] == "input"
            assert sys.argv[1] == "abc"
            assert sys.argv[2] == "5"
            m = MyClass()
            m.MyMethodRenamed(MyEnum.VALUE1)
        """,
        api_root=["product", "core"],
        in_process=False,
        extra_args=["abc", "5"],
    )
