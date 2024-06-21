IVehiclePassBreak
=================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePassBreak

   object
   
   Satellite Pass Break properties.

.. py:currentmodule:: IVehiclePassBreak

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassBreak.set_pass_numbering_type`
              - Set the pass number corresponding to the initial conditions of the satellite.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassBreak.definition`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassBreak.partial_pass_measurement`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassBreak.coordinate_system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassBreak.repeat_ground_track_numbering`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassBreak.pass_numbering_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassBreak.pass_numbering`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassBreak.supported_coordinate_systems`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePassBreak


Property detail
---------------

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.definition
    :type: IVehicleDefinition

    Get the break angle type and, in the case of latitude, the direction at latitiude crossing.

.. py:property:: partial_pass_measurement
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.partial_pass_measurement
    :type: VEHICLE_PARTIAL_PASS_MEASUREMENT

    Gets or sets the method for calculating partial passes.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.coordinate_system
    :type: VEHICLE_COORDINATE_SYSTEM

    Gets or sets the coordinate system in which latitude and longitude are to be measured.

.. py:property:: repeat_ground_track_numbering
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.repeat_ground_track_numbering
    :type: IVehicleRepeatGroundTrackNumbering

    Get data on repeat ground track numbering.

.. py:property:: pass_numbering_type
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.pass_numbering_type
    :type: VEHICLE_PASS_NUMBERING

    Get the criterion for pass numbering.

.. py:property:: pass_numbering
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.pass_numbering
    :type: IVehiclePassNumbering

    Get pass numbering data.

.. py:property:: supported_coordinate_systems
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.supported_coordinate_systems
    :type: list

    Returns supported coordinate systems.


Method detail
-------------








.. py:method:: set_pass_numbering_type(self, passNumbering: VEHICLE_PASS_NUMBERING) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.set_pass_numbering_type

    Set the pass number corresponding to the initial conditions of the satellite.

    :Parameters:

    **passNumbering** : :obj:`~VEHICLE_PASS_NUMBERING`

    :Returns:

        :obj:`~None`



