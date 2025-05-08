TimeToolPointSamplingInterval
=============================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval

   The interface represents an interval with the time, position and velocity arrays.

.. py:currentmodule:: TimeToolPointSamplingInterval

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.times`
              - A time array associated with the interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.positions`
              - An array of 3-tuples each tuple representing the point's cartesian position (x,y,z).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.velocities`
              - An array of velocities.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.start`
              - The start time of the interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.stop`
              - The stop time of the interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolPointSamplingInterval


Property detail
---------------

.. py:property:: times
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.times
    :type: list

    A time array associated with the interval.

.. py:property:: positions
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.positions
    :type: list

    An array of 3-tuples each tuple representing the point's cartesian position (x,y,z).

.. py:property:: velocities
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.velocities
    :type: list

    An array of velocities.

.. py:property:: start
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.start
    :type: typing.Any

    The start time of the interval.

.. py:property:: stop
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval.stop
    :type: typing.Any

    The stop time of the interval.


