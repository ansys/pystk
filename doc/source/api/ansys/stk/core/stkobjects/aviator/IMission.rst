IMission
========

.. py:class:: ansys.stk.core.stkobjects.aviator.IMission

   object
   
   Interface for the mission of an aircraft using the Aviator propagator.

.. py:currentmodule:: IMission

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMission.get_first_invalid_procedure`
              - Get the first invalid procedure in the mission. Calling this method will propagate the mission.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMission.phases`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMission.vehicle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMission.configuration`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMission.wind_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMission.atmosphere_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMission.is_valid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMission


Property detail
---------------

.. py:property:: phases
    :canonical: ansys.stk.core.stkobjects.aviator.IMission.phases
    :type: IPhaseCollection

    Get the mission phases.

.. py:property:: vehicle
    :canonical: ansys.stk.core.stkobjects.aviator.IMission.vehicle
    :type: IAviatorVehicle

    Gets or sets the vehicle used in the mission.

.. py:property:: configuration
    :canonical: ansys.stk.core.stkobjects.aviator.IMission.configuration
    :type: IConfiguration

    Get the aircraft's configuration for the mission.

.. py:property:: wind_model
    :canonical: ansys.stk.core.stkobjects.aviator.IMission.wind_model
    :type: IWindModel

    Get the mission wind model.

.. py:property:: atmosphere_model
    :canonical: ansys.stk.core.stkobjects.aviator.IMission.atmosphere_model
    :type: IAtmosphereModel

    Get the mission atmosphere model.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.aviator.IMission.is_valid
    :type: bool

    Check whether the mission is valid. Calling this property will propagate the mission.


Method detail
-------------








.. py:method:: get_first_invalid_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IMission.get_first_invalid_procedure

    Get the first invalid procedure in the mission. Calling this method will propagate the mission.

    :Returns:

        :obj:`~IProcedure`

