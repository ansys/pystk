IVectorGeometryToolAxesAtTimeInstant
====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant

   object
   
   Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

.. py:currentmodule:: IVectorGeometryToolAxesAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.reference_time_instant`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.source_axes`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.reference_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesAtTimeInstant


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.reference_time_instant
    :type: ITimeToolEvent

    A reference time instant. Can be any Time event.

.. py:property:: source_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.source_axes
    :type: IVectorGeometryToolAxes

    A base axes defining the orientation. Can be any VGT axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.reference_axes
    :type: IVectorGeometryToolAxes

    A reference axes. Can be any VGT axes.


