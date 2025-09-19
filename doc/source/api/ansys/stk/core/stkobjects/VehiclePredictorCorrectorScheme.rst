VehiclePredictorCorrectorScheme
===============================

.. py:class:: ansys.stk.core.stkobjects.VehiclePredictorCorrectorScheme

   IntEnum


.. py:currentmodule:: VehiclePredictorCorrectorScheme

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FULL_CORRECTION`
              - Full correction: use a full evaluation of the acceleration model at the end of a Gauss-Jackson integration step.

            * - :py:attr:`~PSEUDOCORRECTION`
              - Pseudo correction: use a pseudo-evaluation where only the two body acceleration is updated.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePredictorCorrectorScheme


