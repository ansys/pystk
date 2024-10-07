VehicleSGP4AutoUpdate
=====================

.. py:class:: ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate

   SGP4 AutoUpdate.

.. py:currentmodule:: VehicleSGP4AutoUpdate

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate.selected_source`
              - Gets or sets the source type for element updates.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate.properties`
              - Get the Automatic Update selection and method.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate.file_source`
              - A file to be used as the element source, containing GP data (either TLEs or CCSDS OMM content).
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate.online_source`
              - AGI server to be used as the element source.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSGP4AutoUpdate


Property detail
---------------

.. py:property:: selected_source
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate.selected_source
    :type: VEHICLE_SGP4_AUTO_UPDATE_SOURCE

    Gets or sets the source type for element updates.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate.properties
    :type: VehicleSGP4AutoUpdateProperties

    Get the Automatic Update selection and method.

.. py:property:: file_source
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate.file_source
    :type: VehicleSGP4AutoUpdateFileSource

    A file to be used as the element source, containing GP data (either TLEs or CCSDS OMM content).

.. py:property:: online_source
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate.online_source
    :type: VehicleSGP4AutoUpdateOnlineSource

    AGI server to be used as the element source.


