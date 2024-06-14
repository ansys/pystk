IVehicleGraphics3DSystemsElementBase
====================================

.. py:class:: IVehicleGraphics3DSystemsElementBase

   object
   
   Define methods and properties used to configure the 3D properties of a reference system used for displaying vehicle orbits and trajectories.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~inherit`
            * - :py:meth:`~color`
            * - :py:meth:`~graphics_3d_window`
            * - :py:meth:`~available_graphics_3d_windows`
            * - :py:meth:`~persist_for_all_passes`


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

    Gets or sets the selected 3D Graphics window.

.. py:property:: available_graphics_3d_windows
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.available_graphics_3d_windows
    :type: list

    3D Graphics Windows available to display the reference system.

.. py:property:: persist_for_all_passes
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase.persist_for_all_passes
    :type: bool

    Persistent the reference system when all passes are displayed.


