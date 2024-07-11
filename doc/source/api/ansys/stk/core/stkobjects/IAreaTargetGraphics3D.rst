IAreaTargetGraphics3D
=====================

.. py:class:: ansys.stk.core.stkobjects.IAreaTargetGraphics3D

   object
   
   AgATVO used to access the 3D attributes of an AreaTarget interface.

.. py:currentmodule:: IAreaTargetGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTargetGraphics3D.enable_label_max_viewing_dist`
              - Use the maximum viewing distance for displaying the area target label.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTargetGraphics3D.label_max_viewing_dist`
              - Specify the maximum distance (distance from the viewer's eye position in 3D to the centroid) at which the area target label is displayed. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTargetGraphics3D.fill_interior`
              - Display the area target as a filled polygon indicating the portion of the globe that the area target covers.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTargetGraphics3D.percent_translucency_interior`
              - The translucency percent of the filled area, where 100 percent is invisible.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTargetGraphics3D.border_wall`
              - Retrieve the border wall properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTargetGraphics3D.vector`
              - Gets Vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAreaTargetGraphics3D.fill_granularity`
              - Allows the user to control the speed vs. visual quality of a filled area target. Uses Angle Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAreaTargetGraphics3D


Property detail
---------------

.. py:property:: enable_label_max_viewing_dist
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.enable_label_max_viewing_dist
    :type: bool

    Use the maximum viewing distance for displaying the area target label.

.. py:property:: label_max_viewing_dist
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.label_max_viewing_dist
    :type: float

    Specify the maximum distance (distance from the viewer's eye position in 3D to the centroid) at which the area target label is displayed. Uses Distance Dimension.

.. py:property:: fill_interior
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.fill_interior
    :type: bool

    Display the area target as a filled polygon indicating the portion of the globe that the area target covers.

.. py:property:: percent_translucency_interior
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.percent_translucency_interior
    :type: float

    The translucency percent of the filled area, where 100 percent is invisible.

.. py:property:: border_wall
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.border_wall
    :type: IGraphics3DBorderWall

    Retrieve the border wall properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.vector
    :type: IGraphics3DVector

    Gets Vector.

.. py:property:: fill_granularity
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.fill_granularity
    :type: float

    Allows the user to control the speed vs. visual quality of a filled area target. Uses Angle Dimension.


