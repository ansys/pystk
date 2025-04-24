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
