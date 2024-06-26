IAccessConstraint
=================

.. py:class:: ansys.stk.core.stkobjects.IAccessConstraint

   object
   
   AgAccessConstraint used to access the AccessConstraint attributes.

.. py:currentmodule:: IAccessConstraint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.constraint_name`
              - Property used to access the constraint name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.is_plugin`
              - Returns true if the access constraint is a plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.excl_intvl`
              - Exclude Time Intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.constraint_type`
              - Property used to access the constraint type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.max_time_step`
              - Maximum time step used in adaptive sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.max_rel_motion`
              - Maximum relative motion used in adaptive sampling.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraint


Property detail
---------------

.. py:property:: constraint_name
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.constraint_name
    :type: str

    Property used to access the constraint name.

.. py:property:: is_plugin
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.is_plugin
    :type: bool

    Returns true if the access constraint is a plugin.

.. py:property:: excl_intvl
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.excl_intvl
    :type: bool

    Exclude Time Intervals.

.. py:property:: constraint_type
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.constraint_type
    :type: ACCESS_CONSTRAINTS

    Property used to access the constraint type.

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.max_time_step
    :type: float

    Maximum time step used in adaptive sampling.

.. py:property:: max_rel_motion
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.max_rel_motion
    :type: float

    Maximum relative motion used in adaptive sampling.


