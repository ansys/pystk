ITerrainOverlay
===============

.. py:class:: ITerrainOverlay

   object
   
   A globe overlay which shows terrain.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_offset`
            * - :py:meth:`~altitude_scale`
            * - :py:meth:`~supported`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITerrainOverlay


Property detail
---------------

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.graphics.ITerrainOverlay.altitude_offset
    :type: float

    Gets or sets the value from which to offset the terrain height.

.. py:property:: altitude_scale
    :canonical: ansys.stk.core.graphics.ITerrainOverlay.altitude_scale
    :type: float

    Gets or sets the value from which to scale the terrain height.

.. py:property:: supported
    :canonical: ansys.stk.core.graphics.ITerrainOverlay.supported
    :type: bool

    Gets whether the video card supports adding terrain overlay objects. Video cards that support OpenGL 1.2 or higher support terrain overlay objects.


