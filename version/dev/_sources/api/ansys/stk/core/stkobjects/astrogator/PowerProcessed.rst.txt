PowerProcessed
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.PowerProcessed

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Power - Processed Power Unit.

.. py:currentmodule:: PowerProcessed

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed.efficiency`
              - Get or set the efficiency of the PPU unit. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed.input_power_source_name`
              - Get or set the source of power available to PPU.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed.load`
              - Get or set the power diverted from power source and unavailable to PPU. Uses Power Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import PowerProcessed


Property detail
---------------

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerProcessed.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerProcessed.efficiency
    :type: float

    Get or set the efficiency of the PPU unit. Dimensionless.

.. py:property:: input_power_source_name
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerProcessed.input_power_source_name
    :type: str

    Get or set the source of power available to PPU.

.. py:property:: load
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerProcessed.load
    :type: float

    Get or set the power diverted from power source and unavailable to PPU. Uses Power Dimension.


Method detail
-------------


.. py:method:: disable_control_parameter(self, param: ControlPowerProcessed) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerProcessed.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlPowerProcessed`


    :Returns:

        :obj:`~None`



.. py:method:: enable_control_parameter(self, param: ControlPowerProcessed) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerProcessed.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlPowerProcessed`


    :Returns:

        :obj:`~None`



.. py:method:: is_control_parameter_enabled(self, param: ControlPowerProcessed) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerProcessed.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlPowerProcessed`


    :Returns:

        :obj:`~bool`



