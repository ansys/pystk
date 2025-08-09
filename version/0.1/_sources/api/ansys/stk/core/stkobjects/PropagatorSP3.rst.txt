PropagatorSP3
=============

.. py:class:: ansys.stk.core.stkobjects.PropagatorSP3

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).

.. py:currentmodule:: PropagatorSP3

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3.propagate`
              - Propagates the vehicle's path using the specified time interval.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3.interpolation_order`
              - An interpolation order of 1 specifies linear interpolation and is appropriate for closely spaced data or data with significant jitter. Higher interpolation orders yield more accurate interpolation when the data is smooth and continuous.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3.interpolation_method`
              - By default, the SP3 propagator uses the standard Lagrange interpolation scheme, interpolating position and velocity separately. Some files may be configured to allow the Hermitian interpolation.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3.interpolate_across_boundaries`
              - Whether to interpolate across file boundaries. If this option is set, STK will interpolate ephemeris steps according to the user-defined Step Size between the end of one SP3 file and the beginning of the next.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3.extrapolate_one_step_past_end`
              - Extrapolate 1 step beyond last data point. If this option is selected, STK will calculate an additional ephemeris step beyond the last data point provided by the SP3 file(s) assigned to the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3.satellite_identifier`
              - Get or set a selected satellite identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3.files`
              - Access and manipulate the collection of SP3 files. You can add multiple files to a single satellite object and - if there are no gaps between the files - the whole ephemeris will be propagated in sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3.available_identifiers`
              - An array of available satellite identifiers.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSP3


Property detail
---------------

.. py:property:: interpolation_order
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3.interpolation_order
    :type: int

    An interpolation order of 1 specifies linear interpolation and is appropriate for closely spaced data or data with significant jitter. Higher interpolation orders yield more accurate interpolation when the data is smooth and continuous.

.. py:property:: interpolation_method
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3.interpolation_method
    :type: VehicleInterpolationMethod

    By default, the SP3 propagator uses the standard Lagrange interpolation scheme, interpolating position and velocity separately. Some files may be configured to allow the Hermitian interpolation.

.. py:property:: interpolate_across_boundaries
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3.interpolate_across_boundaries
    :type: bool

    Whether to interpolate across file boundaries. If this option is set, STK will interpolate ephemeris steps according to the user-defined Step Size between the end of one SP3 file and the beginning of the next.

.. py:property:: extrapolate_one_step_past_end
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3.extrapolate_one_step_past_end
    :type: bool

    Extrapolate 1 step beyond last data point. If this option is selected, STK will calculate an additional ephemeris step beyond the last data point provided by the SP3 file(s) assigned to the satellite.

.. py:property:: satellite_identifier
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3.satellite_identifier
    :type: str

    Get or set a selected satellite identifier.

.. py:property:: files
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3.files
    :type: PropagatorSP3FileCollection

    Access and manipulate the collection of SP3 files. You can add multiple files to a single satellite object and - if there are no gaps between the files - the whole ephemeris will be propagated in sequence.

.. py:property:: available_identifiers
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3.available_identifiers
    :type: list

    An array of available satellite identifiers.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3.propagate

    Propagates the vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`













