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

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.is_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.set_type`
              - Set the type of sampling method.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.strategy`
              - Sampling method strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessSampling.type`
              - Type of sampling method used.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessSampling


Property detail
---------------

.. py:property:: strategy
    :canonical: ansys.stk.core.stkobjects.AccessSampling.strategy
    :type: ISamplingMethodStrategy

    Sampling method strategy.

.. py:property:: supported_types
    :canonical: ansys.stk.core.stkobjects.AccessSampling.supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.AccessSampling.type
    :type: SamplingMethod

    Type of sampling method used.


Method detail
-------------

.. py:method:: is_type_supported(self, sampling_method: SamplingMethod) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessSampling.is_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **sampling_method** : :obj:`~SamplingMethod`


    :Returns:

        :obj:`~bool`

.. py:method:: set_type(self, sampling_method: SamplingMethod) -> None
    :canonical: ansys.stk.core.stkobjects.AccessSampling.set_type

    Set the type of sampling method.

    :Parameters:

        **sampling_method** : :obj:`~SamplingMethod`


    :Returns:

        :obj:`~None`




