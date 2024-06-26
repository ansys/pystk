IVectorGeometryToolVectorOrbitAngularMomentum
=============================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorOrbitAngularMomentum

   object
   
   Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

.. py:currentmodule:: IVectorGeometryToolVectorOrbitAngularMomentum

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorOrbitAngularMomentum.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorOrbitAngularMomentum.reference_point`
              - Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorOrbitAngularMomentum.mean_element_type`
              - Specify the mean element theory type for approximating motion.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorOrbitAngularMomentum


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorOrbitAngularMomentum.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorOrbitAngularMomentum.reference_point
    :type: IVectorGeometryToolPointRefTo

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.

.. py:property:: mean_element_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorOrbitAngularMomentum.mean_element_type
    :type: CRDN_MEAN_ELEMENT_THEORY

    Specify the mean element theory type for approximating motion.


