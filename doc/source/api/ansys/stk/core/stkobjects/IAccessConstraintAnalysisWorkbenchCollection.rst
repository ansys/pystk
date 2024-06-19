IAccessConstraintAnalysisWorkbenchCollection
============================================

.. py:class:: IAccessConstraintAnalysisWorkbenchCollection

   object
   
   IAgAccessCnstrAWBCollection used to access angle, vector and condition constraint List interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove_index`
              - Remove an item given an index.
            * - :py:meth:`~remove_all`
              - Remove all items from the collection.
            * - :py:meth:`~remove_constraint`
              - Remove a Analysis Workbench using Reference/Component.
            * - :py:meth:`~add_constraint`
              - Add a constraint to the AWB Constraint Collection.
            * - :py:meth:`~get_available_references`
              - Return an array of available References.
            * - :py:meth:`~item`
              - Get an IAgAccessCnstrAWB interface using an index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintAnalysisWorkbenchCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintAnalysisWorkbenchCollection.count
    :type: int

    Number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintAnalysisWorkbenchCollection._NewEnum
    :type: EnumeratorProxy

    Enumerate the IAgAccessCnstrAWB interfaces.


Method detail
-------------


.. py:method:: remove_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintAnalysisWorkbenchCollection.remove_index

    Remove an item given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintAnalysisWorkbenchCollection.remove_all

    Remove all items from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_constraint(self, type: ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS, reference: str) -> None
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintAnalysisWorkbenchCollection.remove_constraint

    Remove a Analysis Workbench using Reference/Component.

    :Parameters:

    **type** : :obj:`~ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS`
    **reference** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_constraint(self, eConstraint: ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS, reference: str) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintAnalysisWorkbenchCollection.add_constraint

    Add a constraint to the AWB Constraint Collection.

    :Parameters:

    **eConstraint** : :obj:`~ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS`
    **reference** : :obj:`~str`

    :Returns:

        :obj:`~IAccessConstraint`

.. py:method:: get_available_references(self, type: ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS) -> list
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintAnalysisWorkbenchCollection.get_available_references

    Return an array of available References.

    :Parameters:

    **type** : :obj:`~ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS`

    :Returns:

        :obj:`~list`

.. py:method:: item(self, index: int) -> IAccessConstraintAnalysisWorkbench
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintAnalysisWorkbenchCollection.item

    Get an IAgAccessCnstrAWB interface using an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAccessConstraintAnalysisWorkbench`


