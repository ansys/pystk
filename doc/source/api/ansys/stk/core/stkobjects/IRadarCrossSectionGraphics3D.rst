IRadarCrossSectionGraphics3D
============================

.. py:class:: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics3D

   object
   
   IAgRadarCrossSectionVO Interface for radar cross section 3D properties.

.. py:currentmodule:: IRadarCrossSectionGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics3D.show_contours`
              - Option for displaying radar cross section contour graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionGraphics3D.volume_graphics`
              - Gets the radar cross section volume graphics interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionGraphics3D


Property detail
---------------

.. py:property:: show_contours
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics3D.show_contours
    :type: bool

    Option for displaying radar cross section contour graphics.

.. py:property:: volume_graphics
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionGraphics3D.volume_graphics
    :type: IRadarCrossSectionVolumeGraphics

    Gets the radar cross section volume graphics interface.


