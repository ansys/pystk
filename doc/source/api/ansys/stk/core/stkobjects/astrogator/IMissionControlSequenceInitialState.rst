IMissionControlSequenceInitialState
===================================

.. py:class:: IMissionControlSequenceInitialState

   object
   
   Properties for an Initial State segment.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_element_type`
              - Select an coordinate type.
            * - :py:meth:`~enable_control_parameter`
              - Enable a control parameter.
            * - :py:meth:`~disable_control_parameter`
              - Disables a control parameter.
            * - :py:meth:`~is_control_parameter_enabled`
              - Sees if a control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~coord_system_name`
            * - :py:meth:`~orbit_epoch`
            * - :py:meth:`~spacecraft_parameters`
            * - :py:meth:`~fuel_tank`
            * - :py:meth:`~element_type`
            * - :py:meth:`~element`
            * - :py:meth:`~control_parameters_available`
            * - :py:meth:`~user_variables`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceInitialState


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.coord_system_name
    :type: str

    Gets or sets the coordinate system.

.. py:property:: orbit_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.orbit_epoch
    :type: typing.Any

    Gets or sets the orbit epoch. Uses DateFormat Dimension.

.. py:property:: spacecraft_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.spacecraft_parameters
    :type: IAgVASpacecraftParameters

    Get the spacecraft  parameters.

.. py:property:: fuel_tank
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.fuel_tank
    :type: IAgVAFuelTank

    Get the fuel tank parameters.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.element_type
    :type: ELEMENT_TYPE

    Get the coordinate type.

.. py:property:: element
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.element
    :type: IAgVAElement

    Get the elements of the selected coordinate type.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.user_variables
    :type: IAgVAUserVariableCollection

    Interface used to modify user variables for the initial state segment.


Method detail
-------------








.. py:method:: set_element_type(self, elementType: ELEMENT_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.set_element_type

    Select an coordinate type.

    :Parameters:

    **elementType** : :obj:`~ELEMENT_TYPE`

    :Returns:

        :obj:`~None`


.. py:method:: enable_control_parameter(self, param: CONTROL_INIT_STATE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.enable_control_parameter

    Enable a control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_INIT_STATE`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_INIT_STATE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.disable_control_parameter

    Disables a control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_INIT_STATE`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_INIT_STATE) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState.is_control_parameter_enabled

    Sees if a control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_INIT_STATE`

    :Returns:

        :obj:`~bool`



