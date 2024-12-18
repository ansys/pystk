"""Sphinx documentation configuration file."""

from datetime import datetime
import fnmatch
import hashlib
import os
import pathlib
import shutil
import subprocess
import xml.etree.ElementTree as ET
import zipfile

import sphinx
from sphinx.util import logging
from sphinx.util.display import status_iterator
from sphinx.errors import NoUri

from ansys_sphinx_theme import (
    ansys_favicon,
    get_version_match,
)

from ansys.stk.core import __version__

# Project information
project = "ansys-stk-core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", "stk.docs.pyansys.com")

# Configure the HTML theme
html_favicon = ansys_favicon
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "PySTK"
html_context = {
    "github_user": "ansys-internal",
    "github_repo": "pystk",
    "github_version": "main",
    "doc_path": "doc/source",
    "version": "main" if version.endswith("dev0") else f"release/{version.split('.')[:-1]}",
    "base_url": f"https://github.com/ansys-internal/pystk/blob/main",
    "edit_page_provider_name": "GitHub",
    "edit_page_url_template": "{{ base_url }}/{{ 'doc/source/' if 'examples/' not in file_name else '' }}{{ file_name }}",
}
html_theme_options = {
    "header_links_before_dropdown": 6,
    "github_url": "https://github.com/ansys-internal/pystk",
    "show_prev_next": True,
    "show_breadcrumbs": True,
    "use_edit_page_button": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
    "check_switcher": False,
    "navigation_with_keys": True,
    "logo": "pyansys",
    "static_search": {
        "limit": 10,
        "minMatchCharLength": 2,
    },
}
html_static_path = ["_static"]
html_css_files = ["css/highlight.css"]

