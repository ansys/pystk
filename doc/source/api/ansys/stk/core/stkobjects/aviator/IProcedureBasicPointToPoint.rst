IProcedureBasicPointToPoint
===========================

.. py:class:: IProcedureBasicPointToPoint

   object
   
   Interface used to access the options for a basic point to point procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_options`
            * - :py:meth:`~navigation_options`
            * - :py:meth:`~enroute_options`
            * - :py:meth:`~enroute_cruise_airspeed_options`
            * - :py:meth:`~vertical_plane_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureBasicPointToPoint


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.altitude_options
    :type: IAgAvtrAltitudeOptions

    Get the altitude options.

.. py:property:: navigation_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.navigation_options
    :type: IAgAvtrNavigationOptions

    Get the navigation options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.enroute_options
    :type: IAgAvtrEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.enroute_cruise_airspeed_options
    :type: IAgAvtrCruiseAirspeedAndProfileOptions

    Get the enroute cruise airspeed options.

.. py:property:: vertical_plane_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.vertical_plane_options
    :type: IAgAvtrVerticalPlaneAndFlightPathOptions

    Get the vertical plane options.


Method detail
-------------






.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

