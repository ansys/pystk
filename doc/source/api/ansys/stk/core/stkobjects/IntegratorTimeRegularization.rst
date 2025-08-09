IntegratorTimeRegularization
============================

.. py:class:: ansys.stk.core.stkobjects.IntegratorTimeRegularization

   Class defining time regularization for the HPOP integrator, i.e. integration the orbit with respect to regularized time.

.. py:currentmodule:: IntegratorTimeRegularization

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IntegratorTimeRegularization.exponent`
              - Exponent used in the regularization equation. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IntegratorTimeRegularization.steps_per_orbit`
              - Integration steps per orbit. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IntegratorTimeRegularization.use`
              - Opt whether to integrate the orbit with respect to regularized time.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IntegratorTimeRegularization


Property detail
---------------

.. py:property:: exponent
    :canonical: ansys.stk.core.stkobjects.IntegratorTimeRegularization.exponent
    :type: float

    Exponent used in the regularization equation. Dimensionless.

.. py:property:: steps_per_orbit
    :canonical: ansys.stk.core.stkobjects.IntegratorTimeRegularization.steps_per_orbit
    :type: int

    Integration steps per orbit. Dimensionless.

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.IntegratorTimeRegularization.use
    :type: bool

    Opt whether to integrate the orbit with respect to regularized time.


