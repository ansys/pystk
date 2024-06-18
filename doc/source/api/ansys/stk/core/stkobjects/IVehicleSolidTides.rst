IVehicleSolidTides
==================

.. py:class:: IVehicleSolidTides

   object
   
   Interface for additional force model options related to solid tides.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~inc_time_dep_solid_tides`
            * - :py:meth:`~min_amplitude`
            * - :py:meth:`~truncate_solid_tides`


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


