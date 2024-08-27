VectorGeometryToolAxesFixedAtEpoch
==================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesFixedAtEpoch

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Axes based on another set fixed at a specified epoch.

.. py:currentmodule:: VectorGeometryToolAxesFixedAtEpoch

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesFixedAtEpoch.source_axes`
              - Specify a source axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesFixedAtEpoch.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesFixedAtEpoch.epoch`
              - Specify an epoch.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesFixedAtEpoch


Property detail
---------------

.. py:property:: source_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesFixedAtEpoch.source_axes
    :type: VectorGeometryToolAxesRefTo

    Specify a source axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesFixedAtEpoch.reference_axes
    :type: VectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: epoch
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesFixedAtEpoch.epoch
    :type: typing.Any

    Specify an epoch.


