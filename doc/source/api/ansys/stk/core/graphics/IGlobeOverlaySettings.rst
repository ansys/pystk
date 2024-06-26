IGlobeOverlaySettings
=====================

.. py:class:: ansys.stk.core.graphics.IGlobeOverlaySettings

   object
   
   Settings used by globe overlay objects. These setting affect all scenes.

.. py:currentmodule:: IGlobeOverlaySettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlaySettings.terrain_cache_size`
              - Gets or sets the size of the terrain cache in megabytes. It is not recommended to go above 128 megabytes. Large cache sizes can slow down rendering since so much imagery will be rendered.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlaySettings.imagery_cache_size`
              - Gets or sets the size of the imagery cache in megabytes. It is not recommended to go above 128 megabytes. Large cache sizes can slow down rendering since so much imagery will be rendered.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlaySettings.preload_terrain_and_imagery`
              - Gets or sets whether terrain and imagery are preloaded. When set to true, terrain and imagery are preloaded to get the best visual quality; when set to false, they are not preloaded...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGlobeOverlaySettings


Property detail
---------------

.. py:property:: terrain_cache_size
    :canonical: ansys.stk.core.graphics.IGlobeOverlaySettings.terrain_cache_size
    :type: int

    Gets or sets the size of the terrain cache in megabytes. It is not recommended to go above 128 megabytes. Large cache sizes can slow down rendering since so much imagery will be rendered.

.. py:property:: imagery_cache_size
    :canonical: ansys.stk.core.graphics.IGlobeOverlaySettings.imagery_cache_size
    :type: int

    Gets or sets the size of the imagery cache in megabytes. It is not recommended to go above 128 megabytes. Large cache sizes can slow down rendering since so much imagery will be rendered.

.. py:property:: preload_terrain_and_imagery
    :canonical: ansys.stk.core.graphics.IGlobeOverlaySettings.preload_terrain_and_imagery
    :type: bool

    Gets or sets whether terrain and imagery are preloaded. When set to true, terrain and imagery are preloaded to get the best visual quality; when set to false, they are not preloaded...


