IVehicleGraphics2DElevContours
==============================

.. py:class:: IVehicleGraphics2DElevContours

   object
   
   General settings regarding display of elevation contours.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~is_fill_visible`
            * - :py:meth:`~fill_style`
            * - :py:meth:`~num_of_decimal_digits`
            * - :py:meth:`~elevations`
            * - :py:meth:`~fill_translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DElevContours


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DElevContours.is_visible
    :type: bool

    Opt whether to display elevation contours.

.. py:property:: is_fill_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DElevContours.is_fill_visible
    :type: bool

    Opt whether to display a fill over the area within the contours.

.. py:property:: fill_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DElevContours.fill_style
    :type: "FILL_STYLE"

    Gets or sets the type of fill to display.

.. py:property:: num_of_decimal_digits
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DElevContours.num_of_decimal_digits
    :type: int

    Number of decimal digits. Dimensionless.

.. py:property:: elevations
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DElevContours.elevations
    :type: "IAgVeGfxElevationsCollection"

    Collection of Levels.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DElevContours.fill_translucency
    :type: float

    Specify the fill translucency percentage of the area within the contours. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


