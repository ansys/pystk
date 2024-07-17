TerrainNormSlopeAzimuth
=======================

.. py:class:: ansys.stk.core.stkobjects.TerrainNormSlopeAzimuth

   Bases: :py:class:`~ansys.stk.core.stkobjects.ITerrainNormData`

   Class defining Slope/Azimuth data for the TerrainNormal.

.. py:currentmodule:: TerrainNormSlopeAzimuth

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TerrainNormSlopeAzimuth.slope`
              - Specify the Slope of the local terrain, defined as the angle between the normal to the local terrain and local surface normal, where the local surface normal is defined by the reference shape of the globe. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.TerrainNormSlopeAzimuth.azimuth`
              - Specify the Azimuth (measured in an easterly sense from local north) of the normal to local terrain. This may also be thought of as the azimuth of the downhill direction. Uses Longitude Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TerrainNormSlopeAzimuth


Property detail
---------------

.. py:property:: slope
    :canonical: ansys.stk.core.stkobjects.TerrainNormSlopeAzimuth.slope
    :type: typing.Any

    Specify the Slope of the local terrain, defined as the angle between the normal to the local terrain and local surface normal, where the local surface normal is defined by the reference shape of the globe. Uses Angle Dimension.

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.TerrainNormSlopeAzimuth.azimuth
    :type: typing.Any

    Specify the Azimuth (measured in an easterly sense from local north) of the normal to local terrain. This may also be thought of as the azimuth of the downhill direction. Uses Longitude Dimension.


