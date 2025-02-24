from runner import run


def test_rename_constructor_no_arguments():
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

        def main():
            m = MyClass()
        """,
        """
        from product.core.api import *

        def main():
            m = MyNewClass()
        """,
        api_root=["product", "core"],
    )


def test_rename_constructor_with_arguments():
    run(
        """
        class MyClass:
            def __init__(self, a, b, c):
                pass
        """,
        """
        <Mappings>
            <Mapping OldName="MyClass" NewName="MyNewClass" Category="class" />
        </Mappings>
        """,
        """
        from product.core.api import *

        def main():
            m = MyClass(1, "abc", 2.0)
        """,
        """
        from product.core.api import *

        def main():
            m = MyNewClass(1, "abc", 2.0)
        """,
        api_root=["product", "core"],
    )


def test_rename_nested_constructor():
    run(
        """
        class MyClass1:
            def __init__(self, a):
                pass
        class MyClass2:
            def __init__(self, b):
                pass
        class MyClass3:
            def __init__(self, c):
                pass
        """,
        """
        <Mappings>
            <Mapping OldName="MyClass1" NewName="MyNewClassA" Category="class" />
            <Mapping OldName="MyClass2" NewName="MyNewClassB" Category="class" />
            <Mapping OldName="MyClass3" NewName="MyNewClassC" Category="class" />
        </Mappings>
        """,
        """
        from product.core.api import *

        def main():
            m = MyClass1(MyClass2(MyClass3(1)))
        """,
        """
        from product.core.api import *

        def main():
            m = MyNewClassA(MyNewClassB(MyNewClassC(1)))
        """,
        api_root=["product", "core"],
    )


def test_rename_constructor_no_arguments_fully_qualified():
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
        import product.core.api

        def main():
            m = product.core.api.MyClass()
        """,
        """
        import product.core.api

        def main():
            m = product.core.api.MyNewClass()
        """,
        api_root=["product", "core"],
    )
