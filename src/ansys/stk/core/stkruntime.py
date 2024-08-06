################################################################################
#          Copyright 2023-2024, Analytical Graphics, Inc.
################################################################################

"""Starts STK Runtime or attaches to an already running STK Runtime, and provides access to the Object Model root."""

__all__ = ["STKRuntime", "STKRuntimeApplication"]

import atexit
import subprocess
import os

from .stkx import STKXApplication
from .stkobjects import StkObjectRoot, StkObjectModelContext
from .utilities.exceptions import STKInitializationError
from .utilities.grpcutilities import GrpcCallBatcher
from .internal.grpcutil import GrpcClient
from .internal.apiutil import InterfaceProxy, read_registry_key, winreg_stk_binary_dir

class STKRuntimeApplication(STKXApplication):
    """
    Interact with STK Runtime.

    Use STKRuntime.StartApplication() or STKRuntime.AttachToApplication() 
    to obtain an initialized STKRuntimeApplication object.
    """

    def __init__(self):
        """Construct an object of type STKRuntimeApplication."""
        self.__dict__["_intf"] = InterfaceProxy()
        STKXApplication.__init__(self)
        self.__dict__["_root"] = None
        
    def _private_init(self, intf: InterfaceProxy):
        STKXApplication._private_init(self, intf)
        
    def __del__(self):
        """Destruct the STKRuntimeApplication object when all references to the object are deleted."""
        if self._intf:
            client: GrpcClient = self._intf.client
            client.terminate_connection(False)
        
    def new_object_root(self) -> StkObjectRoot:
        """May be used to obtain an Object Model Root from a running STK Engine application."""
        if self._intf:
            client: GrpcClient = self._intf.client
            root_unk = client.new_object_root()
            root = StkObjectRoot()
            root._private_init(root_unk)
            return root
        raise STKInitializationError(f"Not connected to the gRPC server.")
            
    def new_object_model_context(self) -> StkObjectModelContext:
        """May be used to obtain an Object Model Context from a running STK Engine application."""
        if self._intf:
            client: GrpcClient = self._intf.client
            context_unk = client.new_object_model_context()
            context = StkObjectModelContext()
            context._private_init(context_unk)
            return context
        raise STKInitializationError(f"Not connected to the gRPC server.")

    def SetGrpcOptions(self, options:dict) -> None:
        """
        Set advanced-usage options for the gRPC client.

        Available options include:
        { "collection iteration batch size" : int }. Number of items to preload while iterating
        through a collection object. Default is 100. Use 0 to indicate no limit (load entire collection).
        { "disable batching" : bool }. Disable all batching operations.
        { "release batch size" : int }. Number of interfaces to be garbage collected before 
        sending the entire batch to STK to be released. Default value is 12.
        """
        if self._intf:
            client: GrpcClient = self._intf.client
            client.set_grpc_options(options)
            
    def NewGrpcCallBatcher(self, max_batch:int=None, disable_batching:bool=False) -> GrpcCallBatcher:
        """
        Construct a GrpcCallBatcher linked to this gRPC client that may be used to improve API performance.
        
        max_batch is the maximum number of calls to batch together.
        Set disable_batching=True to disable batching operations for this batcher.
        See grpcutilities module for more information.
        """
        batcher = GrpcCallBatcher(disable_batching)
        batcher._private_init(self._intf.client, max_batch)
        return batcher

    def shutdown(self) -> None:
        """Shut down the STKRuntime application."""
        if self._intf:
            client: GrpcClient = self._intf.client
            client.set_shutdown_stkruntime(True)
        self._disconnect()

    def _disconnect(self) -> None:
        """Safely disconnect from STKRuntime."""
        if self._intf:
            client: GrpcClient = self._intf.client
            client.terminate_connection()
            self.__dict__["_intf"] = InterfaceProxy()

class STKRuntime(object):
    """Connect to STKRuntime using gRPC."""

    @staticmethod
    def start_application(grpc_host:str="0.0.0.0", \
                         grpc_port:int=40704, \
                         grpc_timeout_sec:int=60, \
                         userControl:bool=False, \
                         noGraphics:bool=True) -> STKRuntimeApplication:
        """
        Create a new STK Runtime instance and attach to the remote host.  

        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using.
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        Specify userControl = True to return the application to the user's control 
        (the application remains open) after terminating the Python API connection.
        """
        cmd_line = None
        if os.name != "nt":
            ld_env = os.getenv('LD_LIBRARY_PATH')
            if ld_env:
                for path in ld_env.split(':'):
                    if os.path.exists(os.path.join(path, 'stkruntime')):
                        cmd_line = f"{os.path.join(path, 'stkruntime')} --grpcHost {grpc_host} --grpcPort {grpc_port}" + (" --noGraphics" if noGraphics else "")
                        break
            else:
                raise STKInitializationError("LD_LIBRARY_PATH not defined. Add STK bin directory to LD_LIBRARY_PATH before running.")
        else:
            clsid_stkxapplication = "{062AB565-B121-45B5-A9A9-B412CEFAB6A9}"
            stkx_dll_path = read_registry_key(f"CLSID\\{clsid_stkxapplication}\\InprocServer32", silent_exception=True)
            bin_dir, dll_name = (None, None) if stkx_dll_path is None else os.path.split(stkx_dll_path)
            if bin_dir is None or not os.path.exists(os.path.join(bin_dir, "STKRuntime.exe")):
                bin_dir = winreg_stk_binary_dir()
                if bin_dir is None:
                    raise STKInitializationError(f"Could not find STKRuntime.exe. Verify STK installation.")
            cmd_line = f"\"{os.path.join(bin_dir, 'STKRuntime.exe')}\" /grpcHost {grpc_host} /grpcPort {grpc_port}" + (" /noGraphics" if noGraphics else "")

        subprocess.Popen(cmd_line, shell=True)
        host = "localhost" if grpc_host=="0.0.0.0" else grpc_host
        app = STKRuntime.attach_to_application(host, grpc_port, grpc_timeout_sec)
        app._intf.client.set_shutdown_stkruntime(not userControl)
        return app

        
    @staticmethod
    def attach_to_application(grpc_host:str="localhost", \
                            grpc_port:int=40704, \
                            grpc_timeout_sec:int=60) -> STKRuntimeApplication:
        """
        Attach to STKRuntime.

        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using.
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        """
        client = GrpcClient.new_client(grpc_host, grpc_port, grpc_timeout_sec)
        if client is not None:
            app_intf = client.get_stk_application_interface()
            app = STKRuntimeApplication()
            app._private_init(app_intf)
            atexit.register(app._disconnect)
            return app
        raise STKInitializationError(f"Cannot connect to the gRPC server on {grpc_host}:{grpc_port}.")
        
       
################################################################################
#          Copyright 2023-2024, Analytical Graphics, Inc.
################################################################################
