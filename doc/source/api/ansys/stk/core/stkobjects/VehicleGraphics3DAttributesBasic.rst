VehicleGraphics3DAttributesBasic
================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DAttributes`

   Basic 3D graphics for covariance pointing contours.

.. py:currentmodule:: VehicleGraphics3DAttributesBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.show_graphics`
              - Opt to display the selected graphics properties instead of using those defined in terms of intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.color`
              - Gets or sets the line color used when UseCustomColor is true.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.line_width`
              - Gets or sets the line width.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.translucency`
              - Gets or sets the translucency. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.use_custom_color`
              - Use custom color for lines if true, otherwise use the vehicle color for the line color.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DAttributesBasic


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.show_graphics
    :type: bool

    Opt to display the selected graphics properties instead of using those defined in terms of intervals.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.color
    :type: agcolor.Color

    Gets or sets the line color used when UseCustomColor is true.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.line_width
    :type: LineWidth

    Gets or sets the line width.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.translucency
    :type: float

    Gets or sets the translucency. Dimensionless.

.. py:property:: use_custom_color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic.use_custom_color
    :type: bool

    Use custom color for lines if true, otherwise use the vehicle color for the line color.


