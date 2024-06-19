IGeospatialImageGlobeOverlayFactory
===================================

.. py:class:: IGeospatialImageGlobeOverlayFactory

   object
   
   A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize_with_string`
              - Initialize a geospatial image globe overlay with the provided values.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGeospatialImageGlobeOverlayFactory



Method detail
-------------

.. py:method:: initialize_with_string(self, uri: str) -> IGeospatialImageGlobeOverlay
    :canonical: ansys.stk.core.graphics.IGeospatialImageGlobeOverlayFactory.initialize_with_string

    Initialize a geospatial image globe overlay with the provided values.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~IGeospatialImageGlobeOverlay`

