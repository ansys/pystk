StateCalcRepeatingGroundTrackErr
================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   RepeatingGrTrackErr Calc objects.

.. py:currentmodule:: StateCalcRepeatingGroundTrackErr

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.reference_longitude`
              - Get or set the longitude at the equator to be used as a reference for the repeating ground track. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.repeat_count`
              - Get or set the number of orbits before the ground track repeats over the same longitude. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.control_parameters_available`
              - Return whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcRepeatingGroundTrackErr


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: reference_longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.reference_longitude
    :type: typing.Any

    Get or set the longitude at the equator to be used as a reference for the repeating ground track. Uses Angle Dimension.

.. py:property:: repeat_count
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.repeat_count
    :type: float

    Get or set the number of orbits before the ground track repeats over the same longitude. Dimensionless.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.


Method detail
-------------







.. py:method:: enable_control_parameter(self, param: ControlRepeatingGroundTrackErr) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~ControlRepeatingGroundTrackErr`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlRepeatingGroundTrackErr) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~ControlRepeatingGroundTrackErr`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlRepeatingGroundTrackErr) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~ControlRepeatingGroundTrackErr`

    :Returns:

        :obj:`~bool`


