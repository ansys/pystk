MAGNIFICATION_FILTER
====================

.. py:class:: MAGNIFICATION_FILTER

   IntEnum


.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NEAREST`
              - Use the texel that is closest to the center of the pixel being textured. This usually faster than Linear but can produce images with sharper edges.

            * - :py:attr:`~LINEAR`
              - Use the weighted average of the four texels that are closest to the center of the pixel being textured.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MAGNIFICATION_FILTER


