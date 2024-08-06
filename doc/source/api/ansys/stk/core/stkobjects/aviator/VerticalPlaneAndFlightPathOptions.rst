VerticalPlaneAndFlightPathOptions
=================================

.. py:class:: ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions

   Class defining the vertical plane options for an arc procedure.

.. py:currentmodule:: VerticalPlaneAndFlightPathOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions.final_flight_path_angle`
              - Gets or sets the pitch angle of the flight path at the end of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions.min_enroute_flight_path_angle`
              - Gets or sets the minimum pitch angle of the flight path during enroute segments of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions.max_enroute_flight_path_angle`
              - Gets or sets the maximum pitch angle of the flight path during enroute segments of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions.max_vert_plane_radius_factor`
              - Gets or sets the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import VerticalPlaneAndFlightPathOptions


Property detail
---------------

.. py:property:: final_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions.final_flight_path_angle
    :type: typing.Any

    Gets or sets the pitch angle of the flight path at the end of the procedure.

.. py:property:: min_enroute_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions.min_enroute_flight_path_angle
    :type: typing.Any

    Gets or sets the minimum pitch angle of the flight path during enroute segments of the procedure.

.. py:property:: max_enroute_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions.max_enroute_flight_path_angle
    :type: typing.Any

    Gets or sets the maximum pitch angle of the flight path during enroute segments of the procedure.

.. py:property:: max_vert_plane_radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions.max_vert_plane_radius_factor
    :type: float

    Gets or sets the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.


