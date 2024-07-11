IStateCalcScript
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcScript

   object
   
   Properties for a Script calculation object.

.. py:currentmodule:: IStateCalcScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcScript.calc_arguments`
              - Get the arguments to be applied to the function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcScript.inline_func`
              - Gets or sets the expression to be applied as a function.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcScript.unit_dimension`
              - Gets or sets the unit dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcScript.calc_arguments_link_embed`
              - Get the arguments to be applied to the function.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcScript


Property detail
---------------

.. py:property:: calc_arguments
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcScript.calc_arguments
    :type: ICalcObjectCollection

    Get the arguments to be applied to the function.

.. py:property:: inline_func
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcScript.inline_func
    :type: str

    Gets or sets the expression to be applied as a function.

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcScript.unit_dimension
    :type: str

    Gets or sets the unit dimension.

.. py:property:: calc_arguments_link_embed
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcScript.calc_arguments_link_embed
    :type: ICalcObjectLinkEmbedControlCollection

    Get the arguments to be applied to the function.


