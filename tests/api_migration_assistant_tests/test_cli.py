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
