GridSearchControlCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection

   Properties for the list of Grid Search control parameters.

.. py:currentmodule:: GridSearchControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GridSearchControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> GridSearchControl
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~GridSearchControl`



.. py:method:: get_control_by_paths(self, object_path: str, control_path: str) -> GridSearchControl
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

        **object_path** : :obj:`~str`

        **control_path** : :obj:`~str`


    :Returns:

        :obj:`~GridSearchControl`

