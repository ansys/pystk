ObjectCoverageFigureOfMerit
===========================

.. py:class:: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit

   Bases: 

   Class defining the fom on the coverage object tool.

.. py:currentmodule:: ObjectCoverageFigureOfMerit

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_definition_type`
              - Set the definition type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.is_definition_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_access_constraint_definition`
              - Set the access constraint definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_access_constraint_definition_name`
              - Set the access constraint definition by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.definition_type`
              - Definition type for the FOM.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.definition_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.definition`
              - Definition properties of the FOM.
            * - :py:attr:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.graphics`
              - 2D graphics properties of the FOM.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ObjectCoverageFigureOfMerit


Property detail
---------------

.. py:property:: definition_type
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.definition_type
    :type: FIGURE_OF_MERIT_DEFINITION_TYPE

    Definition type for the FOM.

.. py:property:: definition_supported_types
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.definition_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.definition
    :type: IFigureOfMeritDefinition

    Definition properties of the FOM.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.graphics
    :type: IFigureOfMeritGraphics

    2D graphics properties of the FOM.


Method detail
-------------


.. py:method:: set_definition_type(self, defn: FIGURE_OF_MERIT_DEFINITION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_definition_type

    Set the definition type.

    :Parameters:

    **defn** : :obj:`~FIGURE_OF_MERIT_DEFINITION_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_definition_type_supported(self, defn: FIGURE_OF_MERIT_DEFINITION_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.is_definition_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **defn** : :obj:`~FIGURE_OF_MERIT_DEFINITION_TYPE`

    :Returns:

        :obj:`~bool`



.. py:method:: set_access_constraint_definition(self, constraintName: FIGURE_OF_MERIT_CONSTRAINT_NAME) -> FigureOfMeritDefinitionAccessConstraint
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_access_constraint_definition

    Set the access constraint definition.

    :Parameters:

    **constraintName** : :obj:`~FIGURE_OF_MERIT_CONSTRAINT_NAME`

    :Returns:

        :obj:`~FigureOfMeritDefinitionAccessConstraint`


.. py:method:: set_access_constraint_definition_name(self, constraintName: str) -> FigureOfMeritDefinitionAccessConstraint
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_access_constraint_definition_name

    Set the access constraint definition by name.

    :Parameters:

    **constraintName** : :obj:`~str`

    :Returns:

        :obj:`~FigureOfMeritDefinitionAccessConstraint`

