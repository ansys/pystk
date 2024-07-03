CHAIN_PARENT_PLATFORM_RESTRICTION
=================================

.. py:class:: ansys.stk.core.stkobjects.CHAIN_PARENT_PLATFORM_RESTRICTION

   IntEnum


.. py:currentmodule:: CHAIN_PARENT_PLATFORM_RESTRICTION

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
              - The From and To objects must have a common parent platorm.

            * - :py:attr:`~DIFFERENT`
              - The From and To objects must have different parent platorm.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CHAIN_PARENT_PLATFORM_RESTRICTION


