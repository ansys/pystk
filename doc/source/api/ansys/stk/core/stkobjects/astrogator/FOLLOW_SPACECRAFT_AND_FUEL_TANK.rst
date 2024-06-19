FOLLOW_SPACECRAFT_AND_FUEL_TANK
===============================

.. py:class:: FOLLOW_SPACECRAFT_AND_FUEL_TANK

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~SPECIFY`
              - Specify Spacecraft Configuration - manually define the spacecraft for this segment. Spacecraft physical parameters will become apparent on new tabs - Spacecraft Parameters and Fuel Tank.

            * - :py:attr:`~INHERIT`
              - Inherit Spacecraft Configuration From Previous Segment - the spacecraft will be defined by its configuration at the end of the previous segment. The configuration will not be changed by the Follow segment.

            * - :py:attr:`~LEADER`
              - Inherit Spacecraft Configuration From Leader - if leader is an Astrogator satellite, configuration will be defined by the leader's configuration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import FOLLOW_SPACECRAFT_AND_FUEL_TANK


