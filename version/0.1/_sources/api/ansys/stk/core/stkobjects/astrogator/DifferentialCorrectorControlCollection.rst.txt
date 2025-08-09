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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.count`
              - Return the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.provide_runtime_type_info`
              - Return the RuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DifferentialCorrectorControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.count
    :type: int

    Return the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.provide_runtime_type_info
    :type: RuntimeTypeInfo

    Return the RuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, index: int) -> DifferentialCorrectorControl
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~DifferentialCorrectorControl`



.. py:method:: get_control_by_paths(self, object_path: str, control_path: str) -> DifferentialCorrectorControl
    :canonical: ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

        **object_path** : :obj:`~str`

        **control_path** : :obj:`~str`


    :Returns:

        :obj:`~DifferentialCorrectorControl`


