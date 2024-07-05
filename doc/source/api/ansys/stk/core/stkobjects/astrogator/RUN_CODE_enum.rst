RUN_CODE
========

.. py:class:: ansys.stk.core.stkobjects.astrogator.RUN_CODE

   IntEnum


.. py:currentmodule:: RUN_CODE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~MARCHING`
              - Marching - a segment has run successfully.

            * - :py:attr:`~PROFILE_FAILURE`
              - Profile Failure - a search profile failed to converge.

            * - :py:attr:`~ERROR`
              - Error - encountered an error.

            * - :py:attr:`~STOPPED`
              - Stopped - encountered a stop segment.

            * - :py:attr:`~RETURNED`
              - Returned - encountered a return segment.

            * - :py:attr:`~CANCELLED`
              - Cancelled - cancelled by user.

            * - :py:attr:`~HIT_GLOBAL_STOP`
              - Global Stop - hit a global stopping condition.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import RUN_CODE


