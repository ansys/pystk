IPhaseCollection
================

.. py:class:: IPhaseCollection

   object
   
   Interface used to access the collection of phases for a mission.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~add`
              - Add a phase at the end of the mission.
            * - :py:meth:`~add_at_index`
              - Add a phase at the given index.
            * - :py:meth:`~remove`
              - Remove given phase.
            * - :py:meth:`~remove_at_index`
              - Remove phase at the given index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IPhaseCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.aviator.IPhaseCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.aviator.IPhaseCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IPhase"

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IPhase"`


.. py:method:: add(self) -> "IPhase"

    Add a phase at the end of the mission.

    :Returns:

        :obj:`~"IPhase"`

.. py:method:: add_at_index(self, index:int) -> "IPhase"

    Add a phase at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IPhase"`

.. py:method:: remove(self, phase:"IPhase") -> None

    Remove given phase.

    :Parameters:

    **phase** : :obj:`~"IPhase"`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at_index(self, index:int) -> None

    Remove phase at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

