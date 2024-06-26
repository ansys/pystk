IVectorGeometryToolAngleRotation
================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAngleRotation

   object
   
   Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

.. py:currentmodule:: IVectorGeometryToolAngleRotation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleRotation.from_axes`
              - Specify an axes to rotate from.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleRotation.to_axes`
              - Specify an axes to rotate to.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAngleRotation.reference_direction`
              - Specify a rotation direction.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleRotation


Property detail
---------------

.. py:property:: from_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleRotation.from_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify an axes to rotate from.

.. py:property:: to_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleRotation.to_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify an axes to rotate to.

.. py:property:: reference_direction
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleRotation.reference_direction
    :type: CRDN_DISPLAY_AXIS_SELECTOR

    Specify a rotation direction.


