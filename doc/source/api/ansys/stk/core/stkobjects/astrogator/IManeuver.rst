IManeuver
=========

.. py:class:: IManeuver

   object
   
   Properties of an Impulsive Maneuver Segment.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_attitude_control_type`
              - Set the attitude control type.
            * - :py:meth:`~set_propulsion_method`
              - Set the propulsion type and associated engine/thruster set.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~attitude_control_type`
            * - :py:meth:`~attitude_control`
            * - :py:meth:`~propulsion_method`
            * - :py:meth:`~propulsion_method_value`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuver


Property detail
---------------

.. py:property:: attitude_control_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.attitude_control_type
    :type: ATTITUDE_CONTROL

    Determines the attitude parameters available for you to specify.

.. py:property:: attitude_control
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.attitude_control
    :type: IAgVAAttitudeControl

    Get the attitude control properties collection.

.. py:property:: propulsion_method
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.propulsion_method
    :type: PROPULSION_METHOD

    Get the propulsion type to be modeled.

.. py:property:: propulsion_method_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.propulsion_method_value
    :type: str

    Get the specific engine model or thruster set to be used for the maneuver.


Method detail
-------------


.. py:method:: set_attitude_control_type(self, attitudeControlType: ATTITUDE_CONTROL) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.set_attitude_control_type

    Set the attitude control type.

    :Parameters:

    **attitudeControlType** : :obj:`~ATTITUDE_CONTROL`

    :Returns:

        :obj:`~None`



.. py:method:: set_propulsion_method(self, propulsionMethod: PROPULSION_METHOD, value: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuver.set_propulsion_method

    Set the propulsion type and associated engine/thruster set.

    :Parameters:

    **propulsionMethod** : :obj:`~PROPULSION_METHOD`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`


