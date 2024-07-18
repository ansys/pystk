SensorPointingFixedAxes
=======================

.. py:class:: ansys.stk.core.stkobjects.SensorPointingFixedAxes

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPointing`

   Class defining the fixed in axes pointing type for a Sensor.

.. py:currentmodule:: SensorPointingFixedAxes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixedAxes.reference_axes`
              - The reference axes with respect to which the sensor is pointed. The sensor's body axes or any axes dependent upon the sensor's body axes are invalid; all other axes are valid choices for the reference axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixedAxes.orientation`
              - Get the sensor's orientation properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixedAxes.available_axes`
              - Get the available Reference Axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingFixedAxes.use_reference_axes_flipped_about_x`
              - Use the specified ReferenceAxes, after flipping it 180 deg about its x-axis, as the sensor's body axes. Setting is only available for Facility, Target, Place objects and defaults to true for such objects.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorPointingFixedAxes


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixedAxes.reference_axes
    :type: str

    The reference axes with respect to which the sensor is pointed. The sensor's body axes or any axes dependent upon the sensor's body axes are invalid; all other axes are valid choices for the reference axes.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixedAxes.orientation
    :type: IOrientation

    Get the sensor's orientation properties.

.. py:property:: available_axes
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixedAxes.available_axes
    :type: list

    Get the available Reference Axes.

.. py:property:: use_reference_axes_flipped_about_x
    :canonical: ansys.stk.core.stkobjects.SensorPointingFixedAxes.use_reference_axes_flipped_about_x
    :type: bool

    Use the specified ReferenceAxes, after flipping it 180 deg about its x-axis, as the sensor's body axes. Setting is only available for Facility, Target, Place objects and defaults to true for such objects.


