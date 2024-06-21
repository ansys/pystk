MARKER_BATCH_SORT_ORDER
=======================

.. py:class:: ansys.stk.core.graphics.MARKER_BATCH_SORT_ORDER

   IntEnum


.. py:currentmodule:: MARKER_BATCH_SORT_ORDER

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BACK_TO_FRONT`
              - The markers are sorted in back to front order before rendering. For overlapping translucent markers, this enables correct blending results...

            * - :py:attr:`~FRONT_TO_BACK`
              - The markers are sorted in front to back order before rendering. For overlapping opaque markers, this can enable the GPU to quickly eliminate markers that are hidden behind other markers...

            * - :py:attr:`~BY_TEXTURE`
              - The markers are sorted by texture. This minimizes costly texture changes during rendering and does not require resorting when the camera moves or a marker changes position.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MARKER_BATCH_SORT_ORDER