# Sphinx extensions
extensions = [
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_jinja",
    "numpydoc",
    "nbsphinx",
    "myst_parser",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = set()  # numpydoc validation is turned off due to performance (see PR#44)
# numpydoc_validation_checks = {
#    "GL06",  # Found unknown section
#    "GL07",  # Sections are in the wrong order.
#    # "GL08",  # The object does not have a docstring
#    "GL09",  # Deprecation warning should precede extended summary
#    "GL10",  # reST directives {directives} must be followed by two colons
#    "SS01",  # No summary found
#    # "SS02",  # Summary does not start with a capital letter
#    # "SS03", # Summary does not end with a period
#    # "SS04",  # Summary contains heading whitespaces
#    # "SS05", # Summary must start with infinitive verb, not third person
#    "RT02",  # The first line of the Returns section should contain only the
#    # type, unless multiple values are being returned"
# }


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Directories excluded when looking for source files
exclude_examples = ["solar_panel_tool.py", "stk_tutorial.py", "stk_vgt_tutorial.py"]
exclude_patterns = exclude_examples + ["conf.py", "_static/README.md", "api/generated", "links.rst"]

# Ignore warnings
suppress_warnings = [
    # TODO: Reactivate warnings for duplicated cross-references in documentation
    # https://github.com/ansys-internal/pystk/issues/414
    "ref.python",
    # Sphinx-design downloads some font-awesome icons that conflict with the
    # ones in pydata-sphinx-theme.
    "design.fa-build",
    # If Jinja is used to skip the rendering of the examples and the API reference,
    # Sphinx design complains about the indentation of these cards.
    "design.grid",
    # Some pages, like the API reference, follow a template. This template
    # contains some sections for every object. Because multiple objects are
    # documented, the same sections repeat across the documentation, fooling
    # `autosectionlabel` into thinking that the same section is being repeated.
    "autosectionlabel.*",
]

# The suffix(es) of source filenames
source_suffix = {
    ".rst": "restructuredtext",
    ".mystnb": "jupyter_notebook",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# Common content for every RST file such us links
rst_epilog = ""
links_filepath = pathlib.Path(__file__).parent.absolute() / "links.rst"
with open(links_filepath) as links_file:
    rst_epilog += links_file.read()

# -- Autosectionlabel configuration ------------------------------------------
autosectionlabel_maxdepth = 6


# -- Linkcheck configuration -------------------------------------------------
user_repo = f"{html_context['github_user']}/{html_context['github_repo']}"
linkcheck_ignore = [
    "https://www.ansys.com/*",
    # Requires sign-in
    f"https://github.com/{user_repo}/*",
    "https://support.agi.com/3d-models",
    "https://support.agi.com/downloads",
]

# -- Declare the Jinja context -----------------------------------------------
BUILD_API = True if os.environ.get("BUILD_API", "true") == "true" else False
if not BUILD_API:
    exclude_patterns.extend(["api/**"])

BUILD_EXAMPLES = True if os.environ.get("BUILD_EXAMPLES", "true") == "true" else False
if not BUILD_EXAMPLES:
    exclude_patterns.extend(["examples/**"])
else:
    extensions.extend(["myst_parser", "nbsphinx"])
    nbsphinx_execute = "always"
    nbsphinx_custom_formats = {
        ".mystnb": ["jupytext.reads", {"fmt": "mystnb"}],
        ".py": ["jupytext.reads", {"fmt": ""}],
    }
    nbsphinx_prompt_width = ""
    nbsphinx_prolog = """

.. grid:: 3 
    :gutter: 1

    .. grid-item::
        :child-align: center
    
        .. button-link:: {cname_pref}/{python_file_loc}
           :color: primary
           :shadow:
        
            Download as Python script :fab:`python`

    .. grid-item::
        :child-align: center

        .. button-link:: {cname_pref}/{ipynb_file_loc}
           :color: primary
           :shadow:
        
            Download as Jupyter notebook :fas:`book`

    .. grid-item::
        :child-align: center

        .. button-link:: {cname_pref}/{pdf_file_loc}
           :color: primary
           :shadow:
        
            Download as PDF document :fas:`file-pdf`

----
    
    """.format(
        cname_pref=f"https://{cname}/version/{get_version_match(version)}",
        python_file_loc="{{ env.docname }}.py",
        ipynb_file_loc="{{ env.docname }}.ipynb",
        pdf_file_loc="{{ env.docname }}.pdf",
    )


# -- Jinja context configuration ---------------------------------------------


def zip_directory(directory_path: pathlib.Path, zip_filename: pathlib.Path, ignore_patterns=None):
    """Compress a directory using ZIP.

    Parameters
    ----------
    directory_path : ~pathlib.Path
        Directory to compress.
    zip_filename : ~pathlib.Path
        Output file path.
    ignore_patterns : list
        List of Unix-like pattern to ignore.

    """
    if ignore_patterns is None:
        ignore_patterns = []

    if not zip_filename.suffix == ".zip":
        zip_filename = zip_filename.with_suffix(".zip")

    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in directory_path.rglob("*"):
            if file_path.is_file():
                if any(fnmatch.fnmatch(file_path.relative_to(directory_path), pattern) for pattern in ignore_patterns):
                    continue

                relative_path = file_path.relative_to(directory_path)
                zipf.write(file_path, relative_path)


def get_sha256_from_file(filepath: pathlib.Path):
    """Compute the SHA-256 for a file.

    Parameters
    ----------
    filepath : ~pathlib.Path
        Desired file.

    Returns
    -------
    str
        String representing the SHA-256 hash.

    """
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as file:
        while chunk := file.read(8192):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def get_file_size_in_mb(file_path):
    """
    Compute the size of a file in megabytes.

    Parameters
    ----------
    file_path : str or Path
        The path to the file whose size is to be computed.

    Returns
    -------
    float
        The size of the file in megabytes.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    OSError
        If an OS-related error occurs while accessing the file.

    """
    path = pathlib.Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    file_size_bytes = path.stat().st_size
    return file_size_bytes / (1024 * 1024)


STATIC_PATH = pathlib.Path(__file__).parent / "_static"
ARTIFACTS_PATH = STATIC_PATH / "artifacts"
ARTIFACTS_WHEEL = ARTIFACTS_PATH / f"{project.replace('-', '_')}-{version}-py3-none-any.whl"
ARTIFACTS_SDIST = ARTIFACTS_PATH / f"{project.replace('-', '_')}-{version}.tar.gz"

WHEELHOUSE_PATH = pathlib.Path().parent / "_static" / "wheelhouse"
if not WHEELHOUSE_PATH.exists():
    linkcheck_ignore.append(r".*/wheelhouse/.*")


MIGRATION_TABLES = STATIC_PATH / "migration-tables"

def migration_table_to_dict(migration_table):
    """Convert an XML migration table to a dictionary."""

    print(migration_table, flush=True)

    table = {
        "module": migration_table.name[:-4],
        "interfaces": {},
        "classes": {},
        "enums": {},
    }

    root = ET.parse(migration_table).getroot()

    # Interfaces
    for interface in root.findall('./Mapping[@Category="interface"]'):
        table["interfaces"][interface.get("OldName")] = {
            "new_name": interface.get("NewName"),
            "methods": {},
            "properties": {},
        }

    # Classes
    for klass in root.findall('./Mapping[@Category="class"]'):
        table["classes"][klass.get("OldName")] = {
            "new_name": klass.get("NewName"),
            "methods": {},
            "properties": {},
        }

    # Methods and properties
    for method in root.findall('./Mapping[@Category="method"]'):
        is_interface_method = method.get("ParentScope") in table["interfaces"]
        category = "interfaces" if is_interface_method else "classes"
        parent = method.get("ParentScope")

        table[category][parent]["methods"][method.get("OldName")] = method.get("NewName")

    # Enums
    for enum in root.findall('./Mapping[@Category="enum_type"]'):
        table["enums"][enum.get("OldName")] = {
            "new_name": enum.get("NewName"),
            "values": {},
        }

    # Enum values
    for enum_value in root.findall('./Mapping[@Category="enum_value"]'):
        parent = enum_value.get("ParentScope")
        table["enums"][parent]["values"][enum_value.get("OldName")] = enum_value.get("NewName")

    return table
    



    

# table = {
#     "module": ...,
#     "interfaces": [
#         {
#             "name": ...,
#             "new_name": ...,
#             "properties": [
#                 {
#                     "name": ...,
#                     "new_name": ...,
#                 }
#             ],
#             "methods": [
#                 {
#                     "name": ...,
#                     "new_name": ...,
#                 }
#             ],
#         },    
#     ],
#     "classes": ...,
#     "enums": ...,
# }





jinja_globals = {
    "SUPPORTED_PYTHON_VERSIONS": ["3.11", "3.12", "3.13"],
    "SUPPORTED_PLATFORMS": ["windows", "ubuntu"],
    "PYSTK_VERSION": version,
    "STK_VERSION": "12.9.0",
}

jinja_contexts = {
    "toxenvs": {
        "envs": subprocess.run(["tox", "list", "-d", "-q"], capture_output=True, text=True).stdout.splitlines()[1:],
    },
    "main_toctree": {
        "build_api": BUILD_API,
        "build_examples": BUILD_EXAMPLES,
    },
    "artifacts": {
        "wheels": ARTIFACTS_WHEEL.name,
        "wheels_size": f"{get_file_size_in_mb(ARTIFACTS_WHEEL):.2f} MB",
        "wheels_hash": get_sha256_from_file(ARTIFACTS_WHEEL),
        "source": ARTIFACTS_SDIST.name,
        "source_size": f"{get_file_size_in_mb(ARTIFACTS_SDIST):.2f} MB",
        "source_hash": get_sha256_from_file(ARTIFACTS_SDIST),
    },
    # NOTE: wheelhouse artifacts are only available during CI/CD runs
    "wheelhouse": {
        "wheelhouse": {
            platform: {
                python: {
                    target: WHEELHOUSE_PATH / f"{project}-v{version}-{target}-wheelhouse-{platform}-latest-{python}"
                    for target in ["all", "grpc", "visualization"]
                }
                for python in jinja_globals["SUPPORTED_PYTHON_VERSIONS"]
            }
            for platform in ["windows", "ubuntu"]
        }
    },
    "oldapi": {
        "tables": list(map(migration_table_to_dict, list(MIGRATION_TABLES.glob("*.xml")))),
    },
}

print(jinja_contexts["wheelhouse"]["wheelhouse"])

# -- autodoc configuration ---------------------------------------------------
autodoc_default_options = {
    #'members': 'var1, var2',
    "member-order": "alphabetical",
    #'special-members': '__init__',
    "show-inheritance": True,
    "undoc-members": True,
    #'exclude-members': '__weakref__'
}
autodoc_class_signature = "separated"
autodoc_mock_imports = ["tkinter"]

# -- MyST Sphinx configuration -----------------------------------------------
myst_heading_anchors = 3

# -- LaTeX configuration
latex_elements = {
    "extraclassoptions": "openany,oneside",
}

# -- Sphinx application setup ------------------------------------------------


def copy_docker_files_to_static_dir(app: sphinx.application.Sphinx):
    """
    Copy the examples directory to the source directory of the documentation.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.

    """
    SOURCE_DIR = pathlib.Path(app.srcdir)
    DOCKER_DIR = SOURCE_DIR.parent.parent / "docker"
    STATIC_DOCKER_DIR = SOURCE_DIR / "_static" / "docker"
    if not STATIC_DOCKER_DIR.exists():
        STATIC_DOCKER_DIR.mkdir()

    COMPRESSED_DOCKER_WINDOWS_IMAGES = STATIC_DOCKER_DIR / "windows.zip"
    COMPRESSED_DOCKER_LINUX_IMAGES = STATIC_DOCKER_DIR / "linux.zip"

    logger = logging.getLogger(__name__)

    logger.info(f"\nCompressing Docker images...")
    zip_directory(DOCKER_DIR / "windows", COMPRESSED_DOCKER_WINDOWS_IMAGES, ignore_patterns=["*.tgz"])
    zip_directory(DOCKER_DIR / "linux", COMPRESSED_DOCKER_LINUX_IMAGES, ignore_patterns=["*.tgz"])

    # Add the new files and their information to the Jinja context. This
    # operation can not be performed outside of this function since the compressed files do not yet exist.

    DOCKER_RECIPES = SOURCE_DIR / "_static" / "docker"
    DOCKER_RECIPES_WINDOWS = DOCKER_RECIPES / "windows.zip"
    DOCKER_RECIPES_LINUX = DOCKER_RECIPES / "linux.zip"

    jinja_contexts["docker_images"] = {
        "docker_recipes_windows": DOCKER_RECIPES_WINDOWS.name,
        "docker_recipes_windows_size": f"{get_file_size_in_mb(DOCKER_RECIPES_WINDOWS):.2f} MB",
        "docker_recipes_windows_hash": f"{get_sha256_from_file(DOCKER_RECIPES_WINDOWS)}",
        "docker_recipes_linux": DOCKER_RECIPES_LINUX.name,
        "docker_recipes_linux_size": f"{get_file_size_in_mb(DOCKER_RECIPES_LINUX):.2f} MB",
        "docker_recipes_linux_hash": f"{get_sha256_from_file(DOCKER_RECIPES_LINUX)}",
    }


def copy_examples_to_output_dir(app: sphinx.application.Sphinx, exception: Exception):
    """
    Copy the examples directory to the output directory of the documentation.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.
    exception : Exception
        Exception encountered during the building of the documentation.

    """
    # TODO: investigate issues when using OUTPUT_EXAMPLES instead of SOURCE_EXAMPLES
    # https://github.com/ansys-internal/pystk/issues/415
    OUTPUT_EXAMPLES = pathlib.Path(app.outdir) / "examples"
    OUTPUT_IMAGES = OUTPUT_EXAMPLES / "img"
    for directory in [OUTPUT_EXAMPLES, OUTPUT_IMAGES]:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)

    SOURCE_EXAMPLES = pathlib.Path(app.srcdir) / "examples"
    EXAMPLES_DIRECTORY = SOURCE_EXAMPLES.parent.parent.parent / "examples"
    IMAGES_DIRECTORY = EXAMPLES_DIRECTORY / "img"

    # Copyt the examples
    all_examples = list(EXAMPLES_DIRECTORY.glob("*.py"))
    examples = [file for file in all_examples if f"{file.name}" not in exclude_examples]
    for file in status_iterator(
        examples,
        f"Copying example to doc/_build/examples/",
        "green",
        len(examples),
        verbosity=1,
        stringify_func=(lambda x: x.name),
    ):
        destination_file = OUTPUT_EXAMPLES / file.name
        destination_file.write_text(file.read_text(encoding="utf-8"), encoding="utf-8")

    # Copy the static images
    images = list(IMAGES_DIRECTORY.glob("*.png"))
    for file in status_iterator(
        images,
        f"Copying image to doc/source/examples/img",
        "green",
        len(images),
        verbosity=1,
        stringify_func=(lambda file: file.name),
    ):
        destination_file = OUTPUT_IMAGES / file.name
        destination_file.write_bytes(file.read_bytes())


def copy_examples_files_to_source_dir(app: sphinx.application.Sphinx):
    """
    Copy the examples directory to the source directory of the documentation.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.

    """
    SOURCE_EXAMPLES = pathlib.Path(app.srcdir) / "examples"
    SOURCE_IMAGES = SOURCE_EXAMPLES / "img"
    for directory in [SOURCE_EXAMPLES, SOURCE_IMAGES]:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)

    EXAMPLES_DIRECTORY = SOURCE_EXAMPLES.parent.parent.parent / "examples"
    IMAGES_DIRECTORY = EXAMPLES_DIRECTORY / "img"

    # Copy the the examples
    all_examples = list(EXAMPLES_DIRECTORY.glob("*.py"))
    examples = [file for file in all_examples if f"{file.name}" not in exclude_examples]
    for file in status_iterator(
        examples,
        f"Copying example to doc/source/examples/",
        "green",
        len(examples),
        verbosity=1,
        stringify_func=(lambda file: file.name),
    ):
        destination_file = SOURCE_EXAMPLES / file.name
        destination_file.write_text(file.read_text(encoding="utf-8"), encoding="utf-8")

    # Copy the static images
    images = list(IMAGES_DIRECTORY.glob("*.png"))
    for file in status_iterator(
        images,
        f"Copying image to doc/source/examples/img",
        "green",
        len(images),
        verbosity=1,
        stringify_func=(lambda file: file.name),
    ):
        destination_file = SOURCE_IMAGES / file.name
        destination_file.write_bytes(file.read_bytes())


