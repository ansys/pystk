IScenarioGenDatabaseCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.IScenarioGenDatabaseCollection

   object
   
   Represents a collection of the scenario's databases.

.. py:currentmodule:: IScenarioGenDatabaseCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioGenDatabaseCollection.item`
              - Return scenario database settings at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioGenDatabaseCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenarioGenDatabaseCollection._NewEnum`
              - Enumerates the elements in the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenarioGenDatabaseCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IScenarioGenDatabaseCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IScenarioGenDatabaseCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> IScenarioGenDatabase
    :canonical: ansys.stk.core.stkobjects.IScenarioGenDatabaseCollection.item

    Return scenario database settings at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScenarioGenDatabase`

