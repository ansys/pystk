IPrimitive
==========

.. py:class:: ansys.stk.core.graphics.IPrimitive

   object
   
   Primitives represent objects rendered in the 3D scene.

.. py:currentmodule:: IPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPrimitive.reference_frame`
              - Gets or sets the reference frame this primitive is defined and rendered in.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitive.bounding_sphere`
              - Gets or sets the bounding sphere that encompasses the primitive. The center is defined in the primitive's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitive.automatically_compute_bounding_sphere`
              - Gets or sets if the primitive's bounding sphere is automatically computed.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitive.display_condition`
              - Gets or sets the display condition that determines if the primitive should be rendered. Both this and display must evaluate to true for the primitive to be rendered.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitive.display`
              - Gets or sets if the primitive should be rendered. Both this and display condition must evaluate to true for the primitive to be rendered.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitive.color`
              - Gets or sets the primitive's color.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitive.translucency`
              - Gets or sets the primitive's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitive.tag`
              - Gets or sets custom value associated with this primitive.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPrimitive


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.graphics.IPrimitive.reference_frame
    :type: IVectorGeometryToolSystem

    Gets or sets the reference frame this primitive is defined and rendered in.

.. py:property:: bounding_sphere
    :canonical: ansys.stk.core.graphics.IPrimitive.bounding_sphere
    :type: IBoundingSphere

    Gets or sets the bounding sphere that encompasses the primitive. The center is defined in the primitive's reference frame.

.. py:property:: automatically_compute_bounding_sphere
    :canonical: ansys.stk.core.graphics.IPrimitive.automatically_compute_bounding_sphere
    :type: bool

    Gets or sets if the primitive's bounding sphere is automatically computed.

.. py:property:: display_condition
    :canonical: ansys.stk.core.graphics.IPrimitive.display_condition
    :type: IDisplayCondition

    Gets or sets the display condition that determines if the primitive should be rendered. Both this and display must evaluate to true for the primitive to be rendered.

.. py:property:: display
    :canonical: ansys.stk.core.graphics.IPrimitive.display
    :type: bool

    Gets or sets if the primitive should be rendered. Both this and display condition must evaluate to true for the primitive to be rendered.

.. py:property:: color
    :canonical: ansys.stk.core.graphics.IPrimitive.color
    :type: agcolor.Color

    Gets or sets the primitive's color.

.. py:property:: translucency
    :canonical: ansys.stk.core.graphics.IPrimitive.translucency
    :type: float

    Gets or sets the primitive's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.

.. py:property:: tag
    :canonical: ansys.stk.core.graphics.IPrimitive.tag
    :type: typing.Any

    Gets or sets custom value associated with this primitive.


