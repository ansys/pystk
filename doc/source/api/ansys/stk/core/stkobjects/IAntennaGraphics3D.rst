IAntennaGraphics3D
==================

.. py:class:: ansys.stk.core.stkobjects.IAntennaGraphics3D

   object
   
   IAgAntennaVO Interface for a antenna's 3D Graphics properties.

.. py:currentmodule:: IAntennaGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaGraphics3D.vector`
              - Get the antenna's Vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaGraphics3D.show_boresight`
              - Opt whether to display boresight graphics for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaGraphics3D.show_contours`
              - Opt whether to display contour graphics for the antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaGraphics3D.volume_graphics`
              - Gets the antenna volume graphics interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaGraphics3D


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics3D.vector
    :type: IGraphics3DVector

    Get the antenna's Vector properties.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics3D.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the antenna.

.. py:property:: show_contours
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics3D.show_contours
    :type: bool

    Opt whether to display contour graphics for the antenna.

.. py:property:: volume_graphics
    :canonical: ansys.stk.core.stkobjects.IAntennaGraphics3D.volume_graphics
    :type: IAntennaVolumeGraphics

    Gets the antenna volume graphics interface.


