StateCalcScript
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcScript

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Script Calc objects.

.. py:currentmodule:: StateCalcScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript.calculation_object_arguments`
              - Get the arguments to be applied to the function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript.calculation_object_arguments_link_embed`
              - Get the arguments to be applied to the function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript.inline_func`
              - Get or set the expression to be applied as a function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript.unit_dimension`
              - Get or set the unit dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcScript


Property detail
---------------

.. py:property:: calculation_object_arguments
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcScript.calculation_object_arguments
    :type: CalculationObjectCollection

    Get the arguments to be applied to the function.

.. py:property:: calculation_object_arguments_link_embed
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcScript.calculation_object_arguments_link_embed
    :type: CalculationObjectLinkEmbedControlCollection

    Get the arguments to be applied to the function.

.. py:property:: inline_func
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcScript.inline_func
    :type: str

    Get or set the expression to be applied as a function.

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcScript.unit_dimension
    :type: str

    Get or set the unit dimension.


