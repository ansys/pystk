IVehicleHPOPForceModelDragOptions
=================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDragOptions

   object
   
   Interface for additional options for atmospheric drag.

.. py:currentmodule:: IVehicleHPOPForceModelDragOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDragOptions.use_approx_altitude`
              - Opt whether to have the drag model use an approximate expression to determine altitude, instead of finding the exact altitude, when computing density.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDragOptions.use_apparent_sun_position`
              - Opt whether to use the apparent position of the sun; otherwise, the true position of the sun is used.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPForceModelDragOptions


Property detail
---------------

.. py:property:: use_approx_altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDragOptions.use_approx_altitude
    :type: bool

    Opt whether to have the drag model use an approximate expression to determine altitude, instead of finding the exact altitude, when computing density.

.. py:property:: use_apparent_sun_position
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDragOptions.use_apparent_sun_position
    :type: bool

    Opt whether to use the apparent position of the sun; otherwise, the true position of the sun is used.


