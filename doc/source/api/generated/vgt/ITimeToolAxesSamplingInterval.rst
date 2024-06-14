ITimeToolAxesSamplingInterval
=============================

.. py:class:: ITimeToolAxesSamplingInterval

   object
   
   The interface represents an interval with the time, orientation and velocity arrays.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~times`
            * - :py:meth:`~quaternions`
            * - :py:meth:`~velocities`
            * - :py:meth:`~start`
            * - :py:meth:`~stop`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolAxesSamplingInterval


Property detail
---------------

.. py:property:: times
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingInterval.times
    :type: list

    A time array associated with the interval.

.. py:property:: quaternions
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingInterval.quaternions
    :type: list

    An array of 4-tuples each tuple representing the orientation of the axes as a quaternion (q1,q2,q3,q4).

.. py:property:: velocities
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingInterval.velocities
    :type: list

    An array of angular velocities.

.. py:property:: start
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingInterval.start
    :type: typing.Any

    The start time of the interval.

.. py:property:: stop
    :canonical: ansys.stk.core.vgt.ITimeToolAxesSamplingInterval.stop
    :type: typing.Any

    The stop time of the interval.


