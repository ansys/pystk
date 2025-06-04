CoverageEllipseCollection
=========================

.. py:class:: ansys.stk.core.stkobjects.CoverageEllipseCollection

   Collection of elliptical areas of interest.

.. py:currentmodule:: CoverageEllipseCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageEllipseCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageEllipseCollection.add`
              - Add a new ellipse centered on a Place, Facility, or Target object.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageEllipseCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageEllipseCollection.remove_all`
              - Remove all elements from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageEllipseCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageEllipseCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageEllipseCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CoverageEllipseCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.CoverageEllipseCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> CoverageEllipse
    :canonical: ansys.stk.core.stkobjects.CoverageEllipseCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~CoverageEllipse`


.. py:method:: add(self, center_object_name: str) -> CoverageEllipse
    :canonical: ansys.stk.core.stkobjects.CoverageEllipseCollection.add

    Add a new ellipse centered on a Place, Facility, or Target object.

    :Parameters:

        **center_object_name** : :obj:`~str`


    :Returns:

        :obj:`~CoverageEllipse`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageEllipseCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageEllipseCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

