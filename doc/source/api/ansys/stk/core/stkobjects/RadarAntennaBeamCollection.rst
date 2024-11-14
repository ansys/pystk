RadarAntennaBeamCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.RadarAntennaBeamCollection

   Class defining an radar antenna beam collection.

.. py:currentmodule:: RadarAntennaBeamCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection.remove_at`
              - Remove the layer with the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection.insert_at`
              - Insert a new beam at the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection.add`
              - Add a new beam to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection.duplicate_beam`
              - Duplicates the beam at the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarAntennaBeamCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeamCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeamCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> RadarAntennaBeam
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeamCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~RadarAntennaBeam`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeamCollection.remove_at

    Remove the layer with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: insert_at(self, index: int) -> RadarAntennaBeam
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeamCollection.insert_at

    Insert a new beam at the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~RadarAntennaBeam`

.. py:method:: add(self) -> RadarAntennaBeam
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeamCollection.add

    Add a new beam to the collection.

    :Returns:

        :obj:`~RadarAntennaBeam`

.. py:method:: duplicate_beam(self, index: int) -> RadarAntennaBeam
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeamCollection.duplicate_beam

    Duplicates the beam at the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~RadarAntennaBeam`

