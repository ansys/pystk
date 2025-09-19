SensorProjectionDistanceType
============================

.. py:class:: ansys.stk.core.stkobjects.SensorProjectionDistanceType

   IntEnum


.. py:currentmodule:: SensorProjectionDistanceType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CONSTANT_ALTITUDE`
              - Constant altitude: projects the sensor to one or more altitudes above the facility/place/target, measured along the normal to the surface of the parent.

            * - :py:attr:`~CONSTANT_RANGE_FROM_PARENT`
              - Constant range from parent object: projects the sensor to one or more ranges from the parent facility/place/target.

            * - :py:attr:`~OBJECT_ALTITUDE`
              - Object altitude: projects the sensor to the altitude of a selected vehicle.

            * - :py:attr:`~RANGE_CONSTRAINT`
              - Range constraint: projects the sensor to a specified range constraint for the facility, place or target.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorProjectionDistanceType


