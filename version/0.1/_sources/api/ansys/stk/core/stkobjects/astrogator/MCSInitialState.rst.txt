MCSInitialState
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSInitialState

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Initial State segment.

.. py:currentmodule:: MCSInitialState

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.set_element_type`
              - Select an coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.enable_control_parameter`
              - Enable a control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.disable_control_parameter`
              - Disables a control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.is_control_parameter_enabled`
              - Sees if a control is enabled.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.coord_system_name`
              - Get or set the coordinate system.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.orbit_epoch`
              - Get or set the orbit epoch. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.spacecraft_parameters`
              - Get the spacecraft  parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.fuel_tank`
              - Get the fuel tank parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.element_type`
              - Get the coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.element`
              - Get the elements of the selected coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState.user_variables`
              - Interface used to modify user variables for the initial state segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSInitialState


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.coord_system_name
    :type: str

    Get or set the coordinate system.

.. py:property:: orbit_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.orbit_epoch
    :type: typing.Any

    Get or set the orbit epoch. Uses DateFormat Dimension.

.. py:property:: spacecraft_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.spacecraft_parameters
    :type: SpacecraftParameters

    Get the spacecraft  parameters.

.. py:property:: fuel_tank
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.fuel_tank
    :type: FuelTank

    Get the fuel tank parameters.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.element_type
    :type: ElementSetType

    Get the coordinate type.

.. py:property:: element
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.element
    :type: IElement

    Get the elements of the selected coordinate type.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.user_variables
    :type: UserVariableCollection

    Interface used to modify user variables for the initial state segment.


Method detail
-------------








.. py:method:: set_element_type(self, element_type: ElementSetType) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.set_element_type

    Select an coordinate type.

    :Parameters:

        **element_type** : :obj:`~ElementSetType`


    :Returns:

        :obj:`~None`


.. py:method:: enable_control_parameter(self, param: ControlInitState) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.enable_control_parameter

    Enable a control parameter.

    :Parameters:

        **param** : :obj:`~ControlInitState`


    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlInitState) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.disable_control_parameter

    Disables a control parameter.

    :Parameters:

        **param** : :obj:`~ControlInitState`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlInitState) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSInitialState.is_control_parameter_enabled

    Sees if a control is enabled.

    :Parameters:

        **param** : :obj:`~ControlInitState`


    :Returns:

        :obj:`~bool`



