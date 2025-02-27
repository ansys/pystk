VolumetricGraphics3D
====================

.. py:class:: ansys.stk.core.stkobjects.VolumetricGraphics3D

   Class defining 3D graphics properties of volumetric object.

.. py:currentmodule:: VolumetricGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.visible`
              - Display volumetric object including Grid, Volume, and Cross Sections in 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.smoothing`
              - Enable to smooth out the volume and surface boundaries using interpolation between grid points.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.shading`
              - Enable to add shading to the boundary surface. Shading slows down animation but generates helpful lighting effects based on surfaces.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.quality`
              - Get or set the quality of the graphics display.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.grid`
              - Get the Grid properties of 3D Graphics window for the volumetric object.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.cross_section`
              - Get the 3D Graphics properties for planar cross-sections through the volumetric grid.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.volume`
              - Get the 3D Graphics properties for Volume.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.show_boundary_legend`
              - Enable/disable boundary legends in 3D Graphics window for Volumetric object.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.show_fill_legend`
              - Enable/disable fill legends in 3D Graphics window for Volumetric object.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.boundary_legend`
              - Get the 3D Graphics properties for Volumetric Boundary Legend.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.fill_legend`
              - Get the 3D Graphics properties for Volumetric Fill Legend.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3D.volume_type`
              - Get or set the graphics volume display type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VolumetricGraphics3D


Property detail
---------------

.. py:property:: visible
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.visible
    :type: bool

    Display volumetric object including Grid, Volume, and Cross Sections in 3D Graphics window.

.. py:property:: smoothing
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.smoothing
    :type: bool

    Enable to smooth out the volume and surface boundaries using interpolation between grid points.

.. py:property:: shading
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.shading
    :type: bool

    Enable to add shading to the boundary surface. Shading slows down animation but generates helpful lighting effects based on surfaces.

.. py:property:: quality
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.quality
    :type: VolumetricDisplayQualityType

    Get or set the quality of the graphics display.

.. py:property:: grid
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.grid
    :type: VolumetricGraphics3DGrid

    Get the Grid properties of 3D Graphics window for the volumetric object.

.. py:property:: cross_section
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.cross_section
    :type: VolumetricGraphics3DCrossSection

    Get the 3D Graphics properties for planar cross-sections through the volumetric grid.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.volume
    :type: VolumetricGraphics3DVolume

    Get the 3D Graphics properties for Volume.

.. py:property:: show_boundary_legend
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.show_boundary_legend
    :type: bool

    Enable/disable boundary legends in 3D Graphics window for Volumetric object.

.. py:property:: show_fill_legend
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.show_fill_legend
    :type: bool

    Enable/disable fill legends in 3D Graphics window for Volumetric object.

.. py:property:: boundary_legend
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.boundary_legend
    :type: VolumetricGraphics3DLegend

    Get the 3D Graphics properties for Volumetric Boundary Legend.

.. py:property:: fill_legend
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.fill_legend
    :type: VolumetricGraphics3DLegend

    Get the 3D Graphics properties for Volumetric Fill Legend.

.. py:property:: volume_type
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3D.volume_type
    :type: VolumetricDisplayVolumeType

    Get or set the graphics volume display type.


