ITimeToolLightTimeDelay
=======================

.. py:class:: ITimeToolLightTimeDelay

   object
   
   Manage Light Time Delay options..

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_light_time_delay`
            * - :py:meth:`~time_delay_convergence`
            * - :py:meth:`~aberration_type`
            * - :py:meth:`~clock_host`
            * - :py:meth:`~time_sense`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolLightTimeDelay


Property detail
---------------

.. py:property:: use_light_time_delay
    :canonical: ansys.stk.core.vgt.ITimeToolLightTimeDelay.use_light_time_delay
    :type: bool

    Flag indicating whether to include minimum and maximum coordinate values in the defined set of values.

.. py:property:: time_delay_convergence
    :canonical: ansys.stk.core.vgt.ITimeToolLightTimeDelay.time_delay_convergence
    :type: float

    Set light Time Delay Convergence.

.. py:property:: aberration_type
    :canonical: ansys.stk.core.vgt.ITimeToolLightTimeDelay.aberration_type
    :type: CRDN_VOLUME_ABERRATION_TYPE

    Method used to Aberration Type.

.. py:property:: clock_host
    :canonical: ansys.stk.core.vgt.ITimeToolLightTimeDelay.clock_host
    :type: CRDN_VOLUME_CLOCK_HOST_TYPE

    Indicates whether object1 or object2 of an Access instance holds the clock for Access times.

.. py:property:: time_sense
    :canonical: ansys.stk.core.vgt.ITimeToolLightTimeDelay.time_sense
    :type: CRDN_VOLUME_TIME_SENSE_TYPE

    Indicates whether apparent position is computed in a transmit or receive sense.


