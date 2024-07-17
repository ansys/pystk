CommSystemAccessSamplingMethodFixed
===================================

.. py:class:: ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodFixed

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICommSystemAccessSamplingMethod`

   Class defining a CommSystem access options.

.. py:currentmodule:: CommSystemAccessSamplingMethodFixed

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodFixed.fixed_time_step`
              - Specifies the fixed step size for the fixed step control.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodFixed.time_bound`
              - Controls alignment of samples with a UTC time grid. Using proper time bound can improve computational performance if the ephemeris lies on a fixed UTC time grid. The time bound determines the reference time for taking fixed step samples.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CommSystemAccessSamplingMethodFixed


Property detail
---------------

.. py:property:: fixed_time_step
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodFixed.fixed_time_step
    :type: float

    Specifies the fixed step size for the fixed step control.

.. py:property:: time_bound
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodFixed.time_bound
    :type: float

    Controls alignment of samples with a UTC time grid. Using proper time bound can improve computational performance if the ephemeris lies on a fixed UTC time grid. The time bound determines the reference time for taking fixed step samples.


