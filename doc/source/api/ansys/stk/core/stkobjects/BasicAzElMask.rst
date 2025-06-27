BasicAzElMask
=============

.. py:class:: ansys.stk.core.stkobjects.BasicAzElMask

   The Azimuth-Elevation Mask class.

.. py:currentmodule:: BasicAzElMask

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.display_mask_over_altitude_range`
              - Display the terrain mask at a specified number of steps from the minimum to the maximum altitude above the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.number_of_altitude_steps`
              - The relative intervals at which the terrain mask is displayed, e.g. if this value is 3 steps, and the minimum and maximum altitudes are 500 and 1500 km, respectively, then the terrain mask is displayed at altitudes of 500, 1000 and 1500 km.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.show_mask_over_range`
              - Display the terrain mask at the specified number of steps from the minimum to the maximum range from the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.number_of_range_steps`
              - The relative intervals at which the terrain mask is displayed, e.g. if this value is 3 steps, and the minimum and maximum ranges are 500 and 1500 km, respectively, then the terrain mask is displayed at ranges of 500, 1000 and 1500 km.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.display_range_minimum`
              - The shortest range at which the terrain mask is displayed. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.display_range_maximum`
              - The longest range at which the terrain mask is displayed. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.display_altitude_minimum`
              - The lowest altitude at which the terrain mask is displayed. The minimum altitude must be at least equal to the altitude of the facility, place or target, including the height above ground, if specified. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.display_altitude_maximum`
              - The highest altitude above the central body at which the terrain mask is displayed. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.display_color_at_altitude`
              - Display the color at altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.altitude_color`
              - Get or set the altitude color.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.show_color_at_range`
              - Display the color at range.
            * - :py:attr:`~ansys.stk.core.stkobjects.BasicAzElMask.range_color`
              - Get or set the range color.



Examples
--------

Display the AzEl Mask in 2D/3D

.. code-block:: python

    # Facility facility: Facility Object
    azelMask = facility.graphics.az_el_mask
    azelMask.show_mask_over_range = True
    azelMask.number_of_range_steps = 10
    azelMask.display_range_minimum = 0  # km
    azelMask.display_range_maximum = 100  # km
    azelMask.show_color_at_range = True
    azelMask.range_color = Colors.Cyan


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import BasicAzElMask


Property detail
---------------

.. py:property:: display_mask_over_altitude_range
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.display_mask_over_altitude_range
    :type: bool

    Display the terrain mask at a specified number of steps from the minimum to the maximum altitude above the central body.

.. py:property:: number_of_altitude_steps
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.number_of_altitude_steps
    :type: int

    The relative intervals at which the terrain mask is displayed, e.g. if this value is 3 steps, and the minimum and maximum altitudes are 500 and 1500 km, respectively, then the terrain mask is displayed at altitudes of 500, 1000 and 1500 km.

.. py:property:: show_mask_over_range
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.show_mask_over_range
    :type: bool

    Display the terrain mask at the specified number of steps from the minimum to the maximum range from the facility, place or target.

.. py:property:: number_of_range_steps
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.number_of_range_steps
    :type: int

    The relative intervals at which the terrain mask is displayed, e.g. if this value is 3 steps, and the minimum and maximum ranges are 500 and 1500 km, respectively, then the terrain mask is displayed at ranges of 500, 1000 and 1500 km.

.. py:property:: display_range_minimum
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.display_range_minimum
    :type: float

    The shortest range at which the terrain mask is displayed. Uses Distance Dimension.

.. py:property:: display_range_maximum
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.display_range_maximum
    :type: float

    The longest range at which the terrain mask is displayed. Uses Distance Dimension.

.. py:property:: display_altitude_minimum
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.display_altitude_minimum
    :type: float

    The lowest altitude at which the terrain mask is displayed. The minimum altitude must be at least equal to the altitude of the facility, place or target, including the height above ground, if specified. Uses Distance Dimension.

.. py:property:: display_altitude_maximum
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.display_altitude_maximum
    :type: float

    The highest altitude above the central body at which the terrain mask is displayed. Uses Distance Dimension.

.. py:property:: display_color_at_altitude
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.display_color_at_altitude
    :type: bool

    Display the color at altitude.

.. py:property:: altitude_color
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.altitude_color
    :type: agcolor.Color

    Get or set the altitude color.

.. py:property:: show_color_at_range
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.show_color_at_range
    :type: bool

    Display the color at range.

.. py:property:: range_color
    :canonical: ansys.stk.core.stkobjects.BasicAzElMask.range_color
    :type: agcolor.Color

    Get or set the range color.


