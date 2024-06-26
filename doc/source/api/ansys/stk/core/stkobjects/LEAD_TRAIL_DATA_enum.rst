LEAD_TRAIL_DATA
===============

.. py:class:: ansys.stk.core.stkobjects.LEAD_TRAIL_DATA

   IntEnum


.. py:currentmodule:: LEAD_TRAIL_DATA

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~DATA_UNKNOWN`
              - Unknown.

            * - :py:attr:`~DATA_NONE`
              - None: Display none of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~DATA_ALL`
              - All: Display the track spanning the entire vehicle ephemeris.

            * - :py:attr:`~DATA_FRACTION`
              - Fraction: Display the specified fraction of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~DATA_FULL`
              - Full: Display all of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~DATA_HALF`
              - Half: Display 1/2 of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~DATA_ONE_PASS`
              - One pass (satellites only): Display forward to the first pass break. At the pass break, display forward to the next one.

            * - :py:attr:`~DATA_QUARTER`
              - Quarter:  Display 1/4 of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~DATA_TIME`
              - Time: Display the segment of the selected portion (leading or trailing) of the vehicle's path that it traverses in the specified amount of time.

            * - :py:attr:`~DATA_CURRENT_INTERVAL`
              - Current Interval: Display the leading portion of the vehicle's track for the current animation time interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LEAD_TRAIL_DATA


