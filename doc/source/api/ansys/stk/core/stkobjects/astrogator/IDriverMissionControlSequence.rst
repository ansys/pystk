IDriverMissionControlSequence
=============================

.. py:class:: IDriverMissionControlSequence

   object
   
   Properties for the Mission Control Sequence.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~run_mission_control_sequence`
              - Run the current MCS.
            * - :py:meth:`~begin_run`
              - Begins an individual segment mode run.
            * - :py:meth:`~end_run`
              - End an individual segment mode run.
            * - :py:meth:`~clear_dwc_graphics`
              - Clear the draw while calculating graphics.
            * - :py:meth:`~reset_all_profiles`
              - Reset all active profiles in all target sequences.
            * - :py:meth:`~apply_all_profile_changes`
              - Apply all active profile changes in all target sequences.
            * - :py:meth:`~append_run`
              - Append the existing ephemeris with another individual segment mode run.
            * - :py:meth:`~append_run_from_time`
              - Append the existing ephemeris with another individual segment mode run, starting at a specified time. Ephemeris is cleared from time based on clear direction.
            * - :py:meth:`~append_run_from_state`
              - Append the existing ephemeris with another individual segment mode run, starting at a specified state. Ephemeris is cleared from time based on clear direction.
            * - :py:meth:`~run_mission_control_sequence2`
              - Run the current MCS and returns an error code.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~main_sequence`
            * - :py:meth:`~options`
            * - :py:meth:`~auto_sequence`
            * - :py:meth:`~calculation_graphs`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IDriverMissionControlSequence


Property detail
---------------

.. py:property:: main_sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.main_sequence
    :type: IAgVAMCSSegmentCollection

    Get the Mission Control Sequence.

.. py:property:: options
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.options
    :type: IAgVAMCSOptions

    Get the Mission Control Sequence options.

.. py:property:: auto_sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.auto_sequence
    :type: IAgVAAutomaticSequenceCollection

    Get the Automatic Sequences.

.. py:property:: calculation_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.calculation_graphs
    :type: IAgVACalculationGraphCollection

    Get the calculation graphs.


Method detail
-------------




.. py:method:: run_mission_control_sequence(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.run_mission_control_sequence

    Run the current MCS.

    :Returns:

        :obj:`~None`

.. py:method:: begin_run(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.begin_run

    Begins an individual segment mode run.

    :Returns:

        :obj:`~None`

.. py:method:: end_run(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.end_run

    End an individual segment mode run.

    :Returns:

        :obj:`~None`

.. py:method:: clear_dwc_graphics(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.clear_dwc_graphics

    Clear the draw while calculating graphics.

    :Returns:

        :obj:`~None`

.. py:method:: reset_all_profiles(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.reset_all_profiles

    Reset all active profiles in all target sequences.

    :Returns:

        :obj:`~None`

.. py:method:: apply_all_profile_changes(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.apply_all_profile_changes

    Apply all active profile changes in all target sequences.

    :Returns:

        :obj:`~None`

.. py:method:: append_run(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.append_run

    Append the existing ephemeris with another individual segment mode run.

    :Returns:

        :obj:`~None`

.. py:method:: append_run_from_time(self, epoch: typing.Any, clearEphemerisDirection: CLEAR_EPHEMERIS_DIRECTION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.append_run_from_time

    Append the existing ephemeris with another individual segment mode run, starting at a specified time. Ephemeris is cleared from time based on clear direction.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **clearEphemerisDirection** : :obj:`~CLEAR_EPHEMERIS_DIRECTION`

    :Returns:

        :obj:`~None`

.. py:method:: append_run_from_state(self, appendState: IState, clearEphemerisDirection: CLEAR_EPHEMERIS_DIRECTION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.append_run_from_state

    Append the existing ephemeris with another individual segment mode run, starting at a specified state. Ephemeris is cleared from time based on clear direction.

    :Parameters:

    **appendState** : :obj:`~IState`
    **clearEphemerisDirection** : :obj:`~CLEAR_EPHEMERIS_DIRECTION`

    :Returns:

        :obj:`~None`

.. py:method:: run_mission_control_sequence2(self) -> RUN_CODE
    :canonical: ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence.run_mission_control_sequence2

    Run the current MCS and returns an error code.

    :Returns:

        :obj:`~RUN_CODE`


