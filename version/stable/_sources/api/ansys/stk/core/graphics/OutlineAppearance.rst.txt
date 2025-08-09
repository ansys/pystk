OutlineAppearance
=================

.. py:class:: ansys.stk.core.graphics.OutlineAppearance

   IntEnum


.. py:currentmodule:: OutlineAppearance

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FRONT_AND_BACK_LINES`
              - Both the front and back lines are displayed.

            * - :py:attr:`~FRONT_LINES_ONLY`
              - Only the front lines are displayed. This can be used to declutter the outline.

            * - :py:attr:`~STYLIZE_BACK_LINES`
              - Both the front and back lines are displayed. The back lines are displayed using a different color, translucency, and width. This is used to declutter the outline but still provide a visual cue for the back facing geometry.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import OutlineAppearance


