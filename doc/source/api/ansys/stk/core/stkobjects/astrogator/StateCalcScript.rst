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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript.calc_arguments`
              - Get the arguments to be applied to the function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript.inline_func`
              - Gets or sets the expression to be applied as a function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript.unit_dimension`
              - Gets or sets the unit dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript.calc_arguments_link_embed`
              - Get the arguments to be applied to the function.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcScript


Property detail
---------------

.. py:property:: calc_arguments
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcScript.calc_arguments
    :type: ICalcObjectCollection

    Get the arguments to be applied to the function.

.. py:property:: inline_func
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcScript.inline_func
    :type: str

    Gets or sets the expression to be applied as a function.

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcScript.unit_dimension
    :type: str

    Gets or sets the unit dimension.

.. py:property:: calc_arguments_link_embed
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcScript.calc_arguments_link_embed
    :type: ICalcObjectLinkEmbedControlCollection

    Get the arguments to be applied to the function.


