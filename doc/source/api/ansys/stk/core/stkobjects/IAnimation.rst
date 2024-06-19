IAnimation
==========

.. py:class:: IAnimation

   object
   
   Provide methods to control scenario animation.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~play_forward`
              - Animate forward.
            * - :py:meth:`~play_backward`
              - Animate backward.
            * - :py:meth:`~pause`
              - Pause the animation.
            * - :py:meth:`~rewind`
              - Stop and reset the animation.
            * - :py:meth:`~step_forward`
              - Advance the animation one step forward.
            * - :py:meth:`~step_backward`
              - Reverse the animation one step backward.
            * - :py:meth:`~faster`
              - Increase the speed of the animation.
            * - :py:meth:`~slower`
              - Decrease the speed of the animation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~mode`
            * - :py:meth:`~current_time`
            * - :py:meth:`~step`
            * - :py:meth:`~animation_options`
            * - :py:meth:`~high_speed`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAnimation


Property detail
---------------

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.IAnimation.mode
    :type: ANIMATION_MODES

    Animation mode.

.. py:property:: current_time
    :canonical: ansys.stk.core.stkobjects.IAnimation.current_time
    :type: float

    Current animation time. In Epoch seconds.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IAnimation.step
    :type: str

    Get animation time step.

.. py:property:: animation_options
    :canonical: ansys.stk.core.stkobjects.IAnimation.animation_options
    :type: ANIMATION_OPTIONS

    Animation options.

.. py:property:: high_speed
    :canonical: ansys.stk.core.stkobjects.IAnimation.high_speed
    :type: bool

    Controls the animation speed.


Method detail
-------------

.. py:method:: play_forward(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.play_forward

    Animate forward.

    :Returns:

        :obj:`~None`

.. py:method:: play_backward(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.play_backward

    Animate backward.

    :Returns:

        :obj:`~None`

.. py:method:: pause(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.pause

    Pause the animation.

    :Returns:

        :obj:`~None`

.. py:method:: rewind(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.rewind

    Stop and reset the animation.

    :Returns:

        :obj:`~None`

.. py:method:: step_forward(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.step_forward

    Advance the animation one step forward.

    :Returns:

        :obj:`~None`

.. py:method:: step_backward(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.step_backward

    Reverse the animation one step backward.

    :Returns:

        :obj:`~None`

.. py:method:: faster(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.faster

    Increase the speed of the animation.

    :Returns:

        :obj:`~None`

.. py:method:: slower(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAnimation.slower

    Decrease the speed of the animation.

    :Returns:

        :obj:`~None`










