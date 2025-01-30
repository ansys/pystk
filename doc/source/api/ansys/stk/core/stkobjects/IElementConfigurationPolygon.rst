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
              - Gets or sets the lattice type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_sides`
              - Gets or sets the number of polygon sides.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.equilateral`
              - Gets or sets the option for evenly spacing adjacent elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_x_elements`
              - Gets or sets the number of elements in the x direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_y_elements`
              - Gets or sets the number of elements in the y direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_x`
              - Gets or sets the spacing of the elements in the x direction, in wavelengths.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_y`
              - Gets or sets the spacing of the elements in the y direction, in wavelengths.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.maximum_look_angle_elevation`
              - Gets the maximum look angle in the x direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.maximum_look_angle_azimuth`
              - Gets the maximum look angle in the y direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_unit`
              - Gets or sets the spacing unit.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IElementConfigurationPolygon


Property detail
---------------

.. py:property:: lattice_type
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.lattice_type
    :type: LatticeType

    Gets or sets the lattice type.

.. py:property:: number_of_sides
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_sides
    :type: int

    Gets or sets the number of polygon sides.

.. py:property:: equilateral
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.equilateral
    :type: bool

    Gets or sets the option for evenly spacing adjacent elements.

.. py:property:: number_of_x_elements
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_x_elements
    :type: int

    Gets or sets the number of elements in the x direction.

.. py:property:: number_of_y_elements
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.number_of_y_elements
    :type: int

    Gets or sets the number of elements in the y direction.

.. py:property:: spacing_x
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_x
    :type: float

    Gets or sets the spacing of the elements in the x direction, in wavelengths.

.. py:property:: spacing_y
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_y
    :type: float

    Gets or sets the spacing of the elements in the y direction, in wavelengths.

.. py:property:: maximum_look_angle_elevation
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.maximum_look_angle_elevation
    :type: typing.Any

    Gets the maximum look angle in the x direction.

.. py:property:: maximum_look_angle_azimuth
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.maximum_look_angle_azimuth
    :type: typing.Any

    Gets the maximum look angle in the y direction.

.. py:property:: spacing_unit
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_unit
    :type: SpacingUnit

    Gets or sets the spacing unit.


