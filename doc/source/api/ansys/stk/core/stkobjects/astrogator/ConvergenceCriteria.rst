ConvergenceCriteria
===================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ConvergenceCriteria

   IntEnum


.. py:currentmodule:: ConvergenceCriteria

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EQUALITY_CONSTRAINT_WITHIN_TOLERANCE`
              - Equality Constraints Satisfied - the differences between the achieved and desired equality constraint values must be within the specified tolerances for convergence.

            * - :py:attr:`~CONVERVENCE_CRITERIA_EITHER_EQUALITY_CONSTRAINTS_OR_CONTROL_PARAMS`
              - Equality Constraints Satisfied or Parameter Variations within Tolerance - the differences between the achieved and desired EC values must be within tolerances, or the last updates to the control parameters must be within tolerances for convergence.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ConvergenceCriteria


