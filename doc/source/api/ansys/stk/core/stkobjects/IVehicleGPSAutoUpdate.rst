IVehicleGPSAutoUpdate
=====================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate

   object
   
   Interface for GPS AutoUpdate.

.. py:currentmodule:: IVehicleGPSAutoUpdate

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.selected_source`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.properties`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.file_source`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.online_source`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGPSAutoUpdate


Property detail
---------------

.. py:property:: selected_source
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.selected_source
    :type: VEHICLE_GPS_AUTO_UPDATE_SOURCE

    Gets or sets the source type for element updates.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.properties
    :type: IVehicleGPSAutoUpdateProperties

    Get the Automatic Update selection and method.

.. py:property:: file_source
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.file_source
    :type: IVehicleGPSAutoUpdateFileSource

    A file to be used as the element source.

.. py:property:: online_source
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.online_source
    :type: IVehicleGPSAutoUpdateOnlineSource

    AGI server to be used as the element source.


