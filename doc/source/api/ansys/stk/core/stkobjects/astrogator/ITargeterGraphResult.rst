ITargeterGraphResult
====================

.. py:class:: ITargeterGraphResult

   object
   
   Properties for targeter graph result.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~parent_name`
            * - :py:meth:`~show_desired_value`
            * - :py:meth:`~line_color`
            * - :py:meth:`~point_style`
            * - :py:meth:`~y_axis`
            * - :py:meth:`~graph_option`
            * - :py:meth:`~show_tolerance_band`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ITargeterGraphResult


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult.name
    :type: str

    Get the name of the result.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult.parent_name
    :type: str

    Get the segment or component for which this result has been selected.

.. py:property:: show_desired_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult.show_desired_value
    :type: bool

    Show the desired value.

.. py:property:: line_color
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult.line_color
    :type: agcolor.Color

    Line Color.

.. py:property:: point_style
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult.point_style
    :type: str

    Point Style.

.. py:property:: y_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult.y_axis
    :type: str

    Select whether to display the result's value range on the left or right side of the graph.

.. py:property:: graph_option
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult.graph_option
    :type: GRAPH_OPTION

    Graph option.

.. py:property:: show_tolerance_band
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult.show_tolerance_band
    :type: bool

    Show the tolerance band.


