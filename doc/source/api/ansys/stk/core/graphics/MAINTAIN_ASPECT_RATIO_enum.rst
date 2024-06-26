MAINTAIN_ASPECT_RATIO
=====================

.. py:class:: ansys.stk.core.graphics.MAINTAIN_ASPECT_RATIO

   IntEnum


.. py:currentmodule:: MAINTAIN_ASPECT_RATIO

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NONE`
              - The aspect ratio of the texture is not maintained during sizing of the screen overlay.

            * - :py:attr:`~WIDTH`
              - The aspect ratio of the texture is maintained based on the width property of the screen overlay. When used, the height property is ignored and the height is automatically calculated based on the aspect ratio of the texture and the overlay's width property.

            * - :py:attr:`~HEIGHT`
              - The aspect ratio of the texture is maintained based on the height property of the screen overlay. When used, the width property is ignored and the width is automatically calculated based on the aspect ratio of the texture and the overlay's height property.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MAINTAIN_ASPECT_RATIO


