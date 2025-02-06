IStkRfcmSceneContributorCollection
==================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection

   Represents a collection of scene contributors.

.. py:currentmodule:: IStkRfcmSceneContributorCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.remove_at`
              - Remove the scene contributor with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.remove`
              - Remove the supplied scene contributor from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.add_new`
              - Add and returns a new scene contributor.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.remove_all`
              - Clear all scene contributors from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.contains`
              - Check to see if a given scene contributor exists in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection._new_enum`
              - Returns an enumerator for the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import IStkRfcmSceneContributorCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmSceneContributor
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmSceneContributor`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.remove_at

    Remove the scene contributor with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, stk_object_path: str) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.remove

    Remove the supplied scene contributor from the collection.

    :Parameters:

    **stk_object_path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_new(self, stk_object_path: str) -> StkRfcmSceneContributor
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.add_new

    Add and returns a new scene contributor.

    :Parameters:

    **stk_object_path** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmSceneContributor`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.remove_all

    Clear all scene contributors from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, stk_object_path: str) -> bool
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection.contains

    Check to see if a given scene contributor exists in the collection.

    :Parameters:

    **stk_object_path** : :obj:`~str`

    :Returns:

        :obj:`~bool`

