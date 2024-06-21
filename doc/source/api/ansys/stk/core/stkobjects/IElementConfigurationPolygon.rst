IElementConfigurationPolygon
============================

.. py:class:: ansys.stk.core.stkobjects.IElementConfigurationPolygon

   object
   
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
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.num_sides`
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.equilateral`
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.num_elements_x`
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.num_elements_y`
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_x`
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_y`
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.max_look_angle_el`
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.max_look_angle_az`
            * - :py:attr:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_unit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IElementConfigurationPolygon


Property detail
---------------

.. py:property:: lattice_type
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.lattice_type
    :type: LATTICE_TYPE

    Gets or sets the lattice type.

.. py:property:: num_sides
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.num_sides
    :type: int

    Gets or sets the number of polygon sides.

.. py:property:: equilateral
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.equilateral
    :type: bool

    Gets or sets the option for evenly spacing adjacent elements.

.. py:property:: num_elements_x
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.num_elements_x
    :type: int

    Gets or sets the number of elements in the x direction.

.. py:property:: num_elements_y
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.num_elements_y
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

.. py:property:: max_look_angle_el
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.max_look_angle_el
    :type: typing.Any

    Gets the maximum look angle in the x direction.

.. py:property:: max_look_angle_az
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.max_look_angle_az
    :type: typing.Any

    Gets the maximum look angle in the y direction.

.. py:property:: spacing_unit
    :canonical: ansys.stk.core.stkobjects.IElementConfigurationPolygon.spacing_unit
    :type: SPACING_UNIT

    Gets or sets the spacing unit.


