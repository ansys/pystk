FigureOfMeritDefinitionScalarCalculation
========================================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation

   Bases: :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute`, :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinition`

   Scalar Calculation Figure of Merit.

.. py:currentmodule:: FigureOfMeritDefinitionScalarCalculation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation.time_step`
              - Gets or sets the value to be used during the sampling of the dynamic definition for use in the static definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation.calculation_scalar`
              - Reference Scalar Calculation component.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation.should_update_accesses`
              - Update Accesses computed outside Coverage.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritDefinitionScalarCalculation


Property detail
---------------

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation.time_step
    :type: float

    Gets or sets the value to be used during the sampling of the dynamic definition for use in the static definition.

.. py:property:: calculation_scalar
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation.calculation_scalar
    :type: str

    Reference Scalar Calculation component.

.. py:property:: should_update_accesses
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation.should_update_accesses
    :type: bool

    Update Accesses computed outside Coverage.


