ISensorEOIRSaturationCollection
===============================

.. py:class:: ISensorEOIRSaturationCollection

   object
   
   IAgSnEOIRSaturationCollection Interface. A collection of Radiometric pairs defining the saturations.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an IAgSnEOIRRadiometricPair interface.
            * - :py:meth:`~add`
              - Add a radiometric pair.
            * - :py:meth:`~remove_at`
              - Remove a radiometric pair given an index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorEOIRSaturationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSaturationCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSaturationCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> ISensorEOIRRadiometricPair
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSaturationCollection.item

    Given an index, returns an IAgSnEOIRRadiometricPair interface.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ISensorEOIRRadiometricPair`

.. py:method:: add(self) -> ISensorEOIRRadiometricPair
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSaturationCollection.add

    Add a radiometric pair.

    :Returns:

        :obj:`~ISensorEOIRRadiometricPair`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRSaturationCollection.remove_at

    Remove a radiometric pair given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

