RadarGraphics3D
===============

.. py:class:: ansys.stk.core.stkobjects.RadarGraphics3D

   Class defining 3D Graphics properties of a Radar.

.. py:currentmodule:: RadarGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics3D.vector`
              - Get the radar's Vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics3D.show_boresight`
              - Opt whether to display boresight graphics for the radar's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics3D.show_contours`
              - Opt whether to display contour graphics for the radar's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarGraphics3D.volume`
              - Get the radar's antenna volume graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarGraphics3D


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.RadarGraphics3D.vector
    :type: Graphics3DVector

    Get the radar's Vector properties.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.RadarGraphics3D.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the radar's antenna.

.. py:property:: show_contours
    :canonical: ansys.stk.core.stkobjects.RadarGraphics3D.show_contours
    :type: bool

    Opt whether to display contour graphics for the radar's antenna.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.RadarGraphics3D.volume
    :type: AntennaVolumeGraphics

    Get the radar's antenna volume graphics interface.


