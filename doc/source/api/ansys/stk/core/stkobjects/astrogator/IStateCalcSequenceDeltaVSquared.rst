IStateCalcSequenceDeltaVSquared
===============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcSequenceDeltaVSquared

   object
   
   Properties for a Sequence DeltaV Squared calculation object.

.. py:currentmodule:: IStateCalcSequenceDeltaVSquared

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSequenceDeltaVSquared.sequence_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSequenceDeltaVSquared.squared_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcSequenceDeltaVSquared


Property detail
---------------

.. py:property:: sequence_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSequenceDeltaVSquared.sequence_name
    :type: str

    Gets or sets the sequence whose DeltaV's are to be accumulated.

.. py:property:: squared_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSequenceDeltaVSquared.squared_type
    :type: SQUARED_TYPE

    Whether the value should be calculated as the sum of the squares of the maneuver Delta-Vs or the square of the sum of the maneuver Delta-Vs.


