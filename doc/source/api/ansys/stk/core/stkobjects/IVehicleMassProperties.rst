IVehicleMassProperties
======================

.. py:class:: IVehicleMassProperties

   object
   
   Satellite Mass properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~mass`
            * - :py:meth:`~inertia`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleMassProperties


Property detail
---------------

.. py:property:: mass
    :canonical: ansys.stk.core.stkobjects.IVehicleMassProperties.mass
    :type: float

    Gets or sets the satellite mass. Uses Mass Dimension.

.. py:property:: inertia
    :canonical: ansys.stk.core.stkobjects.IVehicleMassProperties.inertia
    :type: "IAgVeInertia"

    Get the satellite inertia matrix.


