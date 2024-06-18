IFigureOfMeritDefinitionAccessConstraint
========================================

.. py:class:: IFigureOfMeritDefinitionAccessConstraint

   IFigureOfMeritDefinitionCompute
   
   Access Constraint Figure of Merit.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~across_assets`
            * - :py:meth:`~time_step`
            * - :py:meth:`~constraint_name`
            * - :py:meth:`~constraint`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionAccessConstraint


Property detail
---------------

.. py:property:: across_assets
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionAccessConstraint.across_assets
    :type: "FIGURE_OF_MERIT_ACROSS_ASSETS"

    Value of the constraint that is to be selected based on all currently available assets.

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionAccessConstraint.time_step
    :type: float

    Gets or sets the value to be used during the sampling of the dynamic definition for use in the static definition.

.. py:property:: constraint_name
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionAccessConstraint.constraint_name
    :type: "FIGURE_OF_MERIT_CONSTRAINT_NAME"

    Name of the access constraint as an enumeration. If the constraint is not in AgEFmConstraintName then use Constraint instead.

.. py:property:: constraint
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionAccessConstraint.constraint
    :type: str

    Name of the access constraint.


