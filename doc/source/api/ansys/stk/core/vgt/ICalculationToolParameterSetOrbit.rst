ICalculationToolParameterSetOrbit
=================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolParameterSetOrbit

   object
   
   Orbit parameter set contains various trajectory representations of an orbiting point.

.. py:currentmodule:: ICalculationToolParameterSetOrbit

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.orbiting_point`
              - Get the point for which orbital parameters are computed.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.reference_system`
              - Get the reference system in which orbital parameters are computed. Only used if the option to specify reference system is selected.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.gravitational_parameter`
              - Get the gravitational parameter for the mass relative to which orbital parameters are computed. Only used if the option to specify gravitational parameter is selected.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.central_body`
              - Get the central body relative to which orbital parameters are computed.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.use_central_body_gravitational_parameter`
              - Get the option that determines whether to specify the gravitational parameter value or to inherit it from the central body.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.use_central_body_inertial`
              - Get the option that determines whether to specify the reference coordinate system or to the inherit inertial reference system from the central body.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolParameterSetOrbit


Property detail
---------------

.. py:property:: orbiting_point
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.orbiting_point
    :type: IVectorGeometryToolPoint

    Get the point for which orbital parameters are computed.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which orbital parameters are computed. Only used if the option to specify reference system is selected.

.. py:property:: gravitational_parameter
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.gravitational_parameter
    :type: float

    Get the gravitational parameter for the mass relative to which orbital parameters are computed. Only used if the option to specify gravitational parameter is selected.

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.central_body
    :type: str

    Get the central body relative to which orbital parameters are computed.

.. py:property:: use_central_body_gravitational_parameter
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.use_central_body_gravitational_parameter
    :type: bool

    Get the option that determines whether to specify the gravitational parameter value or to inherit it from the central body.

.. py:property:: use_central_body_inertial
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetOrbit.use_central_body_inertial
    :type: bool

    Get the option that determines whether to specify the reference coordinate system or to the inherit inertial reference system from the central body.


