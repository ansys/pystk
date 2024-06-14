ICoverageGraphics3DAttributes
=============================

.. py:class:: ICoverageGraphics3DAttributes

   object
   
   3D animation or static graphics options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~translucency`
            * - :py:meth:`~point_size`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGraphics3DAttributes


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3DAttributes.is_visible
    :type: bool

    Show Animation Graphics: specify whether to display coverage data for all points based on evaluation over the entire coverage interval.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3DAttributes.translucency
    :type: float

    Animation Translucency Percentage: the translucency of the static graphics when grid points are filled. Dimensionless.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3DAttributes.point_size
    :type: float

    Animation Point Size: the size of a grid point for static graphics when grid points are not filled. Dimensionless.


