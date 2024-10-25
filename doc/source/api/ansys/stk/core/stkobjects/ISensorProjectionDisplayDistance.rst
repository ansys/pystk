ISensorProjectionDisplayDistance
================================

.. py:class:: ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance

   IAgSnProjDisplayDistance Interface for setting projection altitude options for a sensor.

.. py:currentmodule:: ISensorProjectionDisplayDistance

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.minimum`
              - Minimum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.maximum`
              - Maximum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.number_of_steps`
              - Step count. Determines the interval between sensor projections. For a specified min/max altitude: the step count determines the number and altitude of projections to be displayed. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.projects_thru_crossing`
              - Specify whether the sensor's field-of-view will extend beyond specified crossings.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.altitude_crossing_sides`
              - Indicates which crossings are computed and displayed in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.direction`
              - Indicates the direction in which the sensor's field of view crosses the specified altitude.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorProjectionDisplayDistance


Property detail
---------------

.. py:property:: minimum
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.minimum
    :type: float

    Minimum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.

.. py:property:: maximum
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.maximum
    :type: float

    Maximum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.

.. py:property:: number_of_steps
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.number_of_steps
    :type: int

    Step count. Determines the interval between sensor projections. For a specified min/max altitude: the step count determines the number and altitude of projections to be displayed. Dimensionless.

.. py:property:: projects_thru_crossing
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.projects_thru_crossing
    :type: bool

    Specify whether the sensor's field-of-view will extend beyond specified crossings.

.. py:property:: altitude_crossing_sides
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.altitude_crossing_sides
    :type: SENSOR_ALTITUDE_CROSSING_SIDE_TYPE

    Indicates which crossings are computed and displayed in the 2D Graphics window.

.. py:property:: direction
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance.direction
    :type: SENSOR_ALTITUDE_CROSSING_DIRECTION

    Indicates the direction in which the sensor's field of view crosses the specified altitude.


