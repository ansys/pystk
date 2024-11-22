StkRfcmRadarTargetCollection
============================

.. py:class:: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection

   A collection of radar target objects.

.. py:currentmodule:: StkRfcmRadarTargetCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.remove_at`
              - Remove the radar target with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.remove`
              - Remove the supplied radar target from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.add_new`
              - Add and returns a new radar target.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.remove_all`
              - Clear all radar targets from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.contains`
              - Check to see if a given radar target exists in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfcm import StkRfcmRadarTargetCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmRadarTarget
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmRadarTarget`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.remove_at

    Remove the radar target with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, stk_object_path: str) -> None
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.remove

    Remove the supplied radar target from the collection.

    :Parameters:

    **stk_object_path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_new(self, stk_object_path: str) -> StkRfcmRadarTarget
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.add_new

    Add and returns a new radar target.

    :Parameters:

    **stk_object_path** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmRadarTarget`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.remove_all

    Clear all radar targets from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, stk_object_path: str) -> bool
    :canonical: ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection.contains

    Check to see if a given radar target exists in the collection.

    :Parameters:

    **stk_object_path** : :obj:`~str`

    :Returns:

        :obj:`~bool`

