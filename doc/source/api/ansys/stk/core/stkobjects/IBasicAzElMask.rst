IBasicAzElMask
==============

.. py:class:: IBasicAzElMask

   object
   
   AgAzElMask Azimuth-elevation access points.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_visible`
            * - :py:meth:`~number_of_altitude_steps`
            * - :py:meth:`~range_visible`
            * - :py:meth:`~number_of_range_steps`
            * - :py:meth:`~display_range_minimum`
            * - :py:meth:`~display_range_maximum`
            * - :py:meth:`~display_altitude_minimum`
            * - :py:meth:`~display_altitude_maximum`
            * - :py:meth:`~altitude_color_visible`
            * - :py:meth:`~altitude_color`
            * - :py:meth:`~range_color_visible`
            * - :py:meth:`~range_color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IBasicAzElMask


Property detail
---------------

.. py:property:: altitude_visible
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.altitude_visible
    :type: bool

    Display the terrain mask at a specified number of steps from the minimum to the maximum altitude above the central body.

.. py:property:: number_of_altitude_steps
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.number_of_altitude_steps
    :type: int

    The relative intervals at which the terrain mask is displayed, e.g. if this value is 3 steps, and the minimum and maximum altitudes are 500 and 1500 km, respectively, then the terrain mask is displayed at altitudes of 500, 1000 and 1500 km.

.. py:property:: range_visible
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.range_visible
    :type: bool

    Display the terrain mask at the specified number of steps from the minimum to the maximum range from the facility, place or target.

.. py:property:: number_of_range_steps
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.number_of_range_steps
    :type: int

    The relative intervals at which the terrain mask is displayed, e.g. if this value is 3 steps, and the minimum and maximum ranges are 500 abd 1500 km, respectively, then the terrain mask is displayed at ranges of 500, 1000 and 1500 km.

.. py:property:: display_range_minimum
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.display_range_minimum
    :type: float

    The shortest range at which the terrain mask is displayed. Uses Distance Dimension.

.. py:property:: display_range_maximum
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.display_range_maximum
    :type: float

    The longest range at which the terrain mask is displayed. Uses Distance Dimension.

.. py:property:: display_altitude_minimum
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.display_altitude_minimum
    :type: float

    The lowest altitude at which the terrain mask is displayed. The minimum altitude must be at least equal to the altitude of the facility, place or target, including the height above ground, if specified. Uses Distance Dimension.

.. py:property:: display_altitude_maximum
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.display_altitude_maximum
    :type: float

    The highest altitude above the central body at which the terrain mask is displayed. Uses Distance Dimension.

.. py:property:: altitude_color_visible
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.altitude_color_visible
    :type: bool

    Display the color at altitude.

.. py:property:: altitude_color
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.altitude_color
    :type: agcolor.Color

    Gets or sets the altitude color.

.. py:property:: range_color_visible
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.range_color_visible
    :type: bool

    Display the color at range.

.. py:property:: range_color
    :canonical: ansys.stk.core.stkobjects.IBasicAzElMask.range_color
    :type: agcolor.Color

    Gets or sets the range color.


