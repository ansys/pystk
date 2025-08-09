TargeterGraphActiveControlCollection
====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Targeter Graph Active Control Collection.

.. py:currentmodule:: TargeterGraphActiveControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection.count`
              - Return the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection.provide_runtime_type_info`
              - Return the RuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import TargeterGraphActiveControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection.count
    :type: int

    Return the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection.provide_runtime_type_info
    :type: RuntimeTypeInfo

    Return the RuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, index: int) -> TargeterGraphActiveControl
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~TargeterGraphActiveControl`




