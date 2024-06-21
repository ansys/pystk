IOnePointAccessConstraint
=========================

.. py:class:: ansys.stk.core.stkobjects.IOnePointAccessConstraint

   object
   
   One Point Access Result.

.. py:currentmodule:: IOnePointAccessConstraint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessConstraint.status`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessConstraint.constraint`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessConstraint.value`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccessConstraint.object_path`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOnePointAccessConstraint


Property detail
---------------

.. py:property:: status
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessConstraint.status
    :type: ONE_POINT_ACCESS_STATUS

    An indicator describing the status  of whether the constraint is satisfied or violated at the computed time.

.. py:property:: constraint
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessConstraint.constraint
    :type: ACCESS_CONSTRAINTS

    Get the type of the constraint being evaluated.

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessConstraint.value
    :type: float

    Get the value of the constraint at the computed time, in internal units.

.. py:property:: object_path
    :canonical: ansys.stk.core.stkobjects.IOnePointAccessConstraint.object_path
    :type: str

    Get the object path of the owner of the constraint.


