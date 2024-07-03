IProfileBisection
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileBisection

   IProfile
   
   Properties of Single Parameter Bisection profile.

.. py:currentmodule:: IProfileBisection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileBisection.control_parameters`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileBisection.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileBisection.targeter_graphs`
              - Graphs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileBisection.scripting_tool`
              - Returns the Scripting tool for the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileBisection.reset_controls_before_run`
              - Reset controls before each run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileBisection.maximum_iterations`
              - Gets or sets the maximum number of iterations allowed.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileBisection


Property detail
---------------

.. py:property:: control_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileBisection.control_parameters
    :type: IBisectionControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileBisection.results
    :type: IBisectionResultCollection

    Get the list of results defined for the profile.

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileBisection.targeter_graphs
    :type: ITargeterGraphCollection

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileBisection.scripting_tool
    :type: IScriptingTool

    Returns the Scripting tool for the sequence.

.. py:property:: reset_controls_before_run
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileBisection.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: maximum_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileBisection.maximum_iterations
    :type: int

    Gets or sets the maximum number of iterations allowed.


