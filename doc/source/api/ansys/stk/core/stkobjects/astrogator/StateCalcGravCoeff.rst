StateCalcGravCoeff
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Gravity Coefficient Calc objects.

.. py:currentmodule:: StateCalcGravCoeff

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.gravity_filename`
              - Source for the gravity coefficient.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.coefficient_type`
              - Coefficient type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.degree`
              - Degree of the coefficient.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.order`
              - Order of the coefficient.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.normalization_type`
              - Normalization type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcGravCoeff


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: gravity_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.gravity_filename
    :type: str

    Source for the gravity coefficient.

.. py:property:: coefficient_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.coefficient_type
    :type: GravityCoefficientType

    Coefficient type.

.. py:property:: degree
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.degree
    :type: int

    Degree of the coefficient.

.. py:property:: order
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.order
    :type: int

    Order of the coefficient.

.. py:property:: normalization_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff.normalization_type
    :type: GravityCoefficientNormalizationType

    Normalization type.


