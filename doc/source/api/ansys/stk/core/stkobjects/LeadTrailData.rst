LeadTrailData
=============

.. py:class:: ansys.stk.core.stkobjects.LeadTrailData

   IntEnum


.. py:currentmodule:: LeadTrailData

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown.

            * - :py:attr:`~NONE`
              - None: Display none of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~ALL`
              - All: Display the track spanning the entire vehicle ephemeris.

            * - :py:attr:`~FRACTION`
              - Fraction: Display the specified fraction of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~FULL`
              - Full: Display all of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~HALF`
              - Half: Display 1/2 of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~ONE_PASS`
              - One pass (satellites only): Display forward to the first pass break. At the pass break, display forward to the next one.

            * - :py:attr:`~QUARTER`
              - Quarter:  Display 1/4 of the selected portion (leading or trailing) of the track.

            * - :py:attr:`~TIME`
              - Time: Display the segment of the selected portion (leading or trailing) of the vehicle's path that it traverses in the specified amount of time.

            * - :py:attr:`~CURRENT_INTERVAL`
              - Current Interval: Display the leading portion of the vehicle's track for the current animation time interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LeadTrailData


