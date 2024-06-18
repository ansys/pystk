IVehicleGravity
===============

.. py:class:: IVehicleGravity

   object
   
   Gravity options for covariance matrix.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~maximum_degree`
            * - :py:meth:`~maximum_order`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGravity


Property detail
---------------

.. py:property:: maximum_degree
    :canonical: ansys.stk.core.stkobjects.IVehicleGravity.maximum_degree
    :type: int

    Maximum degree to use in the gravity field when propagating the state error covariance matrix. Dimensionless.

.. py:property:: maximum_order
    :canonical: ansys.stk.core.stkobjects.IVehicleGravity.maximum_order
    :type: int

    Maximum order to use in the gravity field when propagating the state error covariance matrix. Dimensionless.


