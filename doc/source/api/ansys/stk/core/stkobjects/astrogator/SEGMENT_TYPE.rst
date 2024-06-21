SEGMENT_TYPE
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.SEGMENT_TYPE

   IntEnum


.. py:currentmodule:: SEGMENT_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~INITIAL_STATE`
              - Initial State - can be used to define the initial conditions of your MCS, or of a subsequence within the MCS.

            * - :py:attr:`~LAUNCH`
              - Launch - can be used to model a simple spacecraft launch from Earth or another central body.

            * - :py:attr:`~MANEUVER`
              - Maneuver - can be used to model a spacecraft maneuver.

            * - :py:attr:`~FOLLOW`
              - Follow - can be used to set the spacecraft to follow another vehicle (Satellite, Launch Vehicle, Missile, Aircraft, Ship, or Ground Vehicle) at a specified offset, and to separate from that vehicle upon meeting specified conditions.

            * - :py:attr:`~HOLD`
              - Hold - can be used to model landing or rendezvous operations by setting the spacecraft to maintain a fixed position in reference to another object or body, until meeting specified conditions.

            * - :py:attr:`~PROPAGATE`
              - Propagate - can be used to model the movement of the spacecraft along its current trajectory until meeting specified stopping conditions.

            * - :py:attr:`~SEQUENCE`
              - Sequence - can be used to organize segments and define the nature of the results that are passed on to the next segment or sequence in the MCS.

            * - :py:attr:`~RETURN`
              - Return - can be used to control the execution of the Mission Control Sequence by returning control to its parent segment.

            * - :py:attr:`~TARGET_SEQUENCE`
              - Target Sequence - can be used to define maneuvers and propagations in terms of the goals they are intended to achieve.

            * - :py:attr:`~STOP`
              - Stop - can be used to control the execution of the Mission Control Sequence by halting execution of the MCS.

            * - :py:attr:`~UPDATE`
              - Update - can be used to modify some of the satellite properties to reflect changes that occur during the mission.

            * - :py:attr:`~BACKWARD_SEQUENCE`
              - Backward Sequence - can be used to organize segments and define the nature of the results that are passed on to the next segment or sequence in the MCS.

            * - :py:attr:`~END`
              - End - The End segment is a default segment of the MCS that functions similarly to a Return segment; it returns control to the beginning of the MCS. The End segment cannot be disabled or deleted, nor can any segments be inserted into the MCS after it.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SEGMENT_TYPE


