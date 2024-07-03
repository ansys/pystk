ICalculationToolConditionPointInVolume
======================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolConditionPointInVolume

   object
   
   Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

.. py:currentmodule:: ICalculationToolConditionPointInVolume

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionPointInVolume.point`
              - Get the trajectory point from the condition.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionPointInVolume.constraint`
              - Get the volume constraint on trajectory point.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionPointInVolume


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionPointInVolume.point
    :type: IVectorGeometryToolPoint

    Get the trajectory point from the condition.

.. py:property:: constraint
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionPointInVolume.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on trajectory point.


