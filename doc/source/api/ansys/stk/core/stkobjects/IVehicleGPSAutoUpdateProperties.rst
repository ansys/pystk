IVehicleGPSAutoUpdateProperties
===============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateProperties

   object
   
   Interface for GPS AutoUpdate properties.

.. py:currentmodule:: IVehicleGPSAutoUpdateProperties

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateProperties.selection`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateProperties.switch_method`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateProperties.week_reference_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGPSAutoUpdateProperties


Property detail
---------------

.. py:property:: selection
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateProperties.selection
    :type: VEHICLE_GPS_ELEM_SELECTION

    Whether Automatic Update is active.

.. py:property:: switch_method
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateProperties.switch_method
    :type: VEHICLE_GPS_SWITCH_METHOD

    When to switch between element sets.

.. py:property:: week_reference_epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateProperties.week_reference_epoch
    :type: GPS_REFERENCE_WEEK

    Week reference epoch.


