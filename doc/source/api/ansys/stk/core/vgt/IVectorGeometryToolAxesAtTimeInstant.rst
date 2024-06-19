IVectorGeometryToolAxesAtTimeInstant
====================================

.. py:class:: IVectorGeometryToolAxesAtTimeInstant

   object
   
   Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_time_instant`
            * - :py:meth:`~source_axes`
            * - :py:meth:`~reference_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesAtTimeInstant


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.reference_time_instant
    :type: IAgCrdnEvent

    A reference time instant. Can be any Time event.

.. py:property:: source_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.source_axes
    :type: IAgCrdnAxes

    A base axes defining the orientation. Can be any VGT axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAtTimeInstant.reference_axes
    :type: IAgCrdnAxes

    A reference axes. Can be any VGT axes.


