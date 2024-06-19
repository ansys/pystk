DERIVE_CALC_METHOD
==================

.. py:class:: DERIVE_CALC_METHOD

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FORWARD`
              - Forward Difference - ((f(x + delta) - f(x))/ delta).

            * - :py:attr:`~CENTRAL`
              - Central Difference - ((f(x + delta) - f(x - delta)) / 2delta).

            * - :py:attr:`~SIGNED`
              - Signed Difference - if x is positive, use the forward difference; if x is negative, use the backward difference.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import DERIVE_CALC_METHOD


