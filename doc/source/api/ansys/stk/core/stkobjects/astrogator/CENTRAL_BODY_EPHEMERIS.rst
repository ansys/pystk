CENTRAL_BODY_EPHEMERIS
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CENTRAL_BODY_EPHEMERIS

   IntEnum


.. py:currentmodule:: CENTRAL_BODY_EPHEMERIS

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ANALYTIC_ORBIT`
              - Specified values and rates of change for the classical orbital elements.

            * - :py:attr:`~FILE`
              - An external ephemeris (.e) file.

            * - :py:attr:`~JPLDE`
              - Ephemerides from the Jet Propulsion Laboratory's JPL DE set are used.

            * - :py:attr:`~JPLSPICE`
              - The SPICE propagator reads ephemeris from binary files that are in a standard format produced by the Jet Propulsion Laboratory for ephemeris for celestial bodies but can be used for spacecraft.

            * - :py:attr:`~PLANETARY`
              - A planetary ephemeris (.pe) file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CENTRAL_BODY_EPHEMERIS


