ISiteSTKObjectWaypoint
======================

.. py:class:: ISiteSTKObjectWaypoint

   object
   
   Interface used to access the options for a STK Object Waypoint site.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~object_name`
            * - :py:meth:`~valid_object_names`
            * - :py:meth:`~min_time`
            * - :py:meth:`~waypoint_time`
            * - :py:meth:`~minimize_site_proc_time_diff`
            * - :py:meth:`~max_time`
            * - :py:meth:`~offset_mode`
            * - :py:meth:`~bearing`
            * - :py:meth:`~use_magnetic_bearing`
            * - :py:meth:`~range`
            * - :py:meth:`~vgt_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteSTKObjectWaypoint


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.object_name
    :type: str

    Gets or sets the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.valid_object_names
    :type: list

    Returns the valid object names.

.. py:property:: min_time
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.min_time
    :type: typing.Any

    Gets the earliest time that the object is available as a site.

.. py:property:: waypoint_time
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.waypoint_time
    :type: typing.Any

    Gets or sets the time at which the object's position will be used as a waypoint.

.. py:property:: minimize_site_proc_time_diff
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.minimize_site_proc_time_diff
    :type: MINIMIZE_SITE_PROC_TIME_DIFF

    Gets or sets the mode to minimize the time difference between the procedure and site times.

.. py:property:: max_time
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.max_time
    :type: typing.Any

    Get the latest time that the object is available as a site.

.. py:property:: offset_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.offset_mode
    :type: STK_OBJECT_WAYPOINT_OFFSET_MODE

    Gets or sets the mode to offset the site location relative from the STK Object.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.bearing
    :type: typing.Any

    Gets or sets the bearing offset of the site location relative to the object's position.

.. py:property:: use_magnetic_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.use_magnetic_bearing
    :type: bool

    Gets or sets the option to use a magnetic heading for the bearing.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.range
    :type: float

    Gets or sets the range offset of the site location relative to the object's position.

.. py:property:: vgt_point
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.vgt_point
    :type: str

    Gets or sets the reference VGT Point.


Method detail
-------------




















.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKObjectWaypoint.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

