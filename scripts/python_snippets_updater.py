"""Provide a utility that makes the corresponding changes to doc and source files when code snippets are added, deleted, or modified."""

import _ast
import ast
import inspect
import logging
from pathlib import Path
import re
import stat
import textwrap

import libcst


class SnippetsParser(object):
    """A utility for parsing PySTK code snippets."""

    def __init__(self, doc_snippets_dir):
        self.doc_snippets_dir = doc_snippets_dir
        self.all_snippets = []

    def parse_all_snippets(self):
        """Parse and return a representation of the PySTK code snippets."""
        for file in list(self.doc_snippets_dir.rglob("*_snippets.py")):
            with Path.open(file, "r") as in_file:
                tree = ast.parse(in_file.read())
                in_file.seek(0)
                file_content = in_file.readlines()
                snippet_class_definitions = [
                    type_defintion for type_defintion in tree.body if isinstance(type_defintion, _ast.ClassDef)
                ]
                for snippet_class_definition in snippet_class_definitions:
                    all_funcs = [n for n in snippet_class_definition.body if isinstance(n, ast.FunctionDef)]
                    snippets = [
                        func
                        for func in all_funcs
                        if len(
                            [
                                dec
                                for dec in func.decorator_list
                                if isinstance(dec, ast.Call)
                                and hasattr(dec.func, "id")
                                and dec.func.id == "code_snippet"
                            ]
                        )
                        != 0
                    ]
                    for snippet in reversed(snippets):
                        body = []
                        for i in range(snippet.lineno, snippet.end_lineno):
                            line = file_content[i]
                            if line.startswith("        "):
                                line = line[
                                    len("        ") :
                                ]  # remove 2 left indentations due to being inside a test in the Python file
                            body.append(line.rstrip())

                        snippet_decorator = [
                            dec
                            for dec in snippet.decorator_list
                            if isinstance(dec, ast.Call) and dec.func.id == "code_snippet"
                        ][0]
                        decorator_attrs = {kw.arg: kw.value.value for kw in snippet_decorator.keywords}

                        snippet_repr = {
                            "name": decorator_attrs["name"],
                            "description": decorator_attrs["description"],
                            "category": decorator_attrs["category"],
                            "eid": decorator_attrs["eid"],
                            "body": "\n".join(body),
                        }
                        self.all_snippets.append(snippet_repr)
        return self.all_snippets


class SnippetsRSTGenerator(object):
    """A utility for generating an rST documentation file with all of the PySTK code snippets."""

    def __init__(self, all_snippets, destination):
        self.all_snippets = all_snippets
        self.destination = destination

    def _build_snippet_tree(self):
        snippet_tree = {"sub_cats": {}, "snippets": []}
        for snip in self.all_snippets:
            category_parts = [subcat.strip() for subcat in snip["category"].split("|")]
            current_level = snippet_tree
            for category_part in category_parts:
                if category_part not in current_level["sub_cats"]:
                    current_level["sub_cats"][category_part] = {"sub_cats": {}, "snippets": []}
                current_level = current_level["sub_cats"][category_part]
            current_level["snippets"].append({"description": snip["description"], "name": snip["name"]})
        return snippet_tree

    def _write_snippet_tree(self, out_file, tree, indentation):
        sub_cats = tree["sub_cats"].keys()
        for node_name in sub_cats:
            out_file.write(indentation * " " + node_name + "\n")
            self._write_snippet_tree(out_file, tree["sub_cats"][node_name], indentation + 2)
        if len(sub_cats) and len(tree["snippets"]) > 0:
            out_file.write(
                "\n"
            )  # Required by Sphinx to avoid warning: Block quote ends without a blank line; unexpected unindent.
        for snippet in tree["snippets"]:
            out_file.write(
                "{}- :ref:`{} <{}>`\n".format(indentation * " ", snippet["description"].capitalize(), snippet["name"])
            )

    def write_rst(self):
        """Output the rST file for this generator's representation of the PySTK code snippets."""
        if not Path.exists(Path(self.destination).parent):
            Path.mkdir(Path(self.destination).parent, parents=True)

        Path.chmod(self.destination, stat.S_IWRITE)
        with Path.open(self.destination, "w") as out_file:
            rst_header = textwrap.dedent(
                """
            PySTK code snippets
            ###################

            The following code snippets demonstrate tasks that are commonly encountered when working with the PySTK API.

            How do I
            ========

            """
            )
            out_file.write(rst_header.lstrip())

            snippet_tree = self._build_snippet_tree()
            for top_level in snippet_tree["sub_cats"].keys():
                out_file.write(top_level + "\n")
                self._write_snippet_tree(out_file, snippet_tree["sub_cats"][top_level], 2)

            out_file.write("\n")

            for snippet in self.all_snippets:
                description = snippet["description"].capitalize()

                # Substitutions to make vale happy
                vale_substitutions = {
                    "2d": "2D",
                    "3d": "3D",
                    "advcat": "AdvCat",
                    "astrogator": "Astrogator",
                    "azel": "AzEl",
                    "cartesian": "Cartesian",
                    "earth": "Earth",
                    "euler": "Euler",
                    "hpop": "HPOP",
                    "mcs": "MCS",
                    "mto": "MTO",
                    "stk engine": "STK Engine",
                    "stk": "STK",
                    "vgt": "VGT",
                    "ypr": "YPR",
                }
                ored_substitutions = "|".join(vale_substitutions)
                description = re.sub(rf"\b({ored_substitutions})\b", lambda s: vale_substitutions[s[1]], description)

                snippet_format = """
                .. _{}:
                
                {}
                {}

                .. code-block:: python
                    
                {}
                """
                out_file.write(
                    textwrap.dedent(snippet_format).format(
                        snippet["name"],
                        description,
                        len(snippet["description"]) * "=",
                        textwrap.indent(snippet["body"], "    "),
                    )
                )


