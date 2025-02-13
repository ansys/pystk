from runner import run


def test_rename_simple_type_hint():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
        """,
        """
        <Mappings OldRootScope="product.core.api" NewRootScope="product.core.api">
            <Mapping OldName="MyClass" NewName="MyNewClass" Category="class" />
        </Mappings>
        """,
        """
        from product.core.api import *

        def main():
            m: MyClass = MyClass()
        """,
        """
        from product.core.api import *

        def main():
            m: MyNewClass = MyNewClass()
        """,
        api_root=["product", "core"],
    )


def test_rename_simple_double_quoted_type_hint():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
        """,
        """
        <Mappings OldRootScope="product.core.api" NewRootScope="product.core.api">
            <Mapping OldName="MyClass" NewName="MyNewClass" Category="class" />
        </Mappings>
        """,
        """
        from product.core.api import *

        def main():
            m: "MyClass" = MyClass()
        """,
        """
        from product.core.api import *

        def main():
            m: "MyNewClass" = MyNewClass()
        """,
        api_root=["product", "core"],
    )


def test_rename_type_only_in_fully_qualified_type_hint():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
        """,
        """
        <Mappings OldRootScope="product.core.api" NewRootScope="product.core.api">
            <Mapping OldName="MyClass" NewName="MyNewClass" Category="class" />
        </Mappings>
        """,
        """
        import product.core.api

        def main():
            m: product.core.api.MyClass = product.core.api.MyClass()
        """,
        """
        import product.core.api

        def main():
            m: product.core.api.MyNewClass = product.core.api.MyNewClass()
        """,
        api_root=["product", "core"],
    )


def test_rename_fully_qualified_type_hint():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
        """,
        """
        <Mappings OldRootScope="product.core.api" NewRootScope="other.utility">
            <Mapping OldName="MyClass" NewName="MyNewClass" Category="class" />
        </Mappings>
        """,
        """
        import product.core.api

        def main():
            m: product.core.api.MyClass = product.core.api.MyClass()
        """,
        """
        import other.utility

        def main():
            m: other.utility.MyNewClass = other.utility.MyNewClass()
        """,
        api_root=["product", "core"],
    )


def test_rename_fully_qualified_quoted_type_hint():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
        """,
        """
        <Mappings OldRootScope="product.core.api" NewRootScope="other.utility">
            <Mapping OldName="MyClass" NewName="MyNewClass" Category="class" />
        </Mappings>
        """,
        """
        import product.core.api

        def main():
            m: "product.core.api.MyClass" = product.core.api.MyClass()
        """,
        """
        import other.utility

        def main():
            m: "other.utility.MyNewClass" = other.utility.MyNewClass()
        """,
        api_root=["product", "core"],
    )
