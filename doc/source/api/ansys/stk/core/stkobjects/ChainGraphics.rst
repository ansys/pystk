ChainGraphics
=============

.. py:class:: ansys.stk.core.stkobjects.ChainGraphics

   2D graphics properties of a chain.

.. py:currentmodule:: ChainGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics.animation_settings`
              - Get the chain's 3D graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics.show_graphics`
              - Specify whether graphics attributes of the chain are visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics.show_graphics_2d`
              - Specify whether graphics attributes of the chain are visible in 2D Windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics.static`
              - Get the chain's 2D static graphics properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainGraphics


Property detail
---------------

.. py:property:: animation_settings
    :canonical: ansys.stk.core.stkobjects.ChainGraphics.animation_settings
    :type: ChainGraphics2DAnimation

    Get the chain's 3D graphics properties.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.ChainGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the chain are visible.

.. py:property:: show_graphics_2d
    :canonical: ansys.stk.core.stkobjects.ChainGraphics.show_graphics_2d
    :type: bool

    Specify whether graphics attributes of the chain are visible in 2D Windows.

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.ChainGraphics.static
    :type: ChainGraphics2DStatic

    Get the chain's 2D static graphics properties.


