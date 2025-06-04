GrpcCallBatcher
===============

.. py:class:: ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher

   object

   A class used to batch together API calls to optimize performance.

   Activating batching will cause the normal API exception behavior to be 
   altered. Exceptions from one command may appear asynchronously. Therefore
   it is not recommended to use call batching while building and debugging,
   but rather as a performance optimization.

   Only calls that do not return a value may be batched together, 
   such as set-property requests and methods without a return value.
   Any method that has a return value (including get-property requests) 
   will automatically execute any previously batched commands before the 
   method with a return value is executed.

   Therefore, to reduce the number of remote API requests and improve 
   performance, code must be organized to group together commands that
   do not have a return value. Call chaining will interrupt a batch request
   because of the get-property command within the chain. E.g.:

   .. code-block:: python

       root.CurrentScenario.ShortDescription = short_description
       root.CurrentScenario.LongDescription = long_description

   will not be batched together because the call to `CurrentScenario` will
   get the scenario via an API call. These commands may be batched by 
   factoring out the call chaining:

   .. code-block:: python

       scen = root.CurrentScenario
       scen.ShortDescription = short_description
       scen.LongDescription = long_description

   This class may be used via the explicit commands or by using the "with" 
   statement to batch together the commands within the statement block.
   e.g.

   .. code-block:: python

       call_batcher = stk.NewGrpcCallBatcher()
       with call_batcher:
           facility1.LocalTimeOffset = 1.0
           facility1.HeightAboveGround = 10.0
           facility1.UseLocalTimeOffset = True
           facility1.ResetAzElMask()

.. py:currentmodule:: GrpcCallBatcher


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher.start_batching`
              - Explicitly start batching until stop_batching() is called.
            * - :py:attr:`~ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher.execute_batch`
              - Explicitly execute any queued batch commands.
            * - :py:attr:`~ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher.stop_batching`
              - Explicitly stop batching.
            * - :py:attr:`~ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher.create_future`
              - Create an object of type future_type that supports batching operations.
                
                source_obj is an STK Object Model type, e.g. STKObjectRoot.
                future_provider is a member method or property of source_obj, e.g. STKObjectRoot.CurrentScenario.
                future_type is the STK Object Model type that is returned from future_provider, e.g. Scenario.
                args are the arguments passed to future_provider if applicable.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.utilities.grpcutilities import GrpcCallBatcher


Method detail
-------------

.. py:method:: start_batching(self) -> None
    :canonical: ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher.start_batching

    Explicitly start batching until stop_batching() is called.

    :Returns:

        :obj:`~None`

.. py:method:: execute_batch(self) -> None
    :canonical: ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher.execute_batch

    Explicitly execute any queued batch commands.

    :Returns:

        :obj:`~None`

.. py:method:: stop_batching(self) -> None
    :canonical: ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher.stop_batching

    Explicitly stop batching.

    :Returns:

        :obj:`~None`

.. py:method:: create_future(self, source_obj, future_provider, future_type)
    :canonical: ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher.create_future

    Create an object of type future_type that supports batching operations.
    
    source_obj is an STK Object Model type, e.g. STKObjectRoot.
    future_provider is a member method or property of source_obj, e.g. STKObjectRoot.CurrentScenario.
    future_type is the STK Object Model type that is returned from future_provider, e.g. Scenario.
    args are the arguments passed to future_provider if applicable.


