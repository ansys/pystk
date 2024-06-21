IVehiclePropagator11ParamDescriptor
===================================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor

   object
   
   11-Param file definition.

.. py:currentmodule:: IVehiclePropagator11ParamDescriptor

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.epoch`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.filename`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.satellite_identification`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.nominal_longitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lm0`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lm1`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lm2`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lonc`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lonc1`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lons`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lons1`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.latc`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.latc1`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lats`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lats1`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagator11ParamDescriptor


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.epoch
    :type: typing.Any

    Epoch time on which the ephemeris is based.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.filename
    :type: str

    11-Parameter file path.

.. py:property:: satellite_identification
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.satellite_identification
    :type: str

    Satellite identification.

.. py:property:: nominal_longitude
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.nominal_longitude
    :type: float

    GEO satellite's reference longitude. Uses LongitudeUnit.

.. py:property:: lm0
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lm0
    :type: float

    Mean longitude (East of Greenwich).

.. py:property:: lm1
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lm1
    :type: float

    Drift rate.

.. py:property:: lm2
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lm2
    :type: float

    Drift acceleration.

.. py:property:: lonc
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lonc
    :type: float

    Longitude oscillation: amplitude (cosine term). Uses AngleUnit.

.. py:property:: lonc1
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lonc1
    :type: float

    Longitude oscilation: rate of change (cosine term). Uses AngleUnit.

.. py:property:: lons
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lons
    :type: float

    Longitude oscillation: amplitude (sine term). Uses AngleUnit.

.. py:property:: lons1
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lons1
    :type: float

    Longitude oscilation: rate of change (sine term). Uses AngleUnit.

.. py:property:: latc
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.latc
    :type: float

    Latitude oscillation: amplitude (cosine term). Uses AngleUnit.

.. py:property:: latc1
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.latc1
    :type: float

    Latitude oscillation: rate of change (cosine term). Uses AngleUnit.

.. py:property:: lats
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lats
    :type: float

    Latitude oscillation: amplitude (sine term). Uses AngleUnit.

.. py:property:: lats1
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptor.lats1
    :type: float

    Latitude oscillation: rate of change (sine term). Uses AngleUnit.


