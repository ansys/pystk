EngineConstAcc
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.EngineConstAcc

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Constant Acceleration engine model.

.. py:currentmodule:: EngineConstAcc

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineConstAcc.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineConstAcc.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineConstAcc.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineConstAcc.g`
              - Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineConstAcc.acceleration`
              - Gets or sets the acceleration for this engine. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineConstAcc.isp`
              - Gets or sets the specific impulse for this engine. Uses SpecificImpulse Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineConstAcc.control_parameters_available`
              - Returns whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import EngineConstAcc


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineConstAcc.g
    :type: float

    Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: acceleration
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineConstAcc.acceleration
    :type: float

    Gets or sets the acceleration for this engine. Uses Acceleration Dimension.

.. py:property:: isp
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineConstAcc.isp
    :type: float

    Gets or sets the specific impulse for this engine. Uses SpecificImpulse Dimension.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineConstAcc.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------







.. py:method:: enable_control_parameter(self, param: CONTROL_ENGINE_CONST_ACC) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineConstAcc.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CONST_ACC`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ENGINE_CONST_ACC) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineConstAcc.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CONST_ACC`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ENGINE_CONST_ACC) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineConstAcc.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CONST_ACC`

    :Returns:

        :obj:`~bool`


