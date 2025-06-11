ProcedureBasicPointToPoint
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a basic point to point procedure.

.. py:currentmodule:: ProcedureBasicPointToPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.navigation_options`
              - Get the navigation options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.vertical_plane_options`
              - Get the vertical plane options.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureBasicPointToPoint


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.altitude_options
    :type: AltitudeOptions

    Get the altitude options.

.. py:property:: navigation_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.navigation_options
    :type: NavigationOptions

    Get the navigation options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.enroute_options
    :type: EnrouteOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedAndProfileOptions

    Get the enroute cruise airspeed options.

.. py:property:: vertical_plane_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.vertical_plane_options
    :type: VerticalPlaneAndFlightPathOptions

    Get the vertical plane options.


Method detail
-------------






.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

