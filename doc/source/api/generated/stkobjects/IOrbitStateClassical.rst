IOrbitStateClassical
====================

.. py:class:: IOrbitStateClassical

   IOrbitState
   
   Classical (Keplerian) coordinate type.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~coordinate_system_type`
            * - :py:meth:`~coordinate_system`
            * - :py:meth:`~size_shape_type`
            * - :py:meth:`~size_shape`
            * - :py:meth:`~orientation`
            * - :py:meth:`~location_type`
            * - :py:meth:`~location`
            * - :py:meth:`~supported_coordinate_system_types`
            * - :py:meth:`~state_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateClassical


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.coordinate_system_type
    :type: "COORDINATE_SYSTEM"

    Coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.coordinate_system
    :type: "IAgOrbitStateCoordinateSystem"

    Get the coordinate system and coordinate epoch.

.. py:property:: size_shape_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.size_shape_type
    :type: "CLASSICAL_SIZE_SHAPE"

    Gets or sets the pair of elements used for specifying orbit size and shape.

.. py:property:: size_shape
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.size_shape
    :type: "IAgClassicalSizeShape"

    Get the size and shape of the orbit.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.orientation
    :type: "IAgClassicalOrientation"

    Get the orbit orientation.

.. py:property:: location_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.location_type
    :type: "CLASSICAL_LOCATION"

    Gets or sets the element used for specifying spacecraft location in the orbit at epoch.

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.location
    :type: "IAgClassicalLocation"

    Get the location of the spacecraft in the orbit at epoch.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateClassical.state_epoch
    :type: "IAgCrdnEventSmartEpoch"

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


