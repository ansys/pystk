AreaTargetGraphics3D
====================

.. py:class:: ansys.stk.core.stkobjects.AreaTargetGraphics3D

   Class to define the 3D attributes of an AreaTarget.

.. py:currentmodule:: AreaTargetGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D.enable_label_max_viewing_dist`
              - Use the maximum viewing distance for displaying the area target label.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D.label_maximum_viewing_dist`
              - Specify the maximum distance (distance from the viewer's eye position in 3D to the centroid) at which the area target label is displayed. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D.fill_interior`
              - Display the area target as a filled polygon indicating the portion of the globe that the area target covers.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D.percent_translucency_interior`
              - The translucency percent of the filled area, where 100 percent is invisible.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D.border_wall`
              - Retrieve the border wall properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D.vector`
              - Get Vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D.fill_granularity`
              - Allow the user to control the speed vs. visual quality of a filled area target. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AreaTargetGraphics3D


Property detail
---------------

.. py:property:: enable_label_max_viewing_dist
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics3D.enable_label_max_viewing_dist
    :type: bool

    Use the maximum viewing distance for displaying the area target label.

.. py:property:: label_maximum_viewing_dist
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics3D.label_maximum_viewing_dist
    :type: float

    Specify the maximum distance (distance from the viewer's eye position in 3D to the centroid) at which the area target label is displayed. Uses Distance Dimension.

.. py:property:: fill_interior
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics3D.fill_interior
    :type: bool

    Display the area target as a filled polygon indicating the portion of the globe that the area target covers.

.. py:property:: percent_translucency_interior
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics3D.percent_translucency_interior
    :type: float

    The translucency percent of the filled area, where 100 percent is invisible.

.. py:property:: border_wall
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics3D.border_wall
    :type: Graphics3DBorderWall

    Retrieve the border wall properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics3D.vector
    :type: Graphics3DVector

    Get Vector.

.. py:property:: fill_granularity
    :canonical: ansys.stk.core.stkobjects.AreaTargetGraphics3D.fill_granularity
    :type: float

    Allow the user to control the speed vs. visual quality of a filled area target. Uses Angle Dimension.


