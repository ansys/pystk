MTO_RANGE_MODE
==============

.. py:class:: MTO_RANGE_MODE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EACH`
              - For every track, returns the track id, 1 (within range) or 0 (not in range), and the range value in Connect distance units.

            * - :py:attr:`~EACH_IN_RANGE`
              - Return the Track_id for each track in range, a 1 and the range value in Connect distance units.

            * - :py:attr:`~EACH_NOT_IN_RANGE`
              - Return the Track_id for each track not in range, a 0 and the range value in Connect distance units.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTO_RANGE_MODE


