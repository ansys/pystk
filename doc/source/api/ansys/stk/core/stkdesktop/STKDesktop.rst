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

            * - :py:attr:`~ansys.stk.core.stkdesktop.STKDesktop.attach_to_application`
              - Attach to an existing STK Desktop instance.

                Specify the Process ID (PID) in case multiple processes are open.
                Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
                grpc_host is the IP address or DNS name of the gRPC server.
                grpc_port is the integral port number that the gRPC server is using.
                grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
                grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
                Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or other remote address as the grpc_host.
                grpc_client_cert is the path to the client certificate. Required to perform mTLS authentication.
                grpc_client_key is the path to the client private encryption key. Required to perform mTLS authentication.
                grpc_ca is the path to the issuing certificate authority. Required to perform mTLS authentication.
                grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER.
                Only available on Windows.
            * - :py:attr:`~ansys.stk.core.stkdesktop.STKDesktop.create_thread_marshaller`
              - Return a ThreadMarshaller instance capable of marshalling the stk_object argument to a new thread.

                Not applicable to gRPC connections.
            * - :py:attr:`~ansys.stk.core.stkdesktop.STKDesktop.release_all`
              - Release all handles from Python to STK Desktop applications.

                Not applicable to gRPC connections.
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
                Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or other remote address as the grpc_host.
                grpc_server_cert is the path to the server certificate file. Required for mTLS authentication.
                grpc_server_key is the path to the server key file. Required for mTLS authentication.
                grpc_client_cert is the path to the client certificate file. Required for mTLS authentication.
                grpc_client_key is the path to the client key file. Required for mTLS authentication.
                grpc_ca is the path to the issuing certificate authority. Required for mTLS authentication.
                grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER.
                Only available on Windows.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkdesktop import STKDesktop


Method detail
-------------

.. py:method:: attach_to_application(pid: int = None, grpc_server: bool = False, grpc_host: str = 127.0.0.1, grpc_port: int = 40704, grpc_timeout_sec: int = 60, grpc_max_message_size: int = 0, grpc_allow_remote_host: bool = False, grpc_client_cert: str = None, grpc_client_key: str = None, grpc_ca: str = None, grpc_authentication_mode: GrpcAuthenticationMode) -> STKDesktopApplication
    :canonical: ansys.stk.core.stkdesktop.STKDesktop.attach_to_application

    Attach to an existing STK Desktop instance.

    Specify the Process ID (PID) in case multiple processes are open.
    Specify grpc_server = True to attach to STK Desktop Application running the gRPC server at grpc_host:grpc_port.
    grpc_host is the IP address or DNS name of the gRPC server.
    grpc_port is the integral port number that the gRPC server is using.
    grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
    grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
    Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or other remote address as the grpc_host.
    grpc_client_cert is the path to the client certificate. Required to perform mTLS authentication.
    grpc_client_key is the path to the client private encryption key. Required to perform mTLS authentication.
    grpc_ca is the path to the issuing certificate authority. Required to perform mTLS authentication.
    grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER.
    Only available on Windows.

    :Parameters:

        **pid** : :obj:`~int`

        **grpc_server** : :obj:`~bool`

        **grpc_host** : :obj:`~str`

        **grpc_port** : :obj:`~int`

        **grpc_timeout_sec** : :obj:`~int`

        **grpc_max_message_size** : :obj:`~int`

        **grpc_allow_remote_host** : :obj:`~bool`

        **grpc_client_cert** : :obj:`~str`

        **grpc_client_key** : :obj:`~str`

        **grpc_ca** : :obj:`~str`

        **grpc_authentication_mode** : :obj:`~GrpcAuthenticationMode`


    :Returns:

        :obj:`~STKDesktopApplication`

.. py:method:: create_thread_marshaller(stk_object) -> ThreadMarshaller
    :canonical: ansys.stk.core.stkdesktop.STKDesktop.create_thread_marshaller

    Return a ThreadMarshaller instance capable of marshalling the stk_object argument to a new thread.

    Not applicable to gRPC connections.

    :Returns:

        :obj:`~ThreadMarshaller`

.. py:method:: release_all() -> None
    :canonical: ansys.stk.core.stkdesktop.STKDesktop.release_all

    Release all handles from Python to STK Desktop applications.

    Not applicable to gRPC connections.

    :Returns:

        :obj:`~None`

.. py:method:: start_application(visible: bool = False, user_control: bool = False, grpc_server: bool = False, grpc_host: str = 127.0.0.1, grpc_port: int = 40704, grpc_timeout_sec: int = 60, grpc_max_message_size: int = 0, grpc_allow_remote_host: bool = False, grpc_server_cert: str = None, grpc_server_key: str = None, grpc_client_cert: str = None, grpc_client_key: str = None, grpc_ca: str = None, grpc_authentication_mode: GrpcAuthenticationMode) -> STKDesktopApplication
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
    Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or other remote address as the grpc_host.
    grpc_server_cert is the path to the server certificate file. Required for mTLS authentication.
    grpc_server_key is the path to the server key file. Required for mTLS authentication.
    grpc_client_cert is the path to the client certificate file. Required for mTLS authentication.
    grpc_client_key is the path to the client key file. Required for mTLS authentication.
    grpc_ca is the path to the issuing certificate authority. Required for mTLS authentication.
    grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER.
    Only available on Windows.

    :Parameters:

        **visible** : :obj:`~bool`

        **user_control** : :obj:`~bool`

        **grpc_server** : :obj:`~bool`

        **grpc_host** : :obj:`~str`

        **grpc_port** : :obj:`~int`

        **grpc_timeout_sec** : :obj:`~int`

        **grpc_max_message_size** : :obj:`~int`

        **grpc_allow_remote_host** : :obj:`~bool`

        **grpc_server_cert** : :obj:`~str`

        **grpc_server_key** : :obj:`~str`

        **grpc_client_cert** : :obj:`~str`

        **grpc_client_key** : :obj:`~str`

        **grpc_ca** : :obj:`~str`

        **grpc_authentication_mode** : :obj:`~GrpcAuthenticationMode`


    :Returns:

        :obj:`~STKDesktopApplication`


