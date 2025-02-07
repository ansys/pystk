StkRfcmRadarImagingDataProductCollection
========================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection

   A collection of radar transceivers.

.. py:currentmodule:: StkRfcmRadarImagingDataProductCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection.contains`
              - Check to see if a imaging data product with given identifier exists in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection.find_by_identifier`
              - Return the imaging data product in the collection with the supplied identifier or Null if not found or invalid.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import StkRfcmRadarImagingDataProductCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmRadarImagingDataProduct
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmRadarImagingDataProduct`


.. py:method:: contains(self, identifier: str) -> bool
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection.contains

    Check to see if a imaging data product with given identifier exists in the collection.

    :Parameters:

    **identifier** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: find_by_identifier(self, identifier: str) -> StkRfcmRadarImagingDataProduct
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection.find_by_identifier

    Return the imaging data product in the collection with the supplied identifier or Null if not found or invalid.

    :Parameters:

    **identifier** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmRadarImagingDataProduct`

