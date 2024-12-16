CalculationToolScalarVectorComponent
====================================

.. py:class:: ansys.stk.core.vgt.CalculationToolScalarVectorComponent

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   The specified component of a vector when resolved in the specified axes.

.. py:currentmodule:: CalculationToolScalarVectorComponent

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarVectorComponent.input_vector`
              - Vector.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarVectorComponent.reference_axes`
              - Axes used to resolve the vector's components.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarVectorComponent.component`
              - The component of the vector to return as the value of the scalar.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolScalarVectorComponent


Property detail
---------------

.. py:property:: input_vector
    :canonical: ansys.stk.core.vgt.CalculationToolScalarVectorComponent.input_vector
    :type: IVectorGeometryToolVector

    Vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.CalculationToolScalarVectorComponent.reference_axes
    :type: IVectorGeometryToolAxes

    Axes used to resolve the vector's components.

.. py:property:: component
    :canonical: ansys.stk.core.vgt.CalculationToolScalarVectorComponent.component
    :type: VectorComponentType

    The component of the vector to return as the value of the scalar.


