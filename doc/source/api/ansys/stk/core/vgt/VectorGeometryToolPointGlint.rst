VectorGeometryToolPointGlint
============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointGlint

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Point on central body surface that reflects from source to observer.

.. py:currentmodule:: VectorGeometryToolPointGlint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGlint.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGlint.source_point`
              - Specify a source point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGlint.observer_point`
              - Specify an observer point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointGlint


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGlint.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: source_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGlint.source_point
    :type: VectorGeometryToolPointReference

    Specify a source point.

.. py:property:: observer_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGlint.observer_point
    :type: VectorGeometryToolPointReference

    Specify an observer point.


