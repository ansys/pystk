ISwath
======

.. py:class:: ansys.stk.core.stkobjects.ISwath

   object
   
   Provide access to the Swath properties.

.. py:currentmodule:: ISwath

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.add_time_interval`
              - Add an interval to the list of valid swath intervals. Start/Stop Times use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.modify_time_interval`
              - Modify an interval given an index. Start/Stop Times use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.get_time_interval_index`
              - Retrieve an index given a start and stop time. Start/Stop Times use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.remove_time_interval`
              - Remove the interval given the start and stop times. Start/Stop Times use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.remove_time_interval_index`
              - Remove an interval given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.remove_all_intervals`
              - Remove all intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.to_array`
              - Return an array of all time intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.enable`
              - Enables swath.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.color`
              - Gets or sets the color in which swath graphics are displayed in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.line_style`
              - Gets or sets the style of the line defining the boundaries of the swath display in the 2D Graphics window. A member of the AgELineStyle enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.line_width`
              - Gets or sets the width of the line defining the boundaries of the swath display in the 2D Graphics window. A member of the AgELineWidth enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.time_interval_count`
              - Number of Time Intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.minimum_step`
              - Gets or sets the minimum step size for the adaptive step size of swath computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.maximum_step`
              - Gets or sets the maximum step size for the adaptive step size of swath computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.use_maximum_cone`
              - Whether to perform swath computations based on the maximum cone that encompasses the sensor pattern instead of actual pattern. Setting this option may result in a more informative swath with a superior appearance.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.scattering_tolerance`
              - Determines the angle with respect to the swath line within which candidate points are considered for possible connection to it.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.curvature_tolerance`
              - Controls the adaptive step size of swath computation and ensures that neighboring samples adequately capture the curvature of the swath line.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISwath.computational_method`
              - Select the Analytical or Numerical Computaional Method for generating swaths.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISwath


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.ISwath.enable
    :type: bool

    Enables swath.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.ISwath.color
    :type: agcolor.Color

    Gets or sets the color in which swath graphics are displayed in the 2D Graphics window.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.ISwath.line_style
    :type: LINE_STYLE

    Gets or sets the style of the line defining the boundaries of the swath display in the 2D Graphics window. A member of the AgELineStyle enumeration.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.ISwath.line_width
    :type: LINE_WIDTH

    Gets or sets the width of the line defining the boundaries of the swath display in the 2D Graphics window. A member of the AgELineWidth enumeration.

.. py:property:: time_interval_count
    :canonical: ansys.stk.core.stkobjects.ISwath.time_interval_count
    :type: int

    Number of Time Intervals.

.. py:property:: minimum_step
    :canonical: ansys.stk.core.stkobjects.ISwath.minimum_step
    :type: float

    Gets or sets the minimum step size for the adaptive step size of swath computation.

.. py:property:: maximum_step
    :canonical: ansys.stk.core.stkobjects.ISwath.maximum_step
    :type: float

    Gets or sets the maximum step size for the adaptive step size of swath computation.

.. py:property:: use_maximum_cone
    :canonical: ansys.stk.core.stkobjects.ISwath.use_maximum_cone
    :type: bool

    Whether to perform swath computations based on the maximum cone that encompasses the sensor pattern instead of actual pattern. Setting this option may result in a more informative swath with a superior appearance.

.. py:property:: scattering_tolerance
    :canonical: ansys.stk.core.stkobjects.ISwath.scattering_tolerance
    :type: float

    Determines the angle with respect to the swath line within which candidate points are considered for possible connection to it.

.. py:property:: curvature_tolerance
    :canonical: ansys.stk.core.stkobjects.ISwath.curvature_tolerance
    :type: float

    Controls the adaptive step size of swath computation and ensures that neighboring samples adequately capture the curvature of the swath line.

.. py:property:: computational_method
    :canonical: ansys.stk.core.stkobjects.ISwath.computational_method
    :type: SWATH_COMPUTATIONAL_METHOD

    Select the Analytical or Numerical Computaional Method for generating swaths.


Method detail
-------------









.. py:method:: add_time_interval(self, startTime: typing.Any, stopTime: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.ISwath.add_time_interval

    Add an interval to the list of valid swath intervals. Start/Stop Times use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: modify_time_interval(self, index: int, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.ISwath.modify_time_interval

    Modify an interval given an index. Start/Stop Times use DateFormat Dimension.

    :Parameters:

    **index** : :obj:`~int`
    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: get_time_interval_index(self, start: typing.Any, stop: typing.Any) -> int
    :canonical: ansys.stk.core.stkobjects.ISwath.get_time_interval_index

    Retrieve an index given a start and stop time. Start/Stop Times use DateFormat Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~int`

.. py:method:: remove_time_interval(self, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.ISwath.remove_time_interval

    Remove the interval given the start and stop times. Start/Stop Times use DateFormat Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_time_interval_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ISwath.remove_time_interval_index

    Remove an interval given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_intervals(self) -> None
    :canonical: ansys.stk.core.stkobjects.ISwath.remove_all_intervals

    Remove all intervals.

    :Returns:

        :obj:`~None`


.. py:method:: to_array(self, index: int, length: int) -> list
    :canonical: ansys.stk.core.stkobjects.ISwath.to_array

    Return an array of all time intervals.

    :Parameters:

    **index** : :obj:`~int`
    **length** : :obj:`~int`

    :Returns:

        :obj:`~list`













