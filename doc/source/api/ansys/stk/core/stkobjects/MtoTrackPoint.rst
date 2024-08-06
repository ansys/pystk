MtoTrackPoint
=============

.. py:class:: ansys.stk.core.stkobjects.MtoTrackPoint

   The points defined for the selected track.

.. py:currentmodule:: MtoTrackPoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPoint.time`
              - Get the time at which the point occurs. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPoint.latitude`
              - Gets or sets the latitude of the point. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPoint.longitude`
              - Gets or sets the longitude of the point. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPoint.altitude`
              - Gets or sets the altitude of the point. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPoint.position`
              - Whether to interpolate the track's position between each defined point. The track's marker and label position will be linearly interpolated between the track points for the current animation time.
            * - :py:attr:`~ansys.stk.core.stkobjects.MtoTrackPoint.id`
              - Get the ID number assigned to the track. This field is auto-populated in numeric sequential order, and cannot be modified.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MtoTrackPoint


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.MtoTrackPoint.time
    :type: typing.Any

    Get the time at which the point occurs. Uses DateFormat Dimension.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.MtoTrackPoint.latitude
    :type: float

    Gets or sets the latitude of the point. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.MtoTrackPoint.longitude
    :type: float

    Gets or sets the longitude of the point. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.MtoTrackPoint.altitude
    :type: float

    Gets or sets the altitude of the point. Uses Distance Dimension.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.MtoTrackPoint.position
    :type: IPosition

    Whether to interpolate the track's position between each defined point. The track's marker and label position will be linearly interpolated between the track points for the current animation time.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.MtoTrackPoint.id
    :type: int

    Get the ID number assigned to the track. This field is auto-populated in numeric sequential order, and cannot be modified.


