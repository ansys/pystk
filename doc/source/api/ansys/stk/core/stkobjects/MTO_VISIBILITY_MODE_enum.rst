MTO_VISIBILITY_MODE
===================

.. py:class:: ansys.stk.core.stkobjects.MTO_VISIBILITY_MODE

   IntEnum


.. py:currentmodule:: MTO_VISIBILITY_MODE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EACH`
              - Return the Track_id and 1 or 0 for every track; where 1 indicates the track is visible and 0 indicates it is not.

            * - :py:attr:`~EACH_VISIBLE`
              - Return the Track_id and 1 only for those tracks having visibility. If all objects are invisible then the message 'No Visibility' is returned.

            * - :py:attr:`~EACH_NOT_VISIBLE`
              - Return the Track_id and 0 for those tracks not having visibility. If all objects are visible then the message 'Complete Visibility' is returned.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MTO_VISIBILITY_MODE


