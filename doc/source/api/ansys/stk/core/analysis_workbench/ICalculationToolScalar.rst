ICalculationToolScalar
======================

.. py:class:: ansys.stk.core.analysis_workbench.ICalculationToolScalar

   Any scalar calculation that is not constant by construction.

.. py:currentmodule:: ICalculationToolScalar

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.evaluate`
              - Evaluate the scalar calculation at the specified time instant.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate`
              - Evaluate the scalar calculation at the specified time instant and returns the results as an array with two elements, the first element being of boolean type indicating whether the computation succeeded, followed by a double-precision value representing...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.evaluate_with_rate`
              - Evaluate the scalar calculation at the specified time instant. The result is a scalar value and its rate of change.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_with_rate`
              - Evaluate the scalar calculation at the specified time instant and returns the results as an array with three elements, the first element being of boolean type indicating whether the computation succeeded, followed by two double-precision values one rep...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.get_availability`
              - Return a list of availability intervals.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_array`
              - Evaluate the scalar calculation, and rate, over an array of times, entered as strings in the Scenario date unit. It returns an array corresponding to the input times...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_with_rate_array`
              - Evaluate the scalar calculation over the array of times provided by an Event Array component. It returns an array corresponding to the input times...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_time_array`
              - Evaluate the scalar calculation, and rate, over the array of times provided by an Event Array component. It returns an array corresponding to the input times...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_with_rate_event_array`
              - Evaluate the scalar calculation, and rate, over the array of times provided by an Event Array component. It returns an array corresponding to the input times...

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.type`
              - Return the scalar calculation type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar.unit_of_measure`
              - Return calc scalar's unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import ICalculationToolScalar


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.type
    :type: CalculationScalarType

    Return the scalar calculation type.

.. py:property:: unit_of_measure
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.unit_of_measure
    :type: str

    Return calc scalar's unit of measure, i.e. 'AngleUnit', 'DistanceUnit', etc.


Method detail
-------------


.. py:method:: evaluate(self, epoch: typing.Any) -> CalculationToolEvaluateResult
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.evaluate

    Evaluate the scalar calculation at the specified time instant.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~CalculationToolEvaluateResult`

.. py:method:: quick_evaluate(self, epoch: typing.Any) -> list
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate

    Evaluate the scalar calculation at the specified time instant and returns the results as an array with two elements, the first element being of boolean type indicating whether the computation succeeded, followed by a double-precision value representing...

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: evaluate_with_rate(self, epoch: typing.Any) -> CalculationToolEvaluateWithRateResult
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.evaluate_with_rate

    Evaluate the scalar calculation at the specified time instant. The result is a scalar value and its rate of change.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~CalculationToolEvaluateWithRateResult`

.. py:method:: quick_evaluate_with_rate(self, epoch: typing.Any) -> list
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_with_rate

    Evaluate the scalar calculation at the specified time instant and returns the results as an array with three elements, the first element being of boolean type indicating whether the computation succeeded, followed by two double-precision values one rep...

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: get_availability(self) -> TimeToolIntervalCollection
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.get_availability

    Return a list of availability intervals.

    :Returns:

        :obj:`~TimeToolIntervalCollection`


.. py:method:: quick_evaluate_array(self, times: list) -> list
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_array

    Evaluate the scalar calculation, and rate, over an array of times, entered as strings in the Scenario date unit. It returns an array corresponding to the input times...

    :Parameters:

        **times** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: quick_evaluate_with_rate_array(self, times: list) -> list
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_with_rate_array

    Evaluate the scalar calculation over the array of times provided by an Event Array component. It returns an array corresponding to the input times...

    :Parameters:

        **times** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: quick_evaluate_time_array(self, ref_array: ITimeToolTimeArray) -> list
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_time_array

    Evaluate the scalar calculation, and rate, over the array of times provided by an Event Array component. It returns an array corresponding to the input times...

    :Parameters:

        **ref_array** : :obj:`~ITimeToolTimeArray`


    :Returns:

        :obj:`~list`

.. py:method:: quick_evaluate_with_rate_event_array(self, ref_array: ITimeToolTimeArray) -> list
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolScalar.quick_evaluate_with_rate_event_array

    Evaluate the scalar calculation, and rate, over the array of times provided by an Event Array component. It returns an array corresponding to the input times...

    :Parameters:

        **ref_array** : :obj:`~ITimeToolTimeArray`


    :Returns:

        :obj:`~list`

