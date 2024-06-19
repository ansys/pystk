IVehicleGPSAutoUpdate
=====================

.. py:class:: IVehicleGPSAutoUpdate

   object
   
   Interface for GPS AutoUpdate.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~selected_source`
            * - :py:meth:`~properties`
            * - :py:meth:`~file_source`
            * - :py:meth:`~online_source`


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
    :type: IAgVeGPSAutoUpdateProperties

    Get the Automatic Update selection and method.

.. py:property:: file_source
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.file_source
    :type: IAgVeGPSAutoUpdateFileSource

    A file to be used as the element source.

.. py:property:: online_source
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdate.online_source
    :type: IAgVeGPSAutoUpdateOnlineSource

    AGI server to be used as the element source.


