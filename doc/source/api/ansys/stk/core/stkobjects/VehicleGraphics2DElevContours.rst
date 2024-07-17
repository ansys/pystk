VehicleGraphics2DElevContours
=============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DElevContours

   Bases: 

   General settings regarding display of elevation contours.

.. py:currentmodule:: VehicleGraphics2DElevContours

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.is_visible`
              - Opt whether to display elevation contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.is_fill_visible`
              - Opt whether to display a fill over the area within the contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.fill_style`
              - Gets or sets the type of fill to display.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.num_of_decimal_digits`
              - Number of decimal digits. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.elevations`
              - Collection of Levels.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.fill_translucency`
              - Specify the fill translucency percentage of the area within the contours. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DElevContours


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.is_visible
    :type: bool

    Opt whether to display elevation contours.

.. py:property:: is_fill_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.is_fill_visible
    :type: bool

    Opt whether to display a fill over the area within the contours.

.. py:property:: fill_style
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.fill_style
    :type: FILL_STYLE

    Gets or sets the type of fill to display.

.. py:property:: num_of_decimal_digits
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.num_of_decimal_digits
    :type: int

    Number of decimal digits. Dimensionless.

.. py:property:: elevations
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.elevations
    :type: IVehicleGraphics2DElevationsCollection

    Collection of Levels.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DElevContours.fill_translucency
    :type: float

    Specify the fill translucency percentage of the area within the contours. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.


