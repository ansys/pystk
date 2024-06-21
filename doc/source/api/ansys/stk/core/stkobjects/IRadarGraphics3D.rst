IRadarGraphics3D
================

.. py:class:: ansys.stk.core.stkobjects.IRadarGraphics3D

   object
   
   IAgRadarVO Interface for a radar's 3D Graphics properties.

.. py:currentmodule:: IRadarGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarGraphics3D.vector`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarGraphics3D.show_boresight`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarGraphics3D.show_contours`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarGraphics3D.volume`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarGraphics3D


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics3D.vector
    :type: IGraphics3DVector

    Get the radar's Vector properties.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics3D.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the radar's antenna.

.. py:property:: show_contours
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics3D.show_contours
    :type: bool

    Opt whether to display contour graphics for the radar's antenna.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.IRadarGraphics3D.volume
    :type: IAntennaVolumeGraphics

    Gets the radar's antenna volume graphics interface.


