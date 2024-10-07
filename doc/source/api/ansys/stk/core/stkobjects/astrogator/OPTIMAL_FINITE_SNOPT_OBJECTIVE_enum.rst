OPTIMAL_FINITE_SNOPT_OBJECTIVE
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_SNOPT_OBJECTIVE

   IntEnum


.. py:currentmodule:: OPTIMAL_FINITE_SNOPT_OBJECTIVE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~MINIMIZE_TIME_OF_FLIGHT`
              - Minimize the total TOF along the collocation arc.

            * - :py:attr:`~MAXIMIZE_FINAL_RAD`
              - Minimize the total calculated DeltaV along the collocation arc.

            * - :py:attr:`~MINIMIZE_PROPELLANT_USE`
              - Maximize the final mass after the collocation arc.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import OPTIMAL_FINITE_SNOPT_OBJECTIVE


