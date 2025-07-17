IGraphics3DReferenceAnalysisWorkbenchComponent
==============================================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent

   IGraphics3DReferenceAnalysisWorkbenchComponent used to access the shared properties of all 3D RefCrdn.

.. py:currentmodule:: IGraphics3DReferenceAnalysisWorkbenchComponent

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.type_identifier`
              - Type of component (vector, axes, angle, plane, point). A member of the GeometricElementType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.name`
              - Get the name of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.visible`
              - Whether component is visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.color`
              - Color of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.show_label`
              - Is the label for the component visible?


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DReferenceAnalysisWorkbenchComponent


Property detail
---------------

.. py:property:: type_identifier
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.type_identifier
    :type: GeometricElementType

    Type of component (vector, axes, angle, plane, point). A member of the GeometricElementType enumeration.

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
    :type: Color

    Color of the component.

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.show_label
    :type: bool

    Is the label for the component visible?


