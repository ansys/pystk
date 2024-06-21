IVectorGeometryToolVectorEccentricity
=====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorEccentricity

   object
   
   A vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

.. py:currentmodule:: IVectorGeometryToolVectorEccentricity

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorEccentricity.central_body`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorEccentricity.reference_point`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorEccentricity.mean_element_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorEccentricity


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorEccentricity.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorEccentricity.reference_point
    :type: IVectorGeometryToolPointRefTo

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorEccentricity.mean_element_type
    :type: CRDN_MEAN_ELEMENT_THEORY

    Specify the mean element theory type for approximating motion.


