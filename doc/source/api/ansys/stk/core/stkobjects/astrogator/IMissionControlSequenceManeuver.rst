IMissionControlSequenceManeuver
===============================

.. py:class:: IMissionControlSequenceManeuver

   object
   
   General properties for a Maneuver segment.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_maneuver_type`
              - Set the maneuver type.
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

            * - :py:meth:`~maneuver_type`
            * - :py:meth:`~maneuver`
            * - :py:meth:`~control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceManeuver


Property detail
---------------

.. py:property:: maneuver_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceManeuver.maneuver_type
    :type: "MANEUVER_TYPE"

    Get the maneuver type.

.. py:property:: maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceManeuver.maneuver
    :type: "IAgVAManeuver"

    Get the Maneuver properties.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceManeuver.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------


.. py:method:: set_maneuver_type(self, maneuverType:"MANEUVER_TYPE") -> None

    Set the maneuver type.

    :Parameters:

    **maneuverType** : :obj:`~"MANEUVER_TYPE"`

    :Returns:

        :obj:`~None`


.. py:method:: enable_control_parameter(self, param:"CONTROL_MANEUVER") -> None

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_MANEUVER"`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param:"CONTROL_MANEUVER") -> None

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_MANEUVER"`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param:"CONTROL_MANEUVER") -> bool

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~"CONTROL_MANEUVER"`

    :Returns:

        :obj:`~bool`


