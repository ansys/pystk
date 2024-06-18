IChainGraphics
==============

.. py:class:: IChainGraphics

   object
   
   2D graphics properties of a chain.

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
            * - :py:meth:`~is_object_graphics_visible`
            * - :py:meth:`~is_object_graphics_visible_in_2d`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IChainGraphics


Property detail
---------------

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.IChainGraphics.static
    :type: "IAgChGfxStatic"

    Get the chain's 2D static graphics properties.

.. py:property:: animation
    :canonical: ansys.stk.core.stkobjects.IChainGraphics.animation
    :type: "IAgChGfxAnimation"

    Get the chain's 3D graphics properties.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IChainGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the chain are visible.

.. py:property:: is_object_graphics_visible_in_2d
    :canonical: ansys.stk.core.stkobjects.IChainGraphics.is_object_graphics_visible_in_2d
    :type: bool

    Specify whether graphics attributes of the chain are visible in 2D Windows.


