ProcedureTakeoff
================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a takeoff procedure.

.. py:currentmodule:: ProcedureTakeoff

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.runway_heading_options`
              - Get the runway heading options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_normal`
              - Get the interface for a normal takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_departure_point`
              - Get the interface for a departure point takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_low_transition`
              - Get the interface for a low transition takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.takeoff_mode`
              - Gets or sets the type of takeoff the aircraft will perform.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureTakeoff


Property detail
---------------

.. py:property:: runway_heading_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.runway_heading_options
    :type: IRunwayHeadingOptions

    Get the runway heading options.

.. py:property:: mode_as_normal
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_normal
    :type: ITakeoffNormal

    Get the interface for a normal takeoff.

.. py:property:: mode_as_departure_point
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_departure_point
    :type: ITakeoffDeparturePoint

    Get the interface for a departure point takeoff.

.. py:property:: mode_as_low_transition
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.mode_as_low_transition
    :type: ITakeoffLowTransition

    Get the interface for a low transition takeoff.

.. py:property:: takeoff_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.takeoff_mode
    :type: TAKEOFF_MODE

    Gets or sets the type of takeoff the aircraft will perform.


Method detail
-------------







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTakeoff.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

