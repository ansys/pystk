IObjectCoverageFigureOfMerit
============================

.. py:class:: IObjectCoverageFigureOfMerit

   object
   
   Provide access to the Figure of Merit on the Object Coverage tool.

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

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~definition_type`
            * - :py:meth:`~definition_supported_types`
            * - :py:meth:`~definition`
            * - :py:meth:`~graphics`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IObjectCoverageFigureOfMerit


Property detail
---------------

.. py:property:: definition_type
    :canonical: ansys.stk.core.stkobjects.IObjectCoverageFigureOfMerit.definition_type
    :type: FIGURE_OF_MERIT_DEFINITION_TYPE

    Definition type for the FOM.

.. py:property:: definition_supported_types
    :canonical: ansys.stk.core.stkobjects.IObjectCoverageFigureOfMerit.definition_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: definition
    :canonical: ansys.stk.core.stkobjects.IObjectCoverageFigureOfMerit.definition
    :type: IAgFmDefinition

    Definition properties of the FOM.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IObjectCoverageFigureOfMerit.graphics
    :type: IAgFmGraphics

    2D graphics properties of the FOM.


Method detail
-------------


.. py:method:: set_definition_type(self, defn: FIGURE_OF_MERIT_DEFINITION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IObjectCoverageFigureOfMerit.set_definition_type

    Set the definition type.

    :Parameters:

    **defn** : :obj:`~FIGURE_OF_MERIT_DEFINITION_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_definition_type_supported(self, defn: FIGURE_OF_MERIT_DEFINITION_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.IObjectCoverageFigureOfMerit.is_definition_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **defn** : :obj:`~FIGURE_OF_MERIT_DEFINITION_TYPE`

    :Returns:

        :obj:`~bool`



.. py:method:: set_access_constraint_definition(self, constraintName: FIGURE_OF_MERIT_CONSTRAINT_NAME) -> IFigureOfMeritDefinitionAccessConstraint
    :canonical: ansys.stk.core.stkobjects.IObjectCoverageFigureOfMerit.set_access_constraint_definition

    Set the access constraint definition.

    :Parameters:

    **constraintName** : :obj:`~FIGURE_OF_MERIT_CONSTRAINT_NAME`

    :Returns:

        :obj:`~IFigureOfMeritDefinitionAccessConstraint`


.. py:method:: set_access_constraint_definition_name(self, constraintName: str) -> IFigureOfMeritDefinitionAccessConstraint
    :canonical: ansys.stk.core.stkobjects.IObjectCoverageFigureOfMerit.set_access_constraint_definition_name

    Set the access constraint definition by name.

    :Parameters:

    **constraintName** : :obj:`~str`

    :Returns:

        :obj:`~IFigureOfMeritDefinitionAccessConstraint`

