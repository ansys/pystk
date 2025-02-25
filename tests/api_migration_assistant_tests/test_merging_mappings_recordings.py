# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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
