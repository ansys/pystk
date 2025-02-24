from runner import run


def test_rename_single_property():
    run(
        """
        class MyClass:
            def __init(self):
                self.my_property = 0
            @property
            def MyProperty(self):
                return self.my_property
            @MyProperty.setter
            def MyProperty(self, value):
                self.my_property = value
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyProperty" NewName="MyPropertyRenamed" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyProperty = 5
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyPropertyRenamed = 5
        """,
    )


def test_rename_chained_properties():
    run(
        """
        class MyClassA:
            def __init(self):
                self.my_property1 = 0
            @property
            def MyProperty1(self):
                return self.my_property1
            @MyProperty1.setter
            def MyProperty1(self, value):
                self.my_property1 = value
        class MyClassB:
            def __init__(self):
                self.my_property2 = MyClassA()
            @property
            def MyProperty2(self):
                return self.my_property2
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClassA" OldName="MyProperty1" NewName="MyPropertyRenamed1" Category="method" />
            <Mapping ParentScope="MyClassB" OldName="MyProperty2" NewName="MyPropertyRenamed2" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClassB

        def main():
            m = MyClassB()
            m.MyProperty2.MyProperty1 = 5
        """,
        """
        from api import MyClassB

        def main():
            m = MyClassB()
            m.MyPropertyRenamed2.MyPropertyRenamed1 = 5
        """,
    )


def test_rename_property_via_setattr():
    run(
        """
        def set_class_attribute2(this, attrname, value, classType):
            print("set_class_attribute")
            found_prop = classType._get_property(this, attrname)
            if found_prop is not None:
                found_prop.__set__(this, value)
            else:
                raise RuntimeError(f"{attrname} is not a recognized attribute in {classType.__name__}.")
            
        def set_class_attribute1(this, attrname, value, classType):
            set_class_attribute2(this, attrname, value, classType)
            
        def set_class_attribute(this, attrname, value, classType):
            set_class_attribute1(this, attrname, value, classType)
            
        class MyClass:
            def __init(self):
                self.my_property = 0
            @property
            def MyProperty(self):
                return self.my_property
            @MyProperty.setter
            def MyProperty(self, value):
                self.__dict__["my_property"] = value
            def __setattr__(self, attrname, value):
                set_class_attribute(self, attrname, value, MyClass)
            def _get_property(self, attrname):
                if attrname == "MyProperty":
                    return MyClass.MyProperty
        """,
        """
        <Mappings>
            <Mapping ParentScope="MyClass" OldName="MyProperty" NewName="MyPropertyRenamed" Category="method" />
        </Mappings>
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyProperty = 5
            print(m.MyProperty)
        """,
        """
        from api import MyClass

        def main():
            m = MyClass()
            m.MyPropertyRenamed = 5
            print(m.MyPropertyRenamed)
        """,
    )
