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


def test_rename_constructor_no_arguments():
    run(
        """
        class MyClass:
            def __init__(self):
                pass
        """,
        """
        {
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ]
        }
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
        {
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ]
        }
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
        {
            "ClassMappings": [
                { "OldName": "MyClass1", "NewName": "MyNewClassA" },
                { "OldName": "MyClass2", "NewName": "MyNewClassB" },
                { "OldName": "MyClass3", "NewName": "MyNewClassC" }
            ]
        }
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
        {
            "ClassMappings": [
                { "OldName": "MyClass", "NewName": "MyNewClass" }
            ]
        }
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
