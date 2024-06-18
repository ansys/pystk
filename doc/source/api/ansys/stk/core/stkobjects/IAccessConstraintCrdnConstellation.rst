IAccessConstraintCrdnConstellation
==================================

.. py:class:: IAccessConstraintCrdnConstellation

   IAccessConstraint
   
   Access Constraint used for Vector Constraints.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_min`
            * - :py:meth:`~enable_max`
            * - :py:meth:`~min`
            * - :py:meth:`~max`
            * - :py:meth:`~reference`
            * - :py:meth:`~available_references`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintCrdnConstellation


Property detail
---------------

.. py:property:: enable_min
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCrdnConstellation.enable_min
    :type: bool

    Enables the Min property.

.. py:property:: enable_max
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCrdnConstellation.enable_max
    :type: bool

    Enables the Max property.

.. py:property:: min
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCrdnConstellation.min
    :type: typing.Any

    Min value for the access constraint.

.. py:property:: max
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCrdnConstellation.max
    :type: typing.Any

    Max value for the access constraint.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCrdnConstellation.reference
    :type: str

    Reference value for the access constraint.

.. py:property:: available_references
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCrdnConstellation.available_references
    :type: list

    Returns an array of available References.


