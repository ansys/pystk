CommSystemAccessSamplingMethodAdaptive
======================================

.. py:class:: ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodAdaptive

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICommSystemAccessSamplingMethod`

   Class defining a CommSystem access options.

.. py:currentmodule:: CommSystemAccessSamplingMethodAdaptive

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodAdaptive.max_time_step`
              - Gets or sets the maximum step size to be used in new access computations. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodAdaptive.min_time_step`
              - Gets or sets the minimum step size that is allowed to be taken.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CommSystemAccessSamplingMethodAdaptive


Property detail
---------------

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodAdaptive.max_time_step
    :type: float

    Gets or sets the maximum step size to be used in new access computations. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.

.. py:property:: min_time_step
    :canonical: ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodAdaptive.min_time_step
    :type: float

    Gets or sets the minimum step size that is allowed to be taken.


