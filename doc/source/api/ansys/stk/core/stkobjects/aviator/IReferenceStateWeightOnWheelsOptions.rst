IReferenceStateWeightOnWheelsOptions
====================================

.. py:class:: IReferenceStateWeightOnWheelsOptions

   object
   
   Interface used to access the weight on wheels options for a reference state procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_longitudinal_accel`
              - Set the longitudinal acceleration.
            * - :py:meth:`~set_lateral_accel`
              - Set the lateral acceleration.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~groundspeed`
            * - :py:meth:`~tas_dot`
            * - :py:meth:`~groundspeed_dot`
            * - :py:meth:`~longitudinal_accel_type`
            * - :py:meth:`~heading`
            * - :py:meth:`~heading_is_magnetic`
            * - :py:meth:`~heading_dot`
            * - :py:meth:`~course_dot`
            * - :py:meth:`~lateral_accel_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IReferenceStateWeightOnWheelsOptions


Property detail
---------------

.. py:property:: groundspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.groundspeed
    :type: float

    Gets or sets the aircraft's speed relative to the ground.

.. py:property:: tas_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.tas_dot
    :type: float

    Get the true airspeed acceleration.

.. py:property:: groundspeed_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.groundspeed_dot
    :type: float

    Get the groundspeed acceleration.

.. py:property:: longitudinal_accel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.longitudinal_accel_type
    :type: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE

    Get the mode to specify the longitudinal acceleration.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.heading
    :type: typing.Any

    Gets or sets the direction the aircraft is pointing.

.. py:property:: heading_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.heading_is_magnetic
    :type: bool

    Opt whether to specify the heading using magnetic North.

.. py:property:: heading_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.heading_dot
    :type: typing.Any

    Get the heading rate of change.

.. py:property:: course_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.course_dot
    :type: typing.Any

    Get the course rate of change.

.. py:property:: lateral_accel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.lateral_accel_type
    :type: REFERENCE_STATE_LATERAL_ACCEL_MODE

    Get the mode to specify the lateral acceleration.


Method detail
-------------






.. py:method:: set_longitudinal_accel(self, accelType: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.set_longitudinal_accel

    Set the longitudinal acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`








.. py:method:: set_lateral_accel(self, accelType: REFERENCE_STATE_LATERAL_ACCEL_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateWeightOnWheelsOptions.set_lateral_accel

    Set the lateral acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LATERAL_ACCEL_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

