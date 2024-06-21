IVehicleStepSizeControl
=======================

.. py:class:: ansys.stk.core.stkobjects.IVehicleStepSizeControl

   object
   
   Interface for step size control.

.. py:currentmodule:: IVehicleStepSizeControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleStepSizeControl.method`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleStepSizeControl.error_tolerance`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleStepSizeControl.min_step_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleStepSizeControl.max_step_size`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleStepSizeControl


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.IVehicleStepSizeControl.method
    :type: VEHICLE_METHOD

    Fixed step or relative error.

.. py:property:: error_tolerance
    :canonical: ansys.stk.core.stkobjects.IVehicleStepSizeControl.error_tolerance
    :type: float

    If the method is relative error. Dimensionless.

.. py:property:: min_step_size
    :canonical: ansys.stk.core.stkobjects.IVehicleStepSizeControl.min_step_size
    :type: float

    If the method is relative error. Uses Time Dimension.

.. py:property:: max_step_size
    :canonical: ansys.stk.core.stkobjects.IVehicleStepSizeControl.max_step_size
    :type: float

    If the method is relative error. Uses Time Dimension.


