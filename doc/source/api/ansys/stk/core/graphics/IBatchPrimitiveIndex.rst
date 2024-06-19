IBatchPrimitiveIndex
====================

.. py:class:: IBatchPrimitiveIndex

   object
   
   Represents an individual item index that is associated with a batch primitive. Provides the Index of the individual item and the Primitive that contains that index...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~index`
            * - :py:meth:`~primitive`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBatchPrimitiveIndex


Property detail
---------------

.. py:property:: index
    :canonical: ansys.stk.core.graphics.IBatchPrimitiveIndex.index
    :type: int

    The index of the item contained by the Primitive.

.. py:property:: primitive
    :canonical: ansys.stk.core.graphics.IBatchPrimitiveIndex.primitive
    :type: IAgStkGraphicsPrimitive

    The Primitive that contains the item at the Index specified.


