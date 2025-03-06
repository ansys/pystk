TargeterGraph
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.TargeterGraph

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Targeter Graph.

.. py:currentmodule:: TargeterGraph

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.name`
              - Get or set the name of the graph.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.generate_on_run`
              - Generate the graph while MCS is being run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.user_comment`
              - User Comment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.show_label_iterations`
              - Label each of the points on the graph labeled according to its iteration number.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.show_desired_value`
              - Show the desired equality constraint value(s) on the graph. Not applicable to SNOPT and IPOPT search profiles.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.show_tolerance_band`
              - Show the tolerance band on the graph. Not applicable to SNOPT and IPOPT search profiles.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.independent_variable`
              - Select the graph's X axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.active_controls`
              - Active Controls.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph.results`
              - Results.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import TargeterGraph


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.name
    :type: str

    Get or set the name of the graph.

.. py:property:: generate_on_run
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.generate_on_run
    :type: bool

    Generate the graph while MCS is being run.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.user_comment
    :type: str

    User Comment.

.. py:property:: show_label_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.show_label_iterations
    :type: bool

    Label each of the points on the graph labeled according to its iteration number.

.. py:property:: show_desired_value
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.show_desired_value
    :type: bool

    Show the desired equality constraint value(s) on the graph. Not applicable to SNOPT and IPOPT search profiles.

.. py:property:: show_tolerance_band
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.show_tolerance_band
    :type: bool

    Show the tolerance band on the graph. Not applicable to SNOPT and IPOPT search profiles.

.. py:property:: independent_variable
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.independent_variable
    :type: str

    Select the graph's X axis.

.. py:property:: active_controls
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.active_controls
    :type: TargeterGraphActiveControlCollection

    Active Controls.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraph.results
    :type: TargeterGraphResultCollection

    Results.


