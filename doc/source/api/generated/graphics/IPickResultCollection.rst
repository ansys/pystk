IPickResultCollection
=====================

.. py:class:: IPickResultCollection

   object
   
   A collection of picked objects.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return a picked object at the specified position in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPickResultCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IPickResultCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IPickResultCollection._NewEnum
    :type: EnumeratorProxy




Method detail
-------------


.. py:method:: item(self, index:int) -> "IPickResult"

    Return a picked object at the specified position in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IPickResult"`


