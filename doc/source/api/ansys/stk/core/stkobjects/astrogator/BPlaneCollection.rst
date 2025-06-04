BPlaneCollection
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.BPlaneCollection

   The collection of B-Planes.

.. py:currentmodule:: BPlaneCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BPlaneCollection.add`
              - Add a BPlane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BPlaneCollection.remove`
              - Remove a BPlane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BPlaneCollection.remove_all`
              - Remove all BPlanes.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BPlaneCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BPlaneCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BPlaneCollection.count`
              - Get the number of active BPlanes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BPlaneCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.BPlaneCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.BPlaneCollection.count
    :type: int

    Get the number of active BPlanes.


Method detail
-------------

.. py:method:: add(self, plane_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.BPlaneCollection.add

    Add a BPlane.

    :Parameters:

        **plane_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove(self, plane_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.BPlaneCollection.remove

    Remove a BPlane.

    :Parameters:

        **plane_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.BPlaneCollection.remove_all

    Remove all BPlanes.

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkobjects.astrogator.BPlaneCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~str`



