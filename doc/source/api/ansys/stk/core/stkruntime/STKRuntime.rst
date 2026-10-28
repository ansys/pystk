STKRuntime
==========

.. py:class:: ansys.stk.core.stkruntime.STKRuntime

   object

   Connect to STKRuntime using gRPC.

.. py:currentmodule:: STKRuntime


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkruntime.STKRuntime.attach_to_application`
              - Attach to STKRuntime.

                grpc_host is the IP address or DNS name of the gRPC server.
                grpc_port is the integral port number that the gRPC server is using.
                grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
                grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
                Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or

                grpc_client_cert is the path to the client certificate file. Required for mTLS authentication.
                grpc_client_key is the path to the client key file. Required for mTLS authentication.
                grpc_ca is the path to the issuing certificate authority. Required for mTLS authentication.
                grpc_uds_directory is an optional override of the path to the directory for UDS socket files. Only supported on Linux.
                grpc_uds_id is the optional ID for UDS socket file naming (stk-runtime-grpc<-id>.sock). Only supported on Linux.
                grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER on Windows,

            * - :py:attr:`~ansys.stk.core.stkruntime.STKRuntime.start_application`
              - Create a new STK Runtime instance and attach to the remote host.

                grpc_host is the IP address or DNS name of the gRPC server.
                grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
                grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
                grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
                user_control specifies if the application returns to the user's control
                (the application remains open) after terminating the Python API connection.
                no_graphics controls if runtime is started with or without graphics.
                Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or

                grpc_server_cert is the path to the server certificate file. Required for mTLS authentication.
                grpc_server_key is the path to the server key file. Required for mTLS authentication.
                grpc_client_cert is the path to the client certificate file. Required for mTLS authentication.
                grpc_client_key is the path to the client key file. Required for mTLS authentication.
                grpc_ca is the path to the issuing certificate authority. Required for mTLS authentication.
                grpc_uds_directory is an optional override of the path to the directory for UDS socket files. Only supported on Linux.
                grpc_uds_id is the optional ID for UDS socket file naming (stk-runtime-grpc<-id>.sock). Only supported on Linux.
                grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER on Windows,


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkruntime import STKRuntime


Method detail
-------------

.. py:method:: attach_to_application(grpc_host: str = 127.0.0.1, grpc_port: int = 40704, grpc_timeout_sec: int = 60, grpc_max_message_size: int = 0, grpc_allow_remote_host: bool = False, grpc_client_cert: str = None, grpc_client_key: str = None, grpc_ca: str = None, grpc_uds_directory: str = None, grpc_uds_id: str = None, grpc_authentication_mode: GrpcAuthenticationMode) -> STKRuntimeApplication
    :canonical: ansys.stk.core.stkruntime.STKRuntime.attach_to_application

    Attach to STKRuntime.

    grpc_host is the IP address or DNS name of the gRPC server.
    grpc_port is the integral port number that the gRPC server is using.
    grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
    grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
    Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or

    grpc_client_cert is the path to the client certificate file. Required for mTLS authentication.
    grpc_client_key is the path to the client key file. Required for mTLS authentication.
    grpc_ca is the path to the issuing certificate authority. Required for mTLS authentication.
    grpc_uds_directory is an optional override of the path to the directory for UDS socket files. Only supported on Linux.
    grpc_uds_id is the optional ID for UDS socket file naming (stk-runtime-grpc<-id>.sock). Only supported on Linux.
    grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER on Windows,


    :Parameters:

        **grpc_host** : :obj:`~str`

        **grpc_port** : :obj:`~int`

        **grpc_timeout_sec** : :obj:`~int`

        **grpc_max_message_size** : :obj:`~int`

        **grpc_allow_remote_host** : :obj:`~bool`

        **grpc_client_cert** : :obj:`~str`

        **grpc_client_key** : :obj:`~str`

        **grpc_ca** : :obj:`~str`

        **grpc_uds_directory** : :obj:`~str`

        **grpc_uds_id** : :obj:`~str`

        **grpc_authentication_mode** : :obj:`~GrpcAuthenticationMode`


    :Returns:

        :obj:`~STKRuntimeApplication`

.. py:method:: start_application(grpc_host: str = 127.0.0.1, grpc_port: int = 40704, grpc_timeout_sec: int = 60, grpc_max_message_size: int = 0, user_control: bool = False, no_graphics: bool = True, grpc_allow_remote_host: bool = False, grpc_server_cert: str = None, grpc_server_key: str = None, grpc_client_cert: str = None, grpc_client_key: str = None, grpc_ca: str = None, grpc_uds_directory: str = None, grpc_uds_id: str = None, grpc_authentication_mode: GrpcAuthenticationMode) -> STKRuntimeApplication
    :canonical: ansys.stk.core.stkruntime.STKRuntime.start_application

    Create a new STK Runtime instance and attach to the remote host.

    grpc_host is the IP address or DNS name of the gRPC server.
    grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
    grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
    grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
    user_control specifies if the application returns to the user's control
    (the application remains open) after terminating the Python API connection.
    no_graphics controls if runtime is started with or without graphics.
    Specify grpc_allow_remote_host = True to allow external connections, not allowed by default. Required when using 0.0.0.0 or

    grpc_server_cert is the path to the server certificate file. Required for mTLS authentication.
    grpc_server_key is the path to the server key file. Required for mTLS authentication.
    grpc_client_cert is the path to the client certificate file. Required for mTLS authentication.
    grpc_client_key is the path to the client key file. Required for mTLS authentication.
    grpc_ca is the path to the issuing certificate authority. Required for mTLS authentication.
    grpc_uds_directory is an optional override of the path to the directory for UDS socket files. Only supported on Linux.
    grpc_uds_id is the optional ID for UDS socket file naming (stk-runtime-grpc<-id>.sock). Only supported on Linux.
    grpc_authentication_mode is the method of client-server authentication to use for gRPC. Default is SINGLE_USER on Windows,


    :Parameters:

        **grpc_host** : :obj:`~str`

        **grpc_port** : :obj:`~int`

        **grpc_timeout_sec** : :obj:`~int`

        **grpc_max_message_size** : :obj:`~int`

        **user_control** : :obj:`~bool`

        **no_graphics** : :obj:`~bool`

        **grpc_allow_remote_host** : :obj:`~bool`

        **grpc_server_cert** : :obj:`~str`

        **grpc_server_key** : :obj:`~str`

        **grpc_client_cert** : :obj:`~str`

        **grpc_client_key** : :obj:`~str`

        **grpc_ca** : :obj:`~str`

        **grpc_uds_directory** : :obj:`~str`

        **grpc_uds_id** : :obj:`~str`

        **grpc_authentication_mode** : :obj:`~GrpcAuthenticationMode`


    :Returns:

        :obj:`~STKRuntimeApplication`


