CalculationToolParameterSetTrajectory
=====================================

.. py:class:: ansys.stk.core.vgt.CalculationToolParameterSetTrajectory

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolParameterSet`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

.. py:currentmodule:: CalculationToolParameterSetTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetTrajectory.point`
              - Get the point for which trajectory representations are computed.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetTrajectory.reference_system`
              - Get the reference system relative to which trajectory representations are computed.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolParameterSetTrajectory


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetTrajectory.point
    :type: IVectorGeometryToolPoint

    Get the point for which trajectory representations are computed.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetTrajectory.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system relative to which trajectory representations are computed.


