IStoppingCondition
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStoppingCondition

   IStoppingConditionComponent
   
   Basic properties for a stopping condition.

.. py:currentmodule:: IStoppingCondition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.copy_user_calc_object_to_clipboard`
              - Copy the user-defined stopping condition calc object to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.paste_user_calc_object_from_clipboard`
              - Replace the user-defined stopping condition calc object with the calc object in the clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.trip`
              - Gets or sets the desired value - the value at which the condition will be satisfied. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.tolerance`
              - Gets or sets the desired tolerance for achieving the stopping condition. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.repeat_count`
              - Gets or sets the number of times the condition must be satisfied before the propagation ends or moves on to the designated automatic sequence. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.inherited`
              - Condition Inherited by Automatic Sequences - if true, the stopping condition will be applied to any automatic sequences activated within the same segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.max_trip_times`
              - Gets or sets the maximum number of times that the stopping condition will be applied - and any resulting automatic sequences executed. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.coord_system`
              - Gets or sets the coordinate system. The default coordinate system of a stopping condition is Earth Inertial.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.sequence`
              - Gets or sets the automatic sequence to trigger if the highlighted stopping condition is satisfied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.constraints`
              - Further conditions that must be met in order for the stopping condition to be deemed satisfied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.user_calc_object_name`
              - User Calc Object - a User Calculation Object for the highlighted stopping condition. For user-defined stopping conditions, use this field to specify what kind of value you want to stop on.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.user_calc_object`
              - A User Calculation Object for the highlighted stopping condition. For user-defined stopping conditions, use this field to specify what kind of value you want to stop on.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.central_body_name`
              - Gets or sets the central body. The default central body of a stopping condition is the Earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.criterion`
              - Specifies the direction from which the stopping condition value must be achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.before_conditions`
              - A 'before' stopping condition is used to define a stopping condition that depends on two events. Astrogator will ignore a stopping condition until its 'before' conditions are met. Astrogator then interpolates backwards to the normal stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.dimension`
              - Get the dimension of the stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.reference_point`
              - Gets or sets the reference point used for calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition.user_calc_object_link_embed_control`
              - Gets the link / embed controller for managing the user calc. object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStoppingCondition


Property detail
---------------

.. py:property:: trip
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.trip
    :type: typing.Any

    Gets or sets the desired value - the value at which the condition will be satisfied. Dimension depends on context.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.tolerance
    :type: float

    Gets or sets the desired tolerance for achieving the stopping condition. Dimension depends on context.

.. py:property:: repeat_count
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.repeat_count
    :type: float

    Gets or sets the number of times the condition must be satisfied before the propagation ends or moves on to the designated automatic sequence. Dimensionless.

.. py:property:: inherited
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.inherited
    :type: bool

    Condition Inherited by Automatic Sequences - if true, the stopping condition will be applied to any automatic sequences activated within the same segment.

.. py:property:: max_trip_times
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.max_trip_times
    :type: float

    Gets or sets the maximum number of times that the stopping condition will be applied - and any resulting automatic sequences executed. Dimensionless.

.. py:property:: coord_system
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.coord_system
    :type: str

    Gets or sets the coordinate system. The default coordinate system of a stopping condition is Earth Inertial.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.sequence
    :type: str

    Gets or sets the automatic sequence to trigger if the highlighted stopping condition is satisfied.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.constraints
    :type: IConstraintCollection

    Further conditions that must be met in order for the stopping condition to be deemed satisfied.

.. py:property:: user_calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.user_calc_object_name
    :type: str

    User Calc Object - a User Calculation Object for the highlighted stopping condition. For user-defined stopping conditions, use this field to specify what kind of value you want to stop on.

.. py:property:: user_calc_object
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.user_calc_object
    :type: IComponentInfo

    A User Calculation Object for the highlighted stopping condition. For user-defined stopping conditions, use this field to specify what kind of value you want to stop on.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.central_body_name
    :type: str

    Gets or sets the central body. The default central body of a stopping condition is the Earth.

.. py:property:: criterion
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.criterion
    :type: CRITERION

    Specifies the direction from which the stopping condition value must be achieved.

.. py:property:: before_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.before_conditions
    :type: IStoppingConditionCollection

    A 'before' stopping condition is used to define a stopping condition that depends on two events. Astrogator will ignore a stopping condition until its 'before' conditions are met. Astrogator then interpolates backwards to the normal stopping condition.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.dimension
    :type: str

    Get the dimension of the stopping condition.

.. py:property:: reference_point
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.reference_point
    :type: str

    Gets or sets the reference point used for calculation.

.. py:property:: user_calc_object_link_embed_control
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.user_calc_object_link_embed_control
    :type: IComponentLinkEmbedControl

    Gets the link / embed controller for managing the user calc. object.


Method detail
-------------




























.. py:method:: copy_user_calc_object_to_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.copy_user_calc_object_to_clipboard

    Copy the user-defined stopping condition calc object to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_user_calc_object_from_clipboard(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingCondition.paste_user_calc_object_from_clipboard

    Replace the user-defined stopping condition calc object with the calc object in the clipboard.

    :Returns:

        :obj:`~None`


