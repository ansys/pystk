# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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

from argparse import Namespace
from stk_environment import StkEnvironment


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


def pytest_sessionstart(session):
    target = session.config.getoption("--target")
    attach = session.config.getoption("--attach")
    grpc_host = session.config.getoption("--grpc_host")
    grpc_port = session.config.getoption("--grpc_port")

    print(f"\nInitializing STK in {target} mode")
    StkEnvironment.initialize(args=Namespace(target=target, attach=attach, grpc_host=grpc_host, grpc_port=grpc_port))

    print()


def pytest_sessionfinish(session):
    print("\n\nUninitializing STK")
    StkEnvironment.terminate()
