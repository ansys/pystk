IAccessConstraintMinMax
=======================

.. py:class:: IAccessConstraintMinMax

   IAccessConstraint
   
   Access Constraint used for min/max constraints.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintMinMax


Property detail
---------------

.. py:property:: enable_min
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintMinMax.enable_min
    :type: bool

    Enable the Min property.

.. py:property:: enable_max
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintMinMax.enable_max
    :type: bool

    Enable the Max property.

.. py:property:: min
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintMinMax.min
    :type: typing.Any

    Min value for the access constraint.

.. py:property:: max
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintMinMax.max
    :type: typing.Any

    Max value for the access constrain.


