Propagator11ParametersDescriptor
================================

.. py:class:: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor

   11-Param file definition.

.. py:currentmodule:: Propagator11ParametersDescriptor

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.epoch`
              - Epoch time on which the ephemeris is based.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.filename`
              - 11-Parameter file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.satellite_identifier`
              - Satellite identification.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.nominal_longitude`
              - GEO satellite's reference longitude. Uses LongitudeUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lm0`
              - Mean longitude (East of Greenwich).
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lm1`
              - Drift rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lm2`
              - Drift acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lonc`
              - Longitude oscillation: amplitude (cosine term). Uses AngleUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lonc1`
              - Longitude oscilation: rate of change (cosine term). Uses AngleUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lons`
              - Longitude oscillation: amplitude (sine term). Uses AngleUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lons1`
              - Longitude oscilation: rate of change (sine term). Uses AngleUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.latc`
              - Latitude oscillation: amplitude (cosine term). Uses AngleUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.latc1`
              - Latitude oscillation: rate of change (cosine term). Uses AngleUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lats`
              - Latitude oscillation: amplitude (sine term). Uses AngleUnit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lats1`
              - Latitude oscillation: rate of change (sine term). Uses AngleUnit.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Propagator11ParametersDescriptor


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.epoch
    :type: typing.Any

    Epoch time on which the ephemeris is based.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.filename
    :type: str

    11-Parameter file path.

.. py:property:: satellite_identifier
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.satellite_identifier
    :type: str

    Satellite identification.

.. py:property:: nominal_longitude
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.nominal_longitude
    :type: float

    GEO satellite's reference longitude. Uses LongitudeUnit.

.. py:property:: lm0
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lm0
    :type: float

    Mean longitude (East of Greenwich).

.. py:property:: lm1
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lm1
    :type: float

    Drift rate.

.. py:property:: lm2
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lm2
    :type: float

    Drift acceleration.

.. py:property:: lonc
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lonc
    :type: float

    Longitude oscillation: amplitude (cosine term). Uses AngleUnit.

.. py:property:: lonc1
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lonc1
    :type: float

    Longitude oscilation: rate of change (cosine term). Uses AngleUnit.

.. py:property:: lons
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lons
    :type: float

    Longitude oscillation: amplitude (sine term). Uses AngleUnit.

.. py:property:: lons1
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lons1
    :type: float

    Longitude oscilation: rate of change (sine term). Uses AngleUnit.

.. py:property:: latc
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.latc
    :type: float

    Latitude oscillation: amplitude (cosine term). Uses AngleUnit.

.. py:property:: latc1
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.latc1
    :type: float

    Latitude oscillation: rate of change (cosine term). Uses AngleUnit.

.. py:property:: lats
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lats
    :type: float

    Latitude oscillation: amplitude (sine term). Uses AngleUnit.

.. py:property:: lats1
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptor.lats1
    :type: float

    Latitude oscillation: rate of change (sine term). Uses AngleUnit.


