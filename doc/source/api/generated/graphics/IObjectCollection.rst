IObjectCollection
=================

.. py:class:: IObjectCollection

   object
   
   A collection of objects.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return an item in the collection at the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IObjectCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IObjectCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IObjectCollection._NewEnum
    :type: EnumeratorProxy




Method detail
-------------


.. py:method:: item(self, index:int) -> typing.Any

    Return an item in the collection at the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~typing.Any`


