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


def test_rename_single_method_no_argument():
    run(
        """
        class MyClass:
            def MyMethod(self):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyMethod" NewName="MyMethodRenamed" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod()
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodRenamed()
        """,
    )


def test_rename_single_method_with_arguments():
    run(
        """
        class MyClass:
            def MyMethod(self, a, b, c):
                pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyMethod" NewName="MyMethodRenamed" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod(1, 2, 3)
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodRenamed(1, 2, 3)
        """,
    )


def test_rename_single_repeated_method_no_argument():
    run(
        """
        class MyClass:
            def MyMethod(self):
                return self
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyMethod" NewName="MyMethodRenamed" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod().MyMethod()
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodRenamed().MyMethodRenamed()
        """,
    )


def test_rename_single_repeated_method_with_arguments():
    run(
        """
        class MyClass:
            def MyMethod(self, a, b, c, d, e, f):
                return self
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyMethod" NewName="MyMethodRenamed" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod(1, 2, 3, 4, 5, 6).MyMethod(1, 2, 3, 4, 5, 6)
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodRenamed(1, 2, 3, 4, 5, 6).MyMethodRenamed(1, 2, 3, 4, 5, 6)
        """,
    )


def test_rename_multiple_methods_with_arguments():
    run(
        """
        class MyClass:
            def MyMethod1(self, a, b, c, d, e, f):
                return self
            def MyMethod2(self, a, b, c, d, e, f):
                return self
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyMethod1" NewName="MyMethodRenamed1" Category="method" />
            <Mapping ParentScope="MyClass" OldName="MyMethod2" NewName="MyMethodRenamed2" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod1(1, 2, 3, 4, 5, 6).MyMethod2(1, 2, 3, 4, 5, 6)
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethodRenamed1(1, 2, 3, 4, 5, 6).MyMethodRenamed2(1, 2, 3, 4, 5, 6)
        """,
    )


def test_rename_correct_method_when_two_methods_with_same_name():
    run(
        """
        class MyClass1:
            def MyMethod(self, a, b, c, d, e, f):
                return self
        class MyClass2:
            def MyMethod(self, a, b, c, d):
                return MyClass1()
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass1" OldName="MyMethod" NewName="MyMethodRenamed1" Category="method" />
            <Mapping ParentScope="MyClass2" OldName="MyMethod" NewName="MyMethodRenamed2" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass2

        def main():
            m = MyClass2()
            m.MyMethod(1, 2, 3, 4).MyMethod(1, 2, 3, 4, 5, 6)
        """,
        """
        from api import MyClass2

        def main():
            m = MyClass2()
            m.MyMethodRenamed2(1, 2, 3, 4).MyMethodRenamed1(1, 2, 3, 4, 5, 6)
        """,
    )


def test_rename_method_with_mro():
    run(
        """
        class MyBaseClass1:
            def MyMethod1(self):
                pass
        class MyBaseClass2:
            def MyMethod2(self):
                pass
        class MyClass(MyBaseClass1, MyBaseClass2):
            pass
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyBaseClass1" OldName="MyMethod1" NewName="MyMethod1Renamed" Category="method" />
            <Mapping ParentScope="MyBaseClass2" OldName="MyMethod2" NewName="MyMethod2Renamed" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod1()
            m.MyMethod2()
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyMethod1Renamed()
            m.MyMethod2Renamed()
        """,
    )
