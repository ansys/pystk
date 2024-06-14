IBPlaneCollection
=================

.. py:class:: IBPlaneCollection

   object
   
   Properties for the collection of B-Planes.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add a BPlane.
            * - :py:meth:`~remove`
              - Remove a BPlane.
            * - :py:meth:`~remove_all`
              - Remove all BPlanes.
            * - :py:meth:`~item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


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

.. py:method:: add(self, bPlaneName:str) -> None

    Add a BPlane.

    :Parameters:

    **bPlaneName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, bPlaneName:str) -> None

    Remove a BPlane.

    :Parameters:

    **bPlaneName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all BPlanes.

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index:int) -> str

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`



