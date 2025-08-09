ER3BPFunc
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.ER3BPFunc

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   ER3BP Function.

.. py:currentmodule:: ER3BPFunc

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.secondary_name`
              - Get or set the secondary body  which should be consistently defined with ER3BP model definitions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.ephemeris_epoch`
              - Get the epoch from which the eccentricity value is reported from the secondary.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.true_anomaly`
              - Get the true anomaly used for initializing ideal secondary.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.eccentricity`
              - Get the eccentricity at the reference epoch for the secondary's orbit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.mass_parameter`
              - Get the mass parameter computed from the primary and secondary bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.characteristic_distance`
              - Get the characteristic distance computed from the primary and secondary bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.characteristic_time`
              - Get the characteristic time computed from the primary and secondary bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.characteristic_velocity`
              - Get the characteristic velocity computed from the primary and secondary bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc.characteristic_acceleration`
              - Get the characteristic acceleration computed from the primary and secondary bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ER3BPFunc


Property detail
---------------

.. py:property:: secondary_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.secondary_name
    :type: str

    Get or set the secondary body  which should be consistently defined with ER3BP model definitions.

.. py:property:: ephemeris_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.ephemeris_epoch
    :type: typing.Any

    Get the epoch from which the eccentricity value is reported from the secondary.

.. py:property:: true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.true_anomaly
    :type: typing.Any

    Get the true anomaly used for initializing ideal secondary.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.eccentricity
    :type: float

    Get the eccentricity at the reference epoch for the secondary's orbit.

.. py:property:: mass_parameter
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.mass_parameter
    :type: float

    Get the mass parameter computed from the primary and secondary bodies.

.. py:property:: characteristic_distance
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.characteristic_distance
    :type: float

    Get the characteristic distance computed from the primary and secondary bodies.

.. py:property:: characteristic_time
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.characteristic_time
    :type: float

    Get the characteristic time computed from the primary and secondary bodies.

.. py:property:: characteristic_velocity
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.characteristic_velocity
    :type: float

    Get the characteristic velocity computed from the primary and secondary bodies.

.. py:property:: characteristic_acceleration
    :canonical: ansys.stk.core.stkobjects.astrogator.ER3BPFunc.characteristic_acceleration
    :type: float

    Get the characteristic acceleration computed from the primary and secondary bodies.


