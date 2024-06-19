IVectorGeometryToolAxes
=======================

.. py:class:: IVectorGeometryToolAxes

   object
   
   The interface defines methods and properties common to all axes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~find_in_axes_with_rate`
              - Find an angular velocity and orientation in the specified axes.
            * - :py:meth:`~find_in_axes`
              - Find an orientation in the specified axes.
            * - :py:meth:`~transform`
              - Transform the input vector from this axes into the output axes.
            * - :py:meth:`~transform_with_rate`
              - Transform the input vector and vector's rate from this axes into the output axes.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~labels`
            * - :py:meth:`~x`
            * - :py:meth:`~y`
            * - :py:meth:`~z`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxes


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.type
    :type: VECTOR_GEOMETRY_TOOL_AXES_TYPE

    Returns a type of the axes object.

.. py:property:: labels
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.labels
    :type: IAgCrdnAxesLabels

    Returns an object that allows modifying the axes labels.

.. py:property:: x
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.x
    :type: IAgCrdnVector

    Returns the X axis of the component.

.. py:property:: y
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.y
    :type: IAgCrdnVector

    Returns the Y axis of the component.

.. py:property:: z
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.z
    :type: IAgCrdnVector

    Returns the Z axis of the component.


Method detail
-------------


.. py:method:: find_in_axes_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IVectorGeometryToolAxesFindInAxesWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.find_in_axes_with_rate

    Find an angular velocity and orientation in the specified axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IVectorGeometryToolAxesFindInAxesWithRateResult`

.. py:method:: find_in_axes(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IVectorGeometryToolAxesFindInAxesResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.find_in_axes

    Find an orientation in the specified axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IVectorGeometryToolAxesFindInAxesResult`





.. py:method:: transform(self, epoch: typing.Any, outputAxes: IVectorGeometryToolAxes, vectorInMyAxes: ICartesian3Vector) -> IVectorGeometryToolAxesTransformResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.transform

    Transform the input vector from this axes into the output axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **outputAxes** : :obj:`~IVectorGeometryToolAxes`
    **vectorInMyAxes** : :obj:`~ICartesian3Vector`

    :Returns:

        :obj:`~IVectorGeometryToolAxesTransformResult`

.. py:method:: transform_with_rate(self, epoch: typing.Any, outputAxes: IVectorGeometryToolAxes, vectorInMyAxes: ICartesian3Vector, rateInMyAxes: ICartesian3Vector) -> IVectorGeometryToolAxesTransformWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxes.transform_with_rate

    Transform the input vector and vector's rate from this axes into the output axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **outputAxes** : :obj:`~IVectorGeometryToolAxes`
    **vectorInMyAxes** : :obj:`~ICartesian3Vector`
    **rateInMyAxes** : :obj:`~ICartesian3Vector`

    :Returns:

        :obj:`~IVectorGeometryToolAxesTransformWithRateResult`

