RENDER_PASS_HINT
================

.. py:class:: RENDER_PASS_HINT

   IntEnum


.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~OPAQUE`
              - The collection of colors contains only opaque colors. This implies that each color's alpha component is 255.

            * - :py:attr:`~TRANSLUCENT`
              - The collection of colors contains translucent colors. This implies that at least one color has an alpha component that is not 255.

            * - :py:attr:`~UNKNOWN`
              - It is unknown if the collection of colors contains opaque or translucent colors.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RENDER_PASS_HINT


