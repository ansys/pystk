RefreshRate
===========

.. py:class:: ansys.stk.core.graphics.RefreshRate

   IntEnum


.. py:currentmodule:: RefreshRate

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FASTEST`
              - The animation will occur as fast as possible. The maximum frame rate is the refresh rate of the display or is the maximum that video card is capable of if the video card's vertical sync is off.

            * - :py:attr:`~TARGETED_FRAMES_PER_SECOND`
              - The animation will target a specified frame rate.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RefreshRate


