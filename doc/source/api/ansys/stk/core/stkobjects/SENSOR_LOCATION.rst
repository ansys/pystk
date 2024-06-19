SENSOR_LOCATION
===============

.. py:class:: SENSOR_LOCATION

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FIXED`
              - Fixed: the location of the sensor is defined using a fixed displacement vector with respect to the parent objects body frame.

            * - :py:attr:`~MODEL_3D`
              - 3D Model: the location of the sensor is defined using the sensor's 3D Graphics Vertex Offset properties.

            * - :py:attr:`~MODEL_3D_WITH_SCALE`
              - 3D Model with Scale: the location of the sensor is defined using the sensor's 3D Graphics Vertex Offset properties. Location is computed using the scaled model defined for visualization.

            * - :py:attr:`~CENTER`
              - Center: the sensor is located at the center of its parent object.

            * - :py:attr:`~VECTOR_GEOMETRY_TOOL_POINT`
              - Point: the sensor's location is based upon a Vector Geometry Tool point.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SENSOR_LOCATION