class SnippetsRSTInjector(object):
    """A utility for making changes to docstrings in .rst files based on the state of the doc_snippets_tests directory."""

    def __init__(self, api_src_dir: Path, api_doc_dir: Path, all_snippets: Path):
        self.api_src_dir = api_src_dir
        self.api_doc_dir = api_doc_dir
        self.all_snippets = all_snippets

        self.class_targets = {}
        self.method_targets = {}
        for snippet in self.all_snippets:
            locations = self._compute_identifying_location_info(snippet)
            content = {"desc": snippet["description"], "code": snippet["body"]}

            for location in locations:
                if ".rst:" in location:
                    self.method_targets.setdefault(location, []).append(content)
                else:
                    self.class_targets.setdefault(location, []).append(content)

    def _format_class_examples(self, filename):
        if filename in self.class_targets.keys():
            all_examples = ""
            for content in self.class_targets[filename]:
                all_examples += content["desc"] + "\n\n"
                all_examples += ".. code-block:: python\n\n"
                all_examples += textwrap.indent(content["code"], "    ") + "\n\n\n"

            return f"""Examples\n--------\n\n{all_examples}"""

        return ""

    def inject_class_docstrings(self):
        """Update class docstring examples in .rst files."""
        for filename in self.api_doc_dir.rglob("*.rst"):
            with Path.open(filename, "r") as in_file:
                original_content = in_file.read()

            matched = re.match(r"([\S\s]*)(Examples\n--------[\S\s]*?)(Import detail[\S\s]*)", original_content)

            if matched:
                with Path.open(filename, "w") as out_file:
                    out_file.seek(0)
                    out_file.write(matched.group(1))
                    out_file.write(self._format_class_examples(str(filename)))
                    out_file.write(matched.group(3))
                    out_file.truncate()

    def remove_method_docstring_examples(self):
        """Remove docstring examples from method docstrings in .rst files."""
        for filename in self.api_doc_dir.rglob("*.rst"):
            with Path.open(filename, "r") as in_file:
                original_content = in_file.read()
                in_file.close()

            matched = re.findall(
                r"(?:property::|method::)[\S\s]*?([ \t]*Examples\s*--------[\S\s]*?)(?:\.\. py:|Method detail|$)",
                original_content,
            )

            for method_examples in matched:
                original_content = original_content.replace(method_examples, "")

                with Path.open(filename, "w") as out_file:
                    out_file.seek(0)
                    out_file.write(original_content)
                    out_file.truncate()
                    out_file.close()

    def add_method_docstring_examples(self):
        """Re-add docstring examples to method docstrings in .rst files."""
        for target in self.method_targets:
            print(target)

    #     with Path.open(filename, "r") as in_file:
    #         original_content = in_file.read()

    #     target_location = -1
    #     original_content = []
    #     original_filename = target.rsplit(":", 1)[0]
    #     temp_filename = target.rsplit(":", 1)[0].replace(".rst", "_temp.rst")
    #     with Path.open(original_filename, "r") as in_file:
    #         original_content = in_file.readlines()
    #         member_name = str(target.rsplit(":", 1)[1])
    #         if (".. py:property:: " + member_name + "\n") in original_content:
    #             target_location = original_content.index(".. py:property:: " + member_name + "\n") + 1
    #         else:

    #             def match_till_beginning_of_argument_list(line):
    #                 return line.startswith(".. py:method:: " + member_name + "(")

    #             method_line = [
    #                 line for line in original_content if match_till_beginning_of_argument_list(line)
    #             ][0]
    #             target_location = original_content.index(method_line) + 1

    #         while (
    #             ".. py:method::" not in original_content[target_location]
    #             and ".. py:property::" not in original_content[target_location]
    #         ):
    #             target_location += 1

    #     with Path.open(temp_filename, "w") as out_file:
    #         for line in original_content[:target_location]:
    #             out_file.write(line)

    #         out_file.write("    Examples\n")
    #         out_file.write("    --------\n")

    #         examples_template = """
    #         {}

    #         .. code-block:: python

    #         {}

    #         """
    #         for content in all_content:
    #             out_file.write(
    #                 textwrap.indent(
    #                     textwrap.dedent(examples_template).format(
    #                         content["desc"], textwrap.indent(content["code"], "    ")
    #                     ),
    #                     "    ",
    #                 )
    #             )

    #         out_file.write("\n")
    #         start_writing = False
    #         for line in original_content[target_location:]:
    #             if ".. py:property::" in line or ".. py:method::" in line:
    #                 start_writing = True
    #             if start_writing:
    #                 out_file.write(line)

    def _compute_identifying_location_info(self, snippet_repr):
        unique_locations = snippet_repr["eid"].split("|")

        for i, location in enumerate(unique_locations):
            location_components = location.strip().split("~")
            libname = location_components[0]
            class_name = location_components[1]
            method_name = None if len(location_components) == 2 else location_components[2]

            unique_locations[i] = str(self.api_doc_dir.joinpath(*libname.split("."), class_name).with_suffix(".rst"))
            if method_name is not None:
                unique_locations[i] += ":" + method_name

        return unique_locations


