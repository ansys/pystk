VehicleConsiderAnalysisCollection
=================================

.. py:class:: ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection

   The Consider Analysis list for HPOP covariance.

.. py:currentmodule:: VehicleConsiderAnalysisCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.remove_by_type`
              - Remove an element from the collection using the VehicleConsiderAnalysisType type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleConsiderAnalysisCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleConsiderAnalysisCollectionElement
    :canonical: ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VehicleConsiderAnalysisCollectionElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, param_type: VehicleConsiderAnalysisType) -> VehicleConsiderAnalysisCollectionElement
    :canonical: ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.add

    Add a new element to the collection.

    :Parameters:

        **param_type** : :obj:`~VehicleConsiderAnalysisType`


    :Returns:

        :obj:`~VehicleConsiderAnalysisCollectionElement`

.. py:method:: remove_by_type(self, param_type: VehicleConsiderAnalysisType) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection.remove_by_type

    Remove an element from the collection using the VehicleConsiderAnalysisType type.

    :Parameters:

        **param_type** : :obj:`~VehicleConsiderAnalysisType`


    :Returns:

        :obj:`~None`

