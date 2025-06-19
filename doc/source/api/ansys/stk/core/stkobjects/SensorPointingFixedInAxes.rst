SensorPointingFixedInAxes
=========================

.. py:class:: ansys.stk.core.stkobjects.SensorPointingFixedInAxes

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPointing`

   Class defining the fixed in axes pointing type for a Sensor.

.. py:currentmodule:: SensorPointingFixedInAxes

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixedInAxes.reference_axes`
              - The reference axes with respect to which the sensor is pointed. The sensor's body axes or any axes dependent upon the sensor's body axes are invalid; all other axes are valid choices for the reference axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixedInAxes.orientation`
              - Get the sensor's orientation properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixedInAxes.available_axes`
              - Get the available Reference Axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixedInAxes.use_reference_axes_flipped_about_x`
              - Use the specified ReferenceAxes, after flipping it 180 deg about its x-axis, as the sensor's body axes. Setting is only available for Facility, Target, Place objects and defaults to true for such objects.



Examples
--------

Define sensor pointing fixed axes YPR

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_ypr("CentralBody/Sun J2000 Axes", YPRAnglesSequence.RYP, 11, 22, 33)


Define sensor pointing fixed axes Quaternion

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_quaternion("CentralBody/Sun J2000 Axes", 0.1, 0.2, 0.3, 0.4)


Define sensor pointing fixed axes Euler

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_euler(
        "CentralBody/Sun J2000 Axes", EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50
    )


Define sensor pointing fixed axes AzEl

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_az_el("CentralBody/Sun J2000 Axes", 11, 22, AzElAboutBoresight.HOLD)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorPointingFixedInAxes


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixedInAxes.reference_axes
    :type: str

    The reference axes with respect to which the sensor is pointed. The sensor's body axes or any axes dependent upon the sensor's body axes are invalid; all other axes are valid choices for the reference axes.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixedInAxes.orientation
    :type: IOrientation

    Get the sensor's orientation properties.

.. py:property:: available_axes
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixedInAxes.available_axes
    :type: list

    Get the available Reference Axes.

.. py:property:: use_reference_axes_flipped_about_x
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixedInAxes.use_reference_axes_flipped_about_x
    :type: bool

    Use the specified ReferenceAxes, after flipping it 180 deg about its x-axis, as the sensor's body axes. Setting is only available for Facility, Target, Place objects and defaults to true for such objects.


