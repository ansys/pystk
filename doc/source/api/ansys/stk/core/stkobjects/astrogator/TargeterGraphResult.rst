TargeterGraphResult
===================

.. py:class:: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Targeter Graph Result.

.. py:currentmodule:: TargeterGraphResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.name`
              - Get the name of the result.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.parent_name`
              - Get the segment or component for which this result has been selected.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.show_desired_value`
              - Show the desired value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.line_color`
              - Line Color.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.point_style`
              - Point Style.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.y_axis`
              - Select whether to display the result's value range on the left or right side of the graph.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.graph_option`
              - Graph option.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.show_tolerance_band`
              - Show the tolerance band.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import TargeterGraphResult


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.name
    :type: str

    Get the name of the result.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.parent_name
    :type: str

    Get the segment or component for which this result has been selected.

.. py:property:: show_desired_value
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.show_desired_value
    :type: bool

    Show the desired value.

.. py:property:: line_color
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.line_color
    :type: agcolor.Color

    Line Color.

.. py:property:: point_style
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.point_style
    :type: str

    Point Style.

.. py:property:: y_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.y_axis
    :type: str

    Select whether to display the result's value range on the left or right side of the graph.

.. py:property:: graph_option
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.graph_option
    :type: GRAPH_OPTION

    Graph option.

.. py:property:: show_tolerance_band
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphResult.show_tolerance_band
    :type: bool

    Show the tolerance band.


