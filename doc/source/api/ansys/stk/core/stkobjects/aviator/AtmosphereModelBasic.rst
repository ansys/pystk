AtmosphereModelBasic
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic

   Class defining the basic atmosphere model.

.. py:currentmodule:: AtmosphereModelBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.name`
              - Gets or sets the name of the atmosphere model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.basic_model_type`
              - Gets or sets the type of basic atmosphere.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.use_non_standard_atmosphere`
              - Opt whether to use non standard atmosphere conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.temperature`
              - Gets or sets the sea-level temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.pressure`
              - Gets or sets the sea-level pressure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.density_altitude`
              - Get the sea-level density altitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AtmosphereModelBasic


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.name
    :type: str

    Gets or sets the name of the atmosphere model.

.. py:property:: basic_model_type
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.basic_model_type
    :type: ATMOSPHERE_MODEL

    Gets or sets the type of basic atmosphere.

.. py:property:: use_non_standard_atmosphere
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.use_non_standard_atmosphere
    :type: bool

    Opt whether to use non standard atmosphere conditions.

.. py:property:: temperature
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.temperature
    :type: float

    Gets or sets the sea-level temperature.

.. py:property:: pressure
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.pressure
    :type: float

    Gets or sets the sea-level pressure.

.. py:property:: density_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.density_altitude
    :type: float

    Get the sea-level density altitude.


