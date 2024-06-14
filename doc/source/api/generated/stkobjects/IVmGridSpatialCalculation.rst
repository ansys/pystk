IVmGridSpatialCalculation
=========================

.. py:class:: IVmGridSpatialCalculation

   object
   
   IAgVmGridSpatialCalculation Interface volume grid spatial calculation.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~volume_grid`
            * - :py:meth:`~use_spatial_calculation`
            * - :py:meth:`~spatial_calculation`
            * - :py:meth:`~available_volume_grids`
            * - :py:meth:`~available_spatial_calculations`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmGridSpatialCalculation


Property detail
---------------

.. py:property:: volume_grid
    :canonical: ansys.stk.core.stkobjects.IVmGridSpatialCalculation.volume_grid
    :type: str

    The volume grid for spatial calculations.

.. py:property:: use_spatial_calculation
    :canonical: ansys.stk.core.stkobjects.IVmGridSpatialCalculation.use_spatial_calculation
    :type: bool

    Flag controls whether spatial calculation is used.

.. py:property:: spatial_calculation
    :canonical: ansys.stk.core.stkobjects.IVmGridSpatialCalculation.spatial_calculation
    :type: str

    The volume grid for spatial calculations.

.. py:property:: available_volume_grids
    :canonical: ansys.stk.core.stkobjects.IVmGridSpatialCalculation.available_volume_grids
    :type: list

    Get the available Volume Grids.

.. py:property:: available_spatial_calculations
    :canonical: ansys.stk.core.stkobjects.IVmGridSpatialCalculation.available_spatial_calculations
    :type: list

    Get the available Spatial Calculations.


