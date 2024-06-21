IAtmosphereModelBasic
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic

   object
   
   Interface used to access the basic atmosphere model.

.. py:currentmodule:: IAtmosphereModelBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.basic_model_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.use_non_standard_atmosphere`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.pressure`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.density_altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAtmosphereModelBasic


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.name
    :type: str

    Gets or sets the name of the atmosphere model.

.. py:property:: basic_model_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.basic_model_type
    :type: ATMOSPHERE_MODEL

    Gets or sets the type of basic atmosphere.

.. py:property:: use_non_standard_atmosphere
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.use_non_standard_atmosphere
    :type: bool

    Opt whether to use non standard atmosphere conditions.

.. py:property:: temperature
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.temperature
    :type: float

    Gets or sets the sea-level temperature.

.. py:property:: pressure
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.pressure
    :type: float

    Gets or sets the sea-level pressure.

.. py:property:: density_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAtmosphereModelBasic.density_altitude
    :type: float

    Get the sea-level density altitude.


