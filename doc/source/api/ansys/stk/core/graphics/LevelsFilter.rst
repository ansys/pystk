LevelsFilter
============

.. py:class:: ansys.stk.core.graphics.LevelsFilter

   Bases: :py:class:`~ansys.stk.core.graphics.IRasterFilter`

   Adjusts the band levels of the source raster linearly.

.. py:currentmodule:: LevelsFilter

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.LevelsFilter.set_level_adjustment`
              - Set the linear level adjustment value for the given raster band. Both negative and positive values are accepted.
            * - :py:attr:`~ansys.stk.core.graphics.LevelsFilter.clear_adjustments`
              - Clear the level adjustment values for all bands.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import LevelsFilter



Method detail
-------------

.. py:method:: set_level_adjustment(self, band: RASTER_BAND, adjustment: int) -> None
    :canonical: ansys.stk.core.graphics.LevelsFilter.set_level_adjustment

    Set the linear level adjustment value for the given raster band. Both negative and positive values are accepted.

    :Parameters:

    **band** : :obj:`~RASTER_BAND`
    **adjustment** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: clear_adjustments(self) -> None
    :canonical: ansys.stk.core.graphics.LevelsFilter.clear_adjustments

    Clear the level adjustment values for all bands.

    :Returns:

        :obj:`~None`

