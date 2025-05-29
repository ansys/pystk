FigureOfMerit
=============

.. py:class:: ansys.stk.core.stkobjects.FigureOfMerit

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Figure of Merit properties.

.. py:currentmodule:: FigureOfMerit

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.set_definition_type`
              - Set the definition type.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.is_definition_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.set_access_constraint_definition`
              - Set the access constraint definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.set_access_constraint_definition_name`
              - Set the access constraint definition by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.set_scalar_calculation_definition`
              - Set the scalar calculation definition.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.definition_type`
              - Definition type for the FOM.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.definition_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.definition`
              - Definition properties of the FOM.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.graphics`
              - 2D graphics properties of the FOM.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.graphics_3d`
              - 3D graphics properties of the FOM.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMerit.grid_inspector`
              - Get the Grid inspector tool.



Examples
--------

Configure the Contours of the figure of merit (FOM) and define a color ramp

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    # FigureOfMerit fom: Figure Of Merit object
    satisfaction = coverage.graphics.static
    satisfaction.show_region = False
    Animation = fom.graphics_3d.animation_graphics_3d_settings
    Animation.show_graphics = False
    VOcontours = fom.graphics_3d.static
    VOcontours.show_graphics = True
    contours = fom.graphics.static.contours
    contours.show_graphics = True
    contours.contour_type = FigureOfMeritGraphics2DContourType.SMOOTH_FILL
    contours.color_method = FigureOfMeritGraphics2DColorMethod.COLOR_RAMP
    contours.level_attributes.remove_all()

    contours.level_attributes.add_level_range(590, 660, 10)  # Start, Start, Step
    contours.ramp_color.start_color = Colors.Red
    contours.ramp_color.end_color = Colors.Blue


Create a new Figure of Merit of type Access Duration

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    fom = coverage.children.new(STKObjectType.FIGURE_OF_MERIT, "AccessDuration")
    fom.set_definition_type(FigureOfMeritDefinitionType.ACCESS_DURATION)
    fom.definition.set_compute_type(FigureOfMeritCompute.MAXIMUM)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMerit


Property detail
---------------

.. py:property:: definition_type
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.definition_type
    :type: FigureOfMeritDefinitionType

    Definition type for the FOM.

.. py:property:: definition_supported_types
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.definition_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.definition
    :type: IFigureOfMeritDefinition

    Definition properties of the FOM.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.graphics
    :type: FigureOfMeritGraphics

    2D graphics properties of the FOM.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.graphics_3d
    :type: FigureOfMeritGraphics3D

    3D graphics properties of the FOM.

.. py:property:: grid_inspector
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.grid_inspector
    :type: FigureOfMeritGridInspector

    Get the Grid inspector tool.


Method detail
-------------


.. py:method:: set_definition_type(self, defn: FigureOfMeritDefinitionType) -> None
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.set_definition_type

    Set the definition type.

    :Parameters:

        **defn** : :obj:`~FigureOfMeritDefinitionType`


    :Returns:

        :obj:`~None`

.. py:method:: is_definition_type_supported(self, defn: FigureOfMeritDefinitionType) -> bool
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.is_definition_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **defn** : :obj:`~FigureOfMeritDefinitionType`


    :Returns:

        :obj:`~bool`



.. py:method:: set_access_constraint_definition(self, constraint_name: FigureOfMeritConstraintName) -> FigureOfMeritDefinitionAccessConstraint
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.set_access_constraint_definition

    Set the access constraint definition.

    :Parameters:

        **constraint_name** : :obj:`~FigureOfMeritConstraintName`


    :Returns:

        :obj:`~FigureOfMeritDefinitionAccessConstraint`




.. py:method:: set_access_constraint_definition_name(self, constraint_name: str) -> FigureOfMeritDefinitionAccessConstraint
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.set_access_constraint_definition_name

    Set the access constraint definition by name.

    :Parameters:

        **constraint_name** : :obj:`~str`


    :Returns:

        :obj:`~FigureOfMeritDefinitionAccessConstraint`

.. py:method:: set_scalar_calculation_definition(self, calc_scalar: str) -> FigureOfMeritDefinitionScalarCalculation
    :canonical: ansys.stk.core.stkobjects.FigureOfMerit.set_scalar_calculation_definition

    Set the scalar calculation definition.

    :Parameters:

        **calc_scalar** : :obj:`~str`


    :Returns:

        :obj:`~FigureOfMeritDefinitionScalarCalculation`

