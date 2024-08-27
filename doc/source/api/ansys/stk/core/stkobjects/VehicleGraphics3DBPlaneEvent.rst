VehicleGraphics3DBPlaneEvent
============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent

   3D BPlane Event.

.. py:currentmodule:: VehicleGraphics3DBPlaneEvent

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent.event_epoch`
              - Gets or sets the event epoch. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent.before_event`
              - Gets or sets the duration before the event that the B-Plane will be displayed. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent.after_event`
              - Gets or sets the duration after the event that the B-Plane will be displayed. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent.always_display`
              - Whether the B-Plane will be displayed throughout the scenario's animation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DBPlaneEvent


Property detail
---------------

.. py:property:: event_epoch
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent.event_epoch
    :type: typing.Any

    Gets or sets the event epoch. Uses DateFormat Dimension.

.. py:property:: before_event
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent.before_event
    :type: float

    Gets or sets the duration before the event that the B-Plane will be displayed. Uses Time Dimension.

.. py:property:: after_event
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent.after_event
    :type: float

    Gets or sets the duration after the event that the B-Plane will be displayed. Uses Time Dimension.

.. py:property:: always_display
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent.always_display
    :type: bool

    Whether the B-Plane will be displayed throughout the scenario's animation.


