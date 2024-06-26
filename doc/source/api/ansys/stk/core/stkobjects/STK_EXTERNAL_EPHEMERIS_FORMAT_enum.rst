STK_EXTERNAL_EPHEMERIS_FORMAT
=============================

.. py:class:: ansys.stk.core.stkobjects.STK_EXTERNAL_EPHEMERIS_FORMAT

   IntEnum


.. py:currentmodule:: STK_EXTERNAL_EPHEMERIS_FORMAT

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported ephemeris format.

            * - :py:attr:`~STK`
              - ASCII text file formatted for compatibility with STK that ends with '.e' extension.

            * - :py:attr:`~CCSDS`
              - CCSDS orbit ephemeris file format that ends with '.oem' extension.

            * - :py:attr:`~ITC`
              - Define a file format that ends with '.itc' extension. The file type is utilized by some Air Force entities and requires USGOV license.

            * - :py:attr:`~STK_BINARY`
              - STK Binary ephemeris file format that ends with '.be' extension.

            * - :py:attr:`~CODE500`
              - Code500 ephemeris file format that ends with '.EPH' extension.

            * - :py:attr:`~CCSD_SV2`
              - CCSDS v2 orbit ephemeris file format that ends with '.oem' extension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import STK_EXTERNAL_EPHEMERIS_FORMAT


