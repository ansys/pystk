FIGURE_OF_MERIT_METHOD
======================

.. py:class:: FIGURE_OF_MERIT_METHOD

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~GDOP`
              - Geometric Dilution of Precision: Measures the dilution of precision for the entire navigation solution.

            * - :py:attr:`~HDOP`
              - Horizontal Dilution of Precision: Measures the dilution of precision for the horizontal (latitude/longitude) components of the positional portion of the navigation solution.

            * - :py:attr:`~HDOP3`
              - Same as HDOP, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~PDOP`
              - Position Dilution of Precision: Measures only the dilution of precision associated with the positional portion of the navigation solution.

            * - :py:attr:`~PDOP3`
              - Same as PDOP, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~TDOP`
              - Time Dilution of Precision: Measures the dilution of precision of the time portion of the navigation solution.

            * - :py:attr:`~VDOP`
              - Vertical Dilution of Precision: Measures the dilution of precision for the vertical (altitude) components of the positional portion of the navigation solution.

            * - :py:attr:`~VDOP3`
              - Same as VDOP, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~GACC`
              - Geometric Accuracy: Measures the accuracy of the entire navigation solution.

            * - :py:attr:`~HACC`
              - Horizontal Accuracy: Measures the accuracy for the horizontal (latitude/longitude) components of the positional portion of the navigation solution.

            * - :py:attr:`~HACC3`
              - Same as HACC, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~PACC`
              - Position Accuracy: Measures only the accuracy associated with the positional portion of the navigation solution.

            * - :py:attr:`~PACC3`
              - Same as PACC, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~TACC`
              - Time Accuracy: Measures the accuracy of the time portion of the navigation solution.

            * - :py:attr:`~VACC`
              - Vertical Accuracy: Measures the accuracy for the vertical (altitude) components of the positional portion of the navigation solution.

            * - :py:attr:`~VACC3`
              - Same as VACC, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~EDOP`
              - East Dilution of Precision: Measures the dilution of precision for the east components of the positional portion of the navigation solution.

            * - :py:attr:`~EDOP3`
              - Same as eEDOP, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~NDOP`
              - North Dilution of Precision: Measures the dilution of precision for the east components of the positional portion of the navigation solution.

            * - :py:attr:`~NDOP3`
              - Same as eNDOP, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~EACC`
              - East Accuracy: Measures the accuracy for the east components of the positional portion of the navigation solution.

            * - :py:attr:`~EACC3`
              - Same as EACC, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.

            * - :py:attr:`~NACC`
              - North Accuracy: Measures the accuracy for the north components of the positional portion of the navigation solution.

            * - :py:attr:`~NACC3`
              - Same as NACC, but the DOP value is computed even if only 3 navigation sources are available, in which case the clock component is ignored.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_METHOD


