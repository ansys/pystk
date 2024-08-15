MissionControlSequenceManeuver
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Maneuver segment.

.. py:currentmodule:: MissionControlSequenceManeuver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.set_maneuver_type`
              - Set the maneuver type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.maneuver_type`
              - Get the maneuver type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.maneuver`
              - Get the Maneuver properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.control_parameters_available`
              - Returns whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MissionControlSequenceManeuver


Property detail
---------------

.. py:property:: maneuver_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.maneuver_type
    :type: MANEUVER_TYPE

    Get the maneuver type.

.. py:property:: maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.maneuver
    :type: IManeuver

    Get the Maneuver properties.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------


.. py:method:: set_maneuver_type(self, maneuverType: MANEUVER_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.set_maneuver_type

    Set the maneuver type.

    :Parameters:

    **maneuverType** : :obj:`~MANEUVER_TYPE`

    :Returns:

        :obj:`~None`


.. py:method:: enable_control_parameter(self, param: CONTROL_MANEUVER) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_MANEUVER`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_MANEUVER) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_MANEUVER`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_MANEUVER) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_MANEUVER`

    :Returns:

        :obj:`~bool`


