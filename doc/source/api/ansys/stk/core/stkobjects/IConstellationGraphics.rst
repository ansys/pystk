IConstellationGraphics
======================

.. py:class:: ansys.stk.core.stkobjects.IConstellationGraphics

   object
   
   Graphics options for constellation.

.. py:currentmodule:: IConstellationGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationGraphics.hide_graphics`
              - Remove the graphics for all objects within the constellation from the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellationGraphics.restore_graphics`
              - Restore the graphics for all objects within the constellation in the 2D Graphics window.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IConstellationGraphics



Method detail
-------------

.. py:method:: hide_graphics(self) -> None
    :canonical: ansys.stk.core.stkobjects.IConstellationGraphics.hide_graphics

    Remove the graphics for all objects within the constellation from the 2D Graphics window.

    :Returns:

        :obj:`~None`

.. py:method:: restore_graphics(self) -> None
    :canonical: ansys.stk.core.stkobjects.IConstellationGraphics.restore_graphics

    Restore the graphics for all objects within the constellation in the 2D Graphics window.

    :Returns:

        :obj:`~None`

