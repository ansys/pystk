IVehicleGraphics3DOrbitTrackData
================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitTrackData

   object
   
   Interface for 3D leading/trailing track data for satellites.

.. py:currentmodule:: IVehicleGraphics3DOrbitTrackData

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitTrackData.inherit_from_2d`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitTrackData.pass_data`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DOrbitTrackData


Property detail
---------------

.. py:property:: inherit_from_2d
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitTrackData.inherit_from_2d
    :type: bool

    Opt whether to inherit the 3D leading/trailing track data from 2D graphics.

.. py:property:: pass_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitTrackData.pass_data
    :type: IVehicleGraphics3DOrbitPassData

    Get the 3D leading/trailing track data.


