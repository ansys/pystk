VehicleTimeRegularization
=========================

.. py:class:: ansys.stk.core.stkobjects.VehicleTimeRegularization

   Bases: 

   Class defining time regularization for the HPOP integrator, i.e. integration the orbit with respect to regularized time.

.. py:currentmodule:: VehicleTimeRegularization

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTimeRegularization.use`
              - Opt whether to integrate the orbit with respect to regularized time.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTimeRegularization.exponent`
              - Exponent used in the regularization equation. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTimeRegularization.steps_per_orbit`
              - Integration steps per orbit. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleTimeRegularization


Property detail
---------------

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.VehicleTimeRegularization.use
    :type: bool

    Opt whether to integrate the orbit with respect to regularized time.

.. py:property:: exponent
    :canonical: ansys.stk.core.stkobjects.VehicleTimeRegularization.exponent
    :type: float

    Exponent used in the regularization equation. Dimensionless.

.. py:property:: steps_per_orbit
    :canonical: ansys.stk.core.stkobjects.VehicleTimeRegularization.steps_per_orbit
    :type: int

    Integration steps per orbit. Dimensionless.


