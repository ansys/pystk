IAccessConstraint
=================

.. py:class:: ansys.stk.core.stkobjects.IAccessConstraint

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
              - Return true if the access constraint is a plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.exclusion_interval`
              - Exclude Time Intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.constraint_type`
              - Property used to access the constraint type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.maximum_time_step`
              - Maximum time step used in adaptive sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraint.maximum_relative_motion`
              - Maximum relative motion used in adaptive sampling.


Examples
--------

Add an Exclusion Zone access constraint

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    excludeZone: "AccessConstraintLatitudeLongitudeZone" = accessConstraints.add_named_constraint('ExclusionZone')
    excludeZone.maximum_latitude = 45
    excludeZone.minimum_latitude = 15
    excludeZone.minimum_longitude = -75
    excludeZone.maximum_longitude = -35


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

    Return true if the access constraint is a plugin.

.. py:property:: exclusion_interval
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.exclusion_interval
    :type: bool

    Exclude Time Intervals.

.. py:property:: constraint_type
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.constraint_type
    :type: AccessConstraintType

    Property used to access the constraint type.

.. py:property:: maximum_time_step
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.maximum_time_step
    :type: float

    Maximum time step used in adaptive sampling.

.. py:property:: maximum_relative_motion
    :canonical: ansys.stk.core.stkobjects.IAccessConstraint.maximum_relative_motion
    :type: float

    Maximum relative motion used in adaptive sampling.


