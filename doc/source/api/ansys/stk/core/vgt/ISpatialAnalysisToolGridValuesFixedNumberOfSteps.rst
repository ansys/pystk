ISpatialAnalysisToolGridValuesFixedNumberOfSteps
================================================

.. py:class:: ISpatialAnalysisToolGridValuesFixedNumberOfSteps

   object
   
   Fixed step grid values.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~min`
            * - :py:meth:`~max`
            * - :py:meth:`~number_of_steps`
            * - :py:meth:`~min_ex`
            * - :py:meth:`~max_ex`


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
    :type: IAgQuantity

    Minimum coordinate value as IAgQuantity.

.. py:property:: max_ex
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesFixedNumberOfSteps.max_ex
    :type: IAgQuantity

    Maximum coordinate value as IAgQuantity.


