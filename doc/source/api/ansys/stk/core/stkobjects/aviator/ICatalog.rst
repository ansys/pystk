ICatalog
========

.. py:class:: ICatalog

   object
   
   Interface used to access the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aircraft_category`
            * - :py:meth:`~runway_category`
            * - :py:meth:`~airport_category`
            * - :py:meth:`~navaid_category`
            * - :py:meth:`~vtol_point_category`
            * - :py:meth:`~waypoint_category`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ICatalog


Property detail
---------------

.. py:property:: aircraft_category
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalog.aircraft_category
    :type: IAgAvtrAircraftCategory

    Get the aircraft category.

.. py:property:: runway_category
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalog.runway_category
    :type: IAgAvtrRunwayCategory

    Get the runway category.

.. py:property:: airport_category
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalog.airport_category
    :type: IAgAvtrAirportCategory

    Get the airport category.

.. py:property:: navaid_category
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalog.navaid_category
    :type: IAgAvtrNavaidCategory

    Get the navaid category.

.. py:property:: vtol_point_category
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalog.vtol_point_category
    :type: IAgAvtrVTOLPointCategory

    Get the vtol point category.

.. py:property:: waypoint_category
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalog.waypoint_category
    :type: IAgAvtrWaypointCategory

    Get the waypoint category.


