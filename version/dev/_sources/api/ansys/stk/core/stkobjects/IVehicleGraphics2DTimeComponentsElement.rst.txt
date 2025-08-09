IVehicleGraphics2DTimeComponentsElement
=======================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement

   Provide properties to configure the vehicle's appearance in 2D and 3D views.

.. py:currentmodule:: IVehicleGraphics2DTimeComponentsElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.decrease_priority`
              - Decrease the time component's rendering priority.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.increase_priority`
              - Increase the time component's rendering priority.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.set_highest_priority`
              - Set the highest time component's rendering priority.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.set_lowest_priority`
              - Set the lowest time component's rendering priority.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.priority`
              - Priority indicates the order of a time component when resolving the overlapping intervals during rendering.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.qualified_path`
              - A fully qualified path of a time component.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeComponentsElement


Property detail
---------------

.. py:property:: priority
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.priority
    :type: int

    Priority indicates the order of a time component when resolving the overlapping intervals during rendering.

.. py:property:: qualified_path
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.qualified_path
    :type: str

    A fully qualified path of a time component.


Method detail
-------------

.. py:method:: decrease_priority(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.decrease_priority

    Decrease the time component's rendering priority.

    :Returns:

        :obj:`~None`

.. py:method:: increase_priority(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.increase_priority

    Increase the time component's rendering priority.

    :Returns:

        :obj:`~None`



.. py:method:: set_highest_priority(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.set_highest_priority

    Set the highest time component's rendering priority.

    :Returns:

        :obj:`~None`

.. py:method:: set_lowest_priority(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.set_lowest_priority

    Set the lowest time component's rendering priority.

    :Returns:

        :obj:`~None`

