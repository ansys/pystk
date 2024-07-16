VectorGeometryToolVectorFixedAtEpoch
====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtEpoch

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Based on another vector fixed at a specified epoch.

.. py:currentmodule:: VectorGeometryToolVectorFixedAtEpoch

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtEpoch.epoch`
              - Specify an epoch.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtEpoch.source_vector`
              - Specify a source vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtEpoch.reference_axes`
              - Specify a reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorFixedAtEpoch


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtEpoch.epoch
    :type: typing.Any

    Specify an epoch.

.. py:property:: source_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtEpoch.source_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a source vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtEpoch.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.


