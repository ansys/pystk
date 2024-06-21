IAlphaFromRasterFilter
======================

.. py:class:: ansys.stk.core.graphics.IAlphaFromRasterFilter

   object
   
   Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

.. py:currentmodule:: IAlphaFromRasterFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IAlphaFromRasterFilter.raster`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IAlphaFromRasterFilter


Property detail
---------------

.. py:property:: raster
    :canonical: ansys.stk.core.graphics.IAlphaFromRasterFilter.raster
    :type: IRaster

    Gets or sets the raster that the source raster will use to derive an alpha band.


