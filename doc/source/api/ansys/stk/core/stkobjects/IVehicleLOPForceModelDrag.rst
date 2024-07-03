IVehicleLOPForceModelDrag
=========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleLOPForceModelDrag

   object
   
   Interface for atmospheric drag for LOP propagator.

.. py:currentmodule:: IVehicleLOPForceModelDrag

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPForceModelDrag.use`
              - Opt whether to use drag parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPForceModelDrag.cd`
              - Gets or sets the atmospheric drag coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPForceModelDrag.advanced`
              - Get the advanced drag parameters.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleLOPForceModelDrag


Property detail
---------------

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModelDrag.use
    :type: bool

    Opt whether to use drag parameters.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModelDrag.cd
    :type: float

    Gets or sets the atmospheric drag coefficient. Dimensionless.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPForceModelDrag.advanced
    :type: IVehicleAdvanced

    Get the advanced drag parameters.


