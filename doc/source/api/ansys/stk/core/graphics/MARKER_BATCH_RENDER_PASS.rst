MARKER_BATCH_RENDER_PASS
========================

.. py:class:: MARKER_BATCH_RENDER_PASS

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
              - The marker batch contains all opaque textures and therefore should be rendered using the opaque pass.

            * - :py:attr:`~TRANSLUCENT`
              - The marker batch contains textures with translucency and therefore should be rendered using the translucent pass. For correct blending of overlapping textures, also consider using back to front.

            * - :py:attr:`~BASED_ON_TRANSLUCENCY`
              - The marker batch render pass should be determined based on the marker batch's translucency. This includes the translucency set per marker when SetColors is used.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MARKER_BATCH_RENDER_PASS


