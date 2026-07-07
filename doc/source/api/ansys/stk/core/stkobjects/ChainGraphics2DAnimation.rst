ChainGraphics2DAnimation
========================

.. py:class:: ansys.stk.core.stkobjects.ChainGraphics2DAnimation

   2D Animation graphics for a chain.

.. py:currentmodule:: ChainGraphics2DAnimation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.color`
              - Get or set the color in which valid strand lines are to be displayed during animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.hide_animation_graphics_2d_if_more_than_n_strands_number`
              - Get or set the maximum number of animation strand lines to show. If there are more than the specified number of valid strands, the animation lines are not displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.line_width`
              - Get or set the width of the valid strand lines used in animation graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_end_nodes_color`
              - The color for the end nodes for network throughput graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_link_combine_strands`
              - Combine strand link data when multiple strands overlap for Network Throughput graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_link_data_mode`
              - The data mode for displaying link labels and lines for network throughput graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_link_labels_include_num_strands`
              - Include the number of strands in the link labels for Network Throughput graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_link_line_width`
              - Line width of links when network throughput graphics are displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_node_data_mode`
              - The data mode for displaying nodes labels and points for network throughput graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_node_point_size`
              - Pixel size of nodes when network throughput graphics are displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_one_hundred_pct_contour_color`
              - The color for the 100 percentage network throughput contours graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_zero_pct_contour_color`
              - The color for the 0 percentage network throughput contours graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.number_of_optimal_strands_to_display`
              - The number of animation optimal strands lines to show.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.optimal_path_color_ramp_end_color`
              - The end color for the color ramp in which the optimal strands lines are to be displayed during animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.optimal_path_color_ramp_start_color`
              - The start color for the color ramp in which the optimal strands lines are to be displayed during animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.optimal_path_line_width`
              - Get or set the width of the optimal strands lines used in animation graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_highlight`
              - Opt whether to display access in bold print during animation. A box appears around each object during access.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_line`
              - Opt whether to display lines between the valid strands in the chain during animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_link_numbers_in_strands`
              - Opt whether to have each link line in the valid strand lines is numbered to show the sequence of the links between the objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_graphics_2d`
              - Show or hide all network throughput graphics if computed.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_link_graphics_2d`
              - Show or hide all network throughput link graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_link_labels_graphics_2d`
              - Show or hide all network throughput link labels.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_node_graphics_2d`
              - Show or hide all network throughput node graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_node_labels_graphics_2d`
              - Show or hide all network throughput node labels.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_optimal_path_line`
              - Opt whether to display lines for the optimal strands in the chain during animation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation.use_hide_animation_graphics_2d_if_more_than_n_strands`
              - Use the maximum number of animation strand lines to show. If there are more than the specified number of valid strands, the animation lines are not displayed.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainGraphics2DAnimation


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.color
    :type: Color

    Get or set the color in which valid strand lines are to be displayed during animation.

.. py:property:: hide_animation_graphics_2d_if_more_than_n_strands_number
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.hide_animation_graphics_2d_if_more_than_n_strands_number
    :type: int

    Get or set the maximum number of animation strand lines to show. If there are more than the specified number of valid strands, the animation lines are not displayed.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.line_width
    :type: LineWidth

    Get or set the width of the valid strand lines used in animation graphics.

.. py:property:: network_throughput_end_nodes_color
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_end_nodes_color
    :type: Color

    The color for the end nodes for network throughput graphics.

.. py:property:: network_throughput_link_combine_strands
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_link_combine_strands
    :type: bool

    Combine strand link data when multiple strands overlap for Network Throughput graphics.

.. py:property:: network_throughput_link_data_mode
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_link_data_mode
    :type: ChainGraphics2DNetworkDataMode

    The data mode for displaying link labels and lines for network throughput graphics.

.. py:property:: network_throughput_link_labels_include_num_strands
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_link_labels_include_num_strands
    :type: bool

    Include the number of strands in the link labels for Network Throughput graphics.

.. py:property:: network_throughput_link_line_width
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_link_line_width
    :type: LineWidth

    Line width of links when network throughput graphics are displayed.

.. py:property:: network_throughput_node_data_mode
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_node_data_mode
    :type: ChainGraphics2DNetworkDataMode

    The data mode for displaying nodes labels and points for network throughput graphics.

.. py:property:: network_throughput_node_point_size
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_node_point_size
    :type: float

    Pixel size of nodes when network throughput graphics are displayed.

.. py:property:: network_throughput_one_hundred_pct_contour_color
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_one_hundred_pct_contour_color
    :type: Color

    The color for the 100 percentage network throughput contours graphics.

.. py:property:: network_throughput_zero_pct_contour_color
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.network_throughput_zero_pct_contour_color
    :type: Color

    The color for the 0 percentage network throughput contours graphics.

.. py:property:: number_of_optimal_strands_to_display
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.number_of_optimal_strands_to_display
    :type: int

    The number of animation optimal strands lines to show.

.. py:property:: optimal_path_color_ramp_end_color
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.optimal_path_color_ramp_end_color
    :type: Color

    The end color for the color ramp in which the optimal strands lines are to be displayed during animation.

.. py:property:: optimal_path_color_ramp_start_color
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.optimal_path_color_ramp_start_color
    :type: Color

    The start color for the color ramp in which the optimal strands lines are to be displayed during animation.

.. py:property:: optimal_path_line_width
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.optimal_path_line_width
    :type: LineWidth

    Get or set the width of the optimal strands lines used in animation graphics.

.. py:property:: show_highlight
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_highlight
    :type: bool

    Opt whether to display access in bold print during animation. A box appears around each object during access.

.. py:property:: show_line
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_line
    :type: bool

    Opt whether to display lines between the valid strands in the chain during animation.

.. py:property:: show_link_numbers_in_strands
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_link_numbers_in_strands
    :type: bool

    Opt whether to have each link line in the valid strand lines is numbered to show the sequence of the links between the objects in the chain.

.. py:property:: show_network_throughput_graphics_2d
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_graphics_2d
    :type: bool

    Show or hide all network throughput graphics if computed.

.. py:property:: show_network_throughput_link_graphics_2d
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_link_graphics_2d
    :type: bool

    Show or hide all network throughput link graphics.

.. py:property:: show_network_throughput_link_labels_graphics_2d
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_link_labels_graphics_2d
    :type: bool

    Show or hide all network throughput link labels.

.. py:property:: show_network_throughput_node_graphics_2d
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_node_graphics_2d
    :type: bool

    Show or hide all network throughput node graphics.

.. py:property:: show_network_throughput_node_labels_graphics_2d
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_network_throughput_node_labels_graphics_2d
    :type: bool

    Show or hide all network throughput node labels.

.. py:property:: show_optimal_path_line
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.show_optimal_path_line
    :type: bool

    Opt whether to display lines for the optimal strands in the chain during animation.

.. py:property:: use_hide_animation_graphics_2d_if_more_than_n_strands
    :canonical: ansys.stk.core.stkobjects.ChainGraphics2DAnimation.use_hide_animation_graphics_2d_if_more_than_n_strands
    :type: bool

    Use the maximum number of animation strand lines to show. If there are more than the specified number of valid strands, the animation lines are not displayed.


