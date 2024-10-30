AccessConstraintAnalysisWorkbenchCollection
===========================================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAccessConstraint`

   Collection of Analysis Workbench constraints.

.. py:currentmodule:: AccessConstraintAnalysisWorkbenchCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_index`
              - Remove an item given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_all`
              - Remove all items from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_constraint`
              - Remove a Analysis Workbench using Reference/Component.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.add_constraint`
              - Add a constraint to the AWB Constraint Collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.get_available_references`
              - Return an array of available References.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.item`
              - Get an IAgAccessCnstrAWB interface using an index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.count`
              - Number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection._NewEnum`
              - Enumerate the IAgAccessCnstrAWB interfaces.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintAnalysisWorkbenchCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.count
    :type: int

    Number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection._NewEnum
    :type: EnumeratorProxy

    Enumerate the IAgAccessCnstrAWB interfaces.


Method detail
-------------


.. py:method:: remove_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_index

    Remove an item given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_all

    Remove all items from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_constraint(self, type: ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE, reference: str) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_constraint

    Remove a Analysis Workbench using Reference/Component.

    :Parameters:

    **type** : :obj:`~ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE`
    **reference** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_constraint(self, eConstraint: ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE, reference: str) -> IAccessConstraint
    :canonical: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.add_constraint

    Add a constraint to the AWB Constraint Collection.

    :Parameters:

    **eConstraint** : :obj:`~ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE`
    **reference** : :obj:`~str`

    :Returns:

        :obj:`~IAccessConstraint`

.. py:method:: get_available_references(self, type: ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE) -> list
    :canonical: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.get_available_references

    Return an array of available References.

    :Parameters:

    **type** : :obj:`~ANALYSIS_WORKBENCH_ACCESS_CONSTRAINT_TYPE`

    :Returns:

        :obj:`~list`

.. py:method:: item(self, index: int) -> AccessConstraintAnalysisWorkbench
    :canonical: ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.item

    Get an IAgAccessCnstrAWB interface using an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AccessConstraintAnalysisWorkbench`


