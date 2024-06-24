IVectorGeometryToolVectorPeriapsis
==================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis

   object
   
   Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

.. py:currentmodule:: IVectorGeometryToolVectorPeriapsis

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.central_body`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.reference_point`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.mean_element_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorPeriapsis


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.reference_point
    :type: IVectorGeometryToolPointRefTo

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorPeriapsis.mean_element_type
    :type: CRDN_MEAN_ELEMENT_THEORY

    Specify the mean element theory type for approximating motion.


