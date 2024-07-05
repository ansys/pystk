IWaypointCategory
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.IWaypointCategory

   object
   
   Interface used to access the waypoints in the Aviator catalog.

.. py:currentmodule:: IWaypointCategory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_waypoints`
              - Get the User Waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_runways`
              - Get the User Runways.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_vtol_points`
              - Get the User VTOL Points.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_airports`
              - Get the ARINC-424 airports.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_helipads`
              - Get the ARINC-424 helipads.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_navaids`
              - Get the ARINC-424 navaids.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_runways`
              - Get the ARINC-424 runways.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_waypoints`
              - Get the ARINC-424 waypoints.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_helipads`
              - Get the DAFIF helipads.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_runways`
              - Get the DAFIF runways.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_waypoints`
              - Get the DAFIF waypoints.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IWaypointCategory


Property detail
---------------

.. py:property:: user_waypoints
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_waypoints
    :type: IUserWaypointSource

    Get the User Waypoints.

.. py:property:: user_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_runways
    :type: IUserRunwaySource

    Get the User Runways.

.. py:property:: user_vtol_points
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_vtol_points
    :type: IUserVTOLPointSource

    Get the User VTOL Points.

.. py:property:: arinc424_airports
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_airports
    :type: IARINC424Source

    Get the ARINC-424 airports.

.. py:property:: arinc424_helipads
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_helipads
    :type: IARINC424Source

    Get the ARINC-424 helipads.

.. py:property:: arinc424_navaids
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_navaids
    :type: IARINC424Source

    Get the ARINC-424 navaids.

.. py:property:: arinc424_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_runways
    :type: IARINC424Source

    Get the ARINC-424 runways.

.. py:property:: arinc424_waypoints
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_waypoints
    :type: IARINC424Source

    Get the ARINC-424 waypoints.

.. py:property:: dafif_helipads
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_helipads
    :type: IDAFIFSource

    Get the DAFIF helipads.

.. py:property:: dafif_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_runways
    :type: IDAFIFSource

    Get the DAFIF runways.

.. py:property:: dafif_waypoints
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_waypoints
    :type: IDAFIFSource

    Get the DAFIF waypoints.


