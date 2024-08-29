RefuelDumpProperties
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.RefuelDumpProperties

   Class defining the refuel/dump properties for the current procedure.

.. py:currentmodule:: RefuelDumpProperties

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.set_refuel_dump_mode`
              - Set RefuelDumpMode and RefuelDumpModeValue if applicable.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.refuel_dump_mode`
              - Get the RefuelDumpMode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.refuel_dump_mode_value`
              - Get the RefuelDumpModeValue if applicable.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.refuel_dump_rate`
              - Gets or sets the RefuelDump rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.refuel_dump_time_offset`
              - Gets or sets the RefuelDump time offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.can_use_end_of_enroute_segment_as_epoch`
              - Can use end of enroute segment as the epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.use_end_of_enroute_segment_as_epoch`
              - Use end of enroute segment as the epoch.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import RefuelDumpProperties


Property detail
---------------

.. py:property:: refuel_dump_mode
    :canonical: ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.refuel_dump_mode
    :type: REFUEL_DUMP_MODE

    Get the RefuelDumpMode.

.. py:property:: refuel_dump_mode_value
    :canonical: ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.refuel_dump_mode_value
    :type: float

    Get the RefuelDumpModeValue if applicable.

.. py:property:: refuel_dump_rate
    :canonical: ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.refuel_dump_rate
    :type: float

    Gets or sets the RefuelDump rate.

.. py:property:: refuel_dump_time_offset
    :canonical: ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.refuel_dump_time_offset
    :type: float

    Gets or sets the RefuelDump time offset.

.. py:property:: can_use_end_of_enroute_segment_as_epoch
    :canonical: ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.can_use_end_of_enroute_segment_as_epoch
    :type: bool

    Can use end of enroute segment as the epoch.

.. py:property:: use_end_of_enroute_segment_as_epoch
    :canonical: ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.use_end_of_enroute_segment_as_epoch
    :type: bool

    Use end of enroute segment as the epoch.


Method detail
-------------



.. py:method:: set_refuel_dump_mode(self, mode: REFUEL_DUMP_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.RefuelDumpProperties.set_refuel_dump_mode

    Set RefuelDumpMode and RefuelDumpModeValue if applicable.

    :Parameters:

    **mode** : :obj:`~REFUEL_DUMP_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`








