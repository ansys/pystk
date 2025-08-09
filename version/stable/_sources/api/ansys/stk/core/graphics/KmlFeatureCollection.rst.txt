KmlFeatureCollection
====================

.. py:class:: ansys.stk.core.graphics.KmlFeatureCollection

   A collection of KML features.

.. py:currentmodule:: KmlFeatureCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlFeatureCollection.item`
              - Get an element at the specified position in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlFeatureCollection.count`
              - A total number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.KmlFeatureCollection._new_enum`
              - Return an enumerator that iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import KmlFeatureCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.KmlFeatureCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.KmlFeatureCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IKmlFeature
    :canonical: ansys.stk.core.graphics.KmlFeatureCollection.item

    Get an element at the specified position in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IKmlFeature`


