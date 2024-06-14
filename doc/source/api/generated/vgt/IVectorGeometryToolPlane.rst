IVectorGeometryToolPlane
========================

.. py:class:: IVectorGeometryToolPlane

   object
   
   The interface defines methods and properties common to all VGT planes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~find_in_axes`
              - Compute the plane's axes vectors in a specified reference axes.
            * - :py:meth:`~find_in_axes_with_rate`
              - Compute the plane's axes vectors and their rates in a specified reference axes.
            * - :py:meth:`~find_in_system`
              - Compute the position and X and Y axes in the specified coordinate system.
            * - :py:meth:`~find_in_system_with_rate`
              - Compute the position, X and Y axes and their rates of change in the specified coordinate system.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~labels`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlane


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlane.type
    :type: "VECTOR_GEOMETRY_TOOL_PLANE_TYPE"

    Returns a type of the plane object.

.. py:property:: labels
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlane.labels
    :type: "IAgCrdnPlaneLabels"

    Allows configuring the plane's X and Y axes labels.


Method detail
-------------


.. py:method:: find_in_axes(self, epoch:typing.Any, axes:"IVectorGeometryToolAxes") -> "IVectorGeometryToolPlaneFindInAxesResult"

    Compute the plane's axes vectors in a specified reference axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~"IVectorGeometryToolAxes"`

    :Returns:

        :obj:`~"IVectorGeometryToolPlaneFindInAxesResult"`

.. py:method:: find_in_axes_with_rate(self, epoch:typing.Any, axes:"IVectorGeometryToolAxes") -> "IVectorGeometryToolPlaneFindInAxesWithRateResult"

    Compute the plane's axes vectors and their rates in a specified reference axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~"IVectorGeometryToolAxes"`

    :Returns:

        :obj:`~"IVectorGeometryToolPlaneFindInAxesWithRateResult"`

.. py:method:: find_in_system(self, epoch:typing.Any, system:"IVectorGeometryToolSystem") -> "IVectorGeometryToolPlaneFindInSystemResult"

    Compute the position and X and Y axes in the specified coordinate system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~"IVectorGeometryToolSystem"`

    :Returns:

        :obj:`~"IVectorGeometryToolPlaneFindInSystemResult"`

.. py:method:: find_in_system_with_rate(self, epoch:typing.Any, system:"IVectorGeometryToolSystem") -> "IVectorGeometryToolPlaneFindInSystemWithRateResult"

    Compute the position, X and Y axes and their rates of change in the specified coordinate system.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **system** : :obj:`~"IVectorGeometryToolSystem"`

    :Returns:

        :obj:`~"IVectorGeometryToolPlaneFindInSystemWithRateResult"`


