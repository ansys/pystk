"""Sphinx documentation configuration file."""

from datetime import datetime
import os
import pathlib
import shutil
import subprocess

import sphinx
from sphinx.util import logging
from sphinx.util.display import status_iterator

from ansys_sphinx_theme import (
    ansys_favicon,
    get_version_match,
    pyansys_logo_black,
)

from ansys.stk.core import __version__

# Project information
project = "ansys-stk-core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", "stk.docs.pyansys.com")

# Configure the HTML theme
html_logo = pyansys_logo_black
html_favicon = ansys_favicon
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "PySTK"
html_sidebars = {"**": ["globaltoc.html"]}
html_context = {
    "github_user": "ansys-internal",
    "github_repo": "pystk",
    "github_version": "main",
    "doc_path": "doc/source",
}
html_theme_options = {
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
}
html_static_path = ["_static"]
html_css_files = ["css/highlight.css", "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"]

# Sphinx extensions
extensions = [
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
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
exclude_examples = ["facility-to-satellite-access.py", "solar_panel_tool.py", "stk_tutorial.py", "stk_vgt_tutorial.py"]
exclude_patterns = exclude_examples + ["conf.py", "_static/README.md", "api/generated", "links.rst"]

# Ignore warnings
suppress_warnings = [
    # TODO: Reactivate warnings for duplicated cross-references in documentation
    # https://github.com/ansys-internal/pystk/issues/414
    "ref.python",
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


# Read available Docker images for Windows and Linux
DOCKER_DIR = pathlib.Path(__file__).parent.parent.parent.absolute() / "docker"
WINDOWS_IMAGES, CENTOS_IMAGES, UBUNTU_IMAGES = [
    DOCKER_DIR / path for path in ["windows", "linux/centos", "linux/ubuntu"]
]


def get_images_directories_from_path(path):
    """Get all the Docker images present in the retrieved Path."""
    images = [
        folder.name for folder in path.glob("**/*") if folder.name != path.name and (folder / "Dockerfile").exists()
    ] or ["No images available."]
    images.sort()
    return images


# -- Declare the Jinja context -----------------------------------------------
BUILD_API = True if os.environ.get("BUILD_API", "true") == "true" else False
if not BUILD_API:
    exclude_patterns.extend(["api.rst", "api/**"])

BUILD_EXAMPLES = True if os.environ.get("BUILD_EXAMPLES", "true") == "true" else False
if not BUILD_EXAMPLES:
    exclude_patterns.extend(["examples.rst", "examples/**"])
else:
    extensions.extend(["myst_parser", "nbsphinx"])
    nbsphinx_execute = "always"
    nbsphinx_custom_formats = {
        ".mystnb": ["jupytext.reads", {"fmt": "mystnb"}],
        ".py": ["jupytext.reads", {"fmt": ""}],
    }
    nbsphinx_thumbnails = {
        "examples/hohmann-transfer": "_static/thumbnails/hohmann-transfer.png",
        "examples/lambert-transfer": "_static/thumbnails/lambert-transfer.png",
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
jinja_contexts = {
    "docker_images": {
        "windows_images": get_images_directories_from_path(WINDOWS_IMAGES),
        "linux_images": get_images_directories_from_path(CENTOS_IMAGES),
    },
    "install_guide": {
        "version": f"v{version}" if not version.endswith("dev0") else "main",
    },
    "main_toctree": {
        "build_api": BUILD_API,
        "build_examples": BUILD_EXAMPLES,
    },
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

# -- Linkcheck configuration -------------------------------------------------
user_repo = f"{html_context['github_user']}/{html_context['github_repo']}"
linkcheck_ignore = [f"https://github.com/{user_repo}/*", "https://www.ansys.com/*"]


# -- Sphinx application setup ------------------------------------------------


def copy_examples_files_to_source_dir(app: sphinx.application.Sphinx):
    """
    Copy the examples directory to the source directory of the documentation.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        Sphinx application instance containing the all the doc build configuration.

    """
    SOURCE_EXAMPLES = pathlib.Path(app.srcdir) / "examples"
    if not SOURCE_EXAMPLES.exists():
        SOURCE_EXAMPLES.mkdir(parents=True, exist_ok=True)

    EXAMPLES_DIRECTORY = SOURCE_EXAMPLES.parent.parent.parent / "examples"

    all_examples = list(EXAMPLES_DIRECTORY.glob("**/*.py"))
    examples = [file for file in all_examples if f"{file.name}" not in exclude_examples]

    print(f"BUILDER: {app.builder.name}")

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
    if not OUTPUT_EXAMPLES.exists():
        OUTPUT_EXAMPLES.mkdir(parents=True, exist_ok=True)

    SOURCE_EXAMPLES = pathlib.Path(app.srcdir) / "examples"
    EXAMPLES_DIRECTORY = SOURCE_EXAMPLES.parent.parent.parent / "examples"

    all_examples = list(EXAMPLES_DIRECTORY.glob("**/*.py"))
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
        notebooks = RENDERED_EXAMPLES_DIRECTORY.glob("*.ipynb")

        for notebook in status_iterator(
            notebooks,
            "Rendering notebook as PDF",
            "green",
            len(list(notebooks)),
            verbosity=1,
            stringify_func=(lambda x: x.name),
        ):
            subprocess.run(["quarto", "render", notebook, "--to", "pdf"], check=True)
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
    if BUILD_EXAMPLES:
        app.connect("builder-inited", copy_examples_files_to_source_dir)
        app.connect("build-finished", remove_examples_from_source_dir)
        app.connect("build-finished", copy_examples_to_output_dir)
        #app.connect("build-finished", render_examples_as_pdf)
