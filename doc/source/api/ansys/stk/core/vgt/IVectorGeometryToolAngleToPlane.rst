IVectorGeometryToolAngleToPlane
===============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane

   object
   
   An angle between a vector and a plane.

.. py:currentmodule:: IVectorGeometryToolAngleToPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.reference_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.reference_plane`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.signed`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleToPlane


Property detail
---------------

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.reference_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a reference vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.reference_plane
    :type: IVectorGeometryToolPlaneRefTo

    Specify a reference plane.

.. py:property:: signed
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.signed
    :type: CRDN_SIGNED_ANGLE_TYPE

    Controls whether the angle is measured as either Positive or Negative when the reference Vector is directed toward the plane's normal, or always positive.


