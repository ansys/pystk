VehicleZonalPropagatorInitialState
==================================

.. py:class:: ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState

   Class defining initial state for the J2/4 propagators.

.. py:currentmodule:: VehicleZonalPropagatorInitialState

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.ellipse_options`
              - Options for modeling elliptical motion.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.representation`
              - Representation.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.propagation_frame`
              - Gets or sets the propagation frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.supported_propagation_frames`
              - Returns supported propagation frames.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.orbit_epoch`
              - Get the smart epoch component to configure the orbit state epoch.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleZonalPropagatorInitialState


Property detail
---------------

.. py:property:: ellipse_options
    :canonical: ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.ellipse_options
    :type: VehicleEllipseOptionType

    Options for modeling elliptical motion.

.. py:property:: representation
    :canonical: ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.representation
    :type: IOrbitState

    Representation.

.. py:property:: propagation_frame
    :canonical: ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.propagation_frame
    :type: VehiclePropagationFrame

    Gets or sets the propagation frame.

.. py:property:: supported_propagation_frames
    :canonical: ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.supported_propagation_frames
    :type: list

    Returns supported propagation frames.

.. py:property:: orbit_epoch
    :canonical: ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState.orbit_epoch
    :type: ITimeToolInstantSmartEpoch

    Get the smart epoch component to configure the orbit state epoch.


