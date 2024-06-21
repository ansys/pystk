SENSOR_GRAPHICS_3D_INHERIT_FROM_2D
==================================

.. py:class:: ansys.stk.core.stkobjects.SENSOR_GRAPHICS_3D_INHERIT_FROM_2D

   IntEnum


.. py:currentmodule:: SENSOR_GRAPHICS_3D_INHERIT_FROM_2D

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown.

            * - :py:attr:`~NO`
              - Crossings and distances defined for the 2D Graphics window are ignored in the 3D Graphics window.

            * - :py:attr:`~YES`
              - All crossings and distances defined for the 2D Graphics window are displayed in the 3D Graphics window.

            * - :py:attr:`~EXTENT_ONLY`
              - Only the highest altitude/farthest range crossings and distances defined for the 2D Graphics window are displayed in the 3D Graphics window.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SENSOR_GRAPHICS_3D_INHERIT_FROM_2D


