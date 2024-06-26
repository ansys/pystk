ISRPGSPM04aeIIA
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA

   object
   
   Properties for the Bar-Sever GPS Solar Pressure Model 04ae for block IIA.

.. py:currentmodule:: ISRPGSPM04aeIIA

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.atmos_altitude`
              - Gets or sets the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.shadow_model`
              - Gets or sets the shadow model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.sun_position`
              - Gets or sets the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.eclipsing_bodies`
              - Other eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.include_boundary_mitigation`
              - True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.use_sun_central_body_file_values`
              - True if solar radius should come from the Sun.cb file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.solar_radius`
              - Gets or sets the solar radius value to use in eclipse calculations.  Uses Distance Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISRPGSPM04aeIIA


Property detail
---------------

.. py:property:: atmos_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.atmos_altitude
    :type: float

    Gets or sets the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.

.. py:property:: shadow_model
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.shadow_model
    :type: SHADOW_MODEL

    Gets or sets the shadow model type.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.eclipsing_bodies
    :type: ICentralBodyCollection

    Other eclipsing bodies.

.. py:property:: include_boundary_mitigation
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.include_boundary_mitigation
    :type: bool

    True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.

.. py:property:: use_sun_central_body_file_values
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.use_sun_central_body_file_values
    :type: bool

    True if solar radius should come from the Sun.cb file.

.. py:property:: solar_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA.solar_radius
    :type: float

    Gets or sets the solar radius value to use in eclipse calculations.  Uses Distance Dimension.


