CRDN_INTEGRATION_WINDOW_TYPE
============================

.. py:class:: CRDN_INTEGRATION_WINDOW_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~TOTAL`
              - Define the integral's window as the entire available interval list which effectively makes the value of the integral constant.

            * - :py:attr:`~CUMULATIVE_TO_CURRENT`
              - Define the integral's window as the window of time from the beginning of the available interval until the current time, i.e. window duration grows over time.

            * - :py:attr:`~CUMULATIVE_FROM_CURRENT`
              - Define the integral's window as window of time from the current time until the end of the available interval, i.e. window duration decreases over time.

            * - :py:attr:`~SLIDING_WINDOW`
              - Define the integral's window as the interval of times centered around the current time with the specified front and back durations.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_INTEGRATION_WINDOW_TYPE


