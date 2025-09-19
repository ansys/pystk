SensorEOIRSensitivityCollection
===============================

.. py:class:: ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection

   Class defining the Sensitivities collection for an EOIR Sensor.

.. py:currentmodule:: SensorEOIRSensitivityCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection.add`
              - Add a radiometric pair.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection.item`
              - Given an index, returns an SensorEOIRRadiometricPair interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection.remove_at`
              - Remove a radiometric pair given an index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection._new_enum`
              - Enumerates through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection.count`
              - The number of items in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorEOIRSensitivityCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection.count
    :type: int

    The number of items in the collection.


Method detail
-------------

.. py:method:: add(self) -> SensorEOIRRadiometricPair
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection.add

    Add a radiometric pair.

    :Returns:

        :obj:`~SensorEOIRRadiometricPair`


.. py:method:: item(self, index: int) -> SensorEOIRRadiometricPair
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection.item

    Given an index, returns an SensorEOIRRadiometricPair interface.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SensorEOIRRadiometricPair`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection.remove_at

    Remove a radiometric pair given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


