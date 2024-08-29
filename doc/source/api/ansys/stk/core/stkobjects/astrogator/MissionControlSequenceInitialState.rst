MissionControlSequenceInitialState
==================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Initial State segment.

.. py:currentmodule:: MissionControlSequenceInitialState

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.set_element_type`
              - Select an coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.enable_control_parameter`
              - Enable a control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.disable_control_parameter`
              - Disables a control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.is_control_parameter_enabled`
              - Sees if a control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.coord_system_name`
              - Gets or sets the coordinate system.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.orbit_epoch`
              - Gets or sets the orbit epoch. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.spacecraft_parameters`
              - Get the spacecraft  parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.fuel_tank`
              - Get the fuel tank parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.element_type`
              - Get the coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.element`
              - Get the elements of the selected coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.control_parameters_available`
              - Returns whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.user_variables`
              - Interface used to modify user variables for the initial state segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MissionControlSequenceInitialState


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.coord_system_name
    :type: str

    Gets or sets the coordinate system.

.. py:property:: orbit_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.orbit_epoch
    :type: typing.Any

    Gets or sets the orbit epoch. Uses DateFormat Dimension.

.. py:property:: spacecraft_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.spacecraft_parameters
    :type: SpacecraftParameters

    Get the spacecraft  parameters.

.. py:property:: fuel_tank
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.fuel_tank
    :type: FuelTank

    Get the fuel tank parameters.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.element_type
    :type: ELEMENT_TYPE

    Get the coordinate type.

.. py:property:: element
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.element
    :type: IElement

    Get the elements of the selected coordinate type.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.user_variables
    :type: UserVariableCollection

    Interface used to modify user variables for the initial state segment.


Method detail
-------------








.. py:method:: set_element_type(self, elementType: ELEMENT_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.set_element_type

    Select an coordinate type.

    :Parameters:

    **elementType** : :obj:`~ELEMENT_TYPE`

    :Returns:

        :obj:`~None`


.. py:method:: enable_control_parameter(self, param: CONTROL_INIT_STATE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.enable_control_parameter

    Enable a control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_INIT_STATE`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_INIT_STATE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.disable_control_parameter

    Disables a control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_INIT_STATE`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_INIT_STATE) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState.is_control_parameter_enabled

    Sees if a control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_INIT_STATE`

    :Returns:

        :obj:`~bool`



