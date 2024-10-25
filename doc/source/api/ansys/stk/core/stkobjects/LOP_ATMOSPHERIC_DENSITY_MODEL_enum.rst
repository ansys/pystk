LOP_ATMOSPHERIC_DENSITY_MODEL
=============================

.. py:class:: ansys.stk.core.stkobjects.LOP_ATMOSPHERIC_DENSITY_MODEL

   IntEnum


.. py:currentmodule:: LOP_ATMOSPHERIC_DENSITY_MODEL

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported or unknown atmospheric density model.

            * - :py:attr:`~STANDARD_ATMOSPHERE_MODEL_1976`
              - 1976 Standard Atmosphere: look-up model based on the satellite's altitude, with a valid range of 86km - 1000 km.

            * - :py:attr:`~EXPONENTIAL`
              - Exponential Model: uses equation calculating atmospheric density on basis of a specified altitude, reference density, reference altitude and scale altitude.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LOP_ATMOSPHERIC_DENSITY_MODEL


