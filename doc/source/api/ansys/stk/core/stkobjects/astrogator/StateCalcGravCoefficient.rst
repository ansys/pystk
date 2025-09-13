StateCalcGravCoefficient
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Gravity Coefficient Calc objects.

.. py:currentmodule:: StateCalcGravCoefficient

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.coefficient_type`
              - Coefficient type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.degree`
              - Degree of the coefficient.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.gravity_filename`
              - Source for the gravity coefficient.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.normalization_type`
              - Normalization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.order`
              - Order of the coefficient.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcGravCoefficient


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: coefficient_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.coefficient_type
    :type: GravityCoefficientType

    Coefficient type.

.. py:property:: degree
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.degree
    :type: int

    Degree of the coefficient.

.. py:property:: gravity_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.gravity_filename
    :type: str

    Source for the gravity coefficient.

.. py:property:: normalization_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.normalization_type
    :type: GravityCoefficientNormalizationType

    Normalization type.

.. py:property:: order
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravCoefficient.order
    :type: int

    Order of the coefficient.


