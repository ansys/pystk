ISensorEOIRBandCollection
=========================

.. py:class:: ISensorEOIRBandCollection

   object
   
   IAgSnEOIRBandCollection Interface. A collection of EOIR bands.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an IAgSnEOIRBand interface.
            * - :py:meth:`~add`
              - Add a target.
            * - :py:meth:`~remove_at`
              - Remove a target given an index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve an item from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorEOIRBandCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRBandCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRBandCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ISensorEOIRBand
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRBandCollection.item

    Given an index, returns an IAgSnEOIRBand interface.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ISensorEOIRBand`


.. py:method:: add(self) -> ISensorEOIRBand
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRBandCollection.add

    Add a target.

    :Returns:

        :obj:`~ISensorEOIRBand`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRBandCollection.remove_at

    Remove a target given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: get_item_by_name(self, name: str) -> ISensorEOIRBand
    :canonical: ansys.stk.core.stkobjects.ISensorEOIRBandCollection.get_item_by_name

    Retrieve an item from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ISensorEOIRBand`

