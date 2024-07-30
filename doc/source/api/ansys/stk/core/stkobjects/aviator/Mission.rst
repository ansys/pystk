Mission
=======

.. py:class:: ansys.stk.core.stkobjects.aviator.Mission

   Bases: 

   Class defining the Aviator mission.

.. py:currentmodule:: Mission

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.get_first_invalid_procedure`
              - Get the first invalid procedure in the mission. Calling this method will propagate the mission.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.phases`
              - Get the mission phases.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.vehicle`
              - Gets or sets the vehicle used in the mission.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.configuration`
              - Get the aircraft's configuration for the mission.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.wind_model`
              - Get the mission wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.atmosphere_model`
              - Get the mission atmosphere model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Mission.is_valid`
              - Check whether the mission is valid. Calling this property will propagate the mission.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import Mission


Property detail
---------------

.. py:property:: phases
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.phases
    :type: IPhaseCollection

    Get the mission phases.

.. py:property:: vehicle
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.vehicle
    :type: IAviatorVehicle

    Gets or sets the vehicle used in the mission.

.. py:property:: configuration
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.configuration
    :type: IConfiguration

    Get the aircraft's configuration for the mission.

.. py:property:: wind_model
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.wind_model
    :type: IWindModel

    Get the mission wind model.

.. py:property:: atmosphere_model
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.atmosphere_model
    :type: IAtmosphereModel

    Get the mission atmosphere model.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.is_valid
    :type: bool

    Check whether the mission is valid. Calling this property will propagate the mission.


Method detail
-------------








.. py:method:: get_first_invalid_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.Mission.get_first_invalid_procedure

    Get the first invalid procedure in the mission. Calling this method will propagate the mission.

    :Returns:

        :obj:`~IProcedure`

