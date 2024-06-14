IPathPrimitiveUpdatePolicy
==========================

.. py:class:: IPathPrimitiveUpdatePolicy

   object
   
   A class that encapsulates the update logic for a path primitive. Derived classes must implement the Update method.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~update`
              - Update the pathPrimitive at the specified date.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPathPrimitiveUpdatePolicy



Method detail
-------------

.. py:method:: update(self, pathPrimitive:"IPathPrimitive", date:"IDate") -> None

    Update the pathPrimitive at the specified date.

    :Parameters:

    **pathPrimitive** : :obj:`~"IPathPrimitive"`
    **date** : :obj:`~"IDate"`

    :Returns:

        :obj:`~None`

