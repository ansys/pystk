CoverageLatLonBoxCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.CoverageLatLonBoxCollection

   Collection of latitude/longitude boxes of interest.

.. py:currentmodule:: CoverageLatLonBoxCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.add`
              - Add a new box centered on a Place, Facility, or Target object, defined by latitude and longitude spans.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.remove_all`
              - Remove all elements from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageLatLonBoxCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageLatLonBoxCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.CoverageLatLonBoxCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> CoverageLatLonBox
    :canonical: ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~CoverageLatLonBox`


.. py:method:: add(self, center_object_name: str) -> CoverageLatLonBox
    :canonical: ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.add

    Add a new box centered on a Place, Facility, or Target object, defined by latitude and longitude spans.

    :Parameters:

    **center_object_name** : :obj:`~str`

    :Returns:

        :obj:`~CoverageLatLonBox`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageLatLonBoxCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

