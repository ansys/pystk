GoldenSectionControlCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection

   Properties for the list of Golden Section control parameters.

.. py:currentmodule:: GoldenSectionControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GoldenSectionControlCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------


.. py:method:: get_control_by_paths(self, object_path: str, control_path: str) -> GoldenSectionControl
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

        **object_path** : :obj:`~str`

        **control_path** : :obj:`~str`


    :Returns:

        :obj:`~GoldenSectionControl`

.. py:method:: item(self, index: int) -> GoldenSectionControl
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~GoldenSectionControl`


