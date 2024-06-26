IBPlaneCollection
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IBPlaneCollection

   object
   
   Properties for the collection of B-Planes.

.. py:currentmodule:: IBPlaneCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.add`
              - Add a BPlane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.remove`
              - Remove a BPlane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.remove_all`
              - Remove all BPlanes.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBPlaneCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.count`
              - Get the number of active BPlanes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBPlaneCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IBPlaneCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.count
    :type: int

    Get the number of active BPlanes.


Method detail
-------------

.. py:method:: add(self, bPlaneName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.add

    Add a BPlane.

    :Parameters:

    **bPlaneName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, bPlaneName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.remove

    Remove a BPlane.

    :Parameters:

    **bPlaneName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.remove_all

    Remove all BPlanes.

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkobjects.astrogator.IBPlaneCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`



