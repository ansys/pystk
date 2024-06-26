IVehicleGraphics3DSystemsElement
================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement

   IVehicleGraphics3DSystemsElementBase
   
   Element for reference system used for displaying vehicle orbits and trajectories.

.. py:currentmodule:: IVehicleGraphics3DSystemsElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement.get_graphics_3d_window_ids`
              - Get the selected 3D Graphics window ids.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement.set_graphics_3d_window_ids`
              - Select the 3D Graphics window ids.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement.name`
              - Get the name of the reference system.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement.is_visible`
              - Controls whether the reference system is visible.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DSystemsElement


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement.name
    :type: str

    Get the name of the reference system.

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement.is_visible
    :type: bool

    Controls whether the reference system is visible.


Method detail
-------------




.. py:method:: get_graphics_3d_window_ids(self) -> list
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement.get_graphics_3d_window_ids

    Get the selected 3D Graphics window ids.

    :Returns:

        :obj:`~list`

.. py:method:: set_graphics_3d_window_ids(self, windowIds: list) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElement.set_graphics_3d_window_ids

    Select the 3D Graphics window ids.

    :Parameters:

    **windowIds** : :obj:`~list`

    :Returns:

        :obj:`~None`

