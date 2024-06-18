ICalculationToolConditionPointInVolume
======================================

.. py:class:: ICalculationToolConditionPointInVolume

   object
   
   Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~point`
            * - :py:meth:`~constraint`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionPointInVolume


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionPointInVolume.point
    :type: "IAgCrdnPoint"

    Get the trajectory point from the condition.

.. py:property:: constraint
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionPointInVolume.constraint
    :type: "IAgCrdnVolume"

    Get the volume constraint on trajectory point.


