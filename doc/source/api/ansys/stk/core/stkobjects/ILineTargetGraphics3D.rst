ILineTargetGraphics3D
=====================

.. py:class:: ansys.stk.core.stkobjects.ILineTargetGraphics3D

   object
   
   Line Target 3D Graphics properties.

.. py:currentmodule:: ILineTargetGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics3D.enable_label_max_viewing_dist`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics3D.label_max_viewing_dist`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics3D.border_wall`
            * - :py:attr:`~ansys.stk.core.stkobjects.ILineTargetGraphics3D.vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILineTargetGraphics3D


Property detail
---------------

.. py:property:: enable_label_max_viewing_dist
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics3D.enable_label_max_viewing_dist
    :type: bool

    Use the maximum viewing distance for displaying the line target label.

.. py:property:: label_max_viewing_dist
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics3D.label_max_viewing_dist
    :type: float

    Specify the maximum distance at which the line target label is displayed. Uses Distance Dimension.

.. py:property:: border_wall
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics3D.border_wall
    :type: IGraphics3DBorderWall

    Retrieve the border wall properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.ILineTargetGraphics3D.vector
    :type: IGraphics3DVector

    Get the vector.


