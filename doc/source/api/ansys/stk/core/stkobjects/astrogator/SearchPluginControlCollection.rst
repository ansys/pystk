SearchPluginControlCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection

   The list of search plugin control parameters.

.. py:currentmodule:: SearchPluginControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection._new_enum`
              - Property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SearchPluginControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection._new_enum
    :type: EnumeratorProxy

    Property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> SearchPluginControl
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SearchPluginControl`



.. py:method:: get_control_by_paths(self, object_path: str, control_path: str) -> SearchPluginControl
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

        **object_path** : :obj:`~str`

        **control_path** : :obj:`~str`


    :Returns:

        :obj:`~SearchPluginControl`

