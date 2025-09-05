IAnimation
==========

.. py:class:: ansys.stk.core.stkobjects.IAnimation

   Provide methods to control scenario animation.

.. py:currentmodule:: IAnimation

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.faster`
              - Increase the speed of the animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.pause`
              - Pause the animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.play_backward`
              - Animate backward.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.play_forward`
              - Animate forward.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.rewind`
              - Stop and reset the animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.slower`
              - Decrease the speed of the animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.step_backward`
              - Reverse the animation one step backward.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.step_forward`
              - Advance the animation one step forward.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.animation_options`
              - Animation options.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.current_time`
              - Current animation time. In Epoch seconds.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.high_speed`
              - Control the animation speed.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.mode`
              - Animation mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAnimation.step`
              - Get animation time step.


Examples
--------

Reset the scenario time

.. code-block:: python

    # STKObjectRoot root: STK Object Model Root
    root.rewind()


Change animation mode

.. code-block:: python

    # STKObjectRoot root: STK Object Model Root
    scenario = root.current_scenario
    root.animation_options = AnimationOptionType.STOP
    root.mode = AnimationEndTimeMode.X_REAL_TIME
    scenario.animation_settings.animation_step_value = 1  # second
    scenario.animation_settings.refresh_delta = 0.03  # second


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAnimation


Property detail
---------------

.. py:property:: animation_options
    :canonical: ansys.stk.core.stkobjects.IAnimation.animation_options
    :type: AnimationOptionType

    Animation options.

.. py:property:: current_time
    :canonical: ansys.stk.core.stkobjects.IAnimation.current_time
    :type: float

    Current animation time. In Epoch seconds.

.. py:property:: high_speed
    :canonical: ansys.stk.core.stkobjects.IAnimation.high_speed
    :type: bool

    Control the animation speed.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.IAnimation.mode
    :type: AnimationEndTimeMode

    Animation mode.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IAnimation.step
    :type: str

    Get animation time step.


Method detail
-------------





.. py:method:: faster(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.faster

    Increase the speed of the animation.

    :Returns:

        :obj:`~None`





.. py:method:: pause(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.pause

    Pause the animation.

    :Returns:

        :obj:`~None`

.. py:method:: play_backward(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.play_backward

    Animate backward.

    :Returns:

        :obj:`~None`

.. py:method:: play_forward(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.play_forward

    Animate forward.

    :Returns:

        :obj:`~None`

.. py:method:: rewind(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.rewind

    Stop and reset the animation.

    :Returns:

        :obj:`~None`

.. py:method:: slower(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.slower

    Decrease the speed of the animation.

    :Returns:

        :obj:`~None`


.. py:method:: step_backward(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.step_backward

    Reverse the animation one step backward.

    :Returns:

        :obj:`~None`

.. py:method:: step_forward(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.step_forward

    Advance the animation one step forward.

    :Returns:

        :obj:`~None`

