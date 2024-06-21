IFigureOfMeritSatisfaction
==========================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction

   object
   
   Satisfaction properties for a Figure of Merit.

.. py:currentmodule:: IFigureOfMeritSatisfaction

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.enable_satisfaction`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.satisfaction_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.satisfaction_threshold`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.invalid_data_indicator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.use_value_range_check`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.min_value_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.max_value_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.exclude_value_range`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritSatisfaction


Property detail
---------------

.. py:property:: enable_satisfaction
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.enable_satisfaction
    :type: bool

    Specify whether to apply the graphical properties of the figure of merit only when a chosen satisfaction criterion is met.

.. py:property:: satisfaction_type
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.satisfaction_type
    :type: FIGURE_OF_MERIT_SATISFACTION_TYPE

    Gets or sets the relationship to the specified threshold that must be achieved to satisfy the Figure of Merit.

.. py:property:: satisfaction_threshold
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.satisfaction_threshold
    :type: typing.Any

    Gets or sets the threshold for satisfying the Figure of Merit.

.. py:property:: invalid_data_indicator
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.invalid_data_indicator
    :type: typing.Any

    A value to indicate when contouring is invalid.

.. py:property:: use_value_range_check
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.use_value_range_check
    :type: bool

    Enable FOM Values Limits for computing Statistics.

.. py:property:: min_value_range
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.min_value_range
    :type: typing.Any

    Gets or sets the Min Value in the range.

.. py:property:: max_value_range
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.max_value_range
    :type: typing.Any

    Gets or sets the Max Value in the range.

.. py:property:: exclude_value_range
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritSatisfaction.exclude_value_range
    :type: bool

    Exclude Value Range.


