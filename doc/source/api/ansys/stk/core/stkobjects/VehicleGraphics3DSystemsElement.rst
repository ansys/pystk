VehicleGraphics3DSystemsElement
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase`

   Element for reference system used for displaying vehicle orbits and trajectories.

.. py:currentmodule:: VehicleGraphics3DSystemsElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement.get_graphics_3d_window_identifiers`
              - Get the selected 3D Graphics window ids.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement.set_graphics_3d_window_identifiers`
              - Select the 3D Graphics window ids.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement.name`
              - Get the name of the reference system.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement.show_graphics`
              - Control whether the reference system is visible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DSystemsElement


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement.name
    :type: str

    Get the name of the reference system.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement.show_graphics
    :type: bool

    Control whether the reference system is visible.


Method detail
-------------




.. py:method:: get_graphics_3d_window_identifiers(self) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement.get_graphics_3d_window_identifiers

    Get the selected 3D Graphics window ids.

    :Returns:

        :obj:`~list`

.. py:method:: set_graphics_3d_window_identifiers(self, window_ids: list) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement.set_graphics_3d_window_identifiers

    Select the 3D Graphics window ids.

    :Parameters:

        **window_ids** : :obj:`~list`


    :Returns:

        :obj:`~None`

