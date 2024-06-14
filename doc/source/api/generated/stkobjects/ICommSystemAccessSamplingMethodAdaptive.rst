ICommSystemAccessSamplingMethodAdaptive
=======================================

.. py:class:: ICommSystemAccessSamplingMethodAdaptive

   object
   
   Provide access to the properties for a adaptive sampling method.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_time_step`
            * - :py:meth:`~min_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICommSystemAccessSamplingMethodAdaptive


Property detail
---------------

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessSamplingMethodAdaptive.max_time_step
    :type: float

    Gets or sets the maximum step size to be used in new access computations. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.

.. py:property:: min_time_step
    :canonical: ansys.stk.core.stkobjects.ICommSystemAccessSamplingMethodAdaptive.min_time_step
    :type: float

    Gets or sets the minimum step size that is allowed to be taken.


