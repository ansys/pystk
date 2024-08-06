TimeToolAxesSamplingInterval
============================

.. py:class:: ansys.stk.core.vgt.TimeToolAxesSamplingInterval

   The interface represents an interval with the time, orientation and velocity arrays.

.. py:currentmodule:: TimeToolAxesSamplingInterval

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolAxesSamplingInterval.times`
              - A time array associated with the interval.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolAxesSamplingInterval.quaternions`
              - An array of 4-tuples each tuple representing the orientation of the axes as a quaternion (q1,q2,q3,q4).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolAxesSamplingInterval.velocities`
              - An array of angular velocities.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolAxesSamplingInterval.start`
              - The start time of the interval.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolAxesSamplingInterval.stop`
              - The stop time of the interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolAxesSamplingInterval


Property detail
---------------

.. py:property:: times
    :canonical: ansys.stk.core.vgt.TimeToolAxesSamplingInterval.times
    :type: list

    A time array associated with the interval.

.. py:property:: quaternions
    :canonical: ansys.stk.core.vgt.TimeToolAxesSamplingInterval.quaternions
    :type: list

    An array of 4-tuples each tuple representing the orientation of the axes as a quaternion (q1,q2,q3,q4).

.. py:property:: velocities
    :canonical: ansys.stk.core.vgt.TimeToolAxesSamplingInterval.velocities
    :type: list

    An array of angular velocities.

.. py:property:: start
    :canonical: ansys.stk.core.vgt.TimeToolAxesSamplingInterval.start
    :type: typing.Any

    The start time of the interval.

.. py:property:: stop
    :canonical: ansys.stk.core.vgt.TimeToolAxesSamplingInterval.stop
    :type: typing.Any

    The stop time of the interval.


