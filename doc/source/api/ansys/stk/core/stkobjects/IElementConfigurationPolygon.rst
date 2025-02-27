IElementConfigurationPolygon
============================

.. py:class:: ansys.stk.core.stkobjects.IElementConfigurationPolygon

   Provide access to the properties and methods defining a polygon element configuration.

.. py:currentmodule:: IElementConfigurationPolygon

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.lattice_type`
              - Get or set the lattice type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_sides`
              - Get or set the number of polygon sides.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.equilateral`
              - Get or set the option for evenly spacing adjacent elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_x_elements`
              - Get or set the number of elements in the x direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_y_elements`
              - Get or set the number of elements in the y direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_x`
              - Get or set the spacing of the elements in the x direction, in wavelengths.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_y`
              - Get or set the spacing of the elements in the y direction, in wavelengths.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.maximum_look_angle_elevation`
              - Get the maximum look angle in the x direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.maximum_look_angle_azimuth`
              - Get the maximum look angle in the y direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_unit`
              - Get or set the spacing unit.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IElementConfigurationPolygon


Property detail
---------------

.. py:property:: lattice_type
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.lattice_type
    :type: LatticeType

    Get or set the lattice type.

.. py:property:: number_of_sides
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_sides
    :type: int

    Get or set the number of polygon sides.

.. py:property:: equilateral
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.equilateral
    :type: bool

    Get or set the option for evenly spacing adjacent elements.

.. py:property:: number_of_x_elements
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_x_elements
    :type: int

    Get or set the number of elements in the x direction.

.. py:property:: number_of_y_elements
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_y_elements
    :type: int

    Get or set the number of elements in the y direction.

.. py:property:: spacing_x
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_x
    :type: float

    Get or set the spacing of the elements in the x direction, in wavelengths.

.. py:property:: spacing_y
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_y
    :type: float

    Get or set the spacing of the elements in the y direction, in wavelengths.

.. py:property:: maximum_look_angle_elevation
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.maximum_look_angle_elevation
    :type: typing.Any

    Get the maximum look angle in the x direction.

.. py:property:: maximum_look_angle_azimuth
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.maximum_look_angle_azimuth
    :type: typing.Any

    Get the maximum look angle in the y direction.

.. py:property:: spacing_unit
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_unit
    :type: SpacingUnit

    Get or set the spacing unit.


