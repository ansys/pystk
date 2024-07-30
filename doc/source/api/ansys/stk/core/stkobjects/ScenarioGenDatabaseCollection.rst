ScenarioGenDatabaseCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.ScenarioGenDatabaseCollection

   Bases: 

   Collection of Scenario database settings.

.. py:currentmodule:: ScenarioGenDatabaseCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGenDatabaseCollection.item`
              - Return scenario database settings at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGenDatabaseCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioGenDatabaseCollection._NewEnum`
              - Enumerates the elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioGenDatabaseCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ScenarioGenDatabaseCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ScenarioGenDatabaseCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> ScenarioGenDatabase
    :canonical: ansys.stk.core.stkobjects.ScenarioGenDatabaseCollection.item

    Return scenario database settings at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScenarioGenDatabase`

