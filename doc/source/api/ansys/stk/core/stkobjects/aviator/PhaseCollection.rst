PhaseCollection
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.PhaseCollection

   Bases: 

   Class defining the collection of phases.

.. py:currentmodule:: PhaseCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PhaseCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PhaseCollection.add`
              - Add a phase at the end of the mission.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PhaseCollection.add_at_index`
              - Add a phase at the given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PhaseCollection.remove`
              - Remove given phase.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PhaseCollection.remove_at_index`
              - Remove phase at the given index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PhaseCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PhaseCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import PhaseCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.aviator.PhaseCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.aviator.PhaseCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> Phase
    :canonical: ansys.stk.core.stkobjects.aviator.PhaseCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~Phase`


.. py:method:: add(self) -> Phase
    :canonical: ansys.stk.core.stkobjects.aviator.PhaseCollection.add

    Add a phase at the end of the mission.

    :Returns:

        :obj:`~Phase`

.. py:method:: add_at_index(self, index: int) -> Phase
    :canonical: ansys.stk.core.stkobjects.aviator.PhaseCollection.add_at_index

    Add a phase at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~Phase`

.. py:method:: remove(self, phase: Phase) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PhaseCollection.remove

    Remove given phase.

    :Parameters:

    **phase** : :obj:`~Phase`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PhaseCollection.remove_at_index

    Remove phase at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

