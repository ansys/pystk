EphemSourceType
===============

.. py:class:: ansys.stk.core.stkobjects.EphemSourceType

   IntEnum


.. py:currentmodule:: EphemSourceType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ANALYTIC`
              - Analytic ephemeris: use an analytic propagator. Available when orbital elements are known for the Central Body about its parent.

            * - :py:attr:`~DEFAULT`
              - Default: use STK's internal definition of the Central Body to generate ephemeris. By default, STK's internal definition uses the DE file if available.

            * - :py:attr:`~SPICE`
              - SPICE: use the SPICE toolkit to generate ephemeris. Available only if a SPICE ephemeris file (.bsp) has been loaded for the selected planet.

            * - :py:attr:`~JPL_DEVELOPMENTAL_EPHEMERIS`
              - Default JPL DE file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import EphemSourceType


