from runner import run


def test_merging_multiple_recordings():
    run(
        """
        class MyClass1:
            def __init__(self):
                pass
            def MyMethod1(self):
                pass
        class MyClass2:
            def __init__(self):
                pass
            def MyMethod2(self):
                pass
        """,
        [
            """
            <Mappings>
                <Mapping OldName="MyClass1" NewName="MyNewClass1" Category="class" />
                <Mapping ParentScope="MyClass1" OldName="MyMethod1" NewName="MyMethod1Renamed" Category="method" />
            </Mappings>
            """,
            """
            <Mappings>
                <Mapping ParentScope="MyClass2" OldName="MyMethod2" NewName="MyMethod2Renamed" Category="method" />
                <Mapping OldName="MyClass2" NewName="MyNewClass2" Category="class" />
            </Mappings>
            """,
        ],
        [
            {
                "code": """
                    from product.core.api import *
                    from common import common_function

                    def main1():
                        m = MyClass1()
                        m.MyMethod1()
                        common_function(1)
                    """,
                "filename": "test1.py",
                "entry_point": "main1",
            },
            {
                "code": """
                    from product.core.api import *
                    from common import common_function

                    def main2():
                        m = MyClass2()
                        m.MyMethod2()
                        common_function(2)
                    """,
                "filename": "test2.py",
                "entry_point": "main2",
            },
            {
                "code": """
                    from product.core.api import *

                    def common_function(i):
                        m = MyClass1() if i == 1 else MyClass2()
                        return m.MyMethod1() if i == 1 else m.MyMethod2()
                    """,
                "filename": "common.py",
                "entry_point": None,
            },
        ],
        [
            """
            from product.core.api import *
            from common import common_function

            def main1():
                m = MyNewClass1()
                m.MyMethod1Renamed()
                common_function(1)
            """,
            """
            from product.core.api import *
            from common import common_function

            def main2():
                m = MyNewClass2()
                m.MyMethod2Renamed()
                common_function(2)
            """,
            """
            from product.core.api import *

            def common_function(i):
                m = MyNewClass1() if i == 1 else MyNewClass2()
                return m.MyMethod1Renamed() if i == 1 else m.MyMethod2Renamed()
            """,
        ],
        api_root=["product", "core"],
    )
