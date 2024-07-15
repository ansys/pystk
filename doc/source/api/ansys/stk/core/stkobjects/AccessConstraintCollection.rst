AccessConstraintCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintCollection

   Bases: 

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
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection._NewEnum`
              - Enumerate the AccessConstraint items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.analysis_workbench_constraints`
              - Returns a AgAccessCnstrAWBCollection constraint used to access angle, vector and condition constraint.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.use_preferred_max_time_step`
              - Flag indicating that the preferred max time step should be used in access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintCollection.preferred_max_time_step`
              - Maximum time step to be considered in access computations. New access computations consider this value when determining a suitable maximum step size.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection._NewEnum
    :type: EnumeratorProxy

    Enumerate the AccessConstraint items in the collection.

.. py:property:: analysis_workbench_constraints
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.analysis_workbench_constraints
    :type: IAccessConstraintAnalysisWorkbenchCollection

    Returns a AgAccessCnstrAWBCollection constraint used to access angle, vector and condition constraint.

.. py:property:: use_preferred_max_time_step
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.use_preferred_max_time_step
    :type: bool

    Flag indicating that the preferred max time step should be used in access computations.

.. py:property:: preferred_max_time_step
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.preferred_max_time_step
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


.. py:method:: add_constraint(self, eConstraint: ACCESS_CONSTRAINTS) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.add_constraint

    Add a constraint to the Constraint Collection.

    :Parameters:

    **eConstraint** : :obj:`~ACCESS_CONSTRAINTS`

    :Returns:

        :obj:`~IAccessConstraint`

.. py:method:: remove_constraint(self, eConstraint: ACCESS_CONSTRAINTS) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.remove_constraint

    Remove a constraint from the collection.

    :Parameters:

    **eConstraint** : :obj:`~ACCESS_CONSTRAINTS`

    :Returns:

        :obj:`~None`

.. py:method:: get_active_constraint(self, eConstraint: ACCESS_CONSTRAINTS) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.get_active_constraint

    Retrieve the active constraint.

    :Parameters:

    **eConstraint** : :obj:`~ACCESS_CONSTRAINTS`

    :Returns:

        :obj:`~IAccessConstraint`

.. py:method:: is_constraint_active(self, eConstraint: ACCESS_CONSTRAINTS) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.is_constraint_active

    Given an AgEAccessConstraints enum, informs the user if the constraint is active.

    :Parameters:

    **eConstraint** : :obj:`~ACCESS_CONSTRAINTS`

    :Returns:

        :obj:`~bool`

.. py:method:: available_constraints(self) -> list
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.available_constraints

    Return a rectangular two-dimensional array of available constraints. A row of the array consists of two elements where the first element is a symbolic name of the constraint and the second is a corresponding enumeration value.

    :Returns:

        :obj:`~list`

.. py:method:: is_constraint_supported(self, eConstraint: ACCESS_CONSTRAINTS) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.is_constraint_supported

    Is the constraint supported for this object.

    :Parameters:

    **eConstraint** : :obj:`~ACCESS_CONSTRAINTS`

    :Returns:

        :obj:`~bool`

.. py:method:: is_named_constraint_supported(self, cnstrName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.is_named_constraint_supported

    Is the named constraint supported for this object.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_named_constraint(self, cnstrName: str) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.add_named_constraint

    Add a constraint with the given name to the collection.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~IAccessConstraint`

.. py:method:: remove_named_constraint(self, cnstrName: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.remove_named_constraint

    Do not use this method, as it is deprecated. Use RemoveNamedConstraintEx instead. Removes a constraint with the given name from the collection.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: is_named_constraint_active(self, cnstrName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.is_named_constraint_active

    Given a constraint name, returns whether the specified constraint is active.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: get_active_named_constraint(self, cnstrName: str) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.get_active_named_constraint

    Retrieve an active constraint with the given name.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~IAccessConstraint`






.. py:method:: remove_named_constraint_ex(self, cnstrName: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintCollection.remove_named_constraint_ex

    Remove a constraint with the given name from the collection.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~None`

