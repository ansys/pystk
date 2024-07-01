STKRuntimeApplication
=====================

.. py:class:: ansys.stk.core.stkruntime.STKRuntimeApplication

   STKXApplication

   Interact with STK Runtime.

   Use STKRuntime.StartApplication() or STKRuntime.AttachToApplication() 
   to obtain an initialized STKRuntimeApplication object.

.. py:currentmodule:: STKRuntimeApplication


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkruntime.STKRuntimeApplication.new_object_root
              - May be used to obtain an Object Model Root from a running STK Engine application.
            * - :py:attr:`~ansys.stk.core.stkruntime.STKRuntimeApplication.new_object_model_context
              - May be used to obtain an Object Model Context from a running STK Engine application.
            * - :py:attr:`~ansys.stk.core.stkruntime.STKRuntimeApplication.SetGrpcOptions
              - Set advanced-usage options for the gRPC client.
                
                Available options include:
                { "collection iteration batch size" : int }. Number of items to preload while iterating
                through a collection object. Default is 100. Use 0 to indicate no limit (load entire collection).
                { "disable batching" : bool }. Disable all batching operations.
                { "release batch size" : int }. Number of interfaces to be garbage collected before 
                sending the entire batch to STK to be released. Default value is 12.
            * - :py:attr:`~ansys.stk.core.stkruntime.STKRuntimeApplication.NewGrpcCallBatcher
              - Construct a GrpcCallBatcher linked to this gRPC client that may be used to improve API performance.
                
                max_batch is the maximum number of calls to batch together.
                Set disable_batching=True to disable batching operations for this batcher.
                See grpcutilities module for more information.
            * - :py:attr:`~ansys.stk.core.stkruntime.STKRuntimeApplication.shutdown
              - Shut down the STKRuntime application.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkruntime import STKRuntimeApplication


Method detail
-------------

.. py:method:: new_object_root(self) -> StkObjectRoot
    :canonical: ansys.stk.core.stkruntime.STKRuntimeApplication.new_object_root

    May be used to obtain an Object Model Root from a running STK Engine application.

    :Returns:

        :obj:`~StkObjectRoot`

.. py:method:: new_object_model_context(self) -> StkObjectModelContext
    :canonical: ansys.stk.core.stkruntime.STKRuntimeApplication.new_object_model_context

    May be used to obtain an Object Model Context from a running STK Engine application.

    :Returns:

        :obj:`~StkObjectModelContext`

.. py:method:: SetGrpcOptions(self, options: dict) -> None
    :canonical: ansys.stk.core.stkruntime.STKRuntimeApplication.SetGrpcOptions

    Set advanced-usage options for the gRPC client.
    
    Available options include:
    { "collection iteration batch size" : int }. Number of items to preload while iterating
    through a collection object. Default is 100. Use 0 to indicate no limit (load entire collection).
    { "disable batching" : bool }. Disable all batching operations.
    { "release batch size" : int }. Number of interfaces to be garbage collected before 
    sending the entire batch to STK to be released. Default value is 12.

    :Parameters:

    **options** : :obj:`~dict`

    :Returns:

        :obj:`~None`

.. py:method:: NewGrpcCallBatcher(self, max_batch: int = None, disable_batching: bool = None) -> GrpcCallBatcher
    :canonical: ansys.stk.core.stkruntime.STKRuntimeApplication.NewGrpcCallBatcher

    Construct a GrpcCallBatcher linked to this gRPC client that may be used to improve API performance.
    
    max_batch is the maximum number of calls to batch together.
    Set disable_batching=True to disable batching operations for this batcher.
    See grpcutilities module for more information.

    :Parameters:

    **max_batch** : :obj:`~int`
    **disable_batching** : :obj:`~bool`

    :Returns:

        :obj:`~GrpcCallBatcher`

.. py:method:: shutdown(self) -> None
    :canonical: ansys.stk.core.stkruntime.STKRuntimeApplication.shutdown

    Shut down the STKRuntime application.

    :Returns:

        :obj:`~None`


