IVehicleConsiderAnalysisCollection
==================================

.. py:class:: IVehicleConsiderAnalysisCollection

   object
   
   AgVeConsiderAnalysisCollection.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new element to the collection.
            * - :py:meth:`~remove_by_type`
              - Remove an element from the collection using the AgEVeConsiderAnalysisType type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleConsiderAnalysisCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleConsiderAnalysisCollectionElement
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleConsiderAnalysisCollectionElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, paramType: VEHICLE_CONSIDER_ANALYSIS_TYPE) -> IVehicleConsiderAnalysisCollectionElement
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollection.add

    Add a new element to the collection.

    :Parameters:

    **paramType** : :obj:`~VEHICLE_CONSIDER_ANALYSIS_TYPE`

    :Returns:

        :obj:`~IVehicleConsiderAnalysisCollectionElement`

.. py:method:: remove_by_type(self, eParamType: VEHICLE_CONSIDER_ANALYSIS_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollection.remove_by_type

    Remove an element from the collection using the AgEVeConsiderAnalysisType type.

    :Parameters:

    **eParamType** : :obj:`~VEHICLE_CONSIDER_ANALYSIS_TYPE`

    :Returns:

        :obj:`~None`

