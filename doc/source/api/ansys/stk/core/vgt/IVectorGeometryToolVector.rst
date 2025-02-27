IVectorGeometryToolVector
=========================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVector

   The interface defines methods and properties common to all vectors.

.. py:currentmodule:: IVectorGeometryToolVector

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVector.find_in_axes`
              - Compute the vector in the specified axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVector.find_in_axes_with_rate`
              - Compute the vector and its rate in the specified axes.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVector.type`
              - Return a type of the vector object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVector


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVector.type
    :type: VectorType

    Return a type of the vector object.


Method detail
-------------


.. py:method:: find_in_axes(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchVectorFindInAxesResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVector.find_in_axes

    Compute the vector in the specified axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~AnalysisWorkbenchVectorFindInAxesResult`

.. py:method:: find_in_axes_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchVectorFindInAxesWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVector.find_in_axes_with_rate

    Compute the vector and its rate in the specified axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~AnalysisWorkbenchVectorFindInAxesWithRateResult`

