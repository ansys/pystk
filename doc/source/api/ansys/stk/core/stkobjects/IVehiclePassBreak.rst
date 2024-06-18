IVehiclePassBreak
=================

.. py:class:: IVehiclePassBreak

   object
   
   Satellite Pass Break properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_pass_numbering_type`
              - Set the pass number corresponding to the initial conditions of the satellite.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~definition`
            * - :py:meth:`~partial_pass_measurement`
            * - :py:meth:`~coordinate_system`
            * - :py:meth:`~repeat_ground_track_numbering`
            * - :py:meth:`~pass_numbering_type`
            * - :py:meth:`~pass_numbering`
            * - :py:meth:`~supported_coordinate_systems`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePassBreak


Property detail
---------------

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.definition
    :type: "IAgVeDefinition"

    Get the break angle type and, in the case of latitude, the direction at latitiude crossing.

.. py:property:: partial_pass_measurement
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.partial_pass_measurement
    :type: "VEHICLE_PARTIAL_PASS_MEASUREMENT"

    Gets or sets the method for calculating partial passes.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.coordinate_system
    :type: "VEHICLE_COORDINATE_SYSTEM"

    Gets or sets the coordinate system in which latitude and longitude are to be measured.

.. py:property:: repeat_ground_track_numbering
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.repeat_ground_track_numbering
    :type: "IAgVeRepeatGroundTrackNumbering"

    Get data on repeat ground track numbering.

.. py:property:: pass_numbering_type
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.pass_numbering_type
    :type: "VEHICLE_PASS_NUMBERING"

    Get the criterion for pass numbering.

.. py:property:: pass_numbering
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.pass_numbering
    :type: "IAgVePassNumbering"

    Get pass numbering data.

.. py:property:: supported_coordinate_systems
    :canonical: ansys.stk.core.stkobjects.IVehiclePassBreak.supported_coordinate_systems
    :type: list

    Returns supported coordinate systems.


Method detail
-------------








.. py:method:: set_pass_numbering_type(self, passNumbering:"VEHICLE_PASS_NUMBERING") -> None

    Set the pass number corresponding to the initial conditions of the satellite.

    :Parameters:

    **passNumbering** : :obj:`~"VEHICLE_PASS_NUMBERING"`

    :Returns:

        :obj:`~None`



