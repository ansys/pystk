ReturnControl
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ReturnControl

   IntEnum


.. py:currentmodule:: ReturnControl

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ENABLE`
              - Enable - returns control of the MCS run to the parent segment.

            * - :py:attr:`~DISABLE`
              - Disable - the MCS ignores this segment and continues to run.

            * - :py:attr:`~ENABLE_EXCEPT_PROFILES_BYPASS`
              - Enable (except Profiles bypass)- functions as enabled except when run from a Target Sequence profile (e.g., a differential corrector), which will ignore it.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ReturnControl


