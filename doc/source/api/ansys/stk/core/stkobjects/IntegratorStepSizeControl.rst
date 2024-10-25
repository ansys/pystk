IntegratorStepSizeControl
=========================

.. py:class:: ansys.stk.core.stkobjects.IntegratorStepSizeControl

   Class defining step size control for the HPOP integrator.

.. py:currentmodule:: IntegratorStepSizeControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IntegratorStepSizeControl.method`
              - Fixed step or relative error.
            * - :py:attr:`~ansys.stk.core.stkobjects.IntegratorStepSizeControl.error_tolerance`
              - If the method is relative error. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IntegratorStepSizeControl.minimum_step_size`
              - If the method is relative error. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IntegratorStepSizeControl.maximum_step_size`
              - If the method is relative error. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IntegratorStepSizeControl


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.IntegratorStepSizeControl.method
    :type: VEHICLE_METHOD

    Fixed step or relative error.

.. py:property:: error_tolerance
    :canonical: ansys.stk.core.stkobjects.IntegratorStepSizeControl.error_tolerance
    :type: float

    If the method is relative error. Dimensionless.

.. py:property:: minimum_step_size
    :canonical: ansys.stk.core.stkobjects.IntegratorStepSizeControl.minimum_step_size
    :type: float

    If the method is relative error. Uses Time Dimension.

.. py:property:: maximum_step_size
    :canonical: ansys.stk.core.stkobjects.IntegratorStepSizeControl.maximum_step_size
    :type: float

    If the method is relative error. Uses Time Dimension.


