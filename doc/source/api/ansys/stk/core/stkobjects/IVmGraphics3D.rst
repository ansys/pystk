IVmGraphics3D
=============

.. py:class:: ansys.stk.core.stkobjects.IVmGraphics3D

   object
   
   IAgVmVO Interface for a volumetric object's 3D Graphics properties.

.. py:currentmodule:: IVmGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.smoothing`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.shading`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.quality`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.grid`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.cross_section`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.volume`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.show_boundary_legend`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.show_fill_legend`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.boundary_legend`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.fill_legend`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVmGraphics3D.volume_type`


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
    :type: VM_DISPLAY_QUALITY_TYPE

    Sets/gets the quality of the graphics display.

.. py:property:: grid
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.grid
    :type: IVmGraphics3DGrid

    Get the Grid properties of 3D Graphics window for the volumetric object.

.. py:property:: cross_section
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.cross_section
    :type: IVmGraphics3DCrossSection

    Get the 3D Graphics properties for planar cross-sections through the volumetric grid.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.volume
    :type: IVmGraphics3DVolume

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
    :type: IVmGraphics3DLegend

    Get the 3D Graphics properties for Volumetric Boundary Legend.

.. py:property:: fill_legend
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.fill_legend
    :type: IVmGraphics3DLegend

    Get the 3D Graphics properties for Volumetric Fill Legend.

.. py:property:: volume_type
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3D.volume_type
    :type: VM_DISPLAY_VOLUME_TYPE

    Sets/gets the graphics volume display type.


