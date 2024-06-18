IVmGraphics3DSpatialCalculationLevels
=====================================

.. py:class:: IVmGraphics3DSpatialCalculationLevels

   object
   
   IAgVmVOSpatialCalculationLevels Interface for defining Spatial Calculation Levels for Volumetric Object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show_boundary_levels`
            * - :py:meth:`~boundary_levels`
            * - :py:meth:`~show_fill_levels`
            * - :py:meth:`~display_colors_outside_min_max`
            * - :py:meth:`~fill_levels`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmGraphics3DSpatialCalculationLevels


Property detail
---------------

.. py:property:: show_boundary_levels
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DSpatialCalculationLevels.show_boundary_levels
    :type: bool

    Show or hide Spatial Calculation Boundary Levels.

.. py:property:: boundary_levels
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DSpatialCalculationLevels.boundary_levels
    :type: "IAgVmVOSpatialCalculationLevelCollection"

    Access and manipulate the collection of Spatial Calculation Boundary Levels for Volumetric object.

.. py:property:: show_fill_levels
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DSpatialCalculationLevels.show_fill_levels
    :type: bool

    Show or hide Fill Levels.

.. py:property:: display_colors_outside_min_max
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DSpatialCalculationLevels.display_colors_outside_min_max
    :type: bool

    Sets/gets Display Colors Outside MinMax.

.. py:property:: fill_levels
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DSpatialCalculationLevels.fill_levels
    :type: "IAgVmVOSpatialCalculationLevelCollection"

    Access and manipulate the collection of Spatial Calculation Fill Levels for Volumetric object.


