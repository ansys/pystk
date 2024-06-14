IVmGraphics3D
=============

.. py:class:: IVmGraphics3D

   object
   
   IAgVmVO Interface for a volumetric object's 3D Graphics properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~visible`
            * - :py:meth:`~smoothing`
            * - :py:meth:`~shading`
            * - :py:meth:`~quality`
            * - :py:meth:`~grid`
            * - :py:meth:`~cross_section`
            * - :py:meth:`~volume`
            * - :py:meth:`~show_boundary_legend`
            * - :py:meth:`~show_fill_legend`
            * - :py:meth:`~boundary_legend`
            * - :py:meth:`~fill_legend`
            * - :py:meth:`~volume_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmGraphics3D


Property detail
---------------

.. py:property:: visible
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.visible
    :type: bool

    Display volumetric object including Grid, Volume, and Cross Sections in 3D Graphics window.

.. py:property:: smoothing
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.smoothing
    :type: bool

    Enables to smooth out the volume and surface boundaries using interpolation between grid points.

.. py:property:: shading
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.shading
    :type: bool

    Enables to add shading to the boundary surface. Shading slows down animation but generates helpful lighting effects based on surfaces.

.. py:property:: quality
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.quality
    :type: "VM_DISPLAY_QUALITY_TYPE"

    Sets/gets the quality of the graphics display.

.. py:property:: grid
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.grid
    :type: "IAgVmVOGrid"

    Get the Grid properties of 3D Graphics window for the volumetric object.

.. py:property:: cross_section
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.cross_section
    :type: "IAgVmVOCrossSection"

    Get the 3D Graphics properties for planar cross-sections through the volumetric grid.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.volume
    :type: "IAgVmVOVolume"

    Get the 3D Graphics properties for Volume.

.. py:property:: show_boundary_legend
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.show_boundary_legend
    :type: bool

    Enables/disables boundary legends in 3D Graphics window for Volumetric object.

.. py:property:: show_fill_legend
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.show_fill_legend
    :type: bool

    Enables/disables fill legends in 3D Graphics window for Volumetric object.

.. py:property:: boundary_legend
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.boundary_legend
    :type: "IAgVmVOLegend"

    Get the 3D Graphics properties for Volumetric Boundary Legend.

.. py:property:: fill_legend
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.fill_legend
    :type: "IAgVmVOLegend"

    Get the 3D Graphics properties for Volumetric Fill Legend.

.. py:property:: volume_type
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.volume_type
    :type: "VM_DISPLAY_VOLUME_TYPE"

    Sets/gets the graphics volume display type.


