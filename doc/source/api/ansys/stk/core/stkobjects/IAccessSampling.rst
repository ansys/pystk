IAccessSampling
===============

.. py:class:: IAccessSampling

   object
   
   Define properties and methods to configure the sampling strategy used in access computations.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_type`
              - Set the type of sampling method.
            * - :py:meth:`~is_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~supported_types`
            * - :py:meth:`~strategy`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessSampling


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IAccessSampling.type
    :type: "SAMPLING_METHOD"

    Type of sampling method used.

.. py:property:: supported_types
    :canonical: ansys.stk.core.stkobjects.IAccessSampling.supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: strategy
    :canonical: ansys.stk.core.stkobjects.IAccessSampling.strategy
    :type: "IAgSamplingMethodStrategy"

    Sampling method strategy.


Method detail
-------------


.. py:method:: set_type(self, samplingMethod:"SAMPLING_METHOD") -> None

    Set the type of sampling method.

    :Parameters:

    **samplingMethod** : :obj:`~"SAMPLING_METHOD"`

    :Returns:

        :obj:`~None`

.. py:method:: is_type_supported(self, samplingMethod:"SAMPLING_METHOD") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **samplingMethod** : :obj:`~"SAMPLING_METHOD"`

    :Returns:

        :obj:`~bool`



