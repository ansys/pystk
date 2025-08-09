CompositePrimitiveFactory
=========================

.. py:class:: ansys.stk.core.graphics.CompositePrimitiveFactory

   A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

.. py:currentmodule:: CompositePrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CompositePrimitiveFactory.initialize`
              - Initialize a default composite primitive.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CompositePrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> CompositePrimitive
    :canonical: ansys.stk.core.graphics.CompositePrimitiveFactory.initialize

    Initialize a default composite primitive.

    :Returns:

        :obj:`~CompositePrimitive`

