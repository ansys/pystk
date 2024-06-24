ISpatialAnalysisToolGridValuesFixedNumberOfSteps
================================================

.. py:class:: ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps

   object
   
   Fixed step grid values.

.. py:currentmodule:: ISpatialAnalysisToolGridValuesFixedNumberOfSteps

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.min`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.max`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.number_of_steps`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.min_ex`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.max_ex`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolGridValuesFixedNumberOfSteps


Property detail
---------------

.. py:property:: min
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.min
    :type: float

    This property is deprecated. Use MinEx.

.. py:property:: max
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.max
    :type: float

    This property is deprecated. Use MaxEx.

.. py:property:: number_of_steps
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.number_of_steps
    :type: int

    The number of steps between coordinate values.

.. py:property:: min_ex
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.min_ex
    :type: IQuantity

    Minimum coordinate value as IAgQuantity.

.. py:property:: max_ex
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.max_ex
    :type: IQuantity

    Maximum coordinate value as IAgQuantity.


