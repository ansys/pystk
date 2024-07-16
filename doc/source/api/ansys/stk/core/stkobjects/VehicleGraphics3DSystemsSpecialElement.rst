VehicleGraphics3DSystemsSpecialElement
======================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase`

   Define methods and properties to configure 3D properties of Inertial or Fixed reference system used for displaying vehicle orbits and trajectories.

.. py:currentmodule:: VehicleGraphics3DSystemsSpecialElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement.get_graphics_3d_window_ids`
              - Get the selected 3D Graphics window ids.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement.set_graphics_3d_window_ids`
              - Select the 3D Graphics window ids.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement.is_visible`
              - Controls whether the reference system is visible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DSystemsSpecialElement


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement.is_visible
    :type: bool

    Controls whether the reference system is visible.


Method detail
-------------



.. py:method:: get_graphics_3d_window_ids(self) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement.get_graphics_3d_window_ids

    Get the selected 3D Graphics window ids.

    :Returns:

        :obj:`~list`

.. py:method:: set_graphics_3d_window_ids(self, windowIds: list) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement.set_graphics_3d_window_ids

    Select the 3D Graphics window ids.

    :Parameters:

    **windowIds** : :obj:`~list`

    :Returns:

        :obj:`~None`

