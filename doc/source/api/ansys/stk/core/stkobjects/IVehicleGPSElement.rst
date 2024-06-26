IVehicleGPSElement
==================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGPSElement

   object
   
   An element of the GPS element collection.

.. py:currentmodule:: IVehicleGPSElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSElement.epoch`
              - The almanac reference date for all almanacs in the (.al3) file per ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSElement.week`
              - The almanac reference week (VINA) for all almanacs in this (.al3) file per the ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSElement.time_of_almanac`
              - The almanac reference time (Time of Appilcability) for all almanacs in the (.al3) file per ICD-GPS-200.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSElement.age`
              - The age of the satellite.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGPSElement


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSElement.epoch
    :type: typing.Any

    The almanac reference date for all almanacs in the (.al3) file per ICD-GPS-200.

.. py:property:: week
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSElement.week
    :type: int

    The almanac reference week (VINA) for all almanacs in this (.al3) file per the ICD-GPS-200.

.. py:property:: time_of_almanac
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSElement.time_of_almanac
    :type: float

    The almanac reference time (Time of Appilcability) for all almanacs in the (.al3) file per ICD-GPS-200.

.. py:property:: age
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSElement.age
    :type: float

    The age of the satellite.


