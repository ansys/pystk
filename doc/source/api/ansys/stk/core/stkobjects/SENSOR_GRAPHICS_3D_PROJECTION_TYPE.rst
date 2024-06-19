SENSOR_GRAPHICS_3D_PROJECTION_TYPE
==================================

.. py:class:: SENSOR_GRAPHICS_3D_PROJECTION_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~PROJECTION_ALL_INTERSECTIONS`
              - All intersections: the entire sensor projection is displayed.

            * - :py:attr:`~PROJECTION_EARTH_INTERSECTIONS`
              - Earth intersections: 0nly the portion of the sensor projection that intersects the Earth is displayed.

            * - :py:attr:`~PROJECTION_NONE`
              - None: no projection is displayed for sensors attached to facilities. For other objects, the part of the sensor projection that does not intersect with the central body is displayed.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SENSOR_GRAPHICS_3D_PROJECTION_TYPE


