IOnePointAccessResult
=====================

.. py:class:: ansys.stk.core.stkobjects.IOnePointAccessResult

   object
   
   One Point Access Result.

.. py:currentmodule:: IOnePointAccessResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessResult.access_satisfied`
              - Indicates whether all constraints are satisfied at this time.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessResult.time`
              - Get the time of evaluation of the constraints in a IAgOnePtAccess Compute request.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessResult.constraints`
              - List of constraints evaluated at this time.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOnePointAccessResult


Property detail
---------------

.. py:property:: access_satisfied
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessResult.access_satisfied
    :type: bool

    Indicates whether all constraints are satisfied at this time.

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessResult.time
    :type: typing.Any

    Get the time of evaluation of the constraints in a IAgOnePtAccess Compute request.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessResult.constraints
    :type: IOnePointAccessConstraintCollection

    List of constraints evaluated at this time.


