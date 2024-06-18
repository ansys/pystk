ISensorProjection
=================

.. py:class:: ISensorProjection

   object
   
   IAgSnProjection Interface for setting and retrieving 2D Graphics Projection properties for a sensor.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~available_constraints`
              - Return the available constraints.
            * - :py:meth:`~enabled_constraints`
              - Return the enabled constraints.
            * - :py:meth:`~enable_constraint`
              - Enable the constraint with the name given.
            * - :py:meth:`~disable_constraint`
              - Disables the constraint with the name given.
            * - :py:meth:`~available_altitude_objects`
              - Return the available altitude objects.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~persistence`
            * - :py:meth:`~forward_persistence`
            * - :py:meth:`~project_at_altitude_object`
            * - :py:meth:`~intersection_type`
            * - :py:meth:`~distance_type`
            * - :py:meth:`~distance_data`
            * - :py:meth:`~fill_persistence`
            * - :py:meth:`~use_constraints`
            * - :py:meth:`~show_on_2d_map`
            * - :py:meth:`~use_distance`
            * - :py:meth:`~display_times_hides_persistance`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorProjection


Property detail
---------------

.. py:property:: persistence
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.persistence
    :type: float

    Length of time the sensor's footprint remains visible during animation. Used to display sensor footprints for a specified period of time so that you can determine quickly and easily whether coverage requirements are being met. Uses Time Dimension.

.. py:property:: forward_persistence
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.forward_persistence
    :type: bool

    Specify whether persistence is to apply in a forward animation direction only.

.. py:property:: project_at_altitude_object
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.project_at_altitude_object
    :type: str

    The altitude of the object to which the sensor is projected (if this option for setting projection distance is selected).

.. py:property:: intersection_type
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.intersection_type
    :type: "INTERSECTION_TYPE"

    The type of intersections to be shown. A member of the AgEIntersectionType enumeration.

.. py:property:: distance_type
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.distance_type
    :type: "SENSOR_PROJECTION_DISTANCE_TYPE"

    The criterion used for determining the projection distance. A member of the AgESnProjectionDistanceType enumeration.

.. py:property:: distance_data
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.distance_data
    :type: "IAgDisplayDistance"

    Value of the criterion used for determining the projection distance.

.. py:property:: fill_persistence
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.fill_persistence
    :type: bool

    Specify whether to display the sensor's footprints as filled areas on the surface of the central body.

.. py:property:: use_constraints
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.use_constraints
    :type: bool

    Specify whether to evaluate the effect of various constraints on visibility along all possible lines of sight within the field of view.

.. py:property:: show_on_2d_map
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.show_on_2d_map
    :type: bool

    Show Projection on 2D map.

.. py:property:: use_distance
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.use_distance
    :type: bool

    Opt whether the sensor's field-of-view crossings at specified distances are to be computed and displayed in the 2D Graphics window.

.. py:property:: display_times_hides_persistance
    :canonical: ansys.stk.core.stkobjects.ISensorProjection.display_times_hides_persistance
    :type: bool

    Specify whether to allow display times to affect the sensor's persistence on/off state.


Method detail
-------------
















.. py:method:: available_constraints(self) -> list

    Return the available constraints.

    :Returns:

        :obj:`~list`

.. py:method:: enabled_constraints(self) -> list

    Return the enabled constraints.

    :Returns:

        :obj:`~list`

.. py:method:: enable_constraint(self, constraintName:str) -> None

    Enable the constraint with the name given.

    :Parameters:

    **constraintName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: disable_constraint(self, constraintName:str) -> None

    Disables the constraint with the name given.

    :Parameters:

    **constraintName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: available_altitude_objects(self) -> list

    Return the available altitude objects.

    :Returns:

        :obj:`~list`







