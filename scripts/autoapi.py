import ast
import os
from pathlib import Path
import textwrap
from typing import Union


class ManualRSTGenerator:
    def __init__(self, core_namespace, module_dir, doc_dir):
        self.core_namespace = core_namespace
        self.module_dir = module_dir
        self.doc_dir = doc_dir

    def generate_rst_for_manual_modules(self, auto_files):
        auto_file_paths = [Path(f).resolve() for f in auto_files]

        for path in Path(self.module_dir).rglob("*.py"):
            path_resolved = path.resolve()
            is_autofile = any(
                auto_path in path_resolved.parents or auto_path == path_resolved for auto_path in auto_file_paths
            )
            is_internal_file = "internal" in path.parts

            if not is_autofile and not is_internal_file:
                self._generate_rst_for_pymodule(str(path))

    def _wrap_python_code_snippets(self, unformatted_docstring: str):
        lines = unformatted_docstring.splitlines()
        formatted_lines = []

        in_snippet = False
        for line in lines:
            stripped = line.lstrip()
            indent_level = len(line) - len(stripped)

            if not in_snippet and indent_level > 0 and stripped:
                in_snippet = True
                formatted_lines.append(".. code-block:: python\n")
                formatted_lines.append("")

            elif in_snippet and indent_level == 0 and stripped:
                in_snippet = False

            formatted_lines.append(line)

        return "\n".join(formatted_lines).rstrip()

    def _generate_rst_for_pymodule(self, path_to_src_file: Union[str, Path]):
        path_to_src_file = Path(path_to_src_file).resolve()
        module_dir_path = Path(self.module_dir).resolve()
        relative_path = path_to_src_file.relative_to(module_dir_path)

        # DBG: output file should have the same name as the module
        if path_to_src_file.name == "__init__.py" and path_to_src_file.parent == module_dir_path:
            return

        relative_namespace = ".".join(relative_path.with_suffix("").parts).replace(".__init__", "")
        full_namespace = self.core_namespace + relative_namespace
        containing_namespace = ".".join(full_namespace.split(".")[:-1])
        module_name = full_namespace.split(".")[-1]

        out_file_path = Path(self.doc_dir) / relative_path.with_suffix(".rst")
        out_file_path.parent.mkdir(parents=True, exist_ok=True)

        with (
            open(path_to_src_file, "r", encoding="utf-8") as in_file,
            open(out_file_path, "w", encoding="utf-8") as out_file,
        ):
            tree = ast.parse(in_file.read())

            submodules = []
            subpackages = []

            if path_to_src_file.name == "__init__.py":
                for entry in path_to_src_file.parent.iterdir():
                    if entry.is_file() and entry.suffix == ".py" and entry.name != "__init__.py":
                        submodules.append(entry.stem)
                    elif entry.is_dir() and entry.name != "__pycache__":
                        subpackages.append(entry.name)

            type_definitions = [node for node in tree.body if isinstance(node, ast.ClassDef)]
            enums = [
                td
                for td in type_definitions
                if any(getattr(base, "id", "") in ("IntEnum", "IntFlag") for base in td.bases)
            ]
            interfaces = [td for td in type_definitions if td not in enums and td.name.startswith("I")]
            classes = [
                td
                for td in type_definitions
                if td not in enums and not td.name.startswith("_") and td not in interfaces
            ]

            def write_line(lines):
                out_file.writelines([line + "\n" for line in lines])

            write_line(
                [
                    f"The ``{module_name}`` module",
                    "=" * (len(module_name) + 20),
                    "",
                    f".. py:module:: {containing_namespace}.{module_name}",
                    "",
                ]
            )

            if any([subpackages, submodules, interfaces, classes, enums]):
                write_line(["Summary", "-------", "", ".. tab-set::", ""])

                def write_list_tab(title, items, formatter):
                    write_line(
                        [
                            f"    .. tab-item:: {title}",
                            "",
                            "        .. list-table::",
                            "            :header-rows: 0",
                            "            :widths: auto",
                            "",
                        ]
                    )
                    for item in items:
                        write_line([f"            * - {formatter(item)}", ""])

                if subpackages:
                    write_list_tab(
                        "Subpackages", subpackages, lambda sp: f":py:obj:`~{containing_namespace}.{module_name}.{sp}`"
                    )

                if submodules:
                    write_list_tab(
                        "Submodules", submodules, lambda sm: f":py:obj:`~{containing_namespace}.{module_name}.{sm}`"
                    )

                for def_type, defs in [("Interfaces", interfaces), ("Classes", classes), ("Enums", enums)]:
                    if defs:
                        write_list_tab(
                            def_type,
                            defs,
                            lambda d: f":py:class:`~{containing_namespace}.{module_name}.{d.name}`"
                            + (
                                f"\n              - {ast.get_docstring(d).splitlines()[0]}"
                                if ast.get_docstring(d)
                                else ""
                            ),
                        )

            write_line(["Description", "-----------", ""])
            if len(tree.body) > 0 and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Str):
                write_line([tree.body[0].value.s.strip(), ""])

            write_line([f".. py:currentmodule:: {containing_namespace}.{module_name}", "", ".. TABLE OF CONTENTS", ""])

            def write_toc_block(items, symbol, folder_name):
                if items:
                    write_line([".. toctree::", "    :titlesonly:", "    :maxdepth: 1", "    :hidden:", ""])
                    for item in items:
                        write_line([f"     {symbol} {item}<{module_name}/{item}>"])

            write_toc_block(subpackages, "🖿", "subpackage")
            write_toc_block(submodules, "🗎", "submodule")

            if any([classes, interfaces, enums]):
                for def_type, defs in [("Interfaces", interfaces), ("Classes", classes), ("Enums", enums)]:
                    if defs:
                        symbol = {"Interfaces": "", "Classes": "", "Enums": "≔ "}[def_type]
                        write_line([".. toctree::", "    :titlesonly:", "    :maxdepth: 1", "    :hidden:", ""])
                        for d in defs:
                            write_line([f"     {symbol}{d.name}<{module_name}/{d.name}>"])

            for obj in classes + interfaces:
                self._generate_rst_for_pyobj(obj, containing_namespace, module_name, str(out_file_path))
            for enum in enums:
                self._generate_rst_for_pyenum(enum, containing_namespace, module_name, str(out_file_path))

    def _generate_rst_for_pyobj(self, obj_definition, containing_namespace, module_name, module_rst_file_path):
        out_dir = os.path.join(os.path.dirname(module_rst_file_path), module_name)
        out_obj_file_path = os.path.join(out_dir, obj_definition.name + ".rst")
        os.makedirs(out_dir, exist_ok=True)

        fq_name = f"{containing_namespace}.{module_name}.{obj_definition.name}"
        base_classes = ", ".join(base.id for base in obj_definition.bases if hasattr(base, "id"))

        def write_docstring(f, docstring, indent="   "):
            if docstring:
                formatted = self._wrap_python_code_snippets(docstring)
                f.write(textwrap.indent(formatted, indent) + "\n\n")

        def write_summary_table(f, title, items, ref_type):
            if not items:
                return
            f.writelines(
                [
                    ".. tab-set::\n\n",
                    f"    .. tab-item:: {title}\n\n",
                    "        .. list-table::\n",
                    "            :header-rows: 0\n",
                    "            :widths: auto\n\n",
                ]
            )
            for item in items:
                f.write(f"            * - :py:{ref_type}:~{fq_name}.{item.name}\n")
                doc = ast.get_docstring(item)
                if doc:
                    f.write(f"              - {doc.splitlines()[0]}\n")
            f.write("\n")

        def parse_args(method):
            args = []
            defaults = list(method.args.defaults or [])
            default_offset = len(method.args.args) - len(defaults)

            for i, arg in enumerate(method.args.args):
                arg_str = arg.arg
                if arg.annotation and hasattr(arg.annotation, "id"):
                    arg_str += f": {arg.annotation.id}"
                if i >= default_offset and defaults:
                    default = defaults[i - default_offset]
                    if isinstance(default, ast.Constant):
                        arg_str += f" = {default.value!r}"
                args.append(arg_str)
            return ", ".join(args)

        def parse_return_type(node):
            if isinstance(node, ast.Constant):
                return "None"
            if node and hasattr(node, "id"):
                return node.id
            return ""

        with open(out_obj_file_path, "w", encoding="utf-8") as f:
            f.writelines(
                [
                    f"{obj_definition.name}\n",
                    "=" * len(obj_definition.name) + "\n\n",
                    f".. py:class:: {fq_name}\n\n",
                    f"   {base_classes}\n\n",
                ]
            )
            write_docstring(f, ast.get_docstring(obj_definition))
            f.write(f".. py:currentmodule:: {obj_definition.name}\n\n\n")

            methods = [m for m in obj_definition.body if isinstance(m, ast.FunctionDef) and not m.name.startswith("_")]
            props = [m for m in methods if any(getattr(d, "id", None) == "property" for d in m.decorator_list)]
            setters = [m for m in methods if any(getattr(d, "attr", None) == "setter" for d in m.decorator_list)]
            methods = [m for m in methods if m not in props and m not in setters]

            if props or methods:
                f.write("Overview\n--------\n\n")
            write_summary_table(f, "Methods", methods, "attr")
            write_summary_table(f, "Properties", props, "attr")

            f.writelines(
                [
                    "Import detail\n-------------\n\n",
                    ".. code-block:: python\n\n",
                    f"    from {containing_namespace}.{module_name} import {obj_definition.name}\n\n\n",
                ]
            )

            if props:
                f.write("Property detail\n---------------\n\n")
                for p in props:
                    ret_type = parse_return_type(p.returns)
                    f.writelines(
                        [
                            f".. py:property:: {p.name}\n",
                            f"    :canonical: {fq_name}.{p.name}\n",
                            f"    :type: {ret_type}\n\n",
                        ]
                    )
                    write_docstring(f, ast.get_docstring(p), "    ")

            if methods:
                f.write("Method detail\n-------------\n\n")
                for m in methods:
                    arg_str = parse_args(m)
                    ret_type = parse_return_type(m.returns)
                    f.writelines(
                        [
                            f".. py:method:: {m.name}({arg_str})",
                            f"{' -> ' + ret_type if ret_type else ''}\n",
                            f"    :canonical: {fq_name}.{m.name}\n\n",
                        ]
                    )
                    write_docstring(f, ast.get_docstring(m), "    ")

                    args_with_types = [
                        (a.arg, a.annotation.id)
                        for a in m.args.args
                        if a.annotation and hasattr(a.annotation, "id") and a.arg != "self"
                    ]
                    if args_with_types:
                        f.write("    :Parameters:\n\n")
                        for arg, type_hint in args_with_types:
                            f.write(f"    **{arg}** : :obj:~{type_hint}\n")
                        f.write("\n")

                    if ret_type:
                        f.writelines(
                            [
                                "    :Returns:\n\n",
                                f"        :obj:~{ret_type}\n\n",
                            ]
                        )

            f.write("\n")

    def _generate_rst_for_pyenum(self, enum_def, namespace, module_name, module_rst_path):
        output_dir = os.path.join(os.path.dirname(module_rst_path), module_name)
        os.makedirs(output_dir, exist_ok=True)

        out_path = os.path.join(output_dir, f"{enum_def.name}.rst")
        with open(out_path, "w", encoding="utf-8") as f:
            # Header and class declaration
            f.writelines(
                [
                    f"{enum_def.name}\n",
                    f"{'=' * len(enum_def.name)}\n\n",
                    f".. py:class:: {namespace}.{module_name}.{enum_def.name}\n\n",
                    f"   {', '.join(base.id for base in enum_def.bases)}\n\n",
                ]
            )

            # Class docstring
            docstring = ast.get_docstring(enum_def)
            if docstring:
                f.write(f"{textwrap.indent(docstring, '   ')}\n\n")

            # Set current module context
            f.writelines([f".. py:currentmodule:: {enum_def.name}\n\n\n"])

            # Extract enum members and their docstrings
            members = []
            for i, node in enumerate(enum_def.body):
                if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
                    name = node.targets[0].id
                    value = node.value.value if isinstance(node.value, ast.Constant) else None
                    doc = None
                    if i + 1 < len(enum_def.body):
                        next_node = enum_def.body[i + 1]
                        if isinstance(next_node, ast.Expr) and isinstance(next_node.value, ast.Constant):
                            doc = next_node.value.value
                    members.append({"name": name, "value": value, "doc": doc})

            # Render enum member table if present
            if members:
                f.writelines(
                    [
                        "Overview\n",
                        "--------\n\n",
                        ".. tab-set::\n\n",
                        "    .. tab-item:: Members\n\n",
                        "        .. list-table::\n",
                        "            :header-rows: 0\n",
                        "            :widths: auto\n\n",
                    ]
                )
                for m in members:
                    f.write(f"            * - :py:attr:~{m['name']}\n")
                    if m["doc"]:
                        lines = m["doc"].splitlines()
                        f.write(f"              - {lines[0]}\n")
                        for line in lines[1:]:
                            f.write(f"                {line}\n")
                f.write("\n")

            # Import statement
            f.writelines(
                [
                    "Import detail\n",
                    "-------------\n\n",
                    ".. code-block:: python\n\n",
                    f"    from {namespace}.{module_name} import {enum_def.name}\n\n\n",
                ]
            )


def main():
    namespace = "ansys.stk.extensions"
    module_path = Path(__file__).resolve().parent.parent / "extensions" / "src" / "ansys" / "stk"
    doc_path = Path(__file__).resolve().parent.parent / "doc" / "source" / "api" / "ansys" / "stk"

    auto_files = list(module_path.rglob("*.py"))  # ensure it's a list
    auto_files = []
    autoapi = ManualRSTGenerator(namespace, module_path, doc_path)
    autoapi.generate_rst_for_manual_modules([])


if __name__ == "__main__":
    main()
