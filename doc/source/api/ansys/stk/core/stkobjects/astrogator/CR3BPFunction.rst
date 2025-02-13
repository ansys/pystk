CR3BPFunction
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.CR3BPFunction

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   CR3BP Function.

.. py:currentmodule:: CR3BPFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction.secondary_name`
              - Get or set the secondary body  which should be consistently defined with CR3BP model definitions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction.ephemeris_epoch`
              - Get the epoch from which the eccentricity value is reported from the secondary.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction.eccentricity`
              - Get the eccentricity at the reference epoch for the secondary's orbit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction.mass_parameter`
              - Get the mass parameter computed from the primary and secondary bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction.characteristic_distance`
              - Get the characteristic distance computed from the primary and secondary bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction.characteristic_time`
              - Get the characteristic time computed from the primary and secondary bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction.characteristic_velocity`
              - Get the characteristic velocity computed from the primary and secondary bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction.characteristic_acceleration`
              - Get the characteristic acceleration computed from the primary and secondary bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CR3BPFunction


Property detail
---------------

.. py:property:: secondary_name
    :canonical: ansys.stk.core.stkobjects.astrogator.CR3BPFunction.secondary_name
    :type: str

    Get or set the secondary body  which should be consistently defined with CR3BP model definitions.

.. py:property:: ephemeris_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.CR3BPFunction.ephemeris_epoch
    :type: typing.Any

    Get the epoch from which the eccentricity value is reported from the secondary.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.CR3BPFunction.eccentricity
    :type: float

    Get the eccentricity at the reference epoch for the secondary's orbit.

.. py:property:: mass_parameter
    :canonical: ansys.stk.core.stkobjects.astrogator.CR3BPFunction.mass_parameter
    :type: float

    Get the mass parameter computed from the primary and secondary bodies.

.. py:property:: characteristic_distance
    :canonical: ansys.stk.core.stkobjects.astrogator.CR3BPFunction.characteristic_distance
    :type: float

    Get the characteristic distance computed from the primary and secondary bodies.

.. py:property:: characteristic_time
    :canonical: ansys.stk.core.stkobjects.astrogator.CR3BPFunction.characteristic_time
    :type: float

    Get the characteristic time computed from the primary and secondary bodies.

.. py:property:: characteristic_velocity
    :canonical: ansys.stk.core.stkobjects.astrogator.CR3BPFunction.characteristic_velocity
    :type: float

    Get the characteristic velocity computed from the primary and secondary bodies.

.. py:property:: characteristic_acceleration
    :canonical: ansys.stk.core.stkobjects.astrogator.CR3BPFunction.characteristic_acceleration
    :type: float

    Get the characteristic acceleration computed from the primary and secondary bodies.


