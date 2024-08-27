OrbitStateClassical
===================

.. py:class:: ansys.stk.core.stkobjects.OrbitStateClassical

   Bases: :py:class:`~ansys.stk.core.stkobjects.IOrbitState`

   Classical (Keplerian) coordinate type.

.. py:currentmodule:: OrbitStateClassical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.coordinate_system_type`
              - Coordinate system being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.coordinate_system`
              - Get the coordinate system and coordinate epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.size_shape_type`
              - Gets or sets the pair of elements used for specifying orbit size and shape.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.size_shape`
              - Get the size and shape of the orbit.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.orientation`
              - Get the orbit orientation.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.location_type`
              - Gets or sets the element used for specifying spacecraft location in the orbit at epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.location`
              - Get the location of the spacecraft in the orbit at epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.supported_coordinate_system_types`
              - Returns an array of supported coordinate system types.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateClassical.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OrbitStateClassical


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: size_shape_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.size_shape_type
    :type: CLASSICAL_SIZE_SHAPE

    Gets or sets the pair of elements used for specifying orbit size and shape.

.. py:property:: size_shape
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.size_shape
    :type: IClassicalSizeShape

    Get the size and shape of the orbit.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.orientation
    :type: ClassicalOrientation

    Get the orbit orientation.

.. py:property:: location_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.location_type
    :type: CLASSICAL_LOCATION

    Gets or sets the element used for specifying spacecraft location in the orbit at epoch.

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.location
    :type: IClassicalLocation

    Get the location of the spacecraft in the orbit at epoch.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.OrbitStateClassical.state_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


