IVectorGeometryToolPointGlint
=============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointGlint

   object
   
   Point on central body surface that reflects from source to observer.

.. py:currentmodule:: IVectorGeometryToolPointGlint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointGlint.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointGlint.source_point`
              - Specify a source point.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointGlint.observer_point`
              - Specify an observer point.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointGlint


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGlint.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: source_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGlint.source_point
    :type: IVectorGeometryToolPointRefTo

    Specify a source point.

.. py:property:: observer_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGlint.observer_point
    :type: IVectorGeometryToolPointRefTo

    Specify an observer point.