class SnippetsDocstringInjector(libcst.CSTTransformer):
    """A utility for making changes to docstrings in .py files based on the state of the doc_snippets_tests directory."""

    def __init__(self, api_src_dir, all_snippets):
        self.api_src_dir = api_src_dir
        self.all_snippets = all_snippets

        self.docstrings_to_replace = []

        self.local_targets = {}
        self.current_class = None

    def inject(self):
        """Rewrite docstrings in .py files based on the snippets defined in doc_snippets_tests."""
        targets_per_file = {}
        for snippet in self.all_snippets:
            locations = self._compute_identifying_location_info(snippet["eid"])
            content = {"desc": snippet["description"], "code": snippet["body"]}

            for location in locations:
                filename = location.rsplit(":", 1)[0]
                if filename not in targets_per_file.keys():
                    targets_per_file.setdefault(filename, {"method_targets": {}, "class_targets": {}})

                element_name = location.rsplit(":", 1)[1]
                if "." in element_name:
                    targets_per_file[filename]["method_targets"].setdefault(element_name, []).append(content)
                else:
                    targets_per_file[filename]["class_targets"].setdefault(element_name, []).append(content)

        self._transform_modules(targets_per_file)

    def _transform_modules(self, targets_per_file):
        for path_number, path in enumerate(targets_per_file.keys()):
            print(
                f"Checking for updates to docstrings in .py files... file {path_number + 1} of {len(targets_per_file.keys())}."
            )
            self._transform_module(path, targets_per_file[str(path)])

    def _transform_module(self, path: Path, local_targets: dict):
        self.local_targets = local_targets

        new_tree = None
        with Path.open(path, "r") as file:
            source = file.read()
            tree = libcst.parse_module(source)
            new_tree = tree.visit(self)

        with Path.open(path, "w") as file:
            file.write(new_tree.code)

    def visit_FunctionDef(self, node: libcst.FunctionDef) -> bool:
        """Mark method docstrings for change, if needed."""
        scoped_method_name = f"{self.current_class}.{node.name.value}"
        docstring = node.get_docstring()

        if (docstring and "Examples" in docstring) or scoped_method_name in self.local_targets["method_targets"].keys():
            self.docstrings_to_replace.append(f'"""{node.get_docstring(clean=False)}"""')
            self.examples_to_add = self.local_targets["method_targets"].get(scoped_method_name)
            return True

        return False

    def visit_ClassDef(self, node: libcst.ClassDef) -> bool:
        """Mark class docstrings for change, if needed."""
        self.current_class = node.name.value
        docstring = node.get_docstring()

        if "Examples" in docstring or node.name.value in self.local_targets["class_targets"].keys():
            self.docstrings_to_replace.append(f'"""{node.get_docstring(clean=False)}"""')
            self.examples_to_add = self.local_targets["class_targets"].get(node.name.value)
            return True

        return False

    def leave_SimpleString(
        self, original_node: libcst.SimpleString, updated_node: libcst.SimpleString
    ) -> libcst.BaseExpression:
        """Apply docstring changes, according to those that were marked in visits."""
        if original_node.value.lstrip("r") in self.docstrings_to_replace:
            docstring_to_replace = self.docstrings_to_replace.pop(
                self.docstrings_to_replace.index(original_node.value.lstrip("r"))
            )
            docstring_to_replace, indent_lvl = self._remove_and_return_indentation(docstring_to_replace)
            docstring_pattern = r"(r?)(\"\"\")(\s*)(\S[\S\s]*\S)(\s*Examples\s*--------[\S\s]*)?(\"\"\")"

            if self.examples_to_add:
                formatted_snippets = self._format_snippet_content(self.examples_to_add)
                replacement_pattern = r"\4" + formatted_snippets.replace("\\", r"\\")
                new_docstring = re.sub(docstring_pattern, replacement_pattern, docstring_to_replace)
            else:
                replacement_pattern = r"\4"
                new_docstring = re.sub(docstring_pattern, replacement_pattern, docstring_to_replace)

            if "\n" in new_docstring:
                new_docstring = '"""' + textwrap.indent("\n" + new_docstring + '"""', indent_lvl * " ")
            else:
                new_docstring = f'"""{new_docstring}"""'

            if "\\" in new_docstring:
                new_docstring = "r" + new_docstring

            return updated_node.with_changes(value=new_docstring)
        return updated_node

    def _remove_and_return_indentation(self, docstring):
        last_line = docstring.split("\n")[-1]
        indent_lvl = len(last_line) - len(last_line.lstrip())
        return inspect.cleandoc(docstring), indent_lvl

    def _format_snippet_content(self, content):
        formatted_snippets_lines = ["\n", "Examples", "--------"]

        for snip in content:
            formatted_snippets_lines.append(snip["desc"] + ":")
            formatted_snippets_lines.append(">>> " + snip["code"].replace("\n", "\n>>> "))
            formatted_snippets_lines.append("")
        formatted_snippets = "\n".join(formatted_snippets_lines)
        return formatted_snippets

    def _filename_from_eid_component(self, eid_comp):
        libname_path_stem = self.api_src_dir.joinpath(*eid_comp.split("."))
        if libname_path_stem.with_suffix(".py").is_file():
            return libname_path_stem.with_suffix(".py")
        elif libname_path_stem.joinpath("__init__.py").is_file():
            return libname_path_stem.joinpath("__init__.py")
        else:
            raise Warning(f"Library specified in eid does not map to a Python module: {eid_comp}")

    def _compute_identifying_location_info(self, eid):
        unique_locations = eid.split("|")

        for i, location in enumerate(unique_locations):
            location_components = location.strip().split("~")
            filename = self._filename_from_eid_component(location_components[0])
            class_name = location_components[1]
            method_name = None if len(location_components) == 2 else location_components[2]
            unique_locations[i] = f"{filename}:{class_name}"
            if method_name is not None:
                unique_locations[i] += "." + method_name

        return unique_locations


