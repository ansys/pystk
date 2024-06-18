IChainGraphics2DAnimation
=========================

.. py:class:: IChainGraphics2DAnimation

   object
   
   2D Animation graphics for a chain.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_highlight_visible`
            * - :py:meth:`~is_line_visible`
            * - :py:meth:`~is_direction_visible`
            * - :py:meth:`~color`
            * - :py:meth:`~line_width`
            * - :py:meth:`~optimal_path_is_line_visible`
            * - :py:meth:`~optimal_path_color`
            * - :py:meth:`~optimal_path_line_width`
            * - :py:meth:`~use_hide_animation_graphics_2d_if_more_than_n_strands`
            * - :py:meth:`~hide_animation_graphics_2d_if_more_than_n_strands_num`
            * - :py:meth:`~number_of_opt_strands_to_display`
            * - :py:meth:`~optimal_path_color_ramp_start_color`
            * - :py:meth:`~optimal_path_color_ramp_end_color`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IChainGraphics2DAnimation


Property detail
---------------

.. py:property:: is_highlight_visible
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.is_highlight_visible
    :type: bool

    Opt whether to display access in bold print during animation. A box appears around each object during access.

.. py:property:: is_line_visible
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.is_line_visible
    :type: bool

    Opt whether to display lines between the valid strands in the chain during animation.

.. py:property:: is_direction_visible
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.is_direction_visible
    :type: bool

    Opt whether to have each link line in the valid strand lines is numbered to show the sequence of the links between the objects in the chain.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.color
    :type: agcolor.Color

    Gets or sets the color in which valid strand lines are to be displayed during animation.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.line_width
    :type: "LINE_WIDTH"

    Gets or sets the width of the valid strand lines used in animation graphics.

.. py:property:: optimal_path_is_line_visible
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.optimal_path_is_line_visible
    :type: bool

    Opt whether to display lines for the optimal strands in the chain during animation.

.. py:property:: optimal_path_color
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.optimal_path_color
    :type: agcolor.Color

    This property is deprecated. Use OptimalPathColorRampStartColor. Gets or sets the color in which the optimal strands lines are to be displayed during animation.

.. py:property:: optimal_path_line_width
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.optimal_path_line_width
    :type: "LINE_WIDTH"

    Gets or sets the width of the optimal strands lines used in animation graphics.

.. py:property:: use_hide_animation_graphics_2d_if_more_than_n_strands
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.use_hide_animation_graphics_2d_if_more_than_n_strands
    :type: bool

    Use the maximum number of animation strand lines to show. If there are more than the specified number of valid strands, the animation lines are not displayed.

.. py:property:: hide_animation_graphics_2d_if_more_than_n_strands_num
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.hide_animation_graphics_2d_if_more_than_n_strands_num
    :type: int

    Gets or sets the maximum number of animation strand lines to show. If there are more than the specified number of valid strands, the animation lines are not displayed.

.. py:property:: number_of_opt_strands_to_display
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.number_of_opt_strands_to_display
    :type: int

    The number of animation optimal strands lines to show.

.. py:property:: optimal_path_color_ramp_start_color
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.optimal_path_color_ramp_start_color
    :type: agcolor.Color

    The start color for the color ramp in which the optimal strands lines are to be displayed during animation.

.. py:property:: optimal_path_color_ramp_end_color
    :canonical: ansys.stk.core.stkobjects.IChainGraphics2DAnimation.optimal_path_color_ramp_end_color
    :type: agcolor.Color

    The end color for the color ramp in which the optimal strands lines are to be displayed during animation.


