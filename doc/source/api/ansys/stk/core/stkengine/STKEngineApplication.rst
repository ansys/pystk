STKEngineApplication
====================

.. py:class:: ansys.stk.core.stkengine.STKEngineApplication

   STKXApplication

   Interact with STK Engine.

   Use STKEngine.StartApplication() to obtain an initialized STKEngineApplication object.

.. py:currentmodule:: STKEngineApplication


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkengine.STKEngineApplication.new_object_root
              - Create a new object model root for the STK Engine application.
            * - :py:attr:`~ansys.stk.core.stkengine.STKEngineApplication.new_object_model_context
              - Create a new object model context for the STK Engine application.
            * - :py:attr:`~ansys.stk.core.stkengine.STKEngineApplication.SetGrpcOptions
              - Grpc is not available with STK Engine. Provided for parity with STK Runtime and Desktop.
                
                Available options include:
                { "raise exceptions with STK Engine" : bool }. Set to false to suppress exceptions when
                using SetGrpcOptions and NewGrpcCallBatcher with STK Engine.
            * - :py:attr:`~ansys.stk.core.stkengine.STKEngineApplication.NewGrpcCallBatcher
              - Grpc is not available with STK Engine. Provided for parity with STK Runtime and Desktop.
            * - :py:attr:`~ansys.stk.core.stkengine.STKEngineApplication.shutdown
              - Shut down the STK Engine application.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkengine import STKEngineApplication


Method detail
-------------

.. py:method:: new_object_root(self) -> StkObjectRoot
    :canonical: ansys.stk.core.stkengine.STKEngineApplication.new_object_root

    Create a new object model root for the STK Engine application.

    :Returns:

        :obj:`~StkObjectRoot`

.. py:method:: new_object_model_context(self) -> StkObjectModelContext
    :canonical: ansys.stk.core.stkengine.STKEngineApplication.new_object_model_context

    Create a new object model context for the STK Engine application.

    :Returns:

        :obj:`~StkObjectModelContext`

.. py:method:: SetGrpcOptions(self, options: dict) -> None
    :canonical: ansys.stk.core.stkengine.STKEngineApplication.SetGrpcOptions

    Grpc is not available with STK Engine. Provided for parity with STK Runtime and Desktop.
    
    Available options include:
    { "raise exceptions with STK Engine" : bool }. Set to false to suppress exceptions when
    using SetGrpcOptions and NewGrpcCallBatcher with STK Engine.

    :Parameters:

    **options** : :obj:`~dict`

    :Returns:

        :obj:`~None`

.. py:method:: NewGrpcCallBatcher(self, max_batch: int = None, disable_batching: bool = None) -> GrpcCallBatcher
    :canonical: ansys.stk.core.stkengine.STKEngineApplication.NewGrpcCallBatcher

    Grpc is not available with STK Engine. Provided for parity with STK Runtime and Desktop.

    :Parameters:

    **max_batch** : :obj:`~int`
    **disable_batching** : :obj:`~bool`

    :Returns:

        :obj:`~GrpcCallBatcher`

.. py:method:: shutdown(self) -> None
    :canonical: ansys.stk.core.stkengine.STKEngineApplication.shutdown

    Shut down the STK Engine application.

    :Returns:

        :obj:`~None`


