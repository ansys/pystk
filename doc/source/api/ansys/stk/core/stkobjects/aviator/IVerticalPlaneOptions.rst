IVerticalPlaneOptions
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IVerticalPlaneOptions

   Interface used to access the Vertical Plane options for an Aviator procedure.

.. py:currentmodule:: IVerticalPlaneOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IVerticalPlaneOptions.min_enroute_flight_path_angle`
              - Get or set the minimum pitch angle of the flight path during enroute segments of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IVerticalPlaneOptions.max_enroute_flight_path_angle`
              - Get or set the maximum pitch angle of the flight path during enroute segments of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IVerticalPlaneOptions.max_vert_plane_radius_factor`
              - Get or set the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IVerticalPlaneOptions


Property detail
---------------

.. py:property:: min_enroute_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IVerticalPlaneOptions.min_enroute_flight_path_angle
    :type: typing.Any

    Get or set the minimum pitch angle of the flight path during enroute segments of the procedure.

.. py:property:: max_enroute_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IVerticalPlaneOptions.max_enroute_flight_path_angle
    :type: typing.Any

    Get or set the maximum pitch angle of the flight path during enroute segments of the procedure.

.. py:property:: max_vert_plane_radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IVerticalPlaneOptions.max_vert_plane_radius_factor
    :type: float

    Get or set the maximum amount the radius of vertical curve will be increased to minimize the flight path angle required to complete it.


