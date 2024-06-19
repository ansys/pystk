ISRPAeroT20
===========

.. py:class:: ISRPAeroT20

   object
   
   Properties for the Aerospace T20 solar radiation pressure model for GPS block IIA.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~atmos_altitude`
            * - :py:meth:`~shadow_model`
            * - :py:meth:`~sun_position`
            * - :py:meth:`~eclipsing_bodies`
            * - :py:meth:`~include_boundary_mitigation`
            * - :py:meth:`~use_sun_central_body_file_values`
            * - :py:meth:`~solar_radius`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISRPAeroT20


Property detail
---------------

.. py:property:: atmos_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPAeroT20.atmos_altitude
    :type: float

    Gets or sets the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.

.. py:property:: shadow_model
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPAeroT20.shadow_model
    :type: SHADOW_MODEL

    Gets or sets the shadow model type.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPAeroT20.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPAeroT20.eclipsing_bodies
    :type: IAgVACentralBodyCollection

    Other eclipsing bodies.

.. py:property:: include_boundary_mitigation
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPAeroT20.include_boundary_mitigation
    :type: bool

    True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.

.. py:property:: use_sun_central_body_file_values
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPAeroT20.use_sun_central_body_file_values
    :type: bool

    True if solar radius should come from the Sun.cb file.

.. py:property:: solar_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPAeroT20.solar_radius
    :type: float

    Gets or sets the solar radius value to use in eclipse calculations.  Uses Distance Dimension.


