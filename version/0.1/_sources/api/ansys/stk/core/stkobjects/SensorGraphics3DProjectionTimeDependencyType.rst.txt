SensorGraphics3DProjectionTimeDependencyType
============================================

.. py:class:: ansys.stk.core.stkobjects.SensorGraphics3DProjectionTimeDependencyType

   IntEnum


.. py:currentmodule:: SensorGraphics3DProjectionTimeDependencyType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CONSTANT`
              - Use a constant length at all times. This length can be set with the SpaceProjection or Targeting property on the SensorGraphics3D interface depending on the sensor's pointing settings.

            * - :py:attr:`~TIME_VARYING`
              - Use a user provided list of times and lengths. The times and lengths can be set with the ProjectionIntervals or TargetProjectionIntervals property on the SensorGraphics3D interface depending on the sensor's pointing settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorGraphics3DProjectionTimeDependencyType


