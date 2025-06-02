SolidPrimitiveFactory
=====================

.. py:class:: ansys.stk.core.graphics.SolidPrimitiveFactory

   Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

.. py:currentmodule:: SolidPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitiveFactory.initialize`
              - Initialize a default solid primitive. This is equivalent to constructing a solid primitive with a set hint of Frequent.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitiveFactory.initialize_with_hint`
              - Initialize a solid primitive with the specified setHint.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitiveFactory.minimum_silhouette_width_supported`
              - Get the minimum silhouette width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.SolidPrimitiveFactory.maximum_silhouette_width_supported`
              - Get the maximum silhouette width, in pixels, supported by the video card.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SolidPrimitiveFactory


Property detail
---------------

.. py:property:: minimum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.SolidPrimitiveFactory.minimum_silhouette_width_supported
    :type: float

    Get the minimum silhouette width, in pixels, supported by the video card.

.. py:property:: maximum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.SolidPrimitiveFactory.maximum_silhouette_width_supported
    :type: float

    Get the maximum silhouette width, in pixels, supported by the video card.


Method detail
-------------

.. py:method:: initialize(self) -> SolidPrimitive
    :canonical: ansys.stk.core.graphics.SolidPrimitiveFactory.initialize

    Initialize a default solid primitive. This is equivalent to constructing a solid primitive with a set hint of Frequent.

    :Returns:

        :obj:`~SolidPrimitive`

.. py:method:: initialize_with_hint(self, set_hint: SetHint) -> SolidPrimitive
    :canonical: ansys.stk.core.graphics.SolidPrimitiveFactory.initialize_with_hint

    Initialize a solid primitive with the specified setHint.

    :Parameters:

        **set_hint** : :obj:`~SetHint`


    :Returns:

        :obj:`~SolidPrimitive`



