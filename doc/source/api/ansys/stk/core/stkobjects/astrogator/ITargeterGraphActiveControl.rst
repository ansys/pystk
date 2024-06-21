ITargeterGraphActiveControl
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl

   object
   
   Properties for targeter graph active control.

.. py:currentmodule:: ITargeterGraphActiveControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.parent_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.show_graph_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.line_color`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.point_style`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.y_axis`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ITargeterGraphActiveControl


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.name
    :type: str

    Get the name of the active control.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.parent_name
    :type: str

    Get the segment or component to which the element belongs.

.. py:property:: show_graph_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.show_graph_value
    :type: bool

    Show the value.

.. py:property:: line_color
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.line_color
    :type: agcolor.Color

    Line Color.

.. py:property:: point_style
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.point_style
    :type: str

    Point Style.

.. py:property:: y_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl.y_axis
    :type: str

    Select whether to display the control's value range on the left or right side of the graph.


