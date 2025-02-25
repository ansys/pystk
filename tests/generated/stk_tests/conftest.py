# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from argparse import Namespace
from test_util import EngineLifetimeManager, CategoryManager


def pytest_addoption(parser):
    parser.addoption(
        "--target",
        action="store",
        dest="target",
        help="target application to run the tests with",
        default="StkXNoGfx",
        choices=["Stk", "StkX", "StkXNoGfx", "StkGrpc", "StkRuntime", "StkRuntimeNoGfx"],
    )

    parser.addoption(
        "--attach",
        action="store_true",
        dest="attach",
        help="Attach to a running Stk process (not applicable to StkX targets)",
        default=False,
    )

    parser.addoption(
        "--grpc_port",
        action="store",
        type=int,
        default=40704,
        dest="grpc_port",
        help="Specify gRPC port to use.",
        metavar="<port>",
    )

    parser.addoption(
        "--grpc_host",
        action="store",
        type=str,
        default="localhost",
        dest="grpc_host",
        help="Specify gRPC host to use.",
        metavar="<host>",
    )

    parser.addoption(
        "--include",
        action="append",
        dest="included_categories",
        help="name of category to include, repeat option to include multiple categories",
        metavar="<category name>",
    )

    parser.addoption(
        "--exclude",
        action="append",
        dest="excluded_categories",
        help="name of category to exclude, repeat option to exclude multiple categories",
        metavar="<category name>",
    )


def pytest_sessionstart(session):
    target = session.config.getoption("--target")
    attach = session.config.getoption("--attach")
    grpc_host = session.config.getoption("--grpc_host")
    grpc_port = session.config.getoption("--grpc_port")

    print(f"\nInitializing STK in {target} mode")
    EngineLifetimeManager.Initialize(
        lock=True, args=Namespace(target=target, attach=attach, grpc_host=grpc_host, grpc_port=grpc_port)
    )

    CategoryManager.SetUsingPyTest(True)

    included_categories = session.config.getoption("--include")
    if included_categories is not None:
        print(f"Included categories: {','.join(included_categories)}")
        for category in included_categories:
            CategoryManager.AddIncludedCategory(category)

    excluded_categories = session.config.getoption("--exclude")
    if excluded_categories is not None:
        print(f"Excluded categories: {','.join(excluded_categories)}")
        for category in excluded_categories:
            CategoryManager.AddExcludedCategory(category)

    print()


def pytest_sessionfinish(session):
    print("\n\nUninitializing STK")
    EngineLifetimeManager.Uninitialize(force=True)


def pytest_runtest_setup(item):
    """
    Check the categories on each item to appropriately include
    or exclude them based on the --exclude and --include command
    line arguments. See @category decorator.
    """
    categories = getattr(item.function, "categories", [])
    first_excluded_category = next((item for item in categories if CategoryManager.IsExcluded(item)), None)
    if first_excluded_category is not None:
        pytest.skip(f'Category "{first_excluded_category}" is excluded')
    if len(CategoryManager.included_categories) > 0:
        # there are some inclusion specified
        if len(categories) == 0:
            pytest.skip(f"No category, not included.")
        elif not any(CategoryManager.IsIncluded(name) for name in categories):
            pytest.skip(f"Category not included.")
