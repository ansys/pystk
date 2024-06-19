IVectorGeometryToolAngleToPlane
===============================

.. py:class:: IVectorGeometryToolAngleToPlane

   object
   
   An angle between a vector and a plane.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_vector`
            * - :py:meth:`~reference_plane`
            * - :py:meth:`~signed`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleToPlane


Property detail
---------------

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.reference_vector
    :type: IAgCrdnVectorRefTo

    Specify a reference vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.reference_plane
    :type: IAgCrdnPlaneRefTo

    Specify a reference plane.

.. py:property:: signed
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleToPlane.signed
    :type: CRDN_SIGNED_ANGLE_TYPE

    Controls whether the angle is measured as either Positive or Negative when the reference Vector is directed toward the plane's normal, or always positive.


