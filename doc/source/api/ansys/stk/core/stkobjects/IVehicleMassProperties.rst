IVehicleMassProperties
======================

.. py:class:: ansys.stk.core.stkobjects.IVehicleMassProperties

   object
   
   Satellite Mass properties.

.. py:currentmodule:: IVehicleMassProperties

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleMassProperties.mass`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleMassProperties.inertia`


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
    :type: IVehicleInertia

    Get the satellite inertia matrix.


