IEngineConstant
===============

.. py:class:: IEngineConstant

   object
   
   Properties for a Constant Thrust and Isp engine model.

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
            * - :py:meth:`~thrust`
            * - :py:meth:`~isp`
            * - :py:meth:`~control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IEngineConstant


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstant.g
    :type: float

    Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: thrust
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstant.thrust
    :type: float

    Gets or sets the thrust for this engine. Uses Force Dimension.

.. py:property:: isp
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstant.isp
    :type: float

    Gets or sets the specific impulse for this engine. Uses SpecificImpulse Dimension.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineConstant.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------







.. py:method:: enable_control_parameter(self, param:"CONTROL_ENGINE_CONSTANT") -> None

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_ENGINE_CONSTANT"`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param:"CONTROL_ENGINE_CONSTANT") -> None

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_ENGINE_CONSTANT"`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param:"CONTROL_ENGINE_CONSTANT") -> bool

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~"CONTROL_ENGINE_CONSTANT"`

    :Returns:

        :obj:`~bool`


