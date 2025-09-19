OnePointAccessResult
====================

.. py:class:: ansys.stk.core.stkobjects.OnePointAccessResult

   One Point Access Result.

.. py:currentmodule:: OnePointAccessResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessResult.access_is_satisfied`
              - Indicate whether all constraints are satisfied at this time.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessResult.constraints`
              - List of constraints evaluated at this time.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessResult.time`
              - Get the time of evaluation of the constraints in a OnePointAccess Compute request.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OnePointAccessResult


Property detail
---------------

.. py:property:: access_is_satisfied
    :canonical: ansys.stk.core.stkobjects.OnePointAccessResult.access_is_satisfied
    :type: bool

    Indicate whether all constraints are satisfied at this time.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.OnePointAccessResult.constraints
    :type: OnePointAccessConstraintCollection

    List of constraints evaluated at this time.

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.OnePointAccessResult.time
    :type: typing.Any

    Get the time of evaluation of the constraints in a OnePointAccess Compute request.


