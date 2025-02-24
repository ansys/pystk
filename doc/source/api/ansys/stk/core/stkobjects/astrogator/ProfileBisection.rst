ProfileBisection
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileBisection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Single Parameter Bisection profile.

.. py:currentmodule:: ProfileBisection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileBisection.control_parameters`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileBisection.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileBisection.targeter_graphs`
              - Graphs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileBisection.scripting_tool`
              - Return the Scripting tool for the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileBisection.reset_controls_before_run`
              - Reset controls before each run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileBisection.maximum_iterations`
              - Get or set the maximum number of iterations allowed.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileBisection


Property detail
---------------

.. py:property:: control_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileBisection.control_parameters
    :type: BisectionControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileBisection.results
    :type: BisectionResultCollection

    Get the list of results defined for the profile.

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileBisection.targeter_graphs
    :type: TargeterGraphCollection

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileBisection.scripting_tool
    :type: ScriptingTool

    Return the Scripting tool for the sequence.

.. py:property:: reset_controls_before_run
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileBisection.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: maximum_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileBisection.maximum_iterations
    :type: int

    Get or set the maximum number of iterations allowed.


