VehiclePhysicalData
===================

.. py:class:: ansys.stk.core.stkobjects.VehiclePhysicalData

   Bases: 

   Class defining physical data for the LOP force model.

.. py:currentmodule:: VehiclePhysicalData

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePhysicalData.drag_cross_sectional_area`
              - Gets or sets the satellite's cross-sectional area to be used in atmospheric drag calculations. Uses Area Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePhysicalData.srp_cross_sectional_area`
              - Gets or sets the satellite's cross-sectional area to be used in solar radiation pressure calculations. Uses Area Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePhysicalData.satellite_mass`
              - Gets or sets the mass of the satellite to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePhysicalData


Property detail
---------------

.. py:property:: drag_cross_sectional_area
    :canonical: ansys.stk.core.stkobjects.VehiclePhysicalData.drag_cross_sectional_area
    :type: float

    Gets or sets the satellite's cross-sectional area to be used in atmospheric drag calculations. Uses Area Dimension.

.. py:property:: srp_cross_sectional_area
    :canonical: ansys.stk.core.stkobjects.VehiclePhysicalData.srp_cross_sectional_area
    :type: float

    Gets or sets the satellite's cross-sectional area to be used in solar radiation pressure calculations. Uses Area Dimension.

.. py:property:: satellite_mass
    :canonical: ansys.stk.core.stkobjects.VehiclePhysicalData.satellite_mass
    :type: float

    Gets or sets the mass of the satellite to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.


