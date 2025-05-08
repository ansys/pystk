VectorGeometryToolPointGrazing
==============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

.. py:currentmodule:: VectorGeometryToolPointGrazing

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing.reference_point`
              - Specify a reference point which will serve as the starting location for the line along which the grazing point will be computed.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing.direction_vector`
              - Specify a direction vector to be used in conjunction with the position vector from the selected central body to the reference point to define a plane in which the line will lie.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing.altitude`
              - The point of closest approach to the central body surface occurs at the specified altitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointGrazing


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point which will serve as the starting location for the line along which the grazing point will be computed.

.. py:property:: direction_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing.direction_vector
    :type: VectorGeometryToolVectorReference

    Specify a direction vector to be used in conjunction with the position vector from the selected central body to the reference point to define a plane in which the line will lie.

.. py:property:: altitude
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing.altitude
    :type: float

    The point of closest approach to the central body surface occurs at the specified altitude.


