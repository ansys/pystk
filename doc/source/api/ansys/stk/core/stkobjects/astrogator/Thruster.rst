Thruster
========

.. py:class:: ansys.stk.core.stkobjects.astrogator.Thruster

   Bases: 

   Thruster definition.

.. py:currentmodule:: Thruster

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.copy`
              - Make a copy of the specified thruster.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.name`
              - Gets or sets the thruster name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.user_comment`
              - A user comment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.engine_model_name`
              - Gets or sets the engine model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.thruster_efficiency`
              - Gets or sets the thruster efficiency. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.equivalent_on_time`
              - Gets or sets the equivalent on-time percentage is a factor multiplied by the thrust. The thrust is applied continuously throughout the maneuver and is reduced by the percentage. The mass flow rate is likewise reduced. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.thruster_direction`
              - A thruster direction value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.Thruster.control_parameters_available`
              - Returns whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import Thruster


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.name
    :type: str

    Gets or sets the thruster name.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.user_comment
    :type: str

    A user comment.

.. py:property:: engine_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.engine_model_name
    :type: str

    Gets or sets the engine model.

.. py:property:: thruster_efficiency
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.thruster_efficiency
    :type: float

    Gets or sets the thruster efficiency. Dimensionless.

.. py:property:: equivalent_on_time
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.equivalent_on_time
    :type: float

    Gets or sets the equivalent on-time percentage is a factor multiplied by the thrust. The thrust is applied continuously throughout the maneuver and is reduced by the percentage. The mass flow rate is likewise reduced. Dimensionless.

.. py:property:: thruster_direction
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.thruster_direction
    :type: IDirection

    A thruster direction value.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------





.. py:method:: copy(self) -> Thruster
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.copy

    Make a copy of the specified thruster.

    :Returns:

        :obj:`~Thruster`








.. py:method:: enable_control_parameter(self, param: CONTROL_THRUSTERS) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_THRUSTERS`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_THRUSTERS) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_THRUSTERS`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_THRUSTERS) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.Thruster.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_THRUSTERS`

    :Returns:

        :obj:`~bool`


