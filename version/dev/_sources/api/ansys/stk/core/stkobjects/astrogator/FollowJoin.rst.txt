FollowJoin
==========

.. py:class:: ansys.stk.core.stkobjects.astrogator.FollowJoin

   IntEnum


.. py:currentmodule:: FollowJoin

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~SPECIFY`
              - Specify Joining Conditions - specify joining conditions to define when the spacecraft will begin to follow the leader. Joining conditions will become apparent on a new tab - Joining.

            * - :py:attr:`~AT_BEGINNING`
              - Join at Beginning of Leader's Ephemeris - the spacecraft will follow the leader from the beginning of the leader's ephemeris.

            * - :py:attr:`~AT_END`
              - Join at End of Leader's Ephemeris - the spacecraft will use the leader's final ephemeris point as the initial and final state of the Follow segment; the separation parameter will automatically be set to 'Separate at End of Leader's Ephemeris'.

            * - :py:attr:`~AT_FINAL_EPOCH_OF_PREVIOUS_SEG`
              - Join at Final Epoch of Previous Segment - the spacecraft will follow the leader from the final epoch at the end of the previous segment.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import FollowJoin


