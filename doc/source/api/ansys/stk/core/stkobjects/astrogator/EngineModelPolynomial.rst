EngineModelPolynomial
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Polynomial Thrust and Isp engine model.

.. py:currentmodule:: EngineModelPolynomial

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.g`
              - Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.thrust_coefficients`
              - Get the thrust Coefficients.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.isp_coefficients`
              - Get the Isp Coefficients.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.control_parameters_available`
              - Returns whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import EngineModelPolynomial


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.g
    :type: float

    Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: thrust_coefficients
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.thrust_coefficients
    :type: EngineModelThrustCoefficients

    Get the thrust Coefficients.

.. py:property:: isp_coefficients
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.isp_coefficients
    :type: EngineModelIspCoefficients

    Get the Isp Coefficients.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------





.. py:method:: enable_control_parameter(self, param: CONTROL_ENGINE_MODEL_POLYNOMIAL) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_MODEL_POLYNOMIAL`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ENGINE_MODEL_POLYNOMIAL) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_MODEL_POLYNOMIAL`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ENGINE_MODEL_POLYNOMIAL) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_MODEL_POLYNOMIAL`

    :Returns:

        :obj:`~bool`


