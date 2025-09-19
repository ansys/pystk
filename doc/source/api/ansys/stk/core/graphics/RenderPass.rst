RenderPass
==========

.. py:class:: ansys.stk.core.graphics.RenderPass

   IntFlag


.. py:currentmodule:: RenderPass

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~OPAQUE`
              - Render during the opaque rendering pass.

            * - :py:attr:`~TRANSLUCENT`
              - Render during the translucent rendering pass.

            * - :py:attr:`~CENTRAL_BODY_CLIPPED`
              - Render before the central body is rendered.

            * - :py:attr:`~ORDERED_COMPOSITE_CENTRAL_BODY_CLIPPED`
              - Rendered in an ordered composite before all other primitives and before the central body is rendered.

            * - :py:attr:`~ORDERED_COMPOSITE`
              - Rendered in an ordered composite before all primitives but after the central body is rendered.

            * - :py:attr:`~TERRAIN`
              - Render after the terrain is rendered.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RenderPass


