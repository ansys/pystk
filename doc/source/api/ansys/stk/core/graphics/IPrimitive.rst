IPrimitive
==========

.. py:class:: IPrimitive

   object
   
   Primitives represent objects rendered in the 3D scene.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_frame`
            * - :py:meth:`~bounding_sphere`
            * - :py:meth:`~automatically_compute_bounding_sphere`
            * - :py:meth:`~display_condition`
            * - :py:meth:`~display`
            * - :py:meth:`~color`
            * - :py:meth:`~translucency`
            * - :py:meth:`~tag`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPrimitive


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.graphics.IPrimitive.reference_frame
    :type: "IAgCrdnSystem"

    Gets or sets the reference frame this primitive is defined and rendered in.

.. py:property:: bounding_sphere
    :canonical: ansys.stk.core.graphics.IPrimitive.bounding_sphere
    :type: "IAgStkGraphicsBoundingSphere"

    Gets or sets the bounding sphere that encompasses the primitive. The center is defined in the primitive's reference frame.

.. py:property:: automatically_compute_bounding_sphere
    :canonical: ansys.stk.core.graphics.IPrimitive.automatically_compute_bounding_sphere
    :type: bool

    Gets or sets if the primitive's bounding sphere is automatically computed.

.. py:property:: display_condition
    :canonical: ansys.stk.core.graphics.IPrimitive.display_condition
    :type: "IAgStkGraphicsDisplayCondition"

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


