IVehiclePhysicalData
====================

.. py:class:: IVehiclePhysicalData

   object
   
   Physical data interface for LOP propagator.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~drag_cross_sectional_area`
            * - :py:meth:`~srp_cross_sectional_area`
            * - :py:meth:`~satellite_mass`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePhysicalData


Property detail
---------------

.. py:property:: drag_cross_sectional_area
    :canonical: ansys.stk.core.stkobjects.IVehiclePhysicalData.drag_cross_sectional_area
    :type: float

    Gets or sets the satellite's cross-sectional area to be used in atmospheric drag calculations. Uses Area Dimension.

.. py:property:: srp_cross_sectional_area
    :canonical: ansys.stk.core.stkobjects.IVehiclePhysicalData.srp_cross_sectional_area
    :type: float

    Gets or sets the satellite's cross-sectional area to be used in solar radiation pressure calculations. Uses Area Dimension.

.. py:property:: satellite_mass
    :canonical: ansys.stk.core.stkobjects.IVehiclePhysicalData.satellite_mass
    :type: float

    Gets or sets the mass of the satellite to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.


