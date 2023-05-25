"""Sphinx documentation configuration file."""
from datetime import datetime
import os
import pathlib

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
    "github_user": "pyansys",
    "github_repo": "pystk",
    "github_version": "main",
    "doc_path": "doc/source",
}
html_theme_options = {
    "github_url": "https://github.com/pyansys/pystk",
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
}
html_static_path = ["_static"]
html_css_files = [
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
exclude_patterns = ["api/generated", "links.rst"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

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
BUILD_API = True if os.environ.get("BUILD_API", "false") == "true" else False
if not BUILD_API:
    exclude_patterns.append("api")

BUILD_EXAMPLES = (
    True if os.environ.get("BUILD_EXAMPLES", "false") == "true" else False
)
if not BUILD_EXAMPLES:
    exclude_patterns.append("examples.rst")

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
