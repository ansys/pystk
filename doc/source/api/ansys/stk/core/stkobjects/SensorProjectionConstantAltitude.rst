SensorProjectionConstantAltitude
================================

.. py:class:: ansys.stk.core.stkobjects.SensorProjectionConstantAltitude

   Bases: :py:class:`~ansys.stk.core.stkobjects.IDisplayDistance`, :py:class:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance`

   Class defining projection altitude options for constant altitude for a sensor.

.. py:currentmodule:: SensorProjectionConstantAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.min`
              - Minimum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.max`
              - Maximum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.number_of_steps`
              - Step count. Determines the interval between sensor projections. For a specified min/max altitude: the step count determines the number and altitude of projections to be displayed. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.projects_thru_crossing`
              - Specify whether the sensor's field-of-view will extend beyond specified crossings.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.altitude_crossing_sides`
              - Indicates which crossings are computed and displayed in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.direction`
              - Indicates the direction in which the sensor's field of view crosses the specified altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.exclude_horizon_arcs`
              - Specify whether to exclude horizon arcs.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorProjectionConstantAltitude


Property detail
---------------

.. py:property:: min
    :canonical: ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.min
    :type: float

    Minimum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.

.. py:property:: max
    :canonical: ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.max
    :type: float

    Maximum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.

.. py:property:: number_of_steps
    :canonical: ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.number_of_steps
    :type: int

    Step count. Determines the interval between sensor projections. For a specified min/max altitude: the step count determines the number and altitude of projections to be displayed. Dimensionless.

.. py:property:: projects_thru_crossing
    :canonical: ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.projects_thru_crossing
    :type: bool

    Specify whether the sensor's field-of-view will extend beyond specified crossings.

.. py:property:: altitude_crossing_sides
    :canonical: ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.altitude_crossing_sides
    :type: SENSOR_ALTITUDE_CROSSING_SIDES

    Indicates which crossings are computed and displayed in the 2D Graphics window.

.. py:property:: direction
    :canonical: ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.direction
    :type: SENSOR_ALTITUDE_CROSSING_DIRECTION

    Indicates the direction in which the sensor's field of view crosses the specified altitude.

.. py:property:: exclude_horizon_arcs
    :canonical: ansys.stk.core.stkobjects.SensorProjectionConstantAltitude.exclude_horizon_arcs
    :type: bool

    Specify whether to exclude horizon arcs.


