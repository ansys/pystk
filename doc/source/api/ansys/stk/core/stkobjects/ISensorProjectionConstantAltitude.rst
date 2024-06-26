ISensorProjectionConstantAltitude
=================================

.. py:class:: ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude

   object
   
   IAgSnProjConstantAlt Interface for setting projection altitude options for constant altitude for a sensor.

.. py:currentmodule:: ISensorProjectionConstantAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.min`
              - Minimum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.max`
              - Maximum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.number_of_steps`
              - Step count. Determines the interval between sensor projections. For a specified min/max altitude: the step count determines the number and altitude of projections to be displayed. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.projects_thru_crossing`
              - Specify whether the sensor's field-of-view will extend beyond specified crossings.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.altitude_crossing_sides`
              - Indicates which crossings are computed and displayed in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.direction`
              - Indicates the direction in which the sensor's field of view crosses the specified altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.exclude_horizon_arcs`
              - Specify whether to exclude horizon arcs.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorProjectionConstantAltitude


Property detail
---------------

.. py:property:: min
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.min
    :type: float

    Minimum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.

.. py:property:: max
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.max
    :type: float

    Maximum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.

.. py:property:: number_of_steps
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.number_of_steps
    :type: int

    Step count. Determines the interval between sensor projections. For a specified min/max altitude: the step count determines the number and altitude of projections to be displayed. Dimensionless.

.. py:property:: projects_thru_crossing
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.projects_thru_crossing
    :type: bool

    Specify whether the sensor's field-of-view will extend beyond specified crossings.

.. py:property:: altitude_crossing_sides
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.altitude_crossing_sides
    :type: SENSOR_ALTITUDE_CROSSING_SIDES

    Indicates which crossings are computed and displayed in the 2D Graphics window.

.. py:property:: direction
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.direction
    :type: SENSOR_ALTITUDE_CROSSING_DIRECTION

    Indicates the direction in which the sensor's field of view crosses the specified altitude.

.. py:property:: exclude_horizon_arcs
    :canonical: ansys.stk.core.stkobjects.ISensorProjectionConstantAltitude.exclude_horizon_arcs
    :type: bool

    Specify whether to exclude horizon arcs.


