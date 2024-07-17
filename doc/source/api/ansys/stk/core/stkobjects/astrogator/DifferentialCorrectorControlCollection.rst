DifferentialCorrectorControlCollection
======================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The collection of Control Parameters for a differential corrector profile.

.. py:currentmodule:: DifferentialCorrectorControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.provide_runtime_type_info`
              - Returns the IAgRuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DifferentialCorrectorControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, index: int) -> DifferentialCorrectorControl
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~DifferentialCorrectorControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> DifferentialCorrectorControl
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~DifferentialCorrectorControl`


