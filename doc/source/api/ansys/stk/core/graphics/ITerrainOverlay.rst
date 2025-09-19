ITerrainOverlay
===============

.. py:class:: ansys.stk.core.graphics.ITerrainOverlay

   A globe overlay which shows terrain.

.. py:currentmodule:: ITerrainOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITerrainOverlay.altitude_offset`
              - Get or set the value from which to offset the terrain height.
            * - :py:attr:`~ansys.stk.core.graphics.ITerrainOverlay.altitude_scale`
              - Get or set the value from which to scale the terrain height.
            * - :py:attr:`~ansys.stk.core.graphics.ITerrainOverlay.supported`
              - Get whether the video card supports adding terrain overlay objects. Video cards that support OpenGL 1.2 or higher support terrain overlay objects.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITerrainOverlay


Property detail
---------------

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.graphics.ITerrainOverlay.altitude_offset
    :type: float

    Get or set the value from which to offset the terrain height.

.. py:property:: altitude_scale
    :canonical: ansys.stk.core.graphics.ITerrainOverlay.altitude_scale
    :type: float

    Get or set the value from which to scale the terrain height.

.. py:property:: supported
    :canonical: ansys.stk.core.graphics.ITerrainOverlay.supported
    :type: bool

    Get whether the video card supports adding terrain overlay objects. Video cards that support OpenGL 1.2 or higher support terrain overlay objects.


