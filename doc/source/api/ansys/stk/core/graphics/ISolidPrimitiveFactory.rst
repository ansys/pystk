ISolidPrimitiveFactory
======================

.. py:class:: ansys.stk.core.graphics.ISolidPrimitiveFactory

   object
   
   Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

.. py:currentmodule:: ISolidPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitiveFactory.initialize`
              - Initialize a default solid primitive. This is equivalent to constructing a solid primitive with a set hint of Frequent.
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitiveFactory.initialize_with_hint`
              - Initialize a solid primitive with the specified setHint.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitiveFactory.minimum_silhouette_width_supported`
            * - :py:attr:`~ansys.stk.core.graphics.ISolidPrimitiveFactory.maximum_silhouette_width_supported`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISolidPrimitiveFactory


Property detail
---------------

.. py:property:: minimum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.ISolidPrimitiveFactory.minimum_silhouette_width_supported
    :type: float

    Gets the minimum silhouette width, in pixels, supported by the video card.

.. py:property:: maximum_silhouette_width_supported
    :canonical: ansys.stk.core.graphics.ISolidPrimitiveFactory.maximum_silhouette_width_supported
    :type: float

    Gets the maximum silhouette width, in pixels, supported by the video card.


Method detail
-------------

.. py:method:: initialize(self) -> ISolidPrimitive
    :canonical: ansys.stk.core.graphics.ISolidPrimitiveFactory.initialize

    Initialize a default solid primitive. This is equivalent to constructing a solid primitive with a set hint of Frequent.

    :Returns:

        :obj:`~ISolidPrimitive`

.. py:method:: initialize_with_hint(self, setHint: SET_HINT) -> ISolidPrimitive
    :canonical: ansys.stk.core.graphics.ISolidPrimitiveFactory.initialize_with_hint

    Initialize a solid primitive with the specified setHint.

    :Parameters:

    **setHint** : :obj:`~SET_HINT`

    :Returns:

        :obj:`~ISolidPrimitive`



