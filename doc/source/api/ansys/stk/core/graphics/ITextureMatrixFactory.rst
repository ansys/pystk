ITextureMatrixFactory
=====================

.. py:class:: ITextureMatrixFactory

   object
   
   A 4 by 4 matrix applied to a texture coordinate.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a texture matrix to the identity matrix.
            * - :py:meth:`~initialize_by_values`
              - Initialize a texture matrix. The subscripts define [row][column].
            * - :py:meth:`~initialize_with_affine_transform`
              - Initialize a texture matrix from a matrix. The upper left 2x2 matrix defines rotation and scaling. The top two elements of the last column define translation.
            * - :py:meth:`~initialize_with_rectangles`
              - Initialize a texture matrix from texture corner points. Normally, a texture is mapped such that the lower left corner is texture coordinate (0, 0), the lower right is (1, 0), the upper right is (1, 1), and the upper left is (0, 1)...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextureMatrixFactory



Method detail
-------------

.. py:method:: initialize(self) -> "ITextureMatrix"

    Initialize a texture matrix to the identity matrix.

    :Returns:

        :obj:`~"ITextureMatrix"`

.. py:method:: initialize_by_values(self, m11:float, m12:float, m13:float, m14:float, m21:float, m22:float, m23:float, m24:float, m31:float, m32:float, m33:float, m34:float, m41:float, m42:float, m43:float, m44:float) -> "ITextureMatrix"

    Initialize a texture matrix. The subscripts define [row][column].

    :Parameters:

    **m11** : :obj:`~float`
    **m12** : :obj:`~float`
    **m13** : :obj:`~float`
    **m14** : :obj:`~float`
    **m21** : :obj:`~float`
    **m22** : :obj:`~float`
    **m23** : :obj:`~float`
    **m24** : :obj:`~float`
    **m31** : :obj:`~float`
    **m32** : :obj:`~float`
    **m33** : :obj:`~float`
    **m34** : :obj:`~float`
    **m41** : :obj:`~float`
    **m42** : :obj:`~float`
    **m43** : :obj:`~float`
    **m44** : :obj:`~float`

    :Returns:

        :obj:`~"ITextureMatrix"`

.. py:method:: initialize_with_affine_transform(self, matrix:list) -> "ITextureMatrix"

    Initialize a texture matrix from a matrix. The upper left 2x2 matrix defines rotation and scaling. The top two elements of the last column define translation.

    :Parameters:

    **matrix** : :obj:`~list`

    :Returns:

        :obj:`~"ITextureMatrix"`

.. py:method:: initialize_with_rectangles(self, corner0:list, corner1:list, corner2:list, corner3:list) -> "ITextureMatrix"

    Initialize a texture matrix from texture corner points. Normally, a texture is mapped such that the lower left corner is texture coordinate (0, 0), the lower right is (1, 0), the upper right is (1, 1), and the upper left is (0, 1)...

    :Parameters:

    **corner0** : :obj:`~list`
    **corner1** : :obj:`~list`
    **corner2** : :obj:`~list`
    **corner3** : :obj:`~list`

    :Returns:

        :obj:`~"ITextureMatrix"`

