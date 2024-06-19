IVehicleInitialState
====================

.. py:class:: IVehicleInitialState

   object
   
   Propagator Initial State.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~representation`
            * - :py:meth:`~propagation_frame`
            * - :py:meth:`~supported_propagation_frames`
            * - :py:meth:`~orbit_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleInitialState


Property detail
---------------

.. py:property:: representation
    :canonical: ansys.stk.core.stkobjects.IVehicleInitialState.representation
    :type: IAgOrbitState

    Representation.

.. py:property:: propagation_frame
    :canonical: ansys.stk.core.stkobjects.IVehicleInitialState.propagation_frame
    :type: VEHICLE_PROPAGATION_FRAME

    This property is deprecated. Use Two-body, J2 and J4 propagators to configure propagation frame. The propagation frame.

.. py:property:: supported_propagation_frames
    :canonical: ansys.stk.core.stkobjects.IVehicleInitialState.supported_propagation_frames
    :type: list

    This property is deprecated. Use Two-body, J2 and J4 propagators to get a list of supported propagation frames. Returns supported propagation frames.

.. py:property:: orbit_epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleInitialState.orbit_epoch
    :type: IAgCrdnEventSmartEpoch

    Get the smart epoch component to configure the orbit state epoch.


