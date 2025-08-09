GlobeOverlaySettings
====================

.. py:class:: ansys.stk.core.graphics.GlobeOverlaySettings

   Settings used by globe overlay objects. These setting affect all scenes.

.. py:currentmodule:: GlobeOverlaySettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.GlobeOverlaySettings.terrain_cache_size`
              - Get or set the size of the terrain cache in megabytes. It is not recommended to go above 128 megabytes. Large cache sizes can slow down rendering since so much imagery will be rendered.
            * - :py:attr:`~ansys.stk.core.graphics.GlobeOverlaySettings.imagery_cache_size`
              - Get or set the size of the imagery cache in megabytes. It is not recommended to go above 128 megabytes. Large cache sizes can slow down rendering since so much imagery will be rendered.
            * - :py:attr:`~ansys.stk.core.graphics.GlobeOverlaySettings.preload_terrain_and_imagery`
              - Get or set whether terrain and imagery are preloaded. When set to true, terrain and imagery are preloaded to get the best visual quality; when set to false, they are not preloaded...



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import GlobeOverlaySettings


Property detail
---------------

.. py:property:: terrain_cache_size
    :canonical: ansys.stk.core.graphics.GlobeOverlaySettings.terrain_cache_size
    :type: int

    Get or set the size of the terrain cache in megabytes. It is not recommended to go above 128 megabytes. Large cache sizes can slow down rendering since so much imagery will be rendered.

.. py:property:: imagery_cache_size
    :canonical: ansys.stk.core.graphics.GlobeOverlaySettings.imagery_cache_size
    :type: int

    Get or set the size of the imagery cache in megabytes. It is not recommended to go above 128 megabytes. Large cache sizes can slow down rendering since so much imagery will be rendered.

.. py:property:: preload_terrain_and_imagery
    :canonical: ansys.stk.core.graphics.GlobeOverlaySettings.preload_terrain_and_imagery
    :type: bool

    Get or set whether terrain and imagery are preloaded. When set to true, terrain and imagery are preloaded to get the best visual quality; when set to false, they are not preloaded...


