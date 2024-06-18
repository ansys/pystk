IVehicleGraphics3DIntervalsElement
==================================

.. py:class:: IVehicleGraphics3DIntervalsElement

   object
   
   Intervals graphics interface for covariance pointing contour.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~is_visible`
            * - :py:meth:`~color`
            * - :py:meth:`~line_width`
            * - :py:meth:`~translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DIntervalsElement


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DIntervalsElement.start_time
    :type: typing.Any

    Time at which the interval begins and the selected graphics display in the 3D window. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DIntervalsElement.stop_time
    :type: typing.Any

    Time at which the interval ends. Uses DateFormat Dimension.

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DIntervalsElement.is_visible
    :type: bool

    Opt whether to display the object during the selected time using the selected graphics properties.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DIntervalsElement.color
    :type: agcolor.Color

    Gets or sets the line color.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DIntervalsElement.line_width
    :type: "LINE_WIDTH"

    Gets or sets the line width.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DIntervalsElement.translucency
    :type: float

    Gets or sets the translucency. Dimensionless.


