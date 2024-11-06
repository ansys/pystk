DifferentialCorrectorResultCollection
=====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The collection of results for a differential corrector.

.. py:currentmodule:: DifferentialCorrectorResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.get_result_by_paths`
              - Return the result specified by the object/result path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.provide_runtime_type_info`
              - Returns the IAgRuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DifferentialCorrectorResultCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, index: int) -> DifferentialCorrectorResult
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~DifferentialCorrectorResult`



.. py:method:: get_result_by_paths(self, object_path: str, result_path: str) -> DifferentialCorrectorResult
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

    **object_path** : :obj:`~str`
    **result_path** : :obj:`~str`

    :Returns:

        :obj:`~DifferentialCorrectorResult`


