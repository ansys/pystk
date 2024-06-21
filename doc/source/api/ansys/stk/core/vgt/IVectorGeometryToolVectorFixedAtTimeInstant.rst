IVectorGeometryToolVectorFixedAtTimeInstant
===========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant

   object
   
   Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

.. py:currentmodule:: IVectorGeometryToolVectorFixedAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.reference_time_instant`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.source_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.reference_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorFixedAtTimeInstant


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.reference_time_instant
    :type: ITimeToolEvent

    A reference time instant. Can be any Time event.

.. py:property:: source_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.source_vector
    :type: IVectorGeometryToolVector

    A source vector. Can be any VGT vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.reference_axes
    :type: IVectorGeometryToolAxes

    A reference axes. Can be any VGT axes.


