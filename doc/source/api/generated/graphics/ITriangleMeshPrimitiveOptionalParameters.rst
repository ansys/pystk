ITriangleMeshPrimitiveOptionalParameters
========================================

.. py:class:: ITriangleMeshPrimitiveOptionalParameters

   object
   
   Optional parameters for triangle mesh primitive...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_texture_coordinates`
              - Define a collection of texture coordinates.
            * - :py:meth:`~set_per_vertex_colors`
              - Define a collection of colors.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITriangleMeshPrimitiveOptionalParameters



Method detail
-------------

.. py:method:: set_texture_coordinates(self, textureCoordinates:list) -> None

    Define a collection of texture coordinates.

    :Parameters:

    **textureCoordinates** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_per_vertex_colors(self, colors:list) -> None

    Define a collection of colors.

    :Parameters:

    **colors** : :obj:`~list`

    :Returns:

        :obj:`~None`

