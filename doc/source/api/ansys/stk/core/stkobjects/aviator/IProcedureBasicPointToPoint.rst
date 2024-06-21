IProcedureBasicPointToPoint
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint

   object
   
   Interface used to access the options for a basic point to point procedure.

.. py:currentmodule:: IProcedureBasicPointToPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.altitude_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.navigation_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.enroute_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.enroute_cruise_airspeed_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.vertical_plane_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureBasicPointToPoint


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.altitude_options
    :type: IAltitudeOptions

    Get the altitude options.

.. py:property:: navigation_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.navigation_options
    :type: INavigationOptions

    Get the navigation options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.enroute_options
    :type: IEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedAndProfileOptions

    Get the enroute cruise airspeed options.

.. py:property:: vertical_plane_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.vertical_plane_options
    :type: IVerticalPlaneAndFlightPathOptions

    Get the vertical plane options.


Method detail
-------------






.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureBasicPointToPoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

