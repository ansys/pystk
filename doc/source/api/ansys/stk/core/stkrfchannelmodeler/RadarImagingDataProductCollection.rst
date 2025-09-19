RadarImagingDataProductCollection
=================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection

   A collection of radar transceivers.

.. py:currentmodule:: RadarImagingDataProductCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection.contains`
              - Check to see if a imaging data product with given identifier exists in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection.find_by_identifier`
              - Return the imaging data product in the collection with the supplied identifier or Null if not found or invalid.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection.item`
              - Given an index, returns the element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import RadarImagingDataProductCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: contains(self, identifier: str) -> bool
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection.contains

    Check to see if a imaging data product with given identifier exists in the collection.

    :Parameters:

        **identifier** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: find_by_identifier(self, identifier: str) -> RadarImagingDataProduct
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection.find_by_identifier

    Return the imaging data product in the collection with the supplied identifier or Null if not found or invalid.

    :Parameters:

        **identifier** : :obj:`~str`


    :Returns:

        :obj:`~RadarImagingDataProduct`

.. py:method:: item(self, index: int) -> RadarImagingDataProduct
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~RadarImagingDataProduct`


