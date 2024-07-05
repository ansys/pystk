SENSOR_SCAN_MODE
================

.. py:class:: ansys.stk.core.stkobjects.SENSOR_SCAN_MODE

   IntEnum


.. py:currentmodule:: SENSOR_SCAN_MODE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNIDIRECTIONAL`
              - Unidirectional: scan from a specified start angle to a specified stop angle, and then begin again at the start angle.

            * - :py:attr:`~BIDIRECTIONAL`
              - Bidirectional: scan in both directions between a specified start angle and stop angle.

            * - :py:attr:`~CONTINUOUS`
              - Continuous: uninterrupted motion about the spin axis.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SENSOR_SCAN_MODE


