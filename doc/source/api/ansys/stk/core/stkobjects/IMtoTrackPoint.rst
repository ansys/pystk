IMtoTrackPoint
==============

.. py:class:: ansys.stk.core.stkobjects.IMtoTrackPoint

   object
   
   The points defined for the selected track.

.. py:currentmodule:: IMtoTrackPoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoTrackPoint.time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoTrackPoint.latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoTrackPoint.longitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoTrackPoint.altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoTrackPoint.position`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoTrackPoint.id`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoTrackPoint


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.IMtoTrackPoint.time
    :type: typing.Any

    Get the time at which the point occurs. Uses DateFormat Dimension.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.IMtoTrackPoint.latitude
    :type: float

    Gets or sets the latitude of the point. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.IMtoTrackPoint.longitude
    :type: float

    Gets or sets the longitude of the point. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IMtoTrackPoint.altitude
    :type: float

    Gets or sets the altitude of the point. Uses Distance Dimension.

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IMtoTrackPoint.position
    :type: IPosition

    Whether to interpolate the track's position between each defined point. The track's marker and label position will be linearly interpolated between the track points for the current animation time.

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.IMtoTrackPoint.id
    :type: int

    Get the ID number assigned to the track. This field is auto-populated in numeric sequential order, and cannot be modified.


