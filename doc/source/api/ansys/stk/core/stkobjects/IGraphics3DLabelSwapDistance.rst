IGraphics3DLabelSwapDistance
============================

.. py:class:: IGraphics3DLabelSwapDistance

   object
   
   Interface to control the level of detail in labels and other screen objects at specified distances.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_distance_level`
              - Select the screen object(s) for which swapping occurs at the specified distance.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~distance_value`
            * - :py:meth:`~distance_level`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DLabelSwapDistance


Property detail
---------------

.. py:property:: distance_value
    :canonical: ansys.stk.core.stkobjects.IGraphics3DLabelSwapDistance.distance_value
    :type: float

    Distance at which one level of detail is swapped for another. Uses Distance Dimension.

.. py:property:: distance_level
    :canonical: ansys.stk.core.stkobjects.IGraphics3DLabelSwapDistance.distance_level
    :type: "GRAPHICS_3D_LABEL_SWAP_DISTANCE"

    Gets Distance Level.


Method detail
-------------



.. py:method:: set_distance_level(self, val:"GRAPHICS_3D_LABEL_SWAP_DISTANCE") -> None

    Select the screen object(s) for which swapping occurs at the specified distance.

    :Parameters:

    **val** : :obj:`~"GRAPHICS_3D_LABEL_SWAP_DISTANCE"`

    :Returns:

        :obj:`~None`


