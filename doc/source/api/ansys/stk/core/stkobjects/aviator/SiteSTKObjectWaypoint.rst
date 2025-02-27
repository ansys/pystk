SiteSTKObjectWaypoint
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a STK Object Waypoint site.

.. py:currentmodule:: SiteSTKObjectWaypoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.object_name`
              - Get or set the object name to link to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.valid_object_names`
              - Return the valid object names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.min_time`
              - Get the earliest time that the object is available as a site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.waypoint_time`
              - Get or set the time at which the object's position will be used as a waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.minimize_site_procedure_time_diff`
              - Get or set the mode to minimize the time difference between the procedure and site times.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.max_time`
              - Get the latest time that the object is available as a site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.offset_mode`
              - Get or set the mode to offset the site location relative from the STK Object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.bearing`
              - Get or set the bearing offset of the site location relative to the object's position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.use_magnetic_bearing`
              - Get or set the option to use a magnetic heading for the bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.range`
              - Get or set the range offset of the site location relative to the object's position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.vgt_point`
              - Get or set the reference VGT Point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteSTKObjectWaypoint


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.object_name
    :type: str

    Get or set the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.valid_object_names
    :type: list

    Return the valid object names.

.. py:property:: min_time
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.min_time
    :type: typing.Any

    Get the earliest time that the object is available as a site.

.. py:property:: waypoint_time
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.waypoint_time
    :type: typing.Any

    Get or set the time at which the object's position will be used as a waypoint.

.. py:property:: minimize_site_procedure_time_diff
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.minimize_site_procedure_time_diff
    :type: MinimizeSiteProcedureTimeDiff

    Get or set the mode to minimize the time difference between the procedure and site times.

.. py:property:: max_time
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.max_time
    :type: typing.Any

    Get the latest time that the object is available as a site.

.. py:property:: offset_mode
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.offset_mode
    :type: STKObjectWaypointOffsetMode

    Get or set the mode to offset the site location relative from the STK Object.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.bearing
    :type: typing.Any

    Get or set the bearing offset of the site location relative to the object's position.

.. py:property:: use_magnetic_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.use_magnetic_bearing
    :type: bool

    Get or set the option to use a magnetic heading for the bearing.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.range
    :type: float

    Get or set the range offset of the site location relative to the object's position.

.. py:property:: vgt_point
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.vgt_point
    :type: str

    Get or set the reference VGT Point.


Method detail
-------------




















.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

