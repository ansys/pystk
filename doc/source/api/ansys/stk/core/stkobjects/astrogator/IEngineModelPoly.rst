IEngineModelPoly
================

.. py:class:: IEngineModelPoly

   object
   
   Properties for a Polynomial Thrust and Isp engine model.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:meth:`~disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:meth:`~is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~g`
            * - :py:meth:`~thrust_coefficients`
            * - :py:meth:`~isp_coefficients`
            * - :py:meth:`~control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IEngineModelPoly


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineModelPoly.g
    :type: float

    Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: thrust_coefficients
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineModelPoly.thrust_coefficients
    :type: IAgVAEngineModelThrustCoefficients

    Get the thrust Coefficients.

.. py:property:: isp_coefficients
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineModelPoly.isp_coefficients
    :type: IAgVAEngineModelIspCoefficients

    Get the Isp Coefficients.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineModelPoly.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------





.. py:method:: enable_control_parameter(self, param: CONTROL_ENGINE_MODEL_POLY) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineModelPoly.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_MODEL_POLY`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ENGINE_MODEL_POLY) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineModelPoly.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_MODEL_POLY`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ENGINE_MODEL_POLY) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineModelPoly.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_MODEL_POLY`

    :Returns:

        :obj:`~bool`


