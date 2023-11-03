################################################################################
#          Copyright 2023-2023, Analytical Graphics, Inc.
################################################################################

__all__ = ["STKRuntime", "STKRuntimeApplication"]

import atexit
import os
import subprocess

if os.name == "nt":
    import winreg

from .internal.apiutil import interface_proxy
from .internal.grpcutil import grpc_client
from .stkobjects import StkObjectModelContext, StkObjectRoot
from .stkx import STKXApplication
from .utilities.exceptions import *


class STKRuntimeApplication(STKXApplication):
    """Interact with STK Runtime.

    Use STKRuntime.StartApplication() or STKRuntime.AttachToApplication() 
    to obtain an initialized STKRuntimeApplication object.
    """

    def __init__(self):
        self.__dict__["_intf"] = interface_proxy()
        STKXApplication.__init__(self)
        self.__dict__["_root"] = None
        
    def _private_init(self, intf:interface_proxy):
        STKXApplication._private_init(self, intf)
        
    def __del__(self):
        if self._intf:
            self._intf.client.TerminateConnection(False)
        
    def NewObjectRoot(self) -> StkObjectRoot:
        """May be used to obtain an Object Model Root from a running STK Engine application."""
        if self._intf:
            root_unk = self._intf.client.NewObjectRoot()
            root = StkObjectRoot()
            root._private_init(root_unk)
            return root
        raise STKInitializationError("Not connected to the gRPC server.")
            
    def NewObjectModelContext(self) -> StkObjectModelContext:
        """May be used to obtain an Object Model Context from a running STK Engine application."""
        if self._intf:
            context_unk = self._intf.client.NewObjectModelContext()
            context = StkObjectModelContext()
            context._private_init(context_unk)
            return context
        raise STKInitializationError("Not connected to the gRPC server.")

    def ShutDown(self) -> None:
        """Shut down the STKRuntime application."""
        if self._intf:
            self._intf.client.set_shutdown_stkruntime(True)
        self._disconnect()

    def _disconnect(self) -> None:
        """Safely disconnect from STKRuntime."""
        if self._intf:
            self._intf.client.TerminateConnection()
            self.__dict__["_intf"] = interface_proxy()

class STKRuntime(object):
    """Connect to STKRuntime using gRPC."""
    
    @staticmethod
    def _read_registry_key(root, key, value=None, silent_exception=False):
        try:
            with winreg.OpenKey(root, key) as hkey:
                (val, typ) = winreg.QueryValueEx(hkey, value)
            return val
        except Exception as e:
            if not silent_exception:
                raise STKInitializationError(f"Error Reading Registry for {key}: {e}")
            return None
        
    @staticmethod
    def StartApplication(grpc_host:str="0.0.0.0", \
                         grpc_port:int=40704, \
                         grpc_timeout_sec:int=60, \
                         userControl:bool=False, \
                         noGraphics:bool=True) -> STKRuntimeApplication:
        """Create a new STK Runtime instance and attach to the remote host.

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
            executable = STKRuntime._read_registry_key(winreg.HKEY_CLASSES_ROOT, 'CLSID\{7ADA6C22-FA34-4578-8BE8-65405A55EE15}\LocalServer32')
            dir, fi = os.path.split(executable)
            cmd_line = f"{os.path.join(dir, 'STKRuntime.exe')}\" /grpcHost {grpc_host} /grpcPort {grpc_port}" + (" /noGraphics" if noGraphics else "")

        subprocess.Popen(cmd_line, shell=True)
        host = "localhost" if grpc_host=="0.0.0.0" else grpc_host
        app = STKRuntime.AttachToApplication(host, grpc_port, grpc_timeout_sec)
        app._intf.client.set_shutdown_stkruntime(not userControl)
        return app

        
    @staticmethod
    def AttachToApplication(grpc_host:str="localhost", \
                            grpc_port:int=40704, \
                            grpc_timeout_sec:int=60) -> STKRuntimeApplication:
        """Attach to STKRuntime.

        grpc_host is the IP address or DNS name of the gRPC server.
        grpc_port is the integral port number that the gRPC server is using.
        grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
        """
        client = grpc_client.new_client(grpc_host, grpc_port, grpc_timeout_sec)
        if client is not None:
            app_intf = client.GetStkApplicationInterface()
            app = STKRuntimeApplication()
            app._private_init(app_intf)
            atexit.register(app._disconnect)
            return app
        raise STKInitializationError(f"Cannot connect to the gRPC server on {grpc_host}:{grpc_port}.")
        
       
################################################################################
#          Copyright 2023-2023, Analytical Graphics, Inc.
################################################################################
