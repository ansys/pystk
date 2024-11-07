AccessSampling
==============

.. py:class:: ansys.stk.core.stkobjects.AccessSampling

   Define properties and methods to configure the sampling strategy used in access computations.

.. py:currentmodule:: AccessSampling

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.set_type`
              - Set the type of sampling method.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.is_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.type`
              - Type of sampling method used.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.strategy`
              - Sampling method strategy.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessSampling


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.AccessSampling.type
    :type: SAMPLING_METHOD

    Type of sampling method used.

.. py:property:: supported_types
    :canonical: ansys.stk.core.stkobjects.AccessSampling.supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: strategy
    :canonical: ansys.stk.core.stkobjects.AccessSampling.strategy
    :type: ISamplingMethodStrategy

    Sampling method strategy.


Method detail
-------------


.. py:method:: set_type(self, sampling_method: SAMPLING_METHOD) -> None
    :canonical: ansys.stk.core.stkobjects.AccessSampling.set_type

    Set the type of sampling method.

    :Parameters:

    **sampling_method** : :obj:`~SAMPLING_METHOD`

    :Returns:

        :obj:`~None`

.. py:method:: is_type_supported(self, sampling_method: SAMPLING_METHOD) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessSampling.is_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **sampling_method** : :obj:`~SAMPLING_METHOD`

    :Returns:

        :obj:`~bool`



