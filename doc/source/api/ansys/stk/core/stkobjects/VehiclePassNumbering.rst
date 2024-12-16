VehiclePassNumbering
====================

.. py:class:: ansys.stk.core.stkobjects.VehiclePassNumbering

   IntEnum


.. py:currentmodule:: VehiclePassNumbering

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Represents pass numbering currently not supported by the Object Model.

            * - :py:attr:`~DATE_OF_FIRST_PASS`
              - Date of First Pass: override the first pass start time (normally the ephemeris start time).

            * - :py:attr:`~FIRST_PASS_NUMBER`
              - First Pass #: an integer to identify the number at which pass numbering begins.

            * - :py:attr:`~MAINTAIN_PASS_NUMBER`
              - Maintain Pass #: STK continues the existing pass numbering sequence when a vehicle is repropagated or the epoch changes.

            * - :py:attr:`~USE_PROPAGATOR_PASS_DATA`
              - Use Propagator Pass Data: should be used when the propagator is SGP4, which has its own definition for passes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePassNumbering


