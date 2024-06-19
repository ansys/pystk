IVectorGeometryToolVector
=========================

.. py:class:: IVectorGeometryToolVector

   object
   
   The interface defines methods and properties common to all vectors.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~find_in_axes`
              - Compute the vector in the specified axes.
            * - :py:meth:`~find_in_axes_with_rate`
              - Compute the vector and its rate in the specified axes.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVector


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVector.type
    :type: VECTOR_GEOMETRY_TOOL_VECTOR_TYPE

    Returns a type of the vector object.


Method detail
-------------


.. py:method:: find_in_axes(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IVectorGeometryToolVectorFindInAxesResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVector.find_in_axes

    Compute the vector in the specified axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IVectorGeometryToolVectorFindInAxesResult`

.. py:method:: find_in_axes_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IVectorGeometryToolVectorFindInAxesWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVector.find_in_axes_with_rate

    Compute the vector and its rate in the specified axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IVectorGeometryToolVectorFindInAxesWithRateResult`

