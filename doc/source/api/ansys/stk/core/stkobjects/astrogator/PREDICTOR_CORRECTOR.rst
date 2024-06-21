PREDICTOR_CORRECTOR
===================

.. py:class:: ansys.stk.core.stkobjects.astrogator.PREDICTOR_CORRECTOR

   IntEnum


.. py:currentmodule:: PREDICTOR_CORRECTOR

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FULL`
              - All force models are re-evaluated at each corrector step.

            * - :py:attr:`~PSEUDO`
              - Only the two-body acceleration is re-evaluated at each corrector step.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import PREDICTOR_CORRECTOR


