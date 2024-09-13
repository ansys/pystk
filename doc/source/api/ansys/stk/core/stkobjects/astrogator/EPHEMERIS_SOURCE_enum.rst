EPHEMERIS_SOURCE
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.EPHEMERIS_SOURCE

   IntEnum


.. py:currentmodule:: EPHEMERIS_SOURCE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CENTRAL_BODY_FILE`
              - The Cb file provided with STK; uses the default ephemeris source for that central body.

            * - :py:attr:`~DESIGN_EXPLORER_OPTIMIZER_FILE`
              - A DE file; body centered for the inner planets and barycentered for the outer planets.

            * - :py:attr:`~SPICE_BARY`
              - A SPICE file, barycentered; uses the entire planetary system as a single effect, with the system center as the point mass.

            * - :py:attr:`~SPICE_BODY`
              - A SPICE file, body centered; uses only the planet as the effect, with the planet's center as the point mass.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import EPHEMERIS_SOURCE


