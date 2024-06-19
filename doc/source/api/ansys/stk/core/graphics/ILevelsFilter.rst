ILevelsFilter
=============

.. py:class:: ILevelsFilter

   object
   
   Adjusts the band levels of the source raster linearly.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_level_adjustment`
              - Set the linear level adjustment value for the given raster band. Both negative and positive values are accepted.
            * - :py:meth:`~clear_adjustments`
              - Clear the level adjustment values for all bands.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ILevelsFilter



Method detail
-------------

.. py:method:: set_level_adjustment(self, band: RASTER_BAND, adjustment: int) -> None
    :canonical: ansys.stk.core.graphics.ILevelsFilter.set_level_adjustment

    Set the linear level adjustment value for the given raster band. Both negative and positive values are accepted.

    :Parameters:

    **band** : :obj:`~RASTER_BAND`
    **adjustment** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: clear_adjustments(self) -> None
    :canonical: ansys.stk.core.graphics.ILevelsFilter.clear_adjustments

    Clear the level adjustment values for all bands.

    :Returns:

        :obj:`~None`

