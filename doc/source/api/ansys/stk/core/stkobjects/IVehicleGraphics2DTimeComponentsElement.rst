IVehicleGraphics2DTimeComponentsElement
=======================================

.. py:class:: IVehicleGraphics2DTimeComponentsElement

   object
   
   Provide properties to configure the vehicle's appearance in 2D and 3D views.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~increase_priority`
              - Increase the time component's rendering priority.
            * - :py:meth:`~decrease_priority`
              - Decrease the time component's rendering priority.
            * - :py:meth:`~set_highest_priority`
              - Set the highest time component's rendering priority.
            * - :py:meth:`~set_lowest_priority`
              - Set the lowest time component's rendering priority.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~qualified_path`
            * - :py:meth:`~priority`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeComponentsElement


Property detail
---------------

.. py:property:: qualified_path
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.qualified_path
    :type: str

    A fully qualified path of a time component.

.. py:property:: priority
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.priority
    :type: int

    Priority indicates the order of a time component when resolving the overlapping intervals during rendering.


Method detail
-------------



.. py:method:: increase_priority(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.increase_priority

    Increase the time component's rendering priority.

    :Returns:

        :obj:`~None`

.. py:method:: decrease_priority(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement.decrease_priority

    Decrease the time component's rendering priority.

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

