EXPORT_TOOL_STEP_SIZE
=====================

.. py:class:: ansys.stk.core.stkobjects.EXPORT_TOOL_STEP_SIZE

   IntEnum


.. py:currentmodule:: EXPORT_TOOL_STEP_SIZE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EPHEMERIS`
              - The Step Size specified in the vehicle's Basic properties.

            * - :py:attr:`~SPECIFY`
              - A specified Step Size to be used for the vehicle.

            * - :py:attr:`~NATIVE`
              - The Step Size specified in the vehicle's Basic properties plus any additional times at which the vehicle's attitude changes abruptly. Creates a more complete attitude file without requiring the use of a very small, performance-reducing step size.

            * - :py:attr:`~TIME_ARRAY`
              - The Step Size specified in time array component for the vehicle.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import EXPORT_TOOL_STEP_SIZE


