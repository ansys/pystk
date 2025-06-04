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
#

import os
import pytest

from typing import Optional


if os.name == "nt":
    from ansys.stk.core.stkdesktop import STKDesktopApplication, STKDesktop
from ansys.stk.core.stkengine import STKEngineApplication, STKEngine
from ansys.stk.core.stkobjects import STKObjectRoot


class StkEnvironment:
    root_provider: Optional["IRootProvider"] = None
    root: Optional["STKObjectRoot"] = None
    stkx_form: Optional["StkEnvironment.StkXForm"] = None

    class IRootProvider:
        def get_root(self) -> "STKObjectRoot":
            raise RuntimeError("get_root must be overriden")

        def shutdown(self):
            pass

    class StkEngineProvider(IRootProvider):

        def __init__(self, args, use_grpc: bool = False):
            if args.attach:
                self.stk: "STKDesktopApplication" = STKDesktop.attach_to_application(
                    grpc_server=use_grpc, grpc_port=args.grpc_port, grpc_host=args.grpc_host
                )
            else:
                STKDesktop._disable_pop_ups = True
                self.stk: "STKDesktopApplication" = STKDesktop.start_application(
                    user_control=False, visible=True, grpc_server=use_grpc
                )

        def shutdown(self):
            self.stk.shutdown()

        def get_root(self) -> "STKObjectRoot":
            return self.stk.root

    class StkRuntimeEngineProvider(IRootProvider):

        def __init__(self, no_graphics: bool, args):
            # Lazy import to avoid direct dependency on grpc and protobug
            from ansys.stk.core.stkruntime import STKRuntimeApplication, STKRuntime

            if args.attach:
                self.stk: "STKRuntimeApplication" = STKRuntime.attach_to_application(
                    grpc_port=args.grpc_port, grpc_host=args.grpc_host
                )
            else:
                self.stk: "STKRuntimeApplication" = STKRuntime.start_application(
                    no_graphics=no_graphics, grpc_port=args.grpc_port, grpc_host=args.grpc_host
                )

        def shutdown(self):
            self.stk.shutdown()

        def get_root(self) -> "STKObjectRoot":
            return self.stk.new_object_root()

    class StkXEngineProvider(IRootProvider):

        def __init__(self):
            self.stk: "STKEngineApplication" = STKEngine.start_application(no_graphics=False)

        def shutdown(self):
            self.stk.shutdown()

        def get_root(self) -> "STKObjectRoot":
            return self.stk.new_object_root()

    class StkXNoGfxEngineProvider(IRootProvider):

        def __init__(self):
            self.stk: "STKEngineApplication" = STKEngine.start_application(no_graphics=True)

        def shutdown(self):
            self.stk.shutdown()

        def get_root(self) -> "STKObjectRoot":
            return self.stk.new_object_root()

    class StkXForm:
        def __init__(self):
            # Lazy import to avoid direct dependency on tkinter
            from tkinter import Tk, BOTH, YES, LEFT
            from ansys.stk.core.stkengine.tkcontrols import GlobeControl, MapControl

            self.window = Tk()
            self.globeControl = GlobeControl(self.window, width=320, height=200)
            self.globeControl.pack(fill=BOTH, expand=YES, side=LEFT)
            self.mapControl = MapControl(self.window, width=320, height=200)
            self.mapControl.pack(fill=BOTH, expand=YES, side=LEFT)
            self.window.update()

        def destroy(self):
            self.window.destroy()

        def update(self):
            self.window.update()

    @staticmethod
    def initialize(args):

        if os.name != "nt" and args.target == "Stk":
            raise RuntimeError("Stk target not supported on Linux.")

        if args.target == "Stk":
            StkEnvironment.root_provider = StkEnvironment.StkEngineProvider(args=args)
        elif args.target == "StkX":
            StkEnvironment.root_provider = StkEnvironment.StkXEngineProvider()
            StkEnvironment.stkx_form = StkEnvironment.StkXForm()
        elif args.target == "StkNoGfx":
            StkEnvironment.root_provider = StkEnvironment.StkXNoGfxEngineProvider()
        elif args.target == "StkGrpc":
            StkEnvironment.root_provider = StkEnvironment.StkEngineProvider(args=args, use_grpc=True)
        elif args.target == "StkRuntime":
            StkEnvironment.root_provider = StkEnvironment.StkRuntimeEngineProvider(no_graphics=False, args=args)
        elif args.target == "StkRuntimeNoGfx":
            StkEnvironment.root_provider = StkEnvironment.StkRuntimeEngineProvider(no_graphics=True, args=args)
        else:
            StkEnvironment.root_provider = StkEnvironment.StkXNoGfxEngineProvider()

        root = StkEnvironment.root_provider.get_root()

        print(root.execute_command("GetStkVersion /")[0])

        StkEnvironment.root = root

    @staticmethod
    def terminate():
        if StkEnvironment.stkx_form is not None:
            StkEnvironment.stkx_form.destroy()
        StkEnvironment.root = None
        if StkEnvironment.root_provider is not None:
            StkEnvironment.root_provider.shutdown()
            StkEnvironment.root_provider = None

    @staticmethod
    def get_root() -> "STKObjectRoot":
        if StkEnvironment.root is not None:
            return StkEnvironment.root
        else:
            raise RuntimeError("StkEnvironment has not been initialized")


@pytest.fixture()
def stk_root():
    root = StkEnvironment.get_root()
    yield root
    if root.current_scenario is not None:
        root.close_scenario()
