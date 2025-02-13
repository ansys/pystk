MTOTrackPoint
=============

.. py:class:: ansys.stk.core.stkobjects.MTOTrackPoint

   The points defined for the selected track.

.. py:currentmodule:: MTOTrackPoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPoint.time`
              - Get the time at which the point occurs. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPoint.latitude`
              - Get or set the latitude of the point. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPoint.longitude`
              - Get or set the longitude of the point. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPoint.altitude`
              - Get or set the altitude of the point. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPoint.position`
              - Whether to interpolate the track's position between each defined point. The track's marker and label position will be linearly interpolated between the track points for the current animation time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MTOTrackPoint.identifier`
              - Get the ID number assigned to the track. This field is auto-populated in numeric sequential order, and cannot be modified.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTOTrackPoint


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.MTOTrackPoint.time
    :type: typing.Any

    Get the time at which the point occurs. Uses DateFormat Dimension.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.MTOTrackPoint.latitude
    :type: float

    Get or set the latitude of the point. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.MTOTrackPoint.longitude
    :type: float

    Get or set the longitude of the point. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.MTOTrackPoint.altitude
    :type: float

    Get or set the altitude of the point. Uses Distance Dimension.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.MTOTrackPoint.position
    :type: IPosition

    Whether to interpolate the track's position between each defined point. The track's marker and label position will be linearly interpolated between the track points for the current animation time.

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.MTOTrackPoint.identifier
    :type: int

    Get the ID number assigned to the track. This field is auto-populated in numeric sequential order, and cannot be modified.


