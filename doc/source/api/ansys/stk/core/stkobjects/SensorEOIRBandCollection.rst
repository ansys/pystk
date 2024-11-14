SensorEOIRBandCollection
========================

.. py:class:: ansys.stk.core.stkobjects.SensorEOIRBandCollection

   Class defining the band collection for an EOIR Sensor.

.. py:currentmodule:: SensorEOIRBandCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBandCollection.item`
              - Given an index, returns an IAgSnEOIRBand interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBandCollection.add`
              - Add a target.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBandCollection.remove_at`
              - Remove a target given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBandCollection.get_item_by_name`
              - Retrieve an item from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBandCollection.count`
              - The number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorEOIRBandCollection._new_enum`
              - Enumerates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorEOIRBandCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBandCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBandCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> SensorEOIRBand
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBandCollection.item

    Given an index, returns an IAgSnEOIRBand interface.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~SensorEOIRBand`


.. py:method:: add(self) -> SensorEOIRBand
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBandCollection.add

    Add a target.

    :Returns:

        :obj:`~SensorEOIRBand`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBandCollection.remove_at

    Remove a target given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: get_item_by_name(self, name: str) -> SensorEOIRBand
    :canonical: ansys.stk.core.stkobjects.SensorEOIRBandCollection.get_item_by_name

    Retrieve an item from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~SensorEOIRBand`

