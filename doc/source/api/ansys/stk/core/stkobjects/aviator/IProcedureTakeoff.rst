IProcedureTakeoff
=================

.. py:class:: IProcedureTakeoff

   object
   
   Interface used to access the options for a takeoff procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~runway_heading_options`
            * - :py:meth:`~mode_as_normal`
            * - :py:meth:`~mode_as_departure_point`
            * - :py:meth:`~mode_as_low_transition`
            * - :py:meth:`~takeoff_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureTakeoff


Property detail
---------------

.. py:property:: runway_heading_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTakeoff.runway_heading_options
    :type: IAgAvtrRunwayHeadingOptions

    Get the runway heading options.

.. py:property:: mode_as_normal
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTakeoff.mode_as_normal
    :type: IAgAvtrTakeoffNormal

    Get the interface for a normal takeoff.

.. py:property:: mode_as_departure_point
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTakeoff.mode_as_departure_point
    :type: IAgAvtrTakeoffDeparturePoint

    Get the interface for a departure point takeoff.

.. py:property:: mode_as_low_transition
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTakeoff.mode_as_low_transition
    :type: IAgAvtrTakeoffLowTransition

    Get the interface for a low transition takeoff.

.. py:property:: takeoff_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTakeoff.takeoff_mode
    :type: TAKEOFF_MODE

    Gets or sets the type of takeoff the aircraft will perform.


Method detail
-------------







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTakeoff.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

