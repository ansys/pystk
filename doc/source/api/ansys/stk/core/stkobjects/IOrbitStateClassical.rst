IOrbitStateClassical
====================

.. py:class:: ansys.stk.core.stkobjects.IOrbitStateClassical

   IOrbitState
   
   Classical (Keplerian) coordinate type.

.. py:currentmodule:: IOrbitStateClassical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.coordinate_system_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.coordinate_system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.size_shape_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.size_shape`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.orientation`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.location_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.location`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.supported_coordinate_system_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateClassical.state_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateClassical


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.coordinate_system
    :type: IOrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: size_shape_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.size_shape_type
    :type: CLASSICAL_SIZE_SHAPE

    Gets or sets the pair of elements used for specifying orbit size and shape.

.. py:property:: size_shape
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.size_shape
    :type: IClassicalSizeShape

    Get the size and shape of the orbit.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.orientation
    :type: IClassicalOrientation

    Get the orbit orientation.

.. py:property:: location_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.location_type
    :type: CLASSICAL_LOCATION

    Gets or sets the element used for specifying spacecraft location in the orbit at epoch.

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.location
    :type: IClassicalLocation

    Get the location of the spacecraft in the orbit at epoch.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.state_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


