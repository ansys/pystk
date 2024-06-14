IRaster
=======

.. py:class:: IRaster

   object
   
   A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~flip`
              - Flips the raster along the given axis.
            * - :py:meth:`~rotate`
              - Rotate the raster by the given angle.
            * - :py:meth:`~apply`
              - Apply a raster filter to the raster and returns a new raster with the results of the filtering. The current raster is not modified.
            * - :py:meth:`~apply_in_place`
              - Apply a raster filter to the raster. The current raster will contain the results of the filtering.
            * - :py:meth:`~extract_band`
              - Extract the band of raster data associated with the given raster band.
            * - :py:meth:`~extract_band_from_raster_format`
              - Extract the bands of raster data associated with the given raster format.
            * - :py:meth:`~copy_from_raster`
              - Copy the data associated with the given raster into this raster.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~attributes`
            * - :py:meth:`~width`
            * - :py:meth:`~height`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IRaster


Property detail
---------------

.. py:property:: attributes
    :canonical: ansys.stk.core.graphics.IRaster.attributes
    :type: "IAgStkGraphicsRasterAttributes"

    Gets the raster attributes that define the raster data.

.. py:property:: width
    :canonical: ansys.stk.core.graphics.IRaster.width
    :type: int

    Gets the width of the raster in pixels.

.. py:property:: height
    :canonical: ansys.stk.core.graphics.IRaster.height
    :type: int

    Gets the height of the raster in pixels.


Method detail
-------------




.. py:method:: flip(self, axis:"FLIP_AXIS") -> None

    Flips the raster along the given axis.

    :Parameters:

    **axis** : :obj:`~"FLIP_AXIS"`

    :Returns:

        :obj:`~None`

.. py:method:: rotate(self, angle:float) -> None

    Rotate the raster by the given angle.

    :Parameters:

    **angle** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: apply(self, filter:"IRasterFilter") -> "IRaster"

    Apply a raster filter to the raster and returns a new raster with the results of the filtering. The current raster is not modified.

    :Parameters:

    **filter** : :obj:`~"IRasterFilter"`

    :Returns:

        :obj:`~"IRaster"`

.. py:method:: apply_in_place(self, filter:"IRasterFilter") -> None

    Apply a raster filter to the raster. The current raster will contain the results of the filtering.

    :Parameters:

    **filter** : :obj:`~"IRasterFilter"`

    :Returns:

        :obj:`~None`

.. py:method:: extract_band(self, band:"RASTER_BAND") -> "IRaster"

    Extract the band of raster data associated with the given raster band.

    :Parameters:

    **band** : :obj:`~"RASTER_BAND"`

    :Returns:

        :obj:`~"IRaster"`

.. py:method:: extract_band_from_raster_format(self, format:"RASTER_FORMAT") -> "IRaster"

    Extract the bands of raster data associated with the given raster format.

    :Parameters:

    **format** : :obj:`~"RASTER_FORMAT"`

    :Returns:

        :obj:`~"IRaster"`

.. py:method:: copy_from_raster(self, raster:"IRaster") -> None

    Copy the data associated with the given raster into this raster.

    :Parameters:

    **raster** : :obj:`~"IRaster"`

    :Returns:

        :obj:`~None`

