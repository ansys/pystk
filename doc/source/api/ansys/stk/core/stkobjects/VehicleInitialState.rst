VehicleInitialState
===================

.. py:class:: ansys.stk.core.stkobjects.VehicleInitialState

   Class defining the initial state of the vehicle.

.. py:currentmodule:: VehicleInitialState

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleInitialState.representation`
              - Representation.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleInitialState.propagation_frame`
              - This property is deprecated. Use Two-body, J2 and J4 propagators to configure propagation frame. The propagation frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleInitialState.supported_propagation_frames`
              - This property is deprecated. Use Two-body, J2 and J4 propagators to get a list of supported propagation frames. Returns supported propagation frames.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleInitialState.orbit_epoch`
              - Get the smart epoch component to configure the orbit state epoch.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleInitialState


Property detail
---------------

.. py:property:: representation
    :canonical: ansys.stk.core.stkobjects.VehicleInitialState.representation
    :type: IOrbitState

    Representation.

.. py:property:: propagation_frame
    :canonical: ansys.stk.core.stkobjects.VehicleInitialState.propagation_frame
    :type: VehiclePropagationFrame

    This property is deprecated. Use Two-body, J2 and J4 propagators to configure propagation frame. The propagation frame.

.. py:property:: supported_propagation_frames
    :canonical: ansys.stk.core.stkobjects.VehicleInitialState.supported_propagation_frames
    :type: list

    This property is deprecated. Use Two-body, J2 and J4 propagators to get a list of supported propagation frames. Returns supported propagation frames.

.. py:property:: orbit_epoch
    :canonical: ansys.stk.core.stkobjects.VehicleInitialState.orbit_epoch
    :type: ITimeToolInstantSmartEpoch

    Get the smart epoch component to configure the orbit state epoch.


