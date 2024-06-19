IVehicleLOPForceModelDrag
=========================

.. py:class:: IVehicleLOPForceModelDrag

   object
   
   Interface for atmospheric drag for LOP propagator.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use`
            * - :py:meth:`~cd`
            * - :py:meth:`~advanced`


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
    :type: IAgVeAdvanced

    Get the advanced drag parameters.


