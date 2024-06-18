IAccessConstraintCollection
===========================

.. py:class:: IAccessConstraintCollection

   object
   
   AgAccessConstraintCollection used to access the list of constraints.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return an AccessConstraint interface using an index.
            * - :py:meth:`~add_constraint`
              - Add a constraint to the Constraint Collection.
            * - :py:meth:`~remove_constraint`
              - Remove a constraint from the collection.
            * - :py:meth:`~get_active_constraint`
              - Retrieve the active constraint.
            * - :py:meth:`~is_constraint_active`
              - Given an AgEAccessConstraints enum, informs the user if the constraint is active.
            * - :py:meth:`~available_constraints`
              - Return a rectangular two-dimensional array of available constraints. A row of the array consists of two elements where the first element is a symbolic name of the constraint and the second is a corresponding enumeration value.
            * - :py:meth:`~is_constraint_supported`
              - Is the constraint supported for this object.
            * - :py:meth:`~is_named_constraint_supported`
              - Is the named constraint supported for this object.
            * - :py:meth:`~add_named_constraint`
              - Add a constraint with the given name to the collection.
            * - :py:meth:`~remove_named_constraint`
              - Do not use this method, as it is deprecated. Use RemoveNamedConstraintEx instead. Removes a constraint with the given name from the collection.
            * - :py:meth:`~is_named_constraint_active`
              - Given a constraint name, returns whether the specified constraint is active.
            * - :py:meth:`~get_active_named_constraint`
              - Retrieve an active constraint with the given name.
            * - :py:meth:`~remove_named_constraint_ex`
              - Remove a constraint with the given name from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~analysis_workbench_constraints`
            * - :py:meth:`~use_preferred_max_time_step`
            * - :py:meth:`~preferred_max_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCollection._NewEnum
    :type: EnumeratorProxy

    Enumerate the AccessConstraint items in the collection.

.. py:property:: analysis_workbench_constraints
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCollection.analysis_workbench_constraints
    :type: "IAgAccessCnstrAWBCollection"

    Returns a AgAccessCnstrAWBCollection constraint used to access angle, vector and condition constraint.

.. py:property:: use_preferred_max_time_step
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCollection.use_preferred_max_time_step
    :type: bool

    Flag indicating that the preferred max time step should be used in access computations.

.. py:property:: preferred_max_time_step
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintCollection.preferred_max_time_step
    :type: float

    Maximum time step to be considered in access computations. New access computations consider this value when determining a suitable maximum step size.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IAccessConstraint"

    Return an AccessConstraint interface using an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IAccessConstraint"`


.. py:method:: add_constraint(self, eConstraint:"ACCESS_CONSTRAINTS") -> "IAccessConstraint"

    Add a constraint to the Constraint Collection.

    :Parameters:

    **eConstraint** : :obj:`~"ACCESS_CONSTRAINTS"`

    :Returns:

        :obj:`~"IAccessConstraint"`

.. py:method:: remove_constraint(self, eConstraint:"ACCESS_CONSTRAINTS") -> None

    Remove a constraint from the collection.

    :Parameters:

    **eConstraint** : :obj:`~"ACCESS_CONSTRAINTS"`

    :Returns:

        :obj:`~None`

.. py:method:: get_active_constraint(self, eConstraint:"ACCESS_CONSTRAINTS") -> "IAccessConstraint"

    Retrieve the active constraint.

    :Parameters:

    **eConstraint** : :obj:`~"ACCESS_CONSTRAINTS"`

    :Returns:

        :obj:`~"IAccessConstraint"`

.. py:method:: is_constraint_active(self, eConstraint:"ACCESS_CONSTRAINTS") -> bool

    Given an AgEAccessConstraints enum, informs the user if the constraint is active.

    :Parameters:

    **eConstraint** : :obj:`~"ACCESS_CONSTRAINTS"`

    :Returns:

        :obj:`~bool`

.. py:method:: available_constraints(self) -> list

    Return a rectangular two-dimensional array of available constraints. A row of the array consists of two elements where the first element is a symbolic name of the constraint and the second is a corresponding enumeration value.

    :Returns:

        :obj:`~list`

.. py:method:: is_constraint_supported(self, eConstraint:"ACCESS_CONSTRAINTS") -> bool

    Is the constraint supported for this object.

    :Parameters:

    **eConstraint** : :obj:`~"ACCESS_CONSTRAINTS"`

    :Returns:

        :obj:`~bool`

.. py:method:: is_named_constraint_supported(self, cnstrName:str) -> bool

    Is the named constraint supported for this object.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_named_constraint(self, cnstrName:str) -> "IAccessConstraint"

    Add a constraint with the given name to the collection.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~"IAccessConstraint"`

.. py:method:: remove_named_constraint(self, cnstrName:str) -> None

    Do not use this method, as it is deprecated. Use RemoveNamedConstraintEx instead. Removes a constraint with the given name from the collection.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: is_named_constraint_active(self, cnstrName:str) -> bool

    Given a constraint name, returns whether the specified constraint is active.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: get_active_named_constraint(self, cnstrName:str) -> "IAccessConstraint"

    Retrieve an active constraint with the given name.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~"IAccessConstraint"`






.. py:method:: remove_named_constraint_ex(self, cnstrName:str) -> None

    Remove a constraint with the given name from the collection.

    :Parameters:

    **cnstrName** : :obj:`~str`

    :Returns:

        :obj:`~None`

