StateCalcCartSTMElem
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Cartesian STM Elements Calc objects.

.. py:currentmodule:: StateCalcCartSTMElem

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.coord_system_name`
              - Gets or sets the coordinate system within which the element is defined.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.final_var`
              - Gets or sets the final variation variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.init_var`
              - Gets or sets the initial variation variable.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcCartSTMElem


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.coord_system_name
    :type: str

    Gets or sets the coordinate system within which the element is defined.

.. py:property:: final_var
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.final_var
    :type: STM_PERT_VARIABLES

    Gets or sets the final variation variable.

.. py:property:: init_var
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.init_var
    :type: STM_PERT_VARIABLES

    Gets or sets the initial variation variable.


