ScenarioDatabaseCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.ScenarioDatabaseCollection

   Collection of Scenario database settings.

.. py:currentmodule:: ScenarioDatabaseCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioDatabaseCollection.item`
              - Return scenario database settings at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioDatabaseCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioDatabaseCollection._NewEnum`
              - Enumerates the elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioDatabaseCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ScenarioDatabaseCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ScenarioDatabaseCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> ScenarioDatabase
    :canonical: ansys.stk.core.stkobjects.ScenarioDatabaseCollection.item

    Return scenario database settings at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScenarioDatabase`

