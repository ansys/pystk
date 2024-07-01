Colors
======

.. py:class:: ansys.stk.core.utilities.colors.Colors

   object

   A factory for creating Color objects that may be used with the STK object model.

   Contains factory methods and named colors.

.. py:currentmodule:: Colors


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.utilities.colors.Colors.from_rgb
              - Create a new Color from R, G, B values in the range [0, 255].
            * - :py:attr:`~ansys.stk.core.utilities.colors.Colors.from_rgba
              - Create a new Color from R, G, B, A values in the range [0, 255].
            * - :py:attr:`~ansys.stk.core.utilities.colors.Colors.from_argb
              - Create a new Color from an arbitrary number of values in the range [0, 255], inferred from the arguments provided.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.utilities.colors import Colors


Method detail
-------------

.. py:method:: from_rgb(r: int, g: int, b: int) -> Color
    :canonical: ansys.stk.core.utilities.colors.Colors.from_rgb

    Create a new Color from R, G, B values in the range [0, 255].

    :Parameters:

    **r** : :obj:`~int`
    **g** : :obj:`~int`
    **b** : :obj:`~int`

    :Returns:

        :obj:`~Color`

.. py:method:: from_rgba(r: int, g: int, b: int, a: int) -> ColorRGBA
    :canonical: ansys.stk.core.utilities.colors.Colors.from_rgba

    Create a new Color from R, G, B, A values in the range [0, 255].

    :Parameters:

    **r** : :obj:`~int`
    **g** : :obj:`~int`
    **b** : :obj:`~int`
    **a** : :obj:`~int`

    :Returns:

        :obj:`~ColorRGBA`

.. py:method:: from_argb()
    :canonical: ansys.stk.core.utilities.colors.Colors.from_argb

    Create a new Color from an arbitrary number of values in the range [0, 255], inferred from the arguments provided.


