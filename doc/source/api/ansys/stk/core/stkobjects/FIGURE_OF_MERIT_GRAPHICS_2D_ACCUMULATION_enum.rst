FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION
========================================

.. py:class:: ansys.stk.core.stkobjects.FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION

   IntEnum


.. py:currentmodule:: FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CURRENT_TIME`
              - When animating, grid points that currently meet the satisfaction criterion are highlighted.

            * - :py:attr:`~NOT_CURRENT`
              - When animating, grid points that currently do not meet the satisfaction criterion are highlighted.

            * - :py:attr:`~NOT_UP_TO_CURRENT`
              - When animating, grid points that have not met the satisfaction criterion based on the dynamic definition of the figure of merit from the start time to the current time are highlighted.

            * - :py:attr:`~UP_TO_CURRENT`
              - When animating, grid points that have met the satisfaction criterion based on the dynamic definition of the figure of merit from the start time to the current time are highlighted.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION


