# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from runner import run


def test_renaming_module_in_import():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "product.core.api",
                "NewRootScope": "other.utility"
            },
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        import product.core.api

        def main():
            m = product.core.api.MyClass()
            m.MyMethod()
        """,
        """
        import other.utility

        def main():
            m = other.utility.MyNewClass()
            m.MyMethodRenamed()
        """,
        api_root=["product", "core"],
    )


def test_renaming_module_and_type_in_from_import():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "product.core.api",
                "NewRootScope": "other.utility.api"
            },
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        from product.core.api import MyClass

        def main():
            m = MyClass()
            m.MyMethod()
        """,
        """
        from other.utility.api import MyNewClass

        def main():
            m = MyNewClass()
            m.MyMethodRenamed()
        """,
        api_root=["product", "core"],
    )


def test_renaming_module_and_enum_type_in_from_import():
    run(
        """
        from enum import IntEnum
        class MyEnum(IntEnum):
            Value1 = 1
        class MyClass:
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "product.core.api",
                "NewRootScope": "other.utility.api"
            },
            "EnumTypeMappings": [
                { "OldName": "MyEnum", "NewName": "MyNewEnum" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        from product.core.api import MyEnum, MyClass

        def main():
            c = MyEnum.Value1
            m = MyClass()
            m.MyMethod()
        """,
        """
        from other.utility.api import MyNewEnum, MyClass

        def main():
            c = MyNewEnum.Value1
            m = MyClass()
            m.MyMethodRenamed()
        """,
        api_root=["product", "core"],
    )


def test_renaming_module_only_in_from_import():
    run(
        """
        class MyClass:
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "product.core.api",
                "NewRootScope": "other.utility.api"
            },
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        from product.core.api import MyClass

        def main():
            m = MyClass()
            m.MyMethod()
        """,
        """
        from other.utility.api import MyClass

        def main():
            m = MyClass()
            m.MyMethodRenamed()
        """,
        api_root=["product", "core"],
    )


def test_renaming_type_only_in_from_import():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "product.core.api",
                "NewRootScope": "product.core.api"
            },
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        from product.core.api import MyClass

        def main():
            m = MyClass()
            m.MyMethod()
        """,
        """
        from product.core.api import MyNewClass

        def main():
            m = MyNewClass()
            m.MyMethodRenamed()
        """,
        api_root=["product", "core"],
    )


def test_renaming_deep_from_import():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "a.b.c.d.e.f.api",
                "NewRootScope": "x.y.z"
            },
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        from a.b.c.d.e.f.api import MyClass

        def main():
            m = MyClass()
            m.MyMethod()
        """,
        """
        from x.y.z import MyNewClass

        def main():
            m = MyNewClass()
            m.MyMethodRenamed()
        """,
        api_root=["a", "b", "c", "d", "e", "f"],
    )


def test_renaming_shallow_from_import():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "api",
                "NewRootScope": "xyz"
            },
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod()
        """,
        """
        from xyz import MyNewClass

        def main():
            m = MyNewClass()
            m.MyMethodRenamed()
        """,
    )


def test_renaming_module_in_import_as():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "product.core.api",
                "NewRootScope": "other.utility.api"
            },
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        import product.core.api as prod

        def main():
            m = prod.MyClass()
            m.MyMethod()
        """,
        """
        import other.utility.api as prod

        def main():
            m = prod.MyNewClass()
            m.MyMethodRenamed()
        """,
        api_root=["product", "core"],
    )


def test_renaming_module_in_from_import_as():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "product.core.api",
                "NewRootScope": "other.utility.api"
            },
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        from product.core.api import MyClass as MyKlass

        def main():
            m = MyKlass()
            m.MyMethod()
        """,
        """
        from other.utility.api import MyNewClass as MyKlass

        def main():
            m = MyKlass()
            m.MyMethodRenamed()
        """,
        api_root=["product", "core"],
    )


def test_renaming_module_in_import_with_explicit_use():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
            def MyMethod(self):
                pass
        """,
        """
        {
            "RootMapping": {
                "OldRootScope": "product.core.api",
                "NewRootScope": "other.utility.api"
            },
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ],
            "MemberMappings": [
                { "ParentScope": "MyClass", "OldName": "MyMethod", "NewName": "MyMethodRenamed" }
            ]
        }
        """,
        """
        import product.core.api

        def main():
            m = product.core.api.MyClass()
            m.MyMethod()
        """,
        """
        import other.utility.api

        def main():
            m = other.utility.api.MyNewClass()
            m.MyMethodRenamed()
        """,
        api_root=["product", "core"],
    )
