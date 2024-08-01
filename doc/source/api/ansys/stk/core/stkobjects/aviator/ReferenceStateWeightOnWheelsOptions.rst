ReferenceStateWeightOnWheelsOptions
===================================

.. py:class:: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions

   Bases: 

   Class defining the Weight on Wheels options for a Reference State procedure.

.. py:currentmodule:: ReferenceStateWeightOnWheelsOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.set_longitudinal_acceleration`
              - Set the longitudinal acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.set_lateral_acceleration`
              - Set the lateral acceleration.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.groundspeed`
              - Gets or sets the aircraft's speed relative to the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.tas_dot`
              - Get the true airspeed acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.groundspeed_dot`
              - Get the groundspeed acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.longitudinal_acceleration_type`
              - Get the mode to specify the longitudinal acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.heading`
              - Gets or sets the direction the aircraft is pointing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.heading_is_magnetic`
              - Opt whether to specify the heading using magnetic North.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.heading_dot`
              - Get the heading rate of change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.course_dot`
              - Get the course rate of change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.lateral_acceleration_type`
              - Get the mode to specify the lateral acceleration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ReferenceStateWeightOnWheelsOptions


Property detail
---------------

.. py:property:: groundspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.groundspeed
    :type: float

    Gets or sets the aircraft's speed relative to the ground.

.. py:property:: tas_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.tas_dot
    :type: float

    Get the true airspeed acceleration.

.. py:property:: groundspeed_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.groundspeed_dot
    :type: float

    Get the groundspeed acceleration.

.. py:property:: longitudinal_acceleration_type
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.longitudinal_acceleration_type
    :type: REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE

    Get the mode to specify the longitudinal acceleration.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.heading
    :type: typing.Any

    Gets or sets the direction the aircraft is pointing.

.. py:property:: heading_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.heading_is_magnetic
    :type: bool

    Opt whether to specify the heading using magnetic North.

.. py:property:: heading_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.heading_dot
    :type: typing.Any

    Get the heading rate of change.

.. py:property:: course_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.course_dot
    :type: typing.Any

    Get the course rate of change.

.. py:property:: lateral_acceleration_type
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.lateral_acceleration_type
    :type: REFERENCE_STATE_LATERAL_ACCELERATION_MODE

    Get the mode to specify the lateral acceleration.


Method detail
-------------






.. py:method:: set_longitudinal_acceleration(self, accelType: REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.set_longitudinal_acceleration

    Set the longitudinal acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`








.. py:method:: set_lateral_acceleration(self, accelType: REFERENCE_STATE_LATERAL_ACCELERATION_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions.set_lateral_acceleration

    Set the lateral acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LATERAL_ACCELERATION_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

