IVehicleGraphics2DAttributesRoute
=================================

.. py:class:: IVehicleGraphics2DAttributesRoute

   IVehicleGraphics2DAttributesBasic
   
   2D Graphics attributes for aircraft, ships and ground vehicles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_route_visible`
            * - :py:meth:`~is_route_marker_visible`
            * - :py:meth:`~pick_string`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DAttributesRoute


Property detail
---------------

.. py:property:: is_route_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRoute.is_route_visible
    :type: bool

    Opt whether to show the vehicle's route.

.. py:property:: is_route_marker_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRoute.is_route_marker_visible
    :type: bool

    Opt whether to show the vehicle's route marker.

.. py:property:: pick_string
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRoute.pick_string
    :type: str

    String displayed after instance name when the vehicle line is picked in 2D or 3D.


