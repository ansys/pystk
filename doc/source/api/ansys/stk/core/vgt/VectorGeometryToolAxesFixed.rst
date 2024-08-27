VectorGeometryToolAxesFixed
===========================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesFixed

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Axes fixed in reference axes.

.. py:currentmodule:: VectorGeometryToolAxesFixed

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesFixed.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesFixed.fixed_orientation`
              - Specify a desired orientation and the applicable parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesFixed


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesFixed.reference_axes
    :type: VectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: fixed_orientation
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesFixed.fixed_orientation
    :type: IOrientation

    Specify a desired orientation and the applicable parameters.


