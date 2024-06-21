SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE
==================================================

.. py:class:: ansys.stk.core.stkobjects.SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE

   IntEnum


.. py:currentmodule:: SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CONSTANT`
              - Use a constant length at all times. This length can be set with the SpaceProjection or Targeting property on the IAgSnVO interface depending on the sensor's pointing settings.

            * - :py:attr:`~TIME_VARYING`
              - Use a user provided list of times and lengths. The times and lengths can be set with the ProjectionIntervals or TargetProjectionIntervals property on the IAgSnVO interface depending on the sensor's pointing settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE


