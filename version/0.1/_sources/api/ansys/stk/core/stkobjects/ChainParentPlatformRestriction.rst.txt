ChainParentPlatformRestriction
==============================

.. py:class:: ansys.stk.core.stkobjects.ChainParentPlatformRestriction

   IntEnum


.. py:currentmodule:: ChainParentPlatformRestriction

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported Chain parent platform restriction.

            * - :py:attr:`~NONE`
              - No restriction on parent platform relationship.

            * - :py:attr:`~SAME`
              - The From and To objects must have a common parent platform.

            * - :py:attr:`~DIFFERENT`
              - The From and To objects must have different parent platform.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainParentPlatformRestriction


