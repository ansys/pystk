IKmlFeatureCollection
=====================

.. py:class:: ansys.stk.core.graphics.IKmlFeatureCollection

   object
   
   A collection of KML features.

.. py:currentmodule:: IKmlFeatureCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeatureCollection.item`
              - Get an element at the specified position in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeatureCollection.count`
            * - :py:attr:`~ansys.stk.core.graphics.IKmlFeatureCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IKmlFeatureCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IKmlFeatureCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IKmlFeatureCollection._NewEnum
    :type: EnumeratorProxy




Method detail
-------------


.. py:method:: item(self, index: int) -> IKmlFeature
    :canonical: ansys.stk.core.graphics.IKmlFeatureCollection.item

    Get an element at the specified position in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IKmlFeature`