def remove_examples_from_source_dir(app: sphinx.application.Sphinx, exception: Exception):
    """
    Remove the example files from the documentation source directory.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.
    exception : Exception
        Exception encountered during the building of the documentation.

    """
    EXAMPLES_DIRECTORY = pathlib.Path(app.srcdir) / "examples"
    logger = logging.getLogger(__name__)
    logger.info(f"\nRemoving {EXAMPLES_DIRECTORY} directory...")
    shutil.rmtree(EXAMPLES_DIRECTORY)


def render_examples_as_pdf(app: sphinx.application.Sphinx, exception: Exception):
    """
    Render notebook examples as PDF files using Quarto.

    Quarto needs to be installed in the system to render the PDF files. See
    https://quarto.org/docs/get-started/.
    Artifact

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.
    exception : Exception
        Exception encountered during the building of the documentation.

    """
    try:
        SOURCE_EXAMPLES = pathlib.Path(app.srcdir) / "examples"
        RENDERED_EXAMPLES_DIRECTORY = SOURCE_EXAMPLES.parent.parent / "_build" / "html" / "examples"
        notebooks = list(RENDERED_EXAMPLES_DIRECTORY.glob("*.ipynb"))

        for notebook in status_iterator(
            notebooks,
            "Rendering notebook as PDF",
            "green",
            len(notebooks),
            verbosity=1,
            stringify_func=(lambda x: x.name),
        ):
            subprocess.run(
                [
                    "quarto",
                    "render",
                    notebook,
                    "--to",
                    "pdf",
                    "-M",
                    f"author:{author}",
                    "-M",
                    "highlight-style:pygments",
                ],
                check=True,
            )
    except FileNotFoundError:
        logger = logging.getLogger(__name__)
        logger.warning(
            "Quarto is not installed in the system. PDF files will not be rendered. \
            See https://quarto.org/docs/get-started/"
        )


def setup(app: sphinx.application.Sphinx):
    """
    Run different hook functions during the documentation build.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.

    """
    # HACK: rST files are copied to the doc/source directory before the build.
    # Sphinx needs all source files to be in the source directory to build.
    # However, the examples are desired to be kept in the root directory. Once the
    # build has completed, no matter its success, the examples are removed from
    # the source directory.
    app.connect("builder-inited", copy_docker_files_to_static_dir)
    if BUILD_EXAMPLES:
        app.connect("builder-inited", copy_examples_files_to_source_dir)
        app.connect("build-finished", remove_examples_from_source_dir)
        app.connect("build-finished", copy_examples_to_output_dir)
        app.connect("build-finished", render_examples_as_pdf)
