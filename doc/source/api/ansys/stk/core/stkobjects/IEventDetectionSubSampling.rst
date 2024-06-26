IEventDetectionSubSampling
==========================

.. py:class:: ansys.stk.core.stkobjects.IEventDetectionSubSampling

   IEventDetectionStrategy
   
   Interface for event detection strategy involving subsampling.

.. py:currentmodule:: IEventDetectionSubSampling

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IEventDetectionSubSampling.time_convergence`
              - Time convergence value used in access computations. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IEventDetectionSubSampling.abs_value_convergence`
              - Use absolute convergence value for access. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IEventDetectionSubSampling.rel_value_convergence`
              - Use relative convergence value for access. Dimensionless.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IEventDetectionSubSampling


Property detail
---------------

.. py:property:: time_convergence
    :canonical: ansys.stk.core.stkobjects.IEventDetectionSubSampling.time_convergence
    :type: float

    Time convergence value used in access computations. Uses Time Dimension.

.. py:property:: abs_value_convergence
    :canonical: ansys.stk.core.stkobjects.IEventDetectionSubSampling.abs_value_convergence
    :type: float

    Use absolute convergence value for access. Dimensionless.

.. py:property:: rel_value_convergence
    :canonical: ansys.stk.core.stkobjects.IEventDetectionSubSampling.rel_value_convergence
    :type: float

    Use relative convergence value for access. Dimensionless.


