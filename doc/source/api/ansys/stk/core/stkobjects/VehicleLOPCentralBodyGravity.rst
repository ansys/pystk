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

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity.maximum_degree`
              - Gets or sets the maximum degree of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity.maximum_order`
              - Gets or sets the maximum order of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleLOPCentralBodyGravity


Property detail
---------------

.. py:property:: maximum_degree
    :canonical: ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity.maximum_degree
    :type: int

    Gets or sets the maximum degree of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.

.. py:property:: maximum_order
    :canonical: ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity.maximum_order
    :type: int

    Gets or sets the maximum order of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.


