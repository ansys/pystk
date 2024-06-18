IRadarCrossSectionFrequencyBandCollection
=========================================

.. py:class:: IRadarCrossSectionFrequencyBandCollection

   object
   
   Represents a collection of radar cross section frequency bands.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns the element in the collection.
            * - :py:meth:`~remove_at`
              - Remove the band with the supplied index.
            * - :py:meth:`~add`
              - Add a band with supplied minimum and maximum frequencies.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionFrequencyBandCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionFrequencyBandCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionFrequencyBandCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IRadarCrossSectionFrequencyBand"

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IRadarCrossSectionFrequencyBand"`


.. py:method:: remove_at(self, index:int) -> None

    Remove the band with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, minFrequency:float, maxFrequency:float) -> "IRadarCrossSectionFrequencyBand"

    Add a band with supplied minimum and maximum frequencies.

    :Parameters:

    **minFrequency** : :obj:`~float`
    **maxFrequency** : :obj:`~float`

    :Returns:

        :obj:`~"IRadarCrossSectionFrequencyBand"`

