IPowerProcessed
===============

.. py:class:: IPowerProcessed

   object
   
   Properties for the Processed Power power source component.

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

            * - :py:meth:`~load`
            * - :py:meth:`~efficiency`
            * - :py:meth:`~input_power_source_name`
            * - :py:meth:`~control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPowerProcessed


Property detail
---------------

.. py:property:: load
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerProcessed.load
    :type: float

    Gets or sets the power diverted from power source and unavailable to PPU. Uses Power Dimension.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerProcessed.efficiency
    :type: float

    Gets or sets the efficiency of the PPU unit. Dimensionless.

.. py:property:: input_power_source_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerProcessed.input_power_source_name
    :type: str

    Gets or sets the source of power available to PPU.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerProcessed.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------







.. py:method:: enable_control_parameter(self, param:"CONTROL_POWER_PROCESSED") -> None

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_POWER_PROCESSED"`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param:"CONTROL_POWER_PROCESSED") -> None

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_POWER_PROCESSED"`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param:"CONTROL_POWER_PROCESSED") -> bool

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~"CONTROL_POWER_PROCESSED"`

    :Returns:

        :obj:`~bool`


