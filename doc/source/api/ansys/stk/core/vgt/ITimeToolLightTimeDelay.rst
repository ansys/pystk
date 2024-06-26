ITimeToolLightTimeDelay
=======================

.. py:class:: ansys.stk.core.vgt.ITimeToolLightTimeDelay

   object
   
   Manage Light Time Delay options..

.. py:currentmodule:: ITimeToolLightTimeDelay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolLightTimeDelay.use_light_time_delay`
              - Flag indicating whether to include minimum and maximum coordinate values in the defined set of values.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolLightTimeDelay.time_delay_convergence`
              - Set light Time Delay Convergence.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolLightTimeDelay.aberration_type`
              - Method used to Aberration Type.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolLightTimeDelay.clock_host`
              - Indicates whether object1 or object2 of an Access instance holds the clock for Access times.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolLightTimeDelay.time_sense`
              - Indicates whether apparent position is computed in a transmit or receive sense.


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


