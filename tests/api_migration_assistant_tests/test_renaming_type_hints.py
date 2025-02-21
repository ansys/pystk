# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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
