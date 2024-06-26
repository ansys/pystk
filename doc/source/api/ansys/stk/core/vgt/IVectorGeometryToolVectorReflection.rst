IVectorGeometryToolVectorReflection
===================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorReflection

   object
   
   A vector (incident vector) reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

.. py:currentmodule:: IVectorGeometryToolVectorReflection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.incoming_vector`
              - The reflecting vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.use_opposite_of_selected_vector`
              - When set to false, resets the direction of the Incident Vector to default.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.normal_vector`
              - The vector defines the reflection surface.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.allow_reflections_on_backside`
              - Controls whether to reflect the indicent vector on both sides of the plane.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.scale_factor`
              - The vector's scale factor.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorReflection


Property detail
---------------

.. py:property:: incoming_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.incoming_vector
    :type: IVectorGeometryToolVectorRefTo

    The reflecting vector.

.. py:property:: use_opposite_of_selected_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.use_opposite_of_selected_vector
    :type: bool

    When set to false, resets the direction of the Incident Vector to default.

.. py:property:: normal_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.normal_vector
    :type: IVectorGeometryToolVectorRefTo

    The vector defines the reflection surface.

.. py:property:: allow_reflections_on_backside
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.allow_reflections_on_backside
    :type: bool

    Controls whether to reflect the indicent vector on both sides of the plane.

.. py:property:: scale_factor
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorReflection.scale_factor
    :type: float

    The vector's scale factor.


