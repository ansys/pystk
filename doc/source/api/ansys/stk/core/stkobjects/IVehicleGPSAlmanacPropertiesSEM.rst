IVehicleGPSAlmanacPropertiesSEM
===============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM

   IVehicleGPSAlmanacProperties
   
   SEM almanac properties.

.. py:currentmodule:: IVehicleGPSAlmanacPropertiesSEM

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.avg_ura`
              - Get the satellite 'average' URA number, with the URA number as defined in the ICD-GPS-200. This is not an item in the raw almanac file, but is based on the average URA value transmitted by this satellite in its subframe 1 data sets.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.almanac_week`
              - Get the week number from the reference week.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.reference_week`
              - Gets or sets the almanac reference week (VINA) for all almanacs in this file per the ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.time_of_almanac`
              - Get the almanac reference time (Time of Appilcability) for all almanacs in the file per ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.date_of_almanac`
              - Get the almanac reference date for all almanacs in the file per ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.health`
              - Get the satellite health code as defined in the ICD-GPS-200 expressed in integer form. 0=healthy.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGPSAlmanacPropertiesSEM


Property detail
---------------

.. py:property:: avg_ura
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.avg_ura
    :type: int

    Get the satellite 'average' URA number, with the URA number as defined in the ICD-GPS-200. This is not an item in the raw almanac file, but is based on the average URA value transmitted by this satellite in its subframe 1 data sets.

.. py:property:: almanac_week
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.almanac_week
    :type: int

    Get the week number from the reference week.

.. py:property:: reference_week
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.reference_week
    :type: GPS_REFERENCE_WEEK

    Gets or sets the almanac reference week (VINA) for all almanacs in this file per the ICD-GPS-200.

.. py:property:: time_of_almanac
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.time_of_almanac
    :type: float

    Get the almanac reference time (Time of Appilcability) for all almanacs in the file per ICD-GPS-200.

.. py:property:: date_of_almanac
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.date_of_almanac
    :type: str

    Get the almanac reference date for all almanacs in the file per ICD-GPS-200.

.. py:property:: health
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAlmanacPropertiesSEM.health
    :type: int

    Get the satellite health code as defined in the ICD-GPS-200 expressed in integer form. 0=healthy.


