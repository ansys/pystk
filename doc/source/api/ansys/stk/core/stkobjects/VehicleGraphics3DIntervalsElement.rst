VehicleGraphics3DIntervalsElement
=================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement

   Intervals graphics for covariance pointing contour.

.. py:currentmodule:: VehicleGraphics3DIntervalsElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.start_time`
              - Time at which the interval begins and the selected graphics display in the 3D window. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.stop_time`
              - Time at which the interval ends. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.show_graphics`
              - Opt whether to display the object during the selected time using the selected graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.color`
              - Gets or sets the line color.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.line_width`
              - Gets or sets the line width.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.translucency`
              - Gets or sets the translucency. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DIntervalsElement


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.start_time
    :type: typing.Any

    Time at which the interval begins and the selected graphics display in the 3D window. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.stop_time
    :type: typing.Any

    Time at which the interval ends. Uses DateFormat Dimension.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.show_graphics
    :type: bool

    Opt whether to display the object during the selected time using the selected graphics properties.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.color
    :type: agcolor.Color

    Gets or sets the line color.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.line_width
    :type: LineWidth

    Gets or sets the line width.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement.translucency
    :type: float

    Gets or sets the translucency. Dimensionless.


