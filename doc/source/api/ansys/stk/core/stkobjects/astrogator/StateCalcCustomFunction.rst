StateCalcCustomFunction
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Custom Function Calc objects.

.. py:currentmodule:: StateCalcCustomFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction.eval_function_name`
              - Get or set the custom function used to calculate this object's value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction.reset_function_name`
              - Get or set the custom function called before computing, before each segment runs, and before reporting.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction.unit_dimension`
              - Get or set the unit dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcCustomFunction


Property detail
---------------

.. py:property:: eval_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction.eval_function_name
    :type: str

    Get or set the custom function used to calculate this object's value.

.. py:property:: reset_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction.reset_function_name
    :type: str

    Get or set the custom function called before computing, before each segment runs, and before reporting.

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction.unit_dimension
    :type: str

    Get or set the unit dimension.


