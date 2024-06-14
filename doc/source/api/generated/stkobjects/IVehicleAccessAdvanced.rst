IVehicleAccessAdvanced
======================

.. py:class:: IVehicleAccessAdvanced

   IAccessAdvanced
   
   Interface for configuring a vehicle's advanced targeting access computation properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_light_time_delay`
            * - :py:meth:`~time_sense`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAccessAdvanced


Property detail
---------------

.. py:property:: use_light_time_delay
    :canonical: ansys.stk.core.stkobjects.IVehicleAccessAdvanced.use_light_time_delay
    :type: bool

    Opt whether light time delay is applied when computing accesses.

.. py:property:: time_sense
    :canonical: ansys.stk.core.stkobjects.IVehicleAccessAdvanced.time_sense
    :type: "IV_TIME_SENSE"

    Signal sense of the clock host.


