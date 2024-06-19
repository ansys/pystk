IRefuelDumpProperties
=====================

.. py:class:: IRefuelDumpProperties

   object
   
   Interface used to access the refuel/dump properties for the current procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_refuel_dump_mode`
              - Set RefuelDumpMode and RefuelDumpModeValue if applicable.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~refuel_dump_mode`
            * - :py:meth:`~refuel_dump_mode_value`
            * - :py:meth:`~refuel_dump_rate`
            * - :py:meth:`~refuel_dump_time_offset`
            * - :py:meth:`~can_use_end_of_enroute_segment_as_epoch`
            * - :py:meth:`~use_end_of_enroute_segment_as_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IRefuelDumpProperties


Property detail
---------------

.. py:property:: refuel_dump_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IRefuelDumpProperties.refuel_dump_mode
    :type: REFUEL_DUMP_MODE

    Get the RefuelDumpMode.

.. py:property:: refuel_dump_mode_value
    :canonical: ansys.stk.core.stkobjects.aviator.IRefuelDumpProperties.refuel_dump_mode_value
    :type: float

    Get the RefuelDumpModeValue if applicable.

.. py:property:: refuel_dump_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IRefuelDumpProperties.refuel_dump_rate
    :type: float

    Gets or sets the RefuelDump rate.

.. py:property:: refuel_dump_time_offset
    :canonical: ansys.stk.core.stkobjects.aviator.IRefuelDumpProperties.refuel_dump_time_offset
    :type: float

    Gets or sets the RefuelDump time offset.

.. py:property:: can_use_end_of_enroute_segment_as_epoch
    :canonical: ansys.stk.core.stkobjects.aviator.IRefuelDumpProperties.can_use_end_of_enroute_segment_as_epoch
    :type: bool

    Can use end of enroute segment as the epoch.

.. py:property:: use_end_of_enroute_segment_as_epoch
    :canonical: ansys.stk.core.stkobjects.aviator.IRefuelDumpProperties.use_end_of_enroute_segment_as_epoch
    :type: bool

    Use end of enroute segment as the epoch.


Method detail
-------------



.. py:method:: set_refuel_dump_mode(self, mode: REFUEL_DUMP_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IRefuelDumpProperties.set_refuel_dump_mode

    Set RefuelDumpMode and RefuelDumpModeValue if applicable.

    :Parameters:

    **mode** : :obj:`~REFUEL_DUMP_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`








