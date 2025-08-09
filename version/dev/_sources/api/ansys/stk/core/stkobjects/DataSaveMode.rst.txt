DataSaveMode
============

.. py:class:: ansys.stk.core.stkobjects.DataSaveMode

   IntEnum


.. py:currentmodule:: DataSaveMode

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported mode.

            * - :py:attr:`~DONT_SAVE_ACCESSES`
              - Access computations are not saved with the chain.

            * - :py:attr:`~DONT_SAVE_COMPUTE_ON_LOAD`
              - Access computations are not saved with the chain, but they are recalculated each time that the chain is opened in STK.

            * - :py:attr:`~SAVE_ACCESSES`
              - Access computations are saved with the chain.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataSaveMode


