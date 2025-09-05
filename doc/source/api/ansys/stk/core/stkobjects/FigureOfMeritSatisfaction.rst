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
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.exclude_value_range`
              - Exclude Value Range.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.invalid_data_indicator`
              - A value to indicate when contouring is invalid.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.maximum_value_range`
              - Get or set the Max Value in the range.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.minimum_value_range`
              - Get or set the Min Value in the range.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.satisfaction_threshold`
              - Get or set the threshold for satisfying the Figure of Merit.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.satisfaction_type`
              - Get or set the relationship to the specified threshold that must be achieved to satisfy the Figure of Merit.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.use_value_range_check`
              - Enable FOM Values Limits for computing Statistics.



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

.. py:property:: exclude_value_range
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.exclude_value_range
    :type: bool

    Exclude Value Range.

.. py:property:: invalid_data_indicator
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.invalid_data_indicator
    :type: typing.Any

    A value to indicate when contouring is invalid.

.. py:property:: maximum_value_range
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.maximum_value_range
    :type: typing.Any

    Get or set the Max Value in the range.

.. py:property:: minimum_value_range
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.minimum_value_range
    :type: typing.Any

    Get or set the Min Value in the range.

.. py:property:: satisfaction_threshold
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.satisfaction_threshold
    :type: typing.Any

    Get or set the threshold for satisfying the Figure of Merit.

.. py:property:: satisfaction_type
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.satisfaction_type
    :type: FigureOfMeritSatisfactionType

    Get or set the relationship to the specified threshold that must be achieved to satisfy the Figure of Merit.

.. py:property:: use_value_range_check
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritSatisfaction.use_value_range_check
    :type: bool

    Enable FOM Values Limits for computing Statistics.


