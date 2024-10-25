CoverageGraphics3DAttributes
============================

.. py:class:: ansys.stk.core.stkobjects.CoverageGraphics3DAttributes

   3D animation or static graphics options.

.. py:currentmodule:: CoverageGraphics3DAttributes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3DAttributes.show_graphics`
              - Show Animation Graphics: specify whether to display coverage data for all points based on evaluation over the entire coverage interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3DAttributes.translucency`
              - Animation Translucency Percentage: the translucency of the static graphics when grid points are filled. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3DAttributes.point_size`
              - Animation Point Size: the size of a grid point for static graphics when grid points are not filled. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageGraphics3DAttributes


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3DAttributes.show_graphics
    :type: bool

    Show Animation Graphics: specify whether to display coverage data for all points based on evaluation over the entire coverage interval.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3DAttributes.translucency
    :type: float

    Animation Translucency Percentage: the translucency of the static graphics when grid points are filled. Dimensionless.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3DAttributes.point_size
    :type: float

    Animation Point Size: the size of a grid point for static graphics when grid points are not filled. Dimensionless.


