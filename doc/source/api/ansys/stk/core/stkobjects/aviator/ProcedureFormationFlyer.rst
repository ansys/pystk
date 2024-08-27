ProcedureFormationFlyer
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining an formationflyer procedure.

.. py:currentmodule:: ProcedureFormationFlyer

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.min_time_step`
              - Get Min time Step.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.max_time_step`
              - Get Max time Step.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.cross_range_close_rate`
              - Get Cross Range close rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.initial_close_max_speed_advantage`
              - Get Initial Close Max Speed Advantage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_condition`
              - Get Stop condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_time`
              - Get stop time.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_down_range`
              - Get stop downrange.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_fuel_state`
              - Get stop fuel state.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_on_hover`
              - Set Stop on hover mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureFormationFlyer


Property detail
---------------

.. py:property:: min_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.min_time_step
    :type: float

    Get Min time Step.

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.max_time_step
    :type: float

    Get Max time Step.

.. py:property:: cross_range_close_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.cross_range_close_rate
    :type: float

    Get Cross Range close rate.

.. py:property:: initial_close_max_speed_advantage
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.initial_close_max_speed_advantage
    :type: float

    Get Initial Close Max Speed Advantage.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_condition
    :type: FORMATION_FLYER_STOP_CONDITION

    Get Stop condition.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_time
    :type: float

    Get stop time.

.. py:property:: stop_down_range
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_down_range
    :type: float

    Get stop downrange.

.. py:property:: stop_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_fuel_state
    :type: float

    Get stop fuel state.

.. py:property:: stop_on_hover
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.stop_on_hover
    :type: None

    Set Stop on hover mode.


Method detail
-------------

















.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`



