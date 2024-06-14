IGraphics3DBorderWall
=====================

.. py:class:: IGraphics3DBorderWall

   object
   
   Border Wall Properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_altitude_reference_type_supported`
              - Provide verification of the availability of borderwall edge altitude reference.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_border_wall`
            * - :py:meth:`~upper_edge_altitude_reference`
            * - :py:meth:`~upper_edge_height`
            * - :py:meth:`~lower_edge_altitude_reference`
            * - :py:meth:`~lower_edge_height`
            * - :py:meth:`~use_wall_translucency`
            * - :py:meth:`~wall_translucency`
            * - :py:meth:`~use_line_translucency`
            * - :py:meth:`~line_translucency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DBorderWall


Property detail
---------------

.. py:property:: use_border_wall
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.use_border_wall
    :type: bool

    Display the border for the area target as a solid or translucent wall that extends from the lower edge altitude to the upper edge altitude.

.. py:property:: upper_edge_altitude_reference
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.upper_edge_altitude_reference
    :type: "BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE"

    Reference used in defining the upper edge of the border wall. A member of the AgEBorderWallUpperLowerEdgeAltRef enumeration.

.. py:property:: upper_edge_height
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.upper_edge_height
    :type: float

    Height of the upper edge of the border wall.

.. py:property:: lower_edge_altitude_reference
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.lower_edge_altitude_reference
    :type: "BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE"

    Reference used in defining the lower edge of the border wall. A member of the AgEBorderWallUpperLowerEdgeAltRef enumeration.

.. py:property:: lower_edge_height
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.lower_edge_height
    :type: float

    Height of the lower edge of the border wall.

.. py:property:: use_wall_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.use_wall_translucency
    :type: bool

    Display the border wall at the specified translucency percentage.

.. py:property:: wall_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.wall_translucency
    :type: float

    Gets or sets the border wall's translucency percentage, where 100% = invisible.

.. py:property:: use_line_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.use_line_translucency
    :type: bool

    Display the lines at the upper and lower edges of the border wall at the specified translucency percentage.

.. py:property:: line_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DBorderWall.line_translucency
    :type: float

    Gets or sets the translucency of the lines at the upper and lower edges of the border wall, where 100% = invisible.


Method detail
-------------



















.. py:method:: is_altitude_reference_type_supported(self, refType:"BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE") -> bool

    Provide verification of the availability of borderwall edge altitude reference.

    :Parameters:

    **refType** : :obj:`~"BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE"`

    :Returns:

        :obj:`~bool`

