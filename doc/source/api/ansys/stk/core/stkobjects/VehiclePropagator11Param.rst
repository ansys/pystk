VehiclePropagator11Param
========================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagator11Param

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

.. py:currentmodule:: VehiclePropagator11Param

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11Param.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11Param.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11Param.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11Param.parameter_files`
              - Returns a collection of 11-Parameter satellite definitions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagator11Param


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11Param.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11Param.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: parameter_files
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11Param.parameter_files
    :type: VehiclePropagator11ParamDescriptorCollection

    Returns a collection of 11-Parameter satellite definitions.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11Param.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`





