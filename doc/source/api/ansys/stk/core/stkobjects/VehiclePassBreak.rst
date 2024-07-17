VehiclePassBreak
================

.. py:class:: ansys.stk.core.stkobjects.VehiclePassBreak

   Bases: 

   Satellite Pass Break properties.

.. py:currentmodule:: VehiclePassBreak

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePassBreak.set_pass_numbering_type`
              - Set the pass number corresponding to the initial conditions of the satellite.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePassBreak.definition`
              - Get the break angle type and, in the case of latitude, the direction at latitiude crossing.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePassBreak.partial_pass_measurement`
              - Gets or sets the method for calculating partial passes.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePassBreak.coordinate_system`
              - Gets or sets the coordinate system in which latitude and longitude are to be measured.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePassBreak.repeat_ground_track_numbering`
              - Get data on repeat ground track numbering.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePassBreak.pass_numbering_type`
              - Get the criterion for pass numbering.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePassBreak.pass_numbering`
              - Get pass numbering data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePassBreak.supported_coordinate_systems`
              - Returns supported coordinate systems.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePassBreak


Property detail
---------------

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.VehiclePassBreak.definition
    :type: IVehicleDefinition

    Get the break angle type and, in the case of latitude, the direction at latitiude crossing.

.. py:property:: partial_pass_measurement
    :canonical: ansys.stk.core.stkobjects.VehiclePassBreak.partial_pass_measurement
    :type: VEHICLE_PARTIAL_PASS_MEASUREMENT

    Gets or sets the method for calculating partial passes.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.VehiclePassBreak.coordinate_system
    :type: VEHICLE_COORDINATE_SYSTEM

    Gets or sets the coordinate system in which latitude and longitude are to be measured.

.. py:property:: repeat_ground_track_numbering
    :canonical: ansys.stk.core.stkobjects.VehiclePassBreak.repeat_ground_track_numbering
    :type: IVehicleRepeatGroundTrackNumbering

    Get data on repeat ground track numbering.

.. py:property:: pass_numbering_type
    :canonical: ansys.stk.core.stkobjects.VehiclePassBreak.pass_numbering_type
    :type: VEHICLE_PASS_NUMBERING

    Get the criterion for pass numbering.

.. py:property:: pass_numbering
    :canonical: ansys.stk.core.stkobjects.VehiclePassBreak.pass_numbering
    :type: IVehiclePassNumbering

    Get pass numbering data.

.. py:property:: supported_coordinate_systems
    :canonical: ansys.stk.core.stkobjects.VehiclePassBreak.supported_coordinate_systems
    :type: list

    Returns supported coordinate systems.


Method detail
-------------








.. py:method:: set_pass_numbering_type(self, passNumbering: VEHICLE_PASS_NUMBERING) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePassBreak.set_pass_numbering_type

    Set the pass number corresponding to the initial conditions of the satellite.

    :Parameters:

    **passNumbering** : :obj:`~VEHICLE_PASS_NUMBERING`

    :Returns:

        :obj:`~None`



