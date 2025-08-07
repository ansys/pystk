PathPrimitiveFactory
====================

.. py:class:: ansys.stk.core.graphics.PathPrimitiveFactory

   Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

.. py:currentmodule:: PathPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitiveFactory.initialize`
              - Initialize a default path primitive. This is equivalent to constructing a path primitive with an initial capacity of 16.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitiveFactory.initialize_with_capacity`
              - Initialize a path primitive with the specified capacity.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitiveFactory.maximum_width_supported`
              - Get the maximum width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitiveFactory.minimum_width_supported`
              - Get the minimum width, in pixels, supported by the video card.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PathPrimitiveFactory


Property detail
---------------

.. py:property:: maximum_width_supported
    :canonical: ansys.stk.core.graphics.PathPrimitiveFactory.maximum_width_supported
    :type: float

    Get the maximum width, in pixels, supported by the video card.

.. py:property:: minimum_width_supported
    :canonical: ansys.stk.core.graphics.PathPrimitiveFactory.minimum_width_supported
    :type: float

    Get the minimum width, in pixels, supported by the video card.


Method detail
-------------

.. py:method:: initialize(self) -> PathPrimitive
    :canonical: ansys.stk.core.graphics.PathPrimitiveFactory.initialize

    Initialize a default path primitive. This is equivalent to constructing a path primitive with an initial capacity of 16.

    :Returns:

        :obj:`~PathPrimitive`

.. py:method:: initialize_with_capacity(self, capacity: int) -> PathPrimitive
    :canonical: ansys.stk.core.graphics.PathPrimitiveFactory.initialize_with_capacity

    Initialize a path primitive with the specified capacity.

    :Parameters:

        **capacity** : :obj:`~int`


    :Returns:

        :obj:`~PathPrimitive`



