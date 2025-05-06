VectorGeometryToolVectorReflection
==================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Incident vector reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

.. py:currentmodule:: VectorGeometryToolVectorReflection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.incoming_vector`
              - The reflecting vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.use_opposite_of_selected_vector`
              - When set to false, resets the direction of the Incident Vector to default.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.normal_vector`
              - The vector defines the reflection surface.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.allow_reflections_on_backside`
              - Control whether to reflect the indicent vector on both sides of the plane.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.scale_factor`
              - The vector's scale factor.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorReflection


Property detail
---------------

.. py:property:: incoming_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.incoming_vector
    :type: VectorGeometryToolVectorReference

    The reflecting vector.

.. py:property:: use_opposite_of_selected_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.use_opposite_of_selected_vector
    :type: bool

    When set to false, resets the direction of the Incident Vector to default.

.. py:property:: normal_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.normal_vector
    :type: VectorGeometryToolVectorReference

    The vector defines the reflection surface.

.. py:property:: allow_reflections_on_backside
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.allow_reflections_on_backside
    :type: bool

    Control whether to reflect the indicent vector on both sides of the plane.

.. py:property:: scale_factor
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection.scale_factor
    :type: float

    The vector's scale factor.


