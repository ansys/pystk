FILE_INTERPOLATOR_TYPE
======================

.. py:class:: ansys.stk.core.vgt.FILE_INTERPOLATOR_TYPE

   IntEnum


.. py:currentmodule:: FILE_INTERPOLATOR_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~INVALID`
              - Unknown or invalid interpolator.

            * - :py:attr:`~LAGRANGE`
              - Lagrange interpolation.

            * - :py:attr:`~HERMITE`
              - Hermite interpolation.

            * - :py:attr:`~HOLD_PREVIOUS`
              - Holds the value at the closest previous sample time to any requested time.

            * - :py:attr:`~HOLD_NEXT`
              - Holds the value at the closest next sample time to any requested time.

            * - :py:attr:`~HOLD_NEAREST`
              - Holds the value at the closest sample time (either the previous sample or the next sample) to any requested time.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import FILE_INTERPOLATOR_TYPE


