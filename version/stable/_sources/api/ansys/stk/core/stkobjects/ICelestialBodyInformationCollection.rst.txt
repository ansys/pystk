ICelestialBodyInformationCollection
===================================

.. py:class:: ansys.stk.core.stkobjects.ICelestialBodyInformationCollection

   Represents a collection of celestial bodies.

.. py:currentmodule:: ICelestialBodyInformationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformationCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformationCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformationCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformationCollection.recycle`
              - Control whether to reuse the same celestial info object when accessing the elements of the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICelestialBodyInformationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformationCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformationCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: recycle
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformationCollection.recycle
    :type: bool

    Control whether to reuse the same celestial info object when accessing the elements of the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ICelestialBodyInformation
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformationCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ICelestialBodyInformation`




