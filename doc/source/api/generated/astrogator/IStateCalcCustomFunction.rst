IStateCalcCustomFunction
========================

.. py:class:: IStateCalcCustomFunction

   object
   
   Properties for a Custom Function calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reset_function_name`
            * - :py:meth:`~eval_function_name`
            * - :py:meth:`~unit_dimension`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcCustomFunction


Property detail
---------------

.. py:property:: reset_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCustomFunction.reset_function_name
    :type: str

    Gets or sets the custom function called before computing, before each segment runs, and before reporting.

.. py:property:: eval_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCustomFunction.eval_function_name
    :type: str

    Gets or sets the custom function used to calculate this object's value.

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCustomFunction.unit_dimension
    :type: str

    Gets or sets the unit dimension.


