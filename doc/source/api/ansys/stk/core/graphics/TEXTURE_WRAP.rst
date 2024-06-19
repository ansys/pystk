TEXTURE_WRAP
============

.. py:class:: TEXTURE_WRAP

   IntEnum


.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CLAMP`
              - Clamp the texture coordinate to the range [0, 1].

            * - :py:attr:`~CLAMP_TO_BORDER`
              - Clamp the texture coordinate to the range [-1/2N, 1 + 1/2N], where N is the size the texture in the direction of clamping.

            * - :py:attr:`~CLAMP_TO_EDGE`
              - Clamp the texture coordinate to the range [1/2N, 1 - 1/2N], where N is the size the texture in the direction of clamping.

            * - :py:attr:`~MIRRORED_REPEAT`
              - If the integer part of the texture coordinate is even, use the fractional part of the texture coordinate. Otherwise, use one minus the fractional part of the texture coordinate.

            * - :py:attr:`~REPEAT`
              - Ignore the integer part of the texture coordinate.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TEXTURE_WRAP


