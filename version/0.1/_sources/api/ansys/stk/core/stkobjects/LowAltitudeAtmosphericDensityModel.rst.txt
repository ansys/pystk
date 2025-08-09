LowAltitudeAtmosphericDensityModel
==================================

.. py:class:: ansys.stk.core.stkobjects.LowAltitudeAtmosphericDensityModel

   IntEnum


.. py:currentmodule:: LowAltitudeAtmosphericDensityModel

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported or unknown low altitude atmospheric density model.

            * - :py:attr:`~NONE`
              - No atmospheric density model to be used.

            * - :py:attr:`~NRLMSISE2000`
              - NRLMSISE 2000: finds the total density by accounting for the contribution of N, N2, O, O2, He, Ar and H. Includes anomalous oxygen. 2000 version, valid range of 0-1000 km.

            * - :py:attr:`~MSISE1990`
              - MSISE 1990: finds the total density by accounting for the contribution of N2, O, O2, He, Ar and H. 1990 version, valid range of 0-1000 km.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LowAltitudeAtmosphericDensityModel


