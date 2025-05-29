PassBreak
=========

.. py:class:: ansys.stk.core.stkobjects.PassBreak

   Satellite Pass Break properties.

.. py:currentmodule:: PassBreak

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PassBreak.set_pass_numbering_type`
              - Set the pass number corresponding to the initial conditions of the satellite.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PassBreak.definition`
              - Get the break angle type and, in the case of latitude, the direction at latitiude crossing.
            * - :py:attr:`~ansys.stk.core.stkobjects.PassBreak.partial_pass_measurement`
              - Get or set the method for calculating partial passes.
            * - :py:attr:`~ansys.stk.core.stkobjects.PassBreak.coordinate_system`
              - Get or set the coordinate system in which latitude and longitude are to be measured.
            * - :py:attr:`~ansys.stk.core.stkobjects.PassBreak.repeat_ground_track_numbering`
              - Get data on repeat ground track numbering.
            * - :py:attr:`~ansys.stk.core.stkobjects.PassBreak.pass_numbering_type`
              - Get the criterion for pass numbering.
            * - :py:attr:`~ansys.stk.core.stkobjects.PassBreak.pass_numbering`
              - Get pass numbering data.
            * - :py:attr:`~ansys.stk.core.stkobjects.PassBreak.supported_coordinate_systems`
              - Return supported coordinate systems.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PassBreak


Property detail
---------------

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.PassBreak.definition
    :type: VehicleDefinition

    Get the break angle type and, in the case of latitude, the direction at latitiude crossing.

.. py:property:: partial_pass_measurement
    :canonical: ansys.stk.core.stkobjects.PassBreak.partial_pass_measurement
    :type: VehiclePartialPassMeasurement

    Get or set the method for calculating partial passes.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.PassBreak.coordinate_system
    :type: VehicleCoordinateSystem

    Get or set the coordinate system in which latitude and longitude are to be measured.

.. py:property:: repeat_ground_track_numbering
    :canonical: ansys.stk.core.stkobjects.PassBreak.repeat_ground_track_numbering
    :type: RepeatGroundTrackNumbering

    Get data on repeat ground track numbering.

.. py:property:: pass_numbering_type
    :canonical: ansys.stk.core.stkobjects.PassBreak.pass_numbering_type
    :type: VehiclePassNumbering

    Get the criterion for pass numbering.

.. py:property:: pass_numbering
    :canonical: ansys.stk.core.stkobjects.PassBreak.pass_numbering
    :type: IVehiclePassNumbering

    Get pass numbering data.

.. py:property:: supported_coordinate_systems
    :canonical: ansys.stk.core.stkobjects.PassBreak.supported_coordinate_systems
    :type: list

    Return supported coordinate systems.


Method detail
-------------








.. py:method:: set_pass_numbering_type(self, pass_numbering: VehiclePassNumbering) -> None
    :canonical: ansys.stk.core.stkobjects.PassBreak.set_pass_numbering_type

    Set the pass number corresponding to the initial conditions of the satellite.

    :Parameters:

        **pass_numbering** : :obj:`~VehiclePassNumbering`


    :Returns:

        :obj:`~None`



