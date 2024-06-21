IMissionControlSequenceFollow
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow

   object
   
   Properties for a Follow segment.

.. py:currentmodule:: IMissionControlSequenceFollow

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.leader`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.x_offset`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.y_offset`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.z_offset`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.separation_conditions`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.spacecraft_parameters`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.fuel_tank`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.joining_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.separation_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.spacecraft_and_fuel_tank_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.joining_conditions`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.control_parameters_available`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.user_variables`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceFollow


Property detail
---------------

.. py:property:: leader
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.leader
    :type: ILinkToObject

    Get the leader object.

.. py:property:: x_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.x_offset
    :type: float

    Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the X axis. Uses Distance Dimension.

.. py:property:: y_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.y_offset
    :type: float

    Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the Y axis. Uses Distance Dimension.

.. py:property:: z_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.z_offset
    :type: float

    Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the Z axis. Uses Distance Dimension.

.. py:property:: separation_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.separation_conditions
    :type: IStoppingConditionCollection

    If separation conditions are specified, the list of separation conditions.

.. py:property:: spacecraft_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.spacecraft_parameters
    :type: ISpacecraftParameters

    Get the spacecraft's physical properties.

.. py:property:: fuel_tank
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.fuel_tank
    :type: IFuelTank

    Get the spacecraft's fuel tank properties.

.. py:property:: joining_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.joining_type
    :type: FOLLOW_JOIN

    Gets or sets the joining type.

.. py:property:: separation_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.separation_type
    :type: FOLLOW_SEPARATION

    Gets or sets the separation type.

.. py:property:: spacecraft_and_fuel_tank_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.spacecraft_and_fuel_tank_type
    :type: FOLLOW_SPACECRAFT_AND_FUEL_TANK

    Gets or sets the spacecraft snd fuel tank configuration type.

.. py:property:: joining_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.joining_conditions
    :type: IStoppingConditionCollection

    If joining conditions are specified, the list of joining conditions.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.user_variables
    :type: IUserVariableCollection

    Interface used to modify user variables for the follow segment.


Method detail
-------------


















.. py:method:: enable_control_parameter(self, param: CONTROL_FOLLOW) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_FOLLOW`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_FOLLOW) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_FOLLOW`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_FOLLOW) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_FOLLOW`

    :Returns:

        :obj:`~bool`



