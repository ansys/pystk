ISamplingMethodAdaptive
=======================

.. py:class:: ansys.stk.core.stkobjects.ISamplingMethodAdaptive

   ISamplingMethodStrategy
   
   Define an adaptive sampling method.

.. py:currentmodule:: ISamplingMethodAdaptive

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISamplingMethodAdaptive.max_time_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISamplingMethodAdaptive.min_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISamplingMethodAdaptive


Property detail
---------------

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.ISamplingMethodAdaptive.max_time_step
    :type: float

    Maximum sampling step size used in access calculations. Uses Time Dimension.

.. py:property:: min_time_step
    :canonical: ansys.stk.core.stkobjects.ISamplingMethodAdaptive.min_time_step
    :type: float

    Minimum sampling step size used in access calculations. Uses Time Dimension.


