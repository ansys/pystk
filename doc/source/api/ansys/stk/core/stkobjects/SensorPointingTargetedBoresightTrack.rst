SensorPointingTargetedBoresightTrack
====================================

.. py:class:: ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPointingTargetedBoresight`

   Class defining a targeted sensor with tracking boresight.

.. py:currentmodule:: SensorPointingTargetedBoresightTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.about_boresight`
              - The orientation of the antenna's X and Y axes with respect to the parent's reference frame. (The Z axis always coincides with its boresight direction and is unambiguously defined by the azimuth and elevation.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.track_mode`
              - The antenna orientation option for the sensor. A member of the AgETrackModeType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.constraint_vector_for_up_vector_boresight`
              - Gets or sets the constraint vector for UpVector boresight type.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.available_constraint_vectors`
              - Get the available constraint vectors.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.clock_angle_offset_for_up_vector_boresight`
              - Gets or sets the clock angle offset for UpVector boresight type. It is an optional value measured in the Sensor Body axes xy-plane, positive about the boresight, locating the direction closest to the ConstraintVector from the Sensor Body x-axis.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorPointingTargetedBoresightTrack


Property detail
---------------

.. py:property:: about_boresight
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.about_boresight
    :type: BORESIGHT_TYPE

    The orientation of the antenna's X and Y axes with respect to the parent's reference frame. (The Z axis always coincides with its boresight direction and is unambiguously defined by the azimuth and elevation.

.. py:property:: track_mode
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.track_mode
    :type: TRACK_MODE_TYPE

    The antenna orientation option for the sensor. A member of the AgETrackModeType enumeration.

.. py:property:: constraint_vector_for_up_vector_boresight
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.constraint_vector_for_up_vector_boresight
    :type: str

    Gets or sets the constraint vector for UpVector boresight type.

.. py:property:: available_constraint_vectors
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.available_constraint_vectors
    :type: list

    Get the available constraint vectors.

.. py:property:: clock_angle_offset_for_up_vector_boresight
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack.clock_angle_offset_for_up_vector_boresight
    :type: typing.Any

    Gets or sets the clock angle offset for UpVector boresight type. It is an optional value measured in the Sensor Body axes xy-plane, positive about the boresight, locating the direction closest to the ConstraintVector from the Sensor Body x-axis.


