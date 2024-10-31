FigureOfMeritSatisfaction
=========================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction

   Satisfaction properties for a Figure of Merit.

.. py:currentmodule:: FigureOfMeritSatisfaction

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.enable_satisfaction`
              - Specify whether to apply the graphical properties of the figure of merit only when a chosen satisfaction criterion is met.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.satisfaction_type`
              - Gets or sets the relationship to the specified threshold that must be achieved to satisfy the Figure of Merit.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.satisfaction_threshold`
              - Gets or sets the threshold for satisfying the Figure of Merit.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.invalid_data_indicator`
              - A value to indicate when contouring is invalid.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.use_value_range_check`
              - Enable FOM Values Limits for computing Statistics.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.minimum_value_range`
              - Gets or sets the Min Value in the range.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.maximum_value_range`
              - Gets or sets the Max Value in the range.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.exclude_value_range`
              - Exclude Value Range.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritSatisfaction


Property detail
---------------

.. py:property:: enable_satisfaction
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.enable_satisfaction
    :type: bool

    Specify whether to apply the graphical properties of the figure of merit only when a chosen satisfaction criterion is met.

.. py:property:: satisfaction_type
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.satisfaction_type
    :type: FIGURE_OF_MERIT_SATISFACTION_TYPE

    Gets or sets the relationship to the specified threshold that must be achieved to satisfy the Figure of Merit.

.. py:property:: satisfaction_threshold
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.satisfaction_threshold
    :type: typing.Any

    Gets or sets the threshold for satisfying the Figure of Merit.

.. py:property:: invalid_data_indicator
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.invalid_data_indicator
    :type: typing.Any

    A value to indicate when contouring is invalid.

.. py:property:: use_value_range_check
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.use_value_range_check
    :type: bool

    Enable FOM Values Limits for computing Statistics.

.. py:property:: minimum_value_range
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.minimum_value_range
    :type: typing.Any

    Gets or sets the Min Value in the range.

.. py:property:: maximum_value_range
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.maximum_value_range
    :type: typing.Any

    Gets or sets the Max Value in the range.

.. py:property:: exclude_value_range
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.exclude_value_range
    :type: bool

    Exclude Value Range.


