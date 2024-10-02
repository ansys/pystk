CalculationToolScalarVectorMagnitude
====================================

.. py:class:: ansys.stk.core.vgt.CalculationToolScalarVectorMagnitude

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Scalar equal to the magnitude of a specified vector.

.. py:currentmodule:: CalculationToolScalarVectorMagnitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarVectorMagnitude.input_vector`
              - Specify any vector in VGT. Note that its magnitude is reference axes independent which is why it is not specified.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolScalarVectorMagnitude


Property detail
---------------

.. py:property:: input_vector
    :canonical: ansys.stk.core.vgt.CalculationToolScalarVectorMagnitude.input_vector
    :type: IVectorGeometryToolVector

    Specify any vector in VGT. Note that its magnitude is reference axes independent which is why it is not specified.


