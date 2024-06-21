ITerrainNormSlopeAzimuth
========================

.. py:class:: ansys.stk.core.stkobjects.ITerrainNormSlopeAzimuth

   object
   
   AgTerrainNormSlopeAzimuth used to access the Slope/Azimuth data for the TerrainNormal.

.. py:currentmodule:: ITerrainNormSlopeAzimuth

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ITerrainNormSlopeAzimuth.slope`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITerrainNormSlopeAzimuth.azimuth`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITerrainNormSlopeAzimuth


Property detail
---------------

.. py:property:: slope
    :canonical: ansys.stk.core.stkobjects.ITerrainNormSlopeAzimuth.slope
    :type: typing.Any

    Specify the Slope of the local terrain, defined as the angle between the normal to the local terrain and local surface normal, where the local surface normal is defined by the reference shape of the globe. Uses Angle Dimension.

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.ITerrainNormSlopeAzimuth.azimuth
    :type: typing.Any

    Specify the Azimuth (measured in an easterly sense from local north) of the normal to local terrain. This may also be thought of as the azimuth of the downhill direction. Uses Longitude Dimension.


