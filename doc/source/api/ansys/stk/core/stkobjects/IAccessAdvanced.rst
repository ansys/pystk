IAccessAdvanced
===============

.. py:class:: ansys.stk.core.stkobjects.IAccessAdvanced

   Interface for configuring advanced targeting access computation properties.

.. py:currentmodule:: IAccessAdvanced

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessAdvanced.aberration_type`
              - Model used for including aberration in apparent direction computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessAdvanced.time_delay_convergence`
              - Time delay convergence tolerance. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessAdvanced.event_detection`
              - Event detection strategy used in access calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessAdvanced.sampling`
              - Sampling method used in access calculations.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessAdvanced


Property detail
---------------

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.IAccessAdvanced.aberration_type
    :type: AberrationType

    Model used for including aberration in apparent direction computations.

.. py:property:: time_delay_convergence
    :canonical: ansys.stk.core.stkobjects.IAccessAdvanced.time_delay_convergence
    :type: float

    Time delay convergence tolerance. Uses Time Dimension.

.. py:property:: event_detection
    :canonical: ansys.stk.core.stkobjects.IAccessAdvanced.event_detection
    :type: AccessEventDetection

    Event detection strategy used in access calculations.

.. py:property:: sampling
    :canonical: ansys.stk.core.stkobjects.IAccessAdvanced.sampling
    :type: AccessSampling

    Sampling method used in access calculations.


