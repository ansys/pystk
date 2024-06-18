IGraphics3DReferenceAnalysisWorkbenchComponent
==============================================

.. py:class:: IGraphics3DReferenceAnalysisWorkbenchComponent

   object
   
   IAgVORefCrdn used to access the shared properties of all 3D RefCrdn.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type_id`
            * - :py:meth:`~name`
            * - :py:meth:`~visible`
            * - :py:meth:`~color`
            * - :py:meth:`~label_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DReferenceAnalysisWorkbenchComponent


Property detail
---------------

.. py:property:: type_id
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.type_id
    :type: "GEOMETRIC_ELEM_TYPE"

    Type of component (vector, axes, angle, plane, point). A member of the AgEGeometricElemType enumeration.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.name
    :type: str

    Get the name of the component.

.. py:property:: visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.visible
    :type: bool

    Whether component is visible.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.color
    :type: agcolor.Color

    Color of the component.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.label_visible
    :type: bool

    Is the label for the component visible?


