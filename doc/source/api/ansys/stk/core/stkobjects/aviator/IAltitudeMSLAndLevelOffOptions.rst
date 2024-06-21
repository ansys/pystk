IAltitudeMSLAndLevelOffOptions
==============================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions

   object
   
   Interface used to access the altitude MSL and Level off options for an Aviator procedure.

.. py:currentmodule:: IAltitudeMSLAndLevelOffOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions.use_default_cruise_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions.msl_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions.must_level_off`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions.level_off_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAltitudeMSLAndLevelOffOptions


Property detail
---------------

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: msl_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions.msl_altitude
    :type: float

    Get the MSL altitude. Can only be used when the option to use the default cruise altitude is off.

.. py:property:: must_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions.must_level_off
    :type: bool

    Opt whether the procedure must level off.

.. py:property:: level_off_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeMSLAndLevelOffOptions.level_off_mode
    :type: ALTITUDE_CONSTRAINT_MANEUVER_MODE

    Gets or sets the level off mode. This is only used when the must level off option is on.


