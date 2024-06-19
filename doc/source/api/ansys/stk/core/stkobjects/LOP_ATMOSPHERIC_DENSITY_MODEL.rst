LOP_ATMOSPHERIC_DENSITY_MODEL
=============================

.. py:class:: LOP_ATMOSPHERIC_DENSITY_MODEL

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN_DENSITY_MODEL`
              - Unsupported or unknown atmospheric density model.

            * - :py:attr:`~LOP1976_STANDARD_ATMOS_MODEL`
              - 1976 Standard Atmosphere: look-up model based on the satellite's altitude, with a valid range of 86km - 1000 km.

            * - :py:attr:`~EXPONENTIAL_MODEL`
              - Exponential Model: uses equation calculating atmospheric density on basis of a specified altitude, reference density, reference altitude and scale altitude.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LOP_ATMOSPHERIC_DENSITY_MODEL


