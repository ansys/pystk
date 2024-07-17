SpatialAnalysisToolGridValuesFixedStep
======================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesMethod`

   Fixed step grid values.

.. py:currentmodule:: SpatialAnalysisToolGridValuesFixedStep

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.min`
              - Minimum coordinate value.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.max`
              - Maximum coordinate value.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.include_min_max`
              - Flag indicating whether to include minimum and maximum coordinate values in the defined set of values.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.reference_value`
              - Reference coordinate value from which steps are taken.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.step`
              - Step between subsequent coordinate values.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolGridValuesFixedStep


Property detail
---------------

.. py:property:: min
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.min
    :type: float

    Minimum coordinate value.

.. py:property:: max
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.max
    :type: float

    Maximum coordinate value.

.. py:property:: include_min_max
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.include_min_max
    :type: bool

    Flag indicating whether to include minimum and maximum coordinate values in the defined set of values.

.. py:property:: reference_value
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.reference_value
    :type: float

    Reference coordinate value from which steps are taken.

.. py:property:: step
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep.step
    :type: float

    Step between subsequent coordinate values.


