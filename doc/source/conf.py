"""Sphinx documentation configuration file."""

from datetime import datetime
import fnmatch
import hashlib
import os
import pathlib
import shutil
import subprocess
import sys
import toml
import xml.etree.ElementTree as ET
import zipfile

import sphinx
from sphinx.util import logging
from sphinx.util.display import status_iterator

from ansys_sphinx_theme import (
    ansys_favicon,
    get_version_match,
)

from ansys.stk import __version__

# Project information
project = "ansys-stk"
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
    "page_assets": {
        "getting-started/install/windows/local": {
            "needs_datatables": True,
        },
        "getting-started/install/linux/local": {
            "needs_datatables": True,
        },
        "user-guide/migration": {
            "needs_datatables": True,
        },
    },
}
html_theme_options = {
    "header_links_before_dropdown": 7,
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
html_css_files = [
    "css/highlight.css",
    "css/search.css",
]
html_js_files = []

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
    "sphinxcontrib.jquery",
    "sphinxcontrib.mermaid"
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
exclude_examples = []
exclude_patterns = exclude_examples + ["conf.py", "_static/README.md", "api/generated", "links.rst", "changelog/*.md"]

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
rst_epilog += links_filepath.read_text(encoding="utf-8")

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
    "https://www.khronos.org/collada/",
    # TODO: Determine a way to link to examples without breaking the linkcheck
    # https://github.com/ansys-internal/pystk/issues/657
    r"../examples/",
    # TODO: changelog links
    # https://github.com/ansys-internal/pystk/issues/706
    f"https://github.com/ansys/{html_context['github_repo']}/*",
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

    file_bytes = filepath.read_bytes()
    for i in range(0, len(file_bytes), 8192):
        sha256_hash.update(file_bytes[i : i + 8192])

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

def read_optional_dependencies_from_pyproject():
    """Read the extra dependencies declared in the project file."""
    pyproject = pathlib.Path(__file__).parent.parent.parent / "pyproject.toml"
    if not pyproject.exists():
        raise ValueError(f"The file {pyproject} does not exist.")

    pyproject_content = toml.loads(pyproject.read_text(encoding="utf-8"))
    optional_dependencies = {
        target: {
            (pkg.split("==")[0] if "==" in pkg else pkg): (pkg.split("==")[1] if "==" in pkg else "latest")
            for pkg in deps
        }
        for target, deps in pyproject_content["project"]["optional-dependencies"].items()
    }

    return optional_dependencies

STATIC_PATH = pathlib.Path(__file__).parent / "_static"
ARTIFACTS_PATH = STATIC_PATH / "artifacts"
ARTIFACTS_WHEEL = ARTIFACTS_PATH / f"{project.replace('-', '_')}-{version}-py3-none-any.whl"
ARTIFACTS_SDIST = ARTIFACTS_PATH / f"{project.replace('-', '_')}-{version}.tar.gz"

WHEELHOUSE_PATH = pathlib.Path().parent / "_static" / "wheelhouse"
if not WHEELHOUSE_PATH.exists():
    linkcheck_ignore.append(r".*/wheelhouse/.*")


jinja_globals = {
    "SUPPORTED_PYTHON_VERSIONS": ["3.11", "3.12", "3.13"],
    "SUPPORTED_PLATFORMS": ["windows", "ubuntu"],
    "PYSTK_VERSION": version,
    "STK_VERSION": "12.10.0",
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
                    for target in ["all", "grpc", "jupyter"]
                }
                for python in jinja_globals["SUPPORTED_PYTHON_VERSIONS"]
            }
            for platform in ["windows", "ubuntu"]
        }
    },
    "optional_dependencies": {"optional_dependencies": read_optional_dependencies_from_pyproject()},
}

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


def read_migration_tables(app: sphinx.application.Sphinx):
    """Convert an XML migration table to a JSON format.

    The final JSON format is as follows:

    .. code-block:: json

        { <old_type_name>:
              {
                  'new_name': <new_type_name>,
                  'members':
                  {
                      <old__name>: <new__name>
                  }
              }
        }

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.

    """
    ROOT_DIR = pathlib.Path(app.srcdir).parent.parent
    TOOLS_DIR = ROOT_DIR / "src" / "ansys" / "stk" / "core" / "tools"
    API_MAPPINGS = TOOLS_DIR / "api_migration_assistant" / "api-mappings"
    if not API_MAPPINGS.exists():
        raise FileNotFoundError(f"API mappings directory not found at {API_MAPPINGS}")
    TABLE_FILES = [file for file in API_MAPPINGS.glob("*.xml") if "internal" not in file.name]

    mappings = {}
    for xml_file in status_iterator(
        TABLE_FILES,
        "Rendering migration table",
        "green",
        len(TABLE_FILES),
        verbosity=1,
        stringify_func=(lambda x: x.name),
    ):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        type_categories = ["enum_type", "class", "interface"]
        for type_category in type_categories:
            type_mappings = root.findall(f'./Mapping[@Category="{type_category}"]')
            for type_mapping in type_mappings:
                type_old_name = type_mapping.get("OldName")
                type_new_name = type_mapping.get("NewName")
                mappings[type_old_name] = {"new_name": type_new_name, "members": {}}

        member_categories = ["enum_value", "method"]
        for member_category in member_categories:
            method_mappings = root.findall(f'./Mapping[@Category="{member_category}"]')
            for method_mapping in method_mappings:
                member_old_name = method_mapping.get("OldName")
                if member_old_name[0] != "_": # Filter out private methods
                    type_old_name = method_mapping.get("ParentScope")
                    member_new_name = method_mapping.get("NewName")
                    if not type_old_name in mappings:
                        mappings[type_old_name] = {"new_name": type_old_name, "members": {}}
                    mappings[type_old_name]["members"][member_old_name] = member_new_name

        jinja_contexts["migration_table"] = {
            "mappings": mappings,
        }

def run_autoapi(app: sphinx.application.Sphinx):
    """
    Run the autoapi script to generate API documentation.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.

    """
    logger = logging.getLogger(__name__)
    logger.info("\nWriting reST files for API documentation...", color="green")

    scritps_dir = pathlib.Path(app.srcdir).parent.parent / "scripts"
    sys.path.append(str(scritps_dir.resolve()))

    from autoapi import autodoc_extensions
    autodoc_extensions()

    logger.info("Done!\n")

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
    app.connect("builder-inited", read_migration_tables)

    if BUILD_API:
        app.connect("builder-inited", run_autoapi)

    if BUILD_EXAMPLES:
        app.connect("builder-inited", copy_examples_files_to_source_dir)
        app.connect("build-finished", remove_examples_from_source_dir)
        app.connect("build-finished", copy_examples_to_output_dir)
        app.connect("build-finished", render_examples_as_pdf)
