IAreaTargetGraphics3D
=====================

.. py:class:: IAreaTargetGraphics3D

   object
   
   AgATVO used to access the 3D attributes of an AreaTarget interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_label_max_viewing_dist`
            * - :py:meth:`~label_max_viewing_dist`
            * - :py:meth:`~fill_interior`
            * - :py:meth:`~percent_translucency_interior`
            * - :py:meth:`~border_wall`
            * - :py:meth:`~vector`
            * - :py:meth:`~fill_granularity`


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
    :type: IAgVOBorderWall

    Retrieve the border wall properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.vector
    :type: IAgVOVector

    Gets Vector.

.. py:property:: fill_granularity
    :canonical: ansys.stk.core.stkobjects.IAreaTargetGraphics3D.fill_granularity
    :type: float

    Allows the user to control the speed vs. visual quality of a filled area target. Uses Angle Dimension.


