CalculationToolScalarVectorMagnitude
====================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarVectorMagnitude

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Scalar equal to the magnitude of a specified vector.

.. py:currentmodule:: CalculationToolScalarVectorMagnitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarVectorMagnitude.input_vector`
              - Specify any vector in VGT. Note that its magnitude is reference axes independent which is why it is not specified.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarVectorMagnitude


Property detail
---------------

.. py:property:: input_vector
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarVectorMagnitude.input_vector
    :type: IVectorGeometryToolVector

    Specify any vector in VGT. Note that its magnitude is reference axes independent which is why it is not specified.


