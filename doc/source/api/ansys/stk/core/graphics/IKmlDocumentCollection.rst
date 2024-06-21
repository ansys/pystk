IKmlDocumentCollection
======================

.. py:class:: ansys.stk.core.graphics.IKmlDocumentCollection

   object
   
   A collection of KML documents.

.. py:currentmodule:: IKmlDocumentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IKmlDocumentCollection.item`
              - Get an element at the specified position in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IKmlDocumentCollection.count`
            * - :py:attr:`~ansys.stk.core.graphics.IKmlDocumentCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IKmlDocumentCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IKmlDocumentCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IKmlDocumentCollection._NewEnum
    :type: EnumeratorProxy




Method detail
-------------


.. py:method:: item(self, index: int) -> IKmlDocument
    :canonical: ansys.stk.core.graphics.IKmlDocumentCollection.item

    Get an element at the specified position in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IKmlDocument`


