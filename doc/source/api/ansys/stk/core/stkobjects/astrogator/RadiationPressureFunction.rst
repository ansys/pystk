RadiationPressureFunction
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Radiation Pressure Propagator Function.

.. py:currentmodule:: RadiationPressureFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction.central_body_name`
              - Name of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction.ground_reflection_model_filename`
              - A file containing a ground reflection model used for albedo and thermal radiation pressure.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction.include_albedo`
              - True if including accelerations derived from albedo (reflected sunlight radiation from the central body).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction.include_thermal_radiation_pressure`
              - True if including accelerations derived from thermal radiation pressure from the central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import RadiationPressureFunction


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction.central_body_name
    :type: str

    Name of the central body.

.. py:property:: ground_reflection_model_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction.ground_reflection_model_filename
    :type: str

    A file containing a ground reflection model used for albedo and thermal radiation pressure.

.. py:property:: include_albedo
    :canonical: ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction.include_albedo
    :type: bool

    True if including accelerations derived from albedo (reflected sunlight radiation from the central body).

.. py:property:: include_thermal_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction.include_thermal_radiation_pressure
    :type: bool

    True if including accelerations derived from thermal radiation pressure from the central body.


