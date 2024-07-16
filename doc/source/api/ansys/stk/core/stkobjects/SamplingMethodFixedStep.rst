SamplingMethodFixedStep
=======================

.. py:class:: ansys.stk.core.stkobjects.SamplingMethodFixedStep

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISamplingMethodStrategy`

   Define a fixed time-step sampling method.

.. py:currentmodule:: SamplingMethodFixedStep

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SamplingMethodFixedStep.fixed_time_step`
              - Fixed sampling time step. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SamplingMethodFixedStep.time_bound`
              - Duration used to align sample times with UTC. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SamplingMethodFixedStep


Property detail
---------------

.. py:property:: fixed_time_step
    :canonical: ansys.stk.core.stkobjects.SamplingMethodFixedStep.fixed_time_step
    :type: float

    Fixed sampling time step. Uses Time Dimension.

.. py:property:: time_bound
    :canonical: ansys.stk.core.stkobjects.SamplingMethodFixedStep.time_bound
    :type: float

    Duration used to align sample times with UTC. Uses Time Dimension.


