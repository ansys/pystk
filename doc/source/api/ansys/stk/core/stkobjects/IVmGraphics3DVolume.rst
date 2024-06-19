IVmGraphics3DVolume
===================

.. py:class:: IVmGraphics3DVolume

   object
   
   IAgVmVOVolume Interface for defining volume for volumetric object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~active_grid_points`
            * - :py:meth:`~spatial_calculation_levels`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmGraphics3DVolume


Property detail
---------------

.. py:property:: active_grid_points
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DVolume.active_grid_points
    :type: IAgVmVOActiveGridPoints

    Get Active Grid Points values for Volume property in the 3D Graphics properties for Volumetric object.

.. py:property:: spatial_calculation_levels
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DVolume.spatial_calculation_levels
    :type: IAgVmVOSpatialCalculationLevels

    Get Spatial Calculation Levels for Volume property in the 3D Graphics properties for Volumetric object.


