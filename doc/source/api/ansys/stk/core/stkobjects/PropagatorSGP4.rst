PropagatorSGP4
==============

.. py:class:: ansys.stk.core.stkobjects.PropagatorSGP4

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the SGP4 propagator.

.. py:currentmodule:: PropagatorSGP4

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.segments`
              - Get the element set list.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.automatic_update_enabled`
              - Whether automatic update is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.automatic_update_settings`
              - Allow configuring the auto-update parameters and settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.common_tasks`
              - Most commonly used tasks such as importing file data, etc.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.settings`
              - Propagator settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4.international_designator`
              - International designation of the satellite.



Examples
--------

Set satellite propagator to SGP4 and propagate

.. code-block:: python

    # Satellite satellite: Satellite object
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.ephemeris_interval.set_implicit_interval(
        root.current_scenario.analysis_workbench_components.time_intervals.item("AnalysisInterval")
    )  # Link to scenario period
    propagator.common_tasks.add_segments_from_online_source("25544")  # International Space Station
    propagator.automatic_update_enabled = True
    propagator.propagate()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSGP4


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.segments
    :type: PropagatorSGP4SegmentCollection

    Get the element set list.

.. py:property:: automatic_update_enabled
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.automatic_update_enabled
    :type: bool

    Whether automatic update is enabled.

.. py:property:: automatic_update_settings
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.automatic_update_settings
    :type: PropagatorSGP4AutoUpdate

    Allow configuring the auto-update parameters and settings.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.common_tasks
    :type: PropagatorSGP4CommonTasks

    Most commonly used tasks such as importing file data, etc.

.. py:property:: settings
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.settings
    :type: PropagatorSGP4PropagatorSettings

    Propagator settings.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: international_designator
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.international_designator
    :type: str

    International designation of the satellite.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`












