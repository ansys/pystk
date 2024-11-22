STKDesktop
==========

.. py:class:: ansys.stk.core.stkdesktop.STKDesktop

   object

   Create, initialize, and manage STK Desktop application instances.

.. py:currentmodule:: STKDesktop


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkdesktop.STKDesktop.start_application`
              - Create a new STK Desktop application instance.  
                
                Specify visible = True to show the application window.
                Specify user_control = True to return the application to the user's control.
                (the application remains open) after terminating the Python API connection.
                Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
                grpc_host is the IP address or DNS name of the gRPC server.
                grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
                grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
                grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
                Only available on Windows.
            * - :py:attr:`~ansys.stk.core.stkdesktop.STKDesktop.attach_to_application`
              - Attach to an existing STK Desktop instance. 
                
                Specify the Process ID (PID) in case multiple processes are open.
                Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
                grpc_host is the IP address or DNS name of the gRPC server.
                grpc_port is the integral port number that the gRPC server is using.
                grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
                grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
                Only available on Windows.
            * - :py:attr:`~ansys.stk.core.stkdesktop.STKDesktop.release_all`
              - Release all handles from Python to STK Desktop applications.
                
                Not applicable to gRPC connections.
            * - :py:attr:`~ansys.stk.core.stkdesktop.STKDesktop.create_thread_marshaller`
              - Return a ThreadMarshaller instance capable of marshalling the stk_object argument to a new thread.
                
                Not applicable to gRPC connections.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkdesktop import STKDesktop


Method detail
-------------

.. py:method:: start_application(visible: bool = False, user_control: bool = False, grpc_server: bool = False, grpc_host: str = False, grpc_port: int = False, grpc_max_message_size: int = False, grpc_timeout_sec: int = False) -> STKDesktopApplication
    :canonical: ansys.stk.core.stkdesktop.STKDesktop.start_application

    Create a new STK Desktop application instance.  
    
    Specify visible = True to show the application window.
    Specify user_control = True to return the application to the user's control.
    (the application remains open) after terminating the Python API connection.
    Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
    grpc_host is the IP address or DNS name of the gRPC server.
    grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
    grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
    grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
    Only available on Windows.

    :Parameters:

    **visible** : :obj:`~bool`
    **user_control** : :obj:`~bool`
    **grpc_server** : :obj:`~bool`
    **grpc_host** : :obj:`~str`
    **grpc_port** : :obj:`~int`
    **grpc_max_message_size** : :obj:`~int`
    **grpc_timeout_sec** : :obj:`~int`

    :Returns:

        :obj:`~STKDesktopApplication`

.. py:method:: attach_to_application(pid: int = None, grpc_server: bool = None, grpc_host: str = None, grpc_port: int = None, grpc_timeout_sec: int = None, grpc_max_message_size: int = None) -> STKDesktopApplication
    :canonical: ansys.stk.core.stkdesktop.STKDesktop.attach_to_application

    Attach to an existing STK Desktop instance. 
    
    Specify the Process ID (PID) in case multiple processes are open.
    Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
    grpc_host is the IP address or DNS name of the gRPC server.
    grpc_port is the integral port number that the gRPC server is using.
    grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
    grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
    Only available on Windows.

    :Parameters:

    **pid** : :obj:`~int`
    **grpc_server** : :obj:`~bool`
    **grpc_host** : :obj:`~str`
    **grpc_port** : :obj:`~int`
    **grpc_timeout_sec** : :obj:`~int`
    **grpc_max_message_size** : :obj:`~int`

    :Returns:

        :obj:`~STKDesktopApplication`

.. py:method:: release_all() -> None
    :canonical: ansys.stk.core.stkdesktop.STKDesktop.release_all

    Release all handles from Python to STK Desktop applications.
    
    Not applicable to gRPC connections.

    :Returns:

        :obj:`~None`

.. py:method:: create_thread_marshaller(stk_object) -> ThreadMarshaller
    :canonical: ansys.stk.core.stkdesktop.STKDesktop.create_thread_marshaller

    Return a ThreadMarshaller instance capable of marshalling the stk_object argument to a new thread.
    
    Not applicable to gRPC connections.

    :Returns:

        :obj:`~ThreadMarshaller`


