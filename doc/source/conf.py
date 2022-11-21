"""Sphinx documentation configuration file."""
from datetime import datetime

from ansys_sphinx_theme import pyansys_logo_black as logo

# Project information
project = "ansys-stk-core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = "0.1.dev0"

# Select desired logo, theme, and declare the html title
html_logo = logo
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "pystk-core"

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/pyansys/pystk-core",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
}

# Sphinx extensions
extensions = [
    "enum_tools.autoenum",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "numpydoc",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    # "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    # "SS02",  # Summary does not start with a capital letter
    # "SS03", # Summary does not end with a period
    # "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# Path to static files
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Directories excluded when looking for source files
exclude_patterns = ['api/generated/*.rst']

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# autodoc configuration
autodoc_default_options = {
    #'members': 'var1, var2',
    'member-order': 'alphabetical',
    #'special-members': '__init__',
    "show-inheritance": True,
    'undoc-members': True,
    #'exclude-members': '__weakref__'
}
autodoc_class_signature = "separated"
autodoc_mock_imports = ["tkinter"]