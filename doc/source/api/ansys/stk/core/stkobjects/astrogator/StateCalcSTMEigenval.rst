StateCalcSTMEigenval
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Cartesian STM Eigenvalues Calc objects.

.. py:currentmodule:: StateCalcSTMEigenval

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval.coord_system_name`
              - Get or set the coordinate system within which the element is defined.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval.eigenvalue_number`
              - Get or set the number identifying one of the six Eigenvalues.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval.eigenvalue_complex_part`
              - Whether this value represents the real or imaginary part of the Eigenvalue.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcSTMEigenval


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval.coord_system_name
    :type: str

    Get or set the coordinate system within which the element is defined.

.. py:property:: eigenvalue_number
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval.eigenvalue_number
    :type: STMEigenNumber

    Get or set the number identifying one of the six Eigenvalues.

.. py:property:: eigenvalue_complex_part
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval.eigenvalue_complex_part
    :type: ComplexNumber

    Whether this value represents the real or imaginary part of the Eigenvalue.


