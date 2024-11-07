ProcedureCollection
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureCollection

   Class defining the collection of procedures in the phase of an Aviator mission.

.. py:currentmodule:: ProcedureCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.add`
              - Add a procedure with the specified site at the end of the current phase.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.add_at_index`
              - Add a procedure with the specified site at the given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.remove`
              - Remove given procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.remove_at_index`
              - Remove procedure at the given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.enable_auto_propagate`
              - Enable automatically propagating the mission. Aviator will automatically propagate before adding a procedure, ensuring a valid initial state for the new procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.disable_auto_propagate`
              - Disable automatically propagating the mission. Use with caution. Aviator will not automatically propagate before adding new procedures.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IProcedure`


.. py:method:: add(self, site_type: SITE_TYPE, procedure_type: PROCEDURE_TYPE) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.add

    Add a procedure with the specified site at the end of the current phase.

    :Parameters:

    **site_type** : :obj:`~SITE_TYPE`
    **procedure_type** : :obj:`~PROCEDURE_TYPE`

    :Returns:

        :obj:`~IProcedure`

.. py:method:: add_at_index(self, index: int, site_type: SITE_TYPE, procedure_type: PROCEDURE_TYPE) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.add_at_index

    Add a procedure with the specified site at the given index.

    :Parameters:

    **index** : :obj:`~int`
    **site_type** : :obj:`~SITE_TYPE`
    **procedure_type** : :obj:`~PROCEDURE_TYPE`

    :Returns:

        :obj:`~IProcedure`

.. py:method:: remove(self, procedure: IProcedure) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.remove

    Remove given procedure.

    :Parameters:

    **procedure** : :obj:`~IProcedure`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.remove_at_index

    Remove procedure at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: enable_auto_propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.enable_auto_propagate

    Enable automatically propagating the mission. Aviator will automatically propagate before adding a procedure, ensuring a valid initial state for the new procedure.

    :Returns:

        :obj:`~None`

.. py:method:: disable_auto_propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureCollection.disable_auto_propagate

    Disable automatically propagating the mission. Use with caution. Aviator will not automatically propagate before adding new procedures.

    :Returns:

        :obj:`~None`

