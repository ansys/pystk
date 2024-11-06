Graphics3DLabelSwapDistance
===========================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance

   Control the level of detail in labels and other screen objects at specified distances.

.. py:currentmodule:: Graphics3DLabelSwapDistance

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance.set_distance_level`
              - Select the screen object(s) for which swapping occurs at the specified distance.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance.distance_value`
              - Distance at which one level of detail is swapped for another. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance.distance_level`
              - Gets Distance Level.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DLabelSwapDistance


Property detail
---------------

.. py:property:: distance_value
    :canonical: ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance.distance_value
    :type: float

    Distance at which one level of detail is swapped for another. Uses Distance Dimension.

.. py:property:: distance_level
    :canonical: ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance.distance_level
    :type: GRAPHICS_3D_LABEL_SWAP_DISTANCE

    Gets Distance Level.


Method detail
-------------



.. py:method:: set_distance_level(self, value: GRAPHICS_3D_LABEL_SWAP_DISTANCE) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance.set_distance_level

    Select the screen object(s) for which swapping occurs at the specified distance.

    :Parameters:

    **value** : :obj:`~GRAPHICS_3D_LABEL_SWAP_DISTANCE`

    :Returns:

        :obj:`~None`


