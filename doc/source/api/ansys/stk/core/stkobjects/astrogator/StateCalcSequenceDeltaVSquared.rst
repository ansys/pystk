StateCalcSequenceDeltaVSquared
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Sequence DeltaV Squared Calc objects.

.. py:currentmodule:: StateCalcSequenceDeltaVSquared

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared.sequence_name`
              - Gets or sets the sequence whose DeltaV's are to be accumulated.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared.squared_type`
              - Whether the value should be calculated as the sum of the squares of the maneuver Delta-Vs or the square of the sum of the maneuver Delta-Vs.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcSequenceDeltaVSquared


Property detail
---------------

.. py:property:: sequence_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared.sequence_name
    :type: str

    Gets or sets the sequence whose DeltaV's are to be accumulated.

.. py:property:: squared_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared.squared_type
    :type: SquaredType

    Whether the value should be calculated as the sum of the squares of the maneuver Delta-Vs or the square of the sum of the maneuver Delta-Vs.


