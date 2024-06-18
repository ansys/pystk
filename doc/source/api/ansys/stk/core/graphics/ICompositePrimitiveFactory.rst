ICompositePrimitiveFactory
==========================

.. py:class:: ICompositePrimitiveFactory

   object
   
   A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default composite primitive.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICompositePrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> "ICompositePrimitive"

    Initialize a default composite primitive.

    :Returns:

        :obj:`~"ICompositePrimitive"`

