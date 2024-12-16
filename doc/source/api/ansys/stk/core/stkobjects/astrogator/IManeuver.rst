IManeuver
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.IManeuver

   Properties of an Impulsive Maneuver Segment.

.. py:currentmodule:: IManeuver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuver.set_attitude_control_type`
              - Set the attitude control type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuver.set_propulsion_method`
              - Set the propulsion type and associated engine/thruster set.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuver.attitude_control_type`
              - Determines the attitude parameters available for you to specify.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuver.attitude_control`
              - Get the attitude control properties collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuver.propulsion_method`
              - Get the propulsion type to be modeled.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IManeuver.propulsion_method_value`
              - Get the specific engine model or thruster set to be used for the maneuver.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuver


Property detail
---------------

.. py:property:: attitude_control_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.attitude_control_type
    :type: AttitudeControl

    Determines the attitude parameters available for you to specify.

.. py:property:: attitude_control
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.attitude_control
    :type: IAttitudeControl

    Get the attitude control properties collection.

.. py:property:: propulsion_method
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.propulsion_method
    :type: PropulsionMethod

    Get the propulsion type to be modeled.

.. py:property:: propulsion_method_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.propulsion_method_value
    :type: str

    Get the specific engine model or thruster set to be used for the maneuver.


Method detail
-------------


.. py:method:: set_attitude_control_type(self, attitude_control_type: AttitudeControl) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.set_attitude_control_type

    Set the attitude control type.

    :Parameters:

    **attitude_control_type** : :obj:`~AttitudeControl`

    :Returns:

        :obj:`~None`



.. py:method:: set_propulsion_method(self, propulsion_method: PropulsionMethod, value: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.set_propulsion_method

    Set the propulsion type and associated engine/thruster set.

    :Parameters:

    **propulsion_method** : :obj:`~PropulsionMethod`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`


