ICoverageGraphics
=================

.. py:class:: ICoverageGraphics

   object
   
   2D graphics display options for the coverage grid.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~static`
            * - :py:meth:`~animation`
            * - :py:meth:`~progress`
            * - :py:meth:`~is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGraphics


Property detail
---------------

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics.static
    :type: "IAgCvGfxStatic"

    2D static graphics options.

.. py:property:: animation
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics.animation
    :type: "IAgCvGfxAnimation"

    2D animation graphics options.

.. py:property:: progress
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics.progress
    :type: "IAgCvGfxProgress"

    Access progress graphics options.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the coverage definition are visible.


