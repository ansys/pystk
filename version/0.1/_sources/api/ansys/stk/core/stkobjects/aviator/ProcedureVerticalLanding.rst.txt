ProcedureVerticalLanding
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a vertical landing procedure.

.. py:currentmodule:: ProcedureVerticalLanding

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.set_heading`
              - Set the heading and heading reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.altitude_above_point`
              - Get or set the altitude the aircraft will takeoff to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.final_altitude_rate`
              - Get or set the altitude rate at the end of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.altitude_offset`
              - Get or set the altitude offset from the site to begin the vertical takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.heading_mode`
              - Get or set the mode to define the heading during the landing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.heading`
              - Get the heading for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.use_magnetic_heading`
              - Get the option to use a magnetic heading.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.radius_factor`
              - Get or set the radius factor for turns performed while translating to the hover point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureVerticalLanding


Property detail
---------------

.. py:property:: altitude_above_point
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.altitude_above_point
    :type: float

    Get or set the altitude the aircraft will takeoff to.

.. py:property:: final_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.final_altitude_rate
    :type: VTOLRateMode

    Get or set the altitude rate at the end of the procedure.

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.altitude_offset
    :type: float

    Get or set the altitude offset from the site to begin the vertical takeoff.

.. py:property:: heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.heading_mode
    :type: VertLandingMode

    Get or set the mode to define the heading during the landing.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.heading
    :type: typing.Any

    Get the heading for the procedure.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.use_magnetic_heading
    :type: bool

    Get the option to use a magnetic heading.

.. py:property:: radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.radius_factor
    :type: float

    Get or set the radius factor for turns performed while translating to the hover point.


Method detail
-------------









.. py:method:: set_heading(self, heading: typing.Any, is_magnetic: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.set_heading

    Set the heading and heading reference.

    :Parameters:

        **heading** : :obj:`~typing.Any`

        **is_magnetic** : :obj:`~bool`


    :Returns:

        :obj:`~None`





.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

