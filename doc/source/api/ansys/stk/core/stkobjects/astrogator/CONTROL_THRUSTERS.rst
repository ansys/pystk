CONTROL_THRUSTERS
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CONTROL_THRUSTERS

   IntEnum


.. py:currentmodule:: CONTROL_THRUSTERS

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EQUIV_ON_TIME`
              - The equivalent on-time percentage is a factor multiplied by the thrust. The thrust is applied continuously throughout the maneuver and is reduced by the percentage. The mass flow rate is likewise reduced.

            * - :py:attr:`~THRUST_EFFICIENCY`
              - The thruster efficiency.

            * - :py:attr:`~SPHERICAL_AZIMUTH`
              - Thruster direction defined as a vector in the body frame. Spherical azimuth value.

            * - :py:attr:`~SPHERICAL_ELEVATION`
              - Thruster direction defined as a vector in the body frame. Spherical elevation value.

            * - :py:attr:`~CARTESIAN_X`
              - Thruster direction defined as a vector in the body frame. Cartesian X value.

            * - :py:attr:`~CARTESIAN_Y`
              - Thruster direction defined as a vector in the body frame. Cartesian Y value.

            * - :py:attr:`~CARTESIAN_Z`
              - Thruster direction defined as a vector in the body frame. Cartesian Z value.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CONTROL_THRUSTERS


