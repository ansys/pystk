IRadarCrossSectionGraphics3D
============================

.. py:class:: IRadarCrossSectionGraphics3D

   object
   
   IAgRadarCrossSectionVO Interface for radar cross section 3D properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~show_contours`
            * - :py:meth:`~volume_graphics`


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
    :type: IAgRadarCrossSectionVolumeGraphics

    Gets the radar cross section volume graphics interface.


