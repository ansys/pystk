IVectorGeometryToolPlane
========================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPlane

   The interface defines methods and properties common to all VGT planes.

.. py:currentmodule:: IVectorGeometryToolPlane

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlane.find_in_axes`
              - Compute the plane's axes vectors in a specified reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlane.find_in_axes_with_rate`
              - Compute the plane's axes vectors and their rates in a specified reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlane.find_in_system`
              - Compute the position and X and Y axes in the specified coordinate system.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlane.find_in_system_with_rate`
              - Compute the position, X and Y axes and their rates of change in the specified coordinate system.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlane.type`
              - Returns a type of the plane object.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlane.labels`
              - Allows configuring the plane's X and Y axes labels.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlane


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlane.type
    :type: PLANE_TYPE

    Returns a type of the plane object.

.. py:property:: labels
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlane.labels
    :type: VectorGeometryToolPlaneLabels

    Allows configuring the plane's X and Y axes labels.


Method detail
-------------


.. py:method:: find_in_axes(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IPlaneFindInAxesResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlane.find_in_axes

    Compute the plane's axes vectors in a specified reference axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IPlaneFindInAxesResult`

.. py:method:: find_in_axes_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> IPlaneFindInAxesWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlane.find_in_axes_with_rate

    Compute the plane's axes vectors and their rates in a specified reference axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IPlaneFindInAxesWithRateResult`

.. py:method:: find_in_system(self, epoch: typing.Any, system: IVectorGeometryToolSystem) -> IPlaneFindInSystemResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlane.find_in_system

    Compute the position and X and Y axes in the specified coordinate system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~IVectorGeometryToolSystem`

    :Returns:

        :obj:`~IPlaneFindInSystemResult`

.. py:method:: find_in_system_with_rate(self, epoch: typing.Any, system: IVectorGeometryToolSystem) -> IPlaneFindInSystemWithRateResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlane.find_in_system_with_rate

    Compute the position, X and Y axes and their rates of change in the specified coordinate system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~IVectorGeometryToolSystem`

    :Returns:

        :obj:`~IPlaneFindInSystemWithRateResult`


