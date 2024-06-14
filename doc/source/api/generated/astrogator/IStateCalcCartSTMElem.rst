IStateCalcCartSTMElem
=====================

.. py:class:: IStateCalcCartSTMElem

   object
   
   Properties for a Cartesian STM Element calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~coord_system_name`
            * - :py:meth:`~final_var`
            * - :py:meth:`~init_var`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcCartSTMElem


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCartSTMElem.coord_system_name
    :type: str

    Gets or sets the coordinate system within which the element is defined.

.. py:property:: final_var
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCartSTMElem.final_var
    :type: "STM_PERT_VARIABLES"

    Gets or sets the final variation variable.

.. py:property:: init_var
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCartSTMElem.init_var
    :type: "STM_PERT_VARIABLES"

    Gets or sets the initial variation variable.


