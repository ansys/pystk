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
            * - :py:attr:`~ansys.stk.core.stkruntime.STKRuntime.start_application`
              - Create a new STK Runtime instance and attach to the remote host.

                grpc_host is the IP address or DNS name of the gRPC server.
                grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
                grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
                grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
                Specify user_control = True to return the application to the user's control
                (the application remains open) after terminating the Python API connection.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkruntime import STKRuntime


Method detail
-------------

.. py:method:: attach_to_application(grpc_host: str = localhost, grpc_port: int = 40704, grpc_timeout_sec: int = 60, grpc_max_message_size: int = 0) -> STKRuntimeApplication
    :canonical: ansys.stk.core.stkruntime.STKRuntime.attach_to_application

    Attach to STKRuntime.

    grpc_host is the IP address or DNS name of the gRPC server.
    grpc_port is the integral port number that the gRPC server is using.
    grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
    grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.

    :Parameters:

        **grpc_host** : :obj:`~str`

        **grpc_port** : :obj:`~int`

        **grpc_timeout_sec** : :obj:`~int`

        **grpc_max_message_size** : :obj:`~int`


    :Returns:

        :obj:`~STKRuntimeApplication`

.. py:method:: start_application(grpc_host: str = localhost, grpc_port: int = 40704, grpc_timeout_sec: int = 60, grpc_max_message_size: int = 0, user_control: bool = False, no_graphics: bool = True) -> STKRuntimeApplication
    :canonical: ansys.stk.core.stkruntime.STKRuntime.start_application

    Create a new STK Runtime instance and attach to the remote host.

    grpc_host is the IP address or DNS name of the gRPC server.
    grpc_port is the integral port number that the gRPC server is using (valid values are integers from 0 to 65535).
    grpc_timeout_sec specifies the time allocated to wait for a grpc connection (seconds).
    grpc_max_message_size is the maximum size in bytes that the gRPC client can receive. Set to zero to use the gRPC default.
    Specify user_control = True to return the application to the user's control
    (the application remains open) after terminating the Python API connection.

    :Parameters:

        **grpc_host** : :obj:`~str`

        **grpc_port** : :obj:`~int`

        **grpc_timeout_sec** : :obj:`~int`

        **grpc_max_message_size** : :obj:`~int`

        **user_control** : :obj:`~bool`

        **no_graphics** : :obj:`~bool`


    :Returns:

        :obj:`~STKRuntimeApplication`


