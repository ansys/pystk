VehicleGraphics2DElevationContours
==================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours

   General settings regarding display of elevation contours.

.. py:currentmodule:: VehicleGraphics2DElevationContours

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.show_graphics`
              - Opt whether to display elevation contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.show_filled_contours`
              - Opt whether to display a fill over the area within the contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.fill_style`
              - Gets or sets the type of fill to display.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.number_of_decimal_digits`
              - Number of decimal digits. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.elevations`
              - Collection of Levels.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.fill_translucency`
              - Specify the fill translucency percentage of the area within the contours. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DElevationContours


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.show_graphics
    :type: bool

    Opt whether to display elevation contours.

.. py:property:: show_filled_contours
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.show_filled_contours
    :type: bool

    Opt whether to display a fill over the area within the contours.

.. py:property:: fill_style
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.fill_style
    :type: FillStyle

    Gets or sets the type of fill to display.

.. py:property:: number_of_decimal_digits
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.number_of_decimal_digits
    :type: int

    Number of decimal digits. Dimensionless.

.. py:property:: elevations
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.elevations
    :type: VehicleGraphics2DElevationsCollection

    Collection of Levels.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours.fill_translucency
    :type: float

    Specify the fill translucency percentage of the area within the contours. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


