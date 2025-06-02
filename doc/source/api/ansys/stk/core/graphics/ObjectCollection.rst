ObjectCollection
================

.. py:class:: ansys.stk.core.graphics.ObjectCollection

   A collection of objects.

.. py:currentmodule:: ObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ObjectCollection.item`
              - Return an item in the collection at the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ObjectCollection.count`
              - A total number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ObjectCollection._new_enum`
              - Return an enumerator that iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ObjectCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ObjectCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.ObjectCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> typing.Any
    :canonical: ansys.stk.core.graphics.ObjectCollection.item

    Return an item in the collection at the specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~typing.Any`


