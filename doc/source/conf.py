"""Sphinx documentation configuration file."""
from datetime import datetime
import os
import pathlib
import re

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
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    "css/custom.css"
]
# Override some style from the ansys-sphinx-theme to ensure the API reference
# gets displayed as expected
html_style = "css/custom.css"

# Sphinx extensions
extensions = [
    "sphinx_copybutton",
    #    "sphinx.ext.autodoc",
    #    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_jinja",
    "numpydoc",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "jupyter_rfb": ("https://jupyter-rfb.readthedocs.io/en/stable", None),
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
API_ROOT = "api"
BUILD_API = True if os.environ.get("BUILD_API", "true") == "true" else False
if not BUILD_API:
    exclude_patterns.append("api")
else:
    extensions.append("autoapi.extension")

BUILD_EXAMPLES = (
    True if os.environ.get("BUILD_EXAMPLES", "true") == "true" else False
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
# autodoc_default_options = {
#     #'members': 'var1, var2',
#     "member-order": "alphabetical",
#     #'special-members': '__init__',
#     "show-inheritance": True,
#     "undoc-members": True,
#     #'exclude-members': '__weakref__'
# }
# autodoc_class_signature = "separated"
# autodoc_mock_imports = ["tkinter"]

# -- Linkcheck configuration -------------------------------------------------
user_repo = f"{html_context['github_user']}/{html_context['github_repo']}"
linkcheck_ignore = [
    f"https://github.com/{user_repo}/*",
    "https://www.ansys.com/*"
]

# Configuration for Sphinx autoapi
autoapi_type = "python"
autoapi_dirs = ["../../src/ansys"]
autoapi_root = "api"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
]
#autoapi_template_dir = "_templates/autoapi"
autoapi_python_use_implicit_namespaces = True
autoapi_keep_files = True
autoapi_own_page_level = "class"

def jinja_filter_interface(klass: str):
    """Filter if a class name matches the naming convention for interfaces."""
    pattern = r"^I[A-Z][a-z]*(?:[A-Z][a-z]*)*$"
    return bool(re.match(pattern, klass))

def jinja_filter_enum(base: str):
    """Filter if a base has as name an enum object."""
    return base.endswith(("Enum", "IntEnum", "EnumType", "IntFlag"))

wrong_to_valid_xref_mapper = {
    # Fix references to the Python standard library
    r'ansys.stk.core.*.datetime': 'datetime.datetime',
    r'ansys.stk.core.*.IntEnum': 'enum.IntEnum',
    r'ansys.stk.core.*.Enum': 'enum.Enum',
    r'ansys.stk.core.*.EnumType': 'enum.EnumType',
    r'ansys.stk.core.*.IntFlag': 'enum.IntFlag',
    r'ansys.stk.core.*.typing.Any': 'typing.Any',
    r'ansys.stk.core.*.typing.Tuple': 'typing.Tuple',
    # Fix references to the ``ansys.stk.core.stkobjects`` module
    r'ansys.stk.core.*.StkObjectRoot': 'ansys.stk.core.stkobjects.StkObjectRoot',
    r'ansys.stk.core.*.StkObjectModelContext': 'ansys.stk.core.stkobjects.StkObjectModelContext',
    # Fix references to the ``ansys.stk.core.internal`` module
    r'ansys.stk.core.*.IUnknown': 'ansys.stk.core.internal.comutil.IUnknown',
    r'ansys.stk.core.*.IPictureDisp': 'ansys.stk.core.internal.comutil.IPictureDisp',
    r'ansys.stk.core.*.ISTKXApplicationEventHandler': 'ansys.stk.core.internal.eventutil.ISTKXApplicationEventHandler',
    r'ansys.stk.core.*.IUiAxGraphics2DCntrlEventHandler': 'ansys.stk.core.internal.eventutil.IUiAxGraphics2DCntrlEventHandler',
    r'ansys.stk.core.*.IUiAxGraphics3DCntrlEventHandler': 'ansys.stk.core.internal.eventutil.IUiAxGraphics3DCntrlEventHandler',
    r'ansys.stk.core.*.IImageCollectionEventHandler': 'ansys.stk.core.internal.eventutil.IImageCollectionEventHandler',
    r'ansys.stk.core.*.IKmlGraphicsEventHandler': 'ansys.stk.core.internal.eventutil.IKmlGraphicsEventHandler',
    r'ansys.stk.core.*.ISceneEventHandler': 'ansys.stk.core.internal.eventutil.ISceneEventHandler',
    r'ansys.stk.core.*.ITerrainOverlayCollectionEventHandler': 'ansys.stk.core.internal.eventutil.ITerrainOverlayCollectionEventHandler',
    # Fix references to the ``ansys.stk.core.stkutil`` module
    r'ansys.stk.core.*.IDate': 'ansys.stk.core.stkutil.IDate',
    r'ansys.stk.core.*.IDirection': 'ansys.stk.core.stkutil.IDirection',
    r'ansys.stk.core.*.IPosition': 'ansys.stk.core.stkutil.IPosition',
    r'ansys.stk.core.*.IOrbitState': 'ansys.stk.core.stkutil.IOrbitState',
    r'ansys.stk.core.*.ICartesian3Vector': 'ansys.stk.core.stkutil.ICartesian3Vector',
    r'ansys.stk.core.*.IOrientation': 'ansys.stk.core.stkutil.IOrientation',
    r'ansys.stk.core.*.ILocationData': 'ansys.stk.core.stkutil.ILocationData',
    r'ansys.stk.core.*.IRuntimeTypeInfo': 'ansys.stk.core.stkutil.IRuntimeTypeInfo',
    r'ansys.stk.core.*.IRuntimeTypeInfoProvider': 'ansys.stk.core.stkutil.IRuntimeTypeInfoProvider',
    r'ansys.stk.core.*.IDoublesCollection': 'ansys.stk.core.stkutil.IDoublesCollection',
    r'ansys.stk.core.*.IUnitPreferencesDimensionCollection': 'ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection',
    r'ansys.stk.core.*.IConversionUtility': 'ansys.stk.core.stkutil.IConversionUtility',
    r'ansys.stk.core.*.COORDINATE_SYSTEM': 'ansys.stk.core.stkutil.COORDINATE_SYSTEM',
    r'ansys.stk.core.*.AZ_EL_ABOUT_BORESIGHT': 'ansys.stk.core.stkutil.AZ_EL_ABOUT_BORESIGHT',
    r'ansys.stk.core.*.EULER_ORIENTATION_SEQUENCE': 'ansys.stk.core.stkutil.EULER_ORIENTATION_SEQUENCE',
    r'ansys.stk.core.*.YPR_ANGLES_SEQUENCE': 'ansys.stk.core.stkutil.YPR_ANGLES_SEQUENCE',
    r'ansys.stk.core.*.FILL_STYLE': 'ansys.stk.core.stkutil.FILL_STYLE',
    r'ansys.stk.core.*.LINE_STYLE': 'ansys.stk.core.stkutil.LINE_STYLE',  #TODO: duplicated object definition
    r'ansys.stk.core.*.IExecCmdResult': 'ansys.stk.core.stkutil.IExecCmdResult',  #TODO: duplicated object definition
    r'ansys.stk.core.*.EXEC_MULTI_CMD_RESULT_ACTION': 'ansys.stk.core.stkutil.EXEC_MULTI_CMD_RESULT_ACTION',  #TODO: duplicated object definition
    r'ansys.stk.core.*.IExecMultiCmdResult': 'ansys.stk.core.stkutil.IExecMultiCmdResult',  #TODO: duplicated object definition
    # Fix references to the ``ansys.stk.core.utilities.colors`` module
    r'ansys.stk.core.*.agcolor.Color': 'ansys.stk.core.utilities.colors.Color',
    # Fix references to the ``ansys.stk.core.stkx`` module
    r'ansys.stk.core.*.IUiAxGraphics2DAnalysisCntrl': 'ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl',
    r'ansys.stk.core.*.IUiAx2DCntrl': 'ansys.stk.core.stkx.IUiAx2DCntrl',  # TODO: shows a different style than IUiAxGraphics3DCntrl
    r'ansys.stk.core.*.IUiAxGraphics3DCntrl': 'ansys.stk.core.stkx.IUiAxGraphics3DCntrl', # TODO: shows a different style than IUiAx2DCntrl
    # Fix references to the ``ansys.stk.core.vgt`` module
    r'ansys.stk.core.*.ITimeToolEventArray': 'ansys.stk.core.vgt.ITimeToolEventArray',
    r'ansys.stk.core.*.ITimeToolEventIntervalSmartInterval': 'ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval',
    r'ansys.stk.core.*.ITimeToolEventIntervalList': 'ansys.stk.core.vgt.ITimeToolEventIntervalList',
    r'ansys.stk.core.*.ITimeToolEventSmartEpoch': 'ansys.stk.core.vgt.ITimeToolEventSmartEpoch',
    r'ansys.stk.core.*.IAnalysisWorkbenchComponent': 'ansys.stk.core.vgt.IAnalysisWorkbenchComponent',
    r'ansys.stk.core.*.IAnalysisWorkbenchProvider': 'ansys.stk.core.vgt.IAnalysisWorkbenchProvider',
    r'ansys.stk.core.*.IAnalysisWorkbenchRoot': 'ansys.stk.core.vgt.IAnalysisWorkbenchRoot',
    r'ansys.stk.core.*.IVectorGeometryToolAxes': 'ansys.stk.core.vgt.IVectorGeometryToolAxes',
}
"""Dictionary relating a regular expression with the desired substitution string.

Notes
-----
This variable is used for fixing wrong cross-references in the documentation.
The cross-reference issue is caused by sphinx-autoapi when using relative
imports together with wildcard imports, see issue 
https://github.com/readthedocs/sphinx-autoapi/issues/404

"""

def compile_regex_patterns(regex_dict: dict) -> dict:
    """
    Compile a dictionary containing regular expressions.

    Parameters
    ----------
    regex_dict : dict
        Regular expressions dictionary.

    Returns
    -------
    dict
        Compiled regular expressions dictionary with replacement values.

    """
    return {re.compile(pattern): replacement for pattern, replacement in regex_dict.items()}

WRONG_TO_VALID_XREF_COMPILED_MAPPER = compile_regex_patterns(wrong_to_valid_xref_mapper)
"""Dictionary relating a compiled regular expression with the desired substitution string."""

def fix_typing_xref(wrong_xref: str):
    """
    Filter wrong cross-references and fix it with the right value.

    If no valid mapping is declared for the provided reference, the input value
    is returned.

    Parameters
    ----------
    wrong_xref : str
        String for the wrong cross-reference.

    Returns
    -------
    valid_xref : str
        String for the valid cross-reference.

    """
    for expected_wrong_xref, valid_xref in WRONG_TO_VALID_XREF_COMPILED_MAPPER.items():
        if expected_wrong_xref.match(wrong_xref):
            return valid_xref
    return wrong_xref

def fix_args_typing_xref(wrong_args_xref: str) -> str:
    """
    Fix arguments typing cross-reference.

    Parameters
    ----------
    wrong_args_xref : str
        Wrong cross-reference for the argument type.

    Returns
    -------
    str
        Right cross-reference for the argument type.

    """
    # Regular expression pattern to match argument names and their types
    #arg_pattern = r'([\w_]+)(: ?[\w_]+)?'  # Matches "arg_name" or "arg_name: arg_type"
    #arg_pattern = r'([\w_]+)(: ?[\w_\.]+)?'
    arg_pattern = r'([\w_]+)\s*:\s*([\w_\.]+)?'  # Updated pattern to allow for optional spaces

    # Find all matches of the pattern in the argument string
    matches = re.findall(arg_pattern, wrong_args_xref)

    # Initialize lists to store argument names and types
    argument_names = []
    argument_types = []

    for match in matches:
        arg_name, arg_type = match
        argument_names.append(arg_name)
        if arg_type:
            arg_type = fix_typing_xref(arg_type.lstrip(': ').strip())
            argument_types.append(arg_type)
        else:
            argument_types.append(None)

    # Construct the updated argument string
    updated_arg_string = ", ".join([f"{name}: {type}" if type else name for name, type in zip(argument_names, argument_types)])
    return updated_arg_string

def autoapi_prepare_jinja_env(jinja_env) -> None:
    """
    Customize the Jinja environment by adding custom globals and filters.

    Notes
    -----
    See https://jinja.palletsprojects.com/en/latest/api/#jinja2.Environment

    """
    # Filter wrong cross-references in bases
    jinja_env.filters["fixbase"] = fix_typing_xref
    jinja_env.filters["fixargs"] = fix_args_typing_xref
    jinja_env.filters["fixannotation"] = fix_typing_xref

    # Filter classes, interfaces and enums
    jinja_env.filters["isinterface"] = jinja_filter_interface
    jinja_env.filters["isclass"] = jinja_filter_interface
    jinja_env.filters["isenum"] = jinja_filter_enum

    jinja_env.globals["project_name"] = project
