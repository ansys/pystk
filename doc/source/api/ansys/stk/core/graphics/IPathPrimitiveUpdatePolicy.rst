IPathPrimitiveUpdatePolicy
==========================

.. py:class:: ansys.stk.core.graphics.IPathPrimitiveUpdatePolicy

   A class that encapsulates the update logic for a path primitive. Derived classes must implement the Update method.

.. py:currentmodule:: IPathPrimitiveUpdatePolicy

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPathPrimitiveUpdatePolicy.update`
              - Update the pathPrimitive at the specified date.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPathPrimitiveUpdatePolicy



Method detail
-------------

.. py:method:: update(self, pathPrimitive: PathPrimitive, date: IDate) -> None
    :canonical: ansys.stk.core.graphics.IPathPrimitiveUpdatePolicy.update

    Update the pathPrimitive at the specified date.

    :Parameters:

    **pathPrimitive** : :obj:`~PathPrimitive`
    **date** : :obj:`~IDate`

    :Returns:

        :obj:`~None`

