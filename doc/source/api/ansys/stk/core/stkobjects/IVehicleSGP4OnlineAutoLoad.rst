IVehicleSGP4OnlineAutoLoad
==========================

.. py:class:: IVehicleSGP4OnlineAutoLoad

   IVehicleSGP4LoadData
   
   Do not use this interface, as it is deprecated. Use IAgVeSGP4OnlineLoad instead. Interface for SGP4 propagator. Loads the most current segment from online.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add_latest_seg_from_online`
              - Do not use this method, as it is deprecated. Use AddSegsFromOnline on IAgVeSGP4OnlineLoad instead. Adds the latest segment from Online given an SSC number.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSGP4OnlineAutoLoad



Method detail
-------------

.. py:method:: add_latest_seg_from_online(self, sSCNumber: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4OnlineAutoLoad.add_latest_seg_from_online

    Do not use this method, as it is deprecated. Use AddSegsFromOnline on IAgVeSGP4OnlineLoad instead. Adds the latest segment from Online given an SSC number.

    :Parameters:

    **sSCNumber** : :obj:`~str`

    :Returns:

        :obj:`~None`

