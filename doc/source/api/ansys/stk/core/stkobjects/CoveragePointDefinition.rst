CoveragePointDefinition
=======================

.. py:class:: ansys.stk.core.stkobjects.CoveragePointDefinition

   Point Definition: methods and parameters for specifying the location of points on the coverage grid.

.. py:currentmodule:: CoveragePointDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.set_points_detic`
              - Use an array of latitude/longitude/altitude values to define a coverage grid point.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.altitude`
              - Height of the grid point. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.altitude_method`
              - Specify the height of a grid point.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.available_seeds`
              - Available object instances to use as a grid seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.grid_class`
              - Class of object used to define grid points.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.ground_altitude`
              - Height of the grid point. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.ground_altitude_method`
              - Specify the height of a grid point.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.point_altitude_method`
              - Custom point altitude method specifies whether to use the altitude values in the point file (.*pt) or override them using the altitude at a point on terrain.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.point_file_list`
              - List of point file locations.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.point_location_method`
              - Specify the location of points on the coverage grid.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.seed_instance`
              - Specify the object instance to use as a grid seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.use_grid_seed`
              - Select an object instance for the grid seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoveragePointDefinition.use_object_as_seed`
              - Use the selected object as the grid seed.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoveragePointDefinition


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.altitude
    :type: float

    Height of the grid point. Uses Distance Dimension.

.. py:property:: altitude_method
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.altitude_method
    :type: CoverageAltitudeMethod

    Specify the height of a grid point.

.. py:property:: available_seeds
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.available_seeds
    :type: list

    Available object instances to use as a grid seed.

.. py:property:: grid_class
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.grid_class
    :type: CoverageGridClass

    Class of object used to define grid points.

.. py:property:: ground_altitude
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.ground_altitude
    :type: float

    Height of the grid point. Uses Distance Dimension.

.. py:property:: ground_altitude_method
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.ground_altitude_method
    :type: CoverageGroundAltitudeMethod

    Specify the height of a grid point.

.. py:property:: point_altitude_method
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.point_altitude_method
    :type: CoveragePointAltitudeMethod

    Custom point altitude method specifies whether to use the altitude values in the point file (.*pt) or override them using the altitude at a point on terrain.

.. py:property:: point_file_list
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.point_file_list
    :type: CoveragePointFileListCollection

    List of point file locations.

.. py:property:: point_location_method
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.point_location_method
    :type: CoveragePointLocationMethod

    Specify the location of points on the coverage grid.

.. py:property:: seed_instance
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.seed_instance
    :type: str

    Specify the object instance to use as a grid seed.

.. py:property:: use_grid_seed
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.use_grid_seed
    :type: bool

    Select an object instance for the grid seed.

.. py:property:: use_object_as_seed
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.use_object_as_seed
    :type: bool

    Use the selected object as the grid seed.


Method detail
-------------



















.. py:method:: set_points_detic(self, lla_points: list) -> None
    :canonical: ansys.stk.core.stkobjects.CoveragePointDefinition.set_points_detic

    Use an array of latitude/longitude/altitude values to define a coverage grid point.

    :Parameters:

        **lla_points** : :obj:`~list`


    :Returns:

        :obj:`~None`





