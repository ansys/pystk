IGeospatialImageGlobeOverlay
============================

.. py:class:: ansys.stk.core.graphics.IGeospatialImageGlobeOverlay

   object
   
   A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

.. py:currentmodule:: IGeospatialImageGlobeOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IGeospatialImageGlobeOverlay.use_transparent_color`
            * - :py:attr:`~ansys.stk.core.graphics.IGeospatialImageGlobeOverlay.transparent_color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGeospatialImageGlobeOverlay


Property detail
---------------

.. py:property:: use_transparent_color
    :canonical: ansys.stk.core.graphics.IGeospatialImageGlobeOverlay.use_transparent_color
    :type: bool

    Gets or sets whether transparent color should be used.

.. py:property:: transparent_color
    :canonical: ansys.stk.core.graphics.IGeospatialImageGlobeOverlay.transparent_color
    :type: agcolor.Color

    Gets or sets the color that will become transparent.


