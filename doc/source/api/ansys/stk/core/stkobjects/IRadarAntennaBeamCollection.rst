IRadarAntennaBeamCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.IRadarAntennaBeamCollection

   object
   
   Represents a collection of antenna beams.

.. py:currentmodule:: IRadarAntennaBeamCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.remove_at`
              - Remove the layer with the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.insert_at`
              - Insert a new beam at the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.add`
              - Add a new beam to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.duplicate_beam`
              - Duplicates the beam at the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarAntennaBeamCollection._NewEnum`
              - Returns an enumerator for the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarAntennaBeamCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeamCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IRadarAntennaBeam
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IRadarAntennaBeam`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.remove_at

    Remove the layer with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: insert_at(self, index: int) -> IRadarAntennaBeam
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.insert_at

    Insert a new beam at the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IRadarAntennaBeam`

.. py:method:: add(self) -> IRadarAntennaBeam
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.add

    Add a new beam to the collection.

    :Returns:

        :obj:`~IRadarAntennaBeam`

.. py:method:: duplicate_beam(self, index: int) -> IRadarAntennaBeam
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeamCollection.duplicate_beam

    Duplicates the beam at the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IRadarAntennaBeam`

