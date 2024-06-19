IVehiclePropagatorSGP4CommonTasks
=================================

.. py:class:: IVehiclePropagatorSGP4CommonTasks

   object
   
   Interface provides methods encapsulating most commonly used functionality when working with SGP4 propagator.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add_segs_from_file`
              - Search the specified file for elements matching the specified SSC number and adds them to the collection.
            * - :py:meth:`~add_segs_from_online_source`
              - Search the online source (AGI server) for elements matching the specified SSC number and adds them to the collection. The method uses the propagator's start/stop.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorSGP4CommonTasks



Method detail
-------------

.. py:method:: add_segs_from_file(self, sSCNumber: str, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4CommonTasks.add_segs_from_file

    Search the specified file for elements matching the specified SSC number and adds them to the collection.

    :Parameters:

    **sSCNumber** : :obj:`~str`
    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_segs_from_online_source(self, SSCNum: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4CommonTasks.add_segs_from_online_source

    Search the online source (AGI server) for elements matching the specified SSC number and adds them to the collection. The method uses the propagator's start/stop.

    :Parameters:

    **SSCNum** : :obj:`~str`

    :Returns:

        :obj:`~None`

