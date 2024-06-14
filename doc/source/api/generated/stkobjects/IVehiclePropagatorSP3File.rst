IVehiclePropagatorSP3File
=========================

.. py:class:: IVehiclePropagatorSP3File

   object
   
   SP3 file data.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filename`
            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~reference_time`
            * - :py:meth:`~step_size`
            * - :py:meth:`~agency`
            * - :py:meth:`~orbit_type`
            * - :py:meth:`~available_identifiers`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorSP3File


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSP3File.filename
    :type: str

    Get the file name.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSP3File.start_time
    :type: typing.Any

    Get the start time of the ephemeris interval. Uses DateFormat dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSP3File.stop_time
    :type: typing.Any

    Get the stop time of the ephemeris interval. Uses DateFormat dimension.

.. py:property:: reference_time
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSP3File.reference_time
    :type: typing.Any

    Get the reference time.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSP3File.step_size
    :type: float

    Get the step size.

.. py:property:: agency
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSP3File.agency
    :type: str

    Get the agency identifier.

.. py:property:: orbit_type
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSP3File.orbit_type
    :type: str

    Get the orbit size type.

.. py:property:: available_identifiers
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSP3File.available_identifiers
    :type: list

    A two-dimensional array of available satellite identifiers and their common names. Each array element contains the satellite identifier and its common name (if one is available).


