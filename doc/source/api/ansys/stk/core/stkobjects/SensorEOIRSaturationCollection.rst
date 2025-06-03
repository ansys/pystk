SensorEOIRSaturationCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.SensorEOIRSaturationCollection

   Class defining the Saturations collection for an EOIR Sensor.

.. py:currentmodule:: SensorEOIRSaturationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSaturationCollection.item`
              - Given an index, returns an SensorEOIRRadiometricPair interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSaturationCollection.add`
              - Add a radiometric pair.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSaturationCollection.remove_at`
              - Remove a radiometric pair given an index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSaturationCollection.count`
              - The number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSaturationCollection._new_enum`
              - Enumerates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorEOIRSaturationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSaturationCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSaturationCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> SensorEOIRRadiometricPair
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSaturationCollection.item

    Given an index, returns an SensorEOIRRadiometricPair interface.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SensorEOIRRadiometricPair`

.. py:method:: add(self) -> SensorEOIRRadiometricPair
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSaturationCollection.add

    Add a radiometric pair.

    :Returns:

        :obj:`~SensorEOIRRadiometricPair`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSaturationCollection.remove_at

    Remove a radiometric pair given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

