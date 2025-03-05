SensorProjection
================

.. py:class:: ansys.stk.core.stkobjects.SensorProjection

   Class defining the projection properties of a Sensor.

.. py:currentmodule:: SensorProjection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.available_constraints`
              - Return the available constraints.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.enabled_constraints`
              - Return the enabled constraints.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.enable_constraint`
              - Enable the constraint with the name given.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.disable_constraint`
              - Disables the constraint with the name given.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.available_altitude_objects`
              - Return the available altitude objects.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.persistence`
              - Length of time the sensor's footprint remains visible during animation. Used to display sensor footprints for a specified period of time so that you can determine quickly and easily whether coverage requirements are being met. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.forward_persistence`
              - Specify whether persistence is to apply in a forward animation direction only.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.project_at_altitude_object`
              - The altitude of the object to which the sensor is projected (if this option for setting projection distance is selected).
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.intersection_type`
              - The type of intersections to be shown. A member of the AgEIntersectionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.distance_type`
              - The criterion used for determining the projection distance. A member of the AgESnProjectionDistanceType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.distance_data`
              - Value of the criterion used for determining the projection distance.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.fill_persistence`
              - Specify whether to display the sensor's footprints as filled areas on the surface of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.use_constraints`
              - Specify whether to evaluate the effect of various constraints on visibility along all possible lines of sight within the field of view.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.show_on_2d_map`
              - Show Projection on 2D map.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.use_distance`
              - Opt whether the sensor's field-of-view crossings at specified distances are to be computed and displayed in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorProjection.display_times_hides_persistence`
              - Specify whether to allow display times to affect the sensor's persistence on/off state.



Examples
--------

Sensor Persistence

.. code-block:: python

    # Sensor sensor: Sensor object
    projection = sensor.graphics.projection
    projection.persistence = 7200  # sec
    projection.forward_persistence = True
    projection.fill_persistence = True
    sensor.graphics.show_fill = True
    sensor.graphics.percent_translucency = 50


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorProjection


Property detail
---------------

.. py:property:: persistence
    :canonical: ansys.stk.core.stkobjects.SensorProjection.persistence
    :type: float

    Length of time the sensor's footprint remains visible during animation. Used to display sensor footprints for a specified period of time so that you can determine quickly and easily whether coverage requirements are being met. Uses Time Dimension.

.. py:property:: forward_persistence
    :canonical: ansys.stk.core.stkobjects.SensorProjection.forward_persistence
    :type: bool

    Specify whether persistence is to apply in a forward animation direction only.

.. py:property:: project_at_altitude_object
    :canonical: ansys.stk.core.stkobjects.SensorProjection.project_at_altitude_object
    :type: str

    The altitude of the object to which the sensor is projected (if this option for setting projection distance is selected).

.. py:property:: intersection_type
    :canonical: ansys.stk.core.stkobjects.SensorProjection.intersection_type
    :type: IntersectionType

    The type of intersections to be shown. A member of the AgEIntersectionType enumeration.

.. py:property:: distance_type
    :canonical: ansys.stk.core.stkobjects.SensorProjection.distance_type
    :type: SensorProjectionDistanceType

    The criterion used for determining the projection distance. A member of the AgESnProjectionDistanceType enumeration.

.. py:property:: distance_data
    :canonical: ansys.stk.core.stkobjects.SensorProjection.distance_data
    :type: IDisplayDistance

    Value of the criterion used for determining the projection distance.

.. py:property:: fill_persistence
    :canonical: ansys.stk.core.stkobjects.SensorProjection.fill_persistence
    :type: bool

    Specify whether to display the sensor's footprints as filled areas on the surface of the central body.

.. py:property:: use_constraints
    :canonical: ansys.stk.core.stkobjects.SensorProjection.use_constraints
    :type: bool

    Specify whether to evaluate the effect of various constraints on visibility along all possible lines of sight within the field of view.

.. py:property:: show_on_2d_map
    :canonical: ansys.stk.core.stkobjects.SensorProjection.show_on_2d_map
    :type: bool

    Show Projection on 2D map.

.. py:property:: use_distance
    :canonical: ansys.stk.core.stkobjects.SensorProjection.use_distance
    :type: bool

    Opt whether the sensor's field-of-view crossings at specified distances are to be computed and displayed in the 2D Graphics window.

.. py:property:: display_times_hides_persistence
    :canonical: ansys.stk.core.stkobjects.SensorProjection.display_times_hides_persistence
    :type: bool

    Specify whether to allow display times to affect the sensor's persistence on/off state.


Method detail
-------------
















.. py:method:: available_constraints(self) -> list
    :canonical: ansys.stk.core.stkobjects.SensorProjection.available_constraints

    Return the available constraints.

    :Returns:

        :obj:`~list`

.. py:method:: enabled_constraints(self) -> list
    :canonical: ansys.stk.core.stkobjects.SensorProjection.enabled_constraints

    Return the enabled constraints.

    :Returns:

        :obj:`~list`

.. py:method:: enable_constraint(self, constraint_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.SensorProjection.enable_constraint

    Enable the constraint with the name given.

    :Parameters:

    **constraint_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: disable_constraint(self, constraint_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.SensorProjection.disable_constraint

    Disables the constraint with the name given.

    :Parameters:

    **constraint_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: available_altitude_objects(self) -> list
    :canonical: ansys.stk.core.stkobjects.SensorProjection.available_altitude_objects

    Return the available altitude objects.

    :Returns:

        :obj:`~list`







