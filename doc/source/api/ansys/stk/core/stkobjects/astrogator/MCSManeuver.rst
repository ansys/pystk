MCSManeuver
===========

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSManeuver

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Maneuver segment.

.. py:currentmodule:: MCSManeuver

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSManeuver.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSManeuver.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSManeuver.is_control_parameter_enabled`
              - Sees if the specified control is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSManeuver.set_maneuver_type`
              - Set the maneuver type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSManeuver.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSManeuver.maneuver`
              - Get the Maneuver properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSManeuver.maneuver_type`
              - Get the maneuver type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSManeuver


Property detail
---------------

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSManeuver.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSManeuver.maneuver
    :type: IManeuver

    Get the Maneuver properties.

.. py:property:: maneuver_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSManeuver.maneuver_type
    :type: ManeuverType

    Get the maneuver type.


Method detail
-------------


.. py:method:: disable_control_parameter(self, param: ControlManeuver) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSManeuver.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlManeuver`


    :Returns:

        :obj:`~None`

.. py:method:: enable_control_parameter(self, param: ControlManeuver) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSManeuver.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlManeuver`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlManeuver) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSManeuver.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlManeuver`


    :Returns:

        :obj:`~bool`



.. py:method:: set_maneuver_type(self, maneuver_type: ManeuverType) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSManeuver.set_maneuver_type

    Set the maneuver type.

    :Parameters:

        **maneuver_type** : :obj:`~ManeuverType`


    :Returns:

        :obj:`~None`

