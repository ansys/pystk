IVehicleGraphics3DSystemsElementBase
====================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase

   Define methods and properties used to configure the 3D properties of a reference system used for displaying vehicle orbits and trajectories.

.. py:currentmodule:: IVehicleGraphics3DSystemsElementBase

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.inherit`
              - Inherit color from 2D graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.color`
              - Specify a custom color.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.graphics_3d_window`
              - Get or set the selected 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.available_graphics_3d_windows`
              - 3D Graphics Windows available to display the reference system.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.persist_for_all_passes`
              - Persistent the reference system when all passes are displayed.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DSystemsElementBase


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.inherit
    :type: bool

    Inherit color from 2D graphics.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.color
    :type: agcolor.Color

    Specify a custom color.

.. py:property:: graphics_3d_window
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.graphics_3d_window
    :type: str

    Get or set the selected 3D Graphics window.

.. py:property:: available_graphics_3d_windows
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.available_graphics_3d_windows
    :type: list

    3D Graphics Windows available to display the reference system.

.. py:property:: persist_for_all_passes
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.persist_for_all_passes
    :type: bool

    Persistent the reference system when all passes are displayed.


