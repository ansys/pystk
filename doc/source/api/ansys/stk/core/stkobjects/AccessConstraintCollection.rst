AccessConstraintCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintCollection

   Collection of access constraints.

.. py:currentmodule:: AccessConstraintCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.item`
              - Return an AccessConstraint interface using an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.add_constraint`
              - Add a constraint to the Constraint Collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.remove_constraint`
              - Remove a constraint from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.get_active_constraint`
              - Retrieve the active constraint.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.is_constraint_active`
              - Given an AgEAccessConstraints enum, informs the user if the constraint is active.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.available_constraints`
              - Return a rectangular two-dimensional array of available constraints. A row of the array consists of two elements where the first element is a symbolic name of the constraint and the second is a corresponding enumeration value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.is_constraint_supported`
              - Is the constraint supported for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.is_named_constraint_supported`
              - Is the named constraint supported for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.add_named_constraint`
              - Add a constraint with the given name to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.remove_named_constraint`
              - Do not use this method, as it is deprecated. Use RemoveNamedConstraintEx instead. Removes a constraint with the given name from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.is_named_constraint_active`
              - Given a constraint name, returns whether the specified constraint is active.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.get_active_named_constraint`
              - Retrieve an active constraint with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.remove_named_constraint_ex`
              - Remove a constraint with the given name from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.count`
              - Return the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection._new_enum`
              - Enumerate the AccessConstraint items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.analysis_workbench_constraints`
              - Return a AgAccessCnstrAWBCollection constraint used to access angle, vector and condition constraint.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.use_preferred_maximum_time_step`
              - Flag indicating that the preferred max time step should be used in access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.preferred_maximum_time_step`
              - Maximum time step to be considered in access computations. New access computations consider this value when determining a suitable maximum step size.



Examples
--------

Get handle to the object access constraints

.. code-block:: python

    # Satellitesatellite: Satellite object
    accessConstraints = satellite.access_constraints


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.count
    :type: int

    Return the size of the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection._new_enum
    :type: EnumeratorProxy

    Enumerate the AccessConstraint items in the collection.

.. py:property:: analysis_workbench_constraints
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.analysis_workbench_constraints
    :type: AccessConstraintAnalysisWorkbenchCollection

    Return a AgAccessCnstrAWBCollection constraint used to access angle, vector and condition constraint.

.. py:property:: use_preferred_maximum_time_step
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.use_preferred_maximum_time_step
    :type: bool

    Flag indicating that the preferred max time step should be used in access computations.

.. py:property:: preferred_maximum_time_step
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.preferred_maximum_time_step
    :type: float

    Maximum time step to be considered in access computations. New access computations consider this value when determining a suitable maximum step size.


Method detail
-------------


.. py:method:: item(self, index: int) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.item

    Return an AccessConstraint interface using an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAccessConstraint`


.. py:method:: add_constraint(self, constraint: AccessConstraintType) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.add_constraint

    Add a constraint to the Constraint Collection.

    :Parameters:

    **constraint** : :obj:`~AccessConstraintType`

    :Returns:

        :obj:`~IAccessConstraint`

.. py:method:: remove_constraint(self, constraint: AccessConstraintType) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.remove_constraint

    Remove a constraint from the collection.

    :Parameters:

    **constraint** : :obj:`~AccessConstraintType`

    :Returns:

        :obj:`~None`

.. py:method:: get_active_constraint(self, constraint: AccessConstraintType) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.get_active_constraint

    Retrieve the active constraint.

    :Parameters:

    **constraint** : :obj:`~AccessConstraintType`

    :Returns:

        :obj:`~IAccessConstraint`

.. py:method:: is_constraint_active(self, constraint: AccessConstraintType) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.is_constraint_active

    Given an AgEAccessConstraints enum, informs the user if the constraint is active.

    :Parameters:

    **constraint** : :obj:`~AccessConstraintType`

    :Returns:

        :obj:`~bool`

.. py:method:: available_constraints(self) -> list
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.available_constraints

    Return a rectangular two-dimensional array of available constraints. A row of the array consists of two elements where the first element is a symbolic name of the constraint and the second is a corresponding enumeration value.

    :Returns:

        :obj:`~list`

.. py:method:: is_constraint_supported(self, constraint: AccessConstraintType) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.is_constraint_supported

    Is the constraint supported for this object.

    :Parameters:

    **constraint** : :obj:`~AccessConstraintType`

    :Returns:

        :obj:`~bool`

.. py:method:: is_named_constraint_supported(self, cnstr_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.is_named_constraint_supported

    Is the named constraint supported for this object.

    :Parameters:

    **cnstr_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_named_constraint(self, cnstr_name: str) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.add_named_constraint

    Add a constraint with the given name to the collection.

    :Parameters:

    **cnstr_name** : :obj:`~str`

    :Returns:

        :obj:`~IAccessConstraint`

.. py:method:: remove_named_constraint(self, cnstr_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.remove_named_constraint

    Do not use this method, as it is deprecated. Use RemoveNamedConstraintEx instead. Removes a constraint with the given name from the collection.

    :Parameters:

    **cnstr_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: is_named_constraint_active(self, cnstr_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.is_named_constraint_active

    Given a constraint name, returns whether the specified constraint is active.

    :Parameters:

    **cnstr_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: get_active_named_constraint(self, cnstr_name: str) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.get_active_named_constraint

    Retrieve an active constraint with the given name.

    :Parameters:

    **cnstr_name** : :obj:`~str`

    :Returns:

        :obj:`~IAccessConstraint`






.. py:method:: remove_named_constraint_ex(self, cnstr_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.remove_named_constraint_ex

    Remove a constraint with the given name from the collection.

    :Parameters:

    **cnstr_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

