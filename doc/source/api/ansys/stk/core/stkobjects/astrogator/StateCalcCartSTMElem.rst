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
              - Get or set the coordinate system within which the element is defined.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.final_state_component`
              - Get or set the final variation variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.initial_state_component`
              - Get or set the initial variation variable.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcCartSTMElem


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.coord_system_name
    :type: str

    Get or set the coordinate system within which the element is defined.

.. py:property:: final_state_component
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.final_state_component
    :type: STMPerturbationVariables

    Get or set the final variation variable.

.. py:property:: initial_state_component
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem.initial_state_component
    :type: STMPerturbationVariables

    Get or set the initial variation variable.


