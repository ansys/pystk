StkRfcmRadarSarImageLocationCollection
======================================

.. py:class:: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection

   A collection of image location information.

.. py:currentmodule:: StkRfcmRadarSarImageLocationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.remove_at`
              - Remove the SAR image location with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.remove`
              - Remove the supplied SAR image location from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.add_new`
              - Add and returns a new SAR image location.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.remove_all`
              - Clear all SAR image locations from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.contains`
              - Check to see if a given SAR image location exists in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.find`
              - Find a SAR image location by name. Returns Null if the image location name does not exist in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfcm import StkRfcmRadarSarImageLocationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmRadarSarImageLocation
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmRadarSarImageLocation`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.remove_at

    Remove the SAR image location with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, image_location_name: str) -> None
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.remove

    Remove the supplied SAR image location from the collection.

    :Parameters:

    **image_location_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_new(self) -> StkRfcmRadarSarImageLocation
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.add_new

    Add and returns a new SAR image location.

    :Returns:

        :obj:`~StkRfcmRadarSarImageLocation`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.remove_all

    Clear all SAR image locations from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, image_location_name: str) -> bool
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.contains

    Check to see if a given SAR image location exists in the collection.

    :Parameters:

    **image_location_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: find(self, image_location_name: str) -> StkRfcmRadarSarImageLocation
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection.find

    Find a SAR image location by name. Returns Null if the image location name does not exist in the collection.

    :Parameters:

    **image_location_name** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmRadarSarImageLocation`

