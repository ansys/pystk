CalculationToolParameterSetVector
=================================

.. py:class:: ansys.stk.core.vgt.CalculationToolParameterSetVector

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolParameterSet`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Vector parameter set contains various representations of a vector in a reference set of axes.

.. py:currentmodule:: CalculationToolParameterSetVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetVector.vector`
              - Get the vector for which representations are computed.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetVector.reference_axes`
              - Get the reference axes relative to which representations are computed.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolParameterSetVector


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetVector.vector
    :type: IVectorGeometryToolVector

    Get the vector for which representations are computed.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetVector.reference_axes
    :type: IVectorGeometryToolAxes

    Get the reference axes relative to which representations are computed.


