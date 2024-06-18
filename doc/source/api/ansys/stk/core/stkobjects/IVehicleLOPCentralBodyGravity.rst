IVehicleLOPCentralBodyGravity
=============================

.. py:class:: IVehicleLOPCentralBodyGravity

   object
   
   Central body gravity interface for Long-range Orbit Predictor (LOP) propagator.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_degree`
            * - :py:meth:`~max_order`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleLOPCentralBodyGravity


Property detail
---------------

.. py:property:: max_degree
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPCentralBodyGravity.max_degree
    :type: int

    Gets or sets the maximum degree of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.

.. py:property:: max_order
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPCentralBodyGravity.max_order
    :type: int

    Gets or sets the maximum order of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.


