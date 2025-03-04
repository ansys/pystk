SensorPointingFixed
===================

.. py:class:: ansys.stk.core.stkobjects.SensorPointingFixed

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPointing`

   Class defining the fixed pointing type for a Sensor.

.. py:currentmodule:: SensorPointingFixed

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixed.orientation`
              - Get the sensor's orientation properties.



Examples
--------

Define sensor pointing fixed YPR

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_ypr(YPRAnglesSequence.RPY, 12, 24, 36)


Define sensor pointing fixed Quaternion

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_quaternion(0.1, 0.2, 0.3, 0.4)


Define sensor pointing fixed Euler

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_euler(EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50)


Define sensor pointing fixed AzEl

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_az_el(4.5, -45.0, AzElAboutBoresight.ROTATE)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorPointingFixed


Property detail
---------------

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixed.orientation
    :type: IOrientation

    Get the sensor's orientation properties.


