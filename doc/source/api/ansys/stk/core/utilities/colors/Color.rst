Color
=====

.. py:class:: ansys.stk.core.utilities.colors.Color

   object

   An opaque color representation that can be used with the STK Object Model.

.. py:currentmodule:: Color


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.utilities.colors.Color.from_rgb`
              - Create a new Color from R, G, B values.
            * - :py:attr:`~ansys.stk.core.utilities.colors.Color.get_rgb`
              - Return the R, G, B representation of this color.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.utilities.colors import Color


Method detail
-------------

.. py:method:: from_rgb(cls, r: int, g: int, b: int) -> None
    :canonical: ansys.stk.core.utilities.colors.Color.from_rgb

    Create a new Color from R, G, B values.

    :Parameters:

    **r** : :obj:`~int`
    **g** : :obj:`~int`
    **b** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: get_rgb(self)
    :canonical: ansys.stk.core.utilities.colors.Color.get_rgb

    Return the R, G, B representation of this color.


