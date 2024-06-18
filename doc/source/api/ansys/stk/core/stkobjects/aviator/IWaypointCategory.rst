IWaypointCategory
=================

.. py:class:: IWaypointCategory

   object
   
   Interface used to access the waypoints in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~user_waypoints`
            * - :py:meth:`~user_runways`
            * - :py:meth:`~user_vtol_points`
            * - :py:meth:`~arinc424_airports`
            * - :py:meth:`~arinc424_helipads`
            * - :py:meth:`~arinc424_navaids`
            * - :py:meth:`~arinc424_runways`
            * - :py:meth:`~arinc424_waypoints`
            * - :py:meth:`~dafif_helipads`
            * - :py:meth:`~dafif_runways`
            * - :py:meth:`~dafif_waypoints`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IWaypointCategory


Property detail
---------------

.. py:property:: user_waypoints
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_waypoints
    :type: "IAgAvtrUserWaypointSource"

    Get the User Waypoints.

.. py:property:: user_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_runways
    :type: "IAgAvtrUserRunwaySource"

    Get the User Runways.

.. py:property:: user_vtol_points
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.user_vtol_points
    :type: "IAgAvtrUserVTOLPointSource"

    Get the User VTOL Points.

.. py:property:: arinc424_airports
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_airports
    :type: "IAgAvtrARINC424Source"

    Get the ARINC-424 airports.

.. py:property:: arinc424_helipads
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_helipads
    :type: "IAgAvtrARINC424Source"

    Get the ARINC-424 helipads.

.. py:property:: arinc424_navaids
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_navaids
    :type: "IAgAvtrARINC424Source"

    Get the ARINC-424 navaids.

.. py:property:: arinc424_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_runways
    :type: "IAgAvtrARINC424Source"

    Get the ARINC-424 runways.

.. py:property:: arinc424_waypoints
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.arinc424_waypoints
    :type: "IAgAvtrARINC424Source"

    Get the ARINC-424 waypoints.

.. py:property:: dafif_helipads
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_helipads
    :type: "IAgAvtrDAFIFSource"

    Get the DAFIF helipads.

.. py:property:: dafif_runways
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_runways
    :type: "IAgAvtrDAFIFSource"

    Get the DAFIF runways.

.. py:property:: dafif_waypoints
    :canonical: ansys.stk.core.stkobjects.aviator.IWaypointCategory.dafif_waypoints
    :type: "IAgAvtrDAFIFSource"

    Get the DAFIF waypoints.


