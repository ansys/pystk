IVehicleGPSAutoUpdateOnlineSource
=================================

.. py:class:: IVehicleGPSAutoUpdateOnlineSource

   object
   
   Interface to configure the GPS automatic updates using online source (AGI server).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~preview`
              - Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGPSAutoUpdateOnlineSource



Method detail
-------------

.. py:method:: preview(self) -> IVehicleGPSElementCollection
    :canonical: ansys.stk.core.stkobjects.IVehicleGPSAutoUpdateOnlineSource.preview

    Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    :Returns:

        :obj:`~IVehicleGPSElementCollection`

