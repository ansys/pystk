PropagatorSP3File
=================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSP3File

   SP3 file data.

.. py:currentmodule:: PropagatorSP3File

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3File.filename`
              - Get the file name.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3File.start_time`
              - Get the start time of the ephemeris interval. Uses DateFormat dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3File.stop_time`
              - Get the stop time of the ephemeris interval. Uses DateFormat dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3File.reference_time`
              - Get the reference time.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3File.step_size`
              - Get the step size.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3File.agency`
              - Get the agency identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3File.orbit_type`
              - Get the orbit size type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3File.available_identifiers`
              - A two-dimensional array of available satellite identifiers and their common names. Each array element contains the satellite identifier and its common name (if one is available).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSP3File


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3File.filename
    :type: str

    Get the file name.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3File.start_time
    :type: typing.Any

    Get the start time of the ephemeris interval. Uses DateFormat dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3File.stop_time
    :type: typing.Any

    Get the stop time of the ephemeris interval. Uses DateFormat dimension.

.. py:property:: reference_time
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3File.reference_time
    :type: typing.Any

    Get the reference time.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3File.step_size
    :type: float

    Get the step size.

.. py:property:: agency
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3File.agency
    :type: str

    Get the agency identifier.

.. py:property:: orbit_type
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3File.orbit_type
    :type: str

    Get the orbit size type.

.. py:property:: available_identifiers
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3File.available_identifiers
    :type: list

    A two-dimensional array of available satellite identifiers and their common names. Each array element contains the satellite identifier and its common name (if one is available).


