VEHICLE_PASS_NUMBERING
======================

.. py:class:: ansys.stk.core.stkobjects.VEHICLE_PASS_NUMBERING

   IntEnum


.. py:currentmodule:: VEHICLE_PASS_NUMBERING

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~PASS_NUMBERING_UNKNOWN`
              - Represents pass numbering currently not supported by the Object Model.

            * - :py:attr:`~PASS_NUMBERING_DATE_OF_FIRST_PASS`
              - Date of First Pass: override the first pass start time (normally the ephemeris start time).

            * - :py:attr:`~PASS_NUMBERING_FIRST_PASS_NUM`
              - First Pass #: an integer to identify the number at which pass numbering begins.

            * - :py:attr:`~PASS_NUMBERING_MAINTAIN_PASS_NUM`
              - Maintain Pass #: STK continues the existing pass numbering sequence when a vehicle is repropagated or the epoch changes.

            * - :py:attr:`~PASS_NUMBERING_USE_PROPAGATOR_PASS_DATA`
              - Use Propagator Pass Data: should be used when the propagator is SGP4, which has its own definition for passes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_PASS_NUMBERING


