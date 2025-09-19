VehicleLookAheadMethod
======================

.. py:class:: ansys.stk.core.stkobjects.VehicleLookAheadMethod

   IntEnum


.. py:currentmodule:: VehicleLookAheadMethod

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EXTRAPOLATE`
              - Extrapolate: STK uses the last two history points to extrapolate attitude into the Look Ahead window. This method is best if attitude changes slightly over time.

            * - :py:attr:`~HOLD`
              - Hold: Attitude remains the same from the last data point. This method is best when fixed attitude is more reliable than an approximate value.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleLookAheadMethod


