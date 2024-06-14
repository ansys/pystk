ISamplingMethodFixedStep
========================

.. py:class:: ISamplingMethodFixedStep

   ISamplingMethodStrategy
   
   Define a fixed time-step sampling method.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~fixed_time_step`
            * - :py:meth:`~time_bound`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISamplingMethodFixedStep


Property detail
---------------

.. py:property:: fixed_time_step
    :canonical: ansys.stk.core.stkobjects.ISamplingMethodFixedStep.fixed_time_step
    :type: float

    Fixed sampling time step. Uses Time Dimension.

.. py:property:: time_bound
    :canonical: ansys.stk.core.stkobjects.ISamplingMethodFixedStep.time_bound
    :type: float

    Duration used to align sample times with UTC. Uses Time Dimension.


