MCSDriver
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSDriver

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IPropagator`

   Basic properties of an Astrogator satellite.

.. py:currentmodule:: MCSDriver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.run_mcs`
              - Run the current MCS.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.begin_run`
              - Begins an individual segment mode run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.end_run`
              - End an individual segment mode run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.clear_draw_while_calculating_graphics`
              - Clear the draw while calculating graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.reset_all_profiles`
              - Reset all active profiles in all target sequences.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.apply_all_profile_changes`
              - Apply all active profile changes in all target sequences.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.append_run`
              - Append the existing ephemeris with another individual segment mode run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.append_run_from_time`
              - Append the existing ephemeris with another individual segment mode run, starting at a specified time. Ephemeris is cleared from time based on clear direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.append_run_from_state`
              - Append the existing ephemeris with another individual segment mode run, starting at a specified state. Ephemeris is cleared from time based on clear direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.run_mcs2`
              - Run the current MCS and returns an error code.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.main_sequence`
              - Get the Mission Control Sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.options`
              - Get the Mission Control Sequence options.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.auto_sequence`
              - Get the Automatic Sequences.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSDriver.calculation_graphs`
              - Get the calculation graphs.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSDriver


Property detail
---------------

.. py:property:: main_sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.main_sequence
    :type: MCSSegmentCollection

    Get the Mission Control Sequence.

.. py:property:: options
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.options
    :type: MCSOptions

    Get the Mission Control Sequence options.

.. py:property:: auto_sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.auto_sequence
    :type: AutomaticSequenceCollection

    Get the Automatic Sequences.

.. py:property:: calculation_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.calculation_graphs
    :type: CalculationGraphCollection

    Get the calculation graphs.


Method detail
-------------




.. py:method:: run_mcs(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.run_mcs

    Run the current MCS.

    :Returns:

        :obj:`~None`

.. py:method:: begin_run(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.begin_run

    Begins an individual segment mode run.

    :Returns:

        :obj:`~None`

.. py:method:: end_run(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.end_run

    End an individual segment mode run.

    :Returns:

        :obj:`~None`

.. py:method:: clear_draw_while_calculating_graphics(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.clear_draw_while_calculating_graphics

    Clear the draw while calculating graphics.

    :Returns:

        :obj:`~None`

.. py:method:: reset_all_profiles(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.reset_all_profiles

    Reset all active profiles in all target sequences.

    :Returns:

        :obj:`~None`

.. py:method:: apply_all_profile_changes(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.apply_all_profile_changes

    Apply all active profile changes in all target sequences.

    :Returns:

        :obj:`~None`

.. py:method:: append_run(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.append_run

    Append the existing ephemeris with another individual segment mode run.

    :Returns:

        :obj:`~None`

.. py:method:: append_run_from_time(self, epoch: typing.Any, clear_ephemeris_direction: CLEAR_EPHEMERIS_DIRECTION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.append_run_from_time

    Append the existing ephemeris with another individual segment mode run, starting at a specified time. Ephemeris is cleared from time based on clear direction.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **clear_ephemeris_direction** : :obj:`~CLEAR_EPHEMERIS_DIRECTION`

    :Returns:

        :obj:`~None`

.. py:method:: append_run_from_state(self, append_state: State, clear_ephemeris_direction: CLEAR_EPHEMERIS_DIRECTION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.append_run_from_state

    Append the existing ephemeris with another individual segment mode run, starting at a specified state. Ephemeris is cleared from time based on clear direction.

    :Parameters:

    **append_state** : :obj:`~State`
    **clear_ephemeris_direction** : :obj:`~CLEAR_EPHEMERIS_DIRECTION`

    :Returns:

        :obj:`~None`

.. py:method:: run_mcs2(self) -> RUN_CODE
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSDriver.run_mcs2

    Run the current MCS and returns an error code.

    :Returns:

        :obj:`~RUN_CODE`


