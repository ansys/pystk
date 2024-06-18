IVectorGeometryToolVectorFixedAtTimeInstant
===========================================

.. py:class:: IVectorGeometryToolVectorFixedAtTimeInstant

   object
   
   Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_time_instant`
            * - :py:meth:`~source_vector`
            * - :py:meth:`~reference_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorFixedAtTimeInstant


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.reference_time_instant
    :type: "IAgCrdnEvent"

    A reference time instant. Can be any Time event.

.. py:property:: source_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.source_vector
    :type: "IAgCrdnVector"

    A source vector. Can be any VGT vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtTimeInstant.reference_axes
    :type: "IAgCrdnAxes"

    A reference axes. Can be any VGT axes.


