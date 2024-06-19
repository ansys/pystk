IVehicleSGP4AutoUpdate
======================

.. py:class:: IVehicleSGP4AutoUpdate

   object
   
   SGP4 Automatic Update properties.

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

    from ansys.stk.core.stkobjects import IVehicleSGP4AutoUpdate


Property detail
---------------

.. py:property:: selected_source
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4AutoUpdate.selected_source
    :type: VEHICLE_SGP4_AUTO_UPDATE_SOURCE

    Gets or sets the source type for element updates.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4AutoUpdate.properties
    :type: IAgVeSGP4AutoUpdateProperties

    Get the Automatic Update selection and method.

.. py:property:: file_source
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4AutoUpdate.file_source
    :type: IAgVeSGP4AutoUpdateFileSource

    A file to be used as the element source, containing GP data (either TLEs or CCSDS OMM content).

.. py:property:: online_source
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4AutoUpdate.online_source
    :type: IAgVeSGP4AutoUpdateOnlineSource

    AGI server to be used as the element source.


