IDesignER3BPSetup
=================

.. py:class:: IDesignER3BPSetup

   object
   
   Properties for the ER3BP Setup Tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create_ideal_secondary_cb`
              - Construct the idealized secondary for the three-body system.
            * - :py:meth:`~reset_ideal_secondary_cb`
              - Reset the idealized secondary for the three-body system.
            * - :py:meth:`~update_ideal_secondary_cb`
              - Update the idealized secondary for the three-body system.
            * - :py:meth:`~create_rotating_coordinate_system`
              - Create the coordinate system for the RotatingSystemChoice selection.
            * - :py:meth:`~delete_rotating_coordinate_system`
              - Delete the coordinate system for the RotatingSystemChoice selection.
            * - :py:meth:`~create_calculation_objects`
              - Create the calculation objects for the selected coordinate system.
            * - :py:meth:`~delete_calculation_objects`
              - Delete the calculation objects for the selected coordinate system.
            * - :py:meth:`~create_propagator`
              - Create the propagator for the primary-secondary ER3BP formulation.
            * - :py:meth:`~delete_propagator`
              - Delete the propagator for the primary-secondary ER3BP formulation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~secondary_body_name`
            * - :py:meth:`~initial_epoch`
            * - :py:meth:`~true_anomaly`
            * - :py:meth:`~ideal_secondary_name`
            * - :py:meth:`~mass_parameter`
            * - :py:meth:`~eccentricity`
            * - :py:meth:`~characteristic_distance`
            * - :py:meth:`~characteristic_time`
            * - :py:meth:`~characteristic_velocity`
            * - :py:meth:`~characteristic_acceleration`
            * - :py:meth:`~rotating_system_choice`
            * - :py:meth:`~associated_objects`
            * - :py:meth:`~include_stm`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IDesignER3BPSetup


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.central_body_name
    :type: str

    Primary central body for the three-body system.

.. py:property:: secondary_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.secondary_body_name
    :type: str

    Secondary Body.

.. py:property:: initial_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.initial_epoch
    :type: typing.Any

    Date and time for system construction.

.. py:property:: true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.true_anomaly
    :type: typing.Any

    True anomaly for initializing ideal secondary.

.. py:property:: ideal_secondary_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.ideal_secondary_name
    :type: str

    Name to be used for the idealized secondary.

.. py:property:: mass_parameter
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.mass_parameter
    :type: float

    Get the mass parameter computed from the primary and secondary bodies.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.eccentricity
    :type: float

    Get the eccentricity at epoch to be used for constructing the orbit of the secondary body.

.. py:property:: characteristic_distance
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.characteristic_distance
    :type: float

    Get the characteristic distance computed from the primary and secondary bodies.

.. py:property:: characteristic_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.characteristic_time
    :type: float

    Get the characteristic time computed from the primary and secondary bodies.

.. py:property:: characteristic_velocity
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.characteristic_velocity
    :type: float

    Get the characteristic velocity computed from the primary and secondary bodies.

.. py:property:: characteristic_acceleration
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.characteristic_acceleration
    :type: float

    Get the characteristic acceleration computed from the primary and secondary bodies.

.. py:property:: rotating_system_choice
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.rotating_system_choice
    :type: "ROTATING_COORDINATE_SYSTEM"

    Get the rotating coordinate system and associated calculation objects to interact with.

.. py:property:: associated_objects
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.associated_objects
    :type: "IAgVADesignER3BPObjectCollection"

    Get the list of associated objects.

.. py:property:: include_stm
    :canonical: ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup.include_stm
    :type: bool

    Get whether or not the STM propagator function is included on the propagator.


Method detail
-------------



















.. py:method:: create_ideal_secondary_cb(self) -> None

    Construct the idealized secondary for the three-body system.

    :Returns:

        :obj:`~None`

.. py:method:: reset_ideal_secondary_cb(self) -> None

    Reset the idealized secondary for the three-body system.

    :Returns:

        :obj:`~None`

.. py:method:: update_ideal_secondary_cb(self) -> None

    Update the idealized secondary for the three-body system.

    :Returns:

        :obj:`~None`

.. py:method:: create_rotating_coordinate_system(self) -> None

    Create the coordinate system for the RotatingSystemChoice selection.

    :Returns:

        :obj:`~None`

.. py:method:: delete_rotating_coordinate_system(self) -> None

    Delete the coordinate system for the RotatingSystemChoice selection.

    :Returns:

        :obj:`~None`

.. py:method:: create_calculation_objects(self) -> None

    Create the calculation objects for the selected coordinate system.

    :Returns:

        :obj:`~None`

.. py:method:: delete_calculation_objects(self) -> None

    Delete the calculation objects for the selected coordinate system.

    :Returns:

        :obj:`~None`




.. py:method:: create_propagator(self) -> None

    Create the propagator for the primary-secondary ER3BP formulation.

    :Returns:

        :obj:`~None`

.. py:method:: delete_propagator(self) -> None

    Delete the propagator for the primary-secondary ER3BP formulation.

    :Returns:

        :obj:`~None`

