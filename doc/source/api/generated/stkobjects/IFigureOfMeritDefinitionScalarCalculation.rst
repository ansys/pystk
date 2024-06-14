IFigureOfMeritDefinitionScalarCalculation
=========================================

.. py:class:: IFigureOfMeritDefinitionScalarCalculation

   IFigureOfMeritDefinitionCompute
   
   Figure of Merit using an Analysis Workbench scalar calculation component as the metric.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~time_step`
            * - :py:meth:`~calc_scalar`
            * - :py:meth:`~should_update_accesses`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionScalarCalculation


Property detail
---------------

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionScalarCalculation.time_step
    :type: float

    Gets or sets the value to be used during the sampling of the dynamic definition for use in the static definition.

.. py:property:: calc_scalar
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionScalarCalculation.calc_scalar
    :type: str

    Reference Scalar Calculation component.

.. py:property:: should_update_accesses
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionScalarCalculation.should_update_accesses
    :type: bool

    Update Accesses computed outside Coverage.


