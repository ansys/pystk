ICoverageInterval
=================

.. py:class:: ansys.stk.core.stkobjects.ICoverageInterval

   object
   
   Coverage interval: the time period over which coverage is computed.

.. py:currentmodule:: ICoverageInterval

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageInterval.use_scenario_interval`
              - Use the scenario time period as the coverage interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageInterval.analysis_interval`
              - Get the coverage analysis interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageInterval


Property detail
---------------

.. py:property:: use_scenario_interval
    :canonical: ansys.stk.core.stkobjects.ICoverageInterval.use_scenario_interval
    :type: bool

    Use the scenario time period as the coverage interval.

.. py:property:: analysis_interval
    :canonical: ansys.stk.core.stkobjects.ICoverageInterval.analysis_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the coverage analysis interval.


