PickResultCollection
====================

.. py:class:: ansys.stk.core.graphics.PickResultCollection

   A collection of picked objects.

.. py:currentmodule:: PickResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PickResultCollection.item`
              - Return a picked object at the specified position in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PickResultCollection._new_enum`
              - Return an enumerator that iterates through the collection.
            * - :py:attr:`~ansys.stk.core.graphics.PickResultCollection.count`
              - A total number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PickResultCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.PickResultCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.graphics.PickResultCollection.count
    :type: int

    A total number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> PickResult
    :canonical: ansys.stk.core.graphics.PickResultCollection.item

    Return a picked object at the specified position in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~PickResult`


