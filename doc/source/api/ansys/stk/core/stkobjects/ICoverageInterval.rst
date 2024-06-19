ICoverageInterval
=================

.. py:class:: ICoverageInterval

   object
   
   Coverage interval: the time period over which coverage is computed.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_scenario_interval`
            * - :py:meth:`~analysis_interval`


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
    :type: IAgCrdnEventIntervalSmartInterval

    Get the coverage analysis interval.


