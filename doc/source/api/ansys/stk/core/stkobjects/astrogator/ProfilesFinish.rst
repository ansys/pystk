ProfilesFinish
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfilesFinish

   IntEnum


.. py:currentmodule:: ProfilesFinish

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~RUN_TO_RETURN_AND_CONTINUE`
              - Run To Return And Continue - run to the first Return segment in the sequence, then pass control to the next segment after this target sequence. Often, the only Return is at the end of the target sequence.

            * - :py:attr:`~RUN_TO_RETURN_AND_STOP`
              - Run To Return And Stop - run the target sequence to the first Return segment, and then stop running the MCS altogether.

            * - :py:attr:`~STOP`
              - Stop - stop the MCS as soon as the target sequence has converged.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfilesFinish


