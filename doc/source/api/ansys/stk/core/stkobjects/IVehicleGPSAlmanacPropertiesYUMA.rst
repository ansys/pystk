IVehicleGPSAlmanacPropertiesYUMA
================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA

   IVehicleGPSAlmanacProperties
   
   YUMA almanac properties.

.. py:currentmodule:: IVehicleGPSAlmanacPropertiesYUMA

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.week_number`
              - Get the week number from the reference week.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.almanac_week`
              - Get the almanac reference week (VINA) for all almanacs in this file per the ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.reference_week`
              - Gets or sets the reference week (VINA) for all almanacs in this file per the ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.time_of_almanac`
              - Get the almanac reference time (Time of Appilcability) for all almanacs in the file per ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.date_of_almanac`
              - Get the almanac reference date for all almanacs in the file per ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.health`
              - Get the satellite health code as defined in the ICD-GPS-200 expressed in integer form. 0=healthy.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGPSAlmanacPropertiesYUMA


Property detail
---------------

.. py:property:: week_number
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.week_number
    :type: int

    Get the week number from the reference week.

.. py:property:: almanac_week
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.almanac_week
    :type: int

    Get the almanac reference week (VINA) for all almanacs in this file per the ICD-GPS-200.

.. py:property:: reference_week
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.reference_week
    :type: GPS_REFERENCE_WEEK

    Gets or sets the reference week (VINA) for all almanacs in this file per the ICD-GPS-200.

.. py:property:: time_of_almanac
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.time_of_almanac
    :type: float

    Get the almanac reference time (Time of Appilcability) for all almanacs in the file per ICD-GPS-200.

.. py:property:: date_of_almanac
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.date_of_almanac
    :type: str

    Get the almanac reference date for all almanacs in the file per ICD-GPS-200.

.. py:property:: health
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesYUMA.health
    :type: int

    Get the satellite health code as defined in the ICD-GPS-200 expressed in integer form. 0=healthy.


