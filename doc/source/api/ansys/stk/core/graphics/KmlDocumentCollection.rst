KmlDocumentCollection
=====================

.. py:class:: ansys.stk.core.graphics.KmlDocumentCollection

   Bases: 

   A collection of KML documents.

.. py:currentmodule:: KmlDocumentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlDocumentCollection.item`
              - Get an element at the specified position in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlDocumentCollection.count`
              - A total number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.KmlDocumentCollection._NewEnum`
              - Return an enumerator that iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import KmlDocumentCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.KmlDocumentCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.KmlDocumentCollection._NewEnum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> KmlDocument
    :canonical: ansys.stk.core.graphics.KmlDocumentCollection.item

    Get an element at the specified position in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~KmlDocument`