if __name__ == "__main__":
    pystk_root_dir = Path(__file__).parent.parent

    snippets_dir = pystk_root_dir / "tests" / "doc_snippets_tests"
    src_core_dir = pystk_root_dir / "src" / "ansys" / "stk" / "core"
    doc_core_dir = pystk_root_dir / "doc" / "source" / "api" / "ansys" / "stk" / "core"

    combined_snippets_rst_path = pystk_root_dir / "doc" / "source" / "user-guide" / "code-snippets.rst"

    logging.info(f"Parsing PySTK-migrated snippets in {str(snippets_dir)}")
    pystk_snippets_parser = SnippetsParser(doc_snippets_dir=snippets_dir)
    all_snippets = pystk_snippets_parser.parse_all_snippets()
    logging.info(f"Done parsing PySTK-migrated snippets in {str(snippets_dir)}")

    # logging.info("Injecting PySTK-migrated snippets into PySTK docstrings")
    # pystk_snippets_docstring_injector = SnippetsDocstringInjector(api_src_dir=src_core_dir, all_snippets=all_snippets)
    # pystk_snippets_docstring_injector.inject()
    # logging.info("Done injecting PySTK-migrated snippets into PySTK docstrings")

    logging.info("Creating a reStructuredText file with all of the PySTK-migrated snippets")
    pystk_snippets_rst_generator = SnippetsRSTGenerator(
        all_snippets=all_snippets, destination=combined_snippets_rst_path
    )
    pystk_snippets_rst_generator.write_rst()
    logging.info("Done creating a reStructuredText file with all of the PySTK-migrated snippets")

    logging.info("Injecting PySTK-migrated snippets into PySTK Sphinx documentation")
    pystk_snippets_rst_injector = SnippetsRSTInjector(
        api_src_dir=src_core_dir, api_doc_dir=doc_core_dir, all_snippets=all_snippets
    )
    # pystk_snippets_rst_injector.inject_class_docstrings()
    pystk_snippets_rst_injector.remove_method_docstring_examples()
    logging.info("Done injecting PySTK-migrated snippets into PySTK Sphinx documentation")
