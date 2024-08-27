VehicleGPSAutoUpdateOnlineSource
================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGPSAutoUpdateOnlineSource

   GPS automatic updates using online source (AGI server).

.. py:currentmodule:: VehicleGPSAutoUpdateOnlineSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateOnlineSource.preview`
              - Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGPSAutoUpdateOnlineSource



Method detail
-------------

.. py:method:: preview(self) -> VehicleGPSElementCollection
    :canonical: ansys.stk.core.stkobjects.VehicleGPSAutoUpdateOnlineSource.preview

    Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    :Returns:

        :obj:`~VehicleGPSElementCollection`

