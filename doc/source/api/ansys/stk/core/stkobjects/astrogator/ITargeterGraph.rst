ITargeterGraph
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ITargeterGraph

   object
   
   Properties for a Targeter Graph.

.. py:currentmodule:: ITargeterGraph

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.generate_on_run`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.user_comment`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.show_label_iterations`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.show_desired_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.show_tolerance_band`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.independent_variable`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.active_controls`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph.results`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ITargeterGraph


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.name
    :type: str

    Gets or sets the name of the graph.

.. py:property:: generate_on_run
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.generate_on_run
    :type: bool

    Generate the graph while MCS is being run.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.user_comment
    :type: str

    User Comment.

.. py:property:: show_label_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.show_label_iterations
    :type: bool

    Label each of the points on the graph labeled according to its iteration number.

.. py:property:: show_desired_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.show_desired_value
    :type: bool

    Show the desired equality constraint value(s) on the graph. Not applicable to SNOPT and IPOPT search profiles.

.. py:property:: show_tolerance_band
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.show_tolerance_band
    :type: bool

    Show the tolerance band on the graph. Not applicable to SNOPT and IPOPT search profiles.

.. py:property:: independent_variable
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.independent_variable
    :type: str

    Select the graph's X axis.

.. py:property:: active_controls
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.active_controls
    :type: ITargeterGraphActiveControlCollection

    Active Controls.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraph.results
    :type: ITargeterGraphResultCollection

    Results.


