IVehicleSolidTides
==================

.. py:class:: ansys.stk.core.stkobjects.IVehicleSolidTides

   object
   
   Interface for additional force model options related to solid tides.

.. py:currentmodule:: IVehicleSolidTides

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSolidTides.inc_time_dep_solid_tides`
              - Time-dependent solid tide effects: opt whether to account for the secondary contribution from certain effects of loading the crust and core.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSolidTides.min_amplitude`
              - Minimum tidal amplitude to include in the computation. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSolidTides.truncate_solid_tides`
              - True if solid tide terms (including permanent tide) won't be included beyond the degree and order selected for the gravity model.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSolidTides


Property detail
---------------

.. py:property:: inc_time_dep_solid_tides
    :canonical: ansys.stk.core.stkobjects.IVehicleSolidTides.inc_time_dep_solid_tides
    :type: bool

    Time-dependent solid tide effects: opt whether to account for the secondary contribution from certain effects of loading the crust and core.

.. py:property:: min_amplitude
    :canonical: ansys.stk.core.stkobjects.IVehicleSolidTides.min_amplitude
    :type: float

    Minimum tidal amplitude to include in the computation. Uses SmallDistanceUnit Dimension.

.. py:property:: truncate_solid_tides
    :canonical: ansys.stk.core.stkobjects.IVehicleSolidTides.truncate_solid_tides
    :type: bool

    True if solid tide terms (including permanent tide) won't be included beyond the degree and order selected for the gravity model.


