Graphics3DBorderWall
====================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DBorderWall

   Bases: 

   Class defining 3D Graphics border wall properties.

.. py:currentmodule:: Graphics3DBorderWall

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.is_altitude_reference_type_supported`
              - Provide verification of the availability of borderwall edge altitude reference.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.use_border_wall`
              - Display the border for the area target as a solid or translucent wall that extends from the lower edge altitude to the upper edge altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.upper_edge_altitude_reference`
              - Reference used in defining the upper edge of the border wall. A member of the AgEBorderWallUpperLowerEdgeAltRef enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.upper_edge_height`
              - Height of the upper edge of the border wall.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.lower_edge_altitude_reference`
              - Reference used in defining the lower edge of the border wall. A member of the AgEBorderWallUpperLowerEdgeAltRef enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.lower_edge_height`
              - Height of the lower edge of the border wall.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.use_wall_translucency`
              - Display the border wall at the specified translucency percentage.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.wall_translucency`
              - Gets or sets the border wall's translucency percentage, where 100% = invisible.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.use_line_translucency`
              - Display the lines at the upper and lower edges of the border wall at the specified translucency percentage.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DBorderWall.line_translucency`
              - Gets or sets the translucency of the lines at the upper and lower edges of the border wall, where 100% = invisible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DBorderWall


Property detail
---------------

.. py:property:: use_border_wall
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.use_border_wall
    :type: bool

    Display the border for the area target as a solid or translucent wall that extends from the lower edge altitude to the upper edge altitude.

.. py:property:: upper_edge_altitude_reference
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.upper_edge_altitude_reference
    :type: BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE

    Reference used in defining the upper edge of the border wall. A member of the AgEBorderWallUpperLowerEdgeAltRef enumeration.

.. py:property:: upper_edge_height
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.upper_edge_height
    :type: float

    Height of the upper edge of the border wall.

.. py:property:: lower_edge_altitude_reference
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.lower_edge_altitude_reference
    :type: BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE

    Reference used in defining the lower edge of the border wall. A member of the AgEBorderWallUpperLowerEdgeAltRef enumeration.

.. py:property:: lower_edge_height
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.lower_edge_height
    :type: float

    Height of the lower edge of the border wall.

.. py:property:: use_wall_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.use_wall_translucency
    :type: bool

    Display the border wall at the specified translucency percentage.

.. py:property:: wall_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.wall_translucency
    :type: float

    Gets or sets the border wall's translucency percentage, where 100% = invisible.

.. py:property:: use_line_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.use_line_translucency
    :type: bool

    Display the lines at the upper and lower edges of the border wall at the specified translucency percentage.

.. py:property:: line_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.line_translucency
    :type: float

    Gets or sets the translucency of the lines at the upper and lower edges of the border wall, where 100% = invisible.


Method detail
-------------



















.. py:method:: is_altitude_reference_type_supported(self, refType: BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE) -> bool
    :canonical: ansys.stk.core.stkobjects.Graphics3DBorderWall.is_altitude_reference_type_supported

    Provide verification of the availability of borderwall edge altitude reference.

    :Parameters:

    **refType** : :obj:`~BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE`

    :Returns:

        :obj:`~bool`

