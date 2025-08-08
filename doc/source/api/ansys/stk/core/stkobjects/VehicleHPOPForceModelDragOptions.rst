VehicleHPOPForceModelDragOptions
================================

.. py:class:: ansys.stk.core.stkobjects.VehicleHPOPForceModelDragOptions

   Class defining HPOP atmospheric drag options.

.. py:currentmodule:: VehicleHPOPForceModelDragOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDragOptions.use_apparent_sun_position`
              - Opt whether to use the apparent position of the sun; otherwise, the true position of the sun is used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDragOptions.use_approx_altitude`
              - Opt whether to have the drag model use an approximate expression to determine altitude, instead of finding the exact altitude, when computing density.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleHPOPForceModelDragOptions


Property detail
---------------

.. py:property:: use_apparent_sun_position
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDragOptions.use_apparent_sun_position
    :type: bool

    Opt whether to use the apparent position of the sun; otherwise, the true position of the sun is used.

.. py:property:: use_approx_altitude
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDragOptions.use_approx_altitude
    :type: bool

    Opt whether to have the drag model use an approximate expression to determine altitude, instead of finding the exact altitude, when computing density.


