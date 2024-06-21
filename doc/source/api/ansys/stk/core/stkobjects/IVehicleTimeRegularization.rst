IVehicleTimeRegularization
==========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleTimeRegularization

   object
   
   Interface for time regularization.

.. py:currentmodule:: IVehicleTimeRegularization

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTimeRegularization.use`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTimeRegularization.exponent`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTimeRegularization.steps_per_orbit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTimeRegularization


Property detail
---------------

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.IVehicleTimeRegularization.use
    :type: bool

    Opt whether to integrate the orbit with respect to regularized time.

.. py:property:: exponent
    :canonical: ansys.stk.core.stkobjects.IVehicleTimeRegularization.exponent
    :type: float

    Exponent used in the regularization equation. Dimensionless.

.. py:property:: steps_per_orbit
    :canonical: ansys.stk.core.stkobjects.IVehicleTimeRegularization.steps_per_orbit
    :type: int

    Integration steps per orbit. Dimensionless.


