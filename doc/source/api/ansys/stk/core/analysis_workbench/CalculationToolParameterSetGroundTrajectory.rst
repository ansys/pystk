CalculationToolParameterSetGroundTrajectory
===========================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolParameterSetGroundTrajectory

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolParameterSet`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Ground trajectory parameter set contains various representations of trajectory of a point relative to central body reference shape.

.. py:currentmodule:: CalculationToolParameterSetGroundTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetGroundTrajectory.central_body`
              - Get the central body relative to which ground trajectory representations are computed. Both the central body reference shape and its CBF (central body centered fixed) system are used by this parameter set.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetGroundTrajectory.location`
              - Get the point for which ground trajectory representations are computed.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolParameterSetGroundTrajectory


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetGroundTrajectory.central_body
    :type: str

    Get the central body relative to which ground trajectory representations are computed. Both the central body reference shape and its CBF (central body centered fixed) system are used by this parameter set.

.. py:property:: location
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolParameterSetGroundTrajectory.location
    :type: IVectorGeometryToolPoint

    Get the point for which ground trajectory representations are computed.


