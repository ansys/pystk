ISensorEOIRSensitivityCollection
================================

.. py:class:: ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection

   object
   
   IAgSnEOIRFCollection Interface. A collection of Radiometric pairs defining the Sensitivities.

.. py:currentmodule:: ISensorEOIRSensitivityCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection.item`
              - Given an index, returns an IAgSnEOIRRadiometricPair interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection.add`
              - Add a radiometric pair.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection.remove_at`
              - Remove a radiometric pair given an index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorEOIRSensitivityCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> ISensorEOIRRadiometricPair
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection.item

    Given an index, returns an IAgSnEOIRRadiometricPair interface.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ISensorEOIRRadiometricPair`

.. py:method:: add(self) -> ISensorEOIRRadiometricPair
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection.add

    Add a radiometric pair.

    :Returns:

        :obj:`~ISensorEOIRRadiometricPair`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSensitivityCollection.remove_at

    Remove a radiometric pair given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

