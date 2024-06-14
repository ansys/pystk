IRadiationPressureFunction
==========================

.. py:class:: IRadiationPressureFunction

   object
   
   Properties for the Radiation Pressure propagator function.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~include_albedo`
            * - :py:meth:`~include_thermal_radiation_pressure`
            * - :py:meth:`~ground_reflection_model_filename`
            * - :py:meth:`~central_body_name`
            * - :py:meth:`~override_segment_settings`
            * - :py:meth:`~rad_pressure_coeff`
            * - :py:meth:`~rad_pressure_area`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IRadiationPressureFunction


Property detail
---------------

.. py:property:: include_albedo
    :canonical: ansys.stk.core.stkobjects.astrogator.IRadiationPressureFunction.include_albedo
    :type: bool

    True if including accelerations derived from albedo (reflected sunlight radiation from the central body).

.. py:property:: include_thermal_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.IRadiationPressureFunction.include_thermal_radiation_pressure
    :type: bool

    True if including accelerations derived from thermal radiation pressure from the central body.

.. py:property:: ground_reflection_model_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IRadiationPressureFunction.ground_reflection_model_filename
    :type: str

    A file containing a ground reflection model used for albedo and thermal radiation pressure.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IRadiationPressureFunction.central_body_name
    :type: str

    Name of the central body.

.. py:property:: override_segment_settings
    :canonical: ansys.stk.core.stkobjects.astrogator.IRadiationPressureFunction.override_segment_settings
    :type: bool

    True to use Ck and area values defined on this component for radiation pressure computations, rather than those defined in the MCS segments.

.. py:property:: rad_pressure_coeff
    :canonical: ansys.stk.core.stkobjects.astrogator.IRadiationPressureFunction.rad_pressure_coeff
    :type: float

    Coefficient, Ck, for use with radiation pressure computation.

.. py:property:: rad_pressure_area
    :canonical: ansys.stk.core.stkobjects.astrogator.IRadiationPressureFunction.rad_pressure_area
    :type: float

    Area to be used for radiation pressure computations. Small area dimension.


