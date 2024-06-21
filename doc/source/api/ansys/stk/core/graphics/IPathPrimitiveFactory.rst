IPathPrimitiveFactory
=====================

.. py:class:: ansys.stk.core.graphics.IPathPrimitiveFactory

   object
   
   Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

.. py:currentmodule:: IPathPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPathPrimitiveFactory.initialize`
              - Initialize a default path primitive. This is equivalent to constructing a path primitive with an initial capacity of 16.
            * - :py:attr:`~ansys.stk.core.graphics.IPathPrimitiveFactory.initialize_with_capacity`
              - Initialize a path primitive with the specified capacity.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPathPrimitiveFactory.minimum_width_supported`
            * - :py:attr:`~ansys.stk.core.graphics.IPathPrimitiveFactory.maximum_width_supported`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPathPrimitiveFactory


Property detail
---------------

.. py:property:: minimum_width_supported
    :canonical: ansys.stk.core.graphics.IPathPrimitiveFactory.minimum_width_supported
    :type: float

    Gets the minimum width, in pixels, supported by the video card.

.. py:property:: maximum_width_supported
    :canonical: ansys.stk.core.graphics.IPathPrimitiveFactory.maximum_width_supported
    :type: float

    Gets the maximum width, in pixels, supported by the video card.


Method detail
-------------

.. py:method:: initialize(self) -> IPathPrimitive
    :canonical: ansys.stk.core.graphics.IPathPrimitiveFactory.initialize

    Initialize a default path primitive. This is equivalent to constructing a path primitive with an initial capacity of 16.

    :Returns:

        :obj:`~IPathPrimitive`

.. py:method:: initialize_with_capacity(self, capacity: int) -> IPathPrimitive
    :canonical: ansys.stk.core.graphics.IPathPrimitiveFactory.initialize_with_capacity

    Initialize a path primitive with the specified capacity.

    :Parameters:

    **capacity** : :obj:`~int`

    :Returns:

        :obj:`~IPathPrimitive`



