ISensorPointingTargetedBoresightTrack
=====================================

.. py:class:: ISensorPointingTargetedBoresightTrack

   object
   
   IAgSnPtTrgtBsightTrack Interface for targeted sensor with fixed boresight.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~about_boresight`
            * - :py:meth:`~track_mode`
            * - :py:meth:`~constraint_vector_for_up_vector_boresight`
            * - :py:meth:`~available_constraint_vectors`
            * - :py:meth:`~clock_angle_offset_for_up_vector_boresight`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorPointingTargetedBoresightTrack


Property detail
---------------

.. py:property:: about_boresight
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargetedBoresightTrack.about_boresight
    :type: "BORESIGHT_TYPE"

    The orientation of the antenna's X and Y axes with respect to the parent's reference frame. (The Z axis always coincides with its boresight direction and is unambiguously defined by the azimuth and elevation.

.. py:property:: track_mode
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargetedBoresightTrack.track_mode
    :type: "TRACK_MODE_TYPE"

    The antenna orientation option for the sensor. A member of the AgETrackModeType enumeration.

.. py:property:: constraint_vector_for_up_vector_boresight
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargetedBoresightTrack.constraint_vector_for_up_vector_boresight
    :type: str

    Gets or sets the constraint vector for UpVector boresight type.

.. py:property:: available_constraint_vectors
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargetedBoresightTrack.available_constraint_vectors
    :type: list

    Get the available constraint vectors.

.. py:property:: clock_angle_offset_for_up_vector_boresight
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargetedBoresightTrack.clock_angle_offset_for_up_vector_boresight
    :type: typing.Any

    Gets or sets the clock angle offset for UpVector boresight type. It is an optional value measured in the Sensor Body axes xy-plane, positive about the boresight, locating the direction closest to the ConstraintVector from the Sensor Body x-axis.


