ColorRGBA
=========

.. py:class:: ansys.stk.core.utilities.colors.ColorRGBA

   object

   A variably translucent color representation that can be used with certain methods in the STK Object Model.

.. py:currentmodule:: ColorRGBA


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.utilities.colors.ColorRGBA.alpha`
              - Get or set the ColorRGBA object's value for alpha, which ranges between 0 (fully translucent) and 255 (fully opaque).
            * - :py:attr:`~ansys.stk.core.utilities.colors.ColorRGBA.color`
              - The Color value that contains R, G, B values.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.utilities.colors import ColorRGBA


Method detail
-------------

.. py:method:: alpha(self) -> float
    :canonical: ansys.stk.core.utilities.colors.ColorRGBA.alpha

    Get the ColorRGBA object's value for alpha, which ranges between 0 (fully translucent) and 255 (fully opaque).

    :Returns:

        :obj:`~float`

.. py:method:: alpha(self, value: int) -> None
    :canonical: ansys.stk.core.utilities.colors.ColorRGBA.alpha

    Set the ColorRGBA object's value for alpha, which ranges between 0 (fully translucent) and 255 (fully opaque).

    :Parameters:

    **value** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: color(self) -> Color
    :canonical: ansys.stk.core.utilities.colors.ColorRGBA.color

    The Color value that contains R, G, B values.

    :Returns:

        :obj:`~Color`


