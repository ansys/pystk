SpatialAnalysisToolGridValuesFixedStep
======================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolGridValuesMethod`

   Fixed step grid values.

.. py:currentmodule:: SpatialAnalysisToolGridValuesFixedStep

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.include_minimum_maximum`
              - Flag indicating whether to include minimum and maximum coordinate values in the defined set of values.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.maximum`
              - Maximum coordinate value.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.minimum`
              - Minimum coordinate value.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.reference_value`
              - Reference coordinate value from which steps are taken.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.step`
              - Step between subsequent coordinate values.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolGridValuesFixedStep


Property detail
---------------

.. py:property:: include_minimum_maximum
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.include_minimum_maximum
    :type: bool

    Flag indicating whether to include minimum and maximum coordinate values in the defined set of values.

.. py:property:: maximum
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.maximum
    :type: float

    Maximum coordinate value.

.. py:property:: minimum
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.minimum
    :type: float

    Minimum coordinate value.

.. py:property:: reference_value
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.reference_value
    :type: float

    Reference coordinate value from which steps are taken.

.. py:property:: step
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep.step
    :type: float

    Step between subsequent coordinate values.


