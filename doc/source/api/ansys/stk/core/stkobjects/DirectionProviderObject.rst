DirectionProviderObject
=======================

.. py:class:: ansys.stk.core.stkobjects.DirectionProviderObject

   Bases: :py:class:`~ansys.stk.core.stkobjects.IDirectionProvider`

   Class defining an object direction provider.

.. py:currentmodule:: DirectionProviderObject

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.directions`
              - Gets the beam steering list.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.enabled`
              - Gets or set the option for enabling steering.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.limits_exceeded_behavior_type`
              - Gets or sets the Limits Exceeded Behavior type.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.use_default_direction`
              - Gets or set the option to use default direction when there are zero objects in the field of view.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.azimuth_steering_limit_a`
              - Gets or sets Azimuth Steering Limit A.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.azimuth_steering_limit_b`
              - Gets or sets Azimuth Steering Limit B.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.elevation_steering_limit_a`
              - Gets or sets Elevation Steering Limit A.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.elevation_steering_limit_b`
              - Gets or sets Elevation Steering Limit B.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.maximum_selection_count`
              - Gets or sets the maximum number of targets to select for beam steering.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.target_selection_method_type`
              - Gets or sets the method type used to determin which targets are selected for steering.
            * - :py:attr:`~ansys.stk.core.stkobjects.DirectionProviderObject.target_selection_method`
              - Gets the target selection method.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DirectionProviderObject


Property detail
---------------

.. py:property:: directions
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.directions
    :type: ObjectLinkCollection

    Gets the beam steering list.

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.enabled
    :type: bool

    Gets or set the option for enabling steering.

.. py:property:: limits_exceeded_behavior_type
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.limits_exceeded_behavior_type
    :type: LIMITS_EXCEEDED_BEHAVIOR_TYPE

    Gets or sets the Limits Exceeded Behavior type.

.. py:property:: use_default_direction
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.use_default_direction
    :type: bool

    Gets or set the option to use default direction when there are zero objects in the field of view.

.. py:property:: azimuth_steering_limit_a
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.azimuth_steering_limit_a
    :type: float

    Gets or sets Azimuth Steering Limit A.

.. py:property:: azimuth_steering_limit_b
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.azimuth_steering_limit_b
    :type: float

    Gets or sets Azimuth Steering Limit B.

.. py:property:: elevation_steering_limit_a
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.elevation_steering_limit_a
    :type: float

    Gets or sets Elevation Steering Limit A.

.. py:property:: elevation_steering_limit_b
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.elevation_steering_limit_b
    :type: float

    Gets or sets Elevation Steering Limit B.

.. py:property:: maximum_selection_count
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.maximum_selection_count
    :type: int

    Gets or sets the maximum number of targets to select for beam steering.

.. py:property:: target_selection_method_type
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.target_selection_method_type
    :type: TARGET_SELECTION_METHOD_TYPE

    Gets or sets the method type used to determin which targets are selected for steering.

.. py:property:: target_selection_method
    :canonical: ansys.stk.core.stkobjects.DirectionProviderObject.target_selection_method
    :type: ITargetSelectionMethod

    Gets the target selection method.


