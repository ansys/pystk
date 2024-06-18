IVehicleGraphics3DAttributesBasic
=================================

.. py:class:: IVehicleGraphics3DAttributesBasic

   object
   
   Interface for basic 3D graphics for covariance pointing contours.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~color`
            * - :py:meth:`~line_width`
            * - :py:meth:`~translucency`
            * - :py:meth:`~use_custom_color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DAttributesBasic


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DAttributesBasic.is_visible
    :type: bool

    Opt to display the selected graphics properties instead of using those defined in terms of intervals.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DAttributesBasic.color
    :type: agcolor.Color

    Gets or sets the line color used when UseCustomColor is true.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DAttributesBasic.line_width
    :type: "LINE_WIDTH"

    Gets or sets the line width.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DAttributesBasic.translucency
    :type: float

    Gets or sets the translucency. Dimensionless.

.. py:property:: use_custom_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DAttributesBasic.use_custom_color
    :type: bool

    Use custom color for lines if true, otherwise use the vehicle color for the line color.


