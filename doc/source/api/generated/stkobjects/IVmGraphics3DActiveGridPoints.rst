IVmGraphics3DActiveGridPoints
=============================

.. py:class:: IVmGraphics3DActiveGridPoints

   object
   
   IAgVmVOActiveGridPoints Interface for defining Active Grid Points for Volumetric Object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show_active_inactive_boundary`
            * - :py:meth:`~active_inactive_boundary_color`
            * - :py:meth:`~active_inactive_boundary_translucency`
            * - :py:meth:`~show_active_inactive_fill`
            * - :py:meth:`~inactive_fill_color`
            * - :py:meth:`~inactive_fill_translucency`
            * - :py:meth:`~active_fill_color`
            * - :py:meth:`~active_fill_translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmGraphics3DActiveGridPoints


Property detail
---------------

.. py:property:: show_active_inactive_boundary
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DActiveGridPoints.show_active_inactive_boundary
    :type: bool

    Show or hide the Active/Inactive Boundary.

.. py:property:: active_inactive_boundary_color
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DActiveGridPoints.active_inactive_boundary_color
    :type: agcolor.Color

    Set the color of the Active/Inactive Boundary.

.. py:property:: active_inactive_boundary_translucency
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DActiveGridPoints.active_inactive_boundary_translucency
    :type: float

    Set the percent Translucency for Active/Inactive Boundary.

.. py:property:: show_active_inactive_fill
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DActiveGridPoints.show_active_inactive_fill
    :type: bool

    Show or hide the Active/Inactive Fill.

.. py:property:: inactive_fill_color
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DActiveGridPoints.inactive_fill_color
    :type: agcolor.Color

    Set the color of the Inactive Fill.

.. py:property:: inactive_fill_translucency
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DActiveGridPoints.inactive_fill_translucency
    :type: float

    Set the percent Translucency for Inactive Fill.

.. py:property:: active_fill_color
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DActiveGridPoints.active_fill_color
    :type: agcolor.Color

    Set the color of the Active Fill.

.. py:property:: active_fill_translucency
    :canonical: ansys.stk.core.stkobjects.IVmGraphics3DActiveGridPoints.active_fill_translucency
    :type: float

    Set the percent Translucency for Active Fill.


