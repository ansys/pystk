IFigureOfMerit
==============

.. py:class:: IFigureOfMerit

   object
   
   Figure of Merit properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_definition_type`
              - Set the definition type.
            * - :py:meth:`~is_definition_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:meth:`~set_access_constraint_definition`
              - Set the access constraint definition.
            * - :py:meth:`~set_access_constraint_definition_name`
              - Set the access constraint definition by name.
            * - :py:meth:`~set_scalar_calculation_definition`
              - Set the scalar calculation definition.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~definition_type`
            * - :py:meth:`~definition_supported_types`
            * - :py:meth:`~definition`
            * - :py:meth:`~graphics`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~grid_inspector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMerit


Property detail
---------------

.. py:property:: definition_type
    :canonical: ansys.stk.core.stkobjects.IFigureOfMerit.definition_type
    :type: "FIGURE_OF_MERIT_DEFINITION_TYPE"

    Definition type for the FOM.

.. py:property:: definition_supported_types
    :canonical: ansys.stk.core.stkobjects.IFigureOfMerit.definition_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.IFigureOfMerit.definition
    :type: "IAgFmDefinition"

    Definition properties of the FOM.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IFigureOfMerit.graphics
    :type: "IAgFmGraphics"

    2D graphics properties of the FOM.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IFigureOfMerit.graphics_3d
    :type: "IAgFmVO"

    3D graphics properties of the FOM.

.. py:property:: grid_inspector
    :canonical: ansys.stk.core.stkobjects.IFigureOfMerit.grid_inspector
    :type: "IAgFmGridInspector"

    Get the Grid inspector tool.


Method detail
-------------


.. py:method:: set_definition_type(self, defn:"FIGURE_OF_MERIT_DEFINITION_TYPE") -> None

    Set the definition type.

    :Parameters:

    **defn** : :obj:`~"FIGURE_OF_MERIT_DEFINITION_TYPE"`

    :Returns:

        :obj:`~None`

.. py:method:: is_definition_type_supported(self, defn:"FIGURE_OF_MERIT_DEFINITION_TYPE") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **defn** : :obj:`~"FIGURE_OF_MERIT_DEFINITION_TYPE"`

    :Returns:

        :obj:`~bool`



.. py:method:: set_access_constraint_definition(self, constraintName:"FIGURE_OF_MERIT_CONSTRAINT_NAME") -> "IFigureOfMeritDefinitionAccessConstraint"

    Set the access constraint definition.

    :Parameters:

    **constraintName** : :obj:`~"FIGURE_OF_MERIT_CONSTRAINT_NAME"`

    :Returns:

        :obj:`~"IFigureOfMeritDefinitionAccessConstraint"`




.. py:method:: set_access_constraint_definition_name(self, constraintName:str) -> "IFigureOfMeritDefinitionAccessConstraint"

    Set the access constraint definition by name.

    :Parameters:

    **constraintName** : :obj:`~str`

    :Returns:

        :obj:`~"IFigureOfMeritDefinitionAccessConstraint"`

.. py:method:: set_scalar_calculation_definition(self, calcScalar:str) -> "IFigureOfMeritDefinitionScalarCalculation"

    Set the scalar calculation definition.

    :Parameters:

    **calcScalar** : :obj:`~str`

    :Returns:

        :obj:`~"IFigureOfMeritDefinitionScalarCalculation"`

