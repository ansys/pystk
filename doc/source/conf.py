"""Sphinx documentation configuration file."""
from datetime import datetime
import os
import pathlib

from sphinx.util import logging
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
html_css_files = [
    "css/highlight.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
]

# Sphinx extensions
extensions = [
    "enum_tools.autoenum",
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
numpydoc_validation_checks = (
    set()
)  # numpydoc validation is turned off due to performance (see PR#44)
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
exclude_examples = ["examples/stk_engine/solar_panel_tool.py", "examples/stk_engine/stk_tutorial.py", "examples/stk_engine/stk_vgt_tutorial.py"]
exclude_patterns = exclude_examples + ["conf.py", "_static/README.md", "api/generated", "links.rst"]

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
WINDOWS_IMAGES, LINUX_IMAGES = [
    DOCKER_DIR / path for path in ["windows", "linux"]
]


def get_images_directories_from_path(path):
    """Get all the Docker images present in the retrieved Path."""
    images = [
        folder.name
        for folder in path.glob("**/*")
        if folder.name != path.name and (folder / "Dockerfile").exists()
    ] or ["No images available."]
    images.sort()
    return images


# -- Declare the Jinja context -----------------------------------------------
BUILD_API = True if os.environ.get("BUILD_API", "true") == "true" else False
if not BUILD_API:
    exclude_patterns.append("api")

BUILD_EXAMPLES = (
    True if os.environ.get("BUILD_EXAMPLES", "true") == "true" else False
)
if not BUILD_EXAMPLES:
    exclude_patterns.append("examples/**")
else:
    extensions.extend(["myst_parser", "nbsphinx"])
    nbsphinx_execute = "always"
    nbsphinx_custom_formats = {
        ".mystnb": ["jupytext.reads", {"fmt": "mystnb"}],
        ".py": ["jupytext.reads", {"fmt": ""}],
    }
    nbsphinx_thumbnails = {
        "examples/stk_engine/hohmann_transfer_using_targeter": "_static/thumbnails/hohmann-transfer-using-targeter.png",
    }
    nbsphinx_prompt_width = ""
    nbsphinx_prolog = """

.. grid:: 2 
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

----
    
    """.format(
        cname_pref=f"https://{cname}/version/{get_version_match(version)}",
        python_file_loc="{{ env.docname }}.py",
        ipynb_file_loc="{{ env.docname }}.ipynb",
    )


# -- Jinja context configuration ---------------------------------------------
jinja_contexts = {
    "docker_images": {
        "windows_images": get_images_directories_from_path(WINDOWS_IMAGES),
        "linux_images": get_images_directories_from_path(LINUX_IMAGES),
    },
    "install_guide": {
        "version": version if not version.endswith("dev0") else "main",
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
linkcheck_ignore = [
    f"https://github.com/{user_repo}/*",
    "https://www.ansys.com/*"
]


# -- Sphinx configuration ----------------------------------------------------

def copy_directory_recursive(source_path, destination_path):
    logger = logging.getLogger(__name__)

    if source_path.is_dir():
        destination_path.mkdir(parents=True, exist_ok=True)

        for file in source_path.iterdir():
            if file.is_dir():
                logger.info(f"Copying directory {file.name}/...")
                copy_directory_recursive(file, destination_path / file.name)
            else:
                logger.info(f"Copying file {file.name}...")
                destination_file = destination_path / file.name
                destination_file.write_text(file.read_text())


def remove_directory_recursive(directory_path):
    logger = logging.getLogger(__name__)

    directory_path = pathlib.Path(directory_path)
    if not directory_path.exists():
        return

    for file in directory_path.iterdir():
        if file.is_file():
            logger.info(f"Removing directory {file.name}/...")
            file.unlink()
        elif file.is_dir():
            remove_directory_recursive(file)

    logger.info(f"Removing directory {directory_path.name}/...")
    directory_path.rmdir()


def copy_directory(origin, destination):
    logger = logging.getLogger(__name__)
    logger.info(f"\nCopying {origin}/ to {destination}/...")
    copy_directory_recursive(origin, destination)

def copy_examples_to_source_dir(app):
    SOURCE_DIRECTORY = pathlib.Path(app.srcdir)
    EXAMPLES_DIRECTORY = pathlib.Path().parent.parent / "examples"
    copy_directory(EXAMPLES_DIRECTORY, SOURCE_DIRECTORY / "examples")

def copy_examples_to_output_dir(app):
    OUTPUT_DIRECTORY = pathlib.Path(app.outdir)
    EXAMPLES_DIRECTORY = pathlib.Path().parent.parent / "examples"
    copy_directory(EXAMPLES_DIRECTORY, OUTPUT_DIRECTORY / "examples")

def remove_examples_from_source_dir(app, exception):
    SOURCE_DIRECTORY = pathlib.Path(app.srcdir)
    logger = logging.getLogger(__name__)
    logger.info(f"\nRemoving examples/ from {SOURCE_DIRECTORY} directory...")
    remove_directory_recursive(SOURCE_DIRECTORY / "examples")

def setup(app):
    # HACK: rST files are copied to the doc/source directory before the build.
    # Sphinx needs all source files to be in the source directory to build.
    # However, the examples are desired to be kept in the root directory. Once the
    # build has completed, no matter its success, the examples are removed from
    # the source directory.
    if BUILD_EXAMPLES:
        import os
        app.connect("builder-inited", copy_examples_to_source_dir)
        app.connect("build-finished", remove_examples_from_source_dir)
        app.connect("build-finished", copy_examples_to_output_dir)
