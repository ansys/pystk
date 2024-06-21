IEngineConstAcc
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.IEngineConstAcc

   object
   
   Properties for a Constant Acceleration and Isp engine model.

.. py:currentmodule:: IEngineConstAcc

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.g`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.acceleration`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.isp`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IEngineConstAcc


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.g
    :type: float

    Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: acceleration
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.acceleration
    :type: float

    Gets or sets the acceleration for this engine. Uses Acceleration Dimension.

.. py:property:: isp
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.isp
    :type: float

    Gets or sets the specific impulse for this engine. Uses SpecificImpulse Dimension.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------







.. py:method:: enable_control_parameter(self, param: CONTROL_ENGINE_CONST_ACC) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CONST_ACC`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ENGINE_CONST_ACC) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CONST_ACC`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ENGINE_CONST_ACC) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstAcc.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CONST_ACC`

    :Returns:

        :obj:`~bool`


