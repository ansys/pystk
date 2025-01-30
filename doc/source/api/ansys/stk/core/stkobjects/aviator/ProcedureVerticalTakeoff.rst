ProcedureVerticalTakeoff
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a vertical takeoff procedure.

.. py:currentmodule:: ProcedureVerticalTakeoff

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.set_heading`
              - Set the heading and heading reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.altitude_above_point`
              - Gets or sets the altitude the aircraft will takeoff to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.final_altitude_rate`
              - Gets or sets the altitude rate at the end of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.altitude_offset`
              - Gets or sets the altitude offset from the site to begin the vertical takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.heading`
              - Get the heading for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.use_magnetic_heading`
              - Get the option to use a magnetic heading.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.heading_into_wind`
              - Gets or sets the option to define the heading according to the wind direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.hold_on_deck`
              - Gets or sets the duration the aircraft will wait before beginning the takeoff.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureVerticalTakeoff


Property detail
---------------

.. py:property:: altitude_above_point
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.altitude_above_point
    :type: float

    Gets or sets the altitude the aircraft will takeoff to.

.. py:property:: final_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.final_altitude_rate
    :type: VTOLRateMode

    Gets or sets the altitude rate at the end of the procedure.

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.altitude_offset
    :type: float

    Gets or sets the altitude offset from the site to begin the vertical takeoff.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.heading
    :type: typing.Any

    Get the heading for the procedure.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.use_magnetic_heading
    :type: bool

    Get the option to use a magnetic heading.

.. py:property:: heading_into_wind
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.heading_into_wind
    :type: bool

    Gets or sets the option to define the heading according to the wind direction.

.. py:property:: hold_on_deck
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.hold_on_deck
    :type: typing.Any

    Gets or sets the duration the aircraft will wait before beginning the takeoff.


Method detail
-------------







.. py:method:: set_heading(self, heading: typing.Any, is_magnetic: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.set_heading

    Set the heading and heading reference.

    :Parameters:

    **heading** : :obj:`~typing.Any`
    **is_magnetic** : :obj:`~bool`

    :Returns:

        :obj:`~None`







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

