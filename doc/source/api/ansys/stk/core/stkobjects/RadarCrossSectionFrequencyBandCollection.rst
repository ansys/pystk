RadarCrossSectionFrequencyBandCollection
========================================

.. py:class:: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection

   Class defining a inheritable radar cross section frequency band collection.

.. py:currentmodule:: RadarCrossSectionFrequencyBandCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection.remove_at`
              - Remove the band with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection.add`
              - Add a band with supplied minimum and maximum frequencies.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarCrossSectionFrequencyBandCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> RadarCrossSectionFrequencyBand
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~RadarCrossSectionFrequencyBand`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection.remove_at

    Remove the band with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, min_frequency: float, max_frequency: float) -> RadarCrossSectionFrequencyBand
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection.add

    Add a band with supplied minimum and maximum frequencies.

    :Parameters:

    **min_frequency** : :obj:`~float`
    **max_frequency** : :obj:`~float`

    :Returns:

        :obj:`~RadarCrossSectionFrequencyBand`

