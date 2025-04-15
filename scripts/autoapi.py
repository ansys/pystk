import _ast
import ast
import os
from pathlib import Path
import textwrap


class ManualRSTGenerator(object):
    core_namespace = "ansys.stk.core"

    def __init__(self, module_dir, doc_dir):
        self.module_dir = module_dir
        self.doc_dir = doc_dir

    def generate_rst_for_manual_modules(self, auto_files):
        for path in Path(self.module_dir).rglob("*.py"):
            is_autofile = False
            is_internal_file = False
            for auto_file in auto_files:
                if auto_file.replace("/", "\\") in str(path):
                    is_autofile = True
            if "\\internal\\" in str(path):
                is_internal_file = True
            if not is_autofile and not is_internal_file and str(path).endswith(".py"):
                self._generate_rst_for_pymodule(str(path))

    def _wrap_python_code_snippets(self, unformatted_docstring: str):
        formatted_docstring = ""

        in_snippet = False
        for line in unformatted_docstring.splitlines():
            if not in_snippet and len(line) - len(line.lstrip()) > 0:  # found indentation
                in_snippet = True
                formatted_docstring += ".. code-block:: python\n\n"
            elif in_snippet and len(line) - len(line.lstrip()) == 0:  # found end of indentation
                in_snippet = False

            formatted_docstring += line + "\n"

        return formatted_docstring.rstrip()

    def _generate_rst_for_pymodule(self, path_to_src_file: str):
        relative_namespace = (
            path_to_src_file[len(self.module_dir) :].replace("\\__init__.py", "").replace(".py", "").replace("\\", ".")
        )
        full_namespace = self.core_namespace + relative_namespace

        containing_namespace = ".".join(full_namespace.split(".")[:-1])
        module_name = full_namespace.split(".")[-1]

        if path_to_src_file == self.module_dir + "\\__init__.py":
            return

        out_file_path = self.doc_dir + "\\".join(relative_namespace.split(".")) + ".rst"
        if not os.path.exists(os.path.split(out_file_path)[0]):
            os.makedirs(os.path.split(out_file_path)[0])

        with (
            open(path_to_src_file, "r", encoding="utf-8") as in_file,
            open(out_file_path, "w", encoding="utf-8") as out_file,
        ):
            tree = ast.parse(in_file.read())

            submodules = []
            subpackages = []

            if path_to_src_file.endswith("__init__.py"):
                this_dir = os.path.split(path_to_src_file)[0]
                dir_contents = os.listdir(this_dir)

                for content in dir_contents:
                    if (
                        os.path.isfile(os.path.join(this_dir, content))
                        and content.endswith(".py")
                        and not content.endswith("__init__.py")
                    ):
                        submodules.append(content.replace(".py", ""))
                    elif os.path.isdir(os.path.join(this_dir, content)) and content != "__pycache__":
                        subpackages.append(content)

            type_definitions = [
                type_defintion for type_defintion in tree.body if isinstance(type_defintion, _ast.ClassDef)
            ]
            enums = [
                type_definition
                for type_definition in type_definitions
                if (
                    "IntEnum" in [base.id for base in type_definition.bases]
                    or "IntFlag" in [base.id for base in type_definition.bases]
                )
            ]

            classes = []
            interfaces = []

            for type_definition in type_definitions:
                if type_definition not in enums:
                    if type_definition.name.startswith("I"):
                        interfaces.append(type_definition)
                    elif not type_definition.name.startswith("_"):
                        classes.append(type_definition)

            out_file.writelines(
                [
                    "The ``" + module_name + "`` module\n",
                    "======" + (len(module_name) * "=") + "=========\n",
                    "\n",
                    ".. py:module:: " + containing_namespace + "." + module_name + "\n",
                    "\n",
                ]
            )

            if len(subpackages) + len(submodules) + len(interfaces) + len(classes) + len(enums) > 0:
                out_file.writelines(
                    [
                        "Summary\n",
                        "-------\n",
                        "\n",
                        ".. tab-set::\n",
                        "\n",
                    ]
                )

                if len(subpackages) > 0:
                    out_file.writelines(
                        [
                            "    .. tab-item:: Subpackages\n",
                            "\n",
                            "        .. list-table::\n",
                            "            :header-rows: 0\n",
                            "            :widths: auto\n",
                            "\n",
                        ]
                    )

                    for subpackage in subpackages:
                        out_file.write(
                            f"            * - :py:obj:`~{containing_namespace}.{module_name}.{subpackage}`\n"
                        )

                    out_file.write("\n")
                    out_file.write("\n")

                if len(submodules) > 0:
                    out_file.writelines(
                        [
                            "    .. tab-item:: Submodules\n",
                            "\n",
                            "        .. list-table::\n",
                            "            :header-rows: 0\n",
                            "            :widths: auto\n",
                            "\n",
                        ]
                    )

                    for submodule in submodules:
                        out_file.write(f"            * - :py:obj:`~{containing_namespace}.{module_name}.{submodule}`\n")

                    out_file.write("\n")
                    out_file.write("\n")

                for definition_type, definitions in {
                    "Interfaces": interfaces,
                    "Classes": classes,
                    "Enums": enums,
                }.items():
                    if len(definitions) > 0:
                        out_file.writelines(
                            [
                                "    .. tab-item:: " + definition_type + "\n",
                                "\n",
                                "        .. list-table::\n",
                                "            :header-rows: 0\n",
                                "            :widths: auto\n",
                                "\n",
                            ]
                        )

                        for definition in definitions:
                            out_file.write(
                                f"            * - :py:class:`~{containing_namespace}.{module_name}.{definition.name}`\n"
                            )
                            if ast.get_docstring(definition) is not None:
                                out_file.write(f"              - {ast.get_docstring(definition).splitlines()[0]}\n")
                            out_file.write("\n")

                        out_file.write("\n")

                out_file.write("\n")

            out_file.writelines(["Description\n", "-----------\n", "\n"])

            if len(tree.body) > 0 and hasattr(tree.body[0], "value") and hasattr(tree.body[0].value, "value"):
                out_file.write(tree.body[0].value.value.strip() + "\n")
                out_file.write("\n")

            out_file.writelines(
                [
                    ".. py:currentmodule:: " + containing_namespace + "." + module_name + "\n",
                    "\n",
                    ".. TABLE OF CONTENTS\n",
                    "\n",
                ]
            )

            if len(subpackages) > 0:
                out_file.writelines(
                    [".. toctree::\n", "    :titlesonly:\n", "    :maxdepth: 1\n", "    :hidden:\n", "\n"]
                )

                for subpackage in subpackages:
                    out_file.write(f"     🖿 {subpackage}<{module_name}/{subpackage}>\n")

                out_file.write("\n")
                out_file.write("\n")

            if len(submodules) > 0:
                out_file.writelines(
                    [".. toctree::\n", "    :titlesonly:\n", "    :maxdepth: 1\n", "    :hidden:\n", "\n"]
                )

                for submodule in submodules:
                    out_file.write(f"     🗎 {submodule}<{module_name}/{submodule}>\n")

                out_file.write("\n")
                out_file.write("\n")

            if len(classes) + len(interfaces) + len(enums) > 0:
                for definition_type, definitions in {
                    "Interfaces": interfaces,
                    "Classes": classes,
                    "Enums": enums,
                }.items():
                    if len(definitions) > 0:
                        out_file.writelines(
                            [".. toctree::\n", "    :titlesonly:\n", "    :maxdepth: 1\n", "    :hidden:\n", "\n"]
                        )

                        link_symbol_map = {"Interfaces": "", "Classes": "", "Enums": "≔ "}

                        for definition in definitions:
                            out_file.write(
                                "     "
                                + link_symbol_map[definition_type]
                                + f"{definition.name}<{module_name}/{definition.name}>\n"
                            )

                        out_file.write("\n")

                out_file.write("\n")

            for obj_definition in classes + interfaces:
                self._generate_rst_for_pyobj(obj_definition, containing_namespace, module_name, out_file_path)

            for enum_definition in enums:
                self._generate_rst_for_pyenum(enum_definition, containing_namespace, module_name, out_file_path)

        return

    def _generate_rst_for_pyobj(self, obj_definition, containing_namespace, module_name, module_rst_file_path):
        out_obj_file_path = (
            os.path.join(os.path.split(module_rst_file_path)[0], module_name, obj_definition.name) + ".rst"
        )
        if not os.path.exists(os.path.split(out_obj_file_path)[0]):
            os.makedirs(os.path.split(out_obj_file_path)[0])
        with open(out_obj_file_path, "w", encoding="utf-8") as out_obj_file:
            out_obj_file.writelines(
                [
                    obj_definition.name + "\n",
                    len(obj_definition.name) * "=" + "\n",
                    "\n",
                    ".. py:class:: " + containing_namespace + "." + module_name + "." + obj_definition.name + "\n",
                    "\n",
                    "   " + ", ".join(base.id for base in obj_definition.bases) + "\n",
                    "\n",
                ]
            )

            if ast.get_docstring(obj_definition) is not None:
                formatted_docstring = self._wrap_python_code_snippets(ast.get_docstring(obj_definition))
                out_obj_file.write(f"{textwrap.indent(formatted_docstring, '   ')}\n")
                out_obj_file.write("\n")

            out_obj_file.writelines([".. py:currentmodule:: " + obj_definition.name + "\n", "\n", "\n"])

            def is_property(method):
                return (
                    next((x for x in method.decorator_list if hasattr(x, "id") and x.id == "property"), None)
                    is not None
                )

            def is_setter(method):
                return (
                    next((x for x in method.decorator_list if (hasattr(x, "attr") and x.attr == "setter")), None)
                    is not None
                )

            filtered_methods = [
                n for n in obj_definition.body if isinstance(n, ast.FunctionDef) and not n.name.startswith("_")
            ]
            properties = [method for method in filtered_methods if is_property(method)]
            setters = [method for method in filtered_methods if is_setter(method)]
            filtered_methods = [
                method for method in filtered_methods if method not in properties and method not in setters
            ]

            if len(properties) > 0 or len(filtered_methods) > 0:
                out_obj_file.writelines(
                    [
                        "Overview\n",
                        "--------\n",
                        "\n",
                    ]
                )

            if len(filtered_methods) > 0:
                out_obj_file.writelines(
                    [
                        ".. tab-set::\n",
                        "\n",
                        "    .. tab-item:: Methods\n",
                        "\n",
                        "        .. list-table::\n",
                        "            :header-rows: 0\n",
                        "            :widths: auto\n",
                        "\n",
                    ]
                )

                for method in filtered_methods:
                    out_obj_file.write(
                        f"            * - :py:attr:`~{containing_namespace}.{module_name}.{obj_definition.name}.{method.name}`\n"
                    )
                    if ast.get_docstring(method) is not None:
                        lines = ast.get_docstring(method).splitlines()
                        out_obj_file.write(f"              - {lines[0]}\n")
                        if len(lines) > 1:
                            for line in lines[1:]:
                                out_obj_file.write(f"                {line}\n")

                out_obj_file.write("\n")

            if len(properties) > 0:
                out_obj_file.writelines(
                    [
                        ".. tab-set::\n",
                        "\n",
                        "    .. tab-item:: Properties\n",
                        "\n",
                        "        .. list-table::\n",
                        "            :header-rows: 0\n",
                        "            :widths: auto\n",
                        "\n",
                    ]
                )

                for prop in properties:
                    out_obj_file.write(
                        f"            * - :py:attr:`~{containing_namespace}.{module_name}.{obj_definition.name}.{prop.name}`\n"
                    )
                    if ast.get_docstring(prop) is not None:
                        lines = ast.get_docstring(prop).splitlines()
                        out_obj_file.write(f"              - {lines[0]}\n")
                        if len(lines) > 1:
                            for line in lines[1:]:
                                out_obj_file.write(f"                {line}\n")

                out_obj_file.write("\n")

            out_obj_file.writelines(
                [
                    "Import detail\n",
                    "-------------\n",
                    "\n",
                    ".. code-block:: python\n",
                    "\n",
                    f"    from {containing_namespace}.{module_name} import {obj_definition.name}\n",
                    "\n",
                    "\n",
                ]
            )

            if len(properties) > 0:
                out_obj_file.writelines(
                    [
                        "Property detail\n",
                        "---------------\n",
                        "\n",
                    ]
                )

                for prop in properties:
                    ret = ""
                    has_self = False

                    if isinstance(prop.returns, ast.Constant):
                        ret = "None"
                    else:
                        if prop.returns is not None and hasattr(prop.returns, "id"):
                            ret = prop.returns.id
                        else:
                            ret = ""

                    out_obj_file.writelines(
                        [
                            f".. py:property:: {prop.name}\n",
                            f"    :canonical: {containing_namespace}.{module_name}.{obj_definition.name}.{prop.name}\n",
                            f"    :type: {ret}\n",
                            "\n",
                        ]
                    )

                    if ast.get_docstring(prop) is not None:
                        lines = ast.get_docstring(prop).splitlines()
                        out_obj_file.write(f"    {lines[0]}\n")
                        if len(lines) > 1:
                            for line in lines[1:]:
                                out_obj_file.write(f"    {line}\n")
                        out_obj_file.write("\n")

                out_obj_file.write("\n")

            if len(filtered_methods) > 0:
                out_obj_file.writelines(
                    [
                        "Method detail\n",
                        "-------------\n",
                        "\n",
                    ]
                )

                for method in filtered_methods:
                    args = ""
                    ret = ""
                    first = True
                    has_self = False
                    default_index = 0
                    for index, arg in enumerate(method.args.args):
                        if not first:
                            args += ", "
                        first = False
                        args += arg.arg
                        if arg.annotation is not None and hasattr(arg.annotation, "id"):
                            args += ": " + arg.annotation.id
                            if method.args.defaults is not None and default_index < len(method.args.defaults):
                                default = method.args.defaults[default_index]
                                if isinstance(default, ast.Constant):
                                    args += " = " + str(default.value)
                                    default_index += 1

                    if isinstance(method.returns, ast.Constant):
                        ret = " -> None"
                    else:
                        if method.returns is not None and hasattr(method.returns, "id"):
                            ret = " -> " + method.returns.id
                        else:
                            ret = ""

                    out_obj_file.writelines(
                        [
                            f".. py:method:: {method.name}({args}){ret}\n",
                            f"    :canonical: {containing_namespace}.{module_name}.{obj_definition.name}.{method.name}\n",
                            "\n",
                        ]
                    )

                    if ast.get_docstring(method) is not None:
                        lines = ast.get_docstring(method).splitlines()
                        out_obj_file.write(f"    {lines[0]}\n")
                        if len(lines) > 1:
                            for line in lines[1:]:
                                out_obj_file.write(f"    {line}\n")
                        out_obj_file.write("\n")

                    filtered_args = [
                        arg
                        for arg in method.args.args
                        if arg.annotation is not None and hasattr(arg.annotation, "id") and arg.annotation.id != "self"
                    ]
                    if len(filtered_args) > 0:
                        out_obj_file.write("    :Parameters:\n")
                        out_obj_file.write("\n")
                        for arg in filtered_args:
                            type_hint = ""
                            if arg.annotation is not None and hasattr(arg.annotation, "id"):
                                type_hint = f" : :obj:`~{arg.annotation.id}`"
                            out_obj_file.write(f"    **{arg.arg}**{type_hint}\n")

                        out_obj_file.write("\n")

                    return_type = ""
                    if isinstance(method.returns, ast.Constant):
                        return_type = "None"
                    else:
                        if method.returns is not None and hasattr(method.returns, "id"):
                            return_type = method.returns.id

                    if return_type != "":
                        out_obj_file.writelines(
                            [
                                "    :Returns:\n",
                                "\n",
                                f"        :obj:`~{return_type}`\n",
                                "\n",
                            ]
                        )

                out_obj_file.write("\n")

    def _generate_rst_for_pyenum(self, enum_definition, containing_namespace, module_name, module_rst_file_path):
        out_enum_file_path = (
            os.path.join(os.path.split(module_rst_file_path)[0], module_name, enum_definition.name) + ".rst"
        )
        if not os.path.exists(os.path.split(out_enum_file_path)[0]):
            os.makedirs(os.path.split(out_enum_file_path)[0])
        with open(out_enum_file_path, "w", encoding="utf-8") as out_enum_file:
            out_enum_file.writelines(
                [
                    enum_definition.name + "\n",
                    len(enum_definition.name) * "=" + "\n",
                    "\n",
                    ".. py:class:: " + containing_namespace + "." + module_name + "." + enum_definition.name + "\n",
                    "\n",
                    "   " + ", ".join(base.id for base in enum_definition.bases) + "\n",
                    "\n",
                ]
            )

            if ast.get_docstring(enum_definition) is not None:
                out_enum_file.write(f"{textwrap.indent(ast.get_docstring(enum_definition), '   ')}\n")
                out_enum_file.write("\n")

            out_enum_file.writelines(
                [
                    ".. py:currentmodule:: " + enum_definition.name + "\n",
                    "\n",
                    "\n",
                ]
            )

            enum_value_content = []
            for index, element in enumerate(enum_definition.body):
                if isinstance(element, ast.Assign):
                    enum_value = element.targets[0].id
                    enum_constant = element.value.value
                    docstring = None
                    if index + 1 < len(enum_definition.body):
                        maybe_docstring = enum_definition.body[index + 1]
                        if isinstance(maybe_docstring, ast.Expr):
                            if isinstance(maybe_docstring.value, ast.Constant):
                                docstring = maybe_docstring.value.value
                    enum_value_content.append({"value": enum_value, "constant": enum_constant, "docstring": docstring})

            if len(enum_value_content) > 0:
                out_enum_file.writelines(
                    [
                        "Overview\n",
                        "--------\n",
                        "\n",
                        ".. tab-set::\n",
                        "\n",
                        "    .. tab-item:: Members\n",
                        "\n",
                        "        .. list-table::\n",
                        "            :header-rows: 0\n",
                        "            :widths: auto\n",
                        "\n",
                    ]
                )

                for value_content in enum_value_content:
                    val = value_content["value"]
                    out_enum_file.write(f"            * - :py:attr:`~{val}`\n")
                    if value_content["docstring"] is not None:
                        lines = value_content["docstring"].splitlines()
                        out_enum_file.write(f"              - {lines[0]}\n")
                        if len(lines) > 1:
                            for line in lines[1:]:
                                out_enum_file.write(f"                {line}\n")
                    out_enum_file.write("\n")
                out_enum_file.write("\n")

            out_enum_file.writelines(
                [
                    "Import detail\n",
                    "-------------\n",
                    "\n",
                    ".. code-block:: python\n",
                    "\n",
                    f"    from {containing_namespace}.{module_name} import {enum_definition.name}\n",
                    "\n",
                    "\n",
                ]
            )
