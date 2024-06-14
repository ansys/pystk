ICoverageBoundsLatLonRegion
===========================

.. py:class:: ICoverageBoundsLatLonRegion

   ICoverageBounds
   
   LatLon Region: create a region between user-specified Minimum and Maximum Latitude and Longitude boundaries.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~min_latitude`
            * - :py:meth:`~max_latitude`
            * - :py:meth:`~min_longitude`
            * - :py:meth:`~max_longitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageBoundsLatLonRegion


Property detail
---------------

.. py:property:: min_latitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLatLonRegion.min_latitude
    :type: typing.Any

    Minimum latitude for defining a grid using lat-lon region.  Uses Latitude Dimension.

.. py:property:: max_latitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLatLonRegion.max_latitude
    :type: typing.Any

    Maximum latitude for defining a grid using lat-lon bounds. Uses Latitude Dimension.

.. py:property:: min_longitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLatLonRegion.min_longitude
    :type: typing.Any

    Minimum longitude for defining a grid using lat-lon region.  Uses Longitude Dimension.

.. py:property:: max_longitude
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsLatLonRegion.max_longitude
    :type: typing.Any

    Maximum longitude for defining a grid using lat-lon region. Uses Longitude Dimension.


