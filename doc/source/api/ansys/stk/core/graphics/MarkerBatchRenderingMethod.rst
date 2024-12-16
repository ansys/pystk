MarkerBatchRenderingMethod
==========================

.. py:class:: ansys.stk.core.graphics.MarkerBatchRenderingMethod

   IntEnum


.. py:currentmodule:: MarkerBatchRenderingMethod

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~GEOMETRY_SHADER`
              - Render the marker batch using a geometry shader.

            * - :py:attr:`~VERTEX_SHADER`
              - Render the marker batch using a vertex shader.

            * - :py:attr:`~AUTOMATIC`
              - Render the marker batch using an automatically selected method based on the capabilities of the video card.

            * - :py:attr:`~FIXED_FUNCTION`
              - Render the marker batch using the fixed function pipeline. Generally, this is the slowest method but it supports all video cards.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MarkerBatchRenderingMethod


