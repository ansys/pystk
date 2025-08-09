ArcVerticalPlaneOptions
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions

   Class defining the vertical plane options in a procedure.

.. py:currentmodule:: ArcVerticalPlaneOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.start_arc_flight_path_angle`
              - Get or set the pitch angle of the flight path at the start of the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.stop_arc_flight_path_angle`
              - Get or set the pitch angle of the flight path at the end of the arc.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.min_enroute_flight_path_angle`
              - Get or set the minimum pitch angle of the flight path during enroute segments of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.max_enroute_flight_path_angle`
              - Get or set the maximum pitch angle of the flight path during enroute segments of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.max_vert_plane_radius_factor`
              - Get or set the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ArcVerticalPlaneOptions


Property detail
---------------

.. py:property:: start_arc_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.start_arc_flight_path_angle
    :type: typing.Any

    Get or set the pitch angle of the flight path at the start of the arc.

.. py:property:: stop_arc_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.stop_arc_flight_path_angle
    :type: typing.Any

    Get or set the pitch angle of the flight path at the end of the arc.

.. py:property:: min_enroute_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.min_enroute_flight_path_angle
    :type: typing.Any

    Get or set the minimum pitch angle of the flight path during enroute segments of the procedure.

.. py:property:: max_enroute_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.max_enroute_flight_path_angle
    :type: typing.Any

    Get or set the maximum pitch angle of the flight path during enroute segments of the procedure.

.. py:property:: max_vert_plane_radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions.max_vert_plane_radius_factor
    :type: float

    Get or set the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.


