IVehicleGPSAlmanacPropertiesSP3
===============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSP3

   IVehicleGPSAlmanacProperties
   
   SP3 almanac properties.

.. py:currentmodule:: IVehicleGPSAlmanacPropertiesSP3

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSP3.almanac_week`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSP3.time_of_almanac`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSP3.date_of_almanac`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGPSAlmanacPropertiesSP3


Property detail
---------------

.. py:property:: almanac_week
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSP3.almanac_week
    :type: int

    Get the almanac reference week (VINA) for all almanacs in this file per the ICD-GPS-200.

.. py:property:: time_of_almanac
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSP3.time_of_almanac
    :type: float

    Get the almanac reference time (Time of Appilcability) for all almanacs in the file per ICD-GPS-200.

.. py:property:: date_of_almanac
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSP3.date_of_almanac
    :type: str

    Get the almanac reference date for all almanacs in the file per ICD-GPS-200.


