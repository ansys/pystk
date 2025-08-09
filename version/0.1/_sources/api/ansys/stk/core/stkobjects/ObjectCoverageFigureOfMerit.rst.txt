ObjectCoverageFigureOfMerit
===========================

.. py:class:: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit

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
              - Return an array of valid choices.
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
    :type: FigureOfMeritDefinitionType

    Definition type for the FOM.

.. py:property:: definition_supported_types
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.definition_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.definition
    :type: IFigureOfMeritDefinition

    Definition properties of the FOM.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.graphics
    :type: FigureOfMeritGraphics

    2D graphics properties of the FOM.


Method detail
-------------


.. py:method:: set_definition_type(self, defn: FigureOfMeritDefinitionType) -> None
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_definition_type

    Set the definition type.

    :Parameters:

        **defn** : :obj:`~FigureOfMeritDefinitionType`


    :Returns:

        :obj:`~None`

.. py:method:: is_definition_type_supported(self, defn: FigureOfMeritDefinitionType) -> bool
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.is_definition_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **defn** : :obj:`~FigureOfMeritDefinitionType`


    :Returns:

        :obj:`~bool`



.. py:method:: set_access_constraint_definition(self, constraint_name: FigureOfMeritConstraintName) -> FigureOfMeritDefinitionAccessConstraint
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_access_constraint_definition

    Set the access constraint definition.

    :Parameters:

        **constraint_name** : :obj:`~FigureOfMeritConstraintName`


    :Returns:

        :obj:`~FigureOfMeritDefinitionAccessConstraint`


.. py:method:: set_access_constraint_definition_name(self, constraint_name: str) -> FigureOfMeritDefinitionAccessConstraint
    :canonical: ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit.set_access_constraint_definition_name

    Set the access constraint definition by name.

    :Parameters:

        **constraint_name** : :obj:`~str`


    :Returns:

        :obj:`~FigureOfMeritDefinitionAccessConstraint`

