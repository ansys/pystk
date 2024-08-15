VehicleLOPCentralBodyGravity
============================

.. py:class:: ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity

   Class defining gravity options for the LOP propagator.

.. py:currentmodule:: VehicleLOPCentralBodyGravity

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity.max_degree`
              - Gets or sets the maximum degree of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity.max_order`
              - Gets or sets the maximum order of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleLOPCentralBodyGravity


Property detail
---------------

.. py:property:: max_degree
    :canonical: ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity.max_degree
    :type: int

    Gets or sets the maximum degree of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.

.. py:property:: max_order
    :canonical: ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity.max_order
    :type: int

    Gets or sets the maximum order of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.


