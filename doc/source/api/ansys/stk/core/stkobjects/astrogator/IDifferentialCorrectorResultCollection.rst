IDifferentialCorrectorResultCollection
======================================

.. py:class:: IDifferentialCorrectorResultCollection

   object
   
   Differential Corrector result collection.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Allow you to iterate through the collection.
            * - :py:meth:`~get_result_by_paths`
              - Return the result specified by the object/result path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`
            * - :py:meth:`~provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IDifferentialCorrectorResultCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResultCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResultCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResultCollection.provide_runtime_type_info
    :type: IAgRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, index: int) -> IDifferentialCorrectorResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDifferentialCorrectorResult`



.. py:method:: get_result_by_paths(self, objectPath: str, resultPath: str) -> IDifferentialCorrectorResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **resultPath** : :obj:`~str`

    :Returns:

        :obj:`~IDifferentialCorrectorResult`


